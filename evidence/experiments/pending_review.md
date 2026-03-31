# Pending Experiment Review

Generated: `2026-03-31T13:21:48Z`  
Last review: `2026-03-31T01:15:00Z`  
Pending: **2** item(s) -- 1 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_181b_sd016_context_separation_fix_20260331T131040Z_v3` | 2026-03-31T13:10 | ARC-041, MECH-150 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_181_e1_prior_context_discrimination_20260331T072201Z_v3` | 2026-03-31T07:22 | ARC-041, MECH-150 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
