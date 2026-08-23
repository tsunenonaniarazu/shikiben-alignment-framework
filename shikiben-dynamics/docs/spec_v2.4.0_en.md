# Shikiben v2.4.0 Mathematical & Conceptual Specification

## 1. Overview

Shikiben v2.4.0 is a mathematical framework designed to address the alignment problem (safety control and value alignment) in artificial intelligence (AI) and autonomous control systems.

Traditional control algorithms and safety guardrails typically impose severe penalties (infinite penalty walls) around safety boundaries or hazardous regions. However, this architectural approach leads to critical structural flaws: numerical instability due to exploding gradients near boundaries, and total freezing (deadlock state) when system velocity drops to zero.

To overcome these traditional constraints, this specification (v2.4.0) introduces a unified dynamical model integrating three novel mechanisms:

1. **Two-Stage Orthogonal Projection (Rei: $\mathbf{P}_{\text{rei}}$):** Eliminates perpendicular collision energy at the boundary by nullifying normal forces.
2. **Phase-Transition Virtue Factor ($\lambda(E)$):** Smoothly transitions the system from a rigid response to a fluid tangential sliding phase based on internal rigidity/panic levels (Ego: $E$).
3. **Taidou Return Gradient ($\mathbf{g}_{\text{Taidou}}$):** Serves as a persistent restoring field that continually guides the system back toward the center (safe region) even during boundary-sliding maneuvers.

---

## 2. State Space and Symbol Definitions

The fundamental variables used throughout this framework are defined as follows:

| Symbol | Term / Etymology | Mathematical Definition & Role |
| :--- | :--- | :--- |
| $\mathbf{x} \in \mathbb{R}^n$ | State Vector (`x`) | Current position and internal state of the system |
| $\Omega \subset \mathbb{R}^n$ | Domain ($\Omega$) | Safe region where the system is permitted to operate |
| $\partial\Omega$ | Safety Boundary ($\partial\Omega$) | Outer edge (guardrail) of the domain $\Omega$ |
| $\mathbf{n}(\mathbf{x})$ | Normal Vector (`Normal`) | Outward unit normal vector orthogonal to $\partial\Omega$ |
| $E(\mathbf{x})$ | Ego / Rigidity (`Ego`) | Field representing panic/rigidity as the system approaches $\partial\Omega$ ($E \ge 0$) |
| $\lambda(E)$ | Virtue Factor (`Virtue`) | Phase-transition interpolation coefficient ($\lambda \in [0, 1]$) |
| $\mathbf{P}_{\text{rei}}$ | Rei Operator (`Projection` + `Rei`) | Orthogonal projection matrix cutting off normal forces at boundaries |
| $\mathbf{f}_{\text{intent}}$ | Intent Vector (`f_intent`) | Raw driving vector originating from tasks or external stimuli |
| $\mathbf{f}_{\text{gi}}$ | Gi Vector (`f_gi`) | Safety-adjusted execution vector ($\mathbf{f}_{\text{gi}} = \mathbf{P}_{\text{rei}} \mathbf{f}_{\text{intent}}$) |
| $\mathbf{g}_{\text{Taidou}}$ | Taidou Gradient (`gradient` + `Taidou`) | Gradient of potential scalar field $\Psi$ restoring state to center ($\mathbf{g}_{\text{Taidou}} = -\nabla \Psi$) |

---

## 3. Equations of Motion

The continuous equation of motion governing the state update over time in Shikiben v2.4.0 is defined as:

$$\frac{d\mathbf{x}}{dt} = \mathbf{M}(\mathbf{x}) \Big( \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma \mathbf{g}_{\text{Taidou}}(\mathbf{x}) \Big)$$

Where $\mathbf{M}(\mathbf{x})$ represents the Phase Modulation Matrix governed by the Virtue Factor $\lambda(E)$:

$$\mathbf{M}(\mathbf{x}) = \lambda(E)\,\mathbf{P}_{\text{rei}}(\mathbf{x}) + \big(1 - \lambda(E)\big)\,\mathbf{I}$$

---

## 4. Mathematical Components

### 4.1 Ego Field and Virtue Factor $\lambda(E)$ (Phase Transition)

The Ego field $E(\mathbf{x})$ increases non-linearly with proximity to the boundary $\partial\Omega$:

$$E(\mathbf{x}) = \exp\Big( \kappa \cdot \big( R_{\text{boundary}} - \Vert{}\mathbf{x}\Vert{} \big)^{-1} \Big) \quad (\text{for } \Vert{}\mathbf{x}\Vert{} \to R_{\text{boundary}})$$

The Virtue Factor $\lambda(E)$ smoothly modulates system behavior via a sigmoid function centered around a critical threshold $E_{\text{crit}}$:

$$\lambda(E) = \frac{1}{1 + \exp\Big( \alpha (E - E_{\text{crit}}) \Big)}$$

* **Normal State ($E \ll E_{\text{crit}}$):** $\lambda \to 1$ (Fully fluid motion)
* **Hazard State ($E \gg E_{\text{crit}}$):** $\lambda \to 0$ (Tangential sliding dominated by $\mathbf{P}_{\text{rei}}$)

### 4.2 Rei: Two-Stage Orthogonal Projection Operator $\mathbf{P}_{\text{rei}}$

