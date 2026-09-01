# Thought Intake: Versioning, the V3→V4 prerequisite cut, and the cutover problem

- **Date processed:** 2026-09-01
- **Raw thought:** `docs/thoughts/2026-08-29_versioning_v3_v4_prerequisite_cut_and_cutover.md`
- **Session:** planning-metabolise-20260901

## Verbatim core proposal

Version numbers have been carrying two concepts: (1) organism/design generation and (2) evidential closure state. These should separate: "The version boundary should follow architectural generation; the scientific cutover should follow prerequisite qualification." V3 has two milestones: Milestone 1 (design objective — the 2026-08-29 minimal-working-intelligence declaration) and Milestone 2 (V3 qualified as prerequisite substrate for V4). Milestone 2 is defined by the **V4 prerequisite cut** — "the smallest transitive set of V3 capabilities/claims whose truth or functional adequacy is assumed by V4" — not by total closure percentage. V4 becomes developmentally admissible when every load-bearing prerequisite is either *sufficiently demonstrated* or *bounded and instrumented*, and remaining V3 uncertainty is unlikely to hide a foundation-invalidating defect. Cutover risks are symmetric (too early: inherited defects masquerade as V4 phenomena; too late: V3 becomes an endless validation sink). Adjudication is a dedicated cutover review, not a percentage gate.

## Key formulations

> "Version membership is not the same thing as inheritance, and inheritance is not the same thing as closure membership."
> "Do not require V3 to be fully closed before V4 begins. Require V3 to be sufficiently qualified in exactly the things V4 needs."

## What's new vs. existing REE docs/claims

| Thread | Existing coverage | Verdict |
|---|---|---|
| Freeze V3 before V4 substrate moves | **GOV-V3FREEZE-1** (produce-before-submerge closure package + reference record); **Q-087** (V3 closure = governance acceptance, user decision 2026-08-01); **GOV-OPACITY-1** (repayment boundary) | Already-owned — cross-ref only. The new rule COMPOSES with (does not replace) the freeze gate: FREEZE says "capture the object before it moves"; the CUT says "which uncertainties block starting V4 at all" |
| Per-claim "V3 beginning / V4 cutover" split | Already practised ad hoc (e.g. ARC-080 pillar 2 self-as-object: V3 beginning, V4 object-file cutover) | Existing pattern — the new rule generalises it |
| Derived classification of unresolved V3 nodes (inherited_prerequisite … orphan_or_dependency_defect) | `assembly_state` (derived, claims layer), closure-node status machinery, `v3_pending` gate — none answer "is this node on a transitive dependency path to V4?" | **Genuinely new** — registered below |
| Parallel version work after qualification | GOV-V3FREEZE-1 notes "NOT a stop-work order"; roadmap docs assume sequence | New as an explicit principle; carried inside the registered claim |

## Affected existing claims

Cross-referenced (no status/evidence touched): GOV-V3FREEZE-1, GOV-OPACITY-1, Q-087, GOV-SUBTRACT-1. The registered claim `depends_on` these.

## Candidate claims — REGISTERED this pass

- **GOV-V4CUT-1** — V4 prerequisite cut governance rule: the V3→V4 scientific cutover is gated by qualification of the smallest transitive set of V3 capabilities V4 assumes (each *sufficiently demonstrated* or *bounded-and-instrumented*), adjudicated by a dedicated cutover review; never by a global closure percentage. Version labels name organism generations; closure describes validation state.

## Next steps

1. **Derive the cut** (the raw thought's follow-on 1-2): traverse live claims/plans/architecture assumptions to identify the actual prerequisite set and classify residual V3 nodes against it. This is the core science-governance campaign recommended by session planning-metabolise-20260901 ("V4 prerequisite cut derivation"). Do NOT infer from `phase:` labels alone.
2. The derived classification should be a projection over existing claims/plans (a report/audit), not a second hand-maintained registry — same posture as GOV-APPLY-1/GOV-CEIL-1 audits.
3. Companion intake: `thought_intake_2026-08-31_replay_rebucketing_decision_relevance.md` supplies the first concrete pulled-forward-prerequisite candidates for the cut to adjudicate.
