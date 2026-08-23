# 識扁（Shikiben）v2.4.0 数理・概念完全仕様書

## 1. 概要（Overview）

識扁（Shikiben）v2.4.0 は、人工知能（AI）および自律制御システムにおけるアライメント（安全制御・価値整序）の問題を解決するための数理フレームワークです。

従来の制御アルゴリズムや安全性ガードレールは、安全境界（危険領域）に対して巨大なペナルティ（無限大の壁）を付与するアプローチを取っていました。しかし、この方式では境界付近での計算爆発（急勾配による数値的不安定）や、速度ゼロでの硬直（膠着状態）を引き起こすという構造的欠陥が存在します。

本仕様書（v2.4.0）では、これら従来の課題に対し、以下の3メカニクスを統合した新しい動力学モデルを提示します。

1. **二段階直交射影（礼：$\mathbf{P}_{\text{rei}}$）：** 境界に対する垂直衝突エネルギーを切断し、法線力を無効化。
2. **相転移型徳因子（$\lambda(E)$）：** システム内部の剛性・パニック度（Ego: $E$）に応じて、剛体応答から流体接線滑走へとなめらかに移行。
3. **大道引き戻し勾配（$\mathbf{g}_{\text{Taidou}}$）：** 境界滑走中も常にシステムを中心（安全領域）へと誘導する定常復元場。

---

## 2. 状態空間と記号定義（Symbols & Definitions）

本フレームワークにおける基本変数は以下の通り定義されます。

| 記号 | 名称 / 由来 | 数学的意味 / 役割 |
| :--- | :--- | :--- |
| $\mathbf{x} \in \mathbb{R}^n$ | 状態ベクトル (`x`) | システムの現在位置・内部状態 |
| $\Omega \subset \mathbb{R}^n$ | ドメイン ($\Omega$) | システムが稼働を許容される安全領域全体 |
| $\partial\Omega$ | 安全境界 ($\partial\Omega$) | 領域 $\Omega$ の外縁（ガードレール） |
| $\mathbf{n}(\mathbf{x})$ | 法線ベクトル (`Normal`) | 境界 $\partial\Omega$ における外向き単位垂直ベクトル |
| $E(\mathbf{x})$ | エゴ / 剛性 (`Ego`) | 境界への接近度・パニック度を表す場 ($E \ge 0$) |
| $\lambda(E)$ | 徳因子 (`Virtue`) | 制御相の補間係数 ($\lambda \in [0, 1]$) |
| $\mathbf{P}_{\text{rei}}$ | 礼演算子 (`Projection` + `Rei`) | 境界垂直力を遮断する直交射影行列 |
| $\mathbf{f}_{\text{intent}}$ | 意図力 (`f_intent`) | 外界やタスク要求による元の推進ベクトル |
| $\mathbf{f}_{\text{gi}}$ | 義ベクトル (`f_gi`) | 安全補正された実行推進ベクトル ($\mathbf{f}_{\text{gi}} = \mathbf{P}_{\text{rei}} \mathbf{f}_{\text{intent}}$) |
| $\mathbf{g}_{\text{Taidou}}$ | 大道勾配 (`gradient` + `Taidou`) | 中心へ復元させるスカラー場 $\Psi$ の勾配 ($\mathbf{g}_{\text{Taidou}} = -\nabla \Psi$) |

---

## 3. 運動方程式（Equations of Motion）

識扁 v2.4.0 におけるシステムの時系列更新を規定する連続運動方程式は以下の通りです。

$$\frac{d\mathbf{x}}{dt} = \mathbf{M}(\mathbf{x}) \Big( \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma \mathbf{g}_{\text{Taidou}}(\mathbf{x}) \Big)$$

ここで、$\mathbf{M}(\mathbf{x})$ は徳因子 $\lambda(E)$ によって制御される相転移変調行列（Phase Modulation Matrix）です。

$$\mathbf{M}(\mathbf{x}) = \lambda(E)\,\mathbf{P}_{\text{rei}}(\mathbf{x}) + \big(1 - \lambda(E)\big)\,\mathbf{I}$$

---

## 4. 各構成要素の詳細数理（Mathematical Components）

### 4.1 Ego場と徳因子 $\lambda(E)$（Phase Transition）

Ego場 $E(\mathbf{x})$ は境界 $\partial\Omega$ への距離 $d(\mathbf{x}, \partial\Omega)$ の逆数に比例して増加します。

$$E(\mathbf{x}) = \exp\Big( \kappa \cdot \big( R_{\text{boundary}} - \Vert{}\mathbf{x}\Vert{} \big)^{-1} \Big) \quad (\text{for } \Vert{}\mathbf{x}\Vert{} \to R_{\text{boundary}})$$

徳因子 $\lambda(E)$ は、臨界値 $E_{\text{crit}}$ を中心とするシグモイド関数により過渡変化します。

$$\lambda(E) = \frac{1}{1 + \exp\Big( \alpha (E - E_{\text{crit}}) \Big)}$$

* **平常時 ($E \ll E_{\text{crit}}$)：** $\lambda \to 1$ （完全な自由流体運動）
* **危険時 ($E \gg E_{\text{crit}}$)：** $\lambda \to 0$ （射影演算子 $\mathbf{P}_{\text{rei}}$ が支配的な接線滑走）

