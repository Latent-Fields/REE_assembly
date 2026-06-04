# Principles of object perception (Spelke 1990)

## What the paper did

This is the field-defining synthesis in which Spelke argued that infants do not parse the
visual world into objects using Gestalt "good form" (proximity, similarity, good
continuation), but instead apply a small set of principles that track the behaviour of
*material bodies*. Drawing together a decade of habituation and preferential-looking studies,
she identified three:

- **Cohesion** — an object is a single bounded entity; its surfaces move as one connected
  whole, and a thing cannot break and re-form arbitrarily.
- **Continuity** — an object traces exactly one connected path over space and time, and two
  objects cannot occupy the same place at the same time.
- **Contact** — objects act on one another only when they touch.

These principles, she argued, are early-developing, are not learned associations, and continue
to underwrite object representation into adulthood.

## Why it grounds ARC-006 / MECH-045 and the permanence pillar

For the object-representation thread the key principle is **continuity**, because continuity
*is* permanence stated formally. If an object must trace one connected spatiotemporal path,
then an object that disappears behind an occluder cannot be treated as gone — it must be
represented as continuing along its path until it re-emerges. Permanence is just continuity
applied across a perceptual gap. That gives the proposed permanence pillar a principled
definition to build to, rather than an intuition.

**Cohesion** grounds the other half of ARC-006: the claim that entities are "sparse, bounded,
bindable structures." The cohesion principle tells us what the unit *is* — the connected whole
that an object-file (MECH-045) should key on. **Contact** connects forward to the tools /
affordances pillar (PILLAR 3): causal interaction requires touch, which is the same
intervention-coherence idea MECH-278 uses to define an object. So one short paper supplies a
biology-grounded definition for three of the four pillars at once, and it does so at the
token-neutral, kind-neutral level the spine wants.

## Limitations and caveats

Two boundaries matter. First, these are principles for analysing the perceptual *input* into
objects — they describe segmentation and individuation at the moment of perception. They are
not a theory of the persistence *buffer* that holds an object while it is out of view. They
tell us what the permanence representation must respect (one connected path, one bounded
whole); they are silent on how it is stored, keyed, or queried. That storage layer is exactly
what MECH-045 must add. Second, and worth flagging for REE specifically: the cohesion
principle describes the very segmentation that REE currently *bypasses*. V3's `z_world` is
engineered pre-split — MECH-278 calls this the "architectural shortcut past stage 2" — so REE
gets objects-as-patterns for free rather than deriving them from cohesion. That is a sound V3
simplification, but it means this paper grounds a capability the substrate has not actually
built bottom-up.

A note on scope: the principles are deliberately *kind-neutral*. They define "bounded physical
object" without any sortal/category content. This is the correct level for a token object-file,
and it is orthogonal to REE's SD-049 type-tag identity. The two answer different questions —
"is this one connected thing on one path?" versus "what kind of thing is it?" — and the
object-representation memo's whole point is that REE has built the second and lacks the first.

## Confidence reasoning

Confidence 0.72. Source quality is high (0.80) given the paper's canonical status, but it is a
synthesis — the empirical force lives in the primary studies it reviews. Mapping fidelity is
strong (0.75) for the continuity=permanence and cohesion=unit correspondences, the two we most
need. I hold the aggregate at 0.72 because the principles describe perception rather than
storage, and because REE's engineered `z_world` means the substrate does not yet instantiate
the segmentation the principles assume.
