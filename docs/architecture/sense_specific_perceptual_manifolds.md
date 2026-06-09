# Sense-specific perceptual manifolds before shared world-model entry

Status: SEED / candidate cluster (V4/V5 perception). Off the V3 / GAP-7 critical path.

Home doc for the claim cluster reaped from
[docs/thoughts/2026-06-07_sight_specific_perceptual_manifolds.md](../thoughts/2026-06-07_sight_specific_perceptual_manifolds.md)
(source trigger: the ScienceDaily report on completing Schrodinger's colour theory).

## Seed

Senses differ in **how much transformation they need before entering the shared world model**. A sense
does not contribute raw data directly; it contributes a *shaped geometry of possible differences*.

- **Smell** is naturally gradient-like (stronger/weaker, nearer/farther, attractive/aversive,
  trail/no-trail, source-seeking/avoiding) and can enter cognition as a **near-raw primitive
  orientation signal** with a minimal adaptor -- a local gradient that can be followed, escaped,
  strengthened, weakened, remembered, and associated with outcome. This makes a smell-like sense
  unusually compatible with **early** REE world-model construction.
- **Sight** is not like this. Even colour perception requires a structured perceptual geometry
  (hue/saturation/lightness emerge from the geometry of perceptual *similarity*, not as labels attached
  to raw stimulus) before becoming cognitively useful. Vision needs a **deep adaptor**.

The architectural pattern:

```text
physical signal
-> receptor encoding
-> modality-specific adaptor
-> perceptual metric / manifold
-> stable perceptual primitives
-> shared world-model update
-> action arbitration
```

The adaptor is **not an optional feature extractor**: it is the stage where raw physical signal becomes
a usable geometry of difference. The shared world model is built from sense-specific geometries made
mutually negotiable, **not** from interchangeable raw sensory channels.

## What REE already owns (cross-ref, not duplicated)

| Owned claim | What it covers | Why this cluster is distinct |
|---|---|---|
| **ARC-017** sensory stream tags | Minimal stream-tag set with typed exteroception + reality-coherence lane | Tags the streams; says nothing about per-sense transformation depth or manifold geometry |
| **MECH-103** E1 multimodal exteroceptive fusion | Each modality has its own encoder pathway into the shared latent; complementary structure; multi-source precision-weighted fusion | Treats the pathway as a *feature extractor / fusion* step; does not claim it is a **metric/manifold constructor** whose depth is sense-specific |
| **ARC-027** harm stream parallel pathway | Nociceptive stream runs parallel to z_world | A specific stream-separation, not the general adaptor-depth heterogeneity principle |
| **ARC-019** staged curriculum | Development is gated/staged | This cluster adds *which* sense is admitted when, indexed by adaptor depth (smell-first) |

## Claims in this cluster

- **ARC-087** (architectural_commitment): sense-specific perceptual-manifold adaptor -- each modality
  requires its own adaptor transforming raw stimulus space into a perceptual-manifold (metric) space
  **before** shared-world-model entry; senses are not interchangeable raw streams. The adaptor is a
  metric/manifold constructor, not merely a feature extractor.
  `depends_on: ARC-017, MECH-103, ARC-004, ARC-005, ARC-019`.
- **MECH-372** (mechanism_hypothesis): modality-heterogeneity / adaptor-depth gradient -- senses differ
  in transformation depth (smell near-raw gradient; sight deep manifold: colour geometry, edges,
  figure-ground, depth, invariances, affordance/gaze salience). Developmental-ordering corollary:
  gradient-like (low-adaptor-depth) senses enter earliest. `depends_on: ARC-087, ARC-017, ARC-019,
  MECH-103`.
- **Q-065** (open_question): (1) is each modality's perceptual metric **learned** or partly **defined**?
  (2) how are heterogeneous sense-specific geometries (smell gradient; sight manifold; touch
  boundary/pressure/texture/contact; hearing temporal-source/rhythm/pitch/localisation; proprioception
  body-state transition) made **mutually negotiable** inside one shared world model? `depends_on:
  ARC-087, MECH-372`. `epistemic_category: substrate_conditional` set explicitly so
  `narrow_open_question` does not fire.

## V3 vs V4/V5 boundary (DO NOT build in V3)

All three claims are `status: candidate`, `epistemic_category: substrate_conditional`,
`implementation_phase: v4`, `version_relevance: v4_v5`. For **REE-v3**, smell/gradient-only sensing
remains appropriate and a deep adaptor is unnecessary -- this cluster is **off the V3 / GAP-7 critical
path**. The benchmark dates in the source thought (optimistic 2026-06-28 / strict green-board 2026-07-19
/ pessimistic 2026-08-16) are V3 milestones; this work must not distract from them. For **V4+**,
multimodal sensing must not be treated as "add more input channels" -- each sense needs its own
preprocessing grammar, and the shared world model should receive already-shaped perceptual structure.

Because all three carry `epistemic_category: substrate_conditional`, they are suppressed from
promotion/demotion and from the IGW `/queue-experiment` proposal lane during the V3 phase (same
construction as the play-mode cluster) -- no `blocked_substrate` STOPs needed.
