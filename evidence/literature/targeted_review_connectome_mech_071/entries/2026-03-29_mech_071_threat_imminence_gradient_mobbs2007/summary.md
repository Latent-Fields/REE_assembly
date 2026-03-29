# When fear is near: threat imminence elicits prefrontal-periaqueductal gray shifts in humans
**Mobbs, Petrovic, Marchant, Hassabis, Weiskopf, Seymour, Dolan & Frith (2007) — Science**
DOI: 10.1126/science.1144298 | PMID: 17717184

## What the paper did

The paper asked a deceptively simple question: does the brain encode a nearby threat differently from a distant one, even when the agent is actively trying to avoid both? Mobbs et al. built an active avoidance paradigm in which volunteers navigated a maze while being pursued by a virtual predator that could catch and inflict mild pain via skin electrodes. Crucially, the predator's distance varied continuously during the task, allowing the authors to map brain activation as a function of threat proximity rather than just comparing "threat present" versus "threat absent." fMRI was recorded throughout.

## Key findings

The central finding is a continuous, proximity-driven shift in neural activity. When the predator was distant, vmPFC was most active -- a region associated with planning, evaluation of contingencies, and controlled defensive strategy. As the predator approached, activity progressively shifted toward the periaqueductal gray (PAG) -- a midbrain structure associated with immediate, largely automatic defensive responses (freezing, flight). This shift was maximal when high pain was anticipated. Subjective dread increased and confidence of escape decreased as the predator closed in. The neural and subjective gradients were aligned and graded, not step-functions. Contact (capture) was the endpoint, but the brain was computing danger long before contact occurred.

The authors interpret this within the predatory imminence continuum framework: pre-encounter (risk is diffuse), post-encounter (threat detected, distal), circa-strike (imminent/contact). Each stage corresponds to distinct defensive behaviors and neural substrates, with higher cortical systems dominant at distance and midbrain systems dominant at proximity.

## REE translation -- link to MECH-071

The second sub-claim of MECH-071 is that E3 learns a graded danger model -- an approach gradient rather than a contact-only binary harm signal. Mobbs et al. are the cleanest neural evidence for why such a gradient should exist and how the brain implements it.

The vmPFC-to-PAG shift as a function of proximity is exactly the biological equivalent of what MECH-071 proposes E3 should learn. In REE's architecture, E3 evaluates trajectories produced by the HippocampalModule against z_harm_s. If E3 has learned a graded approach gradient, trajectories that bring the agent toward harm-associated latent states should generate increasing z_harm_s activity before contact -- not just at contact. The Mobbs result validates this as the right computational target: the brain does not wait for contact to signal danger; it computes an escalating danger gradient as a function of proximity.

This also maps directly to what EXQ-032b PASS confirmed: the energy escalation ladder showed none -- hazard_approach -- contact as three distinguishable stages, with the middle stage being prospective (approach) rather than reactive (contact). Mobbs et al. show the biological circuit for this three-stage structure: vmPFC handles the approach stage, PAG handles the circa-strike stage. REE's z_harm_s would need to encode this same gradient in latent space, driven by E3's learned harm model rather than explicit spatial coordinates.

The threat imminence literature also connects to the valence/arousal dimensions of z_beta. Distant threats are processed in cortical regions associated with controlled cognition; immediate threats in midbrain regions associated with automatic affect. The z_beta axis in REE may need to capture this proximity-dependent shift in processing mode, not just the presence or absence of harm.

## Limitations and caveats

The virtual predator paradigm uses explicit spatial proximity, which makes the gradient legible but also artificial. REE's E3 must learn proximity to harm from latent trajectory features -- there is no explicit spatial coordinate in z_world. Whether the learned latent dynamics produce a graded harm signal is an empirical question that cannot be read off from Mobbs et al. directly.

The vmPFC-to-PAG shift is a circuit-level transition in biological brains. REE does not have distinct vmPFC and PAG modules; the graded gradient would need to emerge from E3's continuous harm-evaluation function over trajectories. Whether this emerges from training alone or requires explicit architectural scaffolding (separate processing modes for distal versus proximal harm) is not answered by this paper.

The paper also does not separate agent-caused versus environment-caused threat -- the predator is unambiguously external. So while it strongly supports the approach-gradient sub-claim of MECH-071, it is less directly informative about the agent/environment calibration asymmetry (the first sub-claim).

## Confidence reasoning

Science 2007, widely cited, foundational to the threat imminence field. The core finding (graded neural encoding of threat proximity during active avoidance) is highly relevant to MECH-071's approach-gradient sub-claim. Confidence 0.77: strong mapping to one sub-claim, weaker mapping to the other, plus the explicit-spatial to learned-latent transfer gap.
