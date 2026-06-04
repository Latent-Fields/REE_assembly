# Feature-integration theory of attention (Treisman & Gelade 1980)

**Claims:** ARC-006 (binding clause) | **Direction:** supports | **Confidence:** 0.78

## What the paper did

Treisman and Gelade's feature-integration theory (FIT) is the canonical statement of the
*binding problem*: given that the brain registers colour, orientation, motion and other
features in separate, parallel feature maps, how does it know which colour belongs to which
shape? Their answer, supported by a battery of visual-search, texture-segregation and
illusory-conjunction experiments, is a two-stage architecture. In the pre-attentive stage,
individual features are detected automatically and in parallel across the visual field --
a target defined by a single feature "pops out" regardless of how many distractors are
present. In the focal-attention stage, features at an attended location are *conjoined*
into a coherent object; this stage is serial and capacity-limited, so search for a
conjunction of features scales with set size. The decisive evidence that binding is an
active, attention-gated act rather than a free feedforward merge is the *illusory
conjunction*: when attention is unavailable or overloaded, subjects reliably mis-combine
features from different objects (reporting a red X when shown a red O and a green X).

## Why it matters for the claim

ARC-006's design constraints (entities_and_binding.md) lead with: "Binding is
attention-gated -- feature binding should depend on precision/attention state rather than a
purely feedforward merge." FIT is the foundational source and evidence for that exact
constraint. It establishes three things REE needs: (1) correct binding is not automatic --
it costs an attentional resource; (2) when that resource is absent, binding does not simply
fail to happen, it *mis-happens* (illusory conjunctions); and (3) features are available
pre-attentively but unbound. For REE this licenses a specific architectural choice: entity
formation should be conditioned on a precision/attention signal, not implemented as a
feedforward concatenation of latents. A REE that merged features without such a gate would,
by FIT's logic, predict the mis-binding that the gate exists to prevent.

## The mapping and its boundaries

The transfer is clean for ARC-006's *binding* clause but explicitly does not cover its
other clauses. FIT is about *within-moment* feature conjunction -- what binds into one
object right now -- and says nothing about *across-time persistence* (is this the same
object a second later?) or about *error ownership*. Those are carried by the object-file
and visual-indexing entries in this pull. There is also a historical caveat: the strict
serial-conjunction / parallel-feature dichotomy was softened by later work (Wolfe's Guided
Search; the 2019 *Attention, Perception, & Psychophysics* retrospective forty years on).
The durable, well-supported core that transfers to REE is therefore the weaker and more
robust claim -- *correct binding requires an attention/precision gate* -- not the specific
serial-scan mechanism, which a REE implementation should not over-commit to.

## Confidence

I set confidence at 0.78. The paper is foundational and the mapping onto ARC-006's
attention-gated-binding constraint is strong and near-direct. It is held below the top band
because (a) the serial-search specifics were later revised, so only the gating principle
transfers cleanly, and (b) FIT addresses binding but not the persistence and error-ownership
parts of ARC-006. Together with the object-file entry, the picture is that ARC-006's two
core mechanisms -- attention-gated binding and across-time persistence -- each have a
distinct, well-established biological source, neither of which is yet implemented in V3.

Source: [Treisman & Gelade 1980, Cognitive Psychology 12:97-136](https://doi.org/10.1016/0010-0285(80)90005-5)
