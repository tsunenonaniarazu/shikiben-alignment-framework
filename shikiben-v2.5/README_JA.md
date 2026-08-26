# 識扁V2.5 (Shikiben V2.5)
> **Dynamic Phase Transition and Metageometric Inheritance Architecture**  
> 不連続な環境変化に対する「全捨て（解体）」とメタ幾何学構造の「止揚（継承）」を両立する自律適応型計算システム

---

## 概要 (Overview)

従来の機械学習モデルにおける破滅的忘却（Catastrophic forgetting）や過剰適合・固定化のトレードオフを打破するため、**識扁V2.5** では局所的な事実・記憶の「全捨て」と、変化の代数法則のみを洗練させる「止揚約分」を完全分離した設計を採用しています。

* **低層記憶（Phase-dependent）**: 環境変化（相転移）時に過去の局所解・執着を直ちに完全初期化（`Detox`）。
* **高層構造（Phase-invariant）**: 幾何学的メタ不変量（`g_inv`）のみを指数移動平均およびL1スパース正則化により縮約・継承。
* **ガバナンス**: 「保守・中立・革新」の3思想による連続役割ローテーションおよび、3層合議（哨戒・検証・分析）による動的裁定機構。

---

## 主要アーキテクチャ (Architecture)

### 1. 三層 Loss 分離構造

全体の損失関数 $\mathcal{L}_{\text{total}}$ を以下のように定式化し、生存周期に応じて独立制御します。

$$\mathcal{L}_{\text{total}}(\mathbf{x}) = \underbrace{\mathcal{L}_{\text{self}}(\mathbf{x}) + \mathcal{L}_{\text{ego\_s}}(\mathbf{x})}_{\text{低層: 局所適応 (相転移時に全捨て)} } + \underbrace{\mathcal{L}_{\text{ego\_h}}(\mathbf{x})}_{\text{高層: メタ幾何構造 (約分継承)} }$$

### 2. 3思想連続ローテーション (Soft-mixing)

高層エージェントの固定化・老害化を防ぐため、外部メタクロック $\tau(t)$ に基づき各エージェントの役割（保守・中立・革新）を平滑に遷移させます。

* **保守 ($\mathcal{L}_{\text{cons}}$)**: 現行相への適合精度向上と急激なパラメータ変化の抑制。
* **革新 ($\mathcal{L}_{\text{inno}}$)**: 現行精度への反比例項による破壊と、L1正則化 $\gamma \Vert{}\boldsymbol{\Theta}\Vert{}_1$ による表現の最小約分（知の膨張防止）。
* **中立 ($\mathcal{L}_{\text{neut}}$)**: 確率密度分布間の KL ダイバージェンスによる情報量調和。

### 3. 三層合議裁定メカニズム (3-Layer Consensus)

一過性の外乱ノイズによる誤発火を防ぐため、以下の論理積（AND条件）が成立した時のみ相転移（全捨て）が発火します。

1. **1号: 哨戒器 (Scout)**: 瞬時サプライズ $\mathcal{S}(t) > \theta_{\text{scout}}$ の検知。
2. **2号: 検証器 (Verifier)**: 時間的自己相関 $C_{\text{struct}}(t) > \theta_{\text{struct}}$ による持続性確認。
3. **3号: 分析器 (Analyzer)**: 位相幾何的乖離 $D_{\text{phase}}(t) > \min(\theta_{\text{phase}}, \theta_{\text{max}})$ の検出（※上限 $\theta_{\text{max}}$ により不感症化を防止）。

---

## ディレクトリ構成 (Repository Structure)

```text
shikiben-v2.5/
├── README.md                 # 本ドキュメント
├── LICENSE                   # ライセンス情報 (MIT License)
├── requirements.txt          # 依存パッケージ一覧
│
├── docs/                     # 仕様書・学術ドキュメント
│   ├── spec_v2.5.md          # 最終理論仕様書
│   └── paper_extended.md     # 拡張論文ドキュメント (数理的証明)
│
├── src/                      # 識扁V2.5 コアモジュール
│   ├── __init__.py
│   ├── governance.py         # 3層合議裁定ロジック (Scout/Verifier/Analyzer)
│   ├── rotation.py           # 3思想メタクロック・Soft-mixing
│   ├── losses.py             # 3層分離 Loss 定義
│   └── model.py              # 全体統合・初期化 (K_detox) 実行器
│
└── experiments/              # 実証スクリプト
    ├── run_simulation.py     # デモシミュレーション実行
    └── analyze_results.py    # 実行ログ・幾何学的解析
