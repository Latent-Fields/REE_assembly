# V3-EXQ-123 -- MECH-102 Harm Escalation Gradient Discriminative Pair

**Status:** FAIL
**Claim:** MECH-102
**Proposal:** EXP-0021 / EVB-0017
**Seeds:** [42, 123]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps
**env_drift_prob:** 0.3  **env_drift_interval:** 3
**harm_scale:** 0.02  **proximity_harm_scale:** 0.01

## Design

HARM_EVAL_ON: E3 harm_eval_head trained on harm_signal labels. Gradient score = P(approach_harm_score < contact_harm_score) via cross-pairs.
HARM_EVAL_ABLATED: E3 harm_eval_head frozen at random init (no training). Gradient score should be ~0.5 (chance).

Phase detection: harm_signal in (-0.015, 0) = approach (proximity gradient); harm_signal <= -0.015 = contact (hazard impact). Calibrated for hazard_harm=0.02, proximity_harm_scale=0.01.

## Pre-Registered Thresholds

C1: gradient_score_ON - gradient_score_ABLATED >= 0.15  (relative advantage)
C2: gradient_score_ON >= 0.65  (absolute ordering above chance)
C3: gradient_score_ON > gradient_score_ABLATED for ALL seeds  (consistency)
C4: min_approach_contact_pairs >= 20  (data quality)
C5 (diagnostic): escalation_gap_ON >= 0.05  (mean contact > mean approach)

## Aggregate Results

| Metric | HARM_EVAL_ON | HARM_EVAL_ABLATED | Delta | Pass |
|--------|-------------|------------------|-------|------|
| gradient_score (C1 delta) | 0.5920 | 0.5580 | +0.0340 | NO |
| gradient_score >= 0.65 (C2) | 0.5920 | -- | -- | NO |
| seed consistency (C3) | [True, True] | -- | -- | YES |
| min_pairs (C4) | 45 | -- | -- | YES |
| escalation_gap (C5 diag) | +0.0509 | -- | -- | YES |

## Interpretation

MECH-102 NOT SUPPORTED: E3 harm_eval does not produce graded escalation. gradient_score_ON=0.5920, gradient_score_ABLATED=0.5580, delta=+0.0340. Harm evaluation signal did not escalate systematically from approach to contact phase. Consistent with a binary flag (contact/no-contact) rather than a graded ethical valuation signal.

## Per-Seed (HARM_EVAL_ON)

  seed=42: gradient_score=0.5760 escalation_gap=+0.0494 n_approach=45 n_contact=1066 mean_approach=0.4913 mean_contact=0.5407 train_harm_steps=8525
  seed=123: gradient_score=0.6080 escalation_gap=+0.0525 n_approach=57 n_contact=1037 mean_approach=0.4850 mean_contact=0.5375 train_harm_steps=8472

## Per-Seed (HARM_EVAL_ABLATED)

  seed=42: gradient_score=0.5460 escalation_gap=+0.0001 n_approach=45 n_contact=1066
  seed=123: gradient_score=0.5700 escalation_gap=+0.0001 n_approach=57 n_contact=1037

## Failure Notes

- C1 FAIL: gradient_score_ON=0.5920 vs gradient_score_ABLATED=0.5580 (delta=+0.0340, needs >=0.15). ON condition does not show substantially more ordered harm gradient than the frozen random ablation. Possible causes: (1) harm_eval head does not discriminate approach vs contact, (2) proximity_harm_scale too small to create detectable gradient, (3) world_dim=32 insufficient to encode proximity phase information.
- C2 FAIL: gradient_score_ON=0.5920 (needs >=0.65). ON condition did not achieve reliable gradient ordering. harm_eval head may not have learned proximity-phase distinctions. Check harm_buf_pos_final -- insufficient positive samples.
