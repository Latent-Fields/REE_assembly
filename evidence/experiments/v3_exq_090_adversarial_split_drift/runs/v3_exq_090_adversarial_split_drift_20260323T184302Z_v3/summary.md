# V3-EXQ-090 -- Adversarial Split Drift Test (Schizophrenic Drift Probe)

**Status:** FAIL
**Claims:** SD-005
**World:** CausalGridWorldV2 (4 hazards, env_drift for stress)
**Protocol:** Condition A (no GRL) vs Condition B (AdversarialSplitHead) x 300 eps

## Motivation

SD-005 creates separate z_self and z_world encoders. Under harm training, backprop can
gradually make z_self carry harm-predictive information (a z_world property), blurring
the self/world boundary. This is a model of "schizophrenic drift" -- the efference-copy
comparator (MECH-095) relies on z_self being a pure motor-sensory representation.

AdversarialSplitHead uses gradient reversal (Ganin et al. 2016) to prevent this.

## Results

| Condition | R2(z_self->harm) final | R2(z_world->harm) final |
|-----------|----------------------|------------------------|
| A: no adversarial | 0.0000 | 0.6262 |
| B: with adversarial | 0.0000 | 0.5251 |

Drift delta (A - B): 0.0000

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: R2_B < 0.05 (adversarial prevents drift) | PASS | 0.0000 |
| C2: R2_A > 0.10 (drift does occur without defense) | FAIL | 0.0000 |
| C3: R2(z_world->harm) > 0.20 both conditions | PASS | A=0.6262 B=0.5251 |
| C4: drift_delta > 0.05 | FAIL | 0.0000 |
| C5: no fatal errors | PASS | - |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C2 FAIL: R2_A_final=0.0000 <= 0.10. Drift did not occur without defense -- test may lack statistical power.
- C4 FAIL: drift_delta=0.0000 <= 0.05. GRL not providing sufficient protection.
