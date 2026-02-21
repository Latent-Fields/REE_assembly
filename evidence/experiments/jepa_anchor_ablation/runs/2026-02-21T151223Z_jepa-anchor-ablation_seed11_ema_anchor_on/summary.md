# Experiment Run Summary

## Scenario
- claim_id: `MECH-058`
- experiment_type: `jepa_anchor_ablation`
- condition: `ema_anchor_on`
- run_id: `2026-02-21T151223Z_jepa-anchor-ablation_seed11_ema_anchor_on`
- timestamp_utc: `2026-02-21T15:12:23Z`
- seed: `11`
- seed_cohort: `11`, `29`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- latent_prediction_error_mean: 0.122249
- latent_prediction_error_p95: 0.225988
- latent_rollout_consistency_rate: 0.897066
- e1_e2_timescale_separation_ratio: 2.006285
- representation_drift_rate: 0.019697

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.2` (observed: `0.122249`)
- `latent_prediction_error_p95 <= 0.35` (observed: `0.225988`)
- `latent_rollout_consistency_rate >= 0.8` (observed: `0.897066`)
- `e1_e2_timescale_separation_ratio >= 1.8` (observed: `2.006285`)
- `representation_drift_rate <= 0.04` (observed: `0.019697`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
