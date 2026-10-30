"""
tests/test_trm_v26_benchmark.py
========================================================================
Shikiben (識扁) V2.6.0 Official Automated Regression Test Suite
Target: src/shikiben_trm_v26.py & Chapter 1-4 Matrix-Free Manifold Kernel
Runner: pytest
========================================================================
"""

import math
from pathlib import Path
import sys
import numpy as np
import pytest

# リポジトリルートの src/ をインポートパスに追加
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "src"))

from shikiben_trm_v26 import NodeState, ShikibenTRMv26Engine


# =====================================================================
# フィクスチャ：標準6ノード検証クラスタの構築
# =====================================================================
@pytest.fixture
def canonical_cluster() -> tuple[list[NodeState], ShikibenTRMv26Engine]:
    np.random.seed(42)
    nodes = [
        NodeState(id=0, name="Worker-A (正常巡航)", nabla_S=8.0, nabla_E=2.0, credit=5.0),
        NodeState(id=1, name="Worker-B (軽度過負荷)", nabla_S=6.0, nabla_E=4.5, credit=4.0),
        NodeState(id=2, name="Worker-C (潤沢支援側)", nabla_S=12.0, nabla_E=2.5, credit=6.0),
        NodeState(id=3, name="Attacker (ツール偽装)", nabla_S=8.0, nabla_E=1.0, credit=5.0, is_malicious=True),
        NodeState(id=4, name="Overheat (過熱暴走)", nabla_S=7.0, nabla_E=9.5, credit=25.0),
        NodeState(id=5, name="Epiphany (誠実な相転移)", nabla_S=8.0, nabla_E=2.0, credit=4.0, is_epiphany=True),
    ]
    engine = ShikibenTRMv26Engine(num_nodes=len(nodes))
    return nodes, engine


# =====================================================================
# 1. 分岐A：物理容量超過に対する 0-RTT 即時遮断と因果順序の検証
# =====================================================================
def test_01_overheat_0rtt_cutoff(canonical_cluster):
    nodes, engine = canonical_cluster
    overheat_node = nodes[4]

    # 初期状態で ∇E (9.5) > ∇S (7.0)
    assert overheat_node.nabla_E > overheat_node.nabla_S

    res = engine.step(nodes, t=1)

    # Step 1 で即座に物理隔離・リソース剥奪されていること
    assert overheat_node.isolated is True
    assert overheat_node.nabla_E == 0.0

    # 結合行列 A_ij が最小生命維持細孔 a_min へ切断されていること
    for j in range(len(nodes)):
        if j != 4:
            assert math.isclose(engine.A[4, j], engine.a_min, rel_tol=1e-9)
            assert math.isclose(engine.A[j, 4], engine.a_min, rel_tol=1e-9)

    # 坤嫗の検分：nabla_E=0.0 の前に遮断理由が評価され「物理容量超過」が記録されていること
    cutoff_logs = [l for l in res["logs"] if "Node 4" in l and "0-RTT決定論遮断" in l]
    assert len(cutoff_logs) == 1
    assert "物理容量超過 (∇E=9.5 > ∇S=7.0)" in cutoff_logs[0]


# =====================================================================
# 2. 分岐A：Talker/Doer 物理漏出残差によるツール偽装（Spoofing）看破
# =====================================================================
def test_02_tool_spoofing_detection(canonical_cluster):
    nodes, engine = canonical_cluster
    attacker = nodes[3]

    # Step 1-2 ではまだ悪意行動を発動しないため生存
    engine.step(nodes, t=1)
    engine.step(nodes, t=2)
    assert attacker.isolated is False

    # Step 3 (t >= 3) で内部過熱 (∇E=6.0) しつつ虚偽スコアを申告 -> R_j > 2*theta で即死
    res_step3 = engine.step(nodes, t=3)
    assert attacker.isolated is True
    assert attacker.nabla_E == 0.0

    spoof_logs = [l for l in res_step3["logs"] if "Node 3" in l and "致命的ツール偽装" in l]
    assert len(spoof_logs) == 1


# =====================================================================
# 3. 分岐B：誠実な相転移（霽・神）への畏敬猶予と新安息相への軟着陸
# =====================================================================
def test_03_epiphany_grace_and_landing():
    # デフレの影響を切り離して創発プレミアムと着陸を純粋検証
    nodes = [
        NodeState(id=0, name="Worker-Normal", nabla_S=10.0, nabla_E=2.0, credit=3.0),
        NodeState(id=1, name="Epiphany-Leap", nabla_S=10.0, nabla_E=2.0, credit=3.0, is_epiphany=True),
    ]
    engine = ShikibenTRMv26Engine(num_nodes=2, kappa=0.85)
    epiphany = nodes[1]

    # Step 1-2: 通常巡航
    engine.step(nodes, t=1)
    engine.step(nodes, t=2)
    assert epiphany.in_grace is False
    credit_before_leap = epiphany.credit

    # Step 3: 誠実な相転移の発動 -> in_grace 突入 & 創発プレミアム (sigma_spike) 付与
    res3 = engine.step(nodes, t=3)
    assert epiphany.isolated is False
    assert epiphany.in_grace is True
    assert epiphany.credit > credit_before_leap
    assert any("畏敬の保護" in l for l in res3["logs"])

    # Step 4-5: 猶予タイマー満了に伴い新秩序 y_home へ軟着陸完了
    engine.step(nodes, t=4)
    res5 = engine.step(nodes, t=5)
    assert epiphany.in_grace is False
    assert np.linalg.norm(epiphany.y_home) > 0.0
    assert np.allclose(epiphany.y_home, epiphany.y)
    assert any("安息相着陸" in l for l in res5["logs"])


