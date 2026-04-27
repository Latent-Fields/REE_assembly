# Pending Experiment Review

Generated: `2026-04-27T14:47:47Z`  
Last review: `2026-04-27T14:11:00Z`  
Pending: **6** item(s) -- 3 PASS, 0 FAIL, 3 runner-only (ERROR/UNKNOWN/smoke)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_484_sd033a_distractor_resistance_20260427T054449Z_v3` | 2026-04-27T05:44 | MECH-261, MECH-262, SD-033a |
| `v3_exq_485_sd033b_ofc_analog_landing_20260427T054454Z_v3` | 2026-04-27T05:44 | MECH-261, MECH-263, SD-033b |
| `v3_exq_493_mech295_liking_bridge_validation_20260427T080304Z_v3` | 2026-04-27T08:03 | MECH-117, MECH-295, SD-012, SD-014, SD-015 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-484` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-485` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-493` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
