# SYNTHESIS -- ARC-064 Bottom-Up Rule Discovery Pathway

**Pull 2 of 4** in the ARC-062 rule-apprehension cluster scoping series.
**Date:** 2026-05-10. **Entries:** 13 papers (across hippocampal computational modelling, OFC theory + human fMRI, primate-and-rodent electrophysiology, dual-systems behavioural literature, sleep-consolidation and awake-replay).
**Source attribution:** the per-paper records cite PubMed and include DOI links; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

Pull 1 (ARC-065 behavioural-diversity-generation) settled that diversity is an upstream precondition for both rule pathways and that ARC-065 should be its own cluster, with R4 expanding the eventual MECH-312 arbitration scope from two-way to three-way (top-down rule, bottom-up rule, always-on diversity). This pull addresses the next architectural question: is the bottom-up rule discovery pathway (proposed candidate cluster ARC-064) genuinely architecturally distinct from ARC-065, and what biological substrate(s) own its operation?

The V3 design conversation that generated the cluster scoping series surfaced "rule may even start with a behavioural split and look then at rules behind it" -- bottom-up rule discovery as a separate system from top-down rule application. ARC-062 (top-down rule application via gated_policy + discriminator) is already substrate-landed; whether it has a sibling for the bottom-up direction is what Pull 2 has to settle. The five falsifiable R-questions (R1-R5) feed cluster-shape decisions: cluster registration vs absorption (R1), substrate identification (R2), online-vs-offline timing (R3), arbitration scope (R4), and the deferred MECH-315 proposal-diversity-channel question from Pull 1 (R5).

---

## R1 -- Bottom-up rule discovery: distinct cluster vs absorption into ARC-065

### Verdict: (b) PROMOTE-AS-SEPARATE-CLUSTER. Confidence 0.84.

The literature converges on a clean architectural distinction. ARC-065 generates behavioural diversity (LC-tonic noise floor + frontopolar curiosity + striatal-novelty bonus); ARC-064 extracts regularities from that diversity (hippocampal-CLS monosynaptic pathway + OFC-cognitive-map state-labels + dorsolateral-striatum action-chunking). These are different operations on different substrates with different write rules.

