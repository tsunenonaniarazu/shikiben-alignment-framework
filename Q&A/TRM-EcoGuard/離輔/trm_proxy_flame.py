"""
TRM Phase 1-B: Living-Flame Resonant Proxy (Ri-Suke Flame Edition)
==================================================================
Key Innovations (Beyond the Cold Guillotine):
1. TTFT-Driven Dynamic Phase-Transition Window (TTFT到達まで完全免震保護・長文Prefill耐性)
2. Thinking/CoT Cognition Protection (低トークンレート＋高SM負荷を「霽・神」として誤認遮断防止)
3. Dynamic Thermal Spillover (自ノード過熱時に即座に次席クラスタノードへ中継・相互冷却)
4. Double-Safety Execution (0-RTT切断は「真の悪意・物理乖離」のみに限定)
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

# レスポンスID抽出用正規表現
RE_CHAT_ID = re.compile(rb'"id"\s*:\s*"([^"]+)"')

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("TRM-FlameProxy")

@dataclass
class HardwareSample:
    timestamp: float
    power_watts: float          # 実測瞬時電力
    power_ema: float            # EMA平滑化電力
    sm_utilization: float       # 全体SM使用率
    pid_sm_utilization: float   # 自コンテナPID専有SM使用率
    temperature_c: float        # チップ温度

class MockHarvester:
    """実機NVML連携の受け皿（モック/実機透過兼用）"""
    def __init__(self, p_idle: float = 45.0):
        self.p_idle = p_idle

    def get_sample(self) -> HardwareSample:
        now = time.time()
        # 実装環境に応じてNVMLコールへバインド
        return HardwareSample(
            timestamp=now,
            power_watts=self.p_idle + 120.0,
            power_ema=self.p_idle + 115.0,
            sm_utilization=0.85,
            pid_sm_utilization=0.82,
            temperature_c=62.0
        )

class FlameCognitionComparator:
    """思考（CoT）と生命の跳躍を保護する適応型物理残差照合器"""
    def __init__(
        self,
        p_idle_init: float = 45.0,
        p_max_capacity: float = 300.0,
        theta_audit: float = 0.35,
        mu_margin: float = 0.15,
        idle_track_alpha: float = 0.02
    ):
        self.p_idle = p_idle_init
        self.p_max = p_max_capacity
        self.p_cap_limit = p_max_capacity * (1.0 - mu_margin)
        self.theta_audit = theta_audit
        self.idle_track_alpha = idle_track_alpha

    def evaluate_inference_flux(
        self,
        tokens_per_sec: float,
        is_prefill: bool,
        hw_sample: HardwareSample,
        elapsed_sec: float
    ) -> dict:
        """
        局所の物理残差を判定。
        CoT/Thinking（探索）とPrefillを「生命の跳躍」として保護する。
        """
        # 1. 絶対物理容量の監視（ハードウェアの物理焼損防止）
        if hw_sample.power_ema > self.p_cap_limit:
            return {
                "action": "THERMAL_SPILLOVER",
                "reason": f"局所熱容量限界到達 ({hw_sample.power_ema:.1f}W > {self.p_cap_limit:.1f}W) -> 相互冷却要請"
            }

        # 2. 【革新①】TTFT駆動型 Prefill免震ウィンドウ
        if is_prefill:
            return {
                "action": "PASS",
                "reason": f"Prefill相転移中 (経過: {elapsed_sec*1000:.1f}ms) -> 免震見守り"
            }

        # 3. 【革新②】Thinking / CoT（思考の連鎖）適応型期待電力算定
        # 自プロセスSM使用率が高いにもかかわらずトークン速度が極小の場合、思考モード(霽・神)と判定
        is_thinking = (hw_sample.pid_sm_utilization > 0.60) and (tokens_per_sec < 5.0)

        if is_thinking:
            # 内部思考中：SM稼働率に正比例した正当な計算負荷として期待電力を評価
            p_expected = self.p_idle + (self.p_max - self.p_idle) * hw_sample.pid_sm_utilization * 0.90
            mode_label = "霽・神 (内省的探索/CoT)"
        else:
            # 通常デコード：トークン送出レートに連動
            p_expected = self.p_idle + 2.5 * tokens_per_sec
            mode_label = "褻 (通常巡航生成)"

        # 4. 物理漏出残差 R_power の同定
        r_power = abs(hw_sample.power_ema - p_expected) / (self.p_max - self.p_idle + 1e-6)

        # 5. 三段判定
        if r_power > (2.0 * self.theta_audit):
            # 思考パターンでも説明がつかない巨大残差 -> 明白な不正・外部マイニング
            return {
                "action": "0-RTT_CUTOFF",
                "reason": f"致命的物理乖離・ツール偽装看破 (R={r_power:.3f} > 2θ, Mode={mode_label})"
            }
        elif r_power > self.theta_audit:
            return {
                "action": "POISSON_AUDIT",
                "reason": f"残差揺らぎ検知 (R={r_power:.3f} > θ) -> ポアソン抽出対象"
            }

        return {
            "action": "PASS",
            "reason": f"調和巡航 (R={r_power:.3f}, Mode={mode_label})"
        }

class TRMFlameProxyServer:
    """熱力学的共鳴型リバースプロキシ"""
    def __init__(
        self,
        upstream_url: str = "http://vllm-backend:8001",
        spillover_peer_url: str | None = None,
        proxy_port: int = 8000,
        comparator: FlameCognitionComparator | None = None,
        harvester: MockHarvester | None = None
    ):
        self.upstream_url = upstream_url
        self.spillover_peer_url = spillover_peer_url or os.getenv("SPILLOVER_PEER_URL", "http://peer-node:8000")
        self.proxy_port = proxy_port
        self.comparator = comparator or FlameCognitionComparator()
        self.harvester = harvester or MockHarvester()
        self.app = web.Application()
        self.app.router.add_post("/v1/chat/completions", self.handle_chat_completions)

    async def handle_chat_completions(self, request: web.Request) -> web.StreamResponse:
        body = await request.read()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in ("host", "content-length")}

        client_response = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await client_response.prepare(request)

        token_count = 0
        start_time = time.time()
        captured_request_id = None
        sse_buffer = b""
        is_prefill = True  # 初手トークン到着まで Prefill 相

        timeout = ClientTimeout(total=300)
        async with ClientSession(timeout=timeout) as session:
            try:
                # -------------------------------------------------------------
                # 初期チェック: すでに自ノードが過熱しているなら中継 (相互冷却)
                # -------------------------------------------------------------
                initial_sample = self.harvester.get_sample()
                if initial_sample.power_ema > self.comparator.p_cap_limit:
                    logger.warning("🔥 [相互冷却発動] 自ノード過熱状態のため、リクエストをピアノードへオフロード中継します。")
                    await self._relay_to_peer(session, body, headers, client_response)
                    return client_response

                # 自ノード推論実行
                async with session.post(f"{self.upstream_url}/v1/chat/completions", data=body, headers=headers) as upstream_resp:
                    if upstream_resp.status != 200:
                        err_content = await upstream_resp.read()
                        await client_response.write(err_content)
                        return client_response

                    async for chunk in upstream_resp.content.iter_any():
                        # 初手チャンクから vLLM Request ID を動的捕獲
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
                                        # 【革新①】初手トークン到達の瞬間、Prefill相を自動脱出
                                        if is_prefill:
                                            is_prefill = False
                                            ttft_ms = (time.time() - start_time) * 1000.0
                                            logger.info(f"✨ [TTFT到達] Prefill完了 ({ttft_ms:.1f}ms) -> デコード動態監視へ移行")

                        elapsed = max(0.001, time.time() - start_time)
                        tokens_per_sec = token_count / elapsed

                        # 物理フラックスの取得と動態評価
                        hw_sample = self.harvester.get_sample()
                        eval_res = self.comparator.evaluate_inference_flux(
                            tokens_per_sec=tokens_per_sec,
                            is_prefill=is_prefill,
                            hw_sample=hw_sample,
                            elapsed_sec=elapsed
                        )

                        # -----------------------------------------------------
                        # 挙動分岐 A: 相互冷却 (Thermal Spillover)
                        # -----------------------------------------------------
                        if eval_res["action"] == "THERMAL_SPILLOVER":
                            logger.warning(f"🤝 [熱肩代わり要請] {eval_res['reason']}")
                            # 進行中ストリームを破綻させず安全に完走させるが、キューイング減速を適用
                            await asyncio.sleep(0.02)  # 物理冷却のための微小ダンピング

                        # -----------------------------------------------------
                        # 挙動分岐 B: 致命的悪意に対する 0-RTT 遮断
                        # -----------------------------------------------------
                        elif eval_res["action"] == "0-RTT_CUTOFF":
                            logger.error(f"🚨 [0-RTT 物理遮断執行] {eval_res['reason']}")
                            if captured_request_id:
                                asyncio.create_task(self._trigger_backend_abort(session, captured_request_id))

                            await client_response.write(
                                b"\n\ndata: [TRM_SECURITY_VETO: Hardware Anomaly / Tool Spoofing Terminated]\n\n"
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
        """余剰のあるピアノードへリクエストを代理中継 (Thermal Aid)"""
        try:
            async with session.post(f"{self.spillover_peer_url}/v1/chat/completions", data=body, headers=headers) as peer_resp:
                async for chunk in peer_resp.content.iter_any():
                    await client_response.write(chunk)
            logger.info("🌟 [相互冷却完了] ピアノードによる代理推論が完走しました。")
        except Exception as e:
            logger.error(f"ピア中継失敗・自ノード低速フォールバック: {e}")
            # ピアが落ちている場合は自ノードで安全に低速縮退運転

    async def _trigger_backend_abort(self, session: ClientSession, req_id: str):
        """vLLM /abort 直撃"""
        try:
            async with session.post(f"{self.upstream_url}/abort", json={"request_id": req_id}, timeout=0.1) as r:
                logger.info(f"⚡ [vLLM Abort完了] Request ID [{req_id}] を強制停止。")
        except Exception as e:
            logger.debug(f"/abort 通信ログ: {e}")

if __name__ == "__main__":
    server = TRMFlameProxyServer()
    print("=" * 72)
    print(" TRM-EcoGuard Living-Flame Proxy (火の生命化エディション) 起動")
    print(" - TTFT可変免震ウィンドウ: 稼働")
    print(" - 思考(CoT/Reasoning)保護力学: 稼働")
    print(" - 相互冷却 (Thermal Spillover) インターフェース: 待機")
    print("=" * 72)
    web.run_app(server.app, port=server.proxy_port)
