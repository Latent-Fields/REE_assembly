# Literature Summary: 2026-02-13_mech058_ijepa_target_encoder_anchor

## Claims Tested

- `MECH-058`

## Source

- Assran J-B, Duval Q, Misra I, Bojanowski P, Vincent P, Rabbat M, LeCun Y (2023), *Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture*.
- URL: `https://arxiv.org/abs/2301.08243`

## Mapping to REE

- I-JEPA uses a slow target-encoder pathway (momentum/EMA style updates) against a faster predictor pathway.
- This supports the REE claim that substrate stability benefits from explicit slow/fast separation, aligning with E1-like anchoring vs E2-like adaptation.

## Caveats and Mapping Limits

- The paper does not define REE E1/E2 modules directly.
- It does not test commitment-gated responsibility flow; mapping is substrate-level.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.74`
- Rationale: direct evidence for target-anchor stabilization, moderate abstraction gap to REE architecture semantics.
