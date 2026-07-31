# Failure Autopsy: V3-EXQ-794a (MECH-204 Phase 7 x SD-076 calibration loop, 2x2 retest)

**Status: AWAITING HUMAN CONFIRMATION (staging mode / headless run).** This is a draft diagnosis. Routing is not finalised; no manifest, claims.yaml, review_tracker.json, or substrate_queue.json field has been written by this session. A human or the next `/governance` walk must confirm before anything here is applied.

- **run_id**: `v3_exq_794a_mech204_phase7_sd076_calibration_loop_2x2_20260724T063301Z_v3`
- **queue_id**: V3-EXQ-794a
- **claim_ids**: MECH-204, SD-076
- **experiment_purpose**: diagnostic (excluded from governance confidence/conflict scoring per the manifest's own note)
- **outcome**: FAIL
- **supersedes**: `v3_exq_794_mech204_phase7_sd076_calibration_loop_2x2`
- **generated_utc**: 2026-07-31T21:53:02Z

## Why this autopsy exists (the reason flagged)

This run is administratively marked **reviewed** in `REE_assembly/evidence/experiments/review_tracker.json` (present in both `reviewed_run_ids` and `discussed_experiment_dirs`), but **"reviewed" means administratively cleared from the pending-review queue, not that a deep diagnosis was ever produced.** These are distinct facts and must not be conflated.

**Correction to the task's premise (important, stated explicitly here rather than silently):** a `failure_autopsy_*.json` artifact covering this run_id *does* already exist -- `REE_assembly/evidence/planning/failure_autopsy_backlog_2026-07-24.json` (status `confirmed`, scope `cluster`, generated 2026-07-24T18:59:26Z) lists it as one of 24 batch targets, with:

```
recommended_epistemic_category: measurement_test_design_defect
recommended_evidence_direction: inconclusive
routing: queue-experiment
four_layer_diagnosis: {claim_alignment: "unclear", biological_reference: "partial",
  prerequisites: "present", implementation: "complete", environment: "adequate",
  measurement: "misleading", integration: "coupled", scale: "adequate"}
```

That entry carries `status: "confirmed"` but is a **shallow batch pass**: single-word-per-layer values with no explanatory notes, no structured `biological_reference` object (dependencies / divergence / lit_status), no `learning_extracted`, no `re_derive_brake` accounting, no `granularity_debt_trigger` check, and no `recommended_substrate_queue_entry`. It never received the full four-layer diagnosis this skill exists to produce. `claims.yaml`'s `evidence_quality_note` for both MECH-204 and SD-076 still cites the *predecessor* run (794), not 794a -- confirming governance never actually applied either artifact's recommendation for 794a specifically, despite the review-tracker clearance. **This artifact is the deep diagnosis that never happened**, and supersedes the backlog entry's terse read of this run_id (it does not touch or withdraw the backlog file itself).

## Step 2a -- dry-run gate

```
scripts/check_dry_run_citations.py v3_exq_794a_..._20260724T063301Z_v3 v3_exq_794_..._20260721T113848Z_v3
-> 0 dry cited, 2 clean, exit 0
```
Neither the target nor its predecessor is a dry-run smoke. Manifest `dry_run` field is absent/falsy on both. Recording check (`ree-v3/validate_recording.py`) flags one advisory always-core gap: missing top-level `substrate_commit` (substrate_hash IS present). Not blocking.

## Facts reconstruction

**Design.** A 2x3 factorial (broadcast {OFF,ON} x asymmetry {OFF, LO=0.6, HI=0.8}), same-question re-run of V3-EXQ-794 against the repaired SD-076 headroom (`sd_waking_confidence_inflation_headroom`, ree-v3 `452f99e367`). V3-EXQ-794's confirmed autopsy found SD-076's absolute `rv` floor (0.01) sat above this substrate's real operating point, clamping `rv_final` at exactly 0.010000 on every inflation arm -- a saturation defect, not a null. The repair replaced the absolute floor with a scale-relative, softplus-saturating one.

**Preconditions.** All green. `all_green: true`. Every readiness gate (rv_live, f1_recalib_engaged, zero_point_populated, broadcast_moves_rv, inflation_lowers_rv, dose_levels_separated) passed on every arm.

**Criteria:**

| Criterion | Load-bearing | Passed | Non-degenerate | Note |
|---|---|---|---|---|
| C1 inflation creates absolute overconfidence | yes | **No** | **Yes (real)** | 0/6 seed-arm combos overconfident vs minimum 2 |
| C2 broadcast corrects under drift | yes | No | No (degenerate) | `d_broadcast_under_drift_at_operative` per_seed empty -- no operative drift level to correct |
| C3 interaction correction larger under drift | no | No | No (degenerate) | same cause as C2 |
| C4 OFF_OFF reproduces 774 ceiling | no | **Yes** | Yes | -0.192, matches 774's baseline regime |
| C5 asymmetry dose-response monotone | no | **Yes** | -- | LO score -0.041 -> HI score -0.023 |

`dose_levels_separated` precondition passed but **fragile**: measured 0.0001274 vs a floor of 0.0001, only ~27% margin.

**Interpretation label**: `drift_source_insufficient_dv_still_tautological` (same label string as the predecessor V3-EXQ-794, despite the underlying cause being materially different -- see adjudication below).

## The load-bearing new fact this autopsy surfaces

`substrate_queue.json`'s own record of the SD-076 headroom repair (`sd_waking_confidence_inflation_headroom` entry) documents its **validation smoke** result at this run's own measured error scale (true_error ~0.0037):

> "repaired config gives rv_final 0.0025377 (LO) vs 0.0021031 (HI), dose-ordered and **both genuinely overconfident**"

Compare against what the full behavioural run (794a) actually achieved:

| | baseline (ARM_OFF_OFF) | smoke prediction (repaired mechanism, isolated) | 794a full-loop result | full-loop reduction achieved vs smoke's demonstrated reduction |
|---|---|---|---|---|
| rv_final, LO | 0.005420 | 0.0025377 (53% reduction) | 0.003998 (26% reduction) | ~half |
| rv_final, HI | 0.005420 | 0.0021031 (61% reduction) | 0.003870 (29% reduction) | ~half |

**The same repaired mechanism demonstrably reaches the target "genuinely overconfident" regime in isolation, at this exact error scale, in the unit smoke -- but the full behavioural loop only gets about halfway there.** A DV that is tautological *by construction* (774's actual defect) cannot be pushed into the target regime by any input. This one demonstrably can be. So:

- **"drift_source_insufficient" is well-supported**: C1 fails non-degenerately at both doses in the full loop.
- **"dv_still_tautological" is NOT well-supported as stated**: the construction defect from 774 is fixed (confirmed by the repair's own smoke and by dose separation in the full run). What remains is an *unexplained gap between the full behavioural loop and the isolated-mechanism smoke*, not a residual tautology.

This is exactly the skill's "self-route is a hypothesis, not a verdict" case. Recommend the label be revised (e.g. `drift_source_subthreshold_at_full_loop_exposure_gap_vs_smoke_unexplained`) when this leg is next cited, rather than continuing to read "tautological."

## Claim-layer mapping

**MECH-204** (candidate, v3_pending, `depends_on`: MECH-123, MECH-186, MECH-178, INV-045). C2/C3 (the broadcast correction) remain untested for a **second consecutive run** -- 794's clamp bug prevented an operative drift level from forming; 794a's magnitude shortfall does too, for a different and still-unexplained reason. MECH-204's own claim has not been meaningfully exercised by either run.

**SD-076** (candidate, v3_pending, `depends_on`: ARC-016). The raw manifest self-tags `evidence_direction_per_claim.SD-076 = "does_not_support"`. **Recommend withdrawing that self-tag**, for the same class of reason 794's confirmed autopsy withdrew SD-076's prior `does_not_support`: a real, non-degenerate C1 failure exists at the tested doses, but the repair's own smoke shows the mechanism CAN reach the target regime at this scale, so the failure has not been shown to belong to the mechanism itself rather than to this specific full-loop test design.

## Biological-reference triage

Closest mechanism: REM-dependent precision recalibration (MECH-204) correcting waking metacognitive overconfidence drift under fatigue/sleep deprivation (SD-076). The asymmetric-EMA implementation of the drift source is a **formal/statistical import** (`is_formal_import: true`); `lit_status: partial` -- unchanged from 794's autopsy. No literature grounding yet establishes the expected *magnitude* of such drift, which is precisely the fact needed to judge whether the observed small, sub-threshold effect (log-ratio swing of only ~0.02 between LO and HI) is itself biologically plausible, independent of the smoke-vs-full-loop discrepancy documented above.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (both) | Real, dose-ordered, sub-threshold effect in the full loop vs a much larger effect in the isolated repair-validation smoke at the identical scale; an F1-interaction and/or exposure-budget confound is live and untested |
| Biological reference | partial | Formal/statistical import, no dedicated lit-pull on expected magnitude |
| Prerequisites | present (+1 newly surfaced) | Headroom repair confirmed landed and consumed; newly surfaced candidate dependency -- does F1/REM recalibration need to be a controlled variable to let SD-076's drift express its full magnitude? |
| Implementation | complete | No code defect this cycle (contrast with 794) |
| Environment | adequate for what was tested | Training budget (30 episodes, K=1) untested as a variable -- see scale row |
| Measurement | misleading (in one specific respect) | The self-route label overstates a construction defect the repair's own evidence contradicts; the instrumentation itself (per-arm gate, non-degeneracy flags, dose contrast) is sound |
| Integration | coupled but unstable | Unchanged from 794: C2/C3 cannot be evaluated until C1 clears. New: F1-recalibration interaction with SD-076 drift is untested |
| Scale / capacity | likely insufficient (newly flagged) | Full loop reaches ~half the drift magnitude the isolated smoke demonstrated is achievable at this scale |

## Recommended routing

**`queue-experiment`** -- this is a `complex (probe-gated) / puzzle (known rules)` node: the frame is well-posed (why does the full loop underperform the smoke?) but a fact is missing. **Not** `implement-substrate` -- no new substrate build is indicated; the headroom repair already works as designed.

### GOV-FANOUT-1: discrimination portfolio (not a single re-pose)

Three live, structurally distinct hypotheses for the smoke-vs-full-loop gap:

- **H1 (integration axis)** -- F1/REM recalibration (`rem_precision_recalibration_step=0.25`, ON in every arm by design necessity) interacts with and partially damps SD-076's waking-induced drift before eval. *Probe*: re-run the INFL-only arms with F1 recalibration disabled at the same doses/budget; if `rv_final` approaches the smoke's range, H1 is confirmed.
- **H2 (exposure/world axis)** -- the training budget (30 episodes, K=1 sleep) is too short for the asymmetric EMA to accumulate as much drift as the smoke's own update sequence reached. *Probe*: re-run INFL-only arms (F1 held ON as in 794a) with a substantially larger training budget at the same doses.
- **H3 (representation axis, the driver's own pre-registered fallback)** -- the asymmetric-EMA form is the wrong drift-source mechanism entirely. *Probe*: this one is not an experiment -- it needs a `/lit-pull` commission on expected magnitude/timescale of waking overconfidence drift in the literature. **Weakened, not eliminated**, by the smoke-comparison finding above: the same mechanism form demonstrably reaches the target regime in isolation at this scale, arguing against a pure mechanism-form defect.

H1 and H2 are cheap, parallel, single-axis re-runs and should both be queued; do **not** queue a single re-pose of 794a with a higher asymmetry dose -- the driver's own docstring already pre-registers that a both-levels-fail should not be read as "sweep higher," and HI=0.8 is stated to already be at the edge of the defensible optimism-bias band.

## Re-derive brake (MOVE-3) and granularity-debt check

- **Re-derive brake**: MECH-204 = 0 confirmed `substrate_ceiling` hits under the R1-R3 convention (re-derived 2026-07-31 across the 4 prior confirmed files tagging this claim). SD-076 = 0. This target recommends `measurement_test_design_defect`, not `substrate_ceiling`, so the count is unaffected and the brake does **not** fire.
- **Granularity-debt trigger**: re-ran `scripts/granularity_debt_cluster.py` for both claims. MECH-204: 6 targets / 4 files (+1 superseded), alignment distribution `intact=2, strengthened=2, unclear=1 (this target), untested=1` -- **no target reads `weakened`**, so per the skill's own rule this does **not** fire (measurement/implementation debt, not granularity debt, however many autopsies exist). SD-076: 2 targets / 2 files, `unclear=1, untested=1` -- also does not fire.

## Learning extracted

1. A `confirmed` status on a `failure_autopsy_*.json` artifact does not guarantee the skill's full depth was applied -- the 2026-07-24 batch backlog entry for this run carries `confirmed` with only single-word four-layer fields and none of the optional-but-expected substructure (biological triage object, learning_extracted, re_derive_brake, granularity_debt_trigger).
2. `review_tracker.json` "reviewed" means administratively cleared from the pending-review queue, **not** that a deep diagnosis exists -- confirmed here independently: `claims.yaml` still cites the predecessor run for both claims.
3. A substrate repair's own validation-smoke numbers, recorded only in `substrate_queue.json` rather than in any `failure_autopsy` artifact, can be decisive counter-evidence to a self-route label and to a driver's own pre-registered fallback interpretation. Cross-referencing them mattered here.
4. A self-route label generated by the same code path across a lettered sequence can carry forward wording accurate for the predecessor's specific defect but no longer accurate once that defect is repaired -- the label describes the *shape* of the criteria failure, not its cause, and the cause changed materially between 794 and 794a.
5. Minor recording-completeness gap: manifest `config` omits the SD-076 headroom-repair-specific knobs even though the driver applies them; a successor script should fold these in.

## Draft evidence_quality_note (governance to apply, not written by this session)

See `recommended_evidence_quality_note` in the companion JSON -- full text drafted there for both MECH-204 and SD-076.

## EVB-0454 relevance

`experiment_proposals.v1.json` EVB-0454 requires a governance decision (`retain_ree | hybridize | retire_ree_claim`) on SD-076 by **2026-08-03T20:50:36Z**, and was drafted pointing at the *794* experiment_type as its suggested template. 794a already substantively is the requested discriminative pair (matched seeds, pre-registered thresholds), but on this evidence **retiring SD-076 now would be premature** (biology only partially grounded; the smoke-comparison evidence argues against the "wrong mechanism" reading that would most support retirement), and neither retaining without further work nor hybridizing is yet well-founded either. The H1/H2 probes above are queueable immediately and cheap; flagging the timing risk against the 2026-08-03 deadline for governance rather than resolving it here.

## Hypothesis-space ledger (drafted only -- staging mode)

Per Step 9b staging-mode instructions, `hypothesis_space_registry.v1.json` was **not** written. A full pre-registration block (question `mech204-sd076-calibration-loop-drift-source-exposure-gap`, 3 hypotheses H1/H2/H3, `initial_frozen_count: 3`, all `alive`) is drafted in the companion JSON under `hypothesis_space_ledger_pending` for a human/governance session to append.

## Not done in this staging-mode session

- No `AskUserQuestion` / interactive gate (staging mode substitutes this draft).
- No `spawn_task` follow-on from this autopsy's own routing (per the 2026-07-30 rule) -- H1/H2/H3 probes and the biological lit-pull are named here for governance to chip once ratified, not spawned by this session.
- `hypothesis_space_registry.v1.json`, `claims.yaml`, `review_tracker.json`, `substrate_queue.json` -- untouched.
