# Pending Experiment Review

Generated: `2026-03-23T16:26:38Z`  
Last review: `2026-03-23T08:55:00Z`  
Pending: **21** item(s) -- 3 PASS, 18 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_066_mech089_theta_batching_20260323T101009Z_v3` | 2026-03-23T10:10 | MECH-089 | — |
| `v3_exq_047e_sd005_adversarial_separation_20260323T101100Z_v3` | 2026-03-23T10:11 | SD-005 | — |
| `v3_exq_046_arc007_path_memory_ablation_20260323T121655Z_v3` | 2026-03-23T12:16 | ARC-007, SD-004 | — |
| `v3_exq_069_reafference_selectivity_pair_20260323T121755Z_v3` | 2026-03-23T12:17 | MECH-098 | — |
| `v3_exq_047f_sd005_orth_split_pair_20260323T122748Z_v3` | 2026-03-23T12:27 | SD-005 | — |
| `v3_exq_079_mech102_depletion_ordering_20260323T123107Z_v3` | 2026-03-23T12:31 | MECH-102 | — |
| `v3_exq_079_mech071_harm_calib_pair_20260323T123631Z_v3` | 2026-03-23T12:36 | MECH-071 | — |
| `v3_exq_079_mech071_harm_calib_pair_20260323T123932Z_v3` | 2026-03-23T12:39 | MECH-071 | — |
| `v3_exq_047f_sd005_orth_split_pair_20260323T124338Z_v3` | 2026-03-23T12:43 | SD-005 | — |
| `v3_exq_079_mech071_harm_calib_pair_20260323T124535Z_v3` | 2026-03-23T12:45 | MECH-071 | — |
| `v3_exq_080_mech102_terminal_correction_pair_20260323T124922Z_v3` | 2026-03-23T12:49 | MECH-102 | — |
| `v3_exq_080_mech029_breathoscillator_commit_windows_20260323T131055Z_v3` | 2026-03-23T13:10 | MECH-029 | — |
| `v3_exq_083_mech102_terminal_correction_pair_20260323T131415Z_v3` | 2026-03-23T13:14 | MECH-102 | — |
| `v3_exq_080_mech102_depletion_ordering_20260323T131625Z_v3` | 2026-03-23T13:16 | MECH-102 | — |
| `v3_exq_082_mech098_reafference_harm_pair_20260323T131711Z_v3` | 2026-03-23T13:17 | MECH-098 | — |
| `v3_exq_046_arc007_path_memory_ablation_20260323T143303Z_v3` | 2026-03-23T14:33 | ARC-007, SD-004 | — |
| `v3_exq_071_rollout_batched_attribution_20260323T143350Z_v3` | 2026-03-23T14:33 | ARC-024, MECH-071, SD-003 | — |
| `v3_exq_046_arc007_path_memory_ablation_20260323T162327Z_v3` | 2026-03-23T16:23 | ARC-007, SD-004 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_077_arc024_asymptotic_proxy_pair_20260323T122109Z_v3` | 2026-03-23T12:21 | ARC-024 |
| `v3_exq_078_sd005_split_vs_unified_harm_pair_20260323T122154Z_v3` | 2026-03-23T12:21 | SD-005 |
| `v3_scale_benchmark_20260323T145635Z_v3` | 2026-03-23T14:56 | operational_benchmark |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
