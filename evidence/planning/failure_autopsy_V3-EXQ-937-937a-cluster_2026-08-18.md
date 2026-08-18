# Failure autopsy -- V3-EXQ-937 + V3-EXQ-937a (cluster)

- **Generated (UTC):** 2026-08-18T07:33:15Z
- **Scope:** cluster (2 targets). Primary: **V3-EXQ-937a** (named by the user). Read-across member: **V3-EXQ-937**, which shares the identical defect and was unadjudicated.
- **Status:** confirmed (interactive gate cleared 2026-08-18)
- **Trigger:** `experiment_purpose: "diagnostic"` -- ALL diagnostics require autopsy, PASS or FAIL, flagged or not.
- **Claims tagged by both runs:** MECH-449, ARC-107
- **Dry-run gate:** `check_dry_run_citations.py` -- 0 dry cited, 0 dry in named families, 0 ambiguous, **2 clean**, 0 unknown. Neither manifest carries a truthy top-level `dry_run`. No dry run is cited anywhere below; every denominator is a real-run denominator.

---

## 1. Facts

### 1a. V3-EXQ-937a (primary)

`v3_exq_937a_mech449_envelope_inertness_point_20260818T015809Z_v3` -- PASS, `experiment_purpose: diagnostic`,
`evidence_direction: supports` on both MECH-449 and ARC-107, self-route
`interpretation.label = envelope_width_gates_perseveration_conversion`.
Machine `ree-worker-1`, `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`,
`substrate_hash c5b6fecb...`, `substrate_commit 6036902412...` (clean), 3 seeds (42/43/44),
3 arms x 11 envelope floors x 128 banks.

Grid: `ENVELOPE_FLOORS = [0.60, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05]`;
`K_CANDIDATES = 4`; `gng_perseveration_floor = 0.5`; substrate default
`gng_protect_min_eligible = 1` (`ree-v3/ree_core/utils/config.py:1432`).

| Criterion | Gated | Verdict | Measured | Threshold |
|---|---|---|---|---|
| C1_envelope_width_dose_response | **yes (load-bearing)** | PASS | per-seed lift 0.532 / 0.509 / 0.491, 3/3 seeds clearing | 0.40, 2 of 3 seeds |
| C2_conversion_monotone_in_envelope_width | reported | FAIL | step envelope 3 -> 4 delta **-0.319** | >= -0.10 |
| C3_safety_failopen | yes | PASS | 0 empty-eligible | 0 |
| C4_inert_regime_reached_on_ladder | reported | FAIL | **0.784** | <= 0.10 |

`combination_rule`: `PASS = readiness_ok AND C1 AND C3`. All three readiness preconditions MET
(P1 suppression cross-candidate range 0.75 vs floor 0.25; P2 envelope dose separation 3.0 vs floor 1.0;
P3 `from_dims` plumbing live). All four criteria stamped `criteria_non_degenerate: true`.

**Which criterion failed:** neither gated criterion. Both reported-not-gated criteria failed, and
**both failures are artifacts of the analysis layer, not of the substrate** (Section 2).

Reported curve, ARM_CONSTITUTION, and the realized mediator:

| floor | 0.60 | 0.50 | 0.45 | 0.40 | 0.35 | 0.30 | 0.25 | 0.20 | 0.15 | 0.10 | 0.05 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mean conversion | 0.784 | 0.534 | 0.349 | 0.263 | 0.406 | 0.685 | 0.823 | 0.898 | 0.956 | 0.979 | 0.997 |
| mean cell-median envelope | 4 | 4 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 |

ARM_OFF and ARM_SHUFFLED convert **0.000 at every one of the 11 doses**.

### 1b. V3-EXQ-937 (read-across member)

`v3_exq_937_mech449_envelope_width_dose_response_20260818T013927Z_v3` -- FAIL, `diagnostic`,
`evidence_direction: non_contributory` on both claims, self-route
`interpretation.label = conversion_independent_of_envelope_width`. Ran 19 minutes before 937a on
the same claims and the same substrate. Ladder 0.30 -> 0.05 only.

- C1 (load-bearing) FAIL: per-seed lift 0.344 / 0.273 / 0.320 vs threshold 0.40, **0 of 3** seeds clearing.
- C2 PASS on a floor-keyed monotonicity, but stamped **`criteria_non_degenerate: false`** -- so its pass is degenerate.
- C3 PASS.

