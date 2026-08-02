# Failure Autopsy: V3-EXQ-866 (INV-034/Q-021 goal-maintenance-necessary-for-agency)

**Generated:** 2026-08-02T10:50:16Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_866_inv034_q021_goal_maintenance_agency_20260802T074409Z_v3`, FAIL, claims INV-034/Q-021.
- Gate table: G0 non-degeneracy 0/3 FAIL, C1 harm parity 3/3 PASS, C2 survival parity 3/3 PASS, C3 quiescence 3/3 PASS, C4 approach restored 0/3 FAIL, C5 entropy signature 0/3 FAIL, C6 z_goal mechanistic check 2/3 PASS.
- G0: FULL (approach+avoidance) arm's `resource_visit_rate_mean` = 0.0046, **below** the RANDOM baseline's 0.0217 -- the trained agent forages worse than random action selection.
- The driver's own `summary_markdown` already states the correct reading: *"This is a substrate/env non-degeneracy issue (mirrors the EXQ-072b failure mode), NOT evidence against INV-034/Q-021. Per IGW-222 DESIGN.md 5.8, escalate to the full scaffolded_sd054_onboarding curriculum (Option B) rather than re-running this lightweight harness."*
- `experiments/scaffolded_sd054_onboarding.py` already exists (built substrate) -- this is a harness-escalation, not a new implementation gap.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | claims never fairly tested; G0 correctly blocked interpretation |
| Biological reference | unchanged | mechanism not tested |
| Prerequisites | present | C1/C2/C3/C6 all pass individually |
| Environment | **inadequate for this lightweight harness** | below-random foraging |
| Measurement | adequate | G0 gate + self-diagnosis correct |

## Learning extracted

1. The driver's self-diagnosis was already correct and complete -- this autopsy confirms rather than re-derives.
2. Component-level correctness (C1/C2/C3/C6) does not guarantee whole-task competence -- a familiar competence-floor pattern.
3. The remedy is already-built substrate (scaffolded_sd054_onboarding), not a new build.

## Routing

**epistemic_category:** `substrate_not_ready_requeue` | **evidence_direction:** `non_contributory` | **routing:** `/queue-experiment` 866a on the scaffolded_sd054_onboarding curriculum.

**User gate (2026-08-02):** Approved as recommended.
