---
title: Architecture Scaling Needs
parent: Architecture
nav_order: 99
---

# REE Architecture Scaling Needs

**Status:** planning hypothesis  
**Created:** 2026-05-04  
**Scope:** current REE architecture; likely scaling needs for later substrate generations  
**Grounding pass:** claims registry review across 579 registered claims in `docs/claims/claims.yaml`

This document separates two different meanings of "scale REE":

1. **Derived scaling:** a part gets larger because another part made it necessary. Example:
   adding more sensory modalities forces wider modality encoders and typed stream routing.
2. **Deliberate intelligence scaling:** a part is scaled because doing so should increase
   competence, abstraction, reflection, planning quality, or robustness even when the input
   surface is unchanged.

The distinction matters because larger latents are not automatically more intelligent. REE's
claim registry repeatedly points to typed separation, gated access, replay diversity, and
multi-timescale credit assignment as the load-bearing structure. Scaling should preserve that
structure rather than collapse it into a single bigger model.

---

## Current claim-level picture

The claims registry is dominated by mechanism hypotheses and design decisions around:

- E1/E2/E3 separation: `ARC-001`, `ARC-002`, `ARC-003`
- L-space and precision routing: `ARC-004`, `ARC-005`, `INV-008`, `INV-013`
- hippocampal path memory, rollout, replay, and viability mapping: `ARC-007`, `ARC-018`,
  `MECH-022`, `MECH-033`, `MECH-092`, `MECH-165`
- commitment and basal-ganglia-like tri-loop control: `ARC-021`, `ARC-023`,
  `MECH-060`, `MECH-061`, `MECH-062`
- harm, self-attribution, and reafference comparator streams: `ARC-027`, `ARC-033`,
  `ARC-058`, `ARC-061`, `MECH-095`, `SD-010`, `SD-011`, `SD-047`, `SD-048`
- goal and resource vocabulary: `ARC-030`, `ARC-032`, `ARC-036`, `MECH-112`,
  `MECH-116`, `MECH-117`, `SD-012`, `SD-015`, `SD-049`
- frontal/cingulate/control substrates: `ARC-041`, `SD-032`, `SD-033`, `SD-033a`,
  `MECH-150`, `MECH-151`, `MECH-152`, `MECH-153`
- offline consolidation and sleep phases: `INV-010`, `SD-017`, `MECH-120`,
  `MECH-121`, `MECH-122`, `MECH-123`, `MECH-124`, `MECH-166`
- later abstraction and V4/V5 work: `SD-040`, `SD-042`, `SD-045`, `SD-046`,
  `MECH-298`, `MECH-299`, `MECH-300`, `MECH-301`

That distribution suggests that REE intelligence should scale most through **structured
capacity allocation**: more and better indexed memories, richer action-object vocabulary,
more controlled hypothesis generation, deeper offline consolidation, and broader goal/social
state handling. Raw sensory and latent dimensionality are necessary substrates, but they are
not the primary intelligence lever by themselves.

---

## Derived scaling

These are parts that should usually scale because another surface expanded.

| Driver | Derived scaling pressure | Notes |
|---|---|---|
| More sensory modalities | modality encoders, `ARC-017` stream tags, `MECH-103` multimodal fusion, attention/precision routes | Do not put raw modality bandwidth directly into shared `z_world`; bind object-level structure first. |
| Higher information per sense | per-modality compression, sensory precision lanes, event detectors | This may increase `z_self`, `z_world`, or stream-specific dims only after compression fails. |
| Larger action repertoire | E2 action inputs, `SD-004` action-object vocabulary, richer action decoders, reafference comparators | Action-object compression should grow more slowly than raw action/effect space. |
| More resource/goal types | `SD-049` resource identities, per-axis drives, `SD-015` z_resource, goal classifiers | This cascades into E3 scoring, hippocampal anchors, and PFC goal/rule state. |
| More harm/interoceptive channels | `SD-010`, `SD-011`, `ARC-033`/`ARC-058`, comparator family levels | Adds stream-specific forward models and urgency/salience lanes. |
| Longer lifetime or episodes | replay buffers, anchor stores, sleep/consolidation quota, staleness accumulators | Memory growth without consolidation increases interference. |
| Multi-agent ecology | per-agent self/harm/drive state, other-model slots, mirror modelling, social trajectory scoring | Mostly V4/V5 scope; cannot be reduced to wider single-agent `z_world`. |
| More active goals | `SD-046` goal slots, dACC arbitration, ghost-goal bank ranking | Active slot count must remain capacity-limited, not unbounded. |
| Larger latent dims | hidden widths, residue basis count, E1/E2/Hippocampal projection widths | Derived compute scaling. Wider is useful only if specialization remains measurable. |

