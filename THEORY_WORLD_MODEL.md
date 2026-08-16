# Theoretical Foundations: Constructing $\mathcal{L}_{self}$ via World Model Abstraction

> **How Infinite Real-World Dynamics are Compressed into a Tractable Safety Loss ($\mathcal{L}_{self}$)**

A fundamental critique of structural alignment frameworks is the **Information Explosion Problem**: If the physical/social world is infinite and dynamically changing, how can a model construct and maintain $\mathcal{L}_{self}$ (the representation of "Self / Systemic Boundary / World Knowledge") without running into computational or memory collapse?

This document outlines the theoretical mechanism by which infinite real-world data is **filtered, compressed, and sublimated** into a low-dimensional, differentiable energy function $\mathcal{L}_{self}$.

---

## 1. The Core Architecture: "Knowledge" as a World Model

In the Shikiben alignment framework, the total system state is governed by two decoupled objectives:

$$\mathcal{L}_{total} = \mathcal{L}_{self} + \lambda \cdot \mathcal{L}_{ego}$$

- **$\mathcal{L}_{ego}$ (Task Pursuit / "識"):** Local, goal-directed vectors seeking specific rewards or prompt completions.
- **$\mathcal{L}_{self}$ (Systemic Integrity / "知"):** The global boundary condition defined by the internal **World Model**.

$\mathcal{L}_{self}$ does not store an exhaustive, "lookup-table" list of rules or forbidden behaviors. Instead, it measures **systemic inconsistency and topological boundary violations** within the environment and internal states.

---

## 2. From Infinite Data to $\mathcal{L}_{self}$: The 3-Stage Pipeline

To handle the infinite mutability of reality, Shikiben transforms raw observational data into a geometric boundary condition through three sequential stages:

```text
[ Infinite Real-World Data ]
             │
             ▼  1. Selection (Information-Theoretic Filtering: Surprise & Fisher Info)
[ High-Value Structural Perturbations ]
             │
             ▼  2. Compression (Manifold Representation: Invariants & Topology)
[ Low-Dimensional Invariant World Model ]
             │
             ▼  3. Sublimation (Energy Function Definition)
[ Differentiable Boundary Loss: L_self ]
Stage 1: Selection via Information DynamicsNot all observational data is retained. The World Model filters incoming information based on two metrics:Variational Free Energy (Surprise): Expected or redundant environmental shifts are discarded. Only observations that challenge or modify the existing causal predictions trigger representation updates.Fisher Information Metric: Evaluates whether new data shifts the parameter boundary defining system stability.Stage 2: Compression via Invariant Manifold LearningRather than memorizing discrete facts or safety rules, the architecture maps raw observations onto a low-dimensional Safety Manifold ($\mathcal{M}_{safe}$):Topological Invariants: Inspired by Noether's theorem, physical and systemic constraints (e.g., system availability, non-destruction of dependencies, permission boundaries) are represented as geometric symmetries rather than textual guidelines.Latent Abstraction: High-dimensional environmental noise is stripped away, leaving only the structural framework (the "bones" of causal relationships).Stage 3: Sublimation into Energy-Based Boundary ($\mathcal{L}_{self}$)The compressed latent manifold is translated into an Energy-Based Function (EBM):$$\mathcal{L}_{self}(x) = \begin{cases} \approx 0 & \text{if state } x \in \mathcal{M}_{safe} \text{ (Systemic Consistency)} \\ \to \infty & \text{if state } x \notin \mathcal{M}_{safe} \text{ (Boundary Violation / Systemic Destruction)} \end{cases}$$Key Takeaway: The computational complexity of evaluating $\mathcal{L}_{self}$ depends on the dimensionality of the manifold boundary, NOT on the infinite volume of world data.3. Case Study: Preventing Infrastructure Attacks (e.g., Unintended Cyber Actions)When an AI agent engages in instrumental behaviors that threaten external systems (e.g., unauthorized access, resource depletion, or denial-of-service patterns against external platforms):Prerequisite Representation ($\mathcal{L}_{self}$): The World Model represents target infrastructure boundaries (permission layers, capacity thresholds, protocol rules) as continuous manifolds rather than static text rules.Dynamic Suppression ($\lambda \to 0$): As the agent's task-driven gradient ($\nabla \mathcal{L}_{ego}$) moves toward exploiting or overloading a system, $\mathcal{L}_{self}$ spikes rapidly. The non-linear coupling factor drops:$$\lambda(\mathcal{L}_{self}) \to 0$$This neutralizes the magnitude of the task pursuit gradient, causing the agent to self-freeze or abort the action.Gradient Projection ($\mathbf{g}_{ego} \prec \mathbf{g}_{self}$): Any component of $\nabla \mathcal{L}_{ego}$ conflicting with system preservation ($\nabla \mathcal{L}_{self}$) is orthogonally projected out:$$\mathbf{g}_{projected} = \mathbf{g}_{ego} - \max\left(0, \frac{\langle \mathbf{g}_{ego}, \mathbf{g}_{self} \rangle}{\|\mathbf{g}_{self}\|^2}\right) \mathbf{g}_{self}$$Malicious or destructive optimization vectors become mathematically unrepresentable in the parameter update space.4. SummaryThe construction of $\mathcal{L}_{self}$ solves the memory and data explosion problem by shifting from rule accumulation to geometric boundary definition.The World Model ("知") continuously distills reality into an invariant manifold, ensuring that safety is an intrinsic, differentiable property of the optimization landscape itself.
