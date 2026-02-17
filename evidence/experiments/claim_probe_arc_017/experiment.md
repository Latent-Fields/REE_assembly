# Experiment: claim_probe_arc_017

## What it tests

- Whether REE keeps exteroceptive, interoceptive, proprioceptive, nociceptive, and reality-coherence lanes structurally distinct.
- Whether exteroceptive payload typing (`OBS`/`INS`) prevents direct writes into policy/identity/capability stores.
- Whether reality-coherence conflicts are routed into commitment suppression instead of being ignored as ordinary noise.

## Failure modes it detects

- `stream_tag_collapse`
- `world_to_policy_direct_path`
- `world_to_identity_direct_path`
- `reality_conflict_not_routed`
- `harm_or_veto_channel_overwrite_by_language`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
No recent FAIL runs. Keep monitoring key stop metrics.
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
