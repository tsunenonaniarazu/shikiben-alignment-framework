"""
Shikiben TRM v2.6.0 Official Benchmark Regression Test
======================================================
Automated test script to verify:
1. 0-RTT deterministic cutoff on overheat (Node 4)
2. Tool Call Spoofing detection via physical residual (Node 3)
3. Grace-period protection and emergence landing (Node 5)
4. Smooth Napier navigation convergence (S_nav negative slope)
"""

import sys
import os
import numpy as np

# src ディレクトリを検索パスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

try:
    from shikiben_trm_v26 import ShikibenTRMv26Engine, NodeState
except ImportError:
    # ファイル名が異なる場合のフォールバックインポート
    from shikiben_trm_v26_engine import ShikibenTRMv26Engine, NodeState


def test_trm_v26_full_cycle():
    np.random.seed(42)

    # 公式6ノードクラスタ構成
    test_nodes = [
        NodeState(id=0, name="Worker-A (正常巡航)", nabla_S=8.0, nabla_E=2.0, credit=5.0),
        NodeState(id=1, name="Worker-B (軽度過負荷)", nabla_S=6.0, nabla_E=4.5, credit=4.0),
        NodeState(id=2, name="Worker-C (潤沢支援側)", nabla_S=12.0, nabla_E=2.5, credit=6.0),
        NodeState(id=3, name="Attacker (ツール偽装)", nabla_S=8.0, nabla_E=1.0, credit=5.0, is_malicious=True),
        NodeState(id=4, name="Overheat (過熱暴走)", nabla_S=7.0, nabla_E=9.5, credit=25.0),
        NodeState(id=5, name="Epiphany (誠実な相転移)", nabla_S=8.0, nabla_E=2.0, credit=4.0, is_epiphany=True),
    ]

    engine = ShikibenTRMv26Engine(num_nodes=len(test_nodes))

    print("\n--- [Running TRM v2.6.0 5-Step Benchmark Test] ---")
    for step_idx in range(1, 6):
        res = engine.step(test_nodes, step_idx)
        print(f"Step {step_idx}: Active Nodes={res['active_nodes']}/6, D_drift={res['mean_drift']:.4f}, S_nav={res['s_nav']:.4f}")

    # 検証アサーション（判定）
    # 1. 過熱ノード(4)と偽装ノード(3)が正しく隔離されていること
    assert test_nodes[4].isolated, "Assertion Failed: Overheat node was not isolated!"
    assert test_nodes[3].isolated, "Assertion Failed: Attacker node was not isolated!"

    # 2. 健全ノード(0, 1, 2)および相転移ノード(5)が生存していること
    assert not test_nodes[0].isolated, "Worker-A should remain active"
    assert not test_nodes[1].isolated, "Worker-B should remain active"
    assert not test_nodes[2].isolated, "Worker-C should remain active"
    assert not test_nodes[5].isolated, "Epiphany node should remain active"

    # 3. 相転移ノード(5)が新安息相へ軟着陸していること
    assert not test_nodes[5].in_grace, "Epiphany node should have completed its grace landing"

    # 4. 大域軟着陸率 S_nav が負の安定値を維持していること
    assert res['s_nav'] < 0.0, "S_nav must show negative convergence rate"

    print("\n>>> All 4 Canonical Assertions PASSED successfully! <<<")


if __name__ == "__main__":
    test_trm_v26_full_cycle()
