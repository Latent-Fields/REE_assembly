# Pending Experiment Review

Generated: `2026-05-10T10:18:02Z`  
Last review: `2026-05-10T10:11:48Z`  
Pending: **6** item(s) -- 3 PASS, 2 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_543b_arc062_phase3_optimized_falsifier_20260510T100841Z_v3` | 2026-05-10T10:08 | ARC-062, MECH-309, SD-029 | — |
| `v3_exq_543b_arc062_phase3_optimized_falsifier_20260510T101419Z_v3` | 2026-05-10T10:14 | ARC-062, MECH-309, SD-029 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_500a_sd017_sleep_phase_readiness_phase2_20260509T204158Z_v3` | 2026-05-09T20:41 | SD-017 |
| `v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3` | 2026-05-09T21:45 | ARC-062, MECH-309, SD-029 |
| `v3_exq_503a_sd017_sleep_phase_discriminative_phase2_20260509T214628Z_v3` | 2026-05-09T21:46 | SD-017 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-542` | ERROR | `?` | ERROR (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
