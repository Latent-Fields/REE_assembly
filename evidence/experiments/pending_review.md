# Pending Experiment Review

Generated: `2026-04-13T06:11:42Z`  
Last review: `2026-04-12T09:45:00Z`  
Pending: **8** item(s) -- 1 PASS, 7 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_326_wanting_gradient_nav_fix_dry_20260412T101558Z_v3` | 2026-04-12T10:15 | MECH-216, SD-012, SD-015 | — |
| `v3_exq_326_wanting_gradient_nav_fix_dry_20260412T101736Z_v3` | 2026-04-12T10:17 | MECH-216, SD-012, SD-015 | — |
| `v3_exq_326_wanting_gradient_nav_fix_dry_20260412T101952Z_v3` | 2026-04-12T10:19 | MECH-216, SD-012, SD-015 | — |
| `v3_exq_330a_sd013_contrastive_counterfactual_frac05_dry_20260412T102042Z_v3` | 2026-04-12T10:20 | ARC-033, SD-013 | — |
| `v3_exq_353_arc033_sd003_interventional_vs_observational_dry_20260412T102446Z_v3` | 2026-04-12T10:24 | ARC-033, SD-003, SD-013 | — |
| `v3_exq_328a_mech112_zgoal_structured_latent_dry_20260412T102503Z_v3` | 2026-04-12T10:25 | MECH-112, SD-012 | — |
| `v3_exq_328a_mech112_zgoal_structured_latent_dry_20260412T111655Z_v3` | 2026-04-12T11:16 | MECH-112, SD-012 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_354_mech112_wanting_liking_confirmation_20260412T162103Z_v3` | 2026-04-12T16:24 | MECH-112 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
