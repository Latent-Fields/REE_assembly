# Pending Experiment Review

Generated: `2026-08-12T06:09:04Z`  
Last review: `2026-08-10T15:20:50Z`  
Pending: **17** item(s) -- 6 PASS, 11 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 2 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_912_uncensored_survival_fishtank_20260810T190239Z_v3` | 2026-08-10T19:02 | (no claim tags) | — |
| `v3_exq_894c_mech074d_bla_entropy_weight_sweep_20260810T212602Z_v3` | 2026-08-10T21:26 | MECH-074d | — |
| `v3_exq_910a_mech489_defensive_orienting_decision_retest_20260810T213616Z_v3` | 2026-08-10T21:36 | MECH-489 | — |
| `v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T055126Z_v3` | 2026-08-11T05:51 | MECH-236 | — |
| `v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T065911Z_v3` | 2026-08-11T06:59 | MECH-236 | — |
| `v3_exq_603t_instrumental_avoidance_scheduled_external_hazard_20260811T173724Z_v3` | 2026-08-11T17:37 | MECH-357 | — |
| `v3_exq_920_uncensored_survival_single_life_fishtank_20260811T210906Z_v3` | 2026-08-11T21:09 | (no claim tags) | — |
| `v3_exq_919_mech321_harm_aware_selection_unconditional_wholeepisode_20260811T225107Z_v3` | 2026-08-11T22:51 | MECH-321 | — |
| `v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3` | 2026-08-11T23:42 | ARC-032 | — |
| `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3` | 2026-08-12T03:51 | ARC-041, MECH-150, MECH-151, MECH-152 | — |
| `v3_exq_923_mech267_gov_fanout1_h1_iteration_count_20260812T045513Z_v3` | 2026-08-12T04:55 | MECH-267 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_913_developmental_ecology_fishtank_20260810T213204Z_v3` | 2026-08-10T21:32 | (no claim tags) |
| `v3_exq_916_relief_safety_fishtank_showcase_20260811T064913Z_v3` | 2026-08-11T06:49 | (no claim tags) |
| `v3_exq_916a_relief_safety_fishtank_showcase_20260811T194142Z_v3` | 2026-08-11T19:41 | (no claim tags) |
| `v3_exq_917_mech303_harm_threshold_calibration_battery_20260811T205119Z_v3` | 2026-08-11T20:51 | SD-011 |
| `v3_exq_918a_sd_residue_valence_bound_validation_20260812T044049Z_v3` | 2026-08-12T04:40 | (no claim tags) |
| `v3_exq_924_e3_score_variance_decomp_scorer_fix_remeasure_20260812T051115Z_v3` | 2026-08-12T05:11 | (no claim tags) |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_923_mech267_gov_fanout1_h1_iteration_count_20260812T045513Z_v3` | FAIL | h1_refuted_gaps_at_iters2_as_flat_as_iters3 |
| `v3_exq_924_e3_score_variance_decomp_scorer_fix_remeasure_20260812T051115Z_v3` | PASS | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
