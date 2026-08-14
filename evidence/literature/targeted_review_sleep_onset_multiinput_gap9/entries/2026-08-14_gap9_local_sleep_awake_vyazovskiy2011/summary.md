# Vyazovskiy et al. 2011 -- Local sleep in awake rats

According to PubMed: Vyazovskiy VV, Olcese U, Hanlon EC, Nir Y, Cirelli C, Tononi G. *Nature* 2011;472(7344):443-447. [DOI 10.1038/nature10009](https://doi.org/10.1038/nature10009) (PMID 21525926).

## What the paper did

Recorded cortical unit activity and local field potentials in rats kept awake beyond their usual waking period, while the animals continued to behave and perform a task, and while EEG and behaviour both classified them as awake.

## Core finding

Individual cortical populations intermittently entered brief sleep-like **OFF periods** with local slow-wave activity, while the animal remained behaviourally awake. These local off-periods became more frequent with time awake, occurred in different cortical locations at different moments, and their occurrence predicted **task performance errors**. In the authors' framing, local populations of neurons "may be falling asleep, with negative consequences for performance," even as the organism is awake.

## Why this matters for GAP-9

GAP-9 asks what a within-life sleep trigger should read, and the phrasing of the question smuggles in an assumption: that there is one thing to read. This paper is the sharpest available empirical challenge to that assumption. If sleep need were a single global scalar crossing a single threshold, the organism would be either asleep or awake. Instead the regulatory unit is **local**, and local units can go offline independently of the global state.

For the synthesis this supplies the empirical half of Verdict 1 (Krueger 2008 supplies the theoretical half). Its practical consequence for REE is honest rather than obstructive: REE has no cortical topography, so one global MEL scalar is the right V3 simplification -- but it is a **known divergence** to be recorded (synthesis Section 7 item 1), not a faithful model. It also identifies what the divergence costs: local sleep need is what makes *partial* sleep mechanically natural, and partial sleep is exactly what the safety literature (Rattenborg 1999, Tamaki 2016, sibling entries) says the risk response should look like. So the global-scalar simplification and the graded-safety recommendation pull against one another, and the duration lever is REE's stand-in for a mechanism biology implements spatially.

## Where the paper's coverage ends

The animals were sleep-deprived; the paper establishes that local sleep is *exposed* when global sleep regulation is suspended, not that local regulation is the dominant mode at baseline. It also does not offer an aggregation rule -- it shows local units going offline but does not specify how their states combine into the global sleep decision, which is precisely what a REE implementation would need. That gap is Krueger 2008's territory, and Krueger supplies a direction (aggregate upward) rather than a formula.

## Confidence reasoning

Source quality 0.95 -- *Nature*, direct unit recordings, from the Tononi/Cirelli group whose Synaptic Homeostasis Hypothesis frames much of the surrounding corpus (Huber 2004 in `targeted_review_connectome_mech_180/`). Mapping fidelity 0.80: strong for the negative claim (sleep need is not one global scalar), weaker for any positive V3 build, since REE has no regional substrate to host the finding. Transfer risk 0.30 -- the highest in this pull, because the phenomenon is a property of a spatially extended cortex and REE is not one. Confidence 0.88.

## Failure signatures for the cluster

1. **Averaged-away demand.** If REE's sleep-need signal stays a single global scalar and the substrate later needs different subsystems consolidated at different rates, this entry predicts the scalar will average away the very demand differences that should drive routing. Diagnostic: compare the spread of per-region MECH-284 staleness against the single MEL value at cycle entry -- a wide regional spread sitting under a mid-range global MEL is the signature.
