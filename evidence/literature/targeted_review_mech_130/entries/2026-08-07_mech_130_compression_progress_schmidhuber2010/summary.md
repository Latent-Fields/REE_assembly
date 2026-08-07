# Schmidhuber (2010) — Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010)

**Claim tested:** MECH-130 — curiosity-driven approach must distinguish world-state novelty from agent-policy novelty.
**Direction:** weakens · **Confidence:** 0.55

## Why this entry exists

The other four entries in this directory support MECH-130 in one way or another. This one is here to
attack it, because a literature pull that only collects agreement is not evidence, it is advocacy.
The strongest available objection to MECH-130 is that its central failure mode was solved twenty
years before the claim was written, by machinery that never needs to know whether the unpredictable
thing is an agent.

## What the paper did

This is Schmidhuber's twenty-year retrospective on his programme in artificial curiosity, published
in IEEE Transactions on Autonomous Mental Development. The core is a single move. Do not reward the
agent for surprise; reward it for *compression progress* — for "the active creation or discovery of
novel, surprising patterns allowing for improved prediction or data compression". The intrinsic
reward is the derivative, not the level. An agent should "provoke event sequences exhibiting
previously unknown, but learnable algorithmic regularities", with the paper stressing that this must
be computed under limited computational resources for online prediction and compression. He argues
the same principle underwrites science, art, music and humour.

The consequence that matters here is immediate and was the design goal: a source of surprise that
cannot be compressed yields no reward. Random noise is maximally surprising and maximally
uninteresting, and this formulation gets that right by construction. The noisy TV that captures
Burda et al.'s prediction-error agents is invisible to a compression-progress agent.

## What it means for MECH-130

MECH-130 argues from failure mode 1 — "the novelty signal chronically pulls toward the most dangerous
agent in the environment (highest unpredictability = highest information = strongest approach)" —
to the conclusion that novelty must be typed by *source*: world feature versus agent policy.

Schmidhuber types by *reducibility* instead, and reducibility typing is both older and cheaper. If
the danger is an agent whose opacity is irreducible — the adversary that is simply unmodellable —
then a learning-progress signal already declines to chase it, without ever knowing that the thing in
front of it is an agent. On that reading, a world-versus-agent classifier is redundant machinery for
the failure mode MECH-130 leads with. The inference chain "highest unpredictability = highest
information = strongest approach" holds only for raw-novelty or raw-prediction-error signals. It
does not hold for the whole class of learning-progress signals, and that narrows the set of MECH-111
implementations for which MECH-130 is load-bearing.

That is the objection, and I think it lands against the argument as written.

## Why it does not settle the matter

The rebuttal depends on an unstated assumption: that another agent is like noise. It is not, and the
difference runs in an awkward direction.

A noisy TV is irreducibly random and *stationary*. Its compression progress is zero forever, so the
learning-progress agent correctly ignores it. Another agent's policy is neither. It is partially
learnable, so there is real progress to be had. And it is non-stationary — it changes over time, and
it changes *in response to the observer*. A learning-progress signal facing a target that is
continually learnable and continually moving may find another agent an **enduring** source of
positive progress rather than a decaying one.

If that is right, then this paper does not weaken MECH-130 so much as relocate its failure mode.
Instead of entropy-seeking, the pathology becomes progress-chasing: the agent keeps approaching not
because the other is incomprehensible but because it is *always freshly comprehensible*. That is
arguably harder to gate, not easier, because the signal is now doing exactly what it was designed to
do. This is speculative — nothing in Schmidhuber's paper addresses it, because nothing in his paper
is multiagent — but it is the obvious next question and it is not answered anywhere in the material
found by this pull.

There is also the part of MECH-130 that reducibility typing simply cannot reach. Even granting the
objection in full, learning-progress says nothing about routing agent-novelty through social
modelling before approach is permitted, and nothing about inhibiting approach when harm risk is
high. Those requirements need to know that the target is an agent and that the agent may hurt you.
Reducibility does not carry that information.

## Limitations and caveats

The main one is stated above and I want it recorded plainly: the objection is *mine*, constructed by
applying Schmidhuber's principle to a case he never discusses. He writes about single-agent
creativity. There is no multiagent content, no social content, and no harm-avoidance content in the
paper at all. Anyone re-reading this entry should treat it as "here is the strongest rebuttal
available from the literature", not "Schmidhuber contradicts MECH-130".

The entry is marked `weakens` on that basis — the failure-mode-1 argument does not survive as
written, and MECH-130's write-up should be amended to argue from what reducibility typing cannot do
rather than from entropy-seeking alone. It is not marked `weakens` because the claim is refuted.

## Confidence reasoning

Source quality 0.85 — IEEE TAMD, and this is the canonical statement of the learning-progress
principle. Mapping fidelity 0.50, the lowest in this directory, precisely because the objection is
constructed rather than stated. Transfer risk 0.45, also the highest here: the extension crosses
from irreducible noise to a non-stationary strategic actor, which is exactly where I expect the
argument to break. The aggregate 0.55 reflects a serious objection with an unresolved
counter-objection attached, which is roughly the epistemic state the claim should be governed in.
