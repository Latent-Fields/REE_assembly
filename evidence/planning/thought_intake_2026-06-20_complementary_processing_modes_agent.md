# Thought intake: complementary processing modes for REE agent architecture

**Date:** 2026-06-20  
**Status:** thought intake / architecture design note; not an implementation request  
**Scope:** REE agent architecture, not REE_assembly governance machinery  
**Related note:** `thought_intake_2026-06-20_complementary_processing_modes_assembly.md`  
**Related architectural areas:** E3 selector, commitment latch, conflict monitoring, world model, goal / wanting layer, local affordance evaluation, ARC-106 biology grounding, MECH-439 / F-dominance.

---

## 1. Core thought

REE itself may need complementary processing modes analogous to broad-context and local-detail cognition.

The motivating analogy is hemispheric-style functional complementarity: global / contextual / gestalt processing versus local / sequential / detail-adjudicating processing. This should not be treated as literal left-brain/right-brain implementation. It is a functional architecture heuristic.

The architectural question is whether REE requires distinct but interacting processing stances:

```text
global context / world-shape / meaning
+ local detail / rule / affordance / action candidate
+ conflict monitoring
+ selector constitution
+ commitment latch
= viable committed action
```

---

## 2. Why this matters for REE

Current V3 work increasingly suggests that upstream signals can form but fail to purchase committed action. The F-dominance cluster is one expression of this. SD-049 / MECH-436 work may be another: representational or drive signals can appear measurable while behavioural expression remains weak, reversed, or flat.

This raises a broader design issue:

```text
A viable agent may need both wide-field contextual coherence and narrow executable precision.
It must also have a selector that prevents either mode from becoming tyrannical.
```

If broad-context processing dominates, the system may become diffuse, over-associative, or unable to commit.

If local-detail processing dominates, the system may become brittle, myopic, over-literal, or captured by one scalar objective.

The agent needs a mechanism for integration, conflict, arbitration, and commitment.

---

## 3. Candidate complementary modes inside REE

| Candidate mode | Function | Possible current / future substrate |
|---|---|---|
| Global-context synthesis | Maintains broad world-shape, context, meaning, trajectory, and cross-domain coherence. | World model, default-mode-like simulation, hippocampal / path-memory substrate, E1/E2 predictive layers. |
| Local-detail evaluation | Tracks immediate affordances, rules, local action consequences, constraints, and executable detail. | Cue system, rule-state, action candidates, local transition model, sensory-gradient adaptors. |
| Value / drive modulation | Marks salience, need, wanting, cost, urgency, and motivational relevance. | SD-049 / MECH-436-adjacent drive and resource systems; future incentive-salience grounding. |
| Conflict monitoring | Detects incompatible affordances, close action competition, safety conflict, rule conflict, or uncertainty. | dACC-like conflict machinery / MECH-258 / MECH-260 family. |
| Selector / action-gate | Converts candidate pressures into lawful committed action. | E3 selector, MECH-439 / basal-ganglia-like selector constitution. |
| Commitment / de-commit latch | Stabilises action after selection while allowing release when conditions change. | SD-034 / MECH-090 / commitment closure. |
| Reflective / ethical modulation | Later-stage policy layer for self/other implications, care, repair, inhibition, and value-consistent action. | V4/V5/V6 perimeter; not a V3 green-board blocker. |

---

## 4. Functional analogy to hemispheric-style complementarity

This note uses hemispheric-style complementarity as a heuristic only.

Useful functional contrast:

| Axis | Broad-context mode | Local-detail mode |
|---|---|---|
| Scope | Global / relational / contextual | Local / sequential / precise |
| Time horizon | Trajectory, narrative, possible futures | Immediate next action and constraints |
| Error risk | Vague coherence, overgeneralisation, premature synthesis | Myopia, brittleness, scalar capture |
| Value | Maintains meaning and cross-domain coherence | Makes action executable and testable |
| Required counterbalance | Evidence, constraint, commitment | Context, conflict, re-evaluation |

The purpose is not to reproduce brain lateralisation. The purpose is to prevent REE from collapsing all cognition into one processing stance.

