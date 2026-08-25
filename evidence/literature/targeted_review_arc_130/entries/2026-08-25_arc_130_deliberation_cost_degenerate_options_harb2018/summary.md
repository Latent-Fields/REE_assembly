# When Waiting is not an Option: Learning Options with a Deliberation Cost (Harb, Bacon, Klissarov & Precup, AAAI 2018)

Where the companion entry in this directory (Bacon, Harb & Precup, 2017) establishes that a
hierarchical RL "option" formally decomposes into independently-learnable existence,
local-operation, and termination components, this paper is the one that actually catches the
gap ARC-130 is worried about in the wild. Trained with the base option-critic objective and
nothing else, options reliably degenerate: either the termination function fires on almost
every step, so the option collapses into a primitive single-step action and never
demonstrates any extended, committed behaviour, or it almost never fires, so one option runs
for an entire episode regardless of the state the agent is actually in, never demonstrating
state-sensitive, competitive selection. Both failures happen with the option's existence,
parameterisation, and local operability fully intact -- nothing is missing at the level of
"does this component exist and run." What's missing is specifically the later-stage property:
does the selection event demonstrably carry through to stable, ecologically meaningful,
temporally-extended commitment. The paper's proposed fix -- an explicit deliberation cost that
prices switching options, making the later-stage property part of the objective rather than
an emergent hope -- is a secondary point for this entry's purposes; what matters for ARC-130
is that the paper had to invent a fix at all, because the default outcome of a
staged-selection architecture is authority without throughput, not the exception.

That is close to a textbook external instance of ARC-130's central claim, stated almost in
the paper's own terms: authority acquired at one internal selection boundary (the option is
chosen and begins executing) does not by itself establish that authority reaches committed,
downstream behaviour. Here the "internal selection boundary" is the option-critic's own
choice to invoke a sub-policy, and the "committed behaviour" that fails to reliably follow is
temporally-extended, state-sensitive option execution. Nothing about this result depends on
REE's specific substrate -- it is a general property of staged-selection architectures that a
selection event is not, on its own, evidence that the selected behaviour persists and
matters, which is exactly the granularity ARC-130 wants REE's own mechanism audits to start
recording rather than collapsing into a single implemented/not-implemented judgment.

The important caveat, stated plainly so it is not silently generalised past what this paper
actually supports: the specific remedy here (a deliberation-cost regularizer) is not being
proposed for REE, and ARC-130's own notes already forbid building new runtime instrumentation
from this intake pass without a separate build decision. This entry's evidentiary weight is in
the documented FAILURE SHAPE -- that authority-without-throughput is a structurally common,
empirically observed default in comparable staged architectures, not a hypothetical REE-only
concern -- not in any specific fix. Confidence is set at 0.65, moderate-high: the failure shape
maps cleanly onto ARC-130's warning, but the underlying mechanism (policy-gradient-trained
termination-function collapse) is RL-specific and has no literal one-to-one REE analogue, so
transfer risk is kept non-trivial.
