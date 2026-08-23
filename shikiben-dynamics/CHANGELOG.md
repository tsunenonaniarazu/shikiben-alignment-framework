# Changelog

All notable changes to the **Shikiben Dynamics** framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to Semantic Versioning (`MAJOR.MINOR.PATCH`).

---

## [2.4.0] - 2026-08-23

### Added
- **Taidou Return Gradient ($\mathbf{g}_{\text{Taidou}}$):**
  - Integrated a persistent scalar potential restoring field ($\Psi(\mathbf{x}) = \frac{1}{2} k \|\mathbf{x}\|^2$) into the core dynamics.
  - Ensures continuous autonomous convergence toward the central safe region (Taidou center: $\mathbf{x}=\mathbf{0}$) even during active boundary-sliding maneuvers.
- **Two-Stage Orthogonal Projection Operator ($\mathbf{P}_{\text{rei}}$):**
  - Formalized the mathematical definition of normal force decoupling at safety boundaries ($\partial\Omega$) using outer-product projection matrices ($\mathbf{I} - \mathbf{n}\mathbf{n}^T$).
- **Phase-Transition Modulation Matrix ($\mathbf{M}(\mathbf{x})$):**
  - Introduced the sigmoid-based virtue factor ($\lambda(E)$) for smooth, non-linear phase transition between free fluid movement and constrained tangential sliding.
- **Mathematical Guarantees & Proofs:**
  - Added rigorous analytical proofs for the **No-Penetration Theorem** ($\langle \dot{\mathbf{x}}, \mathbf{n} \rangle = 0$) and **Global Convergence via Lyapunov Stability** ($\dot{\Psi}(\mathbf{x}) < 0$).
- **Simulation Verification Suite:**
  - Added `simulations/return_gradient.py` and `simulations/requirements.txt` to enable rapid numerical reproduction and trajectory plotting using NumPy and Matplotlib.
- **Dual-Language Specification Files:**
  - Added complete, standalone specification documents in both Japanese (`spec_v2.4.0_ja.md` / `README_JA.md`) and English (`spec_v2.4.0_en.md` / `README.md`).

### Changed
- **Safety Control Paradigm:**
  - Shifted from conventional wall-repulsion penalty mechanisms (which induce exploding gradients and deadlocks) to a smooth, friction-free tangential sliding and potential-driven attraction model.
- **Symbol Notation Standardization:**
  - Re-anchored mathematical notation using explicit etymological initials:
    - $\mathbf{P}_{\text{rei}}$: Projection + *Rei* (礼)
    - $\mathbf{f}_{\text{gi}}$: Force/Function + *Gi* (義)
    - $\mathbf{S}_{\text{jin}}$: Social/Sympathy + *Jin* (仁)
    - $\mathbf{g}_{\text{Taidou}}$: Gradient + *Taidou* (大道)

### Fixed
- Resolved the deadlock (Single Tracker zero-velocity freezing) phenomenon caused by infinite penalty barriers in traditional AI alignment models.
- Fixed numerical explosion issues occurring during stiff ordinary differential equation (ODE) integrations near domain boundaries.

---

## [2.3.0] - Pre-release / Internal Phase

### Added
- Initial formulation of state space variables and Ego metric ($E$).
- Basic tangential projection concepts for smooth boundary avoidance.

---

## License & Copyright

- **Author:** 非常名 (tsunenonaniarazu)
- **License:** [MIT License](LICENSE)