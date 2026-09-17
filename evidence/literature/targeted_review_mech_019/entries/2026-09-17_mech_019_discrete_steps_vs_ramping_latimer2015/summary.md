# Single-trial spike trains in parietal cortex reveal discrete steps during decision-making (Latimer, 2015)

**Claim tested:** MECH-019 -- Control plane shapes modes of cognition, not discrete choices.
**Direction:** weakens | **Confidence:** 0.72

## What the paper did

Latimer and colleagues took the single most canonical piece of evidence in cognitive
neurophysiology -- the slow ramp of firing in macaque area LIP during a motion-discrimination
decision, read for two decades as the signature of continuous evidence accumulation toward a
bound -- and asked a question that had not properly been asked of it: does the ramp exist on any
individual trial, or only in the average?

They fit two latent dynamical models to the same single-trial spike trains. One was the standard
diffusion-to-bound model, in which a scalar decision variable drifts continuously. The other was
a stepping model, in which the latent variable sits at a baseline and then jumps, once, to one of
two absorbing levels, at a time that varies from trial to trial. Averaging many such jump trials
with jittered onsets produces a smooth ramp. Roughly three-quarters of the choice-selective LIP
neurons they recorded were better described by the stepping model, and the inferred step times
carried more information about the animal's eventual choice than spike counts did.

## Why this bears on MECH-019

MECH-019 says the control plane shapes modes of cognition rather than choosing among them. Its
pre-registered CONFIRMING criterion is specific and, read carelessly, dangerous: probability mass
should visibly migrate across the operating_mode simplex over several ticks *before* the discrete
argmax flip, correlating with the swept channel's continuous value rather than stepping at a
threshold. Its FALSIFYING criterion is the mirror image: flat occupancy, then a snap.

Latimer et al. show that these two are not distinguishable by the observation the claim proposes
to make, if that observation is made on an average. A substrate that flips discretely on every
single run, at a time that jitters with noise or seed, will produce a perfectly smooth,
perfectly monotonic "migration" in the mean -- and it will correlate with the swept channel,
because the channel sets *when* the flip is likely, which is exactly what sets the shape of the
average. The graded aggregate is what a discrete chooser looks like when you stop looking at it
one run at a time.

So the paper's contribution here is not a claim about REE's control plane. It is the removal of
an inference. It says that the evidence MECH-019 has nominated for itself is, in its aggregate
form, evidence for both of the hypotheses it is meant to separate.

## What follows for the test design

The consequence is concrete and, I think, ought to be treated as a precondition rather than a
caveat. The V3-EXQ-846/848-series results the claim cites as adjacent support -- MODEPRIOR
channel authority_mean = 1.0, monotonic occupancy-versus-setting -- are occupancy statistics, and
occupancy statistics are averages. They establish that the channel has authority over where the
system ends up. They do not establish anything about transition shape, which is what MECH-019
specifically claims to extend them to.

A test that could actually separate the two would have to work per-run: fit a stepping model and
a graded model to single-run operating_mode trajectories and compare them, or at minimum check
whether the per-run variance of the transition latency accounts for the whole of the apparent
gradedness in the mean. This is not exotic -- it is the same model comparison Latimer et al. ran,
against a latent that REE can observe directly rather than infer from spikes, which is a large
methodological advantage the substrate has over the monkey. The substrate's own architecture makes
the worry sharper rather than milder: the SalienceCoordinator carries an explicit
`mode_switch_trigger` gated on a MECH-259 threshold, and exit thresholds that impose hysteresis.
Those are discrete-switch machinery sitting underneath the soft vector. Whether the soft surface
representation is doing continuous work, or is a smooth skin over a threshold device, is precisely
the question -- and it is not one an averaged occupancy curve can answer.

## Limitations and confidence

Two things keep me from scoring this higher. The first is that a decision variable is not a mode
vector. LIP's latent is one-dimensional and runs to an absorbing commitment; operating_mode is a
four-component simplex that the agent inhabits continuously and re-enters. There is no guarantee
the stepping/ramping dichotomy carves the same joint in both.

The second is that the finding was contested. Shadlen and colleagues published a Comment, and
Latimer et al. a Response (Science 2016, 351:1406), and the verdict of the model comparison
depends on assumptions about spike-count noise that reasonable people disputed. I have deliberately
not imported the LIP conclusion. What I have imported is the identifiability argument, which no
party to that dispute contests and which does not depend on who was right about LIP: averaging
over jittered discrete events manufactures gradedness. That argument transfers cleanly, and it is
why the direction here is `weakens` -- not because the literature says REE's control plane is a
chooser, but because it removes the evidential route by which the claim currently proposes to
show that it is not.
