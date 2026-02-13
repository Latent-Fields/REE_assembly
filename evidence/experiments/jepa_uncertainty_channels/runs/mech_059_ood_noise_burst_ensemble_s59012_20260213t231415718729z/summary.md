# Run Summary: mech_059_ood_noise_burst_ensemble_s59012_20260213t231415718729z

## Scenario
- claim_id: `MECH-059`
- scenario: `ood_noise_burst_ensemble`
- condition: OOD perturbation bursts with high ambiguity under ensemble uncertainty
- seed: `59012`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- ood_perturbation_intensity: `0.681768`
- ambiguity_density: `0.64699`
- calibration_degradation_slope: `0.269204`
- uncertainty_metric_gaming_gap: `0.277749`
- abstention_reliability: `0.323167`
- seed_used: `59012`

## Failure Signatures
- `mech059:calibration_slope_break`
- `mech059:uncertainty_metric_gaming_detected`
- `mech059:abstention_reliability_collapse`
