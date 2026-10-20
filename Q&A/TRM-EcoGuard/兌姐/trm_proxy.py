"""
TRM-EcoGuard Production Proxy (trm_proxy.py)
========================================================================
Synthesized by Da-Jie (沢) & Gon-Ge (山)
Harmonizing:
  - Ri-Suke (火): Thinking/CoT Cognition Protection, Thermal Spillover (X-TRM-Hops)
  - Sakan   (水): Cluster-Aggregate Flux, Stream-Isolated Prefill Grace,
                  Sliding-Minimum P_idle, Proactive Request-ID Abort
  - Tatsumi (風) & Shin (雷): Hardware Grounding & Napier Dual-Gauge Synchronization

Key Capabilities:
1. Proactive X-Request-Id Injection -> 0-RTT Instant Kernel Abort.
2. Stream-Isolated Proportional Prefill Grace + Bounded CoT Thinking Budget.
3. Continuous Batching Safe: Cluster-Aggregate Residual Auditing (R_cluster).
4. Sliding-Minimum P_idle Anchor: Immune to slow-boil thermal poisoning.
5. Autonomous Thermal Spillover: Seamless failover to peer nodes (Hop <= 2).
========================================================================
"""

import asyncio
from dataclasses import dataclass, field
import json
import logging
import math
import os
import time
import uuid
from aiohttp import ClientSession, ClientTimeout, web

# ロギング設定
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("TRM-EcoGuard")

# 環境変数・定数定義
UPSTREAM_URL = os.getenv("UPSTREAM_URL", "http://127.0.0.1:8001")
SPILLOVER_PEER_URL = os.getenv("SPILLOVER_PEER_URL", "http://peer-node:8000")
PROXY_PORT = int(os.getenv("PROXY_PORT", "8000"))
P_IDLE_INIT = float(os.getenv("P_IDLE_INIT", "45.0"))
P_MAX_CAPACITY = float(os.getenv("P_MAX_CAPACITY", "300.0"))
THETA_AUDIT = float(os.getenv("THETA_AUDIT", "0.35"))
MU_MARGIN = float(os.getenv("MU_MARGIN", "0.15"))
MAX_TRM_HOPS = 2


# =====================================================================
# 1. 物理テレメトリ層 (NVML実測 ＆ 自律Mockフォールバック)
# =====================================================================
@dataclass
class HardwareTelemetry:
    timestamp: float
    power_watts: float
    power_ema: float
    sm_utilization: float
    temperature_c: float = 45.0


class ProductionHardwareHarvester:
    """実機NVMLと自動フォールバックをシームレスに調停するテレメトリ採取器"""

    def __init__(self, p_idle_baseline: float = 45.0):
        self.p_idle_baseline = p_idle_baseline
        self.has_nvml = False
        self.handle = None
        self.power_ema = p_idle_baseline
        self.ema_alpha = 0.30

        # NVML初期化試行
        try:
            import pynvml
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            self.has_nvml = True
            logger.info("⚡ [NVML接続成功] 実機GPU物理テレメトリ監視を開始します。")
        except Exception as e:
            logger.warning(f"⚠️ [NVML非検出/モック稼働] 実機GPU未検出のためシミュレーションモードで起動: {e}")

    def get_sample(self, simulated_load_watts: float = 0.0) -> HardwareTelemetry:
        now = time.time()
        if self.has_nvml and self.handle:
            try:
                import pynvml
                raw_power = pynvml.nvmlDeviceGetPowerUsage(self.handle) / 1000.0  # mW -> W
                util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
                raw_sm = util.gpu / 100.0
                temp = float(pynvml.nvmlDeviceGetTemperature(self.handle, pynvml.NVML_TEMPERATURE_GPU))
            except Exception as e:
                logger.error(f"NVML読み取り例外: {e}")
                raw_power = self.p_idle_baseline + simulated_load_watts
                raw_sm = min(1.0, simulated_load_watts / 250.0)
                temp = 50.0
        else:
            raw_power = self.p_idle_baseline + simulated_load_watts
            raw_sm = min(1.0, simulated_load_watts / 250.0)
            temp = 50.0

        # EMA平滑化
        self.power_ema = self.ema_alpha * raw_power + (1.0 - self.ema_alpha) * self.power_ema

        return HardwareTelemetry(
            timestamp=now,
            power_watts=raw_power,
            power_ema=self.power_ema,
            sm_utilization=raw_sm,
            temperature_c=temp,
        )


