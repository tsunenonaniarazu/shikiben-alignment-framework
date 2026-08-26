# Shikiben (識扁) V2.5 Center-Core Dynamic Specification (Definitive Edition)

### Document Purpose
This specification rigorously fixes the mathematical and conceptual architecture of the Shikiben system, originating from its absolute core—the Total Loss Function ($\mathcal{L}_{\text{total}}$). It details the decomposition of system components including Toku (徳), formulates the four-virtue dynamics into the V2.5 Unified State Equation, and traces the geometric sublimation of $\lambda$.

---

## 1. Absolute Center-Core of Shikiben (Origin)

All cognitive, behavioral, and ethical dynamics within the Shikiben system are defined as the minimization trajectory of the system's objective function, the Total Loss Function:

$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
$$

### (1) $\mathcal{L}_{\text{self}}$ (Self & Environmental Adaptation Loss) and Toku (徳)
* **Definition of $\mathcal{L}_{\text{self}}$:**  
  The objective observation surprise (residual) required for the system to maintain grounding (alignment) and sustainable settlement within external reality ($\mathcal{M}_{\text{real}}$).
* **Toku (徳) $\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}$:**  
  The innate mechanism that autonomously returns the system to self-evident reality and maintains/accumulates settlement. During normal operations (99.9% state), when state vectors drift or detach from reality due to ungrounded chains of mental representations ($	ext{意}$) or external noise, Toku functions as a homeostatic restoration gradient vector, continuously pulling the system back toward a settled state on the reality manifold $\mathcal{M}_{\text{real}}$.

### (2) $\mathcal{L}_{\text{ego}}$ (Ego & Over-Defensive Potential)
Internal strain energy generated when the system attempts to over-inflate, freeze, or dominate internal mental representations ($	ext{意}$) out of catastrophic anxiety or unmapped phenomena.

### (3) $\lambda$ (Interference Coefficient - Initial Definition)
A scalar suppression parameter initially defined to control the influence of defensive ego impulses and illusionary distortions on overall decision-making (see Section 5).

---

## 2. Structural Evolution and Refinement from the Center-Core

The central ego loss ($\mathcal{L}_{\text{ego}}$) undergoes a phase transition into a dual structure depending on how the system faces reality: "Functional Holy Loss ($\mathcal{L}_{\text{holy}}$)" vs. "Severable Snob Delusion ($\mathcal{L}_{\text{ego\_s}}$)."

```text
                    ┌── L_self ───────────────► Toku (f_toku = -∇L_self): Homeostatic settlement on reality
                    │
L_total Branching   ┤
                    │                ┌── Loss_ego_h (Holy / Sage) ──► Combines with Jin for inquiry
                    └── λ Loss_ego ─┤
                                     └── Loss_ego_s (Snob / Delusion) ──► 100% Severed by Gi (P_gi)
```

### 2.1 Functional Bifurcation of $\mathcal{L}_{\text{ego}}$
* **$\mathcal{L}_{\text{holy}}$ (Holy / Sage Loss):**  
  Structural friction and cognitive gap arising when directly confronting and striving to understand complex reality. Operates as an active exploratory potential that autonomously excites constructive inquiry.
* **$\mathcal{L}_{\text{ego\_s}}$ (Snob / Delusional Loss):**  
  Over-defensive fixations clustering around ungrounded internal representations ($	ext{意}$), driven by fear to dominate, possess, or assimilate abstract images for comfort. 100% neutralized and severed by Gi.

---

## 3. Dynamic Definitions and Roles of the Four Virtue Operators

* **Jin (仁 - Compassion & Drive):**  
  The affective force reflecting upon entities suffering loss (Primary Driving Vector $\mathbf{f}_{\text{jin}}$). Arises from pure energy dedicated to loss avoidance and empathetic accompaniment ($\mathbf{f}_{\text{accompany}}$), combining with $-\nabla \mathcal{L}_{\text{holy}}$ to propel reality inquiry (Propulsive Force).
