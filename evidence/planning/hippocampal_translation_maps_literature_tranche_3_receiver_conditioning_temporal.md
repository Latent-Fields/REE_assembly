# Hippocampal Translation Maps — Literature Tranche 3: receiver conditioning, CA1→entorhinal output, and temporal relations

**Date:** 2026-09-10
**Status:** targeted literature synthesis closing three named campaign debts. No claim registration, promotion or demotion; no experiment queued or implemented; no substrate change.
**Parent:** [campaign scaffold](hippocampal_translation_maps_biology_campaign_20260909.md)
**Prior tranches:** [tranche 1](hippocampal_translation_maps_literature_tranche_1.md), [tranche 2 — CA1 transformation mechanics](hippocampal_translation_maps_literature_tranche_2_ca1_transformation.md)
**Parent adjudication:** `docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md` (E-numbered matrix; this tranche extends it and does not renumber it)
**Sibling supplement:** `docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md` (assay B / replay maintenance)

**Debts addressed** (adjudication §9 numbering):

| Debt | Statement in the adjudication | Status after this tranche |
|---|---|---|
| **2** | Receiver state versus cue identity: content-matched interventions on the receiving population, not only task/query switches or projection labels | **Open, but now precisely bounded** — a seven-way taxonomy of what the literature actually manipulates, and an explicit demonstration that none of it holds retrieved content and cue constant while varying receiver state |
| **3** | CA1→EC reconstruction versus trigger/comparison; Butola et al. publication status and controls | **Butola resolved; question partly resolved** — peer-reviewed status and controls verified below; the four alternatives are now ranked, with *reconstruction* identified as the one with neither direct support nor direct refutation |
| **6** | Temporal relations: dedicated time-cell / episode-boundary / nonspatial causal-transfer tranche | **Substantially closed for coding and causal necessity; still open for temporal-frame mediation** |

---

## 1. Bottom line, one paragraph per question

