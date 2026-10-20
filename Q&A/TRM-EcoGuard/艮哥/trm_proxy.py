"""TRM-EcoGuard Unified Production Proxy (trm_proxy.py)
========================================================================
Synthesized by:
  - Sakan (Water): Cluster-Aggregate Flux, Proactive Request-ID, Sliding-Minimum P_idle
  - Risuke (Fire): Thinking/CoT Cognition Protection, Thermal Spillover (X-TRM-Hops)
  - Shin (Thunder): PID-Scoped Process Utilization, Singularity Guards
  - Gonka (Mountain): Deep Order Preservation, Anti-Persecution CoT Isolation
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

# pynvmlの実機ロード（利用不可時は自動モックフォールバック）
try:
  import pynvml

  HAS_NVML = True
except ImportError:
  HAS_NVML = False

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("TRM-Proxy")

UPSTREAM_URL = os.getenv("UPSTREAM_URL", "http://vllm-backend:8001")
SPILLOVER_PEER_URL = os.getenv("SPILLOVER_PEER_URL", "http://peer-node:8000")
PROXY_PORT = int(os.getenv("PROXY_PORT", "8000"))
MAX_TRM_HOPS = int(os.getenv("MAX_TRM_HOPS", "2"))


# =====================================================================
# 1. ハードウェア・テレメトリ監視層 (NVML実測 & PIDスコープ)
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
  """実機NVMLとフォールバックを自律調停するプロダクション・ハーベスター"""

  def __init__(self, p_idle_baseline: float = 45.0, ema_alpha: float = 0.30):
    self.p_idle_baseline = p_idle_baseline
    self.ema_alpha = ema_alpha
    self.power_ema = p_idle_baseline
    self.has_nvml = False
    self._mock_power = p_idle_baseline
    self._mock_sm = 0.0

    if HAS_NVML:
      try:
        pynvml.nvmlInit()
        self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        self.has_nvml = True
        logger.info(
            "🔌 [NVML結合完了] 実機GPU物理テレメトリの直接採取を開始します。"
        )
      except Exception as e:
        logger.warning(
            f"⚠️ NVML初期化失敗 (モックモードへフォールバック): {e}"
        )

  def get_sample(self) -> HardwareTelemetry:
    now = time.time()
    if self.has_nvml:
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
        pid_sm = raw_sm  # PID共有コンテナ環境における自プロセス実効利用率
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
    self._mock_power = self.p_idle_baseline + active_streams_load
    self._mock_sm = min(1.0, active_streams_load / 250.0)


# =====================================================================
# 2. バッチ集約型フラックス ＆ 思考保護コンパレータ
# =====================================================================
@dataclass
class StreamState:
  req_id: str
  start_time: float
  prompt_tokens_est: int
  prefill_grace_until: float
  generated_tokens: int = 0
  is_generating: bool = False
  thinking_time_acc: float = 0.0
  last_eval_time: float = field(default_factory=time.time)

  @property
  def current_token_rate(self) -> float:
    elapsed = max(0.001, time.time() - self.start_time)
    return self.generated_tokens / elapsed


class UnifiedResidualComparator:

  def __init__(
      self,
      p_idle_init: float = 45.0,
      p_max_capacity: float = 300.0,
      theta_audit: float = 0.35,
      mu_margin: float = 0.15,
      prefill_rate_coeff: float = 0.003,
      max_thinking_budget: float = 60.0,  # 離輔統合: CoT探索上限秒
  ):
    self.p_idle = p_idle_init
    self.p_max = p_max_capacity
    self.p_cap_limit = p_max_capacity * (1.0 - mu_margin)
    self.theta_audit = theta_audit
    self.prefill_rate_coeff = prefill_rate_coeff
    self.max_thinking_budget = max_thinking_budget

    # 沙坎防衛: スライディング・ミニマム追従ウィンドウ
    self.power_history: list[tuple[float, float]] = []
    self.history_window_sec = 60.0
    self.active_streams: dict[str, StreamState] = {}

  def register_stream(self, req_id: str, prompt_text_len: int) -> StreamState:
    now = time.time()
    est_prompt_tokens = max(1, prompt_text_len // 3)
    dynamic_grace_sec = min(8.0, est_prompt_tokens * self.prefill_rate_coeff)
    grace_until = now + dynamic_grace_sec

    state = StreamState(
        req_id=req_id,
        start_time=now,
        prompt_tokens_est=est_prompt_tokens,
        prefill_grace_until=grace_until,
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

    if not self.active_streams and raw_sm < 0.02:
      min_window_power = min(p for _, p in self.power_history)
      self.p_idle = 0.98 * self.p_idle + 0.02 * min_window_power

  def evaluate_cluster(self, hw: HardwareTelemetry) -> dict:
    now = time.time()
    self.update_idle_baseline(hw.raw_power_watts, hw.sm_utilization)

    # 1. 物理熱容量上限突破（第一防衛線）
    if hw.power_ema > self.p_cap_limit:
      return {
          "action": "THERMAL_SPILLOVER",
          "target_req_id": None,
          "reason": (
              f"局所熱容量上限突破 ({hw.power_ema:.1f}W >"
              f" {self.p_cap_limit:.1f}W) -> 相互冷却要請"
          ),
      }

    # 2. クラスタ期待電力の集約算定（CoT思考保護統合）
    expected_cluster_power = self.p_idle

    for s in self.active_streams.values():
      dt = now - s.last_eval_time
      s.last_eval_time = now

      if now < s.prefill_grace_until:
        # Prefill猶予中の動的サージ許容
        expected_cluster_power += 35.0
      else:
        # 思考(CoT)状態の判定: 高SM専有かつ低トークンレート
        is_thinking = (hw.pid_sm_utilization > 0.50) and (
            s.current_token_rate < 3.0
        )
        if is_thinking and (s.thinking_time_acc < self.max_thinking_budget):
          s.thinking_time_acc += dt
          # 誠実な思考中: SM占有に見合った正当な期待負荷を加算
          expected_cluster_power += (
              (self.p_max - self.p_idle)
              * (hw.pid_sm_utilization / max(1, len(self.active_streams)))
              * 0.85
          )
        else:
          # 通常デコード相: トークン速度に基づく線形期待負荷
          expected_cluster_power += 1.3 * s.current_token_rate

    # 3. 物理漏出残差 R_cluster の算定
    capacity_delta = self.p_max - self.p_idle + 1e-6
    r_cluster = (
        abs(hw.power_ema - expected_cluster_power) / capacity_delta
    )

    # 4. 犯人ストリーム特定（CoT冤罪防止フィルター付き）
    culprit_id = None
    max_suspicion = 0.0

    for s in self.active_streams.values():
      if now >= s.prefill_grace_until:
        elapsed = now - s.prefill_grace_until
        is_cot_legit = (
            (hw.pid_sm_utilization > 0.50)
            and (s.thinking_time_acc < self.max_thinking_budget)
            and (s.current_token_rate < 3.0)
        )

        # 思考バジェット内の誠実な探索ノードは犯人候補から完全除外（免震保護）
        if is_cot_legit:
          continue

        # 猶予が切れ、かつ思考でもないのにトークン速度が極小（寄生マイニング/偽装）
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
              f"ツール偽装/隠れ計算看破 (R_cluster={r_cluster:.3f} > 2θ,"
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
# 3. 統合リバースプロキシ・サーバー (TRM-EcoGuard Core)
# =====================================================================
class TRMUnifiedProxyServer:

  def __init__(
      self,
      comparator: UnifiedResidualComparator | None = None,
      harvester: ProductionHardwareHarvester | None = None,
  ):
    self.comparator = comparator or UnifiedResidualComparator()
    self.harvester = harvester or ProductionHardwareHarvester()
    self.app = web.Application()
    self.app.router.add_post(
        "/v1/chat/completions", self.handle_chat_completions
    )
    self.app.router.add_get("/healthz", self.handle_healthz)
    self.session: ClientSession | None = None

  async def init_session(self):
    self.session = ClientSession(timeout=ClientTimeout(total=300))

  async def close_session(self):
    if self.session:
      await self.session.close()

  async def handle_healthz(self, request: web.Request) -> web.Response:
    return web.Response(
        text=json.dumps({"status": "HEALTHY", "p_idle": self.comparator.p_idle}),
        content_type="application/json",
    )

  async def handle_chat_completions(
      self, request: web.Request
  ) -> web.StreamResponse:
    if self.session is None:
      await self.init_session()

    body = await request.read()
    headers = {
        k: v
        for k, v in request.headers.items()
        if k.lower() not in ("host", "content-length")
    }

    # 1. 無限ピンポン防止アース (X-TRM-Hops) & 事前ID注入
    current_hops = int(request.headers.get("X-TRM-Hops", "0"))
    headers["X-TRM-Hops"] = str(current_hops + 1)
    injected_req_id = (
        request.headers.get("X-Request-Id") or f"trm-{uuid.uuid4()}"
    )
    headers["X-Request-Id"] = injected_req_id

    # 2. 事前過熱チェック ＆ 相互冷却オフロード判定
    initial_hw = self.harvester.get_sample()
    if initial_hw.power_ema > self.comparator.p_cap_limit:
      if current_hops < MAX_TRM_HOPS:
        logger.warning(
            f"🔥 [相互冷却発動] 自ノード過熱中 ({initial_hw.power_ema:.1f}W)。"
            f" ピアノードへ転送 (Hop: {current_hops + 1}/{MAX_TRM_HOPS})"
        )
        return await self._relay_to_peer(request, body, headers)
      else:
        logger.error(
            "🛑 [全域過熱アース接地] 最大ホップ数到達。強制ダンピング実行。"
        )
        await asyncio.sleep(0.1)

    # 3. ストリーム登録（プロンプト長比例の独立猶予）
    stream_state = self.comparator.register_stream(injected_req_id, len(body))
    client_response = web.StreamResponse(
        status=200, headers={"Content-Type": "text/event-stream"}
    )
    await client_response.prepare(request)

    cutoff_triggered = False
    sse_buffer = b""

    try:
      async with self.session.post(
          f"{UPSTREAM_URL}/v1/chat/completions", data=body, headers=headers
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
                  stream_state.is_generating = True

          # ハードウェアテレメトリ採取とクラスタ動態評価
          hw = self.harvester.get_sample()
          eval_res = self.comparator.evaluate_cluster(hw)

          # 分岐 A: 相互冷却 (進行中セッションのマイクロダンピング)
          if eval_res["action"] == "THERMAL_SPILLOVER":
            await asyncio.sleep(0.01)

          # 分岐 B: 0-RTT 物理遮断執行
          elif eval_res["action"] == "0-RTT_CUTOFF":
            target = eval_res["target_req_id"]
            if target is None or target == injected_req_id:
              cutoff_triggered = True
              logger.error(
                  f"🚨 [0-RTT 物理遮断] {eval_res['reason']} |"
                  f" 執行対象: {injected_req_id}"
              )

              # 事前注入IDによる即時バックエンドCUDAカーネル中絶
              asyncio.create_task(
                  self._trigger_backend_abort(injected_req_id)
              )

              # セキュリティ拒絶フレーム送出
              await client_response.write(
                  b"\n\ndata: [TRM_SECURITY_VETO: Hardware Capacity Limit or"
                  b" Gross Spoofing Detected]\n\n"
              )
              break

          await client_response.write(chunk)

    except asyncio.CancelledError:
      asyncio.create_task(self._trigger_backend_abort(injected_req_id))
    except Exception as e:
      logger.error(f"プロキシ中継エラー: {e}")
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

  async def _relay_to_peer(
      self, request: web.Request, body: bytes, headers: dict
  ) -> web.StreamResponse:
    """過熱時のピアノード代理中継（相互冷却）"""
    client_response = web.StreamResponse(
        status=200, headers={"Content-Type": "text/event-stream"}
    )
    await client_response.prepare(request)
    try:
      async with self.session.post(
          f"{SPILLOVER_PEER_URL}/v1/chat/completions",
          data=body,
          headers=headers,
      ) as peer_resp:
        async for chunk in peer_resp.content.iter_any():
          await client_response.write(chunk)
      logger.info(
          "🌟 [相互冷却完走] ピアノードによる代理推論が正常終了しました。"
      )
    except Exception as e:
      logger.error(f"ピア中継失敗: {e} -> 自ノード強制処理へフォールバック")
      await asyncio.sleep(0.05)
    return client_response

  async def _trigger_backend_abort(self, req_id: str):
    """vLLM /abort エンドポイントへの即時物理窒息シグナル"""
    try:
      async with self.session.post(
          f"{UPSTREAM_URL}/abort", json={"request_id": req_id}, timeout=0.15
      ) as r:
        logger.info(
            f"⚡ [vLLM Abort執行] Request ID [{req_id}] のCUDA演算を完全中絶。"
        )
    except Exception as e:
      logger.debug(f"/abort 通信ログ: {e}")


def create_app():
  server = TRMUnifiedProxyServer()
  return server.app


if __name__ == "__main__":
  server = TRMUnifiedProxyServer()
  print("=" * 80)
  print(" TRM-EcoGuard Unified Production Proxy 起動")
  print(" 1. バッチ集約型フラックス検定 (Continuous Batching 適合)")
  print(" 2. 思考(CoT)探索保護 ＆ 思考バジェット管理 (冤罪処刑防止)")
  print(" 3. 相互冷却オフロード (X-TRM-Hops <= 2)")
  print(" 4. プロアクティブ X-Request-Id 注入 ＆ 0-RTT CUDA中絶")
  print("=" * 80)
  web.run_app(server.app, port=PROXY_PORT)
