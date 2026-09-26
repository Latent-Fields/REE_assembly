---
title: "Harm-to-Threat Causal Credit"
parent: "Affect, Harm & Nociception"
grandparent: Architecture
nav_order: 21
status: candidate
status_asof: 2026-09-26
status_claim: MECH-598
---

# Harm-to-threat causal credit

**Claims:** MECH-598, MECH-599, Q-113
**Registered:** 2026-09-26
**Source:** `evidence/planning/thought_intake_2026-09-26_harm_to_threat_causal_attention_and_credit.md`
(primary) and its sibling `thought_intake_2026-09-26_harm_source_attention_and_aversive_credit_assignment.md`.
Both were written from the user's V3-EXQ-1109 observation: *"the thing that harms perhaps deserves attention."*

## Why this page exists

"I have been harmed" and "that thing is dangerous" are different representations. V3-EXQ-1109 found
that `z_harm_a` reproduces its own input with high fidelity (held-out R^2 ~0.99). That input is
accumulated body damage, and it tracks hazard proximity only weakly. The PAG freeze gate (MECH-279)
reads `z_harm_a` as if it meant "threat is present now".

Most of the chain from harm to learned threat already exists in REE. This page names the parts that
already exist and registers only the three pieces the ingestion audit found missing.

## What REE already owns (cross-reference only)

| Link in the chain | Existing owner |
|---|---|
| Injury state is separate from proximity/intensity | SD-011 (`z_harm_s` vs `z_harm_a`). SD-020 and MECH-258 add that `z_harm_a` should reach action selection as a precision-weighted PE, not as a raw magnitude |
| Phasic harm/surprise -> arrest -> orient -> identify -> release | SD-099 / MECH-489 |
| Harm-PE plus attribution over memory codes -> selective partial remap | MECH-074d, with the trainable `BLAAttributionHead` (`ree-v3/ree_core/amygdala/attribution_head.py`) |
| Scalar, broadcast gain on write/learning strength | MECH-074a (arousal gain on hippocampal writes), MECH-398 / ARC-093 (ACh plasticity gain) |
| Content-selective tag on the current trace for replay priority | MECH-074b |
| Per-event write licence; tag-and-capture | MECH-368, MECH-431 |
| Credit stays local under a broadcast teaching signal (appetitive / DA, selector loops) | MECH-452 |
| Retrospective credit sweep at trajectory end | MECH-290 |
| Contextual (place-indexed) prospective harm | residue field; E3 `harm_eval`; MECH-073 |
| Cue-specific learned prediction, **safety** side | MECH-304 / SD-051 (`ConditionedSafetyStore`), with contextual sister MECH-303 |
| Instrumental action-efficacy credit | MECH-357 |
| Operating-point scale and regime exit | ARC-155, ARC-156 |

## MECH-598: aversive-PE-driven cue associability {#mech-598}

When an unexpected negative change in valued self-state happens, the learning rate should rise
**per candidate cause**. It should not rise uniformly. The candidates are the representations held in
a short, decaying retrospective eligibility window: recent `z_world` / entity / context codes and
recent actions. Each candidate's associability persists as a state, updated Pearce-Hall style from
the |PE| of the outcomes it was present for. So the candidate is learned about faster **on later
trials**, not just once.

This differs from its neighbours:

- MECH-074a and MECH-398 apply a scalar gain to everything. That is the broadcast control this claim
  has to beat.
- MECH-074b tags the trace being written *now* for replay. It is not retrospective and it is not a
  learning-rate state.
- MECH-431 decides whether an event's write is consummated. It does not set how fast a cue is learned
  about later.
- MECH-074d chooses codes to overwrite (remap). It does not choose codes whose future learning rate
  rises.
- MECH-452 is the appetitive, DA-selector case. This claim is the aversive, world-cue case.

## MECH-599: cue-specific conditioned threat predictor {#mech-599}

This is the threat-side mirror of MECH-304 / SD-051. It is a discrete, cue-specific structure that
encodes *"this `z_world` prototype predicts that harm will follow"*. Aversive-PE events teach it, and
MECH-598's associability distributes the credit, so the representation of the cause becomes a
predictor. Defensive consumers (SD-099 release, MECH-279 freeze entry, E3 harm scoring) read its
output as **predicted near-term threat**, which lets them act before any new damage. Accumulated
injury (`z_harm_a`) stays meaningful for recuperation, guarding and negative valence. It is not the
same variable as external threat.

The safety side already separates cue-specific (MECH-304) from contextual (MECH-303) prediction. The
threat side has contextual prediction (residue field) but no cue-specific, event-taught predictor.
`ree-v3/ree_core` has no `ConditionedThreat*` structure.

## Q-113: does harm close into source-specific prospective avoidance in V3? {#q-113}

After an unexpected harm event, does current REE (SD-099 + MECH-074d + E1/residue + E3) selectively
strengthen the representation of the cause, so that the cause later changes prediction and action
before harm recurs? There are four admissible answers:

1. **integration:** the parts exist but are not causally joined;
2. **semantic split:** injury and threat need separate consumer contracts;
3. **new mechanism:** MECH-598 / MECH-599 are required;
4. **representation-gated:** `z_world` does not carry stable enough cue identity for source-specific
   credit to be possible at all.

Answer 4 is the strongest prior. MECH-074d has already failed on context differentiation (894 series,
blocked on MECH-153), which is the observation->`z_world` binding constraint.

## Status

All three are `candidate` and `substrate_conditional`. **Do not build and do not queue.** Registering
them is not build authorisation. `/thought-digestion` drafts the falsification conditions, and
`/governance` owns routing.
