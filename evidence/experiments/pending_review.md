# Pending Experiment Review

Generated: `2026-05-29T06:20:29Z`  
Last review: `2026-05-29T06:13:17Z`  
Pending: **6** item(s) -- 0 PASS, 0 FAIL, 4 runner-only (ERROR/UNKNOWN/smoke), 2 unclaimed manifest(s)

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `v3_exq_612_phase3_cutover_smoke_20260528T175700Z_v3` | v3_exq_612_phase3_cutover_smoke | V3-EXQ-612d | ? |
| FAIL | `v3_exq_598b_gap1_sd033a_bias_head_trainable_ablation_20260527T120345Z_v3` | v3_exq_598b_gap1_sd033a_bias_head_trainable_ablation | V3-EXQ-598b | mixed |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-598b` | FAIL | `?` | FAIL (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-610` | ERROR | `?` | ERROR |
| `V3-EXQ-612` | ERROR | `?` | ERROR |
| `V3-EXQ-611b` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
