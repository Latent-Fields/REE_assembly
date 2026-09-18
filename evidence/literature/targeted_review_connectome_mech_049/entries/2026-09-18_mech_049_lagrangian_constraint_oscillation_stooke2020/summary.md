# Stooke, Achiam & Abbeel (2020) -- what happens when you dissolve a constraint into the gradient

## Why this is the most on-point entry in the directory

MECH-049's distinctive sentence is that temporal compartmentalisation "keeps ethical constraints from being
smoothed into optimisation gradients". Every neuroscience entry in this pull speaks to the *separation* half
of that claim and is silent on the *ethical constraint* half -- rats and macaques do not have harm bounds.
This paper is about a learning agent with an explicit constraint, and the architecture it studies is the
canonical machine-learning instantiation of doing precisely what MECH-049 forbids.

The Lagrangian method takes a hard constraint and converts it into a soft penalty whose weight is itself
learned. The constraint stops being a boundary. It becomes a quantity traded against reward, at an exchange
rate the optimiser adjusts. If MECH-049 is right that this is a bad idea, this is where we should be able to
see it.

## What they found

We can see it. Lagrangian methods, in the authors' words, exhibit oscillations and overshoot which "leads to
constraint-violating behavior during agent training." The diagnosis is mechanistically specific and I find
it the most satisfying part of the paper: the classical multiplier update is *integral control only*. It
accumulates the running constraint violation and responds to the accumulation. Integral control with no
proportional or derivative term produces a characteristic 90-degree phase lag between the controlled
quantity and the control signal -- and that is exactly what they observe between cost and multiplier.

The consequence is an agent that cycles. It runs hot, accumulates violation, the multiplier climbs, it
over-corrects into excessive caution, the multiplier decays, and it runs hot again. The authors report
seeing cost oscillation or overshoot with slow settling in a majority of the Safety Gym environments they
tested. The violations are real behaviour, not bookkeeping.

## What it does for MECH-049, and what it does to it

Two things, pulling in opposite directions. I want to be straight about both, because the second is the
reason this entry is scored `mixed` and not `supports`.

**For.** This is the first genuinely on-point evidence that the failure MECH-049 names occurs in practice, in
a learning system, at scale. Folding a constraint into the objective does not produce a well-behaved agent
that respects a slightly softened boundary. It produces an unstable one that periodically violates the
boundary outright. The neuroscience entries in this directory cannot supply anything like this.

**Against.** The fix is not separation. The authors add proportional and derivative terms to the multiplier
update -- better feedback control -- and the oscillation damps. The constraint stays entirely inside the
optimisation gradient. If constraint-violating oscillation is curable without separating anything, then
temporal compartmentalisation is *not necessary* to keep a constraint satisfied, and MECH-049 cannot be
defended in its strong form.

## The distinction I think the claim should absorb

There is a way through this, and it is worth writing into MECH-049 rather than leaving implicit.

The paper repairs constraint *satisfaction*: with PID control, the boundary ends up mostly respected. It
does not repair, and does not address, constraint *integrity*: whether the constraint remains a boundary at
all, or has become a term with a price. A PID-Lagrangian agent at convergence has an exchange rate between
harm and reward. It is a well-tuned exchange rate, and the agent mostly stays on the right side of it, but
the agent's representation of harm is that of a cost to be traded, and if the reward scale shifted the trade
would shift with it.

MECH-049's defensible form is therefore narrower than it currently reads. Not "separation is how you get a
constraint satisfied" -- feedback control does that. Rather: separation is how a constraint remains a
constraint, rather than becoming a well-priced cost. That is the difference between an agent that does not
harm and an agent that has priced harm correctly, and it is a difference REE explicitly cares about,
since the harm constraint is asserted to be non-optimisable in principle and not merely weighted heavily.

I would flag that as the single most useful thing this pull produced for the claim's wording.

## Limitations

The quantitative reporting is thinner than the rhetorical claim. "A majority of Safety Gym environments" is
asserted without aggregate statistics; Figures 1 and 3 carry the argument visually; the headline metric is a
constructed figure of merit summing non-discounted violations over learning iterates rather than an
interpretable violation rate.

The constraint itself is easy by REE's standards -- scalar, dense, exactly observable, supplied by the
environment. REE's harm bound is evaluative and self-inferred, which is harder, so the transfer flatters the
gradient-based approach.

And the violation documented is transient and occurs during training, with the multiplier eventually pulling
the policy back. MECH-049 worries about permanent absorption at convergence. An oscillating Lagrangian agent
has a tuning problem, not an integrity problem. This paper is direct evidence for the first and only
suggestive about the second, and it should not be cited as if it demonstrated the second.

## Confidence

0.68, direction mixed. Highest mapping fidelity in this directory, because the paper is literally about
folding a safety constraint into an optimisation gradient in a learning agent. Mixed rather than supports
because its own remedy shows that separation is sufficient-but-not-necessary for the outcome it measures.
