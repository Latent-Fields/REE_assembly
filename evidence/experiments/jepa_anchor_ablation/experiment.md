# Experiment: jepa_anchor_ablation

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `exp_0002_20260215T173859495032Z` at `2026-02-15T17:38:59.495032Z` signatures: none
- `exp_0013_20260215T153519635646Z` at `2026-02-15T15:35:19.635646Z` signatures: none
- `exp_0015_20260215T095120253293Z` at `2026-02-15T09:51:20.253293Z` signatures: none

Recurring signatures:
- `mech058:ema_drift_under_shift` occurred in 10 FAIL run(s); latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`
- `mech058:latent_cluster_collapse` occurred in 10 FAIL run(s); latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`
- `mech058:anchor_separation_collapse` occurred in 9 FAIL run(s); latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`

Suggested design TODOs:
- [ ] Investigate signature `mech058:ema_drift_under_shift` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:latent_cluster_collapse` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:anchor_separation_collapse` (9 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
