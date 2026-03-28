# V3-EXQ-126 -- MECH-104: Volatility Gate / Unexpected Harm Surprise Spike

**Status:** FAIL
**Claims:** MECH-104
**Design:** SURPRISE_GATE_ON vs SURPRISE_GATE_ABLATED x seeds [42, 123]
**SPIKE_MAGNITUDE:** 0.05  |  **SURPRISE_THRESHOLD:** 0.02
**Warmup:** 2 eps  |  **Eval:** 2 eps  |  **Steps:** 10

## Design Rationale

MECH-104 (LC-NE volatility interrupt) predicts that unexpected harm events spike
commitment uncertainty (beta / running_variance) via a surprise gate. This is Route-2
validation: the gate is selective for unexpected harm (surprise > threshold), not routine
or anticipated harm.

This matched-seed discriminative pair extends EXQ-064 (single-seed PASS, 5/5) by:
(1) Using two matched seeds [42, 123] for cross-seed consistency.
(2) Explicitly contrasting SURPRISE_GATE_ON vs SURPRISE_GATE_ABLATED on the SAME trained
    agent -- the ablation directly removes the gate's causal contribution.
(3) Adding C4 (discriminative criterion): the cross-condition delta must be >= 0.004.

If SURPRISE_GATE_ON shows higher delta_var_unexpected than SURPRISE_GATE_ABLATED, and the
gate is selective (no spike on expected harm), this supports MECH-104.

## SURPRISE_GATE_ON Results

| seed | n_unexpected | n_spikes | delta_var_unexpected | delta_var_expected |
|------|-------------|---------|---------------------|--------------------|
| 42 | 1 | 0 | 0.000000 | 0.000000 |
| 123 | 9 | 0 | 0.000000 | 0.000000 |

## SURPRISE_GATE_ABLATED Results

| seed | n_unexpected | delta_var_unexpected | delta_var_expected |
|------|-------------|---------------------|-------------------|
| 42 | 16 | 0.000000 | 0.000000 |
| 123 | 4 | 0.000000 | 0.000000 |

## Discriminative Delta (ON - ABLATED, delta_var_unexpected)

| seed | discriminative_delta |
|------|---------------------|
| 42 | 0.000000 |
| 123 | 0.000000 |

## PASS Criteria

| Criterion | Result | Values |
|-----------|--------|--------|
| C1: ON delta_var_unexpected >= 0.005 (both seeds) | FAIL | s42=0.000000, s123=0.000000 |
| C2: ON delta_var_expected < 0.002 (both seeds) | PASS | s42=0.000000, s123=0.000000 |
| C3: ABLATED delta_var_unexpected < 0.002 (both seeds) | PASS | s42=0.000000, s123=0.000000 |
| C4: (ON-ABLATED) delta_var_unexpected >= 0.004 (both seeds) | FAIL | s42=0.000000, s123=0.000000 |
| C5: n_unexpected_harm_ON >= 10 (both seeds) | FAIL | s42=1, s123=9 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 3/6 -> **FAIL**

## Failure Notes

- C1 FAIL seed=42: ON delta_var_unexpected=0.000000 < 0.005
- C4 FAIL seed=42: discriminative_delta=0.000000 < 0.004
- C5 FAIL seed=42: n_unexpected_harm_ON=1 < 10
- C1 FAIL seed=123: ON delta_var_unexpected=0.000000 < 0.005
- C4 FAIL seed=123: discriminative_delta=0.000000 < 0.004
- C5 FAIL seed=123: n_unexpected_harm_ON=9 < 10
