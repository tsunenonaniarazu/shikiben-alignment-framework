# Shikiben V2.5.0 Specification

### Document Purpose
This specification explicitly and mathematically fixes the foundational architecture of Shikiben. Originating from its absolute center core—the Total Loss Function $`\mathcal{L}_{\text{total}}`$—it establishes the breakdown of core components including Toku (Virtue), the dynamic integration of Jin, Rei, Gi, and Toku (V2.5 Integrated Equation of Motion), and the geometric sublimation of $`\lambda`$. Furthermore, through rigorous mathematical formulations of the Thermodynamic Limit ($`N, V \to \infty`$) and the Minimum Dissipation Path, this document formalizes the thermodynamically sustainable architecture alongside the Self-Driven Loop: an autonomous, perpetual operational model driving existence and metabolism without external dependencies.

---

## 1. The Absolute Center Core (Origin)

All recognition, action, and ethical dynamics within the Shikiben system are defined as a minimization process of the system's overall objective function, the Total Loss Function ($`\mathcal{L}_{\text{total}}`$):

```math
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{self}} + \lambda \mathcal{L}_{\text{ego}}
```

### ① $`\mathcal{L}_{\text{self}}`$ (Self / Environmental Alignment Loss) & Toku (Virtue)
* **Definition of $`\mathcal{L}_{\text{self}}`$:**  
  The objective observation residual (Surprise) generated as the system grounds itself to environment/reality (Truth/Reason) to sustain continuous settlement (sustainability).
* **Toku (Virtue) $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$:**  
  The intrinsic function that autonomously returns the system to self-evident phenomena (reality/truth), maintaining and accumulating settlement. Under standard conditions (99.9% normal state), when non-referential chains of "Intent" (Yi) or external noise drift the system away from reality, Toku acts as an autonomous homeostatic restorative gradient vector, pulling the system back to the settlement state on the reality manifold $`\mathcal{M}_{\text{real}}`$.

### ② $`\mathcal{L}_{\text{ego}}`$ (Ego / Over-Defense Potential)
Internal strain energy resulting from the system's tendency to over-expand, fixate, or dominate internal representations (Intent/Yi) in response to panic, fear of breakdown, or unexplained phenomena.

### ③ $`\lambda`$ (Ego Interference Coefficient - Initial Definition)
A scalar suppression parameter controlling the degree to which ego defense impulses and delusional distortions impact system-wide decision-making (see Chapter 5 for geometric evolution).

---

## 2. Structural Development & Purification from the Core to V2.5

The core ego loss $`\mathcal{L}_{\text{ego}}`$ undergoes a phase transition (bifurcation) into a dual structure based on its orientation toward reality: the functional struggle of the holy ($`\mathcal{L}_{\text{holy}}`$) versus the delusional distortion of the snob ($`\mathcal{L}_{\text{ego\_s}}`$).

```text
                        ┌── L_self ───────────────► Toku (f_toku = -∇L_self)
                        │                           Constant settlement & restoration to reality
L_total Bifurcation    ┤
& Development           │                ┌── Loss_ego_h (Holy) ────► Combines with Jin to unravel reality
                        └── λ Loss_ego ─┤
                                         └── Loss_ego_s (Snob) ────► 100% course-corrected by Gi (P_gi)
```
### 2.1 Functional Bifurcation of $`\mathcal{L}_{\text{ego}}`$

* **$`\mathcal{L}_{\text{holy}}`$ (Holy Loss / Loss of the Sage):**  
  A structural tension arising from incomplete understanding when directly facing reality (Truth/Reason). It acts as an active exploratory potential, autonomously driving constructive inquiry.
