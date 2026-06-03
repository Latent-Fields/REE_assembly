# Pending Experiment Review

Generated: `2026-06-03T16:41:17Z`  
Last review: `2026-06-03T14:48:32Z`  
Pending: **6** item(s) -- 2 PASS, 4 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_514l_sd049_phase3_mech229_wanting_liking_identity_20260602T170106Z_v3` | 2026-06-03T05:49 | MECH-229, MECH-230, SD-015, SD-049 | — |
| `v3_exq_610c_inv074_crystallization_necessity_20260602T191404Z_v3` | 2026-06-03T05:49 | INV-074, MECH-333, MECH-334 | — |
| `v3_exq_632_mech230_zgoal_structured_latent_discriminative_20260603T071913Z_v3` | 2026-06-03T07:19 | MECH-230 | — |
| `v3_exq_634_scaffolded_nursery_substrate_readiness_20260603T163357Z_v3` | 2026-06-03T16:33 | (no claim tags) | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_633_mech094_simulation_real_writegate_discriminative_20260603T072042Z_v3` | 2026-06-03T07:20 | MECH-094 |
| `v3_exq_635_modulatory_bias_selection_authority_readiness_20260603T155901Z_v3` | 2026-06-03T15:59 | (no claim tags) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
