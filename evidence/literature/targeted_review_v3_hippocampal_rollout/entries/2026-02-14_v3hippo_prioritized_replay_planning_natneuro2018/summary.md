# Literature Summary: 2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018

## Claims Tested

- `ARC-018`
- `MECH-033`
- `MECH-056`
- `MECH-060`

## Source

- Mattar MG, Daw ND (2018), *Prioritized memory access explains planning and hippocampal replay*.
- URL: `https://www.nature.com/articles/s41593-018-0232-z`

## Mapping to REE

- The paper formalizes replay selection using utility-like priorities (gain and need), reproducing forward and reverse replay properties linked to planning and learning.
- This aligns with REE’s need for selective rollout scheduling and supports trajectory-first update logic in `ARC-018` / `MECH-033`.
- It provides partial grounding for precision-weighted update pathways relevant to `MECH-056` and, more weakly, staged error routing in `MECH-060`.

## Caveats and Mapping Limits

- It is a computational account fit to known replay phenomena, not a direct measurement of a REE-style control plane.
- Gain/need priorities are not equivalent to REE ethical viability constraints; mapping remains functional rather than one-to-one.
- Evidence for explicit pre-commit versus post-commit channel separation is indirect.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.73`
- Rationale: coherent mechanistic fit to replay/planning signatures with moderate inferential distance to REE’s exact channelization claims.
