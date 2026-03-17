# Literature Summary: 2026-03-17_mech096_separate_visual_pathways_goodale1992

## Claims Tested

- `MECH-096`

## Source

- Goodale MA, Milner AD (1992). *Separate visual pathways for perception and action*. Trends in Neurosciences, 15, 20–25.
- DOI: `10.1016/0166-2236(92)90344-8`
- URL: `https://pubmed.ncbi.nlm.nih.gov/1374953/`

## Source Wording

The primate visual system bifurcates from V1 into two anatomically distinct cortical streams. The dorsal stream (V1→MT→posterior parietal cortex) processes visuospatial information in egocentric coordinates to guide action — it encodes where objects are relative to the body and how the body must move to interact with them. The ventral stream (V1→V4→inferotemporal cortex) processes object identity, shape, and colour for recognition and sustained perceptual representation. The streams operate at different temporal scales (dorsal: fast, transient; ventral: slower, sustained) and remain anatomically separate throughout the cortical hierarchy. Patient DF, with selective damage to the ventral stream (visual form agnosia), cannot recognize object orientation but can accurately orient her hand to grasp objects — demonstrating functional dissociation between the two streams.

## REE Translation

**MECH-096 (dual-stream observation encoder)**: The dorsal/ventral distinction grounds the requirement that SD-005's observation encoder must have two anatomically motivated output heads, not a single encoder with a learned routing gate.

- **Dorsal-equivalent head** → z_self: encodes egocentric body-relative information (where am I, what can my body do, what is the spatial relationship between my body and nearby objects), at high temporal resolution. This feeds E2's motor-sensory prediction.
- **Ventral-equivalent head** → z_world: encodes allocentric object-identity information (what objects exist, what are their properties and causal affordances), at sustained temporal resolution. This feeds E3's world model and hippocampal map.

A single learned routing gate is insufficient because: (1) the two streams process structurally different features with different temporal dynamics; (2) gradient pressure during end-to-end training will cause a shared encoder to re-merge them toward z_gamma-style conflation; (3) the biological architecture shows these streams remain structurally separate at every level of the hierarchy — their separation is not a learned emergent property but an architectural commitment. This constrains the V3 encoder design: SD-005 requires two encoder heads as an architectural commitment, not as an emergent learning outcome.

## Caveat

The dorsal/ventral distinction was developed for primate visual processing; REE operates on arbitrary observation spaces. The structural principle (egocentric/action-relevant and allocentric/identity-relevant channels must be architecturally separate) generalises beyond vision, but the specific temporal scale differences and hierarchical separation topology may not transfer to all modality types without further analysis.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.82`
