# Wilson, Takahashi, Schoenbaum & Niv 2014 -- Orbitofrontal Cortex as a Cognitive Map of Task Space

According to PubMed ([DOI](https://doi.org/10.1016/j.neuron.2013.11.005)).

## What the paper does

Wilson and colleagues propose a unifying account of orbitofrontal cortex function. OFC, they argue, supplies an abstraction of currently available information in the form of a *label* for the current task state. That label is then used by reinforcement learning machinery elsewhere -- the dopaminergic system, dorsal and ventral striatum -- to compute value and to learn associations. The function is especially load-bearing when the task state includes unobservable information that the agent must infer rather than perceive: working-memory contingencies, partially observable contexts, hidden reversals. The paper walks through reversal learning, delayed alternation, extinction, and devaluation, and shows that the OFC-labelling theory accounts for all of them -- including the otherwise puzzling finding that OFC lesions disrupt dopaminergic prediction errors in VTA during partially observable tasks.

## Why it matters for V_s invalidation -- the local accumulator question

For my purposes this is the most architecturally consequential paper in the pull. V_s is essentially the verisimilitude of a regional schema -- a graded measure of how well the currently anchored model captures the regional dynamics. The OFC-as-cognitive-map-of-task-space framing is the same construct from a different angle: OFC labels the current latent state, the label gates downstream learning, and changes in the label are changes in the operative schema. If we are looking for the local *accumulator* in MECH-284 -- the substrate that integrates broadcast invalidation signals into a per-schema staleness measure -- OFC representational drift is the strongest candidate the literature provides.

The strength of the mapping is structural. OFC-labelling and V_s play the same role in their respective architectures: both are intermediate state representations that gate downstream computation; both update in response to violations; both must shift discretely (or near-discretely) when the underlying state is judged to have changed. The reversal-learning evidence in particular -- where OFC lesions abolish the ability to update inferred state when sensory observations are unchanged but contingencies have flipped -- is the empirical anchor I would cite when arguing that the local-accumulator role is real biology, not just a theoretical placeholder.

## What the paper does not do

It does not measure V_s. It does not measure online-waking schema downweighting per se -- the experiments it explains are about how OFC supports learning in the next trial, not about how OFC integrates a sequence of mismatches over a window. Whether OFC's representational drift is graded (compatible with continuous V_s) or threshold-crossing (compatible with discrete re-anchoring) is not specified. And the Stalnaker-Cooch-Schoenbaum 2015 critique (next paper in this pull) explicitly cautions against the field's tendency to attribute every cognitive function to OFC -- so the mapping should be made carefully and with the boundary case in mind.

## Clinical resonance

The OFC-lesion phenotype maps cleanly to the V3-EXQ-475 freeze re-commit pattern. If OFC cannot update its labelling, the agent will keep treating the current state as the previously labelled state even when the broadcast trigger (DA dip / LHb burst) is firing repeatedly. The agent notices that something is wrong but cannot relocate itself in task space. Bechara-Damasio gambling-task patients display the same pattern in a different form: trigger intact, accumulator-integration broken. Catatonia subtype II in our internal taxonomy looks like an even more severe version: not just integration failure but lock-in of the anchor itself.

## Confidence reasoning

Source quality very high (Neuron, top-tier authorship). Mapping fidelity high (0.80) because the cognitive-map-of-task-space construct is essentially V_s under another name. Transfer risk low (0.25). Aggregate 0.78 -- the highest in the pull, reflecting that this paper carries the most architectural weight for the local-accumulator role.
