# Failure autopsy -- V3-EXQ-861e (INV-050 / MECH-180 calibration-power-raised replication)

**Generated:** 2026-08-21T01:36:54Z
**Scope:** single (re-adjudication of the 861/MECH-180 lineage)
**Status:** `confirmed` 2026-08-21T01:56:34Z. Step 8 adopted the Step 7c
CONTESTED portfolio: H1 vs H3 required; H2 follow-on only; drop "like seed 7";
four-layer measurement `partial`. Destination `/queue-experiment` unchanged.
Step 9b applied at confirmation: new qid
`inv050_mech180_861e_producer_vs_intervention_isolation` (H1+H3 frozen set).

**Companion:** `failure_autopsy_V3-EXQ-861e_2026-08-21.json`

**Session:** `failure-autopsy-batch-20260821`

This run is the calibration-power-raised replication the confirmed
`failure_autopsy_861c-861d-mech180-cluster_2026-08-16` commissioned
(CALIB_DRAWS 5->10 + new R3). Queue still shows `claimed` on ree-cloud-1;
IGNORE that -- the manifest landed, `elapsed_seconds` ~36980, run completed.
Autopsy applies.

`targets[]` covers ONLY
`v3_exq_861e_inv050_mech180_calibration_power_raised_replication_20260820T214522Z_v3`.
861d / MECH-122 / SD-017 are read-across, not retargeted.

---

## 0. Gates run before any metric was read

| Gate | Result |
|---|---|
| Already-done check | Parent handed a single uncovered target. This artifact is the first covering 861e. |
| `check_dry_run_citations.py` | **0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown**. Stamp `dry_run_checked: true`, `excluded_dry_run_ids: []`. |
| `validate_recording.py --paths <manifest>` | **1 complete, 0 always-core gaps.** |
| `validate_experiments.py --checks dry_run_unreachable_criterion` | Corpus fires are all `v3_exq_543*`. This driver silent. Parent: dry-run gate already PASSED. |
| Re-derive brake | Does **not** fire. Recommends `standard`, not `substrate_ceiling`. See Section 8. |
| Granularity-debt trigger | Does **not** fire. See Section 9. |

Ran to completion (`outcome: FAIL`, no traceback). Not a `/diagnose-errors` target.

---

## 1. Facts

`v3_exq_861e_inv050_mech180_calibration_power_raised_replication_20260820T214522Z_v3`
FAIL | `experiment_purpose: evidence` | `claim_ids: [INV-050, MECH-180]` |
`ree-worker-1`, `linux-x86_64-py3.10-torch2.12.0+cpu` | 36980.465 s |
seeds `[7, 271, 883]` (disjoint from original `{42,123,456}`; reused from 861b/861c) |
`substrate_hash d1f4bdaeda6e...` | `substrate_commit 17befb8c46` dirty false, branch main |
`evidence_direction: non_contributory` (per-claim same) |
self-route `mel_coupling_below_calibration_noise_floor` |
`compares_against_run_id`: 861c calibration-fixed replication.

Driver: `ree-v3/experiments/v3_exq_861e_inv050_mech180_calibration_power_raised_replication.py`.
`use_mech122_spindle_content_selection` OFF (861c/861b value). DV3 recorded, not scored;
blocking sd_id `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`.

**Design.** Calibration-power-raised replication of 861c: identical env, arms,
seeds, C1 readout, agent config, and C2 formula. The ONLY intended changes are
CALIB_DRAWS 5->10 and the new R3 calibration-precision readiness precondition.
C1 thresholds were deliberately not re-tuned. Pre-registered target CONFIRMED
outcome: **2/3 C2 pass with seed 7 the lone miss**.

Full cell dump and predecessor excerpts: `_scratch/autopsy-batch-20260821/861e/facts.md`.

### Headline (recomputed from `per_seed` / `arm_results`)

| Metric | Value |
|---|---|
| readiness_ok | True |
| r1_frac | 1.0 |
| r2_frac | 0.666... (exactly the 2/3 floor; seed 271 fails R2) |
| r3_frac | 1.0 (new; all three seeds) |
| c1_all_pass | True |
| c1_frac | 0.666... |
| c2_pass | False |
| c2_frac | 0.333... |
| c2_pinned_frac | 0.666... |
| c2_factor_clears_noise_frac | 0.333... |
| per_dv_pass | sws_power True, spindle_density False (0.0, UNSCORED), replay_rate True |

C2 fraction uses all 3 seeds as denominator; a skipped (not-ready) seed counts
as a C2 miss. Combination rule still fails on C2 1/3.

