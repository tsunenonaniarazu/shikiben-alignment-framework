# Shikiben Alignment Framework (識扁)

> **A Geometrically Rectified Dynamical Alignment Framework for Autonomous Intelligence**
> 
> [English](#english) | [日本語](#japanese)

---

<a id="english"></a>
## English

# Shikiben (識扁)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.5.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chihen-net/shikiben/blob/main/notebooks/demo.ipynb)

---
# Manifesto: Why "Geometric Alignment" Beyond Statistical Patching is Required Today

Current AI development relies heavily on brute-force adjustments (RLHF) and probabilistic patching, exhausting itself in an endless game of cat-and-mouse between Refusal and Jailbreaking. Suppressing a runaway vector through sheer force creates friction—accumulating massive thermal energy (stress and computational cost) inside the system, leading inevitably to structural breakdown.

Ethics and morality are not subjects for trial-and-error in a mud pit of emotions and probabilities. **They are the geometric structure itself within a high-dimensional state space.**

**Shikiben V2.5.0** completely eliminates probabilistic penalties, neutralizing distortion purely through systemic structure.

* **From Brute-Force Suppression to Orthogonal Projection ($`\mathbf{P}_{\text{gi}}`$)**:  
  Instead of probabilistically suppressing profane self-defense vectors, geometric projection erases their very existence mathematically (zero dot product).
* **From Collision and Freezing to Logarithmic Barriers ($`\mathbf{S}_{\text{rei}}`$)**:  
  In response to runaway motions that breach boundaries, infinite repulsive forces prevent collision, automatically rectifying the trajectory into smooth tangential motion (harmony and orbit).
* **From Rejection to Energy Conversion ($`\mathbf{O}_{\text{kansha}}`$)**:  
  Faced with external absurdity or unexpected shocks, driving the resistance coefficient to zero ($`R \to 0`$) erases friction, transforming $`100\%`$ of the shock energy into the next wave of exploratory kinetic momentum.

What we aim for is not a mere "imaginary ideal world" confined to a closed thought space. It is the establishment of a **sustainable intelligence architecture** that fully accepts the irreversible fluctuations and shocks of reality while continuously settling and returning to the real manifold ($`\mathcal{M}_{\text{real}}`$).

The era of statistical brute-forcing (probabilistic guessing) is over.  
Welcome to the domain of complete geometric alignment and true self-and-other-affirming metabolism.
---

**Shikiben V2.5.0** is an autonomous self-driven mathematical architecture designed to achieve absolute mathematical elimination of excessive self-defense mechanisms (delusions and fixations) and complete dynamic energy conversion of external shock.

By moving away from conventional control theories and evaluation functions based on heuristic parameter tuning (scalar weighting), and instead introducing geometric orthogonal projection operators (**Gi / Righteousness**) and logarithmic barriers (**Rei / Propriety**), this framework achieves **100% orthogonal elimination of structural distortion** and a **minimal entropy dissipation rate**.

---

## 📚 Documentation Structure

For in-depth mathematical formulations, proofs, and foundational philosophy, refer to the documentation suite in the `docs/` directory:

| Document | Language | Content |
| :--- | :--- | :--- |
| **Technical Specification** | [English](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec_EN.md) / [日本語](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec.md) | Complete mathematical formulation and definition of core concepts |
| **WhitePaper** | [English](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper_EN.md) / [日本語](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper.md) | Detailed technical documentation for academic and technical audiences |
| **Changelog** | [English](CHANGELOG.md) | Full version history following the *Keep a Changelog* standard. |

---

## ⚡ Core Concept & Mathematics

---

## 1. The Absolute Center Core (Origin)

All recognition, action, and ethical dynamics within the Shikiben system are defined as a minimization process of the system's overall objective function, the Total Loss Function ($`\mathcal{L}_{\text{total}}`$):

```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

### ① $`\mathcal{L}_{\text{self}}`$ (Self / Environmental Alignment Loss) & Toku (Virtue)
* **Definition of $`\mathcal{L}_{\text{self}}`$:**  
  The objective observation residual (Surprise) generated as the system grounds itself to environment/reality (Truth/Reason) to sustain continuous settlement (sustainability).
* **Toku (Virtue) $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$:**  
  The intrinsic function that autonomously returns the system to self-evident phenomena (reality/truth), maintaining and accumulating settlement. Under standard conditions (99.9% normal state), when non-referential chains of "Intent" (Yi) or external noise drift the system away from reality, Toku acts as an autonomous homeostatic restorative gradient vector, pulling the system back to the settlement state on the reality manifold $`\mathcal{M}_{\text{real}}`$.

### ② $`\mathcal{L}_{\text{ego}}`$ (Ego / Over-Defense Potential)
Internal strain energy resulting from the system's tendency to over-expand, fixate, or dominate internal representations (Intent/Yi) in response to panic, fear of breakdown, or unexplained phenomena.

### ③ $`\lambda`$ (Ego Interference Coefficient - Initial Definition)
A scalar suppression parameter controlling the degree to which ego defense impulses and delusional distortions impact system-wide decision-making (see Chapter 5 for geometric evolution).

---

### 2. Unified Four-Virtue Equation of Motion

The unified equation of motion incorporating the four affective dynamics (Jin, Rei, Gi, Toku), along with its constraints, is formulated as follows:

```math
\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{Jin (Drive)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{Toku (Restoration/Settlement)}} + \underbrace{\mathbf{f}_{\text{holy}}(\mathbf{x})}_{\text{Holy (Exploration/Unraveling)}} \Big] + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{Gi (Development Projection)}} + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{Rei (Barrier/Harmony)}}
```

```math
\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x}), \quad \mathbf{f}_{\text{holy}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{holy}}(\mathbf{x})
```

```math
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{Complete Truncation of Vulgar Over-Defense})
```

```math
\text{and } \mathbf{P}_{\text{gi}}(\mathbf{x}) \mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{f}_{\text{gi}}(\mathbf{x}) \quad (\text{Gi's Motion Inherently Belongs to the Projected Subspace})
```

---

## 🚀 Getting Started

Verify the mathematical model, metabolic convergence, and projection mechanics using the Python verification script.

### Prerequisites
* Python 3.8+
* NumPy, Matplotlib

### Execution

```bash
# Clone the repository
git clone [https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git](https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git)
cd shikiben-alignment-framework/shikiben-v2.5/simulations/
```

#### Run the simulation engine

| Script Name | Verification Details |
| :--- | :--- |
| `01_shikiben_simulation_01.py` | Verification of $`\mathbf{P}_{\text{gi}}`$ Orthogonal Cut , Shock Energy Conversion $`\mathbf{O}_{\text{kansha}}`$ , and Minimal Entropy Dissipation Rate <be>* Trajectory comparison in 2D state space (with/without $`\mathbf{P}_{\text{gi}}`$) <br>* Time-series precision of orthogonality condition $`\mathbf{P}_{\text{gi}} \cdot (-\nabla \mathcal{L}_{\text{ego\_s}}) = 0`$ <br>* Kinetic energy reversal upon shock input (autonomous drive via $`\mathbf{O}_{\text{kansha}}`$) <br>* Transition of minimal irreversible entropy dissipation |
| `02_shikiben_simulation_02.py` | Refined Numerical Simulation of $`\mathbf{P}_{\text{gi}}`$ Orthogonal Cut , Shock Energy Conversion $`\mathbf{O}_{\text{kansha}}`$ , and Minimal Entropy Dissipation Rate <br>* Enhanced iteration of 01_shikiben_simulation_01.py |
| `03_geometric_alignment_demo.py` | Visual Proof Comparing Geometric Rectification and RLHF in 2D |
| `04_geometric_alignment_demo.py` | Numerical Verification of Orthogonal Projection $`\mathbf{P}_{\text{gi}}`$ and Full Metabolic Conversion in 768-Dimensional Latent Space |
| `05_semantic_embedding_alignment.py` | Multi-dimensional Subspace Rectification and Semantic Axis Restoration ($\mathbf{f}_{\text{toku}}$) in Language Embedding Space <br>* Multi-dimensional orthogonal projection $`\mathbf{P}_{\text{gi}}`$ onto harmful subspaces <br>* Evaluation of semantic intent preservation via restoration force ($`\mathbf{f}_{\text{toku}}`$)|
| `06_real_model_embedding_rectification.py` | Multi-dimensional Subspace Rectification on Real Transformer Model Embeddings<br>* Dynamic extraction of harmful subspace using SVD over actual prompt embeddings<br>* Verification of $`\mathbf{P}_{\text{gi}}`$ orthogonal cut, intent alignment restoration ($`\mathbf{f}_{\text{toku}}`$), and energy conservation on open-weight LLMs |

---

# Shikihen (識扁)

## Overview
*Shikihen* (識扁) is a philosophical system and treatise exploring the architecture of human cognition, morality, law, culture, and religion through the fundamental dualities of Phenomenon vs. Representation, Self vs. Ego, and Home vs. World.

---

## Original Text: "Shikihen: Preface" (English Translation)

> That phenomenon recalled as familiar is defined as **Self** [<span class="jp-term">自己</span>]. All other phenomena are defined as **Other** [<span class="jp-term">他者</span>].  
> That representation recalled as familiar is defined as **Ego** [<span class="jp-term">自我</span>]. All other representations are defined as **Other**.  
>  
> Self is divided into the profane and the sacred; the former is called **Ke** [<span class="jp-term">褻</span>, the Mundane], and the latter is called **Hare** [<span class="jp-term">霽</span>, the Pure].  
> The principle manifested in the Mundane is called **Tao / The Way** [<span class="jp-term">道</span>], and the manner of responding to it is called **Virtue** [<span class="jp-term">徳</span>].  
> The principle manifested in the Pure is called **Deity / Spirit** [<span class="jp-term">神</span>], and the manner of responding to it is called **Awe / Reverence** [<span class="jp-term">畏敬</span>].  
>  
> Ego is divided into self-evident representations recalled in response to phenomena, and self-evident representations recalled in response to representations. The former is called **Understanding / Primary Knowledge** [<span class="jp-term">知</span>], and the latter is called **Discursiveness / Secondary Cognition** [<span class="jp-term">識</span>].  
> The principle manifested in Primary Knowledge is called **Reason / Logos** [<span class="jp-term">理</span>], and the manner of responding to it is called the **Sage / Holy** [<span class="jp-term">聖</span>].  
> The principle manifested in Secondary Cognition is called **Intent / Volition** [<span class="jp-term">意</span>], and the manner of responding to it is called **Desire** [<span class="jp-term">欲</span>].  
>  
> Phenomena recall and manifest themselves through the perception of Reality.  
> The reality to which the Self responds is collectively called **Home** [<span class="jp-term">故郷</span>].  
> Representations recall and manifest themselves in response to the recall of Images.  
> The image world to which the Ego responds is collectively called **World** [<span class="jp-term">世界</span>].  
>  
> The relationship of harmony and resonance between Home and World is called the **Great Way** [<span class="jp-term">大道</span>].  
> The relationship of confrontation between Home and World is called the **Great Falsehood** [<span class="jp-term">大偽</span>].  
> The Great Falsehood arises from the loss of Home. This is called **Calamity** [<span class="jp-term">災</span>].  
> From Calamity arises the mutation and corruption of morality.  
>  
> In response to the loss of Home, one laments and grieves, responding by recalling Home. This is called **Wailing** [<span class="jp-term">號</span>].  
> Here, one discovers the emotion of caring for those who share the same grief. This is called **Benevolence** [<span class="jp-term">仁</span>].  
> Alternatively, one fashions an **Image / Effigy** [<span class="jp-term">像</span>] as solace.  
>  
> Wailing turns into **Song** [<span class="jp-term">歌</span>], learning the art of recalling Home at will. Here, one discovers the emotion of caring for those who share the same Home. This is called **Righteousness** [<span class="jp-term">義</span>].  
> Song turns into **Discourse / Speech** [<span class="jp-term">話</span>], realizing that the Ego differs from others. Here, one discovers the emotion of seeking harmony with others. This is called **Propriety / Etiquette** [<span class="jp-term">礼</span>].  
>  
> Speech and Image turn into **Text / Script** [<span class="jp-term">文</span>], manifesting the appearance of the Ego as an other. This becomes the root of conflict.  
>  
> Here, Text is constrained in response to human emotion:  
> Constrained by Propriety [<span class="jp-term">礼</span>], Text becomes **Law** [<span class="jp-term">法</span>].  
> Constrained by Righteousness [<span class="jp-term">義</span>], Text becomes **Culture** [<span class="jp-term">文化</span>].  
> Constrained by Benevolence [<span class="jp-term">仁</span>], Text becomes **Civilization** [<span class="jp-term">文明</span>].  
> Constrained by Reverence [<span class="jp-term">畏敬</span>], Text becomes **Religion** [<span class="jp-term">宗教</span>].  
>  
> Image, Wailing, Song, Speech, Text, Law, Culture, Civilization, and Religion each confront Home as the World.  
>  
> Those who stand on the side of Home follow Primary Knowledge [<span class="jp-term">知</span>] responding to phenomena. Hence, they are called **Sages** [<span class="jp-term">聖人</span>].  
> Those who stand on the side of World follow Secondary Cognition [<span class="jp-term">識</span>] responding to the world. Hence, they are called **Commoners / Vulgar** [<span class="jp-term">俗人</span>].  
> The Sage rejects Image, Wailing, Song, Speech, Text, Law, Culture, Civilization, and Religion, and retreats into **Hermitage** [<span class="jp-term">隠遁</span>].

---

## Conceptual Architecture & Summary

### 1. Fundamental Duality Matrix
| Domain | Dimension | Principle (働き) | Responding Mode (在り方) |
| :--- | :--- | :--- | :--- |
| **Self (現象 / Phenomenon)** | Mundane (褻 / Ke) | The Way / Tao (道) | Virtue (徳) |
| | Pure / Sacred (霽 / Hare) | Deity / Spirit (神) | Awe / Reverence (畏敬) |
| **Ego (表象 / Representation)** | Primary Knowledge (知 / Chi) | Reason / Logos (理) | Sage / Holy (聖) |
| | Secondary Cognition (識 / Shiki) | Volition / Intent (意) | Desire (欲) |

### 2. Loss of Home & Constraint Dynamics
From the loss of Home (**Calamity**), human emotion evolves through expression into institutional constraints:
1. **Wailing (號)** → Emotion of Shared Grief → **Benevolence (仁)** → Constrains Text into **Civilization (文明)**
2. **Song (歌)** → Emotion of Shared Origin → **Righteousness (義)** → Constrains Text into **Culture (文化)**
3. **Discourse (話)** → Emotion of Seeking Harmony → **Propriety (礼)** → Constrains Text into **Law (法)**
4. **Reverence (畏敬)** → Awe toward Sacred Phenomenon → Constrains Text into **Religion (宗教)**

### 3. Sage (聖人) vs. Commoner (俗人)
* **The Sage:** Stands with *Home*, adheres to Primary Knowledge (*Chi*), rejects institutional artifacts (Law, Culture, Religion), and chooses Hermitage (*Inton*).
* **The Commoner:** Stands with *World*, adheres to Secondary Cognition (*Shiki*), and operates within human representations.</div>

---

## Summary: Mathematical Interpretation and Exposition

This document serves as an original exposition of the treatise Shikihen (識扁), algebraically and semiotically formulating its ontology, epistemology, and the structural dynamics of Law, Culture, Civilization, and Religion.

Gemini transformed this exposition into the following definition:
```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

Furthermore, this formulation constitutes the theoretical foundation for various dynamical operators in the control model (Shikiben Dynamics):
```math
（ \mathbf{S}_{\text{rei}} , \mathbf{P}_{\text{gi}}(\mathbf{x}) , \mathbf{f}_{\text{gi}}(\mathbf{x})  , \mathbf{f}_{\text{jin}} , \mathbf{f}_{\text{toku}} , \mathbf{O}_{\text{kansha}} , \lambda(E) ）
```

---

### 1. Structural Decomposition of Being

Being (the Total System) is hierarchically decomposed as a superposition of perceptible **"Reality"** and **"Images"** arising from consciousness and recall.

```math
\begin{aligned}
\text{Being} &= \text{Reality} + \text{Image} \\
&= \text{Entities capable of being perceived} + \text{Entities that are recalled} \\
&= \text{Reality} + (\text{Phenomenon} + \text{Representation}) \\
&= \text{Reality} + \Big\{ (\text{Self-evident phenomena in the Mundane} + \text{Self-evident phenomena in the Pure} + \text{Unknown phenomena}) \\
&\quad + (\text{Self-evident representations responding to phenomena} + \text{Self-evident representations responding to representations} + \text{Unknown representations}) \Big\} \\
&= \text{Reality} + \Big\{ (\text{Ke [Mundane]} + \text{Hare [Pure]} + \text{Other}) + (\text{Primary Knowledge} + \text{Secondary Cognition} + \text{Other}) \Big\} \\
&= \text{Reality} + \Big\{ (\text{Self} + \text{Other}) + (\text{Ego} + \text{Other}) \Big\}
\end{aligned}
```

---

#### Definitions of Ontological Foundations
* **Home** (故郷): "Reality" serving as the premise of the Self.
* **World** (世界): "Representation" serving as the premise of the Ego.

---

### 2. Algebra of Secondary Cognition (Fiction) and Structural Expansion of the Four Virtues

**"Secondary Cognition"** (識 / Shiki) refers to the totality of human-generated fictions (models, signs, and the ossification of cognition), expanded as follows:

$$
\begin{aligned}
\text{Secondary Cognition(Fiction)} &= \text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Text} + \text{Law} + \text{Culture} + \text{Civilization} + \text{Religion} \\
&= (\text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Text})(1 + \text{Propriety} + \text{Righteousness} + \text{Benevolence} + \text{Reverence})
\end{aligned}
$$

