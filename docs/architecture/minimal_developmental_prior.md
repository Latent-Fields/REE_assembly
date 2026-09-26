---
title: "The Minimal Developmental Prior Problem"
parent: "Development & Curriculum"
grandparent: Architecture
nav_order: 18
status: candidate
status_asof: 2026-09-26
status_claim: Q-112
---

# The minimal developmental prior problem

**Source thought:** `docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md`
**Intake:** `evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md`
**Status:** Q-112 and ARC-157 are `candidate`, `substrate_conditional`, v4. MECH-597 is `candidate`, v3,
routing flagged for `/governance`. Registration is not build authorisation.

> How little inherited structure is enough for an organism to become learnable, and how much additional
> general structure makes development reliably tractable without smuggling in solutions to its environment?

## Motivating observation

In the 2026-09-25 babbling probe (`evidence/planning/babbling_e2_action_coverage_probe_20260925.md`), the
coded Phase 0 turned out to be the agent's native policy. On 4/5 seeds that policy was near-monostrategy,
which left E2 no action distinctions to learn and so left E2 rollouts and E3 valuation flat. A structured,
class-balanced source (`StructuredBabbler`, ree-v3 `2ea0e3c`, default-OFF) fixed E2 action
discrimination. A one-off exposure was then overwritten by narrower experience, and a retained minority of
developmental replay preserved it. The downstream flatness had a developmental upstream cause. That cause
is already owned by ARC-074 / MECH-439 / INV-088 / MECH-457 / MECH-588.

## Q-112: the minimal developmental prior set {#q-112}

The question asks which candidates are necessities, which are accelerators, which emerge from others and
which are environment-specific scaffolds. The candidates are:

- a valued, vulnerable self-state (INV-095, SD-012, ARC-138);
- a small general basis for structured endogenous action (INV-073, ARC-074, MECH-461);
- sensitivity to self-action contingency (MECH-277, SD-031);
- persistent but revisable memory (MECH-597).

The answer is found by reduction and ablation, never guessed. Each removal must produce its own predicted
developmental failure. Each restoration must repair development without encoding the environment's
solution. Leg (c) asks whether ablating the developmental implementation of the axioms (A2 / D1) produces
the predicted failure. This is the ablation complement to GOV-INSERT-1's insertion route. Distinct from
Q-108, which is about a minimal working-intelligence event, not a minimal prior set.

## ARC-157: two-axis classification, least environment-specific intervention first {#arc-157}

Every candidate prior is classified on two independent axes:

- candidate-necessary vs developmental accelerator;
- environment-general vs environment-specific.

Enabling architecture (plasticity, memory, time, an action interface, self/world state) is held out as a
class that is not a prior. Rescue interventions are admitted in order of increasing environment-specificity.
A required environment-specific prior is recorded as an ecological finding about that world, not as an
innate requirement. Inherited structure is preferentially procedural (how to discover a world), not
ontological (what the world contains). Worked example: a survival interrupt keyed to self-state
deterioration is general; the same interrupt keyed to a hazard tile is an environment-specific scaffold.
This extends SD-090, which has no generality axis. Natural register host:
`developmental_needs_register.md`.

## MECH-597: retained developmental replay {#mech-597}

Developmental action-consequence knowledge in the E2 world head is not durable under narrower later
on-policy training. Durability requires a retained, overwrite-protected fraction of developmental
experience to keep entering the head's training stream (rehearsal on the world-model plane). This is
distinct from critical-period plasticity reduction on the policy plane (MECH-334). It is asserted for a
frozen read path. The trained-encoder case is open (V3-EXQ-1108, verdict NEITHER). Its opposite-direction
sibling is INV-073: early deficits are permanent, whereas here early gains are fragile.

## Three meanings of "primitive" (vocabulary only)

- innate: MECH-461;
- developmental: ARC-071;
- reopened: ARC-070.
