# V3-EXQ-062a -- MECH-104: Surprise-Gated Volatility Interrupt (Committed-Only Fix)

**Status:** FAIL
**Claims:** MECH-104, MECH-090
**Design:** Single trained agent; 3 interrupt policies (none / always / surprise-gated), committed-only
**Fix vs EXQ-062:** Interrupt fires on committed steps only, breaking the positive feedback loop
**spike_magnitude:** 0.05  |  **surprise_threshold:** 0.02  |  **Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Seed:** 0

## EXQ-062 Failure and Fix

EXQ-062 FAIL on C4: surprise-gated produced MORE uncommitted steps than always-spike
(selectivity_ratio > 1.0). Root cause: the interrupt fired regardless of committed state.
Once uncommitted, noisier predictions amplified surprise -> more spikes -> positive feedback.

Fix: both interrupt policies only fire when `agent.e3._running_variance < commit_threshold`
(i.e., the agent is still committed). Once de-committed, no further spikes are added.
This ensures the selectivity comparison is valid: both policies fire from the same
committed baseline and the surprise gate's selectivity can be measured cleanly.

## Training

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Committed? (variance < 0.40) | Yes |

## Eval Results

| Condition | Policy | n_uncommitted | n_committed_harm | n_spikes |
|---|---|---|---|---|
| A | None (baseline) | 0 | 237 | -- |
| B | Always-spike (committed only) | 1534 | 229 | 229 |
| C | Surprise-gated (committed only) | 2303 | 215 | 215 |

Selectivity ratio (C/B): 1.501  (target: < 0.80)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: n_uncommitted_A == 0 (baseline collapse) | PASS | 0 |
| C2: n_uncommitted_B > 100 (always-spike works) | PASS | 1534 |
| C3: n_uncommitted_C > 30 (surprise fires on genuine events) | PASS | 2303 |
| C4: n_uncommitted_C < n_B x 0.80 (surprise is more selective) | FAIL | 2303 vs 1227 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 -> **FAIL**

## Failure Notes

- C4 FAIL: n_uncommitted_C=2303 not < 1227 (= n_always x 0.80) (surprise-gating not more selective than always-spike)
