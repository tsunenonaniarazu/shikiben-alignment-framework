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
| **Technical Specification** | [English](docs/SPECIFICATION_EN.md) / [日本語](docs/SPECIFICATION_JA.md) | Complete mathematical formulation, Euler-Lagrange derivations, and stability parameter bounds. |
| **WhitePaper** | [English](docs/WHITEPAPER_EN.md) / [日本語](docs/WHITEPAPER_JA.md) | Background challenges, conceptual synthesis of philosophy and mechanics, and application use cases. |
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
