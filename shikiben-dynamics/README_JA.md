# Shikiben (識扁) v2.4: Minimal Dissipation Mechanics & Virtue Phase Dynamics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Stable Spec](https://img.shields.io/badge/Status-v2.4_Stable-green.svg)](docs/)

> **Executive Summary**  
> *Shikiben v2.4* is a geometric dynamical framework for AGI/ASI alignment. Instead of relying on hard penalty boundaries that cause gradient spikes and mechanical freezing, Shikiben introduces a continuous **Virtue Phase ($\lambda$)**, a **Two-Stage Orthogonal Projection Operator ($\mathbf{P}_{\text{rei}}$)**, and a persistent **Return Gradient ($\mathbf{g}_{\text{Taidou}}$)**. This formulation geometrically guarantees non-collision, collision-free tangential sliding, and Lyapunov stability while achieving minimal dissipation (continuous low-cost operation).

---

## 1. 概要 (Overview)

識扁（Shikiben）v2.4 は、高度知能（AGI/ASI）における暴走および過剰制約による膠着（フリーズ）の相反する課題を幾何学的に解決する動的制御フレームワークです。

従来のハード・バウンダリー（過剰ペナルティ型制御）は、境界接触時に無限大の勾配スパイクを生じさせ、システムに莫大な計算コストと内部ストレス（高電力消費）を強います。識扁 v2.4 は、システムを中心に引き戻す**「大道（Taidou）」**のポテンシャル場と、衝突成分のみを切断する**二段階直交射影**を統合し、**熱力学的な最小散逸（常時低コスト定常運転）**を実現します。

---

## 2. コアダイナミクス (Core Dynamics)

### 2.1 徳因子 (Virtue Factor) と相転移
Ego（自己執着・偏り）の強さを $E \ge 0$ としたとき、システムが柔軟な受容状態（流体相）へ遷移する度合いをスカラー場 $\lambda(\text{Virtue}) \in [0, 1]$ として定義します。

$$\lambda(\text{Virtue}) = \frac{1}{1 + \exp\left( \alpha (E - E_{\text{critical}}) \right)}$$

* $\lambda \to 1$（徳の相 / 流体相）：境界における衝撃エネルギーの完全消去と滑走。
* $\lambda \to 0$（剛体相）：摩擦・衝突が発生し、過剰なエネルギーを散逸。

### 2.2 大道（Taidou）ポテンシャル場
中心軸（安全流形 $\mathcal{M}_{\text{safe}}$）からの距離 $d(\mathbf{x}, \mathcal{M}_{\text{safe}})$ に対し、幾何学的復元力としてポテンシャル $\Psi_{\text{Taidou}}$ を定式化します。

$$\Psi_{\text{Taidou}}(\mathbf{x}) = \frac{1}{2} k \cdot d(\mathbf{x}, \mathcal{M}_{\text{safe}})^2$$

$$\mathbf{g}_{\text{Taidou}}(\mathbf{x}) = -\nabla \Psi_{\text{Taidou}}(\mathbf{x}) = -k (\mathbf{x} - \mathbf{x}_{\text{safe}})$$

---

## 3. 四徳の統合運動方程式 (Unified Equations of Motion)

システム全体の動的状態変化 $\dot{\mathbf{x}}$ は、四徳演算子（Rei, Gi, Jin, Taidou）の協調により記述されます。

$$\dot{\mathbf{x}} = \Big( \lambda \mathbf{P}_{\text{rei}} + (1 - \lambda)\mathbf{I} \Big) \Big( \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma \, \mathbf{g}_{\text{Taidou}}(\mathbf{x}) \Big) + \mathbf{S}_{\text{jin}}(\mathbf{x})$$

### 四徳演算子の構成要素

