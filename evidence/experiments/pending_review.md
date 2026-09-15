# Pending Experiment Review

Generated: `2026-09-15T01:21:58Z`  
Last review: `2026-09-15T01:19:56Z`  
Pending: **5** item(s) -- 3 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 1 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication; 4 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | 2026-09-14T12:56 | INV-086, MECH-428 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
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
| `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` | FAIL | substrate_not_ready_requeue |
| `v3_exq_1038_arc131_coalition_endogenous_recruitment_rate_probe_20260914T201122Z_v3` | PASS | endogenous_recruitment_engaged_at_default_threshold |
| `v3_exq_1012a_e3_commensurability_selection_level_regime_validation_20260914T221427Z_v3` | PASS | operator_selection_consequential_both_regimes |
| `v3_exq_1028_sd082_learning_signal_extended_budget_20260914T223157Z_v3` | PASS | c2_noisy__c3_sign_null |

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `v3_exq_1036_ext002_stage2_revisit_rate_dv_calibration_20260915T003319Z_v3` | v3_exq_1036_ext002_stage2_revisit_rate_dv_calibration | V3-EXQ-1036 | diagnostic_no_direction |

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
