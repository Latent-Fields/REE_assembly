# Pending Experiment Review

Generated: `2026-04-29T19:32:12Z`
Last review: `2026-04-28T22:00:00Z`  
Pending: **5** item(s) -- 4 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_490c_mech269b_with_liking_bridge_20260429T055859Z_v3` | 2026-04-29T05:58 | Q-040 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_499_mech094_hypothesis_tag_writegate_discriminative_20260429T184730Z_v3` | 2026-04-29T18:47 | MECH-094 |
| `v3_exq_501_sd035_amygdala_analog_vs_binary_20260429T192730Z_v3` | 2026-04-29T19:27 | SD-035 |
| `v3_exq_502_mech062_tri_loop_gate_coordination_20260429T192736Z_v3` | 2026-04-29T19:27 | MECH-062 |
| `v3_exq_500_sd017_sleep_phase_readiness_20260429T192752Z_v3` | 2026-04-29T19:27 | SD-017 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
