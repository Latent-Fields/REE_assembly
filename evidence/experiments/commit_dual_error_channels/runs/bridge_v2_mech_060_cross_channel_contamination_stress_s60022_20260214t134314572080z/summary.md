# Run Summary: MECH-060

## Scenario
- claim_id: `MECH-060`
- scenario: `cross_channel_contamination_stress`
- condition: high cross-talk pressure to contaminate post-commit attribution
- seed: `60022`
- severity: `0.86`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Metrics
- precommit_channel_contamination_rate: `0.385037`
- postcommit_channel_contamination_rate: `0.357645`
- attribution_reliability_score: `0.677946`

## Failure Signatures
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
- `mech060:attribution_reliability_break`
