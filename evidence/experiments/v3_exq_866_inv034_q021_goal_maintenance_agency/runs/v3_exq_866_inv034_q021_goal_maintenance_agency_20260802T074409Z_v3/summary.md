# V3-EXQ-866 -- INV-034 / Q-021 Goal-Maintenance-Necessary-for-Agency

**Status:** FAIL  **Evidence direction:** non_contributory
**Route reason:** non_degenerate_precondition_unmet
**Claims:** INV-034, Q-021

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| G0 non-degeneracy | 0.00 | False |
| C1 harm parity | 1.00 | True |
| C2 survival parity | 1.00 | True |
| C3 quiescence (avoidance-only flat) | 1.00 | True |
| C4 approach restored (FULL > avoidance) | 0.00 | False |
| C5 entropy signature | 0.00 | False |
| C6 z_goal mechanistic check | 0.67 | True |

## Interpretation

G0 non-degeneracy gate FAILED: the FULL (approach+avoidance) arm did not clear random-baseline resource-visit rate by the pre-registered margin on >= 2/3 seeds. This is a substrate/env non-degeneracy issue (mirrors the EXQ-072b failure mode), NOT evidence against INV-034/Q-021. Per IGW-222 DESIGN.md 5.8, escalate to the full scaffolded_sd054_onboarding curriculum (Option B) rather than re-running this lightweight harness -- that curriculum is the substrate that actually cleared goal_pipeline GAP-2's contact-rate ceiling.
