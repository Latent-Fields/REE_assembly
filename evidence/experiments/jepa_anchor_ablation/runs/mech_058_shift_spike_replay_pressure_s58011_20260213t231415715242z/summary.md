# Run Summary: mech_058_shift_spike_replay_pressure_s58011_20260213t231415715242z

## Scenario
- claim_id: `MECH-058`
- scenario: `shift_spike_replay_pressure`
- condition: abrupt non-stationary regime shift with replay skew pressure
- seed: `58011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- nonstationary_shift_magnitude: `0.850227`
- replay_stress_pressure: `0.800092`
- ema_anchor_separation_margin: `0.140538`
- anchor_drift_rate: `0.717639`
- latent_collapse_index: `0.689207`
- seed_used: `58011`

## Failure Signatures
- `mech058:anchor_separation_collapse`
- `mech058:ema_drift_under_shift`
- `mech058:latent_cluster_collapse`
