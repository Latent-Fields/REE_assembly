# Pending Experiment Review

Generated: `2026-04-06T03:12:59Z`  
Last review: `2026-04-07T01:50:00Z`  
Pending: **0** item(s) -- 0 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

All experiments reviewed. Nothing pending.

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
