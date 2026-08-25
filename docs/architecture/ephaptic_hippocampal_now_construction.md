---
title: Ephaptic Aggregation and the Construction of Actionable "Now"
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 8
---

# Ephaptic Aggregation and the Construction of Actionable "Now"

**Claim Type:** mechanism_hypothesis cluster (both candidate, substrate_conditional)
**Scope:** How a fast, cross-system field-coherence signal could (a) supply the content of the
hippocampal proposer's actionable-now starting state, and (b) gate WHEN a branching predicted
future is coherent enough for commitment to land.
**Depends On:** MECH-228 (ephaptic coupling as general coherence substrate), MECH-270 (ephaptic
CA1/CA3 verisimilitude readout), MECH-269 (hippocampal anchor selection), MECH-022 (hippocampal
hypothesis injection), MECH-149 (CA1 mismatch novelty gate), ARC-018 (hippocampal rollout
generation), MECH-089 (theta-cycle packaging), MECH-090 (beta-gated commit propagation),
MECH-434 (epistemic commitment timing)
**Status:** candidate (both claims)
**Claim IDs:** MECH-499, MECH-500
**Implementation phase:** V4
**Source:** `docs/thoughts/2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md`,
digested in `evidence/planning/thought_intake_2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md`

---

## The gap this closes

REE's existing hippocampal-proposer machinery already answers *which slice of the current latent
becomes the rollout anchor* (MECH-269, `hippocampal_anchor_selection.md`) and *how confident the
proposer should be in each stream* via a candidate ephaptic-field readout (MECH-270). Neither
claim addresses two further questions this cluster raises:

1. **Where does the CONTENT of "now" come from, fast enough to matter?** MECH-270 is explicit
   that it grounds only a confidence/eligibility scalar (`V_s`), not the aggregated state itself
   -- "`V_s` can be computed directly from per-stream prediction/realization alignment... MECH-270
   is the biological-grounding claim, not an implementation requirement." If hippocampal
   proposal generation needs a rapidly-updated organism-level state to start from, and slow
   sequential polling of every subsystem is too slow, something has to aggregate distributed
   oscillatory information into that state fast. MECH-499 names ephaptic/field-level coupling
   as a candidate for that aggregation function specifically (not just the confidence gate).

2. **What decides WHEN a branching future is ready for commitment, as opposed to WHICH future
   wins?** REE's existing commitment machinery (MECH-090 beta-gate, its R-c margin/competence
   readiness conjunction, MECH-434's evidence-driven epistemic commitment timing) answers
   *whether propagation is currently gated* and *whether there is enough external evidence to
   commit*. None of them ask whether the **internal proposal itself** -- the candidate trajectory
   generated from the aggregated "now" -- has become sufficiently coherent, in the field-coherence
   sense, to be a safe thing to commit to. MECH-500 names this as a distinct **temporal/readiness
   authority**, separate from the **content authority** (which candidate wins) that MECH-090 /
   MECH-341 / ARC-003 already govern.

---

## MECH-499: field coherence as content aggregation

Ephaptic coupling -- non-synaptic influence of a neural population by the extracellular field it
itself generates -- is fast (no synaptic delay) and naturally scales with synchrony. The claim is
that this makes it a candidate physical mechanism for **aggregating**, not merely gating, a
temporally-structured population estimate: amplitude, phase, relative phase across streams,
frequency, synchrony, and cross-frequency relationships, rather than one scalar. That aggregate
is the candidate content of the "actionable now" state that hippocampal proposal-generation
machinery (MECH-022 hypothesis injection, MECH-149's novelty-gated rate, ARC-018's rollouts) reads
as its anchor.

This is explicitly **not** a restatement of MECH-270: MECH-270 stays a confidence/eligibility
readout over already-defined per-stream alignment scores; MECH-499 is about where the composed
state's *content* comes from in the first place. Both may be true simultaneously -- one substrate
family (ephaptic field dynamics) plausibly does both jobs, but they are logically and
experimentally separable, and conflating them was already the exact class of error MECH-269 /
MECH-270's own split was written to avoid (function vs. physical substrate).

**Falsifiable in spirit** (from the raw thought, not yet a NON-DEGENERACY-gated experimental
falsifier -- both claims are V4-parked and substrate_conditional): perturbing endogenous field
structure while minimally altering ordinary synaptic drive should alter timing/coherence of
prospective hippocampal representations; disrupting oscillatory coherence should impair
prospective proposal organisation more than simple sensory representation; the relationship
should be timescale-sensitive, not reducible to a static average field magnitude.

## MECH-500: content authority vs. temporal/readiness authority

The BG-like system need not receive the aggregated "now" directly -- its role is proposed to be
**constitutional**: to govern which of the proposals generated from the aggregated state acquires
behavioural authority (content authority, already REE's existing architecture: MECH-090,
MECH-341, ARC-003). This claim names a second, distinct axis: **temporal/readiness authority** --
whether a given candidate future has become sufficiently coherent, in the cross-system
field-coherence sense, for commitment to be permitted to land *at all*, independent of which
candidate is best.

This is explicitly distinguished from two existing V4-parked commitment-timing claims:

- **MECH-434** (epistemic commitment timing) asks whether there is enough *evidence about the
  world* to stop gathering and act -- an inference-layer, belief-state-uncertainty question.
  MECH-500 asks whether the *internal proposal-generating machinery itself* has cohered, a
  question about the state of the generative system, not about external evidential sufficiency.
- **MECH-090**'s beta gate (and its R-c margin/competence readiness conjunction) governs
  propagation of an *already-decided* commit, and admits commitment on score-margin /
  motor-readiness grounds. MECH-500 is upstream of that: a candidate coherence signal for
  *whether commitment should be considered at all*, prior to and orthogonal to margin-based
  admission.

A future V4 scoping pass should determine whether MECH-434 and MECH-500 are independent
readiness signals that AND-compose (mirroring MECH-090's own two-axis R-c precedent) or whether
one subsumes the other once both substrates exist. Not resolved here -- see the intake's Next
Steps.

---

## What this does NOT imply

- Neither claim requires REE to simulate literal biological ephaptic fields. The computational
  question is whether REE needs *some* fast cross-system aggregation/coherence mechanism, and
  whether the ephaptic framing is a useful analogue for it (see MECH-089's own precedent of
  disclaiming literal oscillatory coupling while keeping the functional requirement).
- MECH-270's confidence-readout scope is unchanged; MECH-499 does not revise it.
- MECH-090's propagation-gate scope is unchanged; MECH-500 does not revise it.
- Neither claim authorises V3 work. Both are gated on the MECH-228/MECH-270 ephaptic substrate
  itself, which is not V3-landed -- the closest existing V3 evidence (V3-EXQ-720/725/725a, a
  fixed/learned ephaptic-analog cross-stream binder) has not yet cleared its own
  coherence-specificity gate.
