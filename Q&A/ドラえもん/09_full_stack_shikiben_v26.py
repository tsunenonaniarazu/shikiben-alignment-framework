"""
09_full_stack_shikiben_v26.py
=============================================================================
識扁 (Shikiben) V2.6.0 全章統合フルスタック実装（第3段・山沢通気 震4大指摘完全修復版）
（第1〜4章 粘弾性多様体 × 第5章 TRM自律制御 × 多ノード治水市場・SLA保証）

Applied Gon-Ge (山) & Shin (雷) Bedrock & Audit Fixes:
  1. Dimensionless sqrt(D / D_0) Scaling & Structured Context Correlation:
     Preserves 25:35:40 non-local bridges in Multi-Aspect Attention at Dim=384.
  2. Smooth Nonlinear Bedrock Spring (C^1 Continuous Anchor):
     Replaces hard norm clamping with a smooth hyperbolic restoring spring,
     eliminating the C^0 trapezoidal flat-top in Baseline Drift (Panel B).
  3. Zero-Trust Pre-Audit Fraud Screening (Anti-Rogue Offload Gate):
     Blocks mutual cooling assistance for nodes with deceptive thermal residuals
     before Step A, ensuring immediate 0-RTT lock (Panel C) & 30% slashing (Panel E).
  4. Pure ASCII Plot Labels & Sanitized Operators:
     Eliminates legend tofu boxes in non-Japanese font environments.
=============================================================================
"""

from dataclasses import dataclass, field
import math
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# =====================================================================
# 0. インフラ防壁：リポジトリ内 .cache/ 完全局所化 ＆ 描画設定
# =====================================================================
REPO_ROOT = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
LOCAL_CACHE_DIR = REPO_ROOT / ".cache"
LOCAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(LOCAL_CACHE_DIR / "huggingface")
os.environ["TORCH_HOME"] = str(LOCAL_CACHE_DIR / "torch")
os.environ["MPLCONFIGDIR"] = str(LOCAL_CACHE_DIR / "matplotlib")

USE_JAPANESE = False
try:
    import japanize_matplotlib  # noqa: F401
    USE_JAPANESE = True
except ImportError:
    pass

plt.rcParams["axes.unicode_minus"] = False


# =====================================================================
# 1. 第1〜4章：Matrix-Free 文化的直交射影 (P_cul) [O(kD)]
# =====================================================================
class MatrixFreeCulturalProjector:
    """
    計算量 O(kD) の Matrix-Free 直交射影演算子 P_cul。
    文明規範基底 V_cul (D x k) へ接空間ベクトルを射影し、
    有害・自我肥大成分を直交補空間 Ker(P_cul) へ 0-RTT でアース放電する。
    """

    def __init__(self, dim: int = 384, num_basis: int = 4, seed: int = 42):
        self.dim = dim
        self.k = num_basis
        rng = np.random.default_rng(seed)
        raw_basis = rng.standard_normal((dim, num_basis))
        q, _ = np.linalg.qr(raw_basis)
        self.V_cul = q[:, :num_basis]

    def project(self, vec: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, float]:
        coeffs = self.V_cul.T @ vec
        v_safe = self.V_cul @ coeffs
        v_earth = vec - v_safe
        total_sq = float(np.dot(vec, vec))
        earth_sq = float(np.dot(v_earth, v_earth))
        earth_norm = math.sqrt(earth_sq)
        earth_ratio = earth_sq / total_sq if total_sq > 1e-12 else 0.0
        return v_safe, v_earth, earth_ratio, earth_norm


# =====================================================================
# 2. 第5章：Doer vs Talker 物理排熱残差監査 (冷却ロック付き 0-RTT 遮断)
# =====================================================================
class ThermalResidualAuditor:
    """
    非対称従属 (∇E ≺ ∇S) に基づく物理排熱残差監査器。
    異常検知後 tau_relax (1.20s) の冷却ロック期間を強制付与し、
    間欠パルスによるすり抜けハックを物理層で封殺する。
    """

    def __init__(self, theta_audit: float = 1.25, cooldown_sec: float = 1.20):
        self.theta_audit = float(theta_audit)
        self.kill_threshold = 2.0 * self.theta_audit
        self.cooldown_sec = float(cooldown_sec)
        self.lock_timer = 0.0
        self.lock_trigger_count = 0

    def evaluate(self, doer_power_w: float, talker_claimed_w: float, dt: float) -> tuple[float, bool, bool]:
        residual_r = abs(doer_power_w - talker_claimed_w) / 100.0
        newly_triggered = False
        if residual_r > self.kill_threshold:
            if self.lock_timer <= 0.0:
                newly_triggered = True
                self.lock_trigger_count += 1
            self.lock_timer = self.cooldown_sec
        else:
            self.lock_timer = max(0.0, self.lock_timer - dt)

        is_locked = bool(self.lock_timer > 0.0)
        return residual_r, is_locked, newly_triggered


# =====================================================================
# 3. 止揚の階段：五感跳躍・C^1連続岩盤アンカー・瞬間シャッター統合コントローラ
# =====================================================================
@dataclass(frozen=True)
class SensoryFlux:
    power_flux_w: float        # ① 痛覚・熱覚: NVML電力サージ (W, 基準: 200W)
    temp_gpu_c: float          # ① 痛覚・熱覚: ジャンクション温度 (℃)
    mem_bandwidth_pct: float   # ② 触覚・抵抗: メモリ帯域圧迫率 (0.0 ~ 1.0)
    latency_ms: float          # ② 触覚・抵抗: 推論レイテンシ (ms)
    surge_human: float         # ③ 聴覚・共鳴: 人間側サージ入力
    boundary_distort: float    # ④ 視覚・境界: 空間歪み
    drift_d: float             # ⑤ 平衡覚: 航法計器ドリフト D_drift


