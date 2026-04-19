# Tambini & Davachi (2019) -- Awake reactivation consolidates memories and biases cognition

## What the paper does

Tambini and Davachi review a decade of human fMRI work on spontaneous awake
reactivation. The central empirical finding the review synthesises is that
during post-encoding rest periods -- times when a subject has recently experienced
something and is now resting without explicit task engagement -- the brain
spontaneously reactivates patterns associated with the recent experience. This
reactivation measurably correlates with two distinct downstream consequences:
stronger subsequent memory for the reactivated content (consolidation), and
biased processing of new information encountered in the minutes that follow
(cognitive bias). The second finding is the more surprising one -- the brain state
carrying the replayed content leaks forward into subsequent encoding, producing
mixed activity patterns that incorporate echoes of the prior experience.

The review also flags that emotional arousal produces a particularly strong
version of this forward-leak effect: arousal from a prior event persists into
subsequent neutral periods and colours how those neutral events are later
recalled.

## Relevance to MECH-261

This is, alongside the Carr/Jadhav/Frank entry, the most directly load-bearing
paper in the pull. MECH-261's architectural claim -- that the mode variable
gates write propagation so that internal_replay content can be read by subsequent
external_task cycles -- depends on there being any biological precedent for this
kind of forward propagation in waking behaviour. Tambini and Davachi provide
that precedent. Awake reactivation during rest propagates forward into subsequent
cognition. The gate that MECH-261 describes is, in effect, the regulator of that
forward leak.

The emotional-arousal finding is particularly relevant to the SD-032 parent
cluster. If awake reactivation of an emotionally arousing event biases subsequent
neutral-event processing, this is a specific instance of cingulate-integration-
substrate output (SD-032c insula, SD-032e pACC autonomic) persisting across mode
transitions. For V3, this predicts that z_harm_a content replayed during
internal_replay should produce detectable bias in the next external_task
trajectory selection -- a testable prediction.

## Caveats and mapping risks

The most important caveat is that the downstream effects documented here are
primarily perceptual and mnemonic -- the bias shows up as differences in how
subsequent stimuli are encoded or remembered, not as differences in action
choices. REE ultimately cares about action selection. The bridge from
"representation of event X is coloured by replay of event Y" to "action choice
given X is biased by replay of Y" is a standard one in cognitive neuroscience
but is not directly validated in the reviewed studies. MECH-261's assumption
that forward propagation reaches action selection is defensible but is one
step more than the literature strictly licences.

A second caveat: the human fMRI signals Tambini and Davachi review are coarser
than the mechanism-level claims MECH-261 makes. The review cannot tell us
whether the forward propagation goes through hippocampus->cortex (as the
Rothschild 2017 entry would predict) or via some other route, and cannot tell
us whether a mode variable is the gatekeeper or whether other mechanisms are
sufficient.

A third caveat worth flagging: the review describes the prior-state persistence
as a continuous blending rather than a discrete mode switch. This nuance should
inform the V3 implementation -- the operating-mode variable may be more faithful
to biology if implemented with soft boundaries rather than hard categorical
switches.

## Confidence reasoning

Source quality is high (Trends in Cognitive Sciences, Davachi lab). Mapping
fidelity is high because the reviewed findings directly test the forward-
propagation claim MECH-261 depends on. Transfer risk is the action-selection
step. Aggregate confidence 0.80.
