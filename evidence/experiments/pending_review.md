# Pending Experiment Review

Generated: `2026-04-11T12:16:56Z`  
Last review: `2026-04-11T03:45:00Z`  
Pending: **7** item(s) -- 0 PASS, 6 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_323_sd019_harm_nonredundancy_20260410T160857Z_v3` | 2026-04-10T16:09 | SD-011, SD-019 | — |
| `v3_exq_325_sd021_descending_pain_modulation_20260410T160919Z_v3` | 2026-04-10T22:20 | MECH-090, SD-011, SD-021 | — |
| `v3_exq_330_sd013_contrastive_counterfactual_20260411T023725Z_v3` | 2026-04-11T02:37 | ARC-033, SD-003, SD-013 | — |
| `v3_exq_322_sd015_resource_encoder_seeding_20260410T222041Z_v3` | 2026-04-11T05:05 | MECH-112, SD-015 | — |
| `v3_exq_324_sd020_harm_surprise_pe_20260411T050533Z_v3` | 2026-04-11T05:05 | Q-036, SD-011, SD-020 | — |
| `v3_exq_266a_q020_valence_geometry_pair_fixed_20260411T095750Z_v3` | 2026-04-11T12:16 | Q-020 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-325` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