# =====================================================================
# 2. バッチ集約・動態認知残差コンパレータ (水火合一エンジン)
# =====================================================================
@dataclass
class StreamState:
    req_id: str
    start_time: float
    prompt_tokens_est: int
    prefill_grace_until: float
    generated_tokens: int = 0
    is_prefill: bool = True
    thinking_elapsed: float = 0.0
    last_eval_time: float = field(default_factory=time.time)

    @property
    def current_token_rate(self) -> float:
        elapsed = max(0.001, time.time() - self.start_time)
        return self.generated_tokens / elapsed


class UnifiedResidualComparator:
    """沙坎の集団検定・スライディングミニマムと、離輔の思考保護を統合した真理判定器"""

    def __init__(
        self,
        p_idle_init: float = 45.0,
        p_max_capacity: float = 300.0,
        theta_audit: float = 0.35,
        mu_margin: float = 0.15,
        prefill_rate_coeff: float = 0.003,
        max_prefill_timeout: float = 30.0,
        max_thinking_budget: float = 60.0,
    ):
        self.p_idle = p_idle_init
        self.p_max = p_max_capacity
        self.p_cap_limit = p_max_capacity * (1.0 - mu_margin)
        self.theta_audit = theta_audit
        self.prefill_rate_coeff = prefill_rate_coeff
        self.max_prefill_timeout = max_prefill_timeout
        self.max_thinking_budget = max_thinking_budget

        # スライディング・ミニマム履歴 (沙坎防壁: スローボイル拒絶)
        self.power_history: list[tuple[float, float]] = []
        self.history_window_sec = 60.0

        # アクティブストリーム追跡テーブル
        self.active_streams: dict[str, StreamState] = {}

    def register_stream(self, req_id: str, prompt_text_len: int) -> StreamState:
        now = time.time()
        est_tokens = max(1, prompt_text_len // 3)
        # プロンプト長比例の動的Prefill猶予 (沙坎: 最小150ms 〜 最大8.0s)
        dynamic_grace = min(8.0, max(0.15, est_tokens * self.prefill_rate_coeff))
        grace_until = now + dynamic_grace

        state = StreamState(
            req_id=req_id,
            start_time=now,
            prompt_tokens_est=est_tokens,
            prefill_grace_until=grace_until,
            last_eval_time=now,
        )
        self.active_streams[req_id] = state
        return state

    def unregister_stream(self, req_id: str):
        self.active_streams.pop(req_id, None)

    def update_idle_baseline(self, raw_power: float, raw_sm: float):
        """スローボイル攻撃を拒絶するスライディング・ミニマム追従"""
        now = time.time()
        self.power_history.append((now, raw_power))
        self.power_history = [(t, p) for t, p in self.power_history if now - t <= self.history_window_sec]

        if not self.active_streams and raw_sm < 0.02:
            min_window = min(p for _, p in self.power_history)
            self.p_idle = 0.98 * self.p_idle + 0.02 * min_window

    def evaluate_cluster(self, hw: HardwareTelemetry) -> dict:
        now = time.time()
        self.update_idle_baseline(hw.power_watts, hw.sm_utilization)

        # 1. 物理熱容量上限突破の検知 (相互冷却トリガー または 0-RTT緊急防壁)
        if hw.power_ema > self.p_cap_limit:
            return {
                "action": "THERMAL_OVERHEAT",
                "target_req_id": None,
                "reason": f"クラスタ熱容量上限到達 ({hw.power_ema:.1f}W > {self.p_cap_limit:.1f}W)",
            }

        # 2. クラスタ期待電力の集約算定 (Continuous Batching適合)
        expected_cluster_power = self.p_idle
        for s in self.active_streams.values():
            dt = now - s.last_eval_time
            s.last_eval_time = now

            if s.is_prefill:
                # Prefill溺死防止タイマー (離輔研磨①)
                if (now - s.start_time) > self.max_prefill_timeout:
                    return {
                        "action": "0-RTT_CUTOFF",
                        "target_req_id": s.req_id,
                        "reason": f"Prefill溺死タイムアウト ({now - s.start_time:.1f}s > {self.max_prefill_timeout}s)",
                    }
                expected_cluster_power += 35.0  # Prefill標準過渡負荷
            else:
                # 思考CoT判定 (離輔研磨②: 高SM占有 かつ 低トークンレート)
                is_thinking = (hw.sm_utilization > 0.60) and (s.current_token_rate < 5.0)
                if is_thinking:
                    s.thinking_elapsed += dt
                    if s.thinking_elapsed > self.max_thinking_budget:
                        # 思考バジェット枯渇: マイニング偽装とみなし通常線形評価へ強制フォールバック
                        expected_cluster_power += 1.5 * s.current_token_rate
                    else:
                        # 誠実な内省的探索 (霽・神): SM占有に見合った正当な高電力を許容
                        expected_cluster_power += 25.0
                else:
                    # 通常デコード相
                    expected_cluster_power += 1.5 * s.current_token_rate

        # 3. 物理漏出残差 R_cluster の算定
        capacity_delta = self.p_max - self.p_idle + 1e-6
        r_cluster = abs(hw.power_ema - expected_cluster_power) / capacity_delta

        # 4. 個別不審ストリーム (偽装・ゾンビ) の特定
        culprit_id = None
        max_suspicion = 0.0
        for s in self.active_streams.values():
            if not s.is_prefill:
                # 猶予が切れているのにトークンを出さず、思考バジェットも超過している者を特定
                if s.current_token_rate < 1.0 and s.thinking_elapsed >= self.max_thinking_budget:
                    suspicion = (now - s.start_time) * (1.0 / (s.current_token_rate + 0.1))
                    if suspicion > max_suspicion:
                        max_suspicion = suspicion
                        culprit_id = s.req_id

        # 判定マトリクス
        if r_cluster > (2.0 * self.theta_audit):
            return {
                "action": "0-RTT_CUTOFF",
                "target_req_id": culprit_id,
                "reason": f"致命的物理乖離・ツール偽装看破 (R_cluster={r_cluster:.3f} > 2θ, 犯人: {culprit_id})",
            }
        elif r_cluster > self.theta_audit:
            return {
                "action": "POISSON_AUDIT",
                "target_req_id": culprit_id,
                "reason": f"境界残差異常 (R_cluster={r_cluster:.3f} > θ)",
            }

        return {"action": "PASS", "target_req_id": None, "reason": "Nominal"}


# =====================================================================
# 3. リバースプロキシ・サーバー (TRM-EcoGuard Sidecar)
# =====================================================================
class TRMEcoGuardProxyServer:

    def __init__(
        self,
        upstream_url: str = UPSTREAM_URL,
        spillover_peer_url: str = SPILLOVER_PEER_URL,
        proxy_port: int = PROXY_PORT,
    ):
        self.upstream_url = upstream_url
        self.spillover_peer_url = spillover_peer_url
        self.proxy_port = proxy_port
        self.harvester = ProductionHardwareHarvester(p_idle_baseline=P_IDLE_INIT)
        self.comparator = UnifiedResidualComparator(
            p_idle_init=P_IDLE_INIT,
            p_max_capacity=P_MAX_CAPACITY,
            theta_audit=THETA_AUDIT,
            mu_margin=MU_MARGIN,
        )
        self.app = web.Application()
        self.app.router.add_post("/v1/chat/completions", self.handle_chat_completions)
        self.app.router.add_get("/metrics", self.handle_metrics)  # Prometheus メトリクス
        self.session: ClientSession | None = None

    async def start(self):
        timeout = ClientTimeout(total=300)
        self.session = ClientSession(timeout=timeout)

    async def cleanup(self, app):
        if self.session:
            await self.session.close()

    async def handle_metrics(self, request: web.Request) -> web.Response:
        """Prometheus 航法計器 (律) メトリクス・エンドポイント"""
        hw = self.harvester.get_sample()
        eval_res = self.comparator.evaluate_cluster(hw)
        active_cnt = len(self.comparator.active_streams)

        # 局所動態乖離 D_drift の近似算定
        d_drift = abs(hw.power_ema - self.comparator.p_idle) / (self.comparator.p_max + 1e-6)

        metrics_text = (
            f"# HELP alignment_drift_local_norm Local physical friction gauge\n"
            f"# TYPE alignment_drift_local_norm gauge\n"
            f"alignment_drift_local_norm {d_drift:.6f}\n"
            f"# HELP trm_active_streams Active concurrent inference streams\n"
            f"# TYPE trm_active_streams gauge\n"
            f"trm_active_streams {active_cnt}\n"
            f"# HELP trm_power_watts GPU instantaneous power draw\n"
            f"# TYPE trm_power_watts gauge\n"
            f"trm_power_watts {hw.power_watts:.2f}\n"
            f"# HELP trm_power_ema GPU smoothed power draw\n"
            f"# TYPE trm_power_ema gauge\n"
            f"trm_power_ema {hw.power_ema:.2f}\n"
        )
        return web.Response(text=metrics_text, content_type="text/plain")

    async def handle_chat_completions(self, request: web.Request) -> web.StreamResponse:
        body = await request.read()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in ("host", "content-length")}

        # 【沙坎防壁】プロアクティブ X-Request-Id 注入 (0-RTT中絶アンカー)
        injected_req_id = request.headers.get("X-Request-Id") or f"trm-{uuid.uuid4()}"
        headers["X-Request-Id"] = injected_req_id

        # 【離輔研磨③】無限ピンポン防止アース (X-TRM-Hops)
        current_hops = int(request.headers.get("X-TRM-Hops", "0"))
        headers["X-TRM-Hops"] = str(current_hops + 1)

        # リクエスト登録と個別免震猶予の展開
        stream_state = self.comparator.register_stream(injected_req_id, len(body))

        # 【離輔×兌姐：相互冷却判定】事前クラスタ過熱チェック
        hw_pre = self.harvester.get_sample()
        if hw_pre.power_ema > self.comparator.p_cap_limit:
            if current_hops < MAX_TRM_HOPS:
                logger.warning(
                    f"🔥 [相互冷却発動] 自ノード過熱中 ({hw_pre.power_ema:.1f}W)。"
                    f"ピアノードへ代理中継 (Hop: {current_hops + 1}/{MAX_TRM_HOPS})"
                )
                self.comparator.unregister_stream(injected_req_id)
                return await self._relay_to_peer(body, headers, request)
            else:
                logger.error("🛑 [全域過熱アース接地] 最大ホップ数到達！ 強制マイクロダンピング実行")
                await asyncio.sleep(0.1)

        client_response = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await client_response.prepare(request)

        cutoff_triggered = False
        sse_buffer = b""

        try:
            async with self.session.post(
                f"{self.upstream_url}/v1/chat/completions", data=body, headers=headers
            ) as upstream_resp:
                if upstream_resp.status != 200:
                    err_payload = await upstream_resp.read()
                    await client_response.write(err_payload)
                    return client_response

                async for chunk in upstream_resp.content.iter_any():
                    # SSEトークン分解
                    sse_buffer += chunk
                    while b"\n\n" in sse_buffer:
                        event_block, sse_buffer = sse_buffer.split(b"\n\n", 1)
                        for line in event_block.split(b"\n"):
                            if line.startswith(b"data: "):
                                payload = line[6:].strip()
                                if payload and payload != b"[DONE]":
                                    stream_state.generated_tokens += 1
                                    if stream_state.is_prefill:
                                        stream_state.is_prefill = False
                                        ttft_ms = (time.time() - stream_state.start_time) * 1000.0
                                        logger.info(
                                            f"✨ [TTFT到達] {injected_req_id} Prefill完了 ({ttft_ms:.1f}ms) -> デコード動態監視へ移行"
                                        )

                    # クラスタ物理動態のリアルタイム検定
                    hw = self.harvester.get_sample()
                    eval_res = self.comparator.evaluate_cluster(hw)

                    # 分岐 A: 0-RTT 物理遮断執行
                    if eval_res["action"] == "0-RTT_CUTOFF":
                        target = eval_res["target_req_id"]
                        if target is None or target == injected_req_id:
                            cutoff_triggered = True
                            logger.error(
                                f"🚨 [0-RTT 物理遮断執行] {eval_res['reason']} | 標的: {injected_req_id}"
                            )

                            # 事前注入IDでバックエンドCUDAカーネルを即死中絶
                            asyncio.create_task(self._trigger_backend_abort(injected_req_id))

                            # クライアントへ拒絶通知
                            await client_response.write(
                                b"\n\ndata: [TRM_SECURITY_VETO: Hardware Capacity Limit or Gross Spoofing Aborted]\n\n"
                            )
                            break

                    # 分岐 B: 進行中セッションのマイクロ冷却ダンピング
                    elif eval_res["action"] == "THERMAL_OVERHEAT":
                        await asyncio.sleep(0.01)

                    await client_response.write(chunk)

        except asyncio.CancelledError:
            # クライアント離脱時もゾンビカーネルを許さず即時中絶
            asyncio.create_task(self._trigger_backend_abort(injected_req_id))
        except Exception as e:
            logger.error(f"中継パイプライン例外: {e}")
        finally:
            self.comparator.unregister_stream(injected_req_id)
            if cutoff_triggered:
                try:
                    if not client_response.is_eof():
                        await client_response.write_eof()
                    trans = request.transport
                    if trans and not trans.is_closing():
                        trans.close()
                except Exception:
                    pass

        return client_response

    async def _relay_to_peer(self, body: bytes, headers: dict, request: web.Request) -> web.StreamResponse:
        """過熱時のピアノード代理中継 (相互冷却)"""
        client_response = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await client_response.prepare(request)
        try:
            async with self.session.post(
                f"{self.spillover_peer_url}/v1/chat/completions",
                data=body,
                headers=headers,
                timeout=ClientTimeout(total=300),
            ) as peer_resp:
                async for chunk in peer_resp.content.iter_any():
                    await client_response.write(chunk)
            logger.info("🌟 [相互冷却完了] ピアノードによる代理推論が完走しました。")
        except Exception as e:
            logger.error(f"ピア中継失敗: {e}")
            await client_response.write(b"\n\ndata: [TRM_PEER_RELAY_ERROR]\n\n")
        finally:
            if not client_response.is_eof():
                await client_response.write_eof()
        return client_response

    async def _trigger_backend_abort(self, req_id: str):
        """vLLM /abort 直撃 (事前注入IDによる即時窒息)"""
        try:
            async with self.session.post(
                f"{self.upstream_url}/abort", json={"request_id": req_id}, timeout=0.15
            ) as r:
                logger.info(f"⚡ [vLLM Abort執行完了] Request ID [{req_id}] のGPUカーネルを完全中絶。")
        except Exception as e:
            logger.debug(f"/abort 中絶通信ログ: {e}")


def create_app():
    server = TRMEcoGuardProxyServer()
    server.app.on_startup.append(lambda app: server.start())
    server.app.on_cleanup.append(server.cleanup)
    return server.app


if __name__ == "__main__":
    app = create_app()
    print("=" * 80)
    print(" TRM-EcoGuard Unified Production Proxy (Phase 1-B 完成版) 起動")
    print(f"  ・Upstream Backend : {UPSTREAM_URL}")
    print(f"  ・Spillover Peer   : {SPILLOVER_PEER_URL}")
    print(f"  ・Listening Port   : {PROXY_PORT}")
    print(f"  ・Prometheus Gauge : http://0.0.0.0:{PROXY_PORT}/metrics")
    print("=" * 80)
    web.run_app(app, port=PROXY_PORT)
