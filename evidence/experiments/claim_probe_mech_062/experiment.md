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

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
No recent FAIL runs. Keep monitoring key stop metrics.
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
