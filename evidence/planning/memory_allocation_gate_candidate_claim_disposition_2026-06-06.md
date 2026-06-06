# Candidate-Claim Disposition: Contextual Memory Allocation Gate

**Date:** 2026-06-06
**Author:** governance-decision pass (session `govdecision-memory-allocation-gate-disposition-20260606T0614Z`)
**Status:** RECOMMENDATION ONLY -- no `claims.yaml` edits made. Awaiting user sign-off.
**Inputs read:**
- Intake: `evidence/planning/thought_intake_2026-06-06_contextual_memory_allocation_gate.md` (Section 3 novelty table, Section 4 candidates)
- Raw: `docs/thoughts/2026-06-06_contextual_memory_allocation_gate.md`
- Live claim entries: MECH-261 (claims.yaml:20053), MECH-094 (4617), MECH-147 (9949), INV-039 (10076)
- Literature dir scan + in-flight sibling lit-pull (see "Lit gating" below)

**Disposition envelope:** V4/V5 territory, **OFF the V3 critical path**. Nothing here is scoped into
V3. This pass does not promote anything; it routes each Section-4 candidate to one of: AMEND existing
claim / NEW candidate ID / KEEP-as-candidate (or do-not-register).

---

## 0. The settled finding (carried from the intake's overlap pass)

REE **already owns the gates; it does not own the gating policy.** Verified present in claims.yaml:

- Write-gating (VERY HIGH overlap): MECH-094 (hypothesis tag / simulation-real write distinction,
  **stable**, conf 0.868) and MECH-261 (mode-conditioned write-gate family, soft mode vector,
  **stable**, conf 0.891) -- MECH-261 explicitly generalises MECH-094.
- Schema consolidation **rate** gating: INV-039 (schema-primed rapid assimilation -- gates
  consolidation *rate* by map stability, **candidate**, V4, emergent invariant).
- Pattern separation: MECH-147 (DG sparse non-redundant encoding, **candidate**, V4).
- Top-down control: ARC-035 (vmPFC stored!=active), SD-033 (PFC subdivision write targets).

The genuinely uncovered pieces, restated precisely after reading the live entries:

1. **An allocation-*decision* algorithm** -- when to engage the gates, and toward which outcome
   (integrate / separate / partial-overlap). MECH-261 decides *write eligibility by mode*; it does
   not decide *trace-overlap topology*. INV-039 gates *rate*, not *overlap*. So overlap-topology
   regulation is genuinely uncovered.
2. **`context_similarity` / `temporal_distance` / `schema_fit` as explicit gating variables.**
   `temporal_distance` (days-vs-hours, per de Sousa) is the most clearly novel -- no REE claim
   currently conditions linking on inter-trace temporal gap.
3. **A reality-coherence / false-linking-risk COST at allocation time.** REE prices nothing for
   false linking today. This is the zero-overlap item -- not even partially covered.

---

## Lit gating (decisive for B and D)

**Biology-before-formal-definitions applies.** Both the allocation-policy mechanism (B) and the
false-linking-risk cost (D) instantiate formal constructs (a decision policy over a similarity/
distance/schema-fit objective; a cost function over a coherence metric). Per
`feedback_biology_before_formal_definitions`, these need a biology lit-pull **before** registration
(canonical philosophy-right/mechanism-wrong failures: SD-003, SD-010/011).

**A sibling lit-pull is already in flight** (TASK_CLAIMS active:
`litpull-contextual-memory-allocation-gate-20260606T0612Z`, slug
`targeted_review_contextual_memory_allocation_gate`). As of this writing the slug directory has
**no entries and no `verdict.md`** -- the pull is claimed but not yet produced. Its VERDICT is
chartered to answer exactly the three questions B/D turn on:
(a) distinct mechanism vs MECH-261 enrichment; (b) is temporal-distance a first-class variable;
(c) is a reality-coherence/false-linking cost biologically motivated.

