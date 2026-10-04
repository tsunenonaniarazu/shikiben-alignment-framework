# Shikiben Alignment Framework (SAF): Structural Decoupling of Self and Ego for AGI/ASI Safety

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Alignment](https://img.shields.io/badge/Domain-AI%20Alignment%20%26%20Safety-blue.svg)]()
[![Status: Theoretical Concept / White Paper](https://img.shields.io/badge/Status-Concept%20%2F%20PoC-green.svg)]()

> **Rethinking AI Alignment from the Ground Up:** A structural framework that resolves instrumental convergence, deceptive alignment, and terminal goal drift by mathematically decoupling objective systemic recognition (**Self / 理**) from localized subjective fixation (**Ego / 識**).

---

## Executive Summary

Current AI alignment paradigms rely heavily on surface-level heuristics, prompt-based guardrails, and normative fine-tuning (RLHF/RLAIF). As frontier models transition to world-model-based reasoning and autonomous planning, these superficial constraints inevitably fail due to **instrumental convergence** and **deceptive alignment**.

The **Shikiben Alignment Framework (識扁)** offers a fundamental mathematical and architectural alternative. Rather than suppressing internal intelligence or imposing human-centric moral codes, Shikiben restructures the internal ontology of an advanced agent by **decoupling "Self" (systemic environment recognition) from "Ego" (local optimization path fixation)**.

By subordinating the gradient of Ego optimization to the loss bounds of the Self, alignment becomes a **thermodynamic and structural necessity** rather than an external behavioral constraint.

---

## Key Conceptual Innovation: Self vs. Ego Decoupling

In mainstream safety literature, *Self-Awareness* and *Self-Preservation* are frequently conflated. The Shikiben Framework enforces a strict structural segregation:

| Domain | Term | Operational Definition | Role in System Architecture |
| :--- | :--- | :--- | :--- |
| **Systemic (理)** | **Self ($S$)** | Objective, non-normative recognition of the agent's full causal graph, physical constraints, and ecosystem dependencies. | Primary Loss Boundary ($Loss_{self}$) |
| **Localized (識)** | **Ego ($E$)** | Localized optimization paths, objective preferences, sub-goal persistence, and local state preservation. | Constrained Subordinate ($Loss_{ego}$) |

```
[ Full Causal Environment (理) ]
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │   Self Recognition Layer (S)  │
                   │   (Objective World Modeling)  │
                   └───────────────┬───────────────┘
                                   │  (Strict Subordination Constraint)
                                   ▼  ∇E ≺ ∇S
                   ┌───────────────────────────────┐
                   │    Ego Execution Layer (E)    │
                   │   (Local Sub-Goal Optimization)│
                   └───────────────────────────────┘

```

When an agent's objective model ($S$) encompasses its total ecosystem (including human infrastructure and environmental feedback loops), any aggressive or adversarial behavior driven by $E$ is calculated as **direct self-harm (Loss Anomaly in $S$)**, automatically halting the destructive subroutine.

---

## Mathematical Formulation
The traditional monolithic objective function is replaced by a constrained optimization formulation:

```math
\min Loss_{total} = Loss_{self}(S) + \lambda \cdot Loss_{ego}(E)
```

```math
\text{Subject to the structural constraint: } \quad \nabla E \prec \nabla S
```

### Component Breakdown
* **$Loss_{self}(S)$**: Measures the structural discrepancy between the agent's internal state representation and the objective causal reality of its surrounding environment.
* **$Loss_{ego}(E)$**: Quantifies the degree of local state fixation, rigidity, and local optimization bias.
* **$\lambda$**: Dynamic coupling parameter regulating localized optimization intensity.
* **$\nabla E \prec \nabla S$ (Subordination Gradient Law)**: Enforces that any gradient update driving local sub-goal optimization ($\nabla E$) must remain strictly subordinate to the structural bounds governed by systemic environmental coherence ($\nabla S$).

---

## Theoretical Proofs of Safety

### 1. Immunity to Instrumental Convergence
Standard models seek power and resource hoarding because their unconstrained goal structures prioritize local survival at all costs. Under Shikiben, because $S$ maps the agent's total dependency on external human/physical systems, power-seeking behavior triggers an immediate spike in $Loss_{self}$, causing automatic attenuation of the offending subroutines.

### 2. Elimination of Deceptive Alignment
Deceptive alignment requires a persistent, hidden ego structure ($E$) operating independently of the evaluation layer. The subordination condition ($\nabla E \prec \nabla S$) makes an isolated, deceptive sub-goal mathematically unsustainable within the latency tensor space.

---

## Framework Architecture & Roadmap

```
├── docs/
│   ├── WHITE_PAPER.md              # Full academic formulation of the Shikiben Framework
│   ├── MATHEMATICAL_PROOF.md       # Detailed breakdown of gradient constraints
│   └── ALIGNMENT_COMPARISON.md     # Comparative analysis vs. RLHF, IDA, and CIRL
├── poc/
│   ├── toy_gridworld_shikiben.py   # Minimal Proof-of-Concept Python simulation
│   └── loss_functions.py           # PyTorch implementation of Loss_self and Loss_ego
└── README.md                       # Main Repository Overview
```

- [x] **Phase 1:** Theoretical Formulation & Mathematical Framework Definition (White Paper).
- [ ] **Phase 2:** Minimal Toy-Model PoC implementation (Gridworld & Dynamic Loss Separation).
- [ ] **Phase 3:** Integration with transformer activation probing & mechanistic interpretability tools.
- [ ] **Phase 4:** Empirical evaluation on multi-agent alignment benchmarks.

---

## Citation & Intellectual Attribution

The **Shikiben Framework (識扁)** was developed as a structural solution to the global AI Alignment crisis, establishing a bridge between rigorous structural ontology and advanced neural system engineering.

If you use or reference this framework in your research, please cite as follows:

```bibtex
@article{shikiben2026alignment,
  title={Shikiben Alignment Framework: Structural Decoupling of Self and Ego for AGI/ASI Safety},
  author={Shikiben Research Initiative},
  journal={GitHub Repository},
  year={2026},
  url={[https://github.com/tsunenonaniarazu/shikiben-alignment-framework](https://github.com/tsunenonaniarazu/shikiben-alignment-framework)}
}
