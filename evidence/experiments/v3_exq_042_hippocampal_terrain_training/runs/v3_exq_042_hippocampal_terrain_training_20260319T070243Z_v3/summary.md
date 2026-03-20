# V3-EXQ-042 — Hippocampal Terrain Training

**Status:** FAIL
**Claims:** SD-004, ARC-007, MECH-089
**World:** CausalGridWorldV2 (body=12, world=250)
**alpha_world:** 0.9 (SD-008)  |  **Seed:** 0
**Prerequisite:** EXQ-041 PASS (ThetaBuffer stabilises E3 calibration)

## Motivation

EXQ-041 left terrain_prior frozen. In the full pipeline, HippocampalModule
proposes via CEM guided by terrain_prior, but an untrained terrain_prior produces
uninformed proposals (equivalent to random sampling).

This experiment adds terrain_prior training via E3 behavioral cloning. After E3
selects a trajectory, we teach terrain_prior to predict that trajectory's
action-object sequence, conditioned on (theta_z_world, e1_prior, residue_val).

terrain_prior should learn: from this world state + residue terrain, E3 prefers
these kinds of action objects. Over episodes, proposals become terrain-informed.

ARC-007 STRICT (Q-020): proposals scored by residue field only — no independent
hippocampal value head. The terrain_prior guides CEM sampling; E3 introduces all
weighting via J(ζ) = F(ζ) + λM(ζ) + ρΦ_R(ζ).

## Results

### Terrain_prior Learning
| Phase | terrain_loss |
|---|---|
| Initial (first 100 eps) | 311.2741 |
| Final (last 100 eps) | 311.2741 |
| Reduction | 0.0% |

### Hippocampal vs Random Proposal Quality
| Proposal type | mean residue score |
|---|---|
| Hippocampal (terrain-guided) | 0.000000 |
| Random | 0.394714 |
| Quality gap (random - hippo) | 0.394714 |

Positive quality gap = hippocampal proposals navigate to lower-residue regions.

### E3 Calibration (MECH-089 stability check)
| Type | mean harm_eval | n |
|---|---|---|
| none | 0.4825 | 5 |
| approach | 0.4811 | 5 |
| contact | 0.0000 | 0 |
**calibration_gap_approach:** -0.0014

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: terrain_loss reduced >= 30% | FAIL | 311.2741→311.2741 |
| C2: hippo_quality_gap > 0 | PASS | 0.394714 |
| C3: cal_gap_approach > 0.03 | FAIL | -0.0014 |
| C4: n_approach_eval >= 30 | FAIL | 5 |
| C5: world_forward R² > 0.05 | FAIL | 0.0000 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: terrain_loss not sufficiently reduced (initial=311.2741  final=311.2741, threshold=70% reduction). terrain_prior not learning E3's preferences.
- C3 FAIL: cal_gap_approach=-0.0014 <= 0.03
- C4 FAIL: n_approach_eval=5 < 30
- C5 FAIL: world_forward_r2=0.0000 <= 0.05
