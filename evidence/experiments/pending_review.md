# Pending Experiment Review

Generated: `2026-06-18T08:15:03Z`  
Last review: `2026-06-18T08:04:31Z`  
Pending: **5** item(s) -- 0 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 3 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_468e_sd034_mech268_decommit_hold_behavioural_20260618T060133Z_v3` | 2026-06-18T06:01 | MECH-090, MECH-268, SD-034 | — |
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T061915Z_v3` | 2026-06-18T06:19 | MECH-044 | — |
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T061935Z_v3` | 2026-06-18T06:19 | MECH-044 | — |
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T062812Z_v3` | 2026-06-18T06:28 | MECH-044 | — |
| `v3_exq_514s_sd049_phase2_mech436_drive_coupling_retest_20260618T064933Z_v3` | 2026-06-18T06:49 | MECH-436 | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T061915Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T061935Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_688_mech044_hippocampal_relational_binding_20260618T062812Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
