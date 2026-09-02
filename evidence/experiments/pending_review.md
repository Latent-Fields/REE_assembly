# Pending Experiment Review

Generated: `2026-09-02T05:51:18Z`  
Last review: `2026-09-01T08:08:39Z`  
Pending: **23** item(s) -- 18 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 13 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_259_wanting_gradient_navigation_1775666895` | 2026-04-08T16:48 | ARC-030, MECH-112, SD-012, SD-015 | — |
| `v3_exq_963a_mech063ii_tonic_phasic_dissociation_retest_20260902T001425Z_v3` | 2026-09-02T00:14 | MECH-063, SD-069 | — |
| `v3_exq_395_mech220_harm_hub_dry_20260413T074905Z` | 20260413T074928Z | MECH-220 | — |
| `v3_exq_395_mech220_harm_hub_dry_20260413T075033Z` | 20260413T075102Z | MECH-220 | — |
| `v3_exq_395_mech220_harm_hub_dry_20260413T075133Z` | 20260413T075203Z | MECH-220 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | 2026-04-21T18:36 | SD-011 |
| `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z` | 2026-05-09T20:22 | ARC-062, MECH-309 |
| `v3_exq_544_mech313_noise_floor_substrate_readiness_v3_20260510T104458Z` | 2026-05-10T10:44 | ARC-065, MECH-313 |
| `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T164550Z` | 2026-05-10T16:45 | ARC-065, MECH-314, MECH-314a, MECH-314b, MECH-314c |
| `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T164557Z` | 2026-05-10T16:45 | MECH-319 |
| `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T172604Z` | 2026-05-10T17:26 | ARC-065, MECH-314, MECH-314a, MECH-314b, MECH-314c |
| `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T172610Z` | 2026-05-10T17:26 | MECH-319 |
| `v3_exq_547_mech320_tonic_vigor_substrate_readiness_v3_20260510T205612Z` | 2026-05-10T20:56 | ARC-066, MECH-320 |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002616Z` | 2026-05-20T00:26 | ARC-062, MECH-309 |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002633Z` | 2026-05-20T00:26 | ARC-062, MECH-309 |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T041617Z` | 2026-05-20T04:16 | ARC-062, MECH-309 |
| `v3_exq_613_sd056_e2_action_contrastive_substrate_readiness_v3_20260529T083242Z` | 2026-05-29T08:32 | (no claim tags) |
| `v3_exq_617_sd056_multistep_substrate_readiness_v3_20260531T113129Z` | 2026-05-31T11:31 | (no claim tags) |
| `v3_exq_639_arc063_candidate_rule_field_readiness_v3_20260604T154034Z` | 2026-06-04T15:40 | (no claim tags) |
| `v3_exq_968_sd_e1_output_proj_residual_ab_20260901T162647Z_v3` | 2026-09-01T16:26 | (no claim tags) |
| `v3_exq_871b_mech090_e3_reselection_shortcircuit_retest_20260901T212042Z_v3` | 2026-09-01T21:20 | ARC-071, MECH-090 |
| `v4_exq_002_dr13_self_recurrence_falsifier_20260701T065002Z_v4` | 20260701T065002Z | (no claim tags) |
| `v4_exq_003_dr10_z_self_viability_falsifier_20260701T074023Z_v4` | 20260701T074023Z | (no claim tags) |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | PASS | — |
| `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z` | PASS | — |
| `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T164550Z` | PASS | — |
| `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T164557Z` | PASS | — |
| `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T172604Z` | PASS | — |
| `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T172610Z` | PASS | — |
| `v3_exq_547_mech320_tonic_vigor_substrate_readiness_v3_20260510T205612Z` | PASS | — |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002616Z` | PASS | — |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002633Z` | PASS | — |
| `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T041617Z` | PASS | — |
| `v3_exq_613_sd056_e2_action_contrastive_substrate_readiness_v3_20260529T083242Z` | PASS | — |
| `v3_exq_617_sd056_multistep_substrate_readiness_v3_20260531T113129Z` | PASS | — |
| `v3_exq_639_arc063_candidate_rule_field_readiness_v3_20260604T154034Z` | PASS | — |

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
