# Thought Intake: Offline Representational Reindexing & Counterfactual Model Comparison

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md`
**Session:** loop-ti-offline-reindex-bzimqu (worktree), 2026-08-25

## Verbatim prompt (core proposal)

> When representational primitives change, significant past episodes may need to be reinstated
> and reindexed so that they remain accessible under both their historical representation and the
> system's newer ontology.

> This should not mean rewriting history. The original episode, its source and its original
> representation should remain recoverable. Reindexing would add a new relationship or
> interpretation, with versioning and rollback.

The thought develops three linked ideas. First, perception organises experience into
representational "buckets" (prototypes, attractor basins, schemas, relational partitions, latent
task states) whose number and organisation can change through learning (split, merge, or a
previously unintelligible group of experiences becoming intelligible through a new primitive);
when that happens, memory indexed under the old scheme needs an explicit, additive, versioned
reindex rather than a silent overwrite. Second, a learned attractor carries several separable
quantities (predictive reliability, epistemic confidence, familiarity, affective valence,
salience, action urgency, self-relevance, source confidence); if these conflate, a strongly
valenced and precise attractor stops being a hypothesis and becomes the lens through which further
evidence is perceived, retrieved, and replayed -- a self-reinforcing loop in which
attractor-generated replay is miscounted as independent confirming evidence. Third, an offline
(or waking) counterfactual-replay process could interrupt that loop: preserve anchored evidence
separately from its interpretation, temporarily de-weight the dominant attractor, construct
bounded alternative explanatory models, replay the SAME evidence through all of them to generate
discriminating predictions, and validate any resulting reindex against held-out or later waking
evidence before granting it authority -- with every derived item provenance-linked to its origin
so that repeated simulations of one episode cannot be counted as multiple independent samples.

The thought is explicit throughout that this is proposed integration across known components, not
a claim that any single biological process has been demonstrated to do all of this, and its own
"Evidential boundary" section lists what biology does and does not yet establish (see the novelty
table's psychosis rows below).

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| Representational "buckets" (number/granularity/organisation) change through experience | **MECH-496** (2026-08-23): representational dimensionality is an OUTCOME of a developmental plasticity schedule, not an architectural constant -- ContextMemory-slot-count framing, near-verbatim "buckets" language. | Already owned. Cross-ref only; MECH-513 below treats it as the change driver, not re-asserted. |
| "No rewriting history... versioning and rollback" for consolidated memory | **MECH-392 / INV-080** (2026-06-10 V4 memory-lifecycle cluster): raw-episode preservation + provenance/contradiction-flag/rollback layer over CONSOLIDATION (abstraction of content), plus a planned 6-state lifecycle store (retained/indexed/summarised/consolidated/contested/retired). | Already owned for the ABSTRACTION-fault case. The raw thought's actual leading case -- the INDEXING SCHEME itself changing while content is untouched -- is a distinct failure and is NOT covered by MECH-392/INV-080 as written. **Genuinely new for that distinct case -> registered as MECH-513**, explicitly generalising INV-080's preservation principle rather than duplicating MECH-392's abstraction-fault scope. |
| Attractor carries several separable quantities (reliability, confidence, familiarity, valence, salience, urgency, self-relevance, source) whose conflation turns it into a perceptual lens | **ARC-115** (confidence-readout non-collapse across propositional confidence / attractor stability / cross-subsystem agreement / conflict pressure / action-readiness / social agreement) and **MECH-430** (multi-dimensional provenance source vector across perceived-vs-imagined / who / when / modality) cover adjacent but different axis sets and different problems (social-vs-internal channel separation; source attribution specifically). Neither covers the attractor's own carried-property set as such. | Adjacent, not a duplicate. **Genuinely new -> registered as ARC-132**, wired to both as siblings-with-a-different-cut. |
| Offline counterfactual replay: preserve evidence, de-weight dominant attractor, construct bounded alternatives, replay same evidence through all, validate against held-out/waking evidence, tag every derived item for anti-circularity, require replay-selector independence | **MECH-269** (V3-live single-anchor verisimilitude reset + strengthened-tag probe channel), **MECH-094** (categorical sim/real write gate), **MECH-264/265** (frontopolar counterfactual-VALUE tracking for action alternatives, not explanatory-model comparison), **ARC-014** (Default Mode safe imagination), **MECH-392** (consolidation provenance/anti-circularity, different content class). None of these performs cross-model comparison of the SAME preserved evidence to generate discriminating predictions. | Built from existing ingredients but assembled into something none of them individually is. **Genuinely new -> registered as MECH-514.** |
| Handoff states: `contested`, `pending_reindex`, `under_offline_review`, `provisionally_reindexed`, `validated`, `rollback_required` | The planned 6-state memory-lifecycle store already has `contested`. The other four are not in the existing model. | Partial overlap. Not registered as a separate claim -- flagged as reconciliation work for a future V4 build pass in the new architecture doc (Section 3), not claim-shaped on its own. |
| Biological grounding survey (DG/CA3 pattern separation, CA1 comparator, OFC hidden-state, frontopolar forgone-alternative tracking, source/reality monitoring, schema-primed assimilation, SWR-spindle-SO coupling, synaptic renormalisation, 2025/2026 drift studies) | Individually anchors existing REE claims (MECH-147 DG separation, MECH-269 anchor selection, source-monitoring claim at claims.yaml:34823, INV-039 schema-primed assimilation, sleep-consolidation cluster). The thought does not propose new REE content here -- it corroborates existing mechanisms with literature. | Not new REE content; literature corroboration only (per `feedback_lit_exp_decoupled` -- literature corroboration does not by itself strengthen an existing claim's confidence). Not registered. |
| Psychosis / circular-inference material (Jardri & Deneve 2013, Powers/Mathys/Corlett 2017, Howes et al. 2011) and machine-learning precedents (latent replay drift, generative-replay model collapse) | Cited by the raw thought itself as **failure-mode inspiration only** -- its own "Evidential boundary" section explicitly declines to assert psychosis is one unitary precision failure, that axis-conflation is its demonstrated mechanism, or that counter-attractor replay is a demonstrated function of dreaming. **MECH-244** (psychosis = precision-weighting self-sealing failure) and **ARC-086** (failure-mode taxonomy axes) already own the psychosis material at the level REE currently asserts it. | Correctly left unclaimed by the raw thought's own discipline. Cited in ARC-132/MECH-514's notes as motivating inspiration, not asserted as mechanism. Not separately registered. |

## Key formulations (verbatim, load-bearing)

> An episode organised under an earlier representational system may no longer be correctly
> located or interpreted by the current one.

> Something can be emotionally urgent without being epistemically reliable, familiar without being
> externally sourced, or action-relevant without being a good general explanation.

> attractor -> biased perception and retrieval -> attractor-consistent derived material ->
> selective replay -> apparent confirmation -> stronger attractor.

> The central danger is that material generated or interpreted through the attractor is counted
> as independent evidence for it.

> The counterfactual is therefore a question posed to the model, not evidence about what occurred.

> Repeated simulations derived from one episode must not become multiple independent samples.
> Every derived item requires provenance linking it to its originating evidence and generating
> model. This is an epistemic anti-circularity requirement.

> Sleep or another protected offline state may allow a system to revise the representational
> primitives through which experience is organised while preserving the evidence itself.

## Affected existing claims

- **MECH-496** -- cited as the change driver MECH-513 responds to; not amended, not re-asserted.
- **MECH-392 / INV-080** -- explicitly distinguished from MECH-513 (abstraction-fault scope vs.
  indexing-scheme-change scope); neither amended.
- **ARC-115 / MECH-430** -- explicitly distinguished from ARC-132 (different axis sets, different
  problems); neither amended.
- **MECH-269** -- named as the nearest existing V3-live substrate for MECH-514, extended in kind
  (single-anchor -> multi-model comparison), not restated or amended.
- **MECH-264 / MECH-265** -- explicitly distinguished from MECH-514 (action-value arbitration vs.
  explanatory-model comparison); neither amended.
- **MECH-244 / ARC-086** -- cited only as the psychosis material REE already owns at its current
  assertion level; not amended, not extended.

No existing claim's status, confidence, or evidence record was touched.

## Candidate claims -- REGISTERED this pass (not "for future registration")

- **ARC-132** -- `representation.attractor_property_differentiation`. `claim_type:
  architectural_commitment`, `status: candidate`, `epistemic_category: substrate_conditional`
  (set explicitly), `implementation_phase: v4`, `version_relevance: v4_v5`. `depends_on`:
  ARC-115, MECH-430, MECH-244 (all distinguished-from in the depends_on comments).
- **MECH-513** -- `memory.representation_version_reindexing`. Same status/category/phase pattern.
  `claim_type: mechanism_hypothesis`. `depends_on`: MECH-496, INV-080, MECH-392, MECH-147,
  MECH-154, ARC-039.
- **MECH-514** -- `hippocampal.counterfactual_replay_model_comparison`. Same status/category/phase
  pattern. `claim_type: mechanism_hypothesis`. `depends_on`: MECH-269, MECH-094, MECH-264,
  MECH-265, ARC-014, MECH-392, MECH-513, ARC-132.

All three: `polarity: asserts`, `registered_utc: 2026-08-25`. Compass / architectural framing
only -- promote/demote and `narrow_open_question` are suppressed by the explicit
`epistemic_category: substrate_conditional`; none of the three should be read as a V3 build
authorization. Full comparison against existing machinery, and the explicit "out of scope" list,
is in the new architecture doc
`docs/architecture/offline_representational_reindexing.md`.

## Next steps

1. **Literature pull, before hardening any of the three claims further**: none of the sources the
   raw thought cites were independently verified in this pass (see the architecture doc Section 4
   for the full list). Jardri & Deneve 2013 / Powers, Mathys & Corlett 2017 / Howes et al. 2011
   (psychosis, failure-mode inspiration only, do not harden into a mechanism claim without a
   dedicated review), Pellegrini et al. 2019 (latent replay drift, motivates MECH-513), Shumailov
   et al. 2024 (model collapse, motivates MECH-514's anti-pseudo-replication requirement).
2. **Handoff-state reconciliation**: the raw thought's proposed states (`pending_reindex`,
   `under_offline_review`, `provisionally_reindexed`, `rollback_required`, plus the already-shared
   `contested`) against the existing planned 6-state memory-lifecycle model
   (`evidence/planning/memory_lifecycle_v4_plan.md` MEM-5) is real design work, not attempted in
   this registration -- flagged in the architecture doc Section 3.
3. **Version-routing decision**: all three registered claims are parked `v4`/`substrate_conditional`
   by default, per standing practice for thought-intake registrations. A future `/governance`
   cycle can route any of them explicitly if a cheap, non-degenerate V3 test becomes available;
   none is obviously cheap today (MECH-514 in particular depends on MECH-269's own V3 status,
   which is still `v3_pending`).
4. **REM-vs-NREM architectural placement** for MECH-514's substrate (thought section "Waking and
   sleep") is explicitly flagged by the raw thought itself as more speculative for the REM half;
   not registered as a claim, noted in the architecture doc Section 3.
5. Raw thought file
   `docs/thoughts/2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md`
   marked `Status: processed` with this intake linked, per the Stage 1/2 linking convention.
