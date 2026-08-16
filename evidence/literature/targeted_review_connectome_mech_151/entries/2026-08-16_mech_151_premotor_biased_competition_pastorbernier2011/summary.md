# Pastor-Bernier & Cisek 2011 -- biased competition in premotor cortex

## What the paper does

A monkey performed two versions of a delayed centre-out reach. In the one-target version a single
target appeared and its border style signalled how much reward it was worth. In the two-target version
two targets appeared and both values were varied. Single units were recorded in dorsal premotor cortex
across both, so the same neurons could be compared under competition and without it.

The result has two halves, and they pull in different directions for our purposes.

## The half that supports MECH-151

Under competition, PMd neurons carried a strong value signal on their preferred target during the
delay period -- before any movement, before selection. That is a biasing signal written onto
representations of candidate actions while those candidates are still merely candidates. It is the
thing MECH-151 posits.

The timing is also on our side, and I had not expected it to be. Directional tuning appeared first;
relative-value modulation appeared *much later*. Cisek's two-wave account -- specify, then bias -- is
visible directly in the latencies. MECH-151's ordering (E2 produces o_t, then action_bias is added,
then search) is the same ordering. An implementation that folded the bias into E2's own forward pass
would not reproduce this.

## The half that does not

In the one-target task, directionally tuned delay activity showed *no* modulation with value at all.
The bias only exists when there is something to be biased against. And where it does exist, it is
always expressed relative to the other option's value, not as an absolute quantity.

MECH-151 says `o_t_biased = o_t + action_bias`. That is unconditional. It applies whether there is one
viable action-object or twenty, and it does not normalise against the alternatives. The primate
arrangement is competition-conditioned and relative. These are not the same operation, and the paper's
one-target/two-target contrast is precisely the design that separates them.

I think this is the most useful thing in the entry, so let me say what it implies concretely. The
V3-EXQ-640a autopsy found `mean_cue_action_bias_norm` NULL in all six cells under default settings, and
that was read as a dead-gradient defect. This paper offers a second reading worth ruling out first: if
the diagnostic was measuring bias norm in situations where the affordance set was effectively
single-option, then a *correctly functioning* relative-bias mechanism would also read at floor. Floor
bias norm is only evidence of a broken projection if the measurement was taken where competition
actually existed. Any successor driver should record the size of the live affordance set alongside the
bias norm, or the two hypotheses stay entangled.

## Limits

The biasing variable here is reward value. MECH-151's is cue-indexed sensory context -- what is
situationally appropriate, not what is worth most. Those enter at the same architectural point but they
are different quantities, and this paper cannot speak to whether a context projection behaves like a
value projection. And the load-bearing negative result -- no modulation in the one-target task -- is a
null, from one animal. Nulls in single-unit work are the weakest thing in the toolbox. I have kept the
direction at `mixed` rather than `weakens` for that reason: the architecture is supported, the specific
additive form is challenged but not refuted.

## Confidence

0.66. High source quality, a design that speaks directly to the question, docked for the value-versus-
context content mismatch and for resting part of its weight on a null.
