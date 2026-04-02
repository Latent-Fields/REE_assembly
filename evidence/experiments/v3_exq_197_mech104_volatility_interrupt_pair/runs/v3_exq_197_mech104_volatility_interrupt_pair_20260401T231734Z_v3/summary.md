# V3-EXQ-197 -- MECH-104: Volatility Interrupt Discriminative Pair

**Status:** PASS
**Claims:** MECH-104
**Decision:** retain_ree
**Design:** SURPRISE_GATE_ACTIVE vs SURPRISE_GATE_ABLATED x seeds [42, 7, 13]
**SPIKE_MAGNITUDE:** 0.05  |  **SURPRISE_THRESHOLD:** 0.02
**Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Steps:** 200

## Design Rationale

MECH-104 (LC-NE volatility interrupt) predicts that unexpected harm events spike
commitment uncertainty (running_variance) via a surprise gate. This is the Route-2
validation: norepinephrine release is driven by unexpected outcomes, not routine harm
or background jitter.

Prior evidence: EXQ-049e (Route-1 jitter), EXQ-061 (any-harm spike), EXQ-064 (Route-2
single seed 5/5), EXQ-126 (matched-pair 2 seeds 6/6). All PASS but lacked the
definitive 3-seed matched-seed discriminative pair with pre-registered thresholds.

This experiment provides the final matched-seed pair:
(1) Three seeds [42, 7, 13] for cross-seed replication.
(2) SURPRISE_GATE_ACTIVE vs SURPRISE_GATE_ABLATED on the SAME trained agent per seed.
(3) Pre-registered numeric thresholds for all 6 criteria.

## SURPRISE_GATE_ACTIVE Results

| seed | n_unexpected | n_spikes | delta_var_unexpected | delta_var_expected |
|------|-------------|---------|---------------------|--------------------|
| 42 | 208 | 205 | 0.050780 | 0.000000 |
| 7 | 191 | 187 | 0.050599 | 0.000000 |
| 13 | 218 | 217 | 0.050915 | 0.000000 |

## SURPRISE_GATE_ABLATED Results

| seed | n_unexpected | delta_var_unexpected | delta_var_expected |
|------|-------------|---------------------|-------------------|
| 42 | 208 | 0.000000 | 0.000000 |
| 7 | 191 | 0.000000 | 0.000000 |
| 13 | 218 | 0.000000 | 0.000000 |

## Discriminative Delta (ACTIVE - ABLATED, delta_var_unexpected)

| seed | discriminative_delta |
|------|---------------------|
| 42 | 0.050780 |
| 7 | 0.050599 |
| 13 | 0.050915 |

## PASS Criteria (pre-registered, all must hold across all 3 seeds)

| Criterion | Result | Values |
|-----------|--------|--------|
| C1: ACTIVE delta_var_unexpected >= 0.005 (each seed) | PASS | s42=0.050780, s7=0.050599, s13=0.050915 |
| C2: ACTIVE delta_var_expected < 0.002 (each seed) | PASS | s42=0.000000, s7=0.000000, s13=0.000000 |
| C3: ABLATED delta_var_unexpected < 0.002 (each seed) | PASS | s42=0.000000, s7=0.000000, s13=0.000000 |
| C4: (ACTIVE-ABLATED) delta >= 0.004 (each seed) | PASS | s42=0.050780, s7=0.050599, s13=0.050915 |
| C5: n_unexpected_harm_ACTIVE >= 10 (each seed) | PASS | s42=208, s7=191, s13=218 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 6/6 -> **PASS**

## Decision Scoring

| Criteria met | Decision |
|--------------|----------|
| 6/6 | retain_ree (supports MECH-104) |
| 4-5/6 | inconclusive (mixed evidence) |
| <=3/6 | retire_ree_claim (weakens MECH-104) |

**This run:** 6/6 -> **retain_ree**

