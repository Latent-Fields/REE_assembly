# Kanai, Komura, Shipp & Friston 2015 -- Cerebral hierarchies: predictive processing, precision and the pulvinar

## What the paper did

Kanai and colleagues addressed a missing piece in the predictive-processing programme: what mechanism orchestrates and contextualises message passing across cortical hierarchies? Their answer was that the pulvinar, a higher-order thalamic nucleus with extensive reciprocal connections to most cortical areas, delivers per-cortical-region modulatory gain control on prediction errors. They distinguished two classes of extrinsic connection: driving (first-order) connections that carry content -- the predictions and prediction errors themselves -- and modulatory (second-order) connections that carry context, in the form of salience or precision. The pulvinar is the substrate for the latter. Feature-ground segregation simulations demonstrated the computational consequences.

## Key findings relevant to MECH-269b

This is the strongest direct hit in the anchor list for MECH-269b cortex-side gate. The pulvinar-cortex precision channel is the substrate-equivalent of MECH-269b V_s applied to E1 / E2 streams: a dedicated thalamic substrate computes the precision parameter externally to the receiving cortical area and broadcasts it to consumers. This mirrors REE design, in which V_s is computed in a separate verisimilitude-tracking module and broadcast to E1, E2, and onward to dACC. The two-stream architecture in Kanai et al. (driving content vs modulatory precision) maps directly onto MECH-269b separation of stream content (the latent z) from stream gain (V_s).

This is tag (a) direct cortex-side per-stream precision gating, biologically grounded in pulvinar circuitry, and explicitly framed in terms compatible with MECH-269b architectural intent.

## How the findings translate to REE

REE inherits the pulvinar-mediated precision-gating substrate as the implementation of MECH-269b cortex-side gate. The architectural prediction is that V_s is consumed in cortical regions corresponding to E1 and E2 via the same modulatory pathway that the pulvinar uses for attentional gain control. The mechanism transfers cleanly because the predictive-coding framework Kanai et al. work in is the same framework REE uses for cortical inference.

## Limitations and caveats

Two genuine gaps. First, the granularity in Kanai et al. is per cortical region, not per content stream within a region. MECH-269b claim is that precision can be set independently for each latent stream (z_world, z_self, z_harm_s, z_harm_a, z_goal). Under REE mapping each stream corresponds to a different anatomical territory, so per-region pulvinar gating is a usable substrate, but the per-stream specialisation is a forward extension that the pulvinar literature does not directly demonstrate. Second, and more importantly for MECH-269b symmetric-application novelty, the paper does not engage with hippocampal anchor selection at all -- the frame is cortical hierarchies plus thalamus. The symmetric-V_s-application claim cannot be confirmed or denied from this evidence; it is a measurement gap (tag d).

## Confidence reasoning

Confidence 0.78 -- supports MECH-269b cortex-side gate at the architectural level, with the strongest substrate proposal in the anchor list. Source quality high (top-tier theoretical review, anatomically grounded). Mapping fidelity high because pulvinar-cortex precision gating is essentially the cortical specialisation of what MECH-269b proposes. Transfer risk low because the mechanism is broadly cortical and applies across sensory and association areas. The remaining gap is the symmetric application across hippocampal vs cortical modules, which this paper does not address.
