# Thought Intake: Causal Reach, Installability, and When a Mechanism Becomes Part of the Organism

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`
**Session:** mech-266-rescore-circling-2d31ca (thought-ingestion batch of 3, drafted by a research
subagent, merged and committed by the orchestrating session)
**Origin (per raw thought header):** Structured mining of Antonio Gullì's *Agentic Design
Patterns*, its companion code, and the current `REE_assembly`/`ree-v3` repositories. **This
citation is unverified** -- neither the drafting subagent nor this merge confirmed the book's
existence, publisher, edition, or that its content matches the patterns described.

---

## 1. Core proposal(s) -- this thought contains several distinct formulations

The raw thought (~618 lines) contains six genuinely distinct proposals:

1. **A methodological move for literature mining**: when an external source's mechanism overlaps
   something REE already claims but has *struggled to implement working*, do not stop mining --
   ask whether the source offers a better decomposition, a simpler positive control, an explicit
   routing boundary, a stopping condition, a reference operator, or a diagnostic that shows
   exactly where the REE mechanism loses causal reach.
2. **The causal-reach ladder**: an 8-stage audit projection refining ARC-120's existing 5-stage
   sequence, adding stages after authority.
3. **Installability as a separate, dissociable competence**, distinct from competence retention.
4. **A positive-control validity rule**: a mocked/injected downstream state can certify a
   consumer, not production-path reachability.
5. **An intervention-diagnostic taxonomy**: oracle vs. non-oracle crossed with silky vs.
   oddly-composed, as two independent axes.
6. **A "mechanism passport" / `MechanismReachTrace` recording schema** -- offered tentatively, not
   asserted as an architectural commitment.

The thought's own final formulation: *"The mechanism is not the component. The mechanism is the
reachable pathway through the organism,"* plus: *"Installability is not an afterthought. It is one
of the competences the architecture must demonstrate."*

The thought explicitly states it "does not presently justify a new cognitive module" and offers
itself as "an amendment or elaboration of ARC-120, not a new claim" for item (2) -- both
disclaimers honored below.

## 2. What's new vs. existing REE docs/claims (novelty table)

| Thread | Existing REE coverage | Verdict |
|---|---|---|
| Competence precedes authority (general framing) | **ARC-120**: existence -> representation -> competence -> authority -> behavioural influence. | Already owned as the base sequence. Genuinely extended, not duplicated. |
| Authority may fail to propagate to committed throughput | **MECH-480**: LOFC-analog execution-gain channel dissociable from dACC-analog strategy authority -- a live V3 example. | Already owned as ONE instance. The ladder generalises across instances; MECH-480 becomes a cross-ref, not duplicated. |
| Failure classified into REE/mechanism/measures/environment buckets before charging REE | **GOV-FAILLOC-1**. | Adjacent, not duplicated. GOV-FAILLOC-1 triages a FAIL post hoc; GOV-PATHVALID-1 is about experimental DESIGN validity -- whether a positive control can certify pathway reachability at all. |
| Diagnostic no-verdict recurrence, "the question may be mis-posed" | **GOV-DIAG-1**. | Adjacent (diagnostic epistemics) but different question -- GOV-DIAG-1 is about repeated failure to reach a verdict; GOV-INTERVENE-1 classifies what kind of evidence one diagnostic result is. Not duplicated. |
| "Umpire, not ruler" -- observation/interpretation/mechanism separation, discriminating perturbations | **GOV-BEHADJ-1** + **Q-092**. | Closely adjacent methodology cluster. GOV-BEHADJ-1 already names "discriminating perturbations (positive, destructive, orthogonal negative control)" but lacks the oracle/non-oracle and silky/oddly-composed axes -- those are new. Cross-ref, not duplicated. |
| Repository possibility vs. the configured, instantiated, dynamically reachable organism | Traced to `2026-08-10_ree_as_a_single_understandable_cognifold.md`, whose own intake registered no claim ("a documentation/public-communication proposal with no falsifiable content"). | Already owned in prose, not in the registry. No claim ID to cross-reference; noted only. |
| Persistence must earn continuation / stopping conditions | **ARC-128 / MECH-497 / MECH-498** -- different subject (termination of persistent processes over time), cited only as a structural analogue. | Distinct subject matter. Not duplicated; noted as analogy only. |
| Competence acquisition vs. retention dissociable | **MECH-459** (folded from withdrawn MECH-476) -- retention across subsequent learning/consolidation. | Adjacent but explicitly NOT identical to installability: retention is about surviving time/learning; installability is about surviving simultaneous composition. The raw thought itself flags this needs "a duplication and literature audit" -- taken as a caution, not a blocker. |
| "Competence floor" / conversion-ceiling explanandum already informally called "installability" | `claims.yaml` governance notes on **MECH-457** (V3-EXQ-819) already literally use the phrase "the competence FLOOR / installability explanandum." | Partially already-owned AS A WORD/POINTER, but never formalised as its own general architectural claim. Genuinely new as a general, cross-mechanism property claim; MECH-457 becomes the closest existing INSTANCE, wired via depends_on. |
| Load-bearing positive control must traverse the full production path, not just certify a mocked downstream consumer | Searched for "mock", "contract harness", "production path", "reachability" -- found only instance-level occurrences (the `closure_exclusive_decommit_eval` V3-EXQ-460k finding). No general rule stating this as a standing methodological requirement. | **Genuinely new -> registered as GOV-PATHVALID-1.** |
| Oracle vs. non-oracle epistemic content, crossed with silky vs. oddly-composed construction | "Positive control" used constantly and informally throughout `claims.yaml` (hundreds of hits) but always as a single undifferentiated device, never taxonomised along these two independent axes. No hits for "oracle intervention", "silky injection", "oddly composed" anywhere in the registry. | **Genuinely new -> registered as GOV-INTERVENE-1.** |
| Causal-reach ladder as a refinement of ARC-120, with post-authority stages | ARC-120 stops at "behavioural influence" (5 stages, no post-authority granularity). | **Genuinely new -> registered as ARC-130** (extends, does not supersede, ARC-120). |
| Installability as a general, cross-cutting architectural property distinct from isolated component validation | No existing claim states this as a general requirement; closest is the informal MECH-457 usage noted above. | **Genuinely new -> registered as ARC-131.** |
| "Identify the first broken causal edge and report the furthest stage demonstrated" (candidate instrumentation doctrine) | Overlaps GOV-FAILLOC-1's existing bucket-triage discipline and ARC-130's own "furthest stage reached" recording convention. The thought itself says this "may refine GOV-FAILLOC-1 rather than requiring a separate rule." | **NOT separately registered.** Folded into ARC-130's notes as a corollary and flagged as a possible future GOV-FAILLOC-1 amendment. |
| The mechanism-passport / `MechanismReachTrace` schema | Nothing resembling this exists. The thought itself hedges it ("may be useful... not necessarily as one monolithic runtime object"). | **NOT separately registered.** Recorded as an unbuilt instrumentation proposal in ARC-130's notes. |
| The originating methodological observation itself (mine harder when literature overlaps a struggling REE mechanism) | No existing GOV-* rule captures this. Checked GOV-EXT-1, GOV-ANALOGY-1, GOV-DIAG-1 -- none match. `REE_convergence` normalises external models into comparison format, not a rule about follow-through discipline during reading. `/lit-pull` pulls literature FOR an existing claim, not a rule about this pattern. | **Genuinely new content, explicitly FLAGGED rather than decided** -- see Section 6. Could become (a) a thin GOV-* rule, (b) a process note in `REE_convergence/CONTRIBUTING.md`, or (c) a step in `.claude/skills/lit-pull/SKILL.md`. Not registered in this pass. |

## 3. Key formulations (verbatim, load-bearing)

> A mechanism is not fully part of the organism merely because its code, representation, or local
> operator exists. It becomes part of the organism only when the organism can recruit it under the
> appropriate conditions, its operation can acquire the intended authority, that authority can reach
> committed behaviour, and the resulting competence survives installation into the whole cognifold.

> The meaningful scientific object is therefore not simply the component. It is the **reachable
> pathway through the whole instantiated organism**.

> Competence should precede authority, but authority must also demonstrate throughput.

> A mechanism that cannot be installed without losing its function is not yet a solved
> organism-level mechanism, even if its isolated implementation is correct.

> A contract test that mocks the source of the load-bearing state cannot certify production-path
> reachability.

> oracles establish achievable ceilings and downstream usability; silky injections map local causal
> sensitivity, thresholds, timing dependence, and hysteresis; oddly composed injections test
> factorisation, invariants, compositionality, and shortcut dependence.

> The mechanism is not the component. The mechanism is the reachable pathway through the organism.

> Installability is not an afterthought. It is one of the competences the architecture must
> demonstrate.

## 4. Affected existing claims

- **ARC-120** -- extended (not amended, not superseded) by ARC-130, exactly as the raw thought
  itself proposes. ARC-120 remains the sole owner of the base 5-stage sequence.
- **MECH-480** -- cited as the cleanest existing single-instance demonstration of "authority
  acquired at one boundary failing to reach committed throughput." Wired as a depends_on
  evidentiary instance, not modified.
- **MECH-457** -- cited as the closest existing instance of the installability explanandum. Wired
  as depends_on for ARC-131; MECH-457 itself is untouched.
- **MECH-459 / withdrawn MECH-476** -- explicitly distinguished-from by ARC-131: retention is not
  the same axis as installability. Cross-referenced, not merged, not reweighted.
- **GOV-FAILLOC-1** -- adjacent to GOV-PATHVALID-1, cross-referenced via depends_on, flagged as a
  possible future amendment target (not done here).
- **GOV-DIAG-1** -- adjacent to GOV-INTERVENE-1, cross-referenced, not modified.
- **GOV-BEHADJ-1 / Q-092** -- closest existing methodology cluster, cross-referenced by depends_on
  from GOV-INTERVENE-1.
- **ARC-128 / MECH-497 / MECH-498** -- noted only as a structural analogy. No content overlap.

No existing claim's status, confidence, or evidence record is touched by this intake.

## 5. Candidate claims -- REGISTERED this pass

Four claims registered directly into `docs/claims/claims.yaml` (see that file for the authoritative
entries). Six candidate threads were identified (Section 1); two (the "furthest stage"
instrumentation doctrine and the `MechanismReachTrace` schema) were deliberately folded into notes
rather than given their own IDs, and the methodological literature-mining observation is flagged
rather than registered (Section 6).

- **ARC-130** -- `architecture.mechanism_causal_reach_ladder`. Causal-reach ladder refining
  ARC-120 with post-authority granularity (competitive authority, committed throughput, ecological
  consequence, retention/generalisation).
- **ARC-131** -- `architecture.installability_as_composition_competence`. Installability as a
  composition-dissociable competence, distinct from retention (MECH-459).
- **GOV-PATHVALID-1** -- `governance.epistemics.positive_control_production_path_traversal`.
  Load-bearing positive controls must traverse, not mock, the production path they claim to
  validate.
- **GOV-INTERVENE-1** -- `governance.epistemics.intervention_diagnostic_taxonomy`. Oracle/non-oracle
  x silky/oddly-composed as two independent diagnostic-intervention axes.

**Version-routing deviation, explicitly flagged, not decided unilaterally**: unlike the default
v4/v4_v5 thought-intake park, all four are scoped `implementation_phase: v3` / `version_relevance:
v3` (ARC-130/131) or `binds_at_version: v3` (the GOV-* rules), because they are audit/
interpretation frameworks immediately applicable to already-running V3 mechanisms, not proposals
for new substrate. A future `/governance` cycle should confirm this scoping.

A new architecture doc stub was created:
[`docs/architecture/causal_reach_and_installability.md`](../../docs/architecture/causal_reach_and_installability.md),
in the "Foundations & Rationale" sidebar category, `nav_order: 19`.

## 6. Next steps

1. **ROUTING FLAG -- needs a decision, not made here**: the originating methodological observation
   (Section 2, last row) has no existing home. Three candidate routes: (a) a thin new `GOV-*`
   governance_rule; (b) a process note in `REE_convergence/CONTRIBUTING.md`; (c) a step addition to
   `.claude/skills/lit-pull/SKILL.md`. Recommend the user or a future session pick one.
2. **Literature verification**: the Gullì book citation is unverified. Before any registered claim
   above is described as "literature-grounded," verify the citation and add it to `source` if
   confirmed. The raw thought's "Literature and technical domains worth mining" section lists ~19
   further domains and 12 open questions -- none pulled in this pass; a dedicated `/lit-pull`
   targeting ARC-130 and GOV-INTERVENE-1 (hierarchical-RL option termination and causal
   mediation/probing seem highest-yield) is a natural follow-on, not queued here.
3. **GOV-FAILLOC-1 amendment consideration**: ARC-130's "furthest stage reached" recording
   convention may belong as a refinement to GOV-FAILLOC-1's failure-location summary. Per
   CLAUDE.md's held-out-check discipline, this should NOT be done reflexively -- flagged as a
   follow-on requiring its own held-out check, not decided here.
4. **Duplication/literature audit for ARC-131 vs. MECH-459**: the raw thought itself calls for
   this and it is not done in this pass.
5. **`MechanismReachTrace` schema**: explicitly NOT authorised for building. If a future session
   wants to operationalise it, that is a separate tooling decision.
6. The six "Why current REE makes this visible" examples in the raw thought (coalition control,
   decomposition, wanting/selection, closure/decommitment, epistemic orienting, rule apprehension)
   are explicitly NOT new adjudications of the existing findings for those mechanisms -- this
   intake does not touch any of their claim records.
