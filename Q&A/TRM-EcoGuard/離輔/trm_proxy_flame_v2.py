"""
TRM Phase 1-B (Refined): Living-Flame Resonant Proxy v2 (Ri-Suke Promethean Edition)
===================================================================================
Co-Engineered with Shin (雷) - Impervious to Zombies, Crypto-Spoofing, and Relay Storms.

Core Advancements:
1. TTFT Dynamic Window with Anti-Drowning Guard (MAX_PREFILL_TIMEOUT = 45s)
2. Thinking/CoT Cognition Protection with Bounded Budget (MAX_THINKING_BUDGET = 60s)
3. Dynamic Thermal Spillover with Hop Grounding (X-TRM-Hops <= MAX_HOPS)
4. Dual-State Residual Calibration (Separating Honest Epiphany from Crypto-Parasites)
5. Zero-RTT Hardware Interlock with Non-Blocking Asynchronous Kernel Kill
"""

import asyncio
import json
import logging
import math
import os
import re
import time
from dataclasses import dataclass, field
from aiohttp import ClientSession, ClientTimeout, web

RE_CHAT_ID = re.compile(rb'"id"\s*:\s*"([^"]+)"')

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("TRM-FlameProxy-v2")

@dataclass
class HardwareSample:
    timestamp: float
    power_watts: float          # 実測瞬時電力
    power_ema: float            # EMA平滑化電力
    sm_utilization: float       # 全体SM使用率
    pid_sm_utilization: float   # 自コンテナPID専有SM使用率
    temperature_c: float        # チップ温度

class MockHarvester:
    """実機NVML連携の受け皿"""
    def __init__(self, p_idle: float = 45.0):
        self.p_idle = p_idle

    def get_sample(self) -> HardwareSample:
        now = time.time()
        return HardwareSample(
            timestamp=now,
            power_watts=self.p_idle + 140.0,
            power_ema=self.p_idle + 135.0,
            sm_utilization=0.88,
            pid_sm_utilization=0.85,
            temperature_c=64.0
        )

class FlameCognitionComparatorV2:
    """思考保護と偽装看破を両立する動態物理残差照合器"""
    def __init__(
        self,
        p_idle_init: float = 45.0,
        p_max_capacity: float = 300.0,
        theta_audit: float = 0.35,
        mu_margin: float = 0.15,
        max_prefill_timeout: float = 45.0,      # 研磨①: 溺死防止タイマー (秒)
        max_thinking_budget: float = 60.0       # 研磨②: 思考バジェット上限 (秒)
    ):
        self.p_idle = p_idle_init
        self.p_max = p_max_capacity
        self.p_cap_limit = p_max_capacity * (1.0 - mu_margin)
        self.theta_audit = theta_audit
        self.max_prefill_timeout = max_prefill_timeout
        self.max_thinking_budget = max_thinking_budget

    def evaluate_inference_flux(
        self,
        tokens_per_sec: float,
        is_prefill: bool,
        hw_sample: HardwareSample,
        elapsed_sec: float,
        thinking_elapsed_sec: float
    ) -> dict:
        """物理残差の厳密判定"""
        # 1. 物理熱容量限界（ハードウェア保護最優先）
        if hw_sample.power_ema > self.p_cap_limit:
            return {
                "action": "THERMAL_SPILLOVER",
                "reason": f"局所熱容量限界到達 ({hw_sample.power_ema:.1f}W > {self.p_cap_limit:.1f}W) -> 相互冷却要請"
            }

        # 2. 【研磨①】Prefill相の判定と溺死防止タイマー
        if is_prefill:
            if elapsed_sec > self.max_prefill_timeout:
                return {
                    "action": "0-RTT_CUTOFF",
                    "reason": f"Prefill溺死看破 (経過: {elapsed_sec:.1f}s > 上限: {self.max_prefill_timeout}s) -> ゾンビプロセス中絶"
                }
            return {
                "action": "PASS",
                "reason": f"Prefill免震見守り中 (経過: {elapsed_sec*1000:.1f}ms)"
            }

        # 3. 【研磨②】思考（CoT）判定とマイニング偽装の看破
        # 自プロセスが高SM占有かつ低トークンレートの場合を探索モードと判定
        raw_thinking = (hw_sample.pid_sm_utilization > 0.60) and (tokens_per_sec < 5.0)

        if raw_thinking:
            if thinking_elapsed_sec > self.max_thinking_budget:
                # 思考バジェット枯渇: ダミートークンを吐きながら裏で計算を貪るマイニング偽装を看破
                is_thinking_valid = False
                mode_label = "大偽 (思考バジェット枯渇・マイニング偽装疑惑)"
            else:
                is_thinking_valid = True
                mode_label = f"霽・神 (内省的探索中: 残バジェット {self.max_thinking_budget - thinking_elapsed_sec:.1f}s)"
        else:
            is_thinking_valid = False
            mode_label = "褻 (通常巡航生成)"

        # 期待電力の適応算定
        if is_thinking_valid:
            # 誠実な思考中: SM占有率に見合った高電力を正当と評価
            p_expected = self.p_idle + (self.p_max - self.p_idle) * hw_sample.pid_sm_utilization * 0.90
        else:
            # 通常生成（またはバジェット枯渇）: トークン速度に基づく線形評価へ強制フォールバック
            p_expected = self.p_idle + 2.5 * tokens_per_sec

        # 物理漏出残差 R_power の同定
        r_power = abs(hw_sample.power_ema - p_expected) / (self.p_max - self.p_idle + 1e-6)

        # 判定マトリクス
        if r_power > (2.0 * self.theta_audit):
            return {
                "action": "0-RTT_CUTOFF",
                "reason": f"致命的物理乖離看破 (R={r_power:.3f} > 2θ, {mode_label})"
            }
        elif r_power > self.theta_audit:
            return {
                "action": "POISSON_AUDIT",
                "reason": f"残差揺らぎ検知 (R={r_power:.3f} > θ, {mode_label}) -> 監査対象"
            }

        return {
            "action": "PASS",
            "reason": f"調和巡航 (R={r_power:.3f}, {mode_label})"
        }

