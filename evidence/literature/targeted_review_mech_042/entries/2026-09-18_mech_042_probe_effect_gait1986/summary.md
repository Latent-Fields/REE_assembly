# A probe effect in concurrent programs (Gait, 1986)

## What the paper did

Gait ran an experimental study on a sample concurrent program, inserting delays of the kind
instrumentation introduces and measuring how the frequency of observable run-time errors changed.
The result is a conditional, and both branches matter.

If the program has no synchronization errors, there is no probe effect: observation is free.
If synchronization errors are present, the observed error frequency starts high for small delays,
oscillates rapidly as the delay grows, and settles toward zero for large delays. So sufficiently
heavy instrumentation can almost completely *mask* the errors it was introduced to reveal.

The term "probe effect" traces to this paper.

## Why MECH-042 needs it

MECH-042 sub-claim (1) asserts that running with every telemetry channel read each tick, versus
never reading any of them, yields a bit-identical action, commit and weight trajectory at a fixed
seed. The natural temptation is to treat this as obvious -- the channels are getters, they mutate
nothing, therefore they cannot participate -- and to discharge it by code review.

Gait is the reason that temptation should be resisted. The paper's contribution is precisely that
non-interference is a property of the *observed system*, not a property conferred by the
instrument declining to write anything. An observer that mutates nothing can still change what
else happens, in what order, or how much of a shared consumable is used. Whether that matters
depends on whether the system's behaviour is order-dependent, which is a fact about the substrate
and has to be established.

The constructive half of the conditional actually favours REE. A deterministic single-threaded
tick loop at a fixed seed is the order-independent case, and Gait predicts no probe effect there.
That is a real, if modest, prior in favour of sub-claim (1) passing.

## The REE-specific route Gait does not cover, and which I think is the live risk

Gait's perturbation mechanism is timing -- inserted delays in genuinely concurrent code. That is
not REE's situation. The plausible routes by which a REE telemetry read could perturb selection
are different in kind, and one of them is sharp:

`ree_core/predictors/e3_selector.py` has seven `torch.multinomial` call sites in the live
selection path. Any telemetry read that draws from, reseeds, or reorders draws on the same
generator will change the sampled action while mutating no state at all. A read-only code review
cannot see this. Only the hashed-trajectory comparison that sub-claim (1) already specifies can.

The second route the claim already names itself: `agent.py` reads `e3.last_score_diagnostics` into
`_last_control_vector`. If that value reaches selection, the channel is by definition not
telemetry-only, and the claim's safety premise -- no new decision pathway -- fails. A third, less
likely: a lazily-computed telemetry surface forcing evaluation that changes cached state.

## What a pass would and would not license

This is the part I would most want carried into the eventual experiment, and it comes straight out
of Gait's conditional. "No synchronization errors implies no probe effect" means a passing
sub-claim (1) result confirms two things simultaneously -- that the channels are non-participating
*and* that the substrate is order-independent over the probe window -- and cannot separate them.

The consequence is that a pass is not portable. It licenses the read-only premise for the
configuration tested, at the seeds tested, over the window tested. It does not license it for a
future REE that introduces concurrency, asynchronous evaluation, or any shared mutable
scheduling resource. If sub-claim (1) lands as a `ree-v3` contract test -- which the 2026-09-16
disposition on the claim suggests it should -- that test is a regression guard against exactly
this drift, and is worth more than the one-off result.

## Confidence

0.72, direction `mixed`. Source quality 0.65: canonical and durable, but a single-program
experimental study in a practice journal, forty years old, never replicated in the modern sense.
Mapping fidelity 0.75 -- the conditional maps cleanly onto what sub-claim (1) has to show.
Transfer risk 0.4, because the principle transfers and the mechanism does not.

`mixed` rather than `supports` or `weakens` is deliberate. The paper simultaneously tells REE that
its deterministic substrate is the favourable case and that the favourable case is contingent on a
property nobody has yet checked. Both halves are worth having, and neither dominates. The entry
bears on sub-claim (1) only; it supports no inference at all about lead time.
