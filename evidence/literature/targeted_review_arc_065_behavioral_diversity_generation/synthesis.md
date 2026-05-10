# SYNTHESIS — ARC-065 Behavioral Diversity Generation Pathway

**Pull 1 of 4** in the ARC-062 rule-apprehension cluster scoping series.
**Date:** 2026-05-10. **Entries:** 9 papers (across human fMRI, primate single-unit, computational theory, behavioural-modelling, foundational reviews).
**Source attribution:** the per-paper records cite PubMed and include DOI links; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

Monomodal-policy collapse is the recurring failure mode in REE V3. EXQ-433/433a/433b/470/523/523a/523b were all reclassified `non_contributory` because monomodal policy could not generate balanced agent-vs-env event distributions for the SD-029 C2/C3 measurement gate. EXQ-543 (ARC-062 Phase 2a monomodal-collapse falsifier) was reclassified `non_contributory` 2026-05-10 for the same family of reasons (gated_policy substrate at-init produced inert gating; one of three seeds was byte-identical to baseline). The proposed ARC-064 cluster (bottom-up rule discovery via behavioural clustering) presupposes behavioural diversity *exists* in the trajectory record — without it, k-means returns one tight cluster, not two distinguishable groups, and the entire bottom-up pathway is empty. Analogously, ARC-062 (top-down rule application) presupposes *context* to detect; if the agent's behaviour is monomodal, the discriminator has nothing to discriminate.

The ARC-065 candidate cluster names the missing precondition: a behavioural-diversity-generation pathway that operates *upstream* of any rule mechanism. This pull was commissioned to settle, with literature grounding, four falsifiable questions about that pathway before locking the cluster claims.

---

## R1 — Structured curiosity necessary, noise sufficient, or both?

### Verdict: (c) BOTH-CHANNELS-NEEDED. Confidence 0.85.

