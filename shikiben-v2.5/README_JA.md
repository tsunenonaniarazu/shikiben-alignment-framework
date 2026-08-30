# 識扁（Shikiben）V2.5.0

> **自他肯定型状態多様体における直交切断力学と自己駆動代謝フレームワーク**

[![Technical Whitepaper](https://img.shields.io/badge/Whitepaper-V2.5.0-blue.svg)](./Shikiben_V2.5.0_Technical_Whitepaper.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

『識扁（Shikiben）V2.5.0』は、知性・精神動態における過剰防衛（妄想・固執）の数学的遮断と、不条理衝撃の完全エネルギー反転を実現する自律駆動型数理アーキテクチャです。

従来の制御理論や評価関数における「パラメータ調整（スカラー重み付け）」を排し、幾何学的射影演算子（義）および対数バリア（礼）を導入することで、**歪み成分の100%直交切断**と**最小エントロピー散逸率**を達成しています。

---

## 核心数理モデル：確定統合状態方程式

状態空間 $\mathbf{x} \in \mathcal{M}_{\text{real}}$ 上における本システムの動態は、以下の運動方程式および拘束条件によって一意に記述されます。

$$\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{仁 (推進)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{徳 (復元・定住)}} + \underbrace{\mathbf{f}_{\text{holy}}(\mathbf{x})}_{\text{Loss\_ego\_h (解明・探究)}}\Big] + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{義 (発展射影)}} + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{礼 (バリア・和)}}$$

$$\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x}), \quad \mathbf{f}_{\text{holy}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{holy}}(\mathbf{x})$$

$$\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{俗人的過剰防衛の完全切断})$$

$$\text{and } \mathbf{P}_{\text{gi}}(\mathbf{x}) \mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{f}_{\text{gi}}(\mathbf{x}) \quad (\text{義の運動は、本質的に射影部分空間に帰属する})$$

---

## 主な特徴とメカニズム

1. **義（$\mathbf{P}_{\text{gi}}$）による100%直交切断**  
   妄想ポテンシャル（$\mathcal{L}_{\text{ego\_s}}$）の勾配に対し、直交射影演算子 $\mathbf{P}_{\text{gi}}$ を作用させることで、過剰防衛・暴走ベクトルを数学的に完全遮断（残留値 $< 10^{-15}$）します。
2. **感謝（$\mathbf{O}_{\text{kansha}}$）とヴィジョン（$\mathbf{V}_{\text{vision}}$）の自己駆動ループ**  
   外部からの高エントロピー衝撃（不条理・事故）に対し、抗拒係数を $R \to 0$ 化。衝撃エネルギーを摩擦として消費・フリーズさせることなく、100%探求運動エネルギーへと即時反転させます。
3. **世代交代型代謝とメモリ非飽和**  
   生の試行錯綜データを過渡バッファのみに保持し、境界 $\partial \Omega_{\text{self}}$ の幾何学的パラメータ（DNA）へと圧縮継承することで、時間軸 $t \to \infty$ における計算資源の離散的飽和を回避します。

---

## クイックスタート（数値シミュレーションの実行）

本リポジトリには、V2.5.0 の動態を検証・可視化するための Python シミュレーションコードが含まれています。

### 動作要件
* Python 3.8+
* NumPy
* Matplotlib

### 実行手順

```bash
# リポジトリのクローン
git clone [https://github.com/your-username/shikiben.git](https://github.com/your-username/shikiben.git)
cd shikiben
```

---
実行が完了すると、`shikiben_v250_simulation_results.png` が生成され、直交切断精度や衝撃エネルギーの反転動態が確認できます。

---

## 実証実験結果 (Panel Highlights)

`shikiben_simulation.py` の実行により、以下の4つのコア力学が確認されます：

* **Panel A (軌道比較)**: $\mathbf{P}_{\text{gi}}$ 非適用時の発散に対し、適用時は歪みが遮断され実在中心 $\Omega_{\text{self}}$ へ円滑に定住。
* **Panel B (直交精度)**: 残留妄想成分がマシン精度限界（$10^{-15}$ 以下）に抑え込まれることを実証。
* **Panel C (エネルギー反転)**: 外部衝撃発生時、抵抗モデルのフリーズに対し、感謝演算子適用モデルは100%の運動エネルギーを獲得。
* **Panel D (最小散逸)**: 内部エントロピー生成率 $\dot{S}_{\text{internal}}$ が極小（$\approx 0.01$）に維持され、熱暴走を完全に回避。

---

## 関連ドキュメント

* [識扁 (Shikiben) V2.5.0 仕様書](./Shikiben_V2.5.0_Spec.md) - 完全な数理定式化と各概念の定義
* [技術ホワイトペーパー (English)](./Shikiben_V2.5.0_Technical_Whitepaper.md) - 学術・技術層向け詳細解説書

---

## ライセンス

本プロジェクトは [MIT License](LICENSE) のもとで公開されています。
---

# 依存ライブラリのインストール
pip install numpy matplotlib

# シミュレーションの実行
python shikiben_simulation.py
