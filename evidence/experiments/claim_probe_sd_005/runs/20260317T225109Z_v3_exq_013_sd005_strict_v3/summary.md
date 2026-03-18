# V3-EXQ-013 — SD-005 Strict: Event-Conditional Separation

**Status:** FAIL
**Training:** 600 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Eval:** 100 eps
**Seed:** 0

## Motivation

EXQ-001 (SD-005 PASS) used aggregate correlations. body_selectivity_margin was −0.137
(z_world MORE sensitive to body movement than z_self — backwards) but was not a PASS criterion.
This experiment uses event-conditional measurement to test functional separation.

## Event Counts

| Event Type | n |
|---|---|
| empty_move (transition_type=none) | 1667 |
| env_caused_hazard | 154 |
| agent_caused_hazard | 86 |

## Δz Statistics by Event Type

| Event Type | Δz_self (mean±std) | Δz_world (mean±std) |
|---|---|---|
| empty_move    | 0.0406 ± 0.0344 | 0.0640 ± 0.0230 |
| env_hazard    | 0.0348 ± 0.0307 | 0.0647 ± 0.0219 |
| agent_hazard  | 0.0235 ± 0.0061 | 0.0565 ± 0.0215 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: Δz_world(env_caused) > Δz_world(empty_move), margin > 0.005 | FAIL | margin=0.0008 |
| C2: Δz_self(empty_move) > Δz_world(empty_move) (body selectivity) | FAIL | margin=-0.0234 |
| C3: E2 divergence near-hazard > safe, margin > 0.002 | FAIL | margin=-0.0071 |
| C4: n >= 30 per event type | PASS | empty=1667 env=154 agent=86 |
| C5: No fatal errors | PASS | 0 |

## E2 Divergence Results

- Mean divergence at near-hazard positions: 0.0629
- Mean divergence at safe positions: 0.0700
- Margin: -0.0071
- n_near_hazard probes: 790, n_safe probes: 78

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: Δz_world(env_hazard)=0.0647 vs Δz_world(empty)=0.0640  margin=0.0008 <= 0.005
- C2 FAIL: body_selectivity margin=-0.0234 <= 0.0 [Δz_self(empty)=0.0406 Δz_world(empty)=0.0640]
- C3 FAIL: E2 divergence margin=-0.0071 <= 0.002 [near=0.0629 safe=0.0700]
