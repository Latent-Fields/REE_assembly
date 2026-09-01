# Elman (1993) -- Learning and development in neural networks: the importance of starting small

**Claim tested:** ARC-019 (REE requires staged developmental training with explicit curriculum gates)
**Direction:** supports | **Confidence:** 0.45

## What the paper did

Elman trained simple recurrent networks to predict the next word in sentences drawn from an
artificial English-like grammar containing long-distance agreement dependencies across embedded
relative clauses. Trained on the full-complexity corpus from the outset, the network never reached
acceptable prediction accuracy. Two manipulations rescued it. In the first, the *input* was staged:
the network saw only simple sentences initially, with complex embeddings phased in. In the second
-- the more interesting one, and the one usually cited -- the input was left at full complexity and
instead the network's own working memory was crippled at the start and allowed to mature, its
recurrent context being cleared frequently early in training and less often later. Both produced
successful acquisition where the unstaged network had failed.

## Why this bears on ARC-019

This is the ancestor of the position ARC-019 encodes. Elman's conclusion was not that staging is
convenient but that maturational constraint is *enabling* -- that a learner starting with adult
capacity is worse off than one that grows into it, because early limitation forces the extraction
of coarse structure that later serves as scaffolding. REE's InfantCurriculumScheduler with
phase-advance gates on the DEV-NEED-008 criteria is the engineered version of the same bet, with
the addition that REE's gates are keyed on measured competence rather than on a schedule.

The second manipulation is the one worth holding onto, because it is subtly different from what
REE does. Elman staged the *learner*, not the *task*. REE's phases stage the environment and the
feature set. If Elman's mechanism is the real one, then REE's route to the same benefit would be
maturational constraint on the substrate -- limited memory, limited z-dimensionality early -- and
not phase gating on environmental features at all.

## Limitations, honestly

Three, and together they are why this entry sits below 0.5.

First, the comparison is degenerate in exactly the way ARC-019's own non-degeneracy precondition
warns about. The unstaged control did not underperform; it failed outright. That establishes
"curriculum enables traversal", not "curriculum improves outcome at matched budget", and REE has
already been burned by this distinction once -- V3-EXQ-591 (2026-05-27) produced a
substrate-ceiling non-result of precisely this shape when all arms plateaued at 1/7 criteria.

Second, the total training budget was not equalised across arms in the way ARC-019's falsifier
requires. A staged arm that sees simple sentences for many epochs before complex ones has had a
different amount of exposure to the hard cases than a flat arm at the same total step count.

Third, and decisively for how much weight this deserves: the result did not survive replication.
Rohde and Plaut (1999), whose entry sits alongside this one, ran a substantially broader sweep and
found not merely no advantage to starting small but an active cost that grew with the realism of
the language. Elman remains the canonical statement of the position; it is not, on the current
record, a secure empirical foundation for it.

## Confidence reasoning

`source_quality` 0.60 -- highly influential and carefully argued, but one simulation study, one
grammar, no in-paper replication, and contradicted six years later. `mapping_fidelity` 0.65 --
staged development is genuinely the same architectural family, but Elman's gate is capacity, not a
competence criterion. `transfer_risk` 0.55 -- next-word prediction in a small SRN with no reward,
no body and no policy, generalised to an embodied developmental agent. Aggregate 0.45, weighted
toward mapping fidelity because ARC-019 is an architectural commitment rather than an empirical
prediction, and pulled down further by the replication failure, which is a property of the
evidence rather than of any single component.
