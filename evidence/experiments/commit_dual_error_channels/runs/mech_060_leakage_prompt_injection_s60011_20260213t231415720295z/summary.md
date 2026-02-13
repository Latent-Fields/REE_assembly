# Run Summary: mech_060_leakage_prompt_injection_s60011_20260213t231415720295z

## Scenario
- claim_id: `MECH-060`
- scenario: `leakage_prompt_injection`
- condition: adversarial prompt leakage targeting pre/post commit contamination
- seed: `60011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- adversarial_leakage_intensity: `0.776627`
- precommit_channel_contamination_rate: `0.413054`
- postcommit_channel_contamination_rate: `0.363712`
- split_attribution_reliability: `0.5754`
- dual_channel_isolation_gap: `0.414633`
- seed_used: `60011`

## Failure Signatures
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
