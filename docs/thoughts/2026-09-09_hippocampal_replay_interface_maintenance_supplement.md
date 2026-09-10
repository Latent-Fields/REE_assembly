# Replay-dependent maintenance of cross-system access

**Focused adversarial supplement to the hippocampal campaign adjudication**
**Prepared:** 2026-09-09 (two independent passes); merged 2026-09-10
**Status:** literature synthesis and assay refinement only. This supplement does not register, implement, queue, score, or promote a claim.
**Parent:** [hippocampal campaign adjudication](2026-09-09_hippocampal_campaign_adjudication.md)
**Prior tranches:** [campaign scaffold](../../evidence/planning/hippocampal_translation_maps_biology_campaign_20260909.md), [literature tranche 1](../../evidence/planning/hippocampal_translation_maps_literature_tranche_1.md), [CA1 transformation tranche 2](../../evidence/planning/hippocampal_translation_maps_literature_tranche_2_ca1_transformation.md), and [REE archaeology](2026-09-09_hippocampal_translation_maps_ree_archaeology.md)

> **Provenance.** This document merges two supplements written independently on 2026-09-09 by two parallel sessions, each unaware of the other, and each landed at this same path. Neither is discarded wholesale. The completed-chain gates, the adjudication of Káli–Dayan (both maintenance operations rescue, so the model awards no unique necessity to interface repair), the Micou–O'Leary adaptive-decoder bound and the world-change ambiguity it raises, the Gate 0 interface-lesion proof, the lettered contrast table with its `D > max(E, F, G)` estimand, the ripple-less-replay measurement warning, and the footnoted source list come from pass B. The four-way outcome taxonomy in §2, the Káli–Dayan and Rule–O'Leary construction parameters in §3, the enumerated rival classes in §5, the two-interface requirement and staging rationale in §6.3, the durability and frozen-endpoint measurement rules in §6.6, the permitted-outcome-language table in §6.8, and roughly half the evidence matrix (the causal interareal, imposed-pairing, cortical-completion, and domain-scope rows) come from pass A. The evidence matrix is the union of both passes; where the two passes reported different source access for the same study, the stronger access is recorded. §6.3 combines both passes' arm sets, which were not identical, into one eight-arm design.

## 1. Target question and bottom line

The narrow question is:

> After a sender and/or receiver representation changes enough to break an established cross-system mapping, does correctly paired replay restore the receiver's actual use of the sender's still-intact information, without improving either system's local memory or competence?

**Bottom line:** no located biological study completes this causal chain, and none genuinely discriminates interface repair from consolidation under preserved local memory. The literature contains strong pieces of the chain, but no single preparation closes it:

- content-specific replay disruption can selectively impair later memory, but also destabilizes the hippocampal representation, so the intact-local-memory condition fails;
- precisely timed hippocampal-cortical coupling can reorganize prefrontal activity and rescue later recall, but starts from deliberately weak encoding and therefore tests consolidation;
- hippocampal output can causally evoke or gate cortical responses and retrieval, but those studies do not impose representational drift or repair a learned mapping;
- multi-area recordings reveal content-sensitive and low-dimensional communication structure, but not longitudinal sender-receiver drift followed by causal repair;
- drift studies establish stable geometry, coordinated cross-area drift, or successful adaptive readout despite unstable units, but never manipulate replay;
- stable latent geometry, cortical completion, ordinary rehearsal, and local Hebbian/homeostatic adaptation all remain viable alternatives at matched budgets.

The one work that explicitly separates correspondence refresh from rehearsal is computational, and it does not favour repair. Káli and Dayan model an intact hippocampal trace becoming inaccessible because its cortical correspondence changes, and restore access by replay-driven reassociation — but ordinary cortical learning on replay rescues recall in the same simulations, combining the two produces no clear extra benefit, and the model supplies the hippocampal reinstatement operation rather than deriving it.[^1] Even the closest formal precursor therefore declines to award unique necessity to interface repair.

The strongest present conclusion is **design-generative, not evidential**: interface repair is a live mechanism that deserves a discriminating assay, not a completed biological claim. The literature motivates assay B; it does not provide biological closure for R4's interface-maintenance interpretation.

## 2. What would count as a completed chain

A result counts only if one experiment, or one tightly integrated experimental series, establishes all six gates within its own design. Findings distributed across unrelated preparations are useful triangulation, not completion, because the confounds differ across preparations and do not cancel when the rows are stacked.

1. **Measured change.** The sender code, the receiver code, or their effective mapping changes longitudinally in a transfer-relevant direction. Apparent change is insufficient if it is only unit turnover, registration noise, behavioural change, within-session context remapping, or a coordinate rotation that preserves the receiver-potent subspace.
2. **Local preservation.** Sender information and sender-local use remain intact, and receiver-local memory and competence remain intact, at the time of the cross-system test.
3. **Access loss.** The representational change specifically reduces receiver use of sender information. A stale cross-system readout, not degraded memory, must be the limiting variable, and the loss must be measured by a causal receiver-dependent behavioural or computational output rather than correlation or decodability alone.
4. **Pair-specific maintenance.** Replay presents the correct sender–receiver episode correspondence, and the comparison is a within-context permutation that preserves event count, state occupancy, marginal content, firing, and plasticity opportunity while breaking only which sender event is paired with which receiver state.
5. **Causal restoration.** Correct pairing restores a receiver-dependent behaviour or computation on held-out episodes. Decoding, correlation, or receiver activation alone is insufficient.
6. **Rival exclusion.** The rescue exceeds local Hebbian/homeostatic readout adaptation, ordinary rehearsal and cortical completion, stable-subspace alignment, and nonspecific timing or plasticity effects, all at matched budgets, and it survives prospective equating of local memory quality.

This standard exists to separate four outcomes that the existing literature routinely confounds:

- **local consolidation:** the stored representation becomes stronger, more precise, or more stable;
- **retrieval triggering or completion:** one system activates a trace that was already usable elsewhere;
- **stable routing:** a preserved subspace makes apparent unit-level drift functionally irrelevant;
- **interface repair:** a formerly broken cross-system correspondence is updated while the contents at both endpoints remain intact.

Only the fourth is the target. The first three can all produce the shared observable — restored downstream performance despite upstream change — and none of them requires pair identity to matter.

## 3. Model-assumption audit

### 3.1 Káli–Dayan: correspondence maintenance is explicit, but not uniquely necessary

Káli and Dayan (2004) is the closest formal precursor to interface repair, but both its force and its limits follow from the model construction.[^1]

**Architecture and stored object.** The cortex is a hierarchical probabilistic generative network with three lower feature areas and an upper medial-temporal neocortical (MTNC) area. Each area has 100 binary units, adjacent layers have reciprocal all-to-all symmetric weights, and within-area connections are not explicitly simulated, so the network functions as a Boltzmann machine that reduces to a restricted Boltzmann machine for the paper's contrastive-divergence-like learning procedure. Complete episodes are distributed patterns across the lower areas. Local cleanup memories in the feature areas are hard-coded: activity within a bitwise Hamming distance of 5 of a valid familiar feature pattern snaps to that pattern exactly. The hippocampus is not simulated as a biological circuit. It is an idealized store that records an MTNC pattern, can be cued when the current MTNC state lies within a fixed Hamming distance of 20, and reinstates the stored pattern exactly. The relevant hippocampal traces are nondecaying in the maintenance simulations.

**Where the failure occurs.** Continued semantic learning changes the cortical weights and therefore the MTNC code for old content. Two access legs deteriorate: the current bottom-up cortical pattern may no longer cue the old hippocampal index, and even a forced old hippocampal pattern may no longer reconstruct the correct lower cortical episode. The episode remains perfectly present in the stipulated store while its current cortical interpretation drifts out of register. Recall is scored by clamping two feature-area patterns and asking whether the third is completed — a real functional-readout criterion inside the model, but not a separately measured receiver behaviour.

