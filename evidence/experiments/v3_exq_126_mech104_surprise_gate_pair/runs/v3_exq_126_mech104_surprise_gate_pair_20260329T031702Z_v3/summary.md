# V3-EXQ-126 -- MECH-104: Volatility Gate / Unexpected Harm Surprise Spike

**Status:** PASS
**Claims:** MECH-104
**Design:** SURPRISE_GATE_ON vs SURPRISE_GATE_ABLATED x seeds [42, 123]
**SPIKE_MAGNITUDE:** 0.05  |  **SURPRISE_THRESHOLD:** 0.02
**Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Steps:** 200

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
| 42 | 208 | 205 | 0.050780 | 0.000000 |
| 123 | 211 | 208 | 0.050778 | 0.000000 |

## SURPRISE_GATE_ABLATED Results

| seed | n_unexpected | delta_var_unexpected | delta_var_expected |
|------|-------------|---------------------|-------------------|
| 42 | 226 | 0.000000 | 0.000000 |
| 123 | 212 | 0.000000 | 0.000000 |

## Discriminative Delta (ON - ABLATED, delta_var_unexpected)

| seed | discriminative_delta |
|------|---------------------|
| 42 | 0.050780 |
| 123 | 0.050778 |

## PASS Criteria

| Criterion | Result | Values |
|-----------|--------|--------|
| C1: ON delta_var_unexpected >= 0.005 (both seeds) | PASS | s42=0.050780, s123=0.050778 |
| C2: ON delta_var_expected < 0.002 (both seeds) | PASS | s42=0.000000, s123=0.000000 |
| C3: ABLATED delta_var_unexpected < 0.002 (both seeds) | PASS | s42=0.000000, s123=0.000000 |
| C4: (ON-ABLATED) delta_var_unexpected >= 0.004 (both seeds) | PASS | s42=0.050780, s123=0.050778 |
| C5: n_unexpected_harm_ON >= 10 (both seeds) | PASS | s42=208, s123=211 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 6/6 -> **PASS**

