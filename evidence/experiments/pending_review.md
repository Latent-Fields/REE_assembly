# Pending Experiment Review

Generated: `2026-06-07T13:56:52Z`  
Last review: `2026-06-07T13:55:31Z`  
Pending: **4** item(s) -- 1 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 2 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_648a_mech314a_phase2_substrate_readiness_20260607T105407Z_v3` | 2026-06-07T10:54 | (no claim tags) | — |
| `v3_exq_604b_q044_mech314_subflavour_ablation_authority_on_20260607T110114Z_v3` | 2026-06-07T11:01 | MECH-314, MECH-314a, MECH-314b, MECH-314c, Q-044 | — |
| `v3_exq_651_arc060_blocked_goal_recovery_20260607T131928Z_v3` | 2026-06-07T13:19 | ARC-060 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_649_arc065_gapa_shared_candidate_summary_source_20260607T131429Z_v3` | 2026-06-07T13:14 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_648a_mech314a_phase2_substrate_readiness_20260607T105407Z_v3` | FAIL | phase2_wiring_does_not_support | **precondition_unmet** |
| `v3_exq_649_arc065_gapa_shared_candidate_summary_source_20260607T131429Z_v3` | PASS | gapa_shared_channel_ready | **precondition_unmet** |

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
