# Pending Experiment Review

Generated: `2026-05-06T15:09:36Z`  
Last review: `2026-05-05T22:04:33Z`  
Pending: **31** item(s) -- 7 PASS, 13 FAIL, 11 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_452a_mech257_dual_function_e2_reef_20260505T184639Z_v3` | 2026-05-05T18:46 | ARC-033, MECH-257, SD-013 | — |
| `v3_exq_454a_arc016_adaptive_commitment_reef_20260505T184703Z_v3` | 2026-05-05T18:47 | ARC-016 | — |
| `v3_exq_452a_mech257_dual_function_e2_reef_20260505T215753Z_v3` | 2026-05-05T21:57 | ARC-033, MECH-257, SD-013 | — |
| `v3_exq_525_sd003_attribution_anchor_20260505T220444Z_v3` | 2026-05-05T22:04 | ARC-033, SD-003 | — |
| `v3_exq_445g_sd032b_dacc_reef_20260505T223845Z_v3` | 2026-05-05T22:38 | MECH-258, MECH-260, SD-032b | — |
| `v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3` | 2026-05-06T01:35 | MECH-302 | — |
| `v3_exq_527_mech112_identity_goal_reef_20260506T080028Z_v3` | 2026-05-06T08:00 | MECH-112 | — |
| `v3_exq_526_q034_reef_threshold_sweep_20260506T082834Z_v3` | 2026-05-06T08:28 | Q-034 | — |
| `v3_exq_527_mech112_identity_goal_reef_20260506T082915Z_v3` | 2026-05-06T08:29 | MECH-112 | — |
| `v3_exq_418k_sd016_context_memory_reef_20260505T223834Z_v3` | 2026-05-06T09:01 | SD-016 | — |
| `v3_exq_532_sd005_latent_domain_selectivity_20260506T090607Z_v3` | 2026-05-06T09:06 | SD-005 | — |
| `v3_exq_529_mech098_reafference_selectivity_20260506T091032Z_v3` | 2026-05-06T09:10 | MECH-098 | — |
| `v3_exq_531_sd015_resource_encoder_ablation_20260506T094124Z_v3` | 2026-05-06T15:09 | SD-015 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_418f_sd016_attention_uniformity_probe_20260428T211430Z_v3` | 2026-04-28T21:14 | SD-016 |
| `v3_exq_523a_sd029_reef_comparator_20260506T064939Z_v3` | 2026-05-06T06:49 | MECH-256, SD-029 |
| `v3_exq_525_sd003_attribution_anchor_20260506T065102Z_v3` | 2026-05-06T06:51 | ARC-033, SD-003 |
| `v3_exq_528_sd029_comparator_trained_20260506T094030Z_v3` | 2026-05-06T09:40 | MECH-256, SD-029 |
| `v3_exq_244a_mech165_replay_diversity_validation_v3` | 2026-05-06T15:09 | MECH-165 |
| `v3_exq_533_mech102_harm_stream_ablation_20260506T094157Z_v3` | 2026-05-06T15:09 | MECH-102 |
| `v3_exq_534_sd016_cue_terrain_training_20260506T094249Z_v3` | 2026-05-06T15:09 | SD-016 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-445g` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-514d` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-517b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-514e` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-524` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-531` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-533` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-534` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-418j` | ERROR | `?` | ERROR |
| `V3-EXQ-530` | ERROR | `?` | ERROR |
| `V3-EXQ-244a` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
