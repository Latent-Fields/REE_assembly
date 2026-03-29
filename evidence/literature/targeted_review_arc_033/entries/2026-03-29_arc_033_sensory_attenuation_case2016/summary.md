# Case et al. (2016) -- Encoding of Touch Intensity But Not Pleasantness in Human Primary Somatosensory Cortex

## What the paper did

Case and colleagues at the NIH ran a combined fMRI and rTMS study to determine whether primary somatosensory cortex (S1) encodes both the discriminative (intensity) and affective (pleasantness) qualities of touch, or whether these dimensions are handled by separate cortical areas. Participants received brushing stimulation on the hand during fMRI and rated both intensity and pleasantness. Separately, a group received inhibitory rTMS over S1 before repeated touch stimulation, with the vertex as a control site.

## Key findings relevant to ARC-033

Two clean results emerged. In the fMRI study, intensity ratings predicted S1 activation but pleasantness ratings predicted only ACC activation -- no S1 response to pleasantness variation. In the rTMS arm, S1 stimulation disrupted sensory discrimination (participants with reduced discrimination also rated subsequent touch as more intense, suggesting a renormalisation effect) but left pleasantness ratings unchanged. ACC-mediated pleasantness processing was causally independent of S1 integrity.

This constitutes a double dissociation with a causal component: S1 is both necessary and sufficient for intensity/discrimination encoding, while pleasantness is segregated to ACC. The separation is not merely correlational.

## Translation to ARC-033

ARC-033 argues that E2_harm_s should be a forward model on the sensory-discriminative harm stream. The design requires that z_harm_s is a relatively clean intensity/proximity encoding without heavy affective mixing, because action-conditional structure (moving away from a hazard reduces proximity) is more tractable when the signal is closer to a geometric/physical quantity than an affective blend.

Case et al. provide the strongest human experimental evidence that the discriminative channel is indeed clean -- S1's encoding of intensity is not contaminated by pleasantness processing. If the same logic holds for nociceptive harm signals (and the anatomical literature suggests it does, with S1 receiving neospinothalamic input for discriminative nociception), then z_harm_s based on HarmEncoder trained on harm_obs_s (proximity labels) should be a learnable forward model target.

The rTMS causal arm is particularly relevant: it shows that disrupting S1 affects intensity encoding but not affective processing. In REE terms, this is analogous to asking whether corrupting z_harm_s would degrade forward model accuracy without affecting z_harm_a. The answer from biology is yes, which supports the architectural independence of the two streams.

## Limitations and caveats

The paper uses C-tactile afferent mediated affective touch, which is innocuous and uses a distinct fibre class (CT afferents) from nociceptive harm signals (A-delta and C polymodal nociceptors). The channel separation demonstrated for affective touch may not generalise with the same clarity to the harm domain, where the spinothalamic pathway complexity means there is more overlap at early processing stages. EXQ-095b's finding that harm_obs_s has near-zero variance in many episodes suggests that even if the channel is clean, sparsity remains a challenge for forward model learning.

## Confidence reasoning

Excellent source quality (JNeurosci, fMRI + causal rTMS, NIH lab). The mapping to ARC-033 is conceptually valid but requires a transfer from innocuous affective touch to nociceptive harm. Mapping fidelity is moderate because of this transfer. Overall confidence 0.62.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1523/JNEUROSCI.1130-15.2016
