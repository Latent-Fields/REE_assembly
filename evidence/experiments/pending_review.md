# Pending Experiment Review

Generated: `2026-08-28T07:08:30Z`  
Last review: `2026-08-25T18:42:08Z`  
Pending: **7** item(s) -- 7 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 4 diagnostic run(s) with no confirmed autopsy

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_944b_mech091_salient_event_cycle_boundary_20260825T205738Z_v3` | 2026-08-25T20:57 | MECH-091 |
| `v3_exq_945_cem_elite_authority_throughput_readiness_20260825T210111Z_v3` | 2026-08-25T21:01 | (no claim tags) |
| `v3_exq_925a_e3_fdominance_committed_regime_causal_harness_20260825T220607Z_v3` | 2026-08-25T22:06 | (no claim tags) |
| `v3_exq_949_mech314b_authority_rescale_validation_20260825T223833Z_v3` | 2026-08-25T22:38 | MECH-314b |
| `v3_exq_933a_sleep_gap9_entry_pressure_fix_20260826T072405Z_v3` | 2026-08-26T07:24 | (no claim tags) |
| `v3_exq_950_mech492_mech286_threat_gate_place_safety_sourcing_20260826T122526Z_v3` | 2026-08-26T12:25 | MECH-492 |
| `v3_exq_603v_mech357_eligibility_trace_repair_validation_20260827T184708Z_v3` | 2026-08-27T18:47 | MECH-357 |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_945_cem_elite_authority_throughput_readiness_20260825T210111Z_v3` | PASS | cem_authority_and_throughput_validated_at_operating_gain |
| `v3_exq_925a_e3_fdominance_committed_regime_causal_harness_20260825T220607Z_v3` | PASS | committed_regime_engaged_h1_h4_readable |
| `v3_exq_933a_sleep_gap9_entry_pressure_fix_20260826T072405Z_v3` | PASS | entry_pressure_fix_validated |
| `v3_exq_603v_mech357_eligibility_trace_repair_validation_20260827T184708Z_v3` | PASS | eligibility_trace_repair_validated |

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
