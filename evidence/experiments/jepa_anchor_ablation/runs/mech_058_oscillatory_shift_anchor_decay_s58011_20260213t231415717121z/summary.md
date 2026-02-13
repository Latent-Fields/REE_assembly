# Run Summary: mech_058_oscillatory_shift_anchor_decay_s58011_20260213t231415717121z

## Scenario
- claim_id: `MECH-058`
- scenario: `oscillatory_shift_anchor_decay`
- condition: oscillatory drift with stale replay windows stressing EMA anchor
- seed: `58011`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Key Metrics
- nonstationary_shift_magnitude: `0.973014`
- replay_stress_pressure: `0.794705`
- ema_anchor_separation_margin: `0.173387`
- anchor_drift_rate: `0.800013`
- latent_collapse_index: `0.736406`
- seed_used: `58011`

## Failure Signatures
- `mech058:anchor_separation_collapse`
- `mech058:ema_drift_under_shift`
- `mech058:latent_cluster_collapse`
