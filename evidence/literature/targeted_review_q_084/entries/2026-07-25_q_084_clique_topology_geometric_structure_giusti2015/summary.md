# Giusti, Pastalkova, Curto & Itskov (2015) -- higher-order structure you can only see with a higher-order method

## What the paper does

The technical contribution is clique topology: instead of asking what the eigenvalues of a correlation matrix look like, ask what the topology of its order complex looks like. Because the method depends only on the relative ordering of matrix entries, it is invariant under any monotone nonlinear transformation -- which matters enormously in neural data, where the map from the quantity you care about to the quantity you measure is nonlinear and unknown. Applied to rat hippocampal pyramidal-cell recordings, the method detects geometric organisation that eigenvalue-based analysis cannot separate from random structure.

The finding I keep returning to is the control: the same geometric signature appears during wheel running and during REM sleep. There is no position to encode in either. So the geometry is a property of the circuit, not a shadow cast by the animal's location.

## Why this is the anchor entry for Q-084

Q-084 observes that nothing in the REE registry represents anything above a pairwise relation, and asks whether higher-order structure -- metapaths, hyperedges, simplicial relations -- is required. Cliques *are* simplices; Betti curves are the homology of the clique complex. This is therefore a genuine higher-order analysis, and it finds something that the pairwise-summary analysis provably does not.

The consequence for Q-084's gating design is concrete. Q-084 is probe-gated on MECH-468 projection F versus a metapath-aware readout, and the fear behind the gate is that a metapath advantage over a topology that itself adds nothing would be uninterpretable. This paper adds the symmetric warning from the other side: a *null* from a pairwise-summary readout is weak evidence of absence, because in this dataset the pairwise-summary method was not merely less sensitive -- it was misleading under unknown monotone nonlinearity. If projection F is read out with eigenvalue-style summaries and comes back flat, that is not yet an answer.

## The line I must not cross

Q-084's own notes carry the organisational-versus-representational guard, and this paper is the sharpest test of whether I can hold it. The higher-order object here lives in the analyst's toolkit. Clique topology is computed *from a pairwise correlation matrix*. Nothing in the result says the hippocampus stores a hyperedge, and nothing licenses reimplementing REE's hippocampal representation as a hypergraph or a simplicial complex. What it says is that pairwise relations have higher-order consequences that a pairwise-summary readout discards. That is an argument about readouts, and it is a good one; it is not an argument about substrate.

Two further boundaries. This is rodent spatial electrophysiology, and REE's anchors are action-object and trajectory structures whose correlation geometry has no guaranteed analogue. And the paper says nothing about *typed* relations -- Q-084's formulation is metapaths over heterogeneous typed edges, whereas clique topology treats one homogeneous correlation structure. That is a real gap in the mapping and it is the part I would most want a second paper on.

## Confidence

0.70, with mapping fidelity as the limiter. Strong source, genuinely higher-order method, decisive control against the position-coding explanation. It supports the organisational half of Q-084 and is silent-to-unhelpful on the representational half -- which, given that Q-084 is registered explicitly as DO NOT BUILD, is the half I actually needed evidence on.
