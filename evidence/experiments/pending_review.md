# Pending Experiment Review

Generated: `2026-07-18T08:07:35Z`  
Last review: `2026-07-18T04:54:03Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_sd068_null_content_control_diagnostic_20260718T065939Z_v3` | 2026-07-18T06:59 | INV-047, MECH-168, MECH-169, SD-068 | — |
| `v3_exq_sd068_null_content_control_diagnostic_20260718T072318Z_v3` | 2026-07-18T07:23 | INV-047, MECH-168, MECH-169, SD-068 | — |

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
