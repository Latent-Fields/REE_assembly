# Aston-Jones & Cohen 2005 -- LC-NE adaptive gain as the disengage/explore partner

**Claims:** MECH-264, SD-033e (cross-link: plasticity_neuromodulation)
**Direction:** supports (partner-circuit gating, not the value computation)
**Confidence:** 0.6

## What the paper did

Aston-Jones & Cohen's integrative theory recasts the locus coeruleus-norepinephrine (LC-NE) system from a generic "arousal" knob into a specific controller of the exploit/explore trade-off. LC neurons operate in two modes. **Phasic** LC activation -- time-locked to the outcome of task-related decisions -- facilitates the ensuing behaviour and optimises performance on the *current* task (exploitation). When the task's utility wanes, LC shifts to a **tonic** mode associated with *disengagement* from the current task and a search for alternative behaviours (exploration). Critically, ACC and OFC -- which monitor task utility -- are the prefrontal drivers of these LC mode transitions.

## Findings relevant to the claims

The GDL-8 node names the "LC-NE disengage/explore partner" as a co-constitutive piece of the deliberation circuit, with a cross-link to plasticity_neuromodulation. This paper is that partner:

- **MECH-264 (switch-to-alternative).** MECH-264 frames switching as a value-margin threshold: switch when the counterfactual value beats the chosen value. Aston-Jones & Cohen add the orthogonal trigger the value-margin reading omits -- a **disengagement gate**. The tonic-LC mode is what actually licenses *leaving* a low-utility task to explore. An agent can track counterfactual value perfectly and still fail to disengage if nothing shifts it out of exploit-mode; the LC-NE partner is that shifter.
- **SD-033e (engage<->deliberate transition).** SD-033e reserves the transition between external engagement and internally-generated deliberation. The phasic->tonic LC shift is the neuromodulatory expression of exactly that transition, and the ACC/OFC->LC drive maps onto SD-032b (dACC-analog) and SD-033c (value) feeding it -- so the loop closes: value system detects waning utility, drives the gain shift, gain shift licenses disengagement, deliberation explores alternatives.

This is the third strand of the dACC<->FPC loop story: Boorman/Koechlin give the FPC counterfactual maintenance, Kolling/Shenhav give the dACC search-value/control-allocation, and Aston-Jones & Cohen give the neuromodulatory gain that converts "the alternative looks better" into "actually disengage and go."

## Limitations and caveats

The honest mapping is partner-only. LC-NE is a *diffuse neuromodulatory gain system*, not a value-tracking module -- it grounds the disengage/explore *gate*, not MECH-264's counterfactual-value computation. And REE has **no explicit NE-analog substrate**: there is no module today that implements a tonic/phasic gain mode. So this entry is registered as a cross-link to plasticity_neuromodulation and, more importantly, **surfaces a gap** -- REE has no claim governing the explore/exploit gain parameter that decides how readily the agent disengages. That gap is a candidate completion-set claim (see the proposal raised to the user), not something this pull registers. There is also a cost the biology flags: tonic (explore) mode degrades current-task performance, so an NE-analog tuned for easy disengagement trades exploit-stability for explore-readiness.

## Confidence reasoning

Canonical, heavily cited review (source_quality 0.9). Held to 0.6 overall: mapping_fidelity is only 0.5 because it grounds the gating partner and its prefrontal drive (the loop) rather than MECH-264's value computation, and REE lacks an NE-analog host so the link is a cross-reference plus a flagged gap. Transfer risk is moderate (monkey/diffuse-modulator -> an artificial gain parameter). Raises MECH-264's literature confidence modestly; promotes nothing.
