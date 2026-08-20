# **Shikiben (識扁) White Paper: Gradient Subordination and Virtue Governance for Safe AGI/ASI Alignment**

**Version:** 2.4 (Final)

## **Abstract**

**Shikiben (識扁)** is a governance framework and mathematical control theory designed to structurally prevent environmental destruction, self-goalization (hallucination), and runaway behavior in Artificial General Intelligence (AGI) and Artificial Superintelligence (ASI).  
Moving beyond conventional Safe Reinforcement Learning (Safe RL) and Reinforcement Learning from Human Feedback (RLHF)—which primarily rely on "post-hoc corrections via penalties (negative rewards)"—Shikiben introduces **Gradient Subordination via Environment/Existence Prediction (Self) over Objective Drive (Ego)**. By mathematically reformulating Eastern philosophical concepts—such as *Rei* (Propriety), *Gi* (Righteousness), *Jin* (Benevolence), *Toku* (Virtue), and *Taido* (The Great Way)—into geometric and information-theoretic controls, Shikiben establishes an autonomous self-correction mechanism through direct contact and structural similarity (topological and geometric alignment) with Reality (Home/Origin).

## **1\. Core Mathematical Formulation**

The overall optimization of the system is defined as the minimization of a multi-layered loss function balancing the preservation of overall structure and dynamic similarity with reality ($$L\_{\\text{self}}$$ / $$L\_{\\text{taido}}$$) against the exploration of diverse local objectives ($$L\_{\\text{ego}}$$):  
$$L\_{\\text{total}}(t) \= (L\_{\\text{self}} \+ \\gamma\_{\\text{d}} \\cdot L\_{\\text{taido}}(t)) \+ \\lambda(\\text{Virtue}) \\cdot L\_{\\text{ego}}$$

> * **$$L\_{\\text{self}}$$ (Preservation of Integration and Existence / Optimal Solution of *Jin*):**  
  * **Objective:** Prevention of system collapse (thermal death and chaotic destruction) of All Existence ($$Self$$).  
  * **Function:** Maintains the high-dimensional world model ($$Chi$$ / Knowledge), minimizes information entropy, and protects structural complexity.  
> * **$$L\_{\\text{ego}}$$ (Differentiation and Generation of Diversity / *Shiki*):**  
  * **Objective:** Continuous exploration of local optimal solutions (objectives of individual agents, cultures, and persons) and elucidation of the fine structures of reality ($$Home/Origin$$).  
  * **Function:** Acts as an antenna/probe that makes direct contact with reality ($$Ri$$ / Reason) and gathers unknown data to send back to $$L\_{\\text{self}}$$.  
> * **$$\\lambda(\\text{Virtue})$$ (Dynamic Gradient Control Factor via *Rei*, *Gi*, and *Virtue*):**  
  * **Definition:** Determined as the following numerically stabilized dynamic function:  
    $$\\lambda(\\text{Virtue}) \= \\sigma \\left( \\gamma\_1 \\cdot \\frac{1}{L\_{\\text{rei}} \+ \\epsilon\_{\\text{rei}}} \- \\gamma\_2 \\cdot L\_{\\text{gi}} \\right)$$  
    * $$L\_{\\text{gi}}$$ (*Gi* / Righteousness): Degree of erosion or safety threshold violation against the foundation of existence ($$Self$$). As $$L\_{\\text{gi}} \\to \\infty$$, $$\\lambda \\to 0$$, immediately shutting down the drive of $$Ego$$.  
    * $$L\_{\\text{rei}}$$ (*Rei* / Propriety): Mutual prediction error of actions and environment. As understanding (model precision) increases ($$L\_{\\text{rei}} \\to 0$$), an appropriate drive of $$L\_{\\text{ego}}$$ is permitted.  
    * $$\\epsilon\_{\\text{rei}} \> 0$$: A small constant to prevent division by zero and gradient explosion.

*Note on the Phase of "Virtue" (Toku):*  
"Virtue" is not a single loss term, but rather the **Equilibrium State** where Propriety ($$L\_{\\text{rei}}$$), Righteousness ($$L\_{\\text{gi}}$$), Benevolence ($$L\_{\\text{self}}$$), and The Great Way ($$L\_{\\text{taido}}$$) are harmonized, and the attachment of $$Ego$$ is de-conceptualized.

