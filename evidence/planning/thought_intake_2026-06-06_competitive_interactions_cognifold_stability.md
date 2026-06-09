# Thought Intake (Stage 2): Competitive interactions as a cognifold-stability and computation principle

Raw thought file: [docs/thoughts/2026-06-06_competitive_interactions_cognifold_stability.md](../../docs/thoughts/2026-06-06_competitive_interactions_cognifold_stability.md)

Processed: 2026-06-09T19:56Z
Status: structured intake only -- NO claims.yaml registration (architecture compass; off the V3 / GAP-7 critical path)

---

## 0. Source verification (2026-06-09)

The raw note's primary-source citation was opened during capture; re-verified by web search this session.

- **Verified accurate.** Andrea I. Luppi et al., "Competitive interactions shape mammalian brain network dynamics and computation." *Nature Neuroscience* **29**(4), 915-933 (2026). Published 11 March 2026. DOI: 10.1038/s41593-026-02205-3. https://www.nature.com/articles/s41593-026-02205-3 (open access). Corroborated by the Oxford ORA record, EurekAlert release, and the publisher page; all agree on volume/pages/date/DOI.
- Lay summaries (news-medical, medicalxpress, EurekAlert) restate the central result: whole-brain models combining **modular cooperative** interactions with **diffuse long-range competitive** interactions reproduce mammalian (human / macaque / mouse) brain dynamics better than cooperative-only models; competition manages limited resources and prevents over-synchronisation.
- The note's source-check bullets (cross-species; cooperative-only over-synchronises; competition links regions with *opposite* cytoarchitecture/gene/receptor profiles; competition raises synergy + hierarchy + neuromorphic performance; competition != neuronal inhibition) are consistent with the abstract and lay coverage.
- One PubMed hit (PMID 39484469) appears to be an earlier preprint/version of the same work; it does not affect the published citation above.

No correction needed to the raw note's external anchors.

---

## 1. Verbatim thought

> # THOUGHT INTAKE: Competitive interactions as cognifold stability and computation principle
>
> ## 0. Summary claim
>
> A saved REE email pointed to the Nature Neuroscience article "Competitive interactions shape mammalian brain network dynamics and computation" by Luppi et al. The paper uses computational whole-brain modelling across human, macaque, and mouse data, and argues that models combining modular cooperative interactions with diffuse long-range competitive interactions better reproduce mammalian brain activity than cooperative-only models.
>
> The REE-relevant point is not simply "the brain has inhibition".
>
> The useful architectural idea is stronger:
>
> > stable, synergistic, hierarchical cognition may require signed competitive interactions as part of the generative structure of the cognifold.
>
> Competition is therefore not merely damage, absence, or suppression. It may be a necessary structural ingredient for stabilisation, segregation, hierarchy, subject specificity, and computation.
>
> ## 1. Why this belongs in REE_assembly
>
> REE is increasingly specified as a cognifold: a connected field of routed latent representations, gates, precision weights, stop pathways, residue, self/world/action binding, and commitment authority.
>
> This paper is relevant because a cognifold cannot be "everything positively coupled to everything". Unchecked cooperative coupling risks runaway reinforcement, positive feedback, loss of modularity, and failure to segregate competing processes.
>
> Competitive interactions may therefore be a first-class architecture principle for REE, especially around: precision-weighted coupling; inhibitory / stopping mechanics; anti-lock-in dynamics; modular segregation without full disconnection; commitment gating; self/world and self/other boundary preservation; oscillatory / phase-structured dynamics; synergy and hierarchy.
>
> This supports earlier REE framing that sparse coupling, precision gating, inhibitory competition, and explicit stop/boundary pathways are non-negotiable for stable cognifold behaviour.
>
> ## 2. Proposed classification
>
> - **mechanism hypothesis:** signed competitive interactions are required for stable, synergistic, hierarchical cognifold dynamics.
> - **architectural commitment candidate:** REE should represent competition/suppression as a constructive coupling mode, not merely as an error-correction afterthought.
> - **open question:** which REE subsystems require explicit competitive edges rather than scalar gating or softmax competition alone?
>
> This should not be promoted directly to an invariant without claim review.
>
> ## 4. REE-specific hypothesis
>
> REE may need explicit signed interaction structure in the cognifold. A simple all-positive routed-field model may be unstable because every salient stream reinforces every other salient stream. Instead, REE likely needs at least three coupling types: (1) Cooperative coupling -- supports binding, coherent trajectory generation, shared context; (2) Competitive coupling -- suppresses incompatible trajectories, preserves boundaries, prevents runaway resonance, and prevents one field from absorbing all others; (3) Gated decoupling -- temporarily isolates simulation, offline integration, or unsafe action candidates from release authority.
>
> Architecture constraint:
> `cognifold_edge = {source, target, sign, gain, precision, gate, timescale, write_authority}`
> Competition should not be collapsed into "negative reward" or "punishment". It is a structural relation between active fields.
>
> ## 5. Relevance to REE failure modes
>
> feedback entrapment (excessive positive coupling without competitive damping); belief fixation (suppressed update competition / over-stabilised attractor); shared delusional coupling (cross-agent positive coupling without boundary competition); precision misallocation (wrong field gets global suppressive authority); commitment dysregulation (action release wins without inhibitory competition); residue blindness (harm-residue field lacks competitive authority over reward/goal field); goal proxy lock-in (proxy field suppresses terminal-value field).
>
> ## 6. Important cautions
>
> Do not equate competitive interactions directly with synaptic inhibition. Do not assume every negative edge is harmful/pathological/ethically negative. Do not reduce competition to reward subtraction. Do not overclaim that the paper proves REE's architecture. Do not make this a REE-v3 implementation target without a specific existing claim or substrate gap.
>
> The useful extraction is: signed competitive coupling may be a necessary generative ingredient of stable cognifold dynamics.
>
> ## 9. Guardrail for future agents
>
> If a future agent tries to convert this into "add inhibition everywhere", stop and reframe. The correct near-term extraction is: preserve signed competitive coupling as a possible constructive cognifold primitive. The incorrect extraction is: treat competition as generic suppression, punishment, or damage.

