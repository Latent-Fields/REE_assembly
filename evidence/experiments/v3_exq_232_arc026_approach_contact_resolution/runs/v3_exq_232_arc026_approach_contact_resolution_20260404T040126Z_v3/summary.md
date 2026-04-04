# V3-EXQ-232 -- ARC-026 Approach/Contact Slope Conflict Resolution

**Status:** FAIL  **Criteria met:** 2/4
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
| 42 | 0.000005 | 0.000004 | 0.5310 | 20 | PASS | PASS | FAIL | FAIL |
| 7 | 0.000000 | 0.000000 | 0.5344 | 10 | FAIL | PASS | FAIL | FAIL |
| 13 | 0.000013 | -0.000031 | 0.0012 | 20 | PASS | FAIL | FAIL | FAIL |

## Interpretation

ARC-026 PARTIAL: Some slope evidence but below full threshold. May need longer training or higher hazard_harm signal.

## Failure Notes

- C3 FAIL: n_approach_at_peak < 15: [12, 12, 10]
- C4 FAIL: peak_checkpoint < 400: [20, 10, 20]
