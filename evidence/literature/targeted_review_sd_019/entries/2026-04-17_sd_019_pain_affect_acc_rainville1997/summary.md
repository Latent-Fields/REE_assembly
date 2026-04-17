# Pain affect encoded in human anterior cingulate but not somatosensory cortex
**Rainville, P., Duncan, G. H., Price, D. D., Carrier, B., & Bushnell, M. C. (1997). *Science*, 277(5328), 968-971.**
DOI: [10.1126/science.277.5328.968](https://doi.org/10.1126/science.277.5328.968)

## What the study did

Rainville and colleagues used hypnotic suggestion as a precision tool to dissect the components of pain experience. In a PET imaging study, highly hypnotizable subjects received noxious heat (47 degrees C) to the hand while hypnotic suggestions selectively altered either the perceived unpleasantness of the pain (without changing its perceived intensity) or left both dimensions unaltered. Cerebral blood flow was measured across conditions. The central prediction was that if pain affect and pain intensity are processed by separate neural substrates, then selectively manipulating unpleasantness should produce changes in affect-related areas while leaving sensory-discriminative areas intact.

## Key findings

The result was unambiguous. Suggestions that increased or decreased pain unpleasantness produced significant changes in activity within the anterior cingulate cortex (ACC) -- a region long associated with emotional processing and limbic function. Primary somatosensory cortex (S1) activation, by contrast, was unchanged. A companion paper (Hofbauer et al., 2001) completed the double dissociation by showing that selectively modulating intensity produced changes in S1 without corresponding ACC changes. Together the papers establish that pain intensity and pain unpleasantness are represented by neuroanatomically separable substrates in humans -- neither dimension is simply a linear transform of the other at the cortical level.

## Relevance to SD-019

SD-019 (affective_harm_nonredundancy_constraint) requires that z_harm_a, the affective harm stream, must encode a representationally distinct signal from z_harm_s, the sensory-discriminative stream -- specifically one that captures temporally integrated threat burden rather than a smoothed or monotone-transformed copy of immediate hazard intensity. The Rainville result provides perhaps the most direct biological support available: the brain itself implements exactly this dissociation, with ACC (the biological homologue of z_harm_a's output target) tracking a dimension of nociceptive experience that can be independently altered without touching the sensory-discriminative representation in S1 (the homologue of z_harm_s's output target).

## Limitations and caveats

The manipulation is top-down (hypnotic suggestion), not a test of the input-level architecture. It is possible that the dissociation observed here reflects a cortical gating or attentional mechanism rather than genuinely independent input streams. This matters for SD-019 because the claim is about the representational architecture of the harm streams themselves, not about whether they can be uncoupled by downstream cognitive processes. Additionally, the Rainville paradigm tests steady-state unpleasantness modulation, not the specific temporal-integration dynamics emphasized in SD-019 -- a design that would require manipulating the history of threat exposure independently of current stimulus intensity, which is harder to implement with hypnosis. The proxy gap between thermal pain applied to the hand and the composite harm observations in CausalGridWorldV2 should also be noted: the biological system does not face a heal-rate parameter or a 4-directional limb damage register.

## Confidence reasoning

The source quality is near-ceiling: landmark Science paper, replicated by the same group and many others, now a textbook result. Mapping fidelity is high for the core nonredundancy claim but attenuated for the specific temporal-integration mechanism. The result is taken as converging support for the principle that z_harm_a and z_harm_s are nonredundant by design, grounded in the same biological dissociation that motivated their architecturally separate treatment.
