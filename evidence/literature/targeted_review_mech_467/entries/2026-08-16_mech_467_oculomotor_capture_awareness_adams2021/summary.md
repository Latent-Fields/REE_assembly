# Adams & Gaspelin 2021 -- introspective awareness of oculomotor attentional capture

## What the paper does

Participants search a display for a target shape while a salient colour singleton sits somewhere else in
it. Eye position is tracked, and the measure of interest is where the *first* saccade goes. On half the
trials, participants are then asked to say whether that first eye movement went to the distractor.

Two results. Participants have real, if partial, introspective access -- capture rates were much higher on
trials they reported as captures than on trials they reported as clean. And awareness did not help: knowing
you were just captured did not reduce capture on the trials that followed.

## Why this is the closest thing to a direct leg-3 measurement

MECH-467's leg 3 is behavioural capture: the rule survives intact, and the distractor still controls action
selection. What is needed to demonstrate it is a situation where the goal is unambiguously held and overt
selection nonetheless goes to the distractor.

That is this paradigm. The search template is instructed, simple, stable across the block, and demonstrably
in force (overall performance is good). The first saccade is an overt act of selection. On a substantial
fraction of trials that act lands on the thing the participant is trying to ignore. The dependent measure
here *is* a wrong-target selection rate, which is why I rate its mapping fidelity above the other two
MECH-467 entries.

The awareness result adds something MECH-467 does not currently consider, and it is worth stating as a
prediction rather than leaving implicit. If someone proposes to close leg 3 in REE by *detecting*
wrong-target selection and feeding that back into rule maintenance -- a monitoring loop -- this result says
that will not be enough. Humans have the monitoring signal. It does not fix the behaviour. Leg 3 is not a
detection problem, and a REE design that treats it as one is predicted to fail.

## The confound I cannot rule out

Task-set integrity is inferred, not measured per trial. Nobody probes the search template on the trial
where capture happened. So the leg-2 reading survives: perhaps captured trials are exactly the trials where
the template had momentarily slipped. This is the same confound Duncan's goal-neglect mechanism raises from
the other direction, and it is the reason both of those entries end up pointing at the same design
requirement -- REE has to measure rule state *on the captured trial, in the selection path*, or legs 2 and
3 stay entangled no matter how the battery is arranged. Unlike the human experimenter, REE actually can do
this; the rule representation is available for inspection. That is a genuine advantage and the successor
battery should spend it.

A second boundary worth naming: oculomotor capture is a sub-200ms reflexive selection in a static display.
MECH-467's leg 3 concerns action selection across an extended sequential task with commitment dynamics.
Whether the dissociation survives at that timescale is not established here, and the claim's own sequencing
caution -- exclude the during-commitment arm until commitment behaviour is stable -- is a version of the
same worry.

## Confidence

0.66. Good source quality, the best mapping fidelity available for leg 3, discounted for the unmeasured
task-set confound and for a timescale gap the claim itself already flags.
