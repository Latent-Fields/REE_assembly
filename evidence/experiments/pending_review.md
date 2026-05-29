# Pending Experiment Review

Generated: `2026-05-29T04:18:24Z`  
Last review: `2026-05-27T17:35:00Z`  
Pending: **5** item(s) -- 1 PASS, 2 FAIL, 2 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_598b_gap1_sd033a_bias_head_trainable_ablation_20260527T120345Z_v3` | 2026-05-27T12:03 | MECH-262, SD-033a | — |
| `v3_exq_591_isef005_curriculum_vs_flat_20260527T183919Z_v3` | 2026-05-27T18:39 | ARC-046 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_611b_mech341_retune_6arm_20260528T181445Z_v3` | 2026-05-28T18:14 | MECH-341 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-610` | ERROR | `?` | ERROR |
| `V3-EXQ-612` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
