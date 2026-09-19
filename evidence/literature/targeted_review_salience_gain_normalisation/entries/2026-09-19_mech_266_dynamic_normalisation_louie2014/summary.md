# Dynamic divisive normalization predicts time-varying value coding (Louie, LoFaro, Webb & Glimcher, 2014)

## What the paper does

The earlier normalization results are static: they describe the steady-state relationship between an
option's value, its competitors' values, and a firing rate. This paper asks what happens when you
write the same computation as a differential equation. The payoff is that a single dynamic model
reproduces the characteristic phasic-then-sustained shape of cortical decision activity, and makes
three specific predictions -- value coding during the initial transient, value modulation that
varies over time, and a *delayed* onset of contextual information relative to the option's own
value. All three are then found in macaque LIP saccade neurons.

The structural observation that matters most for REE is almost an aside in the abstract: such models
"naturally incorporate a time-weighted average of past activity, implementing an intrinsic
reference-dependence in value coding".

## Why this bears on MECH-266 rather than on the clamp

Every other entry in this review is about how to bound an input. This one is about memory. MECH-266
claims that entering an operating mode should use a different threshold than exiting it -- a Schmitt
trigger on the aggregate salience vector, with the enter/exit gap providing bistability. Whatever
form it takes, hysteresis requires the gate to know where it has recently been. Today's
SalienceCoordinator softmax is stateless per tick in exactly the relevant sense: the logits are
recomputed from current inputs, and `_operating_mode` is stored but does not feed back into the
threshold.

Louie et al. show that a dynamic normalization pool *is* a running reference. If the bounding
operator carries a time constant, then the current response is already measured against recent
activity, and switching acquires resistance near the boundary without anyone writing a second
threshold.

## The uncomfortable implication, stated plainly

That is support for MECH-266's function and an argument against its form. A leaky-averaged
normalization pool with a *single* threshold reproduces hysteretic switching. MECH-266 asserts
something stronger and more specific: that the asymmetry is explicit, per-mode, and implemented as a
second exit-threshold dictionary alongside the existing enter thresholds. Nothing here validates
that. The honest reading is that this paper puts a simpler substrate change on the table -- give the
normalization a time constant -- that would deliver much of MECH-266's intended behaviour without
its asserted mechanism.

This is the same shape of indirection already recorded against Cools 2008 in
`targeted_review_connectome_mech_266`: the literature keeps supplying baseline- and
history-dependent switching while declining to supply the two-threshold structure specifically.
Two independent entries now converge on that gap, which makes it a finding rather than a quibble.

Two further cautions. The model predicts delayed onset of *contextual* information, which in SD-032a
would mean mode affinity computed briefly on stale context after a switch -- a transient no REE
experiment currently instruments. And the fitted dynamics live on a sub-second timescale with no
principled mapping onto REE's tick, so the time constant would arrive as a free parameter in a
coordinator whose occupancy behaviour is already the thing under investigation.

## Confidence

0.68. Good source, and the only entry that reaches MECH-266 at all, but the mapping does real work
and the paper argues against the claim's specific form while supporting its function. I would rather
record that tension than average it away.
