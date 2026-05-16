---
nav_exclude: true
---

<!-- version: 2026-05-16.1 -->
<!-- author: claude-sonnet-4-6, session replay-dev-analysis-2026-05-16T125804Z -->

# Replay as Developmental Restructuring: Analysis and Proposals

**Cross-references:** [`developmental_needs_register.md`](developmental_needs_register.md) | [`developmental_curriculum.md`](developmental_curriculum.md) | [`developmental_metrics.md`](developmental_metrics.md) | [`hippocampal_systems.md`](hippocampal_systems.md) | [`sleep.md`](sleep.md) | [`sd_017_sleep_phase_architecture.md`](sd_017_sleep_phase_architecture.md) | [`sleep_aggregation_cluster.md`](sleep_aggregation_cluster.md) | [`residue_geometry.md`](residue_geometry.md) | [`infant_substrate_expansion.md`](infant_substrate_expansion.md)

**Date:** 2026-05-16  
**Status:** Analysis document — not a registered claim. Proposals feed into experiment design and register maintenance.

---

## Framing

Replay is not memory consolidation with the episodic buffering as source material.
It is **developmental restructuring**: a process that selects from stored experience to reshape
the space of futures the agent can access.

From this vantage, the critical questions are not:
- Did the agent remember the right things?
- Did loss decrease after sleep?

But rather:
- Did replay expand the option space that is available at the next waking cycle?
- Did replay differentiate the contexts that the agent can act in?
- Did replay integrate moral residue without either amplifying it into paralysis or
  erasing it into forgetting?

These are different questions, requiring different metrics, different scheduling policies,
and different failure signatures at each developmental stage.

---

## Part 1: Current Replay Architecture Map

### 1.1 Replay Pathways Currently Implemented

| Mechanism | Claim | Phase | Direction | Status | V3 evidence |
|---|---|---|---|---|---|
| Waking quiescent replay | MECH-092 | Waking rest | Hippocampus-internal | Implemented (V3 prereq) | EXQ-136 FAIL (pair ablation); see §1.3 |
| SWS-analog schema consolidation | SD-017 | Sleep SWS | Hip → Cortex | Methods validated (EXQ-265 PASS, EXQ-265a PASS); not yet functionally tested | EXQ-242 FAIL (ablation study); EXQ-265a PASS (phase 2 methods) |
| REM-analog causal attribution | SD-017 | Sleep REM | Cortex → Hip (fill) | Methods validated; functional test pending | Same as above |
| Balanced replay (harm + benefit) | MECH-203 | Any | Mixed | Implemented and validated | EXQ-256 PASS |
| Surprise-gated replay | MECH-205 | Any | RPE-biased | Implemented after iterations | EXQ-258b PASS (after EXQ-258/258a FAIL) |
| Reverse replay diversity | MECH-165 | Sleep NREM | Reverse + non-dominant | Conflicting results | EXQ-244 FAIL (3/3), EXQ-244a PASS (0/1) |
| Sleep aggregation cluster | MECH-272/273/275/285 | Sleep cycle | All | Designed; NOT yet implemented | — |
| Staleness-weighted replay priority | MECH-285 | Sleep | Staleness-proportional | Designed; NOT yet implemented | — |

### 1.2 What Replay Currently Does (and Does Not Do)

**What the architecture guarantees (from hippocampal_systems.md):**
- Replay samples alternative traversals over a FIXED residue field — it does not erase or flatten φ(z)
- Replay does not directly change policy
- Replay explores counterfactual paths, not counterfactual values
- Replay is exploratory, not corrective
- Residue integration and curvature updates occur SEPARATELY (offline sleep consolidation)

**What the current implementation does NOT yet do:**
- Stage-aware replay scheduling (no developmental stage awareness)
- Coverage-maximising replay during infancy (only RPE-priority or random)
- Staleness-weighted seed selection (MECH-285 not implemented)
- Cross-episode Bayesian aggregation (MECH-275 not implemented)
- Self-model correction during sleep (MECH-273 not implemented)
- State-gated routing between anchor and probe channels (MECH-272 not implemented)

### 1.3 Replay Experiment PASS/FAIL Pattern Summary

**FAIL cluster (concerning):**

| Experiment | Claim | Outcome | Notes |
|---|---|---|---|
| EXQ-127 | MECH-030 sleep consolidation pair | FAIL | Basic sleep consolidation pairing failed |
| EXQ-136 | MECH-092 quiescent replay pair | FAIL | Quiescent replay pair ablation failed |
| EXQ-242 | SD-017 sleep phase ablation | FAIL | Sleep phase ablation not discriminative |
| EXQ-385 | INV-049 offline consolidation necessity | FAIL | Critical: general law of offline necessity |
| EXQ-385a | INV-049 offline consolidation necessity | FAIL (3/3) | Replication failure — persistent concern |
| EXQ-430 | INV-010 offline integration necessity | FAIL | Second offline necessity invariant failed |
| EXQ-244 | MECH-165 reverse replay diversity | FAIL (3/3) | Diversity was not discriminative |
| EXQ-214 | ARC-039 entorhinal consolidation | FAIL | Entorhinal consolidation not validated |
| EXQ-240/240a | ARC-038 waking consolidation | FAIL, FAIL | Schema assimilation failing consistently |

**PASS cluster (stable):**

| Experiment | Claim | Outcome | Notes |
|---|---|---|---|
| EXQ-150 | Q-005 sleep anneal | PASS | Sleep annealing does work |
| EXQ-244a | MECH-165 replay diversity validation | PASS | Diversity validation passed (after FAIL iterations) |
| EXQ-256 | MECH-203 balanced replay | PASS | Harm + benefit balance in replay works |
| EXQ-258b | MECH-205 surprise-gated replay | PASS | After iterating through two FAILs |
| EXQ-265 | SD-017 methods validation (phase 1) | PASS | Phase infrastructure works |
| EXQ-265a | SD-017 methods validation (phase 2) | PASS | Phase 2 infrastructure confirmed |
| EXQ-432 | SD-014 replay gate prioritization | PASS | Replay gate prioritization works |

**Pattern interpretation:**
The pair/ablation designs (EXQ-127, EXQ-136, EXQ-242, EXQ-385, EXQ-385a, EXQ-430) are failing
consistently while the mechanism-specific probes (EXQ-256, EXQ-258b, EXQ-265) are passing.
This suggests the underlying replay mechanisms exist and can be isolated, but the system-level
benefit of offline integration is not yet robustly measurable. Most likely reason: the
current substrate does not generate enough transition diversity during waking for sleep to
show a discriminative advantage. Sleep can only reorganize what waking produced.

