# Thought intake: fast empathy BOOTSTRAPS cognitive empathy; the object stage is two things at once

**Date:** 2026-09-18 (raw + intake same day)
**Status:** intake / **REGISTERED** -- MECH-569, MECH-570, MECH-571 (2026-09-18)
**Raw thought file:** `docs/thoughts/2026-09-18_fast_empathy_bootstraps_cognitive_empathy.md`
**Predecessor intake:** `evidence/planning/thought_intake_2026-05-04_fast_empathy_stream_binding.md`
(this is its successor, not a replacement -- that intake's candidates are all registered:
ARC-094, ARC-095, MECH-405, MECH-406, MECH-407, MECH-408, Q-073)
**Plan of record:** `evidence/planning/fast_empathy_v5_plan.md` (node **EMP-7**, the grounding-debt
lit-pull, is partially discharged by this work)
**Evidence landed:** REE_assembly `f2af0b691f2` (targeted_review_connectome_arc_094,
targeted_review_arc_089) and `046eaaac236` (targeted_review_self_object_other_ontogeny)

---

## 1. Origin

The `ree-lit-pull-am-b` scheduled pull selected ARC-089 and ARC-094 (both Tier 1, zero prior
coverage). The ARC-094 pull returned an apparent problem: Krishnan et al. 2016 shows somatic and
vicarious pain multivariate patterns cross-predict at **chance** against 100% within-condition.
Reported as a challenge to ARC-094's constructive mechanism. The user's response reframed it:

> "I had always thought the fast empathy system might bootstrap higher cognitive empathy."

and, on which sense of "object" `self -> object -> other` intends: **"Both, deliberately."**

## 2. The correction that drives everything else

**The apparent falsification was an artefact of reading ARC-094 as a RUNTIME claim.**

| Reading | What it says | Krishnan 2016 verdict |
|---|---|---|
| Runtime (concurrent composition) | a mature empathic response is computed by routing through the self's own affective code | **falsified for pain** -- the codes share no content |
| Developmental (temporal scaffolding) | the fast affective route SEEDS the slower mentalizing route, which then differentiates | **predicted** -- mature dissociation is what a scaffold produces |

ARC-094's wording -- "binding existing motivational-affective streams" -- reads as concurrent
composition. The intended meaning is scaffolding. **The defect is wording, not substance.**

Corroboration that both routes persist rather than one replacing the other: Lamm/Decety/Singer
2011 route-dependence -- picture cues recruit somatosensory and action-understanding areas,
abstract cues recruit mentalizing. Two routes, different latencies, both live in the adult.
That is the structure "fast empathy" presupposes.

**Scope honesty:** the corpus does not actually test the bootstrapping claim. Laboratory
vicarious-pain paradigms use images and video with processing time, which plausibly probe the
slow cognitive route only. The fast route is largely unmeasured here.

## 3. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Fast empathy is stream-binding, not a module/scalar | **Yes** -- ARC-094 (the prohibition), MECH-405 (the mechanism) | Confirms -- and the prohibition is now over-determined (see 4) |
| Developmental ordering of other-bound streams | **Yes** -- MECH-408, Q-073 | Confirms; and MECH-408 gains its first literature evidence (see 5) |
| Fast route SCAFFOLDS the cognitive route; adult dissociation is the predicted endpoint | **No** -- MECH-405 states the mechanism with no developmental commitment | **NOVEL** -> **MECH-569** |
| The SELF stage is not primitive as self-KNOWLEDGE; affect self-access is socially acquired | **No** -- ARC-059 and INV-064 both assume a self stage available to be extended | **NOVEL, and a load-bearing biology-vs-design divergence** -> **MECH-570** |
| The OBJECT term is route-specific, not universal | **No** -- `self -> object -> other` is written as one obligatory pipeline | **NOVEL** -> **MECH-571** |
| "Object" means both the cognitive/developmental and the object-relations object | **Implicit** -- never stated | Captured in MECH-571's notes (user-confirmed intent) |

## 4. The prohibition is over-determined -- four independent routes to it

Worth recording because it changes ARC-094's status from "argued" to "hard to avoid":

1. **Shared-network** (Lamm 2011): empathy for pain recruits AI/aMCC shared with first-hand pain -- no dedicated empathy region.
2. **Route-dependence** (Lamm 2011): the network recruited shifts with how the other's state is conveyed -- a module emitting a scalar would not do this.
3. **Content fractionation** (Zhang 2025, 35-study ALE): physical vs social pain empathy show **no shared activated areas** -- a single `empathy_score` would summarise two non-overlapping systems and denote no implemented quantity.
4. **Decoupled secondary representations** (Gergely & Watson 1996): representing another's affect requires a representation decoupled from the primary state; a scalar collapses exactly that decoupling.