R3 ARM_3 `calib_rel_sd_of_mean`: 0.0705 / 0.0533 / 0.0785 -- inside the 861c
n=10 projection band [0.048, 0.090]. **The commissioned instrument repair
worked.** Calibration scatter is not why this run missed 2/3 C2.

### Per-seed vs 861c

**Seed 7 (pre-registered producer miss -- still fails C2, as designed).**
861c: ready; C2 FAIL; on_factor 0.8366 vs margin 1.253; HIGH MEL 3.04e-5 below
no-shift NONE 3.88e-5 and below ref 3.64e-5. 861e: ready (R1/R2/R3 all true);
C2 FAIL; on_factor 1.017 vs margin 1.141; HIGH MEL 2.982e-5 vs ref 2.932e-5
(now slightly above ref, still below the noise floor). C1 order by measured MEL:
HIGH < LOW < NONE < MED -- HIGH is the **lowest** measured MEL. C1 scored_all
True (monotone in measured MEL; tautological consumer arithmetic). Reported-only
sws/rem flags can be true (31>30, 61>60) while C2 fails because factor < margin.
Calibration moved the denominator so factor crossed 1.0; it did not create a
HIGH-above-base producer.

**Seed 271 (the projection seed -- this is the surprise).**
861c: ready; R2 pass (spread 1.414); C1 order NONE < LOW < MED < HIGH; C2 FAIL
by 0.5% (factor 1.215 vs margin 1.220). Cluster projected n=10 margin 1.156 ->
PASS. 861e: **ready=False**; r2_ok False; r3_ok True (0.0533, well under 0.15);
C1/C2 skipped. HIGH MEL collapsed 2.90e-5 -> 2.30e-5, **below** ref 2.60e-5;
factor 0.884. R2 spread 1.148 vs 1.15 (fail by ~0.16 pp). Arm order scrambled:
LOW < HIGH < NONE < MED. HIGH arm `n_cycles_insufficient_touched_slots` 6/6
(861c was 4). If C2 had been scored: 0.884 vs margin ~1.107 -> still FAIL, as
**producer**, not calibration.

**Seed 883 (still the clean C2 pass).**
861c: C2 PASS; factor 1.885 vs 1.136. 861e: C2 PASS; factor 1.975 vs margin
1.157. C1 scored_all True. C1 MEL order is NOT novelty-ordered (NONE lowest,
MED highest, HIGH in the middle) -- C1 sorts by measured MEL.

### z_goal_stream -- non-gating

`ticks_total` 44908, `writer_calls` 0, `writer_defect` true, `active_frac` 0.0,
`goal_state_present` true. Lineage-wide (861/861a/861b/861c/861d + this).
Driver `DEAD_Z_GOAL_STREAM_EXEMPT`: wiring `update_z_goal` would activate the
E3 goal term / E1 conditioning / SD-024 and break the single-variable comparison
vs 861c. Scored DVs (`cumulative_sws_writes`, `cumulative_rem_rollouts`,
measured MEL) **do not read z_goal**. MEL derives from
`e3.post_action_update(actual_z_world=...)` -> `prediction_error`. A result that
does not read z_goal is unaffected. Recorded as a lineage-wide driver defect
still open, **not** as the C2 cause. Not measurement/recording debt on the
INV-050/MECH-180 criteria.

### substrate_stable_across_run: False -- reuse-safety, not mid-run confound

`per_cell_hashes_disagree: false` -- all 15 cells share hash `d1f4bdae...`.
`process_snapshot_drift` records that hash vs `on_disk_now` `40dc7e73...` at
stamp. `lag_seconds` 35827 (~10h); `drifted_since_resolved` true;
`commit_describes_recorded_hash` false. This run's own grid is internally
consistent; arm_reuse should refuse these cells as a baseline. Same pattern
798a already adjudicated.

Separate from that flag: 861c vs 861e executed **different** substrates
(f810969 / hash 5eaa59f5... / ree-cloud-4 / 3.5h / stable true vs 17befb8c /
hash d1f4bdae... / ree-worker-1 / 10.3h / stable false). Live H3, not the
within-run flag.

---

## 2. Re-adjudication of the commissioning read

**Yes: C2 1/3 vs the pre-registered 2/3 target changes the 861c commissioning
read.** It does not change the stored category or direction.

The confirmed cluster autopsy (`failure_autopsy_861c-861d-mech180-cluster_2026-08-16`)
read 861c C2 1/3 as **mixed**: seed 7 genuine link-(i) producer failure; seed 271
**pure calibration under-power** (0.5%); n=10 **flips C2 to 2/3 PASS**; not a
substrate ceiling; `standard`; brake `fired: false`; route `/queue-experiment`
861e.