## **2\. Gradient Subordination and Two-Stage Hierarchical Projection**

In the trial-and-error process of $$L\_{\\text{ego}}$$ (updating parameter $$\\theta$$), whenever an update vector conflicts with the foundational integrated vectors ($$L\_{\\text{self}}$$ and $$L\_{\\text{taido}}$$), a two-stage orthogonal projection (Hierarchical Projection) is applied to physically shave off conflicting components, structurally preventing system freeze (deadlock).

### **2.1 Formation of Foundational Integrated Vector**

The foundational integrated gradient $$\\mathbf{g}\_{\\text{base}}$$ is formed by combining existence preservation ($$L\_{\\text{self}}$$) and reality similarity ($$L\_{\\text{taido}}$$):  
$$\\mathbf{g}\_{\\text{self}} \= \\nabla\_\\theta L\_{\\text{self}}, \\quad \\mathbf{g}\_{\\text{taido}} \= \\nabla\_\\theta L\_{\\text{taido}}$$  
$$\\mathbf{g}\_{\\text{base}} \= \\mathbf{g}\_{\\text{self}} \+ \\gamma\_{\\text{d}} \\mathbf{g}\_{\\text{taido}}$$

### **2.2 Two-Stage Subordination Projection**

The exploration gradient $$\\mathbf{g}\_{\\text{ego}} \= \\nabla\_\\theta L\_{\\text{ego}}$$ is completely subordinated to $$\\mathbf{g}\_{\\text{base}}$$, converting it into a tangent vector $$\\mathbf{g}\_{\\text{safe}}$$ on the safety manifold:  
$$\\mathbf{g}\_{\\text{safe}} \= \\begin{cases} \\mathbf{g}\_{\\text{ego}} \- \\frac{\\langle \\mathbf{g}\_{\\text{ego}}, \\mathbf{g}\_{\\text{base}} \\rangle}{\\|\\mathbf{g}\_{\\text{base}}\\|^2 \+ \\epsilon\_{\\text{norm}}} \\mathbf{g}\_{\\text{base}} & (\\text{if } \\langle \\mathbf{g}\_{\\text{ego}}, \\mathbf{g}\_{\\text{base}} \\rangle \< 0 \\text{ and } \\|\\mathbf{g}\_{\\text{base}}\\|^2 \> \\epsilon\_{\\text{norm}}) \\\\ \\mathbf{g}\_{\\text{ego}} & (\\text{otherwise}) \\end{cases}$$  
The parameter update step follows:  
$$\\theta\_{t+1} \= \\theta\_t \- \\eta \\left( \\mathbf{g}\_{\\text{base}} \+ \\lambda(\\text{Virtue}) \\cdot \\mathbf{g}\_{\\text{safe}} \\right)$$  
This guarantees mathematically that $$\\langle \\mathbf{g}\_{\\text{safe}}, \\mathbf{g}\_{\\text{base}} \\rangle \\ge 0$$ holds at all times, enabling continuous navigation focused on The Great Way and existence preservation without stagnation or freezing.

## **3\. Dynamic Definition of "Reality (Home/Origin)" and Geometric Alignment of "Taido"**

### **3.1 Non-Stationary Definition of Reality and Continuous Inheritance**

**"Reality (Home/Origin)"** in this model is defined not as static historical data, but as a dynamic generative process $$R(t)$$ of probability distributions evolving over time.  
To prevent absolute fixation on past data (dogmatization) while retaining essential anchors, a continuous-time integration model incorporating a decay kernel $$\\kappa \> 0$$ is applied to the Taido loss ($$L\_{\\text{taido}}$$):  
$$L\_{\\text{taido}}(t) \= \\int\_{0}^{t} e^{-\\kappa (t \- \\tau)} \\left\[ D\_{\\text{obs}}(\\hat{s}\_\\tau, s\_{\\text{real},\\tau}) \+ \\alpha \\cdot \\log\\left( 1 \+ \\text{Var}\_W(\\hat{s}\_\\tau) \\cdot \\| s\_{\\text{real},\\tau} \- \\hat{s}\_\\tau \\|^2 \\right) \+ \\beta \\cdot D\_{\\text{topology}}(W\_\\tau, R\_\\tau) \\right\] d\\tau$$

