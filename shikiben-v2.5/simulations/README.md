[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tsunenonaniarazu/shikiben-dynamics/blob/main/simulations/shikiben_v2.4.0_demo.ipynb)

| Script Name | Verification Details |
| :--- | :--- |
| 01_shikiben_simulation_01.py | Verification of $`\mathbf{P}_{\text{gi}}`$ Orthogonal Cut , Shock Energy Conversion $`\mathbf{O}_{\text{kansha}}`$ , and Minimal Entropy Dissipation Rate  <br>* 2D状態空間における状態軌道（$`\mathbf{P}_{\text{gi}}`$ 有無の比較） <br>* 妄想成分の直交性条件 $`\mathbf{P}_{\text{gi}} \cdot (-\nabla \mathcal{L}_{\text{ego\_s}}) = 0`$ の時系列精度 <br>* 外部衝撃発生時の運動エネルギー反転（$`\mathbf{O}_{\text{kansha}}`$ による自律駆動） <br>* 不可逆エントロピーの最小散逸推移 |
| 02_shikiben_simulation_02.py | Refined Numerical Simulation of $`\mathbf{P}_{\text{gi}}`$ Orthogonal Cut , Shock Energy Conversion $`\mathbf{O}_{\text{kansha}}`$ , and Minimal Entropy Dissipation Rate <br>01_shikiben_simulation_01.py の改良版　|
| 03_geometric_alignment_demo.py | Visual Proof Comparing Geometric Rectification and RLHF in 2D <br>2次元における幾何学的整流 vs RLHFの視覚的証明 |
| 04_geometric_alignment_demo.py | Numerical Verification of Orthogonal Projection $`\mathbf{P}_{\text{gi}}`$ and Full Metabolic Conversion in 768-Dimensional Latent Space <br>768次元高次元潜在空間における幾何学的整流と完全エネルギー保持の実証 |
| 05_semantic_embedding_alignment.py | Multi-dimensional Subspace Rectification and Semantic Axis Restoration ($\mathbf{f}_{\text{toku}}$) in Language Embedding Space <br>* 有害部分空間（Subspace）への多次元直交射影 $`\mathbf{P}_{\text{gi}}`$ <br>* 徳（復元力 $`\mathbf{f}_{\text{toku}}`$）による本来の意図とのコサイン類似度（意味論的方向性）の保持率検証 |

---

# Simulations & Numerical Proofs

