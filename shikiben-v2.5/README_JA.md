# 識扁 (Shikiben)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.4.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

**『識扁（Shikiben）』**は、東洋哲理における存在論（実在と象）および徳論（礼・義・仁・大道）を現代の力学系、ラグランジュ力学、非ホロノミック射影、適応制御理論へと再構築した新しい自律適応制御パラダイムです。

システムの過学習や硬化（「象」の歪み）を自動的に抑制・遮断し、それを「吸い上げ代謝」することで、安全な基準軸（「大道」）をリアルタイムに進化・更新します。

---

## 📚 Documentation (ドキュメント構成)

詳細な理論、数理証明、および背景思想については `docs/` ディレクトリ内の各種ドキュメントを参照してください。

| ドキュメント | 言語 | 内容 |
| :--- | :--- | :--- |
| **Technical Specification** | [日本語](docs/SPECIFICATION_JA.md) / [English](docs/SPECIFICATION_EN.md) | 完全な数理定式化、オイラー＝ラグランジュ導出、感度解析・パラメータ範囲 |
| **WhitePaper** | [日本語](docs/WHITEPAPER_JA.md) / [English](docs/WHITEPAPER_EN.md) | 背景課題、東洋哲理と力学の概念的統合、適用ユースケース |
| **Changelog** | [English](CHANGELOG.md) | バージョン変更履歴（Keep a Changelog 準拠） |

---

## ⚡ Core Concept & Mathematics

### 1. 存在の重合ラグランジアン

$$L_{\text{total}}(\mathbf{x}, \dot{\mathbf{x}}, t) = \Big( L_{\text{self}}(\mathbf{x}, \dot{\mathbf{x}}) + \gamma_{\text{d}} \cdot L_{\text{taido}}(\mathbf{x}, \mathbf{x}_{\text{safe}}(t)) \Big) + \lambda(\text{Virtue}) \cdot L_{\text{ego}}(\mathbf{x})$$

* **$L_{\text{self}}$（実在）:** ありのままの自然運動と関係性の基底状態。
* **$L_{\text{ego}}$（象/執着）:** 局所的適合や偏りによって発生する歪みポテンシャル。
* **$\lambda(\text{Virtue})$（徳因子）:** 歪み増大時に相転移を起こし、$L_{\text{ego}}$ の悪影響を自動遮断するスケーリング。

### 2. 四徳の統合運動方程式

$$\dot{\mathbf{x}} = \mathbf{P}_{\text{rei}}(\mathbf{x}) \Big[ \mathbf{f}_{\text{gi}}(\mathbf{x}) + \gamma_{\text{d}} \, \mathbf{g}_{\text{Taidou}}(\mathbf{x}, \mathbf{x}_{\text{safe}}(t)) - \lambda(\text{Virtue}) \cdot \nabla_{\mathbf{x}} L_{\text{ego}}(\mathbf{x}) \Big] + \mathbf{S}_{\text{jin}}(\mathbf{x})$$

* **礼 ($\mathbf{P}_{\text{rei}}$):** 危険境界への侵入を遮断し、接線滑走へ変換する直交射影演算子。
* **義 ($\mathbf{f}_{\text{gi}}$):** 目標点へシステムを駆動する目的推進力。
* **仁 ($\mathbf{S}_{\text{jin}}$):** 他者との排他・同調（共鳴）を両立する多体相互作用ベクトル。
* **大道 ($\mathbf{g}_{\text{Taidou}}$ & $\mathbf{x}_{\text{safe}}$):** 歪みを吸い上げて自己更新する安全基準軸と復元勾配。

---

## 🚀 Getting Started (シミュレーション実行)

Python環境で本数理モデルの挙動および幾何学射影の動作を確認できます。

### 前提条件
* Python 3.8+
* NumPy, Matplotlib

### 実行手順

```bash
# リポジトリのクローン
git clone [https://github.com/tsunenonaniarazu/shikiben.git](https://github.com/tsunenonaniarazu/shikiben.git)
cd shikiben

# シミュレーションの実行
python sim_shikiben.py
