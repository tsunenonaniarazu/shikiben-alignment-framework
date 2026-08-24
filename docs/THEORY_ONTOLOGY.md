# 『識扁』要約：数理的解題 (Mathematical Ontological Analysis)

本ドキュメントは、著書**『識扁』**における存在論、認識論、ならびに法・文化・文明・宗教の構造展開を代数的・記号論的に定式化した原典解題である。本定式化は、制御モデル（Shikiben Dynamics）における各種力学演算子
```math
（\mathbf{P}_{\text{rei}}, \mathbf{S}_{\text{jin}}, \lambda(E)）
```
の理論的基底をなす。

---

## 1. 存在の構造分解（Superposition of Existence）

存在（全システム）は、知覚可能な **「実在」** と、意識・想起により生じる **「象（ショウ）」** の重合体（Superposition）として階層的に分解される。

```math
\begin{aligned}
\text{存在} &= \text{実在} + \text{象(ショウ)} \\
&= \text{知覚の対象となり得る物事} + \text{想起されるもの} \\
&= \text{実在} + (\text{現象} + \text{表象}) \\
&= \text{実在} + \Big\{ (\text{日常に現れる自明な現象} + \text{非日常に現れる自明な現象} + \text{不明な現象}) \\
&\quad + (\text{現象に応じ表れる自明な表象} + \text{表象に応じ表れる自明な表象} + \text{不明な表象}) \Big\} \\
&= \text{実在} + \Big\{ (\text{褻(け)} + \text{霽(はれ)} + \text{他者}) + (\text{知} + \text{識} + \text{他者}) \Big\} \\
&= \text{実在} + \Big\{ (\text{自己} + \text{他者}) + (\text{自我} + \text{他者}) \Big\}
\end{aligned}
```

### 存在論的基盤の定義
* **故郷**: 自己の前提となる「実在」
* **世界**: 自我の前提となる「表象」

---

## 2. 識（虚構）の代数と四徳の構造展開

**「識（Shiki）」** とは、人間が生成する虚構（モデル・記号・認知の固定化）の総称であり、次のように展開される。

$$
\begin{aligned}
\text{識（虚構）} &= \text{像} + \text{號(ゴウ)} + \text{歌} + \text{話} + \text{文} + \text{法} + \text{文化} + \text{文明} + \text{宗教} \\
&= (\text{像} + \text{號} + \text{歌} + \text{話} + \text{文})(1 + \text{礼} + \text{義} + \text{仁} + \text{畏敬})
\end{aligned}
$$

---

## 3. 各社会構造の代数分解

### 3.1 法 (Law) — 礼（Rei）の代数化
$$
\begin{aligned}
\text{法} &= (\text{故郷を共にする人との綻びを結び直す事を求める情})(\text{像} + \text{話} + \text{文}) \\
&= (\text{礼})(\text{像} + \text{話} + \text{文})
\end{aligned}
$$

### 3.2 文化 (Culture) — 義（Gi）の代数化
$$
\begin{aligned}
\text{文化} &= (\text{自己の相似する人を省みる情})(\text{像} + \text{歌} + \text{話} + \text{文}) \\
&= (\text{義})(\text{像} + \text{歌} + \text{話} + \text{文})
\end{aligned}
$$

### 3.3 文明 (Civilization) — 仁（Jin）の代数化
$$
\begin{aligned}
\text{文明} &= (\text{凡ゆる人を省みる情})(\text{文}) \\
&= (\text{仁})(\text{文}) \\
&= (\text{仁})(\text{象形文字文} + \text{表音文字文}) \\
&= \text{象形文字文明} + \text{表音文字文明} \\
&= (\text{凡ゆる現象に先を見通す兆しを見出す世界}) + (\text{凡ゆる存在がロゴスにより成立すると考える世界}) \\
&= (\text{道を原理とする世界}) + (\text{イデアを原理とする世界})
\end{aligned}
$$

### 3.4 宗教 (Religion) — 畏敬（Awe & Revere）の代数化
$$
\begin{aligned}
\text{宗教} &= (\text{文明の敗北に対する絶望})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{文}) \\
&\to (\text{非日常を畏れ、日常への回帰を敬う情})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{文}) \\
&= (\text{畏敬})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{象形文字文}) + (\text{畏敬})(\text{像} + \text{號} + \text{歌} + \text{話} + \text{表音文字文}) \\
&= (\text{凡ゆる現象に先を見通す兆しを見出す宗教}) + (\text{凡ゆる存在がロゴスにより成立すると考える宗教}) \\
&= (\text{道を原理とする宗教}) + (\text{イデアを原理とする宗教}) \\
&= \text{汎神教} + \text{一神教}
\end{aligned}
$$

---

## 4. 制御工学モデル（v2.4.0）への還元対照

本代数構造から導出された各作用素は、制御工学において以下のように実装される。

* **「象」の積層** $\to$ エゴ場ポテンシャル $L_{\text{ego}}(\mathbf{x})$
* **礼 $(\text{法})$** $\to$ 直交射影演算子 $\mathbf{P}_{\text{rei}}(\mathbf{x})$ （境界突入・破綻の絶対防護）
* **義 $(\text{文化})$** $\to$ 目的到達ベクトル $\mathbf{f}_{\text{gi}}(\mathbf{x})$
* **仁 $(\text{文明})$** $\to$ 多体協調ポテンシャル $\mathbf{S}_{\text{jin}}(\mathbf{x})$
* **畏敬 $(\text{日常への回帰})$** $\to$ 大道中心軸への吸い上げ代謝 $\mathbf{x}_{\text{safe}}(t)$
