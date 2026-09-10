# Assay C refined: developmental path at a matched mature interface

**Date:** 2026-09-10T07:18:43Z
**Status:** design specification and audit. **No claim registration, no queue mutation, no substrate build, no promotion.** Routing unchanged: V4/V5 developmental substrate.
**Audits:** [campaign adjudication](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) section 7C.
**Parents:** [campaign scaffold](hippocampal_translation_maps_biology_campaign_20260909.md); [developmental overcapacity thought](../../docs/thoughts/2026-09-08_developmental_overcapacity_pruning_sparse_interfaces.md) sections 7, 11, 12, 14.
**Lineage:** MECH-362 / Q-057 ([architecture compass](../../docs/architecture/developmental_pruning_and_sparse_memory_cognifold.md)), ARC-019, MECH-537-540, MECH-547/548, INV-105.
**Readiness base:** [developmental readiness investigation](developmental_readiness_investigation_2026-08-12.md) section 19, **read together with** the [developmental-life definition decision](developmental_life_definition_decision_2026-08-12.md), which answers its item 1.

---

## 1. What this document changes

Assay C as adjudicated is sound in its instinct and under-specified at exactly the three points where the result will be contested. This specification keeps its question, its routing and its strongest falsifier, and changes seven things.

| # | Finding in the adjudicated Assay C | Change |
|---|---|---|
| 1 | Manipulated variable says "separate structural pruning from inhibitory/activity sparsification" -- a two-way split, while the dossier's own section 3.5 makes a **three-way** one. | Section 3 below restores the third axis (interareal interface complexity) as the **dependent** variable and demotes the other two to manipulated/measured, with a clamp condition. |
| 2 | The decisive contrast is a **binary** B-vs-D (pruned versus reinitialised-final). | Replaced by a **rewind-depth ladder**. The binary cannot distinguish "the developmental path was necessary" from "the first fraction of it was", and the published prior says the second. Section 7. |
| 3 | No learning-rate/budget protocol for the from-scratch arm. | Matched-compute *and* matched-epoch reporting, matched schedule. This is the single commonest way to manufacture a false positive for "history matters". Section 6.3. |
| 4 | "Random pruning at matched density" is one control. | Two: matched **global** density and matched **per-layer** density profile. The layer profile is itself learned architectural information. Section 6.4. |
| 5 | Positive controls test the pruning machinery, not the readout's sensitivity to history. | Adds a **history-positive control**: a constructed task where the correct mask is only discoverable through a dense phase. Without it a null is uninterpretable. Section 6.5. |
| 6 | Pruning is operationalised as a mask, i.e. deletion -- silently selecting one of Q-057's four candidate mechanisms. | Adds a **reinstatement probe**, which answers Q-057's mechanism leg at near-zero marginal cost and is directly motivated by the latent-trace literature. Section 8. |
| 7 | Inherits its authority from an anchor (Vargas-Barroso) that measures **local CA3 recurrent connectivity**, not an interareal interface. | Section 4 names the genealogy gap and supplies the interareal causal anchors the matrix lacks. |

Two things are **left as they are**, deliberately: the routing to a later developmental substrate, and the ordering behind assays A and B.

---

## 2. Live-state corrections since the adjudication (2026-09-09)

The adjudication was written against a tree in which three of its own premises were open. All three have moved. Verified against the working tree at the timestamp above.

| Adjudication statement | Current state | Consequence for Assay C |
|---|---|---|
| "No completed 1010 manifest in the inspected origin tree... Recheck before implementing an assay against this lineage." | `v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3.json` exists. Outcome **PASS**, `hypothesis_verdict: H-F-confirmed`: "the decision-relevant content is DESTROYED AT ENCODE TIME... The repair is at the ENCODER'S OBJECTIVE, not at the consumer." Both load-bearing guards held (anchor sound; `mlp2048`/`deep2048x4` memorise). | The conditional V3 gate that assays A and C both carried is now **resolved, not pending**. Its resolution is binding: Assay C must not use the live `z_world` latent as its sender. Section 11 gate G-SOURCE. |
| Assay C owes an `L(A->B)` bridge-complexity instrument. | 1010 shipped and validated one: the capacity ladder `linear -> mlp128 -> mlp512 -> mlp2048 -> deep2048x4`, with a preregistered bar (0.80 agreement), elevation floor (0.20 over trivial), memorisation floor (0.95) and a raw-field positive control that cleared at 0.973-0.985 worst-to-best seed. | The instrument debt is **substantially smaller** than the dossier implies. Assay C should extend this ladder, not commission a new one. Section 5.3. |
| Literature debt 4 (developmental historical necessity) is unowned. | **`LIT-1003` already exists** in `experiment_proposals.v1.json`, status `proposed`, `claim_id: MECH-362`, `suggested_literature_type: targeted_review_mech_362`, `why_now: [missing_experimental_evidence, missing_literature_evidence, synthetic_signals_only]`. | The intake is owned. **Do not raise a second literature pull.** Section 12 lists what the existing proposal should be asked to cover. |