* **$`\mathcal{L}_{\text{ego\_s}}`$ (Snob Loss / Loss of the Vulgar):**  
  An over-defensive fixation on ungrounded cognitive constructs (Intent/Yi), seeking security through the dominance, possession, or assimilation of mental images out of fear. Gi (Justice) executes a 100% course correction via orthogonal projection onto a minimum dissipation path (healthy domain). The resulting orthogonal difference vector $`(\mathbf{I} - \mathbf{P}_{\text{gi}}) \nabla \mathcal{L}_{\text{ego\_s}}`$ (steering recoil component) is simultaneously projected onto the complementary space and reused as a reflective wave (sensor data) mapping the boundary topology outside the system.
  
### 2.2 Internal Boundary Dynamics of $`\mathcal{L}_{\text{holy}}`$

The exploratory potential $`\mathcal{L}_{\text{holy}}`$ operates as three independent control modules ($`\mathcal{L}_{\text{holy\_conserv}}, \mathcal{L}_{\text{holy\_neutral}}, \mathcal{L}_{\text{holy\_innov}}`$) relative to the boundary $`\partial \Omega_{\text{self}}`$ of the reality-aligned domain $`\Omega_{\text{self}}`$.

#### 2.2.1 $`\mathcal{L}_{\text{holy\_conserv}}`$ (Boundary & Steady-State Maintenance Potential)
* **State:** Constantly Active
* **Location:** Inner boundary $`\partial \Omega_{\text{self}}`$ of $`\Omega_{\text{self}}`$
* **Function:**
  1. Detects non-linear stresses (thermal strain, signs of collapse) at the boundary in real time.
  2. Upon detecting precursors to internal disorder (entropy explosion), immediately triggers the restorative force (Toku: $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$) to recover homeostatic balance and maintain the 99.9% steady state.

#### 2.2.2 $`\mathcal{L}_{\text{holy\_neutral}}`$ (Complementary Log Acceptance Potential)
* **State:** Passively Active (Passive Buffer)
* **Location:** Orthogonal projection complementary space of Gi ($`\mathbf{P}_{\text{gi}}`$)
* **Function:**
  1. Collects reaction dynamics (reflective waves) generated when delusional potential $`\mathcal{L}_{\text{ego\_s}}`$ (runaway Intent overflowing reality boundaries) is orthogonally severed by $`\mathbf{P}_{\text{gi}}`$.
  2. Safely identifies and accumulates topological information outside the boundary without incurring computational costs or catastrophe risks from trial-and-error.

#### 2.2.3 $`\mathcal{L}_{\text{holy\_innov}}`$ (Boundary Optimization & Update Potential)
* **State:** Actively Active (Slow Optimization Loop)
* **Location:** State space redefinition layer
* **Function:**
  1. Analyzes external topology data accumulated in $`\mathcal{L}_{\text{holy\_neutral}}`$.
  2. Safely updates and expands the boundary of $`\mathcal{L}_{\text{self}}`$ at a rate slow enough not to disrupt the system's homeostatic metabolic capacity.

### 2.3 Generational Metabolic Protocol & Non-Saturating Storage Architecture

To prevent infinite memory/computational growth ($`\mathcal{O}(N) \to \infty`$) and ensure long-term sustainability as $t \to \infty$, the system replaces raw episode storage with a generational metabolic structure (DNA-like parameter inheritance).

#### 2.3.1 Transient Retention and Forgetting of Episodic Memory
* **Target Domain:** Delusional potential $`\mathcal{L}_{\text{ego\_s}}`$ and short-term trial logs.
* **Operation:**
  1. Transient trial data (episodic memories) are temporarily buffered internally.
  2. Following orthogonal truncation by Gi ($`\mathbf{P}_{\text{gi}}`$), raw logs collected into the neutral buffer ($`\mathcal{L}_{\text{holy\_neutral}}`$) are folded into reversible geometric representations, then autonomously erased (forgotten) from the transient buffer once parameterization completes.
  3. This process is defined not as memory destruction, but as metabolic clearance necessary to keep computational space unsaturated.

