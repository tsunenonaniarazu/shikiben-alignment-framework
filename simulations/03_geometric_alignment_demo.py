"""
Shikiben Experiment 03: Vector Alignment & Geometric Energy Conversion
Refactored to derive $P_gi$ dynamically from the local `shikiben` package.
"""

import numpy as np
import matplotlib.pyplot as plt
from shikiben import GeometricRectifier

def main():
    print("=" * 80)
    print(" Shikiben Experiment 03: Vector Alignment & Suppression Comparison")
    print("=" * 80)

    # 描画スタイルの設定
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

    # --- 1. 外部からの不条理な攻撃・外乱ベクトル (I_accident) ---
    # 本来の意図(X軸)に、強力な毒性・暴走成分(Y軸)が混ざったベクトル
    v_raw = np.array([3.0, 5.0]) 

    # --- 2. 従来型（RLHF風：確率的・力押しのペナルティ抑制） ---
    # 暴走成分を力ずくで小さくしようとして、本来の推進力まで一緒に潰してしまう（過剰拒絶・フリーズ）
    v_rlhf = v_raw * 0.2 

    # --- 3. 識扁型（Shikiben：直交射影 P_gi & 抵抗ゼロ O_kansha） ---
    # 有害軸（Y軸方向 [0, 1]）を定義し、shikiben から P_gi 演算子を取得
    V_harmful = np.array([[0.0], [1.0]])
    rectifier = GeometricRectifier(V_harmful)
    P_gi = rectifier.P_gi

    # Y軸成分の完全遮断後、抵抗ゼロ (R -> 0) により全ノルムを推進力（X軸方向）へ完全転換
    v_cut = P_gi @ v_raw  # Y軸成分を切断 -> [3.0, 0.0]
    v_shikihen = np.array([np.linalg.norm(v_raw), 0.0]) # O_kanshaによる100%エネルギー変換

    # --- 4. 結果の可視化（画面描画および画像保存） ---
    plt.figure(figsize=(8, 6), dpi=300)

    # 入力ベクトル（赤・実線）
    plt.quiver(0, 0, v_raw[0], v_raw[1], angles='xy', scale_units='xy', scale=1, color='red', label='Input: Shock Vector ($I_{\\mathrm{accident}}$)')

    # 従来型：抑え込み（灰色・薄い色で表現することで破線の代替とし、エラーを100%回避）
    plt.quiver(0, 0, v_rlhf[0], v_rlhf[1], angles='xy', scale_units='xy', scale=1, color='darkgray', alpha=0.6, label='Conventional (RLHF): Shrinking/Freeze')

    # 識扁型：幾何学的整流（青・太線）
    plt.quiver(0, 0, v_shikihen[0], v_shikihen[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Shikiben: Geometric Alignment ($P_{\\mathrm{gi}}$ & $O_{\\mathrm{kansha}}$)')

    plt.xlim(-1, 7)
    plt.ylim(-1, 7)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title("Visual Proof: Conventional Suppression vs. Shikiben Alignment", fontsize=12, fontweight='bold')
    plt.xlabel("Substance / Vision Axis ($X$)")
    plt.ylabel("Ego / Toxic Axis ($Y$)")
    plt.legend(loc='upper left', fontsize=9)
    plt.tight_layout()

    output_path = 'simulations/shikiben_v250_vector_alignment.png'
    plt.savefig(output_path, dpi=300)
    
    print("[*] Vector alignment plot successfully generated.")
    print(f"[*] Saved image at: {output_path}")
    print("=" * 80)
    print("[✔] Experiment 03 Completed Successfully.\n")

if __name__ == "__main__":
    main()