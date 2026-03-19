# Experiment: claim_probe_mech_058

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `20260317T232028Z_v3_exq_019_timescale_v3_v3` at `2026-03-17T23:20:28Z` signatures: none
- `20260315T045933_e1_e2_terrain_timescale_v2` at `2026-03-15T04:59:33.847875+00:00` signatures: v2_verdict_fail:e1_e2_terrain_timescale
- `20260226T205244_claim_probe_mech_058_ree_v1_minimal` at `2026-02-26T20:52:44Z` signatures: mech058:latent_stability_criterion_not_met_at_v1_minimal_scale

Recurring signatures:
- `mech058:anchor_separation_collapse` occurred in 12 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-058_seed47_ema_anchor_off_toyenv_internal_minimal`
- `mech058:ema_drift_under_shift` occurred in 3 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-058_seed29_ema_anchor_off_toyenv_internal_minimal`
- `mech058:latent_stability_criterion_not_met_at_v1_minimal_scale` occurred in 1 FAIL run(s); latest `20260226T205244_claim_probe_mech_058_ree_v1_minimal`
- `v2_verdict_fail:e1_e2_terrain_timescale` occurred in 1 FAIL run(s); latest `20260315T045933_e1_e2_terrain_timescale_v2`

Suggested design TODOs:
- [ ] Investigate signature `mech058:anchor_separation_collapse` (12 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-058_seed47_ema_anchor_off_toyenv_internal_minimal`).
- [ ] Investigate signature `mech058:ema_drift_under_shift` (3 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-058_seed29_ema_anchor_off_toyenv_internal_minimal`).
- [ ] Investigate signature `mech058:latent_stability_criterion_not_met_at_v1_minimal_scale` (1 FAIL run(s), latest `20260226T205244_claim_probe_mech_058_ree_v1_minimal`).
- [ ] Investigate signature `v2_verdict_fail:e1_e2_terrain_timescale` (1 FAIL run(s), latest `20260315T045933_e1_e2_terrain_timescale_v2`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
