# Pending Experiment Review

Generated: `2026-06-12T22:37:36Z`  
Last review: `2026-06-12T22:16:51Z`  
Pending: **6** item(s) -- 0 PASS, 5 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_464c_mech266_competing_goals_behavioural_20260612T115222Z_v3` | 2026-06-12T11:52 | MECH-266, SD-032a | — |
| `v3_exq_466c_sd034_satisficing_residue_discharge_behavioural_20260612T131423Z_v3` | 2026-06-12T13:14 | MECH-094, SD-034 | — |
| `v3_exq_629b_mech342_ecological_maintenance_release_evidence_20260612T155004Z_v3` | 2026-06-12T15:50 | MECH-342 | — |
| `v3_exq_467c_mech266_mode_stickiness_behavioural_20260612T155846Z_v3` | 2026-06-12T15:58 | MECH-266, SD-032a | — |
| `v3_exq_461c_mech090_sd033a_delayed_reward_persistence_behavioural_20260612T213304Z_v3` | 2026-06-12T21:33 | MECH-090, SD-033a, SD-034 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-669` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