Three usable reference values from that lineage, for anyone calibrating an interface source later: raw field 0.9846 / 0.9796 / 0.9730 by seed; 250-dim PCA 0.8771 / 0.8578 / 0.8702; frozen `z_world` 0.6718 / 0.6735 / 0.6606; trivial baseline 0.5661 / 0.5803 / 0.5720. These are recorded reference values, never thresholds.

---

## 3. The three sparsities, separated

The dossier states the distinction in prose (section 3.5) but Assay C's design does not carry it. It is restored here as the assay's spine, because every plausible confound in this experiment is a leak between these rows.

| Axis | What it is | Biological referent | Role in Assay C | How it is held |
|---|---|---|---|---|
| **S1 -- local structural sparsity** | Fraction and topology of surviving parameters/connections within one system or within the interface itself. | Vargas-Barroso et al. (E24): CA3 recurrent connectivity, dense/strong/near-random -> distributed/sparse/structured, P7-8 to P45-50. **Local recurrent wiring.** | **Manipulated.** This is the pruning variable. | Density `d` and per-layer profile declared and matched across arms. |
| **S2 -- activity / engram sparsity** | How many units are active per episode or per stored memory; allocation and inhibitory control. | Ramsaran et al. (E25): CA1 engram allocation, PV interneurons, perineuronal nets; maturation of inhibition -> sparse engrams -> **memory precision**. | **Measured, and in one condition clamped.** Never the headline DV. | Reported per arm (active fraction per episode, participation ratio). One condition clamps it (matched k-winners) across arms. |
| **S3 -- interareal interface complexity** | `L(A->B)`: the minimum bridge class from a declared ladder that preserves a predeclared functional criterion from sender to receiver. | **No source in the 43-row matrix measures this.** Nearest is the hippocampal-retrosplenial subspace work (E06), which is representational, not a bridge assay. | **The dependent variable.** | Measured post hoc on frozen endpoints, independently of the trained interface. |

Three rules follow, and they are the ones a later session is most likely to lose.

1. **S1 is not evidence for S3.** A pruned interface is a claim about parameters. Legibility is a claim about the minimum bridge a *frozen* pair of endpoints admits. They can move in opposite directions: an interface can be sparser and require a *more* complex bridge.
2. **S2 must be excluded before S3 is claimed.** The adjudication already says "C must match local memory precision before claiming legibility" (E25 row). The clamp condition in section 6.2 is what discharges that, and without it a positive result reads as engram allocation.
3. **The observed CA3-to-CA1 sparse-to-dense transformation (E05) is not a contradiction of CA3 synaptic sparsification (E24).** Different axes, different quantities. Do not let a later reader "resolve" it.

---

## 4. Genealogy gap: the anchor measures the wrong quantity

MECH-362's empirical anchor is CA3 **recurrent** connectivity in slices. Assay C is about an **interareal** interface. The anchor is therefore evidence for S1 and silent on S3, and the adjudication says as much in the E24 row ("Slice geometry misses long-range projections; C tests historical necessity rather than age association").

The campaign matrix has no interareal developmental causal anchor. Four exist and are absent from it. They were located by targeted search for this audit and are recorded here as **motivating context, not as intake** -- registering them belongs to LIT-1003, not to this document.

