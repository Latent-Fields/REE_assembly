---
closure_plan:
  id: perceptual_adaptors_v4
  generation: v4
  title: "Sense-specific perceptual-manifold adaptors (V4 modality-heterogeneous perception roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-087, MECH-372, Q-065, ARC-017, MECH-103, ARC-004, ARC-005, ARC-019]
  sibling_plans: [object_representation_v4, inference_belief_state_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 perception substrate step is honest to build.
    generation: v4 keeps these nodes OUT of the V3 closure percentage (serve.py
    read_closure, generate_closure_snapshot.py and check_closure_drift.py are
    all generation-aware). The whole cluster (ARC-087 / MECH-372 / Q-065) is
    epistemic_category substrate_conditional: there is no V4+ multimodal-
    perception substrate yet, so these nodes are suppressed from the IGW
    proposal lane and must NOT be built in V3 -- V3's gradient-only / smell-like
    sensing is correct for V3. A node graduates from roadmap to closure-tracked
    by gaining an owner_exq once its first V4 experiment is queued.
  nodes:
    - id: "perceptual_adaptors_v4:PA-1"
      title: "Smell-vs-sight adaptor-depth fork (the first design decision)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-087, MECH-372]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 LIVE perception is the near-raw / gradient end: smell-like sensing, gradient-only world signal, no deep visual adaptor (ARC-087 + MECH-372 both confirm V3 needs no adaptor)"
        - "ARC-017 minimal stream tags + MECH-103 per-modality encoder pathway already own the STREAM and FUSION layers, but NOT the per-sense transformation depth"
        - "DECISION the fork forces: does a V4 sense enter as a near-raw gradient primitive (smell: stronger/weaker, nearer/farther, attractive/aversive) or via a deep perceptual-manifold adaptor (sight: colour geometry, edges, figure-ground, depth, invariances, gaze salience)? Adaptor depth is per-sense, not uniform."
      last_updated: 2026-06-10
      completion_note: "MECH-372 establishes that modalities are NOT interchangeable raw streams of equal depth. Picking the depth axis (gradient-primitive vs manifold-constructor) is the precondition for every node below. This is a genuine representational gap, not a missing flag."
    - id: "perceptual_adaptors_v4:PA-2"
      title: "PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense"
      phase: 2
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-372, ARC-019]
      depends_on: ["perceptual_adaptors_v4:PA-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 gradient-only sensing already approximates a smell-like primitive (follow / escape / strengthen / weaken / remember / associate-with-outcome) -- this is the LIVE near-raw end, the lowest-risk first V4 adaptor"
        - "ARC-019 staged curriculum (provisional) must carry an adaptor-maturity gate so the low-adaptor sense is admitted first"
        - "MECH-372 developmental-ordering corollary (gradient-like senses enter earliest) must be operationalised as a curriculum primitive, not prose"
      last_updated: 2026-06-10
      completion_note: "The smell-like gradient is the cheapest, earliest-honest V4 adaptor and the proof-of-pattern for the adaptor stage. It builds directly on what V3 already has, so it is the right first concrete substrate step once the fork (PA-1) is chosen."
    - id: "perceptual_adaptors_v4:PA-3"
      title: "PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-087, MECH-372]
      depends_on: ["perceptual_adaptors_v4:PA-1", "perceptual_adaptors_v4:PA-2"]
      cross_plan_link: []
      blocking_on: "MECH-103 is untestable in V3 (EXQ-128 / EXQ-134 FAIL, both superseded: no genuine multimodal input). A real multimodal V4 input substrate must exist before a deep visual adaptor is meaningful."
      readiness_gate:
        - "Reactivate / extend MECH-103 (per-modality encoder pathway) on a genuine V4 multimodal input substrate -- the EXQ-128/134 superseded FAILs flagged the substrate absence, not the mechanism"
        - "ARC-087 metric/manifold-constructor commitment: adaptor must build colour geometry, edge/boundary, figure-ground, motion fields, depth, occlusion, lighting/angle invariances, affordance + gaze salience BEFORE z_world entry (not a flat feature extractor)"
        - "ARC-004 multi-timescale latent stack must carry already-shaped perceptual structure, not raw pixels, into the shared latent"
      last_updated: 2026-06-10
      completion_note: "ARC-087's central claim: vision cannot enter as raw signal; the adaptor IS the metric constructor. This is the deep end of the depth gradient and the hardest substrate -- gated on a real multimodal input substrate (PA-2's pattern proven first) and on MECH-103 reactivation."
    - id: "perceptual_adaptors_v4:PA-4"
      title: "Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [Q-065]
      depends_on: ["perceptual_adaptors_v4:PA-3"]
      cross_plan_link: []
      readiness_gate:
        - "Q-065 part (1): for each modality, is the perceptual metric self-organised from the statistics of perceptual similarity (colour geometry from similarity structure) or partly innate (a structural prior on the manifold)?"
        - "Resolvable only once at least one deep adaptor exists (PA-3) so the learned-vs-defined fork has a substrate to be tested against -- this is why Q-065 is substrate_conditional, not narrow_open_question"
        - "ARC-019 curriculum must allow training-time self-organisation of the metric if the LEARNED arm is taken"
      last_updated: 2026-06-10
      completion_note: "Q-065's first coupled question. It is a fork inside the adaptor design, not a separate pillar: the answer determines whether the adaptor ships with a fixed manifold prior or a learnable similarity metric. Substrate_conditional keeps it off the V3 experiment lane."
    - id: "perceptual_adaptors_v4:PA-5"
      title: "PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world model"
      phase: 4
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [Q-065, MECH-103, "MECH-396"]
      depends_on: ["perceptual_adaptors_v4:PA-2", "perceptual_adaptors_v4:PA-3"]
      cross_plan_link: []
      blocking_on: "Requires at least TWO structurally dissimilar adaptors live (a low-adaptor gradient sense, PA-2, AND a deep-adaptor manifold sense, PA-3) before a negotiation currency between them can be specified or tested."
      readiness_gate:
        - "Q-065 part (2): how are smell's gradient geometry, sight's perceptual manifold, touch's boundary/pressure/texture/contact geometry, hearing's temporal-source/rhythm/pitch/localisation geometry, and proprioception's body-state-transition geometry made MUTUALLY NEGOTIABLE inside one shared world model?"
        - "MECH-103 multi-source precision-weighted fusion already PRESUPPOSES a common negotiation currency across dissimilar manifolds -- this node names and builds that currency (the unification problem behind fusion)"
        - "ARC-005 control plane (precision routing) is the natural home for the negotiation/precision-weighting layer that arbitrates across heterogeneous geometries"
      last_updated: 2026-06-10
      completion_note: "The deepest open problem in the cluster: fusion (MECH-103) assumes a shared currency that no claim currently specifies. PILLAR C is that specification -- a new substrate primitive proposed as MECH-396, not a duplicate of MECH-103's fusion mechanism."
    - id: "perceptual_adaptors_v4:PA-6"
      title: "Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-372, ARC-019, "MECH-397"]
      depends_on: ["perceptual_adaptors_v4:PA-1"]
      cross_plan_link: []
      readiness_gate:
        - "ARC-019 staged developmental curriculum (provisional) -- the existing curriculum-stages claim that this gate specialises"
        - "MECH-372 developmental-ordering corollary: low-adaptor-depth senses enter earliest; high-adaptor-depth (vision) require more scaffolding -- needs to become a concrete gate primitive (adaptor-maturity admission criterion) rather than prose"
        - "PA-1 fork resolved so adaptor depth per sense is known and orderable"
      last_updated: 2026-06-10
      completion_note: "MECH-372's corollary ('smell may have been the first sense') is currently prose inside ARC-019's curriculum. The concrete gate -- an admission criterion keyed to adaptor maturity that orders senses by depth -- is a new mechanism proposed as MECH-397."
    - id: "perceptual_adaptors_v4:PA-7"
      title: "Biology grounding completion (perceptual-manifold / colour-geometry / multisensory-binding lit-pulls)"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-087, MECH-372, Q-065]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "L1 perceptual-manifold / similarity geometry (Schrodinger colour theory completion, the source trigger; Shepard generalisation; colour-opponent geometry) -- NOT yet pulled"
        - "L2 modality-specific adaptors (olfactory gradient chemotaxis; ventral-stream visual hierarchy; somatosensory cortex topography) -- NOT yet pulled"
        - "L3 multisensory convergence currency (STS multisensory neurons; MST optic-flow/vestibular/auditory integration; Murray et al. 2004 cross-modal ventral binding -- already cited in MECH-103) -- partial"
      last_updated: 2026-06-10
      completion_note: "Project rule feedback_biology_before_formal_definitions: ARC-087 / MECH-372 / Q-065 were reaped from a single ScienceDaily-triggered intake with no dedicated biology lit-pull. This node tracks closing that grounding debt before the deep-adaptor substrate (PA-3) is built. The biology-right / mechanism-wrong failure mode (SD-003, SD-010/011) is the canonical risk."
