# V3-EXQ-042 — Hippocampal Terrain Training

**Status:** PASS
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
| Initial (first 100 eps) | 0.2233 |
| Final (last 100 eps) | 0.0000 |
| Reduction | 100.0% |

### Hippocampal vs Random Proposal Quality
| Proposal type | mean residue score |
|---|---|
| Hippocampal (terrain-guided) | 0.000000 |
| Random | 0.392646 |
| Quality gap (random - hippo) | 0.392646 |

Positive quality gap = hippocampal proposals navigate to lower-residue regions.

### E3 Calibration (MECH-089 stability check)
| Type | mean harm_eval | n |
|---|---|---|
| none | 0.0024 | 9792 |
| approach | 0.8075 | 198 |
| contact | 0.7973 | 10 |
**calibration_gap_approach:** 0.8051

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: terrain_loss reduced >= 30% | PASS | 0.2233→0.0000 |
| C2: hippo_quality_gap > 0 | PASS | 0.392646 |
| C3: cal_gap_approach > 0.03 | PASS | 0.8051 |
| C4: n_approach_eval >= 30 | PASS | 198 |
| C5: world_forward R² > 0.05 | PASS | 0.9877 |

Criteria met: 5/5 → **PASS**

