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
* **大道 ($`\mathbf{g}_{\text{Taidou}}`$ & $`\mathbf{x}_{\text{safe}}`$):** 歪みを吸い上げて自己更新する安全基準軸と復元勾配。

---

## 🚀 Getting Started (シミュレーション実行)

Python環境で本数理モデルの挙動および幾何学射影の動作を確認できます。

### 前提条件
* Python 3.8+
* NumPy, Matplotlib

### 実行手順

```bash
# リポジトリのクローン
# Clone the repository
git clone [https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git]
(https://github.com/tsunenonaniarazu/shikiben-alignment-framework.git)
cd shikiben-v2.5/simulations/

# シミュレーションの実行
shikiben_simulation_01.py
shikiben_simulation_02.py

```

---

# 識扁（Shikihen）

## 概要（Overview）
『識扁（しきへん）』は、現象と表象、自己と自我、そして故郷と世界の対比から、人間の認知・文化・法・宗教の発生と構造を記述した思想体系および著作です。


---

## 本文：『識扁 序』（Original Text）

> <ruby>慣<rt>な</rt></ruby>れ<ruby>親<rt>した</rt></ruby>しんだものとして<ruby>相<rt>ソウ</rt></ruby><ruby>起<rt>キ</rt></ruby>される<ruby>現<rt>ゲン</rt></ruby><ruby>象<rt>ショウ</rt></ruby>を、<ruby>自<rt>ジ</rt></ruby><ruby>己<rt>コ</rt></ruby>とする。それ以外の現象を、<ruby>他<rt>タ</rt></ruby><ruby>者<rt>シャ</rt></ruby>とする。  
> 慣れ親しんだものとして想起される<ruby>表<rt>ヒョウ</rt></ruby><ruby>象<rt>ショウ</rt></ruby>を、<ruby>自<rt>ジ</rt></ruby><ruby>我<rt>ガ</rt></ruby>とする。それ以外の表象を、他者とする。  
>  
> 自己を、<ruby>日<rt>ニチ</rt></ruby><ruby>常<rt>ジョウ</rt></ruby>と<ruby>非<rt>ヒ</rt></ruby>日常に<ruby>分<rt>わ</rt></ruby>け、<ruby>前<rt>ゼン</rt></ruby><ruby>者<rt>シャ</rt></ruby>を<ruby>褻<rt>け</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>び、<ruby>後<rt>コウ</rt></ruby><ruby>者<rt>シャ</rt></ruby>を<ruby>霽<rt>はれ</rt></ruby>と呼ぶ。  
> 褻に<ruby>見<rt>み</rt></ruby>出される<ruby>働<rt>はたら</rt></ruby>きを<ruby>道<rt>みち</rt></ruby>と呼び、それに応ずる<ruby>在<rt>あ</rt></ruby>り<ruby>方<rt>かた</rt></ruby>を<ruby>徳<rt>トク</rt></ruby>と呼ぶ。  
> 霽に見出される働きを<ruby>神<rt>シン</rt></ruby>と呼び、それに応ずる在り方を<ruby>畏<rt>イ</rt></ruby><ruby>敬<rt>ケイ</rt></ruby>と呼ぶ。  
>  
> 自我を、現象に応じ想起される<ruby>自<rt>ジ</rt></ruby><ruby>明<rt>メイ</rt></ruby>な表象と、表象に応じ想起される自明な表象に分け、前者を知と呼び、後者を<ruby>識<rt>シキ</rt></ruby>と呼ぶ。  
> <ruby>知<rt>チ</rt></ruby>に見出される働きを<ruby>理<rt>リ</rt></ruby>と呼び、それに応ずる在り方を<ruby>聖<rt>セイ</rt></ruby>と呼ぶ。  
> 識に見出される働きを<ruby>意<rt>イ</rt></ruby>と呼び、それに応ずる在り方を<ruby>欲<rt>ヨク</rt></ruby>と呼ぶ。  
>  
> 現象は、<ruby>実<rt>ジツ</rt></ruby><ruby>在<rt>ザイ</rt></ruby>を<ruby>知<rt>チ</rt></ruby><ruby>覚<rt>カク</rt></ruby>することにより想起され<ruby>現<rt>あらわ</rt></ruby>れる。  
> 自己の応ずる実在を<ruby>総<rt>ソウ</rt></ruby>じて<ruby>故<rt>コ</rt></ruby><ruby>郷<rt>キョウ</rt></ruby>と呼ぶ。  
> 表象は、<ruby>象<rt>ショウ</rt></ruby>の想起に応じ想起され表れる。  
> 自我の応ずる象を総じて<ruby>世<rt>セ</rt></ruby><ruby>界<rt>カイ</rt></ruby>と呼ぶ。  
>  
> 故郷と世界が<ruby>相<rt>ソウ</rt></ruby><ruby>似<rt>ジ</rt></ruby>する<ruby>関<rt>カン</rt></ruby><ruby>係<rt>ケイ</rt></ruby>を、<ruby>大<rt>タイ</rt></ruby><ruby>道<rt>ドウ</rt></ruby>と呼ぶ。  
> 故郷と世界が<ruby>対<rt>タイ</rt></ruby><ruby>峙<rt>ジ</rt></ruby>する関係を、<ruby>大<rt>タイ</rt></ruby><ruby>偽<rt>ギ</rt></ruby>と呼ぶ。  
> 大偽は故郷の<ruby>喪<rt>ソウ</rt></ruby><ruby>失<rt>シツ</rt></ruby>より<ruby>生<rt>ショウ</rt></ruby>じる。これを<ruby>災<rt>サイ</rt></ruby>と呼ぶ。  
> 災より<ruby>道<rt>ドウ</rt></ruby><ruby>徳<rt>トク</rt></ruby>の<ruby>変<rt>ヘン</rt></ruby><ruby>異<rt>イ</rt></ruby>が生じる。  
>  
> 故郷の喪失に対し、<ruby>嘆<rt>なげ</rt></ruby>き<ruby>悲<rt>かな</rt></ruby>しみ、故郷を想起することによりこれに応ずる。これを<ruby>號<rt>ゴウ</rt></ruby>と呼ぶ。  
> ここで、同じ嘆き悲しむ人を<ruby>省<rt>ひとかえり</rt></ruby>みる<ruby>情<rt>ジョウ</rt></ruby>を知る。これを<ruby>仁<rt>ジン</rt></ruby>と呼ぶ。  
> <ruby>或<rt>あるい</rt></ruby>は、<ruby>象<rt>ゾウ</rt></ruby>を作り、<ruby>慰<rt>なぐさ</rt></ruby>めとする。  
> 號は<ruby>歌<rt>カ</rt></ruby>に<ruby>転<rt>テン</rt></ruby>じ、故郷を<ruby>任<rt>ニン</rt></ruby><ruby>意<rt>イ</rt></ruby>に想起する<ruby>術<rt>すべ</rt></ruby>を知る。ここで、故郷を<ruby>共<rt>とも</rt></ruby>にする人を省みる情を知る。これを<ruby>義<rt>ギ</rt></ruby>と呼ぶ。  
> 歌は<ruby>話<rt>タニン</rt></ruby>に転じ、自我が<ruby>他<rt>もと</rt></ruby><ruby>人<rt>レイ</rt></ruby>と相違する事を知る。ここで、他人との和を求める情を知る。これを礼と呼ぶ。  
>  
> 話と像は<ruby>文<rt>ブン</rt></ruby>に転じ、自我の他者としての<ruby>現<rt>あらわ</rt></ruby>れが<ruby>明<rt>メイ</rt></ruby><ruby>示<rt>ジ</rt></ruby>される。これは、<ruby>争<rt>あらそ</rt></ruby>いの<ruby>本<rt>もと</rt></ruby>となる。  
> ここで、情に応じ、文は制約される。  
> 礼に応じ、文は制約され、<ruby>法<rt>ホウ</rt></ruby>となる。  
> 義に応じ、文は制約され、<ruby>文<rt>ブン</rt></ruby><ruby>化<rt>カ</rt></ruby>となる。  
> 仁に応じ、文は制約され、<ruby>文<rt>ブン</rt></ruby><ruby>明<rt>メイ</rt></ruby>となる。  
> 畏敬に応じ、文は制約され、<ruby>修<rt>シュウ</rt></ruby><ruby>教<rt>キョウ</rt></ruby>となる。  
>  
> 像、號、歌、話、文、法、文化、文明、宗教は、それぞれ世界として故郷と対峙する。  
>  
> 故郷の<ruby>側<rt>がわ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つ者は、現象に応ずる知に<ruby>随<rt>したが</rt></ruby>う。故に、<ruby>聖<rt>セイ</rt></ruby><ruby>人<rt>ジン</rt></ruby>と呼ぶ。  
> 世界の側に立つ者は、世界に応ずる識に<ruby>遵<rt>したが</rt></ruby>う。故に、<ruby>俗<rt>ゾク</rt></ruby><ruby>人<rt>ジン</rt></ruby>と呼ぶ。  
> 聖人は、像、號、歌、話、文、法、文化、文明、宗教を否定し、<ruby>隠<rt>イン</rt></ruby><ruby>遁<rt>トン</rt></ruby>する。

