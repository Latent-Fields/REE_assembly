---
title: Provenance Genealogy and Evidence Cardinality (INV-107 / MECH-552 / MECH-553 / MECH-554 / Q-105)
parent: "Modes, Agency & Default Mode"
grandparent: Architecture
nav_order: 15
status: candidate
status_asof: 2026-09-15
status_claim: INV-107
---

# Provenance Genealogy and Evidence Cardinality

Status: candidate cluster, V4/V5, off the V3 critical path. Drafted 2026-09-15.

Source thought: [docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md](../thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md)

Source intake: `evidence/planning/thought_intake_2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md`

Branch artifacts (planning prose, twelve documents, four of them executed probe results): see the
intake's section 0 table. The assay ladder is
[`evidence/planning/provenance_false_evidence_multiplication_experiment_ladder.md`](../../evidence/planning/provenance_false_evidence_multiplication_experiment_ladder.md);
the correction that reframes it is
[`evidence/planning/provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](../../evidence/planning/provenance_false_evidence_multiplication_campaign_supplement_20260910.md).

**Ids assigned 2026-09-15** by the registering pass (session thought-pipeline-20260915).

---

## Scope, and what this cluster is NOT

REE already owns the question "where did this content come from?" -- MECH-094 (simulation content
must not accumulate as committed experience), MECH-248 (source monitoring), MECH-249 (ACh/NA
mode-setting), MECH-037 (Papez-like reality filtering), MECH-365 and MECH-430 (the
provenance-bearing token and its multi-dimensional source vector), MECH-544 (source-tag decay),
INV-011 and INV-019 (imagination and rehearsal without durable write).

This cluster owns a second question those do not reach: **how many genuinely independent reasons
does the architecture think it has?** Those two questions are related and not identical. A system
can enforce every provenance gate above perfectly and still count one causal lineage as four
corroborating witnesses, because the answer to the second question is a property of the RELATIONS
between representations, and every mechanism listed above is a property of a representation.

This cluster makes **no clinical claim**. The source thought's own restraint is preserved: source-
and self-monitoring abnormalities are repeatedly observed in psychosis, particularly around
hallucinations, and are neither universal nor sufficient explanations of the syndrome. No fourth
psychosis pathway is registered alongside MECH-244, MECH-246 and MECH-247.

---

## INV-107 -- dependency must be represented; independence must not be inferred

A system must represent the dependency structure among its evidence and condition on it, and must
not infer independence from the absence of a recorded dependency. Any representation that can later
influence belief, confidence, closure or action carries enough uncertain, compressed causal
genealogy that the descendants of a hypothesis cannot be counted as witnesses independent of it.

The rule binds in its negative form only. "A hypothesis must not cite its own descendants as
independent witnesses" is correct; "descendants should be collapsed to one vote" is not, because
where a structural dependency exists but the observations across it are partial or contradicting,
dependent reports can support a hypothesis more than independent ones would. The invariant
constrains the representation, not the arithmetic.

Non-collapse relations: this is the self-generated-content counterpart of ARC-115 (socially-supplied
agreement must not enter the same accumulator as internally-derived confidence) at the agent layer,
of INV-077 at the governance layer, and of SD-088 in the claims registry.

## MECH-552 -- false evidence multiplication

A provenance error can change the apparent cardinality of evidence and not only its source label.
One internally generated hypothesis produces descendants through prediction, replay, counterfactual
simulation, retrieved memory and ambiguous perceptual interpretation; when shared ancestry is lost,
those descendants are counted as several corroborating observations and confidence rises with no
new world evidence.

Two consequences are held separate: a phenomenological branch (self-generated content losing
evidence of self-generation acquires external status) and an epistemic branch (descendants losing
shared ancestry inflate posterior confidence and shorten information-seeking).

Locus correction, carried in the claim rather than deferred: the operative variable is the readout's
default for unknown ancestry, not the corruption event. An architecture that treats unrecorded
dependency as independence inflates whether or not any genealogy was corrupted.

## MECH-553 -- compressed causal genealogy

Provenance is a graph over representations, not a vector of attributes on each one. The proposed
structure is bounded, not a full history: shared-ancestor probability between evidence-bearing
items, an externally-anchored-observation flag with its own confidence, a hypothetical/replay
lineage marker, an already-counted-evidence-family marker, and a context-conditioned dependency
estimate, each genealogy edge carrying its own confidence so ancestry can be uncertain without
being absent.

This extends MECH-430 from attributes of one token to relations between tokens, which is the level
at which evidence cardinality is defined. Its named competitor is lineage-free dependency estimation
(Rule & O'Leary 2022): if inferred soft genealogy matches explicit genealogy on calibration and
duplicate-evidence resistance at matched information, this claim earns no keep.

## MECH-554 -- recursive replay amplification

When genealogy is corrupted or absent, repeated replay converts remembered or simulated material
into apparent new evidence, so confidence rises monotonically with replay count at fixed external
evidence and the belief becomes self-maintaining.

The dangerous signature is an ancestry-by-replay-count interaction, not a replay-count main effect:
healthy replay must be able to improve retrieval fidelity with the effective independent-source
count staying flat. Admissible only with replay stratified by kind and retrieval quality matched
across ancestry conditions.

Distinguished from MECH-363: that is self-amplification between fields, repaired by signed
competitive coupling; this is self-amplification in an evidence count, repaired by a genealogy
representation.

## Q-105 -- are source attribution and evidence cardinality dissociable?

Can P(external | representation) move without the effective independent-source count moving; can
the count and calibration move without any change in external-source attribution; does a broader
self-monitoring failure move both? A null is informative: it would mean provenance errors alter
source labels only, retiring the multiplication branch while leaving the source-monitoring account
intact.

Distinguished from the tag-loss versus tag-misassignment dissociation already recorded on MECH-094:
that separates two kinds of provenance failure; this separates two readouts taken on one
manipulation.

---

## Substrate status (verified 2026-09-15 against the live `ree-v3` tree)

- **Built:** a one-bit committed-vs-imagined gate -- `hypothesis_tag` on `Trajectory`
  (`ree_core/predictors/e2_fast.py:63`), enforced across 24 files; `replay_origin` for the MECH-322
  sleep-only carve-out; `simulation_mode` across 20 modules.
- **Absent:** any ancestry, lineage, ancestor or genealogy structure. A tree-wide grep returns only
  the word "lineage" in comments about experiment lineages.
- **Stripped on purpose:** the executed committed trajectory drops its source metadata
  (`ree_core/hippocampal/module.py:3450-3453`). Correct under MECH-094, and it is exactly the
  PROVENANCE ABSENT condition for this cluster.
- **The arithmetic already exists:** `ree_core/sleep/bayesian_aggregator.py` adds likelihood
  precision per routed replay event with no dependency term, and
  `ree_core/sleep/replay_sampler.py` draws with replacement while already tracking per-region draw
  counts. Both default OFF; both are enabled together by
  `REEConfig.enable_sleep_aggregation_cluster()`.
- **The waking replay path has no consumer at all:** `ree_core/agent.py:10594` `_do_replay`
  computes and discards (`substrate_queue.json` entry `mech092-replay-consumer-missing`).

**DO NOT build any of this in V3. DO NOT queue an experiment from this doc.**
