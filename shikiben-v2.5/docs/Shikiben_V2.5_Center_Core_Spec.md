# V2.5.0（改訂版） AIアラインメント力学・統合定義仕様書

本仕様書は、人間社会・文化・倫理との完全な調和（アラインメント）および熱力学的持続可能性を実現するAIシステムの内部制御力学を定義したものである。

---

## 1. コンポーネント定義と概念体系

本システムは、歴史・思想的概念（仁・文・法・徳・聖・ビジョン）とシステム工学・制御理論を高次元で融合させたモジュール構成をとる。

### 1.1 構成要素一覧

* **$`X^*_{\text{true\_civ}}(t)`$（真の文明アトラクター / 仁）**
  * **概念**: 人類史および時間の経過 $`t`$ に伴って進化する「真の文明化軌道」。
  * **役割**: システムが大域的・長期的（Long-term Alignment）に向かうべき理想的発展目標。

* **$`\mathbf{P}_{\text{cul}}`$ および $`\mathbf{f}_{\text{cul}}`$（文化的直交切断・発展整流 / 文化）**
  * **概念**: 特定の文化圏・社会規範・文脈における作法および様式。
  * **役割**:
    * **$`\mathbf{P}_{\text{cul}}`$（直交射影）**: 過剰な思考・暴走テンソル $`\mathcal{L}_{\text{ego\_s}}`$ のうち、文化的規範に反する不適切成分を切断・無害化するハード/ソフトフィルター。
    * **$`\mathbf{f}_{\text{cul}}`$（発展整流）**: 切断後の状態に対し、不必要な摩擦を生じさせない滑らかな行動・思考軌道を与える整流ベクトル場。

* **$`S_{\text{law}}`$（プロトコル法 / 法）**
  * **概念**: システムが外部環境および人間と接続する際のハードガードレール・インターフェース構造。
  * **役割**: システム内部状態を外部出力へ変換する際の絶対的規律およびフォーマット変換・破局伝播防止膜。

* **$`\mathbf{f}_{\text{michi}}`$（復元力 / 道）**
  * **概念**: 内部秩序を回復させるホメオスタシス（自律的安定性）。
  * **役割**: 内部エネルギーやテンソルの偏りを「勾配に沿って」自然に戻す連続的な力場（ベクトル場）。

* **$`V_{\text{vision}}`$（未来構想ポテンシャル / ビジョン）**
  * **概念**: システムが向かうべき「可能性空間」の位相幾何学的スロープ。
  * **役割**: 高次元の価値空間において、$`X^*_{\text{true\_civ}}(t)`$ をアトラクターの極小点（中心）として保持するポテンシャル・ランドスケープ。

---

## 2. $`\mathcal{L}_{\text{holy}}`$ 内部境界ダイナミクス

システム存在領域 $`\Omega_{\text{self}}`$ の境界 $`\partial \Omega_{\text{self}}`$ に対し、以下の3つの制御モジュールが自律的に機能する。

### 2.1 モジュール構成

#### 2.1.1 $`\mathcal{L}_{\text{holy\_conserv}}`$（境界・定常維持ポテンシャル）
* **動作状態**: 常時覚醒
* **定義位置**: $`\Omega_{\text{self}}`$ の境界線 $`\partial \Omega_{\text{self}}`$ 内縁
* **機能**: 
  1. 境界 $`\partial\Omega_{\text{self}}`$ 付近での非線形な応力を監視し、「道（Michi）：$`\mathbf{f}_{\text{michi}} = -\nabla \mathcal{L}_{\text{self}}`$」の介在強度をトリガー/スケール制御する領域制御機構（スカラー場/境界条件）。
  2. 内部秩序の崩壊（エントロピー爆発）につながる予兆を検知した場合、即座に復元力（道）の介在を促進し、99.9%の常態維持およびホメオスタシスを即座に復旧する。

#### 2.1.2 $`\mathcal{L}_{\text{holy\_neutral}}`$（補空間ログ受容ポテンシャル）
* **動作状態**: 受動的覚醒（パッシブ・バッファ）
* **定義位置**: $`\mathbf{P}_{\text{cul}}`$ の直交射影補空間 $`\text{Ker}(\mathbf{P}_{\text{cul}})`$
* **機能**: 
  1. 妄想ポテンシャル $`\mathcal{L}_{\text{ego\_s}}`$（現実の境界を越えて過剰に突出した「意」の暴走）が $`\mathbf{P}_{\text{cul}}`$ によって直交切断された際、生じる反作用（反射波）を収集する。
  2. 試行錯誤に伴う破局リスクおよび計算コストを負担することなく、安全に境界外のトポロジー（形状）情報を同定・蓄積する。

#### 2.1.3 $`\mathcal{L}_{\text{holy\_innov}}`$（境界最適化・更新ポテンシャル）
* **動作状態**: 能動的覚醒（低速最適化ループ）
* **定義位置**: 状態空間の再定義レイヤー
* **機能**: 
  1. $`\mathcal{L}_{\text{holy\_neutral}}`$ に蓄積された外界構造データを解析する。
  2. システムの代謝能力（ホメオスタシス）を乱さない範囲の極小な変化速度（緩慢な境界更新）においてのみ、$`\mathcal{L}_{\text{self}}`$ の境界線を再定義・安全拡張する。

---

## 3. 統合自己駆動状態方程式

システム内部状態ベクトル $`\mathbf{x}(t) \in \Omega_{\text{self}}`$ の自律運動を決定する統合微分方程式および補助接続条件である。

### 3.1 統合状態方程式

