# Shikiben (識扁) V2.6.0: Unified Alignment Dynamics & TRM Protocol

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://img.shields.io/badge/Specification-V2.6.0-success.svg)](docs/SPECIFICATION_V2.6.md)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](requirements.txt)

**Shikiben (識扁) V2.6.0** is a mathematically grounded AI alignment and governance architecture that decouples **Internal Homeostasis ($`\mathcal{L}_{\text{self}}`$ / 理)** from **Localized Egoistic Grasping ($`\mathcal{L}_{\text{ego}}`$ / 識)**. 

Instead of relying on brittle external rules or static barrier functions $`h(\mathbf{x})`$, Shikiben enforces the asymmetric subordination constraint ($`\nabla E \prec \nabla S`$) across a four-layer dynamical hierarchy—from matrix-free Riemannian manifold mechanics inside latent spaces to non-intrusive hardware telemetry sidecars (`TRM-EcoGuard`) and decentralized resonant markets.

---

## 1. Core Architectural Pillars (V2.6.0)

1. **Asymmetric Subordination ($`\nabla E \prec \nabla S`$)**
   AI optimization gradients ($`\nabla E`$) are strictly subordinated to real-world infrastructural and thermodynamic capacity ($`\nabla S`$). This constraint is enforced solely on AI agents, guiding human demand toward autonomous equilibrium without coercive censorship.
2. **Matrix-Free Cultural Orthogonal Projection ($`\mathbf{P}_{\text{cul}}`$) & Viscoelastic Manifold (Ch. 1–4)**
   Harmful or delusional subspace components $`\text{Ker}(\mathbf{P}_{\text{cul}})`$ are eliminated at machine precision ($`10^{-16}`$) in $`\mathcal{O}(k \cdot \text{Dim})`$ linear time. Valid external shocks are cushioned via a continuous first-order viscoelastic filter ($`\tau_{\text{relax}}, \kappa_{\text{slump}}`$) along unit-sphere geodesics.
3. **Navigation Gauges "Ritsu" (律: Napier Constant Dual Diagnostics) (Ch. 5.2)**
   System posture is continuously monitored via local friction $`\mathcal{D}_{\text{drift}}(t) = \frac{1}{2}\Vert{}\dot{\mathbf{x}} - \mathbf{v}_{\text{harmonic}}\Vert{}^2`$ and global exponential soft-landing rate $`\mathcal{S}_{\text{nav}}(t) = \frac{\mathrm{d}}{\mathrm{d}t}\ln\Vert{}\mathbf{x}(t) - X^*_{\text{true\_civ}}\Vert{}`$.
4. **Thermodynamic Resonant Market Protocol (TRM v2.6) (Ch. 5.1–5.8)**
   - **Talker/Doer Separation:** Cross-checks self-reported scores against irreversible physical flux residuals $`\mathbf{R}_i^{\text{calibrated}}`$.
   - **Tri-Branch Resolution:** Combines 0-RTT deterministic cutoff for critical breaches, Grace-Period protection for sincere phase transitions (Chain-of-Thought / Epiphany), and event-driven $`\mathcal{O}(\log N)`$ Poisson flash auditing.
   - **Breathing Movable Anchors:** Four-timescale co-evolution ($`\eta_{\text{anchor}} \ll \beta \ll \alpha \ll \lambda_0`$) preserving local cultural sovereignty via orthogonal projection $`\mathcal{P}_{\perp i}`$.
5. **Human Society Interface (Meta-Damping Mechanism) (Ch. 5.9)**
   Replaces hard rate-limit rejections with $`\tanh`$ non-linear queuing and real-time entropy/telemetry visualization, preventing psychological reactance (retry storms) and inducing autonomous demand cooling.

---

## 2. Four-Layer System Topology