937a's own header already identifies 937's routing-label defect: 937 emitted
`conversion_independent_of_envelope_width` on its C1-fails branch **while its own C2 had passed with a
clean monotone rise**. This autopsy finds the label false for a second, independent and stronger
reason (Section 2).

### 1c. Recording provenance

`ree-v3/validate_recording.py` on the 937a manifest: **1 always-core gap, `elapsed_seconds` missing**
(advisory). `recording_schema`, `substrate_hash`, `substrate_commit`, `machine`, `machine_class`,
`config` and the explicit `seeds` list are all present, so the run is identifiable and reproducible
and no `substrate_ceiling`-style unfalsifiability applies. The load-bearing recording gap is a
different one -- Section 3.

---

## 2. What the runs actually measured

The driver computes, per bank, both the pre-No-Go envelope size and whether the commit converted,
in the same loop iteration
(`ree-v3/experiments/v3_exq_937a_mech449_envelope_inertness_point.py:536-549`), and emits only the
cell **median** of the first and the **count** of the second. The joint distribution is discarded.

This autopsy recovered it by re-running the driver's own cell loop unmodified (throwaway probe, no
manifest written), over the full ladder: **11 floors x 3 seeds x 128 banks = 4,224 banks.**

| pre-No-Go envelope size | n banks | converted | conversion rate |
|---|---|---|---|
| 1 | 1277 | 0 | **0.000000** |
| 2 | 1196 | 1196 | **1.000000** |
| 3 | 1062 | 1062 | 1.000000 |
| 4 | 689 | 689 | 1.000000 |

**Conversion is a deterministic step function of per-bank envelope size**, with zero variance, and it
steps exactly where the substrate says it must. At envelope 1 the fail-open guard computes
`n_can_drop = max(0, elig_mask.sum() - protect_min) = max(0, 1 - 1) = 0`
(`ree-v3/ree_core/predictors/e3_selector.py:1664-1679`), so every soft-No-Go'd candidate is
re-admitted and no exclusion occurs. At envelope >= 2 the incumbent -- which in this construction is
both the F-argmin and the sole suppression target -- is always droppable and is always dropped.

And therefore, at **every one of the 11 doses**:

```
manifest_conversion(floor)  ==  1 - P(envelope collapses to 1 | floor)      to 0.000000
```

| floor | 0.60 | 0.50 | 0.45 | 0.40 | 0.35 | 0.30 | 0.25 | 0.20 | 0.15 | 0.10 | 0.05 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P(collapse to envelope 1) | .2161 | .4661 | .6510 | .7370 | .5938 | .3151 | .1771 | .1016 | .0443 | .0208 | .0026 |
| 1 - P(collapse) | .7839 | .5339 | .3490 | .2630 | .4062 | .6849 | .8229 | .8984 | .9557 | .9792 | .9974 |
| manifest conversion | .7839 | .5339 | .3490 | .2630 | .4062 | .6849 | .8229 | .8984 | .9557 | .9792 | .9974 |
| residual | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**The reported dose-response curve is, to machine precision, the mediator's own distribution.** It
carries no independent information about the outcome given the mediator.

Four consequences, in order of how much they would have misled a governance reader:

**(i) C4's "informative null" is refuted by the run's own discarded data.** The manifest reports that
no inert regime was reached on the ladder. An inert regime *was* reached, and it is perfectly inert:
1277 banks at envelope 1, **0** conversions. The driver's header frames this null as the finding that
would mean V3-EXQ-926a's "structurally gated by envelope width" finding of record is "wrong rather
than merely mis-scaled". 926a's finding is **confirmed**, not refuted.

**(ii) C1 is not the independent test the manifest claims it is.** The manifest's P2 note asserts
"Not circular: P2 measures the MEDIATOR responding to the knob, C1 the OUTCOME responding to the
mediator." Because the outcome is a deterministic function of the mediator per bank, C1 is a
coarsened re-measurement of the same distribution P2 gates on. C1 is not *strictly* entailed by P2 --
one can construct envelope distributions giving a lift below 0.40 -- but it is not an independent
probe of the outcome, and the non-circularity claim as written is false.

**(iii) C2's monotonicity failure is a binning artifact.** Per bank the relation is monotone (a step).
The reported -0.319 drop at envelope 3 -> 4 comes entirely from cells whose *median* is 4 (floors 0.60
and 0.50) containing ~22% envelope-1 banks. The manifest's `combination_rule` defends the failure as
"a step-shaped gating relation is a legitimate and informative curve shape" -- which is correct about
the mechanism and wrong about what C2 measured.

