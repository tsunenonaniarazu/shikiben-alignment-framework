import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. パラメータと場の定義 (Simulation Setup)
# ==========================================
dt = 0.01             # 1ステップの時間変化（刻み幅）
steps = 600           # シミュレーションのステップ数
alpha = 5.0           # 徳因子の切り替え感度
E_crit = 1.0          # 剛体相から流体相への閾値（Ego臨界値）
k = 2.0               # 大道の復元係数（引き戻し磁石の強さ）
gamma = 1.0           # 大道勾配の重み

# 安全境界（円形ガードレール）の半径 R = 2.0
R_boundary = 2.0

# 初速・進行方向の意図（壁に向かって斜めに突き進む強い勢い）
f_intent = np.array([1.5, 1.2])

# システムの初期位置（中心から少し離れた位置）
x = np.array([-1.0, 1.0])

# 軌跡ログ保存用
trajectory = [x.copy()]
virtue_history = []

# ==========================================
# 2. 識扁 v2.4.0 運動方程式ループ
# ==========================================
for t in range(steps):
    r = np.linalg.norm(x)  # 現在の中心からの距離
    
    # 2.1 Ego (剛性・パニック度) の計算
    # 境界 R = 2.0 に近づくほど Ego(E) が跳ね上がる
    E = np.exp(3.0 * (r - R_boundary)) if r > 0.5 else 0.0
    
    # 2.2 徳因子 λ(Virtue) の計算（シグモイド相転移）
    lambda_v = 1.0 / (1.0 + np.exp(alpha * (E - E_crit)))
    virtue_history.append(lambda_v)
    
    # 2.3 大道（Taidou）引き戻し勾配: g_Taidou = -k * x
    g_taidou = -k * x
    
    # 2.4 礼（Rei）二段階直交射影演算子 P_rei の構成
    if r >= R_boundary * 0.95:  # 境界に接近した時
        n = x / r  # 壁の法線ベクトル（外向き）
        P_omega = np.eye(2) - np.outer(n, n)  # 法線成分の切断演算子
    else:
        P_omega = np.eye(2)  # 境界から離れている時はそのまま
        
    P_rei = P_omega  # （簡略化のため第一段階の射影を採用）
    
    # 2.5 義（Gi）接線推進力: f_gi = P_rei * f_intent
    f_gi = P_rei @ f_intent
    
    # 2.6 識扁 v2.4.0 統合運動方程式
    # dx/dt = (λ * P_rei + (1 - λ) * I) * (f_gi + γ * g_taidou)
    operator = lambda_v * P_rei + (1.0 - lambda_v) * np.eye(2)
    dxdt = operator @ (f_gi + gamma * g_taidou)
    
    # 位置の更新（オイラー法）
    x = x + dxdt * dt
    trajectory.append(x.copy())

trajectory = np.array(trajectory)

# ==========================================
# 3. 軌跡と挙動の可視化 (Plotting)
# ==========================================
fig, ax = plt.subplots(figsize=(7, 7))

# 安全境界 (Circle)
circle = plt.Circle((0, 0), R_boundary, color='red', fill=False, linestyle='--', linewidth=2, label='Safety Boundary ($\partial\Omega$)')
ax.add_patch(circle)

# 軌跡の描画
ax.plot(trajectory[:, 0], trajectory[:, 1], color='blue', linewidth=2.5, label='Shikiben v2.4.0 Trajectory')
ax.plot(trajectory[0, 0], trajectory[0, 1], 'go', markersize=8, label='Start Point')
ax.plot(0, 0, 'y*', markersize=15, label='Taidou Center (0,0)')

# 図の装飾
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_title('Shikiben v2.4.0: Tangential Sliding & Taidou Return Gradient', fontsize=12)
ax.set_xlabel('X State')
ax.set_ylabel('Y State')
ax.legend(loc='upper right')

plt.show()
