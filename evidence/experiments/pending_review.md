# Pending Experiment Review

Generated: `2026-04-17T20:54:10Z`  
Last review: `2026-04-17T14:17:55Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_431_sd003_causal_discrimination_dry_20260417T142339Z_v3` | 2026-04-17T14:23 | SD-003, SD-013 | — |
| `v3_exq_431_sd003_causal_discrimination_dry_20260417T143459Z_v3` | 2026-04-17T14:34 | SD-003, SD-013 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