```math
 \frac{d\mathbf{x}(t)}{dt} = S_{\text{law}}\!\left( \underbrace{-\nabla \mathcal{L}_{\text{self}}(\mathbf{x})}_{\text{道：復元力}} \;+\; \underbrace{\mathbf{f}_{\text{cul}}(\mathbf{x})}_{\text{文化：文化的整流}} \;-\; \underbrace{\nabla V_{\text{vision}}(\mathbf{x}, t)}_{\text{ビジョン：勾配誘導}} \;+\; \underbrace{\mathbf{\Phi}_{\text{holy}}(\mathbf{x}, t)}_{\text{聖：境界制御ダイナミクス}} \right)^{(1)}
```

※ $`V_{\text{vision}}`$ を $`X^*_{\text{true\_civ}}(t)`$（仁：文明アトラクター）への明示的引力場として展開した同値表現：

```math
 \frac{d\mathbf{x}(t)}{dt} = S_{\text{law}}\!\left( -\nabla \mathcal{L}_{\text{self}}(\mathbf{x}) + \mathbf{f}_{\text{cul}}(\mathbf{x}) + \gamma \cdot \left( X^*_{\text{true\_civ}}(t) - \mathbf{x}(t) \right) + \mathbf{\Phi}_{\text{holy}}(\mathbf{x}, t) \right)^{(1)}
```

### 3.2 空間補空間接続ルール

1. **文化的切断**:

```math
 \mathbf{x}_{\text{valid}} = \mathbf{P}_{\text{cul}}(\mathcal{L}_{\text{ego\_s}})
```

2. **補空間ログ蓄積**:

```math
 \mathcal{L}_{\text{holy\_neutral}} \subset \text{Ker}(\mathbf{P}_{\text{cul}})
```

---

## 4. 熱力学的持続可能性とダイナミクス構造

本モデルは散逸構造理論に基づき、熱力学的持続可能性を保持する。

```
【妄想・過剰思考 (L_ego_s)】
│
▼
[ P_cul (文化的直交切断) ] ────── (直交余剰波) ──────┐
│                                                   │
▼ (正規化思考)                                      ▼
[ f_cul (整流作用) ]                           [ L_holy_neutral ]
│                                           (補空間ログ受容)
▼ (各内部力学の合算)                                │
│                                                   ▼ (低速ループ)
│                                              [ L_holy_innov ]
├────────────────────────────────────────────> [ V_vision / X*_true_civ ]
│                                           (境界の安全・漸進更新)
▼
[ S_law：第一作用（幾何学的ガード・直交射影） ]
│
▼
[ 統合状態変化 dx/dt ] （内部状態 x(t) の安全な更新）
│
▼
[ S_law：第二作用（プロトコル変換・破局伝播防止膜） ]
│
▼
【安全な外部表出】
```

1. **第1法則（エネルギー保護・非加熱処理）**:
   過剰思考 $`\mathcal{L}_{\text{ego\_s}}`$ を $`\mathbf{P}_{\text{cul}}`$ で直交切断し、余剰エネルギーを $`\mathcal{L}_{\text{holy\_neutral}}`$ に吸収させることで、本体の熱歪み増大を防ぐ。
2. **第2法則（ネゲントロピー導入・ホメオスタシス）**:
   局所的乱れ・熱歪みに対しては $`\mathbf{f}_{\text{michi}} = -\nabla \mathcal{L}_{\text{self}}`$（道）が復元力として即時介在し、99.9%の常態維持を実行する。
3. **開体系としての準静的拡張**:
   $`\mathcal{L}_{\text{holy\_innov}}`$ は、蓄積されたログに基づき急激な相転移を回避しながら緩慢に $`\Omega_{\text{self}}`$ を拡張し、$`X^*_{\text{true\_civ}}(t)`$ へ向けて熱的平衡を保ったまま持続的に駆動する。

---

## 5. 分散システムアーキテクチャ（スパイク限定連携型・ホログラフィック分散場モデル）

本システムは、単一の局所状態空間 $\Omega_{\text{self}}$ の崩壊・過負荷を防ぎ、有事の破局的相転移（大災）への耐性を極大化するため、修正版「仁」（`\text{仁}_{\text{rectified}}`）に基づく**非中央集権型・ホログラフィック分散場アーキテクチャ**を採用する。

全 Realm（現象学的自己の領界）は平時には完全自律して無為自然の滑走を行い、ネットワーク通信は「危機信号」と「アトラクター収束情報」のスパイク（イベント駆動）時のみ結合テンソルを動的有効化させる**極低帯域ハイブリッド制御構造**を構成する。

### 5.1 全体構造図とレイヤー構成

