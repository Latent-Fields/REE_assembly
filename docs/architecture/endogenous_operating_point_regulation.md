---
title: "Endogenous Operating-Point Regulation and Regime Coordination"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 24
status: candidate
status_asof: 2026-09-26
status_claim: ARC-155
---

# Endogenous operating-point regulation and regime coordination

**Source thoughts:** `docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md`
(user) and its sibling `docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md` (captured by the
coupled-loop orchestrator).
**Intakes:** `evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md`,
`evidence/planning/thought_intake_2026-09-26_dynamic_control_coordination_hole.md`.
**Status:** all three claims are `candidate`, `substrate_conditional`, registered v3 / v3_v4 with the version
routing flagged for `/governance`. Registration is not build authorisation.

## The observation

REE may possess much of the machinery for several cognitive regimes while lacking endogenous regulation of
**how strongly a signal should count right now**, **when a regime should end**, and **what happens when two
valid controllers want incompatible things**. Today's confirmed autopsies (V3-EXQ-1067, 1090, 1104, 1106,
1107) each show a mechanism that is implemented, causally connected and locally responsive, yet irrelevant
at organism level. The frame is a distributed coordination problem, not a missing executive. No
monolithic controller claim is registered, and Q-041 keeps the supervisor alternative. ARC-131
(installability) is the audit-side framing. The three claims below are its constructive counterparts.

## ARC-155: scale-relative control operating points {#arc-155}

A threshold, cap, saturation constant or cost weight that reads a **learned** quantity must be denominated
on an endogenous estimate of that quantity's own scale, or on a producer whose scale is anchored. It must
not be an absolute raw constant. The denomination must keep the signal's condition-relevant discrimination.
Habituating chronic danger into "baseline" violates the claim. No denomination can restore information the
producer has already lost (GFLAG-0557). Local precedents already in REE: ARC-016, SD-099, MECH-449,
SD-106, MECH-459. Shipped violations: the PAG `theta_freeze` (MECH-279), the CeA gate (MECH-046), the dACC
cap (SD-032a / MECH-266) and the SD-032b effort weight. Competing account: anchor the producer instead
(see `dacc_pe_scale_normalisation.md`, IGW-20260925-219).

## ARC-156: regime-surviving termination evidence {#arc-156}

A strong regime that suppresses interaction or information gathering needs at least one termination input
that keeps changing **during** the regime. A regime whose exit reads only evidence produced by the behaviour
it suppresses is absorbing. This is evidence **starvation**. It is the sibling of MECH-497's evidence
**corruption** (see `persistent_process_termination_taxonomy.md` sec 2b). Measured instances: V3-EXQ-1106
(freeze release path, 0 events while frozen, 3/3 seeds) and the N5 unfreeze-detection probe. Existing
regime-surviving sources it unifies: MECH-280, MECH-482 / MECH-527, MECH-354, MECH-433, SD-036.

## Q-111: controller composition after per-controller correction {#q-111}

Once each controller is individually validated and corrected (ARC-155, ARC-156), do REE's controllers
compose without one removing the action or information substrate another needs? Or does REE need a
**distributed** authority-regulation principle? Motivating cases: V3-EXQ-1090 (the veto fires and is
calibrated, but the executed action is 0 on 3,000/3,000 ticks under freeze) and the mode-switch
one-switch lock. Candidate loci are already registered: ARC-107 / MECH-449, MECH-312a-d / MECH-163,
Q-016, MECH-534 / ARC-145.

## Signal validity (not a claim)

A live signal is not necessarily a valid signal, and scaling cannot repair wrong semantics. This is owned
piecewise by GFLAG-0447, MECH-354, Q-080 and INV-105. A design-review rule is proposed for `/governance`
in the intake (sec 7.2).
