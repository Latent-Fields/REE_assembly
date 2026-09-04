# Thought Intake: Causal Memory Compression and Grounded Development (the 2026-09-04 literature-bounded trio)

**Date:** 2026-09-04
**Session:** thought-ingestion-20260904-batch
**Raw thought files (3, processed together because the third is the routing note for the first two):**

| Raw file | Source | Role |
|---|---|---|
| `docs/thoughts/2026-09-04_sleep_compression_causal_social_learning_thought.md` | Jiang et al. 2026 (bioRxiv 10.64898/2026.08.22.746376, compressed representations and knowledge awareness in sequence learning); Rafiuddin & Sen 2026 (arXiv 2609.02131, C3T counterfactual causal reasoning over conversation trees) | episode retention -> compressed schema -> causally usable social knowledge |
| `docs/thoughts/2026-09-04_grounded_developmental_world_models_thought.md` | Pezzulo et al. 2026 (arXiv 2607.13560, grounded world models in biological organisms and future AI; perspective) | organism-first developmental ordering; preservation invariants |
| `docs/thoughts/2026-09-04_research_fanout_causal_compression_grounded_development.md` | (routing note, no source) | five fan-out routes and four decision gates A-D |

**None of the three external sources was fetched or verified in this pass.** Every characterisation
below is the raw thought's own; a `/lit-pull` chip is spawned (Next steps) covering all three plus the
authority-field bibliography from the sibling intake.

**Sibling intake:** `thought_intake_2026-09-04_regulation_first_organizing_subjective_experience.md`
(the user's own regulation-first cluster, written the same day and reaching the same organising
conclusion from introspection + the live `z_world` wall rather than from literature). Where the two
converge, the claim is registered ONCE, in the sibling intake, and this intake records the convergence.

## Verbatim prompt (core proposals)

Sleep-compression thought:

> REE should distinguish at least three achievements that can otherwise be collapsed into one vague
> notion of "learning": 1. Episode retention ... 2. Compressed schema formation ... 3. Causally usable
> social knowledge ... The crucial bridge is not a generic replay buffer. It is the conversion of
> causally annotated episodes into abstractions that preserve intervention-relevant distinctions
> while discarding incidental detail.

> Compression that loses those handles may improve predictive loss while damaging later social
> understanding.

Grounded-development thought:

> A developmental REE should not begin by treating the world as an unstructured external object that
> must first be fully inferred. It begins as an organism with a body, needs, vulnerabilities, action
> capacities, and consequences. ... `viability and action -> sensorimotor regularities -> affordances
> and controllability -> objects/places/episodes -> other agents and their trajectories -> abstract
> schemas, language, and social norms`

> Does the representation preserve distinctions that are actionable for this organism before it
> preserves distinctions that are merely descriptive to an observer?

Routing note:

> Route the two research-bounded thoughts into the existing REE claim, experiment, and evaluation
> machinery without converting attractive literature into automatic design commitments.