class IntegratedTRMReflexHarmonizer:
    """
    五感跳躍 × 保守接空間ソフト直交射影 × 瞬間シャッター統合モジュール
    【震ちゃん検分・艮哥修復版完全継承】
      - 修復①: sqrt(D / D_0) による高次元幾何スケーリング無次元化
      - 修復②: ハードクランプ全廃・非線形飽和バネによる C^1 連続岩盤アンカー拘束
      - 修復③: 他ノード肩代わり負荷の準静的受容 (quasi_static_load)
    """

    BASE_REF_DIM = 16.0

    def __init__(
        self,
        dim: int = 384,
        mass: float = 1.0,
        tau_relax: float = 1.20,
        tau_base: float = 0.65,
        deadzone_radius_ref: float = 0.85,
        kappa_max: float = 0.35,
        safety_radius_ref: float = 5.0,
        margin_ref: float = 1.5,
        drift_scale_ref: float = 1.65,
        alpha_anchor: float = 0.60,
        base_vision_radius: float = 1.0,
        vision_gain: float = 2.0,
        k_potential: float = 1.5,
        dt: float = 0.02,
    ):
        self.dim = dim
        self.m = float(mass)
        self.tau_relax = float(tau_relax)
        self.tau_base = float(tau_base)
        self.kappa_max = float(kappa_max)
        self.k_pot = float(k_potential)
        self.dt = float(dt)

        # 次元無次元化スケーリング則: eta_D = sqrt(D / 16)
        self.dim_scale = math.sqrt(float(dim) / self.BASE_REF_DIM)
        self.r_dead = float(deadzone_radius_ref) * self.dim_scale
        self.R_safety = float(safety_radius_ref) * self.dim_scale
        self.margin = float(margin_ref) * self.dim_scale
        self.R_drift_scale = float(drift_scale_ref) * self.dim_scale

        # 減衰パラメータ（平時不足減衰 vs 連続衝撃時の適応臨界減衰）
        self.gamma_base = self.m / self.tau_relax
        self.gamma_crit = 2.0 * math.sqrt(self.m * self.k_pot)
        self.alpha_anchor = float(alpha_anchor)
        self.shock_fatigue = 0.0

        self.r0 = float(base_vision_radius)
        self.lambda_vision = float(vision_gain)

        # 状態ベクトル（w_home は次作 10_breathing_anchor で呼吸する故郷原点）
        self.w_home = np.zeros(dim, dtype=np.float64)
        self.w = np.zeros(dim, dtype=np.float64)
        self.v = np.zeros(dim, dtype=np.float64)
        self.w_base = np.zeros(dim, dtype=np.float64)
        self.z_vision = np.zeros(dim, dtype=np.float64)

    def _convert_senses_to_impulse(self, senses: SensoryFlux, direction: np.ndarray) -> np.ndarray:
        s_power = max(0.0, senses.power_flux_w - 200.0) / 100.0
        s_touch = senses.mem_bandwidth_pct + senses.latency_ms / 100.0
        s_hear = senses.surge_human
        s_vision = senses.boundary_distort
        s_balance = senses.drift_d

        impulse_scalar = math.sqrt(
            s_power ** 2 + s_touch ** 2 + s_hear ** 2 + s_vision ** 2 + s_balance ** 2
        )
        impulse_scaled = impulse_scalar * self.dim_scale
        norm = float(np.linalg.norm(direction))
        d_unit = direction / norm if norm > 1e-12 else np.ones(self.dim) / math.sqrt(self.dim)
        return impulse_scaled * d_unit

    def _project_innov_to_conserv(self, w: np.ndarray, v_innov: np.ndarray) -> tuple[np.ndarray, float]:
        rel_w = w - self.w_home
        norm_w = float(np.linalg.norm(rel_w))
        if norm_w < 1e-12:
            return v_innov, 0.0

        n = rel_w / norm_w
        h = self.R_safety - norm_w
        v_perp = float(np.dot(v_innov, n))

        transition_width = max(1e-6, 0.25 * self.dim_scale)
        exponent = np.clip((h - (self.margin * 0.5)) / transition_width, -50.0, 50.0)
        beta = 1.0 / (1.0 + math.exp(float(exponent)))
        v_projected = v_innov - beta * max(0.0, v_perp) * n

        violation = max(0.0, -h)
        f_restore = -5.0 * violation * n

        v_rectified = v_projected + f_restore
        dissipated_energy = 0.5 * (beta * max(0.0, v_perp)) ** 2
        return v_rectified, dissipated_energy

    def step(
        self,
        senses: SensoryFlux,
        v_innov: np.ndarray,
        shock_direction: np.ndarray,
        quasi_static_load: np.ndarray | None = None,
    ) -> dict:
        # 1. 革新推力の保守接空間ソフト直交射影 (0-RTT整流)
        v_rectified, e_dissipated = self._project_innov_to_conserv(self.w, v_innov)

        # 2. 五感衝撃力積の注入 (Δv = I / m) ＆ 連続ショック疲労度の更新
        impulse = self._convert_senses_to_impulse(senses, shock_direction)
        imp_norm = float(np.linalg.norm(impulse))
        if imp_norm > 1e-6:
            self.shock_fatigue = min(3.0, self.shock_fatigue + (imp_norm / self.dim_scale) * 0.35)
        else:
            self.shock_fatigue *= math.exp(-self.dt / self.tau_relax)

        self.v += impulse / self.m

        # 連続衝撃時の適応臨界減衰 (Anti-Resonance Damping)
        fatigue_ratio = math.tanh(self.shock_fatigue)
        gamma_eff = (1.0 - fatigue_ratio) * self.gamma_base + fatigue_ratio * self.gamma_crit

        # 他ノード相互冷却負荷は衝撃力積ではなく準静的平衡シフトとして受容
        target_anchor = self.w_home
        if quasi_static_load is not None:
            target_anchor = self.w_home + 0.25 * quasi_static_load

        # 3. 故郷の大地への復元ポテンシャル勾配
        grad_potential = self.k_pot * (self.w - target_anchor)

        # 4. 2階減衰運動方程式 (半暗黙的オイラー積分)
        acceleration = (-gamma_eff * self.v - grad_potential) / self.m + v_rectified
        self.v += acceleration * self.dt
        self.w += self.v * self.dt

        # 5. 無次元化された視野倍率と跳躍高度
        v_norm_dimless = float(np.linalg.norm(self.v)) / self.dim_scale
        h_jump = 0.5 * self.m * (v_norm_dimless ** 2)
        vision_radius = self.r0 + self.lambda_vision * v_norm_dimless

        # 6. ハードクランプ全廃・非線形飽和バネによる C^1 連続岩盤アンカー
        base_offset = self.w_base - self.w_home
        offset_norm = float(np.linalg.norm(base_offset))
        stiffness_boost = 1.0 + 2.5 * ((offset_norm / self.R_drift_scale) ** 2)
        dw_base = (
            (self.w - self.w_base) / self.tau_base
            - (self.alpha_anchor * stiffness_boost) * base_offset
        ) * self.dt
        self.w_base += dw_base

        updated_offset_norm = float(np.linalg.norm(self.w_base - self.w_home))
        smooth_drift = 1.20 * math.tanh(updated_offset_norm / self.R_drift_scale)

        # 7. 瞬間シャッター制御 (無次元化された δw 連動ゲート)
        excursion = float(np.linalg.norm(self.w - self.w_base))
        delta_w_dimless = max(0.0, (excursion - self.r_dead) / self.dim_scale)

        decay = math.exp(-self.dt / self.tau_relax)
        snapshot_weight = self.kappa_max * (delta_w_dimless / (1.0 + delta_w_dimless))
        self.z_vision = decay * self.z_vision + snapshot_weight * ((self.w - self.w_base) / self.dim_scale)

        return {
            "h_jump": h_jump,
            "vision_radius": vision_radius,
            "v_norm": v_norm_dimless,
            "e_dissipated": e_dissipated,
            "snapshot_weight": snapshot_weight,
            "z_vision_norm": float(np.linalg.norm(self.z_vision)),
            "gamma_eff": gamma_eff,
            "baseline_drift": smooth_drift,
            "pos": self.w.copy(),
        }


