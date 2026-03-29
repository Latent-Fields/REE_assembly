# Causal Inference Gates Corticostriatal Learning
**Dorfman, Tomov, Cheung, Clarke, Gershman & Hughes (2021) — Journal of Neuroscience**
DOI: 10.1523/JNEUROSCI.2796-20.2021 | PMID: 34244363

## What the paper did

The authors asked whether the brain's learning system treats outcomes differently depending on whether the agent believes they caused them. They used a behavioral task that manipulated beliefs about causal structure -- participants completed trials where the probability that their actions caused observed outcomes was experimentally varied. fMRI was recorded while participants completed the task, allowing the authors to ask where in the brain reward prediction errors are modulated by causal beliefs and where they are not.

## Key findings

Two dissociable prediction error signals were found. Standard (unmodulated) RPEs were represented in ventral striatum -- consistent with classic dopaminergic reward encoding. RPEs modulated by causal beliefs (did I cause this?) were represented in dorsal striatum. Critically, causal beliefs themselves were encoded in anterior insula and inferior frontal gyrus. Structural equation modeling revealed effective connectivity from anterior insula to dorsal striatum, suggesting that the insula's causal-belief representation gates how outcomes are credited to actions in the dorsal striatal learning channel.

The architecture is therefore a layered one: ventral striatum tracks raw value; dorsal striatum tracks action-attributable value, filtered by insula-represented causal beliefs. The agent learns which of its actions caused which outcomes via a dedicated circuit, rather than treating all outcomes as equally informative about action value.

## REE translation -- link to MECH-071

MECH-071 predicts that E2's harm prediction is better calibrated for agent-caused transitions than environment-caused ones. This paper provides the neural architecture that would implement that asymmetry at the learning level: a causal-inference gate that selectively routes harm-relevant prediction errors based on whether the agent was the cause.

In REE terms, the anterior insula's causal-belief computation corresponds to the attribution stage that must occur before E3 learns from harm events. When E3 receives a harm signal from z_harm_s, it needs to ask: did I cause this, or did the environment impose it? If the biological brain uses an insula-to-dorsal-striatum gating mechanism for this, REE's E3 needs an analogous circuit -- a causal attribution module whose output modulates how harm prediction errors are weighted for learning. MECH-071's calibration asymmetry would then follow naturally: agent-caused harm errors are heavily weighted (routed through the causal-attribution channel), environment-caused harm errors are not, so the learning system becomes asymmetrically expert at predicting the former.

There is also a convergence with ARC-021's incommensurable error signal argument. The dorsal/ventral striatum dissociation supports the claim that harm-from-action and harm-from-environment should be treated as distinct learning channels rather than averaged together. Collapsing them would misattribute credit -- which is exactly the failure mode ARC-021 identifies.

## Limitations and caveats

The paper studies reward credit assignment, not harm. Harm and reward have overlapping but distinct neural substrates; the insula is implicated in both, but whether the identical causal-gating mechanism operates for harm-from-action attribution is not established by this paper. The effective connectivity finding is from structural equation modeling, which estimates influence rather than demonstrating it causally. The sample (n=31) is moderate and the task involved explicit probabilistic causal cues rather than the implicit causal structure that would be inferred from observation in a naturalistic harm context.

For REE's purposes, the deeper question is whether E3's harm-learning pathway has access to a causal-attribution signal at all. If z_harm_s conflates agent-caused and environment-caused harm, there is nothing to gate -- which is part of why SD-011 (dual nociceptive streams) is architecturally necessary before MECH-071 can be properly tested.

## Confidence reasoning

Journal of Neuroscience 2021, reasonable sample, clean experimental manipulation of causal beliefs, convergent behavioral and imaging results. Mapping fidelity is moderate -- the mechanism (causal gating of prediction errors) is right but the domain is reward not harm. Confidence 0.72.