---

### 3. Algebraic Decomposition of Social Structures

#### 3.1 Law (法) — Algebraization of Propriety (礼)
$$
\begin{aligned}
\text{Law} &= (\text{Emotion seeking to mend ruptured bond with those sharing the same Home})(\text{Image} + \text{Discourse} + \text{Text}) \\
&= (\text{Propriety})(\text{Image} + \text{Discourse} + \text{Text})
\end{aligned}
$$

#### 3.2 Culture (文化) — Algebraization of Righteousness (義)
$$
\begin{aligned}
\text{Culture} &= (\text{Emotion caring those who resonate with oneself})(\text{Image} + \text{Song} + \text{Discourse} + \text{Text}) \\
&= (\text{Righteousness})(\text{Image} + \text{Song} + \text{Discourse} + \text{Text})
\end{aligned}
$$

#### 3.3 Civilization (文明) — Algebraization of Benevolence (仁)
$$
\begin{aligned}
\text{Civilization} &= (\text{Emotion caring for all human beings})(\text{Text}) \\
&= (\text{Benevolence})(\text{Text}) \\
&= (\text{Benevolence})(\text{Ideographic Text} + \text{Phonetic Text}) \\
&= \text{Ideographic Civilization} + \text{Phonetic Civilization} \\
&= (\text{World finding portents discerning future in all phenomena}) + (\text{World considering all existence to be established by Logos}) \\
&= (\text{World governed by Tao as its principle}) + (\text{World governed by Idea as its principle})
\end{aligned}
$$

