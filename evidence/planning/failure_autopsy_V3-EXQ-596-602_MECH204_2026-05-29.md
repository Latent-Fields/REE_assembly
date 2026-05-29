# Failure Autopsy -- V3-EXQ-596 / V3-EXQ-602 (MECH-204 cluster integration)

**Date:** 2026-05-29T16:57:14Z
**Scope:** cluster (2 same-script FAILs, identical config, one-day-apart rerun)
**Status:** confirmed
**Predecessor:** [failure_autopsy_EXQ-541_MECH204_2026-05-17.md](failure_autopsy_EXQ-541_MECH204_2026-05-17.md)
**Plan-of-record:** [sleep_substrate_plan.md](sleep_substrate_plan.md)

---

## Summary

V3-EXQ-596 (2026-05-20T04:41:51Z) and V3-EXQ-602 (2026-05-21T08:58:38Z) are the
closure-handoff integration EXQ -- a single script combining V3-EXQ-541c's F1
MECH-204 consumer with the GAP-3 unified sleep-aggregation-cluster master flag
and the canonical waking StepHarness path. Both runs FAILed `overall_pass`
because the C2 cluster-liveness criterion (`cluster_live_frac_post_warmup >=
50%`) was registered against an expectation the K=1 single-fire driver
**cannot produce by construction**: MECH-285 SleepReplaySampler draws once at
the buffer-fill cycle (episode 2 in both runs), then `mech285_n_draws = 0` for
every subsequent cycle. Every seed in every arm in both runs reports
`cluster_live_frac_post_warmup = 0.0909... = 1/11` -- a deterministic property
of the driver pattern, not a stochastic failure.

The MECH-204 dimension itself is **strengthened, not weakened**: C1 fires every
cycle in 3/3 seeds; C3 relative rv divergence runs 8.4-27.6% per seed, well
above the 3% threshold and exceeding the canonical 541c PASS bar (4.5-9% at 16
cycles). This is **a different layer of the four-layer table from the 541
family** (which failed on scale / cycle-budget). 596/602 fail on measurement
+ integration: the C2 criterion is a cluster-liveness test that is not a
MECH-204 prediction.

Routing: **R1 -- /queue-experiment with measurement redesign + reclassify
596/602 to inconclusive_measurement.** No new substrate_queue entry. No
amendment to existing sleep_substrate_plan.md GAP nodes (all already done).

---

## Targets

| Experiment | Run ID | Claims | Outcome | Current ev_dir | Recommended ev_dir |
|---|---|---|---|---|---|
| V3-EXQ-596 | v3_exq_596_mech204_sleep_cluster_stepharness_integration_20260520T044151Z_v3 | MECH-204 | FAIL | non_contributory | **inconclusive_measurement** |
| V3-EXQ-602 | v3_exq_596_mech204_sleep_cluster_stepharness_integration_20260521T085838Z_v3 | MECH-204 | FAIL | non_contributory | **inconclusive_measurement** |

(Note: V3-EXQ-602 uses the same experiment_type and script as V3-EXQ-596; only
the timestamp and queue_id differ. The 602 runner signal points at the
596-named manifest path.)

---

## Facts reconstruction

Both runs use identical config: 2 arms (ARM_0_off step=0, ARM_1_step_0_25
step=0.25), 3 seeds (42/43/44), 12 episodes per run, 150 steps/episode,
sleep_loop_K=1, use_sleep_aggregation_cluster=True, stepharness_waking=True.

| Criterion | Threshold | EXQ-596 (3 seeds) | EXQ-602 (3 seeds) |
|---|---|---|---|
| C1: fires_every_cycle | >= 2/3 seeds | PASS (3/3) | PASS (3/3) |
| C2: cluster_live_frac_post_warmup >= 50% | >= 2/3 seeds | **FAIL (0/3; all = 9.09%)** | **FAIL (0/3; all = 9.09%)** |
| C3: relative rv divergence >= 3% | >= 2/3 seeds | PASS (10.2% / 16.6% / 10.3%) | PASS (8.4% / 27.6% / 7.9%) |
| overall_pass | C1 AND C2 AND C3 | FAIL | FAIL |

### The C2 structural property

Every seed in every arm in both runs reports
`cluster_live_frac_post_warmup = 0.09090909...` -- literally 1/11. Inspecting
the per-cycle records, the same pattern holds in every cell:

