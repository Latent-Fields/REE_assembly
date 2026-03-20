# Literature Summary: 2026-03-19_mech103_nath_beauchamp_2011_sts_reliability_weighting

## Claims Tested

- `MECH-103`

## Source

- Nath AR, Beauchamp MS (2011). *Dynamic changes in superior temporal sulcus connectivity during perception of noisy audiovisual speech*. Journal of Neuroscience, 31(5), 1704–1714.
- DOI: `10.1523/JNEUROSCI.4853-10.2011`
- URL: `https://pubmed.ncbi.nlm.nih.gov/21289179/`

## Source Wording

STS functional connectivity with auditory cortex increases when auditory input is more reliable (less noisy) and with visual cortex when visual input is more reliable. These changes occur dynamically, even with word-by-word reliability fluctuations. Behavioral perception tracks reliability: subjects perceive incongruent audiovisual syllables as the more reliable modality.

## REE Translation

**MECH-103**: The precision-weighted aspect of exteroceptive fusion is directly demonstrated. Different modalities do not contribute to E1's world latent with fixed weights — contribution is dynamically gated by reliability. This connects MECH-103 to INV-008 (precision is routed): at the WORLD stream input stage, each modality's contribution to z_world is precision-weighted. This has direct implementation implications: E1's multi-stream encoder should include online reliability/precision signals per modality, not just a fixed-weight fusion layer. The dynamic, rapid nature of the weighting (word-by-word) indicates this is an active online process, not slow adaptation.

## Caveat

STS connectivity is an indirect proxy for actual weighting. Speech-specific paradigm. Time scales of reliability fluctuation in REE environments may differ. The precision-weighting principle generalises; the word-by-word dynamics are speech-specific.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.80`
