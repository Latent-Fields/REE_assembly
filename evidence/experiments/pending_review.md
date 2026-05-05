# Pending Experiment Review

Generated: `2026-05-05T20:44:53Z`  
Last review: `2026-05-05T20:40:03Z`  
Pending: **3** item(s) -- 0 PASS, 2 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_445f_sd032b_dacc_reef_20260505T174448Z_v3` | 2026-05-05T17:44 | MECH-258, MECH-260, SD-032b | — |
| `v3_exq_523_sd029_reef_comparator_20260505T180800Z_v3` | 2026-05-05T18:08 | MECH-256, SD-029 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-445f` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
