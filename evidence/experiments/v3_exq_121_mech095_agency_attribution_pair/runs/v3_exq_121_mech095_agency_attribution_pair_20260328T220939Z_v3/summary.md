# V3-EXQ-121 -- MECH-095 Agency Attribution Discriminative Pair

**Status:** FAIL
**Claim:** MECH-095
**Proposal:** EXP-0019 / EVB-0015
**Seeds:** [42, 123]
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
| attribution_AUC (C1) | 0.4110 | 0.7450 | -0.3340 | NO |
| attribution_AUC >= 0.6 (C2) | 0.4110 | -- | -- | NO |
| seed consistency (C3) | [False, False] | -- | -- | NO |
| min_contacts (C4) | 171 | -- | -- | YES |
| mm_env/mm_agent (C5 diag) | 0.928 | -- | -- | NO |

## Interpretation

MECH-095 NOT SUPPORTED at current operationalisation. auc_ON=0.4110, auc_ABLATED=0.7450, delta=-0.3340. AgencyComparator (efference-copy mismatch) did not outperform direct fusion baseline. Possible causes: (1) self_dim=32 z_self delta too noisy for reliable efference-copy prediction; (2) action embedding (one-hot 5) insufficient to predict z_self dynamics; (3) env_drift_prob=0.3 generates sufficient env_caused events but they may not produce discriminable z_self mismatch patterns.

## Per-Seed (AGENCY_ATTRIBUTION_ON)

  seed=42: auc=0.4109 harm_rate=0.8361 contacts_eval=192 (a=107 e=85) mm_agent=1.8663 mm_env=1.7576 train: a=835 e=671
  seed=123: auc=0.4111 harm_rate=0.8463 contacts_eval=171 (a=103 e=68) mm_agent=1.3446 mm_env=1.2228 train: a=842 e=679

## Per-Seed (AGENCY_ATTRIBUTION_ABLATED)

  seed=42: auc=0.7227 harm_rate=0.8361 contacts_eval=192 (a=107 e=85) train: a=835 e=671
  seed=123: auc=0.7673 harm_rate=0.8463 contacts_eval=171 (a=103 e=68) train: a=842 e=679

## Failure Notes

- C1 FAIL: auc_ON=0.4110 vs auc_ABLATED=0.7450 (delta=-0.3340, needs >=0.05). AgencyComparator did not provide relative attribution advantage. Possible causes: (1) z_self delta signal too noisy at self_dim=32, (2) env_drift_prob too low (too few env_caused events), (3) action embedding insufficient for efference copy at scale.
- C2 FAIL: auc_ON=0.4110 (needs >=0.6). ON condition did not achieve reliable attribution above chance. Check n_agent_caused_train and n_env_caused_train -- sparse signal.
- C3 FAIL: per_seed direction inconsistent ([False, False]). ON did not consistently beat ABLATED across seeds.
- C5 (diagnostic): mm_agent=1.6055 mm_env=1.4902 ratio=0.928 < 1.05. Env-caused contacts did not produce higher z_self mismatch than agent-caused. The efference copy may not capture enough predictable self-motion signal.