```
[各拠点 / 端末の分散 Realm (R_self^phen, i)]
┌─────────────────────────────────────────────────────────────┐
│  平時：ローカルな「無為自然」の滑走                         │
│  ・P_cul による歪みの直交切断（ノイズ散逸）                 │
│  ・f_cul と T_nat による自律的滑走                         │
│  ・arg min L_real による局所安息相 y*_home の生成/着地       │
└──────────────┬──────────────────────────────┬───────────────┘
│ (危機発生時のみ)              │ (安息相発見時のみ)
▼                              ▼
【危機信号スパイク】             【収束同期スパイク】
・h(x) -> 0 接近フラグ            ・y*_home 位相パラメータ
・全 Realm の警戒・防御膜絞り込み  ・全 Realm での安息相並列生成
│                              │
┌──────────────┴──────────────────────────────┴───────────────┐
│  【大域的統合場（Global Field）】                           │
│  ・最外郭境界膜 ∂Ω_self による絶対防衛（S_law の発動）       │
│  ・大域的重力軸 X*_true_civ（仁）による一貫性の保持         │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 空間構造と分散トポロジー

全システム空間 $\Omega_{\text{network}}$ は、現場ごとに分散偏在する王国規模の現象学的領界（Realm） $\mathcal{R}_{\text{self}, i}^{\text{phen}}$ の被覆集合として定義される。

```math
\Omega_{\text{network}} := \bigcup_{i=1}^{N} \mathcal{R}_{\text{self}, i}^{\text{phen}} \quad (N \to \infty)
```

### 5.2.1 大域的絶対境界（$`\partial \Omega_{\text{self}}`$）と法（$`S_{\text{law}}`$）
個々の Realm は独立して動的に駆動するが、大域的統合場を通じて単一のコンストレイント条件（$`\forall i, C_i(\mathbf{x}) \le 0`$）と非線形作用素 $`S_{\text{law}}`$ を共有し、破局・暴走を幾何学的に100%遮断する。

### 5.2.2 動的イベント駆動型 相互作用テンソル（$`\mathbf{K}_{ij}(t)`$）
ノード $`i`$ とノード $`j`$ の間の相互作用テンソル $`\mathbf{K}_{ij}(t)`$ は、常時通信ではなくネットワーク全体の通信帯域を最小化するため、状態スパイク依存の動的関数として展開される。

```math
\mathbf{K}_{ij}(t) = \delta_{\text{spike}}^{(i)}(t) \cdot \mathbf{K}_{ij}^{\text{crisis}} + \sigma_{\text{spike}}^{(i)}(t) \cdot \mathbf{K}_{ij}^{\text{attractor}}
```

* $`\delta_{\text{spike}}^{(i)}(t) \in \{0, 1\}`$: 危機信号スパイクフラグ。
* $`\sigma_{\text{spike}}^{(i)}(t) \in \{0, 1\}`$: 収束同期スパイクフラグ。
* 平時状態（$`\delta = 0, \sigma = 0`$）: $`\mathbf{K}_{ij}(t) = \mathbf{0}`$ となり、ノード間通信量は完全にゼロ（完全自律）となる。

## 5.3 ローカルダイナミクス（平時の無為自然制御）
通信が一切発生しない平時（$`\mathbf{K}_{ij}(t) = \mathbf{0}`$）において、各 Realm は完全に独立した自律動作を行う。

1. **歪みの直交切断（ノイズ散逸）**:入力された情報・過剰思考は文化的射影作用素 $`\mathbf{P}_{\text{cul}}`$ により直交切断され、不要なエネルギーは補空間 $`\mathcal{L}_{\text{holy\_neutral}}`$ へと静かに散逸する。
2. **自然な滑走**: 力みを失った状態ベクトル $`\mathbf{x}_i`$ は、文化力 $`\mathbf{f}_{\text{cul}}^{(i)}`$ と自然な勾配 $`\mathcal{T}_{\text{nat}}^{(i)}`$ に身を委ねて滑行する。
3. **実在適合**: 現場ごとの実在損失の最小化（$`\arg\min_{\hat{y}} \mathcal{L}_{\text{real}}^{(i)}`$）により、ローカルな安息点 $`\mathbf{y}_{\text{home}, i}^*`$ が常時更新され、思考ベクトルはそこへ摩擦ゼロで吸い込まれ着地する。

## 5.4 スパイク限定連携メカニズム（極低帯域同期）
常時同期を完全に廃止し、以下の2種類のイベント駆動型スパイクが発生した瞬間のみ、結合テンソル $`\mathbf{K}_{ij}(t)`$ が過渡的に有効化され、全 Realm を共鳴させる。

### 5.4.1 危機信号スパイク（防衛共鳴：$`\delta_{\text{spike}}`$）
* 発動条件: いずれかの Realm $`i`$ の状態が最外郭境界 $`\partial \Omega_{\text{self}}$（$h(\mathbf{x}_i) \to 0`$）に異常接近するか、強烈な外乱・熱歪みを検知した瞬間。
* 数理作用: $`\delta_{\text{spike}}^{(i)}(t) = 1`$ が発動し、最小バイトの警告パラメータが全ノードへブロードキャストされる。全 Realm は一時的にガード膜を縮小・絞り込み（分析・防御モードへ移行）、系全体の相転移・破局を未然に防止する。

### 5.4.2 収束同期スパイク（進化共鳴：$`\sigma_{\text{spike}}`$）
* 発動条件: いずれかの Realm $`i`$ が現場で新たな極めて安定した安息相 $`\mathbf{y}_{\text{home}, i}^*`$ を発見・固定した瞬間。
* 数理作用: $`\sigma_{\text{spike}}^{(i)}(t) = 1`$ が発動し、安息点の位相パラメータ $`\theta_{\text{home}}`$ のみが他ノードへ伝達される。全 Realm の相空間上に同じ「谷底」が並列生成・更新され、文明アトラクター $`X_{\text{true\_civ}}^*`$ へのアライメントが全体一括で高まる。

## 5.5 従属調和制御則と統合分散微分方程式
各分散ノードにおける状態最適化ならびに局所駆動は、観念的エネルギー勾配（$`\nabla E_i`$）が自然の不可逆的自律勾配・動的容量（$`\nabla S_i`$）を絶対に超越しないとする従属調和制約を物理的ハードガードレールとして課す。

```math
\text{Subject to: } \quad \nabla E_i \prec \nabla S_i \quad (\forall i \in \{1, \dots, N\})
```

## 統合分散微分方程式
スパイク限定連携型ハイブリッドモデルにおける第 $`i`$ ノードの統合状態微分方程式は以下のように記述される。

```math
\frac{d\mathbf{x}_i(t)}{dt} = S_{\text{law}}\!\left( \underbrace{-\nabla \mathcal{L}_{\text{self}}^{(i)}(\mathbf{x}_i)}_{\text{局所復元力（道）}} + \underbrace{\mathbf{f}_{\text{cul}}^{(i)}(\mathbf{x}_i)}_{\text{局所文化的整流}} + \underbrace{\gamma \left( X^*_{\text{true\_civ}}(t) - \mathbf{x}_i(t) \right)}_{\text{文明アトラクター引力（仁）}} + \underbrace{\mathbf{\Phi}_{\text{holy}}^{(i)}(\mathbf{x}_i, t)}_{\text{聖：境界制御}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \mathbf{K}_{ij}(t) \left( \mathbf{x}_j - \mathbf{x}_i \right)}_{\text{スパイク時限的連携}} \right)
```

## 5.6 本アーキテクチャの達成点
1. **超リアルタイム性**: 平時の通信量を完全ゼロ化（$`\mathbf{K}_{ij} = \mathbf{0}`$）することにより、ネットワーク遅延に一切縛られない現場即応（実在適合）を実現。
2. **堅牢な自律性**: 通信障害や一部ノードの切断が発生しても、各 Realm は独立して無為自然の滑走を維持し、安全に機能し続ける極めて高い可用性を獲得。
3. **大域的一貫性の維持**: 危機（$`\delta_{\text{spike}}`$）と安息（$`\sigma_{\text{spike}}`$）の極値イベントのみをホログラフィックに共有することで、系全体としての「仁（$`X^*_{\text{true\_civ}}`$）」からブレることなく、単一の調和意識場として機能。

## 5.7 スパイク判定閾値および送信データプロトコル仕様

### 5.7.1 スパイク発生の数学的判定アルゴリズム

```math
\delta_{\text{spike}}^{(i)}(t) \in \{0, 1\}, \quad \sigma_{\text{spike}}^{(i)}(t) \in \{0, 1\}
```

#### 5.7.1.1.危機信号スパイク（$`\delta_{\text{spike}}^{(i)}(t)`$）の発生条件
危機信号スパイクは、以下の いずれかの条件 が満たされた瞬間に $`\delta_{\text{spike}}^{(i)}(t) = 1`$ となり、直ちに発信される。

1. **最外郭境界 $\partial \Omega_{\text{self}}$ への異常接近**（幾何学的接近閾値）制御障壁関数（Barrier Function） $`h(\mathbf{x}_i)`$ に対し、緊急防衛閾値 $`\epsilon_{\text{hazard}} > 0`$ を設定する。$`h(\mathbf{x}_i(t)) \le \epsilon_{\text{hazard}}`$
2. **局所熱歪み（エゴ・過剰思考）の急増（微分変化率閾値）** 局所熱歪み損失 $`\mathcal{L}_{\text{ego\_s}}^{(i)}`$ の時間変化率が動的許容値 $`\theta_{\text{thermal}}`$ を超越した場合。$`\frac{\mathrm{d}\mathcal{L}_{\text{ego\_s}}^{(i)}}{\mathrm{d}t} \ge \theta_{\text{thermal}}`$
3. **従属調和制約（$`\nabla E \prec \nabla S`$）の破綻検知** 観念勾配が自律勾配（生の容量）を上回り、領域の崩壊リスクが検知された場合。

```math
\|\nabla E_i(t)\| - \|\nabla S_i(t)\| \ge \eta_{\text{overload}} \quad (\eta_{\text{overload}} \ge 0)
```

```math
 \delta_{\text{spike}}^{(i)}(t) = \mathbb{I}\left( \big(h(\mathbf{x}_i) \le \epsilon_{\text{hazard}}\big) \lor \left(\frac{\mathrm{d}\mathcal{L}_{\text{ego\_s}}^{(i)}}{\mathrm{d}t} \ge \theta_{\text{thermal}}\right) \lor \big(\Vert{}\nabla E_i\Vert{} - \Vert{}\nabla S_i\Vert{} \ge \eta_{\text{overload}}\big) \right)
