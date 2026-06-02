# Pending Experiment Review

Generated: `2026-06-02T16:55:08Z`  
Last review: `2026-06-02T16:49:58Z`  
Pending: **2** item(s) -- 0 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 2 unclaimed manifest(s)

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| FAIL | `v3_exq_626a_goal_pipeline_developmental_window_diagnostic_20260601T201354Z_v3` | v3_exq_626a_goal_pipeline_developmental_window_diagnostic | V3-EXQ-626a | ? |
| FAIL | `v3_exq_625c_sd037_axis_b_phase1b_dynamic_crossings_mech341_20260602T072226Z_v3` | v3_exq_625c_sd037_axis_b_phase1b_dynamic_crossings_mech341 | V3-EXQ-625c | non_contributory |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