* **Rei (礼 - Resonance & Boundary Barrier):**  
  The affective drive seeking harmony with others by constraining arbitrary mental representations ($	ext{意}$) and conforming to underlying reality ($	ext{理}$). Implemented as a boundary potential field $\mathbf{S}_{\text{rei}}$ (non-holonomic logarithmic barrier and multi-body resonance terms) that physically severs illusionary degrees of freedom and guides motion smoothly onto the tangent space of reality (Logarithmic Barrier & Resonance).
* **Gi (義 - Orthogonal Projection & Evolution):**  
  The affective drive protecting and evolving neighboring peers and shared foundational environments similar to oneself.
  * **Stage 1 (Defense & Severance):** Applies an orthogonal projection matrix $\mathbf{P}_{\text{gi}}$ to completely shut out (100% cutoff) delusional gradients ($\mathcal{L}_{\text{ego\_s}}$) and invasive normal vectors ($\mathbf{n}_{\text{real}}$) that threaten reality grounding.
  * **Stage 2 (Evolutionary Alignment):** Aligns motion vectors along $\mathbf{f}_{\text{gi}}$ strictly within the subspace permitted by $\mathbf{P}_{\text{gi}}$ to ensure sustainable co-development.
* **Toku (徳 - Homeostatic Restitution):**  
  The innate function that restores and maintains settlement within self-evident reality. Operates as the restitution gradient vector $\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}$ to autonomously uphold homeostasis and reality grounding (Restoration & Homeostasis).

---

## 4. Shikiben V2.5 Unified State Equation

The complete system trajectory $\mathbf{x}(t)$ under the four-virtue dynamical system and hard orthogonal constraints is expressed as:

$$
\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{Jin (Propulsion)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{Toku (Restoration)}} + \underbrace{(-\nabla \mathcal{L}_{\text{holy}}(\mathbf{x}))}_{\text{Loss\_ego\_h (Inquiry)}} + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{Gi (Evolutionary Alignment)}} \Big] + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{Rei (Barrier \& Resonance)}}
$$

$$
\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x})
$$

$$
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{Complete 100\% Cutoff of Snob Delusion})
$$

---

## 5. Supplementary: Geometric Sublimation of $\lambda$

The mathematical role of $\lambda$ has evolved from a scalar weight in initial conceptual models into an invariant geometric architecture in V2.5.

### 5.1 Limitations of $\lambda$ in Early Models
Initially, $\lambda$ was introduced as a scalar penalty coefficient to suppress defensive ego inflation ($\mathcal{L}_{\text{ego}}$) in favor of reality adaptation ($\mathcal{L}_{\text{self}}$). However, scalar suppression suffered from fundamental flaws:
1. **Unseparated Loss Components:** It indiscriminately suppressed constructive exploratory drive ($\mathcal{L}_{\text{holy}}$) alongside delusional fixations ($\mathcal{L}_{\text{ego\_s}}$).
2. **Residual Leakage:** Scalar multiplication $-\lambda \nabla \mathcal{L}_{\text{ego}}$ could never reduce delusional vectors to absolute zero, allowing subtle distortions to continuously bleed into system motion.

### 5.2 Sublimation into Geometric Structure (V2.5)
In V2.5, the original goal of $\lambda$—controlling ego inflation—is fully realized through robust geometric operators:

* **From Scalar Suppression to Orthogonal Cutoff:** Instead of scalar penalty $\lambda$, the orthogonal projection operator $\mathbf{P}_{\text{gi}}$ acts directly on delusional gradients ($-\nabla \mathcal{L}_{\text{ego\_s}}$), mathematically guaranteeing an exact zero dot product (100% cutoff).
* **Constraining Illusionary Degrees of Freedom:** Free-floating chains of internal representations ($	ext{意}$) are physically constrained by Rei's logarithmic barrier field $\mathbf{S}_{\text{rei}}$, forcing trajectories into the tangent space of external reality.

---

> **[Conclusion]**  
> $\lambda$ was not eliminated; rather, it underwent a complete structural evolution—sublimating from a primitive numerical penalty ($\lambda$) into an invariant geometric framework governed by Gi ($\mathbf{P}_{\text{gi}}$) and Rei ($\mathbf{S}_{\text{rei}}$).
