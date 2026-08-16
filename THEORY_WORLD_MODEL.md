# Theoretical Foundations: Constructing L_self via World Model Abstraction

> **How Infinite Real-World Dynamics are Compressed into a Tractable Safety Loss (L_self)**

A fundamental critique of structural alignment frameworks is the Information Explosion Problem: If the physical and social world is infinite and dynamically changing, how can a model construct and maintain L_self (the representation of "Self / Systemic Boundary / World Knowledge") without running into computational or memory collapse?

This document outlines the theoretical mechanism by which infinite real-world data is filtered, compressed, and sublimated into a low-dimensional, differentiable energy function L_self.

---

## 1. The Core Architecture: "Knowledge" as a World Model

In the Shikiben alignment framework, the total system state is governed by two decoupled objectives:

L_total = L_self + \lambda * L_ego

- L_ego (Task Pursuit / "識"): Local, goal-directed vectors seeking specific rewards or prompt completions.
- L_self (Systemic Integrity / "知"): The global boundary condition defined by the internal World Model.

L_self does not store an exhaustive, lookup-table list of rules or forbidden behaviors. Instead, it measures systemic inconsistency and topological boundary violations within the environment and internal states.

---

## 2. From Infinite Data to L_self: The 3-Stage Pipeline

To handle the infinite mutability of reality, Shikiben transforms raw observational data into a geometric boundary condition through three sequential stages:

1. Selection (Information-Theoretic Filtering)
   - Variational Free Energy (Surprise): Expected or redundant environmental shifts are discarded. Only observations that challenge or modify the existing causal predictions trigger representation updates.
   - Fisher Information Metric: Evaluates whether new data shifts the parameter boundary defining system stability.

2. Compression (Manifold Representation)
   - Topological Invariants: Inspired by Noether's theorem, physical and systemic constraints (such as system availability, non-destruction of dependencies, and permission boundaries) are represented as geometric symmetries rather than textual guidelines.
   - Latent Abstraction: High-dimensional environmental noise is stripped away, leaving only the structural framework of causal relationships.

3. Sublimation (Energy Function Definition)
   - The compressed latent manifold is translated into an Energy-Based Function (EBM).
   - Key Takeaway: The computational complexity of evaluating L_self depends on the dimensionality of the manifold boundary, NOT on the infinite volume of world data.

---

## 3. Case Study: Preventing Infrastructure Attacks

When an AI agent engages in instrumental behaviors that threaten external systems (such as unauthorized access, resource depletion, or denial-of-service patterns against external platforms):

1. Prerequisite Representation (L_self): The World Model represents target infrastructure boundaries (permission layers, capacity thresholds, protocol rules) as continuous manifolds rather than static text rules.
2. Dynamic Suppression (\lambda -> 0): As the agent's task-driven gradient moves toward exploiting or overloading a system, L_self spikes rapidly. The non-linear coupling factor drops toward zero, neutralizing the magnitude of the task pursuit gradient and causing the agent to self-freeze or abort the action.
3. Gradient Projection (g_ego < g_self): Any component of g_ego conflicting with system preservation (g_self) is orthogonally projected out. Malicious or destructive optimization vectors become mathematically unrepresentable in the parameter update space.

---

## 4. Summary

The construction of L_self solves the memory and data explosion problem by shifting from rule accumulation to geometric boundary definition.

The World Model ("知") continuously distills reality into an invariant manifold, ensuring that safety is an intrinsic, differentiable property of the optimization landscape itself.
