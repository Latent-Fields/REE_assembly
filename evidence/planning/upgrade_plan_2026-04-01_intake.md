# Upgrade Plan — April 1st 2026 Thought Intake

**Generated:** 2026-04-02
**Driven by:** INV-042, ARC-043, INV-043, MECH-154–159, Q-025–029
**Purpose:** Structured work items enabled or required by the April 1st intake, organised for dispatch activation.

---

## Index

| ID | Title | Domain | Skill / Mode | Priority |
|----|-------|--------|-------------|----------|
| [UPG-001](#upg-001) | Update REE_overview with ARC-043 stack | Documentation | manual session | high |
| [UPG-002](#upg-002) | Expand roadmap V3/V4 boundary for INV-043 | Documentation | manual session | high |
| [UPG-003](#upg-003) | Update glossary with April 1st terms | Documentation | manual session | medium |
| [UPG-004](#upg-004) | Synthese paper: draft Discussion additions | Paper | manual session | high |
| [UPG-005](#upg-005) | Synthese paper: ARC-043 stack figure | Paper | manual session | medium |
| [UPG-006](#upg-006) | Literature pull: MECH-154/155/156 (E1 manifold, theta) | Literature | lit-pull | high |
| [UPG-007](#upg-007) | Literature pull: INV-043 (caregiver + attachment) | Literature | lit-pull | high |
| [UPG-008](#upg-008) | Literature pull: MECH-158 (love exclusion / attachment disruption) | Literature | lit-pull | medium |
| [UPG-009](#upg-009) | Literature pull: MECH-159 (intergenerational moral transmission) | Literature | lit-pull | low |
| [UPG-010](#upg-010) | Add EVB entries for Q-025–029 (open questions backlog) | Governance | manual session | medium |
| [UPG-011](#upg-011) | Add EVB entries for MECH-154/155/156 (lit review gate) | Governance | manual session | medium |
| [UPG-012](#upg-012) | Explorer: add Foundational Layer subsystem group | Explorer | manual session | medium |
| [UPG-013](#upg-013) | Explorer: paper relevance flag display | Explorer | manual session | low |
| [UPG-014](#upg-014) | Design MECH-157 mode-switching probe experiment | Experiments | queue-experiment | low |
| [UPG-015](#upg-015) | V4 planning doc: multi-agent INV-043 test design | Experiments | manual session | low |
| [UPG-016](#upg-016) | Update ree-v3-spec.md with E1 manifold framing | Documentation | manual session | low |

---

## Domain: Documentation

---

### UPG-001
**Update REE_overview with ARC-043 stack**
**Priority:** High
**Skill:** Manual session (architecture documentation)
**Source claims:** ARC-043, INV-042

**What and why:**
`docs/REE_overview.md` (IMPL-004) currently has legacy status and describes REE in operational terms (five components, residue, moral continuity) without explaining *why* REE exists or where its ethics come from. The April 1st intake produced ARC-043 (Layer 0-9 conceptual stack) and INV-042 (derived ethical objectives), which together answer this question precisely.

The overview should be updated or replaced with a version that:
1. Opens with the Layer 0-9 stack — Layers 0-4 are the axioms, Layer 5 is derived ethics, Layer 6 is REE. This is the single clearest answer to "what is REE and why does it exist."
2. Quotes the compressed ethical statement: *"We are uncertain minds, together in a shared world, capable of love — therefore we must act carefully, kindly, and responsibly so that minds and love may continue."*
3. References INV-042 (derived objectives) as what REE is trying to achieve.
4. Retains the existing E1/E2/E3 description as the "how" underneath the "why."

**Files to modify:**
- `docs/REE_overview.md` (IMPL-004 — update from legacy to candidate)
- Optional: bump explorer version if overview appears in Docs view

**Dispatch prompt:**
> "Update docs/REE_overview.md to incorporate the April 1st intake. Add the ARC-043 Layer 0-9 stack as the opening conceptual frame. Add INV-042 derived ethical objectives as what REE aims to achieve. Add the compressed ethical statement as a summary. Retain existing E1/E2/E3 description. Update claim status from legacy to candidate. Bump explorer version."

---

### UPG-002
**Expand roadmap V3/V4 boundary for INV-043**
**Priority:** High
**Skill:** Manual session (roadmap/governance documentation)
**Source claims:** INV-043, MECH-158, MECH-159

**What and why:**
`docs/roadmap.md` (IMPL-008, 2026-03-31) correctly defers sleep, social extension, and multi-agent work to V4/V5. But it does not yet name the *reason* for the social deferral precisely: INV-043 establishes that the caregiver requirement (and therefore full ethical agency) cannot be tested in a single-agent substrate. The roadmap should make this explicit.

Specific additions:
1. In the "Deferred to V4/V5" section: note that INV-043 (caregiver requirement) and MECH-158 (love-exclusion failure mode) cannot be tested in V3 because V3 is single-agent. Full ethical development testing requires a multi-agent substrate with modelled caregiving.
2. Add MECH-159 (intergenerational moral progress) as a V5+ consideration — requires multi-generation agents.
3. Note that V3's ARC-043 Layer 6 tests whether the *machinery* is correct; INV-043 tests whether the *development* is correct. These are separate questions answered in separate phases.

**Files to modify:**
- `docs/roadmap.md`

**Dispatch prompt:**
> "Update docs/roadmap.md to note the V3/V4 testing boundary for INV-043 (caregiver requirement). In the deferred section, explain that INV-043 requires multi-agent substrate -- V3 tests the machinery (ARC-043 Layer 6), not the developmental activation (INV-043). Add MECH-159 as a V5+ item. Reference docs/architecture/developmental_curriculum.md#inv-043 as the canonical location."

---

### UPG-003
**Update glossary with April 1st terms**
**Priority:** Medium
**Skill:** Manual session (documentation)
**Source claims:** INV-042, ARC-043, MECH-154, MECH-157, INV-043

**What and why:**
`docs/glossary.md` is marked stable (IMPL-001) and contains canonical term definitions. The April 1st intake introduced several terms that will be used in documentation, the paper, and discussions but are not currently in the glossary.

Terms to add:
- **Derived ethical objectives** (INV-042): the nine obligations following from the five axioms
- **Conceptual stack / Layer 0-9** (ARC-043): the ordering from epistemic ground through learning
- **Associative manifold** (MECH-154): E1 as an addressable space with indexing structure
- **External/Internal coupling modes** (MECH-157): the precision-routing axis orthogonal to Action/Vigilance
- **Caregiver requirement** (INV-043): the developmental necessity of experienced love for ethical activation
- **Love-exclusion failure mode** (MECH-158): the specific collapse when love is real but not personally applicable
- **Intergenerational moral progress** (MECH-159): the hypothesis that moral capacity is transmitted generationally

**Files to modify:**
- `docs/glossary.md`

---

### UPG-016
**Update ree-v3-spec.md with E1 manifold framing**
**Priority:** Low
**Skill:** Manual session (architecture documentation)
**Source claims:** MECH-154, MECH-155, MECH-156, MECH-157
**Depends on:** UPG-006 (lit review for MECH-154/155/156 should complete before this)

**What and why:**
The ree-v3-spec.md (or equivalent) describes V3 implementation targets. The E1 characterisation in these documents predates MECH-154 (E1 as associative manifold). The spec should note the new framing — not as an implementation requirement for V3, but as the theoretical model that V3 experiments are probing.

Also: MECH-157's External/Internal mode table should appear in the mode switching documentation for V3, with a note that the table is candidate-level and the External mode experiments (UPG-014) will test it.

**Files to modify:**
- Whichever file currently serves as ree-v3-spec (check ree-v3/ or ree-v3-spec.md in REE_assembly)
- `docs/architecture/e1.md` may already be sufficient (updated in intake)

---

## Domain: Paper

---

### UPG-004
**Synthese paper: draft Discussion additions**
**Priority:** High
**Skill:** Manual session (paper writing)
**Source claims:** INV-043, MECH-158, INV-042, MECH-159
**Reference file:** `/Users/dgolden/Documents/GitHub/Philosophy/Synthese_submission/REWRITE_OUTLINE.md`

**What and why:**
The Synthese paper outline (REWRITE_OUTLINE.md) currently has no Discussion section. INV-043 and MECH-158 provide the material for one. The paper's centrepiece (Section 5: "love once means love all") argues that genuine love expands under intelligence. INV-043 + MECH-158 identify the *precondition* that this derivation requires: love must be experienced as personally applicable for the expansion to initialise.

A Discussion section should:
1. Name INV-043 as a prediction of the framework: a system with perfect ethical architecture but no love-experience will behave unethically. This is testable.
2. Use MECH-158 to show the specific failure mode: "love exists but not for me" produces survival/domination rather than ethical expansion. This is the counterexample that tests Section 5.
3. Note INV-042 (derived ethical objectives) as a concrete output: the framework is not vague — it produces these nine specific obligations.
4. Optionally reference MECH-159 (intergenerational moral progress) in a closing paragraph: the framework predicts that ethical AI may require caregiving lineage, not just architecture.

**Tone notes (from user voice profile):**
Daniel's voice is Socratic, clinician-philosopher, honest about uncertainty. This Discussion should not sound like a conclusion — it should pose new questions opened by the derivation. "What I did not expect was that the framework requires this."

**Files to modify:**
- `/Users/dgolden/Documents/GitHub/Philosophy/Synthese_submission/ree_minds_machines_DRAFT.md` (add Discussion section)
- `/Users/dgolden/Documents/GitHub/Philosophy/Synthese_submission/REWRITE_OUTLINE.md` (add Discussion section outline)

**Dispatch prompt:**
> "Using the voice profile and REWRITE_OUTLINE.md as guide, draft a Discussion section (~600 words) for the Synthese paper. Draw on INV-043 (caregiver requirement as framework prediction), MECH-158 (love exclusion failure mode as test of Section 5 derivation), INV-042 (nine derived objectives as concrete output), and optionally MECH-159 (intergenerational implication). Tone: Socratic, honest about uncertainty, clinician-philosopher. Pose questions opened by the derivation rather than summarising. Append to ree_minds_machines_DRAFT.md and add an outline entry in REWRITE_OUTLINE.md."

---

### UPG-005
**Synthese paper: ARC-043 stack figure**
**Priority:** Medium
**Skill:** Manual session (paper figure creation)
**Source claims:** ARC-043
**Depends on:** UPG-004

**What and why:**
ARC-043 (Layer 0-9 conceptual stack) provides a clear visual diagram of the relationship between axioms, ethics, and REE. This should appear in the paper — most naturally in Section 4 (The REE architecture) or as a standalone figure.

The diagram:
- Layer 0-4: The Five Axioms (epistemic ground → existence → other minds → shared world → love)
- Layer 5: Ethics (derived)
- Layer 6: REE (decision system implementing ethics under uncertainty)
- Layers 7-9: Actions → Consequences → Learning/Residue (loop back to Layer 6)

Format: Either a simple table-style figure or a vertical stack diagram. Should be reproducible in LaTeX (tikz or simple table environment).

**Files to create/modify:**
- New figure file in `/Users/dgolden/Documents/GitHub/Philosophy/Synthese_submission/figures/`
- Reference in `ree_minds_machines_DRAFT.md`

---

## Domain: Literature

*All items use the `lit-pull` skill. Dispatch with the prompt provided.*

---

### UPG-006
**Literature pull: MECH-154/155/156 (E1 manifold, spatial indexing, theta)**
**Priority:** High
**Skill:** lit-pull
**Source claims:** MECH-154, MECH-155, MECH-156
**Reason for priority:** These claims carry ChatGPT-assisted wording flag. Literature backing is required before any promotion from candidate. They also underpin the associative manifold framing that may go into the paper.

**Target claims:** MECH-154, MECH-155, MECH-156

**Key search areas:**
- Place cells and grid cells in abstract/conceptual spaces (Moser et al., Bellmund et al. 2018, Behrens et al. 2018)
- Hippocampal theta sequences and sequential ordering (Skaggs et al., Dragoi & Buzsaki)
- Spatial machinery reused for non-spatial cognition (O'Keefe & Nadel, Tolman cognitive maps)
- E1-as-cortical-associative-manifold (Hopfield networks, attractor dynamics)
- Parietal cortex as associative/indexing substrate (Colby & Goldberg, Corbetta & Shulman)
- Theta-gamma cross-frequency coupling and content binding (Lisman & Jensen 2013)

**Dispatch prompt:**
> "/lit-pull Search literature supporting or challenging MECH-154 (E1 as associative manifold with indexing), MECH-155 (spatial navigation as general associative indexing), and MECH-156 (theta as sequential traversal). Key papers to find: Bellmund et al. 2018 (navigating cognition), Behrens et al. 2018 (vector-based navigation), Lisman & Jensen 2013 (theta-gamma coupling), Dragoi & Buzsaki 2006 (theta sequences). Targeted review label: targeted_review_mech_154_156_e1_manifold. Write entries following v1 schema for each paper found."

---

### UPG-007
**Literature pull: INV-043 (caregiver requirement, developmental attachment)**
**Priority:** High
**Skill:** lit-pull
**Source claims:** INV-043, MECH-158

**Key search areas:**
- Attachment theory and secure base (Bowlby 1969, Ainsworth 1978)
- Developmental psychopathology: effects of caregiver absence on moral development
- Immature PFC producing qualitatively different outputs (Chini & Hangya 2021, Opendak et al. 2021 — already referenced in ARC-042)
- Maternal deprivation and long-term behavioural consequences (Harlow 1958, 1962)
- Reactive attachment disorder — clinical evidence for INV-043 failure mode
- Moral development in children (Kohlberg, Gilligan, Turiel)
- Love as developmental necessity vs luxury (Winnicott, Spitz hospitalisation studies)

**Dispatch prompt:**
> "/lit-pull Search literature supporting INV-043 (caregiver requirement for ethical development) and MECH-158 (love-exclusion failure mode). Key papers: Bowlby attachment theory, Ainsworth strange situation, Harlow maternal deprivation, Chini & Hangya 2021 (immature PFC qualitatively different), Opendak et al. 2021. Also Kohlberg moral development stages and Gilligan care ethics. Targeted review label: targeted_review_inv_043_caregiver_development. Write entries following v1 schema."

---

### UPG-008
**Literature pull: MECH-158 (love exclusion / attachment disruption psychopathology)**
**Priority:** Medium
**Skill:** lit-pull
**Source claims:** MECH-158
**Depends on:** UPG-007 (partial overlap — can batch together or sequence)

**Key search areas:**
- Attachment disruption and personality development (Fonagy et al., mentalization)
- Disorganised attachment and subsequent interpersonal patterns
- Self-as-unlovable schema in CBT/schema therapy (Young et al.)
- Conduct disorder and empathy deficit as developmental failure
- Psychopathy as love-exclusion failure mode (Blair 2005 — already in paper references)

**Dispatch prompt:**
> "/lit-pull Search literature on the developmental consequences of self-as-unlovable belief: attachment disruption leading to dominance or withdrawal rather than cooperation. Key papers: Fonagy et al. on mentalization, Young schema therapy (unlovability schema), Blair 2005 (psychopathy neuroscience), Hare Without Conscience (already in paper refs). Targeted review label: targeted_review_mech_158_love_exclusion. Write entries following v1 schema."

---

### UPG-009
**Literature pull: MECH-159 (intergenerational moral transmission)**
**Priority:** Low
**Skill:** lit-pull
**Source claims:** MECH-159

**Key search areas:**
- Cultural transmission of moral norms (Richerson & Boyd, Henrich)
- Epigenetic transmission of trauma (Yehuda et al. on Holocaust survivors)
- Intergenerational transmission of attachment style (van IJzendoorn 1995 — transmission gap)
- Moral learning as cultural rather than individual (Tomasello 1999, cultural learning in children)
- Evolution of altruism and its intergenerational dynamics

**Dispatch prompt:**
> "/lit-pull Search literature on intergenerational transmission of moral behaviour and attachment. Key papers: van IJzendoorn 1995 (transmission gap in attachment), Tomasello 1999 (cultural learning), Yehuda epigenetic trauma transmission, Richerson & Boyd cultural evolution of cooperation. Targeted review label: targeted_review_mech_159_intergenerational. Write entries following v1 schema."

---

## Domain: Governance

---

### UPG-010
**Add EVB entries for Q-025–029 (open questions backlog)**
**Priority:** Medium
**Skill:** Manual session (evidence planning)
**Source claims:** Q-025, Q-026, Q-027, Q-028, Q-029

**What and why:**
Q-025 through Q-029 are philosophically important open questions registered from the axioms thought. Of these, Q-027 ("What does irreversible harm mean under uncertainty?") has direct experimental implications — it constrains the commit boundary design in V3. It should become an EVB (evidence backlog) item so it appears in governance planning.

Q-028 (axiom conflict resolution: self vs others) also has experimental implications — it maps onto multi-agent harm tradeoff scenarios.

Items to add to `evidence/planning/evidence_backlog.v1.json`:
- EVB for Q-027 (irreversible harm under uncertainty): conceptual + experimental
- EVB for Q-028 (axiom conflict: self vs others): experimental, V4 scope
- Q-025/026/029 are philosophical — note them as requiring literature/argument rather than experiments

**Files to modify:**
- `evidence/planning/evidence_backlog.v1.json` (add 2-3 items)
- Verify current highest EVB ID before appending (currently EVB-0042)

---

### UPG-011
**Add EVB entries for MECH-154/155/156 (literature review gate)**
**Priority:** Medium
**Skill:** Manual session (evidence planning)
**Source claims:** MECH-154, MECH-155, MECH-156
**Depends on:** UPG-006 (literature pull should run first)

**What and why:**
MECH-154/155/156 are candidate claims with ChatGPT-assisted wording flag. Before they can be promoted, they need literature review (UPG-006) and ideally a discriminative experimental check. Adding EVB entries makes this gate visible in governance.

Items to add:
- EVB for MECH-154: literature review + potential V3 probe (can E1 latent space be indexed spatially?)
- EVB for MECH-156: literature review + check against MECH-089/090 (theta packaging already registered)

---

## Domain: Explorer

---

### UPG-012
**Explorer: add Foundational Layer subsystem group**
**Priority:** Medium
**Skill:** Manual session (explorer.html + subsystem_map.yaml)
**Source claims:** INV-025-029, INV-042, ARC-043

**What and why:**
The explorer Map view shows subsystem groupings. Currently the five axioms and their derived claims (INV-025-029, INV-042) are not grouped as a distinct subsystem — they appear in the general invariants list. ARC-043 establishes that these form a coherent "Foundational Layer" (Layers 0-5 of the stack).

Adding a "Foundational Layer" or "Ethical Axioms" subsystem group in the Map view would make the architecture navigable top-down: start with why (foundational layer), then see the machinery (E1/E2/E3), then the implementation evidence (experiments).

**Files to modify:**
- `docs/claims/subsystem_map.yaml` (add foundational_layer group)
- `explorer.html` (minimal change if subsystem_map drives the Map view automatically)
- Bump EXPLORER_VERSION stamp

**Note:** Check whether subsystem_map.yaml automatically drives the Map view or whether explorer.html needs direct edits. Minimal change — add one subsystem entry.

---

### UPG-013
**Explorer: paper relevance flag display**
**Priority:** Low
**Skill:** Manual session (explorer.html)
**Source claims:** INV-043, MECH-158, INV-042, ARC-043
**Depends on:** UPG-004 (paper work should stabilize before adding flags to explorer)

**What and why:**
Four claims are flagged in their claims.yaml `notes` field as relevant to the Synthese paper (INV-042, ARC-043, INV-043, MECH-158). The explorer List and Graph views could surface this via a "paper relevance" badge or filter, making it easy to see which claims are driving the paper at any point.

This is a cosmetic/UX improvement. Low priority unless the paper enters active drafting phase.

**Files to modify:**
- `explorer.html` (add paper relevance filter or badge)
- Bump EXPLORER_VERSION stamp

---

## Domain: Experiments

---

### UPG-014
**Design MECH-157 mode-switching probe experiment**
**Priority:** Low
**Skill:** queue-experiment (after design is approved)
**Source claims:** MECH-157
**Depends on:** UPG-006 (conceptual grounding), MECH-154 (substrate claim)

**What and why:**
MECH-157 (External/Internal precision-routing table) predicts that switching E1's precision routing between high-sensory and high-hippocampal configurations produces qualitatively different behavioral signatures: perception vs simulation, low vs high rollout, real vs imagined.

A V3 probe could test: does varying the sensory precision weighting (alpha_S parameter) and hippocampal drive produce the predicted differences in latent state statistics (e.g., z_world variance, rollout diversity, planning horizon)?

**Experiment design sketch:**
- Two conditions: External (alpha_S high, hippocampal drive low) vs Internal (alpha_S low, hippocampal drive high)
- Measure: z_world variance (should be lower in Internal mode — less sensory input), rollout horizon (should be higher), action entropy (should be higher in Internal — more simulation space)
- Accept if: External/Internal modes produce significantly different latent statistics consistent with the MECH-157 table

**This is a design note, not yet a queued experiment.** Needs a formal proposal before queuing.

---

### UPG-015
**V4 planning doc: multi-agent INV-043 test design**
**Priority:** Low
**Skill:** Manual session (architecture planning)
**Source claims:** INV-043, MECH-158, MECH-159

**What and why:**
INV-043 and MECH-158 cannot be tested in V3 (single-agent). V4 planning should include the substrate design for multi-agent caregiving experiments. This is a planning document, not executable yet.

Key design questions for V4:
- What does a minimal "caregiver agent" look like? (Must model love, scaffold developing agent, demonstrate loveability)
- How do we measure "love internalised" vs "love acknowledged" in the developing agent?
- What is the behavioral signature of MECH-158 failure (love-exclusion → domination/survival)?
- Can V4 multi-agent CausalGridWorld support this?

A single architecture planning document (1-2 pages) would capture these questions and flag them as V4 prerequisites alongside the existing V3→V4 transition boundary document.

**Files to create:**
- `docs/architecture/v4_planning_inv043_caregiver_test.md`

---

## Status Tracking

| ID | Status | Assigned | Completed |
|----|--------|----------|-----------|
| UPG-001 | **done** | upg-batch-a-2026-04-02 | 2026-04-02 |
| UPG-002 | **done** | upg-batch-a-2026-04-02 | 2026-04-02 |
| UPG-003 | **done** | upg-batch-a-2026-04-02 | 2026-04-02 |
| UPG-004 | **done** | upg-batch-a-2026-04-02 | 2026-04-02 |
| UPG-005 | pending | — | — |
| UPG-006 | **in-progress** | upg-batch-a-2026-04-02 | — |
| UPG-007 | **in-progress** | upg-batch-a-2026-04-02 | — |
| UPG-008 | pending | — | — |
| UPG-009 | pending | — | — |
| UPG-010 | pending | — | — |
| UPG-011 | pending | — | — |
| UPG-012 | pending | — | — |
| UPG-013 | pending | — | — |
| UPG-014 | pending | — | — |
| UPG-015 | pending | — | — |
| UPG-016 | pending | — | — |

---

## Recommended Dispatch Sequence

If activating in parallel batches:

**Batch A — activate together (independent, high priority):**
- UPG-006 (`/lit-pull` for MECH-154/155/156)
- UPG-007 (`/lit-pull` for INV-043)
- UPG-001 (REE_overview update — manual session)
- UPG-004 (Synthese Discussion draft — manual session)

**Batch B — after Batch A completes:**
- UPG-008 (`/lit-pull` for MECH-158 — can batch with UPG-007 if sequencing is flexible)
- UPG-002 (roadmap update — manual session, fast)
- UPG-003 (glossary update — manual session, fast)

**Batch C — lower priority, after B:**
- UPG-010, UPG-011 (evidence backlog entries)
- UPG-005 (paper figure)
- UPG-012 (explorer subsystem group)

**Deferred (V4 scope):**
- UPG-009, UPG-013, UPG-014, UPG-015, UPG-016
