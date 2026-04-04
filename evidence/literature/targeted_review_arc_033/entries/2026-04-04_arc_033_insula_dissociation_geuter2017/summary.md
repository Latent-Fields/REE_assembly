# Functional dissociation of stimulus intensity encoding and predictive coding of pain in the insula

**Geuter, Boll, Eippert & Buchel (2017) — eLife — DOI: 10.7554/eLife.24770**

---

## What the study did

Geuter and colleagues used functional MRI in healthy participants while they received calibrated heat stimuli at two intensities, preceded by probabilistic visual cues that manipulated expectations about upcoming pain probability (25%, 50%, or 75%). The design allowed the researchers to cleanly separate brain activations proportional to stimulus intensity from those following predictive coding dynamics (expectation plus prediction error). Skin conductance responses and pupil dilation were collected alongside fMRI as converging physiological measures.

## Key findings

The central result is a double dissociation within the insula. Posterior insula and parietal operculum encoded pain stimulus intensity in a straightforward, forward manner -- activation scaled with actual heat temperature, independent of prior expectation. Anterior insula, by contrast, followed a predictive coding pattern: its response reflected the combination of prior expectations and prediction errors. Crucially, prediction errors contributed approximately twice as strongly as expectations to the anterior insula signal, consistent with the brain placing higher weight on surprising outcomes than anticipated ones. The physiological measures (skin conductance, pupil dilation) tracked the predictive coding pattern, not raw intensity.

## Translation to REE and ARC-033

ARC-033 asserts that SD-003's counterfactual attribution pipeline requires a dedicated harm forward model, E2_harm_s, operating within the sensory-discriminative harm stream (z_harm_s). The core architectural claim depends on z_harm_s being a structured, learnable channel -- specifically, that it encodes graded intensity or proximity information in a way that changes predictably as a function of action (moving toward or away from a hazard).

The Geuter et al. result provides direct biological evidence that the sensory-discriminative pain channel -- the posterior insula -- does exactly this: it encodes intensity in a clean, graded, context-independent way. This is the precondition for a forward model to exist over it. The anterior insula prediction-error signal corresponds to what E3 reads from the harm stream (the evaluative, unexpected-harm signal), while the posterior insula intensity signal corresponds to what E2_harm_s predicts. The fact that these are anatomically and functionally dissociated supports the REE architectural choice to keep them as separate streams (z_harm_s vs z_harm_a, SD-011) and to build the forward model specifically on the intensity-encoding stream.

## Limitations and caveats

The study manipulates expectations through external cues, not through the agent's own action. The specific claim in ARC-033 is that E2_harm_s supports *action-conditional* harm prediction -- predicting how z_harm_s changes when the agent performs action a versus counterfactual action a_cf. Expectancy modulation (knowing pain is coming) is a related but weaker demonstration than motor-conditional prediction. The biological evidence supports the existence and clean separability of the intensity-encoding channel; it does not directly show that this channel supports action-driven forward modeling of the kind required by SD-003. That step remains an inferential extension.

A second caveat is that the study uses thermal nociception in healthy humans -- the most directly relevant modality for REE harm proximity encoding. The transfer risk is therefore low, but the gap between laboratory pain and ecologically embedded harm avoidance (the REE substrate) should be kept in mind.

## Confidence reasoning

Confidence is assigned at 0.78. The source quality is very high (eLife, Buchel lab, multi-measure convergence). The mapping fidelity is good -- this is the right domain, the right stream dissociation, and the right computational structure -- but falls short of the maximal mapping because action-conditionality is not demonstrated. The result supports ARC-033's necessary architectural precondition (a separable intensity channel exists and is learnable) without fully confirming the specific forward model claim. It is the strongest available neuroscientific evidence for this aspect of ARC-033.
