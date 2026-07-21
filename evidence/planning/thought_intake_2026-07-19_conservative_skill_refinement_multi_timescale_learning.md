# Thought Intake — Conservative skill refinement and multi-timescale learning in REE

**Date of thought:** 2026-07-19
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-19_conservative_skill_refinement_and_multi_timescale_learning.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Source:** Microsoft SkillOpt — *Executive Strategy for Self-Evolving Agent Skills*
**Scope:** **REE cognitive architecture only.** The Assembly-facing half of this source is a separate thought and a separate intake — see `thought_intake_2026-07-19_bounded_knowledge_artifact_optimisation_assembly.md`. Keep the two apart; conflating them is the specific failure this pair of thoughts was split to avoid.
**Status:** structured intake written; candidate claims NOT yet registered (concurrent session held the `claims.yaml` claim).
**Promotes/demotes:** nothing.

## Authorship note

The raw thought is the user's, including the correct-and-load-bearing scope decision: **SkillOpt is a neighbouring implementation strategy, not an architectural template.** A "skill" in REE is not a document — it is distributed across action objects, learned affordances, predictive models, hippocampal trajectories, goal-conditioned policies, rule-state persistence, control settings, and residue-shaped avoidance/repair tendencies. Text-space skill optimisation is not embodied cognitive learning.

## The question this refines

> How should REE refine behavioural competence without erasing previously viable structure or allowing one recent success to rewrite the whole agent?

## Already owned — cross-reference, do NOT re-assert

The raw thought judges the principles "broadly compatible with existing REE commitments." Confirmed, and more strongly than the thought claims — three of its six principles are already *registered claims*:

| Principle in the thought | Existing claim(s) |
|---|---|
| 4. Multiple learning rates / multi-timescale | **SD-006** (characteristic rates, async multi-rate), **ARC-023**, **MECH-058** (slow target-anchor dynamics stabilise E1/E2 via functional rate separation), **MECH-291** (waking vs quiescent parameter profiles) |
| 3. Protection against catastrophic overwrite | **INV-080** (raw-episode preservation: consolidation output MUST NOT replace source-episode evidence), **MECH-401** (consolidation gated-write authority; over-frequent rewriting is a named failure mode), **INV-004/INV-006** (residue persistent, non-erasable) |
| 1. Bounded refinement (local, attributable, inspectable) | **MECH-392** (consolidation provenance + contradiction-flag + **rollback**) — this is bounded, attributable, reversible editing, already registered for the consolidation path |
| Event-/mode-conditioned plasticity | **MECH-261** (mode-conditioned write gating), **MECH-083** (ACh as meta-level plasticity gain governing durable-write vs read-through), **MECH-207**, **Q-072** (does plasticity gain modulate identically across layers) |
| Offline integration as a distinct learning regime | **MECH-018**, **MECH-030**, **MECH-121**, **MECH-275**, **MECH-252**, **SD-017** |
| Licit vs illicit learning from simulation | **ARC-092** (imagination-learning constraint principle: simulated experience may license only LICIT forms of update) |
| Anti-collapse via partially independent controllers | **MECH-063**, **MECH-069**, **ARC-025** |
| Practice-maturity-weighted arbitration between learning systems | **MECH-312b**, **MECH-312c**, **MECH-163** (habit vs goal-directed systems in parallel) |

So principles 1, 3 and 4 are **already REE commitments** — for the consolidation and residue paths specifically. Registering them again would duplicate and contaminate evidence records. The correct move is a cross-reference plus, where the scope differs, a *generalisation* claim (see N1).

## Genuinely new — four things

### N1. The bounded-edit / provenance / rollback discipline exists for CONSOLIDATION but not for SKILL

MECH-392, INV-080 and MECH-401 give the memory-consolidation path exactly the properties the thought asks for: bounded, attributable, provenance-carrying, rollback-capable, gated against over-frequent rewrite. **Nothing equivalent is registered for behavioural competence** — policy/affordance/action-object learning has no rollback, no provenance record, and no gate against a single successful rollout propagating widely.

That asymmetry is the genuinely new observation, and it is a *specific* gap rather than a general aspiration. It also states its own falsifier: does a local competence update degrade unrelated competences?

### N2. Rejected-change memory as a learning structure

> A failed adaptation should remain available as evidence about what was tried, why it failed, and under what conditions it might later become useful.

Nothing in REE retains *rejected* adaptations. Residue retains the consequences of **committed** actions (INV-004/006); MECH-392 flags contradictions in consolidated summaries. Neither preserves a **tried-and-rejected behavioural revision** with its failure conditions. This is a new structure, and it has a clean functional prediction: preserving rejected adaptations should improve later recovery/transfer when conditions change — which is testable and could equally come out negative (the null: rejected-change memory is dead weight that slows adaptation).

Note the honest framing: this is a *V4+ candidate*, not a V3 build. It presupposes a competence-revision unit that can be identified and stored, which V3 does not have.

### N3. Meta-selection of learning strategy

The control plane choosing *which learning process to apply* — practice, exploration, imitation, counterfactual simulation, offline consolidation, rule apprehension, language-mediated scaffolding — rather than one universal learning rule.

Partial precedent exists (MECH-312b/c arbitrate between habit and goal-directed *control*; MECH-261 gates *which substrate may write* by mode; MECH-179 routes error type to sleep phase). But arbitration over the **learning mechanism itself** across that full menu is not registered. Several of the menu items (imitation, language-mediated scaffolding) are not built at all, so the full claim is substrate-blocked; the *narrow* version over the mechanisms REE does have (practice / exploration / counterfactual simulation / offline consolidation) is a live V3-adjacent question and is the one worth registering.

