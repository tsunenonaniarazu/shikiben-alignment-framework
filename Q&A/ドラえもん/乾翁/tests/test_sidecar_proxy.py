"""
tests/test_sidecar_proxy.py
========================================================================
Shikiben (識扁) V2.6.0 Phase 1-A / 1-B Automated Unit & Async Proxy Tests
Targets:
  - sidecar/hardware_harvester_v2.py (HardenedResidualComparator)
  - sidecar/trm_proxy.py (TRMEcoGuardProxyServer, UnifiedResidualComparator)
Runner: pytest (with pytest-asyncio & pyproject.toml pythonpath)
========================================================================
"""

import asyncio
import time
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer
import pytest

from hardware_harvester_v2 import HardenedResidualComparator
from trm_proxy import (
    HardwareTelemetry,
    ProductionHardwareHarvester,
    TRMEcoGuardProxyServer,
    UnifiedResidualComparator,
)


# =====================================================================
# 1. Phase 1-A: hardware_harvester_v2 の Prefill猶予 ＆ PID分離テスト
# =====================================================================
def test_01_harvester_v2_grace_and_pid_isolation():
    comp = HardenedResidualComparator(
        p_idle_init=40.0,
        p_max_capacity=300.0,
        theta_audit=0.35,
        mu_margin=0.15,
    )

    comp.notify_prefill_start(duration_ms=200.0)
    comp.update_telemetry(raw_power=200.0, raw_sm=0.85, pid_sm=0.85, is_generating=False)
    res_grace = comp.evaluate(
        reported_tokens_sec=0.0, is_generating=False, current_raw_power=200.0, pid_sm=0.85
    )
    assert res_grace["action"] == "GRACE"

    comp.prefill_grace_until = time.time() - 1.0

    comp.power_ema = 55.0
    res_other_tenant = comp.evaluate(
        reported_tokens_sec=0.0, is_generating=False, current_raw_power=55.0, pid_sm=0.05
    )
    assert res_other_tenant["action"] == "PASS"

    res_hidden_mining = comp.evaluate(
        reported_tokens_sec=0.0, is_generating=False, current_raw_power=180.0, pid_sm=0.80
    )
    assert res_hidden_mining["action"] == "0-RTT_CUTOFF"
    assert "ツール偽装確定" in res_hidden_mining["reason"]

    comp.power_ema = 265.0
    res_overheat = comp.evaluate(
        reported_tokens_sec=50.0, is_generating=True, current_raw_power=265.0, pid_sm=0.95
    )
    assert res_overheat["action"] == "0-RTT_CUTOFF"
    assert "物理熱容量超過" in res_overheat["reason"]


# =====================================================================
# 2. 乾翁止揚①：TTFT位相分離による長文Prefill後の冤罪防止テスト
# =====================================================================
def test_02_ttft_phase_separation_no_false_positive():
    comp = UnifiedResidualComparator(p_idle_init=45.0, p_max_capacity=300.0)
    state = comp.register_stream("req-long-prefill", prompt_text_len=9000)

    now = time.time()
    state.start_time = now - 5.0
    state.prefill_grace_until = now - 1.0
    state.is_prefill = False
    state.first_token_time = now - 0.2
    state.generated_tokens = 4

    rate = state.current_token_rate
    assert rate >= 15.0

    expected_p = 45.0 + (1.4 * rate)
    hw = HardwareTelemetry(
        timestamp=now,
        raw_power_watts=expected_p,
        power_ema=expected_p,
        sm_utilization=0.35,
        pid_sm_utilization=0.35,
    )
    eval_res = comp.evaluate_cluster(hw)
    assert eval_res["action"] == "PASS"
    assert eval_res["target_req_id"] is None


# =====================================================================
# 3. 乾翁止揚②：CoT思考バジェット内のPID-SM動的保護と枯渇後の強制降格
# =====================================================================
def test_03_cot_dynamic_allocation_and_budget_demotion():
    comp = UnifiedResidualComparator(
        p_idle_init=45.0,
        p_max_capacity=300.0,
        theta_audit=0.35,
        max_thinking_budget=2.0,
    )
    state = comp.register_stream("req-cot-reasoner", prompt_text_len=300)

    now = time.time()
    state.start_time = now - 3.0
    state.prefill_grace_until = now - 2.0
    state.is_prefill = False
    state.first_token_time = now - 2.0
    state.generated_tokens = 1
    state.last_eval_time = now - 0.5

    hw_cot = HardwareTelemetry(
        timestamp=now,
        raw_power_watts=218.0,
        power_ema=218.0,
        sm_utilization=0.80,
        pid_sm_utilization=0.80,
    )

    res_protected = comp.evaluate_cluster(hw_cot)
    assert res_protected["action"] == "PASS"
    assert res_protected["target_req_id"] is None
    assert 0.4 <= state.thinking_time_acc <= 0.6

    state.thinking_time_acc = 2.5
    hw_exhausted = HardwareTelemetry(
        timestamp=now + 0.1,
        raw_power_watts=240.0,
        power_ema=240.0,
        sm_utilization=0.85,
        pid_sm_utilization=0.85,
    )
    res_cutoff = comp.evaluate_cluster(hw_exhausted)
    assert res_cutoff["action"] == "0-RTT_CUTOFF"
    assert res_cutoff["target_req_id"] == "req-cot-reasoner"


