# Pending Experiment Review

Generated: `2026-08-16T18:56:00Z`  
Last review: `2026-08-16T11:25:59Z`  
Pending: **14** item(s) -- 9 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication; 2 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_931_cem_wanting_weight_selection_authority_20260814T123949Z_v3` | 2026-08-14T12:39 | (no claim tags) | — |
| `v3_exq_436f_sd017_mech166_sd016_armed_retest_20260814T194313Z_v3` | 2026-08-14T19:43 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_861c_inv050_mech180_calibration_fixed_replication_20260814T231404Z_v3` | 2026-08-14T23:14 | INV-050, MECH-180 | — |
| `v3_exq_861d_mech180_mech122_spindle_content_selection_dv3_revalidation_20260815T005853Z_v3` | 2026-08-15T00:58 | MECH-122, MECH-180 | — |
| `v3_exq_603u_instrumental_avoidance_agent_pursuit_20260815T020607Z_v3` | 2026-08-15T02:06 | MECH-357 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_927_mech267_cem_selection_fix_validation_20260814T012404Z_v3` | 2026-08-14T01:24 | MECH-267 |
| `v3_exq_928_mech267_cem_selection_fix_validation_20260814T013434Z_v3` | 2026-08-14T01:34 | MECH-267 |
| `v3_exq_929_sleep_gap9_within_life_trigger_20260814T081606Z_v3` | 2026-08-14T08:16 | (no claim tags) |
| `v3_exq_930_mech303_dedicated_proximity_signal_validation_20260814T092437Z_v3` | 2026-08-14T09:24 | MECH-303 |
| `v3_exq_932_zgoal_wanting_coupling_reinstrument_20260814T155424Z_v3` | 2026-08-14T15:54 | (no claim tags) |
| `v3_exq_933_sleep_gap9_need_arm_20260814T155845Z_v3` | 2026-08-14T15:58 | (no claim tags) |
| `v3_exq_922a_sd016_mech152_softsel_ablation_20260814T183708Z_v3` | 2026-08-14T18:37 | MECH-152 |
| `v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3` | 2026-08-14T22:34 | (no claim tags) |
| `v3_exq_934_mech266_cap_sweep_mode_occupancy_20260815T015216Z_v3` | 2026-08-15T01:52 | MECH-266, SD-032a |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_927_mech267_cem_selection_fix_validation_20260814T012404Z_v3` | PASS | fix_effective::H3+BOTH | **vacuous_pass** |
| `v3_exq_928_mech267_cem_selection_fix_validation_20260814T013434Z_v3` | PASS | fix_effective::H3+BOTH | **vacuous_pass** |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_861c_inv050_mech180_calibration_fixed_replication_20260814T231404Z_v3` | FAIL | 57863 | **0** | 0.000 | live |
| `v3_exq_861d_mech180_mech122_spindle_content_selection_dv3_revalidation_20260815T005853Z_v3` | FAIL | 38346 | **0** | 0.000 | live |

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
