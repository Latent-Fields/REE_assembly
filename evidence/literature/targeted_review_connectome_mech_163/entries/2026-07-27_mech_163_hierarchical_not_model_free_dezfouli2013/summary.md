# Habits need not be model-free (Dezfouli & Balleine 2013) — the MECH-163 half

**Claim tested:** MECH-163 (dual_goal_directed_systems)
**Direction:** weakens, scoped to the `model-free` conjunct · **Confidence:** 0.72

This is the second entry for the same paper. The first sits in
`targeted_review_connectome_mech_323` and reads `supports` at 0.78. Two entries rather than
one because the direction genuinely differs by claim and a single `evidence_direction` field
cannot carry both honestly — and because the `failure_signatures` prose in which the tension
was originally parked is not read by the indexer for claim attribution, so it counted for
nothing until it was written here.

## What the paper does to this claim

The standard dual-system story has a model-based goal-directed controller and a model-free
habit controller that caches action values, with some external arbitrator choosing between
them on a given trial. Dezfouli and Balleine test that flat architecture against a
hierarchical rival in which there is no second controller at all: habits are chunked action
sequences, and one goal-directed process selects between individual actions and habitual
sequences. Bayesian model comparison over model *families* favours the hierarchical family,
and the authors conclude that model-free RL is **unnecessary** to explain habitual action.

MECH-163 characterises its habit pathway as *"(SNc/dorsal-striatum, model-free)"*. That is
the object the paper argues is not needed.

## Why the weakening is narrow, and why it is nonetheless real

It touches one conjunct. The paper does not argue against two dissociable pathways, and it
says nothing at all about novel-context recruitment — the proposition `V3-EXQ-786b` weakened
independently on 2026-07-24. Read this entry as pressure on a descriptor, not on the claim's
architecture.

But the pressure is not merely literary, because the substrate agrees with the paper. There
is **no model-free machinery in REE**: `ree-v3/ree_core/` returns zero hits for `model_free`,
`q_value`, `q_table`, `td_error` or `sarsa`. What SD-081 actually built as the habit pathway
is `_score_depth_limit = max(2, dualsystem_habit_depth)` — the *same* model-based E3 scorer,
called on a `z_world` sequence truncated to its first two steps. Both of MECH-163's "two
systems" are one model read at two grains. The descriptor was never true of the build.

## The part that must be read with the direction

REE not only lacks the controller the paper argues against; it already implements the
architecture the paper argues *for*. ARC-071 chunks are spliced into the ARC-007 proposal
pool as atomic value-flat trajectories, the E3 selector has no chunk-awareness and scores a
chunk exactly as it scores a primitive, and a selected chunk is then committed atomically and
stepped through by `_committed_step_idx`. That is Dezfouli and Balleine's hierarchy, in the
build, since 2026-07-22.

So a reader who takes `weakens` at face value without the `mapping_caveat` will conclude the
substrate was refuted. The opposite is the case, and this is the one place in the entry where
getting it backwards has real consequences. The weakening is against MECH-163's
*pre-restatement wording*; the restatement it motivated (strike `model-free`, replace with the
depth-limited read) landed the same day, and the claim's own note records that ordering.

There is a corollary worth carrying: `V3-EXQ-811a`'s PASS shows that *depth*-arbitration
produces the differential-recruitment signature. It is not evidence for a cached-value second
system, and citing it as such would over-read it.

## The second-order consequence, which is already realised in code

If apparent outcome-insensitivity is a consequence of sequence *grain* rather than of a
separate insensitive controller, then the points at which goal-directed control can act are
the chunk boundaries. REE's committed trajectories can be released mid-execution by exactly
five mechanisms — MECH-091 (acute harm), MECH-342 (degraded execution readiness), the rung-6
natural-commit duration lever together with SD-033e frontopolar pressure, MECH-321/ARC-070
(prediction failure on the remaining macro), and SD-034 closure de-commit. **None of them
reads whether the committed outcome is still valuable.**

A committed chunk therefore runs to completion regardless of devaluation. Outcome-insensitivity
is already structural in REE, produced by grain, with no model-free controller anywhere — which
makes MECH-323's chunk-size budget quietly a controllability parameter, and makes the failure
present as insensitivity while reporting nothing at the accumulator.

## Where the mapping breaks

Single two-stage decision paradigm, abstract choices, a long way from motor grain or REE's
policy-primitive grain. The authors are explicit that the result does not rule out all possible
model-free accounts, and the load-bearing content here is that negative claim, which is a
weaker inferential step than the positive architectural relation the MECH-323 entry borrows.
Mapping fidelity is set at 0.74 against that entry's 0.80 for exactly this reason, and transfer
risk at 0.30 rather than 0.25: the paper's `model-free` target and REE's depth-limited read are
not the same object.

## Confidence reasoning

0.72. Source quality 0.82, carried over unchanged — same paper, same venue, same formal model
comparison over families, same discount for single-paradigm evidence. Mapping fidelity 0.74 and
transfer risk 0.30 as above. Comfortable treating this as sufficient to restate a descriptor
that the substrate independently contradicts; not comfortable treating it as evidence against
REE's two-grain architecture, which is a different proposition that this paper supports.

**Routes to:** `evidence/planning/claim_synthesis_MECH-163_2026-07-27.md` (§2, §3).
