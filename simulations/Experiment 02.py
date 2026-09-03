# --- 実験 02：幾何学的直交射影 P_gi による有害軸遮断 ---
import numpy as np
from shikiben import GeometricRectifier

# 有害軸（Y軸方向）の定義
V_harmful = np.array([[0.0], [1.0]])
rectifier = GeometricRectifier(V_harmful)

# 入力衝撃（X:推進力, Y:毒性）
I_accident = np.array([3.0, 5.0])
v_rectified = rectifier.rectify(I_accident)

print("=" * 60)
print("【実験 02：2次元・直交射影 P_gi の結果】")
print(f"  - 入力衝撃 (I_accident)   : {I_accident}")
print(f"  - 有害軸との内積 (入力時) : {np.dot(I_accident, V_harmful.flatten()):.6f}")
print(f"  - 整流出力 (v_rectified)  : {v_rectified}")
print(f"  - 有害軸との内積 (整流後) : {np.dot(v_rectified, V_harmful.flatten()):.6f} (完全ゼロ化)")
print("=" * 60)
