# Pending Experiment Review

Generated: `2026-04-23T17:49:07Z`  
Last review: `2026-04-22T23:11:16Z`  
Pending: **25** item(s) -- 24 PASS, 0 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_456_sd033a_lateral_pfc_analog_landing_v3_20260420T145521Z_v3` | 2026-04-20T14:55 | MECH-261, MECH-262, SD-033a |
| `v3_exq_462_mech267_rule_binding_v3_20260420T235721Z_v3` | 2026-04-20T23:57 | MECH-262, MECH-267, SD-033a |
| `v3_exq_465_mech267_intrusive_simulation_filtering_v3_20260420T235804Z_v3` | 2026-04-20T23:58 | MECH-094, MECH-261, MECH-267 |
| `v3_exq_462_mech267_rule_binding_v3_20260421T055927Z_v3` | 2026-04-21T05:59 | MECH-262, MECH-267, SD-033a |
| `v3_exq_465_mech267_intrusive_simulation_filtering_v3_20260421T055941Z_v3` | 2026-04-21T05:59 | MECH-094, MECH-261, MECH-267 |
| `v3_exq_462_mech267_rule_binding_v3_20260421T055952Z_v3` | 2026-04-21T05:59 | MECH-262, MECH-267, SD-033a |
| `v3_exq_456_sd033a_lateral_pfc_analog_landing_v3_20260421T180848Z_v3` | 2026-04-21T18:08 | MECH-261, MECH-262, SD-033a |
| `v3_exq_460_sd034_verified_but_not_released_v3_20260421T180858Z_v3` | 2026-04-21T18:08 | MECH-260, MECH-261, SD-034 |
| `v3_exq_466_sd034_satisficing_residue_discharge_v3_20260421T180907Z_v3` | 2026-04-21T18:09 | MECH-094, SD-034 |
| `v3_exq_463_mech268_dacc_conflict_saturation_v3_20260421T180917Z_v3` | 2026-04-21T18:09 | MECH-258, MECH-268, SD-032b, SD-034 |
| `v3_exq_468_sd034_mech268_commitment_vs_contradiction_v3_20260421T180927Z_v3` | 2026-04-21T18:09 | MECH-090, MECH-268, SD-034 |
| `v3_exq_464_mech266_competing_goals_v3_20260421T180938Z_v3` | 2026-04-21T18:09 | MECH-259, MECH-266, SD-032a |
| `v3_exq_467_mech266_mode_stickiness_v3_20260421T180948Z_v3` | 2026-04-21T18:09 | MECH-266, SD-032a |
| `v3_exq_462_mech267_rule_binding_v3_20260421T180958Z_v3` | 2026-04-21T18:09 | MECH-262, MECH-267, SD-033a |
| `v3_exq_465_mech267_intrusive_simulation_filtering_v3_20260421T181008Z_v3` | 2026-04-21T18:10 | MECH-094, MECH-261, MECH-267 |
| `v3_exq_456_sd033a_lateral_pfc_analog_landing_v3_20260421T202344Z_v3` | 2026-04-21T20:23 | MECH-261, MECH-262, SD-033a |
| `v3_exq_460_sd034_verified_but_not_released_v3_20260421T202347Z_v3` | 2026-04-21T20:23 | MECH-260, MECH-261, SD-034 |
| `v3_exq_466_sd034_satisficing_residue_discharge_v3_20260421T202351Z_v3` | 2026-04-21T20:23 | MECH-094, SD-034 |
| `v3_exq_463_mech268_dacc_conflict_saturation_v3_20260421T202354Z_v3` | 2026-04-21T20:23 | MECH-258, MECH-268, SD-032b, SD-034 |
| `v3_exq_468_sd034_mech268_commitment_vs_contradiction_v3_20260421T202356Z_v3` | 2026-04-21T20:23 | MECH-090, MECH-268, SD-034 |
| `v3_exq_464_mech266_competing_goals_v3_20260421T202359Z_v3` | 2026-04-21T20:23 | MECH-259, MECH-266, SD-032a |
| `v3_exq_467_mech266_mode_stickiness_v3_20260421T202402Z_v3` | 2026-04-21T20:24 | MECH-266, SD-032a |
| `v3_exq_462_mech267_rule_binding_v3_20260421T202405Z_v3` | 2026-04-21T20:24 | MECH-262, MECH-267, SD-033a |
| `v3_exq_465_mech267_intrusive_simulation_filtering_v3_20260421T202408Z_v3` | 2026-04-21T20:24 | MECH-094, MECH-261, MECH-267 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-471` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
