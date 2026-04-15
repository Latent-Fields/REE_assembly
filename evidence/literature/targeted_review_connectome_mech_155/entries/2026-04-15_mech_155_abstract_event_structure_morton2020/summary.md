# Morton, Schlichting & Preston 2020 -- Common Event Structure Representations Support Efficient Inference

**Source:** Morton NW, Schlichting ML, Preston AR. *PNAS* 117(47):29338-29345, 2020. DOI: 10.1073/pnas.1912338117

**Claim tested:** MECH-155 (spatial navigation machinery is a specific instance of general associative indexing operating over different latent domains)

---

## What the paper did

Morton and colleagues asked how the brain represents abstract relational structure that is common across distinct experience contexts -- the kind of structure that would allow an agent to transfer knowledge from familiar situations to novel ones. Participants learned image pairs (AB, BC) drawn from multiple distinct triads (ABC), each triad sharing the same internal relational structure but with different surface content. After learning, they performed transitive inference tests (inferring AC from AB + BC). The key question was whether the hippocampus and associated regions would form representations that coded the *cross-triad common structure* -- a geometric encoding that abstracts away surface content -- and whether this geometry would support inference efficiency.

## Key findings relevant to MECH-155

Hippocampal and frontoparietal regions formed abstract representations with common geometric structure across distinct triads, coding cross-triad relationships despite no explicit instruction to abstract. Parahippocampal cortex showed hierarchical representations that reflected both within-triad and cross-triad geometry simultaneously. Computational modelling of response times dissociated two processes: hippocampal pattern completion (within-context item retrieval) and parahippocampal/parietal vector-based retrieval (cross-context inference). This dissociation suggests that the same indexed representation supports both direct retrieval (navigating to a known location) and inferential traversal (computing a novel path through previously unexplored relationship space).

## REE translation

MECH-155 claims that planning rollout uses the same indexing substrate as spatial navigation. The Morton et al. 2020 result is directly relevant to the planning-rollout sub-claim: the hippocampus constructs geometric structure over abstract relational sequences and then traverses that structure to infer indirect relationships -- the same operation that a planner performs when chaining action steps to reach a distal goal. For the REE E1 architecture, the AB + BC --> AC inference is structurally identical to the trajectory-chaining that planning rollout requires: if the indexed manifold represents relational position, then inference is simply a traversal operation, the same as following a spatial heading to a destination. The direction vector that represents an AB relationship is the same kind of entity as a spatial heading vector, only defined over abstract event space.

## Limitations and caveats

The relational structure tested is simple (ordered triads with one implied dimension), not the full multidimensional manifold that MECH-155 invokes for concept traversal and planning rollout in complex environments. The paper does not demonstrate mechanistic identity between spatial and abstract indexing -- it shows structural parallelism of fMRI geometry, which is an important constraint but not a confirmed shared circuit. The dissociation between hippocampal pattern completion and parahippocampal vector retrieval actually adds complexity: if abstract inference requires a distinct parahippocampal/parietal mechanism not needed for spatial navigation, the 'single substrate' narrative of MECH-155 may be too simple, or the substrate may be distributed across hippocampal-cortical circuits rather than localised to hippocampus alone.

## Confidence reasoning

This paper is strong on the inference/traversal dimension of MECH-155 -- the one aspect that the Constantinescu and Behrens entries address least directly. PNAS publication and Preston lab's sustained experimental and computational program give good source quality. Mapping fidelity is moderate rather than high because the simple triad structure does not map cleanly onto the full generality claim, and the pattern-completion vs. vector-retrieval dissociation adds a complexity that neither confirms nor disconfirms MECH-155 but needs to be accommodated. Confidence 0.74.
