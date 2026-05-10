# SYNTHESIS -- Rule-Apprehension Vocabulary Mapping + Result Inheritance

**Pull 4 of 4** in the ARC-062 rule-apprehension cluster scoping series.
**Date:** 2026-05-10. **Entries:** 12 papers (across foundational AI options/HRL, schema-tradition cognitive neuroscience, meta-RL theory + implementation, MaxEnt-RL).
**Source attribution:** the per-paper records cite arXiv / DOIs / PubMed where available; this synthesis aggregates and adjudicates.

---

## Why this pull was commissioned

Pulls 1 and 2 generated a substantial new cluster proposal (ARC-064 + ARC-065 + sub-MECHs MECH-313/314/316/317/318) using REE-internal vocabulary -- "rule apprehension", "rule application", "rule discovery", "behavioural-pattern-compression", "rule-state-abstraction-substrate". The user's reframing of Pull 4 was: before locking that cluster, test the working hypothesis that this vocabulary already has well-established names in the AI / RL / cognitive-science literature. If it does, the deliverable is a translation table + an inventory of formal results we can inherit. If it does not, the deliverable identifies the genuinely novel REE contribution that justifies REE-native MECH names.

The 12 papers cover four parallel ancestor lineages of the architectural slot REE has been pointing at:

1. *Options / Hierarchical RL* (Sutton-Precup-Singh 1999, Bacon 2017, Eysenbach 2018, Botvinick-Niv-Barto 2009, Solway 2014).
2. *Schema / Contention Scheduling* (Norman-Shallice 1986, Cooper-Shallice 2000, Botvinick-Plaut 2004).
3. *Meta-RL* (Wang 2018, Duan 2016, Botvinick 2019).
4. *MaxEnt-RL* (Haarnoja 2018).

---

## R1 -- Translation table (the load-bearing artifact)

The table maps each working REE term in the rule-apprehension cluster to its closest existing-literature term. Confidence is in the cleanliness of the mapping, not in the correctness of the underlying claim.

