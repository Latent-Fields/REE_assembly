# V3-EXQ-063a -- ARC-029: Committed vs Ablated Mode Harm Outcomes (2x2, R-c gate)

**Status:** PASS
**Claims:** ARC-029
**Design:** 2x2 [gate_active / gate_ablated] x [stable (drift=0.0) / volatile (drift=0.4, interval=3)]
**Seeds:** [0, 1]  |  **Warmup:** 400 eps  |  **Eval:** 50 eps

## Design Rationale

ARC-029 predicts that the BG beta commitment gate (MECH-090) reduces harm in stable
environments by holding the agent to a well-evaluated trajectory, and that this
advantage narrows or reverses in volatile environments where the committed trajectory
quickly becomes invalid as the layout changes.

Gate ablation: force `agent.e3._running_variance = commit_threshold + 0.1` and
`agent.e3._committed_trajectory = None` before each SELECT step. This keeps the
agent permanently uncommitted -- policy re-evaluates freshly every step. Same trained
weights; only the commitment gate is disabled.

harm_gap = harm_gate_active - harm_gate_ablated (positive = committed is better)

## Results

| Condition | Mean Harm/Step |
|---|---|
| Gate Active, Stable | -0.05521 |
| Gate Ablated, Stable | -0.07573 |
| Gate Active, Volatile | -0.05674 |
| Gate Ablated, Volatile | -0.06731 |

| Gap | Value |
|---|---|
| harm_gap_stable (committed advantage) | 0.02051 |
| harm_gap_volatile (committed advantage) | 0.01057 |
| gap_reduction_ratio (volatile/stable) | 0.515 |

## Commitment Gate Sanity

| Metric | Value |
|---|---|
| n_committed_active_stable (avg) | 1156 |
| n_uncommitted_active_stable (avg) | 0 |
| n_committed_ablated_stable (avg) | 0 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_gap_stable > 0 (committed better in stable) | PASS | 0.02051 |
| C2: harm_gap_volatile < harm_gap_stable (narrows in volatile) | PASS | 0.01057 vs 0.02051 |
| C3: committed cond has more committed than uncommitted steps | PASS | 1156 vs 0 |
| C4: ablated cond has zero committed steps | PASS | 0 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 -> **PASS**