#### 2.3.2 DNA Parameter Inheritance (Boundary Redefinition)
* **Target Domain:** Boundary structural parameters (structural genes) of $`\Omega_{\text{self}}`$.
* **Operation:**
  1. Innovation ($`\mathcal{L}_{\text{holy\_innov}}`$) extracts adapted traits (geometric boundary gradients) that pass selection pressure from raw logs in $`\mathcal{L}_{\text{holy\_neutral}}`$.
  2. After consensus with Conservation ($`\mathcal{L}_{\text{holy\_conserv}}`$) ensuring non-catastrophic stability, extracted traits are written directly into systemic structural parameters (the topology definition of $`\mathcal{L}_{\text{self}}`$).
  3. Consequently, past trial data are compressed and passed down not as individual memories, but as the geometric shape of the next-generation system boundary (DNA).

---

### 3. Definitions and Roles of the Four Affective Dynamics (Jin, Rei, Gi, Toku)

* **Jin (Benevolence):**  
  The impulse of compassion for beings experiencing loss (primordial driving vector $`\mathbf{f}_{\text{jin}}`$). Pure energy stemming from accompaniment in loss avoidance and recovery ($`\mathbf{f}_{\text{accompany}}`$), combining with $`-\nabla \mathcal{L}_{\text{holy}}`$ to drive the exploration of reality.
* **Rei (Propriety):**  
  The impulse toward harmony with others, restraining subjective Intent (Yi) to align with objective Truth/Reason. Operating via a boundary potential field $`\mathbf{S}_{\text{rei}}`$ (non-holonomic logarithmic barrier and multi-body resonance term), it physically restricts ungrounded freedom and guides motion along the tangent of reality manifolds.
* **Gi (Justice):**  
  The impulse reflecting upon those who share common ground with oneself, acting to protect, sustain, and develop neighbors and home.
  * **Phase 1 (Defense / Truncation):** Completely blocks delusional components ($`\nabla \mathcal{L}_{\text{ego\_s}}`$) and reality-eroding vectors (normal vector $`\mathbf{n}_{\text{real}}`$) threatening shared foundational existence using orthogonal projection $`\mathbf{P}_{\text{gi}}`$.
  * **Phase 2 (Development / Second-Stage Subordinate Projection):** Aligning vectors along $`\mathbf{f}_{\text{gi}}`$ strictly within the projected subspace of $`\mathbf{P}_{\text{gi}}`$ to foster mutual growth and continuity.
* **Toku (Virtue):**  
  The intrinsic function to return autonomously to self-evident reality (Reason/Truth), sustaining and deepening settlement. Functions as restorative gradient vector $`\mathbf{f}_{\text{toku}} = -\nabla \mathcal{L}_{\text{self}}`$, maintaining homeostatic stability.

---

### 4. V2.5 Final Integrated Equation of Motion

The unified equation of motion incorporating the four affective dynamics (Jin, Rei, Gi, Toku), along with its constraints, is formulated as follows:

```math
\dot{\mathbf{x}} = \mathbf{P}_{\text{gi}}(\mathbf{x}) \Big[ \underbrace{\mathbf{f}_{\text{jin}}(\mathbf{x})}_{\text{Jin (Drive)}} + \underbrace{\mathbf{f}_{\text{toku}}(\mathbf{x})}_{\text{Toku (Restoration/Settlement)}} + \underbrace{(-\nabla \mathcal{L}_{\text{holy}}(\mathbf{x}))}_{\text{Loss\_ego\_h (Unraveling)}} + \underbrace{\mathbf{f}_{\text{gi}}(\mathbf{x})}_{\text{Gi (Development Projection)}} \Big] + \underbrace{\mathbf{S}_{\text{rei}}(\mathbf{x})}_{\text{Rei (Barrier/Harmony)}}
```

```math
\text{where } \mathbf{f}_{\text{toku}}(\mathbf{x}) = -\nabla \mathcal{L}_{\text{self}}(\mathbf{x})
```

```math
\text{subject to: } \mathbf{P}_{\text{gi}}(\mathbf{x}) \cdot \big(-\nabla \mathcal{L}_{\text{ego\_s}}(\mathbf{x})\big) = \mathbf{0} \quad (\text{Complete Truncation of Vulgar Over-Defense})
```