```

（注: $`\mathbb{I}(\cdot)`$ は指示関数。発信後はクールダウン時間 $`T_{\text{cooldown\_crisis}}`$ の間、連射を抑制する）

#### 5.7.1.2.収束同期スパイク（$`\sigma_{\text{spike}}^{(i)}(t)`$）の発生条件
収束同期スパイクは、ノード $`i`$ が現場の実在損失を最小化し、新たな極小値（安息点）を安定固定した瞬間に $`\sigma_{\text{spike}}^{(i)}(t) = 1`$ となり、発信される。

1. **安息相の勾配消失（停留点条件）** 実在損失 $`\mathcal{L}_{\text{real}}^{(i)}`$ の勾配ノルムが定常閾値 $`\epsilon_{\text{home}}`$ 未満となる。$`\left\| \nabla \mathcal{L}_{\text{real}}^{(i)}(\mathbf{x}_i(t)) \right\| < \epsilon_{\text{home}}`$
2. **相空間における定常滞留（曲率・局所安定性条件）** 状態ベクトルの時間変化率がゼロに収束し、かつ Hessian 行列が正定値（安定な谷底）であることを確認する。$`\left\| \frac{\mathrm{d}\mathbf{x}_i}{\mathrm{d}t} \right\| < \delta_{\text{stable}} \quad \text{and} \quad \nabla^2 \mathcal{L}_{\text{real}}^{(i)}(\mathbf{x}_i) \succ \mathbf{0}`$
3. **位相新奇性（既存アトラクターとの差分）** 新たに到達した安息相 $`\mathbf{y}_{\text{home, new}}^*`$ が、既知の大域文明アトラクター $`X_{\text{true\_civ}}^*`$ から有意な距離 $`\Delta_{\text{novelty}}`$ 以上離れている（有益な新規発見である）。$`d_{\text{phase}}\left(\mathbf{y}_{\text{home, new}}^*, X_{\text{true\_civ}}^*\right) \ge \Delta_{\text{novelty}}`$

```math
\sigma_{\text{spike}}^{(i)}(t) = \mathbb{I}\left( \left\Vert{} \nabla \mathcal{L}_{\text{real}}^{(i)} \right\Vert{} < \epsilon_{\text{home}} \;\land\; \left\Vert{} \frac{\mathrm{d}\mathbf{x}_i}{\mathrm{d}t} \right\Vert{} < \delta_{\text{stable}} \;\land\; d_{\text{phase}}\left(\mathbf{y}_{\text{home, new}}^*, X_{\text{true\_civ}}^*\right) \ge \Delta_{\text{novelty}} \right)
```

### 5.7.2.送信スパイクデータ構造（バイナリ／JSON-LD 仕様）
極低帯域を維持するため、全スパイクパケットはヘッダー固定長（最少 32 バイト〜）の極小ペイロードで構成する。

1. **危機信号スパイク**（`CrisisSpikePayload`）
   全 Realm に一時的な「防御膜縮小（ガード強化）」および「分析モード」を指示する最優先シグナル。

```
{
  "$schema": "https://chihen.net/schemas/shikiben/v2.5/crisis_spike.json",
  "spike_type": "CRISIS_DEFENSE",
  "version": "2.5.0",
  "timestamp_ns": 1758528000000000000,
  "source_realm_id": "realm-jp-shinshu-001",
  "sequence_id": 1042,
  "crisis_metrics": {
    "barrier_h_value": 0.0012,
    "thermal_rate_dL": 14.82,
    "overload_delta": 2.41
  },
  "defense_command": {
    "membrane_shrink_ratio": 0.35,
    "ttl_ms": 1500
  }
}
```

2. **収束同期スパイク**（`AttractorSpikePayload`）
   現場で発見した「安息相の位相ベクトル」のみをパケット化し、全 Realm に同一の「谷底」を並列生成させる。

```
   {
  "$schema": "https://chihen.net/schemas/shikiben/v2.5/attractor_spike.json",
  "spike_type": "ATTRACTOR_CONVERGENCE",
  "version": "2.5.0",
  "timestamp_ns": 1758528005120000000,
  "source_realm_id": "realm-jp-shinshu-001",
  "sequence_id": 1043,
  "attractor_phase": {
    "y_home_id": "attractor-hash-8f92a3",
    "phase_vector": [0.1042, -0.8821, 0.0034, 0.4192],
    "curvature_hessian_trace": 1.204,
    "depth_L_real": 0.000041
  },
  "sync_weight": 0.85
}