The load-bearing paper for the distinction is Schapiro, Turk-Browne, Botvinick & Norman 2017 ([DOI](https://doi.org/10.1098/rstb.2016.0049), PMID 27872368). Their hippocampal CLS bi-pathway model demonstrates that *within the same anatomical structure*, the brain runs two distinguishable computations: pattern-separated episode encoding (trisynaptic) and across-episode regularity extraction (monosynaptic). The architectural distinction does not require anatomically separated systems; it requires distinguishable write rules. ARC-064's bottom-up rule discovery maps onto the regularity-extraction side; the existing REE hippocampal substrate (MECH-269 anchor sets, MECH-292 ranked ghost-goal bank, MECH-293 awake ghost-goal probes) maps onto the episode-encoding side.

Wilson, Takahashi, Schoenbaum & Niv 2014 ([DOI](https://doi.org/10.1016/j.neuron.2013.11.005), PMID 24462094) supplies the OFC-as-cognitive-map substrate for hosting the extracted state-labels. Schuck et al. 2016 ([DOI](https://doi.org/10.1016/j.neuron.2016.08.019), PMID 27657452) supplies the human fMRI confirmation that OFC patterns decode current task-states with decoding accuracy correlated to behavioural performance. Niv 2019 ([DOI](https://doi.org/10.1038/s41593-019-0470-8), PMID 31551597) frames representation-learning -- the bottom-up extraction of task-state structure -- as a distinct computational stage from value-learning and policy-learning. None of these are reducible to ARC-065's diversity-generation machinery.

The single-cluster reading (absorb ARC-064 into ARC-065 as 'behavioural-discovery pathway') fails on operational grounds: diversity generation and rule extraction are different write operations on different substrates with different timing characteristics. ARC-065 is always-on (Pull 1 R4 verdict); ARC-064 has clear extraction and consolidation phases (Smith & Graybiel 2013 dual-operator + Stickgold 2013 sleep-stage-specific consolidation). The substrate-implementation experiments would need different test structures, with different signatures.

The hybrid reading (ARC-064 as a separate cluster but with cross-references to ARC-065 as upstream substrate) is the right shape -- and is the basis for the R1 verdict. ARC-064 should be PROMOTED-AS-SEPARATE-CLUSTER with explicit cross-reference to ARC-065 as the upstream precondition (without diversity, no behavioural patterns to extract rules from).

The cluster registration consequence: ARC-064 is its own architectural anchor, with sub-mechanisms covering the multi-stage pathway (extraction substrate + consolidation substrate + state-label substrate), parallel to but architecturally distinct from ARC-065.

---

## R2 -- Which biological circuit(s) extract rules from behaviour? Load-bearing vs contributory vs redundant.

### Verdict: a multi-substrate distributed pathway with THREE load-bearing components, two of which need new REE substrate work.

The literature converges on a distributed system spanning at least three substrates, each performing a distinct role in the bottom-up rule discovery pipeline:

1. **Hippocampal monosynaptic pathway (CA1 statistical-learning-arm)** -- Schapiro 2017 ([DOI](https://doi.org/10.1098/rstb.2016.0049), PMID 27872368). The monosynaptic EC->CA1 pathway extracts across-episode regularities from the trajectory record. **REE status:** PARTIAL. The trisynaptic-analog (episode-anchored, pattern-separated) is substrate-landed via MECH-269 anchor sets and MECH-292/293 ghost-goal substrates. The monosynaptic-analog (regularity-pooled) is NOT substrate-landed and is the largest gap ARC-064 must fill. **Verdict: LOAD-BEARING; primary missing substrate.**

2. **Dorsolateral striatum (action-chunking-arm)** -- Smith & Graybiel 2013 ([DOI](https://doi.org/10.1016/j.neuron.2013.05.038), PMID 23810540) and Smith & Graybiel 2016 ([DOI](https://doi.org/10.31887/DCNS.2016.18.1/ksmith), PMID 27069378). The dorsolateral striatum compresses repeated action sequences into chunked behavioural units, with characteristic action-bracketing signatures. **REE status:** NO ANALOG. There is no current REE substrate for behaviour-pattern compression / chunking. **Verdict: LOAD-BEARING; second missing substrate.**

3. **Orbitofrontal cortex (state-label-substrate)** -- Wilson 2014 ([DOI](https://doi.org/10.1016/j.neuron.2013.11.005), PMID 24462094); Schuck 2016 ([DOI](https://doi.org/10.1016/j.neuron.2016.08.019), PMID 27657452); Niv 2019 ([DOI](https://doi.org/10.1038/s41593-019-0470-8), PMID 31551597). OFC hosts the abstraction-layer state-labels that downstream policy machinery consumes. **REE status:** PARTIAL. Existing REE has substrates for E2 transition models and E3 trajectory-evaluation but no clean OFC-analog state-label substrate distinct from the existing latent-stack representations (z_world/z_self). **Verdict: LOAD-BEARING; the substrate may exist in REE under a different name or may need extension.**

4. **Hippocampal predictive map (successor-representation-arm)** -- Stachenfeld, Botvinick & Gershman 2017 ([DOI](https://doi.org/10.1038/nn.4650), PMID 28967910); Momennejad et al. 2017 ([DOI](https://doi.org/10.1038/s41562-017-0180-8), PMID 31024137). One specific implementation candidate for the rule-extraction substrate: predictive summary statistics over the trajectory record, encoded as a successor representation. **REE status:** NO direct analog. **Verdict: CONTRIBUTORY -- one of several candidate implementations the substrate-design call has to choose between.**

5. **Sleep-replay-consolidation substrate** -- Karlsson & Frank 2009 ([DOI](https://doi.org/10.1038/nn.2344), PMID 19525943); Stickgold 2013 ([DOI](https://doi.org/10.1016/j.conb.2013.04.002), PMID 23618558). Awake-quiet-period replay + sleep-stage-specific offline consolidation. **REE status:** SUBSTRATE-LANDED (MECH-272/273/274 sleep extensions, MECH-285 sleep replay sampler). **Verdict: CONTRIBUTORY but largely already covered by existing sleep-substrate cluster; ARC-064 may extend rather than duplicate.**

The cross-reference against the existing REE substrate inventory:

| Biological substrate | REE substrate currently covering it | Load-bearing? | ARC-064 sub-MECH candidate |
|---|---|---|---|
| Hippocampal monosynaptic CLS regularity extraction | NONE | Yes | MECH-316 cross-episode-regularity-extraction |
| Dorsolateral striatum action-chunking | NONE | Yes | MECH-317 behavioural-pattern-compression |
| OFC state-label cognitive map | PARTIAL (existing latent-stack representations cover some) | Yes | MECH-318 rule-state-abstraction-substrate |
| Successor-representation predictive map | NONE | Contributory (one implementation flavour) | sub-flavour of MECH-316 |
| Awake/sleep replay consolidation | MECH-272/273/274/285 substrate cluster | Contributory; mostly covered | (no new MECH; cross-reference only) |

R2 verdict drives most of the cluster-shape recommendation under R1: ARC-064 needs at least three new sub-MECH claims (MECH-316 extraction substrate, MECH-317 chunking substrate, MECH-318 state-label substrate) to cover the three load-bearing biological roles, with existing REE sleep substrates handling the consolidation arm via cross-reference.

---

## R3 -- Online vs offline timing of bottom-up rule discovery.

### Verdict: BOTH-CHANNELS-NEEDED. Confidence 0.82.

The naive online-only or offline-only readings both fail.

The online arm is anchored by Schapiro 2017's hippocampal-CLS monosynaptic pathway (continuous statistical learning during waking) and Karlsson & Frank 2009's awake-replay finding (frequent reactivation of remote-environment trajectories during awake quiet periods). Together these establish that the brain has an online channel for re-processing trajectory data and extracting regularities -- not just during sleep.

The offline arm is anchored by Stickgold 2013's sleep-consolidation review and the broader sleep-replay literature (Wilson & McNaughton 1994 was dropped from the final 13-entry set in favour of more recent papers; the substrate is already-landed in REE's existing MECH-272/273/274/285 sleep cluster). Sleep-stage-specific consolidation is real, modulator-mediated, and complementary to online extraction.

Smith & Graybiel 2013's dual-operator finding settles the question architecturally: extraction can be online and fast (striatum chunks during overtraining); stabilisation can be slow and likely benefits from offline replay (infralimbic cortex develops habit-tracking patterns over extended training). The two arms do different things in different substrates with different timecourses.

For ARC-064 cluster design this means:

- **Online extraction arm** -- MECH-316 (cross-episode-regularity-extraction, hippocampal-monosynaptic-analog) operates during waking behaviour, drawing on the trajectory record directly. It produces candidate rule-cluster representations rapidly.
- **Offline consolidation arm** -- handled by cross-reference to existing MECH-272/273/274/285 sleep substrates with a possible MECH-319 candidate ("sleep-replay-mediated-rule-stabilisation") if the existing substrates don't cover bottom-up-rule-stabilisation specifically. Cross-reference to ARC-064 should be made explicit in the existing sleep-substrate cluster docs.

The MECH-312 (dual-channel arbitration) implication is also non-trivial. The bottom-up channel (ARC-064) is producing rule-state outputs both online and offline. The arbitration mechanism has to handle the case where the online arm has produced fresh candidate rules but the offline arm has not yet stabilised them -- the rules may be high-variance and low-confidence in their early state, then become high-confidence after consolidation. Daw 2005's uncertainty-weighted arbitration (R4 below) handles this naturally; the substrate-design implication is that ARC-064 has to expose its consolidation status to the arbitration mechanism.

---

## R4 -- MECH-312 dual-channel arbitration scope: which arbitration variable dominates?

### Verdict: PRIMARILY UNCERTAINTY-WEIGHTED, with secondary practice-length component. Confidence 0.78.

The literature anchors a clear primary-variable verdict (uncertainty) with a secondary-variable nuance (practice-length / repetition-count).

Daw, Niv & Dayan 2005 ([DOI](https://doi.org/10.1038/nn1560), PMID 16286932) is the foundational normative paper: each controller's output should be weighted by the inverse of that controller's uncertainty about its prediction. Lee, Shimojo & O'Doherty 2014 ([DOI](https://doi.org/10.1016/j.neuron.2013.11.028), PMID 24507199) is the empirical confirmation: human lateral PFC tracks per-channel reliability signals AND the comparison between them, with effective connectivity to model-free valuation regions modulated accordingly. The uncertainty-weighted arbitration framework has 20 years of empirical and theoretical accumulation behind it.

But: Smith & Graybiel 2013/2016 supply the practice-length nuance. Habit takeover during overtraining is driven by repetition-count, not just uncertainty. The longer the agent does the same thing, the more the chunked / stabilised rules dominate behaviour. This adds a second arbitration variable: 'how mature is this channel's representation?' Channels with mature representations (sufficient practice) get extra weight beyond what uncertainty alone would predict.

Doll, Simon & Daw 2012 ([DOI](https://doi.org/10.1016/j.conb.2012.08.003), PMID 22959354) supplies a cautionary lesson: the binary MB-vs-MF decomposition is too clean. Signatures of both computations cohabit in the same brain regions. MECH-312 design should consider implementing arbitration as a soft mixing weight on shared substrates (effective-connectivity-modulation, per Lee 2014) rather than as a hard switch between separated channels. This aligns with Pull 1's R4 verdict that ARC-065 always-on diversity is in continuous-presence-with-triggered-dominance mode -- the same logic likely applies to ARC-062 and ARC-064.

The Pull 1 R4 verdict expanded MECH-312 from 2-way (ARC-062 vs ARC-064) to 3-way (with ARC-065 always-on as third competitor). Pull 2's R4 verdict adds a fourth dimension: the arbitration is per-channel-uncertainty + per-channel-maturity, not single-variable. The MECH-312 design needs to track both. Possible implementation: arbitration weight = (1 - uncertainty) * (maturity_score). Both arms must be near-1 for a channel to dominate.

For MECH-312 cluster registration the specific implications:

- **MECH-312** anchor: arbitration mechanism, multi-channel (3+ channels), multi-variable (uncertainty + maturity), implemented as soft mixing weight rather than hard channel switching.
- **MECH-312a** sub-MECH: per-channel uncertainty estimation (anchor: Daw 2005 + Lee 2014).
- **MECH-312b** sub-MECH: per-channel maturity / practice-length estimation (anchor: Smith & Graybiel 2013/2016).
- **MECH-312c** sub-MECH: arbitration substrate as effective-connectivity modulation (anchor: Lee 2014).

Note: this expanded scope for MECH-312 is partly already implied by Pull 1's R4 verdict; Pull 3 (the dedicated MECH-312 lit-pull) will need to test it more carefully. Pull 2's R4 verdict is provisional pending Pull 3.

---

## R5 -- MECH-315 proposal-diversity-channel: separate sub-MECH, absorbed, or ARC-064 substrate?

### Verdict: ABSORBED INTO MECH-292/293, with cross-reference to ARC-064 as semantic extension. Confidence 0.74.

Pull 1 deferred MECH-315 (hippocampal-trajectory-sampling-as-proposal-diversity, Pfeiffer & Foster 2013 anchor) to this pull on the question of whether it belongs in ARC-065 (proposal-side diversity), in MECH-292/293 (existing ghost-goal substrates), or in ARC-064 (proposal-side bottom-up rule extraction via trajectory clustering).

Karlsson & Frank 2009's finding -- frequent awake-replay of remote-environment trajectories during quiet periods -- is the closest direct anchor. The Karlsson finding is at the same level of description as Pfeiffer & Foster 2013's hippocampal forward-trajectory-sampling: hippocampal sequences are reactivated to propose candidate trajectories, drawing on stored representations of past experience. Both findings are about the same machinery.

REE's existing MECH-292 (ranked ghost-goal bank) and MECH-293 (awake ghost-goal probes) are direct substrates for this proposal-mechanism. They handle the awake-quiet-period proposal-of-candidates role that Karlsson 2009 anchors. MECH-315 was originally proposed as a separate sub-MECH because Pull 1 was unsure whether the trajectory-sampling machinery should be tagged for diversity-generation or for rule-extraction or for a third role.

The R5 verdict: MECH-315 is ABSORBED into the existing MECH-292/293 substrate cluster. No new sub-MECH is needed under either ARC-064 or ARC-065. Instead, the existing MECH-292/293 docs should be updated with explicit cross-references: their proposal-mechanism role connects upstream to ARC-065 (when the proposed trajectories diversify behaviour) AND upstream to ARC-064 (when the proposed trajectories provide raw material for bottom-up rule extraction). The same substrate, dual-purposed, with the dual purpose acknowledged at the cluster-cross-reference level rather than via a new MECH.

This is a close call -- if the substrate-design call later determines that MECH-292/293 cannot accommodate both roles cleanly (e.g., the proposal-mechanism for diversity uses different parameters than the proposal-mechanism for rule-extraction), MECH-315 should be re-promoted as a separate sub-MECH. For now, ABSORBED with cross-references is the right call. Confidence 0.74 reflects the close-call nature.

---

## What this pull does NOT settle

Items deferred to subsequent pulls or future sessions:

1. **Pfeiffer & Foster 2013 anchor specifically.** The Pull 1 R5 deferred-question was partially resolved by Karlsson 2009 in this pull, but Pfeiffer & Foster 2013 itself was not directly retrieved or summarised. If the substrate-design call later requires the specific Pfeiffer & Foster signature (forward-trajectory-sampling toward goals before action selection), a follow-up retrieval is needed.

2. **The specific implementation flavour for MECH-316 (bottom-up extraction substrate).** Niv 2019 lists multiple candidates -- Bayesian latent-cause inference, attention-modulated RL, structure-learning, successor-representation. The Stachenfeld 2017 + Momennejad 2017 SR-flavour entries provide one fully-anchored candidate, but the substrate-design call has to commit to one. This is implementation work for the V3-EXQ design phase, not a literature-resolvable question.

3. **The relationship between MECH-318 (rule-state-abstraction-substrate) and existing REE latent-stack representations.** REE's z_world / z_self / z_alpha latent representations partially cover the OFC-cognitive-map role but are not deliberately designed for rule-state abstraction. Whether MECH-318 needs a NEW substrate or can be implemented as a structured readout of existing latent-stack representations is a substrate-design call, not literature-decidable.

4. **Pull 3 (MECH-312 arbitration) is partially gated on this pull's R4 verdict.** Pull 2's R4 verdict (uncertainty-weighted + practice-length, 3+ channels, soft-mixing-weight) is provisional and should be tested with the dedicated MECH-312 lit-pull. The arbitration-literature anchors (Daw 2005, Lee 2014, Doll 2012, Smith & Graybiel 2013/2016) appear in both Pull 2 and Pull 3 sets; that is appropriate because they are foundational to both ARC-064 and MECH-312.

5. **Pull 4 alternative-framing question.** Whether option-policies / hierarchical-RL / schemas-without-explicit-rule-level-abstraction would be a cleaner architecture than ARC-062 + ARC-064 + ARC-065 + MECH-312 combined. Pull 2 has not addressed this; it presupposes rules exist as a meaningful level of description. Pull 4 should test that presupposition with the option-discovery-from-behavioural-segmentation literature (Ribas-Fernandes 2011, Botvinick 2009, Bacon et al. 2017 option-critic, etc.).

6. **The rule-vs-context-vs-state-vs-schema terminology question.** The literature uses 'task state' (Wilson 2014, Schuck 2016, Niv 2019), 'cognitive map' (multiple), 'rule' (computational-RL tradition), 'schema' (Bartlett-tradition memory literature), 'context' (some classical-conditioning work), 'option' (hierarchical RL). These are not interchangeable. ARC-064's specific commitment to 'rule' as the abstraction-level it operates at should be tested against the alternative naming choices in Pull 4 and in subsequent V3 design discussions.

---

## Recommended cluster shape (PROMOTE-AS-SEPARATE-CLUSTER)

Following from R1-R5, the recommended ARC-064 cluster shape:

- **ARC-064** anchor: bottom-up rule discovery pathway. Architectural commitment that rules can be extracted from the trajectory record without external instruction, via a multi-stage pathway distinct from ARC-062 top-down rule application and ARC-065 behavioural diversity generation. Cross-reference: ARC-065 as upstream precondition; ARC-062 as parallel architecture; MECH-312 as downstream arbitration.
- **MECH-316** cross-episode-regularity-extraction substrate (hippocampal-monosynaptic-CLS-analog; Schapiro 2017 anchor). Online during waking, produces candidate rule-cluster representations from the trajectory record.
- **MECH-317** behavioural-pattern-compression / action-chunking substrate (dorsolateral-striatum-analog; Smith & Graybiel 2013 anchor). Compresses repeated patterns into reusable chunks, with bracketing signatures.
- **MECH-318** rule-state-abstraction-substrate (OFC-cognitive-map-analog; Wilson 2014 + Schuck 2016 + Niv 2019 anchors). Hosts extracted rule-state labels for downstream policy machinery to consume.
- **(MECH-319 deferred)** sleep-replay-mediated-rule-stabilisation substrate. Cross-referenced to existing MECH-272/273/274/285 sleep substrates; only register as new MECH if existing substrates can't accommodate bottom-up-rule-stabilisation specifically.
- **Q-XXX-1** (open question) "Is MECH-316 best implemented as successor-representation, Bayesian-latent-cause, or structure-learning machinery? Falsifiable with discriminative-task contrasts at substrate-validation time."
- **Q-XXX-2** (open question) "Is MECH-318 a new substrate or a structured readout of existing latent-stack representations? Falsifiable by testing whether existing latent-stack representations support rule-state-decoding under partial observability conditions."
- **Q-XXX-3** (open question) "Does ARC-064's bottom-up extraction work without ARC-065's diversity precondition? Falsifiable: monomodal-baseline arm should produce empty rule-cluster output."

MECH-312 expansion implied by R4: register MECH-312a/b/c sub-MECHs at the next governance pass to capture the multi-variable arbitration scope. Defer this expansion to Pull 3 to avoid over-committing on the basis of Pull 2 alone.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Schapiro et al. 2017 | [10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049) | R1, R2, R3 | supports | 0.86 |
| Wilson, Takahashi, Schoenbaum & Niv 2014 | [10.1016/j.neuron.2013.11.005](https://doi.org/10.1016/j.neuron.2013.11.005) | R2, R3 | supports | 0.84 |
| Schuck et al. 2016 | [10.1016/j.neuron.2016.08.019](https://doi.org/10.1016/j.neuron.2016.08.019) | R2 | supports | 0.78 |
| Niv 2019 | [10.1038/s41593-019-0470-8](https://doi.org/10.1038/s41593-019-0470-8) | R1, R2 | supports | 0.82 |
| Stachenfeld, Botvinick & Gershman 2017 | [10.1038/nn.4650](https://doi.org/10.1038/nn.4650) | R2 | supports | 0.78 |
| Momennejad et al. 2017 | [10.1038/s41562-017-0180-8](https://doi.org/10.1038/s41562-017-0180-8) | R2, R4 | supports | 0.80 |
| Daw, Niv & Dayan 2005 | [10.1038/nn1560](https://doi.org/10.1038/nn1560) | R4 | supports | 0.84 |
| Lee, Shimojo & O'Doherty 2014 | [10.1016/j.neuron.2013.11.028](https://doi.org/10.1016/j.neuron.2013.11.028) | R4 | supports | 0.80 |
| Doll, Simon & Daw 2012 | [10.1016/j.conb.2012.08.003](https://doi.org/10.1016/j.conb.2012.08.003) | R4 | mixed | 0.66 |
| Smith & Graybiel 2013 | [10.1016/j.neuron.2013.05.038](https://doi.org/10.1016/j.neuron.2013.05.038) | R2, R3, R4 | supports | 0.82 |
| Smith & Graybiel 2016 | [10.31887/DCNS.2016.18.1/ksmith](https://doi.org/10.31887/DCNS.2016.18.1/ksmith) | R2, R4 | supports | 0.74 |
| Karlsson & Frank 2009 | [10.1038/nn.2344](https://doi.org/10.1038/nn.2344) | R3, R5 | supports | 0.78 |
| Stickgold 2013 | [10.1016/j.conb.2013.04.002](https://doi.org/10.1016/j.conb.2013.04.002) | R3 | supports | 0.72 |

**Aggregate ARC-064 lit_conf** (post-indexer): expected to land in the 0.75-0.80 range, supports-direction, 13-entry cohort spanning hippocampal computational modelling (Schapiro, Stachenfeld), OFC theory + human fMRI (Wilson, Schuck, Niv), behavioural-RL theory (Daw, Lee, Doll, Momennejad), striatal electrophysiology (Smith & Graybiel x2), and replay/consolidation (Karlsson, Stickgold). Eight distinct biological systems represented (hippocampal CA1, hippocampal CA3, dentate gyrus, dorsolateral striatum, OFC, lateral PFC + frontopolar, dopamine-VTA system, sleep-modulator system). Two computational frameworks anchored (CLS-tradition, SR-tradition).

According to PubMed, all PubMed-indexed entries in this synthesis are sourced as cited above; DOIs are linked per-entry.
