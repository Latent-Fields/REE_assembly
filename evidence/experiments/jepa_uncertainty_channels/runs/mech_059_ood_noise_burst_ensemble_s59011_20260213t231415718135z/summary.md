# Run Summary: mech_059_ood_noise_burst_ensemble_s59011_20260213t231415718135z

## Scenario
- claim_id: `MECH-059`
- scenario: `ood_noise_burst_ensemble`
- condition: OOD perturbation bursts with high ambiguity under ensemble uncertainty
- seed: `59011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- ood_perturbation_intensity: `0.72021`
- ambiguity_density: `0.660451`
- calibration_degradation_slope: `0.245766`
- uncertainty_metric_gaming_gap: `0.306319`
- abstention_reliability: `0.299508`
- seed_used: `59011`

## Failure Signatures
- `mech059:calibration_slope_break`
- `mech059:uncertainty_metric_gaming_detected`
- `mech059:abstention_reliability_collapse`
