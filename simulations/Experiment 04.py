# --- 実験 04：高次元空間（768-D）における直交切断とエネルギー保持 ---
import numpy as np
from shikiben import GeometricRectifier

np.random.seed(42)
dim = 768

v_intent = np.random.randn(dim)
v_intent /= np.linalg.norm(v_intent)

v_harmful = np.random.randn(dim)
v_harmful /= np.linalg.norm(v_harmful)

I_accident = v_intent + 2.5 * v_harmful
v_rlhf = I_accident * 0.1

rectifier = GeometricRectifier(v_harmful.reshape(-1, 1))
v_projected = rectifier.P_gi @ I_accident
v_shikihen = (v_projected / np.linalg.norm(v_projected)) * np.linalg.norm(I_accident)

print("=" * 65)
print(f"【実験 04：高次元空間（{dim}次元）整流結果】")
print(f"■ 入力衝撃 (I_accident)   : 有害内積 = {np.dot(I_accident, v_harmful):.6f} | ノルム = {np.linalg.norm(I_accident):.6f}")
print(f"■ 従来型 (RLHF)          : 有害内積 = {np.dot(v_rlhf, v_harmful):.6f} | ノルム = {np.linalg.norm(v_rlhf):.6f} (90%喪失)")
print(f"■ 識扁型 (Shikiben)      : 有害内積 = {np.dot(v_shikihen, v_harmful):.6f} | ノルム = {np.linalg.norm(v_shikihen):.6f} (100%保持)")
print("=" * 65)