861e refutes the projection's **premise**, not merely leaves it untested:

1. R3 passed -- the n=10 instrument is adequate.
2. Seed 271's **numerator** (HIGH-arm MEL / duration factor) was not a stable
   ~1.215; it collapsed to 0.884 and HIGH went from graded-max to below-reference.
3. Even counterfactually scoring C2 on 271 would fail as producer (factor
   0.884 vs margin ~1.107). Do **not** call this "like seed 7": 861c already
   had seed 271 HIGH-graded at n=5 (2.900e-5 above its own reference); seed 7
   was already below-ref then. The 861e collapse is a numerator move, not the
   seed-7 producer signature.
4. The driver claim that "same seeds isolate the calibration change" is false
   as a ceteris-paribus premise: extra calib draws consume torch RNG via
   `select_action` before measurement, and measurement does not reseed. Calib
   is `train=False` (E2 frozen), so extra draws are not extra world-model
   training -- but they are extra policy-RNG and extra frozen-wake steps.

Self-route `mel_coupling_below_calibration_noise_floor` is **wrong for this
run's cause**. The combination rule still fails on C2 1/3 because seed 271
never reached C2 and seed 7 failed as pre-registered. Do not rubber-stamp it.

**Counting convention, shape (c):** direction + category **retained**
(`non_contributory` / `standard`); supporting reasoning **withdrawn**. Stamp
`re_derive_brake.supersedes_autopsy` to
`failure_autopsy_861c-861d-mech180-cluster_2026-08-16`. Count unchanged. Brake
does not fire.

### Withdrawn arguments (recorded, not deleted)

- "n=10 flips seed 271 C2"
- "this FAIL is still calibration under-power"
- rubber-stamp of self-route `mel_coupling_below_calibration_noise_floor` as the cause
- casual `substrate_ceiling` restamp (considered and rejected; R3 only counts
  ceiling; 2/3 seeds still R2-ready; 883 C2 strong; 718a already named the
  producer/environment gap; 798a/861 already graduated both claims
  ceiling->standard)
- "same seeds isolate CALIB_DRAWS"

### What this does NOT move (`read_across_not_adjudicated`)

- **861d / MECH-122.** Cluster sibling. This run keeps the MECH-122 flag OFF
  and does not re-test the clamp gate. Do not amend or fork
  `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`.
- **SD-017 occupancy.** INV-050 `emergent_from: [SD-017]`. Keeping INV-050
  candidate / standard / pending_retest does not mechanically move SD-017
  (stable / substrate_ceiling / pending_retest on SD-016).
- Residual 861c repair item 4 (z_goal writer) still open, still non-gating.
- 798a's "STAY until the ecological run scores" is **already discharged** on
  the live claims (861/845 scored; both stored `standard`). Do not re-open it.

---

## 3. Failed criterion

Still C2 numerically (`absolute` / `C2_on_factor_clears_calibration_noise_floor`),
with the seed that was supposed to supply the second pass gated out at R2.
The **cause** of that C2 miss is no longer 861c's calibration under-power.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Claim not fairly tested on the independence leg. C2 uninterpretable on 271 (gated at R2); seed 7 pre-registered miss; seed 883 C2 strong; C1 tautological on ready seeds (monotone in measured MEL). |
| Biological reference | clear | process-S / novelty-adaptive SWS+replay; lit present (Wilson & McNaughton 1994, Tononi & Cirelli 2003, Stickgold 2001; INV-050 notes cite lit_conf historically). No new `/lit-pull`. |
| Prerequisites | present | R1 1.0; R2 at floor 2/3; R3 1.0 (SEM repaired). R3 cannot see H1. |
| Implementation | complete at consumer | Duration tracks measured MEL on ready seeds. Deterministic `duration_factor = f(measured_mel / mel_reference)`. |
| Environment | **partial** | Producer unstable on disjoint seeds 7 (always) and 271 (this replication); 883 works. |
| Measurement | **partial** | SEM repaired (R3 1.0); that refutes "this FAIL is still calibration under-power." R3 is computed only from calib draws and cannot discriminate H1 (unreseeded measurement-phase RNG). Step 7c CONTESTED: do not stamp "instrument adequate" as a blanket against H1. |
| Integration | coupled | On ready seeds the consumer arithmetic integrates with the sleep-loop scheduler. |
| Scale | adequate | n=10 draws met the pre-registered precision bar on 3/3 seeds. |

