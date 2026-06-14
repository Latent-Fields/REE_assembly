---
title: Sense-specific perceptual manifolds before shared world-model entry
parent: "Perception, Representation & Dynamics"
grandparent: Architecture
nav_order: 4
---

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

## PA-1 decision -- adaptor-depth axis structure (2026-06-14)

`perceptual_adaptors_v4:PA-1` was the cluster's first design fork: along what axis do adaptors
differ, and how is that axis structured? Resolved in an interactive design-fork session as
**Option C -- one orderable depth continuum with a biologically-named regime boundary** (not Option A
"single uniform mechanism", not Option B "two unrelated kinds"). The decision was made against the
human-brain existence proof (project rule: *biology before formal definitions*).

**The two-regime structure adopted:**

```text
[ gradient / chemical regime ]                 [ metric-manifold regime ]
  olfaction, interoception                       vision, audition, somatosensation,
  - bypasses thalamus (bulb -> piriform)         vestibular / proprioception
  - 3-layer paleocortex                          - thalamic relay -> 6-layer neocortex
  - non-topographic (content-addressable,        - canonical cortical microcircuit
    combinatorial; no spatial map)               - topographic maps (retinotopy / tonotopy /
  - phylogenetically older                         somatotopy)
                                                 - adaptor depth set by INPUT STATISTICS
                                                   + hierarchy length
              \__________ boundary = thalamic relay + topographic neocortex __________/
```

**Evidence that decided it.**

| Observation | Source | What it settles |
|---|---|---|
| Auditory cortex builds **visual** orientation maps when fed retinal input | Sur et al. rewiring | The thalamocortical senses share **one** canonical mechanism; depth is a continuum dialed by input statistics (rules out Option B *within* that family) |
| Olfaction bypasses the thalamus, is paleocortical and **non-topographic** | olfactory neuroanatomy (bulb -> piriform) | The gradient/chemical sense is a genuinely **distinct, older adaptor class** -- not merely a shallow manifold (rules out a pure Option A) |
| Cross-modal integration is **shared-reference-frame precision/reliability weighting** for cues with a common estimand | Ernst & Banks 2002; Gu 2008 (PA-7) | Within-family senses co-register cheaply; this is the natural PA-5 currency *inside* the metric-manifold regime |
| All perceptual spaces are metric | Shepard 1987 (PA-7) | The metric-manifold regime is internally a true continuum (depth = dimensionality / hierarchy), so the axis is orderable for PA-6 |

**Why this protects multimodal perception + integration (the design concern that drove the call).**
Option A would force chemical/gradient senses into a topographic-manifold mold they do not occupy in
biology (degrading the gradient senses). Option B would deny the canonical mechanism the thalamocortical
senses demonstrably share, fragmenting exactly the senses (vision + audition + touch + proprioception)
that most need tight metric co-registration for spatial world-modelling. Option C keeps that family in
one compatible regime -- they integrate via shared-frame precision-weighting -- while the gradient/
chemical regime integrates through a **coarser valence / orientation / salience channel** (amygdala / OFC
association), which is the integration topology the brain actually exhibits for olfaction.

**Downstream consequences fixed by this decision.**

- **PA-6** (adaptor-maturity curriculum): the developmental ordering is now principled -- the older
  non-topographic regime enters first *as a regime*, not just because it is shallow. "Smell may have
  been the first sense" is the regime-boundary statement.
- **PA-4** (metric origin): the learned-vs-defined fork applies to the **metric-manifold regime**; the
  gradient regime carries a near-identity / structural orientation prior by construction.
- **PA-5** (cross-modal negotiation currency): the currency is now **two-tier** -- shared-frame
  precision-weighting *within* the metric-manifold regime, plus a coarse cross-regime valence/salience
  channel. The harder *unification* problem (structurally dissimilar manifolds; the PA-7 Gu-2008 caveat)
  is correctly localised here and is **not** trivialised by PA-1.

**Honest caveat (recorded on the claims).** "Smell = shallow" is an **architecture** statement
(non-topographic / gradient), not a claim that olfaction is a low-information modality -- human odor
perception is itself high-dimensional and object-like. PA-7's Louis-2007 entry grounds "orientation is
cheap", not "olfaction is shallow".

**Governance.** No new hard `depends_on` edge: the cross-regime valence channel rides ARC-005's
control-plane precision routing (already in `depends_on`); cross-refs to the affect/valence machinery
(SD-012 homeostatic drive, ARC-027 harm stream, ARC-088 anti-collapse map) are PA-5-downstream and
recorded as cross-references, not build dependencies. Recorded on ARC-087 (full rationale) and MECH-372
(developmental-ordering sharpening). Both stay `candidate` / `substrate_conditional` / `v4` -- **PROMOTES
NOTHING** (exp_conf stays 0). Off the V3 / GAP-7 critical path; DO NOT build in V3.
