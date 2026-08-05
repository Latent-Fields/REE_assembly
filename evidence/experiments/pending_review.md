# Pending Experiment Review

Generated: `2026-08-05T06:04:58Z`  
Last review: `2026-08-03T11:58:39Z`  
Pending: **10** item(s) -- 4 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_875_mech471_competence_provenance_20260803T120202Z_v3` | 2026-08-03T12:02 | MECH-471 | — |
| `v3_exq_867b_mech321_harm_aware_selection_matched_pool_20260804T015912Z_v3` | 2026-08-04T01:59 | MECH-321 | — |
| `v3_exq_887_sd014_node_valence_representational_functional_20260804T022547Z_v3` | 2026-08-04T02:25 | SD-014 | — |
| `v3_exq_848b_arc005_precision_only_finer_ladder_20260804T064758Z_v3` | 2026-08-04T06:47 | ARC-005 | — |
| `v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3` | 2026-08-04T07:15 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_875a_mech471_competence_provenance_20260804T114106Z_v3` | 2026-08-04T11:41 | MECH-471 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3` | 2026-08-03T19:24 | MECH-358, SD-059 |
| `v3_exq_873a_mech322_sleep_replay_carveout_fraction_gate_20260804T062309Z_v3` | 2026-08-04T06:23 | MECH-322 |
| `v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3` | 2026-08-04T07:52 | MECH-074, MECH-074a, MECH-074b |
| `v3_exq_149b_q004_tau_r_largebudget_20260804T234245Z_v3` | 2026-08-04T23:42 | Q-004 |

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
