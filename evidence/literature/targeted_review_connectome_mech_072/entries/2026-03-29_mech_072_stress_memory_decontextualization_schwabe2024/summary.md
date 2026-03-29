# Schwabe (2024) -- Memory Under Stress: From Adaptation to Disorder

## What the paper did

Schwabe's review in Biological Psychiatry synthesises two decades of research on how stress alters memory across four processes: formation, contextualisation, retrieval, and flexibility. The review is organised around the dual adaptive/pathological nature of stress-induced memory changes: the same neurobiological mechanisms that promote efficient coping with novel threats can, under the wrong conditions or in the wrong individual, produce the rigid, intrusive, generalised fear-responding characteristic of PTSD and anxiety disorders. Mechanistically, the review focuses on stress hormone (glucocorticoid and catecholamine) effects on hippocampal contextual encoding, amygdala emotional encoding, and prefrontal executive control.

## Key findings relevant to MECH-072

The review's central finding for this purpose is the characterisation of stress-induced decontextualisation: stress mediators produce memory representations that retain strong sensory and emotional content (amygdala-dependent) but lose hippocampal-dependent contextual binding -- the associations between the event and its spatial, temporal, and causal context. This dissociation is adaptive in the short term (stimulus-response responding without computationally expensive contextual retrieval) but maladaptive when it persists, because it strips harm memories of the information needed to determine when and why harm occurred.

The review describes contextual processing as specifically a hippocampal associative learning problem. When hippocampal function is disrupted by stress hormones, the organism retains strong emotional responses to harm-associated stimuli but cannot accurately contextualise those responses -- cannot distinguish "this is the specific situation in which harm occurred" from "any situation with superficial resemblance to where harm occurred." The result is overgeneralised fear and intrusive recall.

## Translation to MECH-072

MECH-072 proposes that residue accumulation in REE should be gated by foreseeable harm: only accumulate moral causal trace when the agent could plausibly have anticipated the harm given what was known at decision time. Schwabe's framework motivates this gate from the opposite direction: what happens when contextual information is unavailable or unreliable for attribution judgments?

Without a foreseeable-harm gate, the REE residue field would accumulate trace at any harm event proximate to the agent's action -- including environmentally-caused harms that happened to co-occur with the agent's presence. This is computationally analogous to the stress-induced decontextualised memory: strong signal at harm events, no contextual filter on whether the agent caused them. Just as hippocampal contextual binding is what prevents overgeneralised fear responding in biology, the foreseeable-harm gate is what prevents false residue accumulation in REE.

The review also touches on the dual-pathway model of episodic memory (contextual hippocampal vs affective amygdalar) which maps loosely onto z_harm_a (affective, less contextual) and z_harm_s (discriminative, more action-conditional and therefore more contextually informative for attribution).

## Limitations and caveats

The mapping is at the level of functional analogy, not mechanistic identity. MECH-072's gate operates at action time, during residue writes; Schwabe's framework addresses memory encoding and retrieval processes that happen over longer timescales. REE does not currently implement anything resembling stress-hormone modulation of hippocampal contextual binding. The paper provides conceptual motivation for why a contextual/foreseeable gate is needed, but does not directly test the kind of gating mechanism MECH-072 proposes.

The V3 experimental record on MECH-072 also shows persistent failure (EXQ-054 FAIL, EXQ-028 FAIL) due to z_world conflating agent and environment dynamics -- a technical failure that this literature cannot address.

## Confidence reasoning

High-quality review (Biological Psychiatry, prominent author). The conceptual mapping is coherent but indirect. Transfer risk is moderate-high because the biological and computational mechanisms are different. Overall confidence 0.60.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1016/j.biopsych.2024.06.005
