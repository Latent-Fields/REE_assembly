# Pending Experiment Review

Generated: `2026-06-01T17:26:22Z`  
Last review: `2026-06-01T17:22:37Z`  
Pending: **2** item(s) -- 1 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_603d_q045_mech313_mech260_scaffolded_sd054_20260601T095345Z_v3` | 2026-06-01T09:53 | MECH-260, MECH-313, Q-045 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_625_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T110921Z_v3` | 2026-06-01T11:09 | (no claim tags) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
