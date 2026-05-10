---
title: Post-Hoc Filter Insufficiency
parent: Architecture
nav_order: 0
---

# Post-Hoc Filter Insufficiency

REE's most compact alignment claim is that safety and ethical content must be
active inside the state that generates candidate futures. It is not enough for a
separate system to inspect a trajectory after it has already been generated.

## The Failure

A post-hoc filter operates after generation. It scores, critiques, suppresses,
or retries candidate outputs that were produced by a generator whose internal
state may not have contained the relevant constraints.

That can improve visible behaviour. It can also improve explanation,
self-critique, and compliance under ordinary conditions. But it leaves a
specific failure mode open: the system can know, say, or score the right thing
while the machinery that generates action remains unconstrained.

REE treats this as an architectural failure, not merely a training failure.

## The Biological Anchor

The vmPFC/OFC lesion literature gives the relevant dissociation. Some patients
retain intelligence, language, declarative memory, and the ability to describe
socially appropriate choices, yet repeatedly make destructive choices in life.
The ethical or social knowledge is stored and declarable. It is not active in
the state from which action is generated.

REE reads this as a direct warning for AI alignment: a correct judge does not
guarantee a constrained generator.

## REE's Alternative

REE internalises the work that is often done after the fact:

- harm modelling must shape trajectory generation, not only score outputs;
- agency attribution must separate self-caused, world-caused, body-caused, and
  other-caused change before responsibility can be assigned;
- goal persistence must keep constructive action live, so harmless quiescence is
  not mistaken for ethical agency;
- commitment must mark the boundary between hypothetical futures and owned
  action;
- residue must alter the future terrain after committed consequences occur.

In short: alignment-relevant content should participate in making futures, not
only in approving or rejecting them.

## Why This Matters

If REE is right, then scaling a capable generator plus a better critic is not
the same thing as building an aligned agent. It may produce better self-report
and better filtering while preserving the failure that matters most: candidate
futures are generated from a state that lacks live access to harm,
responsibility, uncertainty, and care.

The REE test is therefore not "can the system explain why an action is wrong?"
but "was the relevant constraint active before the action became a candidate for
commitment?"

## Where This Lives In The Architecture

The detailed mechanism is developed in [vmPFC](vmPFC.md), especially the
stored-vs-active distinction and the post-hoc filter argument. The corresponding
registered invariant is `INV-038`: post-hoc ethical scoring without active
constraint preparation produces the EVR pattern.

The same framing also motivates the V3 prerequisites for later ethical testing:
agency attribution, motivational persistence, commitment gating, and residue.
V4 multi-agent ethics depends on those prerequisites rather than replacing
them.
