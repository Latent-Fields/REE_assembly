---
nav_exclude: true
---

<!-- DEVGOV_REVIEW_VERSION: 2026-05-16.2 -->
<!-- author: claude-sonnet-4-6, session dev-governance-synthesis-2026-05-16T163217Z -->
<!-- G4 implemented: session g4-heterogeneity-note-gate-2026-05-16T172425Z -->

# Developmental Governance Synthesis Review

**Date:** 2026-05-16  
**Status:** Review document -- synthesis only, not a registered claim.  
**Session:** dev-governance-synthesis-2026-05-16T163217Z  
**Scope:** Full coherence audit across developmental_needs_register.md, developmental_curriculum.md, claims.yaml/claims.json, roadmap.md, experiment proposals, experiment manifests, architecture documents, and telemetry plans.  
**Cross-references:**
[`developmental_needs_register.md`](developmental_needs_register.md) |
[`developmental_curriculum.md`](developmental_curriculum.md) |
[`developmental_metrics.md`](developmental_metrics.md) |
[`monostrategy_developmental_analysis.md`](monostrategy_developmental_analysis.md) |
[`replay_development_analysis.md`](replay_development_analysis.md) |
[`infant_substrate_expansion.md`](infant_substrate_expansion.md) |
[`play_substrate_design.md`](play_substrate_design.md) |
[`behavioral_diversity_acceptance_criteria.md`](../../../evidence/planning/behavioral_diversity_acceptance_criteria.md) |
[`infant_substrate_plan.md`](../../../evidence/planning/infant_substrate_plan.md)

---

## Purpose

This document synthesises findings from seven targeted literature pulls and a structural
audit of REE developmental documentation. It identifies traceability gaps, orphaned claims,
contradictions, missing governance claims, and proposed maintenance rule amendments. Every
recommendation is grounded in either a specific literature finding or a documented structural
gap; no speculative additions are included.

---

## Part 1: Literature Evidence Mapping Table

Literature searches covered seven topics: requirements traceability in safety-critical
systems, assurance cases, AI safety cases, developmental robotics governance, model
cards/system cards for agent development, scientific claim-evidence traceability, and
evidence-based requirements management.

