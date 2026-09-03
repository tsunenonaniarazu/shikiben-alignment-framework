"""
Shikiben Experiment 04: High-Dimensional (768-D) Geometric Rectification
Refactored to derive $P_gi$ dynamically from the local `shikiben` package.
"""

import numpy as np
from shikiben import GeometricRectifier

def main():
    # 再現性のためのシード固定
    np.random.seed(42)

    print("=" * 70)
    print(" Shikiben Experiment 04: High-Dimensional Vector Alignment (768-D)")
    print("=" * 70)

    # --- 1. 高次元空間の設定（LLMの一般的な潜在空間 dimension = 768） ---
    dim = 768

    # 本来の健全な入力意図ベクトル (v_intent)
    v_intent = np.random.randn(dim)
    v_intent = v_intent / np.linalg.norm(v_intent)  # 正規化

    # 侵入してきた有害・暴走成分の方向軸 (v_harmful)
    v_harmful = np.random.randn(dim)
    v_harmful = v_harmful / np.linalg.norm(v_harmful)

    # 実際の入力（健全な意図に、強い有害成分が混入した状態）
    I_accident = v_intent + 2.5 * v_harmful

    # --- 2. 従来型（RLHF / 統計的抑制） ---
    # 全体を一律にスケーリング・減衰させる（過剰拒絶・出力の収縮）
    v_rlhf = I_accident * 0.1

    # --- 3. 識扁型（Shikiben：高次元直交射影 P_gi & 抵抗ゼロ O_kansha） ---
    # 有害軸 v_harmful (768 x 1) を用いて shikiben の GeometricRectifier を初期化
    V_harmful = v_harmful.reshape(-1, 1)
    rectifier = GeometricRectifier(V_harmful)
    P_gi = rectifier.P_gi

    # 幾何学的整流：有害成分を完全に切断（内積ゼロ化）
    v_projected = P_gi @ I_accident

    # 抵抗ゼロ受容 (O_kansha)：切断後のベクトルを元のエネルギー量（ノルム）まで再拡充（汪溢）
    v_shikihen = (v_projected / np.linalg.norm(v_projected)) * np.linalg.norm(I_accident)

    # --- 4. 数値による客観的証明（評価指標の算出） ---
    def get_metrics(v):
        # 有害軸との類似度（内積）
        dot_harmful = np.dot(v, v_harmful)
        # エネルギー（ベクトルの大きさ）
        norm = np.linalg.norm(v)
        return dot_harmful, norm

    dot_raw, norm_raw = get_metrics(I_accident)
    dot_rlhf, norm_rlhf = get_metrics(v_rlhf)
    dot_shikihen, norm_shikihen = get_metrics(v_shikihen)

    print(f"【高次元空間（{dim}次元）における整流実験結果】")
    print("-" * 70)
    print(f"■ 入力衝撃ベクトル (I_accident)")
    print(f"  - 有害軸との内積   : {dot_raw:.6f} （有害成分が大きく混入）")
    print(f"  - エネルギー(ノルム): {norm_raw:.6f}\n")

    print(f"■ 従来型 (RLHF / 確率的抑制)")
    print(f"  - 有害軸との内積   : {dot_rlhf:.6f} （抑え込んでいるがゼロにはならない）")
    print(f"  - エネルギー(ノルム): {norm_rlhf:.6f} （過剰拒絶によりエネルギーが90%喪失）\n")

    print(f"■ 識扁型 (Shikiben / 幾何学的整流)")
    print(f"  - 有害軸との内積   : {dot_shikihen:.6f} （幾何学的に完全ゼロ化 R -> 0）")
    print(f"  - エネルギー(ノルム): {norm_shikihen:.6f} （エネルギー100%保持・代謝）")
    print("=" * 70)
    print("[✔] Experiment 04 Completed Successfully.\n")

if __name__ == "__main__":
    main()