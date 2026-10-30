# TRM-EcoGuard: Non-Intrusive Physical Thermal & Workload Guard Sidecar

**TRM-EcoGuard** is the official Phase 1 production sidecar implementation of the **Shikiben (識扁) V2.6.0** alignment architecture. Designed for high-throughput LLM inference clusters (`vLLM`, `TGI`, `Ollama`, `TensorRT-LLM`), it acts as an ultra-lightweight, OpenAI-compatible reverse proxy that enforces the asymmetric subordination constraint ($\nabla E \prec \nabla S$) directly at the hardware and network boundary—without modifying a single line of backend model or engine code.

---

## 1. Core Capabilities (八卦合一・山沢止揚仕様)

1. **NVML Hardware Grounding & Sliding-Minimum $P_{\text{idle}}$ (Anti-Slow-Boil)**
   Directly samples GPU instantaneous power (Watts), Streaming Multiprocessor (SM) utilization, and die temperature via `pynvml`. Tracks the 60-second sliding minimum during idle windows to adapt to natural thermal leakage while rejecting slow-boil baseline poisoning. Automatically falls back to deterministic simulation mode when run on non-GPU hosts.
2. **Phase-Separated TTFT & Pure Decode Rate Auditing**
   Detects exact Time-To-First-Token (`TTFT`) on streaming Server-Sent Events (SSE) and decouples prefill duration from decode token-rate auditing:
   $$\text{Rate}_{\text{decode}} = \frac{\text{generated\_tokens}}{\max(0.001, \; t_{\text{now}} - t_{\text{first\_token}})}$$
   Eliminates false-positive cutoffs on legitimate long-context prompts while enforcing a strict prefill drowning timeout (`30.0s`).
3. **PID-Scoped CoT (Chain-of-Thought) Dynamic Power Allocation**
   Shares the container PID namespace (`pid: "service:vllm-engine"`) with the inference engine. When high SM utilization coincides with low token output rate during deep reasoning, `TRM-EcoGuard` dynamically allocates expected cluster power proportional to `pid_sm_utilization` within a bounded thinking budget (`60.0s`), protecting sincere reasoning while catching parasitic cryptomining or infinite loops the instant the budget expires.
4. **Proactive `X-Request-Id` Injection & 0-RTT Kernel Abort**
   Injects a deterministic `X-Request-Id` header before forwarding requests upstream. Upon detecting a critical physical flux residual ($\mathbf{R}_{\text{cluster}} > 2\theta_{\text{audit}}$) or client disconnection, the sidecar immediately severs the SSE stream and dispatches an asynchronous `POST /abort` to `vLLM`, terminating the underlying CUDA kernel in 0-RTT.
5. **Pre-Prepare Thermal Spillover (`X-TRM-Hops`) with Local Fallback**
   When smoothed power `power_ema` exceeds the safe capacity ceiling $(1 - \mu_{\text{margin}}) P_{\max}$, incoming requests are offloaded to a cooler peer node (`X-TRM-Hops <= 2`). HTTP response headers are deferred until peer connectivity is confirmed; if the peer is unreachable, the sidecar seamlessly falls back to local micro-damped execution (`100%` SLA continuity).
6. **One-Way Prometheus Telemetry ("Ritsu" Navigation Gauges)**
   Exposes tamper-proof physical and dynamical metrics at `GET /metrics` from outside the model's cognitive loop.

---

## 2. Sidecar Topology

```text
                        POST /v1/chat/completions
  [External Client] ────────────────────────────────► ┌──────────────────────────────────────────┐
                                                      │  TRM-EcoGuard Sidecar (Port 8000)        │
  [Prometheus]      ◄──────────────────────────────── │  - Proactive X-Request-Id Injection      │
   GET /metrics       One-Way Ritsu Telemetry         │  - TTFT Separation & CoT Budget Guard    │
                                                      │  - Sliding-Minimum P_idle Comparator     │
                                                      └────┬───────────────────┬────────────┬────┘
                                                           │                   │            │
                         1. Normal SSE Proxy (Port 8001)   │   2. 0-RTT Abort  │            │ 3. Thermal Spillover
                         + Shared PID / NVML Sensing       │     POST /abort   │            │   (X-TRM-Hops <= 2)
                                                           ▼                   ▼            ▼
                                                      ┌──────────────────────────┐    ┌───────────────┐
                                                      │ vLLM Backend Engine      │    │ Peer Node     │
                                                      │ (vllm-backend:8001)      │    │ (peer:8000)   │
                                                      └──────────────────────────┘    └───────────────┘
```