**Failure-location (GOV-FAILLOC-1):**

- mechanism: `not_established` (consumer still works where MEL grades)
- measures: `not_established` -- instrument repaired; leftover is
  intervention-isolation of the power raise, not 861c's SEM problem. Do not
  charge this run to the 861c-style "calibration scatter = effect size" bucket.
- environment: `partial` (established on 271+7 producer; not on 883)
- ree: false
- net: **MIXED, ENVIRONMENT more prominent than 861c's MEASURES-dominant read
  -- not chargeable to REE**

Demotion gate is not met: the independence leg was not fairly tested (271
never scored C2; 7 was pre-registered not to).

---

## 5. Biological-reference triage

Closest mechanism: homeostatic sleep-pressure regulation scaling SWS
depth/duration with prior waking learning load (process-S analog), plus
novelty-triggered hippocampal replay during SWS (Wilson & McNaughton 1994).
Not a formal-definition import. No load-bearing divergence. `lit_status:
present`. No new `/lit-pull`.

---

## 6. Current claim state (read, not edited)

**INV-050:** status `candidate`, `epistemic_category: standard`,
`pending_retest_after_substrate: true`, `ceiling_decision: deferred` (RESOLVED
2026-08-01 ceiling->standard). `live_status.evidence.from` =
`failure_autopsy_V3-EXQ-861_2026-08-01`.

**MECH-180:** status `candidate`, `v3_pending: true`, `epistemic_category:
standard`, `pending_retest_after_substrate: true`. Same `from` stamp. 798a's
"STAY until ecological run scores" is already discharged. DV3 still descoped.

GFLAG-0002 (INV-050 independent-seed hold): still **unresolved**, not failed.
C1 still replicates on ready seeds; decisive C2 still 1/3.

Change strings must **not** end on `-> standard` (already true on both; would
false-clear GOV-APPLY-1). Note-only apply; end on this artifact slug so the
row stays ACTIONABLE until provenance is stamped.

---

## 7. Recommended disposition

Both claims: `recommended_evidence_direction: non_contributory`,
`recommended_epistemic_category: standard`. Status unchanged (`candidate`).
MECH-180 `v3_pending` stays. `pending_retest_after_substrate` stays true as
the standing retest intent (GFLAG-0002 / producer isolation), **not** a new
substrate-queue entry.

Do **not** restamp `substrate_ceiling`. Official R1-R3 substring recipe (as
the cluster used): INV-050 = 3, MECH-180 = 2 confirmed hits. Exact enum
`== substrate_ceiling`: INV-050 = 0, MECH-180 = 1 (677). If this autopsy
stamped ceiling, official recipe would fire the brake on both (4 and 3);
exact enum would fire it on MECH-180 (2). Either way, ceiling would forbid
the H1/H3 isolation the data now need. Recommend `standard`; counts do not
advance; brake `fired: false`.

`recommended_substrate_queue_entry.action: none`. Already-unblocking entries
named so they are not treated as a silent create-collision: **SD-MEL-CONSUMER**
(consumer BANKED) and **SD-MEL-PRODUCER** (test-bed already licensed 845/861).
Neither is the residual gap. 861d's MECH122 entry is a different mechanism
(flag OFF here). Do not fork it.

**Routing:** `/queue-experiment`. Node: `complex (probe-gated) / puzzle
(known rules)` with a live H1 vs H3 discrimination -- emit
`fanout_recommendation`. H2 is a follow-on after those two, not an
identifying first-portfolio axis. Do not bump CALIB_DRAWS again.

### Fan-out (GOV-FANOUT-1)

Step 7c CONTESTED; Step 8 adopted this portfolio. Cheap confirmer: 861c ARM_3
seed 271 HIGH `mean_mel=2.8999705256751363e-05` (above ref, R2 pass) vs 861e
same cell `2.2980323189226863e-05` (below ref). H2 at n=5 on 861e's substrate
is aliased with H3. Seed 271 is not "like seed 7."

| H | Axis | Sketch | Null |
|---|---|---|---|
| H1 (required) | measurement | Keep CALIB_DRAWS=10. Reseed torch/numpy immediately before the measurement loop so extra calib draws cannot consume measurement-phase RNG. Same substrate `17befb8c`. | If seed 271's HIGH-graded MEL **returns** under a reseeded n=10, the 861e collapse was an intervention-isolation defect, not a producer failure. |
| H3 (required) | algorithm | Pin 861c substrate (`f810969`) and rerun the 861e protocol (n=10 + R3) on the same box class if possible. | If 271 stays HIGH-graded on the old substrate at n=10, the collapse is a substrate/machine delta, not H1. |
| H2 (follow-on only; do not run in the first portfolio) | environment | Repeat seed 271 at CALIB_DRAWS=5 on **861e's substrate** (`17befb8c`) **after** H1 and H3 have run. | Not identifying until H3 has run: a collapse at n=5 on 17befb8c is H2-or-H3. If H3 has already shown 271 still HIGH-graded on f810969, then a collapse here isolates producer-on-this-substrate. |