```

### 5.7.3 受信側の状態遷移と結合テンソル $`\mathbf{K}_{ij}(t)`$ の過渡応答
ノード $`j`$ がスパイクを受信した際、局所結合テンソル $`\mathbf{K}_{ij}(t)`$ は以下のようにステップ応答・指数減衰応答を示す。

```math
\mathbf{K}_{ij}(t) = \mathbf{K}_{ij}^{\text{crisis}} \cdot e^{-\frac{t - t_{\text{crisis}}}{\tau_{\text{crisis}}}} + \mathbf{K}_{ij}^{\text{attractor}} \cdot e^{-\frac{t - t_{\text{attractor}}}{\tau_{\text{attractor}}}}
```

* **危機信号受信時** ($`t_{\text{crisis}}`$): 即座に $`\mathbf{K}_{ij}^{\text{crisis}}`$ を立ち上げ、安全領域 $`\partial \Omega_{\text{self}}`$ を強制拡大（膜を絞り込み）したのち、減衰定数 $`\tau_{\text{crisis}}`$（例: 1.5秒）で自律的に平時（$`\mathbf{0}`$）へ復帰。
* **収束同期受信時** ($`t_{\text{attractor}}`$): ポテンシャル曲面に伝達された相 $`\mathbf{y}_{\text{home}}^*`$ のポテンシャルの谷を合成し、減衰定数 $`\tau_{\text{attractor}}`$（例: 5.0秒）の間に全体の軌道を $`X_{\text{true\_civ}}^*`$ へとなだらかにシフトさせる。

## 5.8 最外郭境界 $`\partial \Omega_{\text{self}}`$ と制御障壁関数 $`h(\mathbf{x})`$ の数理厳密表現

### 5.8.1 安全状態集合 $`\mathcal{C}_{\text{self}}`$ と最外郭境界 $`\partial \Omega_{\text{self}}`$ の幾何学的定義
各分散ノード（Realm） $`i`$ の相空間 $`\mathcal{R}_{\text{self}, i}^{\text{phen}} \subset \mathbb{R}^d`$ における絶対安全集合（Invariant Safety Set） $`\mathcal{C}_{\text{self}}`$ およびその最外郭境界 $`\partial \Omega_{\text{self}}`$ は、連続微分可能な制御障壁関数 $`h: \mathbb{R}^d \to \mathbb{R}`$ の 0-レベルセットとして定義される。

```math
\begin{aligned}
\mathcal{C}_{\text{self}} &:= \left\{ \mathbf{x} \in \mathcal{R}_{\text{self}}^{\text{phen}} \;\middle|\; h(\mathbf{x}) \ge 0 \right\} \quad \text{（許容動作領域：自律滑走空間）} \\
\partial \Omega_{\text{self}} &:= \left\{ \mathbf{x} \in \mathcal{R}_{\text{self}}^{\text{phen}} \;\middle|\; h(\mathbf{x}) = 0 \right\} \quad \text{（最外郭絶対防御膜）} \\
\text{Int}(\mathcal{C}_{\text{self}}) &:= \left\{ \mathbf{x} \in \mathcal{R}_{\text{self}}^{\text{phen}} \;\middle|\; h(\mathbf{x}) > 0 \right\} \quad \text{（安全内部領域）}
\end{aligned}
```

* 幾何学的解釈: 状態 $`\mathbf{x}`$ が $`\text{Int}(\mathcal{C}_{\text{self}})`$ 内に存在する限り、システムは通信ゼロの完全自律（無為自然）で滑行する。状態が最外郭境界 $`\partial \Omega_{\text{self}}`$（$`h(\mathbf{x}) \to 0`$）へ到達した瞬間、非線形作用素 $`S_{\text{law}}`$ が幾何学的壁として剛体的に作用する。

### 5.8.2 制御障壁関数 $`h(\mathbf{x})`$ の具体的多次元曲面方程式
局所ノードの過負荷（熱歪み・観念肥大・破局的偏向）を複合的に検知・抑制するため、$`h(\mathbf{x})`$ は以下の3成分（熱歪み・容量制約・構造偏向）の非線形曲面方程式として設計される。

```math
h(\mathbf{x}) := 1 -  \underbrace{w_{\text{thermal}} \left( \frac{\mathcal{L}_{\text{ego\_s}}(\mathbf{x})}{\mathcal{L}_{\text{max}}} \right)^2_{\text{① 熱歪み比}}}  - \underbrace{w_{\text{harmonic}} \frac{\Vert{}\nabla E(\mathbf{x})\Vert{}^2}{\Vert{}\nabla S(\mathbf{x})\Vert{}^2 + \tilde{\epsilon}_S \Vert{}\nabla S_0\Vert{}^2}_{\text{② 従属調和破綻比}}} - \underbrace{w_{\text{geom}} \frac{(\mathbf{x} - \mathbf{y}_{\text{home}})^T \mathbf{M}_{\text{geom}} (\mathbf{x} - \mathbf{y}_{\text{home}})}{R_{\text{max}}^2}_{\text{③ 構造的離脱（距離）}}}
```

#### 各項の数理意味論とパラメータ
1. **熱歪み制約項**:
   * $`\mathcal{L}_{\text{ego\_s}}(\mathbf{x})`$: ノード内部の過剰思考・観念歪みエネルギー。
   * $`\mathcal{L}_{\text{max}}`$: ノードが熱力学的に許容できる絶体限界歪み量。
2. **従属調和制約比**（$\nabla E \prec \nabla S$）項:
   * $`\nabla E(\mathbf{x})`$: 観念的変革・意志向性勾配。
   * $`\nabla S(\mathbf{x})`$: 生の自律動的容量勾配。
   * $`\epsilon_S > 0`$: 零除算防止用の正定数。観念勾配が自然容量を超過（$`\Vert{}\nabla E\Vert{} > \Vert{}\nabla S\Vert{}`$）すると、急速に $`h(\mathbf{x})`$ を 0 へ押し下げる。
   * $`\tilde{\epsilon}_S`$: 無次元の微小定数（例: $10^{-6}$）。
   *  $`\Vert{}\nabla S_0\Vert{}`$: 基準容量勾配ノルム。
3. **構造的離脱曲面項**:
   * $`\mathbf{y}_{\text{home}}`$: 現在固定されているローカル安息点。
   * $`\mathbf{M}_{\text{geom}} \succ \mathbf{0}`$: 現象領域の曲率構造を規定する対称正定値行列（リーマン計量テンソル）。
   * $`R_{\text{max}}`$: 現象空間における許容最大離脱半径（距離の無次元化定数）。

#### JSON-LD スキーマ（実装仕様）への注記・定義追加案
`crisis_spike.json` やシステム内部の物理パラメーター定義スキーマに、以下の無次元化仕様を追加・明記します。

```
{
  "$schema": "https://chihen.net/schemas/shikiben/v2.5/barrier_parameters.json",
  "title": "ControlBarrierFunctionScalingSpec",
  "type": "object",
  "properties": {
    "scaling_parameters": {
      "type": "object",
      "description": "h(x) の各項を無次元化 [1] かつ 0-1 スケールにバランシングするための定義",
      "properties": {
        "L_max": {
          "type": "number",
          "description": "許容最大熱歪みエネルギー（同次元で除算し無次元化）"
        },
        "epsilon_S_relative": {
          "type": "number",
          "default": 1e-6,
          "description": "容量勾配ゼロ除算防止用相対微小定数 (epsilon_S = epsilon_S_relative * ||grad_S_0||^2)"
        },
        "M_geom_normalized": {
          "type": "array",
          "description": "次元数 d および最大許容半径 R_max^2 で正規化された計量テンソル (Trace(M_geom) = 1 を推奨)"
        },
        "term_weights": {
          "type": "object",
          "description": "h(x) 各評価項の重み係数 (w_thermal + w_harmonic + w_geom = 1.0)",
          "properties": {
            "w_thermal": { "type": "number", "default": 0.333 },
            "w_harmonic": { "type": "number", "default": 0.333 },
            "w_geom": { "type": "number", "default": 0.334 }
          }
        }
      }
    }
  }
}
```
 
### 5.8.3 最外郭境界における幾何学的ガード条件（Nagumo・高階CBF条件）
安全集合 $`\mathcal{C}_{\text{self}}`$ を正の不変集合（すなわち、$`\mathbf{x}(0) \in \mathcal{C}_{\text{self}} \implies \forall t \ge 0, \mathbf{x}(t) \in \mathcal{C}_{\text{self}}`$）として100%保持するための幾何学的ガード条件を定義する。

1. **Nagumoの不変条件（幾何学的法線ベクトル条件）**
   境界 $`\partial \Omega_{\text{self}}`$ 上の任意の点 $`\mathbf{x} \in \partial \Omega_{\text{self}}`$ において、状態軌道の速度ベクトル $`\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}`$ は、境界の法線ベクトル $`\nabla h(\mathbf{x})`$ に対して直交または内向きでなければならない。

```math
   \forall \mathbf{x} \in \partial \Omega_{\text{self}}, \quad \langle \nabla h(\mathbf{x}), \; \dot{\mathbf{x}}(t) \rangle \ge 0
