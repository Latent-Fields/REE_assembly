# V3-EXQ-121 -- MECH-095 Agency Attribution Discriminative Pair

**Status:** FAIL
**Claim:** MECH-095
**Proposal:** EXP-0019 / EVB-0015
**Seeds:** [42]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps
**env_drift_prob:** 0.3  **env_drift_interval:** 3

## Design

AGENCY_ATTRIBUTION_ON: AgencyComparator computes efference-copy mismatch (predicted z_self delta vs observed), encodes as agency signal.
AGENCY_ATTRIBUTION_ABLATED: Direct fusion of [z_self_delta, z_world] without structured comparison.

## Pre-Registered Thresholds

C1: auc_ON - auc_ABLATED >= 0.05  (relative advantage)
C2: auc_ON >= 0.6  (absolute attribution learning)
C3: auc_ON > auc_ABLATED for ALL seeds  (consistency)
C4: min_contacts >= 20  (data quality)
C5 (diagnostic): env mismatch >= 1.05x agent mismatch

## Aggregate Results

| Metric | AGENCY_ON | AGENCY_ABLATED | Delta | Pass |
|--------|-----------|----------------|-------|------|
| attribution_AUC (C1) | 0.6400 | 0.3600 | +0.2800 | YES |
| attribution_AUC >= 0.6 (C2) | 0.6400 | -- | -- | YES |
| seed consistency (C3) | [True] | -- | -- | YES |
| min_contacts (C4) | 10 | -- | -- | NO |
| mm_env/mm_agent (C5 diag) | 0.997 | -- | -- | NO |

## Interpretation

MECH-095 NOT SUPPORTED at current operationalisation. auc_ON=0.6400, auc_ABLATED=0.3600, delta=+0.2800. AgencyComparator (efference-copy mismatch) did not outperform direct fusion baseline. Possible causes: (1) self_dim=32 z_self delta too noisy for reliable efference-copy prediction; (2) action embedding (one-hot 5) insufficient to predict z_self dynamics; (3) env_drift_prob=0.3 generates sufficient env_caused events but they may not produce discriminable z_self mismatch patterns.

## Per-Seed (AGENCY_ATTRIBUTION_ON)

  seed=42: auc=0.6400 harm_rate=0.8507 contacts_eval=10 (a=5 e=5) mm_agent=0.5223 mm_env=0.5206 train: a=6 e=4

## Per-Seed (AGENCY_ATTRIBUTION_ABLATED)

  seed=42: auc=0.3600 harm_rate=0.8507 contacts_eval=10 (a=5 e=5) train: a=6 e=4

## Failure Notes

- C4 FAIL: min_contacts=10 < 20. Insufficient hazard contact events in eval -- data quality issue. Increase env_drift_prob or warmup_episodes.
- C5 (diagnostic): mm_agent=0.5223 mm_env=0.5206 ratio=0.997 < 1.05. Env-caused contacts did not produce higher z_self mismatch than agent-caused. The efference copy may not capture enough predictable self-motion signal.