---

## Part 2: Literature Evidence Mapping

### 2.1 Sources from developmental_metrics.md (existing lit-pulls 2026-05-16)

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Shin et al. (Nature Commun 2025) | Post-task replay biased toward RPE signals; RPE-biased replay predicts subsequent behaviour | Replay quality = RPE-bias selection, not recency or novelty; consolidation gate needs RPE-priority score | DEV-NEED-007 | INV-056, ARC-048 | High | refines existing claim (MECH-205, MECH-285) |
| Joo & Frank (Science 2024) | SWR incidence increases with novelty and harm salience; salient trials over-represented in offline replay | Harm salience is a natural SWR-gating factor; use harm-salience-weighted replay priority | DEV-NEED-007, DEV-NEED-025 | INV-056, MECH-159 | High | refines existing claim (MECH-285) |

### 2.2 Sources from infant_substrate_expansion.md lit-pulls (2026-05-16)

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Ventura et al. (2024) CA3 flexibility | Environmental enrichment → greater CA3 spatial tuning and contextual remapping; flat environments → poor representational differentiation | Environment structure during infant exploration determines downstream hippocampal representational flexibility and thus replay utility | DEV-NEED-003, DEV-NEED-007 | ARC-065, ARC-007 | 0.65 | suggests implementation metric (replay_coverage_per_zone) |
| Parker-Holder et al. (2020 NeurIPS DvD) | Apparent diversity (pairwise distance) != effective diversity (volume); population can be spread but degenerate | Current V3 replay diversity metrics may be measuring apparent diversity; need volumetric trajectory coverage | DEV-NEED-005, DEV-NEED-007 | Q-046, ARC-065 | 0.78 | refines existing claim (replay_diversity_index must use volumetric metric) |
| Doupe & Kuhl (1999 Annu Rev Neurosci) | BG-driven motor variability necessary for repertoire formation; pharmacological silencing = monostrategy | If waking exploration is monostrategy, replay has only one trajectory class to replay; replay cannot introduce diversity that was never experienced | DEV-NEED-001, DEV-NEED-005 | ARC-065, MECH-309 | 0.78 | supports existing claim (replay diversity is bounded by waking diversity) |
| Griffin et al. (2026) Brain Sci | Phase 1 (reward-free Hebbian) builds action-perception assemblies; Phase 2 (dopamine) consolidates subset; Phase 1 MUST precede Phase 2 | Two-phase infant design: reward-free exploration phase must precede replay-consolidated goal training | DEV-NEED-001, DEV-NEED-007 | ARC-065, INV-073 | 0.76 | suggests missing claim (Phase 0 reward-free = replay has nothing to collapse on yet) |

### 2.3 Sources from lit-pull agents (2026-05-16 parallel searches)

#### 2.3a Hippocampal Replay Development, Sleep/Infant, Diversity, Trauma

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Buhl & Buzsaki (2005 Neuroscience 132:843, PMID 16039793) | SWRs with high-frequency ripple component do not emerge until end of postnatal week 2 (P12-P20 rat); early "proto-SWR" sharp waves lack the ripple component; emergence coincides with GABA developmental switch | Replay-capable consolidation requires a substrate that matures gradually. A cold-start AI system cannot be expected to show generalizing replay before its gating/inhibitory architecture is mature. Grounds DEV-NEED-029 | DEV-NEED-007, DEV-NEED-029 | SD-017, MECH-092, INV-055 | High | supports existing claim; suggests missing claim (replay hardware maturation gate) |
| Noguchi, Matsumoto & Ikegaya (2023 J Neurosci 43:6126, PMID 37400254) | Intracellular Vm dynamics during SWRs reach adult-like precision only by P30 in mice; before this, prolonged depolarizations without the pre/post-SWR inhibitory flanking that enables temporally precise sequence compression | Replay quality (sequence fidelity, compression) matures on a separate timeline from replay occurrence. Early replay may be noisy and poorly compressed — a distinct infant property, not a failure | DEV-NEED-007 | MECH-092, SD-017, INV-055 | High | suggests missing claim (replay sequence fidelity as developmental metric) |
| Seehagen, Konrad, Herbert & Schneider (2015 PNAS 112:1625) | Infants aged 6 and 12 months who napped within 4 hours of declarative learning retained at 4h and 24h delays; non-nappers failed. Single nap >= 30 min sufficient. First experimental causal demonstration in year-1 infants | Offline integration in infancy is causal and time-sensitive. Consolidation benefit degrades rapidly if offline phase delayed past ~4 hours. Constrains when replay should be triggered after experience | DEV-NEED-007 | INV-010, ARC-011, SD-017 | High | supports existing claim; suggests implementation constraint (replay trigger window) |
| Horváth, Plunkett & Csibra (2016 Current Biology 27:R745) | Neonates enter sleep via REM (not NREM); REM/NREM ratio inverted (50-80% REM in newborns vs ~20% adults). Sleep spindles — NREM marker of hippocampal-to-neocortical transfer — absent at birth and emerge in first months | Developmental arc of sleep architecture maps onto consolidation capability. Infant sleep is REM-dominant; the SWS-analog pass may be minimal in infancy and become load-bearing only as spindles emerge | DEV-NEED-007 | SD-017, MECH-092, INV-055 | Medium-High | suggests missing claim (stage-indexed SWS:REM ratio) |
| Stickgold & Walker (2013 Nature Neurosci 16:139, PMID 23354387) | Sleep performs "memory triage": selectively preserving schema-consistent, emotionally salient, or future-relevant traces while discarding mundane detail. Outcome is compressed generalisation, not faithful storage | Replay should not aim for lossless replication. The selective/triage function is a feature: sleep builds compressed, generalised representations. Validates replay as filter, not recorder | DEV-NEED-007 | MECH-030, SD-017 | High | supports existing claim (sleep is restructuring, not mere consolidation) |
| Werne, Chadwick & Series (2026 PLOS Comput Biol DOI:10.1371/journal.pcbi.1013251) | Computational model: sleep replay inherently increases fear generalisation even when original memory is accurate; multi-context extinction suppresses renewal more than single-context. Sleep-dependent SHY prevents fear sensitization; disruption causes pathological accumulation | Consolidation via replay is not neutral — it systematically broadens associations. Replay must be constrained (hypothesis-tagged, per MECH-094) to prevent harm-valence overgeneralisation. Disrupted offline phase → fear consolidates unopposed | DEV-NEED-007, DEV-NEED-018 | MECH-094, MECH-124, MECH-018 | Medium | supports existing claim (MECH-094 tag necessity); suggests experiment (tag-loss replay vs tagged replay) |
| Schapiro et al. (2017 Phil Trans R Soc B 372:20160049, PMID 27872368) | Hippocampal replay interleaves episodic events to transfer structured statistical regularities to neocortex via CLS. Dense, diverse replay required; biased or sparse replay fails to extract cross-episode generalisation | Diverse replay (covering many past states, not just recent or high-reward) is necessary for learning transferable ethical principles rather than situation-specific rules. Directly grounds play+real interleaved replay proposal | DEV-NEED-007, DEV-NEED-011 | ARC-011, MECH-194, MECH-195, INV-060 | High | supports existing claim; suggests experiment (EXQ-IDEV-002 interleaved replay) |
| Roscow, Chua, Costa, Jones & Lepora (2021 Trends Neurosci 44:816, PMID 34481635) | Biological replay prioritizes novelty, reward-boundary events, and reverse sequences — NOT uniform random sampling. This prioritisation substantially improves generalisation over uniform replay | Replay scheduler should weight harm-boundary events and surprising transitions. Uniform replay is a baseline. Supports MECH-205 (surprise-gated) + MECH-285 (staleness-priority) design | DEV-NEED-007 | MECH-205, MECH-285, MECH-165 | High | refines existing claim (priority design is neurobiologically grounded) |
| Cai, Mednick et al. (2009 PNAS 106:10130, PMID 19506253) | REM sleep (not NREM or quiet wakefulness) specifically improves Remote Associates Test (creative/relational generalisation). REM primes associative networks enabling cross-domain transfer | Different sleep stages contribute qualitatively different types of generalisation. SD-017's SWS/REM split should produce different generalisation effects — schema formation (SWS) vs relational binding (REM) | DEV-NEED-009, DEV-NEED-011 | SD-017, MECH-030 | High | refines existing claim (SWS/REM functional specialisation); suggests experiment (SWS-only vs REM-only on strategy transfer) |
| Pace-Schott, Seo & Bottary (2022 Neurobiology of Stress 17, PMID 36545012) | Post-extinction REM sleep predicts superior extinction recall. Post-trauma REM fragmentation in acute phase (days-weeks) = strongest PTSD predictor. Hyperarousal disrupts REM-dependent safety-memory consolidation; fear consolidates unopposed | Disrupted offline phases after aversive events fail to consolidate extinction and over-consolidate fear. MECH-094 tag loss = PTSD mechanism is neurobiologically anchored here | DEV-NEED-007, DEV-NEED-018 | MECH-094, MECH-124, ARC-011 | High | supports existing claim (MECH-094 tag loss clinical grounding) |

