# Pending Experiment Review

Generated: `2026-09-04T13:53:29Z`  
Last review: `2026-09-03T20:44:11Z`  
Pending: **5** item(s) -- 2 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication; 1 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_999_mech161_vigilance_inverted_u_heartbeat_20260903T211939Z_v3` | 2026-09-03T21:19 | MECH-161 | — |
| `v3_exq_997_mech162_zresource_zworld_planning_reconvergence_20260904T032212Z_v3` | 2026-09-04T03:22 | MECH-162 | — |
| `v3_exq_1001_ext005_sd031_attribution_causal_shift_20260904T032948Z_v3` | 2026-09-04T03:29 | ARC-037, EXT-005, MECH-095, SD-031 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1000_sd_e1_item3_rollout_endpoint_contrastive_validation_20260903T213659Z_v3` | 2026-09-03T21:36 | (no claim tags) |
| `v3_exq_996_isef005_phase_gate_live_channels_20260904T062128Z_v3` | 2026-09-04T06:21 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1000_sd_e1_item3_rollout_endpoint_contrastive_validation_20260903T213659Z_v3` | PASS | rollout_endpoint_contrastive_lifts_cr_ratio_h1 | **vacuous_pass** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_996_isef005_phase_gate_live_channels_20260904T062128Z_v3` | PASS | crossing_count_gate_discriminates_live_closed_loop |

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
