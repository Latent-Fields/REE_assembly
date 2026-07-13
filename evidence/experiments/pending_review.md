# Pending Experiment Review

Generated: `2026-07-13T04:18:44Z`  
Last review: `2026-07-12T13:26:43Z`  
Pending: **5** item(s) -- 0 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_746_inv089_harm_eval_z_harm_calibrated_bound_20260712T142637Z_v3` | 2026-07-12T14:26 | INV-089 | — |
| `v3_exq_744a_inv088_world_goal_evaluator_dv_coupling_20260712T144028Z_v3` | 2026-07-12T14:40 | INV-088 | — |
| `v3_exq_745_rebinding_ecological_patchflip_20260712T162519Z_v3` | 2026-07-12T16:25 | MECH-456 | — |
| `v3_exq_746a_inv089_harm_eval_z_harm_calibrated_bound_v2_20260712T170011Z_v3` | 2026-07-12T17:00 | INV-089 | — |
| `v3_exq_742_mech457_actor_critic_onoff_20260713T032215Z_v3` | 2026-07-13T03:22 | MECH-457 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
