# Hassabis, Kumaran, Vann & Maguire 2007 -- Hippocampal amnesia and imagined experience

**Claim(s):** MECH-135 | **Direction:** mixed | **Confidence:** 0.55

*According to PubMed* (PMID 17229836), [DOI: 10.1073/pnas.0610561104](https://doi.org/10.1073/pnas.0610561104).

## What the paper did

Amnesic patients are known to have trouble remembering their past. Hassabis and colleagues asked a question that, remarkably, nobody had formally put before: can they *imagine* new experiences? They tested amnesic patients with primary bilateral hippocampal damage, giving short verbal cues outlining simple commonplace scenarios -- imagine lying on a white sandy beach, that sort of thing -- and scoring what the patients constructed.

The patients were markedly impaired relative to matched controls. And the authors went further than the impairment, identifying its character: the patients' imagined experiences "lacked spatial coherence, consisting instead of fragmented images in the absence of a holistic representation of the environmental setting." Their conclusion is that the hippocampus contributes the spatial context into which the disparate elements of an experience are bound.

## Why this entry exists

The V3-EXQ-108b autopsy's four-layer diagnosis recorded `Biological reference: absent (for this specific axis)`, and stated plainly that the multi-step-imagination-versus-intact-perception parallel was "presented as a plausible biological reference class for the follow-on lit-pull to verify with actual citations -- no specific paper is asserted here as REE literature." This is that citation, and it discharges that row.

What it confirms is the **separability** premise, and it confirms it about as cleanly as a lesion study can. Biology does not get multi-step constructive simulation for free as a by-product of having good perceptual representations. It implements it as a distinct system, with its own substrate and its own failure mode, sitting on top of perception. Damage that system and perception survives.

REE-v3 exhibits the same separability, measured rather than lesioned. The sanctioned-trained z_world encoder differentiates real states healthily -- CR_real 0.193 and 0.201 across seeds, holdout probe accuracy 0.80 to 0.94 on hazard, resource-presence and distance -- while the E1 rollout built on that very encoder is fully degenerate, CR_rollout/CR_real between 2.6e-6 and 3.2e-6. For MECH-135 the lesson is that a healthy state representation is not evidence that multi-step imagined rollout on top of it will work, in silicon or in tissue.

## The caveat that set the direction

I want to be careful here, because the tidy version of this mapping is more flattering than the evidence.

The patients fail by **fragmentation**: their imagined scenes come apart into disconnected pieces, losing coherence and holistic structure. E1 fails by **convergence**: forty distinct action sequences produce near-identical endpoints, with score variance around 1e-13 against a 0.002 threshold. Those are both degenerate simulation, but they are close to opposite pathologies -- one loses binding, the other loses variance. Excessive coherence, if you like.

So the biological result establishes that the simulation machinery is separable and can fail on its own. It does *not* predict that it fails the way REE's does, and anyone reaching for "biology shows imagination machinery is separable, therefore REE's collapse is the biologically expected failure" would be overreaching. I would rather the record said so than have someone find this gap later.

The anatomical correspondence is also loose. This is a lesion study in a small patient group, mapped onto an LSTM forward model that has no hippocampal analogue in the pathway under test -- REE's HippocampalModule sits *downstream* of E1's `generate_prior`, receiving the prior rather than being the rollout mechanism. The entry supports the separability premise. It does not support any particular fix.

## Confidence reasoning

Source quality 0.88: PNAS 2007, foundational, heavily cited, methodologically careful with matched controls. Mapping fidelity 0.45 is the low leg and it drives the aggregate down hard, deliberately -- for an architectural claim the mapping is what decides, and here half the mapping (separability) transfers well while the other half (failure signature) does not transfer at all. Transfer risk 0.55 for human-lesion-to-LSTM plus the loose anatomy.

Aggregate 0.55, direction **mixed**. A genuine and load-bearing existence proof for the separability the autopsy hypothesised, paired with a signature mismatch that should stop anyone leaning on it further than that.
