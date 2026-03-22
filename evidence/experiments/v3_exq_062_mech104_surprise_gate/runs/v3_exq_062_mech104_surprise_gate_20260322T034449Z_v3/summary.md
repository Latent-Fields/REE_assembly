# V3-EXQ-062 — MECH-104: Surprise-Gated Volatility Interrupt

**Status:** FAIL
**Claims:** MECH-104, MECH-090
**Design:** Single trained agent; 3 interrupt policies (none / always / surprise-gated)
**spike_magnitude:** 0.05  |  **surprise_threshold:** 0.02  |  **Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Seed:** 0

## Design Rationale

EXQ-061 (PASS) confirmed the jitter mechanism is wired. EXQ-062 tests *selectivity*:
does the surprise-gated policy de-commit less often than the always-spike policy?
MECH-104 requires the interrupt to fire on genuine prediction errors, not routine harm.
C4 operationalises this: surprise-gated must produce <80% of always-spike's de-commitments.

## Training

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Committed? (variance < 0.40) | Yes |

## Eval Results

| Condition | Policy | n_uncommitted | n_spikes |
|---|---|---|---|
| A | None (baseline) | 0 | — |
| B | Always-spike | 1534 | 234 |
| C | Surprise-gated | 2303 | 223 |

Selectivity ratio (C/B): 1.501

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: n_uncommitted_A == 0 (baseline collapse) | PASS | 0 |
| C2: n_uncommitted_B > 100 (always-spike works) | PASS | 1534 |
| C3: n_uncommitted_C > 30 (surprise fires on genuine events) | PASS | 2303 |
| C4: n_uncommitted_C < n_B × 0.80 (surprise is more selective) | FAIL | 2303 vs 1227 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C4 FAIL: n_uncommitted_C=2303 not < 1227 (= n_always × 0.80) (surprise-gating not more selective than always-spike)
