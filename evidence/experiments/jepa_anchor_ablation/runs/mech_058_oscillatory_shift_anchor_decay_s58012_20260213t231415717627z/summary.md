# Run Summary: mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z

## Scenario
- claim_id: `MECH-058`
- scenario: `oscillatory_shift_anchor_decay`
- condition: oscillatory drift with stale replay windows stressing EMA anchor
- seed: `58012`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- nonstationary_shift_magnitude: `0.951956`
- replay_stress_pressure: `0.840037`
- ema_anchor_separation_margin: `0.115448`
- anchor_drift_rate: `0.781724`
- latent_collapse_index: `0.703293`
- seed_used: `58012`

## Failure Signatures
- `mech058:anchor_separation_collapse`
- `mech058:ema_drift_under_shift`
- `mech058:latent_cluster_collapse`
