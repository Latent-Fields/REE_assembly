# Summary: Koene et al. 2003 — Modeling Goal-Directed Spatial Navigation via PFC-Hippocampal Working Memory

**Entry ID:** 2026-04-04_mech_128_pfc_wm_goal_hippocampal_prediction_koene2003
**Claim:** MECH-128 (e1.goal_context_conditioning)
**Evidence direction:** supports | **Confidence:** 0.68

---

What would it look like if a predictive hippocampal system tried to generate goal-directed trajectories without access to goal information held in prefrontal working memory? The Hasselmo lab's 2003 Neural Networks model gives a clear answer: it would not generate goal-directed trajectories at all. The model shows that retrieval of known paths in hippocampal CA1/ECIII requires input from PFC working memory holding the goal location; absent this input, the hippocampal system generates spiking activity that is environmentally contextualised but goal-agnostic. This is precisely the failure mode that MECH-128 is designed to prevent in E1.

The circuit topology the model describes is a multi-stage pathway: PFC holds goal location in working memory, this goal representation gates activity in entorhinal cortex layer III, and ECIII provides the conditioning drive that biases CA1 to generate predictive spiking for the next desired location on the shortest path to the goal. Reading this through the REE lens: PFC working memory is z_goal_latent, ECIII is the injection interface, CA1 predictive spiking is E1's trajectory generation. MECH-128 proposes collapsing the multi-stage biological pathway into a single direct injection -- z_goal_latent fed at each LSTM step -- which simplifies the circuit but preserves the causal logic.

The Hasselmo group's model also gives something the Gonner model does not: it uses theta oscillations to gate retrieval phases, with different path segments predicted at different theta sub-phases. This resonates with the broader ARC-023/MECH-089 architecture in REE (theta-gamma nesting packaging E1 updates for E3). The MECH-128 claim does not require theta-phase gating in its current V3 formulation -- it only requires that z_goal be present in the LSTM input at each step -- but it is worth noting that the biological mechanism is more temporally structured than the simplified LSTM version implies.

The age of this paper (2003) is a legitimate concern. Hippocampal circuit modelling has advanced substantially since then, and specific claims about the role of ECIII as the goal-conditioning interface have been revised in later literature. The core finding -- that PFC working memory is causally upstream of goal-shaped hippocampal prediction -- has held up, but the detailed circuit topology may not. The rat spatial navigation context also limits generalisability; E1 in REE generates predictive trajectories in an abstract latent space, not a spatial map.

On balance, this paper provides foundational biological support for the causal claim at the heart of MECH-128: a recurrent predictive system (hippocampus/E1) requires goal information from a working memory store (PFC/z_goal) to generate goal-shaped trajectory predictions. The evidence is indirect by modern standards but grounded in explicit computational modelling with biologically constrained parameters. The confidence penalty reflects age, spatial specificity, and architectural simplification risk.