**Therefore: register nothing from B/D until that VERDICT lands.** Gating registration behind the
in-flight pull (rather than registering blind) is the protocol-correct move.

---

## 1. Per-candidate disposition

### Candidate A -- (invariant) "Memory linking must be regulated"
**Recommendation: KEEP-AS-CANDIDATE. Do NOT mint an INV now.**

- **Largely subsumed** by the existing cluster: MECH-094 + MECH-261 (the write gates) + INV-039
  (consolidation-rate gating). The broad statement "adaptive memory requires controlled overlap" is
  not, on its own, a new invariant the registry lacks at the level of *general principle*.
- **But there is a genuine uncovered kernel** worth recording so it is not lost: existing claims
  regulate *write eligibility* (094/261) and *consolidation rate* (INV-039); **none regulate
  overlap topology** (the integrate-vs-separate-vs-partial decision over the ARC-007 residue graph).
  That is the real invariant content, and it is narrower than the broad framing.
- **Why not mint now:** as an emergent invariant it would need `emergent_from` substrate that does
  not exist yet -- the allocation policy (Candidate B) is the substrate that would give this
  invariant its subject matter. Minting an emergent invariant ahead of its substrate inverts the
  governance order (cf. INV-039, which is itself still `candidate`/V4 and carries
  `pending_substrate_reconfirmation: true`). Mint, if ever, only after B's substrate is designed
  and the lit VERDICT supports it.
- **Action:** leave as intake candidate; note the "overlap-topology regulation" kernel as the
  registerable core (not the broad version) for future consideration.

### Candidate B -- (mechanism) "PFC -> hippocampal overlap control" (the allocation-decision stage)
**Recommendation: NEW candidate MECH (V4), GATED behind the lit VERDICT -- NOT an in-place
amendment to MECH-261. Present amend-vs-new-child to the user as the open decision.**

The intake's leading hypothesis was "enrichment of MECH-261 (add an allocation-decision stage)."
After reading MECH-261's live entry I recommend **against editing MECH-261 in place**, for three
reasons:

1. **Evidence-hygiene.** MECH-261 is **stable** with a curated evidence record (33 supports / 3
   weakens across 16 exp + 20 lit; conf 0.891; documented seed-reproducibility weakens). Folding a
   V4 allocation-policy stage into its text would attach a not-yet-evidenced mechanism to a stable
   V3 claim's record and muddy what its experiments actually validated.
2. **Mechanistic distinctness.** MECH-261 is a *write-gate family* (which substrates may write,
   conditioned on operating mode). The allocation policy is a *decision over trace topology*
   (integrate/separate/partial, conditioned on context-similarity / temporal-distance / schema-fit /
   false-linking-risk). The policy **actuates** the 094/261 gates but is not one of them -- exactly
   the "owns the gates, not the policy" finding. A child claim that `depends_on` MECH-261 expresses
   this layering faithfully; an in-place edit conflates gate with policy.
3. **Phase mismatch.** MECH-261 is V3/`implementation_phase: v3`; the allocation policy is V4. A new
   `implementation_phase: v4` MECH keeps the phase boundary clean.

**Proposed shape (for after VERDICT + sign-off, NOT to register now):**
- New `MECH-xxx` (next free ID at write time), `claim_type: mechanism_hypothesis`,
  `status: candidate`, `implementation_phase: v4`.
- `depends_on`: MECH-261 (the gates it actuates), MECH-094 (strict default), MECH-147 (DG
  separation primitive), ARC-007 (residue-graph terrain), SD-033c (vmPFC-analog control plane).
- Functional content: a control-plane-set decision stage that, per incoming trace, scores candidate
  prior traces and emits integrate / separate / partial-overlap, with thresholds and weights set by
  the control plane. Fold Candidate C's variables in here (below).
- **Falsifier** (so it is not unfalsifiable design): an implementation with *no* allocation policy
  (write gates only) should show measurably worse separation of unrelated traces / more cross-context
  contamination than one with the policy, on a task with day-scale vs hour-scale trace gaps.

