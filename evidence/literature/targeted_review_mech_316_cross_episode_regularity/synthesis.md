# SYNTHESIS -- MECH-316 cross-episode regularity extraction (ARC-064 Pull-2 follow-on)

**Pull 2 follow-on** to the ARC-064 bottom-up rule discovery cluster lit-pull (2026-05-10).
**Date:** 2026-05-11. **Entries:** 5 papers (Bayesian latent-cause framework + operationalisation; hippocampal empirical anchor; attention-modulated RL; structure-learning boundary case).
**Source attribution:** per-paper records cite PubMed and include DOI links; this synthesis aggregates and adjudicates.

---

## Why this pull was commissioned

Pull 1 (ARC-064 bottom-up rule discovery, 2026-05-10) settled cluster-shape (PROMOTE-AS-SEPARATE-CLUSTER) and identified MECH-316 as the load-bearing missing substrate for the cross-episode regularity-extraction role. Pull 1's R2 verdict identified four candidate implementation flavours but deferred the choice: Bayesian latent-cause inference, successor-representation, attention-modulated RL, and structure-learning. The ARC-064 synthesis (line 132) explicitly named this as a deferral: "the substrate-design call has to commit to one. This is implementation work for the V3-EXQ design phase, not a literature-resolvable question." Pull 2 returns to the literature with a sharper question: given that the literature is the right place to adjudicate which inference family the substrate should belong to, what does the literature say?

The Q-044 lit-pull synthesis (2026-05-11) provided the timing reason for running this pull now: the SD-054 reef substrate is probably insufficient for the Q-044 three-arm ablation without enrichment, and the structural-relatedness between Q-044 (MECH-314 sub-flavour independence) and the MECH-316/317/318 cluster suggests that whatever substrate-enrichment is needed for one will inform the others. Settling the implementation-flavour choice for MECH-316 now means the substrate-design pass can proceed without waiting on Q-044 to land its experimental work first.

---

## R1 -- Which implementation flavour for MECH-316: latent-cause, SR, attention-modulated, or structure-learning?

### Verdict: HYBRID -- Bayesian latent-cause inference as the load-bearing flavour, with attention-modulated RL as a lightweight implementation backbone. Confidence 0.74.

The literature does not cleanly select one flavour. Each of the four has real anchors and real failure modes. But the cluster of evidence weighting points toward a hybrid implementation.

The case for Bayesian latent-cause inference (Gershman & Niv 2010, Gershman 2017): if MECH-316 has to support qualitative context-switching at rule-regime transitions -- the snap-back, summation, and renewal signatures that the latent-cause literature anchors -- then the substrate must maintain a posterior over hidden causal variables. Pure SR cannot do this; it predicts smooth interpolation. Attention-modulated RL cannot do this on its own; it predicts gradual learning of which dimensions matter, not qualitative regime-switching. The case is strongest when the V3 substrate is intended to operate in genuinely multi-regime environments where the optimal policy is non-stationary by design (multi-rule-context substrate for MECH-318's falsifier; Q-044's three-arm curiosity ablation; the ARC-064 multi-context generalisation the Pull-1 framework anchors).

The case for attention-modulated RL (Niv et al. 2015): the substrate-implementation cost is lower than either latent-cause or structure-learning. Attention-modulated routing over the latent stack (z_world / z_self / z_alpha / region-anchor labels) is implementable with the existing REE machinery -- learned gating heads, much like SD-033a LateralPFCAnalog's bias compute or the ARC-062 GatedPolicy discriminator. If the regularity-extraction demand is modest, this is the parsimonious choice. The case is strongest when V3 stays in the SD-054-single-context or modestly-extended regime.

The case against pure SR: Pull 1 already anchored the SR flavour (Stachenfeld 2017, Momennejad 2017). The current pull does not weaken those entries; the SR flavour remains viable AS PART OF a hybrid. But the SR flavour alone is insufficient when qualitative regime-switching is required, which is the load-bearing capability Pull 1's R3 verdict already identified ARC-064 as having to support.

The case against the strong structure-learning reading (Kemp & Tenenbaum 2008): biologically overdetermined. The framework is a normative account of what structure-learning IS computationally; the empirical evidence that brains maintain explicit hypothesis spaces over discrete structural forms is thin. The strong reading is not what MECH-316 should aim for in V3.

The hybrid recommendation reads MECH-316 as:
- **Attention-modulated routing** at the input layer: select which latent-stack components are predictive for the current regime (Niv et al. 2015 as algorithmic anchor; ARC-062 GatedPolicy discriminator + SD-033a rule_state buffer as implementation backbone if Phase 3 wiring lands).
- **Latent-cause inference** at the output layer: maintain a posterior over candidate rule-contexts that the input-routing is consistent with, allowing qualitative regime-switching when evidence accumulates (Gershman & Niv 2010 + Gershman 2017 as anchor).
- **Successor-representation** as an optional auxiliary readout: maintain a discounted-state-occupancy summary under the current posterior, useful for downstream policy machinery (Stachenfeld 2017 anchor, already in Pull 1; not a separate substrate, a readout).

