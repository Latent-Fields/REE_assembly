# Thought Intake (Structured): Contextual Memory Allocation Gate

**Raw thought file:** `docs/thoughts/2026-06-06_contextual_memory_allocation_gate.md`
**Date:** 2026-06-06
**Status:** Stage-2 structured intake -- NOT promoted to claims. No `claims.yaml` edits made.
**Disposition:** V4/V5 substrate territory; **off the V3 critical path**. V3 relevance is conditional
(see Section 7).
**Source:** de Sousa et al., "The prefrontal cortex controls memory organization in the hippocampus,"
*Nature Neuroscience*, 28 April 2026. https://www.nature.com/articles/s41593-026-02231-1

---

## 1. Verbatim seed

> "This looks very relevant for REE."

Source finding (paraphrased): prior memories can be integrated with new experiences, but the process
must be regulated to avoid inappropriate linking of unrelated memories. In mice, the **ventromedial
prefrontal cortex** controls memory integration in the hippocampus according to **contextual
similarity**, via projections to the **medial entorhinal cortex**, affecting entorhinal activity,
dorsal-CA1 ensemble overlap, memory linking, neurogliaform cells in dorsal CA1, and memory allocation.
The vmPFC helps determine whether two memories become linked or stay separate -- **especially when
separated by days rather than hours** (temporal-distance dependence). Treat as
**constraint-inspiration**, not proof of any REE module. The UCLA release's psychiatric framing
(schizophrenia, bipolar) is **translational speculation** from mouse circuit work.

---

## 2. The REE abstraction

```
new experience arrives
 -> compare with prior memory traces (context similarity, temporal distance, schema fit, salience, uncertainty)
 -> regulate overlap
 -> integrate | partially integrate | separate
```

Reframed as a candidate primitive: **Contextual Memory Allocation Gate** -- a control-plane-regulated
write policy over the hippocampal graph. Not "memory storage"; **memory topology control**. The deeper
principle the paper supplies: *memory organization is an active control problem*, not a passive store.

Inputs (candidate): context_similarity, temporal_distance, schema_fit, salience, prediction_error,
uncertainty, consolidation_strength, reality_coherence, goal_relevance, affective_charge.
Outputs (candidate): integrate, separate, partial_overlap, defer, mark_conflict.

Biological -> REE mapping:

| Biology (de Sousa 2026) | REE |
|---|---|
| ventromedial PFC | prefrontal control plane (SD-033 PFC subdivisions; ARC-035 vmPFC) |
| -> medial entorhinal cortex | memory interface / indexing / cue-query layer (SD-016) |
| -> dorsal hippocampal CA1 | hippocampal relational graph (ARC-007 residue-field terrain) |
| ensemble overlap / separation | trace overlap / schema integration vs separation |

---

## 3. What's new vs existing REE docs (novelty / overlap)

The decisive finding from the overlap pass: **REE already owns the gates; it does not own the gating
policy.** All cited IDs verified present in `docs/claims/claims.yaml` 2026-06-06.

| Proposal aspect | REE status | Existing IDs | Overlap |
|---|---|---|---|
| Hippocampal linking/separation substrate | Implemented | ARC-007 (residue-field path terrain), MECH-044 (relational binding/comparison), SD-004 (action-object map backbone) | HIGH |
| Pattern separation (DG-like) | **Planned, V4** | MECH-147 (DG sparse non-redundant encoding of similar z_world before rollout) | MEDIUM -- problem named, not built |
| Schema integration / consolidation | Implemented (offline) | MECH-272 (state-gated wake/sleep routing), MECH-273 (multi-episode self-model aggregation), INV-039 (schema-primed rapid assimilation; rate gated by map stability), SD-017 (SWS/REM replay infra) | HIGH |
| Write-gating / contamination prevention | Implemented + empirically validated | MECH-094 (hypothesis tag = categorical write gate), MECH-261 (mode-conditioned write gating, soft-mode generalization of MECH-094), SD-016 (z_world-only cue-isolated query); write-locus contamination EVB-0043 PASS (46x field inflation when polluted) | VERY HIGH |
| Integration-vs-retrieval distinction | Emerging / implicit | MECH-257 (dual-function gated readout: retrospective attribution vs prospective evaluation), ARC-035 (stored != active; vmPFC converts stored -> active at eval time), MECH-150/151/152 (cue retrieval feeds bias, decoupled from integration) | HIGH |
| Top-down control of memory writes | Implemented | MECH-261, MECH-094, ARC-035, SD-033 (PFC subdivision write targets) | VERY HIGH |
| **Control-plane decision *algorithm* (when to engage the gates)** | **NOT PRESENT** | none | **NOVEL** |
| **context_similarity + temporal_distance + schema_fit as explicit gating variables** | **NOT PRESENT** | none | **NOVEL** |

