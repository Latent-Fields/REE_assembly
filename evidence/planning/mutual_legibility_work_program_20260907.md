# Mutual legibility / communication-subspace work programme

**Date:** 2026-09-07  
**Status:** proposed staged work programme; no experiments queued, no claims registered, no task-ledger mutation performed here  
**Parent thought:** `docs/thoughts/2026-09-07_mutual_legibility_communication_subspaces.md`  
**Implementation companion:** `docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md`  
**Amended:** 2026-09-08 -- ML-13 addendum (receiver-conditioned rung) and ML-15b (recurrence stability assay), the MECH-547 / MECH-548 diagnostic arms; numbering unchanged, items appended only

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
- narrow nonlinear upper bound;
- receiver-conditioned `T(A, B)` (added 2026-09-08, MECH-547; see the addendum below).

Record parameter counts and regularisation.

**Acceptance:** synthetic rotation is recovered by Procrustes; nonlinear-only synthetic case is not falsely credited to the linear arms.

### ML-13 addendum (2026-09-08) -- receiver-conditioned rung `T(A, B)` (MECH-547)

A rung ABOVE the narrow nonlinear upper bound, not a replacement for it. `T(A, B)` takes the frozen sender state AND the frozen receiver's current state / position / context as inputs, so the communication subspace it exposes may be context-indexed (MECH-547 sharpening MECH-537). Endpoints stay frozen throughout, as for every rung.

**Exposure-not-solving constraint.** The rung decides *which part* of already-present sender information is exposed and *how* it is expressed. It must not solve the task independently: a high-capacity `T(A, B)` can compute an arbitrary joint function of both endpoints and become a hidden cognitive module (MECH-538), so this rung carries a stricter evidence burden than any linear rung.

**Mandatory arms whenever this rung is run:**

- **sender-only matched-capacity baseline `T(A)`** -- same parameter count and regularisation as `T(A, B)`, receiver input withheld;
- **receiver-state permutation control `T(A, B_perm)`** -- receiver states permuted across matched rows (episodes / contexts) so the receiver input carries no pairing with the sender row. This is the discriminator: if permutation barely changes the gain, the gain is capacity, not conditioning;
- the ML-14 correct-vs-mismatched sender control (INV-105) and zero / moment-matched random controls, applied to the conditioned bridge exactly as to every other rung;
- held-out environments / tasks -- required, not optional, for this rung.

Report parameter counts and regularisation identically for `T(A)`, `T(A, B)` and `T(A, B_perm)` (Gate C capacity disclosure). The receiver-manifold guard applies at step one here and becomes longitudinal in ML-15b.

**Acceptance (synthetic):** a planted receiver-indexed read surface (the sender exposes different subspaces under different receiver contexts) is recovered by `T(A, B)` and NOT by matched-capacity `T(A)`, and permuting the receiver context destroys that recovery; a planted context-free rotation is recovered equally by `T(A)` and `T(A, B)` and is permutation-insensitive, so the library does not falsely credit conditioning where none exists.

**Readings:** `T(A, B) > T(A)` held-out and permutation destroys the gain -> receiver conditioning is genuinely useful (MECH-547 confirming signature). `T(A, B) > T(A)` but permutation barely matters -> extra capacity; evidence about the bridge (MECH-538), not about conditioning. Either reading is diagnostic output only; nothing here authorises a conditioned bridge in `ree_core`.

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

## ML-15b -- Recurrence stability assay (MECH-548)

Added 2026-09-08. **Distinct from ML-15:** ML-15 asks whether a bridge is compatible with the receiver's *native dynamics* (MECH-539); this item asks whether the bridge's *own output re-entering as its input* stays stable (MECH-548), which can fail with perfectly compatible dynamics and a fixed sender. Applies to every ML-13 rung that shows a one-step rescue, including the receiver-conditioned rung. Both endpoints frozen; capacity matched where possible. The clean-base arm is what separates the two: if recomputing against the clean receiver state restores stability, the failure is MECH-548, not MECH-539.

**Arms** (application mode of the same bridge, repeated over the horizon the system actually traverses the interface):

- **cumulative repeated application** -- each step operates on the previously translated receiver state, `B_0 -> T(A_0, B_0) = B_1' -> T(A_1, B_1') = B_2' -> ...`;
- **clean-base / temporary-overlay application** -- each step computed against an unmodified native receiver state, the residual held as a gated overlay and discarded before the next step (state vs modulatory overlay at an interface; ARC-084 gated, gained coupling);
- at each application mode: the ML-14 zero / moment-matched random and correct-vs-mismatched sender controls, and the ML-13 addendum permutation control where the bridge is receiver-conditioned.

**Measures** (in addition to ML-13/ML-14 one-step consumer performance):

- multi-step consumer performance curve over steps;
- **receiver-manifold distance / drift over steps** -- the Gate C receiver-manifold guard made longitudinal; separates mechanism (a), off-manifold compounding;
- **bridge output norm / gain over time** -- separates mechanism (b), semantic double-counting; escalating gain is the interface-level form of MECH-363's runaway, an analogy across levels;
- **redundant re-injection of already-transmitted content** -- content the receiver already carries being re-amplified rather than recognised as present;
- task-information calibration over steps;
- dynamic compatibility with native receiver transitions (ML-15, MECH-539), recorded alongside so the two long-horizon failures are never conflated;
- correct-pair specificity at horizon, not only at step one.

**Readings** (from `docs/architecture/receiver_conditioned_translation.md`):

| Reading | Interpretation |
|---|---|
| `T(A,B) > T(A)` held-out, permutation destroys the gain | receiver conditioning is genuinely useful (MECH-547) |
| `T(A,B) > T(A)`, permutation barely matters | extra capacity, not conditioning (MECH-538) |
| one-step rescue, cumulative collapse, clean-base stable | recurrent interface instability (MECH-548) |
| cumulative stable with correct-pair specificity | functionally coherent recurrent bridge |
| both bridges fail, richer source information succeeds | upstream representation deficiency more likely |

**Acceptance (synthetic):** a constructed bridge that is one-step exact but drifts under cumulative application is flagged by the drift / gain measures and rescued by the clean-base arm; a constructed dynamics-incompatible bridge (the ML-15 failure case) fails under BOTH application modes, so the assay does not misattribute MECH-539 to MECH-548.

**Sequencing:** ML-15b runs on a live locus only AFTER ML-20's waking metric has shown range and stability at that locus, and BEFORE any ML-60/61 sleep assay -- a sleep-induced change that improves a static probe but destabilises the next waking trajectory is a failure, not consolidation (MECH-548 sleep corollary for MECH-540), so the recurrence measures must exist before a sleep result can be read. Any proposed E1/E2 interface repair is tested over the same horizons used to judge predictive competence.

**Scope note:** the ML-13 addendum and ML-15b together discharge the "diagnostic only" scope of MECH-547 / MECH-548 as registered (both `candidate`, `substrate_conditional`, "do not build in V3, do not queue"). They add no architectural option to Phase 7 or the ML-A* placeholders, queue no experiment, and change no claim. The diagnostic becomes v3-runnable once the ML-13 library exists; any architectural response stays v4 and routes through Gates A-D.

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