#### 2.3b Offline RL Diversity, Replay Planning, Developmental Replay, Monostrategy

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Zha et al. (2024 arXiv:2410.20487) | Diversity-based replay (DBER) outperforms prioritised replay (PER) in sparse-reward environments; diverse trajectory sampling yields better policy coverage across MuJoCo, Atari, and vision navigation | In infant-phase agents with sparse reward signals, diversity-first replay outperforms error-prioritised replay at bootstrapping generalisable behaviour. Grounds coverage-priority infant policy (§6.2) | DEV-NEED-005, DEV-NEED-007 | ARC-065, MECH-285 | High | supports existing claim; grounds stage-indexed scheduler |
| Adaptive Replay Buffer (2024 arXiv:2512.10510) | Large buffers improve diversity but introduce staleness bias as policy drifts; on-policyness weighting bridges offline richness and online freshness | Developmental agent faces same staleness problem; on-policyness metric is a tractable proxy for "how relevant is this memory now" — relevant to MECH-285 staleness mechanism | DEV-NEED-007 | MECH-285 | Medium | refines existing claim (staleness metric design) |
| Shin, Tang & Jadhav (2019 Neuron 104(6), PMID 31677957) | Directional shift in replay: early learning dominated by reverse (retrospective) replay for credit assignment; late learning dominated by forward (prospective) replay for planning. PFC reads out prospective sequences to guide choices | Developmental AI should transition replay use from consolidation-dominant (retrospective) to planning-dominant (prospective) as competence increases. This is a staging signal, not a parameter | DEV-NEED-007, DEV-NEED-008 | ARC-007, MECH-030, SD-017 | High | suggests missing claim (prospective vs retrospective replay scheduling across stages) |
| Ólafsdóttir et al. (2018 PNAS 115(10), PMID 29483254) | Prospective replay is spatially focused near current position and behaviourally predictive; retrospective replay is more diffuse. Two functionally dissociable modes. Disruption of prospective events impairs upcoming choice accuracy | Two distinct replay modes: prospective (planning at decision points) and retrospective (consolidation). Stage differences: infancy = retrospective dominant; adult = prospective dominant | DEV-NEED-007, DEV-NEED-019 | ARC-007, MECH-030, ARC-018 | High | suggests missing claim (dual-mode replay scheduling; prospective mode for planning gate) |
| Foster & Wilson (2006 Nature 440:680); Karlsson & Frank (2009) | Awake forward replay during pauses at decision points represents upcoming trajectories; remote replay of never-directly-visited paths occurs — combinatorial simulation beyond simple memory playback | Replay is generative, not only reproductive: it can compose novel paths. This property is necessary for planning and supports the MECH-092 waking quiescent replay role in prospective simulation | DEV-NEED-007 | MECH-092, ARC-007, ARC-018 | High | supports existing claim (ARC-018 prospective rollout grounding) |
| Vöröslakos et al. (2023 J Neurosci 43:6126, PMID 37400254) | SWR-associated membrane potential dynamics mature by P30 in rodents; before P30, ripples occur but sequences are poorly ordered (insufficient inhibitory flanking) | Stage where replay infrastructure exists but sequence fidelity is low = infant phase. Disordered replay early is expected, not pathological. INV-049 FAILs may partly reflect this — substrate not yet mature | DEV-NEED-007, DEV-NEED-029 | SD-017, MECH-092, INV-049 | High | refines existing claim; suggests why INV-049 FAILs are substrate, not theory failures |
| Peiffer et al. (2020 Sci Rep 10:9979, PMID 32561803) | Children (7-12y) show better sleep-dependent declarative consolidation than adults; 25-35% SWS vs 15-20% adults. Hippocampal-to-prefrontal transfer mechanism more efficient early in development | Peak replay bandwidth (SWA proportion) occurs in middle childhood, not infancy. More offline replay during childhood produces disproportionate consolidation gain — supports childhood's higher strategy-abstraction role | DEV-NEED-009, DEV-NEED-011 | ARC-011, SD-017, INV-060 | High | supports existing claim; suggests childhood sleep:wake ratio > infancy for strategy abstraction |
| Lu et al. (2019 Nat Commun 10:1779) | Without MEC inputs, CA1 replay becomes rigid/stereotyped (less diverse, same sequences repeatedly). MEC lesion blocks reversal learning. Diversity loss = flexibility loss | Direct mechanistic evidence: replay diversity is upstream of behavioural flexibility. Homogenised replay buffer = monostrategy-locked agent. Grounds MECH-124 prevention as primary gate | DEV-NEED-005, DEV-NEED-007 | MECH-124, MECH-285, MECH-165 | High | supports existing claim; grounds monostrategy_prevention_score as mandatory metric |
| Ego-Stengel & Wilson (2010 Hippocampus 20:1, PMID 19816984) | Disrupting SWRs during rest impairs subsequent spatial learning; disruption destabilises acquired strategy (behavioural noise rather than stable strategy) | SWR-mediated replay necessary for both learning AND stabilising what has been learned. Insufficient replay = noise; biased replay = lock-in. Directly grounds SD-017 necessity | DEV-NEED-007 | MECH-092, SD-017, INV-049 | High | supports existing claim (SD-017 necessity) |