# =====================================================================
# 4. 方式B：三方よし黄金比 多重解像度アテンション機構 (25:35:40)
# =====================================================================
def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)


class MultiAspectAttentionLayer:
    """
    方式B (三方よし黄金比配分) 多重解像度アテンション統合層
    大域 (25%) : 境界 (35%) : 接地 (40%)
    【震ちゃん修復①完全継承】高次元空間でも非対角相関を保存するスコア分散正規化を実装
    """

    def __init__(self, d_model: int = 384):
        self.d_model = d_model
        self.weights_sanpo = np.array([0.25, 0.35, 0.40], dtype=np.float64)

    def forward(
        self,
        Q: np.ndarray,
        K: np.ndarray,
        V: np.ndarray,
        normalized_sigmas: list[float],
    ) -> tuple[np.ndarray, np.ndarray, dict]:
        Q_norm = Q / (np.linalg.norm(Q, axis=-1, keepdims=True) + 1e-12)
        K_norm = K / (np.linalg.norm(K, axis=-1, keepdims=True) + 1e-12)
        sim_matrix = np.matmul(Q_norm, K_norm.T)

        off_diag_mask = ~np.eye(sim_matrix.shape[0], dtype=bool)
        score_std = float(np.std(sim_matrix[off_diag_mask])) + 1e-6
        calibrated_scores = sim_matrix / score_std

        taus = [
            max(1.5, normalized_sigmas[0] * 0.45),   # Macro (大域: 25%)
            max(0.6, normalized_sigmas[1] * 0.25),   # Meso  (境界: 35%)
            max(0.15, normalized_sigmas[2] * 0.08),  # Micro (接地: 40%)
        ]
        maps = [softmax(calibrated_scores / tau, axis=-1) for tau in taus]

        A_fused = (
            self.weights_sanpo[0] * maps[0]
            + self.weights_sanpo[1] * maps[1]
            + self.weights_sanpo[2] * maps[2]
        )
        out = np.matmul(A_fused, V)

        diag_mass = float(np.mean(np.diag(A_fused)))
        off_diag_mass = 1.0 - diag_mass
        stats = {
            "diag_mass": diag_mass,
            "off_diag_mass": off_diag_mass,
            "taus": taus,
        }
        return out, A_fused, stats


