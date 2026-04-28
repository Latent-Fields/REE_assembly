# Sunstein, "Irreversible and Catastrophic" (Cornell Law Review, 2006) -- relevance to Q-027

## What the paper does

Sunstein's article is the most-cited legal-philosophy treatment of what
"irreversibility" means as a regulatory concept and how to act on it under
uncertainty. He starts by noting that "the idea of irreversibility remains
poorly defined" despite its central role in environmental law, public health,
and risk regulation. He then offers two operational conceptions:

1. **Option value.** A harm is irreversible to the extent that taking the action
   forecloses options that would otherwise have remained available to a future
   decision-maker. The unique badness of an irreversible action is that it
   removes future flexibility. On this reading, the precautionary measure is
   essentially the purchase of an option -- accept a present cost to keep open
   the choice you might have wanted later.

2. **Qualitative distinctiveness.** Some losses are simply not the kind of
   thing that money or substitution can repair: extinctions, deaths, cultural
   destruction. Here irreversibility names a category of harm rather than a
   feature of any particular outcome.

Sunstein then proposes the **Irreversible Harm Precautionary Principle**:
"when a harm is irreversible, and when regulators lack information about its
magnitude and likelihood, they should purchase an option to prevent the harm
at a later date." Crucially, this rule does not require certainty about
irreversibility -- it requires only that the harm fall into one of the two
operational conceptions and that the agent face genuine uncertainty about
magnitude or likelihood. The paper extends this with a Catastrophic Harm
Precautionary Principle for cases where worst-case outcomes are sufficiently
bad that special precautions are warranted regardless of probability.

## Why this matters for Q-027

Q-027 asks whether REE can have a principled definition of irreversible harm
that does not require certainty about irreversibility. Sunstein's paper is a
direct affirmative answer at the form level: yes, you can define a harm-class
without requiring certainty. He gives two recipes for doing it. The
option-value conception suggests REE could compute irreversibility as a
property of foreclosed reachability in the agent's own state-space -- if
taking action $a$ from state $s$ measurably reduces the set of states the
agent can subsequently reach (relative to taking a comparison action), the
foreclosed-reachability term is the irreversibility component of the harm
signal. The qualitatively-distinctive conception suggests REE could carry a
small, axiomatically-grounded set of harm classes (touching INV-026 self
existence and INV-029 love-bearing capacities) that are stamped as
irreversible by category.

Crucially, neither recipe requires certainty. Foreclosed reachability is a
probabilistic forecast. Categorical class-membership is a structural fact
about the harm-signal taxonomy, not about the world.

## Caveats

Sunstein writes about institutional regulators choosing among policies. REE
is a single agent without an institutional context, without a market in
options, and without the legal vocabulary that gives Sunstein's arguments
purchase. The option-value translation depends on REE having a meaningful
internal model of its own future reachability -- a non-trivial assumption in
partial observability. The qualitatively-distinctive translation risks
importing human category distinctions (e.g. "extinction is unique") that REE
has no axiomatic basis to draw.

The paper also flags a concern that applies directly to Q-027: irreversible
harms are sometimes on all sides of a problem. A precautionary rule that
always favours preserving optionality can itself foreclose options. A naive
implementation in REE would risk freezing the agent whenever any plausible
foreclosure was on the table -- which is exactly the failure mode the
philosophical literature on the precautionary principle calls "paralysis".

## Confidence

I am marking this *supports* with confidence 0.48. The relevance to Q-027 is
high, and the paper does answer the form of the question. But the mapping
into REE's own architectural primitives is interpretive work the paper does
not do, so the per-paper confidence should not be inflated. This is
philosophical scaffolding for an open question, not evidence that closes it.
