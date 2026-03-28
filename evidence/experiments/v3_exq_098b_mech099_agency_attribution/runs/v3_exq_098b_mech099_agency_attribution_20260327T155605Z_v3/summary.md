# V3-EXQ-098b -- MECH-099 Agency Attribution Three-Stream Redesign

**Status:** FAIL
**Claims:** MECH-099, MECH-095
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 100 eps
**env_drift_prob:** 0.3  **env_drift_interval:** 3

## Redesign from EXQ-098

EXQ-098 trained lateral head with BCE on harm_obs (duplicate harm signal). Adverse direction (delta=-0.038) = information disadvantage, not architectural failure. EXQ-098b trains lateral head with BCE on agency attribution labels (agent_caused vs env_caused hazard contact). Motion-delta input (MT analog) added to lateral head (delta_hazard = hazard_ch_t - hazard_ch_{t-1}).

## Pre-Registered Thresholds

C1: attr_AUC_THREE - attr_AUC_TWO >= 0.05  (relative attribution advantage)
C2: attr_AUC_THREE >= 0.65  (absolute attribution learning)
C3: avoidance_THREE >= avoidance_TWO  (behavioral: attribution-guided flee)

## Aggregate Results

| Metric | THREE_STREAM | TWO_STREAM | Delta | Pass |
|--------|-------------|-----------|-------|------|
| attribution_AUC (C1) | 0.9942 | 0.9989 | -0.0047 | NO |
| attribution_AUC >= 0.65 (C2) | 0.9942 | -- | -- | YES |
| harm_avoidance (C3) | 0.0182 | 0.0175 | +0.0007 | YES |

## Interpretation

PARTIAL: C2 passes (absolute AUC=0.9942 >= 0.65) but C1 fails (delta=-0.0047 < 0.05). THREE_STREAM learned attribution but did not outperform TWO_STREAM. z_world may encode agency attribution nearly as well as the dedicated motion head at this scale. Consider: larger motion_dim, deeper lateral head, or longer training.

## Per-Seed (THREE_STREAM)

  seed=42: attr_auc=0.9895 avoidance=0.0215 agent_caused_train=887 env_caused_train=306 contact_eval=324 (a=298 e=26)
  seed=7: attr_auc=0.9988 avoidance=0.0149 agent_caused_train=893 env_caused_train=289 contact_eval=321 (a=295 e=26)

## Per-Seed (TWO_STREAM)

  seed=42: attr_auc=0.9989 avoidance=0.0191 agent_caused_train=887 env_caused_train=306 contact_eval=306 (a=300 e=6)
  seed=7: attr_auc=0.9989 avoidance=0.0158 agent_caused_train=893 env_caused_train=289 contact_eval=309 (a=297 e=12)

## Failure Notes

- C1 FAIL: attr_auc_THREE=0.9942 vs attr_auc_TWO=0.9989 (delta=-0.0047, needs >=0.05). MotionLateralHead did not improve attribution AUC by 5pp over z_world.
