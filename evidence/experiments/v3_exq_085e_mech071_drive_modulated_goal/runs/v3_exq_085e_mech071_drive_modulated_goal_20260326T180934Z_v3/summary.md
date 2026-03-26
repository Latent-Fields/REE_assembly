# V3-EXQ-085e -- MECH-071 / INV-034 Drive-Modulated Goal Seeding

**Status:** FAIL
**Claims:** MECH-071, INV-034
**Decision:** retire_ree_claim
**Seeds:** [42, 7, 13]
**alpha_world:** 0.9  (SD-008)
**novelty_bonus_weight:** 0.1  (MECH-111)
**SD-010:** use_proxy_fields=True (harm_obs wired)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**Curriculum:** first 100 episodes place resource near spawn
**Warmup:** 300 eps  **Eval:** 50 eps
**Supersedes:** V3-EXQ-085d (all prior EXQ-085* non-contributory -- goal latent never instantiated without drive modulation)

## SD-012 Drive Fix

Root cause of EXQ-085 through 085d: benefit_exposure EMA never exceeded threshold during random-walk warmup. Single resource contact gives benefit_exposure += 0.03 (below threshold=0.05). No drive modulation means sated and starving agents react identically to food.

Fix: effective_benefit = benefit_exposure * (1 + drive_weight * drive_level) where drive_level = 1 - energy (obs_body[3]). At drive_level=0.8, drive_weight=2.0: effective_benefit = 2.6x benefit_exposure.

## Pre-Registered Thresholds

C1: z_goal_norm > 0.1 (goal seeded persistently)
C2: benefit_goal_present > benefit_goal_absent * 1.3
C3: calibration_gap_goal_present > 0.02
C4: no fatal errors

## Results

| Condition | benefit/ep | z_goal_norm | cal_gap |
|-----------|-----------|-------------|--------|
| GOAL_PRESENT | 0.820 | 0.135 | 0.1664 |
| GOAL_ABSENT  | 0.820 | -- | -- |

**Benefit ratio (goal/no-goal): 1.00x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm > 0.1 | PASS | 0.135 |
| C2: benefit ratio >= 1.3x | FAIL | 1.00x |
| C3: cal_gap > 0.02 | PASS | 0.1664 |
| C4: no fatal errors | PASS | -- |

Criteria met: 3/4 -> **FAIL**

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.560 z_goal_norm=0.128 cal_gap=0.1990 resource_events=263
  seed=7: benefit/ep=1.000 z_goal_norm=0.101 cal_gap=0.1102 resource_events=238
  seed=13: benefit/ep=0.900 z_goal_norm=0.175 cal_gap=0.1900 resource_events=237

GOAL_ABSENT:
  seed=42: benefit/ep=0.560 resource_events=263
  seed=7: benefit/ep=1.000 resource_events=238
  seed=13: benefit/ep=0.900 resource_events=237

## Failure Notes

- C2 FAIL: benefit_ratio=1.00x < 1.3x (goal_present=0.820 vs goal_absent=0.820)
