# Pending Experiment Review

Generated: `2026-09-26T12:25:51Z`  
Last review: `2026-09-25T06:06:12Z`  
Scanned: 3002 claim_evidence entries considered (3016 already reviewed), 4905 manifest file(s) on disk.  
Pending: **8** item(s) -- 0 PASS, 8 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1105a_grounded_valuation_null_detector_v4a_20260925T154155Z_v3` | 2026-09-25T15:41 | INV-054, MECH-523 | — |
| `v3_exq_1067_mech266_squash_vs_clamp_cap_sweep_20260925T161024Z_v3` | 2026-09-25T16:10 | MECH-266, SD-032a | — |
| `v3_exq_1106_mech287b_stage0_lock_precondition_20260925T164510Z_v3` | 2026-09-25T16:45 | MECH-287 | — |
| `v3_exq_1107_sd032a_trained_mode_reversal_drive_20260925T175306Z_v3` | 2026-09-25T17:53 | MECH-157, SD-032a | — |
| `v3_exq_1099_contamination_truncation_extension_probe_20260925T182543Z_v3` | 2026-09-25T18:25 | (no claim tags) | — |
| `v3_exq_1104_sd032b_effort_proxy_validation_20260925T202059Z_v3` | 2026-09-25T20:20 | (no claim tags) | — |
| `v3_exq_1090_mech449_endogenous_safety_veto_validation_20260925T221242Z_v3` | 2026-09-25T22:12 | MECH-449 | — |
| `v3_exq_1108_n2_replay_encoder_full_dose_pinned_20260926T100252Z_v3` | 2026-09-26T10:02 | (no claim tags) | — |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1107_sd032a_trained_mode_reversal_drive_20260925T175306Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_1108_n2_replay_encoder_full_dose_pinned_20260926T100252Z_v3` | FAIL | neither | **precondition_unmet** |

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
