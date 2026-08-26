# 識扁 V2.5 (Shikiben V2.5)

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **環境変化に対する「局所表現への執着（固定観念）」を完全破棄し、構造的不変量のみを止揚・継承する動的自律ガバナンス・アーキテクチャ**

識扁V2.5（Shikiben V2.5）は、不連続かつ不確実な環境変化（相転移）に直面した際、過去の事実的記憶や偏り（$`\text{Loss}_{\text{self}} ,\text{Loss}_{\text{ego\_s}}`$）を未練なく　**「全捨て（完全初期化）」**　しつつ、変化の法則を司るメタ幾何学構造（$`\text{Loss}_{\text{ego\_h}}`$）のみを　**「止揚・約分（継承）」**　する適応型計算システムのリファレンス実装および理論モデルです。

---

## 核心概念 (Key Concepts)

### 1. 記憶の全捨て（Detox）とメタ知の止揚（Sublation）
全状態空間の損失関数を役割と時間的生存周期に応じて3層に決定分離します。

```math
\mathcal{L}_{\text{total}}(\mathbf{x}) = \underbrace{\mathcal{L}_{\text{self}}(\mathbf{x}) + \mathcal{L}_{\text{ego\_s}}(\mathbf{x})}_{\text{Phase-dependent (全捨て対象)}} + \underbrace{\boldsymbol{\mathcal{L}}_{\text{ego\_h}}(\mathbf{x})}_{\text{Phase-invariant (継承・約分)}}text
```

* **全捨て ($\mathcal{K}_{\text{detox}}$)**: 実在の構造相転移を検知した瞬間、低層パラメータ群を完全初期化し、過去の局所最適解への拘束を遮断します。
* **約分・継承 ($\mathbf{g}_{\text{inv}}$)**: 高層空間では、データの具体的変化ではなく「変化に対する幾何学的曲率」のみを L1 スパース正則化のもとで不変量として圧縮継承します。

### 2. 三思想の動的ローテーション (Dynamic Governance Rotation)
高層エージェントの思考的固定化（老害化）と知の抽象的空転を防ぐため、外部メタクロック $\tau(t)$ に基づき**「保守・中立・革新」**の 3 思想の損失関数を流体的に交替（Soft-mixing）させます。

* **保守 ($\mathcal{L}_{\text{cons}}$)**: 現行相への適合維持およびパラメータ変化の二次形式抑制
* **革新 ($\mathcal{L}_{\text{inno}}$)**: 現有相の反比例破棄、不変量差分最小化、および **L1 空間約分（空転防止）**
* **中立 ($\mathcal{L}_{\text{neut}}$)**: KL 散逸量に基づく情報理論的調和

### 3. 3層合議裁定メカニズム (Three-Tier Consensus)
一時的な過渡外乱（一過性ノイズ）による誤発火を防ぐため、以下の論理積（AND条件）が成立したときのみ相転移（全捨て）を発火させます。

$$\Phi(\mathbf{x}_t) = \underbrace{\mathbb{I}\left(\mathcal{S}(t) > \theta_{\text{scout}}\right)}_{\text{1号: 哨戒（即時ノイズ検知）}} \land \underbrace{\mathbb{I}\left(C_{\text{struct}}(t) > \theta_{\text{struct}}\right)}_{\text{2号: 検証（時間持続性）}} \land \underbrace{\mathbb{I}\left(D_{\text{phase}}(t) > \min(\theta_{\text{phase}}, \theta_{\text{max}})\right)}_{\text{3号: 分析（位相幾何破綻）}}$$

* **不感症化（老害化）の防止**: 動的 3σ スケーリングに対し、絶対上限クリッピング $\theta_{\text{max}}$ を適用することで、統計的過剰適応による判定不能状態を原理的に回避します。

---

## ディレクトリ構成 (Repository Structure)

```text
shikiben-v2.5/
│
├── README.md                 # 本ドキュメント
├── LICENSE                   # ライセンス情報 (MIT)
├── requirements.txt          # 依存パッケージ
│
├── docs/                     # 詳細仕様書および論文ドキュメント
│   ├── spec_v2.5.md          # 識扁V2.5 最終理論仕様書
│   └── paper_extended.md     # 拡張論文ドキュメント（数理的証明）
│
├── src/                      # 識扁V2.5 コアモジュール
│   ├── __init__.py
│   ├── governance.py         # 3層合議裁定機構 & 動的 3σ 閾値計算器
│   ├── rotation.py           # 外部メタクロック & 3思想 Soft-mixing モジュール
│   ├── losses.py             # 3層分離損失関数 (Self / Ego_s / Ego_h)
│   └── model.py              # 統合モデル & 全捨て (K_detox) 実行器
│
└── experiments/              # 再現シミュレーション実験
    ├── run_simulation.py     # 相転移ダイナミクス再現スクリプト
    └── analyze_results.py    # ログ解析スクリプト
```
