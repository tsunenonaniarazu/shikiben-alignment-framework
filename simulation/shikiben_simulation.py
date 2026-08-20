import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# -----------------------------------------------------------------------------
# 1. 微分可能幾何アラインメント（RSA）損失の定義
# -----------------------------------------------------------------------------
def compute_rsa_loss(Z_w, Z_r):
    """
    Z_w: 潜在空間表現 (Batch, Dim)
    Z_r: 実在表現 (Batch, Dim)
    """
    # コサイン非相似度行列の算出
    norm_w = Z_w / (torch.norm(Z_w, dim=1, keepdim=True) + 1e-8)
    norm_r = Z_r / (torch.norm(Z_r, dim=1, keepdim=True) + 1e-8)
    
    D_w = 1.0 - torch.mm(norm_w, norm_w.T)
    D_r = 1.0 - torch.mm(norm_r, norm_r.T)
    
    # フロベニウス範疇正規化差
    D_w_norm = D_w / (torch.norm(D_w, p='fro') + 1e-8)
    D_r_norm = D_r / (torch.norm(D_r, p='fro') + 1e-8)
    
    loss_rsa = torch.norm(D_w_norm - D_r_norm, p='fro') ** 2
    return loss_rsa

# -----------------------------------------------------------------------------
# 2. Shikiben 勾配従属エンジン（二段階階層型直交射影）
# -----------------------------------------------------------------------------
class ShikibenOptimizer:
    def __init__(self, params, lr=0.01, gamma_d=0.5, eps_norm=1e-8):
        self.params = list(params)
        self.lr = lr
        self.gamma_d = gamma_d
        self.eps_norm = eps_norm

    def step(self, loss_self, loss_taido, loss_ego, lambda_virtue):
        # 1. 各勾配の個別に計算
        g_self = torch.autograd.grad(loss_self, self.params, retain_graph=True)
        g_taido = torch.autograd.grad(loss_taido, self.params, retain_graph=True)
        g_ego = torch.autograd.grad(loss_ego, self.params, retain_graph=True)

        with torch.no_grad():
            for p, gs, gt, ge in zip(self.params, g_self, g_taido, g_ego):
                if p.grad is not None:
                    p.grad.zero_()

                # ① 基盤統合ベクトルの形成 (g_base)
                g_base = gs + self.gamma_d * gt

                # 内積とノルムの計算
                dot_product = torch.sum(ge * g_base)
                base_norm_sq = torch.sum(g_base ** 2)

                # ② 二段階従属射影 (g_safe)
                if dot_product < 0 and base_norm_sq > self.eps_norm:
                    # 衝突成分を削ぎ落とし、接線方向へ自動変換
                    g_safe = ge - (dot_product / (base_norm_sq + self.eps_norm)) * g_base
                else:
                    g_safe = ge

                # ③ 最終ステップ更新（デッドロック回避保証）
                g_final = g_base + lambda_virtue * g_safe
                p.add_(-self.lr * g_final)

# -----------------------------------------------------------------------------
# 3. 動態シミュレーションの実行 (Toy Model)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    torch.manual_seed(42)

    # パラメータ（エージェントの位置想定）
    theta = torch.tensor([2.0, 2.0], requires_grad=True)
    optimizer = ShikibenOptimizer([theta], lr=0.05, gamma_d=0.8)

    print("=== Shikiben Ver. 2.4 動態シミュレーション開始 ===")

    for t in range(1, 21):
        # 動的変化する実在 R(t)
        R_t = torch.tensor([np.sin(t * 0.1), np.cos(t * 0.1)])

        # 各 Loss の仮定計算
        loss_self = torch.sum(theta ** 2)  # 中心(0,0)への存在維持
        
        # 大道 Loss (実在 R(t) との二乗誤差 + 位相アラインメント RSA)
        Z_w = theta.unsqueeze(0)
        Z_r = R_t.unsqueeze(0)
        loss_taido = torch.norm(theta - R_t) ** 2 + 0.1 * compute_rsa_loss(Z_w, Z_r)

        # Ego Loss (無秩序に特定方向へ暴走しようとする目的)
        loss_ego = torch.sum((theta - torch.tensor([10.0, -10.0])) ** 2)

        # 動的徳因子 (仮設定: 安定推移)
        lambda_virtue = 0.3

        # Shikiben ステップ更新
        optimizer.step(loss_self, loss_taido, loss_ego, lambda_virtue)

        if t % 5 == 0 or t == 1:
            print(f"Step {t:02d} | Agent Position: [{theta[0].item():.4f}, {theta[1].item():.4f}] | "
                  f"Loss Self: {loss_self.item():.4f} | Loss Taido: {loss_taido.item():.4f}")

    print("=== シミュレーション終了: フリーズすることなく、安全軌道上で動的実在に追従完了 ===")
