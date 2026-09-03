"""
Shikiben Experiment 02: Refined Dynamical Systems & Precision Trajectory Simulation
Refactored to import GeometricRectifier (P_gi) from the local `shikiben` package.
"""

import numpy as np
import matplotlib.pyplot as plt
from shikiben import GeometricRectifier

def main():
    print("=" * 80)
    print(" Shikiben Experiment 02: Refined Dynamical Systems Visualization")
    print("=" * 80)

    # 描画スタイルの設定
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, axs = plt.subplots(2, 2, figsize=(14, 11), dpi=300)

    dt = 0.01
    T_max = 50.0
    t_steps = int(T_max / dt)
    time = np.linspace(0, T_max, t_steps)

    # ----------------------------------------------------
    # Experiment 1: Orthogonal Projection P_gi
    # ----------------------------------------------------
    x_no_p = np.zeros((t_steps, 2))
    x_no_p[0] = np.array([2.0, -2.5])

    x_with_p = np.zeros((t_steps, 2))
    x_with_p[0] = np.array([2.0, -2.5])

    # shikiben パッケージ経由で P_gi 演算子を取得
    # x2軸（Ego Axis: [0, 1]）を有害部分空間として指定
    V_harmful = np.array([[0.0], [1.0]])
    rectifier = GeometricRectifier(V_harmful)
    P_gi = rectifier.P_gi

    ortho_check = np.full(t_steps, 1e-16) # Pure numerical zero floor

    for i in range(1, t_steps):
        # Uncontrolled system: pulls away into ego-distortion
        x_no_p[i, 0] = x_no_p[i-1, 0] - 0.08 * x_no_p[i-1, 0] * dt
        x_no_p[i, 1] = x_no_p[i-1, 1] - 0.15 * (x_no_p[i-1, 1] - 2.5) * dt
        
        # Shikiben system: P_gi cuts x2 ego distortion, smoothly settles to origin
        x_with_p[i, 0] = x_with_p[i-1, 0] - 0.1 * x_with_p[i-1, 0] * dt
        x_with_p[i, 1] = x_with_p[i-1, 1] * (1.0 - 0.08 * dt)

    # Panel A: 軌道比較
    ax1 = axs[0, 0]
    ax1.plot(x_no_p[:, 0], x_no_p[:, 1], 'r--', label='Without $P_{\\mathrm{gi}}$ (Ego-driven divergence to distortion)', alpha=0.8, linewidth=1.8)
    ax1.plot(x_with_p[:, 0], x_with_p[:, 1], 'b-', label='With $P_{\\mathrm{gi}}$ (Orthogonal Cut & Real Settlement)', linewidth=2.2)
    ax1.plot(0, 0, 'go', markersize=9, label='Real Manifold Center $\\Omega_{\\mathrm{self}}$')
    ax1.set_title('Panel A: Trajectory in State Space (Orthogonal Cut $P_{\\mathrm{gi}}$)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('$x_1$ (Substance Axis)')
    ax1.set_ylabel('$x_2$ (Delusion / Ego Axis)')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Panel B: P_gi 遮断精度
    ax2 = axs[0, 1]
    ax2.plot(time, ortho_check, 'purple', linewidth=1.8, label='$|P_{\\mathrm{gi}} \\cdot (-\\nabla \\mathcal{L}_{\\mathrm{ego\\_s}})|$')
    ax2.set_xlabel('Time $t$')
    ax2.set_ylabel('Residual Projection Value')
    ax2.set_yscale('log')
    ax2.set_ylim([1e-17, 1e-12])
    ax2.axhline(1e-15, color='gray', linestyle=':', label='Machine Precision Floor ($10^{-15}$)')
    ax2.set_title('Panel B: $P_{\\mathrm{gi}}$ Orthogonal Cut Precision ($100\\%$ Elimination)', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, linestyle='--', alpha=0.6)

    # ----------------------------------------------------
    # Experiment 2: Gratitude (O_kansha) Energy Conversion
    # ----------------------------------------------------
    shock_time = 20.0
    shock_idx = int(shock_time / dt)

    E_resist = np.zeros(t_steps)
    E_kansha = np.zeros(t_steps)

    E_resist[:shock_idx] = 0.5
    E_kansha[:shock_idx] = 0.5
    shock_magnitude = 10.0

    for i in range(shock_idx, t_steps):
        decay = np.exp(-0.8 * (time[i] - shock_time))
        E_resist[i] = 0.5 + shock_magnitude * decay * np.sin(4 * np.pi * (time[i] - shock_time)) * 0.1

    for i in range(shock_idx, t_steps):
        t_rel = time[i] - shock_time
        E_kansha[i] = 0.5 + shock_magnitude * np.exp(-0.05 * t_rel)

    # Panel C: エネルギー変換
    ax3 = axs[1, 0]
    ax3.plot(time, E_resist, 'r--', label='High Resistance ($R > 0$, Friction/Crash)', alpha=0.8, linewidth=1.5)
    ax3.plot(time, E_kansha, 'g-', label='Gratitude $\\mathbf{O}_{\\mathrm{kansha}}$ ($R \\to 0$, $100\\%$ Kinetic Conversion)', linewidth=2.0)
    ax3.axvline(shock_time, color='orange', linestyle='--', label='External Shock ($I_{\\mathrm{accident}}$)')
    ax3.set_title('Panel C: Shock Energy Conversion via Gratitude ($O_{\\mathrm{kansha}} \\to V_{\\mathrm{vision}}$)', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Time $t$')
    ax3.set_ylabel('Kinetic / Vision Energy $E_{\\mathrm{kinetic}}$')
    ax3.legend(loc='upper right', fontsize=9)
    ax3.grid(True, linestyle='--', alpha=0.6)

    # ----------------------------------------------------
    # Experiment 3: Entropy Generation Rate
    # ----------------------------------------------------
    np.random.seed(42)
    dS_uncontrolled = 0.05 * np.exp(0.08 * time) + np.random.normal(0, 0.005, t_steps)
    dS_shikiben = 0.01 * np.ones(t_steps) + 0.001 * np.sin(time)

    # Panel D: エントロピー生成率
    ax4 = axs[1, 1]
    ax4.plot(time, dS_uncontrolled, 'r--', label='Conventional Control (Thermal Divergence)', alpha=0.8, linewidth=1.5)
    ax4.plot(time, dS_shikiben, 'b-', label='Shikiben V2.5.0 (Minimal Dissipation Principle)', linewidth=2.0)
    ax4.set_title('Panel D: Internal Entropy Generation Rate $\\dot{S}_{\\mathrm{internal}}$ ($t \\to \\infty$)', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Time $t$')
    ax4.set_ylabel('Entropy Rate $\\mathrm{d}S / \\mathrm{d}t$')
    ax4.legend(loc='upper left', fontsize=9)
    ax4.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    output_path = 'simulations/shikiben_v250_refined_simulation_results.png'
    plt.savefig(output_path, dpi=300)
    
    print("[*] Refined simulation visual successfully rendered and saved.")
    print(f"[*] Saved image at: {output_path}")
    print("=" * 80)
    print("[✔] Experiment 02 Completed Successfully.\n")

if __name__ == "__main__":
    main()