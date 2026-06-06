# VERDICT -- Contextual Memory Allocation Gate (lit-pull, 2026-06-06)

**Targeted review:** `targeted_review_contextual_memory_allocation_gate`
**Intake:** `evidence/planning/thought_intake_2026-06-06_contextual_memory_allocation_gate.md`
**Disposition:** V4/V5 groundwork; **off the V3 critical path**. Recommendation-only -- **NO `claims.yaml` promotion**.
**Candidate claim isolation:** all entries tagged `CANDIDATE-contextual-memory-allocation-gate` only. **Zero registered claim IDs touched.**

## Papers pulled (5)

| Entry | Paper | Venue / year | Direction | Conf | Role |
|---|---|---|---|---|---|
| desousa2026 | de Sousa et al., PFC controls memory organization in hippocampus | Nat Neurosci 2026 | supports | 0.72 | ANCHOR -- top-down control of linking vs separation |
| cai2016 | Cai et al., shared ensemble links memories encoded close in time | Nature 2016 | supports | 0.76 | temporal distance as a variable |
| bakker2008 | Bakker et al., pattern separation in human CA3/DG | Science 2008 | supports | 0.78 | DG separation effector (MECH-147) |
| tse2007 | Tse et al., schemas and memory consolidation | Science 2007 | supports | 0.68 | schema_fit variable (integrate-pole) |
| sahay2011 | Sahay et al., neurogenesis improves pattern separation | Nature 2011 | supports | 0.70 | false-linking-risk / over-generalization cost |

Aggregate signal: convergent **supports** across one anchor + four siblings, mean confidence ~0.73. No weakening evidence found. The convergence is on the *existence and shape* of the phenomena; it does **not** lift the candidate to registration, because the novel REE lever (a decision algorithm + cost term) is exactly the part the literature does not supply.

---

## (a) Distinct registerable mechanism, or enrichment of MECH-261?

**Verdict: ENRICHMENT of the existing write-gating cluster (lead: amend MECH-261), NOT a new standalone mechanism -- with ONE genuinely new sub-component that is the only registration-worthy novelty.**

The literature confirms the intake's overlap finding rather than overturning it. de Sousa 2026 demonstrates a top-down controller (vmPFC -> MEC -> dCA1, neurogliaform-gated) that decides linking vs separation. Every *structural* element of that circuit already has a REE home: the controller maps to ARC-035 (vmPFC) / SD-033 (PFC subdivisions); the relay to SD-016 (cue-query interface); the relational graph to ARC-007; and the neurogliaform gatekeeper to the categorical write gate MECH-094 and its mode-conditioned generalization MECH-261. Bakker 2008 anchors the separate-pole effector to REE's already-planned MECH-147. So REE owns the gates and the effectors.

What the literature does **not** supply -- and what REE genuinely lacks -- is the **allocation decision algorithm** (when to engage the gates, with what inputs) and a **false-linking-risk / reality-coherence cost** priced at allocation time. de Sousa shows the decision *happens* and is top-down; it does not formalize the rule. This is consistent with the intake's Section 4 read.

Recommendation (gated, NOT executed):
- Register the policy as an **amendment to MECH-261** adding an explicit *allocation-decision stage* (inputs: context_similarity, temporal_distance, schema_fit; outputs: integrate / partial_overlap / separate), citing de Sousa 2026 + Cai 2016 + Bakker 2008. This avoids over-splitting (cf. `feedback_biology_before_formal_definitions`) -- the decision rides on the same write-gate substrate MECH-261 already governs.
- Mint **one** new candidate only if registration proceeds: a **false-linking-risk / reality-coherence cost term** (Section 4 "cost-term principle"). This is the single aspect with no existing REE home and is the most defensible new ID. Even so, hold it as `substrate_conditional` / V4 -- there is no V3 substrate to test it on.
- Do **not** mint a fresh INV for "memory linking must be regulated" -- it is subsumed by the MECH-094/MECH-261 cluster + INV-039 (the intake already flagged this caution; the literature does not break the tie in favour of a new invariant).

## (b) Is temporal distance (days-vs-hours) supported as a first-class gating variable?

**Verdict: YES -- this is the best-supported single element of the proposal.**