Four methods, four partitions, one conclusion. (3) rests on a thresholded null and is the weakest.

## 5. Affected existing claims

- **ARC-094** -- reword from concurrent binding to temporal scaffolding. **Governance action, not done here.**
- **MECH-405** -- presupposes accessible own-affect streams; MECH-570 questions that starting condition.
- **MECH-408** -- **first literature evidence landed.** `2026-09-18_arc_094_social_referencing_visual_cliff_moller2014` was retagged (it had named only ARC-094). Moller et al. 2014: paternal expressed **anxiety** predicted infant anxiety and avoidance; parental **encouragement** predicted neither, gated by infant temperament. An other-bound protective stream functions as a behaviour-altering input while an other-bound appetitive stream does not -- same infants, same paradigm, same session, so the asymmetry is not cross-study measurement sensitivity. **Caveat: cross-sectional at 10-15 months, so consistent with protective-before-appetitive but not a measurement of the ordering.**
- **Q-073** (why protective before appetitive) -- untouched; Moller does not test the reason.
- **ARC-059 / INV-064** -- MECH-570 amends the spine at the level of self-knowledge while preserving it at substrate level.
- **ARC-089** (same morning pull, unrelated cluster) -- ~5 of 9 cognifold primitives have demonstrated physical affordances; the three distinctive ones (residue-as-action-landscape-deformation, commitment boundary, offline reintegration) are unaddressed by the hardware literature. Also: reservoir computing's fading-memory criterion pulls **against** REE's persistence/residue primitives, so the primitive vocabulary must not be modelled on RC's list.

## 6. Candidate claims -- REGISTERED 2026-09-18

| id | type | one line |
|---|---|---|
| **MECH-569** | mechanism_hypothesis | fast empathy bootstraps cognitive empathy; adult dissociation is the predicted endpoint |
| **MECH-570** | mechanism_hypothesis | affect self-access is socially acquired via marked mirroring (other -> self) |
| **MECH-571** | mechanism_hypothesis | the object term is route-specific (constitutive of the mirror route, absent from the bodily-correspondence route) |

All three: `status: candidate`, `epistemic_category: substrate_conditional` (explicit),
`implementation_phase: v5`, `v3_pending: true`, `version_relevance: v4_v5`,
`location: evidence/planning/fast_empathy_v5_plan.md`. Each carries its falsifier and its
caveats in `notes`. **None licenses a build. DO NOT build in V3.**

## 7. Next steps (gated)

1. **Governance:** reword ARC-094 (scaffolding, not concurrent binding). The only change to an already-registered claim this intake proposes; deliberately not hand-applied.
2. **EMP-7 is PARTIALLY discharged, not closed.** Its three commissioned topics: *mirror/PAM substrate for other-bound affect* -- **covered**; *developmental ordering of empathic concern vs prosocial reward* -- **partly covered** (Moller 2014 here, plus the three existing `targeted_review_q_073` entries incl. Davidov 2020 "concern before prosocial"); *reciprocity intrinsic-reward maturation* -- **NOT covered** (Wu et al. 2026 remains a seed anchor with no pull). A further lit-pull on reciprocity intrinsic-reward maturation is the remaining debt.
3. **The genuinely open design question** MECH-571 hands V5: which route carries FAST empathy specifically. The corpus does not answer it, and the Umilta/Meltzoff disagreement is real rather than a matter of emphasis.
4. **A falsifier for MECH-569 needs developmental or lesion evidence** that cognitive empathy can be acquired without the fast route. Not in this corpus; a candidate lit-pull target.
5. Everything here is V5 social tier, gated behind MECH-163 + V4 substrate per DEV-NEED-021. No V3 work is implied or unblocked.

## 8. Cross-references

- Raw: `docs/thoughts/2026-09-18_fast_empathy_bootstraps_cognitive_empathy.md`
- Predecessor: `thought_intake_2026-05-04_fast_empathy_stream_binding.md`
- Plan: `fast_empathy_v5_plan.md` (EMP-1..EMP-7; this touches EMP-6 and EMP-7)
- Literature: `targeted_review_self_object_other_ontogeny` (4), `targeted_review_connectome_arc_094` (3), `targeted_review_arc_089` (3), `targeted_review_q_073` (3, pre-existing)
- Claims: ARC-094, ARC-095, MECH-405, MECH-406, MECH-407, MECH-408, Q-073, ARC-059, INV-064, ARC-010, SD-011, MECH-112; new MECH-569, MECH-570, MECH-571
- Memory: `feedback_thought_intake_must_register_claims`, `feedback_biology_before_formal_definitions`, `project_object_representation_thread`