**Q1 — does receiver state change the required transformation, with retrieved content and cue identity held constant?** No located study performs this manipulation. Seven neighbouring literatures were separated (§4). Six of them *permit* receiver conditioning without discriminating it. The seventh — optogenetic reactivation of a context engram driving mPFC context reinstatement and rule application rather than a motor output ([Julian et al. 2026](#t3-10), preprint) — is the most discriminating result located, and it points the **other** way: the hippocampal message behaves as a frame/rule selector whose downstream mapping is supplied by the receiver and the trial cue. MECH-547's confirming signature (`T(A,B) > T(A)` at matched capacity, destroyed by receiver-state permutation) has no biological counterpart at all, so it must be earned in assay A rather than imported.

**Q2 — does CA1→entorhinal output reconstruct, trigger native completion, compare, or select a frame?** Ranked by current direct support: **trigger + native completion** and **comparison/coincidence gating** are both directly supported; **frame selection** is real but is demonstrably implemented upstream of the CA1→EC synapse (CA1 input balance, [Qian et al. 2025](#t3-14)) and by third-party gates ([Kim et al. 2026](#t3-08)); **reconstruction** — the inherited McClelland–Goddard reading that tranche 2 §2 already flagged as theoretical in origin — remains untested in either direction. The biggest movement in this pass is Butola et al.: hippocampal input to EC layer 2/3 drives predominantly *feed-forward inhibition* and yields spike output only when paired with cortical layer 1 input. That is the synaptic signature of coincidence-gated comparison, not of pattern reinstatement.

**Q3 — what do time cells, episode boundaries and nonspatial causal transfer add beyond spatial reference-frame evidence?** Three genuine additions and two non-additions. They add (i) a second, *dissociable* frame with its own circuit-specific causal lever and its own negative result; (ii) a *segmentation* variable that is not a coordinate at all, sitting on top of a continuous drift whose origin appears intrinsic; (iii) causal transfer in tasks with no spatial or even multimodal content, carrying the local-competence control the campaign keeps asking for. They do **not** add receiver-conditioning evidence, and they do **not** yet supply temporal-frame *mediation* in the sense R2 requires. One finding transfers directly into the assay-B thread and was not visible from the spatial literature: **two codes in one CA1 population can drift at different rates** ([Taxidis et al. 2020](#t3-22)).

---

## 2. Verification: Butola et al., the direct hippocampus→entorhinal feedback circuit

The adjudication (§9 debt 3) recorded this as a 2023 Research Square preprint whose "publication/version and detailed controls need follow-up before it bears load." Both halves are now discharged, with caveats that are themselves load-bearing.

### 2.1 Publication status — resolved, peer-reviewed

<a id="t3-01"></a>**T3-01.** Butola T, Hernández-Frausto M, Blankvoort S, Flatset MS, Peng L, Hairston A, Johnson CD, Elmaleh M, Amilcar A, Hussain F, Clopath C, Kentros C, Basu J. *Hippocampus shapes entorhinal cortical output through a direct feedback circuit.* **Nature Neuroscience** 28(4):811–822, April 2025 (epub 2025-02-18). DOI [10.1038/s41593-025-01883-9](https://doi.org/10.1038/s41593-025-01883-9). **PMID 39966537**, indexed for MEDLINE.

Preprint of record: Res Sq `rs.3.rs-3270016`, posted 2023-08-23; PMID 37674706; PMCID [PMC10479401](https://pmc.ncbi.nlm.nih.gov/articles/PMC10479401/). PubMed carries the explicit reciprocal `Update in` / `Update of` linkage, so the two records are the same work and should not be double-counted.

**The scope narrowed during review, and the narrowing is informative.** The preprint was titled "Hippocampus shapes *cortical sensory output and novelty coding* through a direct feedback circuit"; the published title is "Hippocampus shapes *entorhinal cortical output*". The preprint's central behavioural claim — that the pathway "provides an important novelty signal during behavior for coding objects and their locations" — is replaced in the published abstract by a **pathway dissociation**: hippocampal inputs to layer 5 versus layer 2/3 support object memory **encoding versus recall** respectively. The published version also adds a **two-photon axonal imaging** experiment during navigation (hippocampal suppression reduces spatially tuned cortical axonal activity) that does not exist in the preprint. Two author additions (Johnson CD, Amilcar A) are consistent with added experiments.

### 2.2 Controls — audited in the open preprint; published version NOT independently audited

The published methods are paywalled and were not retrieved in this pass. What follows is audited from the open preprint full text and should be read as establishing the *anatomical and circuit* claims, which are common to both versions, and **not** as an audit of the added published experiments.

| Control class | What was actually done (preprint version) |
|---|---|
| Anterograde specificity | ChR2-eYFP in CA1 pyramidal neurons, replicated across three further serotypes (AAV2.1, 2.2, 2.9) so the projection is not a serotype artefact |
| Retrograde specificity | Monosynaptic rabies with TVA-2A-rabies-G restricted to layer 3 principal neurons, limiting spread to one upstream neuron |
| Monosynapticity | TTX + 4-AP isolation. **18/22 (81.8%) EC L5 neurons** but only **9/22 (40.9%) EC L2/3 neurons** received direct monosynaptic hippocampal input |
| Off-target infection | Animals showing any viral infection in EC cells were excluded from quantification |
| Opsin function | Somatic photostimulation confirming large sustained photocurrent before inclusion |
| Behavioural control group | JAWS-KGC-GFP cohort vs **EGFP-only** cohort, identical 625 nm / 20 Hz / 20 ms illumination |
| Behavioural dissociation | Barnes maze **spared** (p = 0.9835); novel object recognition impaired (index 0.60 → 0.35, p < 0.0001); novel object location impaired but marginally (0.60 → 0.49, **p = 0.0475**) |

### 2.3 What it can and cannot bear

**Can bear.** (a) A direct, monosynaptic hippocampus→EC layer 2/3 projection exists, in parallel with the canonical disynaptic layer 5 route — this genuinely revises the canonical output diagram, which is what tranche 2 §11 question 2 was asking about. (b) The layer 2/3 arm's dominant postsynaptic effect is **feed-forward inhibition**, converting to spike output only under **repetitive pairing with cortical layer 1 input** (heterosynaptic plasticity), while layer 5 shows homosynaptic potentiation. (c) A within-animal, task-level dissociation: spatial recall spared, object-novelty tasks impaired.

**Cannot bear.** (i) The direct L2/3 connection is a **minority** connection in the audited sample (41%), so "the hippocampus writes to L2/3" overstates it. (ii) **Nothing in the study decodes what CA1 sends or measures whether the EC target reproduces a hippocampal or a prior cortical pattern** — so it is silent on reconstruction, in either direction. (iii) The NOL effect is marginal by the study's own statistic. (iv) The two-photon result is a *suppression* experiment showing loss of spatially tuned axonal activity; that is a permissive/gain contribution, not content reinstatement. (v) The encoding-versus-recall dissociation rests on published-version experiments whose controls were not audited here.

**Net effect on the campaign.** Butola et al. upgrades tranche 2 §7's comparator/mismatch rival from "anatomically well placed" to "synaptically demonstrated on the *output* side as well as the input side", and it does so with a peer-reviewed record. It does not license a hippocampal-decoder reading, and it does not license a receiver-conditioning reading either: pairing-dependence is conditioning on **coincident input**, which is a property of the synapse, not a read of the receiver's latent state.

---

## 3. Vocabulary: five things this tranche keeps apart

The campaign rule is that "gated on X" is only well-formed if X is named precisely. The same applies here. Every row in §4–§6 is labelled with which of these it establishes, and the operational test that would upgrade it.

| Label | What it means | What upgrades it to the next rung |
|---|---|---|
| **Projection identity** | A fixed anatomical channel exposes a particular signal to a particular target. No state variable is read. | Show the *same* channel carries different content under different states with input matched. |
| **Task state** | A variable shared by sender, receiver and behaviour changes the observed coupling. | Dissociate the state variable's effect on the sender from its effect on the receiver. |
| **Cue selection** | The current cue/query determines *which* stored item is exposed; the transformation applied to it is unchanged. | Hold the retrieved item constant and show the transformation itself changes. |
| **Temporal precedence** | One population's activity leads another's, or a phase window predicts efficacy. | Perturb the timing while matching event count, magnitude and content. |
| **Causal receiver use** | Perturbing the pathway changes a behaviour that demonstrably requires the receiver. | Show the receiver is necessary for that behaviour independently of the pathway manipulation. |

A sixth distinction is forced by this tranche's evidence and is not in the campaign's original list:

| **Receiver-originated modulation** | The receiver alters the *sender* (top-down gain, disinhibition, gating) rather than the sender tailoring its output to the receiver. |

This is the confound that most cheaply masquerades as receiver conditioning, and it now has a clean biological instance ([Malik et al. 2022](#t3-05)).

---

## 4. Q1 — receiver state versus cue identity

### 4.1 Evidence rows

Access codes follow the adjudication: `T` full text / results inspected, `A` abstract or primary bibliographic record only, `M` model, `PP` preprint. Most rows here are `A`: records were retrieved via PubMed E-utilities `efetch` and publisher/PMC landing pages, not by line-by-line methods audit. This is a real resolution limit and is restated in §9.

| ID | Study | Manipulation | Which label (§3) | Discriminates or merely permits receiver conditioning | Access |
|---|---|---|---|---|---|
| <a id="t3-02"></a>**T3-02** | Ciocchi, Passecker, Malagon-Vina, Mikus & Klausberger (2015), *Selective information routing by ventral hippocampal CA1 projection neurons.* [DOI 10.1126/science.aaa3245](https://doi.org/10.1126/science.aaa3245) | Optogenetic identification of vCA1 neurons by projection target (PFC / NAc / amygdala) during anxiety and goal tasks | **Projection identity** | **Permits.** A fixed channel selecting different content requires no receiver-state read. This is the assay-A "fixed partner-specific route" comparator in biological form. | A |
| <a id="t3-03"></a>**T3-03** | Kitanishi, Umaba & Mizuseki (2021), *Robust information routing by dorsal subiculum neurons.* [DOI 10.1126/sciadv.abf1913](https://doi.org/10.1126/sciadv.abf1913) (adjudication E36) | Projection-identified subicular neurons; target-related theta/SWR timing | **Projection identity + temporal precedence** | **Permits.** Place coding is uniform across targets while speed/trajectory coding is target-biased — i.e. partial, not complete, segregation. | A |
| <a id="t3-04"></a>**T3-04** | Pettit, Yuan & Harvey (2022), *Hippocampal place codes are gated by behavioral engagement.* Nat Neurosci 25:561–566. [PMID 35449355](https://pubmed.ncbi.nlm.nih.gov/35449355/) | Voluntary task disengagement while the mouse keeps running the *identical* virtual maze — sensory cues and locomotion preserved | **Task state, acting on the SENDER** | **Discriminates — against a naive receiver reading.** An internal state can degrade the sender's code with inputs matched. Any receiver-state effect must be shown not to be this. | A |
| <a id="t3-05"></a>**T3-05** | Malik, Li, Schamiloglu & Sohal (2022), *Top-down control of hippocampal signal-to-noise by prefrontal long-range inhibition.* Cell 185:1602–1617. [PMID 35487191](https://pubmed.ncbi.nlm.nih.gov/35487191/) | Monosynaptic long-range GABAergic PFC→hippocampus projections preferentially inhibiting VIP interneurons; bidirectional manipulation | **Receiver-originated modulation** | **Discriminates the direction.** The receiver changes the sender's SNR for object-location encoding. This is receiver→sender gain control, the opposite of `T(A,B)`. | A |
| <a id="t3-06"></a>**T3-06** | Gonzalez et al. (2026), *Subspace communication in the hippocampal–retrosplenial axis.* [DOI 10.1038/s41586-026-10481-z](https://doi.org/10.1038/s41586-026-10481-z) (adjudication E06) | Multi-area recording; partial CCA partner subspaces varying with experience and brain state | **Task state** | **Permits.** State-indexed subspaces weaken "one globally fixed alignment" (relevant to MECH-537) but cannot separate receiver state from a shared state driving both endpoints. | A |
| <a id="t3-07"></a>**T3-07** | MacDowell, Libby, Jahn, Tafazoli, Ardalan & Buschman (2025), *Multiplexed subspaces route neural activity across brain-wide networks.* Nat Commun 16:3359. [PMID 40204762](https://pubmed.ncbi.nlm.nih.gov/40204762/) | Cortex-wide imaging + high-density recording in 8 regions; alignment of local activity to a subspace-network dimension predicts inter-regional propagation | **Projection identity generalised — receiver-IDENTITY conditioning** | **Discriminates identity from state.** One region simultaneously serves multiple overlapping downstream networks; geometry within the sender selects which. Conditioning on *who is listening* need not involve *what state they are in*. | A |
| <a id="t3-08"></a>**T3-08** | Kim, Suh, So et al. (2026), *A septo–entorhinal GABAergic pathway that enables switching between episodic memories.* Nat Neurosci 29:1439–1451. [PMID 42056598](https://pubmed.ncbi.nlm.nih.gov/42056598/) | Inactivating medial-septum GABAergic projections to MEC after memory updating | **Cue selection, driven by a THIRD PARTY** | **Discriminates the locus.** Behaviour reverts to the pre-update memory and CA1 population activity switches back to the pre-update pattern. Which memory is expressed is set by a pathway that is neither sender nor receiver. | A |
| <a id="t3-09"></a>**T3-09** | Gobbo et al. (2025), *Hippocampal reactivation of planned trajectories is required for effective goal choice in an allocentric memory task.* bioRxiv `2025.05.10.653115` | Optogenetic dCA1 inactivation in the startbox; allocentric vs egocentric training in the **same arena with the same cues and the same motor demands**; GFP controls, within-subject crossover, cue-masking and 180° rotation validation | **Causal receiver use, conditioned on task strategy** | **Discriminates necessity from availability.** Same sender, same environment: hippocampal reactivation is required for allocentric choice and not for egocentric choice. Closest existing instrument to the target question — but the manipulation is at the sender and the consumer population is never identified. | T/PP |
| <a id="t3-10"></a>**T3-10** | Julian, Kaminsky, Tank & Brody (2026), *Hippocampal engrams configure prefrontal context representations to guide flexible decisions.* bioRxiv `2026.07.06.732916`, [PMID 42465509](https://pubmed.ncbi.nlm.nih.gov/42465509/) | Activity-dependent tagging of Pro- or Anti-context dentate ensembles; optogenetic reactivation on 30% of randomly selected trials with simultaneous mPFC recording (296 ± 82 units/session); Cre-negative and dark-tagged controls | **Cue selection + causal receiver use** | **Most discriminating row in this tranche — and it favours the simpler account.** A fixed reactivated hippocampal message reinstates *context* in mPFC within hundreds of ms and makes the animal apply the tagged **rule**, producing **opposite motor actions** depending on the trial's visual guide. The sender selects a frame; the receiver plus the cue supply the mapping. | T/PP |
| <a id="t3-11"></a>**T3-11** | Nitzan et al. (2020), *Propagation of hippocampal ripples to the neocortex by way of a subiculum-retrosplenial pathway.* [DOI 10.1038/s41467-020-15787-8](https://doi.org/10.1038/s41467-020-15787-8) (adjudication E18) | Optogenetic manipulation of bursty subicular cells; state-dependent coupling reported | **Temporal precedence + task/brain state** | **Permits.** State-dependence of coupling efficacy is a gain effect on a fixed pathway. | A |
| <a id="t3-12"></a>**T3-12** | Todorova & Zugaro (2019), *Isolated cortical computations during delta waves support memory consolidation.* Science 366:377–381. [PMID 31624215](https://pubmed.ncbi.nlm.nih.gov/31624215/) | Cortical cells implicated in learning form assemblies during delta waves in response to ripple-locked hippocampal reactivation, selectively during endogenous or induced consolidation | **Temporal precedence + receiver state (cortical delta)** | **Permits, and is the best available biological instance of a receiver-state *window*.** The cortical state determines whether the message is acted on — but it changes *whether*, not *which transformation*. | A |

### 4.2 Adjudication for Q1

1. **No located study holds retrieved content and cue identity constant while varying receiver state.** This was searched for directly (§9 stream 1) and returned nothing. The debt is not closed; it is now specified well enough to be recognised if it appears.
2. **The strongest evidence bears against the strong reading of R3 / MECH-547.** T3-10 is the only row in which the sender's message is *experimentally fixed* and the downstream mapping is allowed to vary. The result is that the mapping varies with the cue, at the receiver, while the hippocampal message behaves as a rule/context selector. The campaign's own split of R3 (adjudication §5, "cue-conditioned retrieval, fixed partner-specific exposure, and receiver-state-conditioned transformation — the first two have stronger biological neighbours than the third") is confirmed and, with T3-10, sharpened from "weaker neighbours" to "the one direct test points the other way."
3. **Two confounds now have named biological instances and must be controls, not caveats.** Sender-side state gating (T3-04) and receiver-originated modulation (T3-05). Assay A currently has neither.
4. **Receiver *identity* and receiver *state* are separable and are currently conflated.** T3-07 makes conditioning-on-who-is-listening a live, measured mechanism distinct from conditioning-on-their-state. Assay A's single "within-query receiver permutation" control cannot tell them apart.
5. **The adjudication §2 safeguard now has a biological analogue.** "A receiver-conditioned bridge can recover performance by introducing missing information from the receiver" — in T3-10 the receiver and the cue genuinely supply the action mapping. Sender-only decoding and conditional joint decoding must stay separately reported.

---

## 5. Q2 — what CA1→entorhinal output does

### 5.1 The four alternatives, stated so they can be scored separately

| Alternative | Committing prediction |
|---|---|
| **Reconstruct** | The EC/cortical target's population state after hippocampal output approximates the state that obtained at encoding, and the approximation depends on the *content* of the hippocampal message. |
| **Trigger native completion** | Hippocampal output is necessary to initiate the target's own attractor dynamics; the resulting target pattern is generated locally and can be evoked by other means. |
| **Compare** | The target's response is a function of the *agreement* between hippocampal input and its own current input, not of the hippocampal input alone. |
| **Select a frame** | Hippocampal output sets which of several available codes/relations the target expresses, without specifying its content. |

### 5.2 Evidence rows

| ID | Study | Bears on | Verdict | Access |
|---|---|---|---|---|
| **T3-01** | Butola et al. (2025), Nat Neurosci 28:811–822 — §2 above | **Compare** (primary), routing | **Discriminates for comparison.** L2/3 spike output requires repetitive pairing with cortical L1 input; the dominant unpaired effect is feed-forward inhibition. Silent on reconstruction: no decoded content, no target-geometry measure. | T/PP + A |
| <a id="t3-13"></a>**T3-13** | Rozov, Rannap, Lorenz, Nasretdinov, Draguhn & Egorov (2020), *Processing of hippocampal network activity in the receiver network of the medial entorhinal cortex layer V.* J Neurosci 40:8413–8425. [PMID 32978288](https://pubmed.ncbi.nlm.nih.gov/32978288/) | Routing within the receiver | **Discriminates against a homogeneous EC receiver.** LVa and LVb excitatory cells and fast-spiking interneurons all receive direct hippocampal input; LVa↔LVb connections are sparse and local processing is **asymmetric**, favouring far-projecting LVa over locally re-entrant LVb. "The receiver" is at least two receivers with different jobs. | A |
| <a id="t3-14"></a>**T3-14** | Qian, Li & Magee (2025), Nat Neurosci 28:1486–1496 (adjudication E04; tranche 2 §6) | **Select a frame** | **Supports frame selection — upstream.** Space- vs goal-referenced input ratio within CA1 determines the expressed frame. The selection happens *before* the output synapse, so it is not evidence that CA1→EC selects a frame for EC. | A |
| <a id="t3-15"></a>**T3-15** | Kitamura, Ogawa, Roy, Okuyama, Morrissey, Smith, Redondo & Tonegawa (2017), *Engrams and circuits crucial for systems consolidation of a memory.* Science 356:73–78. [PMID 28386011](https://pubmed.ncbi.nlm.nih.gov/28386011/) | **Trigger** vs **reconstruct** | **Discriminates against persistent reconstruction.** MEC layer Va — the deep-layer recipient of hippocampal output — is necessary during acquisition for prefrontal engram maturation and **dispensable for remote retrieval** once the engram is mature. A channel that can be removed after training is a training signal, not a reconstruction channel. | A |
| <a id="t3-16"></a>**T3-16** | Tanaka et al. (2014) (adjudication E07) | **Trigger** | **Permits both trigger and reconstruct.** Silencing the encoding-tagged CA1 ensemble impairs retrieval and cortical reactivation; necessity does not identify the operation. | A |
| <a id="t3-17"></a>**T3-17** | Cowansage et al. (2014); de Sousa et al. (2019) (parent supplement §5.3) | **Trigger + native completion** | **Discriminates for local completion.** A tagged retrosplenial ensemble can drive behaviour and downstream amygdala activation with the hippocampus inactivated; repeated RSC-ensemble activation produces remote-like retrieval. Sufficiency of the target's own dynamics is established. | A |
| **T3-08** | Kim et al. (2026) — §4.1 | **Select a frame** | **Supports frame selection — but by a third party.** A septo-entorhinal gate, not the hippocampal output synapse, switches which memory the CA1/EC system expresses. | A |
| <a id="t3-18"></a>**T3-18** | Sürmeli et al. (2015), *Molecularly defined circuitry reveals input-output segregation in deep layers of the medial entorhinal cortex*, [PMC4675718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4675718/); Ohara et al. (eLife 2021; Cell Reports 2023) | Structural constraint | **Permits all four.** EC L5a is the sole origin of long-range telencephalic output; L5b is the re-entry limb to superficial layers. The anatomy separates "send onward" from "re-enter", which any of the four operations could exploit. | A |
| <a id="t3-19"></a>**T3-19** | McClelland & Goddard (1996) (adjudication E37); Schapiro et al. (2017) (E38) | **Reconstruct** | **Model origin, not evidence.** Tranche 2 §2 established this; nothing located in this pass changes it. | M |

### 5.3 Adjudication for Q2

**Ranking by direct support:** *trigger + native completion* ≈ *compare* > *select a frame* (real, but implemented upstream and by third-party gates) > *reconstruct* (**no direct support and no direct refutation**).

Three consequences the campaign should carry forward.

1. **"Reconstruction is untested" is not "reconstruction is refuted."** The measurement that would settle it does not exist in the located literature: decode the hippocampal message, perturb it, and measure the EC target population's geometry against its encoding-time geometry with content matched. Recording this as a debt is more honest than scoring it as weakened.
2. **The receiver is plural.** T3-13's LVa/LVb asymmetry plus T3-01's L5-vs-L2/3 dissociation mean "CA1→EC" names at least three distinct interfaces with different synaptic signs, different plasticity rules and — in Butola's behaviour — different task roles (encoding vs recall). Tranche 2 §5 already warned that "CA1 representation" is too coarse a unit; the same is now true of "the EC receiver". An assay with one sender and one receiver cannot represent this, and assay A's existing **two-interface** requirement (inherited from MECH-540) is the right structure to carry it.
3. **Coincidence-gating is not receiver conditioning.** Butola's pairing dependence conditions on *simultaneous input*, a synaptic property. Conditioning on the receiver's *latent state* would require the same input to be transformed differently under different receiver states. The distinction matters because a synthetic bridge that gates on input coincidence would score as MECH-547 support under a loose reading.

---

## 6. Q3 — temporal relations: time cells, episode boundaries, nonspatial causal transfer

### 6.1 What is added — three things

**(A) A second, dissociable frame, with its own causal lever and its own negative result.**

| ID | Study | Contribution |
|---|---|---|
| <a id="t3-20"></a>**T3-20** | MacDonald & Tonegawa (2021), *Crucial role for CA2 inputs in the sequential organization of CA1 time cells supporting memory.* PNAS 118:e2020698118. [PMID 33431691](https://pubmed.ncbi.nlm.nih.gov/33431691/) | **The causal anchor.** In a task with an explicit *spatial coding phase* (route traversal) and *temporal coding phase* (fixed-location 10 s delay), cell-type-specific optogenetic inhibition of dCA2→dCA1 degrades time-cell coding during the delay **and** impairs the subsequent memory-guided choice. A frame-specific circuit lever inside one task — exactly the shape assay A wants for frames. |
| <a id="t3-21"></a>**T3-21** | Sabariego, Schonwald, Boublil, Zimmerman, Ahmadi, Gonzalez, Leibold, Clark, Leutgeb & Leutgeb (2019), *Time cells in the hippocampus are neither dependent on medial entorhinal cortex inputs nor necessary for spatial working memory.* Neuron 102:1235–1248. [PMID 31056352](https://pubmed.ncbi.nlm.nih.gov/31056352/) | **The negative that keeps this honest.** MEC lesions impair spatial working memory while time cells and stem trajectory-coding cells are indistinguishable from controls. Two lessons: the temporal frame is not the spatial pipeline running on a clock; and **presence of time cells does not license inferring behavioural use** — the same encoded ≠ used gap the campaign's operative distinction already names. It also directly conflicts with earlier reports of MEC-inactivation-induced time-cell destabilisation, so the temporal frame's input dependence is itself contested. |
| <a id="t3-22"></a>**T3-22** | Taxidis, Pnevmatikakis, Dorian, Mylavarapu, Arora, Samadian, Hoffberg & Golshani (2020), *Differential emergence and stability of sensory and temporal representations in context-specific hippocampal sequences.* Neuron 108:984–998. [PMID 32949502](https://pubmed.ncbi.nlm.nih.gov/32949502/) | **Transfers directly into the assay-B thread.** In the *same* CA1 sequences, odour cells were reliably activated with stable fields across trial-structure changes and across days, while time cells were sparse, dynamic, and remapped under both. **Two codes in one population with different drift rates.** "The sender drifted" is therefore not a single fact about a population, and a drift manipulation that treats it as one is under-specified. |
| <a id="t3-23"></a>**T3-23** | Umbach, Kantak, Jacobs, Kahana, Pfeiffer, Sperling & Lega (2020), PNAS 117:28463. [PMID 33109718](https://pubmed.ncbi.nlm.nih.gov/33109718/); Reddy et al. (2021), J Neurosci 41:6714 | **Cross-species anchoring.** Human hippocampal and entorhinal time cells whose activity predicts the temporal organisation of recall; temporal context modulates firing and signals context change during gaps. Observational. |
| <a id="t3-24"></a>**T3-24** | Tsao, Sugar, Lu, Wang, Knierim, Moser & Moser (2018), *Integrating time from experience in the lateral entorhinal cortex.* Nature 561:57–62. [PMID 30158699](https://pubmed.ncbi.nlm.nih.gov/30158699/) | **A temporal signal with a specific source.** Experience-derived time is robustly encoded in LEC population state across seconds-to-hours, and **not** comparably in MEC or CA3/CA1. Constraining behaviour reduces across-trial time coding and improves within-trial time coding. Locates a candidate temporal *sender* — but the hippocampus's *use* of it is inferred, not measured. |

**(B) A segmentation variable that is not a coordinate, on top of a drift that looks intrinsic.**

| ID | Study | Contribution |
|---|---|---|
| <a id="t3-25"></a>**T3-25** | Kanter, Lykken, Polti, Moser & Moser (2025), *Event structure sculpts neural population dynamics in the lateral entorhinal cortex.* Science 388:eadr0927. [PMID 40570128](https://pubmed.ncbi.nlm.nih.gov/40570128/) | **Two findings, both campaign-relevant.** (i) LEC population activity drifts continuously along a one-dimensional manifold during *all* behaviours and states **including sleep**, pointing to an intrinsic origin. (ii) In wake, event boundaries produce **discrete shifts** segmenting activity into temporal units; recurring task structure adds orthogonal encoding directions. Finding (i) is a **rival to replay-dependent maintenance that the spatial literature did not surface**: drift that continues through sleep at a rate set intrinsically is not obviously a thing offline activity is repairing. |
| <a id="t3-26"></a>**T3-26** | Zheng, Schjetnan, Yebra, Gomes, Mosher, Kalia, Valiante, Mamelak, Kreiman & Rutishauser (2022), *Neurons detect cognitive boundaries to structure episodic memories in humans.* Nat Neurosci 25:358–368. [PMID 35260859](https://pubmed.ncbi.nlm.nih.gov/35260859/) | **Boundaries as an explicit trade-off, not a free gain.** Human MTL *boundary cells* respond to soft and hard boundaries; *event cells* only to hard. Boundary-induced neural state change during encoding **predicted better recognition but worse event-order memory**. Any REE segmentation mechanism should be expected to pay this cost, and an assay that measures only one side will misread it. |
| <a id="t3-27"></a>**T3-27** | Sun, Yang, Martin & Tonegawa (2020), *Hippocampal neurons represent events as transferable units of experience.* Nat Neurosci 23:651–663. [PMID 32251386](https://pubmed.ncbi.nlm.nih.gov/32251386/) | **A relational address that is not a spatial coordinate, and it transfers.** Event-specific rate remapping (ESR) cells remain lap-specific when maze length is unpredictably altered, and the ESR pattern is **re-used when the maze geometry is changed square→circle**. ESR activity is separately manipulable from spatial activity. This is the closest biological instance in the campaign of R1's "shared relational address" surviving a change of the substrate it was learned on. |
| <a id="t3-28"></a>**T3-28** | Clewett, Huang & Davachi (2025), *Locus coeruleus activation "resets" hippocampal event representations and separates adjacent memories.* Neuron 113:2521–2535. [PMID 40482639](https://pubmed.ncbi.nlm.nih.gov/40482639/) | **A driver, and a non-monotonicity.** fMRI + neuromelanin + pupillometry: boundaries trigger pupil-linked arousal and LC responses predicting later memory separation, with DG temporal pattern separation correlating with LC response. Elevated *background* LC markers correlate with **reduced** boundary responses — hyperarousal disrupts segmentation. Correlational in humans; the inverted-U is the transferable part. |

**(C) Causal transfer with no spatial content, carrying the local-competence control.**

| ID | Study | Contribution |
|---|---|---|
| <a id="t3-29"></a>**T3-29** | Fortin, Agster & Eichenbaum (2002), *Critical role of the hippocampus in memory for sequences of events.* Nat Neurosci 5:458–462. [PMID 11976705](https://pubmed.ncbi.nlm.nih.gov/11976705/) | **The cleanest relation-vs-content dissociation available.** Hippocampal lesions severely and selectively impair memory for the *order* of a series of odours while recognition of the same odours is intact. Old, causal, nonspatial, and still not superseded for this dissociation. |
| <a id="t3-30"></a>**T3-30** | Talaron, Holmes, Ferreira & Coutureau (2026), *Chemogenetic disruption of the hippocampus impairs gustatory preconditioning in rats.* Neurobiol Learn Mem 226:108187. [PMID 42336191](https://pubmed.ncbi.nlm.nih.gov/42336191/) | **Strongest recent nonspatial causal-transfer row.** Unimodal *gustatory* preconditioning — no spatial and not even multimodal content. Hippocampal disruption during either preconditioning **or** test selectively impairs mediated aversion to A while leaving direct conditioned aversion to X intact. The spared direct association is a **within-subject local-competence control**, phase-resolved across encoding and retrieval — the control structure the campaign repeatedly asks for and rarely finds. |
| <a id="t3-31"></a>**T3-31** | Barron, Reeve, Koolschijn, Perestenko, Shpektor, Nili, Rothaermel, Campo-Urriza, O'Reilly, Bannerman, Behrens & Dupret (2020), *Neuronal computation underlying inferential reasoning in humans and mice.* Cell 183:228–243. [PMID 32946810](https://pubmed.ncbi.nlm.nih.gov/32946810/) | **Offline coactivation composing a NEW relation.** A hippocampal prospective code forecasts temporally structured learned associations during inference; during rest, SWR coactivation represents **inferred** relationships including reward — links between events never observed together. In humans the inferred outcome appears in mPFC and putative dopaminergic midbrain. This is offline activity *constructing* a relation rather than rehearsing one, which bears on R4 and on the provenance branch. |
| <a id="t3-32"></a>**T3-32** | Aronov, Nevers & Tank (2017) (adjudication E12) | Nonspatial continuum coding; no consumer measured. Permits. |

### 6.2 What is NOT added

1. **No receiver conditioning.** Every row in §6 measures sender-side coding or whole-hippocampus necessity. None identifies the consumer population, so the temporal literature contributes nothing to debt 2.
2. **No temporal-frame *mediation* in the R2 sense.** R2 requires a *measured transform between frames* consumed by another system. T3-24 locates a candidate temporal sender (LEC) and T3-20 gives a frame-specific causal lever inside the hippocampus, but no located study measures a temporal-frame conversion being used by an identified receiver. **Debt 6 is therefore closed for temporal/nonspatial coding and causal necessity, and remains open for temporal-frame mediation.** The campaign's original wording — "time-frame mediation has less depth than spatial-frame mediation here" — was accurate and stays accurate at the mediation rung specifically.
3. **No warrant to treat time as "just another axis."** T3-21 (MEC lesion spares time cells but impairs spatial working memory) and T3-22 (different drift rates for temporal vs sensory codes in one population) both say the temporal frame has different dependencies and different dynamics from the spatial one.

---

## 7. Three-layer separation: established / computational inference / REE-specific hypothesis

Required by the campaign's deliverable 5. Each row keeps the three levels apart; only the third column is a REE proposition, and none of it is registered.

| Topic | **Established biological result** | **Computational inference** | **REE-specific hypothesis** |
|---|---|---|---|
| Receiver conditioning (R3 / MECH-547) | Hippocampal output is routed by projection identity (T3-02, T3-03), gated by brain and task state (T3-06, T3-11, T3-12), modulated top-down by its own targets (T3-05), and can be degraded at the sender by internal state alone (T3-04). A reactivated engram reinstates *context* downstream and drives *rule* application, not a motor output (T3-10). | A sender that serves several consumers can index its read-surface by who is listening (T3-07) or by shared task state; both are cheaper than reading the receiver's latent state. A frame/rule selector plus a receiver-local mapping reproduces the T3-10 phenotype without any `T(A,B)`. | `T(A,B) > T(A)` at matched capacity, with receiver-**state** permutation destroying the gain and the gain not attributable to information B already holds. **No biological counterpart exists.** Assay A carries this alone. |
| CA1→EC output (R2 / tranche 2 Q5) | Two parallel hippocampus→EC feedback routes with opposite postsynaptic signs and different plasticity rules; L2/3 output is coincidence-gated on cortical L1 input (T3-01). Deep-EC processing is asymmetric across LVa/LVb (T3-13). MEC Va is necessary for PFC engram maturation and dispensable for remote retrieval (T3-15). Cortical ensembles can complete and drive behaviour without the hippocampus (T3-17). | Comparison and trigger-plus-completion jointly explain the causal data with no inverse map. A decoder is required only if the target cannot generate the pattern itself — and T3-17 shows it often can. | A constrained bridge whose message is a *frame/rule selector* rather than a content vector suffices for held-out consumer use at frozen endpoints. Untested. |
| Temporal relations (R1/R2, debt 6) | Time cells exist in rodents and humans and their organisation is causally required for a memory-guided choice via a specific input (T3-20), yet they survive MEC lesion that impairs behaviour (T3-21). Boundaries produce discrete LEC state shifts on a continuous, sleep-persistent drift (T3-25) and a recognition-vs-order trade-off in humans (T3-26). Event units transfer across geometry (T3-27). Hippocampal disruption selectively abolishes inferred, never-directly-paired associations while sparing the direct ones (T3-29, T3-30, T3-31). | Segmentation is a discrete operation over a continuous latent trajectory, and event identity can act as an address that survives a change of the substrate it was learned on. Different codes in one population can carry different drift rates, so drift is a per-code property, not a population property. | An event/segment index belongs in the same frame factor as spatial reference frames, and is a candidate shared relational address. Untested; and the assay must measure both sides of the T3-26 trade-off. |

---

## 8. Which findings discriminate, and which merely permit

| Finding | Discriminates | What it rules out or ranks |
|---|---|---|
| T3-10 Julian 2026 (fixed engram message, opposite actions by cue) | **Yes — strongest in tranche** | Ranks *cue/frame selection + receiver-local mapping* above *sender-side receiver-conditioned transformation*. Preprint; not peer reviewed. |
| T3-01 Butola 2025 (L2/3 feed-forward inhibition, pairing-dependent output) | **Yes** | Ranks *compare* above *reconstruct* for the L2/3 arm. Silent on reconstruction as such. |
| T3-15 Kitamura 2017 (MEC Va dispensable for remote retrieval) | **Yes** | Rules out a *persistent* reconstruction channel; consistent with a training/trigger signal. |
| T3-17 Cowansage / de Sousa (cortical completion without hippocampus) | **Yes** | Establishes sufficiency of target-local completion; makes it a mandatory comparator, not a residual. |
| T3-04 Pettit 2022 (engagement gates place code, inputs matched) | **Yes — as a control** | Rules out inferring receiver conditioning from any state effect without a sender-side null. |
| T3-05 Malik 2022 (PFC→HPC long-range GABA) | **Yes — as a direction check** | Establishes receiver→sender modulation as a real, separate mechanism. |
| T3-07 MacDowell 2025 (multiplexed subspaces) | **Yes — partially** | Separates receiver-**identity** conditioning from receiver-**state** conditioning. |
| T3-21 Sabariego 2019 (time cells spared by MEC lesion) | **Yes — negative** | Rules out "time cells present ⇒ time cells used"; contests MEC-dependence of the temporal code. |
| T3-22 Taxidis 2020 (odour stable, time cells remap) | **Yes** | Rules out treating drift as a single population-level fact. |
| T3-25 Kanter 2025 (drift persists in sleep; boundaries are discrete shifts) | **Yes** | Adds an intrinsic-drift rival to replay-dependent maintenance, from outside the replay literature. |
| T3-26 Zheng 2022 (recognition↑, order↓ at boundaries) | **Yes** | Rules out reading segmentation as a free memory gain. |
| T3-30 Talaron 2026 (mediated aversion lost, direct spared) | **Yes** | Rules out a generic-performance account of the transfer deficit; nonspatial and unimodal. |
| T3-29 Fortin 2002 (order impaired, recognition intact) | **Yes** | Separates relation from content, causally, without space. |
| T3-08 Kim 2026 (septo-entorhinal switch) | **Partially** | Locates memory selection in a third-party gate rather than in either endpoint. |
| T3-09 Gobbo 2025 (allocentric yes, egocentric no) | **Partially** | Separates causal necessity from availability at matched environment and cues; consumer unidentified. Preprint. |
| T3-02, T3-03, T3-06, T3-11, T3-12, T3-13, T3-14, T3-16, T3-18, T3-23, T3-24, T3-27, T3-28, T3-31, T3-32 | **No — permit** | Each is compatible with two or more of the alternatives it is cited under. Listed here so they are not silently upgraded by accumulation. |

Fifteen of the thirty-two rows merely permit. That ratio is the honest summary of the state of this literature, and it is why §10 proposes amendments to an existing assay rather than a new family.

---

## 9. Minimal changes to assay A

**Boundary first: this section proposes no new experiment family, no new claim, no substrate work and no queue entry.** Assay A (adjudication §7A) already manipulates source-only bridge, index-plus-native-reinstatement, fixed partner-specific route, frame-conditioned bridge and receiver-state-conditioned bridge, with receiver permutation and a receiver-only arm. Four amendments follow from §4–§6. Three cost one arm each; one costs none.

**A1 — split the existing receiver permutation into *state* and *identity* permutation.** *(no new arm; one control becomes two)*
Assay A's "within-query receiver permutation" conflates permuting *which receiver* the message is aimed at with permuting *what state that receiver is in*. T3-07 makes receiver-identity conditioning a measured mechanism, and T3-02/T3-03 make fixed projection identity the standard biological alternative. A gain that survives state permutation but dies under identity permutation is **fixed routing**, which assay A currently scores as receiver conditioning. MECH-547's stated confirming signature depends on this distinction and does not currently name it.

**A2 — add a sender-state null.** *(one arm, or zero if folded into the frozen-endpoint probe schedule)*
Re-run the **source-only** bridge under each receiver state and require equivalence. T3-04 shows an internal state can degrade the sender's code with sensory input and movement matched; if `S(e)` differs across receiver states, any `T(A,B)` advantage is partly a sender effect. Use an equivalence test, not a non-significant difference — the same standard the parent supplement sets for assay B.

**A3 — add one *selector* rung to the existing bridge ladder.** *(one arm)*
Constrain the message to a low-cardinality discrete selector (a k-way frame/rule index) instead of a continuous vector, and score it on the same held-out consumer criterion. T3-10 is the motivation: a biologically fixed message that selects a rule, with the receiver and the cue supplying the mapping, reproduces flexible context-dependent behaviour. If the k-way selector plus the receiver's own query matches the continuous receiver-conditioned bridge on compositional holdouts, the strong reading of R3 is unnecessary at this interface. This is one more rung on MECH-538's existing complexity ladder, not a new design.

**A4 — extend the existing frame factor's level set to include temporal frames.** *(no new factor; more levels on one factor)*
Assay A already permutes reference frame. Add an **event/segment index** (T3-27's transferable event unit) and an **elapsed-time coordinate** (T3-24) as further levels of that same factor. This is the only cheap way to test whether the campaign's frame machinery generalises past spatial frames, which is debt 6's actual purpose. Two reporting requirements ride with it, both from §6: score **both** sides of the T3-26 trade-off (item recognition *and* order), and report drift **per code** rather than per population (T3-22).

**Reaffirmed, not new.** Report sender-only decoding, communication-surface decoding and conditional joint decoding separately. This is already in assay A's dependent variables; T3-10 makes the "the receiver supplied the information" confound concrete rather than hypothetical, so it should not be dropped for economy.

**Explicitly declined.** No receiver-conditioning experiment family; no time-cell or boundary substrate module; no CA1→EC analogue module; no change to assay B or C. Any implementation requires a separate governed decision after V3-EXQ-1010's outcome and the current pending reviews are resolved (adjudication §7 gate).

---

## 10. Search coverage, access limits and stopping rule

Targeted adversarial tranche, not a preregistered systematic review. Records were retrieved through PubMed E-utilities `efetch`/`esearch` (per the standing note that PubMed HTML is cookie-blocked and abstracts must come from E-utilities), publisher landing pages, PMC full text, and preprint servers. Streams explicitly run:

1. `receiver state hippocampal output transformation content held constant`, `gain field coordinate transform receiver state`, `manipulate receiver population state hippocampal retrieved content constant` — **returned nothing matching**; this is the basis for the §4.2(1) negative.
2. `projection-target-specific CA1 output coding`, `dorsal CA1 projections differential behaviour`, `subiculum information routing`, `CA1 collateralisation to multiple targets`.
3. `top-down prefrontal control of hippocampal gain`, `long-range GABAergic PFC hippocampus`, `behavioural engagement gates place code`.
4. `communication subspace task state dependent`, `multiplexed subspaces`, `hippocampal-prefrontal communication subspace`, `context-dependent communication subspace human`.
5. `hippocampus to entorhinal feedback layer 2/3`, `entorhinal layer Va Vb hippocampal output receiver network`, `entorhinal deep layer re-entry loop`, `MEC layer Va necessary retrieval`.
6. Exact-title and DOI resolution for Butola et al. across preprint and published versions, plus the preprint's control structure.
7. `time cells causal optogenetic`, `time cells not necessary`, `MEC lesion time cells`, `human time cells episodic`, `lateral entorhinal time from experience`.
8. `event boundary hippocampus causal`, `boundary cells human single unit`, `event structure entorhinal population dynamics`, `locus coeruleus event segmentation`, `transferable event units`.
9. `nonspatial causal transfer hippocampus`, `sensory preconditioning hippocampus inactivation`, `transitive inference hippocampus causal 2024-2026`, `memory for sequences of events lesion`, `inferential reasoning hippocampus SWR`.
10. `amnesia intact event segmentation` (negative-evidence sweep).

**Access limits, stated rather than papered over.** Most rows are `A`: bibliographic record and abstract via `efetch` plus publisher/PMC landing text, **not** a line-by-line methods or supplement audit. Full text was inspected for the Butola preprint (T3-01, controls in §2.2) and the two bioRxiv preprints (T3-09, T3-10). The **published** Butola methods are paywalled and were not audited. Three rows (T3-09, T3-10, and Butola's preprint) are preprints and are labelled as such wherever they carry weight; T3-10 is the single most discriminating row in the tranche and is *not peer reviewed*, which is the largest single fragility in §8.

**Stopping rule.** Discriminative coverage, per the campaign: for each of the three questions the principal positive streams, the serious alternatives and at least one counterexample or negative result are represented (Q1: T3-04, T3-05, T3-10; Q2: T3-15, T3-17; Q3: T3-21, T3-26). Coverage is sufficient to rank alternatives and to specify assay amendments. It is not sufficient to assert that no relevant paper exists.

---

## 11. Remaining debts

Mapped to the adjudication's §9 numbering where they continue an existing debt, and marked **NEW** where this tranche created one.

1. **(continues debt 2) Content-and-cue-matched receiver-state manipulation.** No located study varies receiver state while holding retrieved content and cue identity constant. The nearest instrument is T3-09's task-strategy contrast at matched environment and cues, but its manipulation is at the sender and it never identifies the consumer population.
2. **(continues debt 2) NEW — receiver identity versus receiver state.** T3-07 makes these separable and measured. No hippocampal study separates them, and no REE assay currently does either (see A1).
3. **(continues debt 2) NEW — sender-side state gating as a routine control.** T3-04 shows an internal state can degrade the sender with inputs matched. No located interareal study includes this null (see A2).
4. **(continues debt 3) Reconstruction is untested, not weakened.** No located study decodes the hippocampal message, perturbs it, and measures the EC target's population geometry against its encoding-time geometry with content matched.
5. **(continues debt 3) Published-version Butola controls.** The added two-photon experiment and the L5-vs-L2/3 encoding/recall dissociation were not audited beyond the abstract. Retrieve the published methods before this dissociation bears load.
6. **(continues debt 3) NEW — the receiver is plural.** L5a/L5b asymmetry (T3-13) plus the L5/L2/3 sign difference (T3-01) mean "CA1→EC" is at least three interfaces. No study treats them jointly with content matched.
7. **(closes the coding half of debt 6; opens its mediation half) Temporal-frame mediation.** A measured temporal-frame conversion consumed by an identified receiver does not exist in the located literature. T3-24 supplies a candidate sender; use is inferred.
8. **(NEW, feeds assay B / the parent supplement) Intrinsic drift as a maintenance rival.** T3-25 reports LEC drift continuing through sleep with an apparently intrinsic origin. The parent supplement's rival list (stable scaffold, receiver-local self-healing, cortical completion, ordinary rehearsal, local consolidation) does not include *drift that offline activity does not arrest*. It should.
9. **(NEW) Per-code drift rates.** T3-22 shows sensory and temporal codes in one CA1 population drift at different rates. No located study measures whether transfer-relevant drift and transfer-irrelevant drift separate this way at an interareal interface — which is precisely the condition assay B's Gate 0 must verify.
10. **(NEW) Segmentation trade-off.** T3-26's recognition-up/order-down result has no computational counterpart in the campaign's assay designs, all of which score a single transfer criterion.
11. **(continues debt 6) Nonspatial causal transfer beyond aversive/gustatory paradigms.** T3-30 is unimodal gustatory; T3-29 is odour order; T3-31 is reward inference. Appetitive-neutral, non-consummatory transfer with the same local-competence control is unrepresented.
12. **(continues debt 5) Replication of the newest geometry work.** T3-25 and T3-07 join E02/E05/E06/E28 in needing independent replication and audits of dimensionality estimators, subsampling and selection effects. Distinct paradigms are not replications of one mechanism.

---

## 12. Landing boundary

This tranche is literature synthesis and assay refinement. It registers no claim, promotes or demotes nothing, marks no experiment reviewed, mutates no queue, proposes no substrate change, and mints no evidence entry. The E-numbered matrix in the parent adjudication is not renumbered; rows here carry independent `T3-` identifiers. The four amendments in §9 are proposals against an existing assay design and require a separate governed decision, after V3-EXQ-1010's outcome and the current pending experiment reviews are resolved.

MECH-547 (receiver-conditioned translation) and MECH-548 (recurrent interface stability) remain `candidate` / `substrate_conditional`. Nothing here changes that, and §4.2(2) is a reason for continued caution about MECH-547's strong reading rather than a reason to act on it.
