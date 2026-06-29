# Pending Experiment Review

Generated: `2026-06-29T04:18:09Z`  
Last review: `2026-06-27T10:04:21Z`  
Pending: **3** item(s) -- 0 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_700d_arc108_sec7_learned_gating_settling_samelayer_null_retune_20260627T221359Z_v3` | 2026-06-27T22:13 | ARC-108, MECH-439, MECH-450 | — |
| `v3_exq_707_arc110_loop_segregation_validation_20260628T071517Z_v3` | 2026-06-28T07:15 | ARC-110 | — |
| `v3_exq_708_mech440_noisy_selection_head_propagation_falsifier_20260628T220908Z_v3` | 2026-06-28T22:09 | MECH-440 | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_707_arc110_loop_segregation_validation_20260628T071517Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_708_mech440_noisy_selection_head_propagation_falsifier_20260628T220908Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

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
