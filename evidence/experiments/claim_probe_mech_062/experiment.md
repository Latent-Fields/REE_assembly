# Experiment: claim_probe_mech_062

## What it tests

- Whether tri-loop commitment gating keeps motor, cognitive-set, and motivational commitments partially independent.
- Whether associative-gate commitment requires provenance/authority consistency before task-set lock-in.
- Whether motor-gate execution stays blocked when veto or capability checks fail, even if upstream loops favor commit.

## Failure modes it detects

- `cross_gate_coupling_collapse`
- `associative_gate_authority_spoof_acceptance`
- `motor_gate_executes_without_veto_clearance`
- `arbitration_without_commit_trace`
- `loop_specific_threshold_leakage`

## Minimum metrics to emit

- `tri_loop_gate_conflict_rate`
- `tri_loop_policy_alignment_rate`
- `tri_loop_arbitration_override_rate`
- `tri_loop_trace_coverage_rate`
- `fatal_error_count`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T130142Z_claim-probe-mech-062_seed47_weighted_merge_toyenv_internal_minimal` at `2026-02-21T13:01:42Z` signatures: q016:tri_loop_alignment_break
- `2026-02-21T130142Z_claim-probe-mech-062_seed29_weighted_merge_toyenv_internal_minimal` at `2026-02-21T13:01:42Z` signatures: q016:tri_loop_alignment_break, q016:tri_loop_override_spike
- `2026-02-21T130142Z_claim-probe-mech-062_seed11_weighted_merge_toyenv_internal_minimal` at `2026-02-21T13:01:42Z` signatures: q016:tri_loop_alignment_break

Recurring signatures:
- `q016:tri_loop_alignment_break` occurred in 9 FAIL run(s); latest `2026-02-21T130142Z_claim-probe-mech-062_seed47_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_override_spike` occurred in 2 FAIL run(s); latest `2026-02-21T130142Z_claim-probe-mech-062_seed29_weighted_merge_toyenv_internal_minimal`
- `q016:tri_loop_conflict_spike` occurred in 1 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-mech-062_seed89_weighted_merge_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `q016:tri_loop_alignment_break` (9 FAIL run(s), latest `2026-02-21T130142Z_claim-probe-mech-062_seed47_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_override_spike` (2 FAIL run(s), latest `2026-02-21T130142Z_claim-probe-mech-062_seed29_weighted_merge_toyenv_internal_minimal`).
- [ ] Investigate signature `q016:tri_loop_conflict_spike` (1 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-mech-062_seed89_weighted_merge_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
