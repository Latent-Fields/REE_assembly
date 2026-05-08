---
title: V4 Planning Index
parent: Architecture
nav_order: 100
---

# V4 Planning Index

**Status:** consolidation map
**Created:** 2026-05-08
**Scope:** V4 planning documents, phase boundaries, and documentation gaps

This document is the entry point for V4 planning. It does not replace the
specification documents. Its job is to make the scattered V4 material
navigable and to name the places where consolidation is still needed.

## Canonical anchors

| Role | Document | Use |
|---|---|---|
| V4 substrate anchor | `v4_spec.md` | Canonical list of V4 primitives and V4-bound claim cohorts. |
| Object/entity harness | `v4_developmental_harness_spec.md` | Object permanence, affordance schemas, intervention, and developmental object-learning tests. |
| V3 counterpart | `substrate_roadmap.md` | V3-tractable enrichments that should not be folded into V4 by accident. |
| Sleep/setpoint boundary | `v3_v4_transition_boundary.md` | V3 static setpoints that become V4 dynamic mechanisms; full sleep/offline consolidation scope. |
| Phase/TCL boundary | `v3_v4_phase_substrate_boundary.md` | V4-deferred phase, TCL, ephaptic, and V(t) substrate commitments. |
| Scaling frame | `architecture_scaling_needs.md` | Derived scaling versus deliberate intelligence scaling. |
| Failure-mode atlas | `psychiatric_failure_modes.md` | Architectural psychopathology mappings used as validation targets. |
| Deployment gate | `../governance/deployment_gating.md` | Policy that V3 remains sandbox-only and serious deployment is V4-gated. |

## Current V4 primitive stack

| Primitive | Current anchor | Notes |
|---|---|---|
| V4-0 object/entity permanence | `v4_spec.md`, `v4_developmental_harness_spec.md` | Added as an explicit primitive because object schemas and persistent entity slots are prerequisites for social agents. |
| V4-1 multi-agent ecology | `v4_spec.md` | Requires separate agents with their own harm, drive, commitment, and policy state. |
| V4-2 self-model integration | `v4_spec.md`, `sd_030_e2_self_forward_model.md`, `sd_031_e2_world_forward_model.md` | DR-10..DR-14: z_self scoring, self-domain goals, E2 PE confidence, temporal self-depth, hedonic/proxy dissociation. |
| V4-3 long-horizon dynamics + persistent identity | `v4_spec.md`, `v3_v4_transition_boundary.md` | Lifetime-scale identity, sleep calibration, chronic dynamics, persistent damage and memory state. |
| V4-4 richer action repertoire | `v4_spec.md`, `v4_developmental_harness_spec.md` | Communication, manipulation, withdrawal, carry, push, place, and use actions. |
| V4 phase substrate | `v3_v4_phase_substrate_boundary.md` | Phase/TCL/ephaptic refinement of V3 synaptic stand-ins. |
| V4 clinical/failure-mode validation | `psychiatric_failure_modes.md` | Failure modes should be re-indexed against V4 primitives after V3 closeout. |

## Consolidation decisions

1. `v4_spec.md` is the canonical V4 substrate spec. Other V4 documents should
   reference it, not drift into independent scope definitions.
2. `v4_developmental_harness_spec.md` is the object/entity permanence harness,
   not a side note. It should be treated as V4-0.
3. `substrate_roadmap.md` remains the V3 enrichment boundary. If a feature can
   be tested honestly in V3, it belongs there unless governance explicitly
   authorises V4-only handling.
4. The two boundary documents remain binding: V3/V4 sleep-setpoint transition
   and V3/V4 phase-substrate deferral answer different questions.
5. Psychiatric failure modes should become a validation matrix, not just a
   narrative catalogue: each syndrome-like regime should map to substrate
   perturbation, REE metric signature, behavioural signature, human analogue,
   and falsifier.

## Documentation gaps

| Gap | Proposed landing place | Why it matters |
|---|---|---|
| V3 anatomical/functional concordance map | new V3 closeout doc | Needed before human-brain labels become too loose or inconsistent. |
| V4 object/entity permanence detail | `v4_spec.md` plus harness spec | Other-agent permanence depends on ordinary object permanence. |
| Failure-mode validation matrix | `psychiatric_failure_modes.md` or companion index | Makes psychopathological phenomenology experimentally actionable. |
| V4 experiment epoch contract | V4 runner/governance planning doc | V4 evidence needs a distinct `architecture_epoch` and script template. |
| V4 claim cohort refresh | `claims.yaml` plus planning docs | Current docs name claim cohorts, but claim registry changes need a governed pass. |
| V4 environment/training curriculum | new V4 curriculum doc | Environment expansion should train affective streams deliberately, not just add complexity. |

## Near-term documentation sequence

1. Finish V3 evidence closeout and freeze the final V3 substrate map.
2. Write a V3 brain-mapping/concordance document with evidence grades.
3. Convert the psychiatric failure-mode document into a matrix indexed by
   affected streams and control substrates.
4. Expand the V4 object/entity permanence section into a harness-to-substrate
   migration plan.
5. Draft the V4 environment and learning curriculum: object tasks first,
   affective stream training second, multi-agent ecology third.
6. Only after V3 full completion and governance authorisation, start V4
   substrate implementation.
