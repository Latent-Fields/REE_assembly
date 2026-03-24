# Pending Experiment Review

Generated: `2026-03-24T19:24:59Z`  
Last review: `2026-03-24T02:40:00Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_093_harm_bridge_e3_fix_20260324T172512Z_v3` | 2026-03-24T17:25 | SD-003, SD-010 | — |
| `v3_exq_094_arc016_rollout_e3_fix_20260324T172536Z_v3` | 2026-03-24T17:25 | ARC-016 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
