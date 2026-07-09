# Pending Experiment Review

Generated: `2026-07-09T19:02:15Z`  
Last review: `2026-07-09T17:58:00Z`  
Pending: **3** item(s) -- 2 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_725_coherence_nonreducibility_learned_binder_20260709T095128Z_v3` | 2026-07-09T09:51 | (no claim tags) | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_721_mech446_closure_latch_lag_distribution_diagnostic_20260709T110001Z_v3` | 2026-07-09T11:00 | (no claim tags) |
| `v3_exq_727_capability_yardstick_calibration_20260709T182049Z_v3` | 2026-07-09T18:20 | (no claim tags) |

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
