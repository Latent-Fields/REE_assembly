# V3-EXQ-035 — MECH-069 Optimizer Separation vs. Merge Ablation

**Status:** FAIL  (3/5 criteria)
**Claims:** MECH-069, SD-003
**World:** CausalGridWorldV2 (size=12, num_hazards=4, num_resources=5)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0
**Warmup:** 500 episodes  |  **Eval:** 50 episodes

## Hypothesis

MECH-069 (`learning.three_incommensurable_error_signals`): sensory prediction error (E1),
motor-sensory error (E2_self), and harm/goal error (E3) are incommensurable. A single merged
optimizer allows gradient interference that prevents each loss from specialising correctly,
degrading calibration, attribution, and world-forward prediction relative to three separated
optimizers.

## Conditions

- **SEPARATED**: standard_optimizer (all params except wf/harm; lr=1e-3) + world_forward_optimizer
  (e2.world_transition + e2.world_action_encoder; lr=1e-3) + harm_eval_optimizer
  (e3.harm_eval_head; lr=1e-4). Independent backward passes.
- **MERGED**: Single Adam(lr=1e-3) over all parameters. merged_loss = e1 + e2 + wf + harm_eval,
  single backward pass.

Both conditions use identical CausalGridWorldV2 configuration, identical random seed reset,
identical E3-on-E2-predictions training fix (from EXQ-030b).

## Results

### Key Comparison

| Metric | Separated | Merged | Delta |
|---|---|---|---|
| calibration_gap_approach | -0.028193 | -0.093306 | +0.065113 |
| attribution_gap | 0.034472 | 0.063537 | -0.029066 |
| world_forward_r2 | 0.9472 | 0.9472 | +0.0000 |

### Causal Signature by Transition Type

| Transition | Separated | Merged |
|---|---|---|
| none (locomotion) | -0.074152 | -0.108629 |
| hazard_approach | 0.005271 | 0.008417 |
| env_caused_hazard | -0.029201 | -0.055120 |
| agent_caused_hazard | 0.017314 | 0.025535 |

### Harm-Eval Score by Transition Type

| Transition | Separated | Merged |
|---|---|---|
| none (locomotion) | 0.3652 | 0.2780 |
| hazard_approach | 0.5567 | 0.6169 |
| env_caused_hazard | 0.5849 | 0.7102 |
| agent_caused_hazard | 0.4724 | 0.4551 |

### Eval Counts (approach events)

| Condition | n_approach | n_env_hazard | n_none |
|---|---|---|---|
| Separated | 832 | 13 | 101 |
| Merged | 832 | 13 | 101 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap_approach_separated > calibration_gap_approach_merged | PASS | -0.028193 vs -0.093306 |
| C2: attribution_gap_separated > attribution_gap_merged | FAIL | 0.034472 vs 0.063537 |
| C3: calibration_gap_approach_separated > 0.05 | FAIL | -0.028193 |
| C4: wf_r2_separated > wf_r2_merged OR > 0.10 | PASS | 0.9472 vs 0.9472 |
| C5: n_approach_eval_separated >= 50 | PASS | 832 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C2 FAIL: attribution_gap_separated(0.034472) <= attribution_gap_merged(0.063537)
- C3 FAIL: calibration_gap_separated=-0.028193 <= 0.05
