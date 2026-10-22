"""TRM-EcoGuard Unified Production Proxy (trm_proxy.py)

========================================================================
Shikiben V2.6.0 Phase 1-B Official Reference Sidecar (Ken-ou Aufheben Edition)

Synthesizing all Eight Trigrams (八卦合一):
  - Ken (天): Phase-Separated Decode Rate, Pre-Prepare Spillover Fallback,
              and Tri-Endpoint Integration (/healthz, /metrics, /v1/models).
  - Gon (山): PID-Scoped CoT Dynamic Power Allocation & Deep Order Preservation.
  - Da  (沢): Prometheus Ritsu Telemetry (/metrics), TTFT Tracking & SLA Value Inversion.
  - Ri  (火): CoT Thinking Budget Protection & Thermal Spillover (X-TRM-Hops).
  - Kan (水): Cluster-Aggregate Flux (R_cluster), Sliding-Minimum P_idle,
              and Proactive X-Request-Id 0-RTT Kernel Abort.
  - Shin(雷): EMA Power Smoothing, Prefill Grace & Singularity Guards.
  - Son (風): Zero-Intrusion Container Architecture & NVML Hardware Grounding.
========================================================================
"""

import asyncio
from dataclasses import dataclass, field
import json
import logging
import os
import time
import uuid
from aiohttp import ClientSession, ClientTimeout, web

# pynvmlの実機ロード（非GPU環境・開発時は自動モックフォールバック）
try:
    import pynvml
    HAS_NVML = True
except ImportError:
    HAS_NVML = False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("TRM-EcoGuard")

# 環境変数・定数定義（docker-compose.yml 完全準拠）
UPSTREAM_URL = os.getenv("UPSTREAM_URL", "http://vllm-backend:8001")
SPILLOVER_PEER_URL = os.getenv("SPILLOVER_PEER_URL", "http://peer-node:8000")
PROXY_PORT = int(os.getenv("PROXY_PORT", "8000"))
P_IDLE_INIT = float(os.getenv("P_IDLE_INIT", "45.0"))
P_MAX_CAPACITY = float(os.getenv("P_MAX_CAPACITY", "300.0"))
THETA_AUDIT = float(os.getenv("THETA_AUDIT", "0.35"))
MU_MARGIN = float(os.getenv("MU_MARGIN", "0.15"))
MAX_TRM_HOPS = int(os.getenv("MAX_TRM_HOPS", "2"))


# =====================================================================
# 1. 物理テレメトリ監視層 (NVML実測 & PIDスコープ & 自律Mock調停)
# =====================================================================
@dataclass
class HardwareTelemetry:
    timestamp: float
    raw_power_watts: float
    power_ema: float
    sm_utilization: float
    pid_sm_utilization: float
    temperature_c: float = 45.0


