# V3-EXQ-032 — MECH-102: Violence as Terminal Error Correction
                      Energy Escalation Under Viability Threat

**Status:** FAIL
**Claims:** MECH-102, ARC-024, SD-003
**World:** CausalGridWorldV2 (6 hazards, 3 resources — high viability pressure)
**Policy:** E3-guided harm-minimizing (argmin E3(E2(z_world, a)))
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## What This Tests

MECH-102: violence (high-energy intervention) is selected when low-energy pathways fail,
NOT because ethical constraint is absent.

Computational test: even the most ethical possible policy (argmin predicted harm)
produces higher causal attribution (causal_sig) when viability is threatened
(harm_exposure high) than when low-energy paths are available (harm_exposure low).

The agent is TRYING to minimize harm at every step. But when all reachable states
carry high harm_eval scores (viability threatened, no safe option), the selected action
carries a high counterfactual signature — because there's no safe counterfactual either.
This is forced escalation: high-energy action not from lack of ethics but from lack of
low-energy options.

## Results

| Condition | harm_exposure | causal_sig | n steps |
|---|---|---|---|
| Low exposure (< 0.1) | low | -0.067962 | 7904 |
| High exposure (>= 0.2) | 0.0000 | 0.000000 | 0 |

**Escalation gap** (high - low): 0.067962

### By Transition Type

| Transition | causal_sig |
|---|---|
| agent_caused_hazard            | -0.050957 |
| env_caused_hazard              | -0.048529 |
| hazard_approach                | -0.052436 |
| none                           | -0.068408 |
| resource                       | -0.062082 |

- **world_forward R²**: 0.9481

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: escalation_gap > 0 (high-exposure → higher attribution) | PASS | 0.067962 |
| C2: causal_sig_high_exposure > 0.001 (positive attribution at threat) | FAIL | 0.000000 |
| C3: n_high_exposure >= 20 (enough threat steps) | FAIL | 0 |
| C4: world_forward_r2 > 0.05 (E2 learned world dynamics) | PASS | 0.9481 |
| C5: mean_harm_exposure_high > 0.15 (genuine viability threat) | FAIL | 0.0000 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C2 FAIL: causal_sig_high_exposure=0.000000 <= 0.001
- C3 FAIL: n_high_exposure=0 < 20
- C5 FAIL: mean_harm_exposure_high=0.0000 <= 0.15
