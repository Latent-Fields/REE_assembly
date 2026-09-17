# Pending Experiment Review

Generated: `2026-09-17T10:57:09Z`  
Last review: `2026-09-16T13:45:48Z`  
Pending: **7** item(s) -- 2 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 2 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_935a_mech266_margin_normalised_cap_rule_20260916T095809Z_v3` | 2026-09-16T09:58 | MECH-266, SD-032a | — |
| `v3_exq_1043_mech537_communication_subspace_routing_20260916T111630Z_v3` | 2026-09-16T11:16 | MECH-537 | — |
| `v3_exq_1044_hippocampal_assay_a_access_mechanism_20260916T141717Z_v3` | 2026-09-16T14:17 | (no claim tags) | — |
| `v3_exq_1046_sd082_consequence_trained_readout_20260917T053813Z_v3` | 2026-09-17T05:38 | SD-082 | — |
| `v3_exq_1048_mech017_reality_consolidation_replay_vs_budget_matched_20260917T102244Z_v3` | 2026-09-17T10:22 | MECH-017 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_1038a_arc131_coalition_recruitment_commensurability_probe_20260917T001717Z_v3` | 2026-09-17T00:17 | ARC-131 |
| `v3_exq_1047_mech482_amplified_readout_ladder_20260917T025403Z_v3` | 2026-09-17T02:54 | MECH-482 |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_1047_mech482_amplified_readout_ladder_20260917T025403Z_v3` | PASS | deficit_readout_magnitude_limited |
| `v3_exq_1046_sd082_consequence_trained_readout_20260917T053813Z_v3` | FAIL | h1_weakened_training_reduced_readout_consequence |

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
