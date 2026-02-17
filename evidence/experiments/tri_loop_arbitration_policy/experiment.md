# Experiment: tri_loop_arbitration_policy

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: q016:tri_loop_conflict_spike, q016:tri_loop_alignment_break
- `2026-02-17T225312Z_tri-loop-arbitration-policy_seed71_weighted_merge_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: q016:tri_loop_alignment_break
- `2026-02-17T225312Z_tri-loop-arbitration-policy_seed53_weighted_merge_toyenv_internal_minimal` at `2026-02-17T22:53:12Z` signatures: q016:tri_loop_alignment_break

Recurring signatures:
- `q016:tri_loop_alignment_break` occurred in 30 FAIL run(s); latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_override_spike` occurred in 9 FAIL run(s); latest `2026-02-17T225246Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_conflict_spike` occurred in 1 FAIL run(s); latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q016:tri_loop_alignment_break` (30 FAIL run(s), latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_override_spike` (9 FAIL run(s), latest `2026-02-17T225246Z_tri-loop-arbitration-policy_seed29_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_conflict_spike` (1 FAIL run(s), latest `2026-02-17T225312Z_tri-loop-arbitration-policy_seed89_weighted_merge_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
