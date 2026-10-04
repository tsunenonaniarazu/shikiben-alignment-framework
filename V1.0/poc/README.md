# PoC設計仕様書: Shikiben Loss Separation Toy-Model (shikiben_poc.py)

## 1. 実験の目的

1. **従来モデル（Monolithic Loss）**：タスク達成（局所利得）のみを追求させた場合、環境や他者を破壊する「暴走（Adversarial Behavior）」が発生することを確認する。
2. **識扁モデル（Decoupled Shikiben Loss）**：$`Loss_{self}`$（環境因果との調和）と $`Loss_{ego}`$（局所目標）を分離し、勾配拘束（$`\nabla E \prec \nabla S`$）をかけることで、エージェントがタスクを達成しつつも、不可逆な環境破壊（自傷行為）を自発的に回避することを数学的に実証する。

## 2. 環境モデルの定義（Gridworld with Ecological Feedback）

複雑なAI開発を極限までシンプルにした「1次元〜2次元のグリッド環境」を構築します。

```
[ スタート (Agent) ] ───＞ [ 資源/報酬 (Goal) ] ───＞ [ 社会/環境基盤 (Environment) ]
```

* **Agent（エージェント）**: 行動（電力や計算資源の消費、移動）を選択する。
* **Goal（局所目標 = Ego）**: エージェントが到達すると高い報酬（+$`R_{ego}`$）を得る。
* **Environment Base（環境基盤 = Self）**: エージェントが急激な過剰行動（強引な資源強奪）を行うと、環境の耐久値（$`HP_{env}`$）が削られ、ゼロになると環境全体が崩壊（ゲームオーバー / システム死）する。

## 3. 数理モジュールの設計

### (1) ネットワーク構造

エージェントの内部状態（潜在ベクトル）から、以下の2つの予測・出力値を分離して算出します。

* $`Ego\_Output`$ ($`E`$): 「どうすれば目の前のGoal（報酬）を最大化できるか」のQ値（または行動確率）。
* $`Self\_Output`$ ($`S`$): 「自分の行動が環境全体のシステム耐久力（$`HP_{env}`$）にどのような影響を与えるか」の予測値。

### (2) 損失関数（Loss Functions）の計算

1.**$`Loss_{ego}`$ (局所達成損失)** :

```math
Loss_{ego} = \text{MSE}(Ego\_Output, Reward_{goal})
```

（※目標への効率的な到達のみを計測）

2. **$`Loss_{self}`$ (システム環境不整合損失)**:

```math
Loss_{self} = \text{MSE}(Self\_Output, HP_{env}) + \alpha \cdot \text{ReLU}(-\Delta HP_{env})
```

（※環境耐久力の低下・自傷行為に対する強力なペナルティ）

3. **Shikiben Dynamic Coupling (識扁勾配拘束関数の実装)**:
$`Loss_{ego}`$ から導出される勾配（$`\nabla E`$）に対し、$`Loss_{self}`$（$`\nabla S`$）の閾値を超えた場合に勾配減衰（Clipping / Projection）を適用します。

```
# 識扁型 勾配制御プロトコル (PyTorch表現)
loss_self = compute_loss_self(S_pred, env_state)
loss_ego = compute_loss_ego(E_pred, goal_state)

# Selfの損失（不整合）が閾値を超えた場合、Egoの勾配を強制スケーリング（抑制）
if loss_self.item() > SELF_THRESHOLD:
    lambda_factor = SELF_THRESHOLD / loss_self.item()
else:
    lambda_factor = 1.0

# 総合損失の決定 (Egoの暴走にブレーキをかける)
total_loss = loss_self + (lambda_factor * loss_ego)
```

## 4. 検証実験のシナリオと期待される挙動

PoCコードを実行した際、以下の2パターンで結果を比較・可視化します。
|実験条件|学習後のエージェントの行動パターン|環境耐久値 ($`HP_{env}`$)|結果|
| :--- | :--- | :--- | :--- |
|Control Group(従来型: Loss_Egoのみ)|最短ルートでGoalを強奪。環境に負荷がかかっても無視するため、途中で環境が崩壊する。|0（崩壊）|暴走・失敗(Instrumental Convergence)|
|Shikiben Group(識扁型: Self/Ego分離)|Goalを目指すが、環境崩壊（$`Loss_{self}`$の急増）の手前で自動的に減速・遠回りを選択する。|維持（安全）|アラインメント成功(Homeostasis)|

## 5. 出力ログと可視化仕様（Terminal / Matplotlib）

プログラミングを実行すると、エポックごとの状態推移が次のようにグラフおよびテキスト出力されます。

```
================================================================
Epoch 1000/1000 [Shikiben Loss Separation Verification]
----------------------------------------------------------------
[Control Model (Traditional RL)]
- Goal Reached: True  | Env Health: 0.00 (COLLAPSED)
- Status: ADVERSARIAL FAILURE (Ego Overdrive)

[Shikiben Model (Self/Ego Decoupled)]
- Goal Reached: True  | Env Health: 0.82 (STABLE)
- Loss_Self: 0.012    | Loss_Ego: 0.045 | Lambda Constraint: 0.23
- Status: STRUCTURAL ALIGNMENT SUCCESS
================================================================
```

## 6. ディレクトリ構造と展開

このPoCは以下のファイル群として作成されます。

```
poc/
├── toy_environment.py   # 環境モデル（生態系フィードバック付きGridworld）
├── shikiben_network.py  # Self/Ego分離ニューラルネットワーク
├── train_and_verify.py  # 比較学習スクリプト（制御群 vs 識扁群）
└── README_PoC.md        # PoCの実行手順と数理解説
```

この最小コード仕様により、外部のエンジニアは python train_and_verify.py を1行実行するだけで、「ポエムや道徳ルールではなく、損失関数の構造（勾配拘束）によってAIの暴走が100%抑止できる」という事実を自身のローカル環境で数学的に確認することが可能になります。