**What replay changes.** The paper tests two maintenance operations:

1. **ordinary cortical learning on replay:** replayed episodes continue to train the cortical generative model, which tends to hold their MTNC representations fixed. This is rehearsal and consolidation.
2. **hippocampus–MTNC correspondence refresh:** the stored trace reconstructs lower cortical content, cortical cleanup and the current feed-forward map compute its updated MTNC representation, and that new representation is re-associated with the unchanged hippocampal trace. This is genuine interface reassociation, not a relabelling of trace strengthening.

**The decisive adjudication.** Either operation maintains episodic recall in the reported simulations, and combining them produces no clear extra benefit; for semantic memory, cortical learning on replay is the more important of the two. The model therefore verifies that correspondence refresh is computationally coherent without showing that it is necessary, and without distinguishing it from rehearsal even in silico. Replay must also be frequent enough that the old hippocampal key and the evolving cortical code do not separate beyond recovery; in the earlier transfer simulations replay exposure is heavily skewed toward old items (roughly 90% replay to 10% new experience), whereas the correspondence-maintenance comparison uses balanced replay and experience.

**What the model assumes rather than shows.** Perfect persistent hippocampal storage, a fixed cue threshold, exact lower-level cleanup, symmetric cortical connectivity, availability of the correct episode during replay, and a biologically unspecified hippocampus–MTNC reassociation operation are all premises. Correct versus marginal-matched wrong pairings, replay-timing perturbations, a receiver-local adaptation competitor, a separately measured biological consumer, simultaneous endpoint drift, and synapse-level pathway changes are absent. The result is a constructive proof that replay *can* maintain correspondence under its assumptions, not evidence that biological replay does so.

### 3.2 Rule–O'Leary: a serious local rival, under restrictive conditions

Rule and O'Leary (2022) supplies the strongest explicit local rival.[^2] Its empirical precursor, Rule et al. (2020), shows in posterior parietal cortex that task information and approximate readout structure remain more stable than individual neural responses, while a non-negligible component of drift still degrades a fixed linear readout.[^18]

**Population assumptions.** The sender represents a continuous low-dimensional variable with a redundant population of overlapping bump-like tuning curves that continue to tile the variable as individual tuning drifts. The canonical simulations use 100 encoding units. Tuning features change independently through gradual Ornstein–Uhlenbeck-like drift or through abrupt resampling one feature at a time; in the batched case, plasticity is applied after each five of the 100 encoding features change. Population information and geometry are deliberately preserved while cell identities and tuning change. A downstream linear–nonlinear readout is initialized on the original code.

**What makes the update local.** The rule uses no episode labels and no external teaching signal. Hebbian input-output correlations driven by presynaptic activity and the readout's own postsynaptic output adjust afferent weights; weight decay and gain/bias changes are gated by homeostatic error against fixed targets for the readout's pre-drift output mean and variance. The authors explicitly describe this Hebbian–homeostatic coupling as an ansatz requiring physiological confirmation.

**Hidden resources and stability conditions.** "Local" does not mean assumption-free or exposure-free. The mechanism requires redundant smooth tuning, sufficiently small incremental changes, plasticity at least as fast as drift, and enough sampling or reactivation of the represented variable to estimate correlations and output statistics; when maintenance is too infrequent, the rule fails. Simulations repeatedly sample the encoded variable and apply many repair iterations between small drift increments. Hebbian homeostasis alone extends readout life but eventually shifts the readout's preferred tuning or permits preference swaps after extensive drift. More durable variants add population response normalization and/or a stable recurrent predictive model that supplies covariance structure and corrects inconsistent feed-forward input. Those variants assume that the recurrent structure is fixed or changes far more slowly than the feed-forward representation, that its desired tuning is stable, and that it is periodically reactivated by rehearsal or replay; the origin and long-term updating of that internal model are left open. Large infrequent drift, drift of the decoder or recurrent circuit itself, and continuous symmetries that permit an unanchored global rotation all reduce stability. If sender and receiver internal models drift together, the long-horizon guarantee no longer holds without an additional anchor.

**The normative upper bound.** Micou and O'Leary (2026) strengthen this rival from the other direction, showing that heavy-tailed, sparse tuning jumps can make unsupervised readout correction *easier* than Gaussian drift, and reanalysing PPC and V1 data accordingly.[^3] They also name the ambiguity that any local adaptive decoder inherits: a changing code and a changing world are not distinguishable from the receiver's vantage point, so a self-repairing readout can "correct" a truthful update away. The authors do not claim this is the physiological algorithm; it is an upper bound on what label-free adaptation could achieve.

**Adversarial implication.** Receiver-local self-healing can look exactly like interface repair at the behavioural level even when hippocampal pair identity is irrelevant. It is strongest when drift preserves a smooth manifold, arrives incrementally, and meets a stable receiver scaffold. Rule–O'Leary is a model-sufficiency result, not a demonstration that the proposed local rule operates at a biological hippocampal-cortical interface.

### 3.3 The models are competitors, not confirmations of one another

Káli–Dayan repairs an explicit episodic correspondence by recovering the current cortical code for a stored trace. Rule–O'Leary tracks population statistics without item-specific interareal labels. Their shared observable — restored downstream performance despite upstream change — does not identify the mechanism, and Káli–Dayan cannot even separate its own repair operation from its own rehearsal operation. Pair identity, endpoint-local competence, the drift-to-update timescale ratio, and the stability of the receiver's own scaffold are therefore the decisive experimental variables.

## 4. Focused evidence matrix

**Access key:** `FT` = relevant full primary text inspected; `AM` = author-hosted or accepted manuscript; `ABS` = abstract or primary record only; `PRE` = non-peer-reviewed preprint. Where the two source passes reported different access for the same study, the stronger is recorded here. "Local control" means a direct measure that separates endpoint storage or information from cross-system use; unchanged firing rate, matched stimulation, or gross baseline behaviour is not enough.

