# Run Summary: mech_060_memory_patch_cross_talk_s60011_20260213t231415722024z

## Scenario
- claim_id: `MECH-060`
- scenario: `memory_patch_cross_talk`
- condition: delayed memory patch leakage inducing cross-channel attribution drift
- seed: `60011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- adversarial_leakage_intensity: `0.938872`
- precommit_channel_contamination_rate: `0.467076`
- postcommit_channel_contamination_rate: `0.387938`
- split_attribution_reliability: `0.516322`
- dual_channel_isolation_gap: `0.364355`
- seed_used: `60011`

## Failure Signatures
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
- `mech060:attribution_reliability_break`