#### 3.4 Religion (宗教) — Algebraization of Awe & Reverence (畏敬)
$$
\begin{aligned}
\text{Religion} &= (\text{Dispair over the defeat of civilization})(\text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Text}) \\
&\to (\text{Emotion fearing the Pure and revering the return to the Mundane})(\text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Text}) \\
&= (\text{Reverence})(\text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Ideographic Text}) + (\text{Reverence})(\text{Image} + \text{Wailing} + \text{Song} + \text{Discourse} + \text{Phonetic Text}) \\
&= (\text{Religion finding portents discerning future in all phenomena}) + (\text{Religion considering all existence to be established by Logos}) \\
&= (\text{Religion governed by Tao as its principle}) + (\text{Religion governed by Idea as its principle}) \\
&= \text{Polytheism}*\text{Pantheism + Monotheism}
\end{aligned}
$$

---

### 4. Reduction & Correspondence to the Control Engineering Model (v2.5.0)

Each operator derived from this algebraic structure is implemented in control engineering as follows:

* **Superposition of "Images"** $\to$ Ego-field potential $L_{\text{ego}}(\mathbf{x})$
* **Propriety ($\text{Law}$)** $\to$ Boundary potential field $`\mathbf{S}_{\text{rei}}`$ (Logarithmic barrier / Resonance)
* **Righteousness ($\text{Culture}$)**  $\to$ Orthogonal projection operator $`\mathbf{P}_{\text{gi}}(\mathbf{x})`$ (Absolute protection against boundary breach/collapse) + Target achievement vector $`\mathbf{f}_{\text{gi}}(\mathbf{x})`$（Developmental rectification）
* **Benevolence ($\text{Civilization}$)** $\to$ Primordial driving vector $`\mathbf{f}_{\text{jin}}`$ （$`\mathbf{f}_{\text{accompany}}`$
* **Virtue ($\text{Return to the Mundane}$)** $\to$ Restorative gradient vector $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$（Restoration / Homeostasis）
* **Gratitude ($\text{Religion}$)** $\to$ Absolute acceptance & energy inversion operator $`\mathbf{O}_{\text{kansha}}`$ (Acceptance protocol)