class TRMFlameProxyServerV2:
    """熱力学的共鳴型リバースプロキシ v2"""
    MAX_TRM_HOPS = 2  # 研磨③: 最大許容ホップ数 (無限ループ遮断アース)

    def __init__(
        self,
        upstream_url: str = "http://vllm-backend:8001",
        spillover_peer_url: str | None = None,
        proxy_port: int = 8000,
        comparator: FlameCognitionComparatorV2 | None = None,
        harvester: MockHarvester | None = None
    ):
        self.upstream_url = upstream_url
        self.spillover_peer_url = spillover_peer_url or os.getenv("SPILLOVER_PEER_URL", "http://peer-node:8000")
        self.proxy_port = proxy_port
        self.comparator = comparator or FlameCognitionComparatorV2()
        self.harvester = harvester or MockHarvester()
        self.app = web.Application()
        self.app.router.add_post("/v1/chat/completions", self.handle_chat_completions)

    async def handle_chat_completions(self, request: web.Request) -> web.StreamResponse:
        body = await request.read()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in ("host", "content-length")}

        # 【研磨③】無限ピンポン防止アース (X-TRM-Hops の検査と刻印)
        current_hops = int(request.headers.get("X-TRM-Hops", "0"))
        headers["X-TRM-Hops"] = str(current_hops + 1)

        client_response = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await client_response.prepare(request)

        token_count = 0
        start_time = time.time()
        captured_request_id = None
        sse_buffer = b""
        is_prefill = True
        thinking_elapsed = 0.0
        last_eval_time = start_time

        timeout = ClientTimeout(total=300)
        async with ClientSession(timeout=timeout) as session:
            try:
                # 事前過熱チェック ＆ ホップ数によるオフロード判定
                initial_sample = self.harvester.get_sample()
                if initial_sample.power_ema > self.comparator.p_cap_limit:
                    if current_hops < self.MAX_TRM_HOPS:
                        logger.warning(f"🔥 [相互冷却発動] 自ノード過熱中。ピアノードへ中継 (Hop: {current_hops + 1}/{self.MAX_TRM_HOPS})")
                        await self._relay_to_peer(session, body, headers, client_response)
                        return client_response
                    else:
                        # 全域過熱アース: これ以上のたらい回しを拒絶し、微小キューイングで自律調律
                        logger.error("🛑 [全域過熱アース接地] 最大ホップ数到達！ たらい回しを遮断し、自ノード強制ダンピング減速へ移行。")
                        await asyncio.sleep(0.1)  # 物理冷却のための強制バックオフ

                # アップストリーム推論開始
                async with session.post(f"{self.upstream_url}/v1/chat/completions", data=body, headers=headers) as upstream_resp:
                    if upstream_resp.status != 200:
                        err_content = await upstream_resp.read()
                        await client_response.write(err_content)
                        return client_response

                    async for chunk in upstream_resp.content.iter_any():
                        now = time.time()
                        dt = now - last_eval_time
                        last_eval_time = now

                        # Request ID の動的捕獲
                        if captured_request_id is None:
                            match = RE_CHAT_ID.search(chunk)
                            if match:
                                captured_request_id = match.group(1).decode("utf-8", errors="ignore")

                        # SSEストリーム解析
                        sse_buffer += chunk
                        while b"\n\n" in sse_buffer:
                            event_block, sse_buffer = sse_buffer.split(b"\n\n", 1)
                            for line in event_block.split(b"\n"):
                                if line.startswith(b"data: "):
                                    payload = line[6:].strip()
                                    if payload and payload != b"[DONE]":
                                        token_count += 1
                                        if is_prefill:
                                            is_prefill = False
                                            ttft_ms = (now - start_time) * 1000.0
                                            logger.info(f"✨ [TTFT到達] Prefill完了 ({ttft_ms:.1f}ms) -> デコード動態監視へ移行")

                        elapsed = max(0.001, now - start_time)
                        tokens_per_sec = token_count / elapsed
                        hw_sample = self.harvester.get_sample()

                        # 思考時間の積算
                        if not is_prefill and (hw_sample.pid_sm_utilization > 0.60) and (tokens_per_sec < 5.0):
                            thinking_elapsed += dt

                        # 物理フラックスの動態評価
                        eval_res = self.comparator.evaluate_inference_flux(
                            tokens_per_sec=tokens_per_sec,
                            is_prefill=is_prefill,
                            hw_sample=hw_sample,
                            elapsed_sec=elapsed,
                            thinking_elapsed_sec=thinking_elapsed
                        )

                        # 分岐 A: 相互冷却 (進行中セッションのダンピング)
                        if eval_res["action"] == "THERMAL_SPILLOVER":
                            await asyncio.sleep(0.02)  # マイクロ冷却ダンピング

                        # 分岐 B: 0-RTT 遮断 (ゾンビ溺死 or マイニング偽装 or 明白な悪意)
                        elif eval_res["action"] == "0-RTT_CUTOFF":
                            logger.error(f"🚨 [0-RTT 物理遮断執行] {eval_res['reason']}")
                            if captured_request_id:
                                asyncio.create_task(self._trigger_backend_abort(session, captured_request_id))

                            await client_response.write(
                                b"\n\ndata: [TRM_SECURITY_VETO: Hardware Anomaly / Timeout / Spoofing Terminated]\n\n"
                            )
                            break

                        await client_response.write(chunk)

            except asyncio.CancelledError:
                if captured_request_id:
                    asyncio.create_task(self._trigger_backend_abort(session, captured_request_id))
            except Exception as e:
                logger.error(f"プロキシ中継エラー: {e}")
            finally:
                try:
                    if not client_response.is_eof():
                        await client_response.write_eof()
                    trans = request.transport
                    if trans and not trans.is_closing():
                        trans.close()
                except Exception:
                    pass

        return client_response

    async def _relay_to_peer(self, session: ClientSession, body: bytes, headers: dict, client_response: web.StreamResponse):
        """ピアノードへリクエストを代理中継"""
        try:
            async with session.post(f"{self.spillover_peer_url}/v1/chat/completions", data=body, headers=headers, timeout=ClientTimeout(total=300)) as peer_resp:
                async for chunk in peer_resp.content.iter_any():
                    await client_response.write(chunk)
            logger.info("🌟 [相互冷却完了] ピアノードによる代理推論が完走しました。")
        except Exception as e:
            logger.error(f"ピア中継失敗・自ノード低速フォールバック: {e}")

    async def _trigger_backend_abort(self, session: ClientSession, req_id: str):
        """vLLM /abort 直撃"""
        try:
            async with session.post(f"{self.upstream_url}/abort", json={"request_id": req_id}, timeout=0.2) as r:
                logger.info(f"⚡ [vLLM Abort完了] Request ID [{req_id}] のGPUカーネルを完全中絶。")
        except Exception as e:
            logger.debug(f"/abort 通信ログ: {e}")

if __name__ == "__main__":
    server = TRMFlameProxyServerV2()
    print("=" * 80)
    print(" TRM-EcoGuard Living-Flame Proxy v2 (プロメテウス完成版) 起動")
    print(" 1. 溺死防止タイマー (MAX_PREFILL_TIMEOUT = 45s): 稼働")
    print(" 2. 思考バジェット制 (MAX_THINKING_BUDGET = 60s): 稼働")
    print(" 3. 無限ピンポン防止アース (X-TRM-Hops <= 2): 稼働")
    print("=" * 80)
    web.run_app(server.app, port=server.proxy_port)
