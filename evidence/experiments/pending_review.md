# Pending Experiment Review

Generated: `2026-09-14T23:45:13Z`  
Last review: `2026-09-11T16:55:00Z`  
Pending: **12** item(s) -- 8 PASS, 4 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication; 8 diagnostic run(s) with no confirmed autopsy; 1 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_964a_mech482_epistemic_deficit_multitarget_readiness_20260911T174949Z_v3` | 2026-09-11T17:49 | MECH-482 | — |
| `v3_exq_1023_sd106_bottleneck_preservation_validation_20260912T045319Z_v3` | 2026-09-12T04:53 | SD-106 | — |
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | 2026-09-14T12:56 | INV-086, MECH-428 | — |
| `v3_exq_1027_sd082_replay_own_rule_state_credit_assignment_20260914T135320Z_v3` | 2026-09-14T13:53 | SD-082 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1025_mech349_crf_churn_retirement_20260911T181100Z_v3` | 2026-09-11T18:11 | MECH-349 |
| `v3_exq_1026_mech423_sleep_integrated_e2_consolidation_20260914T111100Z_v3` | 2026-09-14T11:11 | MECH-423 |
| `v3_exq_861i_inv050_mech091_commit_attribution_pinned_confirmation_20260914T121029Z_v3` | 2026-09-14T12:10 | INV-050, MECH-180 |
| `v3_exq_1029_sd082_selection_authority_readout_consequence_20260914T191118Z_v3` | 2026-09-14T19:11 | SD-082 |
| `v3_exq_1037_sd075_phasic_ema_episode_continuity_validation_20260914T195118Z_v3` | 2026-09-14T19:51 | SD-075 |
| `v3_exq_1038_arc131_coalition_endogenous_recruitment_rate_probe_20260914T201122Z_v3` | 2026-09-14T20:11 | ARC-131 |
| `v3_exq_1012a_e3_commensurability_selection_level_regime_validation_20260914T221427Z_v3` | 2026-09-14T22:14 | MECH-439 |
| `v3_exq_1028_sd082_learning_signal_extended_budget_20260914T223157Z_v3` | 2026-09-14T22:31 | SD-082 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_964a_mech482_epistemic_deficit_multitarget_readiness_20260911T174949Z_v3` | FAIL | readout_differentiates_but_never_changes_committed_action |
| `v3_exq_1023_sd106_bottleneck_preservation_validation_20260912T045319Z_v3` | FAIL | sd106_below_pca32_parity |
| `v3_exq_1026_mech423_sleep_integrated_e2_consolidation_20260914T111100Z_v3` | PASS | sleep_integrated_e2_consolidation_confirmed |
| `v3_exq_861i_inv050_mech091_commit_attribution_pinned_confirmation_20260914T121029Z_v3` | PASS | mover_6293b23_confirmed_full_protocol_reproduces_recorded |
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | FAIL | substrate_not_ready_requeue |
| `v3_exq_1038_arc131_coalition_endogenous_recruitment_rate_probe_20260914T201122Z_v3` | PASS | endogenous_recruitment_engaged_at_default_threshold |
| `v3_exq_1012a_e3_commensurability_selection_level_regime_validation_20260914T221427Z_v3` | PASS | operator_selection_consequential_both_regimes |
| `v3_exq_1028_sd082_learning_signal_extended_budget_20260914T223157Z_v3` | PASS | c2_noisy__c3_sign_null |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_861i_inv050_mech091_commit_attribution_pinned_confirmation_20260914T121029Z_v3` | PASS | 11888 | **0** | 0.000 | live |

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
