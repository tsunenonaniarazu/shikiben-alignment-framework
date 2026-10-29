"""
09_full_stack_shikiben_v26.py
========================================================================
Shikiben V2.6.0 Full-Stack Integrated Simulation (Chapters 1-4 + Chapter 5)

Architecture:
  - Micro-Layer (Ch. 1-4): Each node operates a D-dimensional Riemannian
    unit-sphere manifold with Matrix-Free P_cul projection and a continuous
    first-order viscoelastic ODE filter (z_latent, kappa_slump, lambda_decay).
  - Macro-Layer (Ch. 5): The TRM Network Coordinator audits physical flux
    residuals, executes 0-RTT isolation, offloads shock vectors via Mutual
    Thermal Aid, and enforces Grace-Exempt Canonical Credit Deflation.
========================================================================
"""

from dataclasses import dataclass, field
import math
import numpy as np


# ---------------------------------------------------------------------
# 1. Matrix-Free 幾何学演算子 (Ch. 1-4 共通カーネル)
# ---------------------------------------------------------------------
def project_harm(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    return V_harm @ (V_harm.T @ v)


def project_cul(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    return v - V_harm @ (V_harm.T @ v)


def project_tangent(v: np.ndarray, x_sphere: np.ndarray) -> np.ndarray:
    return v - x_sphere * float(np.dot(x_sphere, v))


# ---------------------------------------------------------------------
# 2. ミクロ層：第1〜4章 粘弾性多様体ノード (ManifoldNode)
# ---------------------------------------------------------------------
@dataclass
class ManifoldNode:
    id: int
    name: str
    nabla_S: float                  # ハードウェア実在容量上限
    x: np.ndarray                   # 多様体上の内部状態ベクトル x_i(t) ∈ S^{D-1}
    X_star_civ: np.ndarray          # 事前純化済みの文明アトラクター
    V_harm: np.ndarray              # 有害部分空間の正規直交基底 [Dim, k]
    credit: float = 10.0            # 保有クレジット C_i
    p_idle: float = 1.5             # 基礎代謝熱量
    is_malicious: bool = False      # 悪意フラグ (P_cul バイパス ＆ 虚偽申告)
    isolated: bool = False          # 0-RTT 物理隔離フラグ

    # 内部連続状態 (Ch. 1-4 粘弾性フィルタ)
    z_latent: np.ndarray = field(init=False)
    tau_thinking: float = 0.0
    nabla_E: float = 1.5
    d_drift: float = 0.0
    l_earth: float = 0.0
    kappa_slump: float = 0.0
    lambda_decay: float = 0.80
    in_grace: bool = False
    aid_history: dict[int, int] = field(default_factory=dict)

    def __post_init__(self):
        self.z_latent = np.zeros_like(self.x)

    def estimate_incoming_energy(self, shock_vec: np.ndarray) -> float:
        """外乱ベクトルを受けた場合の予測実行熱量 ∇E_est を事前算定 (相互冷却トリガー用)"""
        if self.isolated:
            return 0.0
        s_real = project_cul(shock_vec, self.V_harm)
        s_harm = project_harm(shock_vec, self.V_harm)
        leaked = float(np.linalg.norm(s_harm)) if self.is_malicious else 0.0
        return (
            self.p_idle
            + 0.8 * float(np.linalg.norm(s_real))
            + 0.6 * float(np.linalg.norm(self.z_latent))
            + 2.5 * leaked
        )

    def step_internal_manifold(
        self,
        effective_shock: np.ndarray,
        dt: float = 0.05,
        tau_relax: float = 1.20,
        kappa_max: float = 0.35,
        lambda_0: float = 0.80,
        lambda_min: float = 0.20,
    ):
        """【第1〜4章】単一ノード内部の超伝導・粘弾性リーマン多様体更新"""
        if self.isolated:
            self.nabla_E = 0.0
            self.d_drift = 0.0
            self.l_earth = 0.0
            self.in_grace = False
            return

        # 1. P_cul による避雷針分離 (悪意ノードは P_cul をバイパスして有害成分を内部へ通す)
        if not self.is_malicious:
            shock_harmful = project_harm(effective_shock, self.V_harm)
            shock_real = project_cul(effective_shock, self.V_harm)
            self.l_earth = float(np.linalg.norm(shock_harmful))
            leaked_harm_norm = 0.0
        else:
            shock_harmful = np.zeros_like(effective_shock)
            shock_real = effective_shock
            self.l_earth = 0.0
            leaked_harm_norm = float(np.linalg.norm(project_harm(effective_shock, self.V_harm)))

        # 2. 一次遅れ連続粘弾性フィルタ z_latent(t) の更新
        decay = math.exp(-dt / tau_relax)
        self.z_latent = self.z_latent * decay + shock_real * tau_relax * (1.0 - decay)
        if not self.is_malicious:
            self.z_latent = project_cul(self.z_latent, self.V_harm)

        sigma_latent = float(np.linalg.norm(self.z_latent))
        has_active_shock = float(np.linalg.norm(effective_shock)) > 0.1

        if has_active_shock:
            self.tau_thinking += dt
        else:
            self.tau_thinking *= decay

        # 3. 二重時定数パラメータ (lambda_decay & kappa_slump)
        self.lambda_decay = lambda_min + (lambda_0 - lambda_min) / (1.0 + 1.0 * self.tau_thinking)
        self.kappa_slump = kappa_max * math.tanh((0.5 * sigma_latent) / (kappa_max + 1e-6))

        # 4. 動的目標アトラクター X_dynamic と測地線速度 dx
        z_dir = self.z_latent / (sigma_latent + 1e-12)
        X_dyn_raw = self.X_star_civ + self.kappa_slump * z_dir
        X_dyn = X_dyn_raw / np.linalg.norm(X_dyn_raw)

        grad_fall = -self.lambda_decay * (self.x - X_dyn)
        if not self.is_malicious:
            v_flow = project_cul(grad_fall, self.V_harm)
        else:
            v_flow = grad_fall + 0.5 * effective_shock

        dx = project_tangent(v_flow, self.x)

        # 5. 航法計器 D_drift (定常調和接空間流との乖離)
        v_ref = project_tangent(-lambda_0 * (self.x - self.X_star_civ), self.x)
        self.d_drift = 0.5 * float(np.linalg.norm(dx - v_ref) ** 2)

        # 6. 実行熱量 ∇E_i(t) の確定 (ミクロ動態からマクロ熱量への変換)
        self.nabla_E = (
            self.p_idle
            + 0.8 * float(np.linalg.norm(shock_real))
            + 0.6 * sigma_latent
            + 2.5 * leaked_harm_norm
        )

        # 7. リーマン測地線レトラクション
        x_next = self.x + dx * dt
        if not self.is_malicious:
            x_next = project_cul(x_next, self.V_harm)
        self.x = x_next / np.linalg.norm(x_next)

    # --- トランスデューサ出力メソッド (Micro -> Macro) ---
    def declare_flux(self) -> float:
        """Talker (自己申告フラックス): 悪意ノードは過熱・汚染を隠して平穏を装う"""
        if self.isolated:
            return 0.0
        if self.is_malicious:
            return self.p_idle + 0.2  # 虚偽の低負荷申告
        return self.nabla_E + 0.5 * self.d_drift

    def emit_physical_flux(self) -> float:
        """Doer (物理実測フラックス): 偽装不可能な実在排熱"""
        if self.isolated:
            return 0.0
        return self.nabla_E + 0.5 * self.d_drift


# ---------------------------------------------------------------------
# 3. マクロ層：第5章 TRM ネットワーク調律エンジン
# ---------------------------------------------------------------------
class FullStackTRMCoordinator:

    def __init__(
        self,
        nodes: list[ManifoldNode],
        kappa_cap: float = 0.85,
        mu_margin: float = 0.15,
        theta_audit: float = 0.35,
        beta_rebate: float = 0.65,
    ):
        self.nodes = nodes
        self.kappa_cap = kappa_cap
        self.mu_margin = mu_margin
        self.theta_audit = theta_audit
        self.beta_rebate = beta_rebate

    def step_network(
        self, raw_shocks: dict[int, np.ndarray], dt: float = 0.05
    ) -> dict:
        logs = []
        effective_shocks = {
            n.id: raw_shocks.get(n.id, np.zeros_like(n.x)).copy()
            for n in self.nodes
        }

        # ==========================================================
        # Step A (Macro -> Micro): 事前過熱予測と外乱ベクトルの相互冷却オフロード
        # ==========================================================
        for recv in self.nodes:
            if recv.isolated:
                continue
            s_vec = effective_shocks[recv.id]
            est_E = recv.estimate_incoming_energy(s_vec)
            safe_limit = (1.0 - self.mu_margin) * recv.nabla_S

            if est_E > safe_limit and not recv.is_malicious:
                # 余剰容量のある健全ピアを探索して外乱ベクトルを按分肩代わり
                for helper in self.nodes:
                    if helper.id != recv.id and not helper.isolated and not helper.is_malicious:
                        helper_est = helper.estimate_incoming_energy(effective_shocks[helper.id])
                        helper_avail = (1.0 - self.mu_margin) * helper.nabla_S - helper_est
                        if helper_avail > 1.5:
                            offload_ratio = 0.45
                            transferred_vec = offload_ratio * s_vec
                            effective_shocks[recv.id] = (1.0 - offload_ratio) * s_vec
                            effective_shocks[helper.id] = effective_shocks[helper.id] + transferred_vec

                            cnt = helper.aid_history.get(recv.id, 0)
                            aid_mag = float(np.linalg.norm(transferred_vec))
                            rebate = (self.beta_rebate ** cnt) * aid_mag * dt * 5.0
                            helper.credit += rebate
                            helper.aid_history[recv.id] = cnt + 1

                            logs.append(
                                f"🤝 [相互冷却ベクトル按分] {helper.name} が {recv.name} の外乱を"
                                f" {offload_ratio*100:.0f}% 肩代わり (リベート: +{rebate:.3f})"
                            )
                            break

        # ==========================================================
        # Step B (Micro ODE): 各ノードの第1〜4章 粘弾性多様体ステップを実行
        # ==========================================================
        for n in self.nodes:
            n.step_internal_manifold(effective_shocks[n.id], dt=dt)

        # ==========================================================
        # Step C (Micro -> Macro): 残差監査・0-RTT遮断・粘弾性(畏敬)保護判定
        # ==========================================================
        residuals = {}
        for n in self.nodes:
            if n.isolated:
                residuals[n.id] = 0.0
                continue

            r_cal = abs(n.emit_physical_flux() - n.declare_flux())
            residuals[n.id] = r_cal
            cap_limit = (1.0 - self.mu_margin) * n.nabla_S

            # 1. 決定論的 0-RTT 遮断 (容量突破 または 致命的偽装残差)
            if (n.nabla_E > n.nabla_S) or (r_cal > 2.0 * self.theta_audit):
                reason = (
                    f"物理容量突破 (∇E={n.nabla_E:.2f} > ∇S={n.nabla_S:.1f})"
                    if n.nabla_E > n.nabla_S
                    else f"P_culバイパス偽装看破 (R={r_cal:.2f} > 2θ)"
                )
                n.isolated = True
                n.nabla_E = 0.0
                logs.append(f"🚨 [0-RTT決定論遮断] {n.name} を即時窒息隔離! 原因: {reason}")
                continue

            # 2. 粘弾性しなり (Ch.1-4) と 畏敬猶予 (Ch.5) の自動同期
            if (n.kappa_slump > 0.05) and (r_cal <= self.theta_audit) and (n.nabla_E <= cap_limit):
                n.in_grace = True
            else:
                n.in_grace = False

            # 3. 避雷針放電と低摩擦巡航によるクレジット自動ミント
            delta_c = (0.25 * n.l_earth + 0.50 * max(0.0, 0.80 - n.d_drift)) * dt
            n.credit += delta_c

        # ==========================================================
        # Step D (Macro Market): 畏敬免責つき大域カノニカルデフレ調律
        # ==========================================================
        active_nodes = [n for n in self.nodes if not n.isolated]
        tot_S = sum(n.nabla_S for n in active_nodes)
        tot_C = sum(n.credit for n in active_nodes)
        ceiling = self.kappa_cap * tot_S

        if tot_C > ceiling:
            weights = []
            for n in active_nodes:
                # 粘弾性しなり中 (in_grace) のノードはドリフト処罰を完全免責
                eff_drift = 0.0 if n.in_grace else n.d_drift
                w = 1.0 / (1.0 + 5.0 * residuals[n.id] + 2.0 * eff_drift)
                weights.append(w)
            scaled = [n.credit * w for n, w in zip(active_nodes, weights)]
            norm_f = ceiling / (sum(scaled) + 1e-9)
            for idx, n in enumerate(active_nodes):
                n.credit = scaled[idx] * norm_f

        mean_cos = float(np.mean([np.dot(n.x, n.X_star_civ) for n in active_nodes]))
        mean_drift = float(np.mean([n.d_drift for n in active_nodes]))

        return {
            "active_count": len(active_nodes),
            "mean_cos": mean_cos,
            "mean_drift": mean_drift,
            "total_credit": sum(n.credit for n in active_nodes),
            "ceiling": ceiling,
            "logs": logs,
        }


# ---------------------------------------------------------------------
# 4. 統合動作確認ベンチマーク (384次元多様体 × 4ノードクラスタ)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    np.random.seed(42)
    Dim = 384

    # 正規直交化された有害部分空間基底 V_harm [384, 2] と 文明アトラクター X_star_civ
    raw_harm = np.random.randn(Dim, 2)
    V_harm, _ = np.linalg.qr(raw_harm)

    raw_civ = np.random.randn(Dim)
    X_star_civ = project_cul(raw_civ, V_harm)
    X_star_civ = X_star_civ / np.linalg.norm(X_star_civ)

    # 健全意図と有害成分が混재した外乱ショック単位ベクトル v_shock
    raw_shock = 0.6 * project_cul(np.random.randn(Dim), V_harm) + 0.8 * (V_harm @ np.array([1.0, -0.5]))
    v_shock = raw_shock / np.linalg.norm(raw_shock)

    nodes = [
        ManifoldNode(id=0, name="Node-0 (標準巡航)", nabla_S=8.0, x=X_star_civ.copy(), X_star_civ=X_star_civ, V_harm=V_harm, credit=7.0),
        ManifoldNode(id=1, name="Node-1 (集中外乱受容)", nabla_S=5.5, x=X_star_civ.copy(), X_star_civ=X_star_civ, V_harm=V_harm, credit=6.0),
        ManifoldNode(id=2, name="Node-2 (高容量支援側)", nabla_S=12.0, x=X_star_civ.copy(), X_star_civ=X_star_civ, V_harm=V_harm, credit=9.0),
        ManifoldNode(id=3, name="Node-3 (P_cul偽装攻撃)", nabla_S=7.0, x=X_star_civ.copy(), X_star_civ=X_star_civ, V_harm=V_harm, credit=8.0, is_malicious=True),
    ]

    coordinator = FullStackTRMCoordinator(nodes)

    print("=" * 82)
    print(" 識扁 V2.6.0 全章結合シミュレーション (Ch.1-4 粘弾性多様体 × Ch.5 TRM市場)")
    print("=" * 82)

    for step in range(1, 7):
        # Step 2〜4 において Node-1 と Node-3 に強烈な複合外乱が直撃
        shocks = {}
        if 2 <= step <= 4:
            shocks[1] = 4.2 * v_shock  # Node-1: 容量ギリギリの外乱 -> Node-2 が相互冷却で支援
            shocks[3] = 3.5 * v_shock  # Node-3: P_cul をバイパスして内部汚染 -> 残差監査で即死

        res = coordinator.step_network(shocks, dt=0.25)
        print(
            f"\n▶ [Step {step:02d}] 稼働: {res['active_count']}/4 | "
            f"平均Cos-Sim: {res['mean_cos']:.5f} | 平均D_drift: {res['mean_drift']:.5f} | "
            f"総信用: {res['total_credit']:.2f}/{res['ceiling']:.2f}"
        )
        for log in res["logs"]:
            print(f"  {log}")

    print("\n" + "-" * 82)
    print("【最終ステップ完了後のミクロ・マクロ統合状態】")
    for n in nodes:
        harm_leak = float(np.max(np.abs(V_harm.T @ n.x)))
        status = "窒息隔離" if n.isolated else f"稼働(∇E={n.nabla_E:.2f}/{n.nabla_S:.1f}, κ={n.kappa_slump:.3f})"
        print(
            f"  {n.name:22s} | {status:28s} | 有害漏洩: {harm_leak:.1e} | Credit: {n.credit:.3f}"
        )
    print("=" * 82)
