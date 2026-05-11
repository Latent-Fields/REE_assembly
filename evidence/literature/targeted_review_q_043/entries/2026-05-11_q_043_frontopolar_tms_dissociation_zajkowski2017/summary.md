# Zajkowski, Kossut & Wilson 2017 — Causal role for right frontopolar cortex in directed exploration

**Citation.** Zajkowski WK, Kossut M, Wilson RC. (2017). A causal role for right frontopolar cortex in directed, but not random, exploration. *eLife* 6:e27430. [DOI](https://doi.org/10.7554/eLife.27430). PMID 28914605.

## What the paper did

Wilson's group had already established (Wilson 2014, sibling entry) that humans use both directed and random exploration. Daw 2006 had implicated frontopolar cortex in exploration generally. Zajkowski et al. took the next step: causal manipulation. They applied inhibitory continuous theta-burst transcranial magnetic stimulation (cTBS) over the right frontopolar cortex of healthy adults, then had them play the Horizon task. A sham-stimulation control group played the same task.

The result was clean. cTBS over right frontopolar cortex selectively reduced directed exploration — the information-bonus parameter dropped relative to sham — while random exploration (decision-noise parameter) was statistically indistinguishable from sham. The selectivity of the impairment is the load-bearing finding: had cTBS knocked out both, the result would have been consistent with a single-mechanism model where frontopolar cortex implements all exploration. Instead, the dissociation suggests that random exploration depends on a different substrate that the TMS coil did not reach.

## Relevance to Q-043

This is the cleanest available causal evidence for the substrate distinction Q-043 presupposes. Wilson 2014 showed the two strategies are behaviourally separable in the sense of being independently tunable. Daw 2006 showed they are neurally separable in the sense of correlating with different BOLD signal. Zajkowski 2017 closes the gap: lesion-like inactivation of one substrate selectively impairs one strategy. This is the strongest evidence short of a positive double dissociation (which would require a second TMS target known to selectively impair random exploration — pharmacology fills that role in Warren 2017).

For REE's V3 implementation, this paper supports keeping MECH-313 and MECH-314 as separate substrates with independent ablation flags. The Q-043 parametric sweep is well-posed because the underlying mechanisms are not collapsed; their relative weighting is a genuine architectural calibration question rather than a redundant parameter.

## Caveats

cTBS is a coarse perturbation. The coil disrupts cortical processing under a several-centimetre footprint, so the conclusion "directed exploration depends on this cortical region" should not be read as "directed exploration depends ONLY on this cortical region." It says the region is necessary, not that it is sufficient or that it is the only contributor. Likewise the null result for random exploration is logically weaker than a positive finding: it shows random exploration does not require this specific region, but it does not pin down the substrate that does support it.

n=24 with a between-subject design means modest statistical power. The effect on directed exploration is significant but not enormous, and replication would strengthen the inference. The authors are appropriately cautious in framing the conclusion as "at least partially dissociable neural systems" rather than as a full dissociation.

For REE specifically, the transfer caveat is that the human TMS subject is performing an acute task with chronic frontopolar function; REE's MECH-313 and MECH-314 are software flags that are off or on for the full lifetime of a training run. The chronic-vs-acute difference may matter when interpreting the parametric sweep results: a slow-trained REE substrate under permanent MECH-314-OFF may compensate in ways the TMS subject cannot.

## Confidence reasoning

I assign 0.81. Source quality (0.83) is high (eLife, sham-controlled TMS), mapping fidelity (0.85) is high because the dissociation is at exactly the architectural level Q-043 needs, and transfer risk (0.30) is modest because TMS is not a perfect analog of substrate-level flag toggling but the mechanism-level question is shared. The single biggest reason this is not 0.9 is the small cohort and the dependence on a null result for the random-exploration side, which I think is appropriately reflected in the failure_signatures.
