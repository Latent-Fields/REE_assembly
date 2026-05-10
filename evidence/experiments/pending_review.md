# Pending Experiment Review

Generated: `2026-05-10T04:25:55Z`  
Last review: `2026-05-09T20:14:34Z`  
Pending: **8** item(s) -- 3 PASS, 4 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_530c_arc016_precision_commit_stepharness_20260508T172357Z_v3` | 2026-05-08T18:00 | ARC-016 | — |
| `v3_exq_141d_mech111_novelty_drive_rng_desync_20260508T235919Z_v3` | 2026-05-08T23:59 | MECH-111 | — |
| `v3_exq_436a_sd017_arc045_mech166_context_harm_phase2_20260509T214636Z_v3` | 2026-05-09T21:46 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_418l_sd017_action_bias_div_phase2_20260509T215331Z_v3` | 2026-05-09T21:53 | SD-017 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_500a_sd017_sleep_phase_readiness_phase2_20260509T204158Z_v3` | 2026-05-09T20:41 | SD-017 |
| `v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3` | 2026-05-09T21:45 | ARC-062, MECH-309, SD-029 |
| `v3_exq_503a_sd017_sleep_phase_discriminative_phase2_20260509T214628Z_v3` | 2026-05-09T21:46 | SD-017 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-542` | ERROR | `?` | ERROR (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