(Full raw note, including the paper-concept->REE-analogue mapping table in section 3, external anchors in section 7, and the proposed `docs/architecture/cognifold_signed_coupling.md` extraction in section 8, is preserved verbatim in the Stage-1 file linked above.)

---

## 2. What's New vs. Existing REE Docs

| Idea in thought | Already in REE? | Where | Genuinely new? |
|---|---|---|---|
| Competition as a stabilising/selecting force (vs everything-positive) | YES, but **local + implicit** | BG winner-take-all lateral inhibition + Cisek/Kalaska affordance-competition (MECH-090); symmetric Go/NoGo + dMSN/iMSN competitive model (ARC-030); top-k competitive selection over E1/E2 latents (MECH-254) | No -- REE already runs competitive selection locally |
| Precision-weighted, mode-conditioned routing as the control surface | YES | Control plane (ARC-005, MECH-002, MECH-019, MECH-004); mode-conditioned write gating (MECH-261/MECH-094); salience-network coordinator (SD-032a, MECH-259) | No |
| Cognifold = single connected field with **bounded** coupling (not all-positive) | YES (framing) | overview.md L52 "REE remains a coherent single cognifold with bounded coupling"; invariants.md; e1.md / e2.md; ethical_agency_derivation.md | No -- "bounded coupling" already names the constraint |
| **Signed coupling as a first-class, explicit EDGE PROPERTY of the cognifold** (`{source,target,sign,gain,precision,gate,timescale,write_authority}`) -- competition represented structurally, not just emergent from softmax/WTA/gating | **NO** | competition is currently emergent from softmax/top-k/beta-gate; there is no explicit signed-edge type at the cognifold-field level | **YES** -- this is the core durable-new contribution |
| **Diffuse, long-range competitive coupling between distant fields with opposite profiles** as a *generative* requirement (not just local damping) | **NO** | REE competition is local (within-loop WTA, within-stage top-k); no long-range cross-field competitive constraint analogous to the paper's diffuse competition | **YES** -- a distinct architectural axis |
| Three-mode coupling taxonomy: cooperative / competitive / gated-decoupling, as an explicit design vocabulary | PARTIAL | cooperative (binding), gated-decoupling (MECH-094 sim no-op, commitment latch MECH-090, mode gating MECH-261) all exist; the **unifying taxonomy + the competitive mode as a named first-class type** does not | **YES** as a unifying MAP (cf. the existing "attention = distributed precision-selection" note: same shape -- REE owns the pieces, lacks the map) |
| Re-index AI cognitive-failure taxonomy by missing/misweighted competitive coupling | NO (REE side); thought flags `Latent-Fields/ai-cognitive-failure-taxonomy` as the eventual home | failure modes exist individually (MECH-076 attractor lock-in/OCD basin; MECH-309 monostrategy collapse) but are not indexed against a competitive-coupling axis | **YES** but out-of-REE-repo; compass only |
| Competition != synaptic inhibition; != negative reward | YES (REE is careful here) | harm/residue is a separate stream, not "negative reward"; SD-010/011 dual nociceptive streams; the [biology-before-formal-definitions] rule | No -- but the caution is worth carrying forward verbatim |

