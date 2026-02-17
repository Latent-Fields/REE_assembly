# Experiment: claim_probe_q_017

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: q017:control_axis_stability_drop, q017:control_axis_policy_loss_spike, q017:control_axis_entropy_collapse
- `2026-02-17T225311Z_claim-probe-q-017_seed71_reduced_axis_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: q017:control_axis_stability_drop, q017:control_axis_policy_loss_spike, q017:control_axis_entropy_collapse
- `2026-02-17T225311Z_claim-probe-q-017_seed53_reduced_axis_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: q017:control_axis_stability_drop, q017:control_axis_policy_loss_spike, q017:control_axis_entropy_collapse

Recurring signatures:
- `q017:control_axis_stability_drop` occurred in 6 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`
- `q017:control_axis_entropy_collapse` occurred in 6 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`
- `q017:control_axis_policy_loss_spike` occurred in 5 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q017:control_axis_stability_drop` (6 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`).
- [ ] Investigate signature `q017:control_axis_entropy_collapse` (6 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`).
- [ ] Investigate signature `q017:control_axis_policy_loss_spike` (5 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-q-017_seed89_reduced_axis_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
