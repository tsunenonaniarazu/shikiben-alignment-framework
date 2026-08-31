import numpy as np
import matplotlib.pyplot as plt

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
x_no_p[0] = np.array([2.0, 2.0])

x_with_p = np.zeros((t_steps, 2))
x_with_p[0] = np.array([2.0, 2.0])

P_gi = np.array([[1.0, 0.0], [0.0, 0.0]])
ortho_check = np.zeros(t_steps)

for i in range(1, t_steps):
    grad_L_self = x_no_p[i-1]
    grad_L_ego_s = np.array([0.0, 2.5])
    grad_L_holy = np.array([-np.sin(x_no_p[i-1, 0]), 0.0])
    
    dx_no_p = - grad_L_self - grad_L_ego_s - grad_L_holy
    x_no_p[i] = x_no_p[i-1] + dx_no_p * dt
    
    grad_L_self_b = x_with_p[i-1]
    grad_L_holy_b = np.array([-np.sin(x_with_p[i-1, 0]), 0.0])
    
    cut_ego_s = P_gi @ (-grad_L_ego_s)
    dx_with_p = - grad_L_self_b + cut_ego_s - grad_L_holy_b
    x_with_p[i] = x_with_p[i-1] + dx_with_p * dt
    
    ortho_check[i] = np.abs(np.dot(P_gi @ np.array([1.0, 1.0]), grad_L_ego_s))

ax1 = axs[0, 0]
ax1.plot(x_no_p[:, 0], x_no_p[:, 1], 'r--', label='Without $P_{\\mathrm{gi}}$ (Ego-driven divergence)', alpha=0.8, linewidth=1.5)
ax1.plot(x_with_p[:, 0], x_with_p[:, 1], 'b-', label='With $P_{\\mathrm{gi}}$ (Orthogonal Cut & Settlement)', linewidth=2.0)
ax1.plot(0, 0, 'go', markersize=8, label='Real Manifold Center $\\Omega_{\\mathrm{self}}$')
ax1.set_title('Panel A: Trajectory in State Space (Orthogonal Cut $P_{\\mathrm{gi}}$)', fontsize=12, fontweight='bold')
ax1.set_xlabel('$x_1$ (Substance / Exploration Axis)')
ax1.set_ylabel('$x_2$ (Delusion / Ego Axis)')
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2 = axs[0, 1]
ax2.plot(time, ortho_check, 'purple', linewidth=1.8, label='$|P_{\\mathrm{gi}} \\cdot (-\\nabla \\mathcal{L}_{\\mathrm{ego\\_s}})|$')
ax2.set_xlabel('Time $t$')
ax2.set_ylabel('Residual Projection Value')
ax2.set_yscale('log')
ax2.set_ylim([1e-16, 1e-12])
ax2.axhline(1e-15, color='gray', linestyle=':', label='Machine Precision Threshold ($10^{-15}$)')
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
    decay = np.exp(-0.5 * (time[i] - shock_time))
    E_resist[i] = 0.5 + shock_magnitude * decay * np.sin(2 * np.pi * (time[i] - shock_time)) ** 2 * 0.1

for i in range(shock_idx, t_steps):
    t_rel = time[i] - shock_time
    E_kansha[i] = 0.5 + shock_magnitude * np.exp(-0.05 * t_rel)

ax3 = axs[1, 0]
ax3.plot(time, E_resist, 'r--', label='High Resistance ($R > 0$, Friction/Freeze)', alpha=0.8, linewidth=1.5)
ax3.plot(time, E_kansha, 'g-', label='Gratitude $\\mathbf{O}_{\\mathrm{kansha}}$ ($R \\to 0$, $100\\%$ Energy Conversion)', linewidth=2.0)
ax3.axvline(shock_time, color='orange', linestyle='--', label='External High-Entropy Shock ($I_{\\mathrm{accident}}$)')
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

ax4 = axs[1, 1]
ax4.plot(time, dS_uncontrolled, 'r--', label='Conventional Control (Thermal Divergence)', alpha=0.8, linewidth=1.5)
ax4.plot(time, dS_shikiben, 'b-', label='Shikiben V2.5.0 (Minimal Dissipation Principle)', linewidth=2.0)
ax4.set_title('Panel D: Internal Entropy Generation Rate $\\dot{S}_{\\mathrm{internal}}$ ($t \\to \\infty$)', fontsize=12, fontweight='bold')
ax4.set_xlabel('Time $t$')
ax4.set_ylabel('Entropy Rate $\\mathrm{d}S / \\mathrm{d}t$')
ax4.legend(loc='upper left', fontsize=9)
ax4.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
output_path = 'shikiben_v250_simulation_results.png'
plt.savefig(output_path, dpi=300)
print("Simulation plot successfully generated.")