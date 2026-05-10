# Faisal, Selen & Wolpert 2008 — Noise in the nervous system

[DOI](https://doi.org/10.1038/nrn2258) · PMID 18319728 · *Nat Rev Neurosci* 9(4):292–303

## What the paper argues

A foundational review documenting that biological neural systems are intrinsically stochastic at every level of organisation: ion-channel gating, synaptic vesicle release, spike timing, network dynamics, and behavioural outcome. Trial-to-trial variability in behaviour cannot be fully eliminated by training; some of it traces directly to molecular and cellular noise that the system has not evolved to suppress. The paper also documents that biology has co-evolved both noise-suppression mechanisms (averaging, redundancy, population coding) and noise-exploiting mechanisms (stochastic resonance, noise-driven exploration, escape from local optima during learning).

## Why this matters for ARC-065

This is the load-bearing biological grounding for the noise arm of R1. The R1 question — "is unstructured stochastic policy noise sufficient for behavioural diversity, or is structured curiosity required?" — has its noise-side answer partially constrained by Faisal et al.: there is *always* noise, the question is just whether the noise floor alone is enough. Wilson 2014 (PMID 25347535) shows it is not: humans deploy directed exploration in addition to noisy decision-making. But Faisal grounds the noise side: an REE substrate that lacks any policy-noise floor is biologically unrealistic and will fail to reproduce baseline trial-to-trial variability.

The candidate MECH-313 (stochastic-exploration-floor) is justified on this basis: a non-zero softmax temperature on E3 candidate scoring plus low-amplitude policy parameter perturbation is the substrate-level analog of biological intrinsic noise. The Faisal review supports MECH-313 as a *necessary* component of ARC-065 (the substrate would be biologically unrealistic without it) without supporting it as a *sufficient* component (Wilson 2014 shows curiosity is also needed).

## Limitations and confidence

The review establishes that noise is present and functional in biological systems; it does not directly test whether noise alone suffices for behavioural diversity in a decision-making sense (that is Wilson 2014's territory). The mapping from cellular and synaptic noise to action-policy stochasticity in an REE-style decision agent requires several inferential steps the paper does not explicitly traverse. Confidence aggregate 0.83 reflects high venue and foundational status with moderate mapping fidelity at the cellular→policy bridge.

## Failure signature it would falsify

A fully-deterministic REE policy implementation (zero softmax temperature, no policy-parameter perturbation) should fail to reproduce the irreducible behavioural-trial-to-trial variability biological agents exhibit even on highly-trained tasks. The fishtank_viz monostrategy collapse is at least partly the substrate-level prediction of what happens when the noise floor is removed.
