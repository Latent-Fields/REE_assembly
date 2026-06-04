# Visual indexing and multiple-object tracking (Pylyshyn & Storm 1988)

**Claims:** ARC-006 (sparse + persistent clauses), MECH-045 (individuation prerequisite) | **Direction:** supports | **Confidence:** 0.72

## What the paper did

Pylyshyn and Storm showed observers a field of ten identical dots, designated a subset of
four or five as targets, then set all ten moving independently and unpredictably. After the
motion stopped, observers had to say which items were the targets, or detect a change on a
target versus a distractor. People did this strikingly well -- around 87% accurate -- even
though the items were physically indistinguishable and their paths crossed and tangled. A
serial algorithm that tries to update each target's stored location in turn manages only
about 30%. The gap led Pylyshyn to propose **visual indexing theory** (the FINST model,
for "FINgers of INSTantiation"): a small set of pre-attentive pointers that individuate a
handful of objects and *stick to them* through motion, in parallel, without encoding the
objects' features or their trajectories. The index is a primitive demonstrative -- it marks
*that thing* and keeps marking it as it moves -- prior to and independent of knowing what
the thing is.

## Why it matters for the claim

ARC-006 says entities are "sparse, persistent, bindable structures." This paper supplies
direct empirical grounding for the first two of those three adjectives. *Sparse*: tracking
has a hard, small capacity (roughly four to five), which is exactly the kind of bounded,
slot-like limit ARC-006 attributes to entities. *Persistent*: the index maintains the same
token across motion and occlusion of identity -- the pointer survives even when the item is
visually identical to its distractors. For MECH-045 the contribution is upstream but
essential: before you can persist an object's *features* in an object file, you must first
individuate the object and attach a pointer to it. Visual indexing is that individuation
step. It establishes that the visual system has a mechanism for "this is one persisting
thing" that runs before any feature or label is bound -- which is precisely the foundation
an object-file buffer sits on.

## The mapping and its boundaries

The sharp limitation is also what makes the paper useful: the tracked items are *featureless
identical dots*. That isolates pure individuation-plus-tracking and is, by design, silent on
feature *binding*. So this entry grounds ARC-006's sparse-and-persistent-token clauses but
cannot speak to its bindable-feature-bundle clause -- that is the FIT and object-file
entries' job. Two further caveats matter for a REE implementation. The ~4-5 capacity is a
strong but contested empirical number that depends on speed and spacing; REE should treat it
as evidence for *bounded* individuation, not licence to hard-code a fixed slot count.
And FINST indexes deliberately carry *no* identity or feature content -- they are
demonstratives, not files -- so equating an index with a full object file over-reads the
construct. The correct reading is layered: indexing individuates and persists a pointer;
the object file (Kahneman entry) is what fills that pointer with bound features over time.

## Confidence

Confidence 0.72. The paradigm is foundational and the evidence for bounded, persistent,
feature-blind individuation is robust. It is held in the mid-band because featureless dots
isolate individuation and say nothing about binding, the capacity number is debated, and it
is human psychophysics transferring to a latent-stack agent. Its main value to governance is
structural: it cleanly separates *individuation/persistence* (this paper) from *binding*
(FIT) from *file contents* (Kahneman), which is the decomposition a REE object layer would
need to respect.

Source: [Pylyshyn & Storm 1988, Spatial Vision 3(3):179-197](https://doi.org/10.1163/156856888X00122) ([PDF](https://ruccs.rutgers.edu/images/personal-zenon-pylyshyn/docs/storm88.pdf))