---
# Sense-specific Perceptual-Manifold Adaptors -- V4 Modality-Heterogeneous Perception Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the perception-adaptor cluster -- ARC-087 (sense-specific
adaptor substrate), MECH-372 (modality-heterogeneity / adaptor-depth gradient +
developmental ordering), Q-065 (metric origin + cross-modal negotiability) --
against their V3-era prerequisites (ARC-017 stream tags, MECH-103 multimodal
fusion, ARC-004 latent stack, ARC-005 control plane, ARC-019 curriculum), so V4
multimodal-perception substrate work slots in against a registered spine instead
of being built as "add more input channels."

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value here is the **readiness gates** -- for each adaptor pillar, exactly which
V3-era prerequisites (claims/tracks) must land before the V4 substrate step is
honest to build.

---

## One-line framing

> A sense does not contribute raw data to the shared world model -- it
> contributes a *shaped geometry of possible differences*. Smell sits at the
> near-raw / low-adaptor end (a gradient primitive REE-v3 already approximates);
> sight sits at the deep end (a perceptual-manifold constructor that must build
> colour geometry, edges, depth and invariances before world-model entry). The
> open problems are (a) which adaptor depth each sense needs, (b) whether each
> metric is learned or defined, and (c) the common currency that makes
> structurally dissimilar geometries mutually negotiable inside one world model.