### N4. Residue must constrain skill optimisation when a behaviour is effective but harmful

The thought's cautions carry the strongest item, and it is not a caution — it is a constraint:

> Performance gain is not sufficient evidence of viability or ethical adequacy. A validated skill may still conflict with commitments, harm constraints, or broader goals.
> Meta-learning itself requires governance so that it cannot optimise away protected structures.

This is the learning-side twin of the distractor-suppression ethical constraint identified in the 2026-07-12 intake: an optimiser that improves competence by attenuating harm sensitivity has *succeeded on its metric and failed as an agent*. It gives the correct acceptance shape for any skill-refinement mechanism: **improvement in competence AND non-degradation of harm sensitivity / residue accumulation / commitment integrity**, measured jointly, never as one score.

## Explicitly NOT proposed

- Text-based skill documents inside REE, or any literal SkillOpt import.
- A new foundational learning mechanism. The thought is explicit that SkillOpt's contribution is "external convergence and a compact optimisation vocabulary."
- Anything on the V3 critical path.

## Candidate claims (for registration at digestion)

1. **Behavioural-competence updates require the same bounded/provenanced/rollback-capable discipline already registered for consolidation.** *Candidate.* Generalises MECH-392 + INV-080 + MECH-401 from the memory path to the policy/affordance/action-object path. *Falsifier:* a local-update interference test — train a targeted competence improvement, then measure performance on unrelated previously-acquired competences. FAIL (i.e. the discipline is needed) if unrelated competence degrades measurably; PASS (not needed) if it does not, across a perturbation range. *Non-degeneracy guard:* the "unrelated" competences must be demonstrably acquired in the baseline (above-floor performance with live cross-seed variance) — testing interference against competences the agent never had is vacuous. *Type:* architectural / mechanism. *Cross-ref:* MECH-392, INV-080, MECH-401, MECH-083, MECH-261, ARC-092.

2. **Held-out context distinguishes skill acquisition from task memorisation.** *Candidate, methodological but testable.* A competence update should be promoted to durable only on evidence from contexts that did not generate it. *Falsifier:* paired in-context vs held-out-context evaluation of the same learned competence; a gap beyond a threshold marks memorisation. *Non-degeneracy guard:* the held-out contexts must be genuinely reachable by the trained policy (non-zero baseline completion) or the gap is a floor artefact. *Cross-ref:* the validation-before-promotion principle; connects to the governance-side held-out-review idea in the Assembly intake, but is a **separate, REE-internal** claim — do not merge.

3. **Rejected-adaptation memory improves later recovery and transfer.** *Candidate, V4+, substrate_conditional.* Retaining failed behavioural revisions with their failure conditions improves adaptation when conditions later change. *Falsifier:* arms with and without a rejected-adaptation store, evaluated on a condition-reversal task. Register at `implementation_phase: v4` with an explicit "DO NOT build in V3" note — V3 has no competence-revision unit to store. *Cross-ref:* INV-004/006 (residue: the committed-consequence analogue), MECH-392 (contradiction flags), N2 above.

4. **Learning-mechanism meta-selection (narrow form).** *Candidate.* The control plane selects among the learning regimes REE actually has — online practice, exploration, counterfactual simulation, offline consolidation — rather than applying one rule universally, and this selection is state-/mode-dependent. *Falsifier:* fixed-regime arms vs a selecting arm on a task mix that rewards different regimes; PASS requires the selector to beat every fixed regime, not just the mean. *Non-degeneracy guard:* the task mix must actually dissociate the regimes — at least two regimes must win on different sub-tasks in the fixed-arm baseline, or there is nothing to select between. *Cross-ref:* MECH-312b/c, MECH-261, MECH-163, MECH-179, ARC-092. Broad form (adding imitation + language-mediated scaffolding) is substrate-blocked; note it, do not register it as testable.

5. **Skill optimisation must not trade harm sensitivity for competence (learning-side ethical constraint).** *Candidate, INV-flavoured.* Any competence-refinement mechanism must be evaluated jointly on competence gain AND non-degradation of harm sensitivity, residue accumulation, and commitment integrity; a mechanism improving the first by attenuating the second is a failure. *Falsifier:* the joint measurement across a refinement-strength sweep. *Cross-ref:* INV-004/006, ARC-092, EXT-009, the ethics perimeter, and the twin constraint in the 2026-07-12 distractor intake (candidate claim 2 there). **These two should be registered as siblings** — they are the same principle on two different control surfaces.

## Routing

- **Nothing here justifies a V3 build.** Candidate 1's interference test is the cheapest real probe and is the right first move; it is `complicated (buildable)` on existing substrate.
- Candidates 3 and the broad form of 4 are V4+ / substrate-blocked. Register scoped, do not design.
- Candidate 5 belongs cross-listed with the ethics perimeter, not filed only under learning.
- **`/lit-pull`:** continual learning / catastrophic forgetting, elastic weight consolidation and successor methods, meta-learning of learning rates, and the complementary-learning-systems literature — but check overlap first, CLS is already heavily represented (MECH-316, ARC-064, MECH-211).

## Next steps

1. Register candidates 1–2 and 4-narrow as testable; 3 and 4-broad as `substrate_conditional` V4; 5 as an invariant sibling of the distractor-intake ethical claim. **Deferred from this session.**
2. Mark the raw thought `Status: processed` once (1) lands.
3. Scope the local-update interference test (candidate 1).
