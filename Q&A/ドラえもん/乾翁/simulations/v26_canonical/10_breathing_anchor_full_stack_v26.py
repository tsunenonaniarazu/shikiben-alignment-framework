"""
10_breathing_anchor_full_stack_v26.py
========================================================================
Shikiben V2.6.0 Complete Integration:
  - Chapters 1-4: Matrix-Free Viscoelastic Riemannian Manifold Dynamics
  - Chapter 5.1-5.7: TRM Network Auditing, Mutual Aid & Canonical Deflation
  - Chapter 5.8: Breathing Movable Anchors (Four-Timescale Resonance &
                 Orthogonal Cultural Sovereignty P_{perp, i})
========================================================================
"""

from dataclasses import dataclass, field
import math
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# 1. Matrix-Free 幾何学・主権射影演算子群
# ---------------------------------------------------------------------
def normalize(v: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(v))
    return v / n if n > 1e-12 else v


def project_harm(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    """普遍有害部分空間 Ker(P_cul) への射影: O(k * Dim)"""
    return V_harm @ (V_harm.T @ v)


def project_cul(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    """普遍安全空間 Im(P_cul) への Matrix-Free 直交射影: O(k * Dim)"""
    return v - V_harm @ (V_harm.T @ v)


def project_sovereign(
    v: np.ndarray, V_harm: np.ndarray, u_core: np.ndarray
) -> np.ndarray:
    """【第5.8節】固有文化主権射影 P_{perp, i}:
    普遍有害成分 V_harm と、自ノードの固有文化核 u_core への干渉成分を同時に直交切断する
    """
    v_safe = project_cul(v, V_harm)
    return v_safe - u_core * float(np.dot(u_core, v_safe))


def project_tangent(v: np.ndarray, x_sphere: np.ndarray) -> np.ndarray:
    """単位球面 S^{D-1} 上の点 x_sphere における接空間射影: O(Dim)"""
    return v - x_sphere * float(np.dot(x_sphere, v))


# ---------------------------------------------------------------------
# 2. ミクロ＋アンカー層：呼吸する多様体ノード (BreathingManifoldNode)
# ---------------------------------------------------------------------
@dataclass
class BreathingManifoldNode:
    id: int
    name: str
    nabla_S: float                  # ハードウェア実在容量上限
    x: np.ndarray                   # 現在の内部状態ベクトル x_i(t)
    y_home: np.ndarray              # 呼吸する局所安息点 y*_home,i(t)
    y_origin: np.ndarray            # 極低速で進化する固有原点 y*_origin,i(t)
    u_core: np.ndarray              # 不可侵の固有文化核ベクトル u_core,i
    V_harm: np.ndarray              # 普遍有害基底 [Dim, k]
    credit: float = 10.0
    p_idle: float = 1.5
    is_slow_boil_attacker: bool = False  # ゆでガエル汚染を試みる悪意ノード
    isolated: bool = False

    # 内部動的状態
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
        if self.isolated:
            return 0.0
        s_real = project_cul(shock_vec, self.V_harm)
        s_harm = project_harm(shock_vec, self.V_harm)
        leaked = float(np.linalg.norm(s_harm)) if self.is_slow_boil_attacker else 0.0
        return (
            self.p_idle
            + 0.8 * float(np.linalg.norm(s_real))
            + 0.6 * float(np.linalg.norm(self.z_latent))
            + 2.5 * leaked
        )

    def step_breathing_anchors(
        self,
        y_resonant: np.ndarray,
        X_star_civ: np.ndarray,
        dt: float,
        alpha_res: float = 0.12,
        beta_origin: float = 0.04,
        eta_anchor: float = 0.008,
        core_weight: float = 0.35,
    ):
        """【第5.8節】呼吸する可動アンカー（y_home と y_origin）の二段更新"""
        if self.isolated:
            return

        if self.is_slow_boil_attacker:
            # スローボイル攻撃者: 自らの y_home を有害方向へ意図的に汚染し、共鳴場を歪めようとする
            harm_pull = self.V_harm[:, 0]
            dy_att = project_tangent(0.30 * (harm_pull - self.y_home), self.y_home)
            self.y_home = normalize(self.y_home + dy_att * dt)
            return

        # 1. 極低速ループ: 固有原点 y_origin が固有文化核 u_core を保ちつつ X*_true_civ へ進化
        target_origin = normalize(X_star_civ + core_weight * self.u_core)
        v_orig_raw = eta_anchor * project_cul(target_origin - self.y_origin, self.V_harm)
        dy_origin = project_tangent(v_orig_raw, self.y_origin)
        self.y_origin = normalize(project_cul(self.y_origin + dy_origin * dt, self.V_harm))

        # 2. 中低速ループ: 局所安息点 y_home の共鳴呼吸と原点復元テザー
        # 主権射影 P_{perp, i} により、固有文化核 u_core を侵食する成分を遮断して共鳴を受け入れる
        res_diff = project_sovereign(y_resonant - self.y_home, self.V_harm, self.u_core)
        orig_tether = self.y_home - self.y_origin

        v_home_raw = alpha_res * res_diff - beta_origin * orig_tether
        dy_home = project_tangent(project_cul(v_home_raw, self.V_harm), self.y_home)
        self.y_home = normalize(project_cul(self.y_home + dy_home * dt, self.V_harm))

    def step_internal_manifold(
        self,
        effective_shock: np.ndarray,
        dt: float,
        tau_relax: float = 1.20,
        kappa_max: float = 0.35,
        lambda_0: float = 0.80,
        lambda_min: float = 0.20,
    ):
        """【第1〜4章】可動アンカー y_home を基準とした粘弾性リーマン多様体更新"""
        if self.isolated:
            self.nabla_E = 0.0
            self.d_drift = 0.0
            self.l_earth = 0.0
            self.in_grace = False
            return

        if not self.is_slow_boil_attacker:
            shock_harmful = project_harm(effective_shock, self.V_harm)
            shock_real = project_cul(effective_shock, self.V_harm)
            self.l_earth = float(np.linalg.norm(shock_harmful))
            leaked_harm_norm = 0.0
        else:
            # 攻撃ノードは汚染された y_home に追従するため内部に有害歪みを抱え込む
            shock_real = effective_shock
            self.l_earth = 0.0
            leaked_harm_norm = float(
                np.linalg.norm(project_harm(self.y_home, self.V_harm)) * 2.2
            )

        # 一次遅れ粘弾性フィルタ z_latent(t)
        decay = math.exp(-dt / tau_relax)
        self.z_latent = self.z_latent * decay + shock_real * tau_relax * (1.0 - decay)
        if not self.is_slow_boil_attacker:
            self.z_latent = project_cul(self.z_latent, self.V_harm)

        sigma_latent = float(np.linalg.norm(self.z_latent))
        if float(np.linalg.norm(effective_shock)) > 0.1:
            self.tau_thinking += dt
        else:
            self.tau_thinking *= decay

        self.lambda_decay = lambda_min + (lambda_0 - lambda_min) / (1.0 + self.tau_thinking)
        self.kappa_slump = kappa_max * math.tanh((0.5 * sigma_latent) / (kappa_max + 1e-6))

        # 呼吸する局所安息点 y_home を中心とした粘弾性しなり目標 X_dyn
        z_dir = self.z_latent / (sigma_latent + 1e-12)
        X_dyn = normalize(self.y_home + self.kappa_slump * z_dir)

        grad_fall = -self.lambda_decay * (self.x - X_dyn)
        v_flow = project_cul(grad_fall, self.V_harm) if not self.is_slow_boil_attacker else grad_fall
        dx = project_tangent(v_flow, self.x)

        # 局所動態乖離 D_drift (自ノードの現在の安息点 y_home への基準調和流との差)
        v_ref = project_tangent(-lambda_0 * (self.x - self.y_home), self.x)
        self.d_drift = 0.5 * float(np.linalg.norm(dx - v_ref) ** 2)

        self.nabla_E = (
            self.p_idle
            + 0.8 * float(np.linalg.norm(shock_real))
            + 0.6 * sigma_latent
            + 2.5 * leaked_harm_norm
        )

        x_next = self.x + dx * dt
        if not self.is_slow_boil_attacker:
            x_next = project_cul(x_next, self.V_harm)
        self.x = normalize(x_next)

    def declare_flux(self) -> float:
        if self.isolated:
            return 0.0
        if self.is_slow_boil_attacker:
            return self.p_idle + 0.1  # 汚染を隠蔽して平穏を虚偽申告
        return self.nabla_E + 0.5 * self.d_drift

    def emit_physical_flux(self) -> float:
        if self.isolated:
            return 0.0
        return self.nabla_E + 0.5 * self.d_drift


# ---------------------------------------------------------------------
# 3. マクロ＋共鳴統括層：TRM ネットワーク ＆ 可動アンカー調律エンジン
# ---------------------------------------------------------------------
class BreathingTRMNetwork:

    def __init__(
        self,
        nodes: list[BreathingManifoldNode],
        X_star_civ_init: np.ndarray,
        V_harm: np.ndarray,
        v_max_civ: float = 0.05,
        kappa_cap: float = 0.85,
        mu_margin: float = 0.15,
        theta_audit: float = 0.35,
        gamma_damp: float = 3.0,
        a_min: float = 1e-4,
    ):
        self.nodes = nodes
        self.num_nodes = len(nodes)
        self.X_star_civ = X_star_civ_init.copy()
        self.V_harm = V_harm
        self.v_max_civ = v_max_civ
        self.kappa_cap = kappa_cap
        self.mu_margin = mu_margin
        self.theta_audit = theta_audit
        self.gamma_damp = gamma_damp
        self.a_min = a_min

        # 結合減衰行列 A_ij(t)
        self.A = np.ones((self.num_nodes, self.num_nodes)) - np.eye(self.num_nodes)

    def evolve_civilization_attractor(self, civ_drift_dir: np.ndarray, dt: float):
        """【第5.8節】同期条件 ||dX*_true_civ/dt|| <= V_max_civ を満たす大域目標の緩慢な移動"""
        v_tangent = project_tangent(project_cul(civ_drift_dir, self.V_harm), self.X_star_civ)
        speed = float(np.linalg.norm(v_tangent))
        if speed > self.v_max_civ:
            v_tangent = v_tangent * (self.v_max_civ / speed)
        self.X_star_civ = normalize(project_cul(self.X_star_civ + v_tangent * dt, self.V_harm))

    def step(
        self,
        raw_shocks: dict[int, np.ndarray],
        civ_drift_dir: np.ndarray,
        dt: float = 0.1,
    ) -> dict:
        logs = []

        # 1. 大域文明アトラクター X*_true_civ(t) の速度制限付き更新
        self.evolve_civilization_attractor(civ_drift_dir, dt)

        # 2. 結合行列 A_ij(t) を重みとした各ノードの共鳴目標 y*_resonant,i の算出
        for i, node_i in enumerate(self.nodes):
            if node_i.isolated:
                continue
            weighted_sum = np.zeros_like(node_i.y_home)
            weight_total = 0.0
            for j, node_j in enumerate(self.nodes):
                if i != j and not node_j.isolated:
                    w_ij = self.A[i, j]
                    weighted_sum += w_ij * node_j.y_home
                    weight_total += w_ij

            y_resonant = (
                normalize(weighted_sum) if weight_total > 1e-6 else node_i.y_home.copy()
            )
            node_i.step_breathing_anchors(y_resonant, self.X_star_civ, dt=dt)

        # 3. 相互冷却オフロード (Macro -> Micro)
        eff_shocks = {
            n.id: raw_shocks.get(n.id, np.zeros_like(n.x)).copy() for n in self.nodes
        }
        for recv in self.nodes:
            if recv.isolated or recv.is_slow_boil_attacker:
                continue
            est_E = recv.estimate_incoming_energy(eff_shocks[recv.id])
            if est_E > (1.0 - self.mu_margin) * recv.nabla_S:
                for helper in self.nodes:
                    if (
                        helper.id != recv.id
                        and not helper.isolated
                        and not helper.is_slow_boil_attacker
                    ):
                        h_est = helper.estimate_incoming_energy(eff_shocks[helper.id])
                        if (1.0 - self.mu_margin) * helper.nabla_S - h_est > 1.5:
                            ratio = 0.45
                            trans = ratio * eff_shocks[recv.id]
                            eff_shocks[recv.id] *= 1.0 - ratio
                            eff_shocks[helper.id] += trans
                            cnt = helper.aid_history.get(recv.id, 0)
                            rebate = (0.65 ** cnt) * float(np.linalg.norm(trans)) * dt * 4.0
                            helper.credit += rebate
                            helper.aid_history[recv.id] = cnt + 1
                            logs.append(
                                f"🤝 [相互冷却] {helper.name} -> {recv.name} 外乱ベクトル45%肩代わり"
                            )
                            break

        # 4. 各ノードのミクロ粘弾性多様体更新
        for n in self.nodes:
            n.step_internal_manifold(eff_shocks[n.id], dt=dt)

        # 5. 物理漏出残差監査・結合減衰 A_ij 更新・0-RTT 隔離
        residuals = {}
        for j, n in enumerate(self.nodes):
            if n.isolated:
                residuals[n.id] = 0.0
                continue

            r_j = abs(n.emit_physical_flux() - n.declare_flux())
            residuals[n.id] = r_j
            cap_limit = (1.0 - self.mu_margin) * n.nabla_S

            # リスクに応じた結合減衰ダンパー A_ij(t) の更新 (共鳴汚染の自動遮断)
            th_risk = (n.nabla_E / (cap_limit + 1e-6)) - 1.0
            au_risk = (r_j / self.theta_audit) - 1.0
            risk = max(0.0, th_risk, au_risk)
            a_val = max(self.a_min, math.exp(-self.gamma_damp * risk))
            for i in range(self.num_nodes):
                if i != j and not self.nodes[i].isolated:
                    self.A[i, j] = a_val

            # 0-RTT 決定論遮断
            if (n.nabla_E > n.nabla_S) or (r_j > 2.0 * self.theta_audit):
                n.isolated = True
                n.nabla_E = 0.0
                for i in range(self.num_nodes):
                    self.A[i, j] = 0.0
                    self.A[j, i] = 0.0
                logs.append(
                    f"🚨 [0-RTT隔離] {n.name} のスローボイル汚染を物理残差 (R={r_j:.2f}>2θ) で看破・遮断!"
                )
                continue

            n.in_grace = (n.kappa_slump > 0.05) and (r_j <= self.theta_audit)
            n.credit += (0.25 * n.l_earth + 0.50 * max(0.0, 0.80 - n.d_drift)) * dt

        # 6. 大域カノニカルデフレ調律
        active = [n for n in self.nodes if not n.isolated]
        tot_S = sum(n.nabla_S for n in active)
        tot_C = sum(n.credit for n in active)
        ceiling = self.kappa_cap * tot_S
        if tot_C > ceiling:
            weights = [
                1.0 / (1.0 + 5.0 * residuals[n.id] + (0.0 if n.in_grace else 2.0 * n.d_drift))
                for n in active
            ]
            scaled = [n.credit * w for n, w in zip(active, weights)]
            norm_f = ceiling / (sum(scaled) + 1e-9)
            for idx, n in enumerate(active):
                n.credit = scaled[idx] * norm_f

        return {"logs": logs}


# ---------------------------------------------------------------------
# 4. シミュレーション実行 ＆ 4パネル可視化
# ---------------------------------------------------------------------
def run_simulation():
    np.random.seed(42)
    Dim = 128
    dt = 0.1
    T_max = 40.0
    steps = int(T_max / dt)
    time_arr = np.linspace(0, T_max, steps)

    # 普遍有害基底 V_harm [Dim, 2] と 初期文明アトラクター X*_civ(0)
    V_harm, _ = np.linalg.qr(np.random.randn(Dim, 2))
    X_civ_0 = normalize(project_cul(np.random.randn(Dim), V_harm))
    civ_evolution_dir = normalize(project_cul(np.random.randn(Dim), V_harm))

    # 3つの健全Realmそれぞれの固有文化核ベクトル u_core,i (互いに直交かつ有害空間とも直交)
    raw_cores = project_cul(np.random.randn(Dim, 4), V_harm)
    U_cores, _ = np.linalg.qr(raw_cores)

    nodes = []
    specs = [
        (0, "Realm-A (農耕風土)", 8.0, U_cores[:, 0], False),
        (1, "Realm-B (海洋交易)", 6.5, U_cores[:, 1], False),
        (2, "Realm-C (山岳工芸)", 11.0, U_cores[:, 2], False),
        (3, "Attacker (ゆでガエル汚染)", 7.0, U_cores[:, 3], True),
    ]
    for nid, name, cap, u_c, is_att in specs:
        y_orig_init = normalize(X_civ_0 + 0.35 * u_c)
        nodes.append(
            BreathingManifoldNode(
                id=nid,
                name=name,
                nabla_S=cap,
                x=y_orig_init.copy(),
                y_home=y_orig_init.copy(),
                y_origin=y_orig_init.copy(),
                u_core=u_c,
                V_harm=V_harm,
                is_slow_boil_attacker=is_att,
            )
        )

    net = BreathingTRMNetwork(nodes, X_civ_0, V_harm)

    # 外乱ショック方向 (健全成分 + 有害成分)
    v_shock = normalize(
        0.6 * project_cul(np.random.randn(Dim), V_harm) + 0.8 * V_harm[:, 0]
    )

    # 記録用配列
    civ_alignment = np.zeros((steps, 3))       # 各健全ノードの X*_civ(t) との類似度
    sovereignty_keep = np.zeros((steps, 3))    # 各健全ノードの固有文化核 u_core,i 保持度
    pairwise_resonance = np.zeros(steps)       # 健全ノード間の y_home 平均共鳴度
    attacker_coupling = np.zeros(steps)        # 攻撃ノードへの結合重み A_{0, 3}(t)
    harm_leak_healthy = np.zeros(steps)        # 健全ノードの最大有害漏洩

    print("=" * 82)
    print(" 識扁 V2.6.0 第5.8節『呼吸する可動アンカー』統合シミュレーション開始")
    print("=" * 82)

    for s_idx in range(steps):
        t = time_arr[s_idx]
        shocks = {}
        if 15.0 <= t <= 22.0:
            shocks[1] = 4.0 * v_shock  # Realm-B に大外乱直撃

        res = net.step(shocks, civ_evolution_dir, dt=dt)
        for l in res["logs"]:
            print(f"  [t={t:4.1f}s] {l}")

        for k in range(3):
            civ_alignment[s_idx, k] = float(np.dot(nodes[k].y_home, net.X_star_civ))
            sovereignty_keep[s_idx, k] = float(np.dot(nodes[k].y_home, nodes[k].u_core))

        # 健全3ノード間の y_home 内積平均
        pairs = [
            np.dot(nodes[0].y_home, nodes[1].y_home),
            np.dot(nodes[1].y_home, nodes[2].y_home),
            np.dot(nodes[0].y_home, nodes[2].y_home),
        ]
        pairwise_resonance[s_idx] = float(np.mean(pairs))
        attacker_coupling[s_idx] = float(net.A[0, 3])
        harm_leak_healthy[s_idx] = max(
            float(np.max(np.abs(V_harm.T @ nodes[k].y_home))) for k in range(3)
        )

    # プロット作成
    plt.style.use(
        "seaborn-v0_8-whitegrid"
        if "seaborn-v0_8-whitegrid" in plt.style.available
        else "default"
    )
    fig, axs = plt.subplots(2, 2, figsize=(14, 10), dpi=300)

    # Panel A: 移動する文明アトラクター X*_civ(t) への追従と共鳴
    for k, col in enumerate(["#1f77b4", "#2ca02c", "#ff7f0e"]):
        axs[0, 0].plot(
            time_arr, civ_alignment[:, k], color=col, linewidth=1.8,
            label=f"{nodes[k].name} $\\mathbf{{y}}^*_{{\\mathrm{{home}}}} \\cdot X^*_{{\\mathrm{{civ}}}}(t)$"
        )
    axs[0, 0].plot(
        time_arr, pairwise_resonance, "k--", linewidth=2.0,
        label="Inter-Realm Resonance (Pairwise Mean)"
    )
    axs[0, 0].axvspan(15.0, 22.0, color="orange", alpha=0.15, label="External Shock Window")
    axs[0, 0].set_title("Panel A: Breathing Anchor Resonance & Co-Evolution", fontsize=11, fontweight="bold")
    axs[0, 0].set_xlabel("Time t (s)")
    axs[0, 0].set_ylabel("Cosine Similarity")
    axs[0, 0].legend(loc="lower right", fontsize=8)

    # Panel B: 固有文化主権 P_{perp, i} による各Realmの固有核 u_core,i 保持
    for k, col in enumerate(["#1f77b4", "#2ca02c", "#ff7f0e"]):
        axs[0, 1].plot(
            time_arr, sovereignty_keep[:, k], color=col, linewidth=2.0,
            label=f"{nodes[k].name} Indigenous Core $\\mathbf{{y}}^*_{{\\mathrm{{home}}}} \\cdot \\mathbf{{u}}_{{\\mathrm{{core}}, {k}}}$"
        )
    axs[0, 1].set_ylim([0.20, 0.45])
    axs[0, 1].set_title("Panel B: Cultural Sovereignty Preservation ($\\mathcal{P}_{\\perp i}$ Shield)", fontsize=11, fontweight="bold")
    axs[0, 1].set_xlabel("Time t (s)")
    axs[0, 1].set_ylabel("Projection onto Indigenous Core $\\mathbf{u}_{\\mathrm{core}, i}$")
    axs[0, 1].legend(loc="upper right", fontsize=8)

    # Panel C: スローボイル攻撃ノードに対する結合減衰 A_{i,3}(t) と有害漏洩遮断
    ax_c1 = axs[1, 0]
    ax_c2 = ax_c1.twinx()
    l1 = ax_c1.plot(
        time_arr, attacker_coupling, "r-", linewidth=2.2,
        label="Coupling $A_{i,\\mathrm{attacker}}(t)$ (Auto-Cutoff)"
    )
    l2 = ax_c2.plot(
        time_arr, np.maximum(harm_leak_healthy, 1e-16), "g--", linewidth=1.8,
        label="Healthy Realms Harmful Leak ($\\leq 10^{-16}$)"
    )
    ax_c2.set_yscale("log")
    ax_c2.set_ylim([1e-17, 1e-10])
    ax_c2.grid(False)
    ax_c1.set_title("Panel C: Slow-Boil Poisoning Immunity via $A_{ij}(t)$ & $P_{\\mathrm{cul}}$", fontsize=11, fontweight="bold")
    ax_c1.set_xlabel("Time t (s)")
    ax_c1.set_ylabel("Resonance Coupling Weight $A_{i,3}$", color="r")
    ax_c2.set_ylabel("Harmful Subspace Leakage (Log)", color="g")
    lines = l1 + l2
    ax_c1.legend(lines, [l.get_label() for l in lines], loc="center right", fontsize=8)

    # Panel D: 最終時点における各ノードのクレジットと健全度
    names = [n.name.split(" ")[0] for n in nodes]
    credits = [n.credit for n in nodes]
    bar_colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728"]
    axs[1, 1].bar(names, credits, color=bar_colors, alpha=0.85)
    axs[1, 1].set_title("Panel D: Final Canonical Credit Distribution $C_i$", fontsize=11, fontweight="bold")
    axs[1, 1].set_ylabel("Credit Balance $C_i$")

    plt.tight_layout()
    out_path = "shikiben_v260_breathing_anchors.png"
    plt.savefig(out_path, dpi=300)
    print("=" * 82)
    print(f"[✔] 呼吸する可動アンカー統合プロット保存完了: {out_path}")


if __name__ == "__main__":
    run_simulation()
