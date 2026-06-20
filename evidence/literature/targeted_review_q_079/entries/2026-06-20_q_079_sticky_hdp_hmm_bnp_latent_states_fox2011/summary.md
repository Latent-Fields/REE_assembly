# Bayesian-nonparametric latent-state discovery (Fox, Sudderth, Jordan & Willsky 2011) — Q-079

**Source:** Emily B. Fox, Erik B. Sudderth, Michael I. Jordan & Alan S. Willsky, "A sticky HDP-HMM with application to speaker diarization," The Annals of Applied Statistics 5(2A):1020-1056 (2011), DOI 10.1214/10-AOAS395 (arXiv:0905.2592). Builds on Teh, Jordan, Beal & Blei, "Hierarchical Dirichlet Processes," JASA (2006).
**Direction:** mixed.

## What the paper does

The hierarchical Dirichlet process (HDP) places a prior over HMM transition matrices defined on a *countably infinite* state space, so the number of latent states is itself inferred from data rather than fixed in advance. The sticky extension adds a self-transition bias that controls the switching rate (the bare HDP-HMM over-segments), and a split-merge sampler proposes birth and merging of states. The result is full Bayesian posterior inference over latent structure *and* its cardinality.

## Why it bears on Q-079 — and why it is mixed

This is the cleanest, most mature coverage of capacity **(c)** — latent-node birth / death / merge / split — with genuinely unbounded cardinality, going beyond the pre-allocated "spare-slot" expansion of the active-inference structure-learning model (Smith et al 2020). To that extent it *strengthens* the ANSWERED-NEGATIVE finding: (c) is not a missing mathematics.

But it also cuts the other way, which is why the direction is **mixed**. Bayesian nonparametrics delivers *only* (c). There is no cyclic-coherence object (b), no granularity/scale operator (d), and no action coupling — and the inference is offline batch posterior estimation over a time series, not online action-coupled graph transformation. So the sticky HDP-HMM is also the concrete demonstration of the research map's true observation: no single *non-active-inference* formalism covers the combination. The combination is reached by assembling BNP-style structure learning **with** the active-inference / factor-graph substrate — which is an engineering synthesis of existing pieces, not the discovery of a new mathematical object.

## Role in the coverage matrix (non-degeneracy)

This entry exists to keep the matrix honest. The active-inference family (Frey + de Vries-Friston + Smith + RGM) is the path to ANSWERED-NEGATIVE, but the falsifier's non-degeneracy guard demands that each candidate formalism's *actual* coverage be enumerated rather than asserting a gap. The sticky HDP-HMM marks the BNP row precisely: full marks on (c), nothing on (b)/(d)/action — which is exactly why "the gap is the combination" is a weaker claim than "a new object," and why the combination, once shown to live in the active-inference family, does not warrant a standalone formalism.

## Confidence reasoning

0.60. Top-tier authorship and venue give high source quality. Mapping fidelity is moderate because the paper covers a single capacity, in a passive batch-inference setting distant from REE's online, action-coupled use — so it is informative about (c)'s maturity and about BNP's single-capacity scope, but not directly about REE's integrated object.
