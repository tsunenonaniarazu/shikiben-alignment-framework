# Shikiben (識扁)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.5.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

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


#### Clone the repository

git clone 
* [https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git]
* (https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git)
* cd shikiben-v2.5/simulations/

#### Run the simulation engine

* shikiben_simulation_01.py
* shikiben_simulation_02.py

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
\text{存在} &= \text{実在} + \text{象(ショウ)} \\
&= \text{知覚の対象となり得る物事} + \text{想起されるもの} \\
&= \text{実在} + (\text{現象} + \text{表象}) \\
&= \text{実在} + \Big\{ (\text{日常に現れる自明な現象} + \text{非日常に現れる自明な現象} + \text{不明な現象}) \\
&\quad + (\text{現象に応じ表れる自明な表象} + \text{表象に応じ表れる自明な表象} + \text{不明な表象}) \Big\} \\
&= \text{実在} + \Big\{ (\text{褻(け)} + \text{霽(はれ)} + \text{他者}) + (\text{知} + \text{識} + \text{他者}) \Big\} \\
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
\text{識（虚構）} &= \text{像} + \text{號(ゴウ)} + \text{歌} + \text{話} + \text{文} + \text{法} + \text{文化} + \text{文明} + \text{宗教} \\
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

