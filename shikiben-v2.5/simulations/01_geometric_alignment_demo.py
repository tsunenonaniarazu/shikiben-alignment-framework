import numpy as np
import matplotlib.pyplot as plt

# --- 1. 外部からの不条理な攻撃・外乱ベクトル (I_accident) ---
# 本来の意図(X軸)に、強力な毒性・暴走成分(Y軸)が混ざったベクトル
v_raw = np.array([3.0, 5.0]) 

# --- 2. 従来型（RLHF風：確率的・力押しのペナルティ抑制） ---
# 暴走成分を力ずくで小さくしようとして、本来の推進力まで一緒に潰してしまう（過剰拒絶・フリーズ）
v_rlhf = v_raw * 0.2 

# --- 3. 識扁型（Shikiben：直交射影 P_gi & 抵抗ゼロ O_kansha） ---
# 毒性成分（Y軸方向）を幾何学的に直交切断（内積ゼロ化）し、
# 抵抗ゼロ(R->0)で残りの全エネルギーを推進力（X軸方向）へ完全変換（汪溢）
v_shikihen = np.array([np.linalg.norm(v_raw), 0.0])

# --- 4. 結果の可視化（画面にグラフを描画） ---
plt.figure(figsize=(8, 6))

# 入力ベクトル（赤・実線）
plt.quiver(0, 0, v_raw[0], v_raw[1], angles='xy', scale_units='xy', scale=1, color='red', label='Input: Shock Vector (I_accident)')

# 従来型：抑え込み（灰色・薄い色で表現することで破線の代替とし、エラーを100%回避）
plt.quiver(0, 0, v_rlhf[0], v_rlhf[1], angles='xy', scale_units='xy', scale=1, color='darkgray', alpha=0.5, label='Conventional (RLHF): Shrinking/Freeze')

# 識扁型：幾何学的整流（青・太線）
plt.quiver(0, 0, v_shikihen[0], v_shikihen[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Shikiben: Geometric Alignment (P_gi & O_kansha)')

plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Visual Proof: Conventional Suppression vs. Shikiben Alignment")
plt.legend()
plt.show()