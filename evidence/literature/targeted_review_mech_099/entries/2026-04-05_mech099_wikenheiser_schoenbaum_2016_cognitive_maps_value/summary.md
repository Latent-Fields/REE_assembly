# Wikenheiser & Schoenbaum 2016 -- Cognitive Maps Encode Value, Not Just Geometry

**Source:** Wikenheiser AM, Schoenbaum G. "Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex." *Nature Reviews Neuroscience* 17:513-523, 2016. DOI: [10.1038/nrn.2016.56](https://doi.org/10.1038/nrn.2016.56). PMID: 27256552

**Claim evidenced:** MECH-099

---

## What the paper did

Wikenheiser and Schoenbaum reviewed the literature on hippocampal and orbitofrontal cortex (OFC) cognitive maps, arguing that research on both structures has proceeded too independently. They synthesised evidence that the hippocampus encodes not just spatial/contextual relationships but also value relationships -- the 'what outcomes follow from which actions in which context' structure -- and that OFC provides a complementary map that annotates these relationships with value signals. They proposed that HPC-OFC interaction enables flexible use of prior learning to navigate environments when the reward structure changes.

## Key findings relevant to REE

Hippocampal cognitive maps are more than geometrical records of physical space. They encode relationships between cues, actions, and outcomes, including the values of those outcomes. When reward structure changes, hippocampal representations update, allowing organisms to navigate toward value without re-learning from scratch. The map is a navigable structure over the space of outcomes, not just positions.

OFC provides value annotation to the hippocampal map: HPC contributes the structural scaffold (what follows what), OFC contributes the evaluative dimension (how much is that outcome worth). Their interaction is necessary for flexible, goal-directed behaviour in changing environments.

## Translation to REE

MECH-099 claims the residue field is a persistent spatial map of harm and benefit accumulation that guides navigation toward or away from regions based on accumulated evidence. The Wikenheiser-Schoenbaum framework directly justifies the core claim: hippocampal spatial maps are value-annotated, not purely geometric. The residue field is, in their terms, a cognitive map with harm/benefit value annotation.

The OFC-as-value-annotator maps onto E3's harm/goal error signal in REE: the hippocampal module maintains the spatial scaffold (the residue field geometry); E3's evaluation layer writes harm/benefit annotations onto it (the OFC analog). The accumulated harm history in MECH-099 is the temporal integration of these OFC-analog annotations across episodes, which is precisely what Wikenheiser-Schoenbaum argue the hippocampal-OFC system does when tracking value across changing environments.

## Limitations and caveats

The review primarily addresses reward value, not harm. REE's residue field is predominantly harm-tracking. Whether hippocampal-OFC circuits treat harm accumulation identically to reward accumulation is not established -- the amygdala literature suggests asymmetric processing. The OFC component of their framework is not explicitly modelled in V3's architecture. This is a review/theory paper -- the support it provides is architectural justification rather than direct empirical evidence for harm-spatial map persistence.

## Confidence reasoning

Confidence 0.75. Nature Reviews Neuroscience, highly influential. Provides important theoretical grounding that cognitive maps are value-containing structures (directly relevant to MECH-099's residue field concept). Docked for the harm/reward asymmetry gap and the review-rather-than-empirical nature of the evidence.
