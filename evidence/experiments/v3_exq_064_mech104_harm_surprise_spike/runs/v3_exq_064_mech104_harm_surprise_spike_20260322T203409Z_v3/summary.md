# V3-EXQ-064 -- MECH-104: Harm-Surprise Spike (Route-2 Validation)

**Status:** PASS
**Claims:** MECH-104
**Design:** Two-condition -- Condition A: surprise-gated spike (Route-2) vs Condition B: no-spike baseline
**spike_magnitude:** 0.05  |  **surprise_threshold:** 0.02  |  **Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Seed:** 0

## Design Rationale

Route-2 MECH-104: the surprise gate fires selectively on UNEXPECTED harm events
(|actual_harm - predicted_harm| > surprise_threshold). Expected harm does not trigger
a spike because the agent already anticipated it -- no new information, no LC-NE release.

Prior validation:
- EXQ-049e PASS: Route-1 (jitter noise floor) prevents variance collapse.
- EXQ-061  PASS: Route-1 (any harm contact) triggers variance spike.
- EXQ-062b tests SELECTIVITY (fewer spikes than always-gate).
- This experiment tests the SIGNAL: variance rises specifically on unexpected harm steps.

## Training

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Committed? (variance < 0.4000) | Yes |

## Variance Response to Harm Events

| | Condition A (surprise-gated) | Condition B (baseline) |
|---|---|---|
| n_unexpected_harm | 237 | 234 |
| n_expected_harm | 0 | 0 |
| n_surprise_spikes | 235 | 0 |
| delta_var_unexpected | 0.051113 | 0.000000 |
| delta_var_expected | 0.000000 | 0.000000 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: A delta_var_unexpected > 0.005 (spike fires on unexpected) | PASS | 0.051113 |
| C2: A delta_var_expected < 0.002 (gate selective on expected) | PASS | 0.000000 |
| C3: B delta_var_unexpected < 0.002 (baseline stays flat) | PASS | 0.000000 |
| C4: n_unexpected_harm_A >= 10 (sufficient events) | PASS | 237 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 -> **PASS**

