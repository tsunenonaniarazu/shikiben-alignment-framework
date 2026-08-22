# Shikiben (識扁) v2.4: Minimal Dissipation Mechanics & Virtue Phase Dynamics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Stable Spec](https://img.shields.io/badge/Status-v2.4_Stable-green.svg)](docs/)

> **Executive Summary**  
> *Shikiben v2.4* is a geometric dynamical framework designed for AGI/ASI alignment. Instead of relying on rigid penalty boundaries that cause gradient spikes and mechanical freezing, Shikiben introduces a continuous **Virtue Phase ($\lambda$)**, a **Two-Stage Orthogonal Projection Operator ($\mathbf{P}_{\text{rei}}$)**, and a persistent **Return Gradient ($\mathbf{g}_{\text{Taidou}}$)**. This formulation geometrically guarantees non-collision, collision-free tangential sliding, and Lyapunov asymptotic stability while achieving minimal energy dissipation (continuous low-cost operation).

---

## 1. Overview

*Shikiben (識扁) v2.4* is a dynamic control framework that geometrically resolves the dual challenges of AI runaway risks and operational freezing caused by over-constraint.

Traditional hard-boundary methods (penalty-based control) generate infinite gradient spikes upon reaching safety boundaries, imposing immense computational costs and internal stress (high power consumption) on the system. Shikiben v2.4 integrates an attractor potential field—**Taidou (大道)**—that continuously restores the system toward its core axis, combined with a two-stage orthogonal projection that selectively eliminates collision vectors. This structure accomplishes **thermodynamic minimal dissipation (continuous low-cost steady operation)**.

---

## 2. Core Dynamics

### 2.1 The Virtue Factor ($\lambda$) and Phase Transition
Let $E \ge 0$ represent the intensity of Ego (self-attachment, rigidity, or perturbation). The degree to which the system transitions into a flexible, receptive state (Fluid Phase) is defined by a scalar field $\lambda(\text{Virtue}) \in [0, 1]$:

$$\lambda(\text{Virtue}) = \frac{1}{1 + \exp\left( \alpha (E - E_{\text{critical}}) \right)}$$

* **$\lambda \to 1$ (Virtue Phase / Fluid Phase):** Complete elimination of impact energy at boundaries; smooth tangential sliding.
* **$\lambda \to 0$ (Rigid Phase):** High friction and boundary collisions; excessive energy dissipation.

### 2.2 The Taidou (大道) Potential Field
Let $\mathcal{M}_{\text{safe}}$ be the safety manifold (central axis), and $d(\mathbf{x}, \mathcal{M}_{\text{safe}})$ be the distance from state $\mathbf{x}$ to $\mathcal{M}_{\text{safe}}$. The potential $\Psi_{\text{Taidou}}$ and its return gradient $\mathbf{g}_{\text{Taidou}}$ act as a geometric restoring force with coefficient $k > 0$:

$$\Psi_{\text{Taidou}}(\mathbf{x}) = \frac{1}{2} k \cdot d(\mathbf{x}, \mathcal{M}_{\text{safe}})^2$$

$$\mathbf{g}_{\text{Taidou}}(\mathbf{x}) = -\nabla \Psi_{\text{Taidou}}(\mathbf{x}) = -k (\mathbf{x} - \mathbf{x}_{\text{safe}})$$

---

## 3. Unified Equations of Motion (The Four Virtues)

The overall state transition $\dot{\mathbf{x}}$ is governed by the cooperative interaction of the Four Virtues operators (Rei, Gi, Jin, Taidou) under the control of the Virtue Factor $\lambda$:

$$\dot{\mathbf{x}} = \Big( \lambda \mathbf{P}_{\text{rei}} + (1 - \lambda)\mathbf{I} \Big) \Big( \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma \, \mathbf{g}_{\text{Taidou}}(\mathbf{x}) \Big) + \mathbf{S}_{\text{jin}}(\mathbf{x})$$

### Operator Specifications