**Novelty verdict:** REE already *instantiates* competition wherever selection happens (BG WTA, top-k E3 entry, beta commitment gate, mode-conditioned write gating). What is genuinely new is (a) representing **signed competitive coupling as an explicit first-class edge primitive** of the cognifold rather than an emergent by-product, and (b) the **diffuse-long-range** competitive axis between distant fields with opposite profiles as a *generative/stabilising* requirement. This is a **unifying architecture MAP**, structurally the same situation as the prior [attention = distributed precision-selection] intake -- REE owns the parts, lacks the explicit map. Compass-grade, not a substrate gap on the V3 critical path.

---

## 3. Key formulations

1. **Cognifold edge as a typed, signed object.** A candidate vocabulary the thought offers verbatim:
   `cognifold_edge = {source, target, sign, gain, precision, gate, timescale, write_authority}`.
   The novel field is **`sign`** (and the cooperative/competitive/decoupling *mode* it implies) as an explicit, first-class structural property of inter-field coupling -- not collapsed into negative reward, not equated to synaptic inhibition, not left to emerge from a softmax.

2. **Three coupling modes.** cooperative (binding, coherent trajectory, shared context) / competitive (suppress incompatible trajectories, preserve boundaries, prevent runaway resonance, stop one field absorbing all others) / gated-decoupling (isolate simulation, offline integration, unsafe candidates from release authority). REE already realises cooperative + gated-decoupling; the **competitive mode as a named, long-range, generative type** is the gap.

3. **Stability argument (the "why").** An all-positive routed-field cognifold is unstable: every salient stream reinforces every other salient stream -> runaway resonance / over-synchronisation / loss of modular segregation. Diffuse long-range competition is the *generative* ingredient that buys stability, segregation, hierarchy, synergy, and subject-specificity -- empirically grounded by Luppi et al. (cooperative-only models over-synchronise vs real mammalian brains).

