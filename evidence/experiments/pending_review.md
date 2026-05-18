# Pending Experiment Review

Generated: `2026-05-18T04:20:04Z`  
Last review: `2026-05-17T10:24:31Z`  
Pending: **6** item(s) -- 0 PASS, 5 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T125958Z_v3` | 2026-05-17T12:59 | ARC-062, MECH-309 | — |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130046Z_v3` | 2026-05-17T13:00 | ARC-062, MECH-309 | — |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130300Z_v3` | 2026-05-17T13:03 | ARC-062, MECH-309 | — |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T140320Z_v3` | 2026-05-17T14:03 | ARC-062, MECH-309 | — |
| `v3_exq_543g_arc062_outcome_coupled_falsifier_20260517T144716Z_v3` | 2026-05-17T14:47 | ARC-062, MECH-309 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-585` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
