# Pending Experiment Review

Generated: `2026-09-09T01:58:57Z`  
Last review: `2026-09-08T15:28:35Z`  
Pending: **5** item(s) -- 3 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 run(s) with recorded (non-gating) preconditions

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3` | 2026-09-08T20:28 | MECH-465 | — |
| `v3_exq_822f_sd082_candidate_discriminating_init_head_control_20260908T231145Z_v3` | 2026-09-08T23:11 | SD-078, SD-082 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1013_sd031_shortcut_vs_model_portfolio_20260908T190906Z_v3` | 2026-09-08T19:09 | SD-031 |
| `v3_exq_1011_arc021_h3_submargin_paired_ci_20260908T201117Z_v3` | 2026-09-08T20:11 | ARC-021, MECH-069 |
| `v3_exq_1014_ext002_lineage_e3_latching_repertoire_spike_20260908T223415Z_v3` | 2026-09-08T22:34 | (no claim tags) |

## Recorded (non-gating) preconditions

**No action is required on account of this section.** These runs declare a readiness finding in `interpretation.recorded_preconditions[]` that did NOT hold -- but the author deliberately did not gate the run on it, because the run's premise survives the finding (e.g. a shared symmetric prior that biases every arm identically, or a readout-side question with an unaffected control). The entries are kept out of the adjudicating `interpretation.preconditions[]` on purpose: that list is read flat and arm-blind, so an entry there would return a whole-run `precondition_unmet` and bury a valid result. Each run's own `preconditions_scope_note` states the reasoning. Read this as an audit trail when interpreting the run -- it is NOT an adjudication flag, does not block a governance action, and does not exclude the run from scoring. See evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.

| Run ID | Status | Recorded precondition(s) not met | Scope note |
|--------|--------|----------------------------------|------------|
| `v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3` | FAIL | COLD/s0::cold_reproduces_spike_dispersion_band, COLD/s0::p1_all_levels_in_band, COLD/s1::p1_all_levels_in_band, COLD/s3::p1_all_levels_in_band, PHASED400/s1::p1_all_levels_in_band, WARM200/s0::p1_all_levels_in_band, WARM200/s1::p1_all_levels_in_band, WARM400/s0::p1_all_levels_in_band, WARM400/s1::p1_all_levels_in_band, WARM800/s1::p1_all_levels_in_band | — |

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