---

##『識扁』要約・概念構造（Summary & Conceptual Structure）

### 1. 基礎概念の対比軸
| 分類 | 領域 / 構成要素 | 見出される働き | 応ずる在り方 / 実存 |
| :--- | :--- | :--- | :--- |
| **自己（現象）** | 褻（日常） | 道 | 徳 |
| | 霽（非日常） | 神 | 畏敬 |
| **自我（表象）** | 知（現象に応じた想起） | 理 | 聖 |
| | 識（表象に応じた想起） | 意 | 欲 |

### 2. 喪失と転変（文・制約の発生）
故郷の喪失（災）から始まり、感情と表現の転回を経て社会規範・文化へと昇華・制約されるプロセス：
1. **號（嘆き）** → 【仁】同じ嘆きを省みる情 → 文明への制約
2. **歌（任意想起）** → 【義】故郷を共にする人を省みる情 → 文化への制約
3. **話（他者相違）** → 【礼】他人との和を求める情 → 法への制約
4. **像（慰め）** ＋ **話** → **文（表現）** → 争いの本
5. **畏敬** → 宗教への制約

### 3. 聖人と俗人
* **聖人:** 故郷の側に立ち、現象に応ずる「知」に随い、世界（文化・法・宗教等）を否定して隠遁する。
* **俗人:** 世界の側に立ち、世界に応ずる「識」に遵う。
