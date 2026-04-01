# V3-EXQ-186 -- Hybrid Benefit+Harm Selector (ARC-030)

**Status:** FAIL
**Claims:** ARC-030, MECH-112
**Decision:** retire_ree_claim
**Seeds:** [42, 7, 13]

## Design

4 conditions: COMBINED (benefit+harm), BENEFIT_ONLY (ProximityEncoder+RFM),
HARM_ONLY (WFM+E3 harm_eval), RANDOM.

COMBINED action selection:
  combined_score = -benefit_weight * enc.predict_proximity(RFM(rf, a))
                   + harm_weight * harm_eval(wfm(z_world, a))
  Pick action with lowest combined_score.

benefit_weight=2.0, harm_weight=1.0

## Results

| Condition | benefit_rate | harm_rate |
|---|---|---|
| COMBINED | 0.212 | 0.08748 |
| BENEFIT_ONLY | 0.350 | 0.09412 |
| HARM_ONLY | 0.137 | 0.06271 |
| RANDOM | 0.862 | 0.04019 |

**benefit_ratio_vs_random:** 0.25x
**benefit_ratio_vs_harm_only:** 1.55x
**harm_ratio_vs_harm_only:** 1.40x

## Training Diagnostics

| Model | Final Loss |
|---|---|
| ProximityEncoder | 0.0012 |
| ResourceForwardModel | 0.0074 |
| WorldForwardModel | 0.0000 |

**prox_r2 (avg):** 0.902

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: combined/random >= 1.3x | FAIL | 0.25x |
| C2: combined/harm_only >= 1.2x | PASS | 1.55x |
| C3: combined_harm <= 1.3*harm_only | FAIL | 1.40x |
| C4: combined > benefit_only (H-TRAP) | FAIL | 0.212 vs 0.350 |

Criteria met: 1/4 -> **FAIL**

## Per-Seed

  seed=42: combined_br=0.275 benefit_only_br=0.362 harm_only_br=0.100 random_br=0.875 prox_r2=0.890
  seed=7: combined_br=0.212 benefit_only_br=0.212 harm_only_br=0.163 random_br=0.912 prox_r2=0.900
  seed=13: combined_br=0.150 benefit_only_br=0.475 harm_only_br=0.150 random_br=0.800 prox_r2=0.916

## Failure Notes

- C1 FAIL: benefit_ratio_vs_random=0.25x < 1.3x. Combined does not outperform random baseline.
- C3 FAIL: combined_harm_rate=0.08748 > 1.3 * harm_only_harm_rate=0.06271. Goal pursuit increases harm beyond acceptable margin.
- C4 FAIL (H-TRAP): combined_benefit_rate=0.212 <= benefit_only_benefit_rate=0.350. Harm avoidance does NOT improve net benefit -- no H-TRAP effect.
