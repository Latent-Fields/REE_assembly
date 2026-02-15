# Experiment Run Summary

## Scenario
- claim_id: `MECH-060`
- experiment_type: `commit_dual_error_channels`
- condition: `single_error_stream`
- run_id: `2026-02-14T200000Z_commit-dual-error-channels_seed11_single_error_stream`
- timestamp_utc: `2026-02-14T20:00:00Z`
- seed: `11`
- seed_cohort: `11`, `29`, `47`

## Outcome
- status: **FAIL**
- evidence_direction: `weakens`

## Key Metrics
- pre_commit_error_signal_to_noise: 1.264688
- post_commit_error_attribution_gain: 0.174138
- cross_channel_leakage_rate: 0.227950
- commitment_reversal_rate: 0.173721

## PASS/FAIL Thresholds
- `pre_commit_error_signal_to_noise >= 1.8` (observed: `1.264688`)
- `post_commit_error_attribution_gain >= 0.3` (observed: `0.174138`)
- `cross_channel_leakage_rate <= 0.15` (observed: `0.227950`)
- `commitment_reversal_rate <= 0.1` (observed: `0.173721`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `weakens`.
