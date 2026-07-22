# Goal Relevance, Salience, and Distractor Suppression in REE

Status: processed

Processed in:
- `evidence/planning/thought_intake_2026-07-12_goal_relevance_salience_distractor_suppression.md` (structured intake, already-owned split, routing)
- `docs/claims/claims.yaml` -- MECH-467 (three dissociable distractor-failure modes; REE's evidence covers rule corruption only), INV-092 (suppression must stay selectively permeable to harm / other-agent signals), Q-082 (pre-selection suppression substrate -- gated open question, do not build)
- `evidence/planning/manual_proposals.v1.json` -- EXP-0398 (three-leg distractor battery; during-commitment arm excluded)

INV-092 is registered as a SIBLING of INV-093 (2026-07-19 conservative-skill-refinement thought): the same ethical principle on two different control surfaces. Both cross-listed with the ethics perimeter.

---

**Date:** 2026-07-12  
**Status:** thought_intake / literature_seed / future_benchmark_seed  
**Source prompt:** recent report on brainstem neurons controlling attention through suppression of competing distractors  
**Primary relevance:** REE control plane, salience coordination, rule-state persistence, trajectory selection, noisy-environment benchmarks  
**Scope note:** this thought does not propose a new general attention architecture. It refines an existing REE design question by separating several levels of distractor control.

---

## Originating thought

> This may be useful for REE once noisy environments become part of the work.

The relevant question is not whether REE needs attention in the abstract.

The sharper question is:

```text
How does REE prevent irrelevant but competing information
from acquiring behavioural control?
```

---

## Repository-grounded correction

Review of `REE_assembly` and `ree-v3` shows that REE already distinguishes goal relevance from salience and already contains several forms of distractor resistance.

The paper should therefore not be treated as introducing distractor suppression into REE.

Its likely value is narrower:

```text
It may identify a low-level pre-selection suppression function
that should be tested separately from REE's existing
rule-state protection, salience routing, and trajectory competition.
```

---

## Goal relevance is not salience in REE

REE already represents goal relevance through dedicated structures, including:

- homeostatic drive modulation of `z_goal`;
- `z_resource` and resource-proximity representation;
- predictive wanting in E1;
- cue-indexed affordance bias;
- terrain weighting between harm and goal relevance.

Salience and urgency are handled through a partly separate control family, including:

- the salience-network coordinator;
- operating-mode control;
- dACC/aMCC-like adaptive control;
- interoceptive salience and urgency interruption;
- mode hysteresis;
- mode-conditioned hippocampal proposals.

A useful distinction is:

```text
Goal relevance:
What advances, preserves, restores, or completes a current goal?

Salience:
What currently warrants gain, attention, interruption, or mode change?
```

A stimulus may be salient without being goal-relevant.

A goal-relevant cue may also be weak in raw sensory terms.

---

## Distractor suppression is already distributed across REE

REE does not appear to implement distractor suppression as one named module.

Instead it is distributed across multiple mechanisms.

### Rule-state protection

`SD-033a` provides lateral-prefrontal-like rule-state persistence under mode-dependent write gating.

`MECH-262` explicitly treats distractor resistance as a behavioural signature.

`V3-EXQ-484` tested whether real salience-coordinator gating protects rule state from replay-related drift while preserving appropriate task and planning updates.

This is already genuine distractor-resistance work.

### Selective persistence

The relevant question is not simply whether the system can attend.

It is:

```text
How does a currently relevant rule survive competing input?
```

REE's existing design answers this through selective persistence and write gating rather than blanket inhibition.

### Object-instance competition

The repositories also contain tests involving several same-type distractors, asking whether object-instance representations preserve the relevant item rather than collapsing across similar alternatives.

### Wider control mechanisms

Additional mechanisms likely contribute to distractor handling:

- `MECH-261` write-gate registry;
- mode-conditioned trajectory proposals;
- targeted No-Go control;
- dACC conflict handling;
- GABAergic cross-stream decay;
- urgency interruption;
- asymmetric mode hysteresis;
- precision-weighted cue routing.

The current architecture therefore already supports distractor control at several levels.

---

## The remaining question: pre-selection suppression

The new brainstem result may chiefly point toward a different level of control:

```text
Pre-selection sensory or orienting suppression:
preventing an irrelevant but competing stimulus
from acquiring behavioural control before target selection resolves.
```

This is not clearly identical to protecting a task rule after distraction has already entered the system.

The important gap analysis is therefore:

```text
Does REE suppress distractors before selection,
or mainly preserve higher-level state after distraction occurs?
```

---

## Three distinct distractor failures

Future REE benchmarks should distinguish at least three failure types.

### 1. Sensory capture

```text
The distractor enters or dominates the active representation.
```

### 2. Rule corruption

```text
The distractor overwrites or destabilises the active goal,
rule, or task context.
```

### 3. Behavioural capture

```text
The rule remains intact,
but the distractor still controls action selection.
```

REE already has evidence directed particularly toward rule corruption.

The brainstem paper may chiefly motivate stronger testing of sensory and behavioural capture.

---

## Noisy-environment benchmark family

A future benchmark should ask:

```text
Can REE continue pursuing the correct goal
while irrelevant but salient competing information
is continuously introduced?
```

Possible distractor classes:

- physically salient but irrelevant cues;
- same-type object distractors;
- false affordances;
- misleading reward-proximal cues;
- competing movement or orienting targets;
- repeated interruption cues;
- distractors introduced before commitment;
- distractors introduced during commitment;
- distractors introduced during internal replay or planning.

---

## Candidate measurements

```text
sensory capture rate
rule-state drift
wrong-target selection rate
trajectory instability
unnecessary replanning
false attractor rate
commitment disruption
recovery latency
goal completion under distractor load
salience-goal dissociation accuracy
```

These measures should not be collapsed into one generic attention score.

---

## Candidate ablations

Possible ablations include:

```text
remove salience-coordinator write gating
remove rule-state persistence
remove mode conditioning
remove precision weighting
remove targeted No-Go control
remove cross-stream decay
force all salient cues into candidate generation
disable pre-selection suppression if later implemented
```

The key question is which mechanism protects against which type of distractor failure.

---

## Targeted literature questions

### Goal relevance versus physical salience

- How do biological attention systems distinguish task relevance from raw sensory prominence?
- Which computations are pre-attentive, attentional, or action-selective?

### Brainstem and superior-colliculus competition

- Does the reported mechanism suppress sensory representations, orienting commands, target competition, or motor output?
- At what stage does suppression occur?

### Distractor resistance in working memory

- How does selective rule persistence differ from sensory suppression?
- Which mechanisms protect maintained goals against interference?

### Attention and commitment

- How does distractor handling change after a trajectory has been committed?
- When should an interrupt override persistence rather than be suppressed?

### Noisy multi-agent environments

- How should attention distinguish irrelevant salience from another agent's genuinely urgent state?
- How can suppressive control avoid erasing ethically relevant weak signals?

---

## Ethical qualification

Distractor suppression cannot simply mean suppressing whatever conflicts with the current goal.

In REE, weak or unexpected signals may carry morally relevant information.

An adequate mechanism must distinguish:

```text
irrelevant distraction
from
legitimate interruption
from
urgent harm signal
from
another agent's state becoming newly relevant
```

This makes distractor handling an ethical control problem as well as a performance problem.

The architecture must preserve the ability of sufficiently important evidence to interrupt an established rule or commitment.

---

## Current working claim

```text
REE already distinguishes goal relevance from salience
and already implements several forms of distractor resistance.

The new brainstem findings should therefore be assessed
as evidence for a more specific low-level function:
suppressing competing orienting or target-selection signals
before they acquire behavioural control.

The resulting REE question is whether its existing distributed
precision, mode, persistence, conflict, and trajectory-control
mechanisms are sufficient in genuinely noisy environments,
or whether pre-selection competition requires a more explicit substrate.
```

---

## Immediate REE implication

No new subsystem is currently justified.

The immediate actions are:

```text
recognise existing distractor-resistance mechanisms
separate sensory capture, rule corruption, and behavioural capture
inspect current telemetry and experiments for coverage
preserve the paper as a future noisy-environment benchmark seed
avoid conflating goal relevance with salience
```

---

## Open questions

1. Does REE currently suppress irrelevant cues before candidate generation?
2. Can current precision and salience routing prevent behavioural capture without a dedicated low-level suppressor?
3. Which current experiments test sensory capture rather than rule-state drift?
4. How should urgent harm signals bypass distractor suppression?
5. How should distractor handling change before versus after commitment?
6. What degree of suppression improves stability without producing pathological attentional rigidity?
7. Which existing REE claim should own this benchmark family?