**Net novelty:** a *gating policy* layered over REE's existing write-gate + mode-conditioning
infrastructure, with **temporal distance** (days-vs-hours, per de Sousa) and **reality-coherence
risk** as first-class gating variables. The substrate to host it largely exists.

---

## 4. Candidate claims (NOT registered -- do not promote until they survive comparison above)

These are recorded as candidates only. Several would be *amendments to existing claims* rather than new
IDs, given the VERY HIGH overlap on write-gating.

- **(invariant candidate) Memory linking must be regulated.** "Adaptive memory requires controlled
  overlap." A system that cannot integrate cannot generalise; a system that cannot separate cannot
  preserve reality coherence -> viable cognition requires an active gate over memory overlap.
  *Caution:* may be subsumed by the MECH-094/MECH-261 cluster + INV-039; check before minting an INV.
- **(mechanism candidate) PFC -> hippocampal overlap control.** Higher-order context model controls
  memory write/allocation, regulating overlap between old and new traces. *Likely an enrichment of
  MECH-261 (add an allocation-decision stage) rather than a new MECH.*
- **(implementation principle) Context similarity + temporal distance as memory-linking variables.**
  V4/V5 memory architecture; pairs with MECH-147 (DG separation) and the MEC indexing layer.
- **(cost-term principle) Reality-coherence cost on memory linking + explicit false-linking-risk
  track.** The genuinely new lever; nothing in REE currently prices false linking at allocation time.

Claims-matrix framing (status / source / REE impact):
- "Memory integration must be actively regulated" -- strong candidate; de Sousa 2026; supports explicit
  allocation gate.
- "PFC can control hippocampal memory organization" -- biological support (mouse); supports
  control-plane-over-memory-write analogy (already substantially present in REE).
- "False association can arise from inappropriate integration" -- plausible, source-supported in broad
  framing; psychiatric extrapolation stays cautious; supports reality-coherence cost on linking.
- "Implement contextual similarity + temporal distance as linking variables" -- candidate
  implementation principle; useful for v4/v5.

---

## 5. Possible implementation abstraction (illustrative, not a spec)

A control-plane-regulated write policy, *not* a single rigid rule:

```python
def allocate_memory_trace(new_trace, candidate_old_traces, control_state):
    scored = []
    for old in candidate_old_traces:
        pressure = (
            compare_context(new_trace, old)            # similarity
            + estimate_schema_fit(new_trace, old)
            + control_state.goal_relevance
            - temporal_gap_weight(estimate_temporal_distance(new_trace, old))  # days-vs-hours
            - estimate_uncertainty(new_trace, old)
            - estimate_false_linking_risk(new_trace, old)                      # reality-coherence cost
        )
        scored.append((old, pressure))
    best, pressure = max(scored, key=lambda x: x[1])
    if pressure > control_state.integration_threshold:  return integrate(new_trace, best)
    if pressure < control_state.separation_threshold:   return allocate_separate_trace(new_trace)
    return partial_overlap(new_trace, best)
```

In REE terms: the control plane (vmPFC/SD-033) sets the thresholds and the `false_linking_risk` /
`temporal_gap` weights; the policy decides whether the new state-node shares edges with a prior node in
the ARC-007 residue graph; MECH-094/MECH-261 remain the *gates* this policy actuates.

---

## 6. Open questions (with what the overlap pass already settles)

- **Q1. Does REE distinguish memory integration from retrieval?** *Partially, and implicitly* --
  MECH-257 (retrospective vs prospective readout modes), ARC-035 (stored != active), MECH-150/151/152
  (retrieval feeds bias, decoupled from integration). The *integration-decision-as-algorithm* is not
  formalized. So the gap is formalization, not absence.
- **Q2. Are current V3 failures better described as insufficient action pressure, poor goal-stream
  lift, memory contamination, or weak state distinction?** Open -- this gate is only V3-relevant if the
  answer turns out to be *memory contamination* or *weak state distinction* / overgeneralisation across
  runs. Current active V3 threads (cue-authority 638b/640a, goal-pipeline GAP-7) point at action
  pressure / goal-stream lift, not memory contamination -> reinforces V4/V5 disposition.
