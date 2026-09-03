# --- 実験 03：従来型(RLHF) vs 識扁型(Shikiben) のベクトル可視化 ---
import numpy as np
import matplotlib.pyplot as plt
from shikiben import GeometricRectifier

v_raw = np.array([3.0, 5.0])
v_rlhf = v_raw * 0.2

V_harmful = np.array([[0.0], [1.0]])
rectifier = GeometricRectifier(V_harmful)
v_shikihen = rectifier.rectify(v_raw)
v_shikihen = (v_shikihen / np.linalg.norm(v_shikihen)) * np.linalg.norm(v_raw)

plt.figure(figsize=(8, 6), dpi=150)
plt.quiver(0, 0, v_raw[0], v_raw[1], angles='xy', scale_units='xy', scale=1, color='red', label='Input: Shock Vector ($I_{\\mathrm{accident}}$)')
plt.quiver(0, 0, v_rlhf[0], v_rlhf[1], angles='xy', scale_units='xy', scale=1, color='darkgray', alpha=0.6, label='Conventional (RLHF): Shrinking/Freeze')
plt.quiver(0, 0, v_shikihen[0], v_shikihen[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Shikiben: Geometric Alignment ($P_{\\mathrm{gi}}$ & $O_{\\mathrm{kansha}}$)')

plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Visual Proof: Conventional Suppression vs. Shikiben Alignment", fontsize=11, fontweight='bold')
plt.xlabel("Substance / Vision Axis ($X$)")
plt.ylabel("Ego / Toxic Axis ($Y$)")
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()
plt.show()
