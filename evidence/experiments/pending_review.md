# Pending Experiment Review

Generated: `2026-09-24T05:10:22Z`  
Last review: `2026-09-23T18:35:00Z`  
Scanned: 2985 claim_evidence entries considered (3004 already reviewed), 4875 manifest file(s) on disk.  
Pending: **7** item(s) -- 4 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication; 6 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1077_sdppb9_harm_head_undertrain_probe_20260923T184633Z_v3` | 2026-09-23T18:46 | (no claim tags) | — |
| `v3_exq_1082_sdppb5_alpha09_live_battery_revalidation_20260924T045004Z_v3` | 2026-09-24T04:50 | (no claim tags) | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1078_inv069_zself_coherence_unsettled_20260923T182046Z_v3` | 2026-09-23T18:20 | INV-069 |
| `v3_exq_1012c_e3_commensurability_eligibility_stage_validation_20260923T215322Z_v3` | 2026-09-23T21:53 | MECH-439 |
| `v3_exq_1081_sdppb1_world_forward_ranking_reach_probe_20260923T222438Z_v3` | 2026-09-23T22:24 | (no claim tags) |
| `v3_exq_1080_contamination_truncation_prevalence_probe_20260924T000105Z_v3` | 2026-09-24T00:01 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1078_inv069_zself_coherence_unsettled_20260923T182046Z_v3` | PASS | arm_a_state_restores_after_burst_untrained_gru_init_contraction__inv069_undetermined|arm_b_sign_locked_gap_above_noise_non_contributory | **vacuous_pass** |
| `v3_exq_1081_sdppb1_world_forward_ranking_reach_probe_20260923T222438Z_v3` | PASS | sleep_head_change_reaches_e3_ranking__rollout_yes__curiosity_undetermined | **precondition_unmet** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_1078_inv069_zself_coherence_unsettled_20260923T182046Z_v3` | PASS | arm_a_state_restores_after_burst_untrained_gru_init_contraction__inv069_undetermined|arm_b_sign_locked_gap_above_noise_non_contributory |
| `v3_exq_1077_sdppb9_harm_head_undertrain_probe_20260923T184633Z_v3` | FAIL | active_error_removed_AMBIGUOUS |
| `v3_exq_1012c_e3_commensurability_eligibility_stage_validation_20260923T215322Z_v3` | PASS | commensurate_at_eligibility_both_regimes |
| `v3_exq_1081_sdppb1_world_forward_ranking_reach_probe_20260923T222438Z_v3` | PASS | sleep_head_change_reaches_e3_ranking__rollout_yes__curiosity_undetermined |
| `v3_exq_1080_contamination_truncation_prevalence_probe_20260924T000105Z_v3` | PASS | contamination_truncation_present_verdicts_robust_no_reruns_owed |
| `v3_exq_1082_sdppb5_alpha09_live_battery_revalidation_20260924T045004Z_v3` | FAIL | margin_lowers_action_read |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_1066_runner_error_20260920T150823Z_v3` | V3-EXQ-1066 | ree-cloud-3 | Non-zero exit code 1; no runner sentinel (stdout-derived 'PASS' not trusted on c |

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