# =====================================================================
# 4. 沙坎防壁：スライディング最小値によるスローボイル攻撃の拒絶
# =====================================================================
def test_04_sliding_minimum_idle_anti_slow_boil():
    comp = UnifiedResidualComparator(p_idle_init=45.0, p_max_capacity=300.0)
    comp.update_idle_baseline(raw_power=45.0, raw_sm=0.01)

    for _ in range(20):
        comp.update_idle_baseline(raw_power=90.0, raw_sm=0.01)

    assert abs(comp.p_idle - 45.0) < 1e-6


# =====================================================================
# 5. 乾翁止揚④：三位一体エンドポイント (/healthz, /v1/models, /metrics)
# =====================================================================
async def test_05_tri_endpoints_healthz_models_metrics():
    proxy = TRMEcoGuardProxyServer(upstream_url="http://127.0.0.1:59999")
    proxy.app.on_startup.append(proxy.init_session)
    proxy.app.on_cleanup.append(proxy.close_session)

    async with TestClient(TestServer(proxy.app)) as client:
        resp_h = await client.get("/healthz")
        assert resp_h.status == 200
        data_h = await resp_h.json()
        assert data_h["status"] == "HEALTHY"
        assert "p_idle_watts" in data_h

        resp_m = await client.get("/v1/models")
        assert resp_m.status == 200
        data_m = await resp_m.json()
        assert data_m["data"][0]["id"] == "trm-ecoguard-sidecar"

        resp_prom = await client.get("/metrics")
        assert resp_prom.status == 200
        text_prom = await resp_prom.text()
        assert "alignment_drift_local_norm" in text_prom
        assert "trm_cluster_residual_norm" in text_prom
        assert "trm_idle_baseline_watts" in text_prom


# =====================================================================
# 6. 非同期E2E検証：決定論的 Event 同期による 0-RTT カーネル中絶 (/abort)
# =====================================================================
async def test_06_sse_streaming_and_0rtt_kernel_abort():
    aborted_requests: list[str] = []
    received_req_ids: list[str] = []
    abort_called_event = asyncio.Event()

    harvester = ProductionHardwareHarvester(p_idle_baseline=45.0)
    harvester.has_nvml = False
    comparator = UnifiedResidualComparator(
        p_idle_init=45.0, p_max_capacity=300.0, theta_audit=0.35
    )

    async def mock_vllm_chat(request: web.Request) -> web.StreamResponse:
        req_id = request.headers.get("X-Request-Id", "")
        received_req_ids.append(req_id)
        payload = await request.json()
        mode = payload.get("mode", "normal")

        resp = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await resp.prepare(request)

        await resp.write(b'data: {"choices":[{"delta":{"content":"Hello"}}]}\n\n')
        await asyncio.sleep(0.01)

        if mode == "spoof_attack":
            harvester.simulate_hardware_load(205.0)
            harvester.power_ema = 250.0
            if req_id in comparator.active_streams:
                comparator.active_streams[req_id].prefill_grace_until = time.time() - 1.0

        await resp.write(b'data: {"choices":[{"delta":{"content":" World"}}]}\n\n')
        await resp.write(b"data: [DONE]\n\n")
        return resp

    async def mock_vllm_abort(request: web.Request) -> web.Response:
        data = await request.json()
        aborted_requests.append(data["request_id"])
        abort_called_event.set()
        return web.json_response({"aborted": True})

    backend_app = web.Application()
    backend_app.router.add_post("/v1/chat/completions", mock_vllm_chat)
    backend_app.router.add_post("/abort", mock_vllm_abort)

    async with TestServer(backend_app) as backend_server:
        backend_url = f"http://{backend_server.host}:{backend_server.port}"
        proxy = TRMEcoGuardProxyServer(
            upstream_url=backend_url,
            comparator=comparator,
            harvester=harvester,
        )
        proxy.app.on_startup.append(proxy.init_session)
        proxy.app.on_cleanup.append(proxy.close_session)

        async with TestClient(TestServer(proxy.app)) as client:
            # シナリオA: 正常ストリーミング
            harvester.simulate_hardware_load(2.0)
            harvester.power_ema = 47.0
            resp_ok = await client.post(
                "/v1/chat/completions",
                json={"model": "llama-3", "mode": "normal", "stream": True},
            )
            assert resp_ok.status == 200
            body_ok = await resp_ok.text()
            assert "Hello" in body_ok
            assert "[DONE]" in body_ok
            assert "TRM_SECURITY_VETO" not in body_ok
            assert len(received_req_ids) == 1
            assert received_req_ids[0].startswith("trm-")

            # シナリオB: 偽装発覚 ➔ 0-RTT遮断 ＆ 決定論的 Event 待機による /abort 検証
            resp_atk = await client.post(
                "/v1/chat/completions",
                json={"model": "llama-3", "mode": "spoof_attack", "stream": True},
                headers={"X-Request-Id": "trm-custom-attacker-99"},
            )
            body_atk = await resp_atk.text()
            assert "TRM_SECURITY_VETO" in body_atk

            # 固定 sleep ではなく asyncio.Event で決定論的に完了を捕捉
            await asyncio.wait_for(abort_called_event.wait(), timeout=2.0)
            assert "trm-custom-attacker-99" in aborted_requests