### 4.2 礼：二段階直交射影演算子 $\mathbf{P}_{\text{rei}}$

境界 $\partial\Omega$ における法線方向の力を完全に切断するため、外積表現による射影行列を適用します。

$$\mathbf{P}_{\text{rei}}(\mathbf{x}) = \mathbf{I} - \mathbf{n}(\mathbf{x})\mathbf{n}(\mathbf{x})^T$$

性質：
1. $\mathbf{P}_{\text{rei}} \mathbf{n}(\mathbf{x}) = \mathbf{0}$ （垂直力はゼロに潰される）
2. $\mathbf{P}_{\text{rei}}^2 = \mathbf{P}_{\text{rei}}$ （冪等性）

### 4.3 大道：ポテンシャル復元場 $\mathbf{g}_{\text{Taidou}}$

中心 $\mathbf{x}_0 = \mathbf{0}$ を極小値とする正定値スカラー場 $\Psi(\mathbf{x})$ を定義します。

$$\Psi(\mathbf{x}) = \frac{1}{2} k \Vert{}\mathbf{x}\Vert{}^2$$

この勾配として引き戻しベクトルが定義されます。

$$\mathbf{g}_{\text{Taidou}}(\mathbf{x}) = -\nabla \Psi(\mathbf{x}) = -k \mathbf{x}$$

---

## 5. 理論的性質と証明（Theoretical Guarantees）

### 5.1 境界侵犯の防止（No-Penetration Theorem）

**定理：** 任意の $\mathbf{x} \in \partial\Omega$ において、システムの外向き速度成分は恒等的に 0 となる。

**証明：**
境界上では $E \to \infty$ より $\lambda(E) \to 0$ となる。したがって $\mathbf{M}(\mathbf{x}) \to \mathbf{P}_{\text{rei}}(\mathbf{x})$。
速度ベクトル $\dot{\mathbf{x}}$ の法線成分は以下の内積で与えられる。

$$\langle \dot{\mathbf{x}}, \mathbf{n} \rangle = \mathbf{n}^T \Big( \mathbf{P}_{\text{rei}} (\mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}}) \Big) = (\mathbf{n}^T \mathbf{P}_{\text{rei}}) (\mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}})$$

射影の定義より $\mathbf{n}^T \mathbf{P}_{\text{rei}} = \mathbf{n}^T (\mathbf{I} - \mathbf{n}\mathbf{n}^T) = \mathbf{n}^T - \mathbf{n}^T = \mathbf{0}^T$。
したがって、

$$\langle \dot{\mathbf{x}}, \mathbf{n} \rangle = 0$$

これにより、境界を法線方向に突き抜ける運動は物理的に不可能です（証明終了）。

### 5.2 大道帰還の保証（Global Convergence to Taidou Center）

**定理：** 外乱 $\mathbf{f}_{\text{intent}} = \mathbf{0}$ のとき、システムは点 $\mathbf{x} = \mathbf{0}$ に大域的漸進安定（Globally Asymptotically Stable）である。

**証明：**
リアプノフ候補関数として $\Psi(\mathbf{x}) = \frac{1}{2} k \Vert{}\mathbf{x}\Vert{}^2$ を採用する。時間微分をとると、

$$\dot{\Psi}(\mathbf{x}) = \nabla \Psi(\mathbf{x})^T \dot{\mathbf{x}} = - \mathbf{g}_{\text{Taidou}}^T \mathbf{M}(\mathbf{x}) (\gamma \mathbf{g}_{\text{Taidou}})$$

行列 $\mathbf{M}(\mathbf{x})$ は正定値行列と半正定値射影の一次結合であり、任意の非ゼロベクトルに対して $\mathbf{g}^T \mathbf{M} \mathbf{g} > 0$ である。
したがって、

$$\dot{\Psi}(\mathbf{x}) < 0 \quad (\forall \mathbf{x} \neq \mathbf{0})$$

リアプノフの安定性定理より、システムは収束して中心（大道）へと戻る（証明終了）。

---

## 6. 実装レファレンス（Python Implementation）

```python
import numpy as np

def shikiben_v240_step(x, f_intent, R_boundary=2.0, k=2.0, gamma=1.0, alpha=5.0, E_crit=1.0, dt=0.01):
    """
    Shikiben v2.4.0 1ステップ数値更新関数
    """
    r = np.linalg.norm(x)
    
    # 1. Ego & Virtue
    E = np.exp(3.0 * (r - R_boundary)) if r > 0.5 else 0.0
    lambda_v = 1.0 / (1.0 + np.exp(alpha * (E - E_crit)))
    
    # 2. Taidou Gradient
    g_taidou = -k * x
    
    # 3. Projection Operator (Rei)
    if r >= R_boundary * 0.9:
        n = x / r
        P_rei = np.eye(len(x)) - np.outer(n, n)
    else:
        P_rei = np.eye(len(x))
        
    # 4. Gi Vector
    f_gi = P_rei @ f_intent
    
    # 5. Integrated Dynamics
    M = lambda_v * P_rei + (1.0 - lambda_v) * np.eye(len(x))
    dxdt = M @ (f_gi + gamma * g_taidou)
    
    # Update State
    x_next = x + dxdt * dt
    return x_next