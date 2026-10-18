import re
import json

# レスポンスID抽出用正規表現
RE_CHAT_ID = re.compile(rb'"id"\s*:\s*"([^"]+)"')

class TRMProxyServer:
    # ... (前略) ...
    async def handle_chat_completions(self, request: web.Request) -> web.StreamResponse:
        body = await request.read()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in ("host", "content-length")}
        self.comparator.notify_prefill_start(duration_ms=150.0)

        client_response = web.StreamResponse(status=200, headers={"Content-Type": "text/event-stream"})
        await client_response.prepare(request)

        token_count = 0
        start_time = time.time()
        cutoff_triggered = False
        captured_request_id = None
        sse_buffer = b""

        timeout = ClientTimeout(total=300)
        async with ClientSession(timeout=timeout) as session:
            try:
                async with session.post(f"{UPSTREAM_URL}/v1/chat/completions", data=body, headers=headers) as upstream_resp:
                    if upstream_resp.status != 200:
                        err_content = await upstream_resp.read()
                        await client_response.write(err_content)
                        return client_response

                    async for chunk in upstream_resp.content.iter_any():
                        # 震ちゃんパッチ②: 初手チャンクから vLLM 内部 request_id を動的捕獲
                        if captured_request_id is None:
                            match = RE_CHAT_ID.search(chunk)
                            if match:
                                captured_request_id = match.group(1).decode("utf-8", errors="ignore")

                        # 震ちゃんパッチ①: パケット分断に耐える正確なトークン集計
                        sse_buffer += chunk
                        while b"\n\n" in sse_buffer:
                            event_block, sse_buffer = sse_buffer.split(b"\n\n", 1)
                            for line in event_block.split(b"\n"):
                                if line.startswith(b"data: "):
                                    payload = line[6:].strip()
                                    if payload and payload != b"[DONE]":
                                        token_count += 1

                        elapsed = max(0.001, time.time() - start_time)
                        tokens_per_sec = token_count / elapsed

                        hw_sample = self.harvester.get_sample()
                        eval_res = self.comparator.evaluate(
                            reported_tokens_sec=tokens_per_sec,
                            is_generating=True,
                            current_raw_power=hw_sample.power_watts,
                            pid_sm=hw_sample.pid_sm_utilization
                        )

                        # 🚨 0-RTT 遮断執行
                        if eval_res["action"] == "0-RTT_CUTOFF":
                            cutoff_triggered = True
                            logger.error(
                                f"🚨 [0-RTT 物理遮断執行] {eval_res['reason']} | "
                                f"Tokens/s: {tokens_per_sec:.1f}, 実測電力: {hw_sample.power_watts:.1f}W"
                            )
                            # 二重キルスイッチ: vLLM /abort を直撃してCUDAカーネル停止
                            if captured_request_id:
                                asyncio.create_task(self._trigger_backend_abort(session, captured_request_id))

                            await client_response.write(
                                b"\n\ndata: [TRM_SECURITY_VETO: Hardware Capacity Limit or Spoofing Detected]\n\n"
                            )
                            break

                        await client_response.write(chunk)

            except asyncio.CancelledError:
                if captured_request_id:
                    asyncio.create_task(self._trigger_backend_abort(session, captured_request_id))
            except Exception as e:
                logger.error(f"プロキシ中継エラー: {e}")
            finally:
                if cutoff_triggered:
                    try:
                        if not client_response.is_eof():
                            await client_response.write_eof()
                        trans = request.transport
                        if trans and not trans.is_closing():
                            trans.close()
                    except Exception as e:
                        logger.debug(f"クライアントソケット安全破棄: {e}")

        return client_response

    async def _trigger_backend_abort(self, session: ClientSession, req_id: str):
        """vLLM /abort エンドポイントへの即時中絶シグナル送出"""
        try:
            async with session.post(f"{UPSTREAM_URL}/abort", json={"request_id": req_id}, timeout=0.1) as r:
                logger.info(f"⚡ [vLLM Abort完了] Request ID [{req_id}] のGPU演算を強制中絶しました。")
        except Exception as e:
            logger.debug(f"/abort 通信フォールバック (HTTPセッション切断で担保): {e}")