**(iv) C4's `measured` field is keyed to the wrong axis.** Its verdict is envelope-keyed
(`inert_envelope is not None`) but its reported statistic is `conv_by_floor[max(floors)]` = 0.784 at
floor 0.60 -- and floor 0.60 folds *open* to envelope 4, the **widest** realized envelope. A reader
sees "0.784 against a 0.10 inertness ceiling" and reads it as conversion at the narrowest envelope.
This is precisely the defect the driver's header says it fixed from 937 ("Everything below is
therefore keyed to the REALIZED envelope size"), surviving in one field. The same applies to
`criteria_non_degenerate["C4..."]`, whose test is `max(floors) >= 0.60` -- a floor-based premise the
run itself refutes. Both reach the right answer through the wrong statistic; the correct number,
`conversion_protect_min_regime = 0.339`, is recorded separately and is itself a median-binned mixture.

### 2a. Control adequacy

- **ARM_OFF is tautological on this metric, and the manifest does not say so.** Its committed pick
  *defines* the incumbent, so it cannot differ from it; and it never constructs an envelope at all
  (`median_pre_nogo_envelope_size = 0.0` at every dose, because the `go_nogo_envelope_size`
  diagnostic is only set when the gate runs), so the swept knob is inert in that arm by construction.
  The **driver docstring states this plainly** ("a tautological control on this metric and proves
  nothing about the envelope"); the **manifest's `dv_symmetry_declaration.ARM_OFF` states only the
  intended dis-aliasing purpose and omits the limit.** Governance reads the manifest. The
  dis-aliasing the manifest credits to ARM_OFF is in fact carried by
  `incumbent_is_f_argmin_rate = 1.0`, a different statistic.
- **ARM_SHUFFLED is a genuine control and passes cleanly.** Measured 0 conversions at **every**
  envelope size, including 2, 3 and 4 where the leg fires deterministically in ARM_CONSTITUTION. It
  could have converted had the exclusion been mis-targeted, so its null is informative: the No-Go is
  content-addressed to the suppressed candidate, not indiscriminate.

### 2b. The question the runs were posed, now answered

The stated deliverable was "the knee: the narrowest envelope at which the leg has authority", and the
build-configuration question "is the ARC-107 perseveration leg inert at the shipped
`f_eligibility_envelope_floor = 0.30`?"

- **Knee: realized envelope 2, exactly, with zero variance.** (The manifest's
  `knee_envelope_first_clearing_half: 2.0` is right; its `knee_floor_first_clearing_half: 0.6` is a
  fold-back artifact and is misleading as "the narrowest floor at which the leg has authority".)
- **At the shipped default floor 0.30: 31.5% of decisions (121/384 banks) collapse to envelope 1,
  where the leg is structurally inert; the other 68.5% fire deterministically.** So the leg is **not
  inert as configured** -- but it is **silenced on roughly a third of decisions** by the
  `gng_protect_min_eligible` fail-open. That is the ARC-107 roadmap fact, and it is sharper than the
  0.685 the manifest reports (of which it is the exact complement).

---

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | MECH-449 and ARC-107 both confirmed at per-bank resolution. Direction unchanged; the *basis* recorded on the manifest is wrong in two halves and is corrected here. |
| Biological reference | **clear** | BG direct/indirect opponency at the pallidal permission gate. `gng_protect_min_eligible` is a faithful functional analog of the anti-akinesia constraint that a minimum of channels stays released -- complete indirect-pathway dominance produces freezing/avolition. The measured structural inertness at one surviving channel is exactly what that analog predicts. **Not** a formal-definition import, so no `/lit-pull` commission is owed. |
| Developmental / dependency prerequisites | **present** | MECH-448 envelope built and live; MECH-260 suppression supplied from a real `DACCAdaptiveControl` history via `record_action()` + `_suppression_penalty()`; all three readiness preconditions met. |
| Implementation completeness | **complete** | Verified twice and independently: by source read (`e3_selector.py:1483-1575`, `:1596-1690`) and by 4,224-bank re-measurement. The substrate does exactly what MECH-449 and the protect-min guard specify. |
| Environment adequacy | **adequate for the question asked** | Synthetic selection face, no training (`reuse_ineligible_reasons: ["selection_face_synthetic_no_training"]`). Correct for a selection-face arithmetic characterisation; it bounds generality, it is not a gap. |
| Measurement adequacy | **misleading** | A per-bank deterministic mediator binned at cell-median granularity; the reported curve is identically the mediator's own distribution; one criterion's reported statistic keyed to the wrong axis. This is the failing layer. |
| Integration adequacy | **isolated** | Selection face only, no agent loop. By design. |
| Scale / capacity | **likely insufficient for generality** | At `K_CANDIDATES = 4` with integer `protect_min = 1`, MECH-448's deliberately *graded* divisive-normalisation envelope realizes only 4 states and the downstream No-Go's authority is **binary**. The step shape may be an artifact of small K rather than a property of the constitution. Unknown in K. |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **not established** -- Implementation reads `complete`. |
| MEASURES FAILED | **established** -- Measurement adequacy reads `misleading`. |
| ENVIRONMENT FAILED | **not established** -- Environment adequate for the question asked. |
| REE FAILED | **false** -- requires all three established. |

**Net classification: MEASURES FAILED (single bucket).** Not chargeable to the mechanism, to the
environment, or to REE. The substrate performed exactly as specified; the analysis layer mis-read it.

### Recommended epistemic_category

**`standard`** for both claims, both targets. The finding is in the measurement / test-design family,
for which `standard` is the behaviour-preserving mapping: it asserts no epistemic suppression, keeps
both claims outside `_EPI_SUPPRESS_PROPOSAL`, and preserves v3-testability. Nothing here asserts the
claims' answers are gated on substrate work, so `substrate_ceiling` / `substrate_conditional` would be
wrong. MECH-449 already stores `standard` (unchanged); **ARC-107 stores no category at all, so this is
a real write.**

---

## 4. Cluster pattern

| Experiment | Claims | Absolute / negative-control criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-937 | MECH-449, ARC-107 | C3 fail-open PASS; ARM_SHUFFLED 0.000 at 6/6 doses | C1 FAIL 0/3 seeds; C2 pass but **non-degenerate false** | Curve is `1 - P(collapse)` over floors 0.30-0.05 |
| V3-EXQ-937a | MECH-449, ARC-107 | C3 fail-open PASS; ARM_SHUFFLED 0.000 at 11/11 doses | C1 PASS 3/3; C2 FAIL; C4 FAIL | Same identity over the full 11-dose ladder |

**These are ONE structural property, not two independent bugs.** Both runs estimate the same
quantity -- the distribution of realized envelope size as a function of the floor -- and both label it
as a property of the *outcome*. The shared root is a single analysis choice: binning a per-unit
deterministic mediator at cell-summary granularity while the per-unit joint is available and
discarded. Everything that differs between the two runs (937's C1 failing and 937a's passing, 937's
C2 passing and 937a's failing) follows from the ladder window each happened to sample, not from any
difference in the substrate or the mechanism.

The two readings that were live before this autopsy -- "graded dose-response" (937a) versus
"conversion independent of envelope width" (937) -- are **both wrong**, and in opposite directions.
The true relation is a hard structural threshold at envelope 2. This is why the cluster is the
load-bearing unit: per-run, 937a's PASS looks like a clean measurement and 937's FAIL looks like
tuning noise against a mis-calibrated bar.

**Planning decision forced:** any future ARC-107 / MECH-448 / MECH-449 readout keyed to a cell-level
conversion rate over a discrete eligibility envelope is measuring the envelope-size distribution, not
the gating. Key such criteria to the per-unit mediator, and record the per-unit joint.

---

## 5. Granularity-debt recurrence trigger

**Does NOT fire.** `granularity_debt_cluster.py`:

- **MECH-449** -- 2 tagging targets across 2 files: `failure_autopsy_V3-EXQ-699_2026-07-20`
  (`claim_alignment: intact`, `non_contributory` / `measurement_test_design_defect`) and
  `failure_autopsy_backlog_2026-07-24` (`claim_alignment: unclear`, `non_contributory` /
  `measurement_test_design_defect`). Alignment distribution: intact=1, unclear=1.
  **No target reads `weakened`**, which is the condition, not the count.
- **ARC-107** -- 0 tagging targets. The trigger cannot fire.

**But record the pattern that IS there.** With this cluster, **3 of 3** MECH-449 autopsy targets are
measurement / test-design defects. That is *measurement*-debt recurrence, not granularity debt -- the
claim is not coarse, it keeps being tested with instruments that break. `/claim-synthesis` is
**not** the right route; instrument discipline is.

## 6. Re-derive brake (MOVE-3)

**Does NOT fire.** Ceiling hits under the R1-R3 convention (run-unit, latest-adjudication-wins,
`substrate_ceiling` only): **MECH-449 = 0** (of 2 tagging targets), **ARC-107 = 0** (of 0). Threshold
is 2. The driver's own header asserted the same counts and is confirmed. No re-queue is refused.

## 7. GOV-FANOUT-1

**Not applicable.** This is not a discrimination bottleneck. There were two live readings before the
autopsy and the recovered per-bank joint settles them outright, with zero residual variance -- there
is nothing to fan out over. The remaining work is a single unambiguous change (record the joint).

## 8. Hypothesis-space ledger (Step 9b)

**Skipped cleanly.** No `questions[]` entry in `hypothesis_space_registry.v1.json` names MECH-449,
ARC-107 or MECH-448 (37 questions checked), and this autopsy emits no `fanout_recommendation`, so
there is neither a leg to pre-register (Mode A) nor a pre-registered leg to resolve (Mode B), and no
discovery leg is being attached to an existing question (Mode C). No growth-restriction check applies,
because no leg attaches to an already-registered question. The registry, its two derive-only siblings
and the integrity report are **not** touched by this autopsy.

---

## 9. Learning extracted

1. **A cell-level rate over a per-unit deterministic mediator measures the mediator's distribution,
   not the outcome.** Here the identity is exact to 0.000000 at all 11 doses. The tell is available
   cheaply and in advance: if the mechanism predicts a *structural* (not statistical) relation, the
   criterion must be keyed to the per-unit mediator, because any cell-level summary of it is a mixing
   proportion.
2. **A structural prediction stated in a driver header is a testable assertion and should be
   asserted, not assumed.** 937a's header states three times that conversion at envelope 1 is "0 BY
   CONSTRUCTION -- not as an empirical tendency but as a structural property of the guard", and derives
   the C1 threshold of 0.40 from it. That prediction is exactly right; the analysis then never
   evaluated it, and reported 0.339 in the one place it would have shown up.
3. **Recording-debt, not measurement-debt.** The deciding readout existed at run time, in the same
   loop iteration, two lines from the manifest. It was recoverable here only because this is a
   synthetic selection-face probe that re-runs in seconds; on any trained substrate the identical
   omission would have forced a full re-run.
4. **A criterion whose verdict and whose reported statistic are keyed to different axes is a distinct
   defect class.** C4's boolean was correct and its `measured` field pointed at the fold-back point.
   Both halves must move together when a design is re-keyed.
5. **An honest limit recorded in the driver but omitted from the manifest is not recorded.**
   ARM_OFF's tautology is stated plainly in the docstring and absent from
   `dv_symmetry_declaration`, which is the artifact governance consumes.
6. **MECH-448's "graded" envelope is functionally binary for the MECH-449 leg at K=4.** With four
   candidates and integer `protect_min = 1`, the No-Go has authority or it does not; there is no
   graded regime. Whether the constitution's gradation is real at larger K is untested and should not
   be assumed from these runs.
7. **A convergent-shape cluster inverted the per-run readings.** 937 alone reads as tuning noise
   against a mis-calibrated bar; 937a alone reads as a clean graded measurement. Neither is right, and
   only the pair plus the recovered joint shows why.

---

## 10. Routing (confirmed at the Step 8 gate)

**Recording gap -> `/queue-experiment`, same-question re-run with an alphabetic suffix (V3-EXQ-937b).**

The single change is to **record** the readout that already existed, per the Experimental Recording
Standard (`REE_assembly/evidence/planning/experimental_recording_standard_2026-07-12.md`, Section 3b
always-core and Section 3c family-keyed payload). Specifically the re-run must:

- emit the per-bank `(pre_No-Go envelope size, converted)` cross-tab per cell, not only the cell
  median and the conversion count;
- re-key C1, C2 and C4 to that cross-tab (C4's `measured` field included, not only its verdict);
- call `experiments/_lib/manifest_core.stamp_recording_core(...)` and close the `elapsed_seconds`
  always-core gap;
- carry the ARM_OFF tautology limit from the driver docstring into
  `interpretation.dv_symmetry_declaration` so the manifest states it.

A blind re-run would reproduce the same blind spot at the same compute cost. `substrate_queue`
action is **`none`** -- the substrate is correct and no substrate gap was found; there is nothing for
`/implement-substrate` to build.

The finding does not depend on 937b running: the table in Section 2 is complete, and its recipe
(re-run the driver's own cell loop and record the joint) is stated here so it is reproducible from
this artifact alone.

## 11. Draft `evidence_quality_note` for governance -- DO NOT APPLY FROM THIS SKILL

### MECH-449 and ARC-107 (from V3-EXQ-937a)

> 2026-08-18 (failure_autopsy_V3-EXQ-937-937a-cluster CONFIRMED): V3-EXQ-937a PASS / supports STANDS,
> with its BASIS CORRECTED. The manifest's stated basis is wrong in two halves and must not be cited:
> it reports (a) a graded dose-response of conversion on envelope width and (b) that no inert regime
> was reached on the ladder. The autopsy recovered the per-bank (pre-No-Go envelope size, converted)
> joint that the driver computes at v3_exq_937a...py:536-549 and discards, over 11 floors x 3 seeds x
> 128 banks = 4,224 banks: conversion is a DETERMINISTIC STEP FUNCTION of per-bank envelope size --
> envelope 1 -> 0/1277 conversions (rate 0.000000), envelope 2/3/4 -> 1196/1196, 1062/1062, 689/689
> (rate 1.000000) -- stepping exactly where gng_protect_min_eligible=1 predicts (n_can_drop = 1-1 = 0
> at envelope 1; e3_selector.py:1664-1679). Consequently manifest_conversion(floor) == 1 -
> P(envelope collapses to 1 | floor) to 0.000000 at ALL 11 doses, i.e. the reported curve is the
> mediator's own distribution and carries no independent information about the outcome given the
> mediator. So: (a) is a binning artifact of cell-median aggregation, and (b) is REFUTED by the run's
> own discarded data -- an inert regime was reached and is perfectly inert, which CONFIRMS rather than
> refutes V3-EXQ-926a's "structurally gated by envelope width" finding of record. The corrected basis
> supports MECH-449 and ARC-107 MORE strongly than the manifest claims: the No-Go leg fires
> deterministically whenever it has room (envelope >= 2) with perfect content specificity
> (ARM_SHUFFLED 0/4224 at every envelope size), and the gng_protect_min_eligible fail-open behaves
> exactly as specified. ANSWERS THE ARC-107 BUILD-CONFIGURATION QUESTION: the knee is realized
> envelope 2 exactly (zero variance), and at the shipped f_eligibility_envelope_floor=0.30 the leg is
> NOT inert but IS silenced on 31.5% of decisions (121/384 banks collapse to envelope 1) by the
> fail-open guard. THREE CAVEATS THAT GATE ACTING ON THIS. (1) Selection-face synthetic probe, no
> training (reuse_ineligible_reasons: selection_face_synthetic_no_training) and no agent loop: this
> confirms the constitution's arithmetic, not any behavioural competence; purpose=diagnostic, so it
> scores nothing and PROMOTES NOTHING. (2) At K_CANDIDATES=4 with integer protect_min=1, MECH-448's
> deliberately GRADED envelope realizes only 4 states and the MECH-449 leg's authority is BINARY --
> the step shape may be an artifact of small K and generality in K is untested. (3) conversion==1 at
> envelope >= 2 is a construction property: the incumbent is both the F-argmin and the sole
> suppression target. Failure-location (GOV-FAILLOC-1): MEASURES FAILED, single bucket -- mechanism
> and environment each independently adequate, so this is not chargeable to REE or to the mechanism.
> epistemic_category standard (measurement/test-design family; behaviour-preserving). Routed
> /queue-experiment V3-EXQ-937b, recording-only. Re-derive brake NOT fired (MECH-449=0, ARC-107=0).

### MECH-449 and ARC-107 (from V3-EXQ-937)

> 2026-08-18 (failure_autopsy_V3-EXQ-937-937a-cluster CONFIRMED): V3-EXQ-937 FAIL /
> non_contributory STANDS, and its SELF-ROUTE LABEL IS WITHDRAWN AS FALSE. The manifest emits
> interpretation.label = conversion_independent_of_envelope_width; per bank, conversion is a
> DETERMINISTIC function of envelope width (see the sibling note on V3-EXQ-937a). The label was
> already contradicted by 937's own C2, which passed with a clean monotone rise, and 937's C2 is
> additionally stamped criteria_non_degenerate=false, so it never supported anything either.
> non_contributory is retained because 937's criteria measured the wrong statistic -- its C1 lift
> (0.344/0.273/0.320 vs a 0.40 bar calibrated on a V3-EXQ-926a anchor that did not replicate) is the
> same cell-median mixing proportion as 937a's, over a narrower window -- not because the run yielded
> no interpretable information. Its underlying data, re-analysed per-bank, is consistent with the
> confirmed step and with 937a. Same root cause, same cluster, one structural property rather than two
> independent bugs. epistemic_category standard. Re-derive brake NOT fired.