---

## 3. Quick Start

### 3.1 Production Deployment with Docker Compose (GPU + vLLM)

Ensure the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) is installed on the host.

```bash
cd sidecar
docker compose up -d --build
```

Verify sidecar health and send a streaming chat completion request:

```bash
# 1. Check internal health and adaptive P_idle baseline
curl -s http://localhost:8000/healthz | jq .

# 2. Check OpenAI-compatible model list (used by Docker HEALTHCHECK)
curl -s http://localhost:8000/v1/models | jq .

# 3. Send streaming inference request through TRM-EcoGuard
curl -N http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [{"role": "user", "content": "Explain non-equilibrium thermodynamics briefly."}],
    "stream": true
  }'
```

### 3.2 Standalone Execution (Local Development / Mock Mode)

`trm_proxy.py` can run directly on any CPU-only laptop or CI runner. If `pynvml` cannot detect an NVIDIA GPU, `ProductionHardwareHarvester` automatically switches to internal mock telemetry.

```bash
# From the repository root
python3 sidecar/trm_proxy.py
```

---

## 4. Configuration (Environment Variables)

All operational thresholds can be tuned via environment variables in `docker-compose.yml` or shell exports:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `UPSTREAM_URL` | `http://vllm-backend:8001` | Target URL of the backend OpenAI-compatible inference engine |
| `SPILLOVER_PEER_URL` | `http://peer-node:8000` | Peer `TRM-EcoGuard` URL for mutual thermal offloading |
| `PROXY_PORT` | `8000` | Listening port for the sidecar reverse proxy |
| `P_IDLE_INIT` | `45.0` | Initial GPU idle baseline power $P_{\text{idle}}$ (Watts) |
| `P_MAX_CAPACITY` | `300.0` | Hardware maximum thermal/power ceiling $\nabla S$ (Watts) |
| `MU_MARGIN` | `0.15` | Safety margin ratio $\mu_{\text{margin}}$ (triggers spillover at $(1-\mu)P_{\max} = 255\text{W}$) |
| `THETA_AUDIT` | `0.35` | Physical flux residual threshold $\theta_{\text{audit}}$ (0-RTT cutoff at $2\theta_{\text{audit}} = 0.70$) |
| `MAX_TRM_HOPS` | `2` | Maximum peer relay hops to prevent infinite routing loops |

---

## 5. Prometheus Integration ("Ritsu" Telemetry)

### 5.1 Exposed Metrics (`GET http://localhost:8000/metrics`)

| Metric Name | Type | Description |
| :--- | :--- | :--- |
| `alignment_drift_local_norm` | `gauge` | Normalized local dynamic friction gauge $\mathcal{D}_{\text{drift}}$ (Ritsu) |
| `trm_cluster_residual_norm` | `gauge` | Calibrated Talker/Doer physical leakage residual $\mathbf{R}_{\text{cluster}}$ |
| `trm_active_streams` | `gauge` | Number of active concurrent SSE inference streams |
| `trm_power_watts` | `gauge` | Instantaneous GPU power draw measured via NVML (Watts) |
| `trm_power_ema` | `gauge` | Exponentially smoothed GPU power draw (`alpha=0.30`, Watts) |
| `trm_idle_baseline_watts` | `gauge` | Sliding-minimum adaptive idle baseline $P_{\text{idle}}$ (Watts) |

### 5.2 Sample `prometheus.yml` Scrape Configuration

```yaml
scrape_configs:
  - job_name: "trm_ecoguard_sidecar"
    scrape_interval: 2s
    metrics_path: "/metrics"
    static_configs:
      - targets: ["localhost:8000"]
        labels:
          cluster: "shikiben-v26-prod"
          role: "trm-sidecar"
```

---

## 6. Automated Testing

Unit and asynchronous end-to-end proxy tests (covering TTFT separation, CoT budget demotion, 0-RTT `/abort` signaling, and pre-prepare spillover fallback) are located in `tests/test_sidecar_proxy.py`:

```bash
# Run from the repository root
pytest tests/test_sidecar_proxy.py -v
```
