# Hofbauer, Rainville, Duncan & Bushnell 2001 -- Double dissociation of sensory vs affective pain

## What the paper did

Ten volunteers received tonic warm and noxious heat stimuli during PET scanning across four conditions: alert control, hypnosis control, hypnotic suggestion for increased pain intensity, and hypnotic suggestion for decreased pain intensity. The target dimension was pain INTENSITY (the sensory-discriminative component). The paper is the companion to Rainville et al 1997 (Science), which ran an equivalent paradigm with suggestions targeting pain UNPLEASANTNESS (the affective component). Taken together, the two studies establish a double dissociation: hypnotic intensity-modulation changes S1 activity without changing ACC; hypnotic unpleasantness-modulation changes ACC activity without changing S1.

## Key findings relevant to ARC-058

This is the canonical cortical double-dissociation evidence for the sensory/affective split in pain. For ARC-058 it forces a distinction. A strong shared-trunk architecture that commingles signed sensory and affective PE cannot easily produce independent cortical modulation of intensity and unpleasantness -- the top-down intervention would have to somehow enter the shared trunk and emerge only in one readout, which is awkward. A weak shared-trunk architecture (shared unsigned magnitude + separable signed heads) is fully compatible with the double dissociation: hypnotic suggestion modulates the signed heads while leaving the unsigned magnitude trunk approximately invariant. This is ARC-058's spec as actually written.

So Hofbauer 2001 + Rainville 1997 do not destroy ARC-058; they constrain it. They kill the strong "everything is one module" reading and leave the weak trunk-plus-heads reading standing. They also establish that at the SIGNED output level, the architecture behaves like ARC-033 -- separable, independently modulable representations. The question ARC-058 answers that ARC-033 does not is WHERE the shared computation hides: in the unsigned magnitude (AIC) that both heads derive from.

## How this translates to REE

In the SD-011 / SD-032 spec, z_harm_s is the sensory-discriminative stream and z_harm_a is the affective stream. ARC-058 says both streams' forward models share a trunk (HarmForwardTrunk) and have stream-specific heads (HarmForwardHead). The Hofbauer / Rainville double dissociation says the cortical READOUTS of these streams are independently modulable by top-down attention -- which is what separate heads predict.

The one translation issue is that "ACC" in 2001 nomenclature covers both perigenual ACC (SD-032e in REE) and dorsal ACC / aMCC (SD-032b). The unpleasantness modulation found by Rainville 1997 most closely maps to the aMCC's affective-pain component -- which is where MECH-258's precision-weighted z_harm_a PE is supposed to live. This is consistent but not pinpoint.

## Limitations and caveats

PET, N=10, single lab, early fMRI-era statistical methods. Hypnosis as a causal manipulation is strong but confounded with suggestibility, attention, and expectancy variance. The paper does not image predictive-coding PE directly. The ACC attribution is anatomically broad by modern standards.

The double dissociation also does not uniquely select the shared-trunk architecture -- ARC-033 (fully independent substrates) produces the same prediction. The Horing & Buchel 2022 finding of shared unsigned AIC PE is what separates weak-ARC-058 from ARC-033; Hofbauer 2001 by itself is compatible with either.

## Confidence reasoning

Confidence 0.70. Source quality moderate (0.68) -- the paper's impact is canonical but the technology and sample are dated. Mapping fidelity is good (0.70) for the sensory/affective architectural distinction. Transfer risk is moderate (0.40) because the 2001 ACC attribution is less precise than the modern aMCC/dACC/pACC/PCC subdivision SD-032 works with. The evidence weakens strong ARC-058 and supports weak ARC-058 or ARC-033 at the signed-readout level. Combined with Horing & Buchel 2022 (cross-reference in synthesis), the full picture favours ARC-058's actual specification over ARC-033.

According to PubMed, [DOI: 10.1152/jn.2001.86.1.402](https://doi.org/10.1152/jn.2001.86.1.402).
