# Shikiben (識扁)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.4.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

**Shikiben (識扁)** is a novel adaptive control paradigm that reinterprets Eastern ontological concepts (*Authentic Reality* vs. *Ego-Distortion*) and virtue ethics (*Rei*, *Gi*, *Jin*, and *Taidou*) into modern geometric mechanics, Lagrangian dynamics, non-holonomic projections, and adaptive systems theory.

It automatically suppresses and insulates systems from overfitting and rigidity (distortion caused by "Ego") while "metabolizing" that information to evolve a safe reference axis ("Taidou") in real time.

---

## 📚 Documentation Structure

For in-depth mathematical formulations, proofs, and foundational philosophy, refer to the documentation suite in the `docs/` directory:

| Document | Language | Content |
| :--- | :--- | :--- |
| **Technical Specification** | [English](docs/SPECIFICATION_EN.md) / [日本語](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec.md) | Complete mathematical formulation, Euler-Lagrange derivations, and stability parameter bounds. |
| **WhitePaper** | [English](docs/WHITEPAPER_EN.md) / [日本語](shikiben-v2.5/docs/whitepaper_v2_5_ja.md) | Background challenges, conceptual synthesis of philosophy and mechanics, and application use cases. |
| **Changelog** | [English](CHANGELOG.md) | Full version history following the *Keep a Changelog* standard. |

---

## ⚡ Core Concept & Mathematics

### 1. Superposition Lagrangian of Existence

$$L_{\text{total}}(\mathbf{x}, \dot{\mathbf{x}}, t) = \Big( L_{\text{self}}(\mathbf{x}, \dot{\mathbf{x}}) + \gamma_{\text{d}} \cdot L_{\text{taido}}(\mathbf{x}, \mathbf{x}_{\text{safe}}(t)) \Big) + \lambda(\text{Virtue}) \cdot L_{\text{ego}}(\mathbf{x})$$

* **$L_{\text{self}}$ (Authentic Reality):** The baseline state governing natural motion and relational dynamics.
* **$L_{\text{ego}}$ (Ego-Distortion):** Potential energy resulting from local overfitting, bias, or rigid model attachments.
* **$\lambda(\text{Virtue})$ (Virtue Scaling):** A dynamic phase transition parameter that automatically neutralizes harmful $L_{\text{ego}}$ gradients.

### 2. Unified Four-Virtue Equation of Motion

$$\dot{\mathbf{x}} = \mathbf{P}_{\text{rei}}(\mathbf{x}) \Big[ \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma_{\text{d}} \, \mathbf{g}_{\text{Taidou}}(\mathbf{x}, \mathbf{x}_{\text{safe}}(t)) - \lambda(\text{Virtue}) \cdot \nabla_{\mathbf{x}} L_{\text{ego}}(\mathbf{x}) \Big] + \mathbf{S}_{\text{jin}}(\mathbf{x})$$

* **Rei ($\mathbf{P}_{\text{rei}}$):** Two-stage orthogonal projection operator filtering out forces directed into hazard boundaries, redirecting motion into smooth tangential sliding.
* **Gi ($\mathbf{f}_{\text{gi}}$):** Directional force driving the system toward its primary target intent.
* **Jin ($\mathbf{S}_{\text{jin}}$):** Multi-agent interaction potential balancing short-range repulsion and long-range alignment.
* **Taidou ($\mathbf{g}_{\text{Taidou}}$ & $\mathbf{x}_{\text{safe}}$):** Dynamic self-adapting reference axis and restoring gradient updated via metabolic absorption.

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
cd shikiben-v2.5/simulations/

# Run the simulation engine
shikiben_simulation_01.py
shikiben_simulation_02.py
```

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

</body>
</html>
"""
