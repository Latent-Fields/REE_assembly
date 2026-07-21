# Thought Intake — V3 closure as the boundary for external legibility

**Date of thought:** 2026-06-21
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-06-21_v3_closure_as_external_legibility_boundary.md`
**Session:** `confident-pare-9273f1` (orphaned-thought intake pass, 2026-07-21)
**Source:** an external review of the Latent-Fields repositories. Treated as **external process feedback on the Assembly**, not as evidence about REE the agent.
**Status:** structured intake written; candidate claims **NOT yet registered** (concurrent sessions held the `docs/claims/claims.yaml` claim at intake time). Registration deferred.
**Promotes/demotes:** nothing.

## Authorship note

The source position is the user's and is quoted verbatim below. The framing of present inscrutability as *construction-phase opacity with a repayment boundary*, the before/at-closure split, and the transition-gate wording are assistant formalisation developed from that position in the raw thought; they are claim-generative intake material, not canon.

## The position (verbatim)

> I don't think there will be something inspectable until v3 closes. I aim to leave it inscrutable until I have that done. Then perhaps implementing your ideas would be reasonable.

## Register class

This is **Assembly / governance-facing, not cognitive architecture.** It concerns the research programme's release and version-transition policy, not any mechanism in the agent. It therefore registers as `claim_type: governance_rule` (precedent: **INV-077**, **GOV-PROC-1**, **SD-062**, and the SENT-0..16 / GOV-* block), **not** as MECH-* / ARC-* / SD-*. Nothing here should acquire a substrate falsifier or an EXQ id.

A consequence worth stating up front: **a governance rule's "falsifier" is a compliance audit, not an experiment.** Each candidate below therefore carries an audit-shaped PASS/FAIL and, in place of a substrate non-degeneracy guard, a **precondition on the rule being decidable at all** — the governance analogue of `substrate_not_ready`.

## Already owned — cross-reference, do NOT re-assert

The ethics-perimeter Phase-0 block (landed ~2026-06-20, so *contemporaneous with* this thought) already owns most of the release-gating surface:

| Element in the thought | Existing claim / artefact |
|---|---|
| "V3 stays public as bounded work; higher versions gated" | **SENT-14** (responsible release / private higher-version governance) |
| Concise statement of what V3 does and does not establish | **SENT-0** (current-scope boundary statement, re-evaluated at every generation boundary) |
| External legibility of the ethics surface before release | **GOV-EXT-1** (EU AI Act / CoE / NIST / ISO / OECD crosswalk) |
| Capability-release gating | **GOV-SEC-1** |
| Progressive binding of governance across v3->v6 | **GOV-PROC-1** |
| No patient-identifiable data in public repos | **GOV-HEALTH-1** (audited clean) |
| Provenance discipline on confidence updates; human/agent signal classes non-collapsible | **INV-077** |
| The claims index as the typed multi-axis structure a reader would traverse | **SD-062** |
| Reanalysis-before-new-work discipline | **GOV-REUSE-1** |
| "One canonical entry point" (partially BUILT, not merely planned) | `docs/public_explorer/` + `scripts/export_public_explorer.py` + `docs/public_explorer_policy.md`; plus `docs/START_HERE_HOW_REE_DEVELOPS.md`, `docs/CURRENT_FRONT.md`, `docs/REE_MIN_SPEC.md` |
| "How close is V3 to closing" | `docs/closure_dashboard.md` (generated; 77.5% at 2026-07-21, 80 non-deferred nodes across 12 plans) |
| Separating positive results, failures, unresolved claims | the manifest / autopsy / supersession machinery and `evidence_direction` vocabulary |

**Material correction to the thought's premise:** it was written against a review finding "no single inspectable artefact." A curated public explorer, an explicit exposure policy, a generated closure dashboard, and a live-front doc now exist. The *routing and compression* complaint largely stands (too many repositories, accumulated operational history); the *absence of any public artefact* complaint does not. Do not register a claim that asserts the absent-artefact premise.

## Genuinely new — three things

### N1. Nothing gates the START of V4 on the EXISTENCE of a frozen, inspectable V3

This is the thought's actual contribution and the registry does not contain it. SENT-14 gates **release** on welfare/continuity/security governance travelling with the capability. GOV-EXT-1 gates **release** on legal legibility. GOV-SEC-1 gates **release** on containment. All three are release gates.

The thought's risk is different and is not covered by any of them:

> The risk is not that V3 remains difficult to inspect during construction. The risk is that V3 closes and the project moves directly into V4 without producing a stable, inspectable V3 artefact.

That is a **version-transition** gate, and the guarded asset is not the public's safety but the project's own ability to ever produce a reference account of what V3 established. Once V4 development begins moving the substrate, the opportunity is not merely postponed — the object being described stops existing in the form that was validated.

### N2. Opacity as *declared, bounded* technical debt

The positive half of the position, and the reason it is a governance rule rather than a preference: inscrutability is **acceptable** while it carries a defined repayment boundary, and unacceptable once it does not. That converts an intuition ("not yet") into an auditable object ("not yet, until X, and X is named and dated"). The failure mode it guards against is boundary drift — the repayment date silently moving with each new development wave, which is how construction-phase opacity becomes permanent opacity.

It also names a real cost of *premature* externalisation that no existing claim states: external legibility creates a **second design target** while the architecture is still moving, and can distort research toward what is easiest to explain rather than what most needs testing. That is a substantive argument, not a delay tactic, and belongs on the record as the rule's rationale.

### N3. Legibility by subtraction and compression, not by rewriting history

An information-architecture commitment: make V3 legible by **removing and compressing** — separating current work / supporting research / archaeology, curating a reader path, marking human vs agent provenance — rather than by producing a new narrative account of the whole research history. This is the method claim, and it is the one that makes N1 affordable. Without it, "produce a frozen V3 artefact" reads as a months-long documentation project and will therefore not happen.

Note this interlocks with **INV-077** at the presentation layer: human/agent provenance must be visible in the public account, not only enforced at the confidence-update boundary.

### Cross-link

**N1 composes directly with the 2026-06-24 evolutionary-retention intake's candidate 5 (reference-cognifold record).** That thought arrives at the same object from the opposite direction — it wants a frozen V3 as a *manipulable causal artefact for later comparison*; this one wants it as an *inspectable external account*. They should be registered as one gate with two rationales, not two gates. See `thought_intake_2026-06-24_evolutionary_retention_and_post_ree_cognifold_compilation.md`.

## Explicitly NOT proposed

- **Not** proposing to make the moving V3 system publicly legible before closure. The thought argues the opposite and that argument is the rule's rationale.
- **Not** proposing to block V4 work. The raw thought is explicit: *"This is not yet a proposal to block all V4 work."* Any registered gate must be a **produce-before-submerge** requirement, not a stop-work order.
- **Not** a claim about REE the agent. No MECH-*/ARC-*/SD-*; no substrate falsifier; no EXQ id.
- **Not** re-asserting SENT-0, SENT-14, GOV-EXT-1, GOV-SEC-1 or GOV-PROC-1.
- **Not** asserting the review's "no single inspectable artefact" finding, which the public explorer has since partly answered.
- **Not** proposing a public-repository restructure. Repository consolidation is a large, separable decision with its own risks and is out of scope here.

## Candidate claims (for registration at digestion)

1. **Version-transition artefact gate: V4 expansion must not erase the opportunity to freeze, reproduce, describe and inspect the completed V3.** *Candidate, `governance_rule`, binds at the V3->V4 boundary.* Before substantial V4 substrate expansion, a defined **minimum V3 closure package** must exist. Working contents, to be fixed at registration: one canonical entry point; one frozen V3 specification; one reproducible flagship demonstration; one statement of what V3 does and does not establish; one findings document separating positive results, failures, unresolved claims and scope limits. *Audit-shaped PASS/FAIL:* PASS = every package item exists at a named path **and** an independent reader reproduces the flagship result from the frozen spec alone. FAIL = V4 substrate work crosses the named threshold with any item absent. *Decidability precondition (the governance analogue of non-degeneracy):* the rule is only auditable if (a) "V3 closure" and (b) "substantial V4 expansion" both have operational definitions. Absent (a), the gate never triggers; absent (b), it triggers on everything. If either is undefined at audit time the rule self-routes **`definition_not_ready`** and the audit reports that rather than a pass. Candidate 4 supplies (a). *Cross-ref:* SENT-14, SENT-0, GOV-EXT-1, GOV-PROC-1, `docs/closure_dashboard.md`, and the 2026-06-24 reference-cognifold candidate.

2. **Construction-phase opacity is acceptable technical debt only while it carries a named, dated repayment boundary.** *Candidate, `governance_rule`.* External inscrutability during construction is a legitimate choice, not a defect, provided the boundary is declared and reviewed on the same cadence as SENT-0 (every generation boundary). *Audit-shaped PASS/FAIL:* PASS = a boundary event and date are recorded and unchanged, or changed with a recorded reason. FAIL = no boundary recorded, or the date has moved more than once without recorded justification (the drift failure mode). *Decidability precondition:* requires at least one named boundary event to exist; a rule with no declared boundary is vacuous rather than violated, and should report `definition_not_ready`, not FAIL. *Cross-ref:* SENT-0, GOV-PROC-1, candidate 1.

3. **Legibility by subtraction: the closure package is produced by curating and compressing existing material, not by rewriting the research history.** *Candidate, `governance_rule` / method commitment.* Separate the primary reader path (current work) from supporting research and from operational archaeology; retain audit history but remove it from the reader path; mark human vs agent provenance in the public account. *Audit-shaped PASS/FAIL:* PASS = a reader path exists whose length from entry point to a reproducible result is bounded by a pre-registered number of hops, with archaeology reachable but off that path. FAIL = the package is produced as new prose narrating the whole history. *Decidability precondition:* requires an agreed entry point and an agreed "reproducible result" target; without both, hop-count is unmeasurable and the rule reports `definition_not_ready`. *Cross-ref:* INV-077 (provenance, presentation-layer instance), SD-062, `docs/public_explorer_policy.md`, `docs/START_HERE_HOW_REE_DEVELOPS.md`.

4. **Open question: what event counts as V3 closure for the purpose of these gates?** *Candidate, `open_question` (Q-*).* Strict green board, governance acceptance, or an additional reproducibility check — the three are not equivalent and candidate 1 is undecidable until one is chosen. *What would answer it:* a decision, not an experiment. Note the strict green-board date has already passed (target 2026-07-19; the closure dashboard reads 77.5% at 2026-07-21 with 23 nodes remaining and 9 blocked), so "green board" is currently a *future* event and the question is live rather than academic. *Decidability precondition:* none — this question exists precisely because the precondition for the others is missing. *Cross-ref:* candidate 1, `docs/closure_dashboard.md`, `docs/roadmap.md`.

5. **(Deferred, not a claim) Which V3 result serves as the flagship demonstration.** Do not register. It is a selection to be made from the evidence index at package-build time, not a proposition to be held. Recorded here so it is not lost.

## Routing

- **Candidate 4 first — it is a decision, not a discovery**, and candidates 1-3 are undecidable without it. `complicated (buildable)`: put the three options (strict green board / governance acceptance / reproducibility check) to the user with their consequences and record the choice. This is the whole critical path.
- **Then candidates 1-3** as governance text. `complicated (buildable)` throughout — no probe, no unknown; the work is specification.
- **The flagship selection (5)** is `puzzle (known rules)`: the missing item is a *fact* recoverable from the evidence index — the highest-confidence PASS with a complete, re-runnable run pack — not a reframe and not a probe. Retrieve it when the package is built, not before.
- **"Will external readers actually enter, and will the compression land?"** is `aleatoric (irreducible)`. Do not research it, do not build a metric for it in advance; hedge by keeping the package small enough that a wrong guess is cheap to revise.
- **Repository consolidation** is out of scope (see NOT proposed) and should be surfaced separately if the user wants it, not smuggled in under candidate 3.
- **No `/queue-experiment` involvement anywhere in this intake.** If any downstream work here acquires an EXQ id, something has gone wrong.

## Next steps

1. Put candidate 4 to the user as a decision. **Not done in this session** (intake-only pass).
2. Register candidates 1-3 as `governance_rule` once 4 is settled. **Deferred from this session** — `claims.yaml` was held by concurrent sessions at intake time.
3. Mark the raw thought `Status: processed` only once registration lands. It currently remains `unprocessed`, correctly.
4. Register candidate 1 jointly with the 2026-06-24 reference-cognifold candidate rather than as two separate gates.