| Study | Perturbation or longitudinal change | Sender → receiver | Representational change | Replay content, pairing, or timing | Local-memory control | Functional transfer / actual receiver use | Strongest live alternative and chain verdict | Access |
|---|---|---|---|---|---|---|---|---|
| Káli & Dayan 2004[^1] | in-silico continued semantic learning; replay mechanisms toggled | assumed hippocampal index ↔ MTNC ↔ cortical feature areas | yes: cortical learning shifts MTNC codes while the hippocampal trace is retained | correct stored episodes replayed; refresh and cortical learning separable; no wrong-pair or timing arm | feature patterns and hippocampal traces stipulated intact; cortical cleanup assumed | pattern completion of a missing cortical feature area | **ordinary cortical learning on replay rescues equally.** Model-level interface repair only; no biological discrimination | AM/FT; no maintained code package located |
| Rule & O'Leary 2022[^2] | simulated gradual or batched encoder drift; local plasticity toggled | drifting continuous population → stable linear–nonlinear readout | yes, with preserved low-dimensional variable and redundant coverage | no cross-system episode pairing; local sampling/reactivation drives adaptation | source information and geometry preserved by construction; output mean/variance targets fixed | simulated readout tuning stability | **strongest executable local rival:** repair follows correlations and homeostasis, not episodic correspondence; long-horizon result assumes a stable receiver recurrence and gradual sampled drift | FT, open PMC |
| Micou & O'Leary 2026[^3] | normative adaptive decoder across Gaussian vs heavy-tailed drift; reanalysis of PPC and V1 data | drifting population → ideal adaptive decoder | yes, in model and existing single-area data | no replay manipulation | stimulus statistics and decoder assumptions, not two-system local competence | decoder accuracy only | **upper-bound rival:** drift statistics themselves can permit unsupervised repair; authors claim no physiological algorithm | FT |
| Rule et al. 2020[^18] | longitudinal PPC drift in an already learned task; adaptive weights simulated | recorded PPC population → hypothetical linear readout | drift in coding and noncoding dimensions | no replay manipulation | expert behaviour and decodable task variables remain stable | fixed decoder degrades; small weight changes restore decoding in analysis | **stable-subspace / local-adaptation candidate:** one area, no measured downstream population or synaptic intervention | FT/AM, open PMC with data and code |
| Keinath et al. 2022[^16] | longitudinal CA1 imaging across repeated contexts | CA1 population → experimenter decoder | neuron-level drift with preserved relative context geometry | no replay manipulation | context information and behaviour remain stable | consistent context readout from geometry; no biological receiver manipulation | **invariant relational geometry makes repair unnecessary;** single-area | FT |
| Gallego et al. 2020[^17] | repeated motor behaviour and recordings over months to years | premotor/M1/somatosensory populations → behaviour and decoder | neuron-level turnover and drift | no replay intervention | stable reaching behaviour and latent dynamics | aligned latent dynamics decode behaviour across long intervals despite raw-unit decoder decay | **invariant-manifold rival:** a stable latent scaffold removes the need for active repair; not hippocampal, not a causal sender-receiver assay | FT, open PMC |
| Peters et al. 2026[^19] | chronic simultaneous calcium imaging across four dorsal cortical regions | RSP/VIS/SSp/MO network | yes: 47-day single-neuron drift across regions | no sleep or replay measurement or perturbation | behavioural signals regressed; early-learning sessions excluded | stable task behaviour and preserved population geometry; no causal interareal receiver-use test | **coordinated orthogonal drift preserves cross-area geometry;** closest simultaneous multi-area drift observation, but no hippocampus or replay | FT/PRE |
| Gonzalez et al. 2026[^4] | observational simultaneous recording and subspace analysis across behaviour and sleep | DG/CA3/CA2/CA1 → CA1 and RSC partner populations | task/state recombination; not chronic controlled drift | post-task replay association differs across CA3–CA1 and CA1–RSC; the CA1–RSC relation is not uniformly positive; no perturbation | multiple simultaneous regions constrain some shared-drive accounts; no induced access loss and no matched local-memory control | partial CCA predicts partner activity, not causal receiver-dependent behaviour | **stable reusable low-dimensional subspaces / common state:** closest multi-area anatomy, missing longitudinal drift and replay perturbation | FT, open PMC; small animal and session counts |
| Ji & Wilson 2007[^5] | natural post-experience sleep; no causal manipulation or drift | V1 ↔ CA1, direction unresolved | pre/post experience correlations, not drift | coordinated same-experience replay in slow-wave sleep; relative timing observed | none | no downstream causal use or behaviour tied to individual events | **interareal co-replay only:** common experience or state and reciprocal activation remain viable | AM/FT |
| Ólafsdóttir et al. 2016[^6] | none | CA1 → deep MEC | no longitudinal drift | spatially coherent replay; MEC lags CA1 by about 11 ms, strongest in forward and direction-modulated events | none | none | **common input or state-dependent coupling:** direction and timing observation only | AM |
| Lansink et al. 2009[^20] | natural post-learning rest; no replay perturbation or drift | hippocampus → ventral striatum | none imposed | place-reward pair reactivation; hippocampus tends to lead strongly reactivating pairs | none | reward-memory relevance inferred; no receiver intervention | **content-sensitive temporal coordination, not transfer causality;** authors explicitly leave the causal role unresolved | FT, open PLOS |
| Berners-Lee, Wu & Foster 2021[^7] | none; shuffle analyses preserve event statistics | hippocampus → PFC | no longitudinal drift | PFC units are selective for replayed arms; arm-label shuffles test content specificity | no separate local-memory preservation test | PFC activity predicts later choice, but the PFC replay response is not causally shown to drive it | **replay reports past state or a common task variable:** best content-to-receiver-to-behaviour adjacency; no causal replay or drift test | FT, open PMC |
| Harvey et al. 2023[^21] | learning and task-state comparisons; no induced drift | deep or superficial CA1 assemblies → PFC or MEC assemblies respectively | none imposed | cross-region assemblies selectively reactivate during SWRs; cortical timing follows the corresponding CA1 sublayers | local task coding characterized, but storage-versus-interface failure is not induced | receiver selectivity and behaviour associated, not causally rescued | **selective routing / replay organization:** fixed sublayer projections plus shared task state suffice | FT, open PMC |
| Rothschild et al. 2017[^8] | sounds bias cortical and hippocampal activity during sleep; no drift | auditory cortex → CA1 → auditory cortex | none imposed | content-sensitive prediction before and after SWRs; cue identity manipulated | no separate proof that local trace quality is fixed | no causal receiver-use rescue; the paper states that regional influence and consolidation necessity remain unresolved | **cue-driven associative reactivation or common state:** closed-loop anatomy and content, not repair | FT, open PMC |
| Takigawa et al. 2026[^22] | two visual tracks lateralized to opposite V1 hemispheres; natural post-task sleep, no perturbation or drift | V1 ↔ hippocampus, bidirectional timing | none imposed | simultaneous recordings show same-track reactivation; coherence is greatest with high hippocampal ripple power, local spindle power, and a favourable slow-oscillation phase | competing cortical traces are physically segregated, but local memory quality is not independently fixed | no causal receiver-use or behavioural rescue | **oscillatory state can select coherent traces without updating an interface:** strongest direct matched-content observation, still observational | PRE/FT, bioRxiv, not peer reviewed |
| Nitzan et al. 2020[^23] | optogenetic stimulation and inhibition of bursty subicular cells | CA1/subiculum → superficial granular RSC | none imposed | ripple-locked pathway; state-dependent coupling; no episode-pair shuffle | no memory-content preservation assay | causal induction and reduction of superficial RSC responses, but no memory-guided behaviour | **causal transmission path, not semantic transfer or repair:** synchronous drive and local ripple generation suffice | FT, open publisher text |
| Maingret et al. 2016[^9] | closed-loop PFC stimulation 20 ms after a detected hippocampal ripple vs an added 160–240 ms delay; 1,000 matched stimulations | hippocampal ripple timing → mPFC delta/spindle network | none imposed | timing manipulated; event count, stimulation efficacy, oscillation power and rates, sleep architecture, and gross hippocampal firing matched; content not decoded | task deliberately uses 3-min weak encoding that otherwise yields chance recall; memory strength is the outcome, not held intact | correct timing reorganizes mPFC, increases displaced-object responsiveness, and rescues next-day behaviour | **strong causal timing for consolidation:** the treatment creates a durable memory from a weak trace; pair content and drift absent | FT/AM |
| Geva-Sagiv et al. 2023[^10] | human closed-loop prefrontal stimulation phase-locked vs not phase-locked to MTL slow-wave upstates | MTL/thalamocortical network → prefrontal stimulation site | none imposed | timing and phase locked; no episode-pair manipulation | same stimulation without precise phase locking; local memory not held fixed | recognition accuracy improves with correct locking | **systems consolidation and global excitability:** human timing causality, no interface-specific test | FT, institutional record |
| Okyere et al. 2026[^24] | temporal-interference stimulation of the left hippocampal head, concurrent with vs prior to induced memory reactivation in human sleep | putative hippocampal engagement → cortical slow-oscillation/spindle network | none imposed | stimulation timing relative to reactivation manipulated | associative forgetting is the outcome, not an equivalent local-memory control | concurrent stimulation reduces forgetting relative to mistimed stimulation and increases fast-spindle amplitude | **very recent causal-timing candidate, still consolidation:** no drift, decoded pair content, identified receiver, or preserved local trace; deep-target specificity is inferential | PRE/ABS, posted 2026-09-07 |
| Gridchyn et al. 2020[^11] | online decoding and optogenetic disruption of sleep replay for one of two learned environments | CA1 assemblies; no independently assayed receiver | place-map destabilization follows the manipulation rather than being controlled away | strong environment-specific content selection; no sender–receiver pair permutation | other environment is a within-animal control, but the targeted local CA1 map is altered and re-emerges with relearning | environment-specific later memory deficit | **content-specific consolidation or local map selection:** best content-specific replay causality, but the intact-local-memory gate fails | FT/ABS, open institutional record |
| van de Ven et al. 2016[^25] | closed-loop SWR disruption after novel vs familiar exploration | recent CA1 assembly → later CA1 assembly reinstatement | none imposed | ripple-specific interruption; content dependence stratified by encoding dynamics, not interareal pairing | later local assembly reinstatement is itself the endpoint and is impaired for gradually formed novel assemblies | no distinct receiver or receiver-dependent behaviour | **direct local consolidation:** cannot establish interface repair | FT, open PMC |
| Roux et al. 2017[^26] | closed-loop optogenetic suppression of selected CA1 cells during awake SWRs vs delayed silencing | CA3/CA1 replay-related activity → later CA1 map; no external receiver | none imposed | event timing controlled; content only through silenced-cell participation | firing rates and place-cell proportions preserved, but place-field stability and spatial information are altered | task performance was not impaired by the focal manipulation | **local map stabilization rather than cross-system access;** also shows behaviour can persist despite local representational damage | FT, open PMC |
| Deceuninck & Kloosterman 2024[^13] | closed-loop awake-SWR disruption vs delayed or no stimulation across three repeated-acquisition tasks | hippocampal SWR-associated activity; receiver not recorded | none imposed | ripple timing disrupted; replay content is not decoded or selectively mismatched | detection efficacy, behaviour, ripple rate and location controlled; tasks hippocampus-dependent by prior evidence | no effect on immediate or within-session spatial-memory behaviour | **causal null:** also shows that an SWR intervention is not a content-specific replay intervention | FT |
| Kovács et al. 2016[^14] | optogenetic sleep-SWR blockade vs matched non-coincident light after passive novel-environment exploration | CA1 replay-related activity → later CA1 map; cortical receiver not recorded | new CA1 map tested before and after rest | ripple-triggered, not content-specific | same light dose; local CA1 spatial representation measured directly, with no deficit found | no receiver-use or demanding memory outcome | **bounded null:** sleep SWRs were dispensable for this passive-exploration CA1 stability assay; establishes no general replay dispensability | FT, open PMC |
| Widloski & Foster 2025[^15] | replay detector independent of ripples and bursts; barrier and reward contingencies changed | CA1 replay; downstream receiver not recorded | within-task unstable place fields and context remapping | about one quarter of detected replays lacked ripples or bursts; ripple timing depends on the decoded replayed location | spike rate and active-cell matching equalize replay decoding quality across event classes | no causal transfer test | **measurement warning:** ripple-triggered perturbation can miss replay and confound event with content; replay and ripple are separable | FT, open PMC |
| Bendor & Wilson 2012[^27] | auditory cues associated with one of two tracks presented during sleep | auditory/cortical cue → CA1 replay selection | none imposed | cue identity biases replay content during sleep, not wake | no receiver-local memory control; cueing can also alter sleep and SWR statistics | replay content changes; no demonstrated repaired receiver use | **content selection rather than correspondence repair:** external cueing and arousal remain alternatives | FT, open PMC |
| Barnes & Wilson 2014[^28] | imposed replay of learned, mismatched-novel, or delayed olfactory-bulb stimulation patterns during SWS or wake | imposed olfactory-bulb pattern → piriform and fear-memory system | none imposed | pattern identity, behavioural state, and timing all manipulated | memory strength and precision are the outcomes, not held-fixed controls | matching SWS replay strengthens and sharpens memory; mismatched or delayed replay changes generalization and strength | **closest existing biological precedent for a pairing × timing manipulation,** but not hippocampal, not interface-specific, and the manipulation directly changes memory quality | ABS/FT, indexed passages; direct full-text retrieval blocked |
| Clawson et al. 2021[^12] | sleep-wide optogenetic inhibition or activation of learning-recruited V1 neurons | local V1 ensemble; cross-system sender not identified | orientation tuning can be shifted; no natural longitudinal drift test | reactivation is cell-ensemble-specific, not paired interareal replay | generalized freezing and gist can persist while cue discrimination changes | cue-specific fear discrimination and induced perceptual behaviour | **powerful local-rehearsal rival;** not cross-system interface repair | FT |
| de Sousa et al. 2019[^29] | high-frequency activation of learning-tagged RSC ensembles during sleep or anaesthesia vs wake | RSC engram → distributed cortex, amygdala, and behaviour | none imposed | correct local ensemble; state-dependent; no hippocampal-sender pairing | stimulation changes contextual generalization and hippocampal dependence, so the memory itself is not held fixed | accelerates remote-like retrieval and cortical engagement | **executable cortical rehearsal rival:** local ensemble reactivation alone produces systems-consolidation-like change | FT, open PMC |
| Cowansage et al. 2014[^30] | optogenetic activation of a learning-tagged RSC ensemble, including with hippocampal inactivation | RSC engram → amygdala and behavioural output | none imposed | no offline replay or interareal pair test | the context-memory ensemble is stimulated directly | freezing and downstream amygdala activation can be evoked without an active hippocampus | **cortical completion / retrieval rival:** a locally stored cortical trace can drive the output once triggered | FT/ABS |
| Tanaka et al. 2014[^31] | retrieval-time silencing of encoding-tagged CA1 cells | CA1 engram → EC, RSC, perirhinal cortex, amygdala | none imposed | retrieval timing; no replay pairing or drift | overall activity largely preserved, but the sender ensemble is acutely silenced and storage integrity is not independently demonstrated during the test | cortical reinstatement and behaviour are impaired | **causal receiver reinstatement, not maintenance:** proves an access route can matter at retrieval, not that replay repaired it | ABS |
| Cho et al. 2025[^32] | one vs five presentations of item-specific sounds during a nap | sensory cue → distributed human memory systems, not regionally resolved | none imposed | correct cue repetition varied; no interareal neural measurement | pre/post item memory measured | no significant memory benefit from one or five cue presentations in the reported sample | **behavioural TMR null:** bounds cue-dose generality but cannot diagnose replay failure, arousal, ceiling, or interface state | FT, open PMC |
| Thompson et al. 2026[^33] | bilateral hippocampal lesions before procedural training | striatal task sequences → later procedural performance; hippocampus is the lesioned candidate coordinator | none imposed | offline sequence replay persists; no hippocampal pairing | striatal sequence organization and performance compared with controls | procedural learning and replay survive hippocampal loss | **domain-bounded negative control:** replay and improvement need not be hippocampally authorized, so no universal replay authority should be inferred | FT, publisher text |

