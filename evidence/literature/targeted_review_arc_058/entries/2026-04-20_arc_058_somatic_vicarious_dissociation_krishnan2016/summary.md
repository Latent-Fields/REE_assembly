# Krishnan et al 2016 -- Somatic vs vicarious pain dissociation

## What the paper did

Krishnan and colleagues asked whether somatic pain (experienced directly) and vicarious pain (observing others in pain) share brain representations, as "shared experience" theories of empathy propose, or whether they are supported by dissociable circuits. In a primary fMRI study, they used multivariate pattern analysis to derive two distinct signatures -- one trained on somatic thermal pain, one on vicarious pain from photographs -- and tested out-of-sample classification of each against the other. Two additional studies tested (a) whether the somatic pattern generalises from thermal to mechanical and electrical pain, and (b) whether the somatic/vicarious dissociation replicates.

## Key findings relevant to ARC-058

The somatic and vicarious patterns were fully dissociable: each predicted its own target condition at 100% and the other at chance. The somatic pattern generalised across somatic sub-modalities (thermal, mechanical, electrical). The somatic/vicarious dissociation replicated. The somatic pattern loaded on thalamus, dorsal posterior insula, S1/S2, ACC -- the classical nociceptive-ascending stack. The vicarious pattern loaded on mentalising regions: TPJ, STS, ventromedial PFC.

ARC-058 cares about two architectural questions here. First, does a forward-model trunk exist across somatic-pain sub-modalities, or is each nociceptive sub-modality independent? The within-somatic generalisation answers cleanly: yes, a shared somatic-pain substrate exists. This is the z_harm_s case in the REE spec and ARC-058 is supported. Second, how large does the modality gap have to be before patterns become dissociable? Somatic vs vicarious is large enough to produce full dissociation -- but this is a much larger gap than the z_harm_s vs z_harm_a distinction ARC-058 actually draws.

## How this translates to REE

For ARC-058's within-somatic claim (that z_harm_s shares substrate across nociceptive sub-modalities), this paper is strong direct evidence. The REE dual-stream model in SD-011 posits a sensory-discriminative z_harm_s that integrates across A-delta/C-fibre inputs; the NPS generalising from thermal to mechanical to electrical is the biology behind exactly that integration.

For ARC-058's between-stream claim (that z_harm_s and z_harm_a share a trunk), Krishnan 2016 is less direct. The somatic/vicarious contrast is not the right contrast -- vicarious pain is about social cognition, not about the affective component of self-experienced pain. The Woo 2017 SIIPS1 paper is the better arbiter for that question. What Krishnan 2016 contributes by analogy is a calibration point: at sufficiently large architectural gaps, cerebral signatures ARE fully dissociable, so the absence of such dissociation within pain (as Horing & Buchel 2022 find for unsigned AIC PE) is informative evidence for a shared upstream substrate.

## Limitations and caveats

The somatic vs vicarious contrast is not the within-pain affective-vs-sensory split. Generalising the "dissociable patterns" finding from vicarious pain to z_harm_a requires assuming the z_harm_a stream is architecturally similar to the vicarious-pain substrate, which is probably wrong -- z_harm_a is a first-person affective stream, not a mentalising readout.

The within-somatic generalisation is clean for the NPS's sensory-discriminative core, but the NPS also includes ACC and AIC components that the Krishnan paper does not separately decompose. Whether the generalisation is driven by shared dpIns, shared AIC, or both is not resolved here; Horing & Buchel 2022 is the paper that does that decomposition.

## Confidence reasoning

Confidence 0.72. Source quality is good (eLife, three-study design, cross-sub-modality replication). Mapping fidelity is moderate (0.60) -- the within-somatic generalisation is directly relevant to ARC-058's z_harm_s trunk claim; the somatic-vicarious dissociation is a weaker analogue. Transfer risk is the highest of the four entries (0.45) because "vicarious" is not "affective z_harm_a." The evidence is genuinely mixed: supports ARC-058's within-stream trunk, inconclusive on the between-stream trunk.

According to PubMed, [DOI: 10.7554/eLife.15166](https://doi.org/10.7554/eLife.15166).
