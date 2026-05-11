# SYNTHESIS -- MECH-317 behavioural pattern compression (ARC-064 Pull-2 follow-on)

**Pull 2 follow-on** to the ARC-064 bottom-up rule discovery cluster lit-pull (2026-05-10).
**Date:** 2026-05-11. **Entries:** 5 papers (direct empirical anchor for striatal chunking + foundational options framework + gradient option discovery + normative-optimality criterion + diversity-driven skill discovery).
**Source attribution:** per-paper records cite PubMed / arXiv and include DOI links; this synthesis aggregates and adjudicates.

---

## Why this pull was commissioned

Pull 1 (ARC-064 bottom-up rule discovery, 2026-05-10) identified MECH-317 as the load-bearing missing substrate for behavioural-pattern-compression / action-chunking, with the Smith & Graybiel 2013/2016 review-level literature already anchored. Pull 1's R2 verdict noted that "MECH-317 chunks repeated patterns into reusable options; MECH-318 abstracts the higher-level rule state under which those options are deployed" but deferred the question of which implementation flavour the chunking substrate should commit to. Pull 2 returns to the literature with sharper questions: what is the canonical computational target (the options framework), what is the direct empirical anchor for the striatal-chunking biology (Martiros et al. 2018), what implementation flavours have been proposed (option-critic, DIAYN), and what normative criterion adjudicates among them (Solway et al. 2014).

Background context for the timing of this pull: a parallel session today registered MECH-323 (policy_composition_chunk_accumulator) as the ARC-071 first child mechanism -- the formation-operator side of chunk-creation. MECH-317 (in the ARC-064 family) is the structural substrate that the MECH-323 formation operator (in the ARC-071 family) writes to. The two are structurally related and the cluster-shape work for ARC-064 and ARC-071 has been quietly converging. This Pull 2 settles the literature-level adjudication for the ARC-064 side; the architectural decision for whether MECH-317 substrate and MECH-323 operator should share an implementation backbone is a substrate-design call this lit-pull is meant to inform.

---

## R1 -- Which implementation flavour for MECH-317's chunking substrate?

### Verdict: HYBRID -- substrate-driven repetition triggers (Smith & Graybiel / MECH-323 lineage) as the gating layer, options-framework formalisation (Sutton-Precup-Singh) as the representational target, gradient option-component learning (option-critic) as the inner-loop update rule, with Solway-et-al normative-optimality as the validation criterion. Confidence 0.78.

The literature does not select one flavour cleanly. The four candidate implementation flavours have different strengths and known failure modes:

- **Substrate-driven repetition triggers** (Smith & Graybiel 2013/2016 biological anchor; MECH-323 implementation registration): chunks form when behaviour is repeated with consistent outcomes. The biology is well-anchored; the failure mode is that the trigger machinery has to be specified separately and may miss useful chunks that are not strictly-repeated. Strongest case: alignment with Martiros et al. 2018 SPN-bracketing biology.

- **Options framework formalisation** (Sutton, Precup & Singh 1999): chunks should be option triples <initiation-set, intra-option policy, termination-condition>. This is not a competing flavour -- it is the computational target that all the other flavours produce instances of. Failure mode: substrate-agnostic, so does not itself adjudicate among implementations.

- **Gradient option discovery** (Bacon, Harb & Precup 2017 option-critic): learn the option-component parameters end-to-end via policy gradient. Failure modes: option collapse (all options become identical), option degeneracy (zero-length or maximum-length options). Anticipated and partially addressed by deliberation-cost extensions but not fully resolved.

- **Diversity-driven skill discovery** (Eysenbach et al. 2018 DIAYN): learn skills via mutual-information objective. Failure mode: the discovered skills are diverse-by-construction, NOT repeated-pattern-compressions -- so this flavour is the least-aligned with MECH-317's actual objective.

The hybrid recommendation reads MECH-317 as:
- **Substrate-driven trigger machinery** decides WHEN chunks form (MECH-323-style repetition + outcome-consistency + evaluative gate triggers; consistent with the Smith & Graybiel / Martiros biology).
- **Option triple representation** anchors WHAT chunks ARE (Sutton-Precup-Singh structure: initiation_set + intra-option policy + termination_condition).
- **Gradient option-critic** can be used as the inner-loop learning rule for option-component parameters once the triggers have committed to forming a chunk (avoiding the option-collapse and option-degeneracy modes that pure option-critic exhibits without substrate-driven triggers).
- **Solway et al. optimality criterion** validates that the produced chunks are normatively-correct (chunks align with bottleneck states / persistent sub-tasks).

The DIAYN flavour does NOT make it into the hybrid because its objective is genuinely opposed to MECH-317's compression goal. The other three flavours can compose; DIAYN cannot compose with them without the architectural commitment becoming incoherent.

