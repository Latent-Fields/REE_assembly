# Frank et al. (2015) -- fMRI and EEG predictors of dynamic decision parameters during human reinforcement learning

**Claim tested:** MECH-065 -- *Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.*
**Direction:** supports (precondition / measurability) | **Confidence:** 0.76

## What the paper did

Frank and colleagues recorded fMRI and EEG *simultaneously* while healthy adults performed a
probabilistic reinforcement-learning task, and fitted a drift-diffusion model in which the trial-wise
neural signals entered as regressors on the model's own parameters. The framing in the paper's opening
is worth keeping: two literatures had been running past each other, one treating reinforcement learning
as dynamic but the choice process as static, the other treating the choice process as dynamic but the
values as static. The study puts both in motion at once.

The finding is that the decision threshold -- the amount of accumulated evidence required before a
choice is emitted -- is *not* fixed across trials. It co-varied with subthalamic nucleus BOLD, and was
further modulated by trial-by-trial decision conflict and by dorsomedial frontal activity (pre-SMA BOLD
and mediofrontal theta in the EEG). The interpretation offered is a pre-SMA-to-STN communication that
raises the threshold when the available choices differ only subtly in reward value, buying time to pick
the statistically better option.

## What this contributes to MECH-065 that Cavanagh (2011) does not

MECH-065 is unusually explicit about what would make a test of it uninformative. Its non-degeneracy
precondition requires that "commitment threshold and DA_A/DA_M lock-in pressure are themselves
separately measurable at the pre-commit stage, so a shift in them can be attributed to RC_conflict
specifically rather than read off final behavioural outcome." That is a methodological demand, and this
paper is the cleanest existing demonstration that such a demand can actually be met: the threshold is
recovered per trial, and its variation is attributed to a specific, independently-recorded upstream
source.

So I would read this entry as evidence for the *feasibility of the experiment*, more than for the
mechanism. It gives REE a measurement template. Log the commitment threshold per decision. Regress it
trial-by-trial against the RC_conflict channel. Report the drift-rate estimate alongside it, because
the two parameters are only jointly identified and a genuine drift effect will otherwise masquerade as
a threshold effect and spuriously satisfy MECH-065's confirming signature.

There is also a practical warning embedded in the result. Threshold modulation appeared specifically
when the options differed *subtly* in value. If REE sets its authority/provenance mismatch manipulation
too coarsely -- a blatantly spoofed source against an obviously verified one -- it may find no threshold
change, and that null would be about manipulation strength rather than about the mechanism. Graded
mismatch, not binary, is the design implication.

## Limitations

This is correlational work. There is no lesion, no stimulation, no pharmacological manipulation; the
pre-SMA-to-STN-to-threshold direction is inferred from the model and from prior anatomy rather than
demonstrated here. The companion Cavanagh et al. (2011) entry carries the causal weight, and the two
should be read together -- Cavanagh for the causal pathway in a clinical DBS population, Frank for the
trial-resolved measurability in healthy subjects.

And, as with Cavanagh, the conflict is subtle-value conflict in a reward task. Nothing in this
experiment involves provenance, authority, or reality-coherence mismatch. The mapping to MECH-065's
specific *lane* is by analogy to control shape only. Whether reality-coherence conflict is separable
from value conflict -- which is the genuinely novel and still-unevidenced part of MECH-065 -- is
untouched by either paper.

## Confidence reasoning

Source quality 0.84 -- J Neurosci, simultaneous multimodal imaging in healthy subjects, careful
model-based analysis. Mapping fidelity 0.68 -- lower than Cavanagh because this is correlational, and
equally exposed on conflict-content grounds. Transfer risk 0.32 -- healthy population helps, but the
threshold is still a fitted latent rather than a read channel. Aggregate 0.76, with the weight placed
on the methodological contribution: this paper tells REE how to build an informative MECH-065
experiment, which is more immediately useful than one more correlational theta finding would be.
