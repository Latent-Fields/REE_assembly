# Dolan & Dayan 2013 -- Goals and Habits in the Brain: MECH-163 Mapping

**Source:** Dolan, R.J. & Dayan, P. (2013). Goals and Habits in the Brain. *Neuron*, 80(2), 312-325. DOI: [10.1016/j.neuron.2013.09.007](https://doi.org/10.1016/j.neuron.2013.09.007)

---

## What the Paper Does

Dolan and Dayan provide a synthesis of computational reinforcement learning theory with the neuroscience of goal-directed and habitual action. The paper identifies two distinct control systems: a model-free habitual system tied to dopamine-dependent learning in the dorsolateral striatum (SNc/nigrostriatal pathway), and a model-based goal-directed system requiring prefrontal cortex for the maintenance of action-outcome representations. The paper is explicitly framed around the question of why both systems exist and what happens when their balance is disrupted.

The model-free system (dorsolateral striatum) learns stimulus-response (S-R) associations via cached value functions -- what reinforcement learning calls Q-values. These are computed by integrating reward prediction errors over prior experience. The system is computationally cheap: once values are cached, action selection requires only a lookup. But it is inflexible: the cached values do not update with new outcome information until the associations are retrained.

The model-based system (prefrontal cortex and associated circuits) maintains an internal model of the environment -- action-outcome contingencies -- and can compute action values on-the-fly by simulating trajectories through the model. This allows it to be sensitive to outcome devaluation and contingency degradation immediately, without retraining. It is computationally expensive but accurate in novel or changing environments.

## Key Findings

The core empirical evidence comes from three converging lines:

1. **Outcome devaluation studies** in rodents and humans: goal-directed actions (requiring the model-based system) become insensitive to their usual outcomes after devaluation; habitual actions do not update until retrained. This behavioral double dissociation directly demonstrates the architectural separation.

2. **Neural anatomy**: dorsomedial striatum and prelimbic/medial PFC are necessary for goal-directed action; dorsolateral striatum for habitual action. The dopaminergic substrates differ: SNc projects primarily to dorsolateral striatum (nigrostriatal pathway); VTA projects primarily to ventral striatum and PFC (mesolimbic/mesocortical pathways).

3. **Psychopathology**: addiction and OCD are characterised as imbalances between the two systems. Addiction involves excessive model-free control (habit dominance) -- continued drug-seeking even when the drug is devalued. OCD may involve dysregulation of goal-directed suppression of habitual routines. This psychopathological framing is significant for MECH-163: it implies that the ethical failures associated with habit-system dominance (context-blind harm) have empirical analogues in human pathology.

## REE Mapping to MECH-163

MECH-163 claims that both the habit system (SNc/dorsal-striatum, model-free) and the hippocampally-planned system (VTA/hippocampus + PFC, model-based) are necessary for ethical agency. Dolan and Dayan directly support this necessity claim.

The REE habit system maps onto Dolan/Dayan's habitual system: it handles approach to familiar resources by caching S-R associations from cumulative experience. The devaluation insensitivity of the habitual system is precisely the architectural limitation MECH-163 identifies -- this system cannot attribute harm across novel contexts because it has no mechanism to evaluate whether cached associations remain valid in changed circumstances.

The REE planned system (E3 hippocampal) maps onto Dolan/Dayan's goal-directed system, with the addition of the hippocampal contribution for multi-step trajectory generation (which Dolan/Dayan attribute primarily to PFC). The REE extension is that harm/benefit evaluation over longer planning horizons requires hippocampal trajectory generation, not just PFC action-outcome representation.

## Limitations and Confidence Reasoning

The main gap in the mapping is that Dolan and Dayan frame the model-based system primarily around prefrontal cortex rather than foregrounding the hippocampal contribution to multi-step planning. MECH-163's claim that the hippocampally-planned system generates multi-step harm/benefit trajectories requires reading Dolan/Dayan together with hippocampal planning literature (e.g., Balleine & O'Doherty 2010). The harm/benefit evaluation dimension of MECH-163 is also a REE-specific extension not directly tested in this review. Confidence: 0.85.

*Based on article available via PubMed (PMID: 24139036) and PubMed Central (PMC3807793).*
