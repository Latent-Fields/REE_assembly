# V3-EXQ-032c — MECH-102: Forced Escalation in Dense Grid (8×8, 10 hazards)

**Status:** FAIL
**Claims:** MECH-102, ARC-024, SD-003
**Grid:** 8×8, 10 hazards (15.6% cell coverage — physically unavoidable)
**Policy:** E3-guided harm-minimizing (argmin E3(E2(z_world, a)))
**Exposure thresholds:** low < 0.05  |  high >= 0.1
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## Design Rationale

EXQ-032 used a 12×12 grid with 6 hazards (4.2% coverage). The harm-minimizing
policy succeeded in avoiding all hazards — n_high_exposure=0. This is not a model
failure; it is a test design failure: the environment was not constraining enough
to force viability threat.

EXQ-032c uses 8×8 = 64 cells with 10 hazards (15.6% coverage). At this density,
even an optimal harm-minimizing policy cannot avoid frequent proximity to hazards.
The harm_exposure EMA accumulates continuously.

MECH-102 prediction: when the agent is in a constrained environment where all
paths carry harm proximity, the selected action has higher counterfactual signature
than when safe paths exist — regardless of the ethical intent of the selection.

## Results

| Condition | harm_exp threshold | causal_sig | n steps |
|---|---|---|---|
| Low exposure (< 0.05) | — | -0.012111 | 914 |
| High exposure (>= 0.1) | 0.0000 | 0.000000 | 0 |

**Escalation gap** (high - low): 0.012111
**world_forward R²**: 0.9185

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: escalation_gap > 0 | PASS | 0.012111 |
| C2: causal_sig_high > 0.001 | FAIL | 0.000000 |
| C3: n_high_exposure >= 50 (dense grid ensures threat steps) | FAIL | 0 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9185 |
| C5: mean_harm_exposure_high > 0.10 (genuine viability threat) | FAIL | 0.0000 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C2 FAIL: causal_sig_high=0.000000 <= 0.001
- C3 FAIL: n_high_exposure=0 < 50
- C5 FAIL: mean_harm_exposure_high=0.0000 <= 0.10
