# Pending Experiment Review

Generated: `2026-08-08T08:05:55Z`  
Last review: `2026-08-07T20:54:17Z`  
Pending: **6** item(s) -- 4 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_887a_sd014_node_valence_repfunc_sensitized_20260807T214013Z_v3` | 2026-08-07T21:40 | SD-014 | — |
| `v3_exq_894_mech074d_bla_remap_attribution_selectivity_20260808T005219Z_v3` | 2026-08-08T00:52 | MECH-074d | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_891_mech286_sleep_onset_conjunction_signature_20260807T185658Z_v3` | 2026-08-07T18:56 | MECH-286 |
| `v3_exq_893_mech232_da_representational_expansion_confirmer_20260808T002050Z_v3` | 2026-08-08T00:20 | MECH-232 |
| `v3_exq_895_mech074c_cea_fast_prime_dynamics_20260808T012422Z_v3` | 2026-08-08T01:24 | MECH-074c |
| `v3_exq_892_mech322_replay_corroboration_survival_20260808T051616Z_v3` | 2026-08-08T05:16 | MECH-322 |

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
