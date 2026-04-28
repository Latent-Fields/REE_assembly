# Bellmund, Gärdenfors, Moser & Doeller 2018 — Navigating cognition: Spatial codes for human thinking

According to PubMed: Bellmund, Gärdenfors, Moser & Doeller. *Science* 362(6415):eaat6766 (2018). [DOI 10.1126/science.aat6766](https://doi.org/10.1126/science.aat6766). PMID 30409861.

## What the paper did

This is the canonical synthesis paper integrating spatial-navigation neural codes with non-spatial cognition. The authors — including Edvard Moser, who shared the Nobel for the discovery of grid cells — argue that the place / grid / time-cell representational format of the hippocampal formation is *not specific to physical space*. The same primitive serves as a general-purpose cognitive-map machinery, and human thinking (about non-spatial relations, conceptual hierarchies, social structures, abstract task graphs) reuses it.

The framework has three interlocking claims:

1. **Place and grid cell population codes provide a representational format for variable cognitive dimensions.** The dimensions don't have to be spatial; they have to be navigable. Conceptual spaces, social spaces, task-state spaces all qualify.
2. **Remapping enables multiple cognitive spaces to coexist at different resolutions and hierarchical levels.** The same hippocampal substrate can hold a coarse-grained map of a city alongside a fine-grained map of one's home, switching by context.
3. **Action sequences result in trajectories through cognitive space, simulated via sequential coding (theta sequences) in hippocampus.** This is the architecturally important claim for our question — theta sequences are the simulation primitive, and they operate over whatever cognitive space is currently active.

The empirical anchors are reviewed in the same paper: Constantinescu et al. 2016 (already in this lit-pull) showing conceptual grids; Schuck et al. 2016 showing task-stage decoding in mPFC; Garvert et al. 2017 showing knowledge-graph representations in EC; Bao et al. 2019 showing grid-like coding for olfactory dimensions.

## Why this matters for REE's question

For the user's prediction that theta packaging scales with substrate vocabulary, this paper provides the framework anchor. The biology supports the architectural reading that **the hippocampal cognitive-map machinery is general-purpose across abstraction levels**. Theta sequences — which simulate trajectories through that map — inherit the generality. As REE adds chunk / type / option substrates, the theta-packaging primitive (MECH-089) does not need to change architecturally. The *cognitive map* being navigated changes, and the same theta sequence machinery navigates the new map.

This is exactly the architectural shape the user's intuition predicted. The packaging is general; the content scales because the map scales. When SD-045 (action-chunk cache) lands, the cognitive map gains chunk-nodes; theta sequences traverse them at chunk-granularity. When SD-040 (type-encoder) lands, the map gains type-instance-nodes; theta sequences traverse type-graphs. When SD-042 (option library) lands, the map gains option-edges; theta sequences traverse option-sequences.

For MECH-269 (anchor pool with per-stream V_s) and SD-040 (type-encoder substrate), Bellmund 2018 also licenses the architectural choice of putting type-keyed anchors alongside location-keyed anchors in the same AnchorSet — the biology says they're operating on the same substrate, just with different input projections defining different "navigable dimensions."

## What it does NOT settle

This is a theoretical review, not a primary empirical paper. The specific architectural claim — that theta sequences span abstract cognitive spaces with hierarchical levels — is supported by the anchor empirical work cited in the review but not by primary data in this paper itself. The synthesis is canonical; the empirical close depends on the reader following through to Constantinescu 2016, Schuck 2016, etc.

The "hierarchical levels" Bellmund et al. describe are primarily different *resolutions* of the cognitive map — zoom levels, fine vs coarse spatial maps coexisting. This is similar to but not identical to the substrate-level hierarchy REE distinguishes between motor primitives, action chunks, options, and goal-directed actions. The architectural translation assumes these are the same primitive operating at different scales — plausible, but the paper does not directly defend the equivalence.

The framework is most empirically supported for spatial-to-conceptual generalisation. Extending to action-sequence chunking and to option-level abstraction (the SD-045 / SD-042 territory) is supported by other work (Botvinick 2009 hierarchical RL framework, Schuck 2016 task-stage codes) but not by primary data in this Bellmund review.

## Confidence reasoning

I sit this at 0.82. Source quality 0.85 — *Science*, canonical synthesis from leading authorities, the framework anchor for the cognitive-maps-beyond-space line of work. Mapping fidelity 0.78 because the framework directly licenses theta sequences operating across abstraction levels, which is the architectural primitive the user's prediction requires; the gap is from "different cognitive-map resolutions" to "different substrate-vocabulary levels." Transfer risk 0.30 because the multi-domain cognitive-map framework is well-established and the architectural extension to action-substrate vocabulary is supported by adjacent literature.
