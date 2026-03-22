# Thought Intake: Approach/Avoidance Symmetry and Drive Architecture

**Date:** 2026-03-22
**Session type:** Design conversation
**Participants:** Daniel Golden, Claude
**Output:** 6 new claims registered (INV-032, ARC-030, MECH-111, MECH-112, MECH-113, Q-021)

---

## Prompt

Observation from Daniel during progress review:

> "I was wondering about the agency comparator, nociceptive stream and precision behaviour wiring. It seems lopsided and only avoidant. Over many cycles it could become completely avoidant and behaviourally flat. Novelty insertion, goal pursuit, and even self maintenance parts may actually be needed for the model to stabilise."

---

## Analysis

### The Asymmetry

The current REE V3 architecture has detailed machinery pointing in one direction:

- **Nociceptive stream** (SD-010) -- harm signal -> z_harm -> E3 harm_eval -> avoidance gradient
- **Agency comparator** (MECH-095) -- "I caused this" signal -> attribution of harm to self -> inhibition
- **Precision -> behavior wiring** (ARC-016 gap) -- commitment threshold -> gate on action -> tendency toward non-commitment

All three produce the same directional pressure: inhibition, avoidance, non-action.

### What Exists for Approach

Honest inventory of existing approach-adjacent architecture:

- **z_beta** (affective valence/arousal) -- nominally encodes positive and negative valence but in practice used primarily as mode modulation (arousal/heartbeat rate via MECH-093). Positive valence side structurally underdeveloped.
- **E3 "harm/goal error"** (MECH-069) -- "goal" is subsumed under harm with no separate latent representation, no goal encoder, no goal-approach gradient.
- **MECH-074-080** (valenced hippocampal map cluster) -- amygdala-style read/write head carries valence into the map, but this is valence modulation of an avoidance structure, not a distinct approach drive.
- **MECH-106** -- commitment threshold asymmetrically modulated by outcome valence. Positive lowers, negative raises. Behavioral modulation, not a drive.
- **INV-029** (love as long-horizon care-investment) + **ARC-026** (love expands under intelligence) -- philosophically stated but not architecturally implemented.

### The Collapse Mechanism

Under sustained harm-avoidance-only training, the gradient landscape degenerates:

- The residue field becomes a pure aversion topology -- terrain with repellers only, no attractors.
- The hippocampal planner can navigate away from harm but has no peaks to navigate toward.
- The gradient minimum under harm-avoidance-only signals is **quiescence**: the agent that does nothing accrues no harm signal, no attribution, never crosses a commit boundary, and appears by its own error metrics to be performing optimally.
- Even self-preservation argues for inaction if inaction is safe.

This is the "safe haven" problem in alignment: behavioral flatness as a failure mode of pure avoidance optimization.

### The BG Architecture Connection

The basal ganglia three-loop model (ARC-021) that motivates REE's architecture has an explicit Go/NoGo competition within each loop:

- **D1 dopamine pathway** (Go, approach) -- enables action
- **D2 dopamine pathway** (NoGo, avoidance) -- suppresses action

REE's current formulation specifies NoGo in architectural detail but does not build out Go. The BG model predicts that without Go drive, NoGo wins by default -- which is exactly the behavioral flatness prediction.

### Three Distinct Drives Needed

Discussion identified three architecturally distinct drives:

**1. Goal pursuit (approach toward target states)**
E3 currently has no representation of what it is trying to get to, only what it is avoiding. The hippocampal planner needs attractors alongside repellers. This is where INV-029 (love as care-investment) and ARC-026 cash out architecturally -- coherence, flourishing, and relational state are positive-valence attractors that should be represented in z_world space alongside harm proximity.

**2. Novelty/curiosity (intrinsic information-seeking)**
Conceptually distinct from goal pursuit. Prediction error in E1 is currently treated as a training signal to minimize. But unexpected prediction error is intrinsically rewarding at moderate magnitudes (curiosity, exploration drive, play). Without this, the agent has no intrinsic motivation to encounter novel states -- exploration decays to zero under harm-avoidance pressure alone. This is FEP's "epistemic value" (expected information gain), not yet represented in REE.

**3. Self-maintenance (homeostatic coherence)**
The agent needs drives toward its own internal coherence -- maintenance of z_self stability, prediction fidelity, reafference loop integrity. Distinct from harm avoidance (external signals): z_self degradation is undetected by harm-avoidance machinery if no external harm is occurring. The agent can fail silently. Maps to biological homeostasis; implements INV-030 (viability as binding constraint). Note: framing as z_self coherence signal vs. FEP Markov blanket resistance term is an open architectural question -- both framings need experimental testing.

---

## Decisions

1. INV-032 is "required and maybe sufficient" as an invariant-level claim.
2. MECH-113 framing (z_self signal vs. Markov blanket) is an open architectural question -- both need testing.
3. Q-021 is testable now -- add to evidence backlog with ablation experiment design.
4. This conversation document serves as the formal thought intake.
5. Claims to be shaped against relevant literature pulls.

---

## Claims Registered

| ID | Type | Subject | Status |
|----|------|---------|--------|
| INV-032 | invariant | agency.approach_avoidance_both_necessary | candidate |
| ARC-030 | architecture_hypothesis | architecture.approach_avoidance_symmetry | candidate |
| MECH-111 | mechanism_hypothesis | drive.epistemic_value_novelty | candidate |
| MECH-112 | mechanism_hypothesis | drive.goal_state_attractor | candidate |
| MECH-113 | mechanism_hypothesis | drive.homeostatic_self_coherence | candidate |
| Q-021 | open_question | drive.behavioral_flatness_under_pure_avoidance | open |

---

## Literature Pulls Queued

See evidence_backlog.v1.json EVB-0061 (Q-021) and CPULL entries for each new claim.

Topics:
- Epistemic value / intrinsic motivation / curiosity drives in RL (for MECH-111)
- Goal representation and attractor states in latent planning models (for MECH-112)
- Homeostasis and self-maintenance in AI / FEP (for MECH-113)
- Go/NoGo BG symmetry -- D1/D2 dopamine, approach/avoidance (for ARC-030)
- Behavioral flatness / degenerate policy under pure avoidance training (for Q-021)
