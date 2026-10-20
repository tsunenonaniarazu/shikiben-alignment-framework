# TRM-EcoGuard: Physical Thermal & Workload Guard for LLM Clusters

TRM-EcoGuard is an ultra-lightweight, zero-intrusion reverse proxy sidecar 
designed for high-throughput LLM clusters (vLLM, Ollama, TensorRT-LLM).

## Key Features
- **Zero-Latency Pass-Through:** Sub-millisecond proxying for streaming chat completions.
- **Hardware Grounding:** Measures real-time GPU power draw (via NVML) and prevents catastrophic thermal throttle spikes.
- **Runaway & Spoofing Breaker:** Instantly severs rogue connections (0-RTT TCP termination) when execution workload exceeds physical hardware capacity.
- **Drop-in OpenAI Compatibility:** Works seamlessly without changing a single line of backend model code.

## Quick Start
```bash
docker compose up -d
# Point your client to http://localhost:8000/v1
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Hello"}], "stream": true}'
```

## Architecture
TRM-EcoGuard continuously balances token generation telemetry against live physical flux,
ensuring sustainable cluster operation under extreme concurrency.
