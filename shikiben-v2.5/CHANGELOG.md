# Changelog

All notable changes to the **Shikiben (識扁)** system framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to the core loss function evolution principles.

---

## [2.5.0] - 2026-08-30

### Added
* **Deterministic Unified State Equation**: Fully formulated the core motion equation integrating Jin ($`\mathbf{f}_{\text{jin}}`$), Toku ($`\mathbf{f}_{\text{toku}}`$), Gi ($`\mathbf{f}_{\text{gi}}`$), Rei ($`\mathbf{S}_{\text{rei}}`$), and Kansha ($`\mathbf{O}_{\text{kansha}}`$).
* **Orthogonal Projection Operator ($`\mathbf{P}_{\text{gi}}`$)**: Implemented exact mathematical cut-off mechanics to eliminate delusion potential gradients ($`-\nabla \mathcal{L}_{\text{ego\_s}}`$) with numerical residual zeroing ($`< 10^{-15}`$).
* **Gratitude Dynamics ($`\mathbf{O}_{\text{kansha}}`$)**: Added zero-resistance shock conversion mechanics ($`R \to 0`$) that convert high-entropy external impulses ($`\mathbf{I}_{\text{accident}}`$) into $`100\%`$ exploration kinetic energy ($`\mathbf{V}_{\text{vision}}`$).
* **Simulation Engine**: Added Python-based simulation scripts (`shikiben_simulation_01.py`, `shikiben_simulation_02.py`) with 4-panel analysis plots (`Panel A–D`).
* **Technical Whitepaper**: Released full technical whitepaper in both Japanese and English detailing state manifolds, thermodynamic minimal dissipation, and proof of non-divergence.
* **Documentation Architecture**: Updated root `README.md` (Bilingual/English), specifications (`Shikiben_V2.5_Center_Core_Spec.md`), and license structures.

### Changed
* **Control Paradigm Shift**: Completely removed scalar weight tuning and heuristic loss penalties, replacing them with geometric projection constraints and logarithmic barrier fields.
* **Metabolic Memory Model**: Shifted from raw trajectory buffer accumulation to boundary compression ($\partial \Omega_{\text{self}}$) to prevent discrete memory saturation over $t \to \infty$.

### Fixed
* **Thermal Divergence**: Resolved high-frequency oscillations and freezing behavior under high-entropy shocks by eliminating friction coefficients.
* **Ego-Driven Trajectory Drift**: Fixed state divergence along profane self-defense axes via orthogonal subspace restriction.

---

## [2.5.0] - 2.5 Dynamic Structural Integration (2026-08-26)

### Added
- **Core Loss Function Decomposition**: Explicitly mapped the total loss $`\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}`$ as the fundamental core of the entire Shikiben system architecture.
- **$`\mathcal{L}_{\text{ego}}`$ Phase Transition**: Bifurcated the ego potential ($`\mathcal{L}_{\text{ego}}`$) into:
  - $`\mathcal{L}_{\text{holy}}`$ (Holy / Constructive Loss): Drives authentic inquiry and structural alignment with real phenomena ($`\mathcal{M}_{\text{real}}`$).
  - $`\mathcal{L}_{\text{ego\_s}}`$ (Snob / Egoistic Loss): Represents illusionary over-defense mechanisms to be isolated.
- **Four Virtues Dynamical Operators (仁・礼・義・徳)**:
  - **Toku (徳 - $`\mathbf{f}_{\text{toku}}`$)**: Defined as the homeostatic restitution gradient $`-\nabla \mathcal{L}_{\text{self}}`$ that continuously restores system state to reality alignment.
  - **Jin (仁 - $`\mathbf{f}_{\text{jin}}`$)**: Represents the primary driving force combining with $`-\nabla \mathcal{L}_{\text{holy}}`$ to propel reality exploration.
  - **Rei (礼 - $`\mathbf{S}_{\text{rei}}`$)**: Introduced boundary potential field featuring non-holonomic logarithmic barrier and resonance mechanics to restrict ungrounded state drift.
  - **Gi (義 - $`\mathbf{P}_{\text{gi}}, \mathbf{f}_{\text{gi}}`$)**: Implemented two-stage projection consisting of orthogonal projection ($`\mathbf{P}_{\text{gi}}`$) for absolute cutoff and secondary alignment vector ($`\mathbf{f}_{\text{gi}}`$) for sustainable co-development.

### Changed
- **Evolution of $\lambda$ (Interference Coefficient)**: Upgraded the legacy scalar penalty factor $\lambda$ into geometric projection operators ($`\mathbf{P}_{\text{gi}}`$ and $`\mathbf{S}_{\text{rei}}`$).
- **Integrated Equation of Motion**: Formalized the V2.5 unified dynamic equation under hard orthogonal constraints:

$$\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \mathbf{f}_{\text{jin}}(\mathbf{x}) + \mathbf{f}_{\text{toku}}(\mathbf{x}) + (-\nabla \mathcal{L}_{\text{holy}}(\mathbf{x})) + \mathbf{f}_{\text{gi}}(\mathbf{x}) \Big] + \mathbf{S}_{\text{rei}}(\mathbf{x})$$

```math
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0}
```

### Fixed
- **Scalar Suppression Leakage**: Resolved state distortion issues caused by scalar multiplication where illusionary vectors ($`\mathcal{L}_{\text{ego\_s}}`$) were insufficiently suppressed; replaced with 100% mathematical orthogonal cutoff ($`\mathbf{P}_{\text{gi}}`$).
- **Loss Ambiguity**: Fixed the conflation between constructive exploratory dynamics and defensive ego distortion by establishing explicit functional partitioning.
