# Experiment: control_axis_ablation

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T150650Z_control-axis-ablation_seed47_reduced_axis_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q017:control_axis_stability_drop, q017:control_axis_entropy_collapse
- `2026-02-21T150650Z_control-axis-ablation_seed29_reduced_axis_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q017:control_axis_stability_drop, q017:control_axis_policy_loss_spike, q017:control_axis_entropy_collapse
- `2026-02-21T150650Z_control-axis-ablation_seed11_reduced_axis_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q017:control_axis_stability_drop, q017:control_axis_policy_loss_spike, q017:control_axis_entropy_collapse

Recurring signatures:
- `q017:control_axis_stability_drop` occurred in 36 FAIL run(s); latest `2026-02-21T150650Z_control-axis-ablation_seed47_reduced_axis_toyenv_internal_minimal`
- `q017:control_axis_entropy_collapse` occurred in 36 FAIL run(s); latest `2026-02-21T150650Z_control-axis-ablation_seed47_reduced_axis_toyenv_internal_minimal`
- `q017:control_axis_policy_loss_spike` occurred in 25 FAIL run(s); latest `2026-02-21T150650Z_control-axis-ablation_seed29_reduced_axis_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q017:control_axis_stability_drop` (36 FAIL run(s), latest `2026-02-21T150650Z_control-axis-ablation_seed47_reduced_axis_toyenv_internal_minimal`).
- [ ] Investigate signature `q017:control_axis_entropy_collapse` (36 FAIL run(s), latest `2026-02-21T150650Z_control-axis-ablation_seed47_reduced_axis_toyenv_internal_minimal`).
- [ ] Investigate signature `q017:control_axis_policy_loss_spike` (25 FAIL run(s), latest `2026-02-21T150650Z_control-axis-ablation_seed29_reduced_axis_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
