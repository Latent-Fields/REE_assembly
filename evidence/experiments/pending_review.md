# Pending Experiment Review

Generated: `2026-03-30T21:16:11Z`  
Last review: `2026-03-30T21:30:00Z`  
Pending: **19** item(s) -- 6 PASS, 6 FAIL, 7 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_085h_sd015_resource_indicator_diag_20260330T192231Z_v3` | 2026-03-30T19:22 | MECH-112, SD-012, SD-015 | — |
| `v3_exq_085i_sd015_contact_only_seeding_20260330T194234Z_v3` | 2026-03-30T19:42 | MECH-112, SD-012, SD-015 | — |
| `v3_exq_085j_sd015_resource_encoder_20260330T200336Z_v3` | 2026-03-30T20:03 | MECH-112, SD-012, SD-015 | — |
| `v3_exq_085k_sd015_rfm_enc_hybrid_20260330T202205Z_v3` | 2026-03-30T20:22 | MECH-112, SD-012, SD-015 | — |
| `v3_exq_180_resource_prox_gradient_diag_20260330T202316Z_v3` | 2026-03-30T20:23 | ARC-030, MECH-112, SD-012 | — |
| `v3_exq_085l_sd015_proximity_regression_enc_20260330T210913Z_v3` | 2026-03-30T21:09 | MECH-112, SD-012, SD-015 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_166b_sd003_harm_latent_reconstruction_20260330T191329Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |
| `v3_exq_166b_sd003_harm_latent_reconstruction_20260330T191503Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |
| `v3_exq_166c_sd003_harm_latent_shuffled_ablation_20260330T192707Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |
| `v3_exq_166c_sd003_harm_latent_shuffled_ablation_20260330T192815Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |
| `v3_exq_166d_sd003_harm_decoder_discrimination_20260330T194043Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |
| `v3_exq_166d_sd003_harm_decoder_discrimination_20260330T194416Z_v3` | 2026-03-30T21:16 | ARC-033, SD-003, SD-011 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-178` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-166b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-178a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-166c` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-178b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-166d` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-166e` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
