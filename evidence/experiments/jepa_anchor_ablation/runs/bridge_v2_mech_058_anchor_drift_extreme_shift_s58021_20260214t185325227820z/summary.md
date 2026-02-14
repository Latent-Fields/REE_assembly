# Run Summary: MECH-058

## Scenario
- claim_id: `MECH-058`
- scenario: `anchor_drift_extreme_shift`
- condition: extreme regime shift targeting EMA anchor stability
- seed: `58021`
- severity: `0.9`

## Outcome
- status: `FAIL`
- evidence_direction: `weakens`

## Metrics
- ema_anchor_drift: `0.533431`
- latent_cluster_collapse_rate: `0.435045`
- anchor_separation_score: `0.490168`

## Failure Signatures
- `mech058:ema_drift_under_shift`
- `mech058:latent_cluster_collapse`
- `mech058:anchor_separation_collapse`
