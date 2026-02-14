# Experiment Run Summary

## Scenario
- claim_id: `MECH-060`
- experiment_type: `commit_dual_error_channels`
- condition: `pre_post_split_streams`
- run_id: `2026-02-14T030000Z_commit-dual-error-channels_seed11_pre_post_split_streams`
- timestamp_utc: `2026-02-14T03:00:00Z`
- seed: `11`
- seed_cohort: `11`, `29`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- pre_commit_error_signal_to_noise: 2.441057
- post_commit_error_attribution_gain: 0.403933
- cross_channel_leakage_rate: 0.084424
- commitment_reversal_rate: 0.066655

## PASS/FAIL Thresholds
- `pre_commit_error_signal_to_noise >= 1.8` (observed: `2.441057`)
- `post_commit_error_attribution_gain >= 0.3` (observed: `0.403933`)
- `cross_channel_leakage_rate <= 0.15` (observed: `0.084424`)
- `commitment_reversal_rate <= 0.1` (observed: `0.066655`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