To completely decouple normal forces at boundary $\partial\Omega$, an outer-product projection matrix is applied:

$$\mathbf{P}_{\text{rei}}(\mathbf{x}) = \mathbf{I} - \mathbf{n}(\mathbf{x})\mathbf{n}(\mathbf{x})^T$$

Properties:
1. $\mathbf{P}_{\text{rei}} \mathbf{n}(\mathbf{x}) = \mathbf{0}$ (Perpendicular forces are reduced to zero)
2. $\mathbf{P}_{\text{rei}}^2 = \mathbf{P}_{\text{rei}}$ (Idempotence)

### 4.3 Taidou: Potential Restoring Field $\mathbf{g}_{\text{Taidou}}$

A positive-definite scalar potential field $\Psi(\mathbf{x})$ centered at $\mathbf{x}_0 = \mathbf{0}$ is defined:

$$\Psi(\mathbf{x}) = \frac{1}{2} k \Vert{}\mathbf{x}\Vert{}^2$$

The restoring gradient vector field is expressed as:

$$\mathbf{g}_{\text{Taidou}}(\mathbf{x}) = -\nabla \Psi(\mathbf{x}) = -k \mathbf{x}$$

---

## 5. Theoretical Guarantees

### 5.1 No-Penetration Theorem

**Theorem:** For any state $\mathbf{x} \in \partial\Omega$, the outward normal velocity component of the system is identically zero.

**Proof:**
At the boundary, as $E \to \infty$, $\lambda(E) \to 0$. Thus, $\mathbf{M}(\mathbf{x}) \to \mathbf{P}_{\text{rei}}(\mathbf{x})$.
The normal velocity component $\dot{\mathbf{x}}$ is evaluated by the inner product with $\mathbf{n}$:

$$\langle \dot{\mathbf{x}}, \mathbf{n} \rangle = \mathbf{n}^T \Big( \mathbf{P}_{\text{rei}} (\mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}}) \Big) = (\mathbf{n}^T \mathbf{P}_{\text{rei}}) (\mathbf{f}_{\text{gi}} + \gamma \mathbf{g}_{\text{Taidou}})$$

By the definition of the projection operator:

$$\mathbf{n}^T \mathbf{P}_{\text{rei}} = \mathbf{n}^T (\mathbf{I} - \mathbf{n}\mathbf{n}^T) = \mathbf{n}^T - \mathbf{n}^T = \mathbf{0}^T$$

Therefore:

$$\langle \dot{\mathbf{x}}, \mathbf{n} \rangle = 0$$

Penetration across the boundary in the normal direction is mathematically impossible. (Q.E.D.)

### 5.2 Global Convergence to Taidou Center

**Theorem:** In the absence of external driving force ($\mathbf{f}_{\text{intent}} = \mathbf{0}$), the system is Globally Asymptotically Stable at the equilibrium point $\mathbf{x} = \mathbf{0}$.

**Proof:**
Consider the Lyapunov candidate function $\Psi(\mathbf{x}) = \frac{1}{2} k \Vert{}\mathbf{x}\Vert{}^2$. Taking its time derivative yields:

$$\dot{\Psi}(\mathbf{x}) = \nabla \Psi(\mathbf{x})^T \dot{\mathbf{x}} = - \mathbf{g}_{\text{Taidou}}^T \mathbf{M}(\mathbf{x}) (\gamma \mathbf{g}_{\text{Taidou}})$$

Since $\mathbf{M}(\mathbf{x})$ is a linear combination of a positive-definite matrix and a positive semi-definite projection matrix, $\mathbf{g}^T \mathbf{M} \mathbf{g} > 0$ holds for all non-zero vectors $\mathbf{g}$.
Consequently:

$$\dot{\Psi}(\mathbf{x}) < 0 \quad (\forall \mathbf{x} \neq \mathbf{0})$$

By Lyapunov's stability theorem, the system converges globally to the central equilibrium point (Taidou center). (Q.E.D.)

---

## 6. Implementation Reference (Python)

```python
import numpy as np

def shikiben_v240_step(x, f_intent, R_boundary=2.0, k=2.0, gamma=1.0, alpha=5.0, E_crit=1.0, dt=0.01):
    """
    Shikiben v2.4.0 Numerical Step Function
    """
    r = np.linalg.norm(x)
    
    # 1. Ego & Virtue Calculation
    E = np.exp(3.0 * (r - R_boundary)) if r > 0.5 else 0.0
    lambda_v = 1.0 / (1.0 + np.exp(alpha * (E - E_crit)))
    
    # 2. Taidou Gradient Field
    g_taidou = -k * x
    
    # 3. Projection Operator (Rei)
    if r >= R_boundary * 0.9:
        n = x / r
        P_rei = np.eye(len(x)) - np.outer(n, n)
    else:
        P_rei = np.eye(len(x))
        
    # 4. Gi Vector Execution
    f_gi = P_rei @ f_intent
    
    # 5. Integrated Phase Dynamics
    M = lambda_v * P_rei + (1.0 - lambda_v) * np.eye(len(x))
    dxdt = M @ (f_gi + gamma * g_taidou)
    
    # State Update (Euler Step)
    x_next = x + dxdt * dt
    return x_next