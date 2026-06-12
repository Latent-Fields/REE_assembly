# Pending Experiment Review

Generated: `2026-06-12T01:47:25Z`  
Last review: `2026-06-12T01:38:58Z`  
Pending: **9** item(s) -- 0 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 9 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| FAIL | `v3_exq_670_inv048_pharm_sleep_20260611T211811Z_v3` | v3_exq_670_inv048_pharmacological_sleep_disruption_equivalence | V3-EXQ-670 | weakens |
| FAIL | `v3_exq_671_mech025b_precision_responsibility_20260611T215625Z_v3` | v3_exq_671_mech025b_precision_responsibility | V3-EXQ-671 | mixed |
| FAIL | `v3_exq_485f_sd033b_trained_ofc_head_behavioural_20260611T221413Z_v3` | v3_exq_485f_sd033b_trained_ofc_head_behavioural | V3-EXQ-485f | weakens |
| FAIL | `v3_exq_666b_arc063_crf_availability_maintenance_readiness_fracgate_20260612T005245Z_v3` | v3_exq_666b_arc063_crf_availability_maintenance_readiness_fracgate | V3-EXQ-666b | non_contributory |
| FAIL | `v3_exq_590b_mech314a_novelty_goldilocks_20260611T211806Z_v3` | v3_exq_590b_mech314a_novelty_goldilocks | V3-EXQ-590b | does_not_support |
| FAIL | `v3_exq_603o_escape_affordance_bridge_behavioural_redesign_20260611T213609Z_v3` | v3_exq_603o_escape_affordance_bridge_behavioural_redesign | V3-EXQ-603o | non_contributory |
| FAIL | `v3_exq_514n_sd049_phase2_mech229_object_bound_wanting_liking_20260611T224339Z_v3` | v3_exq_514n_sd049_phase2_mech229_object_bound_wanting_liking | V3-EXQ-514n | non_contributory |
| FAIL | `v3_exq_569g_gapa_routerange_matched_entropy_falsifier_20260611T224954Z_v3` | v3_exq_569g_gapa_routerange_matched_entropy_falsifier | V3-EXQ-569g | weakens |
| FAIL | `v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260611T230231Z_v3` | v3_exq_673_mech171_vicious_cycle_sleep_disruption | ? | does_not_support |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