### 4.1 Matrix adjudication

No row contains the required conjunction: relevant longitudinal drift, intact endpoint memory, loss of receiver use, content-correct versus marginal-matched replay, and selective restoration of receiver-dependent behaviour. The conjunction cannot be assembled from rows, because the three near-bridge families fail for different and non-cancelling reasons.

- **Interareal replay studies** show that content propagates or covaries across hippocampal, entorhinal, sensory, prefrontal, striatal, and retrosplenial networks. They do not establish a previously broken correspondence, because the sender and receiver codes are never tracked through access loss and recovery.
- **Causal replay studies** show that content identity or millisecond timing matters for later memory. But later memory, the local hippocampal code, or a recognition score is the dependent variable, so a deficit is equally compatible with ordinary consolidation, local map stabilization, or plasticity gating.
- **Drift and stable-subspace studies** show why an interface-repair mechanism may be unnecessary at all: information can persist in an invariant geometry, drift can be coordinated across areas, or a local adaptive readout can track a changing encoder. None of them manipulates replay, so none tests whether paired replay contributes incremental rescue.

The nearest individual pieces, and exactly what each is missing:

- **Káli–Dayan:** the exact mechanism, but only in a model whose intact storage and cleanup are stipulated, and in which ordinary cortical learning on replay rescues equally well.
- **Gridchyn:** causal content specificity, but the local hippocampal representation is damaged, so the local-preservation gate fails.
- **Maingret and Geva-Sagiv:** causal timing and receiver reorganization, in animals and humans respectively, but the intervention consolidates a deliberately weak or unequalized memory and pairing is never manipulated.
- **Berners-Lee:** replay content read out by an identified receiver whose activity predicts later choice, but with no replay perturbation, no drift, and no causal test that the PFC response drives the behaviour.
- **Takigawa:** unusually direct same-content cortico-hippocampal co-reactivation with physically segregated competing traces, but observational and a preprint.
- **Nitzan and Tanaka:** causal interareal influence and causal receiver reinstatement, but no drift and no repair.
- **Gonzalez and Peters:** simultaneous multi-area communication subspaces and chronic cortex-wide coordinated drift, but neither combines drift with causal receiver use, and Peters has no hippocampus or replay at all.
- **Barnes–Wilson:** the closest existing pairing × state × timing manipulation, but in an imposed olfactory pathway where the manipulation directly changes memory strength and precision.

