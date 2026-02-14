# Literature Summary: 2026-02-14_v3hippo_bidirectional_replay_sequences_natneuro2007

## Claims Tested

- `ARC-018`

## Source

- Diba K, Buzsaki G (2007), *Forward and reverse hippocampal place-cell sequences during ripples*.
- URL: `https://doi.org/10.1038/nn1961`

## Mapping to REE

- The study reports forward sequential activity before runs and reverse sequential activity after runs, both expressed during sharp-wave ripple events.
- This pattern supports `ARC-018` by showing a hippocampal mechanism that can move across candidate trajectory structure in direction-dependent ways, consistent with rollout viability mapping rather than static memory replay.

## Caveats and Mapping Limits

- Task context is rodent linear-track navigation; direct transfer to abstract latent viability mapping in REE is inferential.
- The paper does not define an explicit viability scalar or commitment operator, so REE-specific policy integration remains untested.
- Temporal replay directionality is informative but not sufficient to validate full E1/E2 lane interfaces.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.75`
- Rationale: direct neural sequence evidence aligns with rollout mapping mechanics, with moderate architecture translation gap.
