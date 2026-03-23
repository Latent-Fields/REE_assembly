# V3-EXQ-067 -- MECH-026: Ready Vigilance Mode

**Status:** FAIL
**Claim:** MECH-026 -- ready vigilance is a distinct mode from both neutral baseline and doing mode
**Design:** Two-condition (threat present vs neutral), matched training protocol
**alpha_world:** 0.9  |  **Train:** 500 eps  |  **Eval:** 100 eps  |  **Seed:** 0

## Design Rationale

Ready vigilance predicts that an agent facing distant-but-present threats shows elevated
preparedness (beta_gate elevation) *without* committing to action. If threat simply forced
constant commitment, doing mode and vigilance would be indistinguishable. C1 tests that
the gap exists; C2 tests that vigilance is distinct from doing.

## Condition Comparison

| Metric | Threat (A) | Neutral (B) |
|--------|-----------|-------------|
| mean_beta_uncommitted | 0.0000 | 0.0000 |
| commitment_rate | 1.000 | 1.000 |
| uncommitted_steps | 0 | 0 |
| committed_steps | 20000 | 700 |
| harm_pred_std | 0.0988 | 0.3123 |

**readiness_gap** = +0.0000  (threat.beta_uncommitted - neutral.beta_uncommitted)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: readiness_gap > 0.005 (vigilance elevates gate) | FAIL | +0.0000 |
| C2: threat_commit_rate < neutral_commit_rate * 1.5 (not forced-doing) | PASS | 1.000 vs 1.500 |
| C3: uncommitted_threat_step_count >= 20 | FAIL | 0 |
| C4: harm_pred_std > 0.01 (E3 not collapsed) | PASS | 0.0988 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: readiness_gap=+0.0000 <= 0.005
- C3 FAIL: uncommitted_threat_step_count=0 < 20
