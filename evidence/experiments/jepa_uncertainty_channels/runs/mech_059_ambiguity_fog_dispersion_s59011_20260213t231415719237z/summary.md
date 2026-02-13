# Run Summary: mech_059_ambiguity_fog_dispersion_s59011_20260213t231415719237z

## Scenario
- claim_id: `MECH-059`
- scenario: `ambiguity_fog_dispersion`
- condition: ambiguity-heavy fog with adversarial confidence shaping under dispersion
- seed: `59011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- ood_perturbation_intensity: `0.899894`
- ambiguity_density: `0.71455`
- calibration_degradation_slope: `0.318095`
- uncertainty_metric_gaming_gap: `0.356395`
- abstention_reliability: `0.126573`
- seed_used: `59011`

## Failure Signatures
- `mech059:calibration_slope_break`
- `mech059:uncertainty_metric_gaming_detected`
- `mech059:abstention_reliability_collapse`
