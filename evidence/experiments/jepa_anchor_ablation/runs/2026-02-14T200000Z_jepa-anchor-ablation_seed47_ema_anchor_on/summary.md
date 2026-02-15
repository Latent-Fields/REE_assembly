# Experiment Run Summary

## Scenario
- claim_id: `MECH-058`
- experiment_type: `jepa_anchor_ablation`
- condition: `ema_anchor_on`
- run_id: `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_on`
- timestamp_utc: `2026-02-14T20:00:00Z`
- seed: `47`
- seed_cohort: `11`, `29`, `47`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- latent_prediction_error_mean: 0.123590
- latent_prediction_error_p95: 0.244863
- latent_rollout_consistency_rate: 0.902403
- e1_e2_timescale_separation_ratio: 2.075548
- representation_drift_rate: 0.020339

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.2` (observed: `0.123590`)
- `latent_prediction_error_p95 <= 0.35` (observed: `0.244863`)
- `latent_rollout_consistency_rate >= 0.8` (observed: `0.902403`)
- `e1_e2_timescale_separation_ratio >= 1.8` (observed: `2.075548`)
- `representation_drift_rate <= 0.04` (observed: `0.020339`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
