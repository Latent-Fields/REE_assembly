# Pending Experiment Review

Generated: `2026-05-08T22:38:35Z`  
Last review: `2026-05-08T22:34:09Z`  
Pending: **1** item(s) -- 0 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_530c_arc016_precision_commit_stepharness_20260508T172357Z_v3` | 2026-05-08T18:00 | ARC-016 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
