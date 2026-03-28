# Pending Experiment Review

Generated: `2026-03-28T20:51:49Z`  
Last review: `2026-03-28T18:00:00Z`  
Pending: **36** item(s) -- 4 PASS, 29 FAIL, 3 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_106_harm_obs_a_temporal_persistence_20260328T122330Z_v3` | 2026-03-28T12:23 | SD-011 | — |
| `v3_exq_106_harm_obs_a_temporal_persistence_20260328T122554Z_v3` | 2026-03-28T12:25 | SD-011 | — |
| `v3_exq_104b_e1_parallel_rollout_trained_20260328T122556Z_v3` | 2026-03-28T12:25 | MECH-135 | — |
| `v3_exq_102_harm_obs_a_clip_diagnosis_20260328T123723Z_v3` | 2026-03-28T12:37 | SD-011 | — |
| `v3_exq_104_e1_parallel_rollout_20260328T123736Z_v3` | 2026-03-28T12:37 | MECH-135 | — |
| `v3_exq_105_rollout_horizon_sweep_20260328T123741Z_v3` | 2026-03-28T12:37 | MECH-135 | — |
| `v3_exq_106_harm_obs_a_temporal_persistence_20260328T123745Z_v3` | 2026-03-28T12:37 | SD-011 | — |
| `v3_exq_072b_q021_behavioral_flatness_20260328T135541Z_v3` | 2026-03-28T13:55 | Q-021 | — |
| `v3_exq_073b_mech111_novelty_signal_20260328T145319Z_v3` | 2026-03-28T14:53 | MECH-111 | — |
| `v3_exq_075d_mech113_self_maintenance_20260328T155739Z_v3` | 2026-03-28T15:57 | MECH-113 | — |
| `v3_exq_084d_q022_deff_hopfield_dissociation_20260328T160649Z_v3` | 2026-03-28T16:06 | MECH-118, MECH-119, Q-022 | — |
| `v3_exq_107_arc024_gradient_vs_flat_structure_20260328T161503Z_v3` | 2026-03-28T16:15 | ARC-024 | — |
| `v3_exq_109_sd003_harm_counterfactual_20260328T161634Z_v3` | 2026-03-28T16:16 | ARC-033, SD-003 | — |
| `v3_exq_112_mech071_harm_eval_discriminative_20260328T161808Z_v3` | 2026-03-28T16:18 | MECH-071 | — |
| `v3_exq_113_sd005_double_dissociation_20260328T162148Z_v3` | 2026-03-28T16:21 | SD-005 | — |
| `v3_exq_074e_mech112_117_wanting_liking_20260328T181216Z_v3` | 2026-03-28T18:12 | MECH-112, MECH-117 | — |
| `v3_exq_071d_rollout_batched_attribution_20260328T181225Z_v3` | 2026-03-28T18:12 | ARC-024, MECH-071, SD-003 | — |
| `v3_exq_076e_mech116_arc032_e1_goal_conditioning_20260328T181253Z_v3` | 2026-03-28T18:12 | ARC-032, MECH-116 | — |
| `v3_exq_104b_e1_parallel_rollout_trained_20260328T182606Z_v3` | 2026-03-28T18:26 | MECH-135 | — |
| `v3_exq_051c_q007_zbeta_volatility_injection_20260328T195315Z_v3` | 2026-03-28T19:53 | Q-007 | — |
| `v3_exq_108_mech135_discriminative_pair_20260328T195341Z_v3` | 2026-03-28T19:53 | MECH-135 | — |
| `v3_exq_121_mech095_agency_attribution_pair_20260328T195503Z_v3` | 2026-03-28T19:55 | MECH-095 | — |
| `v3_exq_122_mech089_theta_integration_pair_20260328T200134Z_v3` | 2026-03-28T20:01 | MECH-089 | — |
| `v3_exq_126_mech104_surprise_gate_pair_20260328T203037Z_v3` | 2026-03-28T20:30 | MECH-104 | — |
| `v3_exq_115_sd003_zharms_counterfactual_20260328T204836Z_v3` | 2026-03-28T20:48 | ARC-033, SD-003 | — |
| `v3_exq_111_c1fail_20260328T161718Z_v3` | 2026-03-28T20:51 | SD-007 | — |
| `v3_exq_110_c1fail_20260328T133711Z_v3` | 2026-03-28T20:51 | MECH-098 | — |
| `v3_exq_110_c1fail_20260328T133903Z_v3` | 2026-03-28T20:51 | MECH-098 | — |
| `v3_exq_110_c1fail_20260328T161637Z_v3` | 2026-03-28T20:51 | MECH-098 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_103_e2_training_horizon_ablation_20260328T123730Z_v3` | 2026-03-28T12:37 | MECH-135 |
| `v3_exq_108_mech135_discriminative_pair_20260328T125004Z_v3` | 2026-03-28T12:50 | MECH-135 |
| `v3_exq_106a_harm_obs_a_persistence_fix_20260328T202420Z_v3` | 2026-03-28T20:24 | SD-011 |
| `v3_exq_114_arc007_path_memory_probe_20260328T204815Z_v3` | 2026-03-28T20:48 | ARC-007 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-110` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-111` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-071c` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
