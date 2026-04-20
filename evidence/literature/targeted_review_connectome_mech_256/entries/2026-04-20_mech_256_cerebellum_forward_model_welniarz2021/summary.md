# Welniarz, Worbe, Gallea (2021) -- Cerebellum as Forward Model Substrate

## What the paper does

Welniarz and colleagues attempt to unify two separate literatures under a single computational frame. The first is the classical motor-control account of the cerebellum as a forward model: it predicts the sensory consequences of motor commands so the system can attenuate reafference, correct errors online, and learn from discrepancies. The second is a more recent literature implicating the cerebellum in non-motor cognitive functions, including sense of agency, conditional learning, and reward-based behaviour. Their thesis is that these are not two roles but one: the cerebellum computes forward predictions, and those predictions serve both the motor task of cancelling expected reafference and the cognitive task of recognising an action as one's own.

The review is thematic rather than systematic. It draws on imaging, lesion, electrophysiology, and behavioural studies across two decades and argues that the anatomical position of the cerebellum -- reciprocally connected to motor cortex, parietal cortex, basal ganglia, and spinal cord -- makes it uniquely positioned to host a forward model whose outputs reach any system that needs predictions of sensorimotor consequence.

## What matters for MECH-256

MECH-256 is the REE claim that self-attribution on any reafferent latent stream is implemented by a single-pass forward-model comparator: predicted_z_x = E2_x(z_x_{t-1}, a_actual); residual = z_x_observed - predicted_z_x. The claim is stream-agnostic -- it asserts the computational structure independent of the anatomical substrate.

Welniarz et al. provide the clearest recent statement in the neuroscience literature that this exact structure (forward model plus comparator) is the unifying mechanism behind both motor control and sense of agency. That is, they do not just argue for the forward model as a motor device; they argue that the same computation, read differently, gives rise to the phenomenological experience of agency. This is precisely MECH-256's claim, dressed in neuroscientific rather than computational vocabulary.

The mapping onto REE: ARC-033 (E2_harm_s) and any future stream-specific forward model (E2_self, E2_world) are biologically plausible substrates because the principle -- use a forward model both to predict and to attribute -- is independently motivated by the cerebellar literature. The single-pass residual is computationally sufficient. No counterfactual branch is required for the mechanism to function.

## Caveats and mapping limits

The paper's strength is also its limit. Welniarz et al. argue for one forward-model substrate: the cerebellum. MECH-256 is deliberately substrate-agnostic because REE claims will eventually need per-stream substrates: cerebellum for motor-proprioceptive (z_self), insula/ACC with PAG/RVM for nociceptive (z_harm_s), distributed cortical circuits for z_world. The computational claim transfers cleanly; the anatomical claim does not, at least not without stretching.

A second limit is that the paper does not speak directly to the attenuation magnitude question that motivated this lit pull. V3-EXQ-433a failed C2 because the attenuation ratio for self-caused versus externally-caused harm events came out at 0.95-1.14 when the Shergill 2003 precedent suggests 0.3-0.7 partial attenuation. Welniarz et al. confirm that attenuation happens; they do not quantify how much. For the quantitative constraint one has to read the primary literature (Blakemore 1998, Shergill 2003, Job and Kilteni 2023).

Third, the integration with REE's heartbeat control plane (ARC-023) is entirely absent. The paper treats the forward model as a single component; REE needs to know when the comparator is read for attribution versus when the same substrate is read prospectively for rollout scoring (MECH-257). Welniarz does not address this.

## Confidence reasoning

I set confidence at 0.74. Source quality (0.7) is moderated because the paper is a narrative review, not a primary empirical test or quantitative meta-analysis; the argument is integrative rather than falsificatory. Mapping fidelity (0.8) is high because the 'forward model as unifying mechanism' frame is exactly what MECH-256 asserts -- the paper does not need creative interpretation to support the claim. Transfer risk (0.35) is the main hazard: accepting the paper's single-substrate framing would over-commit MECH-256 to the cerebellum specifically, whereas the REE claim must remain substrate-agnostic until per-stream anatomy is worked out.

The paper supports MECH-256 by establishing the biological plausibility of the computational structure. It does not, on its own, resolve the EXQ-433a C2 failure. That question needs the quantitative attenuation literature.
