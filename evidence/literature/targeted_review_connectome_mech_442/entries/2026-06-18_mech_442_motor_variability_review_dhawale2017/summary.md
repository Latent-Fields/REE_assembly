# Dhawale, Smith & Olveczky 2017 -- motor variability as a regulated feature, not noise

*According to PubMed.* Dhawale, Smith & Olveczky 2017, *Annual Review of Neuroscience* ([DOI](https://doi.org/10.1146/annurev-neuro-072116-031548)).

## What the paper did
This is a synthesis review pulling together human psychophysics and animal motor-learning work around a single reframing: trial-to-trial movement variability, long dismissed as the unwanted output of a noisy nervous system, is better understood as *purposeful exploration* of motor space. Rooted in reinforcement-learning theory, the review argues that variability is actively generated and regulated by dedicated circuits, and that coupling it with reinforcement is how sensorimotor systems learn.

## Key findings relevant to MECH-442
The directly relevant claim is that behavioral diversity is a *maintained feature with its own regulatory machinery* -- not a leak. That is precisely the necessity REE's `behavioral_diversity_isolation:GAP-B` rests on, and the premise MECH-442 builds a mechanism for: if diversity must reach committed action, the brain's stance is that diversity is something the system deliberately keeps around and tunes, rather than something selection is allowed to wash out. The review also emphasizes that variability is regulated *structurally* -- it is task-dependent and dimension-specific, expressed more in task-irrelevant dimensions and suppressed in task-critical ones.

## How it translates to REE
This grounds the "diversity is a regulated property" half of MECH-442 cleanly. It is, however, agnostic between two REE renderings: (a) a per-niche-elite archive that survives the commit (the MAP-Elites structure), and (b) a simpler explore-then-reinforce loop where a variability injector perturbs the selected output and reinforcement shapes it. The review's explore-and-reinforce framing is, if anything, closer to (b) -- which is consistent with the songbird evidence that the variability generator (LMAN) is separate from and upstream of the motor selector. The structural-regulation point (variability concentrated in task-irrelevant dimensions) is a useful warning that a single uniform behavioral-descriptor may be the wrong granularity for an REE archive.

## Limitations and confidence
As a review it carries no single decisive experiment, but it is authoritative (Annu Rev Neurosci, the Olveczky group) and consolidates convergent evidence. Mapping fidelity is good for the necessity-and-regulation premise and weaker for the specific per-niche-elite mechanism. Transfer risk is relatively low because the claim being transferred is a general principle (variability is a regulated feature), not a species-specific circuit detail. Net confidence 0.77, direction supports -- with the honest caveat that it supports the maintained-diversity necessity more than the archive-survives-the-gate mechanism.