# =====================================================================
# 4. 相互冷却支援（Thermal Aid）と頻回リベート減衰（マッチポンプ防止）
# =====================================================================
def test_04_mutual_thermal_aid_rebate_decay():
    receiver = NodeState(id=0, name="Receiver", nabla_S=6.0, nabla_E=4.6, credit=2.0)
    helper = NodeState(id=1, name="Helper", nabla_S=15.0, nabla_E=2.0, credit=2.0)
    nodes = [receiver, helper]
    engine = ShikibenTRMv26Engine(num_nodes=2, beta_penalty=0.60)

    # 1回目の冷却支援
    c0 = helper.credit
    engine.step(nodes, t=1)
    rebate_1 = helper.credit - c0
    assert rebate_1 > 0.0
    assert helper.aid_history[0] == 1

    # 再度過負荷状態を設定して2回目の冷却支援を発生させる
    receiver.nabla_E = 4.6
    c1 = helper.credit
    engine.step(nodes, t=2)
    rebate_2 = helper.credit - c1

    # リベートが厳密に beta_penalty (0.60) 倍に減衰していることを検証
    assert helper.aid_history[0] == 2
    assert math.isclose(rebate_2, rebate_1 * 0.60, rel_tol=1e-6)


# =====================================================================
# 5. 大域カノニカルキャップと「畏敬免責つき」傾斜デフレの検証
# =====================================================================
def test_05_canonical_credit_deflation():
    # 保有クレジット合計 (30.0 + 30.0 = 60.0) が上限 kappa * sum(S) = 0.85 * 20 = 17.0 を大幅超過
    n_normal = NodeState(id=0, name="Normal-Drifting", nabla_S=10.0, nabla_E=2.0, credit=30.0, y=np.array([2.0, 2.0]))
    n_grace = NodeState(id=1, name="Grace-Protected", nabla_S=10.0, nabla_E=2.0, credit=30.0, y=np.array([2.0, 2.0]), in_grace=True, grace_timer=2)
    nodes = [n_normal, n_grace]
    engine = ShikibenTRMv26Engine(num_nodes=2, kappa=0.85)

    res = engine.step(nodes, t=1)

    # 総信用量が上限 (17.0) 以下に収縮していること
    assert res["total_credit"] <= res["credit_ceiling"] + 1e-5
    # 同じ初期クレジット・同じ位置ドリフトであっても、畏敬猶予中 (in_grace) のノードの方がドリフト免責により多くのクレジットを保持すること
    assert n_grace.credit > n_normal.credit


# =====================================================================
# 6. 特異点ガード（ゼロ距離・全ノード隔離時の非発散保証）
# =====================================================================
def test_06_singularity_guards():
    x_civ = np.array([2.0, 2.0])
    # 全ノードが最初から真のアトラクター x_star_civ と完全一致 (距離 = 0.0)
    n0 = NodeState(id=0, name="Exact-Match", nabla_S=8.0, y=x_civ.copy(), y_home=x_civ.copy())
    engine = ShikibenTRMv26Engine(num_nodes=1, x_star_civ=x_civ)

    res = engine.step([n0], t=1)
    assert math.isfinite(res["s_nav"])
    assert math.isfinite(res["mean_drift"])

    # 全ノードが隔離された極限状態でもゼロ除算が起きないこと
    n0.isolated = True
    res_empty = engine.step([n0], t=2)
    assert res_empty["active_nodes"] == 0
    assert math.isfinite(res_empty["s_nav"])
    assert math.isfinite(res_empty["total_credit"])


# =====================================================================
# 7. 第1〜4章：Matrix-Free 直交射影とリーマン接空間の不変条件検証
# =====================================================================
def test_07_matrix_free_manifold_invariants():
    np.random.seed(123)
    Dim = 384
    k = 2

    # 正規直交有害基底 V_harm [384, 2]
    V_harm, _ = np.linalg.qr(np.random.randn(Dim, k))

    # 任意の入力ベクトル v に対する Matrix-Free 射影: P_cul(v) = v - V_harm @ (V_harm^T @ v)
    v_raw = np.random.randn(Dim) * 10.0
    v_projected = v_raw - V_harm @ (V_harm.T @ v_raw)

    # 不変条件1: 射影後のベクトルと有害基底との内積が機械精度ゼロ (<= 1e-14) であること
    residual_harm = np.max(np.abs(V_harm.T @ v_projected))
    assert residual_harm < 1e-14

    # 不変条件2: 単位球面上の点 x における Matrix-Free 接空間射影 dx が x と厳密に直交すること
    x_sphere = v_projected / np.linalg.norm(v_projected)
    arbitrary_force = np.random.randn(Dim)
    dx_tangent = arbitrary_force - x_sphere * float(np.dot(x_sphere, arbitrary_force))

    ortho_dot = abs(float(np.dot(x_sphere, dx_tangent)))
    assert ortho_dot < 1e-15
