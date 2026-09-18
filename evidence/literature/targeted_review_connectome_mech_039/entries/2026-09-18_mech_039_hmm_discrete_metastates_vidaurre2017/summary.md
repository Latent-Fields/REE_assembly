# Vidaurre, Smith & Woolrich (2017) -- Brain network dynamics are hierarchically organized in time

*PNAS 114(48):12827-12832 -- doi:10.1073/pnas.1705120114 -- PMID 29087305*

## Why this entry is here

Every claim deserves its strongest opponent in the record, and for MECH-039 this is it. The claim's falsifying signature reads: transitions between modes that are "measurably instantaneous/discrete across ALL channels simultaneously (indistinguishable from a one-hot module switch)". Vidaurre et al. fit exactly such a model -- a hidden Markov model with twelve discrete states -- to resting fMRI from 820 Human Connectome Project subjects, and it works very well indeed. This is not a strawman alternative. It is the working model of a large part of the field.

## What the paper found

From temporally concatenated group data, twelve HMM states were inferred, each a distinct pattern of whole-brain activity and functional connectivity recurring across time. Transitions between them are not random: certain states reliably follow others. More strikingly, that sequencing is itself hierarchically organised into "two distinct sets of networks, or metastates, that the brain has a tendency to cycle within" -- one sensorimotor and perceptual, the other associated with higher-order cognition -- with transitions more probable within a metastate than between. The proportion of time a subject spends in each state and metastate is a stable subject-specific measure, is significantly heritable (established using the HCP twin structure), predicts occupancy in held-out sessions, and relates to cognitive traits.

## The two-sidedness, stated plainly

**It supports the clustering half of MECH-039.** The metastate result is a genuine stable-region finding at coarse grain: the state space partitions into two basins the system cycles *within* rather than *between*, which is what "modes are stable regions" predicts. And the heritability result is the part I would weight most -- it says those regions are a real, individually characteristic property of a person's dynamics, not an artifact of fitting twelve states to noise. It is hard to inherit a fitting artifact.

**It weakens the continuity half.** The vehicle that produces all of this is a model in which the system is, at every instant, in exactly one of twelve states. There is no representation of being *between* modes. So the paper cannot adjudicate continuous versus discrete, and its success tells us that the discrete reading survives contact with a very large human dataset.

## The lesson I would actually take from this, which is about instrumentation

A model class that assumes discrete states will report discrete states. That sounds obvious written down, and it is nonetheless the trap MECH-039 is most likely to fall into, because the natural way to instrument modes in REE is the natural way here: fit a state estimator and read off the label. If a REE diagnostic instruments modes with an HMM, or with k-means over channel vectors, or -- most temptingly, since the machinery already exists -- with an argmax over the MECH-046 mode-prior distribution the amygdala analogue emits, then it inherits precisely this blindness. It will return discrete switching regardless of which reading is true, and it will return it *confidently*, because that is what the fit is for.

MECH-039's confirming signature requires evidence of graded, channel-by-channel co-movement: a transition where readiness has moved but precision has not yet. An argmax readout cannot represent that state, so it cannot find that evidence. Any experiment queued against this claim needs an instrument whose output space includes the intermediate, and the verdict should report the channel trajectories, not a decoded mode label. I would treat that as the single most actionable thing in this pull.

## Caveats on the mapping

The states here are patterns of activity and connectivity, not values on named control channels, so the transfer runs through an assumed correspondence between "network state" and "control-plane mode" that this paper does not establish. The paradigm is resting-state only, which means two of REE's three named modes are simply not elicited -- there is no task engagement and certainly no emergency in an HCP resting scan -- so the fact that the robust partition here is *two*-fold along a sensory-versus-abstract axis, rather than three-fold along REE's cut, should be read as a report from a paradigm that could not have found the third, not as a refutation of it. The state count is also a chosen hyperparameter; a different K yields a different inventory, which is reason enough not to read any particular state list as ontology. Finally, the dwell times give some pause: the authors note that around half of metastate visits fall below the duration threshold they use to exclude sleep-wake confounds. Short, frequent visits are hard to square with modes as deep committed regimes, and suggest that whatever these states are, they are not operating at the timescale of REE's commitment-threshold channel.

Confidence 0.65, direction `mixed`. Source quality is the highest in this pull at 0.90 -- PNAS, N=820, out-of-sample occupancy prediction, heritability. Mapping fidelity 0.58, because network-connectivity states are two steps from channel values and the paper's cut of state space does not align with REE's. Transfer risk 0.45, elevated because the paradigm structurally cannot elicit the emergency mode. The aggregate sits well below source quality because for a mixed entry the useful quantity is how far it should move a governance reading in *either* direction, and the indirect mapping limits that in both.
