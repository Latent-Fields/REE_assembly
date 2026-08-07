# Pending Experiment Review

Generated: `2026-08-07T19:00:06Z`  
Last review: `2026-08-03T11:58:39Z`  
Pending: **12** item(s) -- 5 PASS, 7 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 3 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_875_mech471_competence_provenance_20260803T120202Z_v3` | 2026-08-03T12:02 | MECH-471 | — |
| `v3_exq_867b_mech321_harm_aware_selection_matched_pool_20260804T015912Z_v3` | 2026-08-04T01:59 | MECH-321 | — |
| `v3_exq_887_sd014_node_valence_representational_functional_20260804T022547Z_v3` | 2026-08-04T02:25 | SD-014 | — |
| `v3_exq_848b_arc005_precision_only_finer_ladder_20260804T064758Z_v3` | 2026-08-04T06:47 | ARC-005 | — |
| `v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3` | 2026-08-04T07:15 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_875a_mech471_competence_provenance_20260804T114106Z_v3` | 2026-08-04T11:41 | MECH-471 | — |
| `v3_exq_882a_mech472_context_memorization_generalization_20260805T110228Z_v3` | 2026-08-05T11:02 | MECH-472 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3` | 2026-08-03T19:24 | MECH-358, SD-059 |
| `v3_exq_873a_mech322_sleep_replay_carveout_fraction_gate_20260804T062309Z_v3` | 2026-08-04T06:23 | MECH-322 |
| `v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3` | 2026-08-04T07:52 | MECH-074, MECH-074a, MECH-074b |
| `v3_exq_149b_q004_tau_r_largebudget_20260804T234245Z_v3` | 2026-08-04T23:42 | Q-004 |
| `v3_exq_890_mech471_acquisition_reliability_probe_20260806T041928Z_v3` | 2026-08-06T04:19 | MECH-471 |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3` | PASS | substrate_reproduces_603q_reference |
| `v3_exq_873a_mech322_sleep_replay_carveout_fraction_gate_20260804T062309Z_v3` | PASS | replay_carveout_fires_and_fails_closed |
| `v3_exq_890_mech471_acquisition_reliability_probe_20260806T041928Z_v3` | PASS | early_divergence_supports_h1_framing |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
