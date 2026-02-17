# Experiment: jepa_anchor_ablation

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-17T225312Z_jepa-anchor-ablation_seed89_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: mech058:anchor_separation_collapse
- `2026-02-17T225312Z_jepa-anchor-ablation_seed71_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: mech058:anchor_separation_collapse
- `2026-02-17T225312Z_jepa-anchor-ablation_seed53_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: mech058:anchor_separation_collapse

Recurring signatures:
- `mech058:anchor_separation_collapse` occurred in 36 FAIL run(s); latest `2026-02-17T225312Z_jepa-anchor-ablation_seed89_ema_anchor_off_toyenv_internal_minimal`
- `mech058:ema_drift_under_shift` occurred in 18 FAIL run(s); latest `2026-02-17T225246Z_jepa-anchor-ablation_seed29_ema_anchor_off_toyenv_internal_minimal`
- `mech058:latent_cluster_collapse` occurred in 10 FAIL run(s); latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`
- `threshold:latent_prediction_error_mean` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`
- `threshold:latent_prediction_error_p95` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`
- `threshold:latent_rollout_consistency_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`
- `threshold:e1_e2_timescale_separation_ratio` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`
- `threshold:representation_drift_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`

Suggested design TODOs:
- [ ] Investigate signature `mech058:anchor_separation_collapse` (36 FAIL run(s), latest `2026-02-17T225312Z_jepa-anchor-ablation_seed89_ema_anchor_off_toyenv_internal_minimal`).
- [ ] Investigate signature `mech058:ema_drift_under_shift` (18 FAIL run(s), latest `2026-02-17T225246Z_jepa-anchor-ablation_seed29_ema_anchor_off_toyenv_internal_minimal`).
- [ ] Investigate signature `mech058:latent_cluster_collapse` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_prediction_error_p95` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_rollout_consistency_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
