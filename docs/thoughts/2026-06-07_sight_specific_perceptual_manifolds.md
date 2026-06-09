# Thought: Sight-specific perceptual manifolds before shared world-model entry

Date: 2026-06-07

Status: processed

Source trigger: ScienceDaily article on completing Schrödinger's colour theory, linked from discussion: https://www.sciencedaily.com/releases/2026/06/260606015140.htm

## Core intuition

Smell may have been the first sense, and may remain one of the least transformed senses before entry into shared world-model space.

Smell is naturally gradient-like:

- stronger / weaker
- nearer / farther
- attractive / aversive
- trail / no trail
- source-seeking / source-avoiding

This makes smell unusually compatible with early REE world-model construction. A smell-like sense can plausibly enter cognition as a primitive orientation signal: a local gradient that can be followed, escaped, strengthened, weakened, remembered, and associated with outcome.

Sight is not like this.

Vision cannot simply enter the shared world model as raw signal. Even colour perception alone appears to require a structured perceptual geometry before it becomes cognitively useful. Hue, saturation, and lightness are not just names attached to raw sensory data after the fact. They can be understood as emerging from the geometry of perceptual similarity itself.

This suggests that visual perception requires a sense-specific adaptor layer: a transformation from raw stimulus space into perceptual-manifold space before the shared world model can make use of it.

## REE implication

A sense does not contribute data directly to the shared world model.

A sense contributes a shaped geometry of possible differences.

Smell contributes gradient geometry.

Sight contributes perceptual-manifold geometry.

Touch may contribute boundary, pressure, texture, resistance, and contact geometry.

Hearing may contribute temporal-source, rhythm, pitch, and localisation geometry.

Proprioception may contribute body-state transition geometry.

The shared world model is therefore not built from raw sensory channels. It is built from sense-specific geometries made mutually negotiable.

## Proposed architecture pattern

```text
physical signal
→ receptor encoding
→ modality-specific adaptor
→ perceptual metric / manifold
→ stable perceptual primitives
→ shared world-model update
→ action arbitration
```

For early REE, smell-like sensing can plausibly remain close to the world model as gradient information.

For later REE, especially v6+, multimodal sensing should not be treated as "add more input channels." Each sense needs its own preprocessing grammar. The shared world model should receive already-shaped perceptual structure, not raw signal.

## Sight-specific version

Sight-specific preprocessing likely needs to construct at least some of the following before visual material enters shared world-model space:

- perceptual distance metrics
- colour geometry
- edge / boundary extraction
- figure-ground separation
- motion fields
- depth relations
- object persistence
- occlusion handling
- invariances across lighting, angle, distance, and motion
- affordance extraction
- agency / face / gaze salience

The colour-perception example is useful because it shows that even a seemingly basic visual property is not a simple mapping from physical stimulus to cognition. The perceptual space itself has structure. It may be curved, compressed, asymmetric, non-additive, or otherwise unlike the raw measurement space.

## Design invariant

Each sensory modality should define or learn its own perceptual metric before being admitted into the shared world model.

The adaptor is not an optional feature extractor. It is the stage where raw physical signal becomes a usable geometry of difference.

## REE-v3 boundary

This should not be allowed to distract from REE-v3 strict green-board work.

Benchmark context:

- Optimistic target: 2026-06-28
- Strict green-board benchmark: 2026-07-19
- Pessimistic plausible date: 2026-08-16

For REE-v3, smell / gradient-only sensing remains appropriate.

For REE-v6+, this becomes relevant as a future multimodal-adaptor principle.

## One-line summary

Smell may enter the world model as gradient; sight must first become a perceptual manifold.

---

## Intake (2026-06-09)

Reaped into claims.yaml as a V4/V5 perception cluster (candidate / substrate_conditional /
implementation_phase v4 / version_relevance v4_v5), off the V3 / GAP-7 critical path. Already-owned
machinery cross-referenced via `depends_on` rather than duplicated: ARC-017 (sensory stream tags),
MECH-103 (per-modality encoder pathways + multi-source fusion), ARC-019 (staged curriculum). The
genuinely-new content registered: the sense-specific perceptual-manifold *adaptor* architecture
(metric/manifold constructor, not a feature extractor) and the modality-heterogeneity / adaptor-depth
gradient (smell near-raw, sight deep) with its smell-first developmental ordering. Home doc:
[docs/architecture/sense_specific_perceptual_manifolds.md](../architecture/sense_specific_perceptual_manifolds.md).

Processed in:

- docs/claims/claims.yaml#ARC-087 (sense-specific perceptual-manifold adaptor)
- docs/claims/claims.yaml#MECH-372 (modality-heterogeneity / adaptor-depth gradient; smell-first ordering)
- docs/claims/claims.yaml#Q-065 (per-sense metric origin + cross-modal negotiability open question)
- docs/architecture/sense_specific_perceptual_manifolds.md (home doc)