Rule of thumb: derived scaling preserves interface contracts. If more modalities, actions, or
goals are added, the dependent modules widen or multiply because they need to keep the same
typed responsibilities under a larger surface.

---

## Deliberate intelligence scaling

These are candidates for independent scaling: they may increase competence even when the
raw input surface is unchanged.

| Subsystem | Independent scale lever | Why it may increase intelligence |
|---|---|---|
| E1 associative manifold | schema depth, ContextMemory slots, abstraction levels, cue-indexed retrieval capacity | Supports more durable priors, cross-context transfer, and stable self/world models (`ARC-001`, `MECH-150`, `MECH-153`, `MECH-156`). |
| E2 counterfactual model | transition ensemble size, action-object resolution, uncertainty heads, calibrated horizon | Improves causal attribution and local planning precision without necessarily widening E1 (`ARC-002`, `SD-004`, `MECH-033`, `MECH-095`). |
| Hippocampal system | anchor count, pattern-separation budget, rollout horizon, candidate count, replay diversity, event-region keys | Directly increases imaginative search, memory specificity, and recovery from stale schemas (`ARC-007`, `ARC-018`, `MECH-149`, `MECH-165`, `MECH-269`, `MECH-284`, `MECH-288`). |
| E3 commitment | number of precommit hypotheses, veto channels, tri-loop arbitration depth, cancel-window modelling | Improves action selection under uncertainty and prevents premature collapse (`ARC-003`, `MECH-061`, `MECH-062`, `MECH-138`, `MECH-140`, `MECH-141`). |
| Goal system | active goal slots, dormant goal library, ghost-goal probe budget, goal-payload richness | Supports parallel workstreams and unresolved-goal recovery (`MECH-112`, `SD-039`, `MECH-292`, `MECH-293`, `SD-046`). |
| PFC/frontal substrates | rule-state capacity, OFC task-structure map size, future frontopolar branching depth | Enables abstract rules, task transfer, nested control, and deliberate branch holding (`SD-033`, `SD-033a`, `SD-033b`, `SD-033e`, `MECH-298`). |
| Cingulate/control plane | operating-mode palette, salience arbitration resolution, precision bandwidth | Better adaptive-control allocation and less mode collapse (`ARC-005`, `ARC-016`, `SD-032`, `MECH-157`, `MECH-267`). |
| Offline consolidation | SWS/REM cycle budget, replay priority schedule, replay diversity floor, schema slot formation/filling | Converts experience into usable structure; prevents harm-dominated replay and monostrategy collapse (`INV-010`, `SD-017`, `MECH-120`-`MECH-124`, `MECH-166`). |
| Residue/valence map | number of valence channels, field basis density, staleness/uncertainty overlays | Supports richer ethical and motivational terrain, but risks over-resolution if z_world is not structured (`ARC-013`, `ARC-036`, `SD-014`). |
| Option/chunk substrate | reusable option library size, action-chunk cache, abstraction vocabulary | Moves planning from atomic action sequences to reusable subroutines (`SD-042`, `SD-045`, `MECH-299`, `MECH-300`). |
| Attention/access gate | E1/E2-to-E3 broadcast capacity, selection policy, competition temperature | Determines which content reaches commitment; more upstream representation is wasted if access is too narrow or noisy (`SD-027`, `MECH-089`). |
| Social/mirror modelling | number of other-agent models, welfare-gradient slots, shared-plan rollout depth | Required for later social intelligence; this is not just derived from sensory input (`ARC-010`, `INV-029`, V4 multi-agent ecology). |

The strongest independent scaling candidates are hippocampal search/replay, E1 schema
capacity, E3/PFC precommit branching, active/dormant goal handling, and offline
consolidation. These are the areas most likely to turn more substrate into better reasoning.

---

## Mixed levers: derived plus deliberate

Some parts scale for both reasons.

### Shared latents

`z_self`, `z_world`, `z_beta`, `z_theta`, and `z_delta` must widen when the encoded domain
outgrows the bottleneck. But widening them deliberately is only justified if diagnostics show
interference, low effective dimensionality, or failed routing. `MECH-069` and the
efficiency-dimensionality hypothesis warn that a wider unified latent can be worse than a
smaller typed latent.

### Hippocampal horizon and candidate count

Horizon and candidate count derive from action-object complexity and task timescale, but
also form an independent intelligence lever. Holding the environment fixed, increasing
rollout diversity and horizon should improve long-horizon problem solving until the
candidate set becomes too noisy or too expensive for E3 to evaluate.

### Goal slots

More resource types and social roles require more possible goals. But the number of
**simultaneously active** goals is an independent capacity decision. Active slots should be
capacity-limited and arbitrated; dormant goals should live in retrievable memory structures.

### Offline replay budget

