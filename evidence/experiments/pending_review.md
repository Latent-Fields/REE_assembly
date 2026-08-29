# Pending Experiment Review

Generated: `2026-08-29T14:14:44Z`  
Last review: `2026-08-29T14:14:34Z`  
Pending: **6** item(s) -- 4 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 4 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_862b_q040c_dacc_pe_weight_delta_correlation_20260828T223750Z_v3` | 2026-08-28T22:37 | Q-040 | — |
| `v3_exq_956_contextmemory_write_gumbel_learned_validation_20260829T014524Z_v3` | 2026-08-29T01:45 | (no claim tags) | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_952_sd075_phasic_warmup_rescue_diagnostic_20260828T211302Z_v3` | 2026-08-28T21:13 | (no claim tags) |
| `v3_exq_936a_mech439_f_variance_share_rollout_clamp_fix_20260829T071510Z_v3` | 2026-08-29T07:15 | MECH-439 |
| `v3_exq_954_mech135_inv088_e1_horizon_sweep_action_divergence_probe_20260829T093705Z_v3` | 2026-08-29T09:37 | INV-088, MECH-135 |
| `v3_exq_957_mech219_controllability_dissociation_substrate_readiness_20260829T113551Z_v3` | 2026-08-29T11:35 | (no claim tags) |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_952_sd075_phasic_warmup_rescue_diagnostic_20260828T211302Z_v3` | PASS | phasic_warmup_rescue_confirmed |
| `v3_exq_956_contextmemory_write_gumbel_learned_validation_20260829T014524Z_v3` | FAIL | gumbel_learned_occupancy_only_content_discrimination_not_confirmed |
| `v3_exq_954_mech135_inv088_e1_horizon_sweep_action_divergence_probe_20260829T093705Z_v3` | PASS | action_blindness_confirmed |
| `v3_exq_957_mech219_controllability_dissociation_substrate_readiness_20260829T113551Z_v3` | PASS | mech219_controllability_dissociation_confirmed |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
