# Pending Experiment Review

Generated: `2026-05-05T17:52:32Z`  
Last review: `2026-05-05T06:52:26Z`  
Pending: **6** item(s) -- 0 PASS, 4 FAIL, 2 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_418i_sd016_divweight_sweep_20260504T221922Z_v3` | 2026-05-04T22:19 | SD-016 | — |
| `v3_exq_517a_mech302_relief_completion_discriminative_pair_20260504T222032Z_v3` | 2026-05-04T22:20 | MECH-302 | — |
| `v3_exq_433e_sd029_eventcond_comparator_reef_20260505T072754Z_v3` | 2026-05-05T07:27 | MECH-256, SD-029 | — |
| `v3_exq_514b_sd049_phase_2_behavioural_validation_20260505T005802Z_v3` | 2026-05-05T17:52 | MECH-229, MECH-230, SD-015, SD-049 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-517a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-433e` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