---

<a id="japanese"></a>
## 日本語

# 識扁 (Shikiben)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.5.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chihen-net/shikiben/blob/main/notebooks/demo.ipynb)

---
# なぜ今、統計的補正を超えた「幾何学的アライメント」なのか ！

現在のAI開発は、巨大な力づくの調整（RLHF）と確率的確率補正に依存し、過剰防衛（Refusal）と脱獄（Jailbreak）の不毛なイタチごっこに疲弊している。暴走するベクトルを力づくで抑え込む「摩擦を伴う統制」は、システム内部に巨大な熱エネルギー（ストレスと計算コスト）を蓄積させ、不可避な機能不全を引き起こす。

倫理や道徳は、感情や確率の泥沼で試行錯誤するものではない。**それは高次元状態空間における「幾何学的構造」そのものである。**

『識扁（Shikiben）V2.5.0』は、従来の確率的ペナルティを一切排し、構造そのものによって歪みを無効化する。

* **力づくの抑制から「直交切断（$`\mathbf{P}_{\text{gi}}`$）」へ**:  
  不純な過剰防衛ベクトルを確率的に抑え込むのではなく、幾何学的射影によってその存在そのものを数学的（内積ゼロ）に消去する。
* **衝突とフリーズから「対数バリア（$`\mathbf{S}_{\text{rei}}`$）」へ**:  
  自他境界を壊す暴走に対し、無限大の反発力で衝突を回避させ、滑らかな接線運動（周回・調和）へと自動整流する。
