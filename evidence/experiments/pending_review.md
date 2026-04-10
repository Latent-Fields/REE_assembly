# Pending Experiment Review

Generated: `2026-04-10T17:09:59Z`  
Last review: `2026-04-09T22:30:00Z`  
Pending: **24** item(s) -- 5 PASS, 14 FAIL, 5 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_258_mech205_surprise_gated_replay_1775672128_v3` | 2026-04-08T18:15 | MECH-205 | — |
| `v3_exq_288_q034_hazard_resource_threshold_sweep_1775783647_v3` | 2026-04-10T01:14 | Q-034 | — |
| `v3_exq_267_arc038_waking_consolidation_discriminative_20260410T093618Z_v3` | 2026-04-10T09:36 | ARC-038 | — |
| `v3_exq_326_wanting_gradient_nav_fix_dry_20260410T154537Z_v3` | 2026-04-10T15:45 | MECH-216, SD-012, SD-015 | — |
| `v3_exq_326_wanting_gradient_nav_fix_dry_20260410T155010Z_v3` | 2026-04-10T15:50 | MECH-216, SD-012, SD-015 | — |
| `v3_exq_327_mech163_goal_conditioned_nav_dry_20260410T155627Z_v3` | 2026-04-10T15:56 | MECH-163, SD-015 | — |
| `v3_exq_328_mech112_zgoal_structured_latent_dry_20260410T155804Z_v3` | 2026-04-10T15:58 | MECH-112, SD-012 | — |
| `v3_exq_330_sd013_contrastive_counterfactual_dry_20260410T160119Z_v3` | 2026-04-10T16:01 | ARC-033, SD-003, SD-013 | — |
| `v3_exq_331_arc030_approach_avoidance_balance_dry_20260410T160253Z_v3` | 2026-04-10T16:02 | ARC-030 | — |
| `v3_exq_263b_sd023_mech216_landmark_wanting_20260410T093942Z_v3` | 2026-04-10T17:09 | MECH-216, SD-023 | — |
| `v3_exq_264_arc033_e2_harm_s_forward_20260409T170322Z_v3` | 2026-04-10T17:09 | ARC-033 | — |
| `v3_exq_266_q020_valence_geometry_pair_20260410T023257Z_v3` | 2026-04-10T17:09 | Q-020 | — |
| `v3_exq_266_q020_valence_geometry_pair_20260410T034439Z_v3` | 2026-04-10T17:09 | Q-020 | — |
| `v3_exq_318_sd022_limb_damage_stream_separation_1775783716_v3` | 2026-04-10T17:09 | SD-011, SD-022 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_248_q034_threshold_sweep_1775666151_v3` | 2026-04-08T16:35 | Q-034 |
| `v3_exq_254_inv052_single_mechanism_sufficiency_1775724484_v3` | 2026-04-09T08:48 | INV-052 |
| `v3_exq_319_sd022_harm_stream_dissociation_20260410T093948Z_v3` | 2026-04-10T11:03 | SD-011, SD-022 |
| `v3_exq_320_sd013_interventional_training_20260410T155756Z_v3` | 2026-04-10T15:58 | SD-003, SD-013 |
| `v3_exq_329_arc033_e2_harm_s_counterfactual_dry_20260410T155945Z_v3` | 2026-04-10T15:59 | ARC-033, SD-003 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-318` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-263b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-320` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-264` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-267` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
