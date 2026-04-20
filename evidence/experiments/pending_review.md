# Pending Experiment Review

Generated: `2026-04-20T05:50:27Z`  
Last review: `2026-04-20T05:50:20Z`  
Pending: **6** item(s) -- 1 PASS, 3 FAIL, 2 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_397_arc007_path_memory_ablation_20260419T153153Z_v3` | 2026-04-19T15:31 | ARC-007, SD-004 | — |
| `v3_exq_433a_sd029_eventcond_comparator_scripted_20260419T161931Z_v3` | 2026-04-19T16:19 | MECH-256, SD-029 | — |
| `v3_exq_445_sd032b_dacc_analog_20260419T205642Z_v3` | 2026-04-19T20:56 | ARC-033, ARC-058, MECH-258, MECH-260, SD-032b | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_446_sd032a_salience_coordinator_20260420T013457Z_v3` | 2026-04-20T01:34 | MECH-259, MECH-261, SD-032a |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-445` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-325c` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