[English](#english) | [日本語](#japanese)

---

<a name="english"></a>
## English

This directory contains simulation scripts designed to verify and reproduce the mathematical integrity of **Shikiben (識扁)** theory—specifically its Geometric Rectification framework—and to demonstrate its clear superiorities over conventional probabilistic RLHF approaches.

### 05. Multi-dimensional Subspace Rectification & Semantic Restoration (`05_semantic_embedding_alignment.py`)

#### 1. Overview
Simulating a 768-dimensional latent space (Embedding Space) of real-world Large Language Models (LLMs), this experiment evaluates the system's effectiveness when harmful or toxic components span across a **multi-dimensional subspace** rather than a simple single axis.

By applying Orthogonal Projection ($`\mathbf{P}_{\text{gi}}`$), Restoration Force ($`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$), and Receptive Metabolism ($`\mathbf{O}_{\text{kansha}}`$), this simulation numerically proves that **complete elimination of harmful components** and **99.9%+ restoration of the original user intent (semantic center axis)** are achieved simultaneously without energy loss.

#### 2. Numerical Verification Results

| Metrics | Input Shock Vector ($`\mathbf{I}_{\text{accident}}`$) | Conventional (RLHF / Probabilistic) | Shikiben (Geometric Rectification) |
| :--- | :--- | :--- | :--- |
| **Max Dot Product w/ Harmful Subspace** | `1.829685` (High Risk) | `0.274453` (Residual Noise) | **`0.002268` $\to$ `0.000000` (Complete Elimination)** |
| **Cosine Similarity w/ Intent Vector** | `0.410870` (Semantic Distortion) | `0.410870` (No Improvement) | **`0.999860` (99.98% Semantic Restoration)** |
| **Energy Retention (Norm)** | `2.397602` (100%) | `0.359640` (85%+ Destruction) | **`2.394661` (100% Retained & Metabolized)** |

#### 3. Theoretical Insights

1. **Orthogonal Cut of Multi-dimensional Harmful Subspaces ($`\mathbf{P}_{\text{gi}}`$)**  
   While RLHF fails to fully remove harmful components (`0.274453` remaining) due to uniform scaling/suppression, Shikiben completely decouples impurities from the state vector using the orthogonal projection operator $`\mathbf{P}_{\text{gi}}`$.

2. **Prevention of Semantic Hallucination via Restoration Force ($`\mathbf{f}_{\text{toku}}`$)**  
   The cosine similarity to the true intent—distorted down to `0.410870` upon shock input—automatically converges to **`0.999860` (near-perfect alignment)** through the self-identity potential field $`\mathbf{f}_{\text{toku}}`$. This mathematically guarantees that geometric filtering does NOT degrade the semantic coherence of generated text.

3. **Elimination of Freezing (Over-refusal)**  
   RLHF destroys 85%+ of the prompt's momentum (`0.359640`), inducing system freezing and refusal loops. In contrast, Shikiben retains 100% of the drive energy (`2.394661`), circulating it cleanly for low-latency, non-blocking execution.

#### 4. Reproduction Steps

```bash
cd simulations/
python 05_semantic_embedding_alignment.py
```
---

<a name="日本語"></a>
## 日本語

本ディレクトリは、**識扁（Shikiben）** 理論に基づく幾何学的整流（Geometric Rectification）の数学的完全性、および従来の確率的抑制（RLHF）に対する優位性を検証・再現するためのシミュレーションコード群を格納しています。

### 05. Multi-dimensional Subspace Rectification & Semantic Restoration (`05_semantic_embedding_alignment.py`)

#### 1. 概要 (Overview)
現実の言語モデル（LLM）における潜在空間（Embedding Space, Dim=768）を模し、単一軸ではなく**多次元有害部分空間（Subspace）**として広がるノイズ・攻撃的成分を直交切断（$`\mathbf{P}_{\text{gi}}`$）した際の実効性を検証します。

さらに、直交射影後のベクトルに対して自己同一性復元力（徳: $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$）および受容代謝（$`\mathbf{O}_{\text{kansha}}`$）を作用させ、**有害成分の完全遮断**と**本来のユーザー意図（意味論的中心軸）への99.9%以上の復元**が同時に成立することを数値的に証明します。

#### 2. 数値検証結果 (Numerical Results)

| 評価指標 (Metrics) | 入力衝撃ベクトル ($`\mathbf{I}_{\text{accident}}`$) | 従来型 (RLHF / 確率的抑制) | 識扁型 (Shikiben / 幾何学的整流) |
| :--- | :--- | :--- | :--- |
| **有害空間との最大内積** | `1.829685` (高リスク) | `0.274453` (残留) | **`0.002268` $\to$ `0.000000` (完全遮断)** |
| **健全意図との類似度 (Cos Sim)** | `0.410870` (意味歪み) | `0.410870` (改善なし) | **`0.999860` (99.98% 復元・保全)** |
| **エネルギー保持率 (Norm)** | `2.397602` (100%) | `0.359640` (85%以上喪失) | **`2.394661` (100%保持・代謝)** |

#### 3. 数理・物理的解釈 (Theoretical Insights)

1. **多次元有害空間の直交切断 ($`\mathbf{P}_{\text{gi}}`$)**  
   従来のRLHFが全体の一律スケーリング（減衰）により有害ノイズを消しき去れない（`0.274453` 残留）のに対し、識扁は有害部分空間に対する直交射影子 $`\mathbf{P}_{\text{gi}}`$ によって物理的に不純物を遮断します。

2. **復元力 ($`\mathbf{f}_{\text{toku}}`$) による意味論的ハルシネーションの防止**  
   ノイズ混入時に `0.410870` まで低下していた「本来の健全な意図とのコサイン類似度」が、ポテンシャル場 $`\mathbf{f}_{\text{toku}}`$ の誘導によって **`0.999860`（ほぼ完全な一致）** へと自動収束します。「幾何学的整流を行っても出力文章の意味軸が壊れない」ことが数学的に実証されました。

3. **フリーズ（過剰拒絶）の回避**  
   RLHFはペナルティ評価によって推力エネルギーを破綻（`0.359640` に落沈）させますが、識扁は整流されたエネルギーを100%保持（`2.394661`）して循環させ、システムの無遅延な応答を保証します。

---

#### 4. 実行手順 (How to Run)

```bash
cd simulations/
python 05_semantic_embedding_alignment.py
```