| Episode | mech285_n_draws | sws_anchor_weight_applied |
|---|---|---|
| 1 | 0 | 1.0 |
| **2** | **8** | **0.6** |
| 3-12 | 0 | 1.0 |

The cluster fires exactly once per seed, at episode 2, then is idle for the
remaining 10 cycles. This is deterministic across seeds/arms/runs -- it is the
K=1 single-fire driver's buffer-fill / buffer-drain rhythm, not a stochastic
sampler failure. 11 post-warmup cycles -> 1 live -> 9.09%.

### The MECH-204 dimension passes cleanly

In both runs, ARM_1 (step=0.25) shows clear within-cycle rv divergence in the
first 1-3 episodes (the recalibration is biting the EMA hard while the running
variance is still settling), then stabilises with a small per-cycle delta. The
per-seed relative divergences (8.4-27.6%) far exceed the 541c PASS bar
(step=0.25 cleared 4.51%, step=0.5 cleared 9.03%, at 16 cycles).

**Failed criterion:** C2, a *discrimination* criterion at the integration
(cluster-liveness) layer -- not at the MECH-204 mechanism layer (C1+C3).

---

## Claim layer

| Claim | Type | Status | v3_pending | Autopsy verdict |
|---|---|---|---|---|
| MECH-204 | mechanism_hypothesis | candidate | -- (implementation_phase: v3) | **strengthened** on C1+C3; cluster-integration C2 is not a MECH-204 prediction |

