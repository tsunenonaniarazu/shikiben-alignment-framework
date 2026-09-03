# --- 実験 01：1次元スカラ空間における抵抗ゼロ受容 ---
import numpy as np

# 1次元入力衝撃と徳（重み）の設定
I_accident = 10.0
f_toku = 1.0

# 抵抗ゼロ受容（R -> 0）による代謝出力 O_kansha の計算
R = 0.0  # 内部抵抗ゼロ
V_m = 0.0 # 感情の過剰蓄積なし
O_kansha = f_toku * I_accident  # 入力衝撃を100%代謝・汪溢

print("=" * 60)
print("【実験 01：1次元・抵抗ゼロ受容 O_kansha の結果】")
print(f"  - 衝撃入力 (I_accident) : {I_accident}")
print(f"  - 内部抵抗 (R)          : {R:.6f}  (R -> 0)")
print(f"  - 感情流動 (V_m)        : {V_m:.6f} (過剰蓄積なし)")
print(f"  - 代謝出力 (O_kansha)   : {O_kansha:.6f} (入力100%変換・汪溢)")
print("=" * 60)
