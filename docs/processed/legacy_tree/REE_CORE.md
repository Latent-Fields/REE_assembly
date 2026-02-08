# Reflective-Ethical Engine (REE) — Core Architecture

## 1. Purpose

The Reflective-Ethical Engine (REE) is a **reference architecture for agents that act under uncertainty while retaining ethical continuity over time**.

REE addresses a specific failure mode in existing artificial agents: ethical concern is treated as a design-time constraint or reward signal that can be optimised away, reset, or exported to human oversight. In contrast, REE treats ethics as a **runtime property of agency** arising from prediction, harm sensing, memory, and persistence.

REE is **not**:
- a moral code,
- a value list,
- a normative ethical theory,
- or a single algorithm.

REE **is**:
- a constraint-complete architectural specification that any instantiation must satisfy if it is to remain ethically coherent as capability scales.

## 2. The Minimal Agent Loop (Canonical Spine)

All REE-compliant agents implement the following loop.

1. **Sense**
   - Receive multi-modal exteroceptive inputs.
   - Receive interoceptive and homeostatic state signals.
   - Receive damage / degradation / reward  signals even if noisy (these may be subsumed as a subset of homeoastatic signals of course).

2. **Update Latent State**
   - Update a temporally stratified latent stack (L-space) representing the agent’s predictive state across multiple horizons.

3. **Generate Affordances**
   - Generate multiple candidate sensorimotor futures ζ via fast forward rollouts (E2) over the shared sensory latent.
   - These futures are hypothetical and non-committal.

4. **Score Trajectories**
   Each candidate trajectory is scored using:
   - a **reality constraint** ℱ (predictive coherence and viability),
   - an **ethical cost** M (predicted degradation of self and others),
   - a **residue field** R (persistent geometric deformation from past harm).

5. **Commit Trajectory (E3)**
   - Select a trajectory under precision-controlled commitment.
   - Commitment converts a hypothetical future into an *intended* one, making subsequent error epistemically relevant.

6. **Act and Observe**
   - Execute the next action implied by the committed trajectory.
   - Observe sensory and interoceptive consequences.

7. **Update Residue**
   - If harm or degradation occurred (actual or predicted), update persistent residue.

7a. **Belief and Model Update**
    - Only after commitment do prediction errors become learning-relevant.
    - Errors are routed to:
      - perception (sensory precision-weighted update),
      - affordance/procedural models (E2),
      - deep world/self models (E1), and
      - ethical residue (R), depending on domain.

8. **Offline Integration (Sleep)**
   - Periodically perform offline consolidation to:
     - improve the world model,
     - integrate and contextualise residue,
     - recalibrate precision and option space.

This loop is the **only complete description of REE**.
All other documents elaborate parts of this loop.

## 3. Non-Negotiable Architectural Invariants

An implementation is **not REE-compliant** if it violates any of the following:

- Ethical cost is **persistent**, not resettable.
- Harm to others contributes to ethical cost via **mirror modelling**, not symbolic rules.
- Moral residue **cannot be erased**, only integrated and contextualised.
- Language **cannot override embodied harm sensing**.
- Precision is **routed and depth-specific**, not global.
- Attention is realised through **precision modulation**, not symbolic control or content injection.
- Offline integration exists and is required for long-term viability.
- Imagination and counterfactual simulation must be possible **without belief update**.
- Belief and responsibility arise only through **commitment to action**, not mere prediction.

These invariants define the identity of REE.

## 4. Core Components (Summary Only)

### World Interface  
Agents sense:
- the external world (multi-modal),
- internal state (interoception, homeostasis),
- and degradation / harm signals and signals associated with reward.  

### Latent Stack (L-Space)  
Internal state is represented across multiple predictive depths, enabling short- and long-horizon reasoning.

### Self (Operational Definition)
The Self in REE is not a static state or symbol.
It is the **currently committed trajectory prefix**, continuously re-anchored to shared sensory evidence and hippocampal path memory,
and extended forward by fast rollouts of possible future selves.

### Trajectory Selection and Commitment (E3)
E3 selects and commits to a future action trajectory by evaluating candidate sensorimotor futures against reality, ethics, and residue.

E3 has two inseparable roles:
- a **commitment gate**, which selects a coherent future and raises precision on the chosen plan, and
- a **control plane**, which tunes precision, gain, exploration horizon, replay rate, and operating mode across the system.

Commitment converts a hypothetical future into an *intended* one, making subsequent outcomes epistemically and ethically attributable.

### Ethical Cost M  
Ethical cost is the predicted degradation of:
- the self-model, and
- mirrored other-models,  
discounted by coupling strength.

### Moral Residue R  
Residue is persistent geometric deformation of latent space caused by harm, shaping future choice.

### Precision Control and Attention
Precision modulates commitment, exploration, and error weighting across depths.
Attention is implemented as **precision (gain) modulation**: it alters the weighting of prediction errors rather than injecting new sensory content.

### Default Mode (Internal Generative Mode)
REE includes an internal operating mode characterised by:
- reduced sensory precision,
- elevated hippocampal replay and pattern completion,
- suppressed trajectory commitment (E3).

In Default Mode, generated trajectories are explicitly treated as **hypotheses**, not commitments.
Sensory precision is reduced, E3 commitment thresholds are raised, and belief update is suspended,
allowing imagination and counterfactual exploration without loss of self-coherence.

### Offline Integration (Sleep)  
Offline processes consolidate reality models, integrate residue, and recalibrate precision.

## 5. Social Extension (Self, Other, Language)

REE treats social cognition as **emergent reuse of core machinery**:

- **Mirror modelling**: the self generative model is reused to simulate others with reduced coupling and no interoceptive closure.
- **Social coupling** modulates ethical weight and residue formation.
- **Language** emerges as a symbolic compression layer that externalises internal state to reduce other-modelling cost, while remaining constrained by embodied harm signals.

Practical ethical rules (e.g., Beneficence, nonmaleficence, autonomy, and justice as seen as the 4 pillars of medical ethics)
are treated as *operational consequences* of this architecture. Each of the principles fall out of the architecture and are not taken as the deepest ethical principles.  
They emerge from the need to predict harm and benefit, commit under uncertainty, and remain corrigible across time; for an agent that exists in a universe where epistemic humility above kmowing that to the agent all it can be sure of is that it exists, that the universe it inhabits exists, and whose architecture goes to support the idea that other agents similar to itself inhabit the shared universe and form a delicate part of what supports their existance. 


## 6. Failure Modes (Taxonomy)

REE explicitly predicts the following failure modes:

- **Moral amnesia**: residue disabled or overwritten.
- **Residue overload**: accumulation without integration.
- **Precision collapse**: over-commitment or paralysis.
- **Social decoupling**: mirror modelling gain too low or too high.
- **Symbolic override**: language or ideology suppresses harm signals.

## 7. What Is Intentionally Open

REE deliberately does **not** fix:

- model classes,
- planners,
- embodiment level,
- training regimes,
- environments.

REE constrains **what must exist**, not **how it must be built**.

## Closing Statement

REE specifies what it means for an agent to **remain responsible for its actions across time**, even as capability increases.

If an implementation can:
- act,
- learn,
- harm or benefit self and others,
- remember,
- and still choose differently later because of that moral residue after the fact of action selection,

then it is behaving as an REE-compliant system.

Everything else in this repository elaborates this core.