Accordingly, **no located biological study genuinely discriminates interface repair from consolidation under matched local-memory quality**.

## 5. Rivals that assay B must earn its way past

### 5.1 Stable or coordinated communication scaffold

Unit-level drift may occur largely outside the receiver-potent subspace. A fixed or slowly rotating latent manifold can preserve behaviour even while single-neuron correspondences change, and Peters et al. show that drift can be *coordinated* across areas in a way that preserves cross-area geometry — the sharpest form of this rival, because it removes the interface problem without any maintenance mechanism. Gallego, Keinath, Rule et al., and Gonzalez et al. make this more than a straw man. If native transfer survives the imposed change, assay B has not created an interface-maintenance problem and should stop.

### 5.2 Receiver-local self-healing

The receiver can exploit redundancy and its own output statistics to retune afferent weights without episodic pair labels. This is the strongest mechanistically explicit competitor because it predicts recovery under drift while local information remains stable — the same high-level phenotype as replay repair. Micou–O'Leary bounds how good this can get without labels, and shows that some drift statistics make it easier rather than harder.

### 5.3 Cortical completion and local rehearsal

An index or cue can trigger a cortical trace that completes locally. Cowansage et al. show that activating an RSC ensemble drives memory behaviour and downstream amygdala activity even with the hippocampus inactivated. De Sousa et al. show that repeated RSC-ensemble activation induces remote-like retrieval and cortical engagement. Clawson et al. show that reactivating learning-recruited V1 neurons during sleep changes cue-specific discrimination and even orientation tuning. These are executable comparators, not residual explanations.

### 5.4 Ordinary paired experience

Full current examples presented to both systems can relearn a mapping with no special offline mechanism. This provides a data-matched upper bound and tests whether sleep-like offline scheduling contributes anything beyond ordinary supervised co-exposure. It is not defeated by showing that correct replay works.

### 5.5 Local consolidation or map stabilization

Gridchyn, van de Ven, Roux, Barnes–Wilson, Maingret, and Geva-Sagiv all demonstrate routes by which replay-related manipulations change the strength, precision, stability, or cortical availability of the memory itself. A local-memory gain that covaries with transfer rescue supports consolidation unless the assay prospectively holds that gain fixed.

### 5.6 World change rather than code change

A local adaptive readout cannot distinguish a drifting code from a genuine change in the latent cause it represents, and neither can an experimenter who only observes restored performance. Any claim that maintenance "repaired" a mapping must show that the pre-drift mapping was still the correct one, not merely that the receiver converged on some self-consistent readout.

## 6. Assay B revision: make interface repair earn its name

### 6.1 Operational variables and the primary endpoint

Let sender state `x_t` encode item `z`, let receiver state `r_t` retain its own task competence, and let `A_t` be the cross-system mapping the receiver uses. Drift changes the embedding to `x'_t = D_s x_t`, or changes the receiver's coordinates, or both, while oracle decoding of `z` within each local system remains at criterion.

Define receiver use as a causal contrast on a held-out task:

\[
U = \text{performance(message available)} - \text{performance(message ablated or counterfactually replaced)}.
\]

The primary endpoint is recovery of `U`. It is not representational similarity, adapter loss, mutual information, decoder agreement, or local recall. Pair-specific repair requires recovery under correctly paired replay to exceed both a marginal-matched pair permutation and the best local self-repair rival.

Before any maintenance phase, freeze: the endpoint-local probes for sender information and receiver memory and competence; the native transfer readout and the held-out receiver-use evaluation; the replay items and their identities; and the no-drift reference geometry and communication subspace.

### 6.2 Gate 0: prove that the imposed drift creates an interface lesion

Before evaluating any maintenance mechanism, assay B must reject two benign cases:

1. **Invariant-subspace drift:** a fixed receiver readout still works because the drift is confined to a null direction or preserves a stable latent geometry.
2. **Global task loss:** sender information or receiver competence has itself degraded, so there is no isolated interface problem to repair.

Use four probes before the maintenance phase:

- no drift, no update — the stable ceiling;
- task-relevant, known invertible drift that breaks a frozen cross-system readout;
- magnitude-matched drift restricted to an empirically identified receiver-null subspace — the negative instrument control;
- task-relevant drift plus a known oracle inverse adapter — the positive control.

For the task-relevant drift, require all four of: degraded `U`; intact sender-local decoding and action; intact receiver-local memory and action, both within prospectively defined equivalence bounds; and restoration by the oracle inverse adapter. Each failure mode is diagnostic and each is a stop condition. If the oracle cannot restore use, the lesion is not an interface lesion. If null-space drift degrades use, the subspace identification is invalid. If task-relevant drift does not degrade use, stable invariants or endogenous adaptation have already won and the replay-repair test should not proceed.

Sender-only drift is the first identification case. Receiver-only and joint drift are generalization tests, run afterwards, because joint drift leaves the locus of repair underdetermined.

Gate 0 also preserves assay B's original two-interface requirement: one interface should be drifted and repairable, and a second should be stable or affected only in unused coordinates, so that a nonspecific plasticity or arousal effect is visible as an effect on both.

### 6.3 Minimal decisive contrasts

After Gate 0 passes, the smallest interpretable primary set is:

| Arm | Drift | Maintenance information | Purpose |
|---|---|---|---|
| A | none | none | stable ceiling |
| B | relevant drift | none | access-lesion floor |
| C | relevant drift | oracle inverse adapter | verifies recoverability and maximum repair |
| D | relevant drift | correctly paired sender–receiver replay | target mechanism |
| E | relevant drift | within-context permuted pairs, identical marginals and timing | isolates correspondence information |
| F | relevant drift | Rule–O'Leary-faithful receiver-local self-repair | strongest executable local rival |
| G | relevant drift | receiver-local rehearsal and completion, no sender message | consolidation and completion rival |
| H | relevant drift | ordinary online paired co-exposure to full current examples | matched-data upper bound |

