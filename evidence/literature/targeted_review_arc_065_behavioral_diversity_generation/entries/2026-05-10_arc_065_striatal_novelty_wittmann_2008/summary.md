# Wittmann, Daw, Seymour & Dolan 2008 — Striatal activity underlies novelty-based choice in humans

[DOI](https://doi.org/10.1016/j.neuron.2008.04.027) · PMID 18579085 · *Neuron* 58(6):967–73

## What the paper did

Healthy human fMRI study of a four-armed-bandit task in which the perceptual familiarity of choice options was experimentally manipulated *independently* of choice outcome. Subjects were more likely to choose perceptually novel options even when the novelty was orthogonal to reward — a clean isolation of novelty as a choice-driving factor distinct from value learning. Striatal BOLD activity tracked novelty-based choice and predicted individual differences in novelty susceptibility. The authors interpret the result as the brain using perceptual novelty as an approximation to choice uncertainty.

## Why this matters for ARC-065

This is the load-bearing R2 paper for the novelty sub-flavour of the curiosity channel (MECH-314 candidate). Kidd & Hayden's (PMID 26539887) heterogeneity argument distinguishes novelty-driven from uncertainty-driven from learning-progress-driven exploration; Wittmann 2008 shows the striatum is a substrate for the novelty flavour specifically. REE's existing MECH-216 (E1 schema-readout wanting) is the closest current candidate but operates in the *opposite* direction — schema MATCH triggers wanting, not schema NOVEL triggers exploration. Wittmann's data argue for a separate substrate write path: VALENCE_WANTING write at unfamiliar z_world locations, weighted by inverse-visit-frequency.

For the cluster registration this becomes a concrete sub-MECH candidate: MECH-314a (novelty-bonus-on-action-value at unfamiliar latent regions, striatum-analog implementation). The other two curiosity sub-flavours (MECH-314b uncertainty-driven via Daw 2006 frontopolar substrate, MECH-314c learning-progress-driven via Schmidhuber/Pathak computational substrate) need separate lit-pull anchoring. The ARC-064 lit-pull (next in the cluster scoping series) will likely surface most of the uncertainty-driven anchors since hippocampal pattern-extraction overlaps that territory.

## Limitations and confidence

The paper uses discrete-stimulus perceptual familiarity in a bandit task; REE's continuous-state grid environment requires a continuous-novelty signal that the paper does not directly operationalise. The mapping from perceptual novelty to spatial-state novelty is plausible (the striatum is involved in both literatures) but introduces a transfer step. Confidence aggregate 0.78 reflects the high venue and clean methodological design with moderate transfer risk on the operationalisation step.

## Failure signature it would falsify

An REE substrate that has no novelty-driven choice bias should fail to reproduce a striatal-equivalent activation pattern during novel-option choice and should fail to show individual-difference variation in novelty susceptibility on a corresponding behavioural probe. If REE's existing MECH-216 schema-readout wanting alone is sufficient, lesioning that mechanism should eliminate the novelty signature; if not, MECH-314a is a separate substrate.
