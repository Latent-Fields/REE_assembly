# Pending Experiment Review

Generated: `2026-04-17T15:46:12Z`  
Last review: `2026-04-17T14:17:55Z`  
Pending: **13** item(s) -- 0 PASS, 0 FAIL, 13 runner-only (ERROR/UNKNOWN/smoke)

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-321b` | ERROR | `?` | ERROR |
| `V3-EXQ-395` | ERROR | `?` | ERROR |
| `V3-EXQ-375` | ERROR | `?` | ERROR |
| `V3-EXQ-406` | ERROR | `?` | ERROR |
| `V3-EXQ-396` | ERROR | `?` | ERROR |
| `V3-EXQ-397` | ERROR | `?` | ERROR |
| `V3-EXQ-429` | ERROR | `?` | ERROR |
| `V3-EXQ-430` | ERROR | `?` | ERROR |
| `V3-EXQ-324b` | ERROR | `?` | ERROR |
| `V3-EXQ-418a` | ERROR | `?` | ERROR |
| `V3-EXQ-385a` | ERROR | `?` | ERROR |
| `V3-EXQ-355a` | ERROR | `?` | ERROR |
| `V3-EXQ-325a` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
