# Scalar reward is not enough (Vamplew et al., 2022)

**Claim tested:** MECH-035 -- VALENCE is vector-valued and ranked without scalar collapse.
**Direction:** supports | **Confidence:** 0.72

## What the paper does

Silver, Singh, Precup and Sutton had argued in "Reward is enough" that maximisation of a single
scalar reward signal is sufficient to account for intelligence, natural and artificial. Vamplew and
twelve co-authors -- effectively the core of the multi-objective reinforcement learning community --
grant the reward-maximisation frame and attack the quiet premise inside it: that the reward being
maximised can be *scalar*. Their case is made by counter-example rather than by proof or
measurement. They walk through classes of problem where a single number cannot carry the structure
the task actually has: objectives that genuinely conflict, constraints that must not be traded away,
situations where the right behaviour depends on which objective is currently binding rather than on
a fixed exchange rate between them. A second, separate argument runs alongside the first: even where
a scalar reward *could* in principle produce competent behaviour, using one to build a general agent
is unsafe, because a scalar makes every dimension of the objective purchasable with enough of
another.

## What it says about MECH-035

This is the nearest thing in the published literature to MECH-035's own thesis, stated by people
with no stake in REE. MECH-035 says VALENCE is a vector of predicted deltas across tagged streams --
HOMEOSTASIS, HARM, TEMPORAL_COHERENCE, SELF_IMPACT error, option volume, inferred other welfare --
and that E3 (ARC-003) ranks candidate trajectories by constraint-first and Pareto or lexicographic
comparison rather than by summing that vector first. Vamplew et al. argue for exactly that shape, and
their alignment argument is the same argument REE makes for non-scalar ethics: harm is the stream
where the exchange rate must not exist.

The honest weight to put on that agreement is smaller than it first looks, and the reason is worth
being explicit about. Their claim is normative and about *specification*: this is how a designer
should write down an agent's objective. MECH-035 is mechanistic and about *behaviour*: REE's observed
rankings are not reproducible by any fixed scalar weighting of the components. Two people can agree
entirely on the first and disagree on the second. A paper arguing that vectors are the right thing to
build cannot tell us whether the thing we built is ranking like a vector.

## Limitations and what could go wrong

Two failure modes matter here, and the second is the one I would bet on.

First, the authors themselves concede the scope: for many tasks a scalar reward is adequate, and
their case rests on the subset where conflicting objectives or hard constraints are live. MECH-035's
own non-degeneracy precondition already anticipates this -- a scenario where only one component
varies cannot distinguish vector ranking from a scalar riding on that one component, and should
self-route `substrate_not_ready` rather than count as a verdict. The paper is a reminder that the
precondition is doing real work and must not be waived for convenience.

Second, and more corrosively: multi-objective RL in practice usually *does* collapse the vector -- it
just collapses it later, via a scalarisation function (weighted sum, Chebyshev norm, a utility over
the vector) applied at decision time. If REE's ranking rule turns out to be of that form, the vector
is preserved in representation and collapsed in use. MECH-035 names this explicitly as the falsifying
outcome: VALENCE "functioning as a de facto scalar reward regardless of its vector representation".
Nothing in this paper protects against it; if anything the paper's own preferred solution family is
where that trap lives.

## Confidence reasoning

Mapping fidelity is the highest in this pull (0.85) because the paper's thesis and the claim's thesis
are near-identical in content. Source quality is capped at 0.75 not by venue -- Autonomous Agents and
Multi-Agent Systems is a strong journal and this is the peer-reviewed version of arXiv:2112.15422 --
but by genre: a response paper's evidence is argument. The aggregate of 0.72 reflects that this entry
can establish MECH-035 as a defended, non-idiosyncratic architectural position, and cannot move the
mechanistic question at all. For that, see the Abel et al. entry in this directory, which supplies the
formal instrument MECH-035's falsifier actually needs.
