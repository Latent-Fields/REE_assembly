# What can I do here? A Theory of Affordances in Reinforcement Learning

Khetarpal, Ahmed, Comanici, Abel & Precup (ICML 2020) start from an observation that is
easy to skip past: reinforcement learning algorithms almost universally assume every action
is available in every state, while people and animals plainly do not think that way. They
build the missing formalism. An *intent* is a map from states to the next-state distribution
an action is supposed to produce, and it is satisfied to degree `epsilon` at state `s` when
the total-variation distance between that intended distribution and the true `P(.|s,a)` is
at most `epsilon`. An *affordance* is then the relation `AF_I`, a subset of `S x A` holding
exactly the state-action pairs where some intent is satisfied to that degree. Two results
follow. Theorem 1 bounds the value loss from planning in the intent-induced MDP rather than
the true one by `2*epsilon*gamma*R_max/(1-gamma)^2`. Theorem 2 covers the case that actually
matters here -- the restricted transition model is *learned* from `n` samples -- and its
estimation term scales as `sqrt((1/2n) log(2|AF_I||Pi_I|/delta))`, so shrinking the model
class to the affordance relation directly shrinks the sample requirement. The demonstrations
are small: gridworlds from 7x7 to 25x25 and a 2D continuous world with walls. Planning got
significantly quicker with an affordance-aware model as the grid grew; in the small-data
regime of 25 to 200 trajectories the minimum planning loss sat at *intermediate* affordance
size `kappa`; and affordance-aware models produced reasonable predictions for
out-of-distribution actions where the baselines did not.

The reason this matters for ARC-002 is not the empirical result but the definition. ARC-002
asserts that E2 is the fast forward predictor *of affordances*, and its own falsifying branch
articulates the worry that E2 might turn out to be a generic world-dynamics predictor that
merely happens to be indexed by action -- with the "of affordances" qualifier doing no work.
That worry presupposes that "forward predictor" and "affordance predictor" are two candidate
descriptions competing for the same slot. Khetarpal et al. show they are not. An affordance
in their sense is *constituted by* the forward model: it is the set of state-action pairs
whose predicted outcome matches an intent within `epsilon`. On that reading E2's two
descriptions sit at different levels, base and readout, and ARC-002's confirming test -- a
readout over predicted world-effect that correlates with ground-truth action viability,
generalising the per-action-class viability index already built for the narrow threat/escape
domain in `ree_core/pfc/e2_escape_affordance_linker.py` -- is the natural way to measure the
relationship rather than an awkward proxy for it.

Theorem 2 supplies something ARC-002 does not currently argue for at all: a reason why the
affordance-structured predictor is the *better engineering choice*, not merely a defensible
description. A model restricted to `AF_I` has a smaller log-cardinality term and so needs
fewer samples to reach the same model error. If that transfers, it says an E2 that carries
viability structure should learn its world model faster than one that does not -- a
prediction ARC-002 could be tested against directly, and a sharper one than the correlational
readout the claim currently proposes.

Two things hold the confidence down. The first is intent-relativity, and it is not a
technicality. The affordance relation exists only once a set of intents is fixed; different
intent sets carve genuinely different relations over identical dynamics. ARC-002 names no
intent set. REE's nearest analogues would be E3's selection objectives or the existing
escape-viability index, but until one is actually fixed, "affordances" in the claim is
under-determined in exactly the way this formalism exposes -- which is a useful finding in
its own right, and arguably the most actionable thing in this pull. The second is scope: the
bounds assume a finite affordance relation whose cardinality enters a logarithm, and E2's
continuous latent readout does not straightforwardly have one. The experiments are tabular
and small-continuous gridworlds, not a learned latent substrate with representations shared
across streams.

Recorded as `supports` at 0.72. The mapping fidelity is high because the paper reproduces
ARC-002's own confirming-test shape from first principles; the discount is for the missing
intent set and for finite-MDP theory reaching toward a continuous learned world model.
