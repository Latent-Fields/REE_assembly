# Literature Summary: LIT-0028 / Q-012

## Claim Tested

`Q-012` - Functional boundary of `z_delta` relative to `z_theta`.

## Source

- Murray JD et al. (2014), *A hierarchy of intrinsic timescales across primate cortex*, Nature Neuroscience.
- DOI: `10.1038/nn.3862`

## Mapping to REE

- The paper shows reliable temporal hierarchy: shorter intrinsic timescales in sensory-related areas and longer timescales in association/prefrontal regions.
- This supports modeling `z_delta` as a slower, context-integrating regime layer, while `z_theta` remains faster and more action-proximal.
- Practical implication for REE: allow `z_delta` updates at lower frequency and higher evidence thresholds than `z_theta`.

## Caveats and Mapping Limits

- Data are not expressed in REE latent variables; mapping is architectural rather than direct.
- The paper does not specify where commitment-gating boundaries should be placed.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.72`
- Rationale: strong empirical grounding for timescale separation, with moderate translation gap to exact REE wiring/thresholds.
