# Desmedt (2021) -- (Re)contextualizing the Trauma to Prevent or Treat PTSD-Related Hypermnesia

## What the paper did

Desmedt, working at INSERM Bordeaux, reported a series of preclinical experiments and a theoretical reframing of PTSD memory pathology. The central argument is that the traditional treatment focus on fear hypermnesia -- intrusive emotional memory, flashbacks, conditioned fear responding -- has been addressing a symptom rather than its cause. The cause, Desmedt argues, is contextual amnesia: the failure to encode a hippocampal-dependent contextual memory of the traumatic event alongside the amygdala-dependent emotional memory. Three converging experimental approaches in rodents -- cognitive-behavioural contextual enhancement, optogenetic activation of hippocampal neurons during trauma recall, and pharmacological enhancement of hippocampal NMDA-dependent plasticity -- all durably prevented and treated fear hypermnesia by restoring contextual binding.

## Key findings relevant to MECH-072

The key causal result is that contextual amnesia is not just a co-symptom of PTSD but the mechanistic driver of hypermnesia. When the contextual memory is strengthened (by any of the three routes), the fear hypermnesia diminishes -- durably, not just acutely. The hypermnesia is not caused by "too strong" an emotional trace but by a "too weak" contextual trace that fails to constrain when and where the emotional trace activates.

This causal inversion matters for MECH-072. The biological evidence shows that the system controlling whether a harm signal fires is not the harm signal itself but the contextual/causal information that gates its expression. Strengthen the contextual binding, and harm responding becomes appropriate; weaken it, and harm responding becomes diffuse and false-positive-prone.

## Translation to MECH-072

MECH-072 claims that residue accumulation should be gated by foreseeable harm: residue should only accumulate when E2_harm_s predicts that the agent's action would lead to harm (harm_pred > threshold). This is a causal/contextual gate: it asks whether the harm was predictable from the agent's perspective at decision time, rather than simply whether harm occurred proximate to the agent.

Desmedt's finding provides the most direct biological evidence for why such a gate is necessary. Without it, the residue field accumulates trace at all harm events near the agent -- the computational equivalent of decontextualised fear hypermnesia. With the gate, residue accumulates only where the agent's action was causally implicated in a way the agent could have anticipated. This is the computational version of contextual binding: it constrains when the harm trace is written based on causal/contextual information.

The optogenetic arm of Desmedt's work is particularly compelling because it provides a causal demonstration: artificially activating hippocampal neurons that encode context, during a recall session, durably suppressed hypermnesia. In REE terms, this is analogous to ensuring that E2_harm_s correctly predicts harm before allowing residue accumulation -- if the forward model predicts no harm, no residue is written, regardless of what actually happened environmentally.

## Limitations and caveats

All evidence is from rodents. The contextual memory failure in PTSD models uses simple contextual cues (cage, environment, conditioned stimulus pairings). MECH-072's foreseeable-harm judgment is considerably more sophisticated: it requires a learned forward model to predict harm under actual versus counterfactual action. The biological evidence shows contextual gating is important but does not validate the specific implementation MECH-072 proposes.

The stage of processing is also different: Desmedt's work addresses memory consolidation and retrieval, while MECH-072's gate operates at residue write time during the agent's action sequence. These are not equivalent stages.

## Confidence reasoning

Moderately strong source (INSERM lab, optogenetic causal evidence, published in peer-reviewed journal). The mapping is the most direct available for MECH-072 but still requires significant inferential steps. Rodent-only evidence limits generalisability. Overall confidence 0.58.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1177/24705470211021073
