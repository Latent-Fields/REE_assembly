# Literature Summary: 2026-03-19_mech103_zhang_2025_seeg_sts_audiovisual

## Claims Tested

- `MECH-103`

## Source

- Zhang Y et al. (2025). *Stereoelectroencephalography Reveals Neural Signatures of Multisensory Integration in the Human Superior Temporal Sulcus during Audiovisual Speech Perception*. Journal of Neuroscience, 45(42).
- DOI: `10.1523/JNEUROSCI.1037-25.2025`
- URL: `https://pubmed.ncbi.nlm.nih.gov/40930977/`

## Source Wording

Direct intracranial sEEG recordings from 42 patients show that a subpopulation of STS electrodes responds to both auditory speech (71ms latency) and visual speech (109ms latency). Audiovisual responses in mid-posterior STS are 40% faster and 18% larger than auditory-only. STS response latencies for audiovisual stimuli were faster than those in STG, suggesting a parallel-pathway model: STG handles auditory-only processing, STS handles multisensory integration.

## REE Translation

**MECH-103**: Different exteroceptive modalities converge on E1's world latent via pathways with distinct temporal profiles (auditory faster, visual slower). The integration zone (STS-equivalent in E1) produces responses that are qualitatively different from either modality alone — faster and larger. This directly supports the MECH-103 claim that multi-source fusion produces more accurate world representations than single-modality input: the integrator is faster and more sensitive than the individual pathways it combines. E1's encoder architecture should reflect this: modality-specific pathways feeding a shared integration mechanism, not concatenated raw inputs to a single encoder.

## Caveat

Speech perception paradigm; epilepsy patients. The 40%/18% improvement figures are speech-specific. The convergence-at-shared-latent principle generalises; the quantitative gains may not.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.85`
