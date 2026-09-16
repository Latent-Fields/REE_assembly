# Pending Experiment Review

Generated: `2026-09-16T13:13:49Z`  
Last review: `2026-09-15T01:19:56Z`  
Pending: **11** item(s) -- 9 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 3 diagnostic self-route(s) flagged for adjudication; 1 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | 2026-09-14T12:56 | INV-086, MECH-428 | — |
| `v3_exq_935a_mech266_margin_normalised_cap_rule_20260916T095809Z_v3` | 2026-09-16T09:58 | MECH-266, SD-032a | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1038_arc131_coalition_endogenous_recruitment_rate_probe_20260914T201122Z_v3` | 2026-09-14T20:11 | ARC-131 |
| `v3_exq_1012a_e3_commensurability_selection_level_regime_validation_20260914T221427Z_v3` | 2026-09-14T22:14 | MECH-439 |
| `v3_exq_1028_sd082_learning_signal_extended_budget_20260914T223157Z_v3` | 2026-09-14T22:31 | SD-082 |
| `v3_exq_1036_ext002_stage2_revisit_rate_dv_calibration_20260915T003319Z_v3` | 2026-09-15T00:33 | (no claim tags) |
| `v3_exq_1040_sd077_centered_super_ordinal_cue_key_20260915T021006Z_v3` | 2026-09-15T02:10 | SD-077 |
| `v3_exq_1039_mech428_inv086_waypoint_field_consumer_drive_signal_20260915T025330Z_v3` | 2026-09-15T02:53 | INV-086, MECH-428 |
| `v3_exq_784a_sd074_probe_warmup_desaturation_budget_sweep_corrected_20260915T135328Z_v3` | 2026-09-15T13:53 | SD-074 |
| `v3_exq_1041_sd106_preservation_step_budget_metric_diagnostic_20260915T203743Z_v3` | 2026-09-15T20:37 | SD-106 |
| `v3_exq_964b_mech482_reachability_verify_lift_20260915T215220Z_v3` | 2026-09-15T21:52 | MECH-482 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_1041_sd106_preservation_step_budget_metric_diagnostic_20260915T203743Z_v3` | PASS | metrics_never_comparable | **vacuous_pass** |
| `v3_exq_964b_mech482_reachability_verify_lift_20260915T215220Z_v3` | PASS | mechanism_inert_at_own_magnitude_detector_verified | **vacuous_pass** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_935a_mech266_margin_normalised_cap_rule_20260916T095809Z_v3` | FAIL | rule_right_r_wrong_requeue |

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
