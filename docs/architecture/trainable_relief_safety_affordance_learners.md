---
title: Trainable relief / safety affordance learners (MECH-375 / MECH-376 / Q-067)
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 31
---

# Trainable relief / safety affordance learners (MECH-375 / MECH-376 / Q-067)

**Status:** candidate cluster, registered 2026-06-09. Home doc for the trainable
successors to the fixed escape-affordance bridge.

**Scope:** V3-NARROW minimal trainable bridge (a post-V3-EXQ-603i successor
candidate, close to the V3 critical path). A V4 / V5-rich tier is described at the
end and is kept **off** the V3 path.

**Source thought:** [`docs/thoughts/2026-06-08_Trainable_Releif_and_Safety.md`](../thoughts/2026-06-08_Trainable_Releif_and_Safety.md)

---

## Why this cluster exists

The escape-affordance bridge (SD-059 / MECH-358) currently binds relief and safety
to escape via a **fixed-arithmetic, per-first-action-class EMA credit table**. The
relief-completion machinery it consumes (MECH-302 / SD-050) is a **non-trainable
rolling-window comparator** that detects a sustained `z_harm_a` descent on the
*current* state. The safety substrate (MECH-303 contextual passive store, MECH-304
cue-specific conditioned inhibition) is a pair of substrate *hypotheses* whose
implemented V3 form is, again, the fixed EMA table.

None of these learns a **generalising function** of state x action x (threat / cue)
context. V3-EXQ-603h showed the consequence: the agent could suppress freezing and
act under threat, but did not learn that a *specific* action / location / policy was
the way out -- a scalar avoidance efficacy did not bind relief to an escape
direction. The biologically stronger architecture makes **both relief and safety
trainable**.

## What REE already owns (cross-ref, NOT duplicated)

| Owned | Role | Why the trainable head is not a duplicate |
|-------|------|-------------------------------------------|
| SD-050 / MECH-302 | non-trainable suffering-derivative comparator + relief-completion pipeline reuse | DETECTS relief on the current state; does not bind / generalise credit to an action |
| MECH-303 / MECH-304 | contextual + cue-specific safety substrate hypotheses | substrate hypotheses; implemented form is a fixed EMA table, not a trained predictor |
| SD-058 / MECH-357 | instrumental-avoidance acquisition + ilPFC freeze-suppression (scalar efficacy) | scalar global efficacy; penalises freeze, does not pick a direction |
| SD-059 / MECH-358 | escape-affordance bridge (fixed per-action-class EMA credit table) | fixed arithmetic; no generalising function over continuous state / action / context |

## The two trainable heads

### MECH-375 -- Trainable relief critic `Q_relief(state, action, threat_context)`

A learned parametric head predicting **expected harm / suffering reduction after an
action** under threat. Function = negative-reinforcement **credit assignment**
("this action reduced suffering / terminated harm"), distinct from generic reward /
wanting even if it reuses reward machinery.

- **Inputs (candidate):** `z_world`, `z_self`, threat / harm streams (esp.
  `z_harm_a`), action class / candidate first action, possibly local E3 trajectory
  features.
- **Training target:** positive when a directed action under threat is followed by a
  `z_harm_a` drop; stronger when temporally close, action-contingent, and not
  explained by passive drift; negative / extinction when the expected relief action
  fails.
- **Role:** under future threat, bias E3 toward actions predicted to reduce harm;
  silent when safe; never credits no-op / freeze unless explicitly modelling passive
  safety.

### MECH-376 -- Trainable safety predictor `P_safety(state, cue, action, context)`

A learned parametric **prospective** predictor of threat-absence / response-produced
safety / conditioned inhibition. Licenses commitment-release, approach, and recovery.
**Distinct from `z_goal`** (predicts threat *absence*, not goal *presence*) and from
relief (prospective prediction, not an aversive-offset event).

- **Inputs (candidate):** `z_world`, cue / context features, action class / recent
  action, threat history, time since threat offset, possibly a hippocampal context
  slot / rule representation.
- **Training target:** positive when a cue / context / action predicts threat
  absence; negative when a "safe" cue is followed by threat recurrence;
  **contrastive** so safety cannot collapse to "low harm" or "recent relief".
- **Role:** support commitment release, permit approach to safety affordances,
  stabilise recovery, prevent persistent defensive mode when threat is genuinely
  absent.

### Why both (Q-067)

Relief alone teaches "that action reduced harm" but need not produce a stable
prospective safety model; safety alone teaches "this context / cue is safe" but need
not solve action-specific escape under active threat. The mature avoidance system
needs action-contingent relief learning (MECH-375) for **escape** and
cue / context-contingent safety learning (MECH-376) for **recovery / inhibition /
future approach**. Q-067 is the decomposition adjudicator routed by the V3-EXQ-603i
outcome (partial pass -> train the missing half first; fail-with-non-vacuity ->
fixed table too crude, trainable learner required; credit-never-fires -> route back
to substrate readiness).

## Design guardrails (binding on any implementation)

The trainable system must remain:

- **bounded** -- cannot dominate E3 scoring (bias_scale clamp, as on MECH-358);
- **threat-gated** -- no global approach bias when safe;
- **extinguishable** -- failed relief / safety predictions decay;
- **contrastive** -- safety cannot mean "low harm" or "recent relief";
- **action-bound** -- relief credits the action / policy that produced harm reduction;
- **cue / context-bound** -- safety credits the cue / context / action that predicts
  threat absence;
- **MECH-094-safe** -- simulated relief / safety in hypothesis mode must not train the
  waking learner unless explicitly authorised as play / training.

## Governance scoping

All three claims are `status: candidate`, `epistemic_category:
substrate_conditional`, `implementation_phase: v3` (`v3_pending: true`). The
`substrate_conditional` category is deliberate: the trainable parametric heads are
**planned but not yet built** (the current bridge is the fixed table), so
promote / demote is suppressed and the cluster is kept off the IGW
experiment-proposal lane until a head exists. The right next step is to **decide
whether to build** the minimal trainable bridge (a later step), not to queue a
vacuous probe on the fixed-table substrate.

<a id="q-067"></a>

## V4 / V5-rich tier (OFF the V3 path -- do not build in V3)

The thought's richer architecture is explicitly deferred and not registered as part
of the V3-narrow cluster:

- expression-as-action-geometry for relief / safety;
- richer continuous state / policy / location indexing (beyond first-action class);
- hippocampal affect-gradient indexing of relief; social safety attribution;
- multi-cue / rule-representation safety contexts.

These belong to the V4 / V5 enrichment programme and must not enter the V3 critical
path; they are recorded here only so the boundary is explicit.
