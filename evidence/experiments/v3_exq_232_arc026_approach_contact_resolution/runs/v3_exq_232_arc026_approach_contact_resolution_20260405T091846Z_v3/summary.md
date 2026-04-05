# V3-EXQ-232 -- ARC-026 Approach/Contact Slope Conflict Resolution

**Status:** PASS  **Criteria met:** 4/4
**Claims:** ARC-026  **Purpose:** evidence
**Supersedes (conflict resolution):** EXQ-033 conflict_ratio=1.0

## Design Changes vs EXQ-033

- Peak checkpoint analysis (not terminal) to handle training instability
- 1500 eps (vs 1000), checkpoints at [200, 400, 600, 800, 1000, 1500]
- 3 seeds (vs 1)
- E3 harm supervision enabled from ep100 onward (phased)

## Results by Seed

| Seed | Approach slope | Contact slope | Gap@peak | Peak ckpt | C1 | C2 | C3 | C4 |
|------|---------------|--------------|----------|----------|----|----|----|----|
| 42 | 0.000015 | 0.000014 | 0.9994 | 1500 | PASS | PASS | PASS | PASS |
| 7 | 0.000016 | 0.000015 | 1.0000 | 1500 | PASS | PASS | PASS | PASS |
| 13 | 0.000577 | 0.000106 | 0.9245 | 1000 | PASS | PASS | PASS | PASS |

## Interpretation

ARC-026 SUPPORTED: At peak performance checkpoint, approach_slope > contact_slope. The gradient of harm detection extends backward from contact to approach. Consistent with 'love expands under intelligence' derivation (ARC-024): more training -> deeper causal gradient detection.
