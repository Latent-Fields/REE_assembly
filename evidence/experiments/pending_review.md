# Pending Experiment Review

Generated: `2026-06-13T09:20:10Z`  
Last review: `2026-06-13T09:14:10Z`  
Pending: **4** item(s) -- 0 PASS, 4 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_468d_sd034_mech268_decommit_hold_behavioural_20260613T045129Z_v3` | 2026-06-13T04:51 | MECH-090, MECH-268, SD-034 | — |
| `v3_exq_655_inv074_crystallization_necessity_taskshift_20260613T070430Z_v3` | 2026-06-13T07:04 | INV-074, MECH-313, MECH-333, MECH-334, MECH-341 | — |
| `v3_exq_460d_sd034_closure_control_plane_behavioural_20260613T072733Z_v3` | 2026-06-13T07:27 | MECH-260, MECH-261, SD-034 | — |
| `v3_exq_669a_mech329_wanting_first_goal_seeding_20260613T074454Z_v3` | 2026-06-13T07:44 | MECH-189, MECH-329 | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_468d_sd034_mech268_decommit_hold_behavioural_20260613T045129Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

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
