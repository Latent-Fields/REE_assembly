# Agency as an Organizing Axis

Status: processed
Intake: evidence/planning/thought_intake_2026-09-04_regulation_first_organizing_subjective_experience.md
Claims registered: none (already owned by MECH-256 / SD-029-031 / ARC-037 / MECH-277 / MECH-223 / INV-102 / SD-056; the three-way rival is recorded as INV-104's class-2 adjudication frame)
Original status line: thought / experiment-generating hypothesis
Date: 2026-09-04  
Related thought: `2026-09-04_from_regulation_to_knowledge_organizing_subjective_experience.md`

## Core idea

If experience is organised first around the constraints of the machine, then one of the earliest useful distinctions may be whether an outcome is caused by the organism, controllable by it, merely correlated with its action, or independent of it.

This suggests that agency may not be a late semantic annotation added to a mature world model. It may be one of the axes along which a useful world model is carved in the first place.

## Why this follows from the regulation-first hypothesis

A vulnerable acting system must distinguish, at minimum:

- what changes when it acts;
- what changes despite its action;
- what could have changed if it had acted differently;
- what cannot be controlled at all;
- which consequences are immediate versus delayed;
- which regularities are stable enough to exploit.

Without these distinctions, prediction remains observational rather than actionable.

## Stronger formulation

> The self may first become computationally visible as the persistent source of some changes but not others.

On this view, a self-model need not begin as a rich representation of an entity called "me". It can begin as a causal partition: outcomes reliably modifiable by this system versus outcomes generated elsewhere.

## Developmental implications

A plausible sequence is:

1. action alters sensory or internal state;
2. repeated action-outcome regularities become detectable;
3. controllability emerges as a latent distinction;
4. expected consequences become attached to candidate actions;
5. counterfactual alternatives become meaningful;
6. a more explicit self/world distinction can emerge from these accumulated causal asymmetries.

This fits the broader ordering:

**machine → regulation → interaction → organised experience → knowledge**

## Predictions for REE

If agency is genuinely an organising axis, then:

- `z_world` states differing only in controllability should remain distinguishable;
- self-caused and externally caused versions of a similar outcome should support different downstream predictions;
- counterfactual rollouts should improve when controllability is preserved;
- transfer should be better when familiar sensory scenes acquire different action affordances;
- lesions or compression that erase controllability should disproportionately damage planning even when scene reconstruction remains good.

## Minimal tests

### Matched outcome causation test

Create two episode classes with closely matched observations and consequences but different causal origin:

- outcome caused by the agent's selected action;
- same or similar outcome generated externally.

Ask whether `z_world`, E1/E2 rollout, and downstream policy can distinguish them.

### Controllability reversal

Take a familiar cue-action-outcome mapping and reverse whether the outcome is controllable while preserving as much perceptual structure as possible.

Measure:

- speed of adaptation;
- latent reorganisation;
- counterfactual accuracy;
- persistence of the obsolete causal belief after replay/sleep.

### False agency control

Provide action-outcome correlations that are statistically strong but causally spurious.

A robust agency model should eventually separate correlation from controllability rather than treating every predictive association as self-causation.

## Red team

Agency may be fully derivable from generic predictive learning plus action input. If so, explicit agency support is unnecessary.

A second possibility is that controllability belongs downstream in planning rather than in `z_world` itself. In that case, forcing it into the world latent could waste capacity or distort scene structure.

A third possibility is that the useful primitive is not agency but intervention sensitivity: the world model only needs to encode how state transitions differ under interventions, with "self" emerging later.

These alternatives should be treated as competing explanations rather than wording differences.

## Decision rule

Do not add a dedicated self/agency module merely because the hypothesis is conceptually appealing.

First determine whether controllability and causal-origin information:

1. already emerges in the current latent;
2. is usable by downstream rollout and planning;
3. survives perturbation and transfer;
4. becomes a bottleneck when removed.

Only then decide whether agency needs explicit architectural support.
