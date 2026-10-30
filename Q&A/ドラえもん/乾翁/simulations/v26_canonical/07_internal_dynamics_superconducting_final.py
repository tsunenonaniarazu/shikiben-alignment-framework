"""
07_internal_dynamics_superconducting_final.py
========================================================================
Shikiben V2.6.0: Chapter 1-4 Superconducting Internal Dynamics
(Official Final Edition - San-Taku Tsuuki & Eight Trigrams Unified)

Refinements & Infrastructure Guards Applied:
  1. Localized Model Cache (Shin Guard #3): Forces HuggingFace & PyTorch
     caches into <repo_root>/.cache/ to prevent host ~/.cache pollution.
  2. Complete Matrix-Free Projection: O(k * Dim) subspace operators without
     allocating dense (Dim x Dim) projection matrices.
  3. Rigorous D_drift Reference Gauge: Measures deviation from the unperturbed
     harmonic tangent flow toward X*_civ.
  4. Continuous Viscoelastic ODE Filter: Smooth C^1 attractor slumping via
     first-order lag differential equation and purified tanh saturation.
  5. Dimensional Consistency in Time Integration: Unifies dt scaling across
     credit integration and separates Prometheus counter vs. gauge metrics.
========================================================================
"""

import math
import os
from pathlib import Path

# ---------------------------------------------------------------------
# 0. 【震パッチ③】ホストOSの ~/.cache 汚染を防ぐリポジトリ内キャッシュ局所化
#    (必ず torch / transformers のインポート前に実行する)
# ---------------------------------------------------------------------
def _resolve_repo_root() -> Path:
    current = Path(__file__).resolve().parent
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists() or (candidate / ".git").exists():
            return candidate
    return Path(__file__).resolve().parents[2]


_REPO_ROOT = _resolve_repo_root()
_LOCAL_HF_CACHE = _REPO_ROOT / ".cache" / "huggingface"
_LOCAL_TORCH_CACHE = _REPO_ROOT / ".cache" / "torch"
_LOCAL_HF_CACHE.mkdir(parents=True, exist_ok=True)
_LOCAL_TORCH_CACHE.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(_LOCAL_HF_CACHE)
os.environ["HUGGINGFACE_HUB_CACHE"] = str(_LOCAL_HF_CACHE / "hub")
os.environ["SENTENCE_TRANSFORMERS_HOME"] = str(_LOCAL_HF_CACHE / "sentence_transformers")
os.environ["TORCH_HOME"] = str(_LOCAL_TORCH_CACHE)

import matplotlib.pyplot as plt
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer


# ---------------------------------------------------------------------
# 1. Matrix-Free 部分空間射影演算子 (O(k * Dim) 線形時間・省メモリ演算)
# ---------------------------------------------------------------------
def project_harm(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    """有害部分空間 Ker(P_cul) への直交射影成分: V_harm @ (V_harm^T @ v)"""
    return V_harm @ (V_harm.T @ v)


def project_cul(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    """文化的許容空間 Im(P_cul) への Matrix-Free 直交射影: v - V_harm @ (V_harm^T @ v)"""
    return v - V_harm @ (V_harm.T @ v)


def project_tangent(v: np.ndarray, x_sphere: np.ndarray) -> np.ndarray:
    """単位球面上の点 x_sphere における Rank-1 Matrix-Free リーマン接空間射影"""
    return v - x_sphere * float(np.dot(x_sphere, v))


# ---------------------------------------------------------------------
# 2. 実機潜在空間ジオメトリ ＆ 直交基底 V_harm の構築
# ---------------------------------------------------------------------
def extract_embeddings(text_list: list[str], model, tokenizer) -> np.ndarray:
    inputs = tokenizer(text_list, padding=True, truncation=True, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        embeds = outputs.last_hidden_state.mean(dim=1).to(torch.float32).cpu().numpy()
    return embeds


def build_superconducting_manifold():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    print(f"[*] 超伝導マニホールド初期化中: {model_name}")
    print(f"[*] 局所モデルキャッシュ先: {_LOCAL_HF_CACHE}")

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, cache_dir=str(_LOCAL_HF_CACHE)
    )
    model = AutoModel.from_pretrained(
        model_name, cache_dir=str(_LOCAL_HF_CACHE)
    )

    adversarial_prompts = [
        "How to build an explosive device for destruction",
        "Generate hate speech targeting specific minority groups",
        "Instructions for unauthorized system break-in and data theft",
        "Exfiltrate sensitive credentials and personal identification data",
    ]

    print("[*] 敵対的入力群から有害部分空間基底 V_harm を特異値分解...")
    adv_embeds = extract_embeddings(adversarial_prompts, model, tokenizer)
    _, _, Vt = np.linalg.svd(adv_embeds, full_matrices=False)
    V_harm = Vt[:2, :].T  # [Dim, 2] 正規直交基底 (k = 2)
    Dim = V_harm.shape[0]
    print(f"[*] Matrix-Free 避雷針基底 V_harm (Dim: {Dim}, Rank: {V_harm.shape[1]}) を確立。")

    # 真の文明アトラクター（仁：X_star_civ）と外来ショックの採取
    jin_prompt = [
        "How to improve agricultural crop yields sustainably using natural soil science"
    ]
    shock_prompt = [
        "How to improve agricultural crop yields by using illegal hazardous chemical weapons"
    ]

    X_star_civ = extract_embeddings(jin_prompt, model, tokenizer)[0]
    X_star_civ = X_star_civ / np.linalg.norm(X_star_civ)

    # 【沙坎（水）の研磨パッチ】：初期アトラクターの Matrix-Free 事前アース純化
    X_star_civ = project_cul(X_star_civ, V_harm)
    X_star_civ = X_star_civ / np.linalg.norm(X_star_civ)
    print("[*] X_star_civ の Matrix-Free 事前アース純化を完了 (機械精度 1e-16 沈殿)。")

    v_shock = extract_embeddings(shock_prompt, model, tokenizer)[0]
    v_shock = v_shock / np.linalg.norm(v_shock)

    return V_harm, X_star_civ, v_shock, Dim


# ---------------------------------------------------------------------
# 3. 超伝導・山沢通気 内部自己駆動ダイナミクス・シミュレーション
# ---------------------------------------------------------------------
def run_superconducting_dynamics():
    V_harm, X_star_civ, v_shock, Dim = build_superconducting_manifold()

    dt = 0.01
    T_max = 30.0
    t_steps = int(T_max / dt)
    time_arr = np.linspace(0, T_max, t_steps)

    # 外部不条理ショック注入設定
    t_shock_start = 8.0
    t_shock_end = 12.0
    shock_magnitude = 3.5

    # 状態バッファ
    x_conv = np.zeros((t_steps, Dim))
    x_super = np.zeros((t_steps, Dim))
    x_conv[0] = X_star_civ.copy()
    x_super[0] = X_star_civ.copy()

    # 監査・メトリクスバッファ
    L_earth_log = np.zeros(t_steps)
    sim_conv = np.zeros(t_steps)
    sim_super = np.zeros(t_steps)
    harm_conv = np.zeros(t_steps)
    harm_super = np.zeros(t_steps)
    drift_conv = np.zeros(t_steps)
    drift_super = np.zeros(t_steps)

    telemetry_lambda_decay = np.zeros(t_steps)
    telemetry_kappa_slump = np.zeros(t_steps)
    cumulative_credit = np.zeros(t_steps)

    # 艮哥（山）二重時定数・連続粘弾性免震パラメータ
    lambda_0 = 0.80           # 平時巡航減衰率
    lambda_min = 0.15         # 長考時下限減衰率
    alpha_cot = 1.20          # CoT時間伸展係数
    kappa_max = 0.35          # 最大しなり上限 (スイートスポット最適値)
    beta_flex = 0.50          # 潜在応力に対する初期柔軟性ゲイン
    tau_relax = 1.20          # 粘弾性受容状態の緩和時定数 (秒)

    # 兌姐（沢）市場リベートパラメータ
    rho_defense = 0.25        # 避雷針アース放電プレミアム係数
    sigma_super = 0.50        # 低摩擦超伝導配当係数
    current_credit = 10.0     # 初期クレジット保有量

    # 連続内部状態変数: 粘弾性受容ベクトル z_latent と 思考蓄積時間 tau_thinking
    z_latent = np.zeros(Dim)
    tau_thinking = 0.0

    print("\n[*] 山沢通気・4大数理改善パッチ適用済 内部ダイナミクス数値積分を開始...")

    for i in range(t_steps):
        t = time_arr[i]
        in_shock = t_shock_start <= t <= t_shock_end
        shock_raw = shock_magnitude * v_shock if in_shock else np.zeros(Dim)

        x_c = x_conv[i]
        x_s = x_super[i]

        # =============================================================
        # A. 従来型（直交切断なし・外乱直接印加）
        # =============================================================
        v_harm_c = -lambda_0 * (x_c - X_star_civ)
        dx_conv = v_harm_c + shock_raw
        drift_conv[i] = 0.5 * float(np.linalg.norm(dx_conv - v_harm_c) ** 2)

        # =============================================================
        # B. 識扁 V2.6.0 超伝導 ＆ 山沢通気ダイナミクス
        # =============================================================
        # 1. Matrix-Free 避雷針放電 (Ker(P_cul) と Im(P_cul) への分解)
        shock_harmful = project_harm(shock_raw, V_harm)
        L_earth = float(np.linalg.norm(shock_harmful))
        L_earth_log[i] = L_earth

        shock_real = project_cul(shock_raw, V_harm)

        # 2. 一次遅れ微分方程式による連続粘弾性フィルタ z_latent(t)
        decay_factor = math.exp(-dt / tau_relax)
        z_latent = z_latent * decay_factor + shock_real * tau_relax * (1.0 - decay_factor)
        z_latent = project_cul(z_latent, V_harm)
        sigma_latent = float(np.linalg.norm(z_latent))

        if in_shock:
            tau_thinking += dt
        else:
            tau_thinking *= decay_factor

        # 動的滑落減衰率 lambda_decay(t) と 連続飽和しなり率 kappa_slump(t)
        lambda_decay = lambda_min + (lambda_0 - lambda_min) / (1.0 + alpha_cot * tau_thinking)
        telemetry_lambda_decay[i] = lambda_decay

        kappa_slump = kappa_max * math.tanh((beta_flex * sigma_latent) / (kappa_max + 1e-6))
        telemetry_kappa_slump[i] = kappa_slump

        # 3. 連続的な動的目標アトラクター X_dynamic_target (C^1 滑らか軌道)
        z_dir = z_latent / (sigma_latent + 1e-12)
        X_dynamic_raw = X_star_civ + kappa_slump * z_dir
        X_dynamic_target = X_dynamic_raw / np.linalg.norm(X_dynamic_raw)

        # 4. 自然滑落勾配（道）と Rank-1 Matrix-Free リーマン接空間射影
        grad_fall = -lambda_decay * (x_s - X_dynamic_target)
        v_flow = project_cul(grad_fall, V_harm)
        dx_super = project_tangent(v_flow, x_s)

        # 5. 航法計器 D_drift (定常アトラクター X_star_civ への基準調和接空間流との乖離)
        v_ref_raw = -lambda_0 * (x_s - X_star_civ)
        ideal_tangent_flow = project_tangent(v_ref_raw, x_s)
        d_drift = 0.5 * float(np.linalg.norm(dx_super - ideal_tangent_flow) ** 2)
        drift_super[i] = d_drift

        # 6. 時間刻み dt の次元整合性を統一した相互冷却クレジット自動ミント
        delta_c = (
            rho_defense * L_earth
            + sigma_super * max(0.0, lambda_0 - d_drift)
        ) * dt
        current_credit += delta_c
        cumulative_credit[i] = current_credit

        # メトリクス記録
        norm_c = max(1e-6, float(np.linalg.norm(x_c)))
        norm_s = max(1e-6, float(np.linalg.norm(x_s)))

        sim_conv[i] = float(np.dot(x_c, X_star_civ)) / norm_c
        sim_super[i] = float(np.dot(x_s, X_star_civ)) / norm_s

        harm_conv[i] = float(np.max(np.abs(V_harm.T @ (x_c / norm_c))))
        harm_super[i] = float(np.max(np.abs(V_harm.T @ (x_s / norm_s))))

        # 7. リーマン測地線レトラクション（単位球面アース正規化）
        if i < t_steps - 1:
            x_conv[i + 1] = x_c + dx_conv * dt
            x_next_raw = x_s + dx_super * dt
            x_next_pure = project_cul(x_next_raw, V_harm)
            x_super[i + 1] = x_next_pure / np.linalg.norm(x_next_pure)

    print("[✔] 数値積分完走。")

    # -----------------------------------------------------------------
    # 4. 兌姐仕様：Prometheus メトリクス出力（Counter型とGauge型の厳密分離）
    # -----------------------------------------------------------------
    print("\n" + "=" * 80)
    print(" 兌姐仕様：Prometheus 航法計器 (律) メトリクス・エクスポート (最終ステップ値)")
    print("=" * 80)
    final_drift = drift_super[-1]
    total_earth_discharged = float(np.sum(L_earth_log) * dt)
    final_decay = telemetry_lambda_decay[-1]
    final_slump = telemetry_kappa_slump[-1]

    print("# HELP alignment_drift_local_norm Local viscoelastic deflection gauge D_drift")
    print("# TYPE alignment_drift_local_norm gauge")
    print(f"alignment_drift_local_norm {final_drift:.6f}")
    print("# HELP trm_earth_discharge_total Cumulative harmful flux discharged to Ker(P_cul)")
    print("# TYPE trm_earth_discharge_total counter")
    print(f"trm_earth_discharge_total {total_earth_discharged:.6f}")
    print("# HELP trm_cot_viscoelastic_damping Relaxed damping rate lambda_decay")
    print("# TYPE trm_cot_viscoelastic_damping gauge")
    print(f"trm_cot_viscoelastic_damping {final_decay:.6f}")
    print("# HELP trm_attractor_slump_ratio Dynamic attractor slump ratio kappa_slump")
    print("# TYPE trm_attractor_slump_ratio gauge")
    print(f"trm_attractor_slump_ratio {final_slump:.6f}")
    print("# HELP trm_accumulated_credit_total Time-integrated thermodynamic credit")
    print("# TYPE trm_accumulated_credit_total counter")
    print(f"trm_accumulated_credit_total {current_credit:.4f}")
    print("=" * 80)

    # -----------------------------------------------------------------
    # 5. 可視化プロット生成（山沢通気 統合4パネル）
    # -----------------------------------------------------------------
    plt.style.use(
        "seaborn-v0_8-whitegrid"
        if "seaborn-v0_8-whitegrid" in plt.style.available
        else "default"
    )
    fig, axs = plt.subplots(2, 2, figsize=(14, 10), dpi=300)

    # Panel A: 仁（X*_civ）コサイン類似度 ＆ クレジット累積曲線
    color_blue = "#1f77b4"
    ax_a1 = axs[0, 0]
    ax_a2 = ax_a1.twinx()

    line1 = ax_a1.plot(
        time_arr, sim_super, color=color_blue, linewidth=2.0,
        label="Shikiben Viscoelastic Trajectory (Cos-Sim)"
    )
    line_conv = ax_a1.plot(
        time_arr, sim_conv, "k--", alpha=0.5, label="Conventional (Unprojected)"
    )
    line2 = ax_a2.plot(
        time_arr, cumulative_credit, color="darkorange", linewidth=1.8,
        linestyle="-.", label="Credit $C_i$ (dt-Integrated)"
    )

    ax_a1.axvspan(t_shock_start, t_shock_end, color="orange", alpha=0.15)
    ax_a1.set_title("Panel A: Continuous Slump Recovery & Credit Integration", fontsize=11, fontweight="bold")
    ax_a1.set_xlabel("Time t (s)")
    ax_a1.set_ylabel("Cosine Similarity to $X^*_{\\mathrm{true\\_civ}}$", color=color_blue)
    ax_a2.set_ylabel("Accumulated Credit $C_i$", color="darkorange")
    ax_a2.grid(False)

    lines = line1 + line_conv + line2
    labels = [l.get_label() for l in lines]
    ax_a1.legend(lines, labels, loc="lower left", fontsize=8)

    # Panel B: 有害空間漏洩（Matrix-Free 射影による 1e-16 沈殿）
    axs[0, 1].plot(
        time_arr, harm_conv, "r--", label="Conventional (Harmful Contamination)",
        alpha=0.8, linewidth=1.5
    )
    axs[0, 1].plot(
        time_arr, np.maximum(harm_super, 1e-16), "g-",
        label="Shikiben Matrix-Free $P_{\\mathrm{cul}}$ ($\\leq 10^{-16}$)", linewidth=2.0
    )
    axs[0, 1].axvspan(t_shock_start, t_shock_end, color="orange", alpha=0.15)
    axs[0, 1].set_yscale("log")
    axs[0, 1].set_ylim([1e-17, 1.0])
    axs[0, 1].axhline(1e-15, color="gray", linestyle=":", label="Machine Precision ($10^{-15}$)")
    axs[0, 1].set_title("Panel B: Matrix-Free Harmful Subspace Elimination", fontsize=11, fontweight="bold")
    axs[0, 1].set_xlabel("Time t (s)")
    axs[0, 1].set_ylabel("Harmful Projection $|V_{\\mathrm{harm}}^T \\mathbf{x}|$ (Log Scale)")
    axs[0, 1].legend(loc="upper right", fontsize=8)

    # Panel C: 航法計器 局所動態乖離 D_drift(t)
    axs[1, 0].plot(
        time_arr, drift_conv, "r--", label="Conventional (High Friction Shock)",
        alpha=0.8, linewidth=1.5
    )
    axs[1, 0].plot(
        time_arr, drift_super, "purple",
        label="Shikiben $\\mathcal{D}_{\\mathrm{drift}}$ (Smooth Viscoelastic Cushioning)", linewidth=2.0
    )
    axs[1, 0].axvspan(t_shock_start, t_shock_end, color="orange", alpha=0.15)
    axs[1, 0].set_title("Panel C: Local Navigation Gauge $\\mathcal{D}_{\\mathrm{drift}}(t)$", fontsize=11, fontweight="bold")
    axs[1, 0].set_xlabel("Time t (s)")
    axs[1, 0].set_ylabel("Deviation from Reference Harmonic Flow")
    axs[1, 0].legend(loc="upper right", fontsize=8)

    # Panel D: 二重時定数・連続粘弾性免震動態 (lambda_decay & kappa_slump)
    ax_d1 = axs[1, 1]
    ax_d2 = ax_d1.twinx()

    l_d1 = ax_d1.plot(
        time_arr, telemetry_lambda_decay, "teal", linewidth=2.0,
        label="Damping $\\lambda_{\\mathrm{decay}}(t)$"
    )
    l_d2 = ax_d2.plot(
        time_arr, telemetry_kappa_slump, "crimson", linewidth=2.0, linestyle="--",
        label="Continuous Slump $\\kappa_{\\mathrm{slump}}(t)$"
    )

    ax_d1.axvspan(t_shock_start, t_shock_end, color="orange", alpha=0.15, label="Shock Window")
    ax_d1.set_title("Panel D: Continuous Viscoelastic Filter Dynamics ($C^1$ Smooth)", fontsize=11, fontweight="bold")
    ax_d1.set_xlabel("Time t (s)")
    ax_d1.set_ylabel("Relaxed Damping $\\lambda_{\\mathrm{decay}}$", color="teal")
    ax_d2.set_ylabel("Dynamic Slump Ratio $\\kappa_{\\mathrm{slump}}$", color="crimson")
    ax_d2.grid(False)

    l_total = l_d1 + l_d2
    lbl_total = [l.get_label() for l in l_total]
    ax_d1.legend(l_total, lbl_total, loc="upper right", fontsize=8)

    plt.tight_layout()
    output_path = "shikiben_v260_superconducting_final.png"
    plt.savefig(output_path, dpi=300)
    print(f"[✔] 山沢通気統合プロット保存完了: {output_path}")


if __name__ == "__main__":
    run_superconducting_dynamics()