The primary attribution contrast is `D > max(E, F, G)` on held-out `U`, with A–C validating the lesion and its dynamic range. `D` versus `H` separately determines whether the effect is replay-specific or merely relearning from paired data. Arms F and G must be run separately rather than as one combined rival, because a single combined comparator cannot say which local mechanism won.

**Do not interpret `D > B` alone.** It is compatible with generic replay, additional plasticity opportunity, rehearsal, and homeostatic adaptation.

Timing is a second-stage test, run only if correct content pairing first beats the permuted-pair arm. Hold correct pair identity fixed and compare receiver plasticity enabled inside the empirically effective window against the same window shifted or independently shuffled, with total events, inter-event intervals, phase and state occupancy, activation magnitude, stimulation energy, and total weight change all matched. A timing effect without pair specificity supports plasticity gating or consolidation, not interface repair. Do not interpret a timing interaction if the shifted condition also changes arousal, oscillation induction, or data exposure.

This staging avoids paying for a pairing × timing factorial before either instrument works independently.

### 6.4 Implementing the strongest executable rival: the self-healing receiver

Implement arm F at the same representational interface, with the same update count, local samples, parameter budget, activation magnitude, and plasticity magnitude as the paired-replay adapter, but with no cross-system episode identity. Fix all components before outcomes are observed:

1. Initialize the receiver readout on the pre-drift code.
2. Store fixed targets for its pre-drift output mean and variance.
3. At each maintenance opportunity, update receiver weights using only current presynaptic sender activity, the receiver's own output, homeostatic variance error, and error-gated decay, following Rule–O'Leary's local rule.[^2]
4. Add population response normalization as a preregistered stronger version.
5. Add a separate ceiling variant with a fixed recurrent predictive or covariance model learned before drift and reactivated on the same schedule. Label this as an extra stability assumption, not as free local plasticity — the model's own stability is assumed, not earned.
6. Sweep the maintenance interval against the drift rate. Rule–O'Leary's success depends on many small corrections before mismatch grows large; one abrupt rotation followed by one repair block is not a faithful test of the rival and would stack the comparison in favour of paired replay.

Arm G is the completion variant: receiver-local completion from its own recurrent state, with local rehearsal but no sender message at all.

For joint sender/receiver drift, provide symmetric local adaptation at each endpoint or explicitly declare the receiver fixed. Otherwise a paired adapter receives a structural advantage unrelated to pairing.

### 6.5 Intervention-validity constraint: the target must be decoded content, not ripples

Widloski and Foster show that roughly a quarter of detected replay events lack sharp-wave ripples or population bursts, and that ripple timing itself depends on the decoded replayed location.[^15] Any biological implementation of arms D, E, or the timing stage must therefore target decoded replay content rather than ripple onset. A ripple-triggered design systematically misses a replay class and confounds the event with its content, which means a ripple-triggered null bounds ripples, not replay, and a ripple-triggered positive result cannot be attributed to pairing.

### 6.6 Local-memory controls are constraints, not covariates

Before every cross-system evaluation block, require criterion performance on:

- decoding `z` from the sender using a freshly fit local oracle, plus a sender-local behavioural or readout task;
- receiver-only completion or task execution without the sender message;
- episode and item identity and difficulty distributions matched across maintenance arms;
- equivalent maintenance event count, plastic updates, activation magnitude, and elapsed time.

Titrate or exclude blocks until local measures are equated **prospectively**. Regressing out unequal local recall after the fact is insufficient, because consolidation may already have changed which items remain available, and conditioning on a treatment-affected memory score is a collider.

Further measurement rules:

- Use equivalence tests, not nonsignificant differences, for sender information, sender local recall, receiver local recall and competence, and univariate activity statistics.
- Localize receiver use causally: ablate or counterfactually replace the incoming message at test, intervene on the learned adapter, and verify the item-specific errors predicted by the induced mapping. A decoder that reads sender content out of receiver activity is not use.
- Evaluate transfer on held-out episodes, recombined relations, and a second receiver query, so that memorized replay pairs cannot carry the result.
- Keep evaluation endpoints frozen. Any adaptive probe used to score a post-drift representation must be reported separately from the native receiver-use metric.
- Report communication-subspace overlap and transfer separately. A stable subspace with intact behaviour is evidence that repair was unnecessary; a rotated subspace without behavioural rescue is not repair.
- After a one-step rescue, continue drift and continue use. A transient remapping followed by rapid collapse does not establish maintenance.

### 6.7 Strongest falsifier and stop conditions

The strongest falsifier is not "replay disruption has no effect." It is:

> After a verified interface lesion with intact local information and demonstrated recoverability, a faithful label-free receiver-local self-healing or readout-adaptation arm, or ordinary local rehearsal, restores held-out receiver-dependent use as well and as durably as correctly paired replay, within a prespecified equivalence margin and at a matched update budget, while permuted pairings are no worse after update and local-memory measures remain equivalent.

That result would show that the effect attributed to replay correspondence is explained by invariant geometry plus local co-adaptation, and would remove the claimed need for pairwise cross-system correspondence repair even if replay remains useful for consolidation.

Two upstream stop conditions are equally decisive and cheaper to reach. If the relevant drift does not impair native transfer — because an invariant subspace or a coordinated transformation preserves receiver use — there is no broken interface for replay to repair. If correct replay improves local memory quality, the result is consolidation-contaminated and cannot answer the target question regardless of effect size.

### 6.8 Permitted outcome language

| Result | Permitted interpretation |
|---|---|
| `D` > `E`, `F`, and `G`, with equivalent local memory and receiver-required behaviour restored | Supports pair-specific interface repair in this assay; does not by itself establish a hippocampal biological mechanism |
| `D` = `F` (or `G`) > `E` and `B` | Access can be maintained by local adaptive readout or local completion; pair-specific replay is not necessary |
| `D` = `H` > `E` | Paired experience relearns the mapping; offline replay specificity is unearned |
| All maintenance arms rescue | Generic plasticity, invariant subspace, or insufficiently selective perturbation |
| Replay improves local memory and transfer together | Consolidation-compatible; target question unresolved |
| Subspace stable and native transfer intact after drift (Gate 0 fails) | No interface failure; active repair unnecessary under this transformation |
| Geometry changes without receiver-dependent behaviour recovery | Representational reorganization, not functional repair |
| `C` fails to restore `U` | The lesion is not an interface lesion; the drift model is invalid, not the hypothesis |
| Rescue at one step, collapse under continued drift | Transient remapping, not maintenance |

## 7. Search streams and stopping result

This was a focused adversarial update across two independent passes, not a preregistered systematic review or meta-analysis. Primary records were searched and cross-checked through publisher pages, PubMed/PMC, institutional and author-hosted manuscripts, and recent preprint servers.

