# Smith, Jayaraman, Clerkin & Yu (2018) -- The Developing Infant Creates a Curriculum for Statistical Learning

**Claim tested:** ARC-019 | **Direction:** supports | **Confidence:** 0.52

## What the paper did

Smith and colleagues review a body of head-camera and eye-tracking work on what infants actually
see, from the infant's own point of view, across the first two years. The empirical picture is
consistent and somewhat striking: the visual input is not a stationary sample of the world. At each
developmental timepoint it is extremely selective -- dominated by a small number of faces early,
then by hands and held objects, then by a distributionally skewed set of object instances -- and
the content shifts systematically as the infant's sensorimotor capabilities change. Head control
changes what is in frame; reaching changes what is central and large; locomotion changes the scene
statistics entirely. The result is a sequence of ordered, narrow, highly structured training sets,
each one apparently well-matched to what can be learned from it at that moment.

Their framing is that the infant is not being taught a curriculum but *generating* one, as a
side-effect of a body that is itself changing.

## Why this bears on ARC-019

REE's design principle is to follow biological construction where feasible, and this is the best
available statement of the biological fact ARC-019 is modelled on. It establishes that natural
learners in fact face a staged, ordered input distribution rather than the full adult problem from
birth, and that the ordering is not accidental -- it is tightly coupled to what the learner can do.
That is real support for the premise underneath ARC-019: an agent trained on the full task
distribution from step zero is not the biologically-motivated design.

## The part that cuts the other way

I want to be careful here, because this entry is easy to over-read and the direction it actually
points is more interesting than a bare "supports".

The curriculum in this work is *emergent*, not *gated*. Nowhere in the infant's development is
there a criterion test that says "phase 1 complete, enable phase 2 features". The ordering falls
out of a maturing body interacting with a fixed world. If that is the mechanism -- and this paper
argues it fairly directly -- then the architecturally load-bearing thing is the *embodiment
constraint*, and REE's explicit gates are a proxy for it. A substrate that implemented the
constraint directly (limited early motor repertoire, limited sensory acuity, limited memory span)
would produce the staging for free and would make the InfantCurriculumScheduler's criterion gates
redundant. That is a genuinely different architecture from the one ARC-019 commits to, and this
paper is arguably better evidence for it than for ARC-019 as written.

There is also no causal arm anywhere in this literature. Nothing here shows that an infant somehow
given adult-like input from birth learns worse -- the manipulation is unavailable for obvious
reasons. So this cannot discriminate ARC-019's CONFIRMING branch from its FALSIFYING branch; it
speaks only to whether the ordering exists, not to whether it is doing work. And the budget
mismatch is total: human visual development runs on millions of waking seconds, where ARC-019's
falsifier is defined over a matched *episode budget* in the low thousands. "Matched total budget"
has no counterpart in this data at all.

## Confidence reasoning

`source_quality` 0.80 -- authoritative review in a strong venue, grounded in first-person corpora
that were genuinely hard to collect and that changed the field's picture of the input problem.
`mapping_fidelity` 0.45 -- the paper documents that a curriculum exists; ARC-019 claims a specific
gating mechanism is load-bearing, and the paper's own account of the mechanism (emergent from
embodiment) is not that one. `transfer_risk` 0.55 -- human infant vision to an embodied RL agent,
across an enormous budget gap. Aggregate 0.52, weighted hard toward mapping fidelity because
ARC-019 is an architectural commitment and this source cannot reach the architecture. Included
anyway, and deliberately: it is the strongest statement of the biological premise, and the
competitor architecture it implies is worth having on the governance record rather than discovered
later.
