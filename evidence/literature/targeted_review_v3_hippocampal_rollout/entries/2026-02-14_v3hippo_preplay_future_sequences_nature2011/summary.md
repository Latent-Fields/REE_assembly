# Literature Summary: 2026-02-14_v3hippo_preplay_future_sequences_nature2011

## Claims Tested

- `MECH-033`

## Source

- Dragoi G, Tonegawa S (2011), *Preplay of future place cell sequences by hippocampal cellular assemblies*.
- URL: `https://doi.org/10.1038/nature09633`

## Mapping to REE

- The paper reports that sequential assemblies observed during rest can appear before first traversal of a novel route.
- This supports `MECH-033` because it is consistent with a reusable sequence-kernel mechanism that can be chained into future rollouts rather than reconstructed purely from immediate experience.

## Caveats and Mapping Limits

- Preplay is shown in spatial rodent paradigms and does not directly establish a software-level kernel API boundary.
- The work does not resolve how uncertainty/precision channels should be represented in such sequence kernels.
- No direct evidence is provided for commitment-stage gating or dual error channels.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.74`
- Rationale: strong biological evidence for anticipatory sequence primitives, with moderate translation gap to REE integration contract details.