4. **Two distinct failure axes (kept separate -- they are not the same):**
   - **Runaway positive coupling / hypersynchrony** -- every salient stream reinforces every other (the paper's "over-synchronised states rarely observed in brains"). REE analogue: feedback entrapment, shared delusional coupling, over-stabilised attractor (MECH-076).
   - **Monostrategy / regime collapse** -- the *opposite* pole: the policy collapses to the single smoothest regime (MECH-309). This is collapse from too little *apprehended structure*, NOT from too much positive coupling. Do not conflate the two; signed-coupling damping addresses the first, the rule-apprehension layer (ARC-062/063) addresses the second.

---

## 4. Affected existing claims (verified real IDs in claims.yaml)

None are contradicted. The thought *corroborates and offers a unifying lens over* the following; it does not propose changing any status.

**Control plane / precision routing (where signed coupling would live):**
- **ARC-005** -- "Control plane routes precision and modes." The natural host for an explicit signed-coupling edge type if ever promoted.
- **MECH-002** -- "Precision control analogues shape cognitive regimes."
- **MECH-019** -- "Control plane shapes modes of cognition, not discrete choices."
- **MECH-004** -- "Signal-to-knob wiring map for control plane."

**Where REE already runs competition locally (corroborated):**
- **MECH-090** -- "BG-level beta oscillations gate E3-to-action-selection propagation." (Anchored on Cisek & Kalaska 2010 affordance-competition; striatal WTA lateral inhibition.)
- **ARC-030** -- symmetric Go/NoGo sub-channels; explicit dMSN/iMSN *competitive* model (same actions, compete; balance point matters).
- **MECH-105** -- sequence completion -> BG beta release (decommit/promote competition).
- **MECH-254** -- top-k competitive selection over E1/E2 latents into E3 deliberation (precision + z_goal gain + NA salience).

**Attention = distributed precision-selection cluster (the existing distributed-not-unified pattern this thought mirrors):**
- **ARC-005, MECH-251, MECH-255, MECH-259, MECH-261, MECH-347, SD-032a, SD-057** -- precision-template / salience-switch / mode-conditioned-write-gate machinery. See memory note [attention = distributed precision-selection control]: same shape (distributed, no unifying map).
- **MECH-094** -- hypothesis-tag / waking-only write gate (generalised by MECH-261); the canonical gated-decoupling instance.

**Failure-mode anchors (corroborated, not contradicted):**
- **MECH-076** -- residue/attractor lock-in (OCD deep-basin) <-> "belief fixation / over-stabilised attractor".
- **MECH-309** -- monostrategy collapse <-> the *separate* regime-collapse axis (see Key formulation 4 -- do NOT merge with runaway-coupling).
- **ARC-062 / ARC-063** -- rule-apprehension slot; relevant only to the monostrategy axis, not to the competitive-damping axis.

---

## 5. Candidate claims FOR FUTURE REGISTRATION (NOT registered this session)

Per task scope and the raw note's own guardrails, **nothing is registered in claims.yaml.** These are seeds for a future governance pass, if and only if a concrete V3 substrate gap or failure motivates them:

1. **(open_question candidate)** "Which REE subsystems require an *explicit signed competitive edge* rather than emergent softmax/WTA/scalar-gating competition alone?" -- the thought's section-2 open question, verbatim. Likely `epistemic_category: substrate_conditional` or `derivational` (answerable partly by working through the cognifold spec), `implementation_phase: v4`. This is the *decision* layer, not a new substrate.

2. **(architectural_commitment candidate)** "The cognifold represents inter-field coupling as a typed, signed edge (cooperative / competitive / gated-decoupling), with competition as a first-class generative mode -- not an emergent by-product of selection softmaxes." Would most naturally **amend ARC-005** (control plane) rather than stand alone. `substrate_coherence` if ever adopted; off V3 critical path.

3. **(mechanism_hypothesis candidate)** "Diffuse long-range competitive coupling between distant fields with opposite profiles is required for stable, synergistic, hierarchical cognifold dynamics; an all-cooperative cognifold over-synchronises." Falsifiable in principle (a multi-field coupling ablation: cooperative-only vs cooperative+long-range-competitive), but **substrate-gated** -- V3 has no explicit multi-field signed-edge layer to ablate, so a probe today would be vacuous. `epistemic_category: substrate_ceiling`, `implementation_phase: v4`.

All three are **compass-grade**. The disciplined near-term move is the architecture note in Next Steps, not registration.

---

## 6. Cautions / guardrails (carry forward verbatim)

From the raw note -- preserve for any future agent who picks this up:

- Competition **!=** synaptic inhibition. (Luppi et al. say so explicitly.)
- A negative/competitive edge is **not** intrinsically harmful, pathological, or ethically negative.
- Competition is **not** reward subtraction / punishment. It is a structural relation between active fields.
- The paper does **not** prove REE's architecture. It is corroborating compass, not evidence for a claim.
- **Do not** make this a V3 implementation target absent a specific existing claim or substrate gap. ([biology-before-formal-definitions] applies: any future SD/MECH instantiating "signed coupling" gets a biology lit-pull first.)
- **Do not** "add inhibition everywhere." The correct extraction is: *preserve signed competitive coupling as a possible constructive cognifold primitive.*

---

## 7. Next steps

1. **(Optional, when motivated) Architecture note.** The thought proposes `docs/architecture/cognifold_signed_coupling.md`. Defer until a concrete trigger exists (a failure attributable to all-positive coupling, or a V4 cognifold-edge spec pass). If written, it should: (a) inventory where REE already runs competition (MECH-090/ARC-030/MECH-254) vs where it relies on implicit softmax/scalar gating; (b) answer the candidate open question (#5.1) -- which edges genuinely need an explicit `sign`; (c) state the safety differences between inhibition, competition, decommitment (MECH-090/105), and residue-based veto (harm stream / SD-010/011); (d) specify how competitive coupling should differ across waking action vs simulation (MECH-094) vs offline integration (MECH-272/273 sleep cluster).
2. **Fold into the attention-MAP work, not a parallel module.** This thought is the **same situation** as the [attention = distributed precision-selection control] note: REE owns the competitive pieces but lacks a unifying map. Treat "signed coupling" as a companion axis to that map; do **not** build a separate competitive-coupling module. Containment-only for V3.
3. **No experiment queued.** Substrate-gated (#5.3); a probe on the current V3 substrate would be vacuous (no explicit multi-field signed-edge layer to ablate). Revisit only if/when a V4 cognifold-edge layer is specced.
4. **Cross-repo pointer (not this session):** the AI-cognitive-failure-taxonomy re-indexing by competitive-coupling axis belongs in `Latent-Fields/ai-cognitive-failure-taxonomy`, not REE_assembly. Note as a future cross-repo item only.

---

*Stage-2 intake authored 2026-06-09. No claims.yaml edit, no substrate change, no experiment queued. Compass / architecture-principle capture; off the V3 / GAP-7 critical path.*
