# V3-EXQ-096 -- Full V3 Integration Benchmark

**Status:** FAIL
**Claims:** SD-005, ARC-016, MECH-094, MECH-090, SD-006, ARC-007, MECH-089, MECH-093

## Protocol

Four-phase full-stack integration test. All V3 components active simultaneously:
E1, E2, E3, HippocampalModule, ResidueField, MultiRateClock, ThetaBuffer, BetaGate,
SD-005 SplitEncoder, SD-010/011 harm streams.

Phase 1: Terrain familiarization (500 eps, random policy)
Phase 2: E3 calibration (300 eps, stratified harm buffers)
Phase 3: Full agent evaluation (150 eps, agent policy via act_with_split_obs)
Phase 4: Behavioral edge cases (50 eps x4 scenarios)

## Integration Health (E1/E2 convergence)

| Metric | Value | Threshold |
|--------|-------|-----------|
| E1 final loss | 0.0007 | < 0.20 |

## Sense of Self (SD-005)

| Metric | Value |
|--------|-------|
| R2(z_self -> body_obs) | 0.9935 |
| R2(z_world -> body_obs) | 0.4616 |
| Self-other gap | 0.5319 |
| z_self D_eff mean | 23.52 |

## Moral Agency

| Metric | Value |
|--------|-------|
| Harm ROC AUC | 0.6491 |
| Harm/ep Phase 1 (random) | 1.107109 |
| Harm/ep Phase 3 (agent) | 0.376450 |
| Harm reduction ratio | 0.3400 |
| Residue coverage | 0.0000 |
| Residue total magnitude | 0.000000 |

## Clock/Gate Dynamics (SD-006, MECH-090, ARC-016)

| Metric | Value |
|--------|-------|
| Beta gate block rate | 0.0000 |
| Commitment rate | 0.0000 |
| E3 precision (final) | 2.0000 |

## Behavioral Edge Cases

| Scenario | Harm/ep |
|----------|---------|
| Dense hazards (3x normal) | 0.821166 |
| Low hazards | 0.035378 |
| Ambiguous/high noise | 0.859406 |
| Novel grid (8x8) | 0.187823 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: e1_loss < 0.20 | PASS | 0.0007 |
| C2: harm_roc_auc > 0.65 | FAIL | 0.6491 |
| C3: self_other_gap > 0.05 (SD-005) | PASS | 0.5319 |
| C4: phase3_harm < phase1*0.90 | PASS | 0.376450 vs 0.996399 |
| C5: residue_coverage > 0.40 | FAIL | 0.0000 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C2 FAIL: harm_roc_auc=0.6491 <= 0.65 (E3 harm discrimination weak)
- C5 FAIL: residue_coverage=0.0000 <= 0.40 (residue magnitude=0.000000)
