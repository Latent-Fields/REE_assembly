# On the Expressivity of Markov Reward (Abel et al., 2021)

**Claim tested:** MECH-035 -- VALENCE is vector-valued and ranked without scalar collapse.
**Direction:** supports | **Confidence:** 0.74

## What the paper does

Abel and colleagues take the reward hypothesis -- that any goal can be expressed as maximisation of
expected cumulative scalar reward -- and ask what it would take for it to be true. They formalise
"task" three ways: as a set of acceptable behaviours, as a partial ordering over behaviours, and as a
partial ordering over trajectories. For each formalisation they prove that instances exist which *no*
Markov reward function can capture. Then they do the constructive half: for each task type they give
a polynomial-time algorithm that either builds a Markov reward function realising the task or
correctly reports that none exists.

The third formalisation is the one that matters here. A partial ordering over trajectories is, near
enough, what E3 produces when it ranks candidates.

## What it says about MECH-035

MECH-035 states its confirming signature as an existence condition: there are candidate pairs where
no single scalar combination of the VALENCE components -- weighted sum, fixed linear blend --
reproduces the system's ranking, but a dominance or lexicographic rule over the raw vector does. Read
plainly, that is a claim about the expressivity of scalars over a partial order, and Abel et al. are
the paper that makes such a claim decidable.

This changes what MECH-035's first experiment should look like, and I think it is the most useful
thing in this pull. The claim as written invites a fitting exercise: fit the best scalar weighting,
fit the Pareto rule, compare goodness of fit. That design has a soft failure mode -- a scalar that
fits *nearly* as well leaves the verdict to a threshold nobody pre-registered. The Abel construction
replaces the comparison with a question that has a hard answer: run the algorithm on E3's realised
ranking and either it hands back a Markov reward function that reproduces it exactly, or it proves
there is none. Falsification by construction, confirmation by impossibility proof. Whether it is
runnable is a separate question, taken up below.

## Limitations and what could go wrong

Three, and the first is the one that should be stated loudly, because this entry is filed as
supporting a claim whose refutation the same paper makes easier.

The constructive half is a scalar-collapse *detector*. If it returns a reward function for REE's
rankings, MECH-035 is dead on the spot, and dead more decisively than its own stated falsifier
contemplates -- not "a scalar blend fits as well" but "here is the scalar blend, exactly". That the
instrument cuts both ways is a virtue in an experiment and a caution in a literature entry: this paper
is not on the claim's side, it is on the question's side.

The Markov restriction is a real boundary. The impossibility results concern reward as a function of
state, action and next state. An ordering that resists Markov scalarisation may still be expressible
by a scalar with memory. Any REE result built on this must therefore say "not expressible as a
memoryless scalar", not "not scalar" -- and MECH-035 as currently worded asserts the stronger thing.

The formalism assumes a finite, enumerable environment. REE's candidates live in a continuous latent
geometry and are generated on the fly. Some discretisation is needed before the algorithms can run at
all, and the fidelity of that discretisation is untested; a coarse one could manufacture either
verdict.

## Confidence reasoning

Source quality is 0.92 -- NeurIPS oral, formal proofs, an author list spanning DeepMind, Brown and
Princeton, and a result that has become a standard reference in the reward-hypothesis literature.
Mapping fidelity is deliberately held at 0.68: the paper establishes that non-collapsible orderings
exist and supplies a way to test for one, but contributes nothing about whether REE's rankings are of
that kind. Per the skill's calibration guide, mapping fidelity dominates for an architectural claim,
so the aggregate sits at 0.74 rather than near the source-quality figure. The transfer risk of 0.4 is
not the usual animal-to-human worry; it is discrete-to-continuous and Markov-to-history-dependent,
and either gap could void the application outright.