Confidence 0.78 because the hybrid is a literature-informed architectural commitment but the specific substrate-design choices (which network components, how the trigger machinery couples to the gradient inner-loop, how the optimality validation is operationalised) are not literature-decidable.

---

## R2 -- What does the chunking signature look like on REE's behavioural substrate?

### Verdict: Martiros et al. 2018 bracketing signature, behaviourally measurable as action-distribution entropy troughs at chunk-boundaries with elevated mid-chunk action-determinism. Confidence 0.82.

The Martiros 2018 paper provides the most-direct empirical evidence for what chunking looks like at the substrate level. The novel finding is the two-population coordination structure: SPN-class neurons fire at chunk start and end (bracket signal), interneuron-class neurons fire mid-chunk (continuation signal). The two signals are coordinated but inverse -- chunks are not represented by a continuous neural code but by a transition pattern at boundaries plus a within-chunk continuation signal.

For REE's behavioural validation, the corresponding signatures are:
- **Action-distribution entropy troughs at chunk-boundaries**: a chunk-onset and chunk-end should show low-entropy action-selection (the agent is committed to the bracket-defining action). Mid-chunk action-entropy can be higher (the within-chunk policy may include lawful variations).
- **Elevated mid-chunk action-determinism in the continuation sense**: the agent commits to the stereotyped behaviour during the chunk; the variability is around a stable behavioural trajectory, not around chunk-existence.
- **Substrate-readiness on the trajectory record**: a substrate that supports MECH-317 should produce these signatures on a sufficiently structured behavioural task (SD-054 reef forage-approach-retreat is a candidate; SD-054 enriched with multi-rule-context would be stronger).

The behavioural-signature reading is the only signal REE has -- there is no direct neural-recording substrate. The substrate-readiness diagnostic for MECH-317 should test whether the substrate produces detectable bracketing signatures on a trajectory record. V3-EXQ-548 (SD-054 bipartite substrate-readiness, PASS earlier today) is a structural analog of this kind of diagnostic; a MECH-317-specific substrate-readiness diagnostic should follow the same template.

---

## R3 -- What does the Solway et al. optimality criterion imply for substrate validation?

### Verdict: Chunks should align with bottleneck states; substrate validation should test whether produced chunks satisfy the information-theoretic criterion. Confidence 0.76.

Solway et al. 2014 supplies the normative criterion against which produced chunks should be evaluated. A behavioural hierarchy is optimal if it minimises the joint description-length of the task's transition structure under the hierarchical decomposition. Operationally, optimal chunks align with bottleneck states (low-entropy transitions in the trajectory record) and with persistent sub-tasks (transition clusters that maintain internal coherence).

For REE's substrate validation:
- **Bottleneck-state alignment test**: identify the bottleneck states in the SD-054 (or enriched) trajectory record; check whether the chunks produced by the substrate align their initiation-set / termination-condition with those bottleneck states. Failure mode: chunks have arbitrary boundaries not aligned with bottleneck states -- the substrate is doing 'chunking' in some loose sense but not 'optimal chunking'.
- **Description-length test**: compute the joint description-length of the trajectory record under (a) flat-policy representation and (b) the substrate's option-decomposition; verify that (b) is shorter than (a). Failure mode: the option decomposition does not reduce description-length, indicating the chunks are not capturing real regularity.
- **Spontaneous-discovery alignment**: Solway et al.'s behavioural experiments produced testable predictions about which decompositions humans converge on. A V3 substrate that aims to instantiate a humanlike chunking mechanism should reproduce at least some of those predictions on an analogous trajectory task.

The Solway criterion is normative -- it specifies what the chunks should look like -- so it is independent of the implementation flavour. It applies whether MECH-317 is implemented via substrate-driven triggers, option-critic gradient discovery, or any hybrid. The validation criterion is the substrate-design pass's quality-assurance gate.

---

## R4 -- Relationship between MECH-317 and the parallel-session-registered MECH-323 chunk-formation operator?

### Verdict: COMPLEMENTARY -- MECH-317 is the substrate structure; MECH-323 is the formation operator that writes to it. Recommendation: implement MECH-317 substrate first, then MECH-323 operator as a thin layer above it. Confidence 0.74.

A parallel session today (mech-323-arc-071-accumulator-2026-05-11T1756Z) registered MECH-323 as the ARC-071 first child mechanism -- the policy_composition_chunk_accumulator that builds chunk candidates from repeated executions with consistent outcomes. The relationship between MECH-323 (ARC-071 family) and MECH-317 (ARC-064 family) is structurally interesting and deserves explicit architectural framing.

