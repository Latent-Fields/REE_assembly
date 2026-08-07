# Nguyen, Le, Do, Venkatesh & Tran (2023) — Social Motivation for Modelling Other Agents under Partial Observability in Decentralised Training

**Claim tested:** MECH-130 — curiosity-driven approach must distinguish world-state novelty from agent-policy novelty.
**Direction:** supports · **Confidence:** 0.72

## What the paper did

Most work on agent modelling in multi-agent RL assumes centralised training, where each agent gets
to see everything about the others and about the environment state while learning. Nguyen et al. drop
that assumption. Their agents are myopic even during training: they must build models of each other
from partial observations. The obvious difficulty is that a partially observing agent may simply not
be in a position to observe the others well enough to model them at all.

Their solution is an intrinsic motivation, explicitly modelled on "human social motivation that
entices humans to meet and understand each other, especially when experiencing a utility loss". In
their words, it "encourages agents to stay near each other to obtain better observations and
construct a model of others. They do so when their model of other agents is poor, or the overall
task performance is bad during the learning phase." They report that this simple mechanism improves
modelling of others and significantly improves cooperative task performance.

## What it means for MECH-130

MECH-130's central mechanistic assertion is that an intrinsic signal keyed on how poorly another
agent is understood will produce chronic approach pressure toward that agent, and that this pressure
then competes with harm avoidance on the same entity because nothing in the signal knows about harm.

This paper builds that signal on purpose and reports that it does exactly that. Agents approach and
stay near other agents, and the strength of the pull is monotone in how poorly modelled the other
agent is. That is not an inference from the paper; it is the paper's stated mechanism and its
selling point.

Which means MECH-130's mechanism is not speculative. It is a working, peer-reviewed method that
improves benchmark performance. What MECH-130 contributes is the observation that the same
mechanism, transplanted into an environment containing a harmful or adversarial agent, changes sign.

Two details make the correspondence sharper than I expected going in.

The trigger condition is *model poverty*. Read that against MECH-130's third failure mode — "an
adversarial agent can exploit this by maintaining surface unpredictability to extract continued
approach and cooperation" — and the fit is uncomfortably exact. An adversary that keeps its policy
hard to model holds the trigger permanently on. Nothing in the method decays the pull for an agent
that resists modelling; resisting modelling is precisely what maximises it.

And there is no harm term anywhere in the reward. Approach is gated on epistemic state alone. So
there is no channel through which a high harm estimate could inhibit the approach the signal is
generating — which is the missing piece MECH-130 names, stated from the other side.

## Limitations and caveats

The confirmation is inadvertent, and that matters for how much it licenses. Their tasks are
cooperative. In a cooperative world, approaching the agent you understand least is simply correct,
and the paper's success is evidence that the mechanism works in the regime where it should work. It
is *not* evidence that the mechanism misbehaves adversarially, because that regime is never run.
What transfers is the existence and the behavioural signature of the mechanism, not its danger. The
danger remains MECH-130's own argument, now attached to a concrete instantiation rather than to a
hypothetical.

The trigger is also model *uncertainty* rather than novelty in MECH-111's sense. Close, but not
identical: an agent that is well modelled yet genuinely high-entropy would attract less approach
here than a raw novelty signal would predict. If anything this is the more benign of the two
formulations, so MECH-111's untyped novelty signal should be expected to behave at least as badly,
not better.

Finally, I assessed this from the published abstract and the IJCAI proceedings record rather than a
full-text read, so the exact reward formulation — and whether any implicit proximity or safety
constraint sits in the environment — is unverified. An earlier automated extraction of the PDF
returned a mismatched title and was discarded; the citation details here come from the IJCAI
proceedings page directly.

## Confidence reasoning

Mapping fidelity 0.80 is the strongest component in this directory and drives the aggregate: the
paper's reward *is* the object MECH-130 says needs a gate, so nothing has to be stretched to make
the correspondence work. Source quality 0.78 — IJCAI is a strong venue with an empirical evaluation,
discounted for abstract-level assessment. Transfer risk 0.30, the lowest here, because the construct
is the same construct rather than an analogy. The aggregate is 0.72, held under the mapping-fidelity
figure because what the paper confirms is that the mechanism exists and produces approach, not that
it is hazardous.
