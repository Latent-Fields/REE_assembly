# Pending Experiment Review

Generated: `2026-05-23T22:03:10Z`  
Last review: `2026-05-23T21:57:44Z`  
Pending: **6** item(s) -- 0 PASS, 4 FAIL, 2 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_483c_sd037_broadcast_gap4_tier1_20260521T064444Z_v3` | 2026-05-21T06:44 | MECH-280, MECH-281, SD-037 | — |
| `v3_exq_597b_mech258_pe_vs_raw_post_spcem_20260521T131756Z_v3` | 2026-05-21T13:17 | MECH-258 | — |
| `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T142648Z_v3` | 2026-05-21T14:26 | MECH-260, MECH-313, Q-045 | — |
| `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T204222Z_v3` | 2026-05-21T20:42 | MECH-260, MECH-313, Q-045 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-606a` | ERROR | `?` | ERROR |
| `V3-EXQ-598` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