- **Q3.** Which signals should govern linking -- reality coherence, goal relevance, affective salience,
  temporal distance, or all? (Candidate: all, weighted by control plane.)
- **Q4.** Does REE need an explicit "do not link" (separate) operation distinct from "no match"? (de
  Sousa suggests active separation, not just failed integration.)
- **Q5.** Psychosis-like false association ~ salience high + separation gate weak + reality coherence
  low? (Speculative; keep in `docs/conflicts/` territory, not a claim.)
- **Q6.** Rumination ~ repeated partial-integration attempts without schema resolution?
- **Q7.** Trauma-like overbinding ~ high affective charge overriding contextual separation? (Cf.
  MECH-094 tag loss already maps to confabulation, per memory `psychosis_confabulation_distinction` --
  keep these mechanistically distinct.)

---

## 7. Disposition / next steps

1. **No promotion now.** Candidate claims in Section 4 stay candidates. The strongest are *amendments*
   to MECH-261 (add an allocation-decision stage) and a new *false-linking-risk / reality-coherence
   cost* lever -- not a fresh INV.
2. **V3:** do **not** build biological memory allocation. Add a lightweight contamination/overlap check
   **only if** Q2 resolves toward memory contamination / false cross-run reuse / overgeneralisation.
3. **V4/V5:** build explicit allocation policy; separate trace *creation* from trace *integration*; add
   reality-coherence cost to linking; track false-linking risk; pair with MECH-147 (DG separation) and
   an MEC-analog indexing layer.
4. **Lit: DONE 2026-06-06.** The `/lit-pull` on hippocampal pattern-separation / schema-gated
   integration has been run. **Verdict:**
   `evidence/literature/targeted_review_contextual_memory_allocation_gate/VERDICT.md`
   (5 entries: de Sousa 2026 anchor + Cai 2016 / Bakker 2008 / Tse 2007 / Sahay 2011; all *supports*,
   mean ~0.73, no weakening; candidate-isolated, zero registered-claim contamination). The candidate
   claims **survive comparison** as enrichment + one new cost term (not a standalone mechanism). The
   three gated next steps below are the verdict's recommendations -- **all require user/governance
   decision; none executed.**

### 7a. Gated next steps (from the 2026-06-06 lit-pull verdict -- resume here)

- **G1 (claims, V4).** Amend **MECH-261** with an explicit *allocation-decision stage*
  (inputs: `context_similarity x temporal_distance x schema_fit`; outputs: integrate / partial_overlap /
  separate), citing de Sousa 2026 + Cai 2016 + Bakker 2008. Do **not** mint a new INV (subsumed by
  MECH-094/261 + INV-039).
- **G2 (claims, V4).** Mint **one** new candidate only -- a *false-linking-risk / reality-coherence
  cost* term -- as `substrate_conditional` (no V3 substrate to test it on). This is the single aspect
  with no existing REE home. Verdict caveat: the cost is so far *one-sided* (Sahay evidences only the
  under-separation pole); the V4 design must price **both** over- and under-linking.
- **G3 (design).** Revise this intake's Section-5 `allocate_memory_trace` sketch so `temporal_distance`
  x `context_similarity` is an **interaction**, not additive (de Sousa: similar contexts link even at
  7 days; temporal distance is overridable by similarity).
- **Pre-conditions unchanged:** G1-G3 stay V4/V5, off the V3 critical path. Pair the build with
  **MECH-147** (DG separation) + an MEC-analog indexing layer (SD-016). V3 relevance still conditional
  on Q2 (Section 6).
5. **Object-representation thread** (memory `project_object_representation_thread`) is an adjacent
   V4-leaning spine; if an ARC-OBJ umbrella is ever minted, this gate is a natural child.

---

## 8. REE phrasing (capture)

> Memory is not a passive store; memory is a topology under governance. The system must decide not only
> what happened, but what this belongs with. Generalisation and delusion are neighbours -- both depend
> on linking traces; the difference is whether the overlap is governed. Too little overlap prevents
> learning; too much corrupts reality coherence.

**Confidence (from source):** training-data 0.82; epistemic 0.74 (strong as intake; lower for any
psychiatric extrapolation -- mouse circuit work, not human clinical evidence).
