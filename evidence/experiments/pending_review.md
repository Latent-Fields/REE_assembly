# Pending Experiment Review

Generated: `2026-07-27T05:36:42Z`  
Last review: `2026-07-26T15:34:37Z`  
Pending: **11** item(s) -- 3 PASS, 8 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_822a_sd078_rule_selection_consumer_20260726T145526Z_v3` | 2026-07-26T14:55 | SD-078 | — |
| `v3_exq_826_mech244_precision_weighting_self_sealing_20260726T152827Z_v3` | 2026-07-26T15:28 | MECH-244 | — |
| `v3_exq_817a_sd080_worldeffect_grounding_falsifier_20260726T153154Z_v3` | 2026-07-26T15:31 | SD-004, SD-080 | — |
| `v3_exq_827_inv091_cross_stream_similarity_band_20260726T163221Z_v3` | 2026-07-26T16:32 | INV-091 | — |
| `v3_exq_824_q081_shared_organisation_landmark_removal_20260726T165630Z_v3` | 2026-07-26T16:56 | Q-081 | — |
| `v3_exq_816d_mech321_policy_decomposition_harshened_env_v2_20260726T185006Z_v3` | 2026-07-26T18:50 | (no claim tags) | — |
| `v3_exq_827a_inv091_cross_stream_similarity_band_phase_sync_20260726T193419Z_v3` | 2026-07-26T19:34 | INV-091 | — |
| `v3_exq_824a_q081_shared_organisation_landmark_removal_20260726T202358Z_v3` | 2026-07-26T20:23 | Q-081 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3` | 2026-07-26T15:21 | MECH-245 |
| `v3_exq_032d_mech102_ttype_escalation_fixed_20260726T180259Z_v3` | 2026-07-26T18:02 | ARC-024, MECH-102, SD-003 |
| `v3_exq_819a_mech457_inv088_zworld_trained_vs_random_gatefix_20260727T005012Z_v3` | 2026-07-27T00:50 | INV-088, MECH-457 |

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