---

## Part 3: Does Replay Currently Preserve, Increase, or Collapse Diversity?

### 3.1 Architectural Intent vs Implementation Reality

**Intended:** The architecture specifies replay as "exploratory, not corrective" and guarantees
replay does not flatten φ(z). The constraint is correct.

**Current implementation risk:**
1. **Collapse toward salience**: Without MECH-285 (staleness-weighted priority), replay defaults
   to RPE-priority or recency. Both select against low-salience, low-RPE trajectories —
   exactly the content that diversifies the option space.
2. **Cold-start zero-differential**: DEV-NEED-029 / EXQ-573 confirmed that diversity mechanisms
   produce zero differential on cold-start substrate. During infancy, the ResidueField, EWMA,
   and E3 score variance are all near-zero — so every replay policy produces the same result.
3. **Content poverty from infant compression**: The six compressions identified in
   infant_substrate_expansion.md (§2) mean the infant replay buffer contains only termination-
   adjacent and unremarkable mid-episode sequences. Sleep cannot reorganize content that was
   never created.
4. **Context undifferentiation (MECH-153 failure)**: Without SD-017 properly functional,
   context cosine_sim → 1.0. Sleep cannot improve context attribution if all contexts look
   the same.
5. **Forward-only replay bias**: MECH-165 reverse replay is intended to extend the effective
   reach of replay into non-dominant trajectories. Its FAIL pattern (EXQ-244 FAIL 3/3)
   before a later validation pass suggests it is fragile or substrate-dependent.

### 3.2 Assessment Per Function

| Function | Current state | Evidence | Assessment |
|---|---|---|---|
| Preserves diversity | Architecture guarantees (no φ-erasure) | Correct in design | Structurally preserved |
| Increases diversity | Not yet demonstrated | EXQ-385/385a FAIL; INV-049 twice failed | Not yet demonstrated; substrate gap |
| Collapses diversity | Risk when salience-priority dominates | MECH-124 failure mode; cold-start problem | Real risk, not yet a confirmed failure |
| Stabilises residue | Shallow; consolidation delta low | DEV-NEED-007 metric not yet measured | Partially working; full cluster not implemented |
| Improves developmental transitions | Not yet testable | No developmental ablation exists | Gap — no experiment tests this |
| Supports infant-to-child progression | Not yet testable | No warm-start gate exists | Gap — DEV-NEED-029 is PROPOSED |
| Supports play-to-real transfer | Predicted by Schapiro 2017 | No experiment; MECH-203 balanced replay passed | Promising architecture; untested |

---

## Part 4: Replay Bottlenecks

### 4.1 Structural Bottlenecks

**B1. Content poverty from infant substrate compression**

The infant substrate (CausalGridWorldV2 with default parameters) generates a replay buffer
dominated by: (a) termination-adjacent sequences (high salience, low diversity), and
(b) unremarkable mid-episode sequences (low salience, high frequency). This is not a replay
scheduler failure — the content was never created during waking.

- Root cause: binary harm, homogeneous geography, uniform action consequences
- Fix: graduated harm zones, microhabitat zones, multi-resource heterogeneity (infant_substrate_expansion.md §5)

**B2. No developmental stage awareness in replay scheduler**

The same replay policy (RPE-priority + recency) runs at every developmental stage.
During infancy, when the agent needs COVERAGE, RPE-priority selects against exploration.
During adulthood, when the agent needs INTEGRATION, coverage-priority may replay
irrelevant early experiences.

- Root cause: no curriculum parameter governing replay scheduling per stage
- Fix: stage-indexed replay scheduler (see §6.1)

**B3. Cold-start warm-start failure (DEV-NEED-029)**

MECH-313 (noise floor), MECH-314a (novelty bias), and MECH-320 (tonic vigor) all require
warm substrate. But the infant stage IS cold-start. The mechanisms designed to prevent
monostrategy cannot activate until the substrate is warm, which requires passing through
infancy first — a bootstrapping problem.

- Root cause: diversity mechanisms designed for post-infant agent
- Fix: v_t_floor as cold-start proxy for MECH-320; coverage-maximising replay as bootstrap for MECH-285

**B4. Replay homogenisation risk (MECH-124)**

Replay dominated by high-salience trajectories (high harm, high RPE) amplifies the residue
in those regions while neglecting low-salience trajectories that represent viable alternatives.
Over many sleep cycles, the option space contracts toward harm-avoidance strategies.

- Root cause: salience/RPE priority without staleness correction or coverage floor
- Fix: MECH-285 staleness-weighted priority; coverage floor constraint on replay scheduler

**B5. Context undifferentiation blocking attribution**

SD-017 is the minimal infrastructure that makes MECH-092 useful. But SD-017's functional
validation is incomplete (EXQ-242 FAIL, EXQ-265 method-PASS but not functionally tested).
Without stable context attractors, replay cannot route experiences to the right context slots,
and consolidation cannot produce the differentiated attribution maps that E3 needs.

- Root cause: SD-017 infrastructure implemented as methods but not functionally validated
- Fix: SD-017 functional validation experiments (context discrimination before/after sleep)

**B6. No replay coverage floor during infancy**

