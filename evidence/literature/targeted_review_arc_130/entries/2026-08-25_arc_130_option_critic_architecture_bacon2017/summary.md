# The Option-Critic Architecture (Bacon, Harb & Precup, AAAI 2017)

This is the foundational paper for the "options" framework in hierarchical reinforcement
learning, and it is included here not because it tests ARC-130 directly -- it predates and
has no knowledge of REE -- but because it is the cleanest external precedent for the
*structural move* ARC-130 is making. The paper's core contribution is to decompose a
temporally-extended behavioural unit (an "option") into three independently-parameterised,
independently-learnable pieces: an intra-option policy (what the option does once running),
an initiation set (where it may begin), and a termination function (when it stops), all
trained jointly by a derived policy-gradient theorem with no hand-specified subgoal or extra
reward. Before this paper, temporal abstraction in RL was either hand-designed or treated as
a monolithic "does this sub-policy work" object; after it, the field routinely asks about
each of these sub-components separately, because they can and do succeed or fail
independently of one another.

That is exactly the epistemic move ARC-130 asks REE governance to make about its own
mechanisms: instead of a flat implemented/not-implemented verdict, record the furthest stage
actually demonstrated along an ordered ladder, because a mechanism can plainly exist and be
represented in the network's parameters (the option exists), be locally invocable (the
intra-option policy runs), and still fail to reach committed, ecologically consequential
behaviour -- a distinction that is meaningless if "the mechanism" is treated as one opaque
unit. The option-critic decomposition is a load-bearing example, from a mature and
extensively cited literature, that this kind of staged accounting is not an REE-specific
formalism invented to rationalise ambiguous internal results -- it is how a neighbouring
field found it necessary to describe temporally-extended behaviour once naive end-to-end
training stopped being sufficient to reason about it.

The honest limits of the mapping: this paper is a single-agent RL result on gridworld and
Atari benchmarks, not a finding about a distributed, multi-rate, recurrent architecture like
REE, and it does not itself document a case where the early stages succeed while a later
stage fails -- for that, see the companion entry in this same directory (Harb, Bacon,
Klissarov & Precup, 2018), which documents exactly the degenerate-without-regularization
failure mode: options that exist and are locally operable but collapse to either
single-step or whole-episode termination absent an explicit cost that makes "the option
should have committed structure" part of the objective. Read together, the two papers give
an external, non-REE instance of ARC-130's central warning: that a stage being *possible*
does not make it *achieved*, and that the gap between them is worth measuring rather than
assuming away.

Confidence is held at a moderate 0.55 rather than higher specifically because this entry on
its own only establishes that the ladder's early stages are formally separable and
jointly-learnable in an external domain -- it is evidence for the *methodology* of staged
accounting, not evidence about REE's own specific ladder stages (competitive authority
against a dominant arbitration term, ecological consequence, retention), none of which have
a direct construct in the options literature.
