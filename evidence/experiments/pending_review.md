# Pending Experiment Review

Generated: `2026-07-18T16:26:22Z`  
Last review: `2026-07-18T04:54:03Z`  
Pending: **8** item(s) -- 3 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_777a_mech063_orthogonal_control_axes_dissociation_20260718T101635Z_v3` | 2026-07-18T10:16 | MECH-063 | — |
| `v3_exq_782_mech459_advantage_composition_probe_20260718T111818Z_v3` | 2026-07-18T11:18 | MECH-459 | — |
| `v3_exq_779a_mech063_tonic_phasic_dissociation_20260718T121351Z_v3` | 2026-07-18T12:13 | MECH-063 | — |
| `v3_exq_780_mech457_bc_prior_discrimination_20260718T123325Z_v3` | 2026-07-18T12:33 | MECH-457 | — |
| `v3_exq_sd068_rem_unpaired_null_diagnostic_20260718T124216Z_v3` | 2026-07-18T12:42 | INV-047, MECH-168, MECH-169, SD-068 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_783_zworld_granularity_training_crossing_20260718T112340Z_v3` | 2026-07-18T11:23 | Q-002, SD-031 |
| `v3_exq_sd068_rem_gen_gain_content_scale_diagnostic_20260718T122200Z_v3` | 2026-07-18T12:22 | INV-047, MECH-168, MECH-169, SD-068 |
| `v3_exq_sd068_sws_content_scored_readout_diagnostic_20260718T130139Z_v3` | 2026-07-18T13:01 | INV-047, MECH-168, MECH-169, SD-068 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_783_zworld_granularity_training_crossing_20260718T112340Z_v3` | PASS | mixed_partial_separation | **vacuous_pass** |
| `v3_exq_sd068_rem_unpaired_null_diagnostic_20260718T124216Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

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
