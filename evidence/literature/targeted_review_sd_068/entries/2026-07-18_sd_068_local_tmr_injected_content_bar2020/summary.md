# Local Targeted Memory Reactivation in Human Sleep

**Bar et al. (2020), _Current Biology_ 30(8):1435-1446.e5.** DOI: [10.1016/j.cub.2020.01.091](https://doi.org/10.1016/j.cub.2020.01.091). Retrieved via PubMed (PMID 32142693).

## What the paper did

Targeted memory reactivation re-presents a learning-associated cue during sleep to bias which memories get consolidated. An open question was whether TMR acts globally on the sleeping brain or locally on specific circuits. Bar and colleagues answered it by exploiting a quirk of olfactory neuroanatomy: unlike other senses, smell is processed ipsilaterally, so an odor delivered to one nostril reaches primarily one hemisphere.

Participants learned associations between words and locations in the left or right visual field, with a contextual odor present throughout. During post-learning naps, odor was delivered to a single nostril during NREM sleep. Memory improved specifically for words that had been processed in the cued hemisphere. Regional slow-wave power *decreased* in the cued hemisphere relative to the uncued one, and that decrease correlated negatively with memory for cued words. Slow-oscillation/spindle phase-amplitude coupling improved specifically in the cued hemisphere.

The control that makes the study is the odor-contingency condition: when learning had happened *without* contextual odor, unilateral olfactory stimulation during sleep produced neither the memory effect nor the oscillatory one. The stimulation alone does nothing. It only does something when there is injected content for it to act on.

## How this maps to SD-068

This entry is here for methodology, not mechanism, and it is the closest structural analog in the pull to what SD-068 actually built.

SD-068's measurement design makes two commitments. It scores per-phase output quality against *known injected content* — following the V3-EXQ-702 precedent, specifically to sidestep the encoding-starvation ceiling that sank V3-EXQ-538a — rather than against whatever the substrate happens to have encoded. And it applies a scoped perturbation (a single RMS-scaled Gaussian sigma per phase) with a readout scoped to the same phase.

Bar et al. are an existence proof that this shape of design yields interpretable dissociations in a real consolidating system. Known content in; perturbation scoped to one locus; readout scoped to the same locus; an unperturbed locus available for comparison. The dissociation they obtained — local, not global — is exactly the kind of result a per-phase lesion harness must be capable of producing if its phases are genuinely separable rather than nominally so.

The odor-contingency control deserves particular attention, because it names a failure mode SD-068 should be able to rule out and I am not certain it currently does. Bar et al. showed their perturbation had no effect absent injected content. The harness analog: if a per-phase quality readout moves in response to the damage sigma even when no known content has been injected, then that readout is measuring perturbation magnitude, not content fidelity — and the staging order it produces would be an ordering of the three phases' noise sensitivity rather than of their functional damage tolerance. That is precisely the vacuity SD-068 claims to have escaped. I have logged it as a failure signature; it reads as a cheap and worthwhile addition to the harness's validation set.

## Limitations and caveats

The scoping axis is the main disanalogy, and it is not small. Bar et al. scope *anatomically* — left hemisphere versus right, within a single sleep stage — which hands them a genuine within-subject control locus, perturbed and unperturbed tissue in the same sleeping brain at the same moment. SD-068 scopes *temporally and functionally*, across pipeline phases, and has no such simultaneous twin. Each phase is compared against its own undamaged baseline across runs. That is a weaker contrast, more exposed to run-to-run variance, and it means the harness cannot do the one thing that makes this paper convincing.

Second, the perturbations are not the same operation. A cue *adds* input; Gaussian noise *degrades* state. Enhancement and lesion are not symmetric, and a system can be locally enhanceable without being locally lesionable in any matching way.

Third, this is NREM only. It says nothing about ordering across phases, which is where SD-068 places its non-vacuity weight.

## Confidence reasoning

0.71, the highest in this pull, and the components are worth reading separately. Source quality is 0.84 — *Current Biology*, a strong multi-lab group, a genuinely elegant design, and a well-chosen negative control. Transfer risk is the lowest here (0.38) because what I am transferring is a *methodological* pattern, and methodology transfers across substrates far more robustly than mechanism does; I am not claiming REE's sleep phases work like human olfactory-cued NREM.

Mapping fidelity (0.68) is the limiting term, held there by the anatomical-versus-temporal scoping mismatch and the cue-versus-noise asymmetry. What this paper licenses is: the injected-content-plus-scoped-readout design is sound and can produce real dissociations. What it does not license is any claim that SD-068's particular phase-scoped implementation of that design achieves the same separability.
