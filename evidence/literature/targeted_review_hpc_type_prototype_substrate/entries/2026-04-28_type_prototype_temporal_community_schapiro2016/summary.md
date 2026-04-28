# Schapiro, Turk-Browne, Norman & Botvinick 2016 — Statistical learning of temporal community structure in the hippocampus

According to PubMed: Schapiro, Turk-Browne, Norman & Botvinick. *Hippocampus* 26(1):3-8 (2016, online 2015). [DOI 10.1002/hipo.22523](https://doi.org/10.1002/hipo.22523). PMID 26332666.

## What the paper did

22 human participants underwent fMRI while passively viewing sequences of abstract fractal images. The sequences were carefully constructed to have **no variance in pairwise transition probability** — every item could be followed by every other item with equal frequency at the local level — but to have **temporal community structure** at the higher level: 15 items partitioned into three communities of five, with within-community transitions more likely than between-community transitions only when integrated over a longer window.

The architectural question this design isolates is whether HPC can extract a regularity that is invisible at the local pairwise level. Representational similarity analysis tested whether hippocampal voxel patterns reflected community membership rather than just specific item identity. They did. Voxel patterns for items within the same community were more similar to each other than to items in different communities, and this community-structured representational geometry developed during the exposure session — i.e. through learning, not from prior knowledge.

## Why this matters for REE's question

For sub-question 2 — does sleep extract type-prototypes, or can waking learning do it? — this paper says **waking learning is sufficient** for the kind of compositional abstraction that requires extracting regularities from overlapping associations. No nap, no overnight period, no sleep stage. The community structure emerges in HPC representations during waking exposure.

This has a specific architectural consequence for REE. An explicit type-prototype substrate (provisional SD-N) does *not* strictly require a sleep operator to populate. The substrate could update during waking — for instance, every time an anchor is written or invalidated, a sliding update on the prototype codebook. Sleep would still enhance the abstraction (Hennies et al. 2017, separate entry, addresses this), but it is not the gating step.

The MECH-269 anchor stream_mixture key already has the right shape for this kind of community-structure representation. Anchors that share a stream_mixture are functionally in the same "community" — they were active during similar latent-state regimes. What REE is missing is an explicit operator that reads out the community structure from the anchor pool and produces a compressed prototype that can be cosine-matched against current `LatentState`. The Schapiro 2016 evidence licenses doing this online, during waking, rather than gating it to the sleep cycle.

## What it does NOT settle

The "statistical learning" demonstrated here is for **temporal sequences**, not for category prototypes in a perceptual or feature-space sense. An REE prototype substrate covering "hazard-type" or "resource-type" would need to extract structure from co-occurrence patterns in *latent space* (which streams co-vary, which valence components co-fire), not from temporal sequence statistics. The architectural primitive — extract invariants from overlapping associations — is the same. The input domain is different. The transfer is plausible but not directly demonstrated.

fMRI is indirect for substrate-level claims. The paper shows community-structured representations in *hippocampus*, but the BOLD signal aggregates over thousands of neurons and several seconds. Which subfield carries the community structure — DG, CA3, CA1, or some combination — is not resolved here. The companion Schapiro et al. 2017 modelling paper (separate entry in this review) attributes it to the monosynaptic EC→CA1 pathway based on architectural reasoning, but that subfield-level claim is inferred from the model's match to behaviour rather than measured directly.

## Confidence reasoning

I sit this at 0.78. Source quality 0.78 — *Hippocampus* journal, RSA methodology, careful task design that isolates higher-order structure from local transition statistics. Mapping fidelity 0.75 because the paper directly evidences waking-driven hippocampal regularity extraction, which licenses the specific architectural inference that REE's prototype substrate does not require a sleep-only operator. Transfer risk 0.35 because the temporal-sequence-to-general-category generalisation is the main uncertainty, and the substrate-level (which subfield) claim is inferred from the companion modelling paper rather than measured here.
