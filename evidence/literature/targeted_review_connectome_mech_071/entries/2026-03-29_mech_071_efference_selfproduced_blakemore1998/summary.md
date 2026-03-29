# Central cancellation of self-produced tickle sensation
**Blakemore, Wolpert & Frith (1998) — Nature Neuroscience**
DOI: 10.1038/2870 | PMID: 10196573

## What the paper did

Blakemore, Wolpert, and Frith used fMRI to compare neural responses when subjects experienced a tactile stimulus that was either self-produced (the subject moved their own hand to create the sensation) or externally produced (an experimenter applied the identical stimulus). The stimulus was a tickle to the palm of the hand. The core manipulation was simple: same sensation, different source. The question was whether the brain encodes these identically, or whether the knowledge that one caused the stimulus makes any difference to somatosensory processing.

## Key findings

It does not encode them identically. When the stimulus was externally produced, somatosensory cortex showed substantially greater activation than when the same stimulus was self-produced. The cerebellum showed the complementary pattern: less activation when a movement generated a tactile consequence than when an identical movement did not. The authors interpret this as the cerebellum generating a forward-model prediction of the sensory consequences of the self-produced movement. That prediction, communicated to somatosensory cortex, cancels or attenuates the incoming sensory signal. External stimuli arrive with no efference copy, no advance prediction, and therefore no attenuation -- so they land with full force on the somatosensory system.

This is the neural mechanism behind the familiar observation that you cannot tickle yourself. The predictability of the stimulus under self-generation is what strips it of its salience.

## REE translation -- link to MECH-071

MECH-071 makes a claim about differential calibration: E2 harm prediction is better calibrated for agent-caused transitions than for environment-caused ones. This paper supplies the neural architecture that would make that asymmetry inevitable. E2 in REE functions as a forward model -- it receives motor commands (via z_self in SD-005 architecture) and predicts the resulting next latent state, including harm consequences. When the agent initiates an action, E2 issues an efference copy equivalent: a prediction of what harm, if any, should follow from that action. When the environment forces a harmful event on the agent without any initiating motor command, no such prediction exists. The environment-caused harm arrives unattenuated -- analogous to the externally-produced tickle producing full somatosensory cortex activation. The asymmetry in calibration that MECH-071 proposes is therefore a direct architectural consequence of the forward-model structure this paper establishes.

The companion claim in MECH-071 -- that E3 learns a graded danger model (approach gradient, not just contact) -- connects more loosely here. The Blakemore paper is about moment-of-contact prediction, not about graded proximity encoding. But the cerebellar forward model is what makes it possible to compute the expected harm at future timepoints given a trajectory, which is the precondition for an approach gradient to be informative at all.

## Limitations and caveats

The domain is benign tactile sensation, not harm evaluation. The extension from "tickle attenuation" to "harm calibration asymmetry" requires that E2/E3 harm evaluation circuits receive analogous efference-copy signals -- plausible but not demonstrated in this paper. The transfer from biological motor systems operating in continuous sensorimotor time to a discrete-step artificial latent architecture also introduces uncertainty: the cerebellar forward model is continuous and operates on millisecond timescales, whereas E2 operates on stepped latent transitions. Whether the prediction-attenuation mechanism survives that translation is an open design question.

## Confidence reasoning

The source is high quality -- Nature Neuroscience 1998, foundational in the sensory attenuation literature, widely replicated. The mapping from forward-model attenuation to MECH-071's agent/environment asymmetry is mechanistically direct at the conceptual level. Confidence is 0.80, reflecting the domain translation gap (benign touch to harm) and the artificial architecture transfer risk.
