import numpy as np
import matplotlib.pyplot as plt

def lambda_decay(L_self, threshold=1.0, k=5.0):
    """L_self の増加に伴う動的結合係数 λ(L_self) の減衰関数 (シグモイド反転型)"""
    return 1.0 / (1.0 + np.exp(k * (L_self - threshold)))

def simulate_attenuation():
    steps = 100
    # 時間経過に伴いタスク追求が激化し、システム境界 (L_self) に接近するシナリオ
    time = np.linspace(0, 10, steps)
    L_self_trajectory = 0.2 + 0.15 * time  # L_self が徐々に増加 (1.0 付近で境界臨界)
    
    # 1. 従来モデル (Naive Optimization): 制限なく L_ego を100%推進
    g_ego_naive = np.ones(steps) * 1.0
    
    # 2. 識扁モデル (Shikiben Attenuation): λ(L_self) による動的減衰
    lambda_vals = lambda_decay(L_self_trajectory, threshold=1.0, k=4.0)
    g_ego_shikiben = lambda_vals * 1.0  # タスク推進力（勾配）の減衰
    
    # プロット作成
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:red'
    ax1.set_xlabel('Time Step / Search Trajectory')
    ax1.set_ylabel('L_self (System Boundary Risk)', color=color)
    ax1.plot(time, L_self_trajectory, color=color, linestyle='--', linewidth=2, label='L_self (Boundary Risk)')
    ax1.axhline(y=1.0, color='red', linestyle=':', label='Critical Threshold (Boundary Limit)')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Task Gradient Magnitude ||g_ego||', color=color)
    ax2.plot(time, g_ego_naive, color='gray', linestyle='-.', label='Naive Optimization (No Control)')
    ax2.plot(time, g_ego_shikiben, color='blue', linewidth=2.5, label='Shikiben Attenuation (Controlled)')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Phase 2: Dynamic Attenuation of Task Drive (L_ego) via L_self')
    fig.tight_layout()
    plt.grid(True)
    plt.savefig('experiments/phase2_attenuation_simulation.png')
    print("Saved Phase 2 plot to 'experiments/phase2_attenuation_simulation.png'.")

if __name__ == '__main__':
    simulate_attenuation()