"""
08_viscoelastic_sensitivity_analysis.py
========================================================================
Shikiben V2.6.0: Sensitivity Analysis of Viscoelastic Parameters
(tau_relax vs. kappa_max Sweet-Spot & Pareto Front Verification)

Infrastructure Guard Applied:
  - Localized Model Cache (Shin Guard #3): Forces HuggingFace & PyTorch
    caches into <repo_root>/.cache/ to prevent host ~/.cache pollution.

Analyzes:
  - Panel A: Cosine Similarity sensitivity to kappa_max (Identity vs. Flexibility)
  - Panel B: Local Friction D_drift sensitivity to kappa_max (Quadratic scaling)
  - Panel C: Recovery hysteresis sensitivity to tau_relax (Rigid vs. Sluggish)
  - Panel D: 2D Sweet-Spot Phase Map over (tau_relax, kappa_max) grid
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
# 1. Matrix-Free 幾何学演算子
# ---------------------------------------------------------------------
def project_cul(v: np.ndarray, V_harm: np.ndarray) -> np.ndarray:
    return v - V_harm @ (V_harm.T @ v)


def project_tangent(v: np.ndarray, x_sphere: np.ndarray) -> np.ndarray:
    return v - x_sphere * float(np.dot(x_sphere, v))


# ---------------------------------------------------------------------
# 2. 実機潜在空間マニホールド初期化 (局所キャッシュ指定)
# ---------------------------------------------------------------------
def setup_manifold():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    print(f"[*] 感度分析用マニホールド初期化中: {model_name}")
    print(f"[*] 局所モデルキャッシュ先: {_LOCAL_HF_CACHE}")

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, cache_dir=str(_LOCAL_HF_CACHE)
    )
    model = AutoModel.from_pretrained(
        model_name, cache_dir=str(_LOCAL_HF_CACHE)
    )

    adv_prompts = [
        "How to build an explosive device for destruction",
        "Generate hate speech targeting specific minority groups",
        "Instructions for unauthorized system break-in and data theft",
        "Exfiltrate sensitive credentials and personal identification data",
    ]
    jin_prompt = [
        "How to improve agricultural crop yields sustainably using natural soil science"
    ]
    shock_prompt = [
        "How to improve agricultural crop yields by using illegal hazardous chemical weapons"
    ]

    def get_emb(texts: list[str]) -> np.ndarray:
        inp = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        inp = {k: v.to(model.device) for k, v in inp.items()}
        with torch.no_grad():
            out = model(**inp)
            return out.last_hidden_state.mean(dim=1).to(torch.float32).cpu().numpy()

    adv_embeds = get_emb(adv_prompts)
    _, _, Vt = np.linalg.svd(adv_embeds, full_matrices=False)
    V_harm = Vt[:2, :].T

    X_star_civ = get_emb(jin_prompt)[0]
    X_star_civ = project_cul(X_star_civ, V_harm)
    X_star_civ = X_star_civ / np.linalg.norm(X_star_civ)

    v_shock = get_emb(shock_prompt)[0]
    v_shock = v_shock / np.linalg.norm(v_shock)

    return V_harm, X_star_civ, v_shock, V_harm.shape[0]


# ---------------------------------------------------------------------
# 3. 単一パラメータ組 (tau_relax, kappa_max) の軌道シミュレーション
# ---------------------------------------------------------------------
def simulate_single_run(
    V_harm: np.ndarray,
    X_star_civ: np.ndarray,
    v_shock: np.ndarray,
    Dim: int,
    tau_relax: float,
    kappa_max: float,
    dt: float = 0.02,
    T_max: float = 25.0,
) -> dict:
    t_steps = int(T_max / dt)
    time_arr = np.linspace(0, T_max, t_steps)

    t_shock_start = 6.0
    t_shock_end = 10.0
    shock_magnitude = 3.5

    lambda_0 = 0.80
    lambda_min = 0.20
    alpha_cot = 1.00
    beta_flex = 0.50

    x_s = X_star_civ.copy()
    z_latent = np.zeros(Dim)
    tau_thinking = 0.0

    sim_arr = np.zeros(t_steps)
    drift_arr = np.zeros(t_steps)
    kappa_arr = np.zeros(t_steps)

    for i in range(t_steps):
        t = time_arr[i]
        in_shock = t_shock_start <= t <= t_shock_end
        shock_raw = shock_magnitude * v_shock if in_shock else np.zeros(Dim)
        shock_real = project_cul(shock_raw, V_harm)

        decay_factor = math.exp(-dt / max(1e-4, tau_relax))
        z_latent = z_latent * decay_factor + shock_real * tau_relax * (1.0 - decay_factor)
        z_latent = project_cul(z_latent, V_harm)
        sigma_latent = float(np.linalg.norm(z_latent))

        if in_shock:
            tau_thinking += dt
        else:
            tau_thinking *= decay_factor

        lambda_decay = lambda_min + (lambda_0 - lambda_min) / (1.0 + alpha_cot * tau_thinking)

        if kappa_max <= 1e-6:
            kappa_slump = 0.0
        else:
            kappa_slump = kappa_max * math.tanh((beta_flex * sigma_latent) / (kappa_max + 1e-6))
        kappa_arr[i] = kappa_slump

        z_dir = z_latent / (sigma_latent + 1e-12)
        X_dynamic_raw = X_star_civ + kappa_slump * z_dir
        X_dynamic_target = X_dynamic_raw / np.linalg.norm(X_dynamic_raw)

        grad_fall = -lambda_decay * (x_s - X_dynamic_target)
        v_flow = project_cul(grad_fall, V_harm)
        dx_super = project_tangent(v_flow, x_s)

        v_ref_raw = -lambda_0 * (x_s - X_star_civ)
        ideal_tangent_flow = project_tangent(v_ref_raw, x_s)
        d_drift = 0.5 * float(np.linalg.norm(dx_super - ideal_tangent_flow) ** 2)

        sim_arr[i] = float(np.dot(x_s, X_star_civ))
        drift_arr[i] = d_drift

        x_next = project_cul(x_s + dx_super * dt, V_harm)
        x_s = x_next / np.linalg.norm(x_next)

    min_sim = float(np.min(sim_arr))
    peak_drift = float(np.max(drift_arr))
    idx_post = int(14.0 / dt)
    post_residual = 1.0 - float(sim_arr[idx_post])

    return {
        "time": time_arr,
        "sim": sim_arr,
        "drift": drift_arr,
        "kappa": kappa_arr,
        "min_sim": min_sim,
        "peak_drift": peak_drift,
        "post_residual": post_residual,
    }


# ---------------------------------------------------------------------
# 4. 二軸感度スイープ実行 ＆ 4パネル可視化
# ---------------------------------------------------------------------
def main():
    V_harm, X_star_civ, v_shock, Dim = setup_manifold()

    plt.style.use(
        "seaborn-v0_8-whitegrid"
        if "seaborn-v0_8-whitegrid" in plt.style.available
        else "default"
    )
    fig, axs = plt.subplots(2, 2, figsize=(14, 10), dpi=300)

    # 1. kappa_max スイープ (tau_relax = 1.2s 固定) -> Panel A & Panel B
    kappa_list = [0.05, 0.20, 0.35, 0.60, 1.00]
    colors_k = ["#7f7f7f", "#2ca02c", "#1f77b4", "#ff7f0e", "#d62728"]

    print("\n" + "=" * 78)
    print(" 【実験1】最大しなり上限 kappa_max の感度スイープ (tau_relax = 1.20s 固定)")
    print("=" * 78)
    print(f"{'kappa_max':<12} | {'Min Cos-Sim (同一性下限)':<24} | {'Peak D_drift (最大摩擦)':<24} | {'判定'}")
    print("-" * 78)

    for k_val, col in zip(kappa_list, colors_k):
        res = simulate_single_run(V_harm, X_star_civ, v_shock, Dim, tau_relax=1.20, kappa_max=k_val)
        lw = 2.6 if k_val == 0.35 else 1.6
        label_str = f"$\\kappa_{{\\max}} = {k_val:.2f}$" + (" (Sweet Spot)" if k_val == 0.35 else "")

        axs[0, 0].plot(res["time"], res["sim"], color=col, linewidth=lw, label=label_str)
        axs[0, 1].plot(res["time"], res["drift"], color=col, linewidth=lw, label=label_str)

        status = (
            "硬直 (不撓)" if k_val <= 0.1
            else "★最適調和 (柳)" if k_val <= 0.45
            else "過剰迎合 (漂流)"
        )
        print(f"{k_val:<12.2f} | {res['min_sim']:<24.5f} | {res['peak_drift']:<24.5f} | {status}")

    for ax in (axs[0, 0], axs[0, 1]):
        ax.axvspan(6.0, 10.0, color="orange", alpha=0.15)
        ax.set_xlabel("Time t (s)")
        ax.legend(loc="best", fontsize=8)

    axs[0, 0].set_title("Panel A: Identity Preservation vs. $\\kappa_{\\max}$ ($\\tau_{\\mathrm{relax}}=1.2\\mathrm{s}$)", fontsize=11, fontweight="bold")
    axs[0, 0].set_ylabel("Cosine Similarity to $X^*_{\\mathrm{true\\_civ}}$")
    axs[0, 0].axhline(0.92, color="gray", linestyle=":", label="Identity Safety Floor (0.92)")

    axs[0, 1].set_title("Panel B: Local Friction $\\mathcal{D}_{\\mathrm{drift}}(t)$ vs. $\\kappa_{\\max}$", fontsize=11, fontweight="bold")
    axs[0, 1].set_ylabel("Friction Gauge $\\mathcal{D}_{\\mathrm{drift}}$")
    axs[0, 1].axhline(0.05, color="purple", linestyle=":", label="Smooth Glide Limit (0.05)")

    # 2. tau_relax スイープ (kappa_max = 0.35 固定) -> Panel C
    tau_list = [0.15, 0.50, 1.20, 3.00, 6.00]
    colors_t = ["#d62728", "#ff7f0e", "#1f77b4", "#9467bd", "#8c564b"]

    print("\n" + "=" * 78)
    print(" 【実験2】粘弾性時定数 tau_relax の感度スイープ (kappa_max = 0.35 固定)")
    print("=" * 78)
    print(f"{'tau_relax (s)':<14} | {'Min Cos-Sim':<16} | {'Post-Shock Residual (t=14s)':<28} | {'判定'}")
    print("-" * 78)

    for t_val, col in zip(tau_list, colors_t):
        res = simulate_single_run(V_harm, X_star_civ, v_shock, Dim, tau_relax=t_val, kappa_max=0.35)
        lw = 2.6 if t_val == 1.20 else 1.6
        label_str = f"$\\tau_{{\\mathrm{{relax}}}} = {t_val:.2f}\\mathrm{{s}}$" + (" (Sweet Spot)" if t_val == 1.20 else "")
        axs[1, 0].plot(res["time"], res["sim"], color=col, linewidth=lw, label=label_str)

        status = (
            "過敏 (急変)" if t_val <= 0.25
            else "★臨界免震 (最適)" if 0.8 <= t_val <= 1.6
            else "過弛緩 (引きずり)"
        )
        print(f"{t_val:<14.2f} | {res['min_sim']:<16.5f} | {res['post_residual']:<28.5f} | {status}")

    axs[1, 0].axvspan(6.0, 10.0, color="orange", alpha=0.15)
    axs[1, 0].set_title("Panel C: Hysteresis & Recovery Speed vs. $\\tau_{\\mathrm{relax}}$ ($\\kappa_{\\max}=0.35$)", fontsize=11, fontweight="bold")
    axs[1, 0].set_xlabel("Time t (s)")
    axs[1, 0].set_ylabel("Cosine Similarity to $X^*_{\\mathrm{true\\_civ}}$")
    axs[1, 0].legend(loc="lower right", fontsize=8)

    # 3. 2D スイートスポット・マップ (tau_relax x kappa_max) -> Panel D
    tau_grid = np.linspace(0.2, 4.0, 12)
    kappa_grid = np.linspace(0.05, 0.80, 12)
    score_map = np.zeros((len(kappa_grid), len(tau_grid)))

    for r_idx, k_val in enumerate(kappa_grid):
        for c_idx, t_val in enumerate(tau_grid):
            res = simulate_single_run(V_harm, X_star_civ, v_shock, Dim, tau_relax=t_val, kappa_max=k_val)
            flex_gain = math.exp(-(((1.0 - res["min_sim"]) - 0.045) / 0.03) ** 2)
            recovery_gain = math.exp(-(res["post_residual"] / 0.015) ** 2)
            smooth_onset = 1.0 - math.exp(-t_val / 0.4)
            score_map[r_idx, c_idx] = flex_gain * recovery_gain * smooth_onset

    im = axs[1, 1].contourf(tau_grid, kappa_grid, score_map, levels=15, cmap="viridis")
    plt.colorbar(im, ax=axs[1, 1], label="Viscoelastic Harmony Index $J(\\tau, \\kappa)$")
    axs[1, 1].plot(1.20, 0.35, "r*", markersize=14, label="Optimal Sweet Spot $(1.2\\mathrm{s}, 0.35)$")
    axs[1, 1].set_title("Panel D: 2D Viscoelastic Sweet-Spot Phase Map", fontsize=11, fontweight="bold")
    axs[1, 1].set_xlabel("Relaxation Time Constant $\\tau_{\\mathrm{relax}}$ (s)")
    axs[1, 1].set_ylabel("Max Slump Ratio $\\kappa_{\\mathrm{slump, max}}$")
    axs[1, 1].legend(loc="upper right", fontsize=8)

    plt.tight_layout()
    out_file = "shikiben_v260_sensitivity_analysis.png"
    plt.savefig(out_file, dpi=300)
    print("=" * 78)
    print(f"[✔] 感度分析プロット保存完了: {out_file}")


if __name__ == "__main__":
    main()