---

## 5. Relation to current selector concern

This thought intake connects directly to the basal-ganglia-like selector constitution note.

If REE has multiple processing modes, then final action selection must not be a simple scalar monarchy. The selector must arbitrate between candidate actions emerging from different modes and pressures:

```text
broad-context pressure
local-affordance pressure
safety pressure
rule pressure
drive pressure
conflict pressure
uncertainty pressure
```

A basal-ganglia-like selector constitution may be needed to decide when these pressures become:

```text
eligible
suppressed
held
widened
committed
released
```

This makes complementary processing modes relevant to MECH-439: the selector bottleneck is not only about action entropy, but about whether distinct cognitive modes can lawfully influence action.

---

## 6. Developmental sequencing

This note should not expand V3 scope unless current evidence forces it.

Possible sequencing:

```text
V3:
  Demonstrate that core signals can form and that action selection can escape scalar capture enough for green-board competence.

V4:
  Formalise broader world-model / action-mode integration and improve mode arbitration.

V5:
  Add richer language / reflective interface if needed.

V6+:
  Social / ethical / care / repair / multi-agent implications.
```

The key V3 relevance is limited:

```text
Complementary modes are relevant now only insofar as formed signals cannot buy action.
```

The broader mode architecture can remain a thought intake unless selector or commitment failures require it.

---

## 7. Possible future architecture questions

Questions to preserve:

1. Does REE require an explicit global-context stream distinct from local action evaluation?
2. Does local-detail action evaluation need to be protected from being overridden by broad but non-actionable coherence?
3. Does global context need a lawful route to action, or only to candidate generation / threshold modulation?
4. Can conflict monitoring detect disagreement between broad-context and local-detail modes?
5. Should commitment be delayed when global and local modes conflict?
6. Does the selector need mode-aware eligibility rules?
7. Can mode imbalance explain some failure signatures currently attributed to F-dominance or drive-coupling failure?
8. Which mode should dominate under immediate hazard, resource pursuit, uncertainty, social context, or ethical conflict?

---

## 8. Proposed future falsifier classes

If this thought becomes architecture work, possible falsifier classes include:

### 8.1 Global-context present but local action absent

The system forms coherent state / trajectory representations but cannot produce distinct action commitments.

### 8.2 Local action works but context-blind

The system learns local policies but fails when context changes or when action should depend on broader state.

### 8.3 Mode-conflict handling

The system must choose under conflict between locally rewarding action and broader trajectory cost.

### 8.4 Mode-to-selector access

A mode forms a measurable signal and reaches the selector, but cannot alter committed action. This overlaps with MECH-439.

### 8.5 Over-wide synthesis failure

A broad-context process increases candidate diversity but impairs stable commitment or safety.

### 8.6 Over-narrow capture failure

A local scalar or rule captures commitment despite meaningful global-context conflict.

---

## 9. Risks

### 9.1 Literal hemispheric mapping

Avoid treating this as a left-brain/right-brain implementation claim. The analogy is only a heuristic for complementary processing modes.

### 9.2 Premature scope expansion

Do not add new modules before V3 closure requires them. The immediate issue remains selector conversion and commitment.

### 9.3 Decorative complexity

Multiple modes should only be introduced where they generate testable differences or explain failure signatures better than the current architecture.

### 9.4 Mode tyranny

A multi-mode system still requires governance. Broad-context and local-detail modes can each become pathological if they dominate without arbitration.

---

## 10. Minimal recommendation

Record complementary processing modes as an architecture pressure for REE.

Do not implement now.

Use this note when interpreting future failures where:

```text
one cognitive stance forms a valid signal,
but another stance or the final selector prevents action conversion.
```

Most immediate linkage:

```text
MECH-439 / E3 selector constitution
SD-049 / drive-to-behaviour coupling
commitment / de-commit latch grounding
future world-model / action integration
```

---

## 11. One-sentence summary

REE may require complementary broad-context and local-detail processing modes, mediated by conflict monitoring, selector constitution, and commitment machinery; this should be treated as a functional architecture heuristic, not a literal hemispheric mapping or immediate V3 implementation request.