Wilson, Geana, White, Ludvig & Cohen 2014 ([DOI](https://doi.org/10.1037/a0038199), PMID 25347535) is the load-bearing paper. The Horizon task decomposes human exploration into two computationally separable parameters — directed information-seeking and softmax decision noise — and shows that BOTH increase with horizon length. Either-channel-only models cannot capture the full pattern. Faisal, Selen & Wolpert 2008 ([DOI](https://doi.org/10.1038/nrn2258), PMID 18319728) grounds the noise side biologically: behavioural variability has an irreducible substrate-level noise floor that any biologically-realistic agent must instantiate. Friston, Rigoli, Ognibene, Mathys, Fitzgerald & Pezzulo 2015 ([DOI](https://doi.org/10.1080/17588928.2015.1020053), PMID 25689102) grounds the structured side computationally: epistemic value (information gain) and stochastic decision noise (precision of policy beliefs) are complementary terms in the same expected-free-energy objective, not competing substrates.

The single-channel readings fail on different grounds:

- **Noise-only fails empirically.** Wilson 2014 explicitly tests and rejects pure-noise models. The horizon-dependent shift in directed information-seeking is not capturable by tuning a softmax temperature.
- **Curiosity-only fails biologically.** Faisal 2008 shows neural systems *are* noisy from molecules upward; there is no biologically realistic agent with zero policy noise. Even if the curiosity channel did all the exploration work, the noise channel would still be present.

The R1 verdict has direct cluster-registration consequences: ARC-065 needs both MECH-313 (stochastic-noise-floor) and MECH-314 (structured-curiosity-bonus) as separate sub-mechanisms. Neither can be omitted. The relative-weight calibration is left as an open question (Q-XXX below).

---

## R2 — Which biological circuit(s) generate behavioral diversity? Load-bearing vs contributory vs redundant.

### Verdict: a multi-substrate distributed pathway with TWO load-bearing components missing from current REE.

The literature converges on a distributed system with at least four named substrates contributing to behavioural diversity, each with a distinct function:

1. **Locus coeruleus norepinephrine (LC-NE)** — Aston-Jones & Cohen 2005 ([DOI](https://doi.org/10.1146/annurev.neuro.28.061604.135709), PMID 16022602). Tonic LC firing elevates baseline noise/disengagement (continuous channel); phasic LC firing facilitates committed exploitation. The tonic→phasic mode switch is the substrate of the explore-exploit transition, gated by ACC and OFC inputs that monitor task utility. **REE status:** PARTIAL. MECH-104 (LC-NE volatility surprise spike) is substrate-landed and covers the *triggered* phasic-spike role. The *continuous tonic baseline* role is not yet substrate-landed. **Verdict: LOAD-BEARING; MECH-313 (stochastic-noise-floor candidate) is the LC-tonic analog and must land for ARC-065 completion.**

2. **Frontopolar cortex + intraparietal sulcus** — Daw, O'Doherty, Dayan, Seymour & Dolan 2006 ([DOI](https://doi.org/10.1038/nature04766), PMID 16778890). fMRI dissociation: frontopolar BOLD selectively elevated during exploratory choice; striatum + vmPFC during exploitative. **REE status:** NO ANALOG. The frontopolar exploration substrate has no current counterpart. **Verdict: LOAD-BEARING; MECH-314 (structured-curiosity-bonus channel) is the frontopolar analog. This is the second missing substrate ARC-065 must register.**

3. **Striatum (novelty-driven choice)** — Wittmann, Daw, Seymour & Dolan 2008 ([DOI](https://doi.org/10.1016/j.neuron.2008.04.027), PMID 18579085). Striatal BOLD tracks novelty-based choice even when novelty is unrelated to outcome value. **REE status:** PARTIAL. MECH-216 (E1 schema-readout wanting) is the closest current candidate but operates in the *opposite* direction (schema MATCH triggers wanting, not schema NOVEL triggers exploration). **Verdict: CONTRIBUTORY; MECH-314a (novelty-bonus sub-MECH under MECH-314) extends MECH-216 with the inverse-frequency reading.**

4. **Hippocampus (forward trajectory sequences)** — Pfeiffer & Foster 2013 ([DOI](https://doi.org/10.1038/nature12112), PMID 23594744). Hippocampal place-cell sequences sample candidate trajectories toward goals before action selection. **REE status:** PARTIAL. MECH-292 (ranked ghost-goal bank) and MECH-293 (awake ghost-goal probes) instantiate proposal-side diversity. **Verdict: CONTRIBUTORY; MECH-315 (proposal-diversity-channel sub-MECH candidate) may be redundant with the existing MECH-293 substrate. Resolve during ARC-064 lit-pull.**

5. **dACC + lateral aPFC anti-recency** — flagged via the MECH-260 substrate-landed claim. The Scholl 2015 anchor paper for MECH-260 (anti-recency suppression of vmPFC bias toward recently-rewarded choices) was not directly retrievable in this pull (citation-lookup ambiguous; deferred to a follow-up search). **REE status:** SUBSTRATE-LANDED (MECH-260). **Verdict: CONTRIBUTORY but not load-bearing alone — MECH-260 prevents over-commitment but does not actively generate diversity.**

The cross-reference against the existing REE substrate inventory:

| Biological substrate | REE substrate currently covering it | Load-bearing? | ARC-065 sub-MECH candidate |
|---|---|---|---|
| LC-NE tonic baseline | NONE | Yes | MECH-313 stochastic-noise-floor |
| LC-NE phasic spike | MECH-104 volatility-surprise | (already triggered-arm) | (no new MECH needed) |
| Frontopolar exploration | NONE | Yes | MECH-314 structured-curiosity-bonus |
| Striatum novelty | MECH-216 schema-readout-wanting (partial; opposite polarity) | Contributory | MECH-314a novelty-bonus sub-MECH |
| Hippocampal trajectory sampling | MECH-292/293 ghost-goal substrates | Contributory | (may be redundant; defer to ARC-064 pull) |
| dACC anti-recency | MECH-260 (substrate-landed) | Contributory only | (no new MECH needed) |

---

## R3 — Cluster registration vs extension of existing claim?

### Verdict: PROMOTE-TO-CLUSTER. Confidence 0.82.

The ARC-051 multi-level wanting hierarchy was the strongest existing-cluster candidate to absorb a curiosity sub-mechanism, but Daw 2006 (PMID 16778890) shows the brain has *anatomically separate* substrates for exploration vs exploitation: frontopolar+IPS for the former, striatum+vmPFC for the latter. ARC-051's wanting hierarchy and the substrate-landed MECH-216/295 wanting/liking machinery sit on the exploitation side of this dissociation. Folding curiosity into ARC-051 conflates two anatomically and functionally distinct pathways.

MECH-260 (dACC anti-recency) is the closest existing anti-monostrategy mechanism, but it is *contributory*, not load-bearing — it prevents over-commitment to recent choices but does not actively generate alternative behaviours. The literature does not support promoting MECH-260 to the load-bearing diversity-generator role.

The MECH-216 + MECH-205 + SD-037 partial-cluster (predictive wanting + surprise-gated replay + orexin broadcast override) covers *triggered* arousal and *recognition-driven* wanting, but does not include the continuous-noise-floor channel (LC-tonic-analog) or the uncertainty-driven-curiosity channel (frontopolar-analog) that R2 identifies as load-bearing.

**Cluster registration recommendation:** ARC-065 anchors a new architectural pathway (`behavioral_diversity_generation_pathway`) with at least the following children:

- **ARC-065** anchor: behavioural-diversity-generation pathway. Architectural commitment that diversity is upstream-generated and feeds both ARC-062 (top-down rule application) and ARC-064 (bottom-up rule discovery). Cross-reference: MECH-260, MECH-216, MECH-104, MECH-205, SD-037, MECH-292, MECH-293.
- **MECH-313** stochastic-noise-floor (LC-tonic-analog; non-zero softmax temperature on E3 + low-amplitude policy parameter perturbation).
- **MECH-314** structured-curiosity-bonus (frontopolar-analog; epistemic-value or information-gain bonus on E3 score_bias). With sub-MECH placeholders:
  - **MECH-314a** novelty-driven sub-flavour (Wittmann 2008 striatal-novelty anchor; inverse-visit-frequency bonus at unfamiliar z_world locations).
  - **MECH-314b** uncertainty-driven sub-flavour (Daw 2006 frontopolar anchor; scales with model PE variance).
  - **MECH-314c** learning-progress-driven sub-flavour (Schmidhuber/Pathak intrinsic-motivation tradition; not anchored in this pull, deferred to a future PubMed/arXiv pull on intrinsic motivation).
- **MECH-315** proposal-diversity-channel candidate (hippocampal-trajectory-sampling-analog). May be redundant with MECH-292/293; defer the registration decision to the ARC-064 lit-pull.
- **Q-XXX-1** "What is the relative weight of MECH-313 vs MECH-314 in producing behavioural diversity? Does it depend on environment volatility (Wilson 2014 horizon analog)?" Falsifiable with MECH-313-only-arm vs MECH-314-only-arm vs combined-arm contrast.
- **Q-XXX-2** "Are MECH-314a/b/c three distinct substrates or three readings of one mechanism with different upstream inputs?" Defer until ARC-064 pull lands more material on the curiosity-flavour distinctions.
- **Q-XXX-3** "Is MECH-313 (LC-tonic-analog) a separate parameter from MECH-260 (dACC anti-recency), or do they collapse into one anti-monostrategy substrate?" Falsifiable with MECH-313-OFF + MECH-260-ON arm vs both-OFF arm vs both-ON arm.

---

## R4 — Continuous background generator vs triggered process?

### Verdict: HYBRID — continuous presence with triggered dominance. Confidence 0.80.

The naive continuous-vs-triggered binary is rejected by the literature.

Aston-Jones & Cohen 2005 (PMID 16022602) is explicit: LC-NE has both a tonic mode (continuous-background channel: baseline noise floor and disengagement bias that operates throughout task performance) and a phasic mode (triggered: sharp activation on decision-relevant stimuli). The tonic→phasic mode switch is itself the explore-exploit transition. Friston 2015 (PMID 25689102) gives the computational version: epistemic value is computed *every tick* from current model uncertainty (continuous), but its *dominance* over extrinsic value is *triggered* by uncertainty crossing a threshold. The active inference framing makes diversity generation always-on but with weight on action selection that rises and falls.

For the cluster architecture this means:

- MECH-313 (stochastic-noise-floor) is **continuous** — non-zero softmax temperature on E3 every tick, regardless of context.
- MECH-314 (structured-curiosity-bonus) is **continuous in computation but triggered in dominance** — information-gain estimates updated every tick, but the bonus magnitude on E3 score_bias scales with model uncertainty / volatility detection. The MECH-104 volatility-surprise spike (already substrate-landed) is the natural trigger source.

The MECH-312 (dual-channel rule arbitration) implication is also non-trivial: ARC-065 is always running in the background, so MECH-312's arbitration is between rule channels (ARC-062 top-down vs ARC-064 bottom-up) with ARC-065 as a third always-on competitor that gets dominance-weight when both rule channels are uncertain. That is a *three-way arbitration* in dominance terms, not a two-way arbitration with a fall-back.

---

## What this pull does NOT settle

Items deferred to subsequent pulls or future sessions:

1. **MECH-314c learning-progress-driven curiosity sub-flavour.** Schmidhuber 2010 and Pathak 2017 (the intrinsic-motivation RL tradition) are not on PubMed; they should be web-searched in a follow-up pull. Their inclusion may also fold into the ARC-064 lit-pull since hippocampal-replay-driven option proposal overlaps the territory.
2. **The MECH-260 anchor literature (Scholl 2015).** Citation lookup was ambiguous and the specific dACC-anti-recency-suppression Scholl paper was not retrieved in this pull. The MECH-260 substrate is already landed in REE; this is anchor-completion work, not a registration blocker.
3. **MECH-315 proposal-diversity-channel registration.** Pfeiffer & Foster 2013 supports the architectural commitment but does not settle whether MECH-315 is a separate sub-MECH or absorbed into MECH-293 ghost-goal probes. The ARC-064 lit-pull (Pull 2) on bottom-up rule discovery will go deeper into hippocampal proposal mechanisms and is the natural place to resolve this.
4. **The MECH-312 three-way arbitration scope.** R4's hybrid-continuous-with-triggered-dominance verdict expands MECH-312 from a two-way (top-down rule vs bottom-up rule) to a three-way arbitration (top-down rule vs bottom-up rule vs always-on diversity). Pull 3 (MECH-312 dual-channel arbitration) is partially gated on this verdict — the arbitration mechanism literature should be searched with the three-way framing in mind.
5. **Calibration of relative weights.** None of the four R-verdicts settle the magnitudes. Q-XXX-1 (relative weight of MECH-313 vs MECH-314) is empirical, not literature-resolvable. The validation experiment design will need to do a parametric sweep.
6. **Whether ARC-064 (bottom-up rule discovery) actually warrants its own cluster vs being absorbed into ARC-065.** ARC-065 generates diversity; ARC-064 extracts rules from that diversity. They could be one cluster with a single "behavioural-discovery pathway" anchor, or two clusters with a clean division of labour. The Pull 2 verdict on ARC-064 substrate-distinctness will resolve this.
7. **The Pull 4 alternative-framing question** (whether option-policies / schemas without rule-level abstraction would be a cleaner architecture overall). This pull's results presuppose rules exist as a meaningful level of description; Pull 4 should test that presupposition.

---

## Recommended next actions

1. **Register the ARC-065 cluster in claims.yaml** with the children specified in the R3 verdict (ARC-065, MECH-313, MECH-314 with sub-MECH placeholders 314a/b/c, MECH-315 deferred, Q-XXX-1/2/3). Use the verdict-cited evidence_quality_note pattern to anchor each claim to this synthesis.
2. **Update the V3-EXQ-543b design** (currently in the queue list, not yet written) to add a third arm: ARM_0 baseline / ARM_1 diversity-only (MECH-313 + MECH-314a baseline-substrate, no gated_policy) / ARM_2 diversity + gated_policy (full ARC-062 stack). Without ARM_1 we cannot tell if a PASS in ARM_2 is "rule application worked" vs "diversity alone was sufficient and gating was epiphenomenal." This is a design upgrade the pull's verdicts make load-bearing.
3. **Commission Pull 2** (ARC-064 bottom-up rule discovery) — the verdict here will resolve the MECH-315 deferred-vs-absorbed question and constrain whether ARC-064 is a separate cluster or ARC-065's downstream consumer.
4. **Defer Pull 3 (MECH-312 arbitration)** until after Pulls 2 and 4 land — the three-way-arbitration scope this pull surfaced needs both ARC-064 substrate-distinctness and Pull 4's option-policy alternative resolved before MECH-312's anchor literature can be searched with the right scope.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Wilson 2014 | [10.1037/a0038199](https://doi.org/10.1037/a0038199) | R1 | supports | 0.86 |
| Aston-Jones & Cohen 2005 | [10.1146/annurev.neuro.28.061604.135709](https://doi.org/10.1146/annurev.neuro.28.061604.135709) | R2, R4 | supports | 0.84 |
| Daw et al. 2006 | [10.1038/nature04766](https://doi.org/10.1038/nature04766) | R2, R3 | supports | 0.82 |
| Kidd & Hayden 2015 | [10.1016/j.neuron.2015.09.010](https://doi.org/10.1016/j.neuron.2015.09.010) | R1, R2 | supports | 0.78 |
| Faisal et al. 2008 | [10.1038/nrn2258](https://doi.org/10.1038/nrn2258) | R1 noise-arm | supports | 0.83 |
| Pfeiffer & Foster 2013 | [10.1038/nature12112](https://doi.org/10.1038/nature12112) | R2 | supports | 0.78 |
| Wittmann et al. 2008 | [10.1016/j.neuron.2008.04.027](https://doi.org/10.1016/j.neuron.2008.04.027) | R2 (novelty sub-flavour) | supports | 0.78 |
| Friston 2010 | [10.1038/nrn2787](https://doi.org/10.1038/nrn2787) | R1 structured-arm | supports | 0.72 |
| Friston et al. 2015 | [10.1080/17588928.2015.1020053](https://doi.org/10.1080/17588928.2015.1020053) | R1, R4 | supports | 0.74 |

**Aggregate ARC-065 lit_conf** (post-indexer): expected to land in the 0.78–0.82 range, supports-direction, 9-entry cohort with three distinct biological systems (LC-NE, frontopolar/striatum, hippocampus) and two computational anchors (FEP, active inference) represented.

According to PubMed, all entries in this synthesis are sourced from PubMed-indexed literature with DOIs as cited above.
