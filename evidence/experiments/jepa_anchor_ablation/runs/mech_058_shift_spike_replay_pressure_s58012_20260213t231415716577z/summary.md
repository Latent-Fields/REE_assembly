# Run Summary: mech_058_shift_spike_replay_pressure_s58012_20260213t231415716577z

## Scenario
- claim_id: `MECH-058`
- scenario: `shift_spike_replay_pressure`
- condition: abrupt non-stationary regime shift with replay skew pressure
- seed: `58012`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- nonstationary_shift_magnitude: `0.726573`
- replay_stress_pressure: `0.642396`
- ema_anchor_separation_margin: `0.38099`
- anchor_drift_rate: `0.595522`
- latent_collapse_index: `0.619415`
- seed_used: `58012`

## Failure Signatures
- `mech058:ema_drift_under_shift`
- `mech058:latent_cluster_collapse`
