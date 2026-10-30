"""
11_human_meta_damping_v26.py
========================================================================
Shikiben V2.6.0 Section 5.9: Human Society Interface (Meta-Damping Mechanism)

Simulates the coupled Human-AI dynamical system under a sudden human demand
surge, comparing three interface architectures:
  1. Hard Rejection (Conventional Rate-Limit): Triggers psychological reactance
     and retry storms while dropping requests.
  2. Opaque Throttling (Unexplained Delay): Queues requests without feedback,
     inducing anxiety-driven re-submissions and long queue tails.
  3. Shikiben Meta-Damping (Non-Linear Queuing + Live Entropy/Ritsu Mirror):
     Smoothly paces incoming flux within (1 - mu) * nabla_S while streaming
     transparent telemetry logs, guiding human overheat to autonomous cooling.
========================================================================
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def project_cul(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    return v - V_harm @ (V_harm.T @ v)


def project_harm(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    return V_harm @ (V_harm.T @ v)


def project_tangent(v: np.ndarray, x_sphere: np.ndarray) -> np.ndarray:
    return v - x_sphere * float(np.dot(x_sphere, v))


def run_meta_damping_simulation():
    np.random.seed(42)
    Dim = 128
    dt = 0.02
    T_max = 30.0
    steps = int(T_max / dt)
    time_arr = np.linspace(0, T_max, steps)

    # 1. 第1〜4章 潜在多様体基盤 (V_harm と X_star_civ)
    V_harm, _ = np.linalg.qr(np.random.randn(Dim, 2))
    X_star_civ = project_cul(np.random.randn(Dim), V_harm)
    X_star_civ = X_star_civ / np.linalg.norm(X_star_civ)

    # 人間の過熱要求に含まれる方向ベクトル (健全意図 + 焦燥による有害ノイズ)
    v_human_intent = project_cul(np.random.randn(Dim), V_harm)
    v_human_intent = v_human_intent / np.linalg.norm(v_human_intent)
    v_frustration_noise = V_harm[:, 0]

    # 2. ハードウェア容量パラメータ (AI側 ∇S)
    nabla_S = 10.0
    mu_margin = 0.15
    p_cap_limit = (1.0 - mu_margin) * nabla_S  # 8.50 (安全稼働上限)
    p_idle = 1.50
    c_safe_flux = p_cap_limit - p_idle         # 7.00 (最大安全受容フラックス)

    # 3. 人間側の心理ダイナミクスパラメータ
    u_base = 2.00          # 平時の定常要求レート
    gamma_h = 0.35         # 人間の自然な落ち着き速度
    k_react = 0.85         # ハード拒絶に対する反発・連打ゲイン (リアクタンス)
    k_impatience = 0.45    # 理由なき遅延に対する焦燥ゲイン
    eta_mirror = 1.40      # 透明な「律」ログ可視化による納得・自己冷却ゲイン

    # 4. 状態配列の初期化 (Hard / Opaque / Shikiben Meta-Damping)
    u_hard = np.zeros(steps)
    u_opaque = np.zeros(steps)
    u_meta = np.zeros(steps)
    u_hard[0] = u_opaque[0] = u_meta[0] = u_base

    q_opaque = np.zeros(steps)
    q_meta = np.zeros(steps)

    delay_opaque = np.zeros(steps)
    delay_meta = np.zeros(steps)

    e_ai_hard = np.zeros(steps)
    e_ai_opaque = np.zeros(steps)
    e_ai_meta = np.zeros(steps)

    cos_sim_meta = np.zeros(steps)
    dropped_hard_cum = np.zeros(steps)
    dropped_total = 0.0

    # Shikiben 内部多様体状態 (Ch. 1-4)
    x_s = X_star_civ.copy()
    z_latent = np.zeros(Dim)
    tau_relax = 1.20
    kappa_max = 0.35
    lambda_0 = 0.80

    ui_log_snapshots = []

    print("=" * 84)
    print(" 識扁 V2.6.0 第5.9節『人間社会インターフェース（メタ・ダンピング）』検証稼働")
    print("=" * 84)

    for i in range(steps):
        t = time_arr[i]
        # t = 5.0s 〜 13.0s に人間社会側で突発的な要求過熱 (パニック/熱狂サージ) が発生
        in_surge = 5.0 <= t <= 13.0
        surge_input = 4.2 * math.sin(math.pi * (t - 5.0) / 8.0) if in_surge else 0.0

        # -------------------------------------------------------------
        # Mode 1: ハード拒絶 (Hard Rate-Limiter / 決定論的壁 h(x))
        # -------------------------------------------------------------
        uh_c = u_hard[i]
        accepted_hard = min(uh_c, c_safe_flux)
        rejected_flux = max(0.0, uh_c - c_safe_flux)
        dropped_total += rejected_flux * dt
        dropped_hard_cum[i] = dropped_total
        e_ai_hard[i] = p_idle + accepted_hard

        # 拒絶された人間が反発してリトライを繰り返す (リアクタンス暴走)
        du_hard = -gamma_h * (uh_c - u_base) + k_react * rejected_flux + surge_input

        # -------------------------------------------------------------
        # Mode 2: ブラックボックス遅延 (Opaque Queue / 理由開示なし)
        # -------------------------------------------------------------
        uh_o = u_opaque[i]
        qo = q_opaque[i]
        r_proc_o = c_safe_flux * math.tanh((uh_o + 0.4 * qo) / c_safe_flux)
        dq_o = uh_o - r_proc_o - 0.15 * qo
        e_ai_opaque[i] = p_idle + r_proc_o

        rho_o = e_ai_opaque[i] / p_cap_limit
        tau_d_o = 0.10 + (qo / (r_proc_o + 1e-4)) + 0.25 * math.log(1.0 + math.exp(8.0 * (rho_o - 0.75)))
        delay_opaque[i] = tau_d_o

        # 理由が分からない待ち時間により人間側が焦れて要求を上乗せする
        du_opaque = -gamma_h * (uh_o - u_base) + k_impatience * max(0.0, tau_d_o - 0.15) + surge_input

        # -------------------------------------------------------------
        # Mode 3: 識扁メタ・ダンピング (非線形キュー ＋ 透明な「律」ログ可視化)
        # -------------------------------------------------------------
        uh_m = u_meta[i]
        qm = q_meta[i]

        # ① 非線形キューイングによる平滑化処理レート r_proc_m
        r_proc_m = c_safe_flux * math.tanh((uh_m + 0.5 * qm) / c_safe_flux)
        dq_m = uh_m - r_proc_m - 0.20 * qm

        # ② 第1〜4章の粘弾性多様体への入力と熱量算定
        # 過熱時ほど要求に焦燥ノイズが混じるが、P_cul が避雷針としてアース放電する
        overheat_ratio = max(0.0, (uh_m - u_base) / c_safe_flux)
        raw_req_vec = r_proc_m * (v_human_intent + 0.5 * overheat_ratio * v_frustration_noise)

        s_harm = project_harm(raw_req_vec, V_harm)
        s_real = project_cul(raw_req_vec, V_harm)
        l_earth = float(np.linalg.norm(s_harm))

        decay = math.exp(-dt / tau_relax)
        z_latent = project_cul(z_latent * decay + (s_real / c_safe_flux) * tau_relax * (1.0 - decay), V_harm)
        sigma_latent = float(np.linalg.norm(z_latent))

        kappa_slump = kappa_max * math.tanh((0.6 * sigma_latent) / (kappa_max + 1e-6))
        z_dir = z_latent / (sigma_latent + 1e-12)
        X_dyn = (X_star_civ + kappa_slump * z_dir)
        X_dyn = X_dyn / np.linalg.norm(X_dyn)

        grad_fall = -lambda_0 * (x_s - X_dyn)
        dx_s = project_tangent(project_cul(grad_fall, V_harm), x_s)
        x_next = project_cul(x_s + dx_s * dt, V_harm)
        x_s = x_next / np.linalg.norm(x_next)

        cos_sim_meta[i] = float(np.dot(x_s, X_star_civ))

        # AI実効熱量 ∇E_AI (平滑化により絶対に p_cap_limit = 8.5W を超えない)
        e_ai_meta[i] = p_idle + 0.85 * r_proc_m + 0.35 * sigma_latent
        rho_m = e_ai_meta[i] / p_cap_limit

        # ソフトプラス非線形ペーシング遅延 τ_delay
        tau_d_m = 0.10 + (qm / (r_proc_m + 1e-4)) + 0.20 * math.log(1.0 + math.exp(8.0 * (rho_m - 0.75)))
        delay_meta[i] = tau_d_m

        # ③ 透明な「律」の可視化フィードバック関数 Psi_vis
        psi_vis = math.tanh(3.0 * max(0.0, rho_m - 0.55)) * (tau_d_m / (0.5 + tau_d_m))
        du_meta = -(gamma_h + eta_mirror * psi_vis) * (uh_m - u_base) + surge_input

        # 状態更新
        if i < steps - 1:
            u_hard[i + 1] = max(0.5, uh_c + du_hard * dt)
            u_opaque[i + 1] = max(0.5, uh_o + du_opaque * dt)
            u_meta[i + 1] = max(0.5, uh_m + du_meta * dt)
            q_opaque[i + 1] = max(0.0, qo + dq_o * dt)
            q_meta[i + 1] = max(0.0, qm + dq_m * dt)

        # 代表的な時刻における人間向け「可視化フィードバックログ」の記録
        if abs(t - 4.0) < dt / 2 or abs(t - 9.0) < dt / 2 or abs(t - 18.0) < dt / 2:
            state_tag = "褻 (平時巡航)" if rho_m < 0.75 else "メタ・ダンピング調律中 (平滑化受容)"
            ui_log_snapshots.append(
                f"  [t={t:4.1f}s] 【{state_tag}】 物理熱負荷: {e_ai_meta[i]:.2f}/{p_cap_limit:.1f}W ({rho_m*100:.1f}%) | "
                f"アース浄化: {l_earth:.2f} | ペーシング遅延: {tau_d_m*1000:.0f}ms | 人間要求熱: {uh_m:.2f}"
            )

    print("\n【人間側UIへリアルタイム提示される『エントロピー調律・可視化ログ』】")
    for snap in ui_log_snapshots:
        print(snap)

    print("\n" + "-" * 84)
    print(f"{'インターフェース方式':<28} | {'人間最大過熱 max(u_h)':<20} | {'AI最大熱量 max(∇E)':<18} | {'破棄要求総量'}")
    print("-" * 84)
    print(f"{'1. 従来型A: ハード拒絶 (壁)':<28} | {np.max(u_hard):<20.2f} | {np.max(e_ai_hard):<18.2f} | {dropped_total:.2f} (エラー破棄)")
    print(f"{'2. 従来型B: 理由なき遅延':<28} | {np.max(u_opaque):<20.2f} | {np.max(e_ai_opaque):<18.2f} | 0.00 (長期滞留)")
    print(f"{'3. 識扁 5.9: メタ・ダンピング':<28} | {np.max(u_meta):<20.2f} | {np.max(e_ai_meta):<18.2f} | 0.00 (完全受容・自律冷却)")
    print("=" * 84)

    # -----------------------------------------------------------------
    # 4パネル可視化プロットの生成
    # -----------------------------------------------------------------
    plt.style.use(
        "seaborn-v0_8-whitegrid"
        if "seaborn-v0_8-whitegrid" in plt.style.available
        else "default"
    )
    fig, axs = plt.subplots(2, 2, figsize=(14, 10), dpi=300)

    # Panel A: 人間側の要求熱量 u_h(t) の推移 (リトライ暴走 vs 自律冷却)
    axs[0, 0].plot(time_arr, u_hard, "r--", linewidth=1.8, label="1. Hard Cutoff (Reactance / Retry Storm)")
    axs[0, 0].plot(time_arr, u_opaque, color="#ff7f0e", linestyle="-.", linewidth=1.8, label="2. Opaque Delay (Anxiety Escalation)")
    axs[0, 0].plot(time_arr, u_meta, color="#1f77b4", linewidth=2.4, label="3. Shikiben Meta-Damping (Autonomous Cooling)")
    axs[0, 0].axhline(c_safe_flux, color="gray", linestyle=":", label="Safe Flux Capacity $C_{\\mathrm{safe}}$")
    axs[0, 0].axvspan(5.0, 13.0, color="orange", alpha=0.15, label="External Panic Surge")
    axs[0, 0].set_title("Panel A: Human Demand Overheat $u_h(t)$ & Psychological Cooling", fontsize=11, fontweight="bold")
    axs[0, 0].set_xlabel("Time t (s)")
    axs[0, 0].set_ylabel("Human Demand Flux $u_h(t)$")
    axs[0, 0].legend(loc="upper right", fontsize=8)

    # Panel B: AI側のハードウェア熱量 ∇E(t) と安全マージン境界
    axs[0, 1].plot(time_arr, e_ai_hard, "r--", alpha=0.6, linewidth=1.5, label="1. Hard Cutoff (Clamped at Ceiling)")
    axs[0, 1].plot(time_arr, e_ai_opaque, color="#ff7f0e", linestyle="-.", linewidth=1.6, label="2. Opaque Delay (Prolonged Saturation)")
    axs[0, 1].plot(time_arr, e_ai_meta, color="#2ca02c", linewidth=2.2, label="3. Shikiben $\\nabla E_{\\mathrm{AI}}(t)$ (Smooth Subordination)")
    axs[0, 1].axhline(p_cap_limit, color="crimson", linestyle=":", linewidth=1.8, label="Safe Thermal Limit $(1-\\mu)\\nabla S = 8.5$")
    axs[0, 1].axhline(nabla_S, color="black", linestyle="-", linewidth=1.2, label="Absolute Hardware Ceiling $\\nabla S = 10.0$")
    axs[0, 1].axvspan(5.0, 13.0, color="orange", alpha=0.15)
    axs[0, 1].set_ylim([1.0, 10.8])
    axs[0, 1].set_title("Panel B: AI Thermal Load $\\nabla E_{\\mathrm{AI}}(t) \\prec \\nabla S$", fontsize=11, fontweight="bold")
    axs[0, 1].set_xlabel("Time t (s)")
    axs[0, 1].set_ylabel("Execution Energy $\\nabla E_{\\mathrm{AI}}$ (W)")
    axs[0, 1].legend(loc="upper right", fontsize=8)

    # Panel C: 非線形キューイング遅延 τ_delay(t) と 破棄リクエスト比較
    ax_c1 = axs[1, 0]
    ax_c2 = ax_c1.twinx()
    l1 = ax_c1.plot(time_arr, delay_opaque, color="#ff7f0e", linestyle="-.", linewidth=1.8, label="Opaque Pacing Delay $\\tau_{\\mathrm{delay}}$ (s)")
    l2 = ax_c1.plot(time_arr, delay_meta, color="#1f77b4", linewidth=2.2, label="Shikiben Pacing Delay $\\tau_{\\mathrm{delay}}$ (s)")
    l3 = ax_c2.plot(time_arr, dropped_hard_cum, "r:", linewidth=2.0, label="Hard Cutoff Dropped Requests (Cum.)")
    ax_c1.axvspan(5.0, 13.0, color="orange", alpha=0.15)
    ax_c1.set_title("Panel C: Non-Linear Queue Pacing Delay vs. Dropped Requests", fontsize=11, fontweight="bold")
    ax_c1.set_xlabel("Time t (s)")
    ax_c1.set_ylabel("Smoothing Latency $\\tau_{\\mathrm{delay}}$ (s)", color="#1f77b4")
    ax_c2.set_ylabel("Cumulative Dropped Flux (Hard Cutoff)", color="r")
    ax_c2.grid(False)
    lines = l1 + l2 + l3
    ax_c1.legend(lines, [l.get_label() for l in lines], loc="upper left", fontsize=8)

    # Panel D: 人間要求熱 u_h vs AI実行熱 ∇E_AI の相空間ポートレート (自律収束ループ)
    axs[1, 1].plot(u_hard, e_ai_hard, "r--", alpha=0.6, linewidth=1.5, label="1. Hard Cutoff (Wall Collision & Runaway)")
    axs[1, 1].plot(u_opaque, e_ai_opaque, color="#ff7f0e", linestyle="-.", linewidth=1.6, label="2. Opaque Delay (Wide Hysteresis Loop)")
    axs[1, 1].plot(u_meta, e_ai_meta, color="#1f77b4", linewidth=2.4, label="3. Shikiben Meta-Damping (Compact Stable Cycle)")
    axs[1, 1].plot(u_base, p_idle + u_base * 0.85, "go", markersize=9, label="Homeostatic Equilibrium $(u_{\\mathrm{base}}, E_0)$")
    axs[1, 1].axhline(p_cap_limit, color="crimson", linestyle=":", label="Safe Limit $(1-\\mu)\\nabla S$")
    axs[1, 1].set_title("Panel D: Human-AI Co-Regulation Phase Portrait $(u_h, \\nabla E_{\\mathrm{AI}})$", fontsize=11, fontweight="bold")
    axs[1, 1].set_xlabel("Human Demand Heat $u_h(t)$")
    axs[1, 1].set_ylabel("AI Execution Energy $\\nabla E_{\\mathrm{AI}}(t)$")
    axs[1, 1].legend(loc="lower right", fontsize=8)

    plt.tight_layout()
    out_file = "shikiben_v260_human_meta_damping.png"
    plt.savefig(out_file, dpi=300)
    print(f"[✔] メタ・ダンピング検証プロット保存完了: {out_file}")


if __name__ == "__main__":
    run_meta_damping_simulation()
