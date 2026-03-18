# V3-EXQ-001 — SD-005 z_self/z_world Channel Separation

**Status:** PASS
**Training episodes:** 10
**Eval episodes:** 20 × 200 steps
**Seed:** 0

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_self/z_world corr < 0.8 | PASS | 0.1134 |
| C2: world_selectivity_margin > 0.0 (trained) | PASS | 0.0683 |
| C3: No fatal errors | PASS | 0 |

## Selectivity Metrics

- z_world ↔ world_delta correlation: 0.2562
- z_self  ↔ world_delta correlation: 0.1879
- z_self  ↔ body_delta correlation:  0.1845
- z_world ↔ body_delta correlation:  0.3210

## Environment Metrics

- Mean survival: 200.0 steps
- Harm events: 4 (agent-caused: 0)
- Total residue: 0.0000
- Records: 4000