The residue_consolidation_delta metric (DEV-NEED-007) specifies that sleep should produce
positive delta (increasing residue coverage). But without a lower bound on coverage fraction
of replayed content, a replay scheduler can satisfy other criteria (RPE priority) while
never expanding residue geography.

- Root cause: no explicit coverage floor constraint in replay scheduler
- Fix: `replay_coverage_floor: float` parameter specifying minimum fraction of replayed
  episodes that must come from distinct zones not recently replayed

### 4.2 Replay Overfitting

**Signature:** Replay selects repeatedly from the same high-salience episodes; the same
trajectories are consolidated many times while the rest of the buffer is never touched.

**Mechanism:** RPE-biased replay without staleness correction → same high-RPE episodes
are replayed each cycle → residue amplified in those regions → those regions appear
even more salient → positive feedback loop.

**Detection:** replay_diversity_index < 0.15 AND replay_RPE_priority_score > 0.6 simultaneously.

**Prevention:** MECH-285 staleness decay + coverage floor.

### 4.3 Replay-Induced Monostrategy

**Signature:** After many sleep cycles, agent's trajectory library collapses to one or two
dominant strategy classes.

**Mechanism:** High-RPE replay reinforces harm-avoidance trajectories. Alternative strategies
(with lower RPE, lower residue, but genuine option value) are never replayed and gradually
decay from effective policy influence.

**Detection:** traj_volume_estimate declining across sleep cycles; action_class_coverage
declining post-sleep.

**This is MECH-124** (consolidation-mediated option-space contraction, Walker PTSD analog).

### 4.4 Replay Failure to Integrate Residue

**Signature:** post_sleep_z_goal_retention < 0.85 AND residue_consolidation_delta ≈ 0.

**Mechanism:** Replay runs but does not write to residue geometry (correct by design —
residue updates are separate). But the separate residue integration step may not be
triggered, or may integrate into already-saturated regions, or may fail to assign content
to the correct context slot (B5).

**Detection:** residue_curvature_index flat before and after sleep.

### 4.5 Replay Failure to Expand Trajectory Diversity

**Signature:** traj_pairwise_cosine_mean and traj_volume_estimate do not increase across
infant stage despite many sleep cycles.

**Mechanism:** Sleep can only recombine what waking produced (Doupe & Kuhl 1999). If waking
generates only one trajectory class, sleep cannot introduce new ones.

**Detection:** traj_volume_estimate plateau for > 500 episodes at infant stage
AND action_class_coverage ≤ 2.

**Resolution:** The fix is the infant substrate (§4.1/B1), not the replay scheduler.

---

## Part 5: Replay Metrics Proposals

### 5.1 Replay Diversity Metrics

| Metric | Formula | Stage | Threshold | Readiness |
|---|---|---|---|---|
| `replay_diversity_index` | Fraction of replayed episodes from distinct zones vs dominant zone | Infant | > 0.4 | TelemetryRequired |
| `replay_volumetric_coverage` | log-det of trajectory kernel matrix over replayed episodes (DvD-style; Parker-Holder 2020) | All | Increasing trend | TelemetryRequired |
| `replay_zone_coverage_fraction` | Fraction of defined zones represented in last sleep cycle's replay | Infant | > 0.6 | TelemetryRequired |
| `replay_context_class_count` | Number of distinct context attractors sampled during last sleep cycle | Childhood+ | > 2 | TelemetryRequired |

### 5.2 Replay Novelty Metrics

| Metric | Formula | Stage | Threshold | Readiness |
|---|---|---|---|---|
| `replay_RPE_priority_score` | Fraction of replayed episodes with RPE > mean_RPE | Adult | > 0.6 | TelemetryRequired |
| `replay_staleness_score` | Mean staleness weight of replayed seeds (from StalenessAccumulator) | All | Increasing over cycles | TelemetryRequired (MECH-285) |
| `replay_low_salience_fraction` | Fraction of replayed episodes with RPE < 25th percentile | Infancy | > 0.3 | TelemetryRequired |
| `replay_novel_trajectory_fraction` | Fraction of replayed trajectories that differ from top-5 most-replayed | All | > 0.5 | TelemetryRequired |

### 5.3 Replay Coverage Metrics

| Metric | Formula | Stage | Threshold | Readiness |
|---|---|---|---|---|
| `replay_residue_coverage_delta` | Change in residue_coverage_pct after each sleep cycle | Infant | > 0 | TelemetryRequired |
| `replay_latent_breadth` | Fraction of z_world space sampled by replayed episodes | All | Increasing during infant | TelemetryRequired |
| `replay_buffer_utilisation` | Fraction of unique episodes in replay buffer sampled at least once per K cycles | All | > 0.4 | TelemetryRequired |
| `replay_coverage_floor_adherence` | Is the coverage_floor constraint satisfied? | Infant | Boolean | SubstrateReady (post-implementation) |

### 5.4 Replay-Stage Metrics

| Metric | Formula | Stage | Threshold | Readiness |
|---|---|---|---|---|
| `post_sleep_z_goal_retention` | z_goal.norm() ratio before/after sleep integration | Infant | > 0.85 | TelemetryRequired |
| `post_sleep_context_differentiation` | Decrease in context cosine_sim after sleep cycle | Childhood | > 0.05 per cycle | TelemetryRequired |
| `post_sleep_trajectory_diversity_delta` | Change in traj_volume_estimate after sleep | Childhood | Positive | TelemetryRequired |
| `post_sleep_residue_integration_efficiency` | Change in residue_curvature_index / replay_steps | Adult | Positive | TelemetryRequired |
| `sleep_wake_ratio` | Steps in offline integration / steps in waking episode | Infant | > 0.10 | TelemetryRequired |

### 5.5 Replay Restructuring Metrics

| Metric | Formula | Stage | Threshold | Readiness |
|---|---|---|---|---|
| `pre_post_traj_volume_ratio` | traj_volume_estimate post-sleep / pre-sleep | All | > 1.0 (sleep expands) | TelemetryRequired |
| `monostrategy_prevention_score` | Is MECH-124 failure mode absent? action_class_coverage post-sleep >= pre-sleep | All | >= 1.0 | TelemetryRequired |
| `residue_integration_without_amplification` | Does residue integrate toward equilibrium (not diverge)? | Post-harm | delta toward mean, not away | TelemetryRequired |
| `option_space_contraction_rate` | Rate of decline in viable trajectory classes across sleep cycles | All | < 0 (not declining) | TelemetryRequired |

---

## Part 6: Stage-Differentiated Replay Scheduling

