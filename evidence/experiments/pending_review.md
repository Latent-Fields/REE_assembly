# Pending Experiment Review

Generated: `2026-07-26T00:09:24Z`  
Last review: `2026-07-26T00:07:00Z`  
Pending: **3** item(s) -- 0 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_820_mech321_policy_decomposition_bottleneck_arm2_20260725T203453Z_v3` | 2026-07-25T20:34 | ARC-070, MECH-321 | — |
| `v3_exq_817_sd080_consequence_grounding_falsifier_20260725T204837Z_v3` | 2026-07-25T20:48 | SD-004, SD-080 | — |
| `v3_exq_816_mech321_policy_decomposition_discriminative_20260725T214751Z_v3` | 2026-07-25T21:47 | ARC-070, MECH-321 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
