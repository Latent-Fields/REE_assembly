# Pending Experiment Review

Generated: `2026-05-07T20:46:48Z`  
Last review: `2026-05-07T04:14:02Z`  
Pending: **7** item(s) -- 0 PASS, 2 FAIL, 5 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_535a_sd029_p3_eval_fix_20260507T203343Z_v3` | 2026-05-07T20:33 | MECH-256, SD-029 | — |
| `v3_exq_536_goal_seeding_lift_ablation_20260507T202858Z_v3` | 2026-05-07T20:46 | ARC-030, MECH-112, MECH-295, SD-012, SD-018 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-514d` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-514e` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-524` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-536` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-530` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