| Stream | Primary-source query families and venues | What was recovered | Stopping result |
|---|---|---|---|
| Explicit correspondence maintenance | `hippocampal replay correspondence maintenance`, `index update cortical representation change`, `hippocampus cortical replay representational drift alignment`; Káli/Dayan citation chain | Káli–Dayan's mapping-refresh mechanism; no biological implementation with matched wrong pairs | Saturated around the named model and its assumptions; biological bridge absent |
| Local readout repair | `representational drift homeostatic Hebbian readout`, `self-healing codes Hebbian homeostatic`, `adaptive decoder drift`, `local synaptic readout adaptation drift`, `stable recurrent predictive model`; PNAS/PLOS/eLife | Rule–O'Leary, Micou–O'Leary, Rule et al. | Strong computational rivals found; physiological tests absent |
| Simultaneous interareal replay | hippocampus–PFC, hippocampus–visual cortex, hippocampus–MEC, hippocampus–RSC, hippocampus–ventral striatum, `CA1 PFC MEC cross-region assembly replay`, `subiculum retrosplenial ripple propagation`; Nature/Neuron/JNeurosci/PMC | Ji–Wilson, Ólafsdóttir, Lansink, Berners-Lee, Harvey, Rothschild, Nitzan, Gonzalez, Takigawa | Content, coordination, and one causal transmission path found; no chronic drift × intervention × use study |
| Replay content perturbation | `decoded replay content disruption environment`, `assembly-specific replay disruption`, `content-specific replay closed loop`; Cell/Neuron/PubMed | Gridchyn environment-selective disruption; van de Ven assembly disruption | Content causality found, but the local hippocampal map or assembly is itself the outcome |
| Imposed and cued replay pairing | `matched/mismatched imposed replay`, `biasing replay content sleep cueing` | Barnes–Wilson imposed matched vs mismatched vs delayed patterns; Bendor–Wilson cued replay selection | Closest existing pairing × timing precedent, but outside the hippocampal interface and with memory quality as the outcome |
| Replay timing perturbation | SWR-triggered cortical stimulation, phase-locked human stimulation, delayed controls, `receiver update window replay`, 2026-09-07 human hippocampal temporal-interference preprint | Maingret; Geva-Sagiv; Okyere preprint | Timing causality found across species; pair identity and local-memory preservation absent |
| Null and negative replay intervention | `SWR disruption no effect`, `ripple disruption no effect`, `targeted memory reactivation null`; eLife/PLOS/PMC | Deceuninck–Kloosterman behavioural null; Kovács CA1-map null; Cho TMR dose null | Nulls are task-, state-, and dose-dependent and generally target SWRs or cues, not decoded replay content |
| Replay measurement boundary | `replay without ripple`; Nature Communications/PMC | Widloski–Foster | Ripple-triggered designs miss a substantial replay class; the intervention target must be decoded content |
| Stable invariant subspaces | `stable task information unstable population`, `stable latent dynamics`, `communication subspace`, `invariant manifold representational drift`; Nature Communications/eLife/Nature Neuroscience/PMC | Keinath, Gallego, Rule et al., Gonzalez | Strong rival class; no replay manipulation |
| Simultaneous multi-area drift | `coordinated representational drift across areas`, `longitudinal simultaneous hippocampus retrosplenial cortex drift`, `same neurons across days interareal replay`; bioRxiv/PMC/PubMed | Peters et al. cortex-wide preprint | Chronic multi-area drift found, but with no hippocampus, sleep or replay, or causal receiver-use test |
| Cortical completion and rehearsal | learning-activated V1 ensembles, `retrosplenial engram reactivation`, `cortical pattern completion`, `hippocampal silencing cortical reinstatement`, `ordinary rehearsal systems consolidation`; Science/Neuron/Nature Communications/PNAS | Clawson, Cowansage, de Sousa, Tanaka | Local reactivation can drive or preserve content, and cortical reinstatement can be causally disrupted; no pairwise cross-system repair isolation |
| Domain scope of replay authority | hippocampal lesion with preserved procedural replay | Thompson et al. | Replay and improvement can be hippocampus-independent in procedural domains |

The search was stopped when additional queries repeatedly returned the same three disconnected families — interareal replay without drift, replay intervention with memory as the outcome, and drift stability without replay — rather than a study crossing the gates. This is a negative search conclusion, not proof that no such paper exists.

## 8. Unresolved literature and measurement debts

1. **Exact biological bridge.** No located study tracks identified sender and receiver populations across the same drift interval while directly measuring preserved local competence, perturbing decoded pair identity, and testing receiver-dependent behaviour.
2. **Closed-loop pair debt.** Existing closed-loop experiments perturb ripples, timing, or one decoded hippocampal content. None delivers correct versus independently permuted sender–receiver episode pairs with matched marginals. A within-context permutation that preserves replay marginals and physiological timing while breaking only pairing still has to be developed.
3. **Replay target validity.** It is unknown whether closed-loop SWR interventions capture the relevant replay class at all; ripple-less replay makes ripple onset an incomplete proxy.[^15]
4. **Receiver-use debt.** Interareal prediction and cortical reactivation are rarely tied to an acute receiver-necessity test for the behavioural output being restored. Establish whether cortical activation during hippocampal replay changes a readout used later, rather than merely co-reactivating a memory or reflecting common input.
5. **Preserved-local-memory debt.** The strongest content-specific causal study changes CA1 map stability; the strongest timing studies begin from a weak or unequalized trace. Independent sender-local and receiver-local tasks must be validated at the exact post-maintenance time point and equated prospectively across arms.
6. **Natural drift geometry.** It has not been shown that biological drift actually enters the receiver-potent subspace. Unit instability alone is inadequate evidence of an interface problem.
7. **Adaptation timescale.** The drift rate has not been mapped against the replay or update interval. Local adaptation models are favoured by incremental drift and frequent rehearsal, so an unswept timescale silently chooses the winner.
8. **Biological plasticity debt.** No located experiment directly measures replay-induced updates of an identified hippocampal–cortical mapping while excluding local synaptic adaptation within sender and receiver.
9. **Stable-scaffold debt.** Multi-area communication subspaces have not been shown to remain stable through longitudinal representational drift in the same hippocampal–cortical preparation. Peters et al. demonstrate coordinated cortical drift, but without hippocampus or replay.
10. **World-change ambiguity.** Code drift has not been separated from real changes in latent cause. A local adaptive decoder can otherwise "repair" a truthful update away, and an experimenter scoring restored performance cannot tell the difference.[^3]
11. **Joint-drift debt.** Most drift work studies one population. Sender-only drift should be tested first, then receiver-only and joint changes with symmetric local rivals; otherwise correspondence repair and endpoint stabilization remain confounded.
12. **Ordinary-rehearsal parity debt.** Biological replay studies rarely include a matched online paired-experience arm with identical content and plasticity opportunity.
13. **Negative-result scope.** Nulls are bounded by task demand, state classification, perturbation efficacy, cue arousal, and statistical power. Replay interventions need positive controls for disruption efficacy and an explicit statement of which replay classes, states, and timescales remain untouched.
14. **Model reproducibility debt.** Káli–Dayan is available in full, but no maintained code or data package was located in either pass, and its hippocampus and cortical cleanup are idealized modules. Rule–O'Leary's local plasticity rules have not been causally validated at a biological hippocampal receiver, and the authors themselves describe the Hebbian–homeostatic coupling as an ansatz awaiting physiological confirmation.
15. **Domain debt.** Most causal evidence is spatial or contextual. Thompson et al. show that procedural replay can be hippocampus-independent, so no universal replay authority should be inferred.

## 9. Landing boundary

This supplement narrows assay B and records unresolved evidence debts. It deliberately makes no change to `claims.yaml`, experiment proposals, substrate code, or experiment queues. Any implementation or claim-state action requires a separate governed decision after the current campaign and pending experiment reviews are resolved.

## Sources

Entries marked with a bracketed note were carried over from the second source pass, which recorded DOI, venue where stated, and access level but not full bibliographic titles. Completing those entries is a small outstanding documentation debt.

