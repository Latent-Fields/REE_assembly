# Pending Experiment Review

Generated: `2026-06-04T04:18:18Z`  
Last review: `2026-06-03T19:57:16Z`  
Pending: **8** item(s) -- 4 PASS, 4 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_460b_sd034_verified_but_not_released_behavioural_20260603T231621Z_v3` | 2026-06-03T23:16 | MECH-260, MECH-261, SD-034 | — |
| `v3_exq_461b_mech090_sd033a_delayed_reward_persistence_behavioural_20260604T001229Z_v3` | 2026-06-04T00:12 | MECH-090, SD-033a, SD-034 | — |
| `v3_exq_464b_mech266_competing_goals_behavioural_20260604T012553Z_v3` | 2026-06-04T01:25 | MECH-266, SD-032a | — |
| `v3_exq_466b_sd034_satisficing_residue_discharge_behavioural_20260604T035511Z_v3` | 2026-06-04T03:55 | MECH-094, SD-034 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_485b_sd033b_devaluation_sensitivity_20260603T201054Z_v3` | 2026-06-03T20:10 | MECH-263, SD-033b |
| `v3_exq_485c_sd033b_task_role_discrimination_20260603T201055Z_v3` | 2026-06-03T20:10 | MECH-263, SD-033b |
| `v3_exq_626b_goal_pipeline_forced_seed_positive_control_20260603T211703Z_v3` | 2026-06-03T21:17 | (no claim tags) |
| `v3_exq_463b_mech268_dacc_conflict_saturation_behavioural_20260604T030903Z_v3` | 2026-06-04T03:09 | MECH-268 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