| Source | Key finding | REE relevance | DEV-NEED IDs | Claim IDs | Conf | Classification |
|---|---|---|---|---|---|---|
| Gotel & Finkelstein 1994 (ICRE; DOI:10.1109/ICRE.1994.292398) | Pre-RS traceability (why a requirement exists) fails more often than post-RS traceability (what it becomes); rationale stripping is the dominant failure mode | REE claims lack a standard `registration_rationale` field recording the biological/clinical motivation that grounded the claim; without it, governance cannot distinguish data-sparse demotion from superseded-rationale demotion | DEV-NEED-028 (cross-stage) | IMPL-018, IMPL-019 | 0.95 | suggests missing governance claim |
| Ramesh & Jarke 2001 (IEEE TSE; DOI:10.1109/32.895989) | High-end traceability adds rationalization links (why a decision was made) beyond satisfiability links (what implements what); both are required for regulatory audit | REE operates a low-end model: satisfiability links exist (claim -> experiment run IDs), but rationalization links (why a governance promotion/demotion was decided) are absent from claims.yaml entries | DEV-NEED-028 (cross-stage) | IMPL-018, IMPL-019 | 0.93 | refines existing governance practice |
| Hayes, Dekhtyar & Osborne 2003 (RE '03; DOI:10.1109/ICRE.2003.1232745) | Automated IR-based traceability recovery retrieves more correct links than manual review at comparable precision | Governance artifacts (claims.yaml, experiment docstrings, queue entries) could support automated link-checking comparable to validate_queue.py -- catching stale or missing claim_id references | DEV-NEED-028 (cross-stage) | IMPL-018 | 0.90 | suggests implementation metric |
| Mader, Jones, Zhang & Cleland-Huang 2013 (IEEE Soft; DOI:10.1109/MS.2013.60) | FDA traceability audit identified 9 recurring problems: missing links, stale links, orphaned artifacts, scope mismatch, absent bidirectionality, inconsistent naming | REE has documented instances of all 9: stale links (EXQ-047i supersession), scope mismatch (evidence_direction applying across all claim_ids without per-claim override pre-2026-04-01), orphaned artifacts (scripts queued outside mandatory skill path) | DEV-NEED-028 (cross-stage) | IMPL-018, IMPL-019 | 0.92 | refines existing governance practice |
| Rempel & Mader 2017 (IEEE TSE; DOI:10.1109/TSE.2016.2622264) | Traceability completeness causally reduces defect rates in 3/4 project types; effect holds regardless of regulatory mandate | The `evidence_direction_per_claim` enforcement (2026-04-01), supersession policy, and claim_ids accuracy rule are all empirically justified by this result -- completeness mechanisms reduce governance defects | DEV-NEED-028 (cross-stage) | IMPL-018, IMPL-019 | 0.93 | supports existing REE governance practice |
| IEC 61508-3:2010 (SIL 2/3 standard) | Bidirectional traceability required at SIL 2: forward (every requirement addressed in later stages) and backward (every artifact justified by a requirement) | REE has forward traceability (pending_review catches unreviewed runs); backward traceability (detecting runs with no claim_ids_tested tag) is not currently automated | DEV-NEED-028 (cross-stage) | IMPL-018, IMPL-019 | 0.90 | suggests missing governance claim |
| Kelly 1998 (PhD thesis, York YCST 99/05) | GSN formalizes safety cases as Goals + Strategies + Evidence; reusable Safety Case Patterns provide argument templates | REE's claims.yaml is functionally a flat-file GSN: INV/ARC/MECH/Q/IMPL IDs are Goals; experiments are Evidence. The maintenance process (promotion/demotion cycle) mirrors Kelly's GSN case evolution process | cross-stage | IMPL-018 | 0.92 | supports existing REE governance practice |
| Bloomfield & Rushby 2020/2021 (arXiv:2004.10474) | Assurance 2.0 requires indefeasibility: every credible defeater must be explicitly identified and countered before a case is closed | REE conflict_ratio threshold and v3_pending gate are partial defeater-handling mechanisms, but no policy requires an explicit named defeater register before promotion | cross-stage | IMPL-018, IMPL-019 | 0.90 | refines existing governance practice |
| Hawkins et al. 2021 AMLAS (arXiv:2102.01564) | 6-stage GSN process for ML; Assurance Claim Points (ACPs) require explicit evidence type specification per claim | REE queues experiments without pre-declared evidence type (what constitutes sufficient evidence) -- the mandatory skill path requires a script but not a formal ACP before the experiment is authorized | cross-stage | IMPL-019 | 0.93 | refines existing governance practice |
| Ashmore, Calinescu & Paterson 2021 (ACM CSUR; DOI:10.1145/3453444) | Deployment-time distribution shift invalidates pre-deployment assurance; claims require lifecycle-phase tagging | REE's pending_substrate_reconfirmation flag is a partial response; no formal protocol specifies what evidence re-closes a claim after a substrate change | cross-stage | IMPL-018 | 0.91 | suggests missing governance claim |
| Burton & Herd 2023 (Front Comput Sci; DOI:10.3389/fcomp.2023.1132580) | Behavioral experiment evidence cannot close semantic/architectural claims without an explicit sufficiency model; three irreducible uncertainty sources for ML systems | REE does not distinguish which claims can be closed by behavioral metrics vs. which require architectural inspection or formal argument; MECH-094, SD-003, ARC-033 are examples | cross-stage | MECH-094, ARC-019 | 0.88 | conflicts with current practice |
| Lee et al. 2026 (arXiv:2601.22773) | 5 AI-specific assurance challenges; CAE taxonomy: assertion-based, constraint-based, capability-limited claims | REE's claim hierarchy lacks formal argument-type tagging; "capability-limited" type directly applies to monostrategy-dependent claims (MECH-269, ARC-007) | DEV-NEED-029 (cross-stage) | MECH-269, ARC-007 | 0.83 | suggests missing governance claim |
| Asada et al. 2001 (Robot Auton Syst; DOI:10.1016/S0921-8890(01)00157-9) | Three-tier complexity model; quantitative stage-gate: success rate threshold + state vector dimensionality; premature escalation impedes learning | DEV-NEED-008 transition gate is qualitative; this provides the earliest explicit precedent for quantitative stage-gate criteria in developmental robotics | DEV-NEED-007, DEV-NEED-008 | ARC-019, IMPL-019 | 0.82 | suggests missing governance claim |
| Oudeyer & Kaplan 2007 (Front Neurorobotics; PMID:18958277) | Learning Progress Motivation (LPM = d(PE)/dt); stage is complete when LPM approaches zero; self-organized developmental stage ordering | LPM-based stage-exit criterion gives REE an automatable gate: stage complete when PASS rate improvement rate approaches zero in the current domain | DEV-NEED-003, DEV-NEED-007, DEV-NEED-008 | INV-055, ARC-019 | 0.90 | suggests implementation metric |
| Vernon, von Hofsten & Fadiga 2010 (Springer; DOI:10.1007/978-3-642-16904-5) | 43-guideline roadmap; prerequisite dependency structure with empirical onset/maturity windows; premature bypass of synergy breakdown causes brittle motor control | REE's DEV-NEED prerequisite structure (claim_ids rows) is informal; the roadmap model shows how to formalize prerequisite blocking with onset/maturity windows | DEV-NEED-001 (cross-stage) | ARC-019, INV-060 | 0.87 | refines existing governance practice |
| Diaz-Rodriguez et al. 2018 (NeurIPS WS; arXiv:1810.13166) | BWT (Backward Transfer): negative BWT = catastrophic forgetting / capability regression; FWT = forward facilitation; both required throughout development | REE has no BWT/FWT metric; cross-stage capability regression (e.g., V3 substrate changes degrading V2-validated capabilities) is undetected | DEV-NEED-007, DEV-NEED-012, DEV-NEED-022 | IMPL-019, INV-055 | 0.85 | suggests implementation metric |
| Lesort et al. 2020 (Inf Fusion; DOI:10.1016/j.inffus.2019.12.004) | Curriculum order is not arbitrary; stage-specific criteria must be prospective, not post-hoc; V1->V2->V3 = domain-incremental (strictest regression requirements) | REE's experiment_queue.json format has no `stage_completion_criteria` field; prospective gate criteria are absent from queue entries | DEV-NEED-001 (cross-stage) | ARC-019, IMPL-019 | 0.88 | suggests missing governance claim |
| Baranes & Oudeyer 2013 (Robot Auton Syst; DOI:10.1016/j.robot.2012.05.008) | SAGG-RIAC operationalizes LPM in a physical robot; pre-specified goal spaces cause representational distortion when imposed prematurely | Pre-specified high-complexity experiments (EXQ-460+ SD-033/OCD cluster) before foundational V_s monostrategy is resolved = premature capability advancement | DEV-NEED-003, DEV-NEED-007, DEV-NEED-031 | INV-055, ARC-019 | 0.80 | suggests experiment or review process |
| Mitchell et al. 2019 Model Cards (FAT*; DOI:10.1145/3287560.3287596) | Structured per-model documentation covering intended use, out-of-scope uses, evaluation conditions; must co-release with model | REE's claims.yaml + developmental_needs_register.md together form an informal model card; formalizing them as a co-release substrate document at each V-boundary is recommended | cross-stage | IMPL-018 | 0.95 | supports existing REE governance practice |
| Gebru et al. 2021 Datasheets (Comm ACM; DOI:10.1145/3458723) | 57-question dataset datasheet covering motivation, composition, collection process, maintenance | REE experiment manifests are functionally datasheets for training episodes; mandatory completeness check (beyond queue validation) is indicated | cross-stage | IMPL-018 | 0.92 | refines existing governance practice |
| Raji et al. 2020 SMACTR (FAT*; DOI:10.1145/3351095.3372873) | 5-stage internal audit (Scoping, Mapping, Artifact collection, Testing, Reflection); artefacts produced at each stage are prerequisites for the next | REE's governance pipeline is a SMACTR instantiation; the "Scoping" artefact (formal pre-experiment specification) is currently absent -- /queue-experiment skill provides a partial substitute | cross-stage | IMPL-019 | 0.88 | suggests missing governance claim |
| Liang et al. 2023 HELM (TMLR; arXiv:2211.09110) | Scenario x metric matrix: no single metric permitted alone; mandatory multi-metric assessment for each capability evaluation | REE experiments declare a primary PASS/FAIL outcome; secondary metrics (diversity, calibration) are optional -- a monostrategy PASS with zero behavioral diversity is not flagged | DEV-NEED-005 (cross-stage) | IMPL-019 | 0.85 | suggests implementation metric |
| Bommasani et al. 2024 Transparency Reports (AIES; arXiv:2402.16268) | Periodic structured transparency reports covering development history, training stages, known limitations; satisfies EU AI Act, US EO requirements | REE lacks a formal substrate transparency report at V-boundary transitions; WORKSPACE_STATE.md + V3 spec are informal substitutes | cross-stage | IMPL-018 | 0.87 | suggests missing governance claim |
| Chhetri et al. 2025 (WWW; DOI:10.1145/3701716.3715483) | SEPIO/RDO ontologies: `Assertion -> [n Evidence Lines] -> [n Evidence Items]`; vertical nesting (one claim's evidence_direction feeds as EvidenceItem into a parent claim) | REE's depends_on chains are soft cross-references; computable evidence lineage propagation (confidence change in dependent claim automatically triggers recalculation in parent) is absent | cross-stage | IMPL-018 | 0.82 | suggests missing governance claim |
| CIViC Griffith et al. 2017 / Krysiak et al. 2023 (Nat Genet / NAR) | Two-tier evidence architecture: EvidenceItem (direction + level A-E + quality) + Assertion (aggregated); evidence_level weights aggregation | REE aggregates PASS/FAIL votes without weighting by experimental quality; adding `evidence_level` per manifest (A=mechanistic causal, B=proxy-causal, C=correlational, D=indirect, E=synthetic) would improve exp_conf calibration | cross-stage | IMPL-018, IMPL-019 | 0.91 | suggests implementation metric |
| GRADE Kirmayr et al. 2021 (Medwave; PMID:33830974) | Certainty of evidence: 5 downgrade domains (bias, inconsistency, indirectness, imprecision, publication bias); certainty is a property of the evidence body, not individual studies | REE's exp_conf via vote-counting should apply structured downgrade penalties for inconsistency (conflict_ratio) and indirectness (proxy substrates); these are currently informal | cross-stage | IMPL-018 | 0.88 | refines existing governance practice |
| PRISMA Page et al. 2021 (BMJ; DOI:10.1136/bmj.n71) | Mandatory heterogeneity reporting: effect estimate + certainty separated; conflicts must carry an explanatory account | REE flags conflict_ratio but does not require a `heterogeneity_note` explaining why results diverge; without the note, governance cannot distinguish real contradiction from substrate-version confound | cross-stage | IMPL-018, IMPL-019 | 0.85 | refines existing governance practice |
| Goodman, Fanelli & Ioannidis 2016 (Sci Transl Med; PMID:27252173) | Three reproducibility types: methods, results, inferential; these are logically independent; claim confidence should index to inferential reproducibility | REE supersession policy addresses methods reproducibility; a `confound_flag` field for claims where positive experiments share a design confound that has not been tested out (inferential reproducibility threat) is missing | cross-stage | IMPL-018 | 0.87 | refines existing governance practice |
| Kale et al. 2023 MetaExplorer (CHI; DOI:10.1145/3544548.3580869) | Structured elicitation required before aggregating heterogeneous evidence; commensurability judgment prevents misleading averages | REE's governance pipeline aggregates V1-proxy and V3-mechanistic experiments without a commensurability gate; `evidence_quality_note` is currently optional and post-hoc | cross-stage | IMPL-018, IMPL-019 | 0.80 | suggests experiment or review process |

---

## Part 2: Structural Audit

### 2.1 Register Rows Lacking Claim IDs

Four rows in the developmental_needs_register.md carry the `PROPOSED` marker with no
registered claim IDs:

| DEV-NEED | Description | Gap |
|---|---|---|
| DEV-NEED-028 | Developmental failure-mode tracking | No dedicated claim; covered by ARC-019/INV-043/MECH-158 but failure-mode tracking as a governance practice is not itself a claim |
| DEV-NEED-029 | ARC-065 diversity mechanisms warm-start gate | No claim registered; gate criterion thresholds (ResidueField coverage, MECH-320 EWMA warmup, E3 score variance floor) need empirical calibration from EXQ-ISEF-001 before a Q-claim can be written |
| DEV-NEED-030 | Stage-aware replay scheduling | No claim registered; stage-indexed scheduler not yet implemented; requires substrate work before a formal MECH or SD can be registered |
| DEV-NEED-031 | MECH-124 prevention gate | No claim registered; monostrategy_prevention_score telemetry not implemented; priority is with sleep aggregation cluster |

**Recommended action:** These remain PROPOSED by design until their empirical prerequisites
are met. Governance pipeline should treat them as open gaps, not undocumented work.

---

### 2.2 Developmental Claims Lacking DEV-NEED Mapping

The claims.json audit found 87 developmental-sounding claims not represented in any
DEV-NEED row. Many of these are correctly outside the register's scope (sleep mechanisms,
language pathology, clinical analogy claims). However, the following require register entries
because they are either referenced in developmental_curriculum.md's Related Claims section,
were registered since the register was created (2026-05-16), or are architecturally critical
to existing DEV-NEED gates:

#### Priority 1 -- Maintenance rule violation (claims registered 2026-05-16 without register update)

These were registered after the maintenance rule was established ("Any future developmental
claim must be entered in this register in the same change that registers or modifies the
claim") but are absent from the register:

| Claim ID | Title | Missing DEV-NEED |
|---|---|---|
| ARC-073 | Play-to-real transition triggered by competence saturation, not scheduled duration | DEV-NEED-009 or DEV-NEED-011 (play progression gates) |
| ARC-074 | Infant Phase 0 reward-free Hebbian babbling epoch prior to E3 scoring | Belongs in infant stage (DEV-NEED-001 or a new DEV-NEED-032) |
| MECH-329 | Wanting-before-liking goal seeding sequencing | DEV-NEED-006 (z_goal seeding from accidental benefit) |
| MECH-327 | Play signal as regulatory punctuation broadcast | DEV-NEED-009 or DEV-NEED-012 |
| MECH-328 | Ongoing monitoring protocol architecture (bilateral frame) | DEV-NEED-013 (games-with-rules) |
| ARC-075 (if registered) | Any new 2026-05-16 ARC claims | Audit at each governance cycle |

#### Priority 2 -- Referenced in developmental_curriculum.md but absent from register

| Claim ID | Title | Relevance | Suggested mapping |
|---|---|---|---|
| ARC-042 | E3 is functionally dark until E1/E2 substrate development is complete | Critical developmental staging prerequisite; cited in curriculum Related Claims | DEV-NEED-019 or new DEV-NEED-032 |
| ARC-059 | Three-stage cognitive development ordering (self-as-object, objects-as-patterns, others-as-special-objects) | Refines ARC-019 curriculum gates with explicit ordering | DEV-NEED-021 (otherness after self-stability) |
| INV-041 | Childhood phase as architectural prerequisite for ARC-041 (ContextMemory) | Cited throughout curriculum | DEV-NEED-009 (play-dominant childhood) |
| INV-049 | Offline phases as mathematical necessity for model-building agents | Architectural grounding for DEV-NEED-007 | DEV-NEED-007 (offline integration between stages) |
| INV-061 | Frame distinction undertrained -> derealization, PTSD, mania, anxiety | Developmental consequence of failed pretend play | DEV-NEED-012 (pretend play failure mode) |

#### Priority 3 -- Indirectly developmental but not critical to register completeness

Claims like MECH-121/122 (NREM sleep phase mechanisms), MECH-165 (replay diversity), MECH-163
(dual goal-directed systems), INV-047/062 (clinical development analogies) are relevant to
sleep and developmental sleep scheduling but primarily belong in the sleep substrate documents
rather than the register unless they gate a specific DEV-NEED stage transition.

---

### 2.3 Experiments Lacking Developmental Traceability

**Current state (from experiment_proposals.v1.json audit, 2026-05-16):**

| Category | Count | DEV-NEED citations | % with DEV-NEED |
|---|---|---|---|
| Total proposals | 317 | 5 (EXP-IDEV-001..005) | 1.6% |
| Status=proposed | 180 | 5 | 2.8% |
| Status=executed | 128 | 0 | 0% |
| V3 experiment scripts (~574 queue entries total) | ~574 | 0 | 0% |
| experiment_queue.json entries | varies | 0 | 0% |

The 5 EXP-IDEV proposals (from replay_development_analysis.md, registered 2026-05-16) are
the only proposals that explicitly cite DEV-NEED IDs. This is not a compliance failure -- the
requirement that experiments cite DEV-NEED IDs was not in force until today's maintenance rule
update. However, the pattern has a governance consequence: there is no way to ask "which
experiments validate DEV-NEED-003's gate criterion?" without manually cross-referencing.

**Recommended action:** When EXP-IDEV experiments are promoted to queue entries via
/queue-experiment, the `dev_need_ids` field should be preserved. For future experiments
targeting developmental gates, include DEV-NEED IDs in `claim_ids` (list) or in a separate
`dev_need_ids` field in the manifest.

---

### 2.4 Contradictions and Naming Inconsistencies Between Developmental Documents

#### Contradiction 1: Cold-start vs. warm-start terminology

- `monostrategy_developmental_analysis.md` §1.2 uses "cold-start substrate" as the
  mechanism of monostrategy failure
- `DEV-NEED-029` uses "warm-start gate" as the needed intervention
- These describe the same phenomenon from opposite directions (the failure vs. the fix),
  but using different terms in different documents creates cross-reference confusion.

**Resolution:** Both documents are correct. Standardize: the phenomenon is "cold-start
failure"; the gate is the "warm-start gate". Document both terms in DEV-NEED-029 open
questions. No claims change required.

#### Contradiction 2: DEV-NEED-006 and DEV-NEED-008 gate operationalization

- DEV-NEED-006 states that `z_goal.norm() > infant_goal_threshold` must hold, but the
  open question notes "threshold not standardized"
- DEV-NEED-008 uses the SAME gate criterion (`z_goal.norm() > infant_goal_threshold`) for
  the infancy-to-childhood transition gate
- `developmental_metrics.md` lists this as a BLOCKING gate with threshold 0.4 for DEV-NEED-006

**Resolution:** The developmental_metrics.md threshold (0.4) should be canonical and back-
referenced in both DEV-NEED-006 and DEV-NEED-008 open questions. No new claim needed; update
the open questions text in the register to point to developmental_metrics.md.

#### Contradiction 3: Play-frame monitoring -- ongoing vs. open/close

- DEV-NEED-013 states that games-with-rules requires "ongoing shared-state monitoring"
- The register's Gap Log explicitly notes "Q-035 is unresolved: games-with-rules text
  implies ongoing monitoring; the minimal ARC-049 mechanism may still be open/close only"
- play_substrate_design.md (Section 13) concludes that Q-035 is resolved: "continuous
  monitoring is primitive from 2-3 months; what escalates is content complexity"
- developmental_needs_register.md (Gap Log, Contradictions section) still lists Q-035 as
  unresolved

**Resolution:** Q-035 is resolved per play_substrate_design.md and claims.yaml (status:
resolved). Update the DEV-NEED-013 open question and the Gap Log Contradictions entry to
reflect the resolution. The monitoring requirement is not a contradiction -- continuous
monitoring is the correct answer; the open question was about its minimal implementation.

#### Contradiction 4: ARC-073 not in play type progression table

- `developmental_curriculum.md` play type progression table (MECH-197) lists 5 play types
  with prerequisite ordering; none mention ARC-073's competence-saturation trigger
- `ARC-073` (registered 2026-05-16) states the play-to-real transition is triggered by
  competence saturation, not scheduled duration -- this contradicts an implicit assumption
  in the curriculum that the transition is curriculum-scheduled

**Resolution:** ARC-073 refines (does not contradict) the curriculum. The curriculum describes
what stages exist; ARC-073 specifies the trigger mechanism. Update DEV-NEED-009 or add a
register row for ARC-073 clarifying that it governs the within-play transition trigger.

---

### 2.5 Orphaned Developmental Ideas

These are developmental specifications present in architecture documents but not linked
to the developmental register or experiment proposals:

| Document | Orphaned item | Suggested link |
|---|---|---|
| infant_substrate_expansion.md | 5 substrate features (harm gradient, microhabitat zones, transient benefit patches, directional wind, dynamic seeds) -- in substrate_queue.json but no DEV-NEED link | DEV-NEED-003 (valence map formation) or DEV-NEED-004 (protected harm exposure) |
| infant_substrate_expansion.md | 4-phase infant curriculum (Phase 0 warmup, Phase 1 harm gradient, Phase 2 benefit differentiation, Phase 3 goal seeding) -- not cross-linked to DEV-NEED row or gate criteria | DEV-NEED-001 through DEV-NEED-008 |
| replay_development_analysis.md | §6.1-6.4 stage-specific replay parameter tables (infant: coverage_floor >= 0.6; childhood: play:real >= 1:1; adult: RPE_weight = 0.6) -- these define DEV-NEED-030 but the document does not cross-link to the register row | DEV-NEED-030 |
| monostrategy_developmental_analysis.md | §4 causal hypothesis ranking (14 hypotheses, 6 falsifiers) -- no explicit link to which DEV-NEED gate each hypothesis tests | DEV-NEED-029 (warm-start gate calibration) |
| developmental_metrics.md | DEV-NEED-010 through DEV-NEED-014 V3 proxy gates -- not cross-referenced back to register rows (register says "see developmental_metrics.md" but the link is one-way) | DEV-NEED-010 through DEV-NEED-014 |
| play_substrate_design.md | MECH-327, MECH-328, ARC-073, Q-048--Q-051 (new claims registered during play design) -- no DEV-NEED register rows added | ARC-073 -> DEV-NEED-009; MECH-327/328 -> DEV-NEED-012/013; Q-048--Q-051 -> respective rows |

---

### 2.6 Duplicate or Near-Duplicate Developmental Claims

No true duplicate claims found. The following near-duplicates are correctly distinct but
risk creating confusion at governance review:

| Claims | Apparent overlap | Actual distinction | Risk |
|---|---|---|---|
| DEV-NEED-015 (caregiver protection) and DEV-NEED-016 (caregiver frame-maintenance) | Both reference INV-043 and MECH-199 | Different developmental phases: protection is infant, frame-maintenance is childhood | Readers may conflate them; both should explicitly state their stage in the Description column |
| INV-055 appears in 8 DEV-NEED rows (001--008) | Load-bearing across entire infant stage | Correct -- INV-055 is the architectural invariant for the infant stage as a whole | Single-point-of-failure: if INV-055 is demoted, all 8 infant-stage gates are affected simultaneously; annotate this dependency in the register |
| ARC-019 appears in 10+ DEV-NEED rows | REE developmental curriculum claim appears everywhere | Correct -- ARC-019 is the parent architectural commitment | Same SPoF risk as INV-055; the register should make this explicit |

---

## Part 3: Register Maintenance Assessment

The developmental_needs_register.md was created on 2026-05-16 (today) and has already
received four updates in the same session. This section assesses whether the current
register structure is adequate for long-term maintenance.

### 3.1 Status Vocabulary -- Adequate

The five-tier status vocabulary (Specified / Claimed / Narrative gate / Implementation-ready /
V3 proxy only / Requires V4 / PROPOSED) is correct and sufficient. No changes recommended.

### 3.2 Priority/Readiness Column -- Adequate

The existing column values (Now / After V_s diversity / Requires play substrate / Requires V4
multi-agent / V3 proxy only / Governance only) correctly reflect the substrate dependency
ordering. No changes recommended.

### 3.3 Stage Coverage Summary -- Adequate

The four-tier summary (Infant / Childhood-play / Social-language-adult / Cross-stage) with
DEV-NEED range anchors is correct. Two additions required:

- ARC-074 (Phase 0 babbling epoch) belongs under Infant, before DEV-NEED-001, or as a new
  row in the Infant block
- ARC-042 (E3 dark until E1/E2 ready) belongs as a note under the Stage Coverage Summary:
  it is an architectural prerequisite that applies across Stages 0-2

### 3.4 Generated Index Integration -- MISSING

The developmental_needs_register.md has no mechanism linking to the generated
claim_evidence.v1.json index or to the promotion_demotion_recommendations.md. As a result:

- When a DEV-NEED's core claims gain experimental confidence, the register does not
  automatically reflect this progress
- When a DEV-NEED's core claims are demoted, the register does not automatically flag that
  its gate criterion may have lost its evidentiary basis

**Recommended addition:** Add a "Evidence state (last governance cycle)" column showing
the current exp_conf and status of each row's primary claim ID. This would be populated
manually at each governance cycle rather than auto-generated (acceptable given the register's
role as an audit-oriented rather than auto-generated document).

### 3.5 Maintenance Rules -- Requires Strengthening

The current maintenance rules are broadly correct but the audit reveals two gaps:

**Gap A: Rules do not specify which document takes precedence when documents disagree.**
During today's session, Q-035 was marked resolved in play_substrate_design.md and claims.yaml,
but the register's Contradictions section was not updated. The maintenance rule should
specify: when claims.yaml carries a status change (e.g., Q-035: resolved), the register
must be updated in the same governance pass.

**Gap B: Rules do not specify a review cadence.**
The register is a point-in-time document that accumulates staleness. A quarterly or per-
governance-cycle review should be required to update evidence state, close resolved items,
and catch new claims that should have been added.

---

## Part 4: Governance Update Proposals

### Proposal G1: Add `registration_rationale` field to claims.yaml

**Grounded in:** Gotel & Finkelstein 1994; Ramesh & Jarke 2001  
**Priority:** Medium  
**Description:** Add an optional but governance-encouraged `registration_rationale` field to
each claims.yaml entry, capturing the biological, clinical, or experimental motivation that
led to the claim's registration. Without this, governance cannot distinguish data-sparse
demotion from superseded-rationale demotion after session transitions.  
**Format suggestion:**
```yaml
registration_rationale: "Surfaced by EXQ-573 null result (2026-05-16); analogous to
Gotel/Finkelstein pre-RS traceability failure. Clinical analog: Alzheimer's reverse-
dependency staging (INV-047)."
```
**Impact:** Low implementation cost; high audit value across multi-session parallel work.

---

### Proposal G2: Backward traceability check in governance pipeline

**Grounded in:** IEC 61508-3:2010; Hayes et al. 2003  
**Priority:** High  
**Description:** Add a `check_backward_traceability.py` script (parallel to
`validate_queue.py`) that detects experiment run IDs present in `evidence/experiments/`
with no `claim_ids_tested` tag in their manifest, and surfaces them as a governance warning.
Forward traceability (every claim should have experiments) is already enforced via
pending_review. Backward traceability (every experiment has a claim it updates) is not.  
**Implementation note:** The script would scan all manifest.json files under
`evidence/experiments/runs/`, check for `claim_ids_tested` presence, and report any
manifests with empty or missing tags as `unlinked_run_ids`.

---

### Proposal G3: `evidence_level` field in experiment manifests

**Grounded in:** CIViC Griffith et al. 2017; Krysiak et al. 2023  
**Priority:** Medium  
**Status: IMPLEMENTED 2026-05-16** — `evidence_level` field added to `RunRecord`, `_scan_runs`,
per-claim entry dict, and `evidence_level_counts` in claim-level aggregation summary in
`evidence/experiments/scripts/build_experiment_indexes.py`. Field is optional and backward-
compatible; manifests without it default to level C. Confidence weighting by level is deferred
to a future governance cycle.  
**Description:** Add an optional `evidence_level` field (A-E scale) to experiment manifests,
allowing the aggregator to weight strong mechanistic experiments above weak proxy experiments:

| Level | Meaning | Example |
|---|---|---|
| A | Strong mechanistic: direct causal isolation, multi-seed, clean criteria | EXQ-565 PASS (GAP-8 routing consumer) |
| B | Proxy-causal: causal argument with known limitations | V3 single-agent proxy for caregiver function |
| C | Correlational: outcome correlates with claim prediction | Early V2 substrate results (default) |
| D | Indirect: logically related but not directly testing the mechanism | |
| E | Synthetic: test environment only, not representative substrate | Old ree-v2 synthetic runs |

Currently all PASS/FAIL votes are treated as co-equal regardless of substrate quality.
Level E evidence should carry near-zero weight; Level A should carry full weight.

---

### Proposal G4: Mandatory `heterogeneity_note` for claims with conflict_ratio > 0.3

**Grounded in:** PRISMA Page et al. 2021; GRADE Kirmayr et al. 2021  
**Priority:** Medium  
**Status: IMPLEMENTED 2026-05-16** — G4 check added to
`evidence/experiments/scripts/build_experiment_indexes.py` in
`_write_promotion_demotion_recommendations()`. For every active claim in `scoped_claims`
with `conflict_ratio > 0.3`, the function checks whether `heterogeneity_note` is present
and non-empty in `claim_registry`. Missing notes are collected and emitted as a "G4:
Heterogeneity Warnings" section at the end of `promotion_demotion_recommendations.md`
with a tabular list (claim_id | status | conflict_ratio) and a summary WARNING line.
Claims with a note present are not flagged. The check is a documentation gate only —
it does not block promotion. Five example notes were added to the highest-entry-count
high-conflict claims (ARC-016, MECH-071, MECH-095, MECH-102, ARC-033) using the
classification vocabulary: substrate-version confound, methodological divergence,
genuine scientific contradiction.  
**Description:** Claims entering a governance cycle with `conflict_ratio > 0.3` must
carry a `heterogeneity_note` field in claims.yaml explaining the divergence before the
cycle's promotion/demotion recommendation is issued. The note should classify the
conflict as one of: substrate-version confound, methodological divergence,
genuine scientific contradiction, or supersession lag.  
**Note:** The existing `evidence_quality_note` field serves a related purpose but is
optional and not conflict-triggered. This proposal makes a structured conflict explanation
mandatory before governance action, rather than a post-hoc annotation.

---

### Proposal G5: Pre-experiment Assurance Claim Point (ACP) in queue entries

**Grounded in:** AMLAS Hawkins et al. 2021; Bloomfield & Rushby 2020; Lesort et al. 2020  
**Priority:** Medium  
**Description:** Experiment queue entries (via /queue-experiment skill) should include a
brief pre-declared ACP specifying: (a) which claim the experiment tests, (b) what constitutes
sufficient evidence (PASS criterion), and (c) which defeaters the experiment addresses
(expected failure modes). This does not require changes to the queue schema -- it can be
encoded in the existing `hypothesis` or `description` field. The /queue-experiment skill
template should be updated to require this structure.  
**Relationship to existing practice:** The mandatory docstring + smoke test pattern in
/queue-experiment already partially implements this; the ACP formalizes what "sufficient
evidence" means before the experiment runs.

---

### Proposal G6: Add `dev_need_ids` field to experiment proposals for developmental experiments

**Grounded in:** structural audit finding (2.3 above); Lesort et al. 2020  
**Priority:** Medium (for developmental experiments specifically)  
**Description:** Experiment proposals targeting developmental gates should include a
`dev_need_ids` list field (parallel to `claim_ids`) in experiment_proposals.v1.json and
in experiment manifests. This enables the governance pipeline to answer: "which experiments
provide evidence for DEV-NEED-003's gate criterion?"  
**Scope:** Only developmental experiments (EXP-IDEV series, EXQ-ISEF series) require this
field. General substrate experiments (EXQ-NNN) do not need it. The field is already used by
EXP-IDEV-001 through EXP-IDEV-005 as a template.

---

### Proposal G7: Substrate transparency report at V-boundary transitions

**Grounded in:** Bommasani et al. 2024; Mitchell et al. 2019; Raji et al. 2020 SMACTR  
**Priority:** Low (forward-planning)  
**Description:** At each major substrate version boundary (V3->V4), produce a formal
"REE Substrate Transparency Report" with mandatory sections:
1. Implemented SDs and their validation status
2. Promoted/demoted/held claims since the prior boundary
3. Developmental stage coverage (DEV-NEED row status)
4. Open governance gaps and PROPOSED rows
5. Known limitations and substrate ceiling claims
6. Intended next-version changes

This would formalize what the V3-spec, sleep substrate plan, and WORKSPACE_STATE.md
already capture informally. The report would be versioned and archived alongside the
V3/V4 code boundary commit.

---

### Proposal G8: Argument-type tag for claims

**Grounded in:** Lee et al. 2026; Bloomfield & Rushby 2020; Burton & Herd 2023  
**Priority:** Low (conceptual)  
**Description:** Add an optional `argument_type` tag to claims.yaml entries:

| Tag | Meaning | Closure requirement |
|---|---|---|
| `assertion_based` | Claim is a positive assertion about behavior | Behavioral experiment evidence can close |
| `constraint_based` | Claim is a constraint that must hold | Ablation/violation experiment required |
| `capability_limited` | Claim's testability depends on the policy's exploration breadth being sufficient | DEV-NEED-029 warm-start gate must be confirmed before experiments are authoritative |

The `capability_limited` tag is the highest-priority addition: monostrategy-dependent claims
(MECH-269, ARC-007, ARC-016) should carry it, preventing governance from treating null
results as evidence when the warm-start gate has not been confirmed.

---

## Part 5: Proposed Maintenance Rule Amendments

The following amendments are proposed for `developmental_needs_register.md`'s Maintenance
Rules section:

### MA-1: Claims.yaml status takes precedence in conflicts

> When a claim referenced in this register changes status in `claims.yaml` (e.g., a Q-claim
> is resolved, an open question is closed), the register row's open questions and gap log
> must be updated in the same governance pass that updates claims.yaml. Do not leave the
> register's narrative inconsistent with the canonical claim status.

**Grounded in:** Q-035 resolved in play_substrate_design.md and claims.yaml but register Gap
Log not updated (detected in today's audit).

### MA-2: Quarterly evidence-state review

> At each governance cycle that includes a full claims walk (typically quarterly), update
> the "Current status / maturity" column of each register row to reflect the current exp_conf
> and any promotion/demotion decisions applied to that row's primary claims. Mark rows as
> "Promoted" or "Demoted" if the underlying claim has changed tier; mark them "Evidence
> advancing" if exp_conf has increased since the last review.

**Grounded in:** Lesort et al. 2020 (prospective criteria must be revisited); Ramesh & Jarke
2001 (rationalization links deteriorate without maintenance cadence).

### MA-3: New developmental claims require register update on registration day

> Any claim registered in claims.yaml whose title or description contains developmental
> language (infant, childhood, play, curriculum, stage, caregiver, loveability, repertoire,
> babbling, pretend, rules, cooperative, neoteny) must have a register row (or an update to
> an existing row) in the same commit that adds the claim to claims.yaml. If the claim is
> V4-only and no appropriate register row exists, add it under the relevant stage with
> status "Requires V4 multi-agent" and a PROPOSED gate.

**Grounded in:** today's audit finding that ARC-073, ARC-074, MECH-329, MECH-327, MECH-328
were registered without register updates (priority 1 in section 2.2).

### MA-4: Orphaned claims flag at governance cycle

> At each governance cycle, run a check comparing claims.yaml entries with the register's
> claim ID column. Any claim with `claim_type: architectural_commitment OR mechanism_hypothesis`
> that is developmental (by MA-3's keyword filter) and absent from the register should be
> flagged as a candidate new row. The check can be a simple grep; no tooling required.

**Grounded in:** Mader et al. 2013 (orphaned artifacts as a recurring safety traceability
problem).

### MA-5: Single-point-of-failure annotate load-bearing claims

> Claims appearing in 5 or more DEV-NEED rows (currently INV-055 and ARC-019) must carry
> an explicit note in the register header: "INV-055 is the single architectural claim
> grounding all 8 infant-stage DEV-NEED rows. A demotion of INV-055 requires governance
> review of all 8 rows." This ensures the dependency chain is visible to any reviewer.

**Grounded in:** IEC 61508-3:2010 (change-impact analysis requirement); Ramesh & Jarke 2001
(evolution link type captures propagation risk).

---

## Part 6: Immediate Actionable Findings

### Action A1 (HIGH): Update DEV-NEED register for 2026-05-16 claim registrations

Maintenance rule MA-3 violation. The following need register rows added or updated today:
- **ARC-074** (Phase 0 babbling epoch): add to Infant stage block; status = Claimed, priority = Now (precedes DEV-NEED-001)
- **MECH-329** (wanting-before-liking sequencing): add to DEV-NEED-006 Open questions or as a note in the gate criterion
- **ARC-073** (competence-saturation play-to-real transition): add to DEV-NEED-009 or 011 open questions
- **MECH-327/328** (play signal punctuation, ongoing monitoring protocol): cross-link to DEV-NEED-012/013

### Action A2 (HIGH): Resolve Q-035 contradiction in register Gap Log

Q-035 is resolved (status: resolved in claims.yaml and play_substrate_design.md). The
register's Contradictions section still lists it as unresolved. Update the Gap Log to
note Q-035 resolution and update DEV-NEED-013's open question.

### Action A3 (MEDIUM): Standardize z_goal threshold reference

DEV-NEED-006 and DEV-NEED-008 both mention "infant_goal_threshold" without specifying the
value. developmental_metrics.md provides 0.4 as the blocking threshold. Add a cross-reference
to developmental_metrics.md in both rows' Gate criterion column.

### Action A4 (MEDIUM): Add ARC-042 and INV-041 to register

Both are cited in developmental_curriculum.md Related Claims but absent from the register.
ARC-042 belongs near DEV-NEED-019 (responsibility expansion) or as a new cross-stage row.
INV-041 belongs as a cross-reference note in DEV-NEED-009 (play-dominant childhood).

### Action A5 (LOW): Link infant_substrate_expansion.md features to DEV-NEED rows

The 5 substrate features in infant_substrate_expansion.md §4 (harm gradient, microhabitat
zones, transient benefit patches, directional wind, dynamic seeds) support DEV-NEED-003 and
DEV-NEED-004 respectively. Add a one-line file link to those rows' Evidence/file links column.

---

## Part 7: Summary Scorecard

| Governance dimension | Current state | Gap severity |
|---|---|---|
| Register rows with claim IDs | 27/31 (87%); 4 PROPOSED | Low -- PROPOSED by design, not by neglect |
| Developmental claims in register | 45/87 developmental claims (52%) | Medium -- 42 uncovered; 6 are priority-1 maintenance violations |
| Experiments citing DEV-NEED IDs | 5/317 proposals (1.6%) | Medium -- rule only just established; not retroactive |
| Register-claim consistency | Q-035 open/resolved mismatch; 6 new claims without register updates | High -- maintenance rule violation on day 1 |
| Document-to-document consistency | Cold-start/warm-start naming; z_goal threshold unstandardized; ARC-073 not in curriculum table | Low-medium -- all clarifiable without new claims |
| Backward traceability | Not automated | Medium -- forward traceability (pending_review) is solid; backward is missing |
| Evidence quality weighting | Uniform PASS/FAIL vote counting | Medium -- no evidence_level field; proxy and mechanistic experiments are co-equal |
| Governance rationalization links | Absent from claims.yaml | Medium -- `evidence_quality_note` is informal; no structured defeater register |
| Substrate transparency documentation | Informal (WORKSPACE_STATE.md + V3 spec) | Low -- adequate for current project phase; critical before external publication |
| Argument-type tagging | Absent | Low -- adds value for monostrategy-dependent claims |

---

## Appendix: Literature Sources Index

| Topic | Sources |
|---|---|
| Requirements traceability | Gotel & Finkelstein 1994 (ICRE); Ramesh & Jarke 2001 (IEEE TSE); Hayes et al. 2003 (RE '03); Mader et al. 2013 (IEEE Soft); Rempel & Mader 2017 (IEEE TSE); IEC 61508-3:2010 |
| Assurance cases / AI safety cases | Kelly 1998 (York thesis); Bloomfield & Rushby 2020 (arXiv:2004.10474); Hawkins et al. 2021 AMLAS (arXiv:2102.01564); Ashmore et al. 2021 (ACM CSUR); Burton & Herd 2023 (Front Comput Sci); Lee et al. 2026 (arXiv:2601.22773) |
| Developmental robotics governance | Asada et al. 2001 (Robot Auton Syst); Oudeyer & Kaplan 2007 (Front Neurorobotics); Vernon et al. 2010 (Springer); Diaz-Rodriguez et al. 2018 (NeurIPS WS); Lesort et al. 2020 (Inf Fusion); Baranes & Oudeyer 2013 (Robot Auton Syst) |
| Model cards / system cards | Mitchell et al. 2019 (FAT*); Gebru et al. 2021 (Comm ACM); Raji et al. 2020 SMACTR (FAT*); Liang et al. 2023 HELM (TMLR); Bommasani et al. 2024 (AIES) |
| Claim-evidence traceability / evidence-based requirements | Chhetri et al. 2025 (WWW); CIViC 2017/2023 (Nat Genet / NAR); GRADE Kirmayr et al. 2021 (Medwave); PRISMA Page et al. 2021 (BMJ); MetaExplorer Kale et al. 2023 (CHI); Goodman et al. 2016 (Sci Transl Med) |