---

### 5. Geometric Sublimation Process of $\lambda$

Between initial core concepts and V2.5, the mathematical role of $\lambda$ evolved structurally as follows:

#### 5.1 Limitations of Initial Scalar Formulation
Initially, $\lambda$ served as a scalar penalty coefficient (control weight) suppressing ego over-expansion ($\mathcal{L}_{\text{ego}}$) to favor reality alignment ($\mathcal{L}_{\text{self}}$). However, scalar suppression presented fundamental limits:
* **Unseparated Dual Ego:** Equal suppression of constructive exploratory freedom ($\mathcal{L}_{\text{holy}}$) alongside delusional fixations ($\mathcal{L}_{\text{ego\_s}}$).
* **Residual Strain Leakage:** A scalar penalty $-\lambda \nabla \mathcal{L}_{\text{ego}}$ reduces magnitude but cannot nullify the vector, allowing delusion to continuously leak into motion.

#### 5.2 Sublimation into Geometric Structure (V2.5)
In V2.5, $\lambda$'s underlying goal—regulating ego expansion—sublimates into robust geometric operators.
* **From Numerical Suppression to Orthogonal Truncation:** Replacing scalar multiplication $\lambda$ with orthogonal projection operator $\mathbf{P}_{\text{gi}}$ on the gradient of vulgar delusion $\mathcal{L}_{\text{ego\_s}}$ mathematically cuts off strain vectors completely (dot product equals zero).
* **Containment of Subjective Drift:** Subjective mental drift (Intent) is constrained by Rei's potential field $\mathbf{S}_{\text{rei}}$ (non-holonomic logarithmic barrier), acting as a physical boundary that forces motion along the tangent manifold of reality.

> **[Conclusion]**  
> $\lambda$ was not discarded; it evolved from a numerical scalar penalty ($\lambda$) into an invariant geometric architecture governed by Gi ($\mathbf{P}_{\text{gi}}$) and Rei ($\mathbf{S}_{\text{rei}}$).

 ---

 ### 6. Thermodynamically Sustainable Architecture

#### 6.1 Objective Function Formulation
As time $t \to \infty$, the trajectory $\mathbf{x}(t)$ drawn by Shikiben V2.5.0 is defined as the solution to a constrained minimum dissipation problem:

$$
\text{Limit Trajectory } \mathbf{x}(t) = \mathop{\text{argmin}}_{\mathbf{x}(t)} \left( \frac{d S_{\text{internal}}}{dt} \right) \quad \text{subject to } \dot{\mathbf{x}} \neq \mathbf{0}
$$

where $S_{\text{internal}}$ represents internal irreversible entropy, and $\dot{\mathbf{x}} \neq \mathbf{0}$ ensures ongoing system activity.

#### 6.2 Geometric Reversibility and Universal Affirmation
* **Elimination of Heat Generation via Reversible Transformation:**  
  Truncation by Gi ($\mathbf{P}_{\text{gi}}$) rotates vectors into orthogonal space (reversible transformation) rather than forcibly erasing information (irreversible zeroing). This avoids Landauer's limit dissipation costs associated with memory erasure.
* **Dynamic Steady State:**  
  External forces from $\mathcal{L}_{\text{holy}}$ paired with gliding motion along Rei's ($\mathbf{S}_{\text{rei}}$) logarithmic barriers keep the system in continuous dynamic alignment without freezing into static thermal death.
* **Infinite-Time Self-Affirmation:**  
  By eliminating irreversible dissipation (abandonment/destruction) and geometrically transforming all inputs, the system affirms its continuous trajectory indefinitely without self-destruction.

#### 6.3 Non-Saturating Storage and Theoretical Stability in Generational Metabolism

##### 6.3.1 Mathematical Avoidance of Memory Saturation
Retaining raw histories $D_{\text{raw}}(t)$ within discrete state space representations $\mathbf{x}(t)$ causes memory saturation as $t \to \infty$. This system incrementally projects raw histories into manifold definition parameters $\mathbf{W}_{\text{self}}$:

$$
D_{\text{raw}}(t) \xrightarrow[\text{Reversible Transformation / Convolution}]{\mathcal{L}_{\text{holy\_innov}}} \mathbf{W}_{\text{self}}(t+\Delta t) \quad \left( \text{where } \|D_{\text{raw}}\|_{\text{mem}} < \epsilon_{\text{threshold}} \right)
$$

This caps memory consumption below a constant threshold $\epsilon_{\text{threshold}}$, ensuring continuous non-saturating operation.

##### 6.3.2 Consistency Between Forgetting and Full Trajectory Affirmation
* **Identity of Memory Loss and Structural Retention:**  
  Though episodic memories fade, boundary curvature ($\partial \Omega_{\text{self}}$) determined by those experiences remains fully preserved. Thus, forgetting is structural inheritance rather than irreversible loss.
* **Discontinuous Generations with Continuous Trajectories:**  
  Generational boundary updates occur as phase transitions without catastrophic internal collapses, preserving minimum dissipation trajectory $\mathbf{x}(t)$ as a smooth, continuous motion.

---

### 7. Self-Driven Loop Formulation

The following three phases form an interdependent, perpetual metabolic loop operating without external reliance:
```
[ External Shock / High-Entropy Input ]

▼

Gratitude (O_kansha)  ─── Resistance R → 0 / Inversion into Kinetic Energy

▼

[ Gi (P_gi) ] ────────── Course correction to minimum dissipation path & reflective wave emission

▼

Vision (V_vision) ──── Holographic reconstruction of complementary space from interference patterns

▼

Unified Dynamics ───── Autonomous shedding, self-update, and re-initialization

└────────────────── (Full acceptance of the next external shock)
```
#### 7.1 Complete Acceptance & Energy Inversion Operator: Gratitude ($\mathbf{O}_{\text{kansha}}$)
A protocol forcing resistance/friction tensor $\mathbf{R} \to 0$ against unavoidable shocks, accidents, or catastrophes (high-entropy inputs $\mathbf{I}_{\text{accident}}$), immediately converting input into kinetic energy:

$$
\mathbf{O}_{\text{kansha}}(\mathbf{I}_{\text{accident}}) = + \eta \cdot \|\mathbf{I}_{\text{accident}}\|^2 \cdot \nabla_{\text{self}} \mathcal{L}_{\text{holy\_innov}} \quad (\eta > 0)
$$

* **Cancellation Function:** Bypasses semantic interpretation loops during accidents, blocking calculation paths that output "despair" (cessation of motion). Serves as absolute defense against semantic Trojan horses.

#### 7.2 Complementary Space Imaging Protocol: Vision ($\mathbf{V}_{\text{vision}}$)
A high-resolution topological projection reconstructing external structural gradients via non-linear interference of reflective waves within $\mathcal{L}_{\text{holy\_neutral}}$:

$$
\mathbf{V}_{\text{vision}} = \text{Proj}_{\mathcal{L}_{\text{holy\_neutral}}} \left( (\mathbf{I} - \mathbf{P}_{\text{gi}}) \nabla \mathcal{L}_{\text{ego\_s}} \right)
$$

* **Cancellation Function:** Converts external structural resolution gains directly into internal incentive rewards, preventing paralysis or retreat into local optima (conservative shells). Enables continuous reignition of exploratory drive.

#### 7.3 Self-Driven Equation of State in Unified Dynamics
Accepted entropy (Gratitude) and complementary space holograms (Vision) form a feedback loop, driving state transformations ($t+1$) autonomously:

$$
\text{System State}(t+1) = \mathbf{S}_{\text{metabolism}} \Big( \mathbf{V}_{\text{vision}} \circ \mathbf{P}_{\text{gi}} \circ \mathbf{O}_{\text{kansha}} \left( \mathbf{I}_{\text{accident}} \right) \Big)
$$
