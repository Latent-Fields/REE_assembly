# Pending Experiment Review

Generated: `2026-05-12T18:15:43Z`  
Last review: `2026-05-12T18:08:09Z`  
Pending: **11** item(s) -- 1 PASS, 6 FAIL, 4 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_549_arc066_tonic_vigor_discriminative_pair_20260511T190124Z_v3` | 2026-05-11T19:01 | ARC-066, MECH-320 | — |
| `v3_exq_550_zgoal_monostrategy_falsifier_20260511T201859Z_v3` | 2026-05-11T20:18 | MECH-269 | — |
| `v3_exq_543d_arc062_mech260_factorial_falsifier_20260512T010638Z_v3` | 2026-05-12T01:06 | ARC-062, MECH-309 | — |
| `v3_exq_540a_mech307_optionb_3arm_conjunction_decomposition_20260511T201750Z_v3` | 2026-05-12T04:18 | MECH-093, MECH-205, MECH-216, MECH-295, MECH-307, SD-014 | — |
| `v3_exq_540b_mech307_conjunction_threshold_sweep_20260512T025041Z_v3` | 2026-05-12T04:18 | MECH-295, MECH-307 | — |
| `v3_exq_540e_mech307_default_fix_validation_20260512T085927Z_v3` | 2026-05-12T18:15 | MECH-093, MECH-205, MECH-216, MECH-295, MECH-307, SD-014 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_540c_mech307_readsite_probe_20260512T062928Z_v3` | 2026-05-12T18:15 | MECH-295, MECH-307 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-552` | FAIL | `?` | FAIL (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-555` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-557` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-540c` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
