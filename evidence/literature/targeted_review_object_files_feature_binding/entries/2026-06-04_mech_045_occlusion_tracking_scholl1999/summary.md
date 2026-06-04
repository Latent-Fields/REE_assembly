# Tracking items through occlusion: clues to visual objecthood (Scholl & Pylyshyn 1999)

**Claims:** MECH-045 (across-time/motion persistence) | **Direction:** supports | **Confidence:** 0.77

## What the paper did

This is the paper that most directly addresses the gap the object-representation memo
flags -- persistence of a *particular instance* across a perceptual gap. Scholl and Pylyshyn
ran three multiple-object-tracking experiments in which the tracked items did not merely
move but periodically *disappeared*. The decisive manipulation was *how* they disappeared.
In the occlusion conditions, items passed behind (invisible) occluding surfaces, vanishing
and reappearing with accretion and deletion cues along a fixed contour -- the gradual
wipe-on/wipe-off that signals a surface passing in front. In the matched non-occlusion
conditions, items disappeared for the same durations and to the same degree, but by
"imploding and exploding" -- shrinking out of and popping back into existence -- with no
occluding-contour cues. Tracking was *unimpaired* by complete occlusion when the
accretion/deletion cues were present, but *impaired* when items disappeared in the
non-occlusion ways. The conclusion: the visual system computes enduring objecthood from
spatiotemporal continuity cues, and when those cues say "this object went behind something,"
it treats the reappearing item as the *same persisting token*.

## Why it matters for the claim

MECH-045 asserts object-file-like buffers that "bind features across time and motion" to
provide "minimal entity persistence across time." This paper exhibits the strongest version
of that persistence -- a token surviving a *total* perceptual gap -- and pins down its
trigger. Persistence is not driven by continuous visibility; it is driven by continuity
*cues*. This is exactly the "this object tracked through occlusion" capability the memo
identifies as the **token-vs-type gap**. REE's live object machinery (SD-015 `z_resource`,
SD-049 type tag, SD-057 `z_object`) is a *type-level* representation: it can say "there is
food here" but it cannot track *this particular* instance through a gap and re-identify it
as the same one on the far side. An object-file buffer in the MECH-045 sense is precisely
the thing that can. So this entry does double duty: it grounds MECH-045's persistence clause
in biology, and it gives the design fork a concrete behavioural target -- the buffer must
re-bind a reappearing token to its pre-gap file when continuity cues warrant, and must *not*
when they do not.

## The mapping and its boundaries

The most important caveat is that persistence here is **conditional**, not automatic. The
visual system persists a token through occlusion only when the disappearance carries the
right cues; when it does not, the token is treated as gone. That is a constraint, not just a
capability: a REE object-file buffer that persisted tokens on *any* temporary absence would
over-generalise beyond what the visual system actually does, and would mis-merge genuinely
new objects with old files. The second caveat is that the paper characterises the
*triggering cues* (accretion/deletion at an occluding contour) rather than an implementable
buffer mechanism -- REE still has to choose a representation that consumes continuity cues,
and a foraging agent's "occlusion" is a different sensory regime from abstract dots on a
screen, so the transfer is non-trivial. This paper is best read as the bridge between this
object-files pull and the planned L2 object-permanence pull (Baillargeon/Spelke): it is the
adult-attention end of the same continuity-driven persistence the infant-cognition
literature studies developmentally.

## Confidence

Confidence 0.77. The mapping onto MECH-045's across-time-and-motion persistence clause is
high, and the result is exactly on the memo's flagged gap. It is held below the top band
because it specifies *which cues* license persistence rather than a mechanism REE can lift
directly, because persistence is cue-conditional (a constraint REE must honour), and because
of the usual human-psychophysics-to-agent transfer risk.

Source: [Scholl & Pylyshyn 1999, Cognitive Psychology 38(2):259-290](https://doi.org/10.1006/cogp.1998.0698) ([PubMed 10090804](https://pubmed.ncbi.nlm.nih.gov/10090804/))
