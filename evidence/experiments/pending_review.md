# Pending Experiment Review

Generated: `2026-09-08T07:15:26Z`  
Last review: `2026-09-06T16:56:48Z`  
Pending: **6** item(s) -- 6 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication; 1 run(s) with recorded (non-gating) preconditions

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3` | 2026-09-06T19:51 | (no claim tags) |
| `v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3` | 2026-09-07T07:23 | MECH-535, MECH-536 |
| `v3_exq_970a_contextmemory_write_content_h1_mi_instrument_20260907T152212Z_v3` | 2026-09-07T15:22 | (no claim tags) |
| `v3_exq_972a_sd070_write_stream_heldout_linear_probe_20260907T162343Z_v3` | 2026-09-07T16:23 | SD-070 |
| `v3_exq_1009_mech267_elite_channel_ceiling_spike_20260907T171115Z_v3` | 2026-09-07T17:11 | (no claim tags) |
| `v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3` | 2026-09-07T23:38 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_1009_mech267_elite_channel_ceiling_spike_20260907T171115Z_v3` | PASS | elite_channel_ceiling_confirmed_all_benches | **vacuous_pass** |

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
