# Literature Summary: 2026-03-19_mech103_venezia_2017_sts_streams

## Claims Tested

- `MECH-103`

## Source

- Venezia JH, Vaden KI, Rong F, Maddox D, Saberi K, Hickok G (2017). *Auditory, Visual and Audiovisual Speech Processing Streams in Superior Temporal Sulcus*. Frontiers in Human Neuroscience, 11, 174.
- DOI: `10.3389/fnhum.2017.00174`
- URL: `https://pubmed.ncbi.nlm.nih.gov/28439236/`

## Source Wording

STS has an anterior-posterior functional gradient: auditory speech is processed in anterior STS, visual speech in posterior STS, and multisensory integration occurs in mid-STS. Mid-STS preferentially responds to multisensory stimulation and speech over non-speech. A subregion of posterior STS distinguishes visual speech from non-speech at an abstract level, independent of low-level motion kinematics.

## REE Translation

**MECH-103**: The different exteroceptive modality streams have their own spatial loci in the convergence zone before arriving at the shared world latent. In E1 implementation terms, this argues for modality-specific encoder heads with their own intermediate representations that converge on z_world — not a single encoder applied to raw multimodal input. Each modality encodes abstract features (visual speech = abstract articulatory information, not raw motion) before fusion, which is why multi-source convergence improves world representation accuracy: each stream contributes complementary, pre-processed information rather than redundant raw signal.

## Caveat

fMRI spatial resolution limits mechanistic claims. Speech-specific paradigm. The gradient organization may not map directly onto non-biological sensory systems, though the convergence-zone principle does.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