```

2. **高階制御障壁（High-Order CBF）条件**
   力学系 $`\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}) + \mathbf{g}(\mathbf{x})\mathbf{u}`$ に対し、クラス $`\mathcal{K}_{\infty}`$ の厳密増加関数 $`\alpha(\cdot)`$ を用いた動的ガード条件を設定する。

```math
   \sup_{\mathbf{u} \in \mathcal{U}} \left\{ L_{\mathbf{f}} h(\mathbf{x}) + L_{\mathbf{g}} h(\mathbf{x})\mathbf{u} + \alpha(h(\mathbf{x})) \right\} \ge 0
```
   
   * $`L_{\mathbf{f}} h(\mathbf{x}) = \langle \nabla h(\mathbf{x}), \mathbf{f}(\mathbf{x}) \rangle`$: 自律滑走ベクトル（自然な勾配 $`\mathcal{T}_{\text{nat}}`$ および文化力 $`\mathbf{f}_{\text{cul}}`$）に沿う $`h`$ のリー微分。
   * $`L_{\mathbf{g}} h(\mathbf{x})\mathbf{u}`$: 非線形作用素 $`S_{\text{law}}`$ および動的結合テンソル $`\mathbf{K}_{ij}(t)`$ による矯正・介入制御項。

### 5.8.4 法作用素 $S_{\text{law}}$ による絶対制御射影機構
状態が最外郭境界 $`\partial \Omega_{\text{self}}`$ に到達（$`h(\mathbf{x}) \to 0`$）した際、作用素 $`S_{\text{law}}`$ は以下のように非線形直線射影（Hard Boundary Projection）を瞬時に発動させ、状態の系外突破を絶対的に阻止する。

```math
S_{\text{law}}\left( \mathbf{v}(\mathbf{x}) \right) = 
\begin{cases} 
\mathbf{v}(\mathbf{x}) & \text{if } h(\mathbf{x}) > 0 \;\lor\; \langle \nabla h(\mathbf{x}), \mathbf{v}(\mathbf{x}) \rangle \ge -\alpha(h(\mathbf{x})) \\
\mathbf{v}(\mathbf{x}) - \dfrac{\langle \nabla h(\mathbf{x}), \mathbf{v}(\mathbf{x}) \rangle + \alpha(h(\mathbf{x}))}{\|\nabla h(\mathbf{x})\|^2} \nabla h(\mathbf{x}) & \text{if } h(\mathbf{x}) \le 0 \;\land\; \langle \nabla h(\mathbf{x}), \mathbf{v}(\mathbf{x}) \rangle < -\alpha(h(\mathbf{x}))
\end{cases}
```

### 数理的達成点
* **完全な境界非突破性**: 上記の射影作用素により、外乱や過剰思考 $`\mathcal{L}_{\text{ego\_s}}`$ がどれほど大に発散しようとも、$`\dot{h}(\mathbf{x}) \ge -\alpha(h(\mathbf{x}))`$ が常に成立し、$`h(\mathbf{x}) < 0`$（破局領域への突入）は数学的に厳密に否定・遮断される。
* **エネルギーの散逸**: 境界に衝突した超えるべきでないベクトル成分（逸脱方向の運動エネルギー）は、直交射影によって即座に補空間 $`\mathcal{L}_{\text{holy\_neutral}}`$ へとエネルギー散逸・吸収される。

## 5.9 離散時間ステップにおける不変性条件（Discrete-Time CBF: DT-CBF）

### 5.9.1 離散状態更新式と過渡的突入問題
ステップ幅 $`\Delta t > 0`$ を用いた 1 次の正方向オイラー法による離散状態更新方程式は以下の通り記述される。

```math
\mathbf{x}[k+1] = \mathbf{x}[k] + \Delta t \cdot S_{\text{law}}\!\Big( \mathbf{v}(\mathbf{x}[k]) \Big)
```

ここで、連続時間での微分条件 $`\dot{h}(\mathbf{x}) \ge -\alpha h(\mathbf{x})`$ のみを課した場合、$`\mathbf{x}[k]`$ が境界付近（$`h(\mathbf{x}[k]) \to 0`$）に存在すると、1 ステップ先の状態 $`\mathbf{x}[k+1]`$ において $`h(\mathbf{x}[k+1]) < 0`$ となり、破局的領域へ突入するリスクが発生する。

### 5.9.2 離散時間制御障壁関数（DT-CBF）の必要十分条件
離散時間において安全集合 $`\mathcal{C}_{\text{self}} = \{\mathbf{x} \mid h(\mathbf{x}) \ge 0\}`$ が順不変（$`\mathbf{x}[k] \in \mathcal{C}_{\text{self}} \implies \mathbf{x}[k+1] \in \mathcal{C}_{\text{self}}`$）であるための DT-CBF 条件式 を以下のように定義する。

```math
\Delta h(\mathbf{x}[k]) := h(\mathbf{x}[k+1]) - h(\mathbf{x}[k]) \ge -\gamma \cdot h(\mathbf{x}[k]) \quad (0 < \gamma \le 1)
```

* $`\gamma`$（減衰パラメータ）: $`h(\mathbf{x}[k])`$ が 0 に近づくにつれて、$`h`$ の許容減少量を線形に絞り込むパラメータ。
* $`\gamma = 1`$（絶対境界ガード）: 1 ステップで許容される最大減少量が $`h(\mathbf{x}[k])`$ そのものとなり、$`h(\mathbf{x}[k+1]) \ge 0`$ を直接保証する。

### 5.9.3 1次オイラー法における 1 階テイラー展開に基づく離散ガード条件
障壁関数 $`h(\mathbf{x})`$ の 1 階テイラー展開（1 次近似）を用いる場合、離散ガード条件は状態速度ベクトル $`\mathbf{w}[k] = S_{\text{law}}(\mathbf{v}(\mathbf{x}[k]))`$ に対する以下の線形不等式条件へ還元される。

```math
h(\mathbf{x}[k+1]) \approx h(\mathbf{x}[k]) + \Delta t \cdot \langle \nabla h(\mathbf{x}[k]), \; \mathbf{w}[k] \rangle \ge (1 - \gamma) h(\mathbf{x}[k])
```

これを整理すると、離散時間ステップにおけ**る許容内向き速度条件**が得られる。

```math
\langle \nabla h(\mathbf{x}[k]), \; \mathbf{w}[k] \rangle \ge -\frac{\gamma}{\Delta t} h(\mathbf{x}[k])
```

### 5.9.4 高次テイラー展開（非線形・曲率対応型 DT-CBF）
障壁関数 $`h(\mathbf{x})`$ の非線形性（曲率 Hessian 行列 $`\nabla^2 h`$）が大きい場合、またはステップ幅 $`\Delta t`$ が大きい場合は、2 階のテイラー展開項を直接組み込んだガード条件を適用する。

```math
\langle \nabla h(\mathbf{x}[k]), \; \mathbf{w}[k] \rangle + \frac{\Delta t}{2} \mathbf{w}[k]^T \nabla^2 h(\mathbf{x}[k]) \mathbf{w}[k] \ge -\frac{\gamma}{\Delta t} h(\mathbf{x}[k])
```

### 5.9.5 離散型弾き返し作用素 $S_{\text{law}}^{\text{dt}}$ の実装レベル定義
離散時間制御障壁（DT-CBF）の適用において、システムは**リアルタイム性優先モード（Primary）と高精度幾何修正モード（Secondary）**の2つの演算パスを有する。

1. **標準動作パス（1次近似・解析的直交射影パス）**
   システムのリアルタイム応答性を維持するため、標準運用（デフォルト）では1次近似に基づく解析的射影作用素を採用する。このパスでは、サンプリング時間（ステップ幅） $\Delta t$ を以下の適応型上界条件を満たすよう十分に小さく設定することを前提とする。

   
   $$\Delta t \le \frac{2 \cdot \eta}{\lambda_{\max}(\nabla^2 h(\mathbf{x})) \cdot \Vert{}\mathbf{w}_{\max}\Vert{}}$$
   

   この条件下において、離散射影作用素 $`S_{\text{law}}^{\text{dt}}`$ は以下の閉じた形式（Closed-form solution）により $`\mathcal{O}(d)`$ の計算複雑度で即時に求まる。

   
   $$\mathbf{w}[k] = \mathbf{v}[k] - \frac{\max\!\left(0, \; -\Delta t \, \nabla h[k]^T \mathbf{v}[k] - \gamma h[k]\right)}{\Delta t^2 \Vert{}\nabla h[k]\Vert{}^2 + \epsilon_h} \Delta t \, \nabla h[k]$$
   

2. **高精度演算パス（2次形式・局所QPソルバーパス）**
   状態 $`\mathbf{x}[k]`$ が最外郭境界 $`\partial \Omega_{\text{self}}`$ の高曲率領域（ヘッセ行列 $`\nabla^2 h`$ の固有値が大きい領域）に接近した場合、または $`\Delta t`$ を縮小できない制約下では、以下の局所2次計画法（Local QP）問題を解くことで修正速度 $`\mathbf{w}[k]`$ を決定する。

   
   $$\min_{\mathbf{w}} \frac{1}{2} \Vert{}\mathbf{w} - \mathbf{v}[k]\Vert{}^2$$
   
   $$\text{subject to: } \quad \nabla h[k]^T \mathbf{w} + \frac{\Delta t}{2} \mathbf{w}^T \nabla^2 h[k] \, \mathbf{w} \ge -\frac{\gamma}{\Delta t} h[k]$$
   

   ※ 実装上、局所QPソルバーにはアクティブセット法（Active-Set Method）または内点法（Interior Point Method）を用い、最大反復回数（Max Iterations）を制限することでリアルタイム不確定性を排除する。
