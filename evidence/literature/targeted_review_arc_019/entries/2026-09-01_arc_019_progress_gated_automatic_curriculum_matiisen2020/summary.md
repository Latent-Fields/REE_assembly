# Matiisen, Oliver, Cohen & Schulman (2020) -- Teacher-Student Curriculum Learning

**Claim tested:** ARC-019 | **Direction:** supports | **Confidence:** 0.63

## What the paper did

TSCL frames curriculum construction as a two-agent problem. A Student learns a complex task; a
Teacher, at each step, picks which sub-task from a given set the Student should train on next. The
Teacher's heuristic is that the Student should practise most where it is improving fastest -- where
the slope of the learning curve is steepest. Crucially, the family of Teacher algorithms also
tracks *negative* slope: sub-tasks on which the Student's performance is degrading get re-selected,
which is how the method handles catastrophic forgetting rather than marching monotonically forward.

They evaluate on two settings with very different character: decimal addition with an LSTM, and
navigation in Minecraft. TSCL matches or surpasses hand-crafted curricula in both, and solves
instances that uniform sub-task sampling does not solve at all.

## Why this bears on ARC-019

Of the five papers here, this is the closest mechanistic analogue to what ARC-019 actually commits
to. Elman and Rohde & Plaut manipulate input complexity on a fixed schedule; Wu et al. manipulate
example ordering in a supervised problem. TSCL is the only one where progression through phases is
*gated on a measured competence signal in a sequential decision problem* -- which is exactly the
shape of REE's InfantCurriculumScheduler holding an agent on a phase until the DEV-NEED-008
criteria are met. It is direct support for the general form of the commitment: criterion-driven
progression through sub-tasks is architecturally productive, not merely organisational.

It also carries a suggestion REE should take seriously. TSCL's gate is *adaptive* -- derived from
the learning curve at run time -- and it matches hand-crafted curricula, meaning the hand-crafted
schedule bought nothing over a signal the learner generates itself. REE's fixed 7-criterion gate is
a hand-crafted schedule in this taxonomy. If ARC-019's staged arm ever comes back null, the
learning-progress framing supplies an immediate alternative hypothesis: the staging was right and
the *criteria* were wrong. Those two failure modes are not distinguishable by the current
staged-vs-flat design.

## The caveat that caps this entry

TSCL's headline comparisons are strongest exactly where the ungated baseline fails outright. That
is the V3-EXQ-591 degenerate-comparison problem in mirror image -- it demonstrates that a curriculum
is *necessary for traversal*, which ARC-019 explicitly treats as a precondition to be independently
verified rather than as the finding. The paper does not report a matched-total-budget flat control
that succeeds and is merely beaten, which is the comparison ARC-019's CONFIRMING branch actually
requires. So this supports the architectural form of the claim while leaving its quantitative
version untested.

Two further gaps. TSCL's sub-tasks are an enumerated set with a designer-supplied decomposition and
a dense per-task score, where REE's phases are stages of one continuous embodied environment and the
gate criteria are themselves under test. And the Minecraft result, while the more REE-like of the
two, is a single environment family -- ARC-019's CONFIRMING branch asks for reproduction across at
least one additional curriculum-bearing lineage, and one paper cannot supply that.

## Confidence reasoning

`source_quality` 0.75 -- peer-reviewed journal version of a well-cited line of work, with a clear
algorithm family and honest reporting, though the empirical scope is two task families.
`mapping_fidelity` 0.70, the highest in this pull, because the mechanism really is criterion-gated
phase advance in a sequential learner. `transfer_risk` 0.45, the lowest here, for the same reason.
Aggregate 0.63 rather than higher: held down by the degenerate-baseline issue, which is the single
most important thing to carry forward from this paper into any REE experiment that tests ARC-019.