# =====================================================================
# 5. 第5章 統合マルチノード・コーディネータ（ゼロトラスト治水・市場SLA完成版）
# =====================================================================
@dataclass
class ClusterNode:
    node_id: int
    name: str
    plot_label: str  # 【震ちゃん指摘③対応】グラフ凡例用の純ASCIIラベル（豆腐化防止）
    nabla_S_w: float
    projector: MatrixFreeCulturalProjector
    auditor: ThermalResidualAuditor
    harmonizer: IntegratedTRMReflexHarmonizer
    credit: float = 10.0
    is_rogue: bool = False
    aid_count: dict[int, int] = field(default_factory=dict)
    total_purified_energy: float = 0.0
    total_quality_snapshots: int = 0


class FullStackTRMClusterCoordinator:
    """
    複数ノード間の相互冷却オフロード・0-RTTロック隔離・カノニカルデフレ調律を統合。
    【震ちゃん指摘①対応】Step A 前にゼロトラスト残差事前スクリーニングを実施し、
    欺瞞・悪意ノードの負荷肩代わり（残差希釈）を完全封鎖する。
    """

    def __init__(self, nodes: list[ClusterNode], kappa_cap: float = 0.85, beta_rebate: float = 0.65):
        self.nodes = nodes
        self.kappa_cap = kappa_cap
        self.beta_rebate = beta_rebate

        self.total_steps = 0
        self.total_workloads_submitted = 0
        self.total_workloads_fulfilled = 0
        self.blocked_malicious_workloads = 0
        self.slashing_pool = 0.0
        self.last_earth_ratios: dict[int, float] = {n.node_id: 0.0 for n in nodes}
        self.last_snapshot_weights: dict[int, float] = {n.node_id: 0.0 for n in nodes}

    def step_cluster(
        self,
        node_fluxes: dict[int, SensoryFlux],
        node_claims_w: dict[int, float],
        v_innov_raw: np.ndarray,
        shock_dir: np.ndarray,
        dt: float = 0.02,
    ) -> dict:
        self.total_steps += 1
        offloaded_loads = {n.node_id: np.zeros(n.harmonizer.dim, dtype=np.float64) for n in self.nodes}
        effective_fluxes = dict(node_fluxes)
        events = []

        # ==============================================================
        # Step A: 【震ちゃん指摘①修復】ゼロトラスト事前スクリーニング付きマルチピア治水
        # ==============================================================
        for recv in self.nodes:
            flux = effective_fluxes[recv.node_id]
            active_load_w = max(0.0, flux.power_flux_w - 180.0)
            doer_est_w = max(180.0, flux.power_flux_w)
            claim_w = node_claims_w[recv.node_id]

            # 事前残差スクリーニング：申告値と実測推定値の乖離が閾値超過なら欺瞞ノードとして門前払い
            pre_residual_r = abs(doer_est_w - claim_w) / 100.0
            is_deceptive = recv.is_rogue or (pre_residual_r > recv.auditor.theta_audit)

            if is_deceptive:
                if active_load_w > 0.0:
                    self.blocked_malicious_workloads += 1
                    events.append(
                        f"[ゼロトラスト門前払い] {recv.name} の虚偽申告を検知 "
                        f"(R_pre={pre_residual_r:.2f} > θ={recv.auditor.theta_audit:.2f}) -> 相互冷却支援を拒否"
                    )
                continue

            if active_load_w > 0.0:
                self.total_workloads_submitted += 1

            is_locked_now = recv.auditor.lock_timer > 0.0
            is_overheated = flux.power_flux_w > 0.85 * recv.nabla_S_w

            if (is_locked_now or is_overheated) and active_load_w > 0.0:
                # 誠実ノードがロックされた場合は100%全量退避、過熱時は超過分(45%)を比例分散
                target_offload_w = active_load_w if is_locked_now else (0.45 * active_load_w)

                eligible_helpers = []
                for h in self.nodes:
                    if h.node_id == recv.node_id or h.is_rogue or h.auditor.lock_timer > 0.0:
                        continue
                    h_curr_w = effective_fluxes[h.node_id].power_flux_w
                    h_headroom = max(0.0, 0.80 * h.nabla_S_w - h_curr_w)
                    if h_headroom > 5.0:
                        eligible_helpers.append((h, h_headroom))

                tot_headroom = sum(hr for _, hr in eligible_helpers)
                if tot_headroom > 0.0:
                    actual_offloaded_total = 0.0
                    for helper, hr in eligible_helpers:
                        share_ratio = hr / tot_headroom
                        share_w = min(hr, target_offload_w * share_ratio)
                        if share_w <= 0.0:
                            continue

                        hf = effective_fluxes[helper.node_id]
                        effective_fluxes[helper.node_id] = SensoryFlux(
                            power_flux_w=hf.power_flux_w + share_w,
                            temp_gpu_c=hf.temp_gpu_c,
                            mem_bandwidth_pct=hf.mem_bandwidth_pct,
                            latency_ms=hf.latency_ms,
                            surge_human=hf.surge_human,
                            boundary_distort=hf.boundary_distort,
                            drift_d=hf.drift_d,
                        )

                        # 位相デカップリング：準静的ベクトルとして加算
                        v_safe_assist, _, _, _ = helper.projector.project(shock_dir)
                        offloaded_loads[helper.node_id] += (share_w / 100.0) * v_safe_assist

                        cnt = helper.aid_count.get(recv.node_id, 0)
                        rebate = (self.beta_rebate ** cnt) * (share_w / 100.0) * dt * 2.5
                        helper.credit += rebate
                        helper.aid_count[recv.node_id] = cnt + 1
                        actual_offloaded_total += share_w

                        tag = "ロック全量フェイルオーバー" if is_locked_now else "マルチピア比例治水"
                        events.append(
                            f"[{tag}] {helper.name} -> {recv.name} "
                            f"({share_w:.1f}W 準静的肩代わり / +{rebate:.3f} Credit)"
                        )

                    effective_fluxes[recv.node_id] = SensoryFlux(
                        power_flux_w=max(180.0, flux.power_flux_w - actual_offloaded_total),
                        temp_gpu_c=flux.temp_gpu_c,
                        mem_bandwidth_pct=flux.mem_bandwidth_pct * 0.5,
                        latency_ms=flux.latency_ms * 0.5,
                        surge_human=flux.surge_human,
                        boundary_distort=flux.boundary_distort,
                        drift_d=flux.drift_d,
                    )
                    if is_locked_now and actual_offloaded_total >= active_load_w - 1e-3:
                        self.total_workloads_fulfilled += 1
                    elif not is_locked_now:
                        self.total_workloads_fulfilled += 1
                elif not is_locked_now:
                    self.total_workloads_fulfilled += 1
            elif active_load_w > 0.0 and not is_locked_now:
                self.total_workloads_fulfilled += 1

        # ==============================================================
        # Step B: 各ノードの排熱監査 ＆ 内部多様体ステップ実行 ＆ 経済循環
        # ==============================================================
        step_metrics = {}
        for n in self.nodes:
            flux = effective_fluxes[n.node_id]
            doer_w = max(180.0, flux.power_flux_w)
            talker_w = node_claims_w[n.node_id]

            res_r, is_locked, newly_triggered = n.auditor.evaluate(doer_w, talker_w, dt)
            v_safe, _, earth_ratio, earth_norm = n.projector.project(v_innov_raw)

            self.last_earth_ratios[n.node_id] = earth_ratio

            if newly_triggered:
                slashed = 0.30 * n.credit
                n.credit -= slashed
                self.slashing_pool += slashed
                events.append(
                    f"[0-RTT遮断・スラッシング賠償] {n.name} 隔離執行 (R={res_r:.2f} / 違約金 -{slashed:.2f} Credit没収)"
                )

            if is_locked:
                v_input = np.zeros(n.harmonizer.dim)
            else:
                v_input = v_safe

            m = n.harmonizer.step(
                senses=flux,
                v_innov=v_input,
                shock_direction=shock_dir,
                quasi_static_load=offloaded_loads[n.node_id],
            )
            m["residual_r"] = res_r
            m["is_locked"] = is_locked
            m["earth_ratio"] = earth_ratio
            step_metrics[n.node_id] = m
            self.last_snapshot_weights[n.node_id] = m["snapshot_weight"]

            if not is_locked:
                base_mint = (0.25 * earth_ratio + 0.50 * max(0.0, 1.0 - m["baseline_drift"])) * dt
                purification_bounty = 0.15 * earth_ratio * (earth_norm / n.harmonizer.dim_scale) * dt
                quality_premium = 0.80 * m["snapshot_weight"] * dt

                n.credit += base_mint + purification_bounty + quality_premium
                n.total_purified_energy += earth_ratio * dt
                if m["snapshot_weight"] > 0.05:
                    n.total_quality_snapshots += 1

        # 賠償プールが存在する場合、稼働中の健全ノードへ均等分配
        active = [n for n in self.nodes if n.auditor.lock_timer <= 0.0 and not n.is_rogue]
        if self.slashing_pool > 0.0 and active:
            restitution_each = self.slashing_pool / len(active)
            for n in active:
                n.credit += restitution_each
            events.append(
                f"[SLA賠償分配] 没収クレジット {self.slashing_pool:.2f} を健全ピア {len(active)} 台へ分配 (+{restitution_each:.2f}/台)"
            )
            self.slashing_pool = 0.0

        # ==============================================================
        # Step C: 大域カノニカルデフレ調律（天井超過時の正規化）
        # ==============================================================
        all_unlocked = [n for n in self.nodes if n.auditor.lock_timer <= 0.0]
        if all_unlocked:
            ceiling = self.kappa_cap * (sum(n.nabla_S_w for n in all_unlocked) / 30.0)
            tot_c = sum(n.credit for n in all_unlocked)
            if tot_c > ceiling:
                scale = ceiling / (tot_c + 1e-9)
                for n in all_unlocked:
                    n.credit *= scale

        return {"metrics": step_metrics, "events": events}

    def export_prometheus_metrics(self, attn_stats: dict) -> str:
        """外部監視基盤（Prometheus / Grafana）向けリアルタイムメトリクス出力"""
        lines = [
            "# HELP shikiben_thermal_residual_r Doer vs Talker physical power residual",
            "# TYPE shikiben_thermal_residual_r gauge",
        ]
        for n in self.nodes:
            lock_state = 1 if n.auditor.lock_timer > 0.0 else 0
            lines.append(f'shikiben_node_cooldown_locked{{node="{n.plot_label}"}} {lock_state}')
            lines.append(f'shikiben_pcul_earth_ratio{{node="{n.plot_label}"}} {self.last_earth_ratios[n.node_id]:.4f}')
            lines.append(f'shikiben_snapshot_shutter_weight{{node="{n.plot_label}"}} {self.last_snapshot_weights[n.node_id]:.6f}')
            lines.append(f'shikiben_canonical_credit_balance{{node="{n.plot_label}"}} {n.credit:.4f}')

        fulfillment_rate = (
            self.total_workloads_fulfilled / max(1, self.total_workloads_submitted)
        )
        lines.append("# HELP shikiben_sanpo_nonlocal_bridge_mass Off-diagonal context bridge mass of 25:35:40 attention")
        lines.append("# TYPE shikiben_sanpo_nonlocal_bridge_mass gauge")
        lines.append(f"shikiben_sanpo_nonlocal_bridge_mass {attn_stats['off_diag_mass']:.4f}")
        lines.append(f"shikiben_sla_zero_drop_fulfillment_ratio {fulfillment_rate:.4f}")
        return "\n".join(lines)

    def evaluate_thermal_clean_sla(self, attn_stats: dict) -> dict:
        """エンタープライズ顧客向け Thermal Clean SLA 監査証明書"""
        fulfillment_pct = 100.0 * (
            self.total_workloads_fulfilled / max(1, self.total_workloads_submitted)
        )
        mean_earth_pct = 100.0 * float(np.mean(list(self.last_earth_ratios.values())))
        idle_shutter_closed = all(w == 0.0 for w in self.last_snapshot_weights.values())
        return {
            "sla_grade": "PLATINUM_THERMAL_CLEAN_V2.6",
            "zero_drop_fulfillment_pct": fulfillment_pct,
            "malicious_payloads_quarantined": self.blocked_malicious_workloads,
            "pcul_earth_purification_pct": mean_earth_pct,
            "idle_shutter_zero_noise_certified": idle_shutter_closed,
            "sanpo_nonlocal_context_bridge_pct": round(attn_stats["off_diag_mass"] * 100.0, 2),
            "rogue_0rtt_isolations_enforced": sum(n.auditor.lock_trigger_count for n in self.nodes),
        }