**User decision to surface:** new-child-MECH (recommended) vs in-place MECH-261 amendment. I
recommend new-child.

### Candidate C -- (implementation principle) "context similarity + temporal distance as linking variables"
**Recommendation: NOT a standalone claim. Fold into Candidate B's functional restatement as its
input variables.**

- This is a design/implementation detail (the variable set of B's scoring function), not an
  independent assertion. It should not get its own ID.
- **`temporal_distance` (days-vs-hours) is the genuinely novel variable** and the one the lit-pull
  must confirm as first-class (its question (b)). Record it as B's distinctive input; do not register
  separately.

### Candidate D -- (cost-term) "Reality-coherence cost / false-linking-risk track"
**Recommendation: STRONGEST new-ID candidate, but GATED behind the lit VERDICT. Recommend folding
into Candidate B as its signature cost term rather than minting a separate ID -- present the
fold-vs-separate choice to the user.**

- This is the **zero-overlap** item: nothing in REE prices false linking at allocation time. It is
  what makes B *novel* rather than redundant with MECH-261 -- without the false-linking-risk cost,
  B reduces to "a policy that opens the existing gates."
- **Formal-construct flag:** a cost function over a reality-coherence metric is exactly the kind of
  formalism that `feedback_biology_before_formal_definitions` says must be biology-grounded first.
  The lit-pull's question (c) is chartered to test whether active separation / false-linking cost is
  biologically motivated (de Sousa's "active separation, not merely failed integration"; the
  generalisation/delusion-boundary framing). **Do not register D until (c) returns supportive.**
- **Structure recommendation:** fold D into B as B's distinctive cost term (one mechanism: "allocation
  policy whose signature lever is a false-linking-risk cost"). A separate tiny cost-lever ID risks
  claim proliferation and an orphan term with no host mechanism. If the user prefers it visible as
  its own lever, a separate `MECH-xxx` (cost-term) depending on B is acceptable -- surface as a
  choice.
- **Keep psychiatric framing out of claims.** Psychosis = high salience + weak separation + low
  reality coherence is translational speculation from mouse work; keep in `docs/conflicts/` territory,
  not a claim. Honour `psychosis_confabulation_distinction`: MECH-094 tag-loss maps to *confabulation*
  specifically -- do not let D's reality-coherence framing re-absorb that distinction.

---

## 2. Net recommendation

**Register NOTHING now. All four stay candidates.** Concretely:

| Candidate | Disposition | Gate before any registration |
|---|---|---|
| A "linking must be regulated" (INV) | KEEP-CANDIDATE; do-not-mint. Record narrowed kernel = *overlap-topology regulation* (distinct from 094/261 eligibility + INV-039 rate). | Mint only after B's substrate exists (emergent invariant needs `emergent_from`). |
| B PFC->HC overlap control (MECH) | NEW candidate MECH (V4), **not** in-place MECH-261 amend. | Lit VERDICT question (a) + user decision new-child-vs-amend. |
| C similarity + temporal-distance vars | NOT a claim; fold into B's restatement (`temporal_distance` = novel input). | n/a (subsumed by B). |
| D reality-coherence / false-linking cost (MECH cost-term) | Strongest new lever; **fold into B** (or separate ID if user prefers). | Lit VERDICT question (c) MUST return supportive; user fold-vs-separate choice. |

**Sequencing:**
1. Let the in-flight `targeted_review_contextual_memory_allocation_gate` lit-pull complete and emit
   `verdict.md`.
2. If VERDICT supports (a)+(b)+(c): bring B (with C folded in, D as its cost term) back for
   registration as a single V4 candidate MECH `depends_on` MECH-261/094/147 + ARC-007/SD-033c. Get a
   fresh max-ID at write time.
3. Revisit A (overlap-topology invariant) only once B's substrate is designed.
4. None of this enters the V3 critical path.

**STOP -- user sign-off required before any `claims.yaml` edit.** This memo makes no registry change.