Two independent, high-quality anchors converge. de Sousa 2026: silencing vmPFC for environments ~5 hours apart changed nothing (memories linked regardless), whereas the days-apart regime (~7 days) is where the vmPFC is *deliberately recruited* to adjudicate linking vs separation -- temporal distance is the variable that gates whether the controller engages at all. Cai 2016: CA1 ensemble overlap (and behavioural co-recall) is higher for contexts encoded within a day than a week apart, with a defined excitability-driven time-window mechanism. Together they give both the top-down (de Sousa) and bottom-up (Cai) sides of a temporal-distance dependence.

Two qualifications carry into any V4 design: (1) **temporal distance interacts with, and can be overridden by, contextual similarity** -- de Sousa found very similar environments still link even after 7 days. So `temporal_gap` is not an independent additive term; it modulates, and is modulated by, context_similarity. The intake's illustrative additive sketch should be revised toward an interaction. (2) The Cai mechanism is **state-conditional** (absent in aged animals), so a REE temporal term modelled on it is a tunable, state-gated weight, not a constant -- which fits routing it through the control plane (the intake's framing) rather than hard-coding it.

## (c) Is a reality-coherence / false-linking-risk cost biologically motivated?

**Verdict: YES, motivated -- but only partially specified by the evidence, and one-sided.**

de Sousa frames the entire circuit as a mechanism that "helps organize memories without allowing different events to become inappropriately linked" -- i.e. inappropriate linking is the failure the gate exists to prevent. Sahay 2011 supplies the cost's behavioural teeth: weak separation produces *overgeneralization* (distinct experiences over-linked), a costly, maladaptive, transdiagnostic phenotype, and boosting the separation effector measurably reduces it. So the claim "false linking has a real cost" is biologically grounded.

Three boundaries on that grounding:
1. The cost is shown as a failure of the separation **effector** (DG/neurogenesis), not as a control-plane cost term *priced at allocation time*. The REE novelty -- a controller that weighs `false_linking_risk` before writing -- is an extrapolation beyond what the papers demonstrate.
2. The evidence is **one-sided**: Sahay measures only the under-separation pole (over-linking). The intake correctly brackets the gate between *two* costs -- over-integration (false association) and over-separation (failure to generalize). The second cost is supported only indirectly, via the *benefit* of integration (Tse 2007). A cost term built on Sahay alone would bias the gate toward separation; the V4 design must price both poles.
3. The clinical / psychiatric mapping (psychosis = high salience + weak separation + low reality coherence) stays **speculation**. de Sousa's schizophrenia framing is explicit translation from mouse circuit work with no human data; Sahay's transdiagnostic framing is a literature trope, not a measurement. Keep this in `docs/conflicts/` territory, not a claim (consistent with `feedback_psychosis_confabulation_distinction`).

---

## Net recommendation (gated -- requires user decision; nothing executed here)

1. **No promotion now.** Candidate stays candidate; this is V4/V5 groundwork. The lit-pull was commissioned to *back the V4 design and test whether the candidate claims survive comparison* -- they survive as **enrichment + one new cost term**, not as a standalone mechanism.
2. **If/when registration proceeds (V4):** amend **MECH-261** with an allocation-decision stage (context_similarity x temporal_distance x schema_fit -> integrate/partial/separate); mint **one** new candidate for the **false-linking-risk / reality-coherence cost** as `substrate_conditional`; pair both with **MECH-147** (DG separation) and an MEC-analog indexing layer (SD-016). Do not mint a new INV.
3. **Revise the intake's illustrative algorithm** to make temporal_distance x context_similarity an *interaction*, not additive, and to price *both* over- and under-linking.
4. **V3:** unchanged -- do not build. Add a lightweight contamination/overlap check only if a V3 experiment surfaces memory contamination / false cross-run reuse / over-generalization (intake Q2; current active threads point at action-pressure / goal-stream lift, not memory contamination).
5. **Keep psychiatric mappings as speculation**, not claims.

**Evidence quadrant note:** this candidate is, by construction, **high-lit / no-exp** (`plausible_unproven` if it were registered) -- the biology is well attested but there is no REE experimental backing because the substrate is V4. That is the correct state for V4 groundwork and is precisely why this is recommendation-only.
