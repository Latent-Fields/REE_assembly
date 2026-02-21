# Experiment Run Summary

## Scenario
- claim_id: `MECH-058`
- experiment_type: `jepa_anchor_ablation`
- condition: `ema_anchor_off`
- run_id: `2026-02-21T151223Z_jepa-anchor-ablation_seed29_ema_anchor_off`
- timestamp_utc: `2026-02-21T15:12:23Z`
- seed: `29`
- seed_cohort: `11`, `29`

## Outcome
- status: **FAIL**
- evidence_direction: `weakens`

## Key Metrics
- latent_prediction_error_mean: 0.234157
- latent_prediction_error_p95: 0.364277
- latent_rollout_consistency_rate: 0.765659
- e1_e2_timescale_separation_ratio: 1.462288
- representation_drift_rate: 0.045538

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.2` (observed: `0.234157`)
- `latent_prediction_error_p95 <= 0.35` (observed: `0.364277`)
- `latent_rollout_consistency_rate >= 0.8` (observed: `0.765659`)
- `e1_e2_timescale_separation_ratio >= 1.8` (observed: `1.462288`)
- `representation_drift_rate <= 0.04` (observed: `0.045538`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `weakens`.
