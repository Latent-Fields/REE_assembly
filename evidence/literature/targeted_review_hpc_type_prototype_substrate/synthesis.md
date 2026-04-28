# Hippocampal Type-Prototype Substrate vs Anchor Substrate — Synthesis

Lit-pull commissioned 2026-04-28 to settle three linked architectural questions raised in conversation (thought captured in `docs/thoughts/2026-04-28_action_object_type_abstraction.md`):

1. Are HPC concept-cell / categorical-prototype representations functionally distinct from anchor / place-cell representations?
2. Is sleep necessary and sufficient for type-prototype extraction, or is waking learning enough?
3. Is the action-policy library HPC-resident or distributed across BG/SMA/PFC?

Five entries pulled, all PubMed-indexed.

## Entries

According to PubMed:

| Paper | Finding | Sub-question |
|---|---|---|
| Quiroga et al. 2005 *Nature* [DOI 10.1038/nature03687](https://doi.org/10.1038/nature03687) | Concept cells in human MTL: instance-invariant abstract identity code, sparse, multimodal | (1) — type representations exist |
| Schapiro et al. 2017 *Phil Trans R Soc B* [DOI 10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049) | Within-HPC dual pathways: trisynaptic for episodes, monosynaptic EC→CA1 for statistical regularities | (1) — substrates are anatomically distinct within HPC |
| Schapiro et al. 2016 *Hippocampus* [DOI 10.1002/hipo.22523](https://doi.org/10.1002/hipo.22523) | HPC learns temporal community structure during waking exposure (no sleep needed) | (2) — waking learning sufficient for some abstraction |
| Constantinescu, O'Reilly & Behrens 2016 *Science* [DOI 10.1126/science.aaf0941](https://doi.org/10.1126/science.aaf0941) | Conceptual 2D space encoded by hexagonal gridlike code in EC + vmPFC (same machinery as spatial nav) | (1) — unified cognitive-map machinery across spatial and conceptual domains |
| Hennies et al. 2017 *Sleep* [DOI 10.1093/sleep/zsx102](https://doi.org/10.1093/sleep/zsx102) | Sleep enhances statistical abstraction (control), but cued reactivation during SWS *abolishes* the sleep benefit | (2) — sleep does extract abstraction, but the operator is content-specific and delicate |

Mean confidence 0.81 (range 0.74-0.88).

## Primary verdicts

### (a) Type-prototype substrate — biologically distinct from anchor substrate?

**Yes, with nuance.** Two converging readings:

- **Within HPC** (Schapiro 2017 *Phil Trans R Soc B*): the trisynaptic (DG → CA3 → CA1) and monosynaptic (EC → CA1 directly) pathways implement complementary learning systems *within hippocampus*. Trisynaptic = pattern-separated episodic instances. Monosynaptic = statistical regularities / community structure. So yes, type and instance representations live on architecturally separate pathways.

- **Beyond HPC** (Constantinescu 2016, Quiroga 2005): the cognitive-map / type-substrate machinery is more accurately described as primarily entorhinal-cortex and frontomedial-cortex resident, with HPC providing instance binding. Concept cells are spread across MTL (HPC + EC + parahippocampal + amygdala). The "type substrate" is not strictly hippocampal even though it is functionally adjacent.

The architectural inference for REE: the type-prototype substrate is biologically distinct from the anchor substrate, but the distinctness is implemented as **shared cognitive-map machinery with different input projections** rather than as a fully parallel codebook. Constantinescu 2016 is the load-bearing evidence here — the same grid-cell architecture handles spatial and conceptual relations, just with different inputs.

### (b) Sleep necessary and sufficient for type extraction?

**Sleep is helpful but not strictly necessary.** Three converging readings:

- Schapiro 2016 shows community-structure abstraction develops during waking exposure with no sleep involved. Waking learning is *sufficient* for at least one form of compositional abstraction.

- Hennies 2017's control group shows sleep does enhance abstraction beyond the waking baseline — so sleep contributes additively. But the SWS-replay group shows the sleep operator is delicate: cued reactivation during SWS *abolishes* the abstraction benefit. The operator works by compositional recombination across instances, not by reinforcing specific instances.

- The Schapiro 2017 modelling paper does not address sleep directly, but the dual-pathway architecture it describes is amenable to both waking and sleep-driven learning.

Architectural inference for REE: do not gate the prototype-extraction operator to sleep only. Implement an online (waking) update step that is enhanced — but not strictly required — by a sleep recombination pass. This is consistent with what MECH-285 already does in V3 (priority-weighted anchor sampling during sleep, where the priority gives compositional structure rather than uniform replay).

### (c) Action-policy library HPC-resident?

**Not directly resolved by these five entries.** The pull was scoped to type-prototype representations and the literature returned addresses object/conceptual prototypes but not action-sequence templates or option libraries. The architectural question Daniel raised about action primitives — are they HPC-resident or BG/SMA-resident? — would need its own follow-up pull anchored on different literature (Botvinick et al. 2009 *Cognition*; Ribas-Fernandes et al. 2011 *Neuron*; Cushman 2013 *Cognition*; Sutton-Precup-Singh 1999 *AI Journal*; recent work by Eichenbaum, Wikenheiser on hippocampal sequence templates beyond spatial domain).

The general pattern from the literature I do know is that **action primitives are distributed**: motor primitives in spinal cord and motor cortex, sequence templates in pre-SMA, abstract options / hierarchical RL in PFC + BG, with HPC contributing temporal-sequence binding. So a hippocampal-resident action-policy library is biologically not the dominant reading. **Flagged for a separate lit-pull if Daniel wants this resolved formally.**

## Architectural recommendation for REE

### Primary recommendation: extend, do not duplicate

Rather than adding a fully separate type-prototype substrate (the original SD-N hypothesis), the parsimonious architectural extension is:

1. **A new input projection onto the existing AnchorSet machinery** that produces *type-keyed* anchors rather than *location-keyed* anchors. Anchors written under this projection share the same dual-trace persistence, the same V_s gating, the same boundary-event triggers — but their `z_world` snapshot is replaced by a category-relevant feature vector (e.g. extracted from `z_resource` + valence vector + stream_mixture signature). This is the Constantinescu 2016 reading: same machinery, different input.

2. **An explicit prototype-readout operator** (provisional MECH-N) that runs *both during waking and during sleep*, computing a softmax-attention-style match between current `LatentState` and the type-keyed anchor pool. The output is a small set of best-matched type-keys plus their confidences. This is the verisimilitude-on-types operation Daniel described. Its waking form provides moment-to-moment type recognition; its sleep form (via MECH-285's priority-weighted replay) consolidates and refines the type-anchor pool.

3. **A type-V_s extension to MECH-269** so the proposer / E3 can gate stream contributions by category-V_s as well as per-stream V_s. This is mechanically a small extension to the existing per_stream_vs / per_region_vs machinery — adding a per-type V_s dimension keyed on the matched type-key.

### Secondary recommendation: respect the dual-pathway constraint

If REE later wants to honour the Schapiro 2017 dual-pathway result more strictly, the architectural extension is to **route type-keyed anchor writes through a different update rule** than instance-keyed writes — equivalent to the monosynaptic-vs-trisynaptic distinction. The instance-keyed AnchorSet write rule (currently in MECH-269 Phase 2 ii) is pattern-separating: each new instance gets its own anchor. The type-keyed write rule would be averaging / EMA: instances of the same type update a shared prototype rather than spawning fresh anchors. This is straightforward to implement once the new input projection is in place.

### Architectural constraint from Hennies 2017

Whatever sleep operator REE adds for prototype extraction, **do not implement it as uniform replay over anchors**. The biological evidence is clear: naive content-specific replay disrupts abstraction. The MECH-285 priority-weighted sampling is roughly the right shape; the new operator should respect that compositional-recombination structure rather than focusing on specific instances.

## What's NOT settled and worth flagging

- **The action-policy library question remains open.** Action primitives are biologically distributed (BG / SMA / PFC) and a hippocampal-resident option library is not the dominant biological reading. If Daniel wants this resolved formally, a separate lit-pull anchored on Botvinick 2009 / Ribas-Fernandes 2011 / Cushman 2013 / Sutton-Precup-Singh 1999 / hierarchical-RL literature would be needed.

- **EC-analogue substrate.** The Constantinescu 2016 result places the cognitive-map machinery primarily in EC, not HPC. REE has no EC-analogue substrate. The proposed input projection onto AnchorSet is a coarse functional substitute; an explicit EC-analogue node would be a more biologically faithful extension. V4 scope.

- **Discrete-vs-continuous transfer.** All the reviewed papers study continuous conceptual spaces or temporal-sequence regularities. REE's category prototypes ("hazard-type", "resource-type") are discrete categories. The transfer is plausible but not directly demonstrated. A V3-internal experiment showing that a type-keyed anchor projection produces meaningful category clustering would be the parsimonious validation step.

- **The substrate-vs-operator question.** Schapiro 2017 says distinct *anatomical pathways*; Constantinescu 2016 says shared *cognitive-map machinery*. These are not strictly contradictory (one machinery output, two learning pathways feeding it), but they suggest different architectural starting points. This lit-pull recommends the Constantinescu reading as the parsimonious starting point for V3 implementation; the Schapiro 2017 reading is available as the V4 refinement if behavioural evidence demands it.

## Net aggregate

Mean confidence 0.81 across five entries. Verdict: REE should add type-keyed projections and a prototype-readout operator, not a fully separate codebook substrate. Sleep remains relevant but is not the gating step — waking learning suffices for the basic abstraction; sleep refines and consolidates. The action-policy library is a separate question and remains open pending a follow-up lit-pull. None of these recommendations is V3-blocking; they are V4 candidates unless behavioural evidence in V3 (e.g. EXQ-495 V3-full-completion-gate failure modes) surfaces a need.
