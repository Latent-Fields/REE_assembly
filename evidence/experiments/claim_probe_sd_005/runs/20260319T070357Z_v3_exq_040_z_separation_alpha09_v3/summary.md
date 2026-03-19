# V3-EXQ-040 — SD-005 z_self/z_world Separation Revalidation (alpha_world=0.9)

**Status:** PASS
**alpha_world:** 0.9 (SD-008 fix)
**Training episodes:** 500
**Eval episodes:** 50 × 200 steps
**Seed:** 0
**Context:** EXQ-001 FAILed with world_selectivity_margin=−0.1252 at alpha_world=0.3.
This rerun tests whether SD-008 fix alone (alpha_world=0.9) restores positive selectivity.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_self/z_world corr < 0.8 | PASS | 0.0848 |
| C2: world_selectivity_margin > 0.0 | PASS | 0.0209 |
| C3: No fatal errors | PASS | 0 |

## Selectivity Metrics

- z_world ↔ world_delta correlation: 0.1624
- z_self  ↔ world_delta correlation: 0.1415
- z_self  ↔ body_delta correlation:  0.0349
- z_world ↔ body_delta correlation:  0.0676

## Interpretation

- C2 PASS → SD-008 fix alone restores functional z_world selectivity; SD-009 not required for baseline separation.
- C2 FAIL → SD-008 insufficient; SD-009 event contrastive supervision (EXQ-020) is necessary.

## Environment Metrics

- Mean survival: 181.6 steps
- Harm events: 2822 (agent-caused: 2624)
- Total residue: 5.2480
- Records: 9080
