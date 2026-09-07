# Pending Experiment Review

Generated: `2026-09-07T04:20:12Z`  
Last review: `2026-09-06T16:56:48Z`  
Pending: **1** item(s) -- 1 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 diagnostic run(s) with no confirmed autopsy; 1 run(s) with recorded (non-gating) preconditions

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3` | 2026-09-06T19:51 | (no claim tags) |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3` | PASS | anchor_restores_centroid_lifts_var__realvar_below_bar__rsd_goal_orthogonal |

## Recorded (non-gating) preconditions

**No action is required on account of this section.** These runs declare a readiness finding in `interpretation.recorded_preconditions[]` that did NOT hold -- but the author deliberately did not gate the run on it, because the run's premise survives the finding (e.g. a shared symmetric prior that biases every arm identically, or a readout-side question with an unaffected control). The entries are kept out of the adjudicating `interpretation.preconditions[]` on purpose: that list is read flat and arm-blind, so an entry there would return a whole-run `precondition_unmet` and bury a valid result. Each run's own `preconditions_scope_note` states the reasoning. Read this as an audit trail when interpreting the run -- it is NOT an adjudication flag, does not block a governance action, and does not exclude the run from scoring. See evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.

| Run ID | Status | Recorded precondition(s) not met | Scope note |
|--------|--------|----------------------------------|------------|
| `v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3` | PASS | dv_headroom_e1coe_score_var_h1 | interpretation.preconditions carries ONLY the per-arm readiness gates (green arms' entries on a partial run, per precondition_gate). interpretation.recorded_preconditions carries (a) the dv_headroo... |

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
