# A Bayesian foundation for individual learning under uncertainty (Mathys et al., 2011)

**Claim under test:** MECH-003 -- *Precision must be tau-scoped with lossy projections.*
**Direction:** supports (with one substantive tension, recorded below)

## What the paper did

Mathys, Daunizeau, Friston and Stephan derive what has since become known as the hierarchical
Gaussian filter. The problem they set themselves is that the two dominant frameworks for modelling
learning each give something up: reinforcement learning is tractable but has no principled account
of uncertainty, while Bayesian models represent uncertainty properly but tend to be agnostic about
individual differences and to require integrals that make online, trial-by-trial learning awkward.
Their solution is a hierarchy in which the state at every level above the first performs a Gaussian
random walk, and -- this is the load-bearing detail -- **the step size of that walk at each level is
determined by the level above it**. Coupling between levels is carried by explicit parameters,
fitted per subject. Using variational Bayes under a mean-field approximation, they obtain analytic
update equations that are cheap enough to run in real time, that read naturally as reinforcement
learning, and whose terms include an explicit precision-weighting of prediction error.

## Why this bears on MECH-003

MECH-003 is, on its face, an architectural prohibition: precision may not be a single global scalar;
it must be stored, updated and applied separately at each temporal depth; and any cross-depth
influence must pass through an explicit projection operator rather than leaking. The interesting
thing about the HGF is that it is not an argument for this position so much as an existence proof of
it. A model built exactly the way MECH-003 demands -- depth-indexed uncertainty, depth-specific
update rates, cross-depth influence confined to named coupling parameters -- turns out to be
analytically tractable, to run online, and to fit human behaviour well enough to have become a
standard instrument.

The correspondence is close to term-by-term. The HGF's per-level state is REE's `z_tau`; its
per-level uncertainty is `pi_tau`; its update rule, in which a prediction error is scaled by a ratio
of precisions, is REE's `Delta z_tau ∝ pi_tau · epsilon_tau`; and its level-specific step sizes are
REE's tau-specific `alpha_tau`. Most consequentially, the HGF's coupling parameters *are* the
projection operator `P` that MECH-003 insists on. In the HGF there is simply no channel by which one
level can influence another except through them. That is the computational content of MECH-003's
rule that no module may "aggregate precisions without a projection operator."

## The tension -- and it is a real one

I want to be direct about this, because it is the most useful thing this pull produced and it would
be easy to bury. MECH-003 says the projection operator is *"Directional (usually short → long tau
only)"*, and gives as its worked example "repeated beta-scale precision → gradual theta-scale
confidence." But the HGF's principal coupling arrow points the other way: it is the *higher* level
that sets the *lower* level's step size, so a slowly-acquired volatility estimate governs how fast a
fast level learns. Both directions are present in the model -- ascending prediction errors do update
the levels above -- but the descending one is the control relationship the architecture is built
around, and it is the one that does the explanatory work.

So the honest reading is: the best-developed formal model of tau-scoped precision supports
MECH-003's *separation* requirement strongly, supports its *explicit-operator* requirement strongly,
and contradicts the unidirectional gloss on its *projection* requirement. I would treat the
directionality clause as the live falsifiable sub-claim in MECH-003 rather than as settled
architecture. It may well be that REE has a reason to want short→long only; if so, that reason
should be stated, because the literature does not supply it.

## Limitations

The HGF's level separation is a stipulation, not a discovery. The paper demonstrates that a model
built this way works; it does not run the comparison that would actually discharge MECH-003's
prohibition -- fitting a well-specified single-global-precision alternative and showing it does
worse. MECH-003's strongest sentence ("There is no global precision scalar in REE") therefore has no
direct comparative support here, only the weaker support of a good model that happens not to use
one. Separately, the coupling parameters are known to trade off against each other during
estimation, so the "slow, many samples required" property of the projection operator is not
independently identified by these fits. And HGF levels are levels of a statistical hierarchy --
outcome, tendency, volatility -- not frequency bands; they acquire distinct effective timescales as
a consequence rather than by definition, so identifying them with gamma/beta/theta/delta remains an
architectural assumption of ours, not a result of theirs.

## Confidence

0.78. High mapping fidelity (0.85) carries this, as the skill directs for architectural claims: the
formal correspondence is unusually tight. It is held back from the 0.8+ band by the fact that this
is a modelling paper without new data, and by the directionality contradiction, which is not a
translation wrinkle but a place where the source and the claim genuinely disagree.
