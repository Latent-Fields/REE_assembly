# Noise-Induced Precursors of State Transitions in the Stochastic Wilson-Cowan Model (Negahbani, 2015)

**Claim tested:** MECH-019 -- Control plane shapes modes of cognition, not discrete choices.
**Direction:** supports | **Confidence:** 0.63

## What the paper did

Negahbani and colleagues took the Wilson-Cowan neural-field equations, added small-amplitude
spatio-temporal white noise, and asked what happens to the *fluctuations* as the system is driven
toward a bifurcation. Using an Ornstein-Uhlenbeck linearisation around the fixed point plus
stochastic simulation, they derived how the correlation and spectral structure of the subthreshold
noise changes on approach: fluctuation variance grows and spectral power focuses toward lower
frequencies, the standard signature of critical slowing down.

They then looked for it in real tissue. In local field potentials recorded from mouse brain slices,
the period preceding a spontaneous seizure-like event showed the predicted spectral focusing toward
lower frequencies and growth in fluctuation variance. Their conclusion is a universality claim:
noise-induced precursors are a generic feature of neural systems approaching a bifurcation, and
carry real value as early warnings of an impending state change.

## Why this bears on MECH-019

MECH-019's CONFIRMING criterion is, at bottom, a claim that a discrete flip is preceded by a
detectable graded signal. That is a good instinct, and this literature is where it has been worked
out properly. But the paper carries a correction that I think matters more than the confirmation.

The precursor is real, and it is graded, and it is detectable -- and it does not live in the mean.
It lives in the second-order statistics: variance growth, lengthening autocorrelation, spectral
power sliding toward low frequencies. Crucially, this holds *even when the transition itself is
sharply discrete*. A system can sit at a fixed point, show no drift whatever in its mean state, and
still be broadcasting -- through the shape of its noise -- that it is approaching a threshold.

Read alongside the Latimer entry in this same pull, that is a constructive answer rather than
another caution. Latimer et al. establish that a graded mean is not evidence of graded dynamics,
because averaging over jittered discrete events manufactures it. Negahbani et al. supply a
precursor observable with the opposite property: variance growth and autocorrelation lengthening
are *not* manufacturable by averaging over jittered step times. Averaging jittered steps inflates
variance uniformly across the window; critical slowing produces a specific, monotone approach
profile as the control parameter nears the boundary, with a matching spectral signature. The two
are distinguishable.

## What follows for the test design

Concretely: as a control-plane channel is swept toward the MECH-259 threshold, the substrate should
be instrumented for tick-to-tick variance in the operating_mode occupancy vector and for the
autocorrelation time of those fluctuations -- both measured per-run, both as functions of the
channel value, both in the window *before* `mode_switch_trigger` fires. If those rise as the
threshold is approached, MECH-019 has a confirming signal that survives the identifiability
objection. If occupancy variance stays flat right up to the flip, that is a much stronger
falsification than a flat mean would be, because it says the system is not near a bifurcation at
all -- it is a comparator reading a threshold.

This costs almost nothing to add. The quantities are already available; the coordinator emits the
soft vector every tick.

## Limitations and confidence

I have scored this lowest in the pull, at 0.63, and the reason is that the transfer is an argument
rather than a measurement. Critical slowing is generic to systems approaching a bifurcation, but
the SalienceCoordinator is a softmax over affinity weights with a hard threshold trigger, not a
continuous dynamical system relaxing around a fixed point. Whether it sits near a bifurcation in
the relevant sense -- and whether it carries enough intrinsic stochasticity to express the
signature at all -- is genuinely unknown, and a deterministic-enough implementation would show no
precursor while being exactly the graded shaper MECH-019 describes. A null result on this
observable would therefore need care before being read as falsification.

The empirical component is also weaker than the theory: pre-seizure LFP in a mouse slice is a
pathological transition, and its relation to a healthy cognitive mode switch is an analogy. The
venue is a specialist mathematical-neuroscience journal rather than a high-visibility empirical one.

So: a prediction worth instrumenting, not a finding worth leaning on. It earns its place in this
pull because it is the only entry that turns the Latimer problem into something actionable rather
than simply warning about it.