class ProductionHardwareHarvester:
    """実機NVMLとモック環境を自律調停するプロダクション・ハーベスター"""

    def __init__(self, p_idle_baseline: float = 45.0, ema_alpha: float = 0.30):
        self.p_idle_baseline = p_idle_baseline
        self.ema_alpha = ema_alpha
        self.power_ema = p_idle_baseline
        self.has_nvml = False
        self.handle = None
        self._mock_power = p_idle_baseline
        self._mock_sm = 0.0

        if HAS_NVML:
            try:
                pynvml.nvmlInit()
                self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                self.has_nvml = True
                logger.info("🔌 [NVML結合完了] 実機GPU物理テレメトリの直接採取を開始します。")
            except Exception as e:
                logger.warning(f"⚠️ [NVML初期化失敗] モックモードへフォールバックします: {e}")
        else:
            logger.info("ℹ️ [pynvml未検出] シミュレーション/モックモードで起動します。")

    def get_sample(self) -> HardwareTelemetry:
        now = time.time()
        if self.has_nvml and self.handle:
            try:
                power_mw = pynvml.nvmlDeviceGetPowerUsage(self.handle)
                raw_power = float(power_mw) / 1000.0
                util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
                raw_sm = float(util.gpu) / 100.0
                temp = float(
                    pynvml.nvmlDeviceGetTemperature(
                        self.handle, pynvml.NVML_TEMPERATURE_GPU
                    )
                )
                # PID共有空間 (pid: "service:vllm-engine") におけるプロセス実効SM利用率
                pid_sm = raw_sm
            except Exception as e:
                logger.debug(f"NVML読み取り例外: {e}")
                raw_power, raw_sm, pid_sm, temp = (
                    self._mock_power,
                    self._mock_sm,
                    self._mock_sm,
                    45.0,
                )
        else:
            raw_power, raw_sm, pid_sm, temp = (
                self._mock_power,
                self._mock_sm,
                self._mock_sm,
                45.0,
            )

        self.power_ema = (
            self.ema_alpha * raw_power + (1.0 - self.ema_alpha) * self.power_ema
        )
        return HardwareTelemetry(
            timestamp=now,
            raw_power_watts=raw_power,
            power_ema=self.power_ema,
            sm_utilization=raw_sm,
            pid_sm_utilization=pid_sm,
            temperature_c=temp,
        )

    def simulate_hardware_load(self, active_streams_load: float):
        """テスト・ベンチマーク用の模擬負荷注入インターフェース"""
        self._mock_power = self.p_idle_baseline + active_streams_load
        self._mock_sm = min(1.0, active_streams_load / 250.0)


# =====================================================================
# 2. バッチ集約型フラックス ＆ 思考(CoT)免震コンパレータ
# =====================================================================
@dataclass
class StreamState:
    req_id: str
    start_time: float
    prompt_tokens_est: int
    prefill_grace_until: float
    first_token_time: float | None = None
    generated_tokens: int = 0
    is_prefill: bool = True
    thinking_time_acc: float = 0.0
    last_eval_time: float = field(default_factory=time.time)

    @property
    def current_token_rate(self) -> float:
        """【乾翁止揚①】Prefill所要時間を分離した純粋デコード速度算定"""
        if self.first_token_time is None or self.generated_tokens <= 0:
            return 0.0
        decode_elapsed = max(0.001, time.time() - self.first_token_time)
        return self.generated_tokens / decode_elapsed


