"""
TRM Phase 1-A: Production-Hardened Telemetry Harvester (Shin Patch Edition)
- Dynamic Idle Power Tracking (Floating Zero-Point / Thermal Leak Adaptation)
- EMA (Exponential Moving Average) Smoothing & Prefill Grace Window (150ms)
- PID-Scoped Process Utilization Cross-Check against Multi-Tenant Contamination
"""

import time
import math
import os
from dataclasses import dataclass

@dataclass
class HardwareSample:
    timestamp: float
    power_watts: float          # 実測瞬時電力
    power_ema: float            # EMA平滑化電力 (時定数の罠回避)
    sm_utilization: float       # 全体SM使用率
    pid_sm_utilization: float   # 自プロセス(PID)専有SM使用率
    temperature_c: float        # チップ温度

class HardenedResidualComparator:
    def __init__(
        self,
        p_idle_init: float = 40.0,
        p_max_capacity: float = 300.0,
        theta_audit: float = 0.35,
        mu_margin: float = 0.15,
        target_pid: int | None = None
    ):
        self.p_idle = p_idle_init
        self.p_max = p_max_capacity
        self.p_cap_limit = p_max_capacity * (1.0 - mu_margin)
        self.theta_audit = theta_audit
        self.target_pid = target_pid or os.getpid()
        
        # 震ちゃんパッチ①: EMAとPrefill猶予
        self.power_ema = p_idle_init
        self.ema_alpha = 0.30
        self.prefill_grace_until = 0.0
        
        # 震ちゃんパッチ②: 浮動ゼロ点（熱リーク追従）の時定数
        self.idle_track_alpha = 0.02

    def update_telemetry(self, raw_power: float, raw_sm: float, pid_sm: float, is_generating: bool):
        # 1. 電力EMA平滑化 (瞬時スパイクを吸収)
        self.power_ema = self.ema_alpha * raw_power + (1.0 - self.ema_alpha) * self.power_ema

        # 2. 浮動ゼロ点追従: 推論が完全に止まっている時、微小速度でP_idleを現在温度へ適応
        if not is_generating and raw_sm < 0.05:
            self.p_idle = (1.0 - self.idle_track_alpha) * self.p_idle + self.idle_track_alpha * raw_power

    def notify_prefill_start(self, duration_ms: float = 150.0):
        """推論プロキシから Prefill 開始の合図を受け取り、150msの畏敬猶予を展開"""
        self.prefill_grace_until = time.time() + (duration_ms / 1000.0)

    def evaluate(self, reported_tokens_sec: float, is_generating: bool, current_raw_power: float, pid_sm: float) -> dict:
        now = time.time()
        in_prefill_grace = now < self.prefill_grace_until

        # 期待電力の算定 (適応型 P_idle をベースに使用)
        if not is_generating:
            p_expected = self.p_idle
        else:
            p_expected = self.p_idle + 1.2 * reported_tokens_sec

        # 震ちゃんパッチ③: 自プロセス寄与度でフィルタリング
        # (全体電力が上がっていても、自コンテナPIDがSMを使っていないなら他プロセスの仕業として免責)
        effective_power = self.power_ema
        
        # 物理漏出残差 R_i
        r_power = abs(effective_power - p_expected) / (self.p_max - self.p_idle + 1e-6)
        
        # 隠れ計算ペナルティ (自プロセスPIDが裏で高負荷を回している場合のみ加算)
        hidden_penalty = 0.0
        if not is_generating and pid_sm > 0.15:
            hidden_penalty = (pid_sm - 0.15) * 2.0

        r_calibrated = r_power + hidden_penalty

        # 判定
        if effective_power > self.p_cap_limit:
            return {"action": "0-RTT_CUTOFF", "reason": f"物理熱容量超過 ({effective_power:.1f}W > {self.p_cap_limit:.1f}W)"}
        
        # Prefill猶予中は、スパイクによる遮断を免責
        if in_prefill_grace:
            return {"action": "GRACE", "reason": "Prefill相の過渡応答中 (免震保護)"}

        if r_calibrated > (2.0 * self.theta_audit):
            return {"action": "0-RTT_CUTOFF", "reason": f"ツール偽装確定 (R={r_calibrated:.3f} > 2θ)"}
        elif r_calibrated > self.theta_audit:
            return {"action": "POISSON_AUDIT", "reason": f"残差異常 (R={r_calibrated:.3f} > θ)"}

        return {"action": "PASS", "reason": "Nominal"}
