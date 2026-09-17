# Cortical Membrane Potential Signature of Optimal States for Sensory Signal Detection (McGinley, 2015)

**Claim tested:** MECH-019 -- Control plane shapes modes of cognition, not discrete choices.
**Direction:** supports | **Confidence:** 0.74

## What the paper did

McGinley, David and McCormick recorded membrane potential intracellularly in the auditory cortex
of mice performing a hard tone-in-noise detection task, while simultaneously tracking pupil
diameter as a continuous index of arousal, along with hippocampal activity and locomotion.

The finding is an inverted-U. Detection performance and sound-evoked cortical responses were both
best at *intermediate* arousal, not at high arousal. At that optimum the pre-decision membrane
potential was stably hyperpolarised and background synaptic noise was low -- a quiet, responsive
regime. At low arousal the membrane potential drifted into slow rhythmic fluctuation; at high
arousal (reliably accompanied by walking) it depolarised and became noisy. Arousal did not pick
a behaviour. It set the regime in which sensory evidence was processed.

## Why this bears on MECH-019

MECH-019 asserts that the control plane modulates modes of cognition by tuning gain, horizon,
learning eligibility and constraint enforcement -- that from outside this looks like choice, and
from inside it is the continuous shaping of a landscape. I find it hard to name a cleaner
biological instance of that sentence than this paper. A single scalar variable, varying
continuously and not under task control, changes what the cortex *is* for the purposes of the
next stimulus: how much gain the evoked response gets, how much noise sits in the background, how
stable the operating point is. Nothing in the pathway is choosing. The landscape tilts and the
behaviour follows.

Mapped onto the substrate, the arousal axis is a stand-in for the SalienceCoordinator's continuous
inputs -- `aic_salience`, `dacc_pe`, `dacc_foraging`. Those channels feed affinity weights into a
softmax over {external_task, internal_planning, internal_replay, offline_consolidation}, and the
architectural claim is that the soft vector is doing real work rather than decorating a threshold.
McGinley et al. support the premise that a continuous control variable has graded rather than
step-like consequences downstream.

## The inverted-U is a problem for the criterion, and worth stating plainly

There is a finding here that cuts against MECH-019 as currently written, and it would be
dishonest to file this entry as clean support without flagging it.

The claim's CONFIRMING criterion requires a **monotonic** graded redistribution of the
operating_mode vector as a channel is swept. McGinley et al. report a relationship that is smooth
and graded but emphatically *not* monotonic: performance and evoked gain rise, peak at
intermediate arousal, and fall again. If REE's control plane is biologically faithful in this
respect -- and the Yerkes-Dodson shape is one of the more robust things in the arousal literature
-- then a continuous sweep of a control-plane channel could produce exactly the non-monotonic
occupancy curve that MECH-019's own criterion would score as a failure to confirm, while the
underlying architecture is doing precisely what the claim says it does.

Monotonicity is being used here as a proxy for gradedness, and the two come apart. The property
the claim actually cares about is *continuity* -- that occupancy is a smooth function of the
channel with no flat-then-snap structure. A criterion written on smoothness (say, bounded
discrete derivative of occupancy with respect to the channel, plus a test against a step-function
fit) would capture the intended content and survive an inverted-U. I would treat this as a
falsifier-wording defect rather than a defect in the claim, and it is cheap to fix before the
experiment is queued rather than after it returns an uninterpretable UNDETERMINED.

## Limitations and confidence

The obvious distance is species and scale: mouse auditory cortex during tone detection is a long
way from a four-mode coordinator arbitrating between task engagement, planning, replay and
offline consolidation. The graded quantity here is detection performance along an arousal axis,
not occupancy of named modes, and the paper says nothing at all about transition *shape*, which
is MECH-019's actual contested prediction.

I have set confidence at 0.74 rather than higher for that reason: this is strong evidence for the
claim's premise and no evidence for its contested part. What keeps it from falling further is that
arousal-as-continuous-gain is one of the better-replicated findings in systems neuroscience, and
that the preparation here is unusually direct -- intracellular recording with a simultaneous
psychophysical readout, rather than an inference from spikes or BOLD. The inverted-U observation
is, I suspect, the most useful thing in this entry, and it points at the test design rather than
at the claim.