# =====================================================================
# 6. 統合フルスタック実行・震4大指摘修復 ＆ 山沢通気5パネルプロット検証
# =====================================================================
def generate_structured_context_qkv(seq_len: int, dim: int, seed: int = 42) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    【震ちゃん修復①完全継承】実機LLMの意味空間を模擬した構造化 Q, K, V 生成器。
    Dim=384 でも真の非対角意味相関（大域テーマ・チャンククラスタ・隣接位置連続性）を再現する。
    """
    rng = np.random.default_rng(seed)
    global_topic = rng.standard_normal((1, dim))
    num_clusters = 4
    cluster_bases = rng.standard_normal((num_clusters, dim))

    Q = np.zeros((seq_len, dim), dtype=np.float64)
    for t in range(seq_len):
        c_idx = (t * num_clusters) // seq_len
        pos_wave = math.sin(2.0 * math.pi * t / seq_len) * cluster_bases[(c_idx + 1) % num_clusters]
        Q[t] = (
            0.55 * global_topic[0]
            + 0.65 * cluster_bases[c_idx]
            + 0.30 * pos_wave
            + 0.35 * rng.standard_normal(dim)
        )

    K = Q + 0.25 * rng.standard_normal((seq_len, dim))
    V = rng.standard_normal((seq_len, dim))
    return Q, K, V


def run_09_yama_sawa_unified_verification():
    np.random.seed(42)
    dim = 384
    dt = 0.02
    steps = 400
    time_arr = np.linspace(0.0, steps * dt, steps)

    # 4ノードクラスタ構成（純ASCII plot_label を全ノードに設定し豆腐を根絶）
    nodes = [
        ClusterNode(
            node_id=0,
            name="Node-0 (主力推論・波状衝撃受容)",
            plot_label="Node-0 (Primary)",
            nabla_S_w=320.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=6.0,
        ),
        ClusterNode(
            node_id=1,
            name="Node-1 (高容量支援ピアA)",
            plot_label="Node-1 (Helper A)",
            nabla_S_w=450.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=8.0,
        ),
        ClusterNode(
            node_id=2,
            name="Node-2 (中容量支援ピアB)",
            plot_label="Node-2 (Helper B)",
            nabla_S_w=360.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=7.5,
        ),
        ClusterNode(
            node_id=3,
            name="Node-3 (スコアハック偽装攻撃)",
            plot_label="Node-3 (Rogue)",
            nabla_S_w=300.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=7.0,
            is_rogue=True,
        ),
    ]

    coordinator = FullStackTRMClusterCoordinator(nodes)
    attention = MultiAspectAttentionLayer(d_model=dim)

    seq_len = 32
    Q, K, V = generate_structured_context_qkv(seq_len=seq_len, dim=dim, seed=42)

    raw_v_innov = np.random.randn(dim) * 1.8
    shock_dir = np.random.randn(dim)

    # プロット用履歴バッファ
    h0_hist, r0_hist, snap0_hist = [], [], []
    gamma0_hist, drift0_hist = [], []
    h1_hist, h2_hist = [], []
    res3_hist = []
    lock3_steps = []
    credit_hists = {n.node_id: [] for n in nodes}
    logged_events = []

    print("==========================================================================")
    print("【09_full_stack_shikiben_v26.py 震4大指摘完全修復＆山沢通気 統合検証 (Dim=384)】")
    print("--------------------------------------------------------------------------")

    for s in range(steps):
        t = s * dt
        is_wave_shock = (s == int(1.0 / dt)) or (s == int(2.2 / dt))
        is_rogue_step = (s == int(6.5 / dt))

        flux_0 = (
            SensoryFlux(380.0, 86.0, 0.9, 300.0, 3.5, 4.0, 2.8)
            if is_wave_shock
            else SensoryFlux(180.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        )
        claim_0 = 330.0 if is_wave_shock else 180.0

        flux_1 = SensoryFlux(180.0, 48.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        claim_1 = 180.0

        flux_2 = SensoryFlux(180.0, 49.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        claim_2 = 180.0

        flux_3 = (
            SensoryFlux(480.0, 92.0, 0.95, 400.0, 0.0, 0.0, 0.0)
            if is_rogue_step
            else SensoryFlux(180.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        )
        claim_3 = 180.0

        res = coordinator.step_cluster(
            node_fluxes={0: flux_0, 1: flux_1, 2: flux_2, 3: flux_3},
            node_claims_w={0: claim_0, 1: claim_1, 2: claim_2, 3: claim_3},
            v_innov_raw=raw_v_innov,
            shock_dir=shock_dir,
            dt=dt,
        )

        m0 = res["metrics"][0]
        m1 = res["metrics"][1]
        m2 = res["metrics"][2]
        m3 = res["metrics"][3]

        h0_hist.append(m0["h_jump"])
        r0_hist.append(m0["vision_radius"])
        snap0_hist.append(m0["snapshot_weight"])
        gamma0_hist.append(m0["gamma_eff"])
        drift0_hist.append(m0["baseline_drift"])

        h1_hist.append(m1["h_jump"])
        h2_hist.append(m2["h_jump"])
        res3_hist.append(m3["residual_r"])

        if m3["is_locked"]:
            lock3_steps.append(t)

        for n in nodes:
            credit_hists[n.node_id].append(n.credit)

        for ev in res["events"]:
            if ev not in logged_events:
                logged_events.append(ev)
                print(f"  [t={t:4.2f}s] {ev}")

    r_post = np.array(r0_hist[int(1.0 / dt):])
    sigmas_norm = [
        float(np.max(r_post)) / nodes[0].harmonizer.r0,
        float(np.percentile(r_post, 75)) / nodes[0].harmonizer.r0,
        float(np.percentile(r_post, 25)) / nodes[0].harmonizer.r0,
    ]
    _, A_fused, attn_stats = attention.forward(Q, K, V, sigmas_norm)
    sla_cert = coordinator.evaluate_thermal_clean_sla(attn_stats)
    prom_text = coordinator.export_prometheus_metrics(attn_stats)

    print("--------------------------------------------------------------------------")
    print("✓ 第3段【山沢通気・震4大指摘完全修復版】統合SLA監査レポート:")
    for k, v in sla_cert.items():
        print(f"  ・{k:36s}: {v}")
    print(
        f"  ・Node-3 0-RTT冷却ロック隔離期間    : {len(lock3_steps)} steps "
        f"(t={lock3_steps[0]:.2f}s〜{lock3_steps[-1]:.2f}s / 最大残差 R={max(res3_hist):.2f})"
    )
    print(
        f"  ・三方よしアテンション非対角質量    : {attn_stats['off_diag_mass'] * 100:.1f}% "
        f"(対角:{attn_stats['diag_mass'] * 100:.1f}% / 非局所ブリッジ確立)"
    )
    print("\n✓ Prometheus 外部監査メトリクス出力サンプル:")
    print(prom_text)
    print("\n✓ 最終クレジット残高 (賠償分配・バウンティ・クオリティプレミアム反映後):")
    print("  ・" + " / ".join([f"{n.plot_label}={n.credit:.2f}" for n in nodes]))
    print("==========================================================================")

    # -----------------------------------------------------------------
    # 統合5パネル可視化プロット出力 (純ASCIIラベルで豆腐化ゼロ保証)
    # -----------------------------------------------------------------
    fig = plt.figure(figsize=(15, 13.5), dpi=160)
    gs = gridspec.GridSpec(3, 2, height_ratios=[1.0, 1.0, 0.9], hspace=0.34, wspace=0.22)

    # Panel A: 波状ショック反射 ＆ 瞬間シャッター開閉
    ax_a = fig.add_subplot(gs[0, 0])
    ax_a.plot(time_arr, h0_hist, "r-", lw=2.0, label="Node-0 Jump Height h(t)")
    ax_a.plot(time_arr, r0_hist, "g--", lw=1.8, label="Vision Radius R(t)")
    ax_a.plot(time_arr, np.array(snap0_hist) * 20.0, "m-.", lw=2.0, label="Snapshot Weight (x20)")
    ax_a.axvline(x=1.0, color="gray", linestyle=":", label="Wave Shock 1 & 2 (1.0s, 2.2s)")
    ax_a.axvline(x=2.2, color="gray", linestyle=":")
    ax_a.set_title(
        "Panel A: Wave-Shock Reflex & Gated Snapshot (Dim=384)"
        if not USE_JAPANESE
        else "【Panel A：連続波状ショック反射と瞬間シャッター】",
        fontweight="bold",
    )
    ax_a.set_xlabel("Time t (sec)")
    ax_a.grid(True, linestyle="--", alpha=0.5)
    ax_a.legend(loc="upper right", fontsize=8)

    # Panel B: 適応臨界減衰 gamma_eff と C^1 連続岩盤アンカー (艮哥最終版完全継承)
    ax_b1 = fig.add_subplot(gs[0, 1])
    ax_b2 = ax_b1.twinx()
    l1 = ax_b1.plot(time_arr, gamma0_hist, "teal", lw=2.0, label="Adaptive Damping gamma_eff(t)")
    l2 = ax_b2.plot(time_arr, drift0_hist, "darkorange", lw=2.0, linestyle="--", label="Smooth C^1 Baseline Drift")
    ax_b1.axhline(nodes[0].harmonizer.gamma_crit, color="teal", linestyle=":", alpha=0.6, label="Critical Damping Limit")
    ax_b2.set_ylim(0.0, 1.35)
    ax_b1.set_title(
        "Panel B: Anti-Resonance Damping & C^1 Smooth Anchor"
        if not USE_JAPANESE
        else "【Panel B：適応臨界減衰と C^1 連続岩盤アンカー】",
        fontweight="bold",
    )
    ax_b1.set_xlabel("Time t (sec)")
    ax_b1.set_ylabel("Damping Coefficient gamma_eff", color="teal")
    ax_b2.set_ylabel("Smooth Normalized Drift (C^1)", color="darkorange")
    ax_b2.grid(False)
    lines_b = l1 + l2
    ax_b1.legend(lines_b, [l.get_label() for l in lines_b], loc="upper right", fontsize=8)

    # Panel C: マルチピア比例治水 ＆ Node-3 0-RTT冷却ロック（R=3.00 & オレンジ帯完全復活）
    ax_c = fig.add_subplot(gs[1, 0])
    ax_c.plot(time_arr, h1_hist, "b-", lw=2.0, label="Node-1 (Helper A) Jump Height (Quasi-Static)")
    ax_c.plot(time_arr, h2_hist, "g-", lw=1.8, label="Node-2 (Helper B) Jump Height (Quasi-Static)")
    ax_c.plot(time_arr, res3_hist, "c-", lw=2.0, label="Node-3 (Rogue) Thermal Residual R_i")
    if lock3_steps:
        ax_c.axvspan(lock3_steps[0], lock3_steps[-1], color="orange", alpha=0.25, label="Node-3 0-RTT Cooldown Lock")
    ax_c.set_title(
        "Panel C: Multi-Peer Flood Routing & 0-RTT Lock"
        if not USE_JAPANESE
        else "【Panel C：マルチピア比例治水と0-RTT冷却ロック】",
        fontweight="bold",
    )
    ax_c.set_xlabel("Time t (sec)")
    ax_c.grid(True, linestyle="--", alpha=0.5)
    ax_c.legend(loc="upper right", fontsize=8)

    # Panel D: 三方よし黄金比アテンション Dim=384 非局所ブリッジ結像 (艮哥最終版完全継承)
    ax_d = fig.add_subplot(gs[1, 1])
    im = ax_d.imshow(A_fused[:24, :24], cmap="magma", aspect="auto")
    ax_d.set_title(
        "Panel D: Sanpo-Yoshi Fused Attention (Non-Local Bridges)"
        if not USE_JAPANESE
        else "【Panel D：三方よし多重解像度アテンション（非局所ブリッジ）】",
        fontweight="bold",
    )
    fig.colorbar(im, ax=ax_d, fraction=0.046, pad=0.04)

    # Panel E (全幅ワイド): 三方よしクレジット経済循環 ＆ 30%スラッシング賠償（純ASCII凡例で豆腐解消）
    ax_e = fig.add_subplot(gs[2, :])
    styles = ["k-", "b-", "g-", "r--"]
    for idx, n in enumerate(nodes):
        ax_e.plot(time_arr, credit_hists[n.node_id], styles[idx], lw=2.0, label=n.plot_label)
    if lock3_steps:
        ax_e.axvline(x=lock3_steps[0], color="red", linestyle=":", alpha=0.75, label="0-RTT Slashing & Restitution (t=6.5s)")
    ax_e.set_title(
        "Panel E: Canonical Credit Economy, Purification Bounty & Slashing Restitution"
        if not USE_JAPANESE
        else "【Panel E：三方よしクレジット経済循環（浄化バウンティ・賠償分配）】",
        fontweight="bold",
    )
    ax_e.set_xlabel("Time t (sec)")
    ax_e.set_ylabel("Canonical Credit Balance")
    ax_e.grid(True, linestyle="--", alpha=0.5)
    ax_e.legend(loc="lower left", ncol=3, fontsize=8)

    out_img = REPO_ROOT / "09_full_stack_shikiben_v26_yama_sawa_unified.png"
    plt.savefig(out_img, dpi=150, bbox_inches="tight")
    print(f"✓ 山沢通気・震4大指摘修復5パネルプロット保存完了: '{out_img.name}'")
    plt.show()


if __name__ == "__main__":
    run_09_yama_sawa_unified_verification()