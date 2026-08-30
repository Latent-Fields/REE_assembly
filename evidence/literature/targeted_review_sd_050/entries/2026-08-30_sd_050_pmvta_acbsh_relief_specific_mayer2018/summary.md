# Mayer et al. 2018 -- a dedicated mesolimbic route for relief

## What the paper did

Sprague Dawley rats in a relief-learning procedure, interrogated with an unusually complete method
stack: anatomical tracing, c-Fos immunohistochemistry, 6-OHDA lesions, chemogenetic (DREADD)
silencing of a specific projection, and local pharmacology. The convergent result is that the
dopaminergic projection from posterior medial VTA to nucleus accumbens shell is activated by
aversive electric stimuli and is *necessary* for relief learning. Lesioning pmVTA blocked relief
learning while sparing fear learning and safety learning. Silencing the pmVTA-to-AcbSh projection
inhibited relief learning. Intra-accumbens raclopride, a D2/3 antagonist, did the same.

## What it settles, and what it complicates

SD-050's `functional_restatement` already leans on Navratilova 2012 for the proposition that pain
relief recruits VTA-DA and NAc-shell dopamine through the same circuitry as appetitive reward. This
paper is the stronger version of that grounding: three independent causal manipulations rather than
a pharmacological block plus conditioned place preference. Taken at the transmitter level it
supports routing relief-completion into MECH-094's VALENCE_LIKING write rather than inventing a
separate valence channel. That is a real strengthening of a load-bearing design decision.

But the specificity is the interesting part, and it complicates the reuse story in the same
direction Yarali and Gerber do. What is necessary here is not "the mesolimbic dopamine system." It
is a narrow anatomical subdivision -- posterior medial VTA to accumbens *shell* -- and the same
manipulations that abolished relief learning left fear learning and safety learning untouched.
Relief has a dedicated route. It is not a generic call into the reward pathway.

## The design constraint this implies

Put the two dissociation results together and a consistent picture emerges: relief shares the
*medium* with reward -- dopamine, accumbens -- while running on its own *channel*. SD-050 currently
implements the first half and not the second. Its comparator writes through the generic MECH-094
path shared with goal-achievement, which means there is no way to ablate relief tagging
independently of goal-achievement tagging, and therefore no way to reproduce in REE the very
dissociation that makes this literature informative.

I want to be careful about how far to push that. REE has no pmVTA/AcbSh distinction to preserve, and
demanding that an artificial architecture recapitulate rodent anatomy is the wrong kind of
biological fidelity -- the brain-like-construction principle is about following the *functional*
organisation where feasible, not the parcellation. The defensible version of the constraint is
weaker and still useful: relief-completion should be separately toggleable and separately
observable from goal-achievement completion, whatever field they both write to. That is cheap to
implement and it is what would make SD-050's falsifier branch (b) actually testable.

## Limitations

This is evidence about the substrate that *carries* a relief signal, not about how the relief event
is *detected*. Nothing here speaks to window length, drop threshold, or descent shape -- SD-050's
real content. The aversive event is once again an experimenter-delivered electric stimulus with a
clean offset, so the range-degeneracy problem that currently makes SD-050 uninterpretable is
untouched. And the force of the finding lies in an anatomical distinction REE does not represent,
which is why transfer risk is scored at 0.48 despite the strength of the causal design.

## Confidence

0.71, filed as `mixed`. Supports the shared-machinery premise with better evidence than the claim
currently cites; qualifies the strong reuse reading by showing the route is dedicated rather than
generic.
