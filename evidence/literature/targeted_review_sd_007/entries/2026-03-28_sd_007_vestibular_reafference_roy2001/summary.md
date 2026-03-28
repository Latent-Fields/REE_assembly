# Roy & Cullen 2001 — Selective processing of vestibular reafference during self-generated head motion

Based on articles retrieved from PubMed (DOI: [10.1523/JNEUROSCI.21-06-02131.2001](https://doi.org/10.1523/JNEUROSCI.21-06-02131.2001)).

## What the paper did

Roy and Cullen recorded single-unit activity from vestibular nucleus neurons in alert rhesus macaques across a range of active and passive head movement conditions. The design was careful: they compared passive whole-body rotation (head fixed to body), passive head-on-body rotation (body held still, head moved), and active head-on-body movements (monkey voluntarily moved its head by activating neck musculature). They also included a critical control — the monkey actively drove its whole head-body unit through space by rotating a steering wheel with its arm, which does not involve neck muscle activation.

## Key findings

The result is clean and mechanistically specific: vestibular nucleus neurons encoded head-in-space velocity during passive rotation but were strongly suppressed during active head-on-body movements. The suppression was not explained by neck proprioceptive feedback (passive head movement produced by external force to the head, even with the neck muscles loaded, did not suppress the neurons). Crucially, when the monkey moved itself through space by rotating a wheel — without activating neck muscles — vestibular neurons were not suppressed and reliably encoded head-in-space velocity. The suppression gate is efference copy of the neck motor command, not knowledge of self-generated motion, not proprioception.

## REE mapping

This is the empirical anchor for a key design judgment in SD-007. The REE ReafferencePredictor takes z_world_raw_prev and a_prev as inputs — it does not take z_self_prev. One might ask: why not use the body state? Wouldn't knowing the agent's velocity be sufficient to predict the expected visual shift? Roy and Cullen's data give a direct answer from biology: in the vestibular system, the suppression mechanism uses the motor command (efference copy), not the proprioceptive signal from the muscles that were activated. The motor command is what specifies the intended movement before its sensory consequences arrive. In REE, a_prev plays this role: it is the action token that was issued, before the resultant z_world_raw change is observed.

The additional design note in SD-007 — that z_world_raw_prev (not z_self_prev) is the input — extends this logic to what the predictor must predict. In a gridworld, the cell content entering the agent's view depends on the world state ahead of the agent, not on the agent's body state per se. Z_world_raw captures this; z_self does not. Roy & Cullen's finding that body-state signals (proprioception) alone do not drive cancellation maps onto this: you cannot compute the world-side consequence of movement from body-state information alone.

## Limitations and caveats

The biological system being studied is the vestibular system, which cancels rotational and translational head-in-space signals. SD-007's ReafferencePredictor targets visual perspective shift in a two-dimensional gridworld. These are different sensory modalities and different computational substrates. The transfer claim is that the principle — efference-copy-based cancellation of motor-induced sensory change — is conserved across modalities; this is supported by subsequent work (Brooks & Cullen 2019 review) but was not directly demonstrated for visual processing by this paper. The macaque context also means the biological implementation involves specific cerebellar and vestibular nucleus circuitry with no direct REE analogue.

## Confidence reasoning

Confidence is 0.77. High source quality: J Neurosci single-unit paper, widely replicated, classic in the vestibular literature. Mapping fidelity is strong for the specific design decision (efference copy not proprioception, motor command not body state). The primary uncertainty is the modality transfer — the claim is about visual/optic flow correction in a gridworld, while this paper is vestibular. The principle has since been demonstrated across sensory modalities, but this specific paper does not provide that cross-modal evidence.
