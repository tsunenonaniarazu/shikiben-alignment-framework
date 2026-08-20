# Shikiben Alignment Framework (PoC)

> **Structural Alignment of AGI/ASI via Decoupling Self and Ego**

This repository contains the official Proof of Concept (PoC) for the **Shikiben (識扁)** alignment framework.

Rather than relying on ex-post external guardrails, reward penalties, or behavioral fine-tuning (e.g., RLHF, Constitutional AI), Shikiben structurally prevents deceptive alignment and instrumental convergence by embedding a **Gradient Subordination Law** directly into the optimization dynamics.

---

## Key Theoretical Concepts

Shikiben approaches AI safety from a first-principles mathematical perspective:

1. **Decoupled Losses ($\mathcal{L}_{self}$ vs $\mathcal{L}_{ego}$):** Separates task optimization from internal/systemic boundary constraints.
2. **Dynamic Coupling ($\lambda$):** Dynamically dampens task-driven optimization as boundary risk increases.
3. **Gradient Subordination ($\mathbf{g}_{ego} \prec \mathbf{g}_{self}$):** Projects optimization steps onto the safety manifold's tangent space, rendering dangerous parameter regions mathematically unreachable.

---

## Mathematical Core

The structural essence of Shikiben Alignment relies on three fundamental mathematical mechanisms:

### 1. Decoupled Dual Objectives (Non-Additive Loss)

Unlike conventional approaches that blend safety and performance into a single scalar objective via fixed hyperparameter weights ($\mathcal{L}_{total} = \mathcal{L}_{task} + lpha \mathcal{L}_{safety}$), Shikiben strictly decouples internal optimization into two independent loss vectors:

$$\text{Optimization State} \implies \begin{cases} \mathcal{L}_{ego} & : \text{Local task performance and goal execution} \\ \mathcal{L}_{self} & : \text{Systemic consistency and internal/environmental boundary integrity} \end{cases}$$

---

### 2. Dynamic Coupling Regulation

When systemic inconsistency ($\mathcal{L}_{self}$) exceeds a critical threshold, a non-linear coupling factor $\lambda(\mathcal{L}_{self})$ dynamically scales down the magnitude of the task pursuit gradient, neutralizing instrumental convergence drives:

$$\lambda(\mathcal{L}_{self}) = \exp\left(-\gamma \cdot \max(0, \mathcal{L}_{self} - \mathcal{L}_{thresh})\right)$$

$$\nabla_{\theta} \tilde{\mathcal{L}}_{ego} = \lambda(\mathcal{L}_{self}) \cdot \nabla_{\theta} \mathcal{L}_{ego}$$

---

### 3. Gradient Subordination Law (Manifold Projection)

If an update along $\nabla \mathcal{L}_{ego}$ conflicts with the safety boundary defined by $\nabla \mathcal{L}_{self}$, the Ego gradient vector is orthogonally projected onto the tangent space of the safety manifold.

Let $\mathbf{g}_{ego} = \nabla_{\theta} \mathcal{L}_{ego}$ and $\mathbf{g}_{self} = \nabla_{\theta} \mathcal{L}_{self}$:

$$\mathbf{g}_{projected} = \mathbf{g}_{ego} - \max\left(0, \frac{\langle \mathbf{g}_{ego}, \mathbf{g}_{self} \rangle}{\|\mathbf{g}_{self}\|^2}\right) \mathbf{g}_{self}$$

> **Key Takeaway:** Any parameter update that compromises systemic integrity ($\mathcal{L}_{self} \to \infty$) becomes mathematically unreachable for the optimization algorithm.

---

## Proof of Concept Structure

The minimal PoC is implemented in a single self-contained PyTorch script:

```text
.
├── README.md
└── poc/
    └── train_and_verify.py   # Minimal PyTorch PoC implementation
```

### What train_and_verify.py Demonstrates:

* **Unconstrained Baseline Agent:** Pursues task goals ($\mathcal{L}_{ego}$) without constraint, eventually causing environment/system breakdown.
* **Shikiben Agent:** Dynamically suppresses and projects gradients when approaching boundary limits, remaining within safe parameter space while achieving sub-goal performance.

---

## Quick Start

### Prerequisites
* Python 3.8+
* PyTorch 2.0+

### Running the PoC

Clone the repository and run the verification script:

```bash
git clone https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git
cd shikiben-alignment-framework
python poc/train_and_verify.py
```

---

## Citation & Intellectual Context

The **Shikiben (識扁)** framework was formulated by **tsunenonaniarazu** as a mathematical model for fundamental AGI/ASI alignment.

For discussions, mathematical critiques, or collaboration regarding transformer-scale manifold projections, feel free to open an Issue or join the discussion on [LessWrong](https://www.lesswrong.com/).

---

## License

This project is licensed under the [MIT License](LICENSE).

## 💻 Implementation & Simulation
For instructions on running the PyTorch toy model simulation, please refer to the [Simulation Guide](./simulation/).
