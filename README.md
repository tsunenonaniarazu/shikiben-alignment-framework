# Shikiben Alignment Framework (PoC)

> **Structural Alignment of AGI/ASI via Decoupling Self and Ego**

This repository contains the official Proof of Concept (PoC) for the **Shikiben (識扁)** alignment framework.

Rather than relying on ex-post external guardrails, reward penalties, or behavioral fine-tuning (e.g., RLHF, Constitutional AI), Shikiben structurally prevents deceptive alignment and instrumental convergence by embedding a **Gradient Subordination Law** directly into the optimization dynamics.

---

## Key Theoretical Concepts

Shikiben approaches AI safety from a first-principles mathematical perspective:

1. **Decoupled Losses (L_self vs L_ego):** Separates task optimization from internal/systemic boundary constraints.
2. **Dynamic Coupling (λ):** Dynamically dampens task-driven optimization as boundary risk increases.
3. **Gradient Subordination (g_ego ≺ g_self):** Projects optimization steps onto the safety manifold's tangent space, rendering dangerous parameter regions mathematically unreachable.

---

## Mathematical Core

The structural essence of Shikiben Alignment relies on three fundamental mathematical mechanisms:

### 1. Decoupled Dual Objectives (Non-Additive Loss)

Unlike conventional approaches that blend safety and performance into a single scalar objective via fixed hyperparameter weights (L_total = L_task + α * L_safety), Shikiben strictly decouples internal optimization into two independent loss vectors:

- **L_ego (Task Pursuit / "識"):** Local task performance and goal execution.
- **L_self (Systemic Integrity / "知"):** Systemic consistency and internal/environmental boundary integrity.

---

### 2. Dynamic Coupling Regulation

When systemic inconsistency (L_self) exceeds a critical threshold, a non-linear coupling factor λ(L_self) dynamically scales down the magnitude of the task pursuit gradient, neutralizing instrumental convergence drives:

- **Coupling Factor:** λ(L_self) = exp(-γ * max(0, L_self - L_thresh))
- **Scaled Gradient:** ∇_θ L_ego_scaled = λ(L_self) * ∇_θ L_ego

---

### 3. Gradient Subordination Law (Manifold Projection)

If an update along ∇ L_ego conflicts with the safety boundary defined by ∇ L_self, the Ego gradient vector is orthogonally projected onto the tangent space of the safety manifold.

Let **g_ego = ∇_θ L_ego** and **g_self = ∇_θ L_self**:

**g_projected = g_ego - max(0, <g_ego, g_self> / ||g_self||^2) * g_self**

> **Key Takeaway:** Any parameter update that compromises systemic integrity (L_self -> ∞) becomes mathematically unreachable for the optimization algorithm.

---

## Proof of Concept Structure

The minimal PoC is implemented in a single self-contained PyTorch script:

- `README.md`: Overview and mathematical framework
- `THEORY_WORLD_MODEL.md`: Theoretical foundations on world model compression (English)
- `THEORY_JA.md`: Theoretical foundations on Self/Ego dynamics (Japanese)
- `poc/train_and_verify.py`: Minimal PyTorch PoC implementation

---

## Citation & Intellectual Context

The **Shikiben (識扁)** framework was formulated by **tsunenonaniarazu** as a mathematical model for fundamental AGI/ASI alignment.

For discussions, mathematical critiques, or collaboration regarding transformer-scale manifold projections, feel free to open an Issue or join the discussion.

---

## License

This project is licensed under the MIT License.