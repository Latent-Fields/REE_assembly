# Deployment Gating for V3 and V4

**Status:** governance note
**Date:** 2026-04-17
**Session:** codex-2026-04-17-deployment-gating

This note formalizes an operating constraint already implied by the roadmap, the
language architecture, and the developmental curriculum: **V3 is a sandboxed
scientific substrate, not a serious deployment target.**

This is a governance constraint, not a new claim-registration pass. It does not
change `claims.yaml`.

---

## Policy

- Do not deliberately instantiate a high-intelligence V3.
- Do not connect V3 to open-ended real-world actuation, unconstrained network
  access, or other persistent external consequence channels.
- Treat V3 as sandbox-only: bounded environments, bounded action sets, bounded
  autonomy duration, bounded memory/tools, bounded compute, and bounded sensory
  richness.
- Gate any high-capability or externally connected REE deployment on **V4
  completion**, including multi-agent social coupling, developmental/caregiver
  substrate, and language-mediated repair/coordination inside the live
  architecture.

---

## Why This Follows From The Current Design

- V3 first-paper scope is explicitly the **waking, single-agent substrate**.
  Social coupling, structured communication, multi-agent ethics, and full
  developmental activation are deferred to V4/V5.
- Language is an **emergent coordination layer**, not a value source or direct
  optimiser. It can scaffold repair and planning, but it cannot replace
  embodied harm sensing or ethical cost.
- INV-043 states that architecture alone is insufficient: without
  caregiver-style developmental experience, the same capacity may resolve into
  survival, domination, or indifference rather than ethics.
- That makes the dangerous regime a **capability-scaled V3**: richer sensors,
  larger latent workspace, stronger planning, more compute, longer autonomy,
  and more world access before the social/developmental gates are in place.

---

## Capability Axes That Count As "Scaling V3"

- sensory richness and fidelity
- action availability and actuator reach
- latent-stack breadth/depth and memory/tool access
- background compute, rollout horizon, and autonomy duration
- network access and real-world connectivity

These axes compound. A V3 that is "only" single-agent can still become
dangerous if enough of them are increased at once.

---

## What Mainly Determines How REE Learns

Once the design is settled, the main free variables are relatively few:

- intrinsic drives and how they seed or pull goals
- what writes as pain, harm, or aversive salience
- sensory and action affordances
- available compute and latent-stack depth/breadth
- developmental curriculum and upbringing
- social coupling and language exposure

The key governance point is that **upbringing is not a minor residual
parameter**. In REE it is one of the dominant determinants of which
motivational regime becomes real.

---

## Operational Consequence

- Sandbox V3 is acceptable for scientific validation.
- Real-world-connected REE should be treated as **V4-gated work**, not as a V3
  scale-up.
- The eventual V4 entry gate should be turned into an explicit deployment
  checklist before any serious external deployment work begins.

---

## Source Anchors

- `docs/roadmap.md`
- `docs/architecture/language.md`
- `docs/architecture/developmental_curriculum.md`
- `docs/architecture/v3_v4_transition_boundary.md`
- `README.md`
