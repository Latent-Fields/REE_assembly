# Pending Experiment Review

Generated: `2026-07-15T04:18:52Z`  
Last review: `2026-07-14T20:43:46Z`  
Pending: **9** item(s) -- 5 PASS, 4 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_750_mech457_inv088_strategy_diversity_readout_20260714T033302Z_v3` | 2026-07-14T03:33 | INV-088, MECH-457 | — |
| `v3_exq_763_mech304_conditioned_inhibition_behavioural_falsifier_20260714T215622Z_v3` | 2026-07-14T21:56 | MECH-304 | — |
| `v3_exq_752_mech457_hcredit_backward_sweep_20260715T001321Z_v3` | 2026-07-15T00:13 | MECH-457 | — |
| `v3_exq_753_mech457_hreturn_go_explore_archive_20260715T020417Z_v3` | 2026-07-15T02:04 | MECH-457 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_751_mech457_hoptim_unsupervised_explorer_actor_critic_20260714T023058Z_v3` | 2026-07-14T02:30 | MECH-457 |
| `v3_exq_760_mech303_contextual_safety_terrain_discrimination_20260714T202728Z_v3` | 2026-07-14T20:27 | MECH-303 |
| `v3_exq_761_mech092_quiescent_replay_selectivity_20260714T204501Z_v3` | 2026-07-14T20:45 | MECH-092 |
| `v3_exq_762_mech046_cea_mode_prior_context_conditioning_20260714T204708Z_v3` | 2026-07-14T20:47 | MECH-046 |
| `v3_exq_742m_mech457_bias_head_baseline_mint_20260715T013328Z_v3` | 2026-07-15T01:33 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_750_mech457_inv088_strategy_diversity_readout_20260714T033302Z_v3` | FAIL | matched_competence_precondition_unmet | **precondition_unmet** |

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
