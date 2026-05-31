# Pending Experiment Review

Generated: `2026-05-31T07:07:11Z`  
Last review: `2026-05-30T19:04:00Z`  
Pending: **6** item(s) -- 3 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_490i_mech295_cascade_gap4_tier1_20260530T184434Z_v3` | 2026-05-30T18:44 | MECH-295 | — |
| `v3_exq_483e_sd037_consumer_cascade_4arm_20260530T195925Z_v3` | 2026-05-30T19:59 | MECH-280, MECH-281, SD-037 | — |
| `v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b_20260531T004944Z_v3` | 2026-05-31T00:49 | ARC-065, MECH-341 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_614a_mech341_p3_behavioural_falsifier_3arm_20260530T193245Z_v3` | 2026-05-30T19:32 | ARC-065, MECH-341 |
| `v3_exq_569d_sd056_action_contrastive_diversity_falsifier_floor_recal_20260531T053648Z_v3` | 2026-05-31T05:36 | ARC-065, MECH-341 |
| `v3_exq_519b_sd051_conditioned_safety_store_readiness_20260531T065940Z_v3` | 2026-05-31T06:59 | MECH-304 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