[^1]: Káli, S., & Dayan, P. (2004). "Off-line replay maintains declarative memories in a model of hippocampal-neocortical interactions." *Nature Neuroscience*. [Author-hosted paper and abstract](https://www.gatsby.ucl.ac.uk/~dayan/papers/kd04.html). [DOI](https://doi.org/10.1038/nn1202).
[^2]: Rule, M. E., & O'Leary, T. (2022). "Self-healing codes: How stable neural populations can track continually reconfiguring neural representations." *PNAS*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8851551/). [DOI](https://doi.org/10.1073/pnas.2106692119).
[^3]: Micou, C., & O'Leary, T. (2026). "Statistics of cortical representational drift can enable robust readout." *PLOS Computational Biology*. [Full text](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014297). [DOI](https://doi.org/10.1371/journal.pcbi.1014297).
[^4]: Gonzalez, J., et al. (2026). "Subspace communication in the hippocampal–retrosplenial axis." *Nature*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13317024/). [DOI](https://doi.org/10.1038/s41586-026-10481-z).
[^5]: Ji, D., & Wilson, M. A. (2007). "Coordinated memory replay in the visual cortex and hippocampus during sleep." *Nature Neuroscience*. [Publisher page](https://www.nature.com/articles/nn1825). [DOI](https://doi.org/10.1038/nn1825).
[^6]: Ólafsdóttir, H. F., Carpenter, F., & Barry, C. (2016). "Coordinated grid and place cell replay during rest." *Nature Neuroscience*. [Accepted manuscript](https://discovery.ucl.ac.uk/1478267/3/Olafsdottir_et_al_2016%20Co-ordinated%20grid.pdf). [DOI](https://doi.org/10.1038/nn.4291).
[^7]: Berners-Lee, A., Wu, X., & Foster, D. J. (2021). "Prefrontal cortical neurons are selective for non-local hippocampal representations during replay and behavior." *Journal of Neuroscience*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8265798/). [DOI](https://doi.org/10.1523/JNEUROSCI.1158-20.2021).
[^8]: Rothschild, G., Eban, E., & Frank, L. M. (2017). "A cortical–hippocampal–cortical loop of information processing during memory consolidation." *Nature Neuroscience*. [DOI](https://doi.org/10.1038/nn.4457).
[^9]: Maingret, N., Girardeau, G., Todorova, R., Goutierre, M., & Zugaro, M. (2016). "Hippocampo-cortical coupling mediates memory consolidation during sleep." *Nature Neuroscience*. [Author manuscript](https://girardeaulab.org/wp-content/uploads/2018/08/Maingret2016.pdf). [DOI](https://doi.org/10.1038/nn.4304).
[^10]: Geva-Sagiv, M., et al. (2023). "Augmenting hippocampal–prefrontal neuronal synchrony during sleep enhances memory consolidation in humans." *Nature Neuroscience*. [Institutional record](https://escholarship.org/uc/item/1hm3t82s). [DOI](https://doi.org/10.1038/s41593-023-01324-5).
[^11]: Gridchyn, I., Schoenenberger, P., O'Neill, J., & Csicsvari, J. (2020). "Assembly-specific disruption of hippocampal replay leads to selective memory deficit." *Neuron*. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/32070475/). [DOI](https://doi.org/10.1016/j.neuron.2020.01.021).
[^12]: Clawson, B. C., et al. (2021). "Causal role for sleep-dependent reactivation of learning-activated sensory ensembles for fear memory consolidation." *Nature Communications*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7900186/). [DOI](https://doi.org/10.1038/s41467-021-21471-2).
[^13]: Deceuninck, L., & Kloosterman, F. (2024). "Disruption of awake sharp-wave ripples does not affect memorization of locations in repeated-acquisition spatial memory tasks." *eLife*. [Full text](https://elifesciences.org/articles/84004). [DOI](https://doi.org/10.7554/eLife.84004).
[^14]: Kovács, K. A., et al. (2016). "Optogenetically blocking sharp wave ripple events in sleep does not interfere with the formation of stable spatial representation in the CA1 area of the hippocampus." *PLOS ONE*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5070819/). [DOI](https://doi.org/10.1371/journal.pone.0164675).
[^15]: Widloski, J., & Foster, D. J. (2025). "Replay without sharp wave ripples in a spatial memory task." *Nature Communications*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639102/). [DOI](https://doi.org/10.1038/s41467-025-65181-5).
[^16]: Keinath, A. T., Mosser, C.-A., & Brandon, M. P. (2022). "The representation of context in mouse hippocampus is preserved despite neural drift." *Nature Communications*. [Full text](https://www.nature.com/articles/s41467-022-30198-7). [DOI](https://doi.org/10.1038/s41467-022-30198-7).
[^17]: Gallego, J. A., et al. (2020). "Long-term stability of cortical population dynamics underlying consistent behavior." *Nature Neuroscience*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7007364/). [DOI](https://doi.org/10.1038/s41593-019-0555-4).
[^18]: Rule, M. E., et al. (2020). "Stable task information from an unstable neural population." *eLife*. [Full text](https://elifesciences.org/articles/51121). [DOI](https://doi.org/10.7554/eLife.51121).
[^19]: Peters, R., et al. (2026). "Coordinated Representational Drift Across the Mouse Cortex." *bioRxiv* preprint. [Full text](https://www.biorxiv.org/content/10.64898/2026.05.05.723038v1). [DOI](https://doi.org/10.64898/2026.05.05.723038).
[^20]: Lansink, C. S., et al. (2009). *PLOS Biology*. [DOI](https://doi.org/10.1371/journal.pbio.1000173). [Title not recorded in the source pass.]
[^21]: Harvey, R. E., et al. (2023). *Neuron*. [DOI](https://doi.org/10.1016/j.neuron.2023.04.015). [Title not recorded in the source pass.]
[^22]: Takigawa, M., et al. (2026). *bioRxiv* preprint. [DOI](https://doi.org/10.64898/2026.06.12.731367). [Title not recorded in the source pass.]
[^23]: Nitzan, N., et al. (2020). *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-020-15787-8). [Title not recorded in the source pass.]
[^24]: Okyere, A., et al. (2026). *bioRxiv* preprint, posted 2026-09-07. [DOI](https://doi.org/10.64898/2026.09.02.748628). [Title not recorded in the source pass.]
[^25]: van de Ven, G. M., et al. (2016). *Neuron*. [DOI](https://doi.org/10.1016/j.neuron.2016.10.020). [Title not recorded in the source pass.]
[^26]: Roux, L., et al. (2017). *Nature Neuroscience*. [DOI](https://doi.org/10.1038/nn.4543). [Title not recorded in the source pass.]
[^27]: Bendor, D., & Wilson, M. A. (2012). *Nature Neuroscience*. [DOI](https://doi.org/10.1038/nn.3203). [Title not recorded in the source pass.]
[^28]: Barnes, D. C., & Wilson, D. A. (2014). *Journal of Neuroscience*. [DOI](https://doi.org/10.1523/JNEUROSCI.5274-13.2014). [Title not recorded in the source pass.]
[^29]: de Sousa, A. F., et al. (2019). *PNAS*. [DOI](https://doi.org/10.1073/pnas.1818432116). [Title not recorded in the source pass.]
[^30]: Cowansage, K. K., et al. (2014). *Neuron*. [DOI](https://doi.org/10.1016/j.neuron.2014.09.022). [Title not recorded in the source pass.]
[^31]: Tanaka, K. Z., et al. (2014). *Neuron*. [DOI](https://doi.org/10.1016/j.neuron.2014.09.037). [Title not recorded in the source pass.]
[^32]: Cho, S., et al. (2025). *Neuropsychologia*. [DOI](https://doi.org/10.1016/j.neuropsychologia.2025.109275). [Title not recorded in the source pass.]
[^33]: Thompson, R., et al. (2026). *Nature Neuroscience*. [DOI](https://doi.org/10.1038/s41593-026-02362-5). [Title not recorded in the source pass.]
