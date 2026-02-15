# Experiment: tri_loop_arbitration_policy

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T145638Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal` at `2026-02-15T14:56:38Z` signatures: q016:tri_loop_alignment_break
- `2026-02-15T145638Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal` at `2026-02-15T14:56:38Z` signatures: q016:tri_loop_alignment_break, q016:tri_loop_override_spike
- `2026-02-15T145638Z_tri-loop-arbitration-policy_seed11_weighted_merge_toyenv_internal_minimal` at `2026-02-15T14:56:38Z` signatures: q016:tri_loop_alignment_break

Recurring signatures:
- `q016:tri_loop_alignment_break` occurred in 12 FAIL run(s); latest `2026-02-15T145638Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_override_spike` occurred in 4 FAIL run(s); latest `2026-02-15T145638Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q016:tri_loop_alignment_break` (12 FAIL run(s), latest `2026-02-15T145638Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_override_spike` (4 FAIL run(s), latest `2026-02-15T145638Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
