# Pending Experiment Review

Generated: `2026-08-10T06:49:11Z`  
Last review: `2026-08-09T06:36:27Z`  
Pending: **16** item(s) -- 7 PASS, 9 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 3 diagnostic self-route(s) flagged for adjudication; 6 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_906a_full_stack_observational_fishtank_20260809T081031Z_v3` | 2026-08-09T08:10 | (no claim tags) | — |
| `v3_exq_894b_mech074d_bla_trainable_attribution_head_20260809T081623Z_v3` | 2026-08-09T08:16 | MECH-074d | — |
| `v3_exq_228c_arc032_theta_bypass_readout_20260809T110214Z_v3` | 2026-08-09T11:02 | ARC-032 | — |
| `v3_exq_905a_mech075_dorsal_lc_arousal_probe_20260809T130730Z_v3` | 2026-08-09T13:07 | MECH-075 | — |
| `v3_exq_903a_mech075_ventral_vta_rpe_probe_20260809T160911Z_v3` | 2026-08-09T16:09 | MECH-075 | — |
| `v3_exq_603s_instrumental_avoidance_freeze_incompatible_hazard_20260809T161324Z_v3` | 2026-08-09T16:13 | MECH-357 | — |
| `v3_exq_324d_sd020_harm_surprise_pe_real_flagpath_20260809T171606Z_v3` | 2026-08-09T17:16 | SD-020 | — |
| `v3_exq_910_mech489_defensive_orienting_validation_20260810T004433Z_v3` | 2026-08-10T00:44 | MECH-489 | — |
| `v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3` | 20260808T153148Z | (no claim tags) | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_907_sd016_h1_ctxdiv_20260809T130845Z_v3` | 2026-08-09T13:08 | (no claim tags) |
| `v3_exq_908_sd016_h3_hard_selection_20260809T131209Z_v3` | 2026-08-09T13:12 | (no claim tags) |
| `v3_exq_876a_mech025_doing_mode_convergence_redesign_20260809T133528Z_v3` | 2026-08-09T13:35 | MECH-025 |
| `v3_exq_906b_full_stack_observational_fishtank_20260809T163034Z_v3` | 2026-08-09T16:30 | (no claim tags) |
| `v3_exq_911_ecology_enrichment_fishtank_20260809T201208Z_v3` | 2026-08-09T20:12 | (no claim tags) |
| `v3_exq_909_sleep_dv_fishtank_multifiring_20260810T011652Z_v3` | 2026-08-10T01:16 | (no claim tags) |
| `v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3` | 2026-08-10T01:47 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_906a_full_stack_observational_fishtank_20260809T081031Z_v3` | FAIL | full_stack_observational_showcase_degenerate | **precondition_unmet** |
| `v3_exq_908_sd016_h3_hard_selection_20260809T131209Z_v3` | PASS | sd016_h3_hard_selection_breaks_saddle:A2_tagger_gumbel | **vacuous_pass** |
| `v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3` | PASS | coupling_instrumentation_live | **precondition_unmet** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_906b_full_stack_observational_fishtank_20260809T163034Z_v3` | PASS | full_stack_observational_showcase_live |
| `v3_exq_911_ecology_enrichment_fishtank_20260809T201208Z_v3` | PASS | ecology_enrichment_confound_reduced |
| `v3_exq_910_mech489_defensive_orienting_validation_20260810T004433Z_v3` | FAIL | defensive_orienting_partial_or_unmet |
| `v3_exq_909_sleep_dv_fishtank_multifiring_20260810T011652Z_v3` | PASS | sleep_dv_nonnull_detected |
| `v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3` | PASS | coupling_instrumentation_live |
| `v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3` | FAIL | readiness_fail_curriculum_gate_blocks_retest |

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