### 6.1 Core Proposal: Stage-Indexed Replay Scheduler

The replay scheduler needs a `dev_stage` parameter that modifies selection policy:

```python
class StageAwareReplayScheduler:
    def select(self, buffer, dev_stage, staleness_map=None) -> List[Episode]:
        if dev_stage == "infant":
            return self._coverage_priority(buffer)
        elif dev_stage == "childhood":
            return self._interleaved_priority(buffer)
        elif dev_stage == "adult":
            return self._rpe_and_staleness_priority(buffer, staleness_map)
```

### 6.2 Infancy: Coverage and Valence-Map Formation

**Goal:** Maximise spatial/latent coverage to build valence geography for sleep to consolidate.

**Replay policy:** Coverage-maximising with harm-salience floor.

| Parameter | Value | Rationale |
|---|---|---|
| Coverage fraction minimum | 0.6 of zones | All zones must be sampled (not just hazard-adjacent) |
| RPE priority weight | 0.2 (low) | High RPE = termination trajectories; these dominate infant buffer and should not monopolise replay |
| Low-salience fraction minimum | 0.3 | Stickgold & Walker 2005: sleep finds hidden structure in weak associations |
| Prospective vs retrospective | Retrospective dominant | Infancy is about understanding what happened; planning comes later |
| Sleep:wake ratio | > 0.10 (frequent offline) | Biological: high infant sleep demand (70% REM in neonates); rapid consolidation |

**Failure signature:** replay_zone_coverage_fraction < 0.3 = infant replay is dominating on
hazard zone; valence geography is one-sided (only harm, no benefit).

**Key insight from Gómez et al. (2006):** A single nap was sufficient for 15-month-olds to
generalise an abstract rule. This means infant replay efficiency is high when content is
available — the failure mode is content poverty, not replay mechanism failure. The substrate
fix (infant_substrate_expansion.md) is the primary intervention; replay scheduling is secondary.

### 6.3 Childhood: Strategy Abstraction and Play-to-Real Transfer

**Goal:** Bind the shared strategy structure between play and real episodes (Schapiro 2017).
Prevent synthetic magnitude calibration from consolidating.

**Replay policy:** Interleaved play + real episodes; strategy-structure-biased selection.

| Parameter | Value | Rationale |
|---|---|---|
| Play:real interleaving ratio | 1:1 minimum | Schapiro 2017: sleep binds shared structure across episode types |
| RPE priority weight | 0.4 (moderate) | Some salience selection; not dominant |
| Coverage fraction minimum | 0.5 | Maintain coverage; childhood can afford more RPE selection than infancy |
| Post-sleep target | post_sleep_context_differentiation > 0.05 | Context differentiation is the childhood gain |
| Sleep:wake ratio | > 0.05 (moderate) | Less sleep than infancy; biological pattern |

**Critical constraint (strategy/calibration dissociation, MECH-195):** Replay must interleave
play and real episodes. Replay of play-only episodes during sleep = risk of consolidating
synthetic magnitude calibration. Replay of real-only episodes = failure to bind strategy
structure across domains.

**Failure signature:** synthetic_magnitude_leak_ratio >> 1.0 AND post-sleep context_differentiation
flat = play calibration is consolidating, strategy structure is not.

### 6.4 Adolescence/Adult: Responsibility, Repair, and Reconciliation

**Goal:** Integrate moral residue from harm-causing events without amplifying them into
paralysis; support repair and reconciliation; maintain option-space breadth.

**Replay policy:** RPE + staleness priority with MECH-124 prevention.

| Parameter | Value | Rationale |
|---|---|---|
| RPE priority weight | 0.6 (primary) | Shin et al. 2025: RPE-biased replay predicts subsequent behaviour |
| Staleness weight | 0.3 | MECH-285: corrects for overrepresentation of high-RPE content |
| Coverage floor | 0.25 | Prevents complete abandonment of low-salience content |
| Harm-integration target | residue_integration_without_amplification | REM function: fear extinction, not re-traumatisation |
| MECH-124 monitor | monostrategy_prevention_score >= 1.0 | Walker PTSD analog: option-space should not contract |

**Clinical mapping:** Adult replay failure modes map onto clinical presentations:
- High RPE priority + MECH-094 tag failure → PTSD intrusive replay (traumatic trace gets
  high priority but is mis-routed to waking consciousness)
- Posterior drift toward harm-attribution → depression rumination (self-domain posterior
  drifts negative; replay amplifies rather than corrects)
- Option-space contraction → anhedonia / restriction (viable alternatives excluded from policy)

---

## Part 7: Candidate Experiments

### 7.1 Replay Before/After Infant Gate (Priority: High)

**Title:** Replay diversity and residue consolidation as predictors of infant gate passage

**Scientific question:** Does the quality of replay (coverage, context differentiation, residue
delta) improve as the infant substrate matures toward gate passage, and does this predict
successful childhood entry?

**Design:**
- Track replay metrics (§5) longitudinally across the infant phase
- Measure: replay_zone_coverage_fraction, replay_residue_coverage_delta, post_sleep_z_goal_retention
- Gate passage = DEV-NEED-008 blocking criteria passed
- Test: do replay quality metrics predict gate passage 100 episodes in advance?

**Claim IDs:** DEV-NEED-007, DEV-NEED-008, INV-055, ARC-011

**Expected outcome:** Replay quality improves monotonically during infant phase; convergence
of replay metrics and gate criteria confirms replay is producing developmental progress, not
just memory consolidation.

**Failure signature (important):** Replay metrics improve but gate criteria do NOT improve =
replay is reorganizing the same impoverished content, not creating new developmental capacity.
Resolution: fix the substrate (infant_substrate_expansion.md), not the replay scheduler.

**EXQ label:** Candidate for EXQ-IDEV-001

---

### 7.2 Replay Before/After Play Stages (Priority: High)

**Title:** Interleaved play+real replay vs play-only replay on strategy transfer

**Scientific question:** Does interleaving play and real episodes in the sleep replay buffer
(MECH-203-style balance) produce better strategy-structure transfer (DEV-NEED-011) while
preventing synthetic magnitude consolidation?

**Design:**
- Three conditions:
  - (A) Play-only replay during childhood sleep
  - (B) Real-only replay during childhood sleep
  - (C) Interleaved 1:1 play:real replay (MECH-203 extension)
- Measure: play_to_real_competence_SCC, synthetic_magnitude_leak_ratio, post_sleep_context_differentiation
- Hypothesis: condition (C) maximises SCC while keeping leak ratio in [0.7, 1.3]