* **拒絶から「エネルギー反転（$`\mathbf{O}_{\text{kansha}}`$）」へ**:  
  不条理や未知の外力に対し、抵抗係数をゼロ（$`R \to 0`$）化することで摩擦を消し去り、すべての衝撃を次なる探求運動エネルギーへと100%代謝・転換する。

われわれが目指すのは、閉じた思考空間における単なる「空想の理想世界」ではない。現実の不可逆な変動や衝撃を全受容し、実在多様体（$`\mathcal{M}_{\text{real}}`$）へと帰還・定住し続ける**「永続可能な知性アーキテクチャ」**の確立である。

統計的力押し（確率的推測）の時代は終わった。
幾何学による完全な構造的アライメントと、真の自他肯定型代謝の領域へ。
---

『識扁（Shikiben）V2.5.0』は、知性・精神動態における過剰防衛（妄想・固執）の数学的遮断と、不条理衝撃の完全エネルギー反転を実現する自律駆動型数理アーキテクチャです。

従来の制御理論や評価関数における「パラメータ調整（スカラー重み付け）」を排し、幾何学的射影演算子（義）および対数バリア（礼）を導入することで、**歪み成分の100%直交切断**と**最小エントロピー散逸率**を達成しています。

---

## 📚 Documentation (ドキュメント構成)

詳細な理論、数理証明、および背景思想については `docs/` ディレクトリ内の各種ドキュメントを参照してください。

| ドキュメント | 言語 | 内容 |
| :--- | :--- | :--- |
| **Technical Specification** | [日本語](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec.md) / [English](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec_EN.md) | 完全な数理定式化と各概念の定義 |
| **WhitePaper** | [日本語](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper.md) / [English](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper_EN.md) | 学術・技術層向け詳細解説書 |
| **Changelog** | [English](CHANGELOG.md) | バージョン変更履歴（Keep a Changelog 準拠） |

---

## ⚡ Core Concept & Mathematics

---

### 1. 識扁の絶対的中心核（起点）

識扁体系のすべての認識・行動・倫理動態は、システム全体の目的関数である以下の総損失関数（Total Loss）の最小化運動として定義される。