| REE working term | Closest existing-literature term | Canonical paper(s) | Confidence | Justification |
|---|---|---|---|---|
| **ARC-062** "top-down rule application via gated_policy + discriminator" | Supervisory Attentional System (SAS) overriding contention scheduling; equivalently, *policy-over-options* in HRL canon; equivalently, *meta-learned context-conditioned policy* in meta-RL | Norman & Shallice 1986; Sutton-Precup-Singh 1999; Wang et al. 2018 | 0.85 | Three converging traditions name this same architectural slot. SAS is the most functionally precise (override of routine for non-routine contexts); options' policy-over-options is the cleanest formal version; meta-RL is the most recent algorithmic instantiation. |
| **ARC-064** "bottom-up rule discovery via behavioural-pattern-extraction" | *Option discovery* in HRL canon; equivalently, *unsupervised skill discovery* (DIAYN) when reward-agnostic; equivalently, *episodic + meta-RL fast learning* (Botvinick 2019) when reward-driven | Bacon et al. 2017; Eysenbach et al. 2018; Botvinick et al. 2019 | 0.80 | Direct algorithmic counterparts. Option-critic (Bacon 2017) handles reward-driven option discovery; DIAYN handles reward-agnostic skill discovery; the fast/slow framing organises the cluster. |
| **ARC-065** "behavioural-diversity-generation pathway" | *Maximum-entropy RL* + *unsupervised skill diversity* (DIAYN's mutual-information term) | Haarnoja et al. 2018; Eysenbach et al. 2018 | 0.85 | MaxEnt-RL is the canonical algorithmic home; DIAYN's mutual-information objective is the structured diversification arm. |
| **MECH-309** "trainers weight rules they do not invent" (logical-necessity diagnostic) | (NO CLEAN EXISTING ANALOG) | -- | 0.20 | This is a meta-claim about the relationship between training signal and rule-content, not a claim about an architectural component. Closest neighbours -- imitation learning, inverse RL -- do not capture the specific REE point. Candidate REE divergence (R3). |
| **MECH-310** "trajectory-clustering primitive" | Successor-representation clustering / state-aggregation; equivalently, k-means-on-trajectory-segments in option-discovery literature | Stachenfeld et al. 2017 (Pull 2 entry); Stolle & Precup 2002 | 0.65 | The primitive exists in the literature but under multiple names. SR-clustering is the most principled. |
| **MECH-311** "cluster-to-supervisory-label transduction" | *Discriminator network* in DIAYN; equivalently, *task-state decoder* in OFC-cognitive-map literature (Pull 2) | Eysenbach et al. 2018; Wilson 2014 / Schuck 2016 (Pull 2) | 0.78 | DIAYN's discriminator IS this transduction. |
| **MECH-312** "dual-channel rule arbitration" | *Contention scheduling* (schema tradition); equivalently, *uncertainty-weighted controller arbitration* (Daw 2005, Pull 2 entry) | Cooper & Shallice 2000; Daw, Niv & Dayan 2005 (Pull 2) | 0.85 | Two lineages with the same essential structure. Contention scheduling is the cognitive-neuroscience name; uncertainty-weighted arbitration is the computational-RL name. They line up cleanly. |
| **MECH-313** "stochastic-noise-floor (LC-tonic-analog)" | *Maximum-entropy policy regularisation* (MaxEnt-RL); equivalently, *softmax temperature* parameter | Haarnoja et al. 2018 | 0.90 | Direct algorithmic counterpart. The biological reading (LC-NE tonic) and the algorithmic reading (MaxEnt entropy term) are the same claim in two vocabularies. |
| **MECH-314** "structured-curiosity-bonus (frontopolar-analog)" | *Intrinsic motivation / information-gain bonus* in RL; equivalently, *epistemic value* in active inference (Pull 1 entries) | Pathak 2017 (not in this pull's entries; cited via Pull 1 R3 deferred); Friston 2015 (Pull 1) | 0.72 | Multiple computational counterparts; the field has not converged on a single canonical name. |
| **MECH-316** "cross-episode-regularity-extraction (hippocampal-monosynaptic-CLS-analog)" | *Episodic-memory-based RL*; equivalently, *successor representation* learning; equivalently, *option discovery via bottleneck states* | Botvinick et al. 2019; Stachenfeld et al. 2017 (Pull 2); Solway et al. 2014 | 0.78 | Three converging accounts of the same mechanism. |
| **MECH-317** "behavioural-pattern-compression (dorsolateral-striatum-analog)" | *Option formation / option-critic* in HRL; equivalently, *action-chunking* in striatal-learning literature (Pull 2) | Bacon et al. 2017; Smith & Graybiel 2013 (Pull 2) | 0.85 | Direct counterparts. Option-critic is the algorithmic version; striatal action-chunking is the biological version. |
| **MECH-318** "rule-state-abstraction-substrate (OFC-cognitive-map-analog)" | *State abstraction* in HRL; equivalently, *task-state representation* in OFC literature (Pull 2); equivalently, *meta-RL recurrent latent state* | Wilson 2014 / Schuck 2016 / Niv 2019 (Pull 2); Wang et al. 2018 | 0.80 | Multiple converging accounts. The meta-RL reading is the most parsimonious -- it collapses MECH-318 into the recurrent latent-stack. |

**Headline R1 verdict.** Approximately 80% of REE's rule-apprehension vocabulary already has well-established names in existing literature, with high-confidence mappings. The genuinely novel REE content (R3) is concentrated in two clusters: (i) MECH-309's logical-necessity diagnostic, and (ii) the simulation-mode write-gating + dual-stream affective interaction + V_s invalidation machinery developed elsewhere in REE. The cluster-level claim "rule apprehension is policy machinery in different vocabulary" is *largely true*, with specific principled exceptions.

---

## R2 -- Inheritable formal results inventory

For each existing-literature framework, the formal results / theorems / well-tested empirical signatures REE could in principle inherit.

### Options / SMDP framework (Sutton-Precup-Singh 1999)

- *Option-augmented MDPs are SMDPs*; standard SMDP value iteration and Q-learning extend with convergence guarantees.
- *Bellman equations for options*: the option-level value function satisfies a temporally-abstract Bellman equation; this is the foundation of all subsequent option-level planning.
- *Intra-option learning*: an option's value can be learned from any trajectory consistent with the option's policy, without needing to fully execute it. This is a substantial sample-efficiency win.

### Option-critic architecture (Bacon 2017)

- *Policy-gradient theorems for options*: gradients exist for both intra-option policy and termination function; end-to-end learning is well-defined.
- *Option-collapse failure mode*: a known and documented failure mode (discovered options become trivially short or trivially identical), with eight years of mitigation literature (entropy regularisation on terminations, deliberation-cost penalties). Diagnostic transfer for REE: V3-EXQ-543's seed-2 byte-identical collapse pattern matches option-collapse signatures.

### DIAYN unsupervised skill discovery (Eysenbach 2018)

- *Mutual-information skill objective*: I(s; z) maximisation under MaxEnt policy gives diverse skills without reward.
- *Skill-conditioned policy + discriminator architecture*: clean separation of the diversity-generation (policy entropy) and rule-extraction (state-to-skill discriminator) arms in one objective.
- *Discriminator-collapse failure mode*: same diagnostic family as option-collapse and REE's monomodal-collapse.

### Hierarchical RL with neural mapping (Botvinick-Niv-Barto 2009)

- *PFC-as-policy-over-options* mapping. Suggestive rather than mechanistically locked-down.
- *Basal-ganglia gating + dopamine learning signals* for option formation.
- *OFC-conditioned-state-abstraction* role (later refined by Pull 2's Wilson 2014, Schuck 2016, Niv 2019).

### Optimal Behavioural Hierarchy (Solway 2014)

- *Bottleneck-state characterisation* of optimal hierarchies. Falsifiable empirical signature: discovered chunks should align with bottleneck states.
- *Empirical evidence* that humans spontaneously discover near-optimal hierarchies in maze tasks.

### Schema / contention scheduling tradition (Norman-Shallice 1986, Cooper-Shallice 2000)

- *SAS vs contention-scheduling dissociation*: frontal-lobe-patient lesion data anchoring the dual-mechanism architecture. Falsifiable empirical signature for REE: ablating ARC-062 (SAS analog) should produce capture-error / utilisation-behaviour patterns, not generalised performance loss.
- *Lateral-inhibition-based action-selection mechanism* directly transferable to MECH-312.

### Botvinick-Plaut 2004 counter-current

- *Recurrent-distributed-state baseline*: a single recurrent network can reproduce schema-hierarchy behaviour in routine action without explicit hierarchical decomposition. Sets the *minimum-architecture baseline* against which the explicit-cluster claim has to be defended.

### Meta-RL (Wang 2018, Duan 2016, Botvinick 2019)

- *RL^2 algorithm* (Duan 2016): training schedule = multi-task distribution; fast inner-loop emerges in recurrent state.
- *PFC-as-meta-RL* mapping (Wang 2018): biological reading.
- *Fast/slow learning synthesis* (Botvinick 2019): episodic-RL + meta-RL = sample-efficient learning.

### MaxEnt-RL (Haarnoja 2018)

- *Soft-Q-learning convergence guarantees*.
- *Auto-tuning of entropy temperature*: principled procedure for setting alpha (target-entropy-constraint).
- *Empirical benchmarks* on continuous control.

**Aggregate R2 verdict.** REE could inherit substantial off-the-shelf machinery if it adopts existing-literature vocabulary. The most valuable inheritances are: convergence guarantees (options + MaxEnt-RL), policy-gradient theorems (option-critic), failure-mode diagnostic literature (option-collapse), bottleneck-state empirical prediction (Solway), and the SAS/contention-scheduling lesion-pattern dissociation (Norman-Shallice). These are concrete results REE would otherwise have to re-derive or abandon.

---

## R3 -- Genuine REE divergences (the actual novel contribution)

The candidate divergences from R3 of the original commission, evaluated against the R1 mapping:

(a) **Hypothesis-tag / MECH-094 simulation-mode gating on write paths.** *Verdict: GENUINE DIVERGENCE, KEEP-AS-IS.* No existing framework distinguishes "rule applied during simulation/replay" from "rule applied during waking action" with a categorical write-gate. Meta-RL has within-episode adaptation; HRL has option-evaluation; neither has the simulation-vs-action write-gate. This is a real REE contribution.

(b) **Dual-stream affective-vs-discriminative harm channel (SD-010/011) shaping rule-application weights.** *Verdict: GENUINE DIVERGENCE, KEEP-AS-IS.* Existing arbitration literature (Daw 2005, Lee 2014 in Pull 2) wires uncertainty into channel-arbitration; none wires *dissociated affective-vs-discriminative streams* into rule weighting. The closest neighbour is Doll-Simon-Daw 2012 (Pull 2) but that paper argues for soft-mixing rather than dual streams. Real REE contribution.

(c) **MECH-309 logical-necessity claim ("trainers weight rules they do not invent").** *Verdict: GENUINE DIVERGENCE, KEEP-AS-IS, but consider reformulating.* This is not an architectural-component claim; it is a *meta-claim about the relationship between training signal and rule content*. No clean existing-literature analog. The closest neighbours (imitation learning, inverse RL) capture different things. Worth keeping but the claim should be tightened -- currently reads more like a methodological observation than a falsifiable mechanism.

(d) **V_s invalidation + region-staleness machinery (MECH-269/284/287) interacting with rule encoding.** *Verdict: GENUINE DIVERGENCE, KEEP-AS-IS.* Options literature has option-deprecation (initiation-set-shrinkage, termination-update) but no clean analog of REE's *region-level world-staleness signal that propagates to all rules indexed in that region*. The closest neighbour is meta-RL's task-distribution-shift handling (Wang 2018), which is at the per-task level, not the per-region level. Real REE contribution.

**Aggregate R3 verdict.** Four genuine REE divergences (MECH-094, dual-stream affective gating, MECH-309 logical-necessity, V_s invalidation). These are the parts of the rule-apprehension cluster that should anchor REE-native MECH names and would NOT be served by renaming to existing vocabulary. They cluster around four themes: simulation-vs-action write gating, affective modulation of cognition, training-signal/content separation, and substrate-level staleness propagation. None are covered by existing options/HRL/schema/meta-RL literature.

---

## R4 -- Renaming recommendation table

For each REE working term, the recommendation. KEEP-AS-IS = genuinely novel; RENAME = existing-literature term covers cleanly; HYBRID = existing primary + REE-specific suffix.

| REE working term | Recommendation | Rationale |
|---|---|---|
| ARC-062 "top-down rule application" | **HYBRID**: rename to "supervisory attentional override (SAS) for context-conditioned policy" with REE-specific cross-reference | SAS is functionally precise; ARC-062 also has the discriminator/gating-policy implementation that needs to be retained. Hybrid keeps both. |
| ARC-064 "bottom-up rule discovery" | **HYBRID**: rename to "option discovery (HRL) + episodic-RL regularity-extraction" | Two-mechanism account from Botvinick 2019 captures it cleanly. The REE-specific part is the cross-reference to ARC-065 as upstream precondition. |
| ARC-065 "behavioural-diversity-generation pathway" | **HYBRID**: rename to "MaxEnt-RL exploration + structured intrinsic motivation pathway" | MaxEnt-RL + intrinsic-motivation literature covers it; the REE-specific part is the LC-NE-tonic-analog biological grounding. |
| MECH-309 "trainers weight rules they do not invent" | **KEEP-AS-IS**, but reformulate for falsifiability | Genuine REE divergence; no clean existing name. |
| MECH-310 trajectory-clustering primitive | **RENAME** to "successor-representation clustering" or "trajectory-state aggregation" | Direct existing-literature counterpart. |
| MECH-311 cluster-to-label transduction | **RENAME** to "skill discriminator network" or "task-state decoder" | DIAYN's discriminator + OFC task-state literature. |
| MECH-312 dual-channel rule arbitration | **HYBRID**: "contention-scheduling-based controller arbitration" | Dual-mechanism inheritance from schema + RL traditions. |
| MECH-313 stochastic-noise-floor | **RENAME** to "max-entropy policy regularisation (LC-NE-tonic substrate)" | MaxEnt-RL is the cleanest home; biological substrate keeps the link. |
| MECH-314 structured-curiosity-bonus | **HYBRID**: "intrinsic-motivation / epistemic-value bonus (frontopolar substrate)" | Multiple existing names; HYBRID with biological substrate. |
| MECH-316 cross-episode-regularity-extraction | **RENAME** to "episodic-RL / successor-representation learning (CLS-monosynaptic substrate)" | Multiple converging accounts. |
| MECH-317 behavioural-pattern-compression | **RENAME** to "option formation / striatal action-chunking" | Direct counterparts. |
| MECH-318 rule-state-abstraction-substrate | **RENAME or ABSORB** into "meta-RL recurrent task-state representation" | Meta-RL collapse. May be redundant with the latent-stack. |
| MECH-094 simulation-mode write gating (cross-reference) | **KEEP-AS-IS** | Genuine REE divergence (R3). |
| Dual-stream affective rule-weighting (SD-010/011 -> MECH-312) | **KEEP-AS-IS** | Genuine REE divergence (R3). |
| V_s invalidation + region-staleness (MECH-269/284/287 -> rule encoding) | **KEEP-AS-IS** | Genuine REE divergence (R3). |

**Aggregate R4 verdict.** Seven RENAMEs, five HYBRIDs, four KEEP-AS-IS. The KEEP-AS-IS items are the genuine REE novelties. The HYBRIDs preserve REE-specific implementation detail while inheriting existing vocabulary at the function level. The RENAMEs are clean wins -- they bring 20-26 years of literature inheritance with negligible loss of REE-specific content.

---

## R5 -- Sequencing impact on remaining work

### (a) Planned ARC-064 + ARC-065 cluster registration

**Verdict: PROCEED WITH MODIFICATION.** The Pulls 1 and 2 verdicts (PROMOTE-TO-CLUSTER for both ARC-064 and ARC-065, with sub-MECHs) remain *substantively* correct -- they identified architectural components that are real and load-bearing. Pull 4's verdict is that those components have *better names* in existing literature, and the cluster registration in claims.yaml should reflect that.

Concrete modifications:

1. Register ARC-062 / ARC-064 / ARC-065 with the working REE names AND explicit cross-references to the existing-literature equivalents in evidence_quality_notes / source attributions. Don't rename in place -- the original names should remain as REE substrate-mapping anchors.
2. Sub-MECH proposals (MECH-313/314/316/317/318) should similarly carry HYBRID names: REE-specific term + existing-literature cross-reference. This makes the inheritance auditable.
3. Add a new MECH-319 candidate **simulation-mode-rule-write-gating** that explicitly anchors the genuine R3 divergence to ARC-062. This is the part that distinguishes REE from meta-RL canon.
4. The dual-stream-rule-weighting interaction (SD-010/011 -> MECH-312) should be registered as a MECH-312 sub-claim (e.g. MECH-312d *affective-stream-modulation-of-arbitration*) rather than absorbed silently. Its REE-specificity is load-bearing.

### (b) Pull 3 (MECH-312 arbitration) scope

**Verdict: PARTIALLY GATED, SCOPE NARROWED.** Pull 4's R1 found that MECH-312 maps cleanly to two existing mechanisms (Cooper-Shallice contention scheduling + Daw 2005 uncertainty-weighted arbitration). Pull 2's R4 already pre-empted much of the MECH-312 dual-channel-arbitration literature search. So Pull 3 should be substantially narrower than originally scoped:

- Skip the foundational arbitration-literature anchors (Daw 2005, Lee 2014, Doll 2012, Smith-Graybiel 2013/2016) -- already in Pull 2.
- Skip the contention-scheduling tradition anchors (Norman-Shallice 1986, Cooper-Shallice 2000) -- in Pull 4.
- Pull 3's remaining scope: (i) the *dual-stream affective modulation* of arbitration (R3 genuine divergence; needs literature on amygdala-OFC interaction in choice arbitration), (ii) the *simulation-mode write gating* (MECH-094) and how it interacts with arbitration during replay vs waking, (iii) the *V_s-region-staleness* propagation through arbitration weights when rules are tagged stale.

This is a meaningful scope reduction. Pull 3 may not need to be a full lit-pull -- it could be a focused 5-8-paper pull on the genuine R3 divergences, with the rest covered by Pulls 2 and 4 cross-references.

### (c) V3-EXQ-543b experiment design

**Verdict: ADD TWO ARMS.** Pull 4's verdicts surface two additional baseline arms for V3-EXQ-543b that were not in the original Pull 1 R5 ARM_1 / ARM_2 proposal:

1. **ARM_meta-RL baseline**: train the existing latent stack with multi-context RL (no explicit ARC-062 gating, no explicit MECH-318 substrate) and test whether within-episode context-conditioning emerges. This is the Wang 2018 / Duan 2016 RL^2 arm. If it succeeds, ARC-062 + MECH-318 are redundant beyond what meta-RL training produces -- a parsimony win.

2. **ARM_recurrent-distributed-baseline**: the Botvinick-Plaut 2004 minimum-architecture arm. A purely-recurrent network with no explicit hierarchy. This is the floor against which the explicit-cluster claim must be defended.

3. The original ARM_1 (MECH-313 noise-floor only) should use SAC-style entropy regularisation as a training-time objective rather than ad-hoc inference-time temperature -- per Haarnoja 2018 entry's R5 implication.

The expanded V3-EXQ-543b is now a five-arm protocol: ARM_0 baseline / ARM_1 noise-floor-only (SAC-style) / ARM_2 noise-floor + curiosity (MECH-313 + MECH-314) / ARM_3 noise-floor + curiosity + gated_policy (full ARC-062 stack) / ARM_meta-RL / ARM_recurrent-distributed. That is more than V3-EXQ-543b should bear in one experiment; the right move is to split into V3-EXQ-543b (the noise-floor-and-gating sweep) and V3-EXQ-543c (the meta-RL and recurrent-distributed baselines).

---

## What this pull does NOT settle

Items deferred:

1. **The MECH-309 reformulation.** Pull 4 R3 said keep-as-is but reformulate for falsifiability. The reformulation is post-cluster-registration substrate-design work, not literature-resolvable.

2. **The relationship between MECH-318 and the existing latent stack.** Pull 2 R5-deferred Q. Pull 4's meta-RL collapse argument *strengthens* the case for absorbing MECH-318 into the latent stack, but the empirical test (does the latent stack support rule-state decoding under partial observability?) is a substrate-design call, not literature-resolvable.

3. **Whether the four R3 KEEP-AS-IS divergences are really four or whether they cluster.** MECH-094 simulation-gating, dual-stream affective gating, MECH-309 logical-necessity, V_s invalidation -- they could be four separate REE contributions or facets of a single deeper architectural commitment (something like "REE has a different relationship between training signal and rule content than canonical RL does"). Worth examining in a future synthesis pass.

4. **How much existing-literature option-discovery vocabulary REE should adopt for ARC-064 + MECH-316/317.** The R4 RENAME recommendations are conservative -- they preserve REE-specific names. A more aggressive renaming would give cleaner literature inheritance but lose substrate-mapping anchors. The right balance is a governance call.

5. **Whether the R4 HYBRID renaming should be done at cluster registration or in a follow-up pass.** Doing it at registration is cleaner; doing it later avoids renaming pressure during the substrate-design phase. Also a governance call.

6. **The Pfeiffer & Foster 2013 anchor** (deferred from Pull 1 R5). Still not retrieved; not gating.

---

## Aggregate Pull 4 headline

**~80% of REE's rule-apprehension vocabulary maps cleanly to existing options-framework / hierarchical-RL / schema-tradition / meta-RL / MaxEnt-RL literature, with high-confidence translations.** The genuine REE contribution is concentrated in four specific divergences: simulation-mode write-gating (MECH-094), dual-stream affective rule-weighting (SD-010/011 -> MECH-312), the MECH-309 logical-necessity diagnostic, and V_s invalidation propagating to rule encoding. These should KEEP-AS-IS. The rest of the cluster vocabulary should be HYBRID-renamed (REE term + literature cross-reference) or RENAMED outright.

The cluster registration plan from Pulls 1 and 2 remains substantively correct. The architectural components are real and load-bearing. Pull 4's contribution is to add literature inheritance on top, sharpen R3 to four specific genuine novelties, and recommend a five-arm V3-EXQ-543b that includes the meta-RL and recurrent-distributed baselines as parsimony tests.

---

## Per-paper summary index

| Entry | DOI | Lineage | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|---|
| Sutton, Precup & Singh 1999 | [10.1016/S0004-3702(99)00052-1](https://doi.org/10.1016/S0004-3702(99)00052-1) | Options framework | R1, R2 | supports | 0.88 |
| Bacon, Harb & Precup 2017 | [10.1609/aaai.v31i1.10916](https://doi.org/10.1609/aaai.v31i1.10916) | Options framework | R1, R2, R5 | supports | 0.82 |
| Eysenbach et al. 2018 (DIAYN) | [10.48550/arXiv.1802.06070](https://doi.org/10.48550/arXiv.1802.06070) | Options/MaxEnt | R1, R2, R5 | supports | 0.78 |
| Botvinick, Niv & Barto 2009 | [10.1016/j.cognition.2008.08.011](https://doi.org/10.1016/j.cognition.2008.08.011) | HRL + neural | R1, R2, R4 | supports | 0.82 |
| Solway et al. 2014 | [10.1371/journal.pcbi.1003779](https://doi.org/10.1371/journal.pcbi.1003779) | HRL + behaviour | R2, R4 | supports | 0.79 |
| Cooper & Shallice 2000 | [10.1080/026432900380427](https://doi.org/10.1080/026432900380427) | Schema tradition | R1, R2, R4 | mixed | 0.72 |
| Botvinick & Plaut 2004 | [10.1037/0033-295X.111.2.395](https://doi.org/10.1037/0033-295X.111.2.395) | Schema tradition (counter) | R3, R5 | weakens | 0.74 |
| Norman & Shallice 1986 | [10.1007/978-1-4757-0629-1_1](https://doi.org/10.1007/978-1-4757-0629-1_1) | Schema tradition (foundational) | R1, R2, R4 | supports | 0.74 |
| Wang et al. 2018 | [10.1038/s41593-018-0147-8](https://doi.org/10.1038/s41593-018-0147-8) | Meta-RL + neural | R1, R3, R4, R5 | supports | 0.80 |
| Duan et al. 2016 (RL^2) | [10.48550/arXiv.1611.02779](https://doi.org/10.48550/arXiv.1611.02779) | Meta-RL ML | R2, R5 | supports | 0.74 |
| Botvinick et al. 2019 | [10.1016/j.tics.2019.02.006](https://doi.org/10.1016/j.tics.2019.02.006) | Meta-RL synthesis | R1, R3, R5 | supports | 0.78 |
| Haarnoja et al. 2018 (SAC) | [10.48550/arXiv.1801.01290](https://doi.org/10.48550/arXiv.1801.01290) | MaxEnt-RL | R1, R2, R4, R5 | supports | 0.80 |

**Aggregate Pull 4 lit_conf** for the cluster (post-indexer): expected to land in the 0.78-0.82 range across ARC-062, ARC-064, ARC-065, MECH-312, MECH-313, MECH-316, MECH-317, MECH-318. One mixed-direction entry (Cooper-Shallice 2000) and one weakens-direction entry (Botvinick-Plaut 2004) provide useful tension; the rest are supports-direction.
