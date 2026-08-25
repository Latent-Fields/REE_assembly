# Thought Intake: Reusable Computational Motifs, Content Binding, and Coalition Composition

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-23_reusable_computational_motifs_content_binding_and_coalition_composition.md`
**Session:** mech-266-rescore-circling-2d31ca (thought-ingestion batch of 3, drafted by a research
subagent, merged and committed by the orchestrating session)

---

## 1. Verbatim prompt / core proposal

The thought's central architectural claim, stated in its own closing synthesis:

> **Combinatorial cognitive capacity may come not from proliferating modules, but from dynamically
> binding content to reusable computational motifs and composing those motifs into task-specific
> coalitions.**

Trigger: Osako et al. 2026 (*Nat Neurosci*, DOI 10.1038/s41593-026-02410-0) show mice performing a
delayed match-to-sample task reuse neuronal subspaces (stimulus-processing, memory-maintenance)
across task phases with different bound content -- the same memory-maintenance population carries
different information at different times, and data-constrained RNNs show computation-specific
lesion effects. Corroborating literature: Driscoll, Shenoy & Sussillo 2024 (*Nat Neurosci*, shared
dynamical motifs in multitask RNNs) and Tafazoli et al. 2026 (*Nature*, shared neural subspaces
across compositionally related monkey tasks).

The thought explicitly proposes separating five dimensions that "should not be assumed to collapse
into one another": (1) computational role/motif, (2) representational content currently bound to
it, (3) substrate identity realizing the role, (4) coalition membership (larger temporary
configuration the role participates in), (5) task/context control (what recruits the role and what
content it receives). It offers a schematic tuple `R_t = (F, X_t, S_t, G_t, theta_t, tau_t)` as a
"reminder," explicitly **not** a proposed implementation schema.

The thought is explicit that it is a candidate *extension* of the existing coalition-control
architecture (SD-091/MECH-481), not a replacement, and that registration should not be automatic --
it names its own comparison targets (SD-091/MECH-481, ARC-071/MECH-323, current working-memory and
routing mechanisms) and instructs that this comparison happen before any claim is registered. This
intake performs that comparison.

---

## 2. What's new vs. existing REE docs/claims (novelty table)

| Thread / concept in the thought | Existing REE coverage | Verdict |
|---|---|---|
| **General architectural separation of computational role from representational content, as an explicit compositional axis distinct from coalition/topology control and from policy composition** | No claim in `claims.yaml` asserts this at the general/architectural level. SD-091 separates *parametric* control from *topology* control (two axes); this thought adds a third (*role selection + content binding*). Nothing currently generalises "same operation, different content" into an architectural commitment. | **Genuinely new -> registered as SD-101.** |
| **Specific mechanism: typed demand/task requirement selects a reusable computational motif from a repertoire, binds task-relevant content to it, and the bound-and-selected motif then participates in coalition instantiation (a step inserted between demand formation and coalition enactment)** | MECH-481 specifies demand -> classify -> **coalition template** -> instantiate, with the coalition template already fixed to a set of subsystems for that demand type; it does not currently separate "which reusable *operation*" from "which *subsystem* performs it" -- the coalition template names subsystems directly, not roles that could be filled by content-varying instances. | **Genuinely new -> registered as MECH-503 (instantiates SD-101).** |
| SD-091's coalition/topology control output (`G_t`), star-topology MVP substrate, typed `ControlDemandType` taxonomy | **SD-091** (design_decision, architectural necessity of a graph-valued control output) + **MECH-481** (mechanism_hypothesis, the typed-demand -> coalition-instantiation sequence). Both partially built in V3 (steps 1-6 landed, ree_core/claustrum/), not yet ablated (step 7, the 4-arm falsifier, not queued). | **Already owned.** The new thought explicitly names this as the closest existing lineage and proposes extending it, not duplicating it. Cross-referenced, not re-asserted; see Section 5. |
| ARC-071/MECH-323 policy composition (chunk repeated action sequences into a single atomic primitive; formation operator) | **ARC-071** (architectural_commitment, "composition via repeated grounding") + **MECH-323** (mechanism_hypothesis, ChunkAccumulator formation operator). Built default-OFF in V3, no experimental evidence yet (LEG 3 -- the compute-savings falsifier -- never attempted). | **Already owned, and the thought itself explicitly distinguishes its own proposal from this axis**: "policy composition reuses learned action/strategy structures; coalition composition reconfigures which systems interact; computational-motif reuse reuses the same operation on different bound content." Cross-referenced, not re-asserted. |
| A specific existing REE instance of "same computational motif, different content, in different places" | **MECH-167**: `z_harm_a` and `drive_level` "instantiate the same computational motif -- slow interoceptive integration converging on ACC-type processing -- without sharing information or overlapping downstream gates." **ARC-061**: self-attribution implemented via "a family of forward-model comparators at motor, interoceptive, and propositional levels -- each instantiating the same reafference-cancellation motif ... at a distinct representational timescale and modality." | **Adjacent-but-distinct.** These are narrow, already-built, single-motif instances of exactly the pattern the new thought generalises -- useful corroborating precedent that the pattern already occurs informally in REE's design, but neither claim asserts (or was written to assert) a general architectural principle, a content-binding mechanism, or a repertoire of reusable roles. Cited in SD-101's notes as precedent, not depended-on as prerequisite machinery. |
| Reuse of an indexing/traversal substrate (E1 associative manifold) across spatial navigation, memory search, concept traversal, planning rollout, working memory ordering | **MECH-155** (mechanism_hypothesis, `e1.spatial_as_general_indexing`) + sibling **MECH-156** (theta-as-traversal-clock). **Both carry an open, unresolved governance flag** (2026-08-08): "within E1" framing conflates E1 with the structurally separate `HippocampalModule`; ChatGPT-assisted provenance flagged as possibly containing false correlations; two of the five named domains ("concept traversal," "working memory ordering") have no operational referent in the codebase. | **Adjacent-but-distinct, and explicitly NOT used as depended-on machinery** because of its own unresolved governance flag -- would import that debt into a fresh registration. Noted in SD-101's notes as a troubled, narrower precedent for the same general intuition, not cross-referenced via `depends_on`. |
| MECH-299: theta-cycle content scales with "the smallest reusable item available in the active substrate stack" (atomic actions / action chunks / type-instance matches / option invocations, depending on which substrates have landed) | **MECH-299** (already registered, refines MECH-089 theta-gamma nesting). | **Different axis, not a duplicate.** This is about the *temporal packaging granularity* of whatever reusable unit currently exists in the substrate stack, not about separating computational role from content. Not cross-referenced as a dependency; noted as a plausibly-related but orthogonal claim if it ever comes up in review. |
| SD-042 option library: "a discrete codebook of named, reusable action subroutines" (initiation-set + termination-function + internal-policy) | **SD-042** (design_decision). | **Different axis (policy/behaviour reuse, same family as ARC-071), not a duplicate** of role/content-binding for cognitive *operations* generally (perception, comparison, retrieval, uncertainty estimation, etc.), which is what the new thought is about. Not cross-referenced. |
| Illustrative motif repertoire (maintain, compare, accumulate, sequence, inhibit, retrieve, simulate, estimate uncertainty, detect discrepancy, bind provenance, maintain a goal, arbitrate alternatives) | No existing REE claim registers a fixed taxonomy of reusable cognitive operations at this grain. | The thought itself calls this list "deliberately provisional." **Not registered verbatim as a taxonomy** (unlike MECH-481's committed 10-item `ControlDemandType` enum). Left as illustrative material in MECH-503's notes, not as a committed field/enum. |
| Candidate experimental programme A-F (same-function-different-content, same-content-different-function, recombination, coalition x binding factorial, lesion, interference/capacity) | No existing REE experiment or queue entry runs any of these designs against a role/content-binding hypothesis. | Not itself a claim; folded into MECH-503's `what_would_answer` (Test D and Test C are the most directly diagnostic) and flagged as future `/queue-experiment` material once version-routed. |
| Relationship to Dynamic Latent Information Field (DLIF) | The thought itself states: "No automatic merger is justified... this thought is principally about functional reuse and composition. It should remain conceptually separate unless explicit analysis shows that DLIF is required to instantiate the binding mechanism." | **Correctly left unclaimed by the raw thought itself.** No DLIF-relationship claim registered here. |
| 10 "architectural questions raised" (does REE conflate substrate identity with role? does SD-091 recruit fixed components where role/content abstraction would generalise? etc.) | Open questions, not assertions. | Not claim-worthy as stated (too broad/exploratory for a single falsifiable Q- claim each). Left as open questions in SD-101/MECH-503 notes. |

---

## 3. Key formulations (verbatim, load-bearing)

> The load-bearing architectural observation is therefore not merely that the brain is modular. It
> is that a computation can be **reused independently of the particular content currently occupying
> it**.

> Complex cognition may scale by reusing computational and representational components whose
> recruitment, binding, sequencing, and interaction are dynamically reconfigured for the current
> task.

> Is the unit being recruited always a fixed subsystem, or should REE also be able to recruit a
> reusable computational role and dynamically bind different content into it?

> If the second is required, then coalition control and computational-role reuse are distinct but
> composable mechanisms.

> - policy composition reuses learned action/strategy structures;
> - coalition composition reconfigures which systems interact;
> - computational-motif reuse reuses the same operation on different bound content.
>
> These three forms of compositionality should not be conflated.

> The controller should not necessarily compute either the content or the computation itself. It
> may only provide the bounded routing/binding authority that allows appropriate reusable
> operations to be instantiated.

> REE should preserve the possibility that a reusable computation is a projection or dynamical
> regime rather than a separately encapsulated component.

> **Combinatorial cognitive capacity may come not from proliferating modules, but from dynamically
> binding content to reusable computational motifs and composing those motifs into task-specific
> coalitions.**

---

## 4. Affected existing claims

- **SD-091** (`control_plane.coalition_topology_control`) -- **extended, not duplicated or amended.**
  SD-091 already establishes that the control plane must produce a graph-valued coalition/topology
  output `G_t` alongside mode `M_t` and parameters `theta_t`. SD-101 adds a further axis this thought
  argues is distinct: *which reusable computational role* fills a coalition slot and *what content*
  is bound into it, as opposed to *which fixed subsystem* is recruited. SD-091's star-topology MVP
  substrate (built, partially wired 2026-08-02/03 in `ree_core/claustrum/`) currently recruits named
  subsystems directly -- it does not yet have a role/content-binding layer to select from. SD-101
  depends_on SD-091.

- **MECH-481** (`control_plane.typed_coalition_instantiation`) -- **extended, not duplicated or
  amended.** MECH-481's sequence is monitor -> classify -> request -> instantiate (coalition
  template) -> operate -> reassess -> dissolve/sustain/escalate. MECH-503 proposes inserting a role
  selection + content binding step between "request" and "instantiate." MECH-481's own taxonomy
  (`ControlDemandType`, 10 classes, 2 templated so far) is untouched; MECH-503 depends_on MECH-481.

- **ARC-071** (`policy.composition_via_repeated_grounding`) -- **cross-referenced as a distinct,
  non-duplicated compositional axis**, exactly as the thought itself insists. No overlap in
  mechanism (ARC-071 uses a repetition-count + outcome-consistency accumulator; SD-101/MECH-503
  have no accumulator at all). depends_on for cross-reference only.

- **MECH-323** (`policy.composition.chunk_accumulator_formation`) -- **cross-referenced via ARC-071,
  same distinction as above.** No role/content-binding machinery and not reused by SD-101/MECH-503
  in either direction. depends_on for cross-reference only.

- **MECH-167, ARC-061** -- narrow, already-built precedents for "the same computational motif serving
  different content/signals" at a local scale. Cited as corroborating precedent in SD-101's notes,
  **not** wired via `depends_on`.

- **MECH-155 / MECH-156** -- narrow, *troubled* precedent (unresolved 2026-08-08 governance flag: E1
  vs. HippocampalModule conflation, ChatGPT-assisted provenance, two ungrounded domain terms).
  Explicitly **not** wired via `depends_on` to avoid importing that open governance debt into a fresh
  registration.

No existing claim's status, confidence, evidence record, or `epistemic_category` was touched by this
intake.

---

## 5. Candidate claims -- REGISTERED this pass

Two claims, mirroring the SD-091/MECH-481 architectural/mechanistic pair shape, registered directly
into `docs/claims/claims.yaml` in this pass (see that file for the authoritative entries):

- **SD-101** -- `control_plane.role_content_binding`. Architectural necessity claim: the control
  plane should be able to represent computational role independently of the content currently bound
  to it, as a distinct axis alongside coalition/topology control (SD-091) and policy composition
  (ARC-071).
- **MECH-503** -- `control_plane.motif_selection_and_content_binding`. Mechanism hypothesis
  instantiating SD-101: typed demand/task requirement selects a reusable computational motif and
  binds task-relevant content to it as a step distinct from and prior to coalition/topology
  instantiation (MECH-481); content-binding and coalition/topology instantiation are separable
  causal axes.

Both: `status: candidate`, `polarity: asserts`, `epistemic_category: substrate_conditional` (set
explicitly), `implementation_phase: v4`, `version_relevance: v4_v5`, `v3_pending: true`,
`registered_utc: 2026-08-25`. Compass / architectural framing only. **DO NOT build a
role/content-binding substrate or queue a V3 experiment from these two claims without an explicit
`/governance` version-routing decision** -- see Section 7.

A new architecture doc stub was created: [`docs/architecture/reusable_computational_motifs.md`](../../docs/architecture/reusable_computational_motifs.md),
in the "Control, Precision & Neuromodulation" sidebar category, `nav_order: 19`.

---

## 6. Next steps

1. **Literature pull** (not performed in this intake): a targeted `/lit-pull` review of the three
   cited papers (Osako et al. 2026 Nat Neurosci DOI 10.1038/s41593-026-02410-0; Driscoll, Shenoy &
   Sussillo 2024 Nat Neurosci DOI 10.1038/s41593-024-01668-6; Tafazoli et al. 2026 Nature DOI
   10.1038/s41586-025-09805-2) for REE-specific applicability, mirroring the depth of SD-091/
   MECH-481's `evidence/literature/targeted_review_claustrum_coalition_control/` (8 entries).

2. **Threads deliberately left unregistered:**
   - The `R_t = (F, X_t, S_t, G_t, theta_t, tau_t)` formal tuple -- explicitly not an implementation
     schema per the source thought; recorded in notes only.
   - The illustrative motif repertoire (12 example operations) -- explicitly provisional; not
     committed as a taxonomy field.
   - The 10 "architectural questions raised" -- too broad/exploratory for individual falsifiable
     `Q-` claims as stated; a future pass could narrow one into its own `Q-` claim if a specific
     empirical handle emerges.
   - Candidate experimental programme Tests A, B, E, F -- folded into MECH-503's notes/
     what_would_answer as corroborating designs, but not separately registered; Test D (coalition x
     binding factorial) is the primary falsifier, Test C (recombination) the secondary one.
   - Relationship to Dynamic Latent Information Field -- the source thought itself declines to merge
     these; no claim registered connecting the two.

3. **Version-routing decision**: both registered claims are parked `v4`/`substrate_conditional` by
   default. A future `/governance` cycle should explicitly weigh whether a narrow slice (Test A/B
   against one of the two currently-templated `ControlDemandType`s) is cheaply testable now, given
   SD-091/MECH-481's existing V3 wiring, rather than waiting for a full V4 build -- flagged in
   MECH-503's notes, not decided here.

4. **Governance-flag hygiene note (side observation, out of scope for this pass)**: while
   cross-checking `claims.yaml` for coverage, this intake noticed MECH-155/MECH-156 still carry an
   open 2026-08-08 governance flag (E1-vs-HippocampalModule conflation) that appears unresolved as of
   this drafting. Not actioned here; worth a mention in case it is not already tracked elsewhere.
