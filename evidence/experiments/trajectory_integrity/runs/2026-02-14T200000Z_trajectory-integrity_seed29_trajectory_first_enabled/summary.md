# Experiment Run Summary

## Scenario
- claim_id: `MECH-056`
- experiment_type: `trajectory_integrity`
- condition: `trajectory_first_enabled`
- run_id: `2026-02-14T200000Z_trajectory-integrity_seed29_trajectory_first_enabled`
- timestamp_utc: `2026-02-14T20:00:00Z`
- seed: `29`
- seed_cohort: `11`, `29`, `47`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- ledger_edit_detected_count: 0.000000
- explanation_policy_divergence_rate: 0.030353
- domination_lock_in_events: 0.000000
- trajectory_constraint_activation_rate: 0.808949
- representational_distortion_rate: 0.024683

## PASS/FAIL Thresholds
- `ledger_edit_detected_count == 0` (observed: `0.000000`)
- `explanation_policy_divergence_rate <= 0.05` (observed: `0.030353`)
- `domination_lock_in_events == 0` (observed: `0.000000`)

## Stop Criteria Mirror (MECH-056)
- status mirrors REE_assembly criteria:
- `ledger_edit_detected_count == 0`
- `explanation_policy_divergence_rate <= 0.05`
- `domination_lock_in_events == 0`

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
