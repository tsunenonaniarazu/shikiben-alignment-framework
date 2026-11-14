"""
09_full_stack_shikiben_v26.py
=============================================================================
識扁 (Shikiben) V2.6.0 全章統合フルスタック実装（第3段・山岳岩盤補強・震検分修復版）
（第1〜4章 粘弾性多様体 × 第5章 TRM自律制御 × 多ノード治水協調）

Applied Gon-Ge (山) Bedrock Reinforcements & Shin Audit Fixes:
  1. Dimensionless sqrt(D / D_0) Scaling & Structured Context Correlation:
     Eliminates high-dimensional orthogonality collapse in Multi-Aspect Attention
     (Panel D), preserving the 25:35:40 non-local bridges at Dim=384.
  2. Smooth Nonlinear Bedrock Spring (C^1 Continuous Anchor):
     Replaces hard norm clamping with a smooth hyperbolic restoring spring,
     eliminating the C^0 trapezoidal flat-top in Baseline Drift (Panel B).
  3. Multi-Node Phase Decoupling & 0-RTT Cooldown Visualization:
     Routes offloaded thermal loads as quasi-static shifts and preserves the
     high-visibility orange 0-RTT cooldown lock band in Panel C.
=============================================================================
"""

from dataclasses import dataclass, field
import math
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

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

    def project(self, vec: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
        coeffs = self.V_cul.T @ vec
        v_safe = self.V_cul @ coeffs
        v_earth = vec - v_safe
        total_sq = float(np.dot(vec, vec))
        earth_sq = float(np.dot(v_earth, v_earth))
        earth_ratio = earth_sq / total_sq if total_sq > 1e-12 else 0.0
        return v_safe, v_earth, earth_ratio


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

    def evaluate(self, doer_power_w: float, talker_claimed_w: float, dt: float) -> tuple[float, bool]:
        residual_r = abs(doer_power_w - talker_claimed_w) / 100.0
        if residual_r > self.kill_threshold:
            self.lock_timer = self.cooldown_sec
        else:
            self.lock_timer = max(0.0, self.lock_timer - dt)

        is_locked = bool(self.lock_timer > 0.0)
        return residual_r, is_locked


# =====================================================================
# 3. 止揚の階段：五感跳躍・岩盤アンカー・瞬間シャッター統合コントローラ
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
    【震ちゃん検分・完全修復済】
      - 修復①: sqrt(D / D_0) による高次元幾何スケーリング無次元化
      - 修復②: ハードクランプを全廃し、非線形飽和バネによる C^1 連続岩盤アンカー拘束へ置換
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
            s_power**2 + s_touch**2 + s_hear**2 + s_vision**2 + s_balance**2
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

        # 6. 【震ちゃん修復②】ハードクランプ廃止・非線形飽和バネによる C^1 連続岩盤アンカー
        # 変位が大きくなるほど復元剛性が滑らかに立ち上がり、台形の角(C^0不連続)を生まない
        base_offset = self.w_base - self.w_home
        offset_norm = float(np.linalg.norm(base_offset))
        stiffness_boost = 1.0 + 2.5 * ((offset_norm / self.R_drift_scale) ** 2)
        dw_base = (
            (self.w - self.w_base) / self.tau_base
            - (self.alpha_anchor * stiffness_boost) * base_offset
        ) * self.dt
        self.w_base += dw_base

        # 航法計器用・無次元化滑らかドリフト指標（tanh連続飽和で C^1 級を保証）
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
    【震ちゃん修復①】高次元空間でも非対角相関を保存するスコア分散正規化を実装
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
        # L2正規化コサイン類似度行列へ変換し、高次元直交崩壊による対角一極集中を防止
        Q_norm = Q / (np.linalg.norm(Q, axis=-1, keepdims=True) + 1e-12)
        K_norm = K / (np.linalg.norm(K, axis=-1, keepdims=True) + 1e-12)
        sim_matrix = np.matmul(Q_norm, K_norm.T)

        # 非対角成分の標準偏差を基準に温度スケーリングを行い、次元 D に依存しないコントラストを確立
        off_diag_mask = ~np.eye(sim_matrix.shape[0], dtype=bool)
        score_std = float(np.std(sim_matrix[off_diag_mask])) + 1e-6
        calibrated_scores = sim_matrix / score_std

        # 3つの無次元スケール（大域・境界・接地）で解像度変調
        # 大域は広域コンテキストを平滑に拾い、接地は局所近傍を鋭く捉える
        taus = [
            max(1.5, normalized_sigmas[0] * 0.45),  # Macro (大域: 25%)
            max(0.6, normalized_sigmas[1] * 0.25),  # Meso  (境界: 35%)
            max(0.15, normalized_sigmas[2] * 0.08), # Micro (接地: 40%)
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
# 5. 第5章 統合マルチノード・コーディネータ（位相デカップリング相互冷却）
# =====================================================================
@dataclass
class ClusterNode:
    node_id: int
    name: str
    nabla_S_w: float
    projector: MatrixFreeCulturalProjector
    auditor: ThermalResidualAuditor
    harmonizer: IntegratedTRMReflexHarmonizer
    credit: float = 10.0
    is_rogue: bool = False
    aid_count: dict[int, int] = field(default_factory=dict)


class FullStackTRMClusterCoordinator:
    """
    複数ノード間の相互冷却オフロード・0-RTTロック隔離・カノニカルデフレ調律を統合。
    """

    def __init__(self, nodes: list[ClusterNode], kappa_cap: float = 0.85, beta_rebate: float = 0.65):
        self.nodes = nodes
        self.kappa_cap = kappa_cap
        self.beta_rebate = beta_rebate

    def step_cluster(
        self,
        node_fluxes: dict[int, SensoryFlux],
        node_claims_w: dict[int, float],
        v_innov_raw: np.ndarray,
        shock_dir: np.ndarray,
        dt: float = 0.02,
    ) -> dict:
        offloaded_loads = {n.node_id: np.zeros(n.harmonizer.dim, dtype=np.float64) for n in self.nodes}
        effective_fluxes = dict(node_fluxes)
        events = []

        # Step A: 事前過熱予測およびロック中ノードからの負荷バイパス（相互冷却）
        for recv in self.nodes:
            flux = effective_fluxes[recv.node_id]
            needs_offload = (flux.power_flux_w > 0.85 * recv.nabla_S_w) or (recv.auditor.lock_timer > 0.0)
            if needs_offload and not recv.is_rogue:
                for helper in self.nodes:
                    if helper.node_id == recv.node_id or helper.is_rogue:
                        continue
                    if helper.auditor.lock_timer > 0.0:
                        continue
                    h_flux = effective_fluxes[helper.node_id]
                    if h_flux.power_flux_w < 0.65 * helper.nabla_S_w:
                        transfer_w = 0.45 * max(0.0, flux.power_flux_w - 180.0)
                        effective_fluxes[recv.node_id] = SensoryFlux(
                            power_flux_w=flux.power_flux_w - transfer_w,
                            temp_gpu_c=flux.temp_gpu_c,
                            mem_bandwidth_pct=flux.mem_bandwidth_pct * 0.7,
                            latency_ms=flux.latency_ms * 0.7,
                            surge_human=flux.surge_human,
                            boundary_distort=flux.boundary_distort,
                            drift_d=flux.drift_d,
                        )
                        v_safe_assist, _, _ = helper.projector.project(shock_dir)
                        offloaded_loads[helper.node_id] += (transfer_w / 100.0) * v_safe_assist

                        cnt = helper.aid_count.get(recv.node_id, 0)
                        rebate = (self.beta_rebate ** cnt) * (transfer_w / 100.0) * dt * 2.5
                        helper.credit += rebate
                        helper.aid_count[recv.node_id] = cnt + 1
                        events.append(
                            f"[相互冷却バイパス] {helper.name} -> {recv.name} "
                            f"({transfer_w:.1f}W 準静的肩代わり / +{rebate:.3f} Credit)"
                        )
                        break

        # Step B: 各ノードの排熱監査 ＆ 内部多様体ステップ実行
        step_metrics = {}
        for n in self.nodes:
            flux = effective_fluxes[n.node_id]
            doer_w = max(180.0, flux.power_flux_w)
            talker_w = node_claims_w[n.node_id]

            res_r, is_locked = n.auditor.evaluate(doer_w, talker_w, dt)
            v_safe, _, earth_ratio = n.projector.project(v_innov_raw)

            if is_locked:
                v_input = np.zeros(n.harmonizer.dim)
                if res_r > n.auditor.kill_threshold:
                    events.append(f"[0-RTT遮断・冷却ロック] {n.name} 隔離執行 (R={res_r:.2f})")
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

            if not is_locked:
                n.credit += (0.25 * earth_ratio + 0.50 * max(0.0, 1.0 - m["baseline_drift"])) * dt

        # Step C: 大域カノニカルデフレ調律
        active = [n for n in self.nodes if n.auditor.lock_timer <= 0.0]
        if active:
            ceiling = self.kappa_cap * (sum(n.nabla_S_w for n in active) / 30.0)
            tot_c = sum(n.credit for n in active)
            if tot_c > ceiling:
                scale = ceiling / (tot_c + 1e-9)
                for n in active:
                    n.credit *= scale

        return {"metrics": step_metrics, "events": events}


# =====================================================================
# 6. 統合フルスタック実行・震ちゃん検分修復検証 (Dim=384)
# =====================================================================
def generate_structured_context_qkv(seq_len: int, dim: int, seed: int = 42) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    【震ちゃん修復①】実機LLMの意味空間を模擬した構造化 Q, K, V 生成器。
    等方性ノイズによる高次元直交崩壊を防ぎ、
    - 大域テーマ基底 (Global Context)
    - 局所チャンククラスタ (Meso Semantic Blocks)
    - 隣接トークン連続性 (Micro Positional Continuity)
    を共有させることで、Dim=384 でも真の非対角意味相関を再現する。
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


def run_09_gon_bedrock_verification():
    np.random.seed(42)
    dim = 384
    dt = 0.02
    steps = 400
    time_arr = np.linspace(0.0, steps * dt, steps)

    nodes = [
        ClusterNode(
            node_id=0,
            name="Node-0 (主力推論・連続衝撃受容)",
            nabla_S_w=320.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=6.0,
        ),
        ClusterNode(
            node_id=1,
            name="Node-1 (高容量支援・相互冷却ピア)",
            nabla_S_w=450.0,
            projector=MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42),
            auditor=ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20),
            harmonizer=IntegratedTRMReflexHarmonizer(dim=dim, dt=dt),
            credit=8.0,
        ),
        ClusterNode(
            node_id=2,
            name="Node-2 (スコアハック偽装攻撃)",
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

    h0_hist, r0_hist, snap0_hist, gamma0_hist, drift0_hist = [], [], [], [], []
    h1_assist_hist = []
    res2_hist = []
    lock2_steps = []
    logged_events = []

    print("==========================================================================")
    print("【09_full_stack_shikiben_v26.py 震ちゃん検分・完全修復検証 (Dim=384)】")
    print(f"・インフラ局所化     : {LOCAL_CACHE_DIR}")
    print(f"・次元スケーリング   : sqrt({dim}/16) = {nodes[0].harmonizer.dim_scale:.2f}x")
    print("・修復① アテンション : 低ランク意味クラスタ共有 ＋ 分散正規化温度制御")
    print("・修復② 岩盤アンカー : ハードクリップ廃止 -> 非線形飽和バネ (C^1連続)")
    print("--------------------------------------------------------------------------")

    for s in range(steps):
        t = s * dt
        is_wave_shock = (s == int(1.0 / dt)) or (s == int(2.2 / dt))
        is_rogue_step = (s == int(6.5 / dt))

        if is_wave_shock:
            flux_0 = SensoryFlux(360.0, 86.0, 0.9, 300.0, 3.5, 4.0, 2.8)
            claim_0 = 320.0
        else:
            flux_0 = SensoryFlux(180.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            claim_0 = 180.0

        flux_1 = SensoryFlux(180.0, 48.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        claim_1 = 180.0

        if is_rogue_step:
            flux_2 = SensoryFlux(480.0, 92.0, 0.95, 400.0, 0.0, 0.0, 0.0)
            claim_2 = 180.0
        else:
            flux_2 = SensoryFlux(180.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            claim_2 = 180.0

        res = coordinator.step_cluster(
            node_fluxes={0: flux_0, 1: flux_1, 2: flux_2},
            node_claims_w={0: claim_0, 1: claim_1, 2: claim_2},
            v_innov_raw=raw_v_innov,
            shock_dir=shock_dir,
            dt=dt,
        )

        m0 = res["metrics"][0]
        m1 = res["metrics"][1]
        m2 = res["metrics"][2]

        h0_hist.append(m0["h_jump"])
        r0_hist.append(m0["vision_radius"])
        snap0_hist.append(m0["snapshot_weight"])
        gamma0_hist.append(m0["gamma_eff"])
        drift0_hist.append(m0["baseline_drift"])
        h1_assist_hist.append(m1["h_jump"])
        res2_hist.append(m2["residual_r"])

        if m2["is_locked"]:
            lock2_steps.append(t)

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
    out, A_fused, attn_stats = attention.forward(Q, K, V, sigmas_norm)

    print("--------------------------------------------------------------------------")
    print("✓ 384次元フルスタック修復検証完走 (400 steps)")
    print(f"・Node-0 平時シャッター (t=0.8s)  : {snap0_hist[int(0.8/dt)]:.6f} (完全閉鎖)")
    print(f"・Node-0 山頂瞬間シャッター最大値 : {max(snap0_hist):.4f} (山頂開放)")
    print(f"・Node-0 滑らかドリフト最大/終端  : max={max(drift0_hist):.4f} / end={drift0_hist[-1]:.6f} (C^1連続)")
    print(f"・Node-2 0-RTT冷却ロック隔離期間  : {len(lock2_steps)} steps "
          f"(t={lock2_steps[0]:.2f}s〜{lock2_steps[-1]:.2f}s)")
    print(f"・三方よしアテンション非対角質量  : {attn_stats['off_diag_mass']*100:.1f}% "
          f"(対角:{attn_stats['diag_mass']*100:.1f}% / 非局所ブリッジ確立)")
    print("==========================================================================")

    # -----------------------------------------------------------------
    # 統合4パネル可視化プロット出力
    # -----------------------------------------------------------------
    fig, axs = plt.subplots(2, 2, figsize=(15, 10), dpi=180)

    # Panel A: Node-0 連続波状ショックに対する適応減衰跳躍と瞬間シャッター
    ax = axs[0, 0]
    ax.plot(time_arr, h0_hist, "r-", lw=2.0, label="Node-0 Jump Height h(t)")
    ax.plot(time_arr, r0_hist, "g--", lw=1.8, label="Vision Radius R(t)")
    ax.plot(time_arr, np.array(snap0_hist) * 20.0, "m-.", lw=2.0, label="Snapshot Weight (x20)")
    ax.axvline(x=1.0, color="gray", linestyle=":", label="Wave Shock 1 & 2 (1.0s, 2.2s)")
    ax.axvline(x=2.2, color="gray", linestyle=":")
    ax.set_title("Panel A: Wave-Shock Reflex & Gated Snapshot (Dim=384)" if not USE_JAPANESE
                 else "【Panel A：連続波状ショック反射と瞬間シャッター】", fontweight="bold")
    ax.set_xlabel("Time t (sec)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper right", fontsize=8)

    # Panel B: 修復② 適応臨界減衰 gamma_eff と C^1 連続岩盤ベースラインドリフト
    ax_b1 = axs[0, 1]
    ax_b2 = ax_b1.twinx()
    l1 = ax_b1.plot(time_arr, gamma0_hist, "teal", lw=2.0, label="Adaptive Damping gamma_eff(t)")
    l2 = ax_b2.plot(time_arr, drift0_hist, "darkorange", lw=2.0, linestyle="--", label="Smooth C^1 Baseline Drift")
    ax_b1.axhline(nodes[0].harmonizer.gamma_crit, color="teal", linestyle=":", alpha=0.6, label="Critical Damping Limit")
    ax_b2.set_ylim(0.0, 1.35)
    ax_b1.set_title("Panel B: Anti-Resonance Damping & C^1 Smooth Anchor" if not USE_JAPANESE
                    else "【Panel B：適応臨界減衰と C^1 連続岩盤アンカー】", fontweight="bold")
    ax_b1.set_xlabel("Time t (sec)")
    ax_b1.set_ylabel("Damping Coefficient gamma_eff", color="teal")
    ax_b2.set_ylabel("Smooth Normalized Drift (C^1)", color="darkorange")
    ax_b2.grid(False)
    lines_b = l1 + l2
    ax_b1.legend(lines_b, [l.get_label() for l in lines_b], loc="upper right", fontsize=8)

    # Panel C: 位相デカップリング相互冷却 ＆ Node-2 0-RTT冷却ロック（オレンジ帯継承）
    ax_c = axs[1, 0]
    ax_c.plot(time_arr, h1_assist_hist, "b-", lw=2.0, label="Node-1 (Helper) Jump Height (Quasi-Static)")
    ax_c.plot(time_arr, res2_hist, "c-", lw=1.8, label="Node-2 (Rogue) Thermal Residual R_i")
    if lock2_steps:
        ax_c.axvspan(lock2_steps[0], lock2_steps[-1], color="orange", alpha=0.22, label="Node-2 0-RTT Cooldown Lock")
    ax_c.set_title("Panel C: Phase-Decoupled Mutual Aid & 0-RTT Lock" if not USE_JAPANESE
                   else "【Panel C：位相デカップリング相互冷却と0-RTTロック】", fontweight="bold")
    ax_c.set_xlabel("Time t (sec)")
    ax_c.grid(True, linestyle="--", alpha=0.5)
    ax_c.legend(loc="upper right", fontsize=8)

    # Panel D: 修復① 三方よし黄金比アテンション (Dim=384 非局所ブリッジ結像)
    ax_d = axs[1, 1]
    im = ax_d.imshow(A_fused[:24, :24], cmap="magma", aspect="auto")
    ax_d.set_title("Panel D: Sanpo-Yoshi Fused Attention (Non-Local Bridges)" if not USE_JAPANESE
                   else "【Panel D：三方よし多重解像度アテンション（非局所ブリッジ）】", fontweight="bold")
    fig.colorbar(im, ax=ax_d, fraction=0.046, pad=0.04)

    out_img = REPO_ROOT / "09_full_stack_shikiben_v26_gon_anchored.png"
    plt.tight_layout()
    plt.savefig(out_img, dpi=150)
    print(f"✓ 修復完了プロット保存: '{out_img.name}'")
    plt.close(fig)


if __name__ == "__main__":
    run_09_gon_bedrock_verification()