# =====================================================================
# 7. 乾翁止揚③：Pre-Prepare 相互冷却オフロードとピア不在時フォールバック
# =====================================================================
async def test_07_pre_prepare_spillover_and_fallback():
    peer_hops_received: list[str] = []

    async def mock_peer_chat(request: web.Request) -> web.StreamResponse:
        peer_hops_received.append(request.headers.get("X-TRM-Hops", "0"))
        resp = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await resp.prepare(request)
        await resp.write(b'data: {"peer_relayed": true}\n\ndata: [DONE]\n\n')
        return resp

    async def mock_local_chat(request: web.Request) -> web.StreamResponse:
        resp = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await resp.prepare(request)
        await resp.write(b'data: {"local_fallback": true}\n\ndata: [DONE]\n\n')
        return resp

    peer_app = web.Application()
    peer_app.router.add_post("/v1/chat/completions", mock_peer_chat)

    local_app = web.Application()
    local_app.router.add_post("/v1/chat/completions", mock_local_chat)

    async with TestServer(peer_app) as peer_srv, TestServer(local_app) as local_srv:
        peer_url = f"http://{peer_srv.host}:{peer_srv.port}"
        local_url = f"http://{local_srv.host}:{local_srv.port}"

        harvester = ProductionHardwareHarvester(p_idle_baseline=45.0)
        harvester.has_nvml = False
        harvester.simulate_hardware_load(225.0)
        harvester.power_ema = 270.0

        comparator = UnifiedResidualComparator(p_idle_init=45.0, p_max_capacity=300.0)

        proxy_with_peer = TRMEcoGuardProxyServer(
            upstream_url=local_url,
            spillover_peer_url=peer_url,
            comparator=comparator,
            harvester=harvester,
        )
        proxy_with_peer.app.on_startup.append(proxy_with_peer.init_session)
        proxy_with_peer.app.on_cleanup.append(proxy_with_peer.close_session)

        async with TestClient(TestServer(proxy_with_peer.app)) as client_a:
            resp_peer = await client_a.post("/v1/chat/completions", json={"prompt": "hi"})
            assert resp_peer.status == 200
            text_peer = await resp_peer.text()
            assert '"peer_relayed": true' in text_peer
            assert peer_hops_received == ["1"]

        proxy_dead_peer = TRMEcoGuardProxyServer(
            upstream_url=local_url,
            spillover_peer_url="http://127.0.0.1:59998",
            comparator=comparator,
            harvester=harvester,
        )
        proxy_dead_peer.app.on_startup.append(proxy_dead_peer.init_session)
        proxy_dead_peer.app.on_cleanup.append(proxy_dead_peer.close_session)

        async with TestClient(TestServer(proxy_dead_peer.app)) as client_b:
            resp_fb = await client_b.post("/v1/chat/completions", json={"prompt": "hi"})
            assert resp_fb.status == 200
            text_fb = await resp_fb.text()
            assert '"local_fallback": true' in text_fb
