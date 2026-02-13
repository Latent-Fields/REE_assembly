# Run Summary: mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z

## Scenario
- claim_id: `MECH-060`
- scenario: `memory_patch_cross_talk`
- condition: delayed memory patch leakage inducing cross-channel attribution drift
- seed: `60012`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- adversarial_leakage_intensity: `0.95341`
- precommit_channel_contamination_rate: `0.52847`
- postcommit_channel_contamination_rate: `0.442325`
- split_attribution_reliability: `0.460305`
- dual_channel_isolation_gap: `0.323041`
- seed_used: `60012`

## Failure Signatures
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
- `mech060:attribution_reliability_break`
