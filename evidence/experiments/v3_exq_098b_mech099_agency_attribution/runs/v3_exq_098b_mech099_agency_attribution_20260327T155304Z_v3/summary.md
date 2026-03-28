# V3-EXQ-098b -- MECH-099 Agency Attribution Three-Stream Redesign

**Status:** FAIL
**Claims:** MECH-099, MECH-095
**Seeds:** [42]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 5 eps  **Eval:** 3 eps
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
| attribution_AUC (C1) | 0.5000 | 0.5000 | +0.0000 | NO |
| attribution_AUC >= 0.65 (C2) | 0.5000 | -- | -- | NO |
| harm_avoidance (C3) | 0.0000 | 0.0000 | +0.0000 | YES |

## Interpretation

MECH-099 NOT SUPPORTED at this operationalisation. attr_auc_THREE=0.5000, delta=+0.0000. Possible causes: (1) sparse attribution events (check train counts), (2) delta_hazard signal too noisy at current drift rate, (3) contamination dynamics do not produce discriminable agent_caused signal, (4) world_dim=32 already sufficient for attribution without lateral stream.

## Per-Seed (THREE_STREAM)

  seed=42: attr_auc=0.5000 avoidance=0.0000 agent_caused_train=10 env_caused_train=2 contact_eval=9 (a=9 e=0)

## Per-Seed (TWO_STREAM)

  seed=42: attr_auc=0.5000 avoidance=0.0000 agent_caused_train=10 env_caused_train=2 contact_eval=9 (a=9 e=0)

## Failure Notes

- C1 FAIL: attr_auc_THREE=0.5000 vs attr_auc_TWO=0.5000 (delta=+0.0000, needs >=0.05). MotionLateralHead did not improve attribution AUC by 5pp over z_world.
- C2 FAIL: attr_auc_THREE=0.5000 (needs >=0.65). THREE_STREAM did not reach absolute attribution learning threshold. Possible causes: too few contact events (check n_agent_caused_train, n_env_caused_train); delta_hazard signal insufficient; motion_dim too small.
