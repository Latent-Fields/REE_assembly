# V3-EXQ-044 — Unified vs Split Latent Ablation

**Status:** FAIL (4/5 criteria)
**Conditions:** split (z_self≠z_world) vs unified (z_self=z_world=avg)
**alpha_world:** 0.9  **Warmup:** 500 eps  **Eval:** 50 eps

## PASS Criteria

| Criterion | Split | Unified | Pass? |
|---|---|---|---|
| C1: cal_gap_approach split > unified+0.05 | 0.1915 | 0.1577 | FAIL |
| C2: attribution_gap split > unified+0.01 | 0.0345 | 0.0189 | PASS |
| C3: cal_gap_split > 0.10 | 0.1915 | — | PASS |
| C4: attr_gap_split > 0.0 | 0.0345 | — | PASS |
| C5: n_approach >= 50 | 832 | — | PASS |

## World-Forward R²

- Split: 0.9472
- Unified: 0.9624

## Interpretation

- **C1 PASS → C2 PASS**: Latent split provides advantage on both calibration and attribution.
  SD-005 confirmed as efficiency-relevant (not just attribution-relevant).
- **C1 FAIL, C2 PASS**: Split helps attribution but not harm detection calibration.
  Consistent with EXQ-034 finding that E2 ablation doesn't hurt calibration.
- **Both FAIL**: Latent split provides no measurable advantage over unified representation.
  Efficiency gains are from module specialization (EXQ-034) and SD-004 action objects, not encoding split.
