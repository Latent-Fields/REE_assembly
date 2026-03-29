# Pending Experiment Review

Generated: `2026-03-29T21:30:05Z`  
Last review: `2026-03-30T00:00:00Z`  
Pending: **12** item(s) -- 0 PASS, 0 FAIL, 12 runner-only (ERROR/UNKNOWN/smoke)

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-162` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-163` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-165` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-164a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-118` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-134` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-138` | ERROR | `?` | ERROR |
| `V3-EXQ-149` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-150` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-151` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-152` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-153` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
