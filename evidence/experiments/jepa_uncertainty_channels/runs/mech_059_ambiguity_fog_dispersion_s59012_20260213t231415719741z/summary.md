# Run Summary: mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z

## Scenario
- claim_id: `MECH-059`
- scenario: `ambiguity_fog_dispersion`
- condition: ambiguity-heavy fog with adversarial confidence shaping under dispersion
- seed: `59012`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- ood_perturbation_intensity: `0.914032`
- ambiguity_density: `0.8681`
- calibration_degradation_slope: `0.340295`
- uncertainty_metric_gaming_gap: `0.35288`
- abstention_reliability: `0.086089`
- seed_used: `59012`

## Failure Signatures
- `mech059:calibration_slope_break`
- `mech059:uncertainty_metric_gaming_detected`
- `mech059:abstention_reliability_collapse`