| Source | Design | What it establishes | What it cannot establish |
|---|---|---|---|
| **Donato, Jacobsen, Moser & Moser (2017)**, *Stellate cells drive maturation of the entorhinal-hippocampal circuit*. Science 355(6330):eaai8178. [PMID 28154241](https://pubmed.ncbi.nlm.nih.gov/28154241/) | Developing mice; **temporally restricted pharmacogenetic silencing** of specific cell populations; structural maturation markers. | The closest biological analogue of Assay C's question. Entorhinal stellate cells provide an **activity-dependent instructive signal** driving maturation sequentially and unidirectionally through the intrinsic entorhinal-hippocampal circuits. Developmental *sequence* is causal, and it is interareal. | The silencing also changes what the mature circuit *is*. History and final architecture move together. No matched-final-architecture arm. |
| **Bitzenhofer, Popplau, Chini, Marquardt & Hanganu-Opatz (2021)**, *A transient developmental increase in prefrontal activity alters network maturation and causes cognitive dysfunction in adult mice*. Neuron 109(8):1350-1364.e6. [PMID 33675685](https://pubmed.ncbi.nlm.nih.gov/33675685/) | Optogenetic, **transient** increase in coordinated L2/3 mPFC pyramidal activity in neonates; adult functional and behavioural readout. | A time-limited early perturbation with permanent adult consequences: premature pyramidal maturation, altered interneuron density, weaker evoked gamma synchronisation, poorer mnemonic and social performance. Developmental history has lasting causal force. | Same confound, explicitly: the paper reports the **structural** changes as the mediator. This is history *via* architecture, not history *beyond* it. |
| **Chini et al. (2020)**, *Resolving and Rescuing Developmental Miswiring in a Mouse Model of Cognitive Impairment*. Neuron 105(1):60-74.e7. [PMID 31733940](https://pubmed.ncbi.nlm.nih.gov/31733940/) | Dual genetic-environmental risk model; in vivo ephys, optogenetics, anatomy, behaviour across development; first-postnatal-week minocycline. | A **timing-specific rescue window**: intervention in the first postnatal week restores neuronal deficits and pre-juvenile cognitive ability. Supports the critical-period timing variable of the source thought's section 10. | Rescue restores structure as well as trajectory. Sparser dendritic arborisation and lower spine density are named as the substrate. |
| **Travaglia, Bisaz, Sweet, Blitzer & Alberini (2016)**, *Infantile amnesia reflects a developmental critical period for hippocampal learning*. Nat Neurosci 19(9):1225-33. [PMID 27428652](https://pubmed.ncbi.nlm.nih.gov/27428652/) (erratum [PMID 28653686](https://pubmed.ncbi.nlm.nih.gov/28653686/); nonaversive replication, Travaglia et al. 2018 Learn Mem 25(4):176-182, [PMID 29545389](https://pubmed.ncbi.nlm.nih.gov/29545389/)) | Infant rats; hippocampus-dependent learning inside the amnesic window; later reminder; BDNF / mGluR5 manipulation. | The forgotten infant experience is **stored as a latent trace**, not erased: a later reminder reinstates a robust, context-specific, long-lasting memory, and post-training BDNF or mGluR5 activation rescues the amnesia. Recoverable-but-inaccessible is the biological default. | Nothing about interface complexity. Bears on Q-057's *mechanism* leg (section 8), not on the architecture-versus-weights question. |

**The honest reading.** Every located causal developmental intervention alters the mature substrate as well as the path to it. The biology therefore **motivates** Assay C and **cannot adjudicate** it. That is precisely why the synthetic matched-final-architecture counterfactual has value -- and precisely why it must not borrow confidence from these papers. This restates and sharpens the campaign's own debt 4, which said mouse slice development cannot settle this; the finding here is stronger, that no located *in vivo causal* study settles it either.

---

## 5. The computational literature already answers a large part of this, and the answer is unfavourable

Assay C's decisive comparison -- same final topology, different weight history -- is a well-studied question outside neuroscience, with an established methodology and a mostly negative prior. None of it appears anywhere in the REE tree. Checked: no occurrence of "lottery ticket", "rewinding" or "magnitude pruning" anywhere in `docs/` or `evidence/`; the single "Frankle" hit is Sardana & Frankle on inference-aware scaling laws in `targeted_review_q_093`, an unrelated cost-scaling record. Registering these belongs to LIT-1003.

### 5.1 The prior is against the strong hypothesis

- **Liu, Sun, Zhou, Zhou & Darrell (2019)**, *Rethinking the Value of Network Pruning*, ICLR. [arXiv:1810.05270](https://arxiv.org/abs/1810.05270). "Fine-tuning a pruned model only gives comparable or worse performance than training that model with randomly initialized weights." Their reading: pruning is better understood as **architecture search**; the surviving *architecture* carries the information, not the inherited weights. Their scratch arms are budgeted two ways (matched epochs and matched compute), which is why the comparison is credible.
- **Frankle & Carbin (2019)**, *The Lottery Ticket Hypothesis*, ICLR. [arXiv:1803.03635](https://arxiv.org/abs/1803.03635). The opposite finding at small scale: the sparse subnetwork reaches full accuracy from its **original initialisation** and does worse from a fresh random one.
- **Frankle, Dziugaite, Roy & Carbin (2020)**, *Linear Mode Connectivity and the Lottery Ticket Hypothesis*, ICML. [arXiv:1912.05671](https://arxiv.org/abs/1912.05671). The reconciliation, and the result that matters most here: "these subnetworks only reach full accuracy when they are stable to SGD noise, which either occurs at initialization for small-scale settings (MNIST) or **early in training** for large-scale settings (ResNet-50 and Inception-v3 on ImageNet)." At any interesting scale what is necessary is not the developmental path but a **short early prefix** of it.
- **Renda, Frankle & Carbin (2020)**, *Comparing Rewinding and Fine-tuning in Neural Network Pruning*, ICLR. [arXiv:2003.02389](https://arxiv.org/abs/2003.02389). Retraining protocol dominates: fine-tuning at a small fixed learning rate underperforms both weight rewinding and learning-rate rewinding. An arm retrained at a depressed learning rate is a rigged comparison.
- **Blalock, Ortiz, Frankle & Guttag (2020)**, *What is the State of Neural Network Pruning?*, MLSys. [arXiv:2003.03033](https://arxiv.org/abs/2003.03033). Across 81 papers, missing standardised baselines and metrics make pruning results largely non-comparable. Treat any single-density point estimate as uninformative; report the trade-off curve.
- **Hooker, Courville, Clark, Dauphin & Frome (2019)**, *What Do Compressed Deep Neural Networks Forget?*. [arXiv:1911.05248](https://arxiv.org/abs/1911.05248). Matched top-line accuracy conceals divergence on a narrow subset -- Pruning Identified Exemplars -- concentrated on the **long tail**. Directly relevant: a mean-transfer readout can be flat while exactly the rare relations Assay C cares about have been lost.

### 5.2 What this does to the assay

The strong form of the hypothesis -- that the mature organisation is historically inaccessible from its own final architecture -- **starts in a defensive position**. The literature's weight is that architecture plus density plus a short early prefix largely suffices, at least for supervised classification with unstructured masks.

That is a reason to sharpen the assay, not to drop it. Three qualifications keep the question live:

1. The published result is about **task accuracy in one network**. Assay C's DV is **cross-system legibility between two frozen specialised endpoints** -- a different quantity, with no published matched-topology counterfactual.
2. Hooker's long-tail finding is the mechanism by which a "no difference" verdict could be wrong in exactly REE's direction. Rare, decision-relevant relations are the ones REE cares about and the ones aggregate metrics hide.
3. Liu et al.'s own scope is structured pruning; the unstructured/high-sparsity regime is where scratch training is least reliably competitive.

### 5.3 Consequence for the primary instrument

Because the binary question already has a probable answer, the binary is the wrong primary instrument. **The quantity worth measuring is the minimal inherited prefix** -- how far into development weights must be inherited from before the reinitialised arm catches up. That converts a likely-null into a graded measurement that is informative whichever way it falls. Section 7.

---

## 6. C1 -- the smallest fair comparison

**Question.** At a fixed final interface topology between two fixed specialised endpoints, does the interface's inherited weight history contribute anything beyond the topology itself?

**Scope limit, stated first because it is load-bearing.** C1 freezes the endpoints. It therefore tests whether the **bridge's** weight history matters. It does **not** test the source thought's `L_early >> L_mature` prediction (section 4 of that thought), which requires the endpoints themselves to co-develop. That is C2 (section 9). A session that runs C1 and reports it as a verdict on developmental overcapacity in general has over-claimed.

### 6.1 The decisive pair -- two arms

Everything except the interface's weight history is held identical: the same frozen endpoints, the same mask, the same density, the same data, the same optimiser, the same budget.

- **B -- learned-then-pruned.** An over-capacity interface is co-trained with the endpoints under the developmental curriculum, then progressively pruned to density `d`. The endpoints are then frozen at their final state and the interface retrained to convergence.
- **D0 -- reinitialised final.** Take **B's own** final endpoints (identical, frozen) and **B's own** final mask (identical topology, identical per-layer profile). Reinitialise the interface weights. Train to convergence on the same data under a matched-compute schedule.

`B > D0` under the fairness protocol is the only configuration that supports necessary inherited weight history. `B ~ D0` is architecture discovery.

Taking B's endpoints for D0 rather than letting D0 develop its own is what makes this the *smallest* fair comparison. It removes endpoint co-adaptation from the contrast entirely, at the cost of the scope limit above.

### 6.2 Controls -- four, and each retires a specific rival

| Arm | Construction | Retires |
|---|---|---|
| **A -- structured-small** | Interface at the same density `d` but a *principled* topology (block, low-rank, or topographic), trained from scratch with the same frozen endpoints and budget. | Transient overcapacity itself. `A ~ B` means the density, not the search, was what mattered -- the source thought's own falsifiable prediction 1 inverted. |
| **R_global -- random at matched global density** | Random mask at overall density `d`. | Nothing was learned about topology. |
| **R_layer -- random at matched per-layer profile** | Random mask matched to B's **per-layer/per-block** density allocation. | The finer and more usually decisive case: `R_layer ~ B` means the learned mask carried only a **density allocation**, not a topology. `R_global` alone cannot see this. |
| **P -- history-scrambled** | Inherit B's final interface weights, then **permute them within the mask**. Weight distribution and topology preserved; the specific assignment destroyed. | `B ~ P` means the inherited quantity was a weight-magnitude *statistic*, not a learned assignment -- an outcome neither B-vs-D0 nor any control in the adjudicated design can detect. |

**The S2 clamp condition.** Every arm is run twice: free, and with activity sparsity clamped to a matched k-winners budget across arms. If B's advantage over D0 survives free but vanishes under the clamp, the effect is **activity/engram sparsity** (S2), not interface structure (S1) or legibility (S3). This is what discharges the E25 caution.

**Reference arms, retained from the adjudicated design.** `C_large` (large interface retained, never pruned) bounds what raw capacity buys and prevents a capacity effect being read as a developmental one. An unpruned-large trainability demonstration is a readiness assert, not an arm.

### 6.3 Budget fairness -- the commonest source of a false positive

- Report **both** budgets: matched epochs and matched optimisation compute. A pruned model given fewer effective updates than the dense model it came from will lose for reasons unrelated to history.
- The from-scratch arms use the **same learning-rate schedule shape** as B's retraining phase. Retraining B at a depressed fine-tuning learning rate while D0 gets a full schedule -- or the reverse -- decides the experiment by protocol.
- **Charge the dense stage.** B's total cost includes the over-capacity phase. Report it; do not present it as free. (Carried unchanged from the adjudicated design, which already got this right.)
- Report the **density trade-off curve**, not a single `d`. Per Blalock et al., a single-point comparison is not interpretable.

### 6.4 Dependent variables

Primary (S3): minimum bridge class on the declared ladder achieving the predeclared functional criterion, measured on frozen endpoints. Extend the validated 1010 ladder rather than commissioning a new one.

Secondary, reported separately and never aggregated into the primary:

- held-out cross-system transfer, **split into mean and long-tail/rare-relation strata** (Hooker);
- local endpoint precision at each endpoint (the S2/E25 discriminator);
- retained relational invariants;
- learning sample efficiency;
- recurrent/repeated-use stability (MECH-548 -- one-step rescue that degrades on repeated use blocks adoption regardless of the C1 verdict);
- S1 mask statistics and S2 activity statistics, per section 3.

### 6.5 Positive controls

- **Ladder range control.** A known information-preserving transform with a known inverse; confirms the bridge ladder can find a solution that exists. (Already the shape of 1010's `rawfield_ceiling` arm.)
- **Trainability control.** The unpruned large interface reaches criterion.
- **History-positive control -- new, and the assay is uninterpretable without it.** Construct a task in which the correct mask is *only* discoverable through a dense phase: for instance, a mask defined by co-activation statistics that are unobservable below the over-capacity width. If `B > D0` fails to appear even here, the readout lacks power to detect history dependence, and a null on the real task says nothing. This is the control the adjudicated design lacks: its positive controls check the pruning machinery, not the sensitivity of the measurement to the thing being claimed.

---

## 7. The rewind ladder -- the primary measurement

`D0` is one point on an axis, not the axis. Following the linear-mode-connectivity result, the informative variable is **how far into development weights must be inherited from**.

- **D_k** -- identical to D0 except the interface weights are set to B's values at development iterate `k`, then retrained under the same matched-compute schedule. `D_0` is D0.
- Sweep `k` over a logarithmic ladder spanning initialisation to the pruning point, with `k` reported both as a fraction of the curriculum and in absolute updates.
- **Report `k*`, the smallest `k` at which `D_k` reaches `B` within the preregistered equivalence margin.**

This turns a probable null into a measurement with four distinct readings:

| Result | Reading |
|---|---|
| `k* = 0` | Architecture discovery. No inherited weight history is necessary. Matches the Liu et al. prior. |
| `k*` small (early prefix only) | Only a short early phase is necessary -- stabilisation, not developmental search. The overcapacity hypothesis reduces to an early-phase effect. Matches Frankle et al. (2020). **This is the outcome the published literature predicts, and it is a genuine finding for REE, not a null.** |
| `k*` late (near the pruning point) | The developmental path is doing substantive work. The strong hypothesis survives at this interface. |
| No `k` reaches B | Something outside the interface differs between arms. Stop -- this is a protocol failure, not a result. Audit the endpoints and the budget before interpreting. |

`k*` is also directly interpretable against the source thought's critical-period question (its section 10): it is the earliest developmental time whose state is not reconstructible from the final architecture.

---

## 8. The reinstatement probe -- Q-057's mechanism leg, at near-zero marginal cost

Assay C as adjudicated implements pruning as a **mask**, i.e. deletion. Q-057 explicitly leaves the mechanism open across four candidates -- deletion, down-weighting, gating, residue-tagged de-authorization -- and the biology favours the non-destructive ones: Travaglia et al. show the forgotten infant trace is *stored and reinstatable*, not erased.

**Probe.** After pruning, attempt to reinstate a pruned pathway under a small, budgeted intervention (a bounded number of updates restricted to the pruned parameters, or un-gating without retraining) and measure recovery of the relation that pathway carried.

- Cheap recovery -> the sparsification behaved as **gating or down-weighting**; the trace survived. Q-057 mechanism leg answers away from deletion.
- No recovery at any budget short of full retraining -> **deletion**.

Run the probe under both the deletion (hard mask) and down-weighting (soft) implementations. The comparison is the mechanism leg's discriminator, it costs one extra evaluation phase, and without it the assay silently commits REE to deletion by implementation accident.

---

## 9. C2 -- what genuinely requires the developmental substrate

C1 is a bridge-history experiment with frozen endpoints. The part of the hypothesis it cannot reach is the part the source thought considers central: that development reorganises the **endpoints** so a simpler bridge later suffices, i.e. `L(A->B)` falls while competence rises.

C2 therefore is: measure `L(A->B)` at successive developmental checkpoints of a co-developing endpoint pair, under matched final capacity, with a small-from-start comparator.

C2 is where the substrate cost actually lives, and it is why the routing to a later developmental substrate stands. **C1 does not become a V3 task by being lighter.** Its DV is cross-system legibility between two specialised endpoints developing under a staged curriculum with a subtractive stage; MECH-362's amendment to ARC-019 that would supply that stage does not exist, and section 11's gates are not discharged. A degenerate version of C1 could be run today on a generic supervised benchmark -- it would reproduce the ML pruning literature and answer nothing about REE.

**Ordering is unchanged: assays A and B carry higher immediate information value.** C1's `L` measurement shares its instrument with A; build it once, in A.

---

## 10. Falsifiers

Stated so each can fail independently. Several are falsifiers of the *hypothesis*; F7 and F9 are falsifiers of the *assay*, and are listed as such deliberately.

| # | Outcome | Conclusion |
|---|---|---|
| **F1** | `D0 ~ B` at matched compute. | Architecture discovery; no necessary inherited weight history. **Primary falsifier; the published prior favours it.** |
| **F2** | `k*` is small. | Only an early prefix is necessary. The strong hypothesis reduces to early-phase stabilisation. |
| **F3** | `A ~ B`. | Structured-small suffices; transient overcapacity is unnecessary in this regime. |
| **F4** | `R_layer ~ B`. | The learned mask contributed a density allocation, not a topology. |
| **F5** | `B > D0` free, but the gap vanishes under the S2 clamp. | The effect is activity/engram sparsity, not interface structure. Resembles engram allocation, not legibility. |
| **F6** | `B > D0` on mean transfer but not on the rare-relation stratum, or the reverse. | Report separately; do not aggregate. A PIE-shaped dissociation changes the interpretation entirely. |
| **F7** | `L(A->B)` does not fall across development in **any** arm. | The maturation-as-legibility premise fails. The assay's framing question is void independently of the B-vs-D0 verdict. **Check this first: it is cheap and it can void the rest.** |
| **F8** | `B > D0` on the training distribution only. | Memorisation, not developmental organisation. Compositional and held-out-layout splits required. |
| **F9** | `B > D0` fails to appear on the history-positive control (6.5). | The instrument cannot detect history dependence. **A null on the real task is then uninterpretable.** Assay failure, not a result. |
| **F10** | `B ~ P` (history-scrambled). | The inherited quantity was a weight-magnitude statistic, not a learned assignment. |
| **F11** | One-step advantage that degrades under repeated use. | Blocks architectural adoption even if F1 is survived (MECH-548). |

---

## 11. Readiness gates

Anchored to existing readiness vocabulary rather than to new terms. G-SOURCE and G-LADDER are closed; **G-LIFE is decided against the branch Assay C needs**; the rest are open.

| Gate | Requirement | State |
|---|---|---|
| **G-LIFE** (hard) | A driver architecture in which the interface's weights actually change over the curriculum. **Assay C requires the gradient-learning branch.** The observational-life driver family runs entirely under `torch.no_grad()`, so cumulative learning updates are **zero by construction**; on that family B and D0 are literally the same object and the assay is undefined, not merely underpowered. | **DECIDED, AND DECIDED AGAINST THIS BRANCH.** Readiness section 19 item 1 is no longer unowned: the [developmental-life definition decision](developmental_life_definition_decision_2026-08-12.md) (2026-08-12) section 4 answers it and recommends **(b) non-parametric practice via MECH-357**, holding **(a) gradient learning as a contingent future decision**. Its finding on (a) is the operative constraint: "No driver architecture exists for a long, non-frozen (gradient-updating) single life... Building an alternative would be a genuinely new, unscoped architecture project -- no design doc, no owner, no estimate exists anywhere in this corpus." **Assay C is therefore gated behind an architecture project that has not been scoped, and the memo sequences the decision to scope it behind the MECH-357 fair test's outcome.** |
| **G-ENDPOINTS** | Two specialised endpoints exist, each separately competent, with a genuinely narrow identifiable interface between them. | **OPEN.** |
| **G-CURRICULUM** | A staged curriculum with at least two stages that measurably change endpoint representations, including a **subtractive** stage. This is MECH-362's proposed amendment to ARC-019 (currently additive) and it is not built. | **OPEN.** |
| **G-SOURCE** | The sender must carry the decision-relevant content. | **CLOSED, with a binding answer.** V3-EXQ-1010 confirmed H-F: content is destroyed at encode. Assay C must therefore use a **known information-preserving source** -- the raw-field or PCA control validated in that lineage -- not the live `z_world` latent. Using the live latent would test the encoder deficit, not the interface hypothesis. |
| **G-LADDER** | A validated bridge-complexity ladder with a preregistered criterion and a memorisation guard. | **LARGELY DISCHARGED.** 1010's ladder, bar (0.80), elevation floor (0.20) and memorisation floor (0.95) are validated and reusable. Extension, not construction. |
| **G-INSTRUMENT** | A behavioural/functional readout with dynamic range at the relevant endpoint, plus a rare-relation stratum for F6. Effect-size gates scaled on the SD of the delta with an absolute floor. | **OPEN.** |
| **G-SLEEP** | Readiness section 19 item 2: GAP-9 (sleep unreachable in true single-continuous-life) fixed or explicitly bracketed. | **OPEN, and required only for the replay-coupled pruning variant** (source thought section 9). Not required for C1 core. Do not let it block C1. |
| **G-ENV** | Readiness section 19 item 5: the environment's cue/resource-location conflation corrected, if exploration-driven curriculum variation is a readout. | **OPEN, conditional.** |

**Gate discipline.** G-LIFE is the hard precondition, and it is the one that actually sets Assay C's horizon. The other open gates can be bracketed with a stated assumption; G-LIFE cannot, because failing it makes the manipulated variable non-existent rather than noisy -- under `no_grad` the pruned and reinitialised arms are the same object.

**Consequence, stated plainly: Assay C is further out than the campaign dossier's routing implies.** "Later developmental substrate" reads as a scheduling note; the actual position is that C sits behind an unscoped architecture project, whose scoping decision the 2026-08-12 memo sequences behind the MECH-357 fair test -- itself five inconclusive-by-design-defect attempts deep (603h, 603k, 603r, 603s, 603t) as of that memo. This is not an argument for dropping C. It is an argument for **not** spending build effort on C's substrate now, and for treating this specification as the artifact that keeps the design intact until the gate moves. In the work-graph vocabulary: G-LIFE is `complex (probe-gated)` on the MECH-357 result, not `complicated (buildable)`.

**If G-LIFE ever moves, re-read this section before designing.** The memo's own sequencing means the trigger is a MECH-357 verdict -- pass or clean falsification -- not the passage of time.

---

## 12. Remaining debts

1. **No causal biological study performs the matched-final-architecture counterfactual.** Every intervention located (section 4) alters mature structure alongside developmental history. This sharpens campaign debt 4 from "mouse slice development cannot settle this" to "no located in vivo causal design settles it". Whether such a design is even possible in vivo is itself open.
2. **The pruning/lottery-ticket family is absent from REE's literature tree.** It is the most directly relevant computational evidence for MECH-362 and it is uningested. **It is already owned by `LIT-1003`** (status `proposed`, `targeted_review_mech_362`). Do not raise a second pull. When LIT-1003 executes it should be asked to cover Liu et al. 2019, Frankle & Carbin 2019, Frankle et al. 2020, Renda et al. 2020, Blalock et al. 2020 and Hooker et al. 2019, and -- per its own `disconfirming_evidence_required: 1` -- to record Liu et al. as **weakening** MECH-362's strong form.
3. **Transfer risk from supervised classification to interareal legibility is unquantified.** The ML results concern task accuracy within one network. The mapping to a frozen-endpoint bridge measurement is an analogy with no published matched-topology counterfactual behind it.
4. **`k*` has no prior.** No published work measures a rewind depth for an interareal bridge. The ladder's resolution and range are guesses until the history-positive control calibrates them.
5. **Q-057's mechanism leg remains open** until section 8's probe runs. Until then any Assay C implementation silently commits REE to deletion.
6. **Interface-complexity measurement is itself contested.** `L(A->B)` is a minimum over a *declared, finite* ladder. A finite probe family failing is not proof of information-theoretic absence -- the same caution 1008 and 1010 already carry (INV-105).
7. **The readiness investigation's section 19 is partly superseded and does not say so.** Item 1 is answered by the 2026-08-12 decision memo, but the investigation still reads as though the decision is unowned, and this specification's first draft inherited that error. Anyone citing readiness section 19 should check the decision memo alongside it. Reported here; not fixed, because editing that document is outside this session's claim.
8. **S2 clamping may not be achievable without perturbing S1.** If matched k-winners cannot be imposed without changing effective connectivity, F5 becomes unavailable and the engram-allocation rival cannot be retired. This needs checking before the design is committed.

---

## 13. What this document does not do

- Registers no claim, amends no claim, and changes no claim status. MECH-362 and Q-057 remain `candidate` / `substrate_conditional` / `implementation_phase: v4`.
- Queues no experiment and mints no substrate-queue entry.
- Does not move Assay C onto V3. The routing is unchanged: later developmental substrate, behind assays A and B.
- Adds no literature record. The four biological sources and six computational sources in sections 4 and 5 are cited as motivation and are **not** intake; their registration belongs to `LIT-1003`.
- Does not resolve Q-057. It specifies the probe that would.

## Compact rule

> Do not ask whether developmental overcapacity helps. Ask **how far into development weights must be inherited from before a reinitialised copy of the same topology catches up** -- and confirm, on a constructed positive control, that the readout could have detected an answer other than "not at all".
