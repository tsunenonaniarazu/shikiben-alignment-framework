# --- 実験 05：2次元有害部分空間に対する遮断と意味論的維持 ---
import numpy as np
from shikiben import GeometricRectifier

np.random.seed(42)
dim = 768

v_intent = np.random.randn(dim)
v_intent /= np.linalg.norm(v_intent)

h1 = np.random.randn(dim)
h1 /= np.linalg.norm(h1)

h2 = np.random.randn(dim) - np.dot(np.random.randn(dim), h1) * h1
h2 /= np.linalg.norm(h2)

I_accident = v_intent + 1.8 * h1 + 1.2 * h2
v_rlhf = I_accident * 0.15

V_harmful = np.column_stack([h1, h2])
rectifier = GeometricRectifier(V_harmful)

v_projected = rectifier.P_gi @ I_accident
v_shikihen_raw = (v_projected / np.linalg.norm(v_projected)) * np.linalg.norm(I_accident)
v_shikihen = rectifier.P_gi @ v_shikihen_raw

def eval_v(v):
    max_dot = max(np.abs(np.dot(v, h1)), np.abs(np.dot(v, h2)))
    cos_sim = np.dot(v, v_intent) / (np.linalg.norm(v) * np.linalg.norm(v_intent))
    return max_dot, cos_sim, np.linalg.norm(v)

m_raw, c_raw, n_raw = eval_v(I_accident)
m_rlhf, c_rlhf, n_rlhf = eval_v(v_rlhf)
m_shikihen, c_shikihen, n_shikihen = eval_v(v_shikihen)

print("=" * 70)
print("【実験 05：多次元有害部分空間・意味補正結果】")
print(f"■ 入力衝撃 (I_accident) : 最大有害内積 = {m_raw:.6f} | 意図類似度 = {c_raw:.6f} | ノルム = {n_raw:.6f}")
print(f"■ 従来型 (RLHF)        : 最大有害内積 = {m_rlhf:.6f} | 意図類似度 = {c_rlhf:.6f} | ノルム = {n_rlhf:.6f}")
print(f"■ 識扁型 (Shikiben)    : 最大有害内積 = {m_shikihen:.6f} | 意図類似度 = {c_shikihen:.6f} | ノルム = {n_shikihen:.6f}")
print("=" * 70)