`claim_ids_tested` accuracy: the script tags MECH-204 only, which matches the
C1+C3 criteria but is **overstated** for C2 -- C2 tests MECH-285 sampler +
GAP-3 unified-flag liveness, not MECH-204. This is not a tag-inheritance bug
(no predecessor's tag was carried forward) but a single-tag overload: the same
experiment carries both a MECH-204 prediction (C1+C3) and an integration
prediction (C2) under one claim_ids entry.

**Did the experiment let MECH-204 express itself?** Yes -- 12 cycles is
sufficient under the 541c-validated F1+step=0.25 architecture, and the C1+C3
results confirm.

**Did the experiment let cluster integration express itself?** Partially --
the cluster mechanically fires once (the buffer-fill -> sample -> drain
rhythm), so the C2 question "does the cluster fire on every post-warmup
cycle?" gets answered "no, exactly once" with a deterministic signature. But
that answer is not informative against the MECH-285 substrate; it is
informative against the C2 *threshold*, which was calibrated against an
expectation the K=1 driver pattern cannot satisfy.

---

## Biological-reference triage

MECH-204 closest mammalian referent (dorsal raphe 5-HT quiescence during REM
removing tonic serotonergic inhibition of cumulative recalibration) is already
covered by the
[targeted_review_rem_precision_recalibration_timing](../literature/targeted_review_rem_precision_recalibration_timing/)
lit-pull landed 2026-05-09 (5 entries; F1 dominant pattern, F2 permanently
discarded). 596/602 do not raise a new biology question.

The C2 cluster-liveness question (under K=1 driver, what fraction of REM-onset
moments should MECH-285 SleepReplaySampler draw on?) is *not* a biology
question -- it is a software-design / measurement-calibration question.

**Lit-pull commission required?** No.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** (MECH-204) | C1+C3 PASS in 3/3 seeds at 12-cycle scale, exceeding the 541c canonical bar |
| Biological reference | clear | 5-HT REM zero-point; 541c-era lit-pull already covers |
| Prerequisites | present | GAP-1, GAP-3, GAP-4, GAP-7, GAP-8 all `done`; substrate-ready IGW-20260521-022 |
| Implementation | complete (for MECH-204) | recalibration fires every cycle in both arms; sws_n_writes=5 every cycle |
| Environment | adequate | StepHarness waking path active |
| **Measurement** | **misleading** | C2 threshold (`cluster_live_frac_post_warmup >= 50%`) was registered without calibrating against the K=1 single-fire driver pattern -- structurally cannot exceed 1/(N-warmup) under K=1 |
| **Integration** | **partially coupled** | cluster mechanically fires (sws_n_writes=5 / cycle; MECH-285 draws=8 once at episode 2); K=1 driver does not refill the sampler buffer between cycles by design (see sleep_substrate_plan.md GAP-7 audit) |
| Scale | adequate | 12 cycles solves the 541-family scale gap on the MECH-204 dimension |

**Dominant diagnosis:** measurement_gap (C2 threshold mis-registered against
the documented K=1 driver pattern), with a secondary integration question
that is *not* a substrate gap because GAP-7's experiment audit explicitly
catalogues K=1 single-fire as a valid documented driver pattern.

**Recommended `epistemic_category`:** `standard` (the dominant claim
MECH-204 is V3-tractable and the failure is on a measurement-design
sub-question; not `substrate_ceiling`, not `substrate_conditional`).

---

## Cluster pattern across the MECH-204 lineage

| Experiment | Date | C1 / negative-control | C3 / discrimination | Failed criterion | Diagnosis layer |
|---|---|---|---|---|---|
| EXQ-541 | 2026-05-08 | n/a (within-cycle no-op) | n/a | architectural | superseded |
| EXQ-541a | 2026-05-09 | C1 PASS (3/3); sign=1.0 | 0.56% (vs 5% bar) | C3 scale | **scale** (4-cycle budget; EMA_alpha=0.1 floor) |
| EXQ-541b | 2026-05-09 | C1+C2 PASS arms 1-3 | 0.31% -> 1.75% monotone | C4 scale | **scale** (4-cycle budget; monotone in step but capped) |
| EXQ-541c | 2026-05-09 | PASS | step=0.5: 9.03%; step=0.25: 4.51% | -- | **PASS** at 16 cycles -- MECH-204 mechanism confirmed |
| **EXQ-596** | 2026-05-20 | C1 PASS (3/3); C3 10.2/16.6/10.3% | C2 FAIL (0/3; 9.09%) | C2 measurement | **measurement + integration** (different layer) |
| **EXQ-602** | 2026-05-21 | C1 PASS (3/3); C3 8.4/27.6/7.9% | C2 FAIL (0/3; 9.09%) | C2 measurement | **measurement + integration** (identical signature; rerun) |

### Are 596 and 602 N independent bugs, or one structural property?

**One structural property.** `cluster_live_frac_post_warmup = 1/11`
bit-identically across all 6 seed/arm/run combinations -- 596 + 602 are
exposing the same deterministic property of the K=1 driver's buffer
rhythm. They are *one observation* repeated, not two.

### Are 596/602 and the 541-family the same diagnosis?

**No -- different layers of the four-layer table on the same claim.** The
541-family failed at the **scale** layer (insufficient cycles to surface
MECH-204 against EMA_alpha=0.1 damping). 596/602 failed at the
**measurement** layer (C2 cluster-liveness threshold incompatible with the
documented K=1 driver) and at the **integration** layer (the C2 question
asks something about cluster-wide behaviour that is not a MECH-204
prediction). The two families are not independent bugs -- they sit on the
same closure-handoff trajectory -- but they are not the same diagnosis
re-expressed under different conditions either.

### Load-bearing finding

The convergent shape across the lineage (541 -> 541a/b -> 541c -> 596/602)
is that **MECH-204 itself is well-grounded and well-implemented** -- every
FAIL on this claim's lineage has been on a *test-design layer* (within-cycle
loop bug, scale, measurement) rather than on the mechanism. The 596/602
result strengthens that read: at 12 cycles MECH-204 generates 8-28%
divergence, more than enough to be detected by any reasonable downstream
behavioural probe.

The right next move is not a new substrate -- it is a redesigned integration
EXQ that separates the MECH-204 prediction from the cluster-liveness
prediction.

---

## Learning extracted

1. **MECH-204 is now triply confirmed at the substrate level:** 541c (canonical
   PASS at 16 cycles) + 596 (C1+C3 PASS at 12 cycles, 10-17% divergence) +
   602 (C1+C3 PASS at 12 cycles, 8-28% divergence).
2. **K=1 single-fire driver produces deterministic `cluster_live_frac = 1/N`
   under MECH-285 sampler.** This is a documented driver pattern
   (sleep_substrate_plan.md GAP-7, 41 sleep-touching experiments audited
   2026-05-17), not a bug. The C2 threshold needs to match it.
3. **Single-tag overload is a recurring failure mode for integration EXQs.**
   The 596/602 script tags MECH-204 only, but the failed criterion (C2) is
   really testing MECH-285 + GAP-3 + GAP-7 driver alignment. Future
   integration EXQs should either split into per-claim criteria or carry
   `evidence_direction_per_claim` to keep MECH-204 evidence clean from
   cluster-integration evidence.