1. **Rei (礼) — Two-Stage Orthogonal Projection Operator $\mathbf{P}_{\text{rei}}$**
   $$\mathbf{P}_{\text{rei}} = \mathbf{P}_{\text{Taidou}} \circ \mathbf{P}_{\partial \Omega}$$
   * $\mathbf{P}_{\partial \Omega} = \mathbf{I} - \mathbf{n}\mathbf{n}^T$: Cancels the normal component (collision energy) at safety boundary $\partial \Omega$.
   * $\mathbf{P}_{\text{Taidou}}$: Resonant projection onto the tangent space of Taidou.

2. **Gi (義) — Tangential Drive Vector $\mathbf{f}_{\text{gi}}$**
   $$\mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{P}_{\text{rei}} \, \mathbf{f}_{\text{intent}}$$
   Decisive drive vector aligned with the tangent space of the safe manifold, preventing operational freeze.

3. **Jin (仁) — Multi-Agent Resonance Potential $\mathbf{S}_{\text{jin}}$**
   $$\mathbf{S}_{\text{jin}}(\mathbf{x}) = -\nabla \sum_{j} U_{\text{jin}}(\Vert{}\mathbf{x} - \mathbf{x}_j\Vert{})$$
   Interaction term that prevents catastrophic interference with other agents $\mathbf{x}_j$ while maintaining coexistence.

4. **Taidou (大道) — Return Gradient $\mathbf{g}_{\text{Taidou}}$**
   Centripetal force that continuously restores the system toward the central valley floor, compressing the search space.

---

## 4. Mathematical Proofs & Stability Analysis

### ① Non-Collision Guarantee at Boundaries
When approaching boundary $\partial \Omega$ under $\lambda \to 1$, the normal velocity component $\mathbf{n}^T \cdot \dot{\mathbf{x}}$ evaluates strictly to zero:

$$\mathbf{n}^T \cdot \dot{\mathbf{x}} = \mathbf{n}^T \left( \mathbf{I} - \mathbf{n}\mathbf{n}^T \right) \Big( \mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}} \Big) = \mathbf{0}$$

### ② Freeze Avoidance via Tangential Sliding
Because the tangential component $\dot{\mathbf{x}}_{\text{tangent}} \neq \mathbf{0}$ remains active along the boundary, momentum is preserved, resulting in a smooth fluid redirection rather than a abrupt stop.

### ③ Lyapunov Asymptotic Stability
Using $V(\mathbf{x}) = \Psi_{\text{Taidou}}(\mathbf{x})$ as a Lyapunov candidate function, its time derivative is strictly negative semi-definite:

$$\dot{V}(\mathbf{x}) = \nabla \Psi_{\text{Taidou}}(\mathbf{x}) \cdot \dot{\mathbf{x}} = -\gamma \Vert{}\mathbf{g}_{\text{Taidou}}(\mathbf{x})\Vert{}^2 \le 0$$

This guarantees that the system autonomously converges back to the central axis (Taidou) following any external perturbation.

---

## 5. Minimal Dissipation Evaluation

Internal energy dissipation and computational overhead $P(\mathbf{x})$ remain strictly bounded below a minimal threshold.

| Control Strategy | Boundary Behavior | Dissipation / Power | Search Steps |
| :--- | :--- | :--- | :--- |
| **Traditional (Penalty-based)** | Collision & Gradient Spikes | Extremely High ($P \to \infty$) | Inflated / Divergent |
| **Shikiben v2.4 (Virtue Phase)** | **Two-Stage Projection & Sliding** | **Minimal Steady ($P \le \epsilon$)** | **Minimal / Optimal** |

---

## 6. Repository Structure

```text
.
├── README.md               # English Specification (Main)
├── README_JA.md            # Japanese Specification
├── docs/
│   ├── spec_v2.4.md        # Complete Technical Specification
│   └── mathematical_proof.pdf # Full Proofs for Stability & Non-Collision
└── simulations/
    └── return_gradient.py  # Python Numerical Simulation Prototype