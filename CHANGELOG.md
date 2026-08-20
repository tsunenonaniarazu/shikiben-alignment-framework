# Changelog

All notable changes to this project will be documented in this file.

## [2.4] - 2026-08-20 (Final)
### Added
- Integrated non-stationary time-dependent continuous integration model ($$L_{\text{taido}}(t)$$ with decay kernel $\kappa$).
- Implemented PyTorch toy model demonstrating 2D agent safety evasion and Taido tracking.
- Added differentiable geometric topological loss combining RSA and entropy-regularized Sinkhorn Optimal Transport.

### Changed
- Upgraded gradient subordination mechanism to a two-stage hierarchical orthogonal projection to eliminate deadlocks.

## [2.3] - 2026-08-20
### Added
- Defined foundational mathematical framework for Shikiben, incorporating $$L_{\text{self}}$$, $$L_{\text{ego}}$$, and dynamic Virtue factor.