The structural form of MECH-316 ends up being something like: 'maintain a posterior over rule-contexts, attentionally select latent-stack components predictive of the inferred context, and expose an SR-style readout to downstream policy machinery'. This is more involved than any single-flavour reading but more parsimonious than the strong structure-learning reading.

Confidence 0.74 because the hybrid is a reasonable synthesis but the substrate-design pass might reasonably commit to a simpler attention-modulated-only implementation as a first pass and only add the latent-cause posterior if behavioural failures motivate it. The hybrid is the right architectural commitment; the implementation can be staged.

---

## R2 -- Does MECH-316 need an explicit inference step over hidden variables, or does a non-inferential substrate suffice?

### Verdict: YES, an explicit inference step is needed if the substrate has to support qualitative regime-switching. Confidence 0.78.

This is the question Pull 1 deferred most explicitly: 'whether MECH-316 needs a NEW substrate or can be implemented as a structured readout of existing latent-stack representations is a substrate-design call, not literature-decidable.' The current pull does not flat-out resolve it -- substrate-design calls genuinely cannot be made from literature alone -- but it does sharpen what the trade-off is.

The argument for explicit inference: latent-cause inference (Gershman & Niv 2010, Gershman 2017) predicts qualitatively-different behavioural signatures from attention-modulated RL or SR. Specifically, snap-back behaviour at context-reappearance, summation-vs-overshadowing dissociations, and renewal effects. Davachi & DuBrow 2015's empirical anchor reinforces this: hippocampal substrate signatures are prediction-error-modulated and context-segmented, not smooth-interpolation-style. If REE's substrate has to reproduce any of these signatures behaviourally, an explicit inference step is necessary.

The argument against: if REE's substrate is only required to support quantitatively-different learning rates across regimes (faster in familiar contexts, slower in novel ones), an attention-modulated substrate is sufficient. The structure-learning reading (Kemp & Tenenbaum 2008) is the strong-version of explicit inference and is probably overkill. Pure SR is too weak. The right level of explicit inference is probably Gershman-style latent-cause inference, not Tenenbaum-style structure-form discovery.

The substrate-design recommendation: stage the implementation. Start with attention-modulated routing (lowest cost, fastest to validate); add a latent-cause posterior only if behavioural validation shows that the attention-only substrate fails to reproduce qualitative regime-switching signatures. This staging is consistent with the MECH-318 absorption-check verdict (the within-V3 portion of MECH-318 is already covered by SD-033a + ARC-062 + Phase 3 wiring; what remains is W2 multi-task-training and W5 cross-episode continuity).

---

## R3 -- Empirical-signature anchor for MECH-316 validation: which behavioural / fMRI signatures should the substrate reproduce?

### Verdict: Davachi-DuBrow 2015 supplies the canonical anchor list. Confidence 0.76.

Davachi & DuBrow 2015 specifies three empirical signatures that a hippocampal-style cross-episode regularity-extraction substrate should reproduce: (1) prediction-error-modulated event-boundary effects on temporal-order memory, (2) context-dependent binding of co-occurring items, (3) statistical-learning of co-occurrence beyond episodic memorisation.

For REE's MECH-316 validation, the corresponding behavioural signatures on a trajectory-record substrate are:
- **Boundary signatures**: V_s-drop or prediction-error events should disrupt cross-episode regularity-extraction across the boundary specifically -- not generic regularity-extraction failures. (MECH-269 anchor-boundary signatures already provide an REE analog for the boundary mechanism; MECH-316 needs to be sensitive to those boundaries when extracting cross-episode statistics.)
- **Context signatures**: items / state-transitions encountered in different anchor-contexts should be encoded into different regularity-clusters, even when surface features match. (The candidate substrate should be context-segmenting, not context-collapsing.)
- **Statistical-learning signatures**: co-occurring state-transitions should acquire shared representations through statistical accumulation, distinct from individual-episode encoding. (The candidate substrate should support cross-episode generalisation that the existing MECH-269 anchor-set substrate -- pattern-separated by design -- does not support.)

These three signatures are falsifiable on a trajectory-record substrate, but the validation requires an environment richer than SD-054 single-context. The multi-rule-context substrate the MECH-318 absorption-check already named -- SD-054 extended with two reef configurations requiring different foraging strategies, or analog -- is the minimum substrate for MECH-316 validation as well.

---

## R4 -- What experimental design distinguishes the four implementation flavours on REE's behavioural-trajectory substrate?

### Verdict: A multi-rule-context substrate with independently-manipulable dimensionality + regime-frequency + transition-statistics is the minimum. Confidence 0.70.

The four implementation flavours make different falsifiable predictions:

| Flavour | Signature on multi-rule-context substrate |
|---|---|
| Bayesian latent-cause inference | Qualitative snap-back at context-reappearance; summation-vs-overshadowing dissociation |
| Successor-representation | Smooth interpolation across regimes; no snap-back |
| Attention-modulated RL | Slow-learning slope proportional to irrelevant-dimensions count; no qualitative regime-switching signature |
| Strong structure-learning | Discrete form-discovery at regime transitions; explicit hypothesis-space exploration signature |