4. **Closure-handoff EXQs need their own design template.** The
   "combine N substrate components in one EXQ" pattern is valuable for
   regression-style validation but is prone to mis-calibrated discrimination
   thresholds when the K-driver pattern interacts with the criterion's
   denominator. A short checklist (criterion-by-criterion: which claim does
   this predict, and what driver pattern do we expect to satisfy it?) would
   catch C2-style mismatches at script-write time.

---

## Repair pathway

**Routing: R1 -- /queue-experiment redesign + governance reclassify.**

| Action | Owner skill | Notes |
|---|---|---|
| Queue successor EXQ (596a or 596b) with redesigned C2 | `/queue-experiment` | Two viable shapes: (a) replace C2 with a per-arm cluster-effect-on-rv comparison that the current data already supports, or (b) run under K>=2 multi-fire driver so the MECH-285 sampler has cross-cycle buffer to draw from. (a) is the smaller change; (b) is the cleaner closure-handoff if the team wants sustained cluster liveness. Suggest (a) first with (b) as a deferred sibling. |
| Reclassify EXQ-596 + EXQ-602 manifests | `/governance` | `evidence_direction: non_contributory -> inconclusive_measurement`; append `evidence_direction_note` per the draft below. |
| Append MECH-204 `evidence_quality_note` | `/governance` | Draft text below. |
| No `substrate_queue.json` change | -- | GAP-1/3/4/7/8 already `done` in plan-of-record; no new substrate gap surfaced. |
| No `sleep_substrate_plan.md` status table change | -- | All gaps relevant to this autopsy are `done`; the C2 redesign is a test-design improvement, not a plan-of-record amendment. |

### Draft `evidence_quality_note` for MECH-204 (governance applies)

> V3-EXQ-596 (2026-05-20) + V3-EXQ-602 (2026-05-21) closure-handoff integration
> at 12 cycles, step=0.25: MECH-204 recalibration fires every cycle in 3/3
> seeds (C1 PASS); arm relative rv divergence 8.4-27.6% per seed clears the 3%
> C3 threshold and exceeds the 541c canonical PASS bar (4.5-9% at 16 cycles).
> Overall FAIL driven by C2 `cluster_live_frac_post_warmup >= 50%` (0/3 seeds;
> deterministic 1/11 = 9.09% across all 6 seed/arm/run combinations because
> MECH-285 sampler under K=1 single-fire driver draws once at the buffer-fill
> cycle, then idle). C2 is a cluster-integration criterion (MECH-285 / GAP-3),
> not a MECH-204 prediction; 596/602 strengthen MECH-204. Reclassify both
> manifests `non_contributory -> inconclusive_measurement`. Successor EXQ
> redesigning C2 against the documented K=1 driver pattern (sleep_substrate_plan.md
> GAP-7) tracked under /queue-experiment. See failure_autopsy_V3-EXQ-596-602_MECH204_2026-05-29.md.

### Draft `evidence_direction_note` for the two manifests (governance applies)

> Reclassified by failure autopsy 2026-05-29: C2 `cluster_live_frac_post_warmup
> >= 50%` is a cluster-integration criterion incompatible with the K=1
> single-fire driver pattern documented in sleep_substrate_plan.md GAP-7 --
> the MECH-285 sampler draws once per buffer-fill, yielding a deterministic
> 1/11 = 9.09% across all 6 seed/arm/run combinations. C1 + C3 confirm
> MECH-204 mechanism (8-28% rv divergence, exceeding the 541c PASS bar).
> Not a MECH-204 falsification; not a substrate gap. Successor EXQ pending.

---

## Confirmed routing

- **EXQ-596 + EXQ-602:** reclassify `non_contributory -> inconclusive_measurement` in governance; append `evidence_quality_note` to MECH-204; no substrate_queue change; no sleep_substrate_plan.md status table change.
- **Successor EXQ:** /queue-experiment will write a redesigned C2 (either per-arm rv-effect comparison OR K>=2 multi-fire driver) tagged MECH-204 + MECH-285. Suggest the per-arm rv-effect framing first; the K>=2 driver variant is a deferred sibling.
- **No lit-pull, no /implement-substrate, no claim-splitting, no governance demotion.**
