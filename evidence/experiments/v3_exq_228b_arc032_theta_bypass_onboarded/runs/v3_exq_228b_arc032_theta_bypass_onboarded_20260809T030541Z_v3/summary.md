# V3-EXQ-228b -- ARC-032 Theta-Rate Pathway Behavioral Test (scaffolded_sd054_onboarding)

**Status:** FAIL  **Evidence direction:** does_not_support  **Decision:** inconclusive
**Supersedes:** V3-EXQ-228a
**Claims:** ARC-032

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| Precondition (goal_norm >= 0.05) | 1.00 | True |
| C1 lift (>= 0.05) | 0.00 | False |
| C2 harm parity (<= 1.5x) [info] | 1.00 | True |

## Interpretation

ARC-032 DOES NOT SUPPORT: with the precondition met (z_goal_norm >= 0.05 on 1.00 of seeds), THETA_ACTIVE and THETA_ZEROED show no measurable resource-collection lift (C1 passed on only 0.00 of seeds, need >= 0.67). The theta channel does not appear to be a necessary pathway for goal-context to reach E3 trajectory scoring on this substrate -- either the theta-averaged signal is redundant with instantaneous z_world already available to E3 through other channels, or E3 scoring is dominated by non-theta factors.
