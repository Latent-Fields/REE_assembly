# Experiment: tri_loop_arbitration_policy

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T150650Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q016:tri_loop_alignment_break
- `2026-02-21T150650Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q016:tri_loop_alignment_break, q016:tri_loop_override_spike
- `2026-02-21T150650Z_tri-loop-arbitration-policy_seed11_weighted_merge_toyenv_internal_minimal` at `2026-02-21T15:06:50Z` signatures: q016:tri_loop_alignment_break

Recurring signatures:
- `q016:tri_loop_alignment_break` occurred in 36 FAIL run(s); latest `2026-02-21T150650Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_override_spike` occurred in 11 FAIL run(s); latest `2026-02-21T150650Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_conflict_spike` occurred in 1 FAIL run(s); latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q016:tri_loop_alignment_break` (36 FAIL run(s), latest `2026-02-21T150650Z_tri-loop-arbitration-policy_seed47_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_override_spike` (11 FAIL run(s), latest `2026-02-21T150650Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_conflict_spike` (1 FAIL run(s), latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