More experience requires more replay. But replay policy is independently intelligent:
diverse, staleness-prioritised, and counterfactual replay can improve future behaviour even
with the same amount of waking data.

### Frontal/PFC capacity

More tasks and goals require more rule-state capacity. But frontopolar branching, event-gated
goal writes, and nested-operation holding are independent levers for deliberative intelligence.

---

## Parts that probably should not scale naively

| Part | Avoid naive scaling because |
|---|---|
| E1 feature basis | `MECH-068` places selectivity in consolidation/gating, not by making E1 represent every downstream preference separately. |
| Unified latent dimensionality | `MECH-069` says sensory, motor-sensory, and harm/goal errors are incommensurable. More shared dimensions can hide credit-assignment failure. |
| Active goal slots | Too many active goals create arbitration collapse. Keep active slots small; scale dormant goal memory separately. |
| Hippocampal replay without hypothesis tags | Replay must not write as if it were committed reality (`MECH-094`, `MECH-120`-`MECH-124`). |
| Sensory bandwidth before binding | More raw input without `ARC-017`/`MECH-103` binding and precision routing produces noise, not intelligence. |
| Residue basis density | Prior evidence notes that fine residue resolution at V3 scale can be counterproductive when z_world lacks spatial organisation. |
| Habit/action chunks | Larger chunk libraries increase speed but can amplify compulsive lock-in unless invalidation and replay remain healthy (`SD-045`, `MECH-284`/`MECH-285`). |

---

## Candidate scaling profiles

These are not implementation presets. They are design profiles that later version specs can
turn into config presets.

| Profile | Primary deliberate scaling | Derived scaling expected |
|---|---|---|
| V3-large single-agent | wider typed latents, stronger E2/action-object model, longer hippocampal horizon, more replay budget | hidden widths, residue basis count, resource/harm heads |
| V4 lifetime agent | persistent memory, long-horizon dynamics, sleep/consolidation depth, self-model temporal depth | replay buffers, anchor stores, staleness maps, persistent body-state |
| V4 deliberative agent | PFC rule/OFC task maps, frontopolar branch depth, precommit hypothesis budget | E3 arbitration, access gate bandwidth, goal payload richness |
| V4/V5 social agent | other-agent model slots, social welfare gradients, joint trajectory rollout | multi-agent env state, mirror channels, communication/manipulation action vocabulary |
| V5 abstraction agent | option libraries, type-prototype anchors, theta packet content at abstraction level | action-object decoder, anchor payloads, hippocampal traversal vocabulary |

---

## Proposed diagnostics

Future scaling experiments should distinguish derived necessity from independent
intelligence gain:

1. **Hold sensory bandwidth fixed; scale hippocampal search.** Vary horizon, candidates,
   and replay diversity. Measure long-horizon benefit, regret recovery, and monostrategy
   collapse.
2. **Hold latent dims fixed; scale E1 schema slots.** Measure cue-indexed retrieval,
   distractor resistance, and cross-context transfer.
3. **Hold E1/E2 fixed; scale active goal slots.** Measure dACC arbitration quality,
   ghost-goal recovery, and commitment instability.
4. **Hold waking data fixed; scale offline consolidation.** Measure slot formation,
   slot filling, replay diversity, and harm-dominant replay contraction.
5. **Hold action count fixed; scale option/chunk abstraction.** Measure planning speed,
   transfer, and compulsive lock-in signatures.
6. **Hold social sensory input fixed; scale other-model slots.** Measure whether mirror
   modelling and welfare-sensitive planning improve without merely increasing observation
   dimensionality.
7. **Scale modality count with and without typed stream routing.** Confirm that wider
   sensory input helps only when `ARC-017`, `MECH-103`, and precision routing remain intact.

These diagnostics should be run as paired sweeps: one sweep where a module scales only as
required by a larger surface, and one sweep where the same module scales independently while
the surface stays fixed.

---

## Working conclusion

The current architecture suggests this hierarchy:

1. **Necessary substrate scale:** sensory streams, action vocabulary, resource/goal identities,
   harm/interoceptive channels, and hidden widths.
2. **Primary intelligence scale:** E1 schema capacity, E2 counterfactual precision,
   hippocampal rollout/replay/search, E3/PFC precommit branching, goal-memory management,
   and offline consolidation.
3. **Risk-control scale:** precision routing, access gates, commit boundaries, hypothesis tags,
   replay priority, and invalidation/staleness mechanisms.

REE should therefore scale by **typed capacity budgets** rather than by a single global model
size. Later versions should make these budgets explicit in a scale profile: sensory bandwidth,
latent dimensions, action-object vocabulary, hippocampal search budget, active goal slots,
PFC branch depth, replay/consolidation budget, social model count, and option/chunk library size.
