# Mutual legibility / communication-subspace work programme

**Date:** 2026-09-07  
**Status:** proposed staged work programme; no experiments queued, no claims registered, no task-ledger mutation performed here  
**Parent thought:** `docs/thoughts/2026-09-07_mutual_legibility_communication_subspaces.md`  
**Implementation companion:** `docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md`

## Purpose

Translate the evidence campaign and thought into a staged programme that can be adopted by the existing REE governance/task machinery without bypassing its pacing, red-team, or claim-synthesis rules.

The programme deliberately separates:

1. **instrument validation**;
2. **current V3 diagnosis**;
3. **causal adjudication**;
4. **development/sleep tests**;
5. **architectural synthesis only if warranted**.

The order matters. A sleep experiment built before the communication-subspace metric is validated would measure an unproven instrument. A bridge built into `ree_core` before frozen-endpoint diagnosis could conceal the real failure locus.

---

# Phase 0 — Governance and evidence intake

## ML-00 — Evidence package completeness check

**Goal:** ensure campaign/tranche documents and main thought form one auditable chain.

Actions:

- verify the Mostik, Interlat, StateBridge, causal-audit, communication-subspace, NoMAD, and Spens/Burgess sources are represented in the literature/evidence system where appropriate;
- distinguish peer-reviewed, preprint, and company-reported evidence;
- record that the specific "sleep reduces bridge complexity" proposition remains a REE hypothesis;
- cross-link the main thought to the `z_world` representation contract, replay/rebucketing thought, MECH-532, and representation->authority->selection correction.

**Output:** evidence crosswalk only.

**Do not:** change claim status automatically.

## ML-01 — Claim overlap / contradiction review

Review, at minimum:

- MECH-532 compression/decompression pairing;
- MECH-507 reciprocal compression/decompression framing;
- ARC-121 shared epistemic-state object;
- relevant INV-088 / z_world differentiation lineage;
- SD-080 / MECH-517/518 action-object training/decode debts;
- sleep/replay claims relevant to interface recalibration.

Question for each:

> Does mutual legibility merely reinterpret existing scope, create a rival implementation, or justify a genuinely new falsifiable claim?

**Output:** claim-synthesis recommendation, not direct mutation from this work programme.

---

# Phase 1 — Build the instrument, not the mechanism

## ML-10 — Interface telemetry schema

**Priority:** highest engineering prerequisite.

Design a reusable read-only capture schema for aligned sender/consumer states.

Minimum fields:

- seed / episode / timestep;
- sender tensor;
- actual consumer input / preactivation;
- task target(s);
- action/candidate identity;
- outcome;
- provenance;
- wake/sleep phase;
- model hashes/config fingerprints;
- relevant gates/masks.

**Acceptance:** can capture one current `z_world -> consumer` locus without changing agent behaviour or RNG sequence.

**Negative control:** telemetry disabled vs enabled produces bit-identical behaviour/checksum where expected.

## ML-11 — Offline interface dataset builder

Build held-out episode/environment splits and standardisation utilities.

**Acceptance:** no row-level random leakage; split provenance recorded; same split reusable across all bridge/subspace models.

## ML-12 — Communication-subspace analysis library

Implement cross-validated Reduced Rank Regression (RRR) with:

- rank sweep;
- held-out receiver prediction;
- communication subspace projection;
- orthogonal complement projection;
- principal-angle comparisons;
- target-information retention;
- seed/checkpoint stability report.

**Acceptance:** synthetic tests recover a known planted low-rank communication subspace and reject a null/no-coupling control.

## ML-13 — Bridge ladder library

Implement frozen-endpoint:

- identity/native;
- orthogonal Procrustes;
- affine linear;
- low-rank affine;
- narrow nonlinear upper bound.

Record parameter counts and regularisation.

**Acceptance:** synthetic rotation is recovered by Procrustes; nonlinear-only synthetic case is not falsely credited to the linear arms.

## ML-14 — Causal replacement library

Implement paired replacements:

- correct;
- mismatched episode;
- zero;
- moment/covariance-matched random;
- optional same-action and same-context mismatch.

**Acceptance:** synthetic paired-information task discriminates correct from mismatch; generic-channel synthetic task shows correct ~= mismatch >> zero.

## ML-15 — Dynamic compatibility library

Implement one-step and multi-step bridge consistency metrics for action-conditioned transitions.