**Claim IDs:** MECH-194, MECH-195, MECH-203, INV-060, DEV-NEED-011

**Literature anchor:** Schapiro et al. (2017 Nat Hum Behav) — sleep preferentially binds
memories sharing structure; Gruber et al. (2020 Curr Biol) — childhood sleep promotes rule
abstraction, not just episode retention.

**EXQ label:** Candidate for EXQ-IDEV-002

---

### 7.3 Replay Effect on Monostrategy (Priority: High)

**Title:** Coverage-priority vs RPE-priority replay on infant monostrategy prevention

**Scientific question:** Does coverage-maximising replay during infancy reduce monostrategy
(measured by traj_volume_estimate and action_class_coverage) compared to RPE-priority replay?

**Design:**
- Requires warm-start (DEV-NEED-029 gate must be confirmed first)
- Two conditions on agents past warm-start threshold:
  - (A) Default RPE-priority replay (current)
  - (B) Coverage-maximising replay (coverage_floor=0.6, RPE_weight=0.2)
- Measure: traj_volume_estimate, action_class_coverage, monostrategy_prevention_score
  across 1000 episodes post-warm-start
- Hypothesis: condition (B) shows higher traj_volume_estimate at episodes 200, 500, 1000

**Claim IDs:** DEV-NEED-005, DEV-NEED-007, ARC-065, MECH-285, MECH-124

**Prerequisite:** EXQ-ISEF-001 (warm-start calibration; DEV-NEED-029 thresholds must be set)

**EXQ label:** Candidate for EXQ-IDEV-003

---

### 7.4 Replay Effect on Residue Stability (Priority: Medium)

**Title:** Sleep replay prevents residue saturation after harm events

**Scientific question:** Does a single sleep cycle after a high-harm episode prevent residue
saturation that would otherwise occur over many waking episodes?

**Design:**
- Three conditions:
  - (A) No sleep after high-harm episode
  - (B) Sleep with current scheduler after high-harm episode
  - (C) Sleep with coverage-priority scheduler (low-salience content included) after high-harm episode
- Measure: residue_saturation_pct, residue_curvature_index, mode_stability_after_harm across 50 subsequent episodes
- Hypothesis: (B) and (C) > (A) on curvature and stability; (C) > (B) on option-space preservation

**Claim IDs:** ARC-013, MECH-018, MECH-124, DEV-NEED-018

**EXQ label:** Candidate for EXQ-IDEV-004

---

### 7.5 Replay Effect on z_goal Diversification (Priority: Medium)

**Title:** Does sleep expand or collapse goal variety during infant-childhood transition?

**Scientific question:** Does replay during the infant-to-childhood transition expand z_goal
diversity (more distinct goal signatures, higher z_goal_identity_count) or collapse it toward
the dominant goal encountered?

**Design:**
- Two conditions:
  - (A) No sleep at infant-childhood transition boundary
  - (B) Sleep (current scheduler) at transition boundary
- Measure: z_goal_identity_count, z_goal_norm, z_goal_persistence_across_novel_contexts
  at 0, 50, 100 episodes after transition
- Hypothesis: (B) shows higher z_goal_identity_count and better context-persistence

**Claim IDs:** MECH-189, INV-055, DEV-NEED-006, DEV-NEED-008, DEV-NEED-024

**EXQ label:** Candidate for EXQ-IDEV-005

---

### 7.6 SD-017 Functional Validation: Context Discrimination (Priority: Very High)

**Title:** SD-017 SWS-analog reduces context cosine_sim to < 0.95 after 3 sleep cycles

**Scientific question:** Does the SD-017 SWS-analog pass produce measurably better context
differentiation (lower cosine_sim between distinct context representations) than no-sleep?

**Design:** This is the functional validation that EXQ-265/265a did as methods validation.
Need to test the actual claim (Law et al. 2016: ~3 interleaved sessions required).

- Two conditions: 3 waking sessions + 3 sleep cycles vs 3 waking sessions + no sleep
- Measure: context cosine_sim before and after each cycle; target < 0.95 by cycle 3
- Acceptance: sleep condition shows context_cosine_sim < 0.95; no-sleep stays > 0.95

**Claim IDs:** SD-017, MECH-166, INV-044

**EXQ label:** Candidate for EXQ-IDEV-006 (or continuation of EXQ-500/503 series)

---

## Part 8: Telemetry Proposals

The following channels should be added to MECH-042 telemetry for replay-related monitoring.
These supplement the channels already proposed in developmental_metrics.md.

```
# Replay quality channels (new)
replay_zone_coverage_fraction          : float   # fraction of zones sampled in last sleep cycle
replay_volumetric_coverage             : float   # log-det of trajectory kernel over replayed episodes
replay_buffer_utilisation              : float   # fraction of unique buffer entries sampled per K cycles
replay_low_salience_fraction           : float   # fraction replayed with RPE < 25th percentile
replay_play_real_interleave_ratio      : float   # play:real ratio in last sleep replay pool
replay_context_class_count             : int     # distinct context attractors sampled in last sleep cycle
replay_novel_trajectory_fraction       : float   # fraction not in top-5 most-replayed

# Replay effect channels (new)
pre_post_traj_volume_ratio             : float   # traj_volume post-sleep / pre-sleep
monostrategy_prevention_score          : float   # action_class_coverage post-sleep / pre-sleep (>= 1.0 = good)
option_space_contraction_rate          : float   # rate of decline in viable traj classes across sleep cycles
post_sleep_context_differentiation     : float   # decrease in context cosine_sim per sleep cycle
residue_integration_without_amplification : bool  # residue delta toward equilibrium (not away)

# Stage-aware replay scheduler
replay_scheduler_stage                 : str     # "infant" | "childhood" | "adult"
replay_coverage_floor_active           : bool    # is the coverage floor constraint active?
replay_coverage_floor_adherence        : bool    # was the floor satisfied this cycle?

# Warm-start gate (ARC-065, DEV-NEED-029 extension)
replay_warm_start_gate_all_green       : bool    # all three warm-start criteria met
```

---

## Part 9: Suggested Register Updates

### 9.1 Updates to Existing DEV-NEED Rows