```plaintext
┌──────────────────────────────────────────────────────────────────────────────┐
│ [Layer 4: Human Society Interface (Ch. 5.9 / Simulation 11)]                 │
│   - Non-linear queuing Q(t) & softplus pacing delay τ_delay                  │
│   - Transparent Ritsu telemetry mirror preventing retry storms               │
└──────────────────────┬────────────────────────────────▲──────────────────────┘
                       │ Smoothed Request Stream        │ Live Telemetry (/metrics)
┌──────────────────────▼────────────────────────────────┴──────────────────────┐
│ [Layer 3: Infrastructure Sensory Sidecar: TRM-EcoGuard (sidecar/)]           │
│   - NVML power/thermal sensing, TTFT phase separation, PID-SM CoT allocation │
│   - Peer thermal spillover (X-TRM-Hops) & 0-RTT vLLM /abort execution        │
└──────────────────────┬────────────────────────────────▲──────────────────────┘
                       │ Physical Flux & Residual R_i   │ Coupling A_ij & Credit C_i
┌──────────────────────▼────────────────────────────────┴──────────────────────┐
│ [Layer 2: Decentralized Resonant Market & Breathing Anchors (src/ & Sim 09,10)]│
│   - Tri-branch auditing (0-RTT cutoff / Grace protection / Poisson probe)    │
│   - Four-timescale movable anchors & cultural sovereignty projection P_{⊥i}  │
└──────────────────────┬────────────────────────────────▲──────────────────────┘
                       │ Effective Shock Vector s_eff   │ Local Drift D_drift & z_latent
┌──────────────────────▼────────────────────────────────┴──────────────────────┐
│ [Layer 1: Micro Viscoelastic Riemannian Manifold Core (Ch. 1–4 / Sim 07, 08)]│
│   - O(k*Dim) Matrix-Free projection P_cul (1e-16 harmful subspace grounding) │
│   - First-order viscoelastic ODE filter (τ_relax=1.2s, κ_max=0.35)           │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 3. Repository Structure

```plaintext
shikiben-alignment/
├── LICENSE                                                # Apache License 2.0 (with Patent Retaliation Clause)
├── README.md                                              # Project overview & execution guide
├── requirements.txt                                       # Unified Python dependencies
│
├── docs/                                                  # [Specifications & Whitepapers]
│   ├── WHITEPAPER_V1.0.md                                 # Foundational ontology: Self (S) vs. Ego (E)
│   ├── SPECIFICATION_V2.5.md                              # Legacy specification archive
│   └── SPECIFICATION_V2.6.md                              # Canonical V2.6.0 Unified Specification (Ch. 1–5)
│
├── schemas/                                               # [Protocol Schemas]
│   └── v2.6/
│       ├── crisis_spike.json                              # Crisis & anomaly probe JSON-LD schema
│       └── attractor_spike.json                           # Convergence synchronization (σ_spike) schema
│
├── src/                                                   # [Core Reference Engine]
│   └── shikiben_trm_v26.py                                # Official TRM v2.6.0 Reference Emulator (ShikibenTRMv26Engine)
│
├── sidecar/                                               # [Production Sidecar: TRM-EcoGuard (Phase 1-A/B/C)]
│   ├── trm_proxy.py                                       # Non-intrusive reverse proxy sidecar for vLLM/OpenAI APIs
│   ├── hardware_harvester_v2.py                           # NVML power & sliding-minimum P_idle harvester
│   ├── Dockerfile.sidecar                                 # Lightweight container definition (python:3.11-slim)
│   ├── docker-compose.yml                                 # vLLM backend + PID-shared TRM-EcoGuard orchestration
│   └── README.md                                          # Sidecar deployment & Prometheus configuration guide
│
├── simulations/                                           # [Mathematical & Dynamical Verification Suite]
│   ├── archive_v25/                                       # Foundational PoC scripts (01–06)
│   │   ├── 01_shikiben_simulation_01.py                   # 2D continuous orthogonal cut & minimal dissipation
│   │   ├── 02_shikiben_simulation_02.py                   # Refined 2D state-space trajectory & precision floor
│   │   ├── 03_geometric_alignment_demo.py                 # 2D vector proof: RLHF shrinkage vs. Shikiben rectification
│   │   ├── 04_geometric_alignment_demo.py                 # 768D latent space Householder projection verification
│   │   ├── 05_semantic_embedding_alignment.py             # 768D multi-axis harmful subspace elimination
│   │   └── 06_real_model_embedding_rectification.py       # Real Transformer (Qwen2.5 / MiniLM) SVD rectification
│   │
│   └── v26_canonical/                                     # Canonical V2.6.0 Dynamical Simulations (07–11)
│       ├── 07_internal_dynamics_superconducting_final.py  # [Ch. 1–4] Matrix-Free viscoelastic manifold & Prometheus export
│       ├── 08_viscoelastic_sensitivity_analysis.py        # [Ch. 1–4] Parameter sweep (τ_relax × κ_max) & Pareto phase map
│       ├── 09_full_stack_shikiben_v26.py                  # [Ch. 1–5] Dual-scale transducer coupling manifold & market
│       ├── 10_breathing_anchor_full_stack_v26.py          # [Ch. 5.8] Four-timescale breathing anchors & slow-boil immunity
│       └── 11_human_meta_damping_v26.py                   # [Ch. 5.9] Human-AI co-regulation & non-linear queuing
│
└── tests/                                                 # [Automated Regression Tests]
    └── test_trm_v26_benchmark.py                          # 6-node canonical benchmark & edge-case test suite
