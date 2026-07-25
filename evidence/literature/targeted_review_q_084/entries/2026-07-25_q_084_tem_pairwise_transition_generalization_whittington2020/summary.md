# Whittington et al. (2020) -- how much you get without anything above a pair

## What the paper does

TEM proposes that medial entorhinal cells form a basis describing structural knowledge and hippocampal cells bind that basis to sensory representations. Train the resulting model on structured sequence prediction and it develops, unbidden, grid cells, band cells, border cells, object-vector cells, place cells and landmark cells -- the whole bestiary that a decade of papers treated as bespoke spatial specialisations. It also matches representations recorded during complex non-spatial relational tasks. And it makes a prediction that turned out to be right: hippocampal remapping is not random, structural knowledge is preserved across it, confirmed in simultaneously recorded place and grid cells.

## Why I am filing this as weakening Q-084

Q-084 asks whether higher-order relational structure -- metapaths, hyperedges, simplicial relations -- is *required*, noting that nothing in the REE registry represents anything above a pairwise relation. TEM is the cleanest available answer in the negative. It learns from pairwise transitions. It contains no hyperedge, no metapath, nothing above a pair. And it reproduces the phenomena Q-084's own motivating examples appeal to: functional identity emerging from relational position rather than local features, multistep structure captured well enough to generalise to new environments.

That is a genuine existence proof, and I would rather record it than only file the entry that supports the question. The honest reading of this folder so far is that its two strongest entries point in opposite directions -- Giusti et al. showing higher-order readouts see what pairwise summaries miss, TEM showing a pairwise model needs no higher-order structure to do the job. Both can be true. The reconciliation is probably that TEM's power comes from *factorising structure from content*, not from relational order, and that the pairwise readouts Giusti et al. embarrassed were unfactorised eigenvalue summaries.

If that reconciliation is right it changes Q-084's probe design, and this is the concrete deliverable from this entry. Q-084 gates on MECH-468 projection F versus a metapath-aware readout. TEM says the confound to fear is not path length but factorisation quality: a metapath readout could beat projection F simply by recovering factorisation that F failed to learn, and I would then wrongly conclude that pairwise typed edges are insufficient. The probe needs a factorisation-matched pairwise baseline, not just a pairwise baseline.

## Limits on the negative

TEM was never benchmarked against a metapath-aware or hyperedge readout on the same held-out labels. So it shows higher-order structure was not needed *for TEM's tasks*; it does not show it is never needed, and Q-084's specified comparison remains unrun. The tasks are also largely homogeneous in edge semantics -- graph traversal and relational inference over one relation type -- whereas Q-084's motivating cases are heterogeneous typed paths: current state to available action to transition region to predicted hazard to repair opportunity to goal completion. Whether a factorised pairwise basis absorbs *typed* multistep structure as gracefully as it absorbs untyped transition structure is exactly the open question, and TEM does not touch it.

And TEM is a model of biology rather than biology. Its success constrains what suffices to reproduce recordings, which is weaker than constraining what the brain does.

## Confidence

0.68. Very strong source and an unusually direct mapping for a neuroscience entry -- TEM is itself an agent architecture, so the transfer risk to REE is lower than usual. Discounted because it bounds the necessity claim without running Q-084's comparison, and because the typed-heterogeneity dimension that makes Q-084 interesting is absent from it. Q-084 remains gated and DO NOT BUILD; this entry sharpens the eventual probe rather than releasing it.
