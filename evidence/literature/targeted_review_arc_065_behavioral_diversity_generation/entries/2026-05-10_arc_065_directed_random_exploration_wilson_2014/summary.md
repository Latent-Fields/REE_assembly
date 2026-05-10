# Wilson, Geana, White, Ludvig & Cohen 2014 — Humans use directed AND random exploration

[DOI](https://doi.org/10.1037/a0038199) · PMID 25347535 · *J Exp Psychol Gen* 143(6):2074–81

## What the paper did

A Horizon task: participants made explore-exploit decisions in two contexts that differed in the number of future choices available (horizon 1 vs horizon 6). The longer horizon makes exploration more valuable, so any exploration-driving mechanism should scale up. Critically, the authors fit a behavioural model that decomposed each subject's exploration into two parameters: an information-seeking bias (directed) and a softmax temperature (random).

Both parameters increased significantly with horizon. Subjects became MORE information-seeking AND noisier in the longer-horizon condition. Either-channel-only models could not capture the full pattern of horizon-dependent behaviour. The two channels are computationally separable and behaviourally double-dissociable.

## Why this matters for ARC-065

This is the load-bearing paper for the R1 verdict in the lit-pull. The question "is structured curiosity necessary, or does noise suffice, or are both required?" was framed in V3 design discussions as a three-way choice; Wilson 2014 forces the (c) both-channels-needed reading by demonstrating that humans deploy both, and that they are dissociable but co-active. An ARC-065 substrate that wires only one channel — either MECH-313 stochastic-noise-floor or MECH-314 curiosity-bonus — will under-generate behavioural diversity in REE agents in the same way that an isolated-channel model under-fits Horizon-task data here. The right architectural commitment is to instantiate both, with separable knobs, and to register the relative-weight calibration as an open question (provisional Q-XXX in the cluster).

## Limitations and confidence

Single behavioural paradigm in healthy humans; the bandit-with-known-horizon design differs in important respects from REE's open-ended foraging environment (no explicit horizon cue, continuous state, embodied agent). The Wilson lab and replications (e.g. Gershman 2018; Hayes & Petrov 2015 PMID 26488587 with pupillometry as an indirect LC marker) have shown the dual-channel pattern is robust across task variants, but the magnitudes do not transfer to REE without empirical calibration. Confidence aggregate 0.86 reflects high source quality and high qualitative-mapping fidelity, with moderate transfer risk on the magnitudes.

## Failure signature it would falsify

A single-channel ARC-065 substrate that fails to reproduce horizon-dependent shifts in BOTH information-seeking AND decision-noise components on the corresponding REE behavioural probe.
