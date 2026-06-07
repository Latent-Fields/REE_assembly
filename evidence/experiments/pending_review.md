# Pending Experiment Review

Generated: `2026-06-07T16:33:35Z`  
Last review: `2026-06-07T14:39:42Z`  
Pending: **3** item(s) -- 0 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_624c_arc068_mech320_niv_salamone_dissociation_20260607T110318Z_v3` | 2026-06-07T11:03 | ARC-068, MECH-320 | — |
| `v3_exq_603g_scaffolded_sd054_substrate_readiness_20260607T150056Z_v3` | 2026-06-07T15:00 | (no claim tags) | — |
| `v3_exq_651a_arc060_blocked_goal_recovery_20260607T150734Z_v3` | 2026-06-07T15:07 | ARC-060 | — |

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
