# Pending Experiment Review

Generated: `2026-04-10T18:11:39Z`  
Last review: `2026-04-10T20:00:00Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_266_q020_valence_geometry_pair_20260410T023257Z_v3` | 2026-04-10T17:09 | Q-020 | — |
| `v3_exq_266_q020_valence_geometry_pair_20260410T034439Z_v3` | 2026-04-10T17:09 | Q-020 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
