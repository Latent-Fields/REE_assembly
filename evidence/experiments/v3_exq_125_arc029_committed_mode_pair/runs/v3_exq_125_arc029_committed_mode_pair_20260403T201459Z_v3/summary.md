# V3-EXQ-125 -- ARC-029: Committed vs Ablated Mode Harm Outcomes (Matched-Seed Pair)

**Status:** FAIL
**Claims:** ARC-029
**Seeds:** [42]  |  **Warmup:** 3 eps  |  **Eval:** 2 eps x 20 steps
**Design:** 2x2 [COMMITTED_MODE_ON / COMMITTED_MODE_ABLATED] x [stable (drift=0.0) / volatile (drift=0.4, interval=3)]

## Design Rationale

ARC-029 predicts that the BG beta commitment gate (MECH-090) reduces harm in stable
environments by holding the agent to a well-evaluated trajectory, and that this
advantage narrows or reverses in volatile environments (where the committed trajectory
quickly becomes invalid as the layout changes).

Gate ablation: force `agent.e3._running_variance = commit_threshold + 0.1` and
`agent.e3._committed_trajectory = None` before each SELECT step. Same trained weights;
only the commitment gate is disabled.

Pre-registered thresholds: MIN_HARM_GAP_STABLE=0.0001,
VOLATILITY_MODULATION_RATIO=0.9.

Strengthens EXQ-063 (PASS 5/5, conf=0.774) with canonical seeds [42, 123].

## Per-Seed Results

| Seed | Act-Stab | Abl-Stab | Gap-Stab | Act-Vol | Abl-Vol | Gap-Vol | GapRatio |
|---|---|---|---|---|---|---|---|
| 42 | -0.00650 | 0.00572 | -0.01222 | -0.00658 | 0.00643 | -0.01301 | -1.064 |

## Aggregated (avg across seeds)

| Metric | Value |
|---|---|
| avg_harm_gap_stable | -0.01222 |
| avg_harm_gap_volatile | -0.01301 |
| avg_gap_ratio (volatile/stable) | -1.064 |

## PASS Criteria (ALL seeds)

| Criterion | Threshold | Result |
|---|---|---|
| C1: harm_gap_stable >= 0.0001 (both seeds) | 0.0001 | FAIL |
| C2: gap_volatile < gap_stable (both seeds) | strict inequality | PASS |
| C3: gap_ratio <= 0.9 (both seeds) | 0.9 | PASS |
| C4: committed steps > uncommitted in ON condition | majority | PASS |
| C5: zero committed steps in ABLATED condition | 0 | PASS |
| C6: no fatal errors | 0 | PASS |

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL seed=42: harm_gap_stable=-0.01222 < MIN=0.0001 (committed did not outperform ablated)
