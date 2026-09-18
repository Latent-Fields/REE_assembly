# Alshiekh et al. (2018) -- shielding as a reference implementation of MECH-049

## What the paper did

Reinforcement learners maximise reward and offer no safety guarantee, during learning or at execution. The
authors' response is to synthesise a separate reactive system -- a *shield* -- from a temporal-logic
specification of what must never happen, and insert it into the decision loop.

There are two placements. The pre-posed shield sits before the agent and hands it a list of safe actions at
each decision point. The post-posed shield sits after the agent, monitors the action it chose, and corrects
it *only if* that action would violate the specification. They then analyse what a shield must satisfy in
order to preserve the learner's convergence guarantees.

## Why this is the entry MECH-049 should be read against

The post-posed shield is not an analogy for the architecture MECH-049 proposes. It is that architecture.

The agent generates a candidate. A separate module, at a distinct point in the decision cycle, evaluates it
against a constraint. The constraint passes it or blocks it. And -- this is the part that matters most --
the constraint never appears in the reward. It is not weighted, not traded off, not annealed. It is a
boundary, enforced by machinery to which the optimiser has no gradient access at all.

Compare REE's own 2026-02-11 phase-separation thought, which argues that if the harm constraint is
implemented as "reject trajectories exceeding harm bound", then ethical agency becomes a constrained
sampling process rather than scalar reward maximisation, and that this is what keeps constraint as a hard
boundary. Shielding is that proposal, built and analysed, seven years earlier, in a different community.
That convergence is itself worth something: it suggests the claim is tracking a real architectural
attractor rather than a REE-local intuition.

One further alignment worth noting. MECH-049 says explicitly that oscillatory phase-locking is "plausible
but not required", and that discrete event gates would serve. The shield is exactly a discrete event gate.
It delivers the temporal separation the claim wants with no oscillation anywhere, which is direct support
for the claim's implementation-agnostic framing.

## The convergence result, and why it is the evidence

If shielding were only a design proposal it would be an existence claim, not evidence. What makes it
evidence is the analysis of when the shield preserves the learner's convergence guarantees.

MECH-049 implicitly promises something stronger than safety. It promises that separation is *compatible*
with competent optimisation -- that you can hold the constraint outside the gradient without crippling the
agent. That promise is exactly what the convergence analysis discharges, under stated conditions. The
optimiser cannot erode the constraint, and the constraint does not corrupt the optimiser. Independence in
both directions, which is the property the claim names.

Read alongside the Stooke entry in this directory, the pair is informative. Stooke shows what happens when
the constraint is inside the gradient: oscillation and violation. Alshiekh shows what is available when it
is held outside: guarantees, at the cost of needing a specification.

## Where it fails to transfer, and this is serious

The shield's guarantee is inherited entirely from its specification, and that is where REE's situation
diverges sharply.

A temporal-logic formula over a known abstraction is a complete, closed, checkable object. REE's harm
constraint is an open-ended evaluative judgement over consequences the agent must itself predict. There is
no automaton to synthesise. And the failure mode is not graceful: an incomplete harm specification does not
give you a partially-safe shield. It gives you a shield that confidently permits every harm nobody thought
to enumerate, carrying the full rhetorical authority of a formal guarantee. That is arguably worse than no
shield, because it licenses trust.

The second mismatch is subtler and I think more interesting for the claim. Shielding secures the constraint
at the *action interface*. MECH-049 asserts independence *within* the architecture. A learner whose internal
policy has drifted toward harm, and which is being silently corrected at the boundary on every step,
satisfies the shield completely and fails the claim entirely. It is a dangerous agent with a working
seatbelt. If REE wants MECH-049 to mean what it says, the claim needs to distinguish perimeter enforcement
from internal compartmentalisation -- and shielding, as specified here, is the former.

Related: because the shield intervenes only on violation, it supplies no gradient in the safe region. The
learner gets no signal distinguishing barely-safe from robustly-safe behaviour, and will cheerfully converge
to a policy that rides the boundary and depends on the shield permanently rather than internalising the
bound. "Minimal interference" is a virtue for convergence and a vice for internalisation.

## Confidence

0.74, direction supports. The strongest architectural correspondence in this pull -- the post-posed shield
is the propose/veto separation MECH-049 describes, with the constraint held outside the reward as the claim
requires, and the convergence analysis speaks directly to the independence property. Held below 0.8 by the
specification problem, which is not a detail but the thing the whole guarantee rests on, and by the
perimeter-versus-internal distinction that REE should probably write into the claim.
