# Object files: object-specific integration of information (Kahneman, Treisman & Gibbs 1992)

**Claims:** MECH-045 (primary), ARC-006 (secondary) | **Direction:** supports | **Confidence:** 0.82

## What the paper did

Across seven experiments (203 participants), Kahneman, Treisman and Gibbs studied what
they called *object reviewing*. A preview field showed letters inside framed boxes; the
boxes then moved, and a target letter appeared in one of them to be named. The crucial
manipulation was whether the target was perceived as a *new state of the same object* that
had earlier contained a matching letter, versus a letter that had appeared in a different
object. Naming was reliably faster in the former case -- the *object-specific preview
benefit* -- even though the matching letter had physically moved across the screen. The
benefit tracked the object's perceived spatiotemporal continuity, not its retinal location
and not its semantic identity. They proposed the **object file**: a temporary episodic
representation that is opened when an object is individuated, addressed by the object's
continuity through space and time, and updated as the object changes state.

## Why it matters for the claim

MECH-045 asserts that "object-file-like buffers provide minimal entity persistence across
time" -- and it borrows the term directly from this paper. So this is not a loose analogy:
it is the source construct. The object file is precisely a *minimal* persistence mechanism:
it carries an object's recent history without requiring a symbolic label, it binds features
to a continuing entity rather than to a location, and it is the structure that lets the
visual system answer "is this the same thing I saw a moment ago?". That is exactly the
function MECH-045 wants a REE buffer to perform. It also speaks to ARC-006's clause that
entities are "persistent, bindable structures": the object file *is* the persistent
bindable structure, and the preview benefit is the empirical signature that such a
structure exists and survives motion.

## The mapping -- and the fork it exposes

The honest caveat is the one the object-representation memo predicted. The biological
object file is strictly **token-instance**: it is *this* apple tracked through *this* motion
episode, indexed by continuity, not "apples" as a category. REE's live object machinery
(SD-015 `z_resource`, SD-049 type tags, SD-057 `IncentiveTokenBank`) is **type-level** and
**tag-indexed** -- a location-invariant embedding of a resource *category*. So this paper
grounds the representation MECH-045 *describes* while simultaneously marking the design
fork: to honour the object-file construct, REE would have to add a token-keyed,
continuity-gated buffer, not reuse the existing type-tag store. The preview benefit's
fragility is itself informative -- it collapses when spatiotemporal continuity cues are
removed, which tells us a REE object-file buffer cannot be a free-floating key-value store;
its persistence must be *gated on a continuity computation* that REE does not currently run.

## Limitations and confidence

This is human visual psychophysics over short preview-target intervals with a single
reviewed object, so it establishes the buffer's existence and its continuity-indexing but
not its capacity (how many concurrent files) or its behaviour across long occlusions -- the
Pylyshyn & Storm and Scholl & Pylyshyn entries cover those. Transferring a psychophysical
construct into a latent-stack agent is non-trivial. I set confidence at 0.82: high because
the construct maps near-verbatim and the evidence is landmark and heavily replicated,
discounted from the top band by the token-vs-type mismatch and the human-to-agent transfer
risk. Read together with the binding-theory entries, the conclusion is that MECH-045 is
*well-motivated by biology* but currently *unimplemented* in the form biology describes.

Source: [Kahneman, Treisman & Gibbs 1992, Cognitive Psychology 24:175-219](https://doi.org/10.1016/0010-0285(92)90007-O) ([PubMed 1582172](https://pubmed.ncbi.nlm.nih.gov/1582172/))