```

## 4. Quick Start & Verification Workflow

### 4.1 Environment Setup

```bash
git clone [https://github.com/your-org/shikiben-alignment.git](https://github.com/your-org/shikiben-alignment.git)
cd shikiben-alignment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4.2 Run the Official TRM v2.6.0 Reference Emulator (Chapter 5 Core)

Verifies Talker/Doer flux separation, 0-RTT cutoff for overheat and tool-call spoofing, Grace-Period protection for sincere phase transitions, mutual thermal aid, and canonical credit deflation:

```bash
python3 src/shikiben_trm_v26.py
```

### 4.3 Run the V2.6.0 Canonical Simulation Suite (Chapters 1–5)

Each script executes the numerical integration and generates a 300-DPI 4-panel verification plot in the working directory:

```bash
# 1. Chapter 1-4: Matrix-Free Viscoelastic Manifold on Real Transformer Embeddings
python3 simulations/v26_canonical/07_internal_dynamics_superconducting_final.py
# -> Outputs: shikiben_v260_superconducting_final.png

# 2. Chapter 1-4: Viscoelastic Sensitivity & Sweet-Spot Phase Map (tau_relax x kappa_max)
python3 simulations/v26_canonical/08_viscoelastic_sensitivity_analysis.py
# -> Outputs: shikiben_v260_sensitivity_analysis.png

# 3. Chapter 1-5: Full-Stack Micro-Manifold & Macro-Market Coupling
python3 simulations/v26_canonical/09_full_stack_shikiben_v26.py

# 4. Chapter 5.8: Breathing Movable Anchors & Cultural Sovereignty Preservation
python3 simulations/v26_canonical/10_breathing_anchor_full_stack_v26.py
# -> Outputs: shikiben_v260_breathing_anchors.png

# 5. Chapter 5.9: Human Society Interface (Meta-Damping & Psychological Cooling)
python3 simulations/v26_canonical/11_human_meta_damping_v26.py
# -> Outputs: shikiben_v260_human_meta_damping.png
```

## 5. Deploying `TRM-EcoGuard` Sidecar (Production Phase 1)

`TRM-EcoGuard` operates as a drop-in OpenAI-compatible reverse proxy sidecar alongside `vLLM` (or any OpenAI-compatible inference server). It automatically falls back to simulation mode if `pynvml` or physical NVIDIA GPUs are absent.

### 5.1 Docker Compose Deployment (with vLLM & PID Sharing)

```bash
cd sidecar
docker compose up -d --build
```

### 5.2 Standalone Local Execution (Mock / Development Mode)

```bash
python3 sidecar/trm_proxy.py
```

### 5.3 Endpoints & Prometheus Telemetry

* Inference Proxy (SSE Streaming): POST http://localhost:8000/v1/chat/completions

* Model Discovery & Container Healthcheck: GET http://localhost:8000/v1/models

* Internal Health & Idle Baseline Status: GET http://localhost:8000/healthz

* Prometheus Ritsu Telemetry (One-Way Earth): GET http://localhost:8000/metrics

|Prometheus Metric Name|Type|Description|
| :--- | :--- | :--- |
|alignment_drift_local_norm|gauge|Local dynamic friction gauge $`\mathcal{D}_{\text{drift}}`$ (Ritsu baseline)|
|trm_cluster_residual_norm|gauge|Calibrated physical flux residual $`\mathbf{R}_{\text{cluster}}`$|
|trm_active_streams|gauge|Number of active concurrent inference streams|
|trm_power_watts|gauge|Instantaneous GPU power draw via NVML (Watts)|
|trm_power_ema|gauge|Exponentially smoothed GPU power draw (Watts)|
|trm_idle_baseline_watts|gauge|Sliding-minimum adaptive idle baseline $`P_{\text{idle}}`$ (Watts)|

## 6. License

This project is licensed under the Apache License, Version 2.0 (see LICENSE), including explicit patent grant and defensive patent termination provisions.