**Acceptance:** known pointwise rotation with compatible dynamics passes; constructed static-fit/dynamic-mismatch case fails.

---

# Phase 2 — First current-V3 diagnosis

## ML-20 — Waypoint z_world communication-subspace assay

**Recommended first live locus.**

Use the V3-EXQ-1004 / `f00402c9` geometry and existing waypoint-direction target.

Questions:

1. trained `z_world` directional decodability vs raw and random-projection floor;
2. what low-rank `z_world -> consumer` subspace predicts the actual reader;
3. how much waypoint-direction signal lies in that subspace vs its orthogonal complement;
4. whether a simple rotation/low-rank bridge increases native consumer use;
5. whether any rescue is correct-pair specific.

### Predeclared outcome categories

- **ML20-A information loss:** trained z_world target signal below justified floor and bridges cannot recover;
- **ML20-B routing mismatch:** target exists in z_world but is weak in native communication subspace;
- **ML20-C coordinate mismatch:** simple frozen bridge restores correct-pair-specific use;
- **ML20-D consumer failure:** target reaches consumer-facing subspace but behaviour remains insensitive;
- **ML20-E generic channel:** rescue survives mismatched content;
- **ML20-F dynamic mismatch:** static rescue but transition consistency fails.

No architectural promotion follows directly from any category.

## ML-21 — Replicate on directional resource-field locus

Use SD-018 / V3-EXQ-978 lineage.

Purpose: determine whether the waypoint result generalises beyond one target or was locus-specific.

Do not pool waypoint/resource conclusions without a formal cross-target comparison.

---

# Phase 3 — Revisit the strongest historical negative case

## ML-30 — Action-object O communication-subspace autopsy

Reanalyse the V3-EXQ-817a / SD-080 lineage under the new vocabulary.

Questions:

- where does consequence information sit in O after grounding?
- what O dimensions actually predict the downstream decoder/planner quantity?
- is consequence structure in the communication subspace or mostly private/orthogonal?
- is the decoder collapse equivalent to an effective rank/decision-boundary failure?

**Output:** measurement-only autopsy first.

## ML-31 — Frozen non-collapsing readout discriminator

Only if ML-30 supports routing/readout mismatch.

Compare:

- legacy downstream path;
- constrained low-complexity readout trained on frozen O;
- same-action mismatched O control;
- shuffled consequence control.

Prediction from interface-first account:

> grounded consequence structure should become behaviourally visible through a non-collapsing readout.

A second null through a demonstrably adequate reader would materially weaken the interface-first reinterpretation.

---

# Phase 4 — ContextMemory content flow

## ML-40 — Write/store/retrieve/use ladder

Use 970a/972a lineage to measure a single target across:

1. incoming write stream;
2. stored slot/content;
3. retrieved context;
4. actual downstream cue/action consumer;
5. behaviour.

This is a natural location to operationalise:

`encoded -> decodable -> retrieved -> natively accessible -> causally used`.

## ML-41 — Retrieval pairing audit

Swap retrieved contexts between matched episodes/contexts while preserving gross retrieval statistics.

Distinguish:

- content-specific retrieval;
- generic retrieval/channel activity;
- retrieval-induced gain/arousal effects independent of identity.

---

# Phase 5 — Developmental trajectory

Proceed only after at least one waking interface instrument is validated and stable.

## ML-50 — Snapshot mutual-legibility trajectory

At predeclared developmental checkpoints, freeze snapshots and run identical held-out interface assays.

Track:

- local sender competence;
- local receiver competence;
- communication rank;
- target overlap;
- minimal successful bridge class/rank;
- pairing-specific effect;
- dynamic compatibility.

Primary hypothesis:

> at selected interfaces, local specialisation/competence can increase while required translation complexity decreases or task information becomes more concentrated in the consumer-facing subspace.

### Rival hypotheses

- global convergence explains both competence and legibility;
- interface complexity is static;
- apparent improvement is merely increasing sender decodability;
- one subsystem loses specialisation and becomes a duplicate of another.

---

# Phase 6 — Sleep / offline interface tests

Proceed only after ML-50 or another waking metric establishes measurement range and reliability.

## ML-60 — Single-boundary pre/post sleep measurement

Use `force_sleep_cycle_at_eval_boundary` or equivalent sanctioned substrate.

Measure the same organism immediately before and after a controlled sleep cycle.

Outcomes:

- sender drift;
- receiver drift;
- communication-subspace rotation;
- effective rank;
- task-overlap change;
- bridge complexity;
- dynamic compatibility;
- causal content effect.

Do not define "improvement" as greater global representational similarity.

## ML-61 — Plastic interface vs stable scaffold discriminator

Select two interfaces predicted to differ in plasticity.

Possible comparison:

- intrahippocampal / replay-facing interface expected to reconfigure;
- cortical-facing or established decision interface expected to remain stable.

Prediction:

> sleep should alter the plastic interface more than the stable scaffold while preserving or improving downstream functional compatibility.

This is stronger and more biologically grounded than a global "sleep aligns representations" claim.

---

# Phase 7 — Architectural synthesis gates

No core architecture change should occur until at least one live locus reaches content-specific causal evidence.

## Gate A — Is there a real interface problem?

Require evidence of sender content plus native consumer inadequacy/routing mismatch.

If no: stop. Do not invent a bridge mechanism.

## Gate B — Is a low-complexity solution sufficient?

Prefer the smallest successful map.

If only high-capacity nonlinear bridging succeeds, treat this as inadequate evidence for a plausible interface mechanism.

## Gate C — Is the bridge performing new cognition?

Require:

- correct-vs-mismatched audit;
- held-out environment transfer;
- receiver-manifold guard;
- parameter/capacity disclosure;
- where possible, target-specific perturbation test.

## Gate D — Does an existing REE mechanism own the function?

Before registering anything new, check whether the correct implementation is actually:

- training an existing decoder/readout (MECH-532-like debt);
- enabling an existing projection;
- repairing a dead gradient;
- correcting a consumer bottleneck;
- changing phased training.

New architecture is last resort.

---

# Possible later architectural work items — NOT YET AUTHORISED

These are placeholders for synthesis only if Phase 2-6 evidence earns them.

## ML-A1 — Consumer-specific low-rank projection

Small trained read surface from a rich sender latent.

## ML-A2 — Compression/decompression co-training schedule

Train paired encoder/readout while retaining frozen-phase validation.

## ML-A3 — Context-gated communication subspace

Allow low-rank interface geometry to depend on mode/context.

## ML-A4 — Offline interface recalibration

Permit selected communication maps to update during sleep while local modules are frozen or semi-frozen.

## ML-A5 — Dynamics-aware interface objective

Preserve action-conditioned transition geometry, not merely pointwise states.

## ML-A6 — Stable core / private dimensions

Explicit interface/private partition only if emergent analyses repeatedly show this structure and a hard partition provides measurable benefit.

---

# Suggested governance routing

The following should be handled through existing REE machinery rather than directly here:

1. **literature intake** for papers not already registered;
2. **claim synthesis** to decide whether mutual legibility deserves a new mechanism/invariant or only amends interpretations of MECH-532/ARC-121/etc.;
3. **implementation chip** for the read-only analysis harness;
4. **diagnostic experiment design** for ML-20 only after the harness synthetic contracts pass;
5. **red-team** specifically tasked with detecting bridge leakage, wrong-tensor capture, temporal leakage, and generic-channel effects;
6. **pacing gate** should treat the initial programme as one campaign so multiple overlapping bridge experiments are not queued independently before the first result is adjudicated.

---

# Recommended immediate sequence

The smallest responsible next sequence is:

1. ML-00 evidence completeness;
2. ML-01 claim overlap review;
3. ML-10 telemetry schema;
4. ML-12 communication-subspace library + synthetic contracts;
5. ML-13/14 bridge and causal-control library;
6. ML-20 waypoint live diagnostic;
7. adjudicate before any second live bridge experiment;
8. ML-30 action-object autopsy if ML-20 establishes instrument credibility;
9. only then consider development/sleep work.

This sequencing maximises information gain while minimising the risk that the new idea becomes a broad architectural fashion imposed on every REE interface.

---

# Decision summary

The campaign should currently be treated as a **diagnostic-method programme with an architectural hypothesis**, not as a proposal to add latent bridges to REE.

The first decisive question is narrow:

> **At a current failure locus where the sender demonstrably contains task information, does that information overlap the actual consumer-facing communication subspace, and does a low-complexity frozen-endpoint transformation restore correct-pair-specific causal use?**

A clear answer to that question would determine whether the broader mutual-legibility thought deserves expansion into developmental and sleep mechanisms.
