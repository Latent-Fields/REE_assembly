# Pending Experiment Review

Generated: `2026-04-24T11:54:11Z`  
Last review: `2026-04-24T08:10:41Z`  
Pending: **13** item(s) -- 0 PASS, 0 FAIL, 13 runner-only (ERROR/UNKNOWN/smoke)

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-471` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-470a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-447a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-445e` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-445d` | ERROR | `?` | ERROR |
| `V3-EXQ-455a` | ERROR | `?` | ERROR |
| `V3-EXQ-433c` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-449b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-449c` | ERROR | `?` | ERROR |
| `V3-EXQ-418c` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-476` | ERROR | `?` | ERROR |
| `V3-EXQ-476a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-476b` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