Distinguishing these requires the substrate to support independent manipulation of:
- **Number of rule-regimes** (1 / 2 / 3+ context conditions, with context-cue independently identifiable to the agent)
- **Dimensionality** (number of latent-state components that matter for the current regime)
- **Regime-frequency** (how often the agent encounters each regime; mostly-one-rule vs evenly-distributed vs novel-rule-prepended)
- **Transition-statistics** (how the regime is signalled; sharp transitions vs gradual ones; cued transitions vs non-cued)

SD-054 single-context does not support any of these manipulations. The substrate-enrichment work the Q-044 synthesis already named is the same enrichment MECH-316 validation needs. The substrate-design pass should treat this as a single combined deliverable, not three separate substrates.

A concrete experimental design that would falsifiably distinguish the four flavours: multi-rule-context substrate with 3 regimes, 4 latent dimensions each (2 relevant + 2 irrelevant per regime; relevance-set differs per regime), regime-frequency 1:1:1 with sharp cued transitions, and a behavioural probe measuring (a) policy correctness at regime-onset (latent-cause prediction: should approach steady-state within 5 trials after regime-recognition; SR prediction: should approach steady-state over many trials regardless), (b) regime-cue dependence (latent-cause prediction: snap-back at cue-reappearance; SR prediction: no snap-back), (c) dimensionality scaling (attention-modulated prediction: learning slope proportional to irrelevant-dimension count; latent-cause prediction: less dependent on irrelevant dimensions if the latent space is correctly inferred).

This experimental design is not currently in V3's substrate set and would need to be commissioned as part of the substrate-enrichment work R4 of this synthesis and R4 of the Q-044 synthesis both flagged.

---

## What this pull does NOT settle

1. **The substrate-design choice itself.** The hybrid recommendation under R1 is a literature-informed architectural commitment, not a substrate specification. The V3 substrate-design pass has to decide HOW to implement the hybrid -- specifically, where in the existing latent stack the latent-cause posterior lives, how the attention-modulated routing relates to the existing SD-033a / ARC-062 cluster, and whether the SR readout is implemented as an explicit auxiliary head or as a derivable quantity from the inferred posterior. None of these are literature-decidable.

2. **The relationship between MECH-316 and the existing MECH-269 anchor-set substrate.** MECH-269 is pattern-separated by design (region-anchor labels are discrete and non-overlapping). MECH-316 needs to operate on the same trajectory-record but extract cross-episode regularities rather than episode-specific anchors. Whether MECH-316 reads off the same anchor-set substrate or runs in parallel is a substrate-design call.

3. **The Q-044 sub-flavour decoupling.** Q-044's R4 flagged that SD-054 reef substrate is probably insufficient for the MECH-314 three-arm ablation without enrichment. MECH-316 validation will need the same enrichment. Whether the enrichments are the same architectural commitment or two parallel ones is a substrate-design call.

4. **The MECH-318 absorption boundary.** The MECH-318 absorption check (2026-05-10) settled that the within-V3 portion of MECH-318 absorbs into SD-033a + ARC-062. Pull 2 of MECH-318 (this round) confirms that the W2 multi-task-training and W5 cross-episode continuity gaps remain. The relationship between MECH-316's latent-cause posterior and MECH-318's rule-state buffer is the same relationship in different framings: a hidden-variable posterior over rule-context. Whether they should be unified into a single substrate or kept as separate-but-coupled is a substrate-design call.

---

## Per-paper summary index

| Entry | DOI | Implementation flavour | Direction | Confidence |
|---|---|---|---|---|
| Gershman & Niv 2010 | [10.1016/j.conb.2010.02.008](https://doi.org/10.1016/j.conb.2010.02.008) | Bayesian latent-cause (framework anchor) | supports | 0.80 |
| Gershman 2017 | [10.3758/s13423-016-1110-x](https://doi.org/10.3758/s13423-016-1110-x) | Bayesian latent-cause (operationalisation) | supports | 0.76 |
| Davachi & DuBrow 2015 | [10.1016/j.tics.2014.12.004](https://doi.org/10.1016/j.tics.2014.12.004) | empirical substrate anchor (hippocampal) | supports | 0.74 |
| Niv et al. 2015 | [10.1523/JNEUROSCI.2978-14.2015](https://doi.org/10.1523/JNEUROSCI.2978-14.2015) | attention-modulated RL (foundational) | supports | 0.82 |
| Kemp & Tenenbaum 2008 | [10.1073/pnas.0802631105](https://doi.org/10.1073/pnas.0802631105) | structure-learning (boundary case) | mixed | 0.62 |

**Aggregate MECH-316 lit_conf** (post-indexer): expected to land in the 0.72-0.78 range, supports-direction-dominant, 5-entry cohort spanning the four candidate implementation flavours. The hybrid R1 recommendation (Bayesian latent-cause + attention-modulated as combined target; SR as readout; structure-learning as boundary case) is the literature-informed input to the substrate-design pass that follows.

According to PubMed, all PubMed-indexed entries in this synthesis are sourced as cited above; DOIs are linked per-entry.
