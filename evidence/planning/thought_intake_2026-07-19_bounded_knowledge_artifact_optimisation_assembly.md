# Thought Intake — Bounded knowledge-artefact optimisation for REE Assembly

**Date of thought:** 2026-07-19
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-19_bounded_knowledge_artifact_optimisation_for_ree_assembly.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Source:** Microsoft SkillOpt — *Executive Strategy for Self-Evolving Agent Skills*
**Scope:** **REE Assembly scientific-development and governance machinery ONLY.** Explicitly separate from REE cognitive architecture — that half is `thought_intake_2026-07-19_conservative_skill_refinement_multi_timescale_learning.md`. The user split the source into two thoughts precisely to prevent the conflation; preserve it.
**Status:** structured intake written; candidate claims NOT yet registered (concurrent session held the `claims.yaml` claim).
**Promotes/demotes:** nothing.

## Self-reference note (read this first)

The raw thought's proposed pilot target is *"thought-intake generation and review workflow"* — the very workflow that produced this document. That is a genuine methodological hazard and should be stated rather than quietly enjoyed: this intake is **not** held-out evidence about intake quality, and must not be counted as such in any later pilot. If the pilot runs, this document belongs in the *training* subset or is excluded entirely.

## Registration target

Assembly-facing material registers as **`claim_type: governance_rule` / INV / GOV-\*** claims, not as REE mechanism claims. Precedent: **INV-077** (evaluation channels as evidence-producing boundaries), **Q-069**, **GOV-PROC-1** (ethics-as-process), **GOV-CEIL-1** (substrate-ceiling exhaustion demotion rule), **SD-062** (claims index as a typed multi-axis structured-uncertainty graph). Do not mint MECH-* for anything in this document.

## Already owned — cross-reference, do NOT re-assert

The raw thought says its loop "closely resembles existing REE Assembly practice." It does, and more of it is already *formalised* than the thought assumes:

| Assembly principle in the thought | Existing machinery / claim |
|---|---|
| Evidence-gated promotion of claims | the `/governance` cycle; `exp_conf >= 0.62` promotion gate; `promotion_demotion_recommendations.md` |
| Bounded edit with supersession rather than deletion | `/thought-digestion` "excrete" rule (`status: superseded` + reason + reverse-dep guard); the EXQ lettered-supersession policy |
| Provenance on every artefact | manifest -> review -> governance -> claim pipeline; `review_tracker.json` as sole source of truth; run-pack manifests |
| Failure preserved as informative | `/failure-autopsy`; `evidence_direction: superseded` as *inactive-but-retained* |
| Demotion on repeated failure | **GOV-CEIL-1** (N>=3 substrate-ceiling hits -> demotion) |
| Meta-optimisation subordinate to human authority | **INV-077**, **GOV-PROC-1**, the governance-interactive rule (pause for user decision, never auto-route) |
| Claims registry as a governed typed structure | **SD-062** |
| Workflow registry | the skills system (`.claude/skills/*/SKILL.md`, mirrored to `.agents/skills/`) — a registry of reusable workflows with intended use, inputs, and prerequisites |

**And one that deserves naming, because it was invented ad hoc and is exactly principle 4:** several CLAUDE.md and SKILL.md sections already carry an explicit **"Scope history — read before 'simplifying' this"** block recording what the rule was, what it was changed to, what was withdrawn, and *why the withdrawal was itself corrected*. That is a rejected-edit memory with reconsideration conditions, hand-rolled at exactly the place where repeated rediscovery was most costly. The thought's principle 4 generalises an existing local practice rather than importing a foreign one — which is the strongest possible argument for it.

## Genuinely new — four things

### N1. Held-out validation is systematically absent

Every layer of Assembly practice edits the artefact from **the session that motivated the edit**. A workflow change is judged by the cycle that produced it; a CLAUDE.md rule is written by the session that hit the incident; an intake template is revised by the intake that strained it. There is no held-out review anywhere in the loop.

This is the sharpest genuinely-new observation, and it has a **measurable and already-visible cost**: rules written from a single incident have repeatedly over-generalised and needed correction (the chip-scope rule was broadened, withdrawn entirely, restored, and then narrowed — four revisions, the third of which the user corrected the same day). A held-out test — *does this rule produce the right call on three past cases it was not written from?* — would have caught at least the over-broad forms.

Note the honest counterweight the thought itself supplies under Risks: held-out validation costs cycles, and *"optimising for easily measured quality may reduce originality or conceptual depth."* This is a real trade, not a free win.

### N2. Artefact-layer update rates are implicit, never stated as a governance hierarchy

```
prompts and local workflow hints:  relatively fast
thought-intake structure:          moderate
claims and mechanism status:       evidence-gated
architecture commitments:          slow
organisational principles:         very slow
axioms:                            exceptional
```

The practice roughly follows this. Nothing states it, so nothing enforces it, and nothing flags when a fast-layer edit silently changes a slow-layer commitment. That last case — **silent scope expansion across authority layers** — is the failure this hierarchy would catch, and it is the same shape as the INV-020 authority-stratification invariant that REE itself is required to satisfy. The symmetry is worth stating: *the Assembly should obey the invariant it demands of the architecture.*

