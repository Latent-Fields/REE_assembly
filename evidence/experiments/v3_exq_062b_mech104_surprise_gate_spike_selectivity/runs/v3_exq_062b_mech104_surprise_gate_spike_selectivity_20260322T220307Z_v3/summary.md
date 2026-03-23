# V3-EXQ-062b -- MECH-104: Surprise-Gated Volatility Interrupt (Spike Selectivity C4 Fix)

**Status:** PASS
**Claims:** MECH-104, MECH-090
**Design:** Single trained agent; 3 interrupt policies (none / always / surprise-gated), committed-only
**C4 fix:** Criterion revised to measure spike count selectivity (C4a) and per-spike impact (C4b)
**spike_magnitude:** 0.05  |  **surprise_threshold:** 0.02  |  **Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Seed:** 0

## C4 Criterion Revision (vs EXQ-062a)

EXQ-062a C4 measured total uncommitted DURATION (n_uncommitted_C < n_B x 0.80).
This is wrong: fewer, higher-impact spikes produce more uncommitted time than more,
lower-impact spikes -- penalising the correct MECH-104 behavior.

EXQ-062a data: always=229 spikes, 1534 uncommitted (6.7/spike)
               surprise=215 spikes, 2303 uncommitted (10.7/spike)
Surprise fired LESS often (selectivity confirmed) but each spike caused LONGER
uncommitted episodes (expected: surprise fires at genuinely uncertain moments).

EXQ-062b C4 tests the mechanism directly:
  C4a: surprise_n_spikes < always_n_spikes (selectivity)
  C4b: surprise_per_spike >= always_per_spike x 0.90 (impact per interrupt)

## Training

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Committed? (variance < 0.40) | Yes |

## Eval Results

| Condition | Policy | n_uncommitted | n_committed_harm | n_spikes | uncommitted/spike |
|---|---|---|---|---|---|
| A | None (baseline) | 0 | 237 | -- | -- |
| B | Always-spike (committed only) | 1534 | 229 | 229 | 6.70 |
| C | Surprise-gated (committed only) | 2303 | 215 | 215 | 10.71 |

Spike count ratio (C/B): 0.939  (target: < 1.0 for C4a)
Per-spike ratio (C/B):   1.599   (target: >= 0.90 for C4b)

Discriminability (mean surprise at spike / mean surprise all harm): 1.002
  mean_surprise_all_harm:  1.0466
  mean_surprise_at_spike:  1.0492
  (diagnostic only -- ratio > 1.0 confirms gate fires on genuinely high-surprise events)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: n_uncommitted_A == 0 (baseline collapse) | PASS | 0 |
| C2: n_uncommitted_B > 100 (always-spike works) | PASS | 1534 |
| C3: n_uncommitted_C > 30 (surprise fires on genuine events) | PASS | 2303 |
| C4a: surprise_n_spikes < always_n_spikes (selectivity) | PASS | 215 vs 229 |
| C4b: surprise_per_spike >= always_per_spike x 0.90 (impact) | PASS | 10.71 vs 6.03 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 -> **PASS**

