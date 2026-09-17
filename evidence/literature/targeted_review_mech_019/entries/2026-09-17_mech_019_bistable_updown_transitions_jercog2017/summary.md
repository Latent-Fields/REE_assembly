# UP-DOWN cortical dynamics reflect state transitions in a bistable network (Jercog, 2017)

**Claim tested:** MECH-019 -- Control plane shapes modes of cognition, not discrete choices.
**Direction:** mixed | **Confidence:** 0.70

## What the paper did

Jercog and colleagues asked whether the alternation between UP and DOWN states in spontaneously
active cortex is a rhythm or a bistability. The distinction matters: a rhythm implies an
oscillator with a characteristic period, whereas bistability implies two attractor states and
transitions driven by fluctuations, with no preferred timescale.

The evidence favoured bistability. UP and DOWN durations were highly variable rather than
periodic. Population firing rates in excitatory cells did not decay appreciably across an UP
period, which an adaptation-driven oscillator requires. The model they built -- an
excitatory-inhibitory rate network with adaptation, plus a spiking implementation -- made a
prediction that distinguished it from the alternatives: inhibitory cell rates should decay
markedly within UP periods even though excitatory rates barely do. They went back to the
recordings and found it. DOWN-to-UP transitions, meanwhile, required synchronous high-amplitude
events: the system did not drift across, it was pushed.

## Why this bears on MECH-019, in both directions

This is the entry in this pull that I think is most useful, and it is useful because it dissolves
the dichotomy the claim is built on.

MECH-019 says the control plane shapes rather than chooses. Its FALSIFYING criterion says that if
the mode vector sits flat and then snaps at a hard boundary, the substrate "functionally implements
a discrete chooser regardless of its soft-vector surface representation." Jercog et al. describe a
system that does exactly that -- states are attractors, transitions are noise-triggered jumps,
there is no graded drift of the state variable across the boundary -- and which is *also*
continuously shaped in every sense MECH-019 cares about. Move the control parameter and you do not
move the state; you move the dwell time, the transition rate, the relative depth of the two basins,
and hence the occupancy statistics. The continuous control is entirely real. It simply does not
live in the trajectory of the state variable. It lives in the rate.

Note how precisely this is the substrate's own architecture. The SalienceCoordinator takes
continuous channels (`dacc_pe`, `dacc_foraging`, `dacc_difficulty`, `aic_salience`, `is_offline`),
converts them to affinity weights, softmaxes over four modes, fires `mode_switch_trigger` only when
a salience aggregate crosses the MECH-259 threshold *and* the argmax has changed -- and then
requires the incumbent mode's occupancy to fall below an `exit_threshold` before it can be
displaced. That last piece is hysteresis, and hysteresis is the fingerprint of bistability. The
substrate was built as a hybrid. The claim, as worded, asks the experiment to decide between the
two halves of a hybrid.

## What follows for the test design

Two things, one of which I think is a genuine defect in the pre-registration.

First, if the system is bistable, occupancy is path-dependent. Sweeping a channel upward and
sweeping it downward will trace different occupancy curves, and the width of the gap is a direct
measurement of the hysteresis the `exit_thresholds` impose. A single-direction sweep -- which is
what the criterion as written implies -- cannot distinguish graded shaping from a hysteretic
switch, because both produce a smooth-looking curve in one direction. A bidirectional sweep
distinguishes them cheaply and turns the ambiguity into a measured quantity.

Second, if the gradedness lives in transition rate rather than in trajectory, then the right
dependent variable is not the shape of the operating_mode vector over the ticks before a flip. It
is the hazard function: how transition probability per tick varies with the channel value. That
would confirm continuous shaping even under a strictly discrete switch, which is, I suspect, the
architecture REE actually has and the one MECH-019 actually means.

## Limitations and confidence

The preparation is a real constraint and I do not want to paper over it. These are anaesthetised
rats with no task and no behaviour, and anaesthesia is known to exaggerate cortical bistability
relative to the awake state. Nothing here is evidence that REE's four operating modes are
attractors in this sense, and I have deliberately not claimed that. What transfers is a dynamical
architecture and a worked demonstration that "continuously shaped" and "discretely switching" are
not competitors, together with the two concrete measurement consequences above.

Confidence 0.70, direction mixed. Mixed is the honest label: the paper supports MECH-019's
insistence that continuous control is real and consequential, and simultaneously supplies the
mechanism by which the claim's own falsifier could fire while the claim remains true. An entry
that made this look like clean support would be misrepresenting it.
