# Summary: Yu & Dayan (2005) — Unexpected Uncertainty, NE, and Attentional Reorienting

**Entry:** 2026-03-29_mech_104_unexpected_uncertainty_ne_yudayan2005
**Claim tested:** MECH-104 (unexpected harm events spike commitment uncertainty via LC-NE volatility interrupt, enabling de-commitment)

---

## What the paper did

Yu and Dayan published a computational modelling paper in *Neuron* proposing a double-dissociation between the neuromodulatory roles of acetylcholine (ACh) and norepinephrine (NE) in attentional control. The framework is Bayesian: the brain continuously maintains a generative model of the world and must allocate processing resources depending on how much the world is deviating from expectation. Their key move is to distinguish two qualitatively different kinds of uncertainty. Expected uncertainty is the irreducible stochasticity of an otherwise stable environment -- the noise that comes with knowing you are in a world that sometimes surprises you even when your model is correct. Unexpected uncertainty is something else: it arises when the generative model itself appears to be violated, when the world seems to have changed structurally rather than just producing the anticipated noise. Their proposal is that these two kinds of uncertainty are neurochemically segregated: ACh tracks expected uncertainty and modulates the influence of top-down priors, while NE signals unexpected uncertainty and drives a more global reset of the inference process.

## Key findings

The core computational argument is elegant. In a cued-attention task (Posner paradigm), they show that appropriate allocation of attention across valid and invalid cues requires the brain to track both sources of uncertainty simultaneously. Their model, when fit to human behavioral data with NE-lesion (clonidine-treated) and ACh-lesion (scopolamine-treated) conditions, correctly predicts the differential effects: NE disruption selectively impairs the ability to reorient from invalid cues (unexpected uncertainty is not properly signalled), while ACh disruption impairs the weighting of prior expectations. The NE signal in their formalism is essentially a signal that says: "the model generating this world may have changed -- increase your learning rate and reduce your commitment to the current prior." This is the key finding for MECH-104: NE is explicitly proposed as the signal for model-change detection, and its downstream effect is attentional reorienting -- disengagement from the current expectation set.

## REE translation

The translation to MECH-104 is the most direct of the four entries. When unexpected harm occurs in the REE framework, the agent's forward model has failed: the planned action sequence led to harm that was not predicted. This is precisely the trigger for Yu and Dayan's unexpected uncertainty signal. The NE released in response propagates a model-violation message to prefrontal cortex and other commitment-gating regions. In REE terms, this raises commitment uncertainty -- the agent should not continue executing the current plan as though the model is valid. The de-commitment mechanism in MECH-104 (the volatility interrupt) is the architectural instantiation of what Yu and Dayan propose as the normative response to unexpected uncertainty: reset the inference process, reduce reliance on the current prior (current plan), and reorient.

This framing also provides a principled answer to why de-commitment should be conditional on harm-surprise rather than any prediction error: harm events signal not just that a specific prediction was wrong (a point prediction error, which dopamine would handle) but that the safety model of the current plan may be structurally incorrect. That is precisely unexpected uncertainty in Yu and Dayan's taxonomy.

## Limitations and caveats

Several cautions are warranted. Yu and Dayan's model is normative and inferred from behavioral pharmacology -- there is no direct LC unit recording, no optogenetic manipulation of LC, and no real-time measurement of NE release in the sites that would gate REE-style commitment. The ACh/NE double dissociation is theoretically clean but empirically supported mainly by blunt pharmacological tools (systemic clonidine, systemic scopolamine) that are far from selective. The identity of the brain region implementing the unexpected uncertainty detector is left open -- the model does not specify whether this is LC itself, or whether it could be another NE source or even a non-noradrenergic system that happens to correlate. Finally, the reorienting described in the paper is attentional (stimulus selection), not motoric de-commitment in the action-planning sense that REE requires; the step from attentional reorienting to plan de-commitment requires additional architectural grounding.

## Confidence reasoning

Despite these caveats, this paper provides the strongest formal theoretical grounding for MECH-104 in the literature. The correspondence between "unexpected uncertainty triggering NE-mediated reorienting" and "unexpected harm triggering LC-NE volatility interrupt enabling de-commitment" is conceptually precise. The gap between attentional reorienting and action de-commitment is a genuine limitation but is bridgeable given what is known about LC projections to ACC and prefrontal action-selection circuitry. Confidence: 0.79.