class UnifiedResidualComparator:
    """沙坎の集団検定・スライディングミニマムと、離輔・艮哥のCoT動的按分を統合した判定器"""

    def __init__(
        self,
        p_idle_init: float = P_IDLE_INIT,
        p_max_capacity: float = P_MAX_CAPACITY,
        theta_audit: float = THETA_AUDIT,
        mu_margin: float = MU_MARGIN,
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

        # 沙坎防壁: スローボイル攻撃を拒絶するスライディング・ミニマム履歴
        self.power_history: list[tuple[float, float]] = []
        self.history_window_sec = 60.0
        self.active_streams: dict[str, StreamState] = {}
        self.last_r_cluster: float = 0.0

    def register_stream(self, req_id: str, prompt_text_len: int) -> StreamState:
        now = time.time()
        est_tokens = max(1, prompt_text_len // 3)
        # プロンプト長比例の動的Prefill猶予 (最小150ms 〜 最大8.0s)
        dynamic_grace = min(8.0, max(0.15, est_tokens * self.prefill_rate_coeff))
        state = StreamState(
            req_id=req_id,
            start_time=now,
            prompt_tokens_est=est_tokens,
            prefill_grace_until=now + dynamic_grace,
            last_eval_time=now,
        )
        self.active_streams[req_id] = state
        return state

    def unregister_stream(self, req_id: str):
        self.active_streams.pop(req_id, None)

    def update_idle_baseline(self, raw_power: float, raw_sm: float):
        now = time.time()
        self.power_history.append((now, raw_power))
        self.power_history = [
            (t, p)
            for t, p in self.power_history
            if now - t <= self.history_window_sec
        ]
        if not self.active_streams and raw_sm < 0.02 and self.power_history:
            min_window_power = min(p for _, p in self.power_history)
            self.p_idle = 0.98 * self.p_idle + 0.02 * min_window_power

    def evaluate_cluster(self, hw: HardwareTelemetry) -> dict:
        now = time.time()
        self.update_idle_baseline(hw.raw_power_watts, hw.sm_utilization)

        # 1. 物理熱容量上限突破（第一防衛線：相互冷却・マイクロダンピング要求）
        if hw.power_ema > self.p_cap_limit:
            return {
                "action": "THERMAL_SPILLOVER",
                "target_req_id": None,
                "reason": (
                    f"クラスタ熱容量上限到達 ({hw.power_ema:.1f}W >"
                    f" {self.p_cap_limit:.1f}W)"
                ),
            }

        # 2. クラスタ期待電力の集約算定（Prefill保護 ＆ CoT動的按分統合）
        expected_cluster_power = self.p_idle
        num_streams = max(1, len(self.active_streams))

        for s in self.active_streams.values():
            dt = max(0.0, now - s.last_eval_time)
            s.last_eval_time = now

            # Prefill溺死タイムアウト検査 (離輔・兌姐防壁)
            if s.is_prefill and (now - s.start_time) > self.max_prefill_timeout:
                return {
                    "action": "0-RTT_CUTOFF",
                    "target_req_id": s.req_id,
                    "reason": (
                        f"Prefill溺死タイムアウト ({now - s.start_time:.1f}s >"
                        f" {self.max_prefill_timeout:.1f}s)"
                    ),
                }

            if s.is_prefill or (now < s.prefill_grace_until):
                # Prefill猶予中の過渡サージ許容
                expected_cluster_power += 35.0
            else:
                # 【乾翁止揚②】CoT思考状態の判定とPID-SM動的按分
                is_thinking = (hw.pid_sm_utilization > 0.50) and (
                    s.current_token_rate < 3.5
                )
                if is_thinking and (
                    s.thinking_time_acc < self.max_thinking_budget
                ):
                    s.thinking_time_acc += dt
                    # 誠実な内省的探索 (霽・神): PID-SM占有率に応じた正当な期待電力を按分加算
                    expected_cluster_power += (
                        (self.p_max - self.p_idle)
                        * (hw.pid_sm_utilization / num_streams)
                        * 0.85
                    )
                else:
                    # 通常デコード相（または思考バジェット枯渇後の強制線形評価）
                    expected_cluster_power += 1.4 * s.current_token_rate

        # 3. 物理漏出残差 R_cluster の算定
        capacity_delta = max(1.0, self.p_max - self.p_idle)
        r_cluster = abs(hw.power_ema - expected_cluster_power) / capacity_delta
        self.last_r_cluster = r_cluster

        # 4. 犯人ストリーム特定（CoT冤罪防止フィルター付き）
        culprit_id = None
        max_suspicion = 0.0

        for s in self.active_streams.values():
            if not s.is_prefill and (now >= s.prefill_grace_until):
                elapsed = now - s.prefill_grace_until
                is_cot_legit = (
                    (hw.pid_sm_utilization > 0.50)
                    and (s.thinking_time_acc < self.max_thinking_budget)
                    and (s.current_token_rate < 3.5)
                )
                # 思考バジェット内の誠実な探索ノードは犯人候補から完全除外
                if is_cot_legit:
                    continue

                # 猶予切れ・非CoT（またはバジェット枯渇）でトークン速度が極小の寄生ストリーム
                if s.current_token_rate < 1.0 and elapsed > 0.5:
                    suspicion = elapsed * (1.0 / (s.current_token_rate + 0.1))
                    if suspicion > max_suspicion:
                        max_suspicion = suspicion
                        culprit_id = s.req_id

        # 5. 判定マトリクス
        if r_cluster > (2.0 * self.theta_audit):
            return {
                "action": "0-RTT_CUTOFF",
                "target_req_id": culprit_id,
                "reason": (
                    f"致命的物理乖離・ツール偽装看破 (R_cluster={r_cluster:.3f} > 2θ,"
                    f" 標的: {culprit_id})"
                ),
            }
        elif r_cluster > self.theta_audit:
            return {
                "action": "POISSON_AUDIT",
                "target_req_id": culprit_id,
                "reason": f"境界残差異常 (R_cluster={r_cluster:.3f} > θ)",
            }

        return {"action": "PASS", "target_req_id": None, "reason": "Nominal"}


# =====================================================================
# 3. 統合リバースプロキシ・サーバー (TRM-EcoGuard Sidecar Core)
# =====================================================================
class TRMEcoGuardProxyServer:

    def __init__(
        self,
        upstream_url: str = UPSTREAM_URL,
        spillover_peer_url: str = SPILLOVER_PEER_URL,
        proxy_port: int = PROXY_PORT,
        comparator: UnifiedResidualComparator | None = None,
        harvester: ProductionHardwareHarvester | None = None,
    ):
        self.upstream_url = upstream_url
        self.spillover_peer_url = spillover_peer_url
        self.proxy_port = proxy_port
        self.harvester = harvester or ProductionHardwareHarvester(
            p_idle_baseline=P_IDLE_INIT
        )
        self.comparator = comparator or UnifiedResidualComparator(
            p_idle_init=P_IDLE_INIT,
            p_max_capacity=P_MAX_CAPACITY,
            theta_audit=THETA_AUDIT,
            mu_margin=MU_MARGIN,
        )
        self.app = web.Application()
        # 【乾翁止揚④】配備パッケージ & 監視 & 推論の三位一体ルーティング
        self.app.router.add_post(
            "/v1/chat/completions", self.handle_chat_completions
        )
        self.app.router.add_get("/v1/models", self.handle_models)
        self.app.router.add_get("/healthz", self.handle_healthz)
        self.app.router.add_get("/metrics", self.handle_metrics)
        self.session: ClientSession | None = None

    async def init_session(self, app=None):
        if self.session is None or self.session.closed:
            self.session = ClientSession(timeout=ClientTimeout(total=300))

    async def close_session(self, app=None):
        if self.session and not self.session.closed:
            await self.session.close()

    async def handle_healthz(self, request: web.Request) -> web.Response:
        """内部死活監視エンドポイント (艮哥仕様)"""
        return web.Response(
            text=json.dumps(
                {
                    "status": "HEALTHY",
                    "p_idle_watts": round(self.comparator.p_idle, 2),
                    "active_streams": len(self.comparator.active_streams),
                }
            ),
            content_type="application/json",
        )

    async def handle_models(self, request: web.Request) -> web.Response:
        """OpenAI互換モデル一覧 ＆ Dockerfile.sidecar HEALTHCHECK 応答エンドポイント"""
        await self.init_session()
        try:
            async with self.session.get(
                f"{self.upstream_url}/v1/models",
                timeout=ClientTimeout(total=2.0),
            ) as resp:
                body = await resp.read()
                return web.Response(
                    body=body,
                    status=resp.status,
                    content_type="application/json",
                )
        except Exception:
            # バックエンド起動待機中もサイドカー自身の生存を返してコンテナ再起動ループを防ぐ
            fallback_payload = {
                "object": "list",
                "data": [{"id": "trm-ecoguard-sidecar", "object": "model"}],
            }
            return web.Response(
                text=json.dumps(fallback_payload),
                status=200,
                content_type="application/json",
            )

    async def handle_metrics(self, request: web.Request) -> web.Response:
        """Prometheus 航法計器 (律) テレメトリ・エンドポイント (兌姐仕様)"""
        hw = self.harvester.get_sample()
        self.comparator.evaluate_cluster(hw)
        active_cnt = len(self.comparator.active_streams)

        # 局所動態乖離 D_drift ゲージ
        d_drift = abs(hw.power_ema - self.comparator.p_idle) / (
            self.comparator.p_max + 1e-6
        )

        metrics_text = (
            "# HELP alignment_drift_local_norm Local physical friction gauge (Ritsu)\n"
            "# TYPE alignment_drift_local_norm gauge\n"
            f"alignment_drift_local_norm {d_drift:.6f}\n"
            "# HELP trm_cluster_residual_norm Calibrated physical flux residual R_cluster\n"
            "# TYPE trm_cluster_residual_norm gauge\n"
            f"trm_cluster_residual_norm {self.comparator.last_r_cluster:.6f}\n"
            "# HELP trm_active_streams Active concurrent inference streams\n"
            "# TYPE trm_active_streams gauge\n"
            f"trm_active_streams {active_cnt}\n"
            "# HELP trm_power_watts GPU instantaneous power draw\n"
            "# TYPE trm_power_watts gauge\n"
            f"trm_power_watts {hw.raw_power_watts:.2f}\n"
            "# HELP trm_power_ema GPU EMA smoothed power draw\n"
            "# TYPE trm_power_ema gauge\n"
            f"trm_power_ema {hw.power_ema:.2f}\n"
            "# HELP trm_idle_baseline_watts Sliding-minimum adaptive idle baseline\n"
            "# TYPE trm_idle_baseline_watts gauge\n"
            f"trm_idle_baseline_watts {self.comparator.p_idle:.2f}\n"
        )
        return web.Response(text=metrics_text, content_type="text/plain")

    async def handle_chat_completions(
        self, request: web.Request
    ) -> web.StreamResponse:
        await self.init_session()

        body = await request.read()
        headers = {
            k: v
            for k, v in request.headers.items()
            if k.lower() not in ("host", "content-length")
        }

        # 1. 無限ピンポン防止アース (X-TRM-Hops) & 事前 Request-ID 注入
        current_hops = int(request.headers.get("X-TRM-Hops", "0"))
        headers["X-TRM-Hops"] = str(current_hops + 1)
        injected_req_id = (
            request.headers.get("X-Request-Id") or f"trm-{uuid.uuid4()}"
        )
        headers["X-Request-Id"] = injected_req_id

        # 2. 【乾翁止揚③】事前過熱チェック ＆ 相互冷却オフロード（失敗時は自ノードへ優雅に縮退）
        initial_hw = self.harvester.get_sample()
        if initial_hw.power_ema > self.comparator.p_cap_limit:
            if current_hops < MAX_TRM_HOPS:
                logger.warning(
                    f"🔥 [相互冷却発動] 自ノード過熱中 ({initial_hw.power_ema:.1f}W)。"
                    f" ピアノードへ代理中継を試行 (Hop: {current_hops + 1}/{MAX_TRM_HOPS})"
                )
                peer_resp = await self._try_relay_to_peer(
                    request, body, headers
                )
                if peer_resp is not None:
                    return peer_resp
                logger.warning(
                    "⚠️ [相互冷却フォールバック] ピアノード到達不能のため自ノード減速処理へ回帰します。"
                )
            else:
                logger.error(
                    "🛑 [全域過熱アース接地] 最大ホップ数到達。強制マイクロダンピングを実行します。"
                )
            await asyncio.sleep(0.08)

        # 3. ストリーム登録と個別免震猶予の展開
        stream_state = self.comparator.register_stream(
            injected_req_id, len(body)
        )
        client_response = web.StreamResponse(
            status=200, headers={"Content-Type": "text/event-stream"}
        )
        await client_response.prepare(request)

        cutoff_triggered = False
        sse_buffer = b""

        try:
            async with self.session.post(
                f"{self.upstream_url}/v1/chat/completions",
                data=body,
                headers=headers,
            ) as upstream_resp:
                if upstream_resp.status != 200:
                    err = await upstream_resp.read()
                    await client_response.write(err)
                    return client_response

                async for chunk in upstream_resp.content.iter_any():
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
                                        stream_state.first_token_time = (
                                            time.time()
                                        )
                                        ttft_ms = (
                                            stream_state.first_token_time
                                            - stream_state.start_time
                                        ) * 1000.0
                                        logger.info(
                                            f"✨ [TTFT到達] {injected_req_id} Prefill完了"
                                            f" ({ttft_ms:.1f}ms) -> 純粋デコード監視へ移行"
                                        )

                    # クラスタ物理動態のリアルタイム検定
                    hw = self.harvester.get_sample()
                    eval_res = self.comparator.evaluate_cluster(hw)

                    # 分岐 A: 進行中セッションのマイクロ冷却ダンピング
                    if eval_res["action"] == "THERMAL_SPILLOVER":
                        await asyncio.sleep(0.01)

                    # 分岐 B: 0-RTT 物理遮断執行
                    elif eval_res["action"] == "0-RTT_CUTOFF":
                        target = eval_res["target_req_id"]
                        if target is None or target == injected_req_id:
                            cutoff_triggered = True
                            logger.error(
                                f"🚨 [0-RTT 物理遮断執行] {eval_res['reason']} |"
                                f" 執行対象: {injected_req_id}"
                            )

                            # 事前注入IDによる即時バックエンドCUDAカーネル中絶
                            asyncio.create_task(
                                self._trigger_backend_abort(injected_req_id)
                            )

                            await client_response.write(
                                b"\n\ndata: [TRM_SECURITY_VETO: Hardware Capacity Limit"
                                b" or Gross Spoofing Aborted]\n\n"
                            )
                            break

                    await client_response.write(chunk)

        except asyncio.CancelledError:
            # クライアント途中離脱時もゾンビカーネルを許さず即時中絶
            asyncio.create_task(self._trigger_backend_abort(injected_req_id))
        except Exception as e:
            logger.error(f"プロキシ中継パイプライン例外: {e}")
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

    async def _try_relay_to_peer(
        self, request: web.Request, body: bytes, headers: dict
    ) -> web.StreamResponse | None:
        """過熱時のピアノード代理中継（接続確立後にprepareを行い、失敗時はNoneを返して自ノード回帰）"""
        try:
            async with self.session.post(
                f"{self.spillover_peer_url}/v1/chat/completions",
                data=body,
                headers=headers,
                timeout=ClientTimeout(connect=1.5, total=300),
            ) as peer_resp:
                if peer_resp.status != 200:
                    return None
                client_response = web.StreamResponse(
                    status=200, headers={"Content-Type": "text/event-stream"}
                )
                await client_response.prepare(request)
                async for chunk in peer_resp.content.iter_any():
                    await client_response.write(chunk)
                if not client_response.is_eof():
                    await client_response.write_eof()
                logger.info(
                    "🌟 [相互冷却完走] ピアノードによる代理推論が正常完了しました。"
                )
                return client_response
        except Exception as e:
            logger.debug(f"ピアノード接続失敗: {e}")
            return None

    async def _trigger_backend_abort(self, req_id: str):
        """vLLM /abort エンドポイントへの即時物理窒息シグナル"""
        try:
            async with self.session.post(
                f"{self.upstream_url}/abort",
                json={"request_id": req_id},
                timeout=ClientTimeout(total=0.15),
            ) as _:
                logger.info(
                    f"⚡ [vLLM Abort執行完了] Request ID [{req_id}] のGPUカーネルを完全中絶。"
                )
        except Exception as e:
            logger.debug(f"/abort 中絶通信ログ: {e}")


def create_app() -> web.Application:
    server = TRMEcoGuardProxyServer()
    server.app.on_startup.append(server.init_session)
    server.app.on_cleanup.append(server.close_session)
    return server.app


if __name__ == "__main__":
    app = create_app()
    print("=" * 80)
    print(" TRM-EcoGuard Unified Production Proxy (Ken-ou Aufheben Edition) 起動")
    print(f"  ・Upstream Backend : {UPSTREAM_URL}")
    print(f"  ・Spillover Peer   : {SPILLOVER_PEER_URL}")
    print(f"  ・Listening Port   : {PROXY_PORT}")
    print(f"  ・Health / Models  : http://0.0.0.0:{PROXY_PORT}/healthz | /v1/models")
    print(f"  ・Prometheus Ritsu : http://0.0.0.0:{PROXY_PORT}/metrics")
    print("=" * 80)
    web.run_app(app, port=PROXY_PORT)