All three are explicitly research-bounded ("preliminary human evidence, not a validated computational
mechanism"; "a perspective, not direct evidence for a single implementation"; "useful hypotheses and
evaluation prompts, not settled REE architecture"). Per `feedback_lit_exp_decoupled`, a paper
resembling REE strengthens no existing claim's confidence; nothing here touches any claim's evidence
record.

## What is new vs existing REE docs/claims (novelty table)

| Thread (source file / section) | Existing REE coverage | Verdict |
|---|---|---|
| **Three achievements (episode retention / compressed schema / causally usable social knowledge) and the counterfactual-handle requirement on compression**: schema must retain agent identity/type, action class, contextual preconditions, uncertainty over causal contribution (sleep-compression, "Core proposition", "REE interpretation") | MECH-166 (slot-formation vs slot-filling, separated across SWS/REM), MECH-274 (sleep-dependent aggregation of other-attributions, V4-reserved), ARC-137 (typed offline outcomes incl. reorganisation and recalibration/attribution repair), MECH-529 (replay-driven rebucketing driven by consequential divergence), INV-049; the *social* handle requirement: EXT-005 (no first-person causal-signature mechanism), EXT-006 (other-model collapse), INV-102 (other-agent-caused hypothesis with bounded prior), MECH-430 (multi-dimensional provenance source vector incl. self-vs-other-generated and source identity -- this IS the "causal ancestry" field on an episode) | **Owned in parts; the compression-preservation requirement is folded into INV-104** (registered in the sibling intake) as a fourth row -- "causal ancestry / intervention handles" -- with this file as a `source_documents` entry. No separate claim. |
| **Waking/offline update asymmetry contract**: waking = bounded, reversible updates, store episodes with uncertainty attached; offline = durable schema proposals subject to validation; protected episodic evidence (sleep-compression, "REE interpretation", "Architectural caution"; routing note, "Claim digestion" row) | INV-049 (offline update necessity as a general computational law), ARC-020 / INV-024 (typed write boundaries; offline consolidation isolated from online commitment), ARC-137 ("sleep may repair access to behavioural authority but must not confer authority directly"; each outcome has a declared write target and provenance class), MECH-094 (simulation content does not accumulate as real experience), MECH-392 / INV-080 (consolidation must not silently overwrite the evidence base) | **Already owned -> cross-reference only.** The "reversible waking/offline update contract" the routing note asks digestion to specify is ARC-137's write-target / provenance-class table; the request is handed to `/thought-digestion` on ARC-137 (Next steps). |
| **Inspectability lags competence** (Jiang: behavioural competence can precede a representation available for report/inspection/higher-level control) (sleep-compression, "What the new work contributes", prediction 5) | INV-037 (stored/retrievable is not active in the navigable state; a preparation substrate converts one to the other), SD-064 (global-workspace-like access channel whose contents are reportable and load-bearing for integrative cognition while reactive behaviour bypasses it), ARC-120 / ARC-130 (competence before authority; causal-reach ladder) | **Already owned -> cross-reference only.** The prediction is a corollary of INV-037 + SD-064; recorded as a lit anchor candidate for SD-064 in the lit-pull chip. |
| **Confounded two-agent causal-attribution environment** (another agent's state shifts after one or more candidate causes: resource change, obstacle, contact, signal, third-party action; score = correct *intervention* choice, not prediction) and the four-arm comparison (online-only / random replay / prioritised sleep replay + compression / same compression with causal annotations ablated) (sleep-compression, "Minimal experimental path") | ARC-047 (multi-agent gridworld with affective scent leakage as the minimal ARC-010 test substrate, v5, unbuilt), SD-047 (multi-source environmental dynamics -- the confounder-generation machinery exists at the env level for the *single*-agent case), MECH-504 (other-agent discovery via responsive intervention), MECH-276 (scientist-agent: correlation is insufficient), ARC-059 stage 3 | **Experiment seed on unbuilt substrate -> NOT registered, NOT chipped.** ARC-047 already owns the substrate; the confounded-cause design and the causal-annotation-ablation arm are recorded here as ARC-047's first experiment design when that substrate exists (V4/V5). Chipping a `/queue-experiment` now would violate the substrate_conditional rule and the routing note's own Gate D. |
| **Pezzulo: developmental order viability -> sensorimotor -> affordances/controllability -> objects/places/episodes -> other agents -> abstract schemas/language/norms; later representations remain answerable to earlier organism-world relations** (grounded-development, "Core proposition") | ARC-059 (self-as-object -> objects-as-patterns -> others-as-special-objects), ARC-122 (innate coupling -> consolidation -> play -> language), INV-094 (social coupling before play before language), MECH-397 (adaptor-maturity curriculum gate), MECH-381 (developmental compression ladder), INV-041, ARC-019 | **Already owned -> cross-reference only.** The Pezzulo ordering interleaves ARC-059's three stages with ARC-122's four phases and adds nothing either lacks except the *rationale* ("answerable to earlier organism-world relations"), which is ARC-138's content (sibling intake). This file is added to ARC-138's `source_documents`. |
| **Protected representational invariants as preservation requirements** (bodily condition / threats to continuation; action availability and controllability; outcome valence and uncertainty; self-generated vs external change; spatial-temporal relation to resources/obstacles/agents; evidence of an independently evolving trajectory) -- "if a compression destroys all access to one of them, treat it as a possible developmental regression" (grounded-development, "Proposed developmental invariants") | Identical to the sibling cluster's representation contract, reached independently from literature | **Registered ONCE as INV-104** (sibling intake); this file is a `source_documents` entry and the "independently evolving trajectory" row is INV-104's fifth preservation class. |
| **Curriculum ordered by the appearance of new environmental regularities and action consequences, not by task difficulty** (grounded-development, "Candidate downstream fan-out"; routing note, "Developmental curriculum" row) | ARC-059's ordering rationale is exactly this (each stage is defined by a new class of regularity: self-caused change, then object-schema, then independent policies); MECH-504 and Gate D ("only introduce agent-intention inference once agents possess independently varying trajectories that cannot be represented as moving obstacles or resources") are ARC-059 stage 3's entry condition; MECH-397 orders by adaptor depth | **Already owned -> cross-reference only.** Gate D is recorded as ARC-059 stage-3 entry criterion wording in INV-104's notes; no edit to ARC-059. |
| **Ethics as an emergent property of world/self/other modelling under the axiom set rather than an added module** (grounded-development, "Near-term REE use") | INV-005, INV-028, ARC-056, ARC-042, INV-043 | Already owned; cross-reference only. |
| **Gate A (representation preservation before a social layer) and Gate C (adopt an offline mechanism only on held-out causal attribution / intervention / transfer / calibration, not training loss or replay reconstruction)** (routing note) | No Assembly rule covers either; GOV-PATHVALID-1 is the nearest | **Registered as the two clauses of GOV-MATCHAUX-1** (sibling intake): representation-objective form (Gate A, plus the matched-control requirement the sibling cluster adds) and offline-mechanism form (Gate C). |
| **Gate B (episode adequacy: stored episodes must distinguish an event from its causes and alternatives before sleep is credited with social learning; a plain state-transition tuple is insufficient in confounded environments)** (routing note) | MECH-430 (source vector), ARC-085 (self-tagged event-token store binding perspective, emotion, residue, self-state), MECH-365, MECH-205 (counterfactual variations generated at replay) | **Already owned as substrate requirements -> cross-reference only.** Gate B is a *precondition check* on those claims, not a new one; recorded in the ARC-047 experiment-design note above. |
| **Candidate measurements** (grounded retention probes; compression: footprint / accuracy / transfer / queryable regularities; causal calibration: probability on the true cause, sensitivity to causal reversal, coincidence vs intervention; ethically relevant behaviour: avoids preventable harm, chooses repair after confirmed contribution, abstains or seeks information under attribution uncertainty) (routing note) | GOV-BEHADJ-1 (behavioural-adjudication methodology), MECH-414 (repair after harm), MECH-434 (epistemic commitment timing -- abstain/seek), INV-102 | Measurement menu, not claims; carried into the gated chip in the sibling intake and into the ARC-047 design note. |
| **"Do not infer yet" list** (sleep required for all abstraction; conscious access necessary for good control; social-media results transfer to embodied agents; an authority/gating mechanism is needed beyond existing precision/policy/control-plane machinery) (routing note) | -- | The fourth item is the explicit brake the authority-field sibling intake operates under (MECH-534 is registered as a *hypothesis with a static-gate falsifier*, not a need). Recorded there. |

## Key formulations (verbatim, load-bearing)

> behavioural competence can precede a representation that is available for flexible inspection,
> report, or higher-level control.

> social learning needs event ancestry, competing causal candidates, and counterfactual tests -- not
> only correlated state transitions.

> if a compression or abstraction destroys all access to one of them, it should be treated as a
> possible developmental regression.

> The ethical dimension is thereby tested as an emergent property of world/self/other modelling under
> the axiom set, rather than supplied as disembodied instruction.

> Passing generic reconstruction while failing direction, controllability, or self/world probes should
> be treated as a failure for REE purposes.

## Affected existing claims

Cross-referenced only; nothing promoted, demoted, or edited: MECH-166, MECH-274, ARC-137, MECH-529,
INV-049, EXT-005, EXT-006, INV-102, MECH-430, ARC-020, INV-024, MECH-094, MECH-392, INV-080, INV-037,
SD-064, ARC-120, ARC-130, ARC-047, SD-047, MECH-504, MECH-276, ARC-059, ARC-122, INV-094, MECH-397,
MECH-381, INV-041, ARC-019, INV-005, INV-028, ARC-056, ARC-042, INV-043, ARC-085, MECH-365, MECH-205,
GOV-BEHADJ-1, MECH-414, MECH-434, GOV-PATHVALID-1.

## Candidate claims -- REGISTERED this pass

**None registered from this intake alone.** Every genuinely-new thread this trio carries (the
preservation invariant; the matched-control / held-out-downstream admissibility rule) is shared with
the sibling regulation-first cluster and is registered ONCE there (INV-104, GOV-MATCHAUX-1, with
ARC-138 carrying the Pezzulo ordering rationale). This intake's three raw files are listed in those
claims' `source_documents`. Recording the convergence -- two independent routes (introspection against
the live wall; three external papers) to one preservation requirement on the same day -- is itself the
useful output; per GOV-INTRO-1 that convergence is what moves an introspectively-sourced hypothesis
toward acquiring a second source, and per `feedback_lit_exp_decoupled` it changes no confidence.

## Next steps

1. **`/lit-pull` chip** (`chip-20260904-litpull-grounded-compression-authority-field`): verify and
   bank Pezzulo et al. 2026 (arXiv 2607.13560) against ARC-138 / INV-104; Jiang et al. 2026 (bioRxiv
   10.64898/2026.08.22.746376) against INV-037 / SD-064; Rafiuddin & Sen 2026 (arXiv 2609.02131)
   against INV-102 / MECH-430 as a *methodological* anchor only; and the authority-field intake's
   12-entry bibliography (Miller/Brincat/Roy 2026 J Neurosci; Muller et al. 2026 Neuron; Jacobs et al.
   2025 arXiv 2502.06034; Pinotsis & Miller 2026 Cereb Cortex; and the 8 already-classic refs) against
   MECH-534 / Q-103 / MECH-499 / MECH-500. One pull, four targets, because the raw thoughts share a
   bibliography style and all four claim targets were registered in the same pass.
2. **`/thought-digestion` hand-off (no chip)**: on ARC-137, spell out the waking/offline update
   contract the routing note asks for as ARC-137's write-target table; on ARC-047, attach the
   confounded-two-agent design and the causal-annotation-ablation arm as its first experiment design.
3. **Deliberately left unregistered:** the confounded two-agent environment (substrate owned by
   ARC-047, unbuilt); Gate B and Gate D (precondition checks on existing claims); the measurement menu;
   the "do not infer yet" list (brakes, not claims).
4. **No plan-of-record doc created.** The sibling intake explains why.
