# Pending Experiment Review

Generated: `2026-04-09T19:21:48Z`  
Last review: `2026-04-09T18:15:00Z`  
Pending: **3** item(s) -- 0 PASS, 0 FAIL, 3 runner-only (ERROR/UNKNOWN/smoke)

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-265` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-308` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-267` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
