# Pending Experiment Review

Generated: `2026-07-11T22:37:16Z`  
Last review: `2026-07-11T22:37:09Z`  
Pending: **8** item(s) -- 0 PASS, 8 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_734_env_difficulty_competence_recovery_sweep_20260711T092149Z_v3` | 2026-07-11T09:21 | (no claim tags) | — |
| `v3_exq_733a_rebinding_pB_directed_traversal_20260711T095846Z_v3` | 2026-07-11T09:58 | MECH-456 | — |
| `v3_exq_733a_rebinding_pA_survival_onboarded_20260711T100753Z_v3` | 2026-07-11T10:07 | MECH-456 | — |
| `v3_exq_735_drive_reward_balance_sweep_20260711T114313Z_v3` | 2026-07-11T11:43 | (no claim tags) | — |
| `v3_exq_737_ree_latent_policy_head_competence_probe_20260711T192837Z_v3` | 2026-07-11T19:28 | (no claim tags) | — |
| `v3_exq_736_curriculum_competence_recovery_diagnostic_20260711T200431Z_v3` | 2026-07-11T20:04 | (no claim tags) | — |
| `v3_exq_740_inv064_maturational_sequence_e3_bounded_20260711T211644Z_v3` | 2026-07-11T21:16 | INV-064 | — |
| `v3_exq_737_ree_latent_policy_head_competence_probe_20260711T222643Z_v3` | 2026-07-11T22:26 | (no claim tags) | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_736_curriculum_competence_recovery_diagnostic_20260711T200431Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

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
