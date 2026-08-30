# Pending Experiment Review

Generated: `2026-08-30T15:50:56Z`  
Last review: `2026-08-30T07:27:59Z`  
Pending: **7** item(s) -- 2 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_436g_sd017_mech166_bias_writesel_ceiling_retest_20260830T105515Z_v3` | 2026-08-30T10:55 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_966_mech143_144_hippocampal_value_sensitivity_causal_20260830T115037Z_v3` | 2026-08-30T11:50 | MECH-143, MECH-144 | — |
| `v3_exq_951_mech320_tonic_vigor_authority_sd054_20260830T125526Z_v3` | 2026-08-30T12:55 | MECH-320 | — |
| `v3_exq_959_mech440_state_conditioning_self_annealing_20260830T143421Z_v3` | 2026-08-30T14:34 | MECH-440 | — |
| `v3_exq_822d_sd082_post_action_summary_validation_20260830T144323Z_v3` | 2026-08-30T14:43 | SD-078, SD-082 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_936a_mech439_f_variance_share_rollout_clamp_fix_20260829T071510Z_v3` | 2026-08-29T07:15 | MECH-439 |
| `v3_exq_965_sd_e1_item1_action_conditioning_validation_20260830T145908Z_v3` | 2026-08-30T14:59 | (no claim tags) |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_965_sd_e1_item1_action_conditioning_validation_20260830T145908Z_v3` | PASS | action_conditioning_converts_both_arms |

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
