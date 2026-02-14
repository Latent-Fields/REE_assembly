# Experiment: jepa_anchor_ablation

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z` at `2026-02-13T23:14:15.717818Z` signatures: mech058:anchor_separation_collapse, mech058:ema_drift_under_shift, mech058:latent_cluster_collapse
- `mech_058_oscillatory_shift_anchor_decay_s58011_20260213t231415717121z` at `2026-02-13T23:14:15.717321Z` signatures: mech058:anchor_separation_collapse, mech058:ema_drift_under_shift, mech058:latent_cluster_collapse
- `mech_058_shift_spike_replay_pressure_s58012_20260213t231415716577z` at `2026-02-13T23:14:15.716794Z` signatures: mech058:ema_drift_under_shift, mech058:latent_cluster_collapse

Recurring signatures:
- `mech058:ema_drift_under_shift` occurred in 4 FAIL run(s); latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`
- `mech058:latent_cluster_collapse` occurred in 4 FAIL run(s); latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`
- `mech058:anchor_separation_collapse` occurred in 3 FAIL run(s); latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`

Suggested design TODOs:
- [ ] Investigate signature `mech058:ema_drift_under_shift` (4 FAIL run(s), latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`).
- [ ] Investigate signature `mech058:latent_cluster_collapse` (4 FAIL run(s), latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`).
- [ ] Investigate signature `mech058:anchor_separation_collapse` (3 FAIL run(s), latest `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