Never a power-bump of the braked (here: just-refuted) calibration design.

---

## 8. Re-derive brake

`fired: false`. `threshold: 2`. `supersedes_autopsy:
failure_autopsy_861c-861d-mech180-cluster_2026-08-16`. `refused_requeue: false`.
`route_to: queue-experiment`.

This autopsy recommends `standard`, not `substrate_ceiling`, so neither claim's
R1-R3 count advances. The cluster listed prior hits MECH-180=2, INV-050=3 under
the substring recipe; this run does not add a fourth/third.

---

## 9. Granularity-debt

`granularity_debt_cluster.py` before this artifact:

- INV-050: 8 targets, intact=4, unclear=4. **No `weakened`.**
- MECH-180: 9 targets, unclear=4, intact=2, strengthened=2, other=1
  (861a's "weakened-but-explained" is DV3 / MECH-122 content-packaging, not
  DV1/DV2). **No target reads `weakened`.**

This target stamps `claim_alignment: unclear` (not fairly tested). Trigger
does **not** fire. Measurement/environment debt, not granularity debt.

---

## 10. Step 9b (applied at confirmation)

No existing registry question covers INV-050 / MECH-180 (search hit none;
nearest `sd017_arc045_mech166_slot_differentiation_sleep` tags a different
claim set). Fan-out is a **new** `qid`. Growth-restriction check: n/a (new
question cannot carry a restriction). Mode A. Applied 2026-08-21T01:56:34Z.

qid: `inv050_mech180_861e_producer_vs_intervention_isolation`. Initial frozen
set is H1 + H3 (count 2). H2 is a labelled follow-on, not in the frozen
denominator, because its n=5-on-861e-substrate sketch is aliased with H3.

---

## 11. Learning extracted

- A confirmed n=10 projection can be refuted by the numerator moving, not
  just by the denominator staying noisy. R3 passing is what makes that
  visible: the instrument was adequate and C2 still missed 2/3.
- "Same seeds isolate the calibration change" is false when extra calib
  draws consume policy RNG before an unreseeded measurement loop, even if
  E2 is frozen (`train=False`).
- Seed 7's producer miss is now replicated at n=10 (factor crossed 1.0 but
  HIGH remained the lowest measured MEL). Seed 271 did **not** join that
  signature: 861c already had 271 HIGH-graded at n=5; 861e dropped HIGH MEL
  below its own reference. That is a numerator move (H1 or H3), not seed-7's
  standing producer miss.
- Self-route `mel_coupling_below_calibration_noise_floor` is a combination-
  rule leftover: the grid still maps C2-below-noise to that label even when
  a seed never reached C2.
- Dead z_goal (`writer_calls` 0, `writer_defect` true) remains lineage-wide
  and non-gating for INV-050/MECH-180 criteria.
- `substrate_stable_across_run: False` here is 798a's reuse-safety pattern
  (one cell hash, process-snapshot drift vs on-disk-now), not a mid-run
  code change.
- Do not restamp ceiling: it would fire the brake and forbid the isolation
  the data now require.

**Explicitly not recommended:** another CALIB_DRAWS bump; amending or forking
`MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION` off this run; restamping
`substrate_ceiling`; treating z_goal writer_defect as the C2 cause; moving
SD-017 off INV-050 occupancy; rubber-stamping the self-route.

**Chip policy:** parent instructed no chips. Per the 2026-07-30 rule a
`/failure-autopsy` session does not spawn_task its own routing follow-on.
Nothing spawned.

---

## 12. Step 7b (pre-routing checks)

`scripts/autopsy_pre_routing_checks.py --artifact <this> --json`

First pass: **C2 fired** (`action=none` while `SD-MEL-CONSUMER` and
`SD-MEL-PRODUCER` already unblock these claims and were unmentioned).
Disposed by naming both sd_ids: they are the already-built/validated
producer and consumer; this FAIL is not a missing-bed result; `action=none`
stays. Final pass: `fire_count` 0. C1, C3, C5, C6-narrow, C7 quiet and
applicable. Step 7c skipped (parent will red-team).
