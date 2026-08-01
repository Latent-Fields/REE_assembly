# Pending Experiment Review

Generated: `2026-08-01T13:56:13Z`  
Last review: `2026-08-01T13:48:21Z`  
Pending: **7** item(s) -- 1 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_836a_mech476_dose_dependent_consolidation_redesign_20260801T000533Z_v3` | 2026-08-01T00:05 | MECH-476 | — |
| `v3_exq_836d_mech476_novelty_tagging_consolidation_redesign_20260801T030035Z_v3` | 2026-08-01T03:00 | MECH-476 | — |
| `v3_exq_836e_mech476_interval_dependent_consolidation_redesign_20260801T124230Z_v3` | 2026-08-01T12:42 | MECH-476 | — |
| `v3_exq_856_sd087_harm_surprise_pe_fingerprint_20260801T124431Z_v3` | 2026-08-01T12:44 | SD-087 | — |
| `v3_exq_857_q086_gentler_env_fingerprint_20260801T134757Z_v3` | 2026-08-01T13:47 | Q-086 | — |
| `v3_exq_848_arc005_precision_only_decoupled_ladder_20260801T134855Z_v3` | 2026-08-01T13:48 | ARC-005 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_852_sd085_f_weight_substrate_readiness_20260801T124251Z_v3` | 2026-08-01T12:42 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_857_q086_gentler_env_fingerprint_20260801T134757Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

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
