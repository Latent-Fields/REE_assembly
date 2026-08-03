# V3-EXQ-883 -- MECH-427 Cross-Level Subgoal Credit

**Status:** PASS  **Evidence direction:** supports
**Route reason:** clean_scripted_contrast_scored
**Claims:** MECH-427

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| G0 readiness (every seed) | 1.00 | True |
| C1 parent-norm lift (ATTAINED > NO_ATTAINMENT) | 1.00 | True |
| C2 measurability floor | 1.00 | True |

## Interpretation

MECH-427 SUPPORTED: on a real environment + agent latent loop, a discrete subgoal-attainment event (env info['transition_type'] in {'waypoint','sequence_complete'}) propagated credit up to the parent (superordinate) goal attractor via REEAgent.notify_subgoal_attainment -> GoalState.credit_subgoal_attainment, measurably raising parent_goal_norm() above a matched no-attainment control with an otherwise identical trajectory. Confirms the 2026-08-02 SD-092 call-site wiring functions end-to-end, not just in the isolated unit-test harness.
