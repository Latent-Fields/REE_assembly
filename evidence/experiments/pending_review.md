# Pending Experiment Review

Generated: `2026-04-19T22:44:59Z`  
Last review: `2026-04-19T22:44:49Z`  
Pending: **3** item(s) -- 0 PASS, 2 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_397_arc007_path_memory_ablation_20260419T153153Z_v3` | 2026-04-19T15:31 | ARC-007, SD-004 | — |
| `v3_exq_433a_sd029_eventcond_comparator_scripted_20260419T161931Z_v3` | 2026-04-19T16:19 | MECH-256, SD-029 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-325c` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
