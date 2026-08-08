# V3-EXQ-866c -- INV-034 / Q-021 Goal-Maintenance-Necessary-for-Agency (onboarded; C6 measurement-harness correction)

**Status:** FAIL  **Evidence direction:** non_contributory
**Route reason:** non_degenerate_precondition_unmet
**Supersedes:** V3-EXQ-866a
**Claims:** INV-034, Q-021

## C6 readout: 866c (contact-gated run_p2 peak) vs 866a (decay-only mean)

| Condition | z_goal_norm_peak_max (866c C6) | zgoal_norm_mean (866a bug) |
|---|---|---|
| FULL | 0.4610 | 0.1481 |
| AVOIDANCE_ONLY | 0.0000 | 0.0000 |

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| G0 non-degeneracy (foraging) | 0.00 | False |
| C1 harm parity | 1.00 | True |
| C2 survival parity | 1.00 | True |
| C3 quiescence (avoidance-only flat) | 1.00 | True |
| C4 approach restored (FULL > avoidance) | 0.00 | False |
| C5 entropy signature | 0.00 | False |
| C6 z_goal mechanistic (contact-gated peak) | 0.67 | True |

## Interpretation

G0 non-degeneracy gate FAILED (foraging-competence ceiling), so the run is non_contributory to INV-034/Q-021 -- as expected and as diagnosed for 866a. 866c's contribution is the CORRECTED C6 z_goal readout (contact-gated run_p2 peak, n_decay_only=0), which replaces 866a's decay-only washout artifact: see z_goal_norm_peak_max_mean_* vs zgoal_norm_mean_866a_style_mean_* in metrics. G0 (foraging) is routed to the GAP-2 / Stage-H foraging-competence thread; it is a foraging/survival problem, not a z_goal-maintenance problem.
