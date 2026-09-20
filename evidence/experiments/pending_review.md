# Pending Experiment Review

Generated: `2026-09-20T11:54:35Z`  
Last review: `2026-09-18T19:03:46Z`  
Pending: **10** item(s) -- 4 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 5 diagnostic self-route(s) flagged for adjudication; 1 run(s) with a DEAD z_goal stream; 2 evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1057_mech017_reality_consolidation_replay_additive_budget_20260918T211119Z_v3` | 2026-09-18T21:11 | MECH-017 | — |
| `v3_exq_1057a_mech017_reality_consolidation_replay_additive_budget_pass_order_20260918T234946Z_v3` | 2026-09-18T23:49 | MECH-017 | — |
| `v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated_20260919T022652Z_v3` | 2026-09-19T02:26 | INV-086, MECH-428 | — |
| `v3_exq_1043a_mech537_communication_subspace_permutation_null_20260919T030056Z_v3` | 2026-09-19T03:00 | MECH-537 | — |
| `v3_exq_1065_sd106_subspace_overlap_mech566_recondition_20260919T223401Z_v3` | 2026-09-19T22:34 | MECH-566, SD-106 | — |
| `v3_exq_1070_arc029_env_operating_point_feasibility_20260920T042654Z_v3` | 2026-09-20T04:26 | ARC-029 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1058_sd071_consolidation_readout_instrument_validity_20260918T213443Z_v3` | 2026-09-18T21:34 | SD-071 |
| `v3_exq_1060_inv063_e2_world_forward_sleep_trainer_20260919T012511Z_v3` | 2026-09-19T01:25 | MECH-423 |
| `v3_exq_1063_inv063_legb_dv_direction_20260919T102929Z_v3` | 2026-09-19T10:29 | INV-063 |
| `v3_exq_1069_inv063_p1_gate_798a_p0_20260920T082003Z_v3` | 2026-09-20T08:20 | INV-063 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated_20260919T022652Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_1043a_mech537_communication_subspace_permutation_null_20260919T030056Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_1063_inv063_legb_dv_direction_20260919T102929Z_v3` | PASS | legb_dv_converged_base_infonce_positive_mse_not | **vacuous_pass** |
| `v3_exq_1070_arc029_env_operating_point_feasibility_20260920T042654Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_1069_inv063_p1_gate_798a_p0_20260920T082003Z_v3` | PASS | inv063_p1_intake_ladder_gradeable | **precondition_unmet** |

## Evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

These `experiment_purpose: "evidence"` results carry a manifest-level `non_degenerate: false` (or a `false` entry in `non_degenerate_per_claim`) -- the driver's own pre-registered non-degeneracy check on its load-bearing criterion failed. The indexer already excludes them from scoring (`scoring_excluded: "degenerate"`), but nothing else routes them for review: `_compute_adjudication` only fires for `experiment_purpose` in {diagnostic, baseline}, so an evidence-purpose degenerate PASS/FAIL sails into the plain PASS/FAIL table above with no flag (confirmed: V3-EXQ-1007). **Route to `/failure-autopsy` (it accepts a PASS target too); do not verify-and-close.**

| Run ID | Status | Claims | Degeneracy reason |
|--------|--------|--------|--------------------|
| `v3_exq_1057_mech017_reality_consolidation_replay_additive_budget_20260918T211119Z_v3` | FAIL | MECH-017 | substrate_not_ready: unmet preconditions: additive_arm_retains_replay_gain |
| `v3_exq_1057a_mech017_reality_consolidation_replay_additive_budget_pass_order_20260918T234946Z_v3` | FAIL | MECH-017 | substrate_not_ready: unmet preconditions: additive_arm_retains_recency_benefit_d2 |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_1069_inv063_p1_gate_798a_p0_20260920T082003Z_v3` | PASS | 16800 | **0** | 0.000 | live |

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