The reading that holds up: MECH-317 names the SUBSTRATE for behavioural-pattern-compression -- the data structure in which chunks live, the option-triple representation, the bracket-detection mechanism, the within-chunk continuation signal. MECH-323 names the FORMATION OPERATOR that decides when new chunks should be added to the substrate. The two are complementary, not competing.

Architecturally:
- **MECH-317 substrate** must exist for MECH-323 to have anywhere to write chunks to. The substrate provides the option-triple representation (Sutton-Precup-Singh structure), the bracket-detection mechanism (Martiros-style), and the within-chunk continuation signal.
- **MECH-323 operator** decides when a new chunk should be formed (repetition + outcome-consistency triggers + evaluative gate) and what its initial parameters should be. It writes to the MECH-317 substrate.
- **The Solway criterion** validates that the chunks the operator writes are normatively-correct.
- **The option-critic gradient** can be used as the inner-loop update rule for refining the parameters of chunks already in the substrate -- but only on chunks that the MECH-323 operator has committed to forming.
- **DIAYN-style discovery is not part of the architecture** because its objective is opposed to MECH-317's compression goal.

The substrate-design pass implication: implement MECH-317 substrate first (option-triple data structure + bracket-detection + within-chunk continuation), then implement MECH-323 operator as a thin layer above it (deciding when new chunks form and what their initial parameters are), then use option-critic-style gradients for refinement, then validate against Solway optimality on the target behavioural substrate. The MECH-317 and MECH-323 claims should NOT be merged but their implementations should share a substrate backbone.

---

## What this pull does NOT settle

1. **The substrate-design choice itself.** The hybrid recommendation under R1 is a literature-informed architectural commitment, not a substrate specification. The V3 substrate-design pass has to decide where in the existing REE machinery the option-triple representation lives, how the trigger machinery couples to the inner-loop gradients, and how the Solway-validation is operationalised. None of these are literature-decidable.

2. **The behavioural-substrate richness question.** SD-054 reef forage-approach-retreat is a candidate trajectory with potential chunking structure, but whether it provides enough behavioural-pattern repetition for MECH-317 validation is a substrate-readiness question. The substrate-readiness diagnostic for MECH-317 should follow the V3-EXQ-548 (SD-054 bipartite) template -- structural-only env-level test with a pre-registered criterion for whether the substrate produces chunkable behaviour.

3. **The MECH-323 implementation pass.** This lit-pull adjudicates the ARC-064 substrate-side implementation flavour for MECH-317. The ARC-071 operator-side implementation pass for MECH-323 is a separate substrate-design call that will need its own treatment.

4. **The Q-044 / MECH-314 cluster relationship.** The Q-044 synthesis flagged that SD-054 reef substrate is probably insufficient for the MECH-314 three-arm ablation without enrichment. MECH-317 validation may need a similar enrichment. Whether the enrichments are the same architectural commitment or two parallel ones is a substrate-design call.

---

## Per-paper summary index

| Entry | DOI | Role | Direction | Confidence |
|---|---|---|---|---|
| Martiros, Burgess & Graybiel 2018 | [10.1016/j.cub.2018.01.031](https://doi.org/10.1016/j.cub.2018.01.031) | direct empirical anchor (DLS chunking; bracket signature) | supports | 0.84 |
| Sutton, Precup & Singh 1999 | [10.1016/S0004-3702(99)00052-1](https://doi.org/10.1016/S0004-3702(99)00052-1) | foundational computational target (option triple) | supports | 0.82 |
| Bacon, Harb & Precup 2017 | [10.1609/aaai.v31i1.10916](https://doi.org/10.1609/aaai.v31i1.10916) | implementation flavour (gradient option discovery) | supports | 0.78 |
| Solway et al. 2014 | [10.1371/journal.pcbi.1003779](https://doi.org/10.1371/journal.pcbi.1003779) | normative criterion (optimal hierarchy) | supports | 0.80 |
| Eysenbach et al. 2018 | [arXiv:1802.06070](https://arxiv.org/abs/1802.06070) | implementation flavour (diversity skill discovery) | mixed | 0.62 |

**Aggregate MECH-317 lit_conf** (post-indexer): expected to land in the 0.74-0.80 range, supports-direction-dominant, 5-entry cohort spanning the direct empirical anchor (Martiros), the foundational computational target (Sutton-Precup-Singh), two implementation flavours (option-critic + DIAYN), and the normative criterion (Solway). The hybrid R1 recommendation (substrate-driven triggers + option-triple representation + option-critic inner loop + Solway validation) is the literature-informed input to the substrate-design pass that follows.

According to PubMed and arXiv, all entries in this synthesis are sourced as cited above; DOIs are linked per-entry.
