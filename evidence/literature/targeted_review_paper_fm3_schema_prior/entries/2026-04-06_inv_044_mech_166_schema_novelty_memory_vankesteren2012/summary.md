# Van Kesteren et al. (2012) — How schema and novelty augment memory formation

**Source:** Van Kesteren MTR, Ruiter DJ, Fernandez G, Henson RN. How schema and novelty augment memory formation. *Trends in Neurosciences* 2012; 35(4): 211–219. DOI: [10.1016/j.tins.2012.02.001](https://doi.org/10.1016/j.tins.2012.02.001)

## What the paper argues

Van Kesteren and colleagues synthesise animal lesion and human neuroimaging evidence to propose the SLIMM model (Schema-Linked Interactions between Medial Prefrontal and Medial Temporal Regions). The central observation is that information congruent with an existing neocortical schema is encoded and consolidated faster and more durably than incongruent information. mPFC is proposed to act as a congruence detector: when incoming information matches a pre-existing schema in neocortex, mPFC promotes rapid direct neocortical encoding, bypassing the slow iterative hippocampal-dependent route. When no schema exists — or when new information is sufficiently incongruent — the system defaults to the slow multi-year consolidation pathway.

The model extends standard systems consolidation theory by adding mPFC as a gating node. The gate has a prerequisite: it can only open if the schema is already present in neocortex. This makes schema installation causally prior to schema-congruent rapid assimilation, not merely temporally prior: the mechanism requires the prior structure to exist before it can function.

## How this connects to FM3 (slot-formation before slot-filling)

The SLIMM model is a neural instantiation of the slot-formation-precedes-slot-filling constraint. The neocortical schema is the installed context prior — the structural representation specifying which distinctions matter and how they relate. mPFC congruence-gating is the check that a slot exists before filling begins. When the prior is installed, new episodes (slot-fillers) are rapidly assimilated into existing structure. When it is absent, the system must proceed without structure, and the result is slow, fragile, hippocampus-dependent encoding — equivalent, in the FM3 argument, to attempting to learn the slot topology and fill the slots simultaneously.

The paper thus provides neural-mechanistic support for both INV-044 (approximate Bayesian contextual inference requires prior construction before posterior inference) and MECH-166 (slot-formation and slot-filling are computationally separated): the SLIMM gate is the neural signature of that separation. The gate's prerequisite is the installed prior; its output is rapid episodic attribution into pre-formed slots.

## Honest caveats

Van Kesteren et al. do not frame their argument in Bayesian terms, and the paper does not model what happens when schema formation and episodic encoding are attempted concurrently. The evidence addresses the contrast between schema-present and schema-absent conditions, not the specific failure mode of simultaneous co-computation producing a degenerate prior that shifts during inference. The FM3 failure-mode prediction — that online co-computation produces systematic attribution noise regardless of training duration — is an inference from the structural logic of the model, not a result directly demonstrated in this paper.

Transfer from the semantic/spatial schema domain (the paper's content) to REE causal attribution context slots requires extending the scope. The paper's 'congruent vs. incongruent' binary also does not capture the graded prior quality effects that the Bayesian formulation predicts. These are honest gaps, not disqualifying ones: the SLIMM model is a compelling neural account of why structure-first matters, even if it does not directly formalise the consequences of violating that constraint.

## Why cite this in §3

Tse et al. (2007) established the behavioural consequence of schema-enabled rapid assimilation in rodents. Van Kesteren et al. (2012) extend this to a full neural-systems mechanistic account — the mPFC gating mechanism — and ground it in human neuroimaging as well as animal lesion work. For a paper arguing that offline phases are necessary rather than merely helpful, having the neural mechanism (not just the behavioural effect) strengthens the case that this is an architectural constraint, not an engineering optimisation. The SLIMM model makes the prior-installation requirement explicit at the circuit level.
