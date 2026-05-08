# Pending Experiment Review

Generated: `2026-05-08T08:55:33Z`  
Last review: `2026-05-08T00:50:00Z`  
Pending: **7** item(s) -- 0 PASS, 1 FAIL, 6 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_445h_sd032b_dacc_reef_20260508T002953Z_v3` | 2026-05-08T00:29 | MECH-258, MECH-260, SD-032b | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-445h` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-514f` | FAIL | `?` | FAIL (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-523b` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-536a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-536b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-433f` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
