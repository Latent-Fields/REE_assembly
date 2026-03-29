# Pending Experiment Review

Generated: `2026-03-29T20:23:17Z`  
Last review: `2026-03-29T21:00:00Z`  
Pending: **25** item(s) -- 8 PASS, 0 FAIL, 17 runner-only (ERROR/UNKNOWN/smoke)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_154_q014_jepa_invariance_blind_spot_20260329T190928Z_v3` | 2026-03-29T20:23 | Q-014 |
| `v3_exq_155_q015_commit_boundary_minimal_contract_20260329T191541Z_v3` | 2026-03-29T20:23 | Q-015 |
| `v3_exq_156_q016_tri_loop_arbitration_policy_20260329T192850Z_v3` | 2026-03-29T20:23 | Q-016 |
| `v3_exq_157_q017_control_axis_minimal_subset_20260329T185928Z_v3` | 2026-03-29T20:23 | Q-017 |
| `v3_exq_158_q018_rc_conflict_threshold_calibration_20260329T192854Z_v3` | 2026-03-29T20:23 | Q-018 |
| `v3_exq_159_q020_arc007_valence_constraint_pair_20260329T193606Z_v3` | 2026-03-29T20:23 | Q-020 |
| `v3_exq_160_q023_multiagent_convergence_pair_20260329T194510Z_v3` | 2026-03-29T20:23 | Q-023 |
| `v3_exq_161_q024_trajectory_representation_triple_20260329T200440Z_v3` | 2026-03-29T20:23 | Q-024 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-157` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-154` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-155` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-156` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-158` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-159` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-160` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-161` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-118` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-134` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-138` | ERROR | `?` | ERROR |
| `V3-EXQ-149` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-150` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-151` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-152` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-153` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-165` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
