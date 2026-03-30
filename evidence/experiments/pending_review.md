# Pending Experiment Review

Generated: `2026-03-30T16:58:15Z`  
Last review: `2026-03-30T06:56:23Z`  
Pending: **36** item(s) -- 5 PASS, 13 FAIL, 18 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_084d_q022_deff_hopfield_dissociation_20260329T215126Z_v3` | 2026-03-29T21:51 | MECH-118, MECH-119, Q-022 | — |
| `v3_exq_086_arc030_go_nogo_symmetry_20260329T215407Z_v3` | 2026-03-29T21:54 | ARC-030 | — |
| `v3_exq_130_mech096_dual_stream_routing_pair_20260329T215504Z_v3` | 2026-03-29T21:55 | MECH-096 | — |
| `v3_exq_131_arc023_multirate_heartbeat_pair_20260329T215546Z_v3` | 2026-03-29T21:55 | ARC-023 | — |
| `v3_exq_137_mech097_pps_commit_locus_pair_20260329T215640Z_v3` | 2026-03-29T21:56 | MECH-097 | — |
| `v3_exq_145_sd008_sd007_sd003_integration_20260329T215806Z_v3` | 2026-03-29T21:58 | SD-003, SD-007, SD-008 | — |
| `v3_exq_166a_sd003_obs_space_forward_model_20260329T213108Z_v3` | 2026-03-30T16:58 | ARC-033, SD-003, SD-011 | — |
| `v3_exq_170_q002_r_field_resolution_pair_20260329T213812Z_v3` | 2026-03-30T16:58 | Q-002 | — |
| `v3_exq_170_q002_r_field_resolution_pair_20260330T070234Z_v3` | 2026-03-30T16:58 | Q-002 | — |
| `v3_exq_172_arc018_rollout_viability_pair_20260330T070425Z_v3` | 2026-03-30T16:58 | ARC-018 | — |
| `v3_exq_176_arc036_valence_dimension_probe_20260329T213701Z_v3` | 2026-03-30T16:58 | ARC-036 | — |
| `v3_exq_176_arc036_valence_dimension_probe_20260330T070447Z_v3` | 2026-03-30T16:58 | ARC-036 | — |
| `v3_exq_177_sd008_integration_test_20260329T215657Z_v3` | 2026-03-30T16:58 | SD-008 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_103_e2_training_horizon_ablation_20260329T215416Z_v3` | 2026-03-29T21:54 | MECH-135 |
| `v3_exq_172_arc018_rollout_viability_pair_20260329T213638Z_v3` | 2026-03-30T16:58 | ARC-018 |
| `v3_exq_157_q017_control_axis_minimal_subset_20260330T065453Z_v3` | 2026-03-30T16:58 | Q-017 |
| `v3_exq_171_mech033_kernel_chain_pair_20260329T213946Z_v3` | 2026-03-30T16:58 | MECH-033 |
| `v3_exq_171_mech033_kernel_chain_pair_20260330T070404Z_v3` | 2026-03-30T16:58 | MECH-033 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-162` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-163` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-165` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-164a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-166a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-177` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-157a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-170a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-171a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-172a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-176a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-118` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-134` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-149` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-150` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-151` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-152` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-153` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
