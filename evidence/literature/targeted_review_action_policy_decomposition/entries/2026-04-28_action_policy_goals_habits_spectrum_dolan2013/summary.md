# Dolan & Dayan 2013 — Goals and habits in the brain

According to PubMed: Dolan & Dayan. *Neuron* 80(2):312-325 (2013). [DOI 10.1016/j.neuron.2013.09.007](https://doi.org/10.1016/j.neuron.2013.09.007). PMID 24139036.

## What the paper did

This is the field-level review of the goal-directed vs habit dichotomy from two of its most prominent contributors. Dolan and Dayan survey four generations of experimental work — starting with the foundational behavioural devaluation paradigms (Adams 1982, Dickinson & Balleine 1994), through the computational model-based / model-free formalism (Daw 2005, Sutton & Barto), through human fMRI and rodent lesion dissociations, and into the most recent generation showing shared circuitry and rich interactions between the systems.

Their central argument is a refinement of the canonical two-system framing. The dichotomy is real but it is better understood as a *spectrum* than as two discretely separated subsystems. The "model-based" and "model-free" labels still apply to the ends of the spectrum, but: the systems share substantial circuitry (the same basal ganglia, the same PFC, with overlapping representations), they interact rather than competing as cleanly separated controllers, and the apparent dichotomy in behavioural measures may reflect a parametric mixture rather than a winner-takes-all arbitration. Pavlovian-to-instrumental transfer paradigms reveal additional intermediate behavioural levels that the strict two-system framing struggles to accommodate.

The "fifth generation" work the paper points toward is still unfolding: shared neural codes for model-based and model-free values in striatum, mixed strategies that don't decompose cleanly into either system, and the open question of whether the dichotomy is computationally meaningful or just a useful descriptive tool.

## Why this matters for REE's decomposition question

This paper provides the meta-architectural constraint that the canonical two-system framing of Daw 2005 has been *refined upward* into a spectrum framing in the field's mature reading. For REE that has architectural consequences. The simple commitment "build a habit-cache substrate and a goal-directed planner as fully separate systems" overshoots the biology. The biology says the systems share substantial circuitry and interact richly.

This reads naturally onto REE's existing ARC-021 framework, which already specifies three BG-like cortico-striatal loops with distinct learning channels. Three loops sharing input (from cortex) and output (to thalamus), differing in internal learning channels and timescales — that is exactly the kind of "shared circuitry, distinct functional roles" architecture the Dolan-Dayan spectrum framing describes. REE's ARC-021 is structurally well-positioned for the modern reading.

The architectural inference for any new habit / chunked-action substrate (the one Graybiel 2008 motivates): integrate it *with* the existing planner machinery, not as a parallel system. A habit cache should be a cached lookup that the HippocampalModule.propose_trajectories or the E3 selector queries *before* falling through to CEM rollout. Not a separate controller competing with the planner. This matches Dolan-Dayan's spectrum reading: the same circuit produces different behavioural signatures depending on parameters and context, rather than two circuits competing for dominance.

## What it does NOT settle

The "spectrum" framing is harder to operationalise architecturally than the "two systems" framing. REE has to commit to specific substrates with specific operators; the spectrum reading licenses richness but does not specify exactly which intermediate substrates to build. A V3 implementation pass would likely simplify to a two-system starting point (habit cache + planner) and refine toward the spectrum framing as evidence demands. The honest reading is that the field has not yet provided a tractable computational specification of "the spectrum" that REE could implement directly.

The paper does not address hierarchical / option-level action representation. The decomposition Dolan & Dayan discuss is goal-directed vs habit; the option level (Botvinick 2009, separate entry in this review) is orthogonal. REE's architectural mapping has to resolve both dimensions, and Dolan-Dayan only constrain one of them.

The "fifth generation" work the paper points to is recent enough that the architectural picture is still evolving. Any REE substrate decision based on Dolan-Dayan's reading should remain provisional and tagged for re-review when subsequent empirical work sharpens the picture.

## Confidence reasoning

I sit this at 0.82. Source quality 0.88 — *Neuron*, two leading authorities, definitive review of the dichotomy literature. Mapping fidelity 0.75 because the spectrum framing is architecturally more honest than the two-system framing but harder to translate directly into REE substrate decisions; the architectural recommendation it licenses (integrate habit substrate with planner machinery rather than as parallel system) is direct and useful. Transfer risk 0.30 because the framework is computational/theoretical and translates directly to REE's architectural scaffolding.