### N3. The skills registry carries no evaluation history

Skills declare intended use and prerequisites. None carries **known failure modes, evaluation history, version/provenance, or confidence and scope**. So there is no basis for a workflow selector, and no way to notice that a skill has been degrading. Adding those fields is `complicated (buildable)` and cheap; building a *selector* on top is not, and should not be attempted until the fields have accumulated real history.

### N4. Rejected-edit memory as a first-class store

Generalising the ad-hoc "Scope history" blocks: a **rejection buffer** holding the proposed edit, why it was proposed, why it was rejected, the evidence considered, and the conditions under which reconsideration is appropriate. The last field is the one that makes it more than an archive.

The nearest existing thing is claim supersession, which retains *superseded assertions* but not *rejected proposals* — a rejected experiment proposal, a rejected workflow change, a rejected claim registration currently leaves no trace at all.

## Kill criteria (adopt as written — this is the best part of the thought)

Demote or stop the approach if it: produces no held-out improvement; increases unsupported claims or duplicate artefacts; makes provenance harder to inspect; optimises superficial formatting over scientific quality; increases governance burden more than it reduces; repeatedly proposes changes already rejected for known reasons; or weakens human review or authority boundaries.

**The sixth is self-referential and load-bearing** — an optimiser that keeps re-proposing rejected changes is precisely what the rejection buffer exists to prevent, so failing it means N4 did not work.

## Candidate claims (for registration at digestion — governance_rule class)

1. **Held-out validation for Assembly workflow and rule changes.** *Candidate, `governance_rule`.* A change to a workflow, skill, or standing rule should be validated against cases that did not generate it. *Falsifier / acceptance:* for a proposed rule change, apply it to N>=3 historical cases outside the motivating incident and check it yields the correct call; a rule that only fits its originating incident is rejected or narrowed. *Non-degeneracy guard:* the held-out cases must be ones where the old and new rule actually differ — cases where both give the same answer test nothing. *Cross-ref:* INV-077, GOV-PROC-1, the chip-scope revision history as the worked example.

2. **Assembly artefact-layer authority stratification.** *Candidate, `governance_rule`.* Assembly artefacts form an update-rate hierarchy (prompts -> intake structure -> claims -> architecture commitments -> organisational principles -> axioms), and an edit at a fast layer must not silently change a slower layer's commitment. *Acceptance:* scope-expansion is detectable — a fast-layer edit that alters a slow-layer commitment is flagged, not merged. *Cross-ref:* **INV-020** (the architectural twin: constraint stores are authority-stratified from direct writes), INV-021, GOV-PROC-1.

3. **Rejected-edit memory with reconsideration conditions.** *Candidate, `governance_rule`.* Rejected proposals (workflow changes, claim registrations, experiment proposals) are retained with proposal, rationale, rejection reason, evidence considered, and reconsideration conditions. *Acceptance:* repeat-rediscovery rate falls; a re-proposal of a previously rejected change is detected. *Cross-ref:* the existing "Scope history" blocks (the ad-hoc precedent), claim supersession, `/failure-autopsy`.

4. **Skill-registry metadata: failure modes, evaluation history, provenance, confidence, scope.** *Candidate, lower-authority — arguably an implementation task rather than a claim.* Register only if it needs governance visibility; otherwise route straight to implementation. *Cross-ref:* the skills system, SD-062.

5. **(Guard, register with 1–4 or not at all) Meta-optimisation remains subordinate to provenance, epistemic honesty, and explicit human authority.** *Candidate, `governance_rule`.* An Assembly self-improvement loop must not shift governance authority, erase authorship distinctions or uncertainty, or increase artefact volume at the expense of quality. *Cross-ref:* INV-077, GOV-PROC-1, the governance-interactive rule, and the Risks list in the raw thought (epistemic monoculture via reviewer selection is the least obvious and most durable of them).

## Routing

- **Do not build a SkillOpt-style optimiser.** The thought does not ask for one, and the pilot it proposes is deliberately low-risk.
- **Cheapest real move: candidate 1 as a manual discipline, not as tooling.** Adding "check this against 3 cases it wasn't written from" to the rule-editing path costs nothing and addresses the observed failure directly. Do that before any registry or harness work.
- **Candidate 3 next**, as a lightweight extension of the existing "Scope history" convention (a named section, not a new system).
- **Candidate 4 is a small implementation task** — add the metadata fields; do not build a selector until history accumulates.
- **The pilot, if run, must exclude this document** (see Self-reference note) and must use the metric panel with the thought's own caution attached: *no single metric should become the optimiser's sole target.* The listed metrics — unsupported-novelty rate, duplicate-claim creation rate, reviewer correction burden, frequency of later supersession caused by avoidable intake defects — are good, and the last is the best because it is measured downstream rather than at production time.
- **`/lit-pull`:** not obviously needed. This is a design/governance thought, not an empirical one.

## Next steps

1. Register candidates 1–3 (+5) as `governance_rule` claims; route 4 to implementation. **Deferred from this session.**
2. Mark the raw thought `Status: processed` once (1) lands.
3. Consider adding the held-out check to the rule-editing path in CLAUDE.md — small, and it is the one item with a demonstrated cost of absence.
