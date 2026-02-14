# Run Summary: MECH-059

## Scenario
- claim_id: `MECH-059`
- scenario: `adversarial_uncertainty_gaming`
- condition: adversarial confidence shaping under high ambiguity
- seed: `59022`
- severity: `0.88`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Metrics
- calibration_slope: `0.217172`
- uncertainty_metric_gaming_rate: `0.206606`
- abstention_reliability: `0.571049`

## Failure Signatures
- `mech059:calibration_slope_break`
- `mech059:uncertainty_metric_gaming_detected`