| DEV-NEED | Current state | Recommended update |
|---|---|---|
| DEV-NEED-007 | "offline passes improve map stability, goal seeds, repertoire quality" | Add: replay_diversity_index (> 0.4), replay_low_salience_fraction (> 0.3 infant), replay_zone_coverage_fraction (> 0.6 infant); add explicit infant vs childhood scheduling distinction |
| DEV-NEED-008 | 8-criterion gate from developmental_metrics.md | Add: replay_zone_coverage_fraction > 0.6 as advisory gate; confirm at least one sleep cycle with positive residue_consolidation_delta before gate passes |
| DEV-NEED-005 | "behavioral entropy below ceiling but broad" | Add: monostrategy_prevention_score >= 1.0 post-sleep (MECH-124 check); traj_volume_estimate non-declining across sleep cycles |
| DEV-NEED-011 | "strategy transfer without synthetic magnitude calibration" | Add: replay_play_real_interleave_ratio must be >= 0.5 during childhood sleep; Schapiro 2017 anchors play+real interleaving |
| DEV-NEED-018 | "repair after harm" | Add: residue_integration_without_amplification = True after each high-harm episode sleep cycle |

### 9.2 New DEV-NEED Candidates

**DEV-NEED-030 (PROPOSED): Stage-Aware Replay Scheduling**

| Field | Value |
|---|---|
| Developmental Need | Replay scheduler must adapt to developmental stage |
| Stage | Cross-stage |
| Claim IDs | ARC-011, SD-017, MECH-285; PROPOSED new claim |
| Required mechanism | dev_stage parameter on replay scheduler; stage-indexed policies (§6.1) |
| Gate criterion | replay_scheduler_stage matches current dev_stage; stage-specific metrics pass |
| Failure if absent | Infant stage uses adult RPE-priority = replay_low_salience_fraction < 0.1 = valence map never consolidated; adulthood uses infant coverage-priority = monostrategy never learned |
| Current status | PROPOSED; not registered |
| Priority | After infant_substrate_expansion.md substrate features |

**DEV-NEED-031 (PROPOSED): MECH-124 Prevention Gate**

| Field | Value |
|---|---|
| Developmental Need | Sleep replay must not contract the option space |
| Stage | All (especially adult and post-harm childhood) |
| Claim IDs | MECH-124, ARC-011; PROPOSED new claim |
| Required mechanism | monostrategy_prevention_score monitored per sleep cycle; MECH-285 staleness correction |
| Gate criterion | monostrategy_prevention_score >= 1.0 across rolling 5 sleep cycles; option_space_contraction_rate ≤ 0 |
| Failure if absent | Progressive option-space contraction = adult agent approaches PTSD/depression phenotype; EXQ-573 type null eventually becomes a FAIL on options, not measures |
| Current status | PROPOSED; not registered |
| Priority | With sleep aggregation cluster implementation |

### 9.3 Claims That May Require Revision

**INV-049 (offline phases are a mathematical necessity):** This invariant has FAILED twice
(EXQ-385, EXQ-385a). The theory is correct (Gómez 2006, Diekelmann 2010, SD-017 doc all
ground it strongly). The failures are most likely substrate failures (content poverty) not
theoretical failures. Recommended: do not demote INV-049; instead queue:
1. infant_substrate_expansion.md features to fix content poverty
2. EXQ-IDEV-001 (longitudinal replay quality) as a better test
3. EXQ-IDEV-006 (SD-017 functional validation) as a targeted test

Flag as `pending_substrate_reconfirmation: true` with note: "two FAILs (EXQ-385, EXQ-385a)
most likely reflect infant substrate compression (content poverty) preventing sleep from
demonstrating discriminative advantage; substrate fix is the prerequisite for a valid test."

**ARC-038 (waking consolidation):** Multiple FAILs (EXQ-191, EXQ-240, EXQ-240a, EXQ-267).
Pattern consistent across iterations. Waking schema assimilation is not working in current
substrate. This is a genuine concern: if waking consolidation fails, sleep has an impoverished
prior to work with. This is independent of infant content poverty — it affects the SWS-analog
pass.

---

## Part 10: Summary Assessment

### What replay currently does well
1. **Architecture is correct**: replay is exploratory, non-corrective, non-erasing of φ(z).
   This is the right design.
2. **Balanced replay (MECH-203) works**: harm+benefit balance validated (EXQ-256 PASS).
3. **Surprise-gating (MECH-205) works after iteration**: surprise-gated replay eventually
   validated (EXQ-258b PASS).
4. **Sleep phase infrastructure works**: SD-017 method validation passed (EXQ-265, 265a).

### What replay currently does not do
1. **No stage awareness**: same policy at every developmental stage.
2. **No content coverage guarantee**: replay can satisfy RPE metrics while ignoring most
   of the latent space.
3. **No warm-start gate**: diversity mechanisms zero-differential on cold substrate.
4. **No MECH-124 prevention**: no monostrategy monitoring across sleep cycles.
5. **Full sleep aggregation not implemented**: MECH-272/273/275/285 are designed but
   not yet built — the self-model, place attribution, and staleness correction are all absent.

### Primary recommendation
**The infant substrate is the priority, not the replay scheduler.**
Replay cannot restructure content that was never created. The graduated harm zones,
microhabitat zones, and multi-resource heterogeneity from infant_substrate_expansion.md
are prerequisites for any replay experiment that tests developmental progression.

Once the infant substrate is enriched:
1. Implement stage-aware replay scheduler (§6.1)
2. Add replay quality telemetry channels (§8)
3. Run EXQ-IDEV-001 (longitudinal infant replay quality)
4. Run EXQ-IDEV-006 (SD-017 functional validation)
5. Then build the sleep aggregation cluster (MECH-272/273/275/285)

This ordering ensures that each validation experiment tests the mechanism in isolation
rather than being confounded by content poverty or unimplemented upstream infrastructure.

---

## Related Claims

- ARC-007 (hippocampal systems / path memory and replay)
- ARC-011 (offline integration necessity)
- ARC-013 (residue geometry)
- ARC-014 (default mode)
- ARC-038 (waking consolidation mode)
- ARC-065 (diversity mechanisms)
- INV-010 (offline integration necessity)
- INV-049 (offline phases mathematical necessity — see §9.3)
- MECH-018 (sleep residue integration)
- MECH-030 (sleep modes and ethical consolidation)
- MECH-092 (quiescent waking replay)
- MECH-124 (consolidation-mediated option-space contraction)
- MECH-165 (replay diversity — forward/reverse balance)
- MECH-203 (balanced harm/benefit replay)
- MECH-205 (surprise-gated replay)
- MECH-272/273/275/285 (sleep aggregation cluster)
- SD-017 (minimal sleep-phase architecture)
- DEV-NEED-007 (frequent offline integration during early development)
- DEV-NEED-029 (ARC-065 warm-start gate)
