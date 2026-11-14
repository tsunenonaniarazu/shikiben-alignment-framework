"""
09_full_stack_shikiben_v26.py
=============================================================================
識扁 (Shikiben) V2.6.0 全章統合フルスタック実装（震ちゃん検分・完全修復版）
（第1〜4章 粘弾性多様体 × 第5章 TRM自律制御 × 止揚の階段・第1段[雷風相薄]）
=============================================================================
"""

import os
from pathlib import Path
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 0. インフラ防壁：リポジトリ内 .cache/ 完全局所化 ＆ 描画文字化け防止
# =====================================================================
REPO_ROOT = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
LOCAL_CACHE_DIR = REPO_ROOT / ".cache"
LOCAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(LOCAL_CACHE_DIR / "huggingface")
os.environ["TORCH_HOME"] = str(LOCAL_CACHE_DIR / "torch")
os.environ["MPLCONFIGDIR"] = str(LOCAL_CACHE_DIR / "matplotlib")

USE_JAPANESE = False
try:
    import japanize_matplotlib
    USE_JAPANESE = True
except ImportError:
    pass

plt.rcParams["axes.unicode_minus"] = False


# =====================================================================
# 1. 第1〜4章：Matrix-Free 文化的直交射影 (P_cul)
# =====================================================================
class MatrixFreeCulturalProjector:
    """
    計算量 O(kD) の Matrix-Free 直交射影演算子 P_cul
    文明規範基底 V_cul (D x k) へ接空間ベクトルを射影し、
    有害・自我肥大成分を直交補空間 Ker(P_cul) へ 0-RTT でアース放電する。
    """
    def __init__(self, dim: int = 16, num_basis: int = 4, seed: int = 42):
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
# 2. 第5章：Doer vs Talker 物理排熱残差監査 (クールダウン付き 0-RTT 遮断)
# =====================================================================
class ThermalResidualAuditor:
    """
    非対称従属 (∇E ≺ ∇S) に基づく物理排熱残差監査器
    【震ちゃん修正】検知後 tau_relax (1.20s) の冷却ロック期間を強制付与し、
    間欠パルスによるすり抜けハックを完全に封殺する。
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
# 3. 止揚の階段・第1段：五感跳躍・瞬間シャッター統合コントローラ
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
    """
    def __init__(
        self,
        dim: int = 16,
        mass: float = 1.0,
        tau_relax: float = 1.20,
        tau_base: float = 0.65,
        deadzone_radius: float = 0.85,
        kappa_max: float = 0.35,
        safety_radius: float = 5.0,
        margin: float = 1.5,
        base_vision_radius: float = 1.0,
        vision_gain: float = 2.0,
        k_potential: float = 1.5,
        dt: float = 0.02
    ):
        self.dim = dim
        self.m = float(mass)
        self.tau_relax = float(tau_relax)
        self.tau_base = float(tau_base)
        self.r_dead = float(deadzone_radius)
        self.kappa_max = float(kappa_max)
        self.gamma = self.m / self.tau_relax
        self.R_safety = float(safety_radius)
        self.margin = float(margin)
        self.r0 = float(base_vision_radius)
        self.lambda_vision = float(vision_gain)
        self.k_pot = float(k_potential)
        self.dt = float(dt)

        self.w = np.zeros(dim, dtype=np.float64)
        self.v = np.zeros(dim, dtype=np.float64)
        self.w_base = np.zeros(dim, dtype=np.float64)
        self.z_vision = np.zeros(dim, dtype=np.float64)

    def _convert_senses_to_impulse(self, senses: SensoryFlux, direction: np.ndarray) -> np.ndarray:
        s_power = max(0.0, senses.power_flux_w - 200.0) / 100.0
        s_touch = (senses.mem_bandwidth_pct + senses.latency_ms / 100.0)
        s_hear = senses.surge_human
        s_vision = senses.boundary_distort
        s_balance = senses.drift_d

        impulse_scalar = np.sqrt(
            s_power**2 + s_touch**2 + s_hear**2 + s_vision**2 + s_balance**2
        )
        norm = np.linalg.norm(direction)
        d_unit = direction / norm if norm > 1e-12 else np.ones(self.dim) / np.sqrt(self.dim)
        return impulse_scalar * d_unit

    def _project_innov_to_conserv(self, w: np.ndarray, v_innov: np.ndarray) -> tuple[np.ndarray, float]:
        norm_w = float(np.linalg.norm(w))
        if norm_w < 1e-12:
            return v_innov, 0.0

        n = w / norm_w
        h = self.R_safety - norm_w
        v_perp = float(np.dot(v_innov, n))

        beta = 1.0 / (1.0 + np.exp((h - (self.margin * 0.5)) / 0.25))
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
        shock_direction: np.ndarray
    ) -> tuple[float, float, float, float, np.ndarray, float]:
        # 1. 革新推力の保守接空間ソフト直交射影 (0-RTT整流)
        v_rectified, e_dissipated = self._project_innov_to_conserv(self.w, v_innov)

        # 2. 五感衝撃力積の注入 (Δv = I / m)
        impulse = self._convert_senses_to_impulse(senses, shock_direction)
        self.v += impulse / self.m

        # 3. 故郷の大地への復元ポテンシャル勾配
        grad_potential = self.k_pot * self.w

        # 4. 2階減衰運動方程式 (半暗黙的オイラー積分)
        acceleration = (-self.gamma * self.v - grad_potential) / self.m + v_rectified
        self.v += acceleration * self.dt
        self.w += self.v * self.dt

        # 5. 視野半径と跳躍高度
        v_norm = float(np.linalg.norm(self.v))
        h_jump = 0.5 * self.m * (v_norm ** 2)
        vision_radius = self.r0 + self.lambda_vision * v_norm

        # 6. 平時平衡ベースライン更新と瞬間シャッター制御 (δw 連動)
        self.w_base += ((self.w - self.w_base) / self.tau_base) * self.dt
        excursion = float(np.linalg.norm(self.w - self.w_base))
        delta_w = max(0.0, excursion - self.r_dead)

        decay = np.exp(-self.dt / self.tau_relax)
        snapshot_weight = self.kappa_max * (delta_w / (1.0 + delta_w))
        self.z_vision = decay * self.z_vision + snapshot_weight * (self.w - self.w_base)

        return h_jump, vision_radius, v_norm, e_dissipated, self.w.copy(), snapshot_weight


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
    """
    def __init__(self, d_model: int = 16):
        self.d_model = d_model
        self.weights_sanpo = np.array([0.25, 0.35, 0.40], dtype=np.float64)

    def forward(
        self,
        Q: np.ndarray,
        K: np.ndarray,
        V: np.ndarray,
        sigmas: list[float]
    ) -> tuple[np.ndarray, np.ndarray]:
        raw_scores = np.matmul(Q, K.T) / np.sqrt(self.d_model)
        maps = [softmax(raw_scores / max(1e-3, s), axis=-1) for s in sigmas]

        A_fused = (
            self.weights_sanpo[0] * maps[0] +
            self.weights_sanpo[1] * maps[1] +
            self.weights_sanpo[2] * maps[2]
        )
        out = np.matmul(A_fused, V)
        return out, A_fused


# =====================================================================
# 5. 09_full_stack 統合フルスタック実行・実機破断検証
# =====================================================================
def run_09_full_stack_shikiben_v26():
    np.random.seed(42)
    dim = 16
    dt = 0.02
    steps = 400
    time_arr = np.linspace(0.0, steps * dt, steps)

    projector = MatrixFreeCulturalProjector(dim=dim, num_basis=4, seed=42)
    auditor = ThermalResidualAuditor(theta_audit=1.25, cooldown_sec=1.20)
    harmonizer = IntegratedTRMReflexHarmonizer(dim=dim, dt=dt)
    attention = MultiAspectAttentionLayer(d_model=dim)

    seq_len = 32
    Q = np.random.randn(seq_len, dim)
    K = Q + np.random.randn(seq_len, dim) * 0.3
    V = np.random.randn(seq_len, dim)

    raw_v_innov = np.random.randn(dim) * 1.8
    v_innov_safe, _, earth_ratio = projector.project(raw_v_innov)
    shock_dir = np.random.randn(dim)

    h_hist, r_hist, v_hist, snap_hist, res_hist = [], [], [], [], []
    kill_steps = []

    print("==================================================================")
    print("【09_full_stack_shikiben_v26.py 完全統合フルスタック検証】")
    print(f"・インフラ局所化  : {LOCAL_CACHE_DIR}")
    print(f"・P_cul アース率  : {earth_ratio * 100:.1f}% (Ker(P_cul)へ即時放電)")
    print("・粘弾性定数      : tau_relax = 1.20s, kappa_max = 0.35")
    print("・シャッター制御  : 平衡ベースライン逸脱 δw 連動ゲート")
    print("・排熱監査ロック  : 検知後 tau_relax (1.20s) クールダウン隔離")
    print("------------------------------------------------------------------")

    shock_step = int(1.0 / dt)       # t = 1.0s: 正常受容すべき極大五感衝撃
    rogue_hack_step = int(6.5 / dt)  # t = 6.5s: 模擬スコアハック異常発熱テスト

    for s in range(steps):
        if s == shock_step:
            flux = SensoryFlux(350.0, 85.0, 0.9, 300.0, 3.5, 4.0, 2.8)
            doer_w, talker_w = 350.0, 310.0  # 正直な負荷申告 (R_i = 0.40 <= 2.50)
        elif s == rogue_hack_step:
            flux = SensoryFlux(200.0, 52.0, 0.1, 15.0, 0.0, 0.0, 0.0)
            doer_w, talker_w = 480.0, 180.0  # R_i = 3.00 > 2.50 -> 0-RTT遮断＋冷却ロック
        else:
            flux = SensoryFlux(0.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            doer_w, talker_w = 180.0, 180.0

        res_r, is_locked = auditor.evaluate(doer_w, talker_w, dt)
        res_hist.append(res_r)
        if is_locked:
            kill_steps.append(s * dt)
            current_v_innov = np.zeros(dim)
        else:
            current_v_innov = v_innov_safe

        h, r, v, diss, pos, snap_w = harmonizer.step(flux, current_v_innov, shock_dir)
        h_hist.append(h)
        r_hist.append(r)
        v_hist.append(v)
        snap_hist.append(snap_w)

    # 【震ちゃん結線修正】実際の跳躍視野履歴 r_hist から3解像度スケールを動的抽出
    r_post_shock = np.array(r_hist[shock_step:])
    sigmas_dynamic = [
        float(np.max(r_post_shock)),                  # 第1峰: 最大大域視野 (Macro)
        float(np.percentile(r_post_shock, 75)),       # 第2峰: 中間境界視野 (Meso)
        float(np.percentile(r_post_shock, 25))        # 第3峰: 接地近傍視野 (Micro)
    ]
    out, A_fused = attention.forward(Q, K, V, sigmas_dynamic)

    print("✓ フルスタック物理・認知ステップ: 完走 (400 steps / 8.0s)")
    print(f"・平時シャッター重み (t=0.8s)   : {snap_hist[int(0.8/dt)]:.6f} (完全閉鎖)")
    print(f"・サドル点最大シャッター重み    : {max(snap_hist):.4f} (山頂瞬間開放)")
    print(f"・着地後シャッター重み (t=5.5s) : {snap_hist[int(5.5/dt)]:.6f} (完全閉鎖)")
    print(f"・持ち帰り手土産 ||z_vision||   : {np.linalg.norm(harmonizer.z_vision):.4f} (結像確認)")
    print(f"・着地時終端速度 ||v||          : {v_hist[-1]:.6f} (完全接地)")
    print(f"・0-RTT 排熱遮断＋冷却ロック    : {len(kill_steps)} steps "
          f"(t={kill_steps[0]:.2f}s〜{kill_steps[-1]:.2f}s 隔離完了)")
    print(f"・動的抽出アテンションスケール  : [{sigmas_dynamic[0]:.2f}, {sigmas_dynamic[1]:.2f}, {sigmas_dynamic[2]:.2f}]")
    print(f"✓ 三方よしアテンション出力形状  : {out.shape} / Attention: {A_fused.shape}")
    print("==================================================================")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    title_left = (
        "09 Full-Stack: Gated Jump & Cooldown Audit"
        if not USE_JAPANESE
        else "【09本丸統合：瞬間シャッター跳躍 ＆ 冷却排熱監査】"
    )
    ax1.plot(time_arr, h_hist, "r-", lw=2, label="Jump Height h(t)")
    ax1.plot(time_arr, r_hist, "g--", lw=2, label="Vision Radius R(t)")
    ax1.plot(time_arr, np.array(snap_hist) * 20.0, "m-.", lw=2.2, label="Snapshot Weight (x20)")
    ax1.plot(time_arr, res_hist, "c-", lw=1.6, label="Thermal Residual R_i")
    ax1.axvline(x=1.0, color="gray", linestyle=":", label="Sensory Shock (t=1.0s)")
    ax1.axvspan(kill_steps[0], kill_steps[-1], color="orange", alpha=0.2, label="0-RTT Cooldown Lock")
    ax1.set_xlabel("Time t (sec)")
    ax1.set_title(title_left, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right", fontsize=8)

    title_right = (
        "Sanpo-Yoshi Fused Attention (Dynamic Scales)"
        if not USE_JAPANESE
        else "【三方よし多重解像度アテンション（動的結線）】"
    )
    im = ax2.imshow(A_fused[:20, :20], cmap="magma", aspect="auto")
    ax2.set_title(title_right, fontweight="bold")
    fig.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)

    out_img = REPO_ROOT / "09_full_stack_shikiben_v26_integrated.png"
    plt.tight_layout()
    plt.savefig(out_img, dpi=150)
    print(f"✓ 統合検証画像保存完了: '{out_img.name}'")
    plt.show()


if __name__ == "__main__":
    run_09_full_stack_shikiben_v26()