---

## The adaptor pillars (specialisations of one depth gradient)

| Pillar | Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| (fork) adaptor depth | PA-1 | ARC-087 / MECH-372 | V4 (first decision) | V3 gradient-only sensing live; ARC-017 tags + MECH-103 pathway own stream+fusion, not depth |
| A -- low-adaptor (smell/gradient) | PA-2 | MECH-372 | V3-straddle / V4 | V3 gradient sensing approximates it; ARC-019 needs adaptor-maturity gate |
| B -- deep-adaptor (sight manifold) | PA-3 | ARC-087 | V4 | reactivate MECH-103 on real multimodal input; ARC-004 carries shaped structure |
| metric-origin fork | PA-4 | Q-065 (1) | V4 | learned-from-similarity vs defined-prior; needs PA-3 substrate to test |
| C -- cross-modal negotiation | PA-5 | Q-065 (2) / MECH-103 | V4 | two dissimilar adaptors live; ARC-005 hosts the negotiation/precision layer |
| adaptor-maturity curriculum | PA-6 | MECH-372 / ARC-019 | V3-straddle / V4 | ARC-019 staged curriculum + MECH-372 smell-first corollary as a concrete gate |
| biology grounding debt | PA-7 | ARC-087/MECH-372/Q-065 | cross-cutting | L1..L3 perceptual-manifold / colour-geometry / multisensory lit-pulls (none yet) |

---

## What this plan deliberately does NOT pull into V3

- **No deep adaptor in V3.** ARC-087 and MECH-372 both state explicitly that
  V3's gradient-only / smell-like sensing is correct and a deep adaptor is
  unnecessary. Building a perceptual-manifold constructor in V3 is off the
  critical path and would distract from the V3 milestones (the source thought's
  green-board dates are V3 work). The first deep-adaptor substrate step (PA-3)
  is V4 and must not enter V3 closure.
- **No experiments, no claim promotions, no substrate code.** The whole cluster
  is `epistemic_category: substrate_conditional`, which (same construction as the
  play-mode cluster) suppresses promotion/demotion and keeps the claims out of
  the IGW `/queue-experiment` proposal lane during V3 -- no `blocked_substrate`
  STOPs needed. Registering this roadmap changes no V3 behaviour.
- **MECH-103 is not re-tested on V3 substrate.** EXQ-128 / EXQ-134 already FAILed
  and were marked superseded (no genuine multimodal input in V3). Re-running them
  on V3 would re-create the same vacuous FAIL; PA-3 gates MECH-103 reactivation on
  a real V4 multimodal input substrate.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/sense_specific_perceptual_manifolds.md](../../docs/architecture/sense_specific_perceptual_manifolds.md) | Home doc for the cluster (ARC-087 / MECH-372 / Q-065) + owned cross-refs |
| docs/thoughts/2026-06-07_sight_specific_perceptual_manifolds.md | Source intake (Schrodinger colour-theory completion trigger) |
| claims.yaml ARC-087 / MECH-372 / Q-065 | adaptor substrate + depth gradient + metric/negotiability question (all `implementation_phase: v4`, `substrate_conditional`, `version_relevance: v4_v5`) |
| claims.yaml ARC-017 / MECH-103 / ARC-004 / ARC-005 / ARC-019 | the V3-era prerequisites named in the readiness gates |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap in the closure-map
  pipeline. Nodes seeded from ARC-087 / MECH-372 / Q-065 with V3 prerequisites
  pinned per pillar. `generation: v4` set so the V3 closure % is unaffected.
  Two prose-only V4 substrate gaps surfaced and proposed as NEWCLAIM stubs:
  `cross_modal_negotiation_currency` (PA-5, the common currency MECH-103 fusion
  presupposes but no claim specifies) and `adaptor_maturity_curriculum_gate`
  (PA-6, the concrete admission gate that makes MECH-372's smell-first corollary
  operational inside ARC-019). No claims.yaml edits.
