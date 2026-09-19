# The functional role of striatal cholinergic interneurons in reinforcement learning (Kim et al., 2019)

## What this adds that Cragg does not

Cragg's review establishes that the cholinergic pause changes what a dopamine signal becomes at the
level of release. That is necessary for MECH-453 but not sufficient, because MECH-453 is a claim
about a *learning rule*: which selector components get updated, and when. Somebody has to carry the
window across that gap.

Kim and colleagues do it explicitly. They model the relationship between TAN activity and dopamine
variation, and their conclusion is stated in the vocabulary MECH-453 uses: the TAN pause is "likely a
time window to gate phasic dopamine release". They then drop that gating relationship into a
previously published model of reward-based motor adaptation and show that it is what delivers reward
information to the learning process *in a timely manner*. When striatal dopamine is depleted, the
TAN-dopamine interaction degrades and adaptation performance falls.

So the window is not merely present in the biology; in a working learning model it is the thing that
makes credit arrive at the right time. That is the shape `plasticity.striatal_da_ach_windowed_write`
is reaching for, and it connects to MECH-090's commitment-gated-output framing in a way worth naming:
a gate on *when* credit is delivered is the temporal sibling of a gate on *whether* output
propagates.

## The finding that should change how the candidate is written

The model's second result is the one I would not want lost in registration. The pause is not an
independent gate. Dopamine variations *reciprocally modulate pause duration*. The window that gates
dopamine is itself set by dopamine.

MECH-453, and the staged `striatal_da_ach_windowed_write` candidate, both read the window as an
exogenous permission -- something handed down from elsewhere that credit assignment must pass
through. If the biology is a closed loop, then a REE implementation with a fixed-width window is not a
simplification of the mechanism; it is a different mechanism, and the loop's stability is a design
question that nobody in this thread has asked yet. That is worth a sentence in the claim text rather
than a discovery six months after registration.

## What it cannot do

It is a model, and models demonstrate sufficiency. Kim et al. show that a cholinergic time window is
*enough* to produce timely credit delivery. They do not show it is *necessary*: a plain eligibility
trace with the right decay could deliver credit at the right time without any cholinergic gate at all.
MECH-453's phrasing has two halves -- the positive (a window admits updates) and the negative
(dopamine should *not* continuously update every recently-active component). This paper supports the
first and leaves the second untouched.

The task is also wrong in a way that matters. Reward-based motor adaptation is continuous control.
MECH-453's target is discrete selector-component credit under ARC-108 learned gating. The model's
timing constants are fitted to the former and have no principled translation to the latter.

## Confidence

0.66. A well-constructed model in a mid-tier venue, operating at exactly the level MECH-453 needs,
discounted for being simulation rather than measurement, for the task mismatch, and because it speaks
only to the claim's positive half.
