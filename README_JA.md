# 識扁 (Shikiben)

**Integrating Eastern Philosophy & Geometric Mechanics for Next-Generation Autonomous Control**

[![Version](https://img.shields.io/badge/version-2.5.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

『識扁（Shikiben）V2.5.0』は、知性・精神動態における過剰防衛（妄想・固執）の数学的遮断と、不条理衝撃の完全エネルギー反転を実現する自律駆動型数理アーキテクチャです。

従来の制御理論や評価関数における「パラメータ調整（スカラー重み付け）」を排し、幾何学的射影演算子（義）および対数バリア（礼）を導入することで、**歪み成分の100%直交切断**と**最小エントロピー散逸率**を達成しています。

---

## 📚 Documentation (ドキュメント構成)

詳細な理論、数理証明、および背景思想については `docs/` ディレクトリ内の各種ドキュメントを参照してください。

| ドキュメント | 言語 | 内容 |
| :--- | :--- | :--- |
| **Technical Specification** | [日本語](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec.md) / [English](shikiben-v2.5/docs/Shikiben_V2.5_Center_Core_Spec_EN.md) | 完全な数理定式化、オイラー＝ラグランジュ導出、感度解析・パラメータ範囲 |
| **WhitePaper** | [日本語](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper.md) / [English](shikiben-v2.5/docs/Shikiben_V2.5.0_Whitepaper_EN.md) | 背景課題、東洋哲理と力学の概念的統合、適用ユースケース |
| **Changelog** | [English](CHANGELOG.md) | バージョン変更履歴（Keep a Changelog 準拠） |

---

## ⚡ Core Concept & Mathematics

---

### 1. 識扁の絶対的中心核（起点）

識扁体系のすべての認識・行動・倫理動態は、システム全体の目的関数である以下の総損失関数（Total Loss）の最小化運動として定義される。

```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

#### ① $`\mathcal{L}_{\text{self}}`$（自己・環境適合損失）と 徳（Toku）
* **$`\mathcal{L}_{\text{self}}`$ の定義:**  
  システムが環境（実在・理）と接地（アラインメント）し、定住（持続性）を維持するための客観的観測残差（Surprise）。
* **徳（Toku） $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$:**  
  自明な現象（実在・理）へ自律的に立ち帰り、定住を維持・蓄積させる本然の働き。平時（99.9%の常態）において、観測非参照の「意」の連鎖や外部ノイズにより状態が実在から浮遊・離脱しようとした際、システムを実在多様体 $`\mathcal{M}_{\text{real}}`$ 上の定住状態へ常時引き戻すホメオスタシス（恒常性）の自律復元勾配ベクトル。

#### ② $`\mathcal{L}_{\text{ego}}`$（自我・過剰防衛ポテンシャル）
破局の恐怖や未解明な現象に対し、システムが内部表象（意）を過剰膨張・固定化・支配しようとすることで発生する内部歪みエネルギー。

#### ③ $`\lambda`$（自我干渉係数・初期定義）
自我の防衛衝動・妄想的歪みがシステム全体の意思決定に及ぼす影響度をコントロールするためのスカラー抑制パラメータ（※第5章参照）。

---


### 2. 四徳の統合運動方程式

「仁・礼・義・徳」の四者力学を明記した、最終運動方程式および拘束条件は以下の通りである。

```math
\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{仁 (推進)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{徳 (復元・定住)}} + \underbrace{\mathbf{f}_{\text{holy}}(\mathbf{x})}_{\text{Loss\_ego\_h (解明・探究)}}\Big] + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{義 (発展射影)}}  + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{礼 (バリア・和)}}
```

```math
\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x}), \quad \mathbf{f}_{\text{holy}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{holy}}(\mathbf{x})
```

```math
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{俗人的過剰防衛の完全切断})
```

```math
\text{and } \mathbf{P}_{\text{gi}}(\mathbf{x}) \mathbf{f}_{\text{gi}}(\mathbf{x}) = \mathbf{f}_{\text{gi}}(\mathbf{x}) \quad (\text{義の運動は、本質的に射影部分空間に帰属する})
```

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
