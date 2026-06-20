# Pending Experiment Review

Generated: `2026-06-20T08:32:17Z`  
Last review: `2026-06-20T08:31:59Z`  
Pending: **3** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 1 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3` | 2026-06-19T23:34 | (no claim tags) | — |
| `v3_exq_460h_sd034_decommit_refractory_independent_20260620T014714Z_v3` | 2026-06-20T01:47 | MECH-445, MECH-446 | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| FAIL | `v3_exq_514t_sd049_phase2_mech436_drive_coupling_retest_20260620T031416Z_v3` | v3_exq_514t_sd049_phase2_mech436_drive_coupling_retest | V3-EXQ-514t | non_contributory |

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