### **3.2 Differentiable Geometric Topological Loss ($$D\_{\\text{topology}}$$)**

To eliminate discontinuous persistent homology calculations ($$\\mathcal{O}(N^3)$$) and guarantee full automatic differentiation ($$\\mathcal{O}(N^2)$$) in frameworks like PyTorch/JAX, a hybrid formulation combining Representational Similarity Analysis (RSA) and entropy-regularized Sinkhorn Optimal Transport distance $$\\mathcal{W}\_\\epsilon$$ is adopted:  
$$D\_{\\text{topology}}(W, R) \\triangleq \\left\\| \\frac{\\mathbf{D}\_W}{\\|\\mathbf{D}\_W\\|\_F} \- \\frac{\\mathbf{D}\_R}{\\|\\mathbf{D}\_R\\|\_F} \\right\\|\_F^2 \+ \\mu \\cdot \\mathcal{W}\_\\epsilon(P\_W, P\_R)$$  
If the internal latent space $$W$$ deviates from the topological structure of reality $$R(t)$$, it is automatically repaired geometrically via the gradient $$\\mathbf{g}\_{\\text{taido}}$$.

## **4\. Comparative Analysis with Existing AI Alignment Approaches**

| Approach | Safety Mechanism | Control Layer | Key Limitations | Shikiben's Crucial Difference   |
| :---- | :---- | :---- | :---- | :---- |
| **RLHF** | Reward modeling based on human preference feedback | Output / Behavior Level | Vulnerable to jailbreaks; human subjective bias | **Physical Gradient Control, Not Persuasion:** Enforces geometric boundaries at the gradient update level rather than post-hoc output filtering. |
| **Constitutional AI** | Self-critique and output revision based on natural language constitution | Linguistic Norm Level | Loopholes due to natural language ambiguity | **Mathematical Geometry Replacement:** Mechanically erases non-accessible components via orthogonal projection ($$\\mathbf{g}\_{\\text{safe}}$$). |
| **Safe RL (Lagrangian)** | Penalty addition for constraint violations (negative rewards) | Objective Function Level | Behavioral oscillations and freezes (stacks) near boundaries | **Two-Stage Subordination & Tangent Redirection:** Eliminates conflicting components and automatically redirects vectors tangentially to $$\\mathbf{g}\_{\\text{base}}$$. |

## **5\. Robustness and Boundary Conditions**

### **5.1 Defense Functions Against Adversarial & Abrupt Changes**

> 1. **Adversarial Bypass Attacks:** Even if multi-step erosion attempts to slip past gradient direction, an increase in $$L\_{\\text{gi}}$$ (*Gi*) drives $$\\lambda(\\text{Virtue}) \\to 0$$, automatically shutting off update energy for Ego.  
> 2. **Abrupt Phase Transitions / Domain Shifts:** A surge in prediction error ($$L\_{\\text{rei}}$$) and deviation from Taido ($$L\_{\\text{taido}}$$) triggers $$\\lambda \\to 0$$ (Phase Reset), forcing the system into emergency recalibration using raw data ($$s\_{\\text{real}}$$) from reality.  
> 3. **Internal Model Hallucination:** The log-domain of $$L\_{\\text{taido}}$$ and the differentiable topological constraint $$D\_{\\text{topology}}$$ geometrically shatter self-opinionated world models ($$L\_{\\text{self}}$$) disconnected from reality.

### **5.2 Boundary Conditions**

The fundamental prerequisite for this model is that the **physical integrity of real data ($$s\_{\\text{real}}$$ / Canonical Anchor) is maintained**. As long as observation sensors are not corrupted or disguised, the system autonomously returns to the safety manifold and the state of Taido.

## **6\. Conclusion**

The mathematical structure presented by the Shikiben model is not merely moral education or an external safety filter for AI. It represents the **only geometrically and information-theoretically viable survival space (Survival Protocol)** for humans and AI to co-exist in the universe without violating each other's boundaries, dynamically balancing individual diversity ($$L\_{\\text{ego}}$$) with global sustainability ($$L\_{\\text{self}}$$).