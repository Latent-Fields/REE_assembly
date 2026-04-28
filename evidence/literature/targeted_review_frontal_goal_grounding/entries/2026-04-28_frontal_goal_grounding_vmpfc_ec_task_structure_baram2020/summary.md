# Baram, Muller, Nili, Garvert & Behrens 2020 — EC and vmPFC abstract and generalise RL task structure

According to PubMed: Baram, Muller, Nili, Garvert & Behrens. *Neuron* 109(4):713-723.e7 (2020 Dec). [DOI 10.1016/j.neuron.2020.11.024](https://doi.org/10.1016/j.neuron.2020.11.024). PMID 33357385.

## What the paper did

Human subjects solved multiple reinforcement-learning problems while undergoing fMRI. The clever bit is the task-remapping paradigm: problems were systematically varied along two orthogonal axes — *structural* properties (the underlying state-state graph, transition geometry, reward distribution shape) and *sensory* properties (the identities of the stimuli that instantiate the structure). This lets representational similarity analysis ask: when neural geometry is preserved across two problems, is it being preserved because the surface stimuli are the same, or because the underlying graph is the same?

The result is clean. Entorhinal cortex representations are preserved across different RL problems if and only if task structure is preserved — surface stimulus identity does not drive entorhinal geometry. Ventromedial prefrontal cortex representations of prediction error show the same dependence: vmPFC PE geometry tracks the structural graph, not the observed stimuli.

## Why this matters for REE's question

The REE question is whether frontal subdivisions consume rich associative content via top-down query, or hold compact handles directly. Baram 2020 is the strongest direct support in this set for the rich-content reading of vmPFC. vmPFC encodes the abstract structural geometry of the RL problem, not a compact "the goal is X" handle. The geometry preserves across surface-different problems with the same structure and *fails* to preserve across structure-different problems.

But the rich content vmPFC carries is not "the goal as a feature vector." It is the task-graph topology in which the goal is embedded. This is an important refinement of the user's intuition. The user's framing was "z_goal as a query, E1 as the rich associative store, frontal reads from E1 keyed by z_goal." The biology suggests the rich store is the task-graph itself, and vmPFC *holds the graph* — not as an external rich substrate that vmPFC queries, but as vmPFC's own intrinsic representation when given enough trials in a stable task structure.

For REE V3, this maps onto [ARC-035](REE_assembly/docs/claims/claims.yaml) and [SD-033b](ree-v3/ree_core/pfc/ofc_analog.py). The MECH-292 anchor `goal_payload` geometry — `z_goal_snapshot + wanting + arousal_tag` per anchor — defines a small task-graph fragment around each anchor. The Baram 2020 architectural insight is: vmPFC analogue should be where these anchor fragments get compressed into a *generalisable structural code* that maintains its similarity geometry across different goal instances with the same structural shape. That graph-structure-encoding capacity is currently absent in REE's ARC-035 substrate. Adding it would be a V4 architectural extension when richer environments require it; in V3's grid-world the task structure is largely fixed and the absence is not load-bearing.

## What it does NOT settle

The paper studies humans on RL tasks via fMRI — group-level statistical maps, not single-unit recording. It cannot say at a mechanistic level whether the structural geometry is computed by vmPFC locally, queried from EC by vmPFC, or held jointly across both substrates with thalamic routing. It also studies a particular notion of "structure" (RL state-graph topology) that is narrower than what REE means by task structure (residue terrain + anchor geometry + drive landscape). The transfer is plausible — both share the property that surface stimuli vary while abstract relations remain — but is not directly tested.

It does not address SD-033a (lateral PFC rule-state) or SD-032b (dACC adaptive control). Those PFC subdivisions might or might not implement the same rich-structural-encoding strategy.

## Confidence reasoning

I sit this at 0.80. Source quality 0.85 — *Neuron*, RSA methodology, structural-vs-sensory dissociation is the right experimental design for the architectural question. Mapping fidelity 0.72 because the rich-encoding result transfers to ARC-035 / SD-033b but only in the V4 timeframe where REE handles richer environments. Transfer risk 0.35 because the structure-vs-content distinction the paper makes is properly captured in REE's anchor-geometry framing, and the human-fMRI-to-substrate transfer is the standard one.
