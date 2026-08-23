# Memory dimensionality should crystallise, and its target is environment-conditional

Date: 2026-08-23
Source: conversation during `/governance` cycle 2026-08-22 (session `bold-chaum-7e245c`),
arising from GFLAG-0047 (the ContextMemory write-selection DV fork: differentiation
statistic vs relational topology).

## Verbatim thought

> and it would seem to me that there would need to be a period where the dimensionality
> and general bucket overview of the system would have to be possible to be changed with
> this diminishing perhaps to crystialise as the environment that the system finds its in
> more clearly stable? THe general ree system may need vastly different systems in
> diffewrent universes and set ups right?

## What it says, unpacked

Two separable assertions:

1. **Dimensionality as outcome.** The number and granularity of representational buckets
   should not be fixed a priori. There should be a period in which the system can change
   its own bucket structure, and that plasticity should *diminish* -- crystallise -- as the
   environment the agent finds itself in resolves as stable.

2. **Environment-conditional target.** The structure the system crystallises TO is a
   property of the world encountered, not of the architecture. The same REE substrate in
   materially different environments requires materially different resolved structures.

## Why it is not already covered

REE already has the open -> diminish -> crystallise schedule registered, as
INV-074 (plasticity crystallization necessity), MECH-333 (critical period open phase),
MECH-334 (critical period closure / crystallization), plus ARC-076, MECH-335, MECH-484.
**All of that is specified over the SCORING / POLICY plane** -- behavioural diversity vs
winner-take-all capture. None of it is about representational structure or dimensionality.

Note MECH-334, the closure half, currently carries `epistemic_category: substrate_ceiling`
with `ceiling_decision: deferred` -- i.e. REE has a live design for opening the window and a
parked one for closing it.

A registry search for environment-conditional architecture returned one hit, unrelated.

## Substrate state at time of writing

`ree-v3/ree_core/predictors/e1_deep.py:36` --
`ContextMemory.__init__(latent_dim, memory_dim=128, num_slots=16, ...)`. A fixed-size
`nn.Module` buffer. No growth, no allocation policy, no conditioning on anything. The
dimensionality is an a-priori architectural constant, not an outcome. Nobody chose 16 on
evidence.

## Bearing on GFLAG-0047

This sharpens the open fork rather than sitting beside it. If bucket structure is itself
plastic and environment-conditional then "maximal separation" is not merely the wrong
target (MECH-495's objection) -- it stops being well-defined, because separation can always
be increased by adding buckets, so the objective degenerates into "use more slots". And
`sws_slot_diversity` measured over 16 slots presupposes the very structure that should be
the outcome. Relational appropriateness survives variable dimensionality because it is an
agreement measure against ground-truth latent structure and is indifferent to how many
slots achieved the agreement.

It also supplies something MECH-495 lacks: a *when*. A system whose structure is still
plastic reads as poor relational agreement on any static snapshot -- an artifact of timing,
not evidence against the objective.

And it gives MECH-495's 2x2 a second use: the off-diagonal cells detect dimensionality
mis-specification (over-provisioning -> spurious splitting; under-provisioning -> forced
merging), not only objective mis-specification.

## Honest counter-argument

A self-sizing memory is a large V4/V5-shaped build sitting on top of MECH-334, which is
already a deferred ceiling -- so a claim depending on it inherits that park, and REE has a
documented pattern of ceiling claims sitting indefinitely (23 parked at time of writing).
The cheap, non-speculative version is much narrower: treat `num_slots` as a declared
experimental variable rather than a constant and check whether the V3-EXQ-436 lineage
results are stable across it. That is a spike, not an architecture.

## Affected components

E1 (ContextMemory), sleep/consolidation pass (`sws_slot_diversity` is emitted by 29
experiment drivers), the developmental-curriculum / critical-period cluster.

Status: processed
Intake: evidence/planning/thought_intake_2026-08-23_memory-dimensionality-crystallisation.md
Claims registered: MECH-496, INV-101 (plus amendment to MECH-495)
