# V3-EXQ-002r6 — SD-003 Self-Attribution (Multi-Step E2 Training)

**Status:** FAIL
**Warmup:** 600 episodes, RANDOM policy + recon loss + 5-step E2 rollouts
**Probe eval:** 10 grid resets x (near-hazard + safe positions)
**Seed:** 0

## r6 Design Change — Multi-Step E2 Training

EXQ-005 confirmed E2 identity shortcut: E2w mean_loss = 0.00002. In 5x5
CausalGridWorld, z_world changes very little step-to-step, so delta≈0 trivially
minimizes 1-step MSE. E2 never learned action-conditional world dynamics.

r6 fix: train E2 on 5-step rollouts through its own world_forward.
Over N=5 steps the agent moves 2-4 cells; delta≈0 accumulates large error.
Mean E2 world loss: 0.000311 | Mean reconstruction loss: 0.02960

(r5 reconstruction loss retained to ensure z_world encodes hazard features.)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: TRAINED calibration_gap > 0.05 | FAIL | -0.0023 |
| C2: RANDOM abs(calibration_gap) < 0.10 | PASS | 0.0001 |
| C3: Warmup harm events > 100 | PASS | 1616 |
| C4: No fatal errors | PASS | 0 |
| C5: harm_eval non-degenerate | PASS | OK |
| C6: Probe coverage >= 10 each | PASS | near=250 safe=46 |

## Calibration Results (Probe-Based)

| Condition | mean_causal_sig(near_hazard) | mean_causal_sig(safe) | calibration_gap |
|---|---|---|---|
| TRAINED | -0.0046 | -0.0023 | -0.0023 |
| RANDOM  | -0.0000 | -0.0001 | 0.0001 |

## Attribution Pipeline

```
z_world = encoder(obs_world)              # now trained with reconstruction loss
recon_loss = MSE(decoder(z_world), obs_world)   # forces hazard info preservation
z_world_actual = E2.world_forward(z_world, a_actual)
z_world_cf     = E2.world_forward(z_world, a_cf)
harm_actual    = E3.harm_eval(z_world_actual)
harm_cf        = E3.harm_eval(z_world_cf)
causal_sig     = harm_actual - harm_cf
```

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL: TRAINED calibration_gap -0.0023 <= 0.05