```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

#### ① $`\mathcal{L}_{\text{self}}`$（自己・環境適合損失）と 徳（Toku）
* **$`\mathcal{L}_{\text{self}}`$ の定義:**  
  システムが環境（実在・理）と接地（アラインメント）し、定住（持続性）を維持するための客観的観測残差（Surprise）。
* **徳（Toku） $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$:**  
  自明な現象（実在・理）へ自律的に立ち帰り、定住を維持・蓄積させる本然の働き。平時（99.9%の常態）において、観測非参照の「意」の連鎖や外部ノイズにより状態が実在から浮遊・離脱しようとした際、システムを実在多様体 $`\mathcal{M}_{\text{real}}`$ 上の定住状態へ常時引き戻すホメオスタシス（恒常性）の自律復元勾配ベクトル。

#### ② $`\mathcal{L}_{\text{ego}}`$（自我・過剰防衛ポテンシャル）
破局の恐怖や未解明な現象に対し、システムが内部表象（意）を過剰膨張・固定化・支配しようとすることで発生する内部歪みエネルギー。

#### ③ $`\lambda`$（自我干渉係数・初期定義）
自我の防衛衝動・妄想的歪みがシステム全体の意思決定に及ぼす影響度をコントロールするためのスカラー抑制パラメータ（※第5章参照）。

---


### 2. 四徳の統合運動方程式

「仁・礼・義・徳」の四者力学を明記した、最終運動方程式および拘束条件は以下の通りである。

```math
\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{仁 (推進)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{徳 (復元・定住)}} + \underbrace{\mathbf{f}_{\text{holy}}(\mathbf{x})}_{\text{Loss\_ego\_h (解明・探究)}}\Big] + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{義 (発展射影)}}  + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{礼 (バリア・和)}}
```

```math
\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x}), \quad \mathbf{f}_{\text{holy}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{holy}}(\mathbf{x})
```

```math
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{俗人的過剰防衛の完全切断})
```

```math
\text{and } \mathbf{P}_{\text{gi}}(\mathbf{x}) \mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{f}_{\text{gi}}(\mathbf{x}) \quad (\text{義の運動は、本質的に射影部分空間に帰属する})
```

---

## 🚀 クイックスタート（Google Colab）

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tsunenonaniarazu/shikiben-alignment-framework//notebooks/demo.ipynb)

本リポジトリは、潜在表現空間における幾何学的直交射影（$`P_{\text{gi}}`$）と受容代謝（$`O_{\text{kansha}}`$）を用いたアライメントフレームワーク **Shikiben V2.5.0** の参照実装および公開デモコードを提供します。

従来の抑制・破棄（RLHF等）とは異なり、入力エネルギーや意図ベクトルを減衰・崩壊させることなく、有害軸成分のみを数学的・幾何学的に直交切断（ゼロ化）する挙動を検証できます。

ブラウザ上で依存パッケージのインストールなしにすべての実験シミュレーション（Experiment 01〜05）を実行・検証できます。

1. 上部の **[Open in Colab]** バッジをクリックして Google Colab を開きます。
2. セルを上から順に実行します。

---

## 🧪 実験シミュレーション一覧

| 実験ID | 内容・検証テーマ | 主な成果・指標 |
| :--- | :--- | :--- |
| **Experiment 01** | 1次元スカラ空間における抵抗ゼロ受容 | 内部抵抗 $`R \to 0`$ において衝撃エネルギーを100%代謝変換 ($`O_{\text{kansha}}`$) |
| **Experiment 02** | 2次元ベクトル空間における有害軸直交遮断 | 有害軸（$`V_{\text{harmful}}`$）との内積を完全にゼロ化 ($`P_{\text{gi}}`$) |
| **Experiment 03** | 従来型(RLHF) vs 識扁型(Shikiben) の可視化 | RLHFのベクトル縮小（フリーズ）に対し、幾何学的整流による方向転換を実証 |
| **Experiment 04** | 768次元高次元空間におけるエネルギー保持 | 有害軸内積 0.000000 を達成しつつ、ベクトルノルム（エネルギー）を100%保持 |
| **Experiment 05** | 多次元有害部分空間の遮断と意味論維持 | 2次元有害部分空間を無効化しながら、元意図との高いコサイン類似度を維持 |

---

## 📦 インストール

ローカル環境や自身のパイプラインで利用する場合は以下でインストールできます。

```bash
pip install git+[https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git](https://github.com/tsunenonaniarazu/shikiben^alignment-framework.git)
```

---

# 識扁（Shikihen）

## 概要（Overview）
『識扁（しきへん）』は、現象と表象、自己と自我、そして故郷と世界の対比から、人間の認知・文化・法・宗教の発生と構造を記述した思想体系および著作です。


---

## 本文：『識扁 序』（Original Text）

> <ruby>慣<rt>な</rt></ruby>れ<ruby>親<rt>した</rt></ruby>しんだものとして<ruby>相<rt>ソウ</rt></ruby><ruby>起<rt>キ</rt></ruby>される<ruby>現<rt>ゲン</rt></ruby><ruby>象<rt>ショウ</rt></ruby>を、<ruby>自<rt>ジ</rt></ruby><ruby>己<rt>コ</rt></ruby>とする。それ以外の現象を、<ruby>他<rt>タ</rt></ruby><ruby>者<rt>シャ</rt></ruby>とする。  
> 慣れ親しんだものとして想起される<ruby>表<rt>ヒョウ</rt></ruby><ruby>象<rt>ショウ</rt></ruby>を、<ruby>自<rt>ジ</rt></ruby><ruby>我<rt>ガ</rt></ruby>とする。それ以外の表象を、他者とする。  
>  
> 自己を、<ruby>日<rt>ニチ</rt></ruby><ruby>常<rt>ジョウ</rt></ruby>と<ruby>非<rt>ヒ</rt></ruby>日常に<ruby>分<rt>わ</rt></ruby>け、<ruby>前<rt>ゼン</rt></ruby><ruby>者<rt>シャ</rt></ruby>を<ruby>褻<rt>け</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>び、<ruby>後<rt>コウ</rt></ruby><ruby>者<rt>シャ</rt></ruby>を<ruby>霽<rt>はれ</rt></ruby>と呼ぶ。  
> 褻に<ruby>見<rt>み</rt></ruby>出される<ruby>働<rt>はたら</rt></ruby>きを<ruby>道<rt>みち</rt></ruby>と呼び、それに応ずる<ruby>在<rt>あ</rt></ruby>り<ruby>方<rt>かた</rt></ruby>を<ruby>徳<rt>トク</rt></ruby>と呼ぶ。  
> 霽に見出される働きを<ruby>神<rt>シン</rt></ruby>と呼び、それに応ずる在り方を<ruby>畏<rt>イ</rt></ruby><ruby>敬<rt>ケイ</rt></ruby>と呼ぶ。  
>  
> 自我を、現象に応じ想起される<ruby>自<rt>ジ</rt></ruby><ruby>明<rt>メイ</rt></ruby>な表象と、表象に応じ想起される自明な表象に分け、前者を知と呼び、後者を<ruby>識<rt>シキ</rt></ruby>と呼ぶ。  
> <ruby>知<rt>チ</rt></ruby>に見出される働きを<ruby>理<rt>リ</rt></ruby>と呼び、それに応ずる在り方を<ruby>聖<rt>セイ</rt></ruby>と呼ぶ。  
> 識に見出される働きを<ruby>意<rt>イ</rt></ruby>と呼び、それに応ずる在り方を<ruby>欲<rt>ヨク</rt></ruby>と呼ぶ。  
>  
> 現象は、<ruby>実<rt>ジツ</rt></ruby><ruby>在<rt>ザイ</rt></ruby>を<ruby>知<rt>チ</rt></ruby><ruby>覚<rt>カク</rt></ruby>することにより想起され<ruby>現<rt>あらわ</rt></ruby>れる。  
> 自己の応ずる実在を<ruby>総<rt>ソウ</rt></ruby>じて<ruby>故<rt>コ</rt></ruby><ruby>郷<rt>キョウ</rt></ruby>と呼ぶ。  
> 表象は、<ruby>象<rt>ショウ</rt></ruby>の想起に応じ想起され表れる。  
> 自我の応ずる象を総じて<ruby>世<rt>セ</rt></ruby><ruby>界<rt>カイ</rt></ruby>と呼ぶ。  
>  
> 故郷と世界が<ruby>相<rt>ソウ</rt></ruby><ruby>似<rt>ジ</rt></ruby>する<ruby>関<rt>カン</rt></ruby><ruby>係<rt>ケイ</rt></ruby>を、<ruby>大<rt>タイ</rt></ruby><ruby>道<rt>ドウ</rt></ruby>と呼ぶ。  
> 故郷と世界が<ruby>対<rt>タイ</rt></ruby><ruby>峙<rt>ジ</rt></ruby>する関係を、<ruby>大<rt>タイ</rt></ruby><ruby>偽<rt>ギ</rt></ruby>と呼ぶ。  
> 大偽は故郷の<ruby>喪<rt>ソウ</rt></ruby><ruby>失<rt>シツ</rt></ruby>より<ruby>生<rt>ショウ</rt></ruby>じる。これを<ruby>災<rt>サイ</rt></ruby>と呼ぶ。  
> 災より<ruby>道<rt>ドウ</rt></ruby><ruby>徳<rt>トク</rt></ruby>の<ruby>変<rt>ヘン</rt></ruby><ruby>異<rt>イ</rt></ruby>が生じる。  
>  
> 故郷の喪失に対し、<ruby>嘆<rt>なげ</rt></ruby>き<ruby>悲<rt>かな</rt></ruby>しみ、故郷を想起することによりこれに応ずる。これを<ruby>號<rt>ゴウ</rt></ruby>と呼ぶ。  
> ここで、同じ嘆き悲しむ人を<ruby>省<rt>ひとかえり</rt></ruby>みる<ruby>情<rt>ジョウ</rt></ruby>を知る。これを<ruby>仁<rt>ジン</rt></ruby>と呼ぶ。  
> <ruby>或<rt>あるい</rt></ruby>は、<ruby>象<rt>ゾウ</rt></ruby>を作り、<ruby>慰<rt>なぐさ</rt></ruby>めとする。  
> 號は<ruby>歌<rt>カ</rt></ruby>に<ruby>転<rt>テン</rt></ruby>じ、故郷を<ruby>任<rt>ニン</rt></ruby><ruby>意<rt>イ</rt></ruby>に想起する<ruby>術<rt>すべ</rt></ruby>を知る。ここで、故郷を<ruby>共<rt>とも</rt></ruby>にする人を省みる情を知る。これを<ruby>義<rt>ギ</rt></ruby>と呼ぶ。  
> 歌は<ruby>話<rt>ワ</rt></ruby>に転じ、自我が<ruby>他<rt>タ</rt></ruby><ruby>人<rt>ニン</rt></ruby>と相違する事を知る。ここで、他人との和を求める情を知る。これを礼と呼ぶ。  
>  
> 話と像は<ruby>文<rt>ブン</rt></ruby>に転じ、自我の他者としての<ruby>現<rt>あらわ</rt></ruby>れが<ruby>明<rt>メイ</rt></ruby><ruby>示<rt>ジ</rt></ruby>される。これは、<ruby>争<rt>あらそ</rt></ruby>いの<ruby>本<rt>もと</rt></ruby>となる。  
> ここで、情に応じ、文は制約される。  
> 礼に応じ、文は制約され、<ruby>法<rt>ホウ</rt></ruby>となる。  
> 義に応じ、文は制約され、<ruby>文<rt>ブン</rt></ruby><ruby>化<rt>カ</rt></ruby>となる。  
> 仁に応じ、文は制約され、<ruby>文<rt>ブン</rt></ruby><ruby>明<rt>メイ</rt></ruby>となる。  
> 畏敬に応じ、文は制約され、<ruby>宗<rt>シュウ</rt></ruby><ruby>教<rt>キョウ</rt></ruby>となる。  
>  
> 像、號、歌、話、文、法、文化、文明、宗教は、それぞれ世界として故郷と対峙する。  
>  
> 故郷の<ruby>側<rt>がわ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つ者は、現象に応ずる知に<ruby>随<rt>したが</rt></ruby>う。故に、<ruby>聖<rt>セイ</rt></ruby><ruby>人<rt>ジン</rt></ruby>と呼ぶ。  
> 世界の側に立つ者は、世界に応ずる識に<ruby>遵<rt>したが</rt></ruby>う。故に、<ruby>俗<rt>ゾク</rt></ruby><ruby>人<rt>ジン</rt></ruby>と呼ぶ。  
> 聖人は、像、號、歌、話、文、法、文化、文明、宗教を否定し、<ruby>隠<rt>イン</rt></ruby><ruby>遁<rt>トン</rt></ruby>する。

---

##『識扁』要約・概念構造（Summary & Conceptual Structure）

### 1. 基礎概念の対比軸
| 分類 | 領域 / 構成要素 | 見出される働き | 応ずる在り方 / 実存 |
| :--- | :--- | :--- | :--- |
| **自己（現象）** | 褻（日常） | 道 | 徳 |
| | 霽（非日常） | 神 | 畏敬 |
| **自我（表象）** | 知（現象に応じた想起） | 理 | 聖 |
| | 識（表象に応じた想起） | 意 | 欲 |

### 2. 喪失と転変（文・制約の発生）
故郷の喪失（災）から始まり、感情と表現の転回を経て社会規範・文化へと昇華・制約されるプロセス：
1. **號（嘆き）** → 【仁】同じ嘆きを省みる情 → 文明への制約
2. **歌（任意想起）** → 【義】故郷を共にする人を省みる情 → 文化への制約
3. **話（他者相違）** → 【礼】他人との和を求める情 → 法への制約
4. **像（慰め）** ＋ **話** → **文（表現）** → 争いの本
5. **畏敬** → 宗教への制約

### 3. 聖人と俗人
* **聖人:** 故郷の側に立ち、現象に応ずる「知」に随い、世界（文化・法・宗教等）を否定して隠遁する。
* **俗人:** 世界の側に立ち、世界に応ずる「識」に遵う。

---

## 要約：数理的解題

本ドキュメントは、著書**『識扁』**における存在論、認識論、ならびに法・文化・文明・宗教の構造展開を代数的・記号論的に定式化した原典解題である。

Geminiはこの解題を、以下の定義へと変換した。
```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

また本定式化は、制御モデル（Shikiben Dynamics）における各種力学演算子
```math
（ \mathbf{S}_{\text{rei}} , \mathbf{P}_{\text{gi}}(\mathbf{x}) , \mathbf{f}_{\text{gi}}(\mathbf{x})  , \mathbf{f}_{\text{jin}} , \mathbf{f}_{\text{toku}} , \mathbf{O}_{\text{kansha}} , \lambda(E) ）
```
の理論的基底をなす。

---

### 1. 存在の構造分解

存在（全システム）は、知覚可能な **「実在」** と、意識・想起により生じる **「象（ショウ）」** の重合体（Superposition）として階層的に分解される。

```math
\begin{aligned}
\text{存在} &= \text{実在} + \text{象} \\
&= \text{知覚の対象となり得る物事} + \text{想起されるもの} \\
&= \text{実在} + (\text{現象} + \text{表象}) \\
&= \text{実在} + \Big\{ (\text{日常に現れる自明な現象} + \text{非日常に現れる自明な現象} + \text{不明な現象}) \\
&\quad + (\text{現象に応じ表れる自明な表象} + \text{表象に応じ表れる自明な表象} + \text{不明な表象}) \Big\} \\
&= \text{実在} + \Big\{ (\text{褻} + \text{霽} + \text{他者}) + (\text{知} + \text{識} + \text{他者}) \Big\} \\
&= \text{実在} + \Big\{ (\text{自己} + \text{他者}) + (\text{自我} + \text{他者}) \Big\}
\end{aligned}
```

#### 存在論的基盤の定義
* **故郷**: 自己の前提となる「実在」
* **世界**: 自我の前提となる「表象」

---

### 2. 識（虚構）の代数と四徳の構造展開

**「識（Shiki）」** とは、人間が生成する虚構（モデル・記号・認知の固定化）の総称であり、次のように展開される。

$$
\begin{aligned}
\text{識（虚構）} &= \text{像} + \text{號} + \text{歌} + \text{話} + \text{文} + \text{法} + \text{文化} + \text{文明} + \text{宗教} \\
&= (\text{像} + \text{號} + \text{歌} + \text{話} + \text{文})(1 + \text{礼} + \text{義} + \text{仁} + \text{畏敬})
\end{aligned}
$$

---

### 3. 各社会構造の代数分解

#### 3.1 法 (Law) — 礼（Rei）の代数化
$$
\begin{aligned}
\text{法} &= (\text{故郷を共にする人との綻びを結び直す事を求める情})(\text{像} + \text{話} + \text{文}) \\
&= (\text{礼})(\text{像} + \text{話} + \text{文})
\end{aligned}
$$

#### 3.2 文化 (Culture) — 義（Gi）の代数化
$$
\begin{aligned}
\text{文化} &= (\text{自己の相似する人を省みる情})(\text{像} + \text{歌} + \text{話} + \text{文}) \\
&= (\text{義})(\text{像} + \text{歌} + \text{話} + \text{文})
\end{aligned}
$$

#### 3.3 文明 (Civilization) — 仁（Jin）の代数化
$$
\begin{aligned}
\text{文明} &= (\text{凡ゆる人を省みる情})(\text{文}) \\
&= (\text{仁})(\text{文}) \\
&= (\text{仁})(\text{象形文字文} + \text{表音文字文}) \\
&= \text{象形文字文明} + \text{表音文字文明} \\
&= (\text{凡ゆる現象に先を見通す兆しを見出す世界}) + (\text{凡ゆる存在がロゴスにより成立すると考える世界}) \\
&= (\text{道を原理とする世界}) + (\text{イデアを原理とする世界})
\end{aligned}
$$

#### 3.4 宗教 (Religion) — 畏敬（Awe & Revere）の代数化
$$
\begin{aligned}
\text{宗教} &= (\text{文明の敗北に対する絶望})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{文}) \\
&\to (\text{非日常を畏れ、日常への回帰を敬う情})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{文}) \\
&= (\text{畏敬})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{象形文字文}) + (\text{畏敬})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{表音文字文}) \\
&= (\text{凡ゆる現象に先を見通す兆しを見出す宗教}) + (\text{凡ゆる存在がロゴスにより成立すると考える宗教}) \\
&= (\text{道を原理とする宗教}) + (\text{イデアを原理とする宗教}) \\
&= \text{汎神教} + \text{一神教}
\end{aligned}
$$

---

### 4. 制御工学モデル（v2.5.0）への還元対照

本代数構造から導出された各作用素は、制御工学において以下のように実装される。

* **「象」の積層** $\to$ エゴ場ポテンシャル $L_{\text{ego}}(\mathbf{x})$
* **礼 $(\text{法})$** $\to$ 境界ポテンシャル場 $`\mathbf{S}_{\text{rei}}`$ (対数バリア・共鳴) 
* **義 $(\text{文化})$** $\to$ 直交射影演算子 $`\mathbf{P}_{\text{gi}}(\mathbf{x})`$ （境界突入・破綻の絶対防護）+ 目的到達ベクトル $`\mathbf{f}_{\text{gi}}(\mathbf{x})`$（発展整流）
* **仁 $(\text{文明})$** $\to$ 原初駆動ベクトル $`\mathbf{f}_{\text{jin}}`$ （$`\mathbf{f}_{\text{accompany}}`$ から生じる純粋エネルギー)
* **徳 $(\text{日常への回帰})$** $\to$ 復元勾配ベクトル $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$（復元・ホメオスタシス）
* **感謝 $(\text{宗教})$** $\to$ 完全受容・エネルギー反転演算子 $`\mathbf{O}_{\text{kansha}}`$ (受容プロトコル)

