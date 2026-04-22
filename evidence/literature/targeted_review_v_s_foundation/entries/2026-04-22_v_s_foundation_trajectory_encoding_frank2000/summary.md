# Frank, Brown & Wilson 2000 -- Trajectory encoding in the hippocampus and entorhinal cortex

DOI: [10.1016/s0896-6273(00)00018-0](https://doi.org/10.1016/s0896-6273(00)00018-0) -- Neuron (PubMed 10939340)

## What the paper did

Single-unit recordings from CA1 and entorhinal cortex (EC) in rats navigating multiple distinct trajectories that share common positions. Two questions: (1) do CA1 cells encode trajectory context (prospective or retrospective coding), and (2) does deep-layer EC -- the target of hippocampal output -- show generalisation across trajectories that share spatial features?

## Findings relevant to V_s foundation

Two main results. First, many CA1 and EC cells fired at significantly different rates at the same position depending on where the animal had come from or was going -- the same trajectory-context phenomenon that Wood et al found in alternation tasks, generalised to free navigation across multiple trajectories. Second, and architecturally more interesting, deep-layer EC cells -- which receive hippocampal output -- showed regularities across trajectories at the same place: they generalised over the trajectory-specific differences and represented similarities between locations on different trajectories.

This is biological evidence for two coexisting representational levels: a CA1 layer that disambiguates by trajectory context (the Wood result generalised), and a downstream EC layer that pools across trajectory-specific differences and re-extracts the shared spatial structure.

## Translation to REE / MECH-269 / MECH-272

The two-level result is directly relevant to anchor architecture. CA1 splitter-style coding supports (place, context) anchors. But the deep-layer EC result implies the substrate also needs a parallel pathway that pools across context-disambiguated anchors and re-derives the shared place structure. This is consistent with the substrate plan having anchors at the schema-region level AND a separate place-cell-field-level structure that aggregates across them.

For the granularity question, this paper argues against a single uniform granularity. The biology runs at least two levels: (place, context) anchors for episodic disambiguation and pure-place pooling for generalisation. The substrate should accommodate both. If the V_s foundation defaults to schema-region-level anchors only, it will lose the EC-deep-layer generalisation pathway -- which is exactly the substrate that supports transfer across episodes that share a common location.

For MECH-272 routing, the implication is that routing happens at the CA1 (place, context) level, but the integrated readout to downstream consumers (E2 forward model, E3 evaluator) should pool across the context-disambiguated anchors at the place level, not at the per-anchor level alone.

## Limitations and caveats

The paper does not dissect what aspect of trajectory the cells are encoding (prospective vs retrospective vs sequence position). The EC generalisation result is from deep layers only; superficial-layer EC (the input pathway to hippocampus) shows different coding properties. Recordings are from a small number of cells per animal; the population-level claim is inferred. Rodent only.

## Confidence reasoning

Source quality very high (Neuron, MIT/Wilson lab, foundational). Mapping fidelity is strong for the qualitative two-level claim. Transfer risk moderate -- the EC generalisation result is a key piece of the substrate architecture but the mapping to specific REE consumers (E2, E3, hippocampal proposer) requires interpretation.