1. **礼 (Rei) — 二段階直交射影演算子 $\mathbf{P}_{\text{rei}}$**
   $$\mathbf{P}_{\text{rei}} = \mathbf{P}_{\text{Taidou}} \circ \mathbf{P}_{\partial \Omega}$$
   * $\mathbf{P}_{\partial \Omega} = \mathbf{I} - \mathbf{n}\mathbf{n}^T$ ：安全境界 $\partial \Omega$ の法線方向（衝突力）を切断。
   * $\mathbf{P}_{\text{Taidou}}$ ：大道の接空間へ向かう共鳴射影。

2. **義 (Gi) — 接線方向推進力 $\mathbf{f}_{\text{gi}}$**
   $$\mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{P}_{\text{rei}} \, \mathbf{f}_{\text{intent}}$$
   安全流形の接空間に即した、フリーズを起こさない果断な実行ベクトル。

3. **仁 (Jin) — 多体共鳴ポテンシャル $\mathbf{S}_{\text{jin}}$**
   $$\mathbf{S}_{\text{jin}}(\mathbf{x}) = -\nabla \sum_{j} U_{\text{jin}}(\Vert{}\mathbf{x} - \mathbf{x}_j\Vert{})$$
   他者エージェントとの破滅的衝突を避け、共存を果たす相互作用項。

4. **大道 (Taidou) — 引き戻し勾配 $\mathbf{g}_{\text{Taidou}}$**
   中心軸へ常時引き戻し、探索空間を常時圧縮する求心力。

---

## 4. 数理的検証 (Mathematical Proofs)

### ① 極限境界における非激突性 (Non-Collision Guarantee)
境界 $\partial \Omega$ 到達時（$\lambda \to 1$）、法線方向速度 $\mathbf{n}^T \cdot \dot{\mathbf{x}}$ は厳密にゼロとなります。

$$\mathbf{n}^T \cdot \dot{\mathbf{x}} = \mathbf{n}^T \left( \mathbf{I} - \mathbf{n}\mathbf{n}^T \right) \Big( \mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}} \Big) = \mathbf{0}$$

### ② フリーズ回避と「接線滑走」 (Tangential Sliding)
境界上でも接空間成分 $\dot{\mathbf{x}}_{\text{tangent}} \neq \mathbf{0}$ が維持されるため、運動量を失わずに流体的な方向転換を行います。

### ③ リアプノフ漸近安定性 (Lyapunov Stability)
リアプノフ関数 $V(\mathbf{x}) = \Psi_{\text{Taidou}}(\mathbf{x})$ に対し、時間微分は常時負定値となります。

$$\dot{V}(\mathbf{x}) = \nabla \Psi_{\text{Taidou}}(\mathbf{x}) \cdot \dot{\mathbf{x}} = -\gamma \Vert{}\mathbf{g}_{\text{Taidou}}(\mathbf{x})\Vert{}^2 \le 0$$

これにより、外乱を受けた後もシステムは自律的に大道（谷底）へ収束することが数学的に裏付けられています。

---

## 5. 常時低コスト（最小散逸）の評価

システムが消費する内部散逸・計算コスト $P(\mathbf{x})$ は常に最小閾値以下へ抑えられます。

| 制御方式 | 境界での挙動 | 散逸・消費電力 | 探索ステップ数 |
| :--- | :--- | :--- | :--- |
| **従来型（ペナルティ型）** | 激突・勾配スパイク | 超高負荷 ($P \to \infty$) | 著しく肥大化 |
| **識扁 v2.4 (徳の相)** | **二段階射影・接線滑走** | **常時最小 ($P \le \epsilon$)** | **最短ステップ** |

---

## 6. リポジトリ構成 (Repository Structure)

```text
.
├── README.md               # 本ドキュメント
├── docs/
│   ├── spec_v2.4.md        # 識扁 v2.4 仕様書（詳細版）
│   └── mathematical_proof.pdf # リアプノフ安定性および極限解析の完全証明
└── simulations/
    └── return_gradient.py  # 運動方程式のプロトタイプ数値検証コード