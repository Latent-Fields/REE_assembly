# Latent interface translation campaign — tranche 3

**Date:** 2026-09-07  
**Status:** evidence-gathering tranche; not a claim promotion or architecture change  
**Parent campaign:** `evidence/planning/latent_interface_translation_campaign_20260907.md`  
**Prior tranche:** `evidence/planning/latent_interface_translation_tranche2_20260907.md`

## Question for this tranche

What makes two specialised representational systems mutually legible without forcing them to share one global representation?

The previous tranche framed this mainly as a bridge/alignment problem. This tranche materially sharpens that framing. The strongest external convergence is that effective communication may be a **subspace property** rather than a whole-representation property, and that temporally structured dynamics may be as important as static state geometry.

## Headline synthesis

A plausible cross-domain principle now has support from artificial systems and neuroscience:

> Two systems can preserve distinct high-dimensional internal representations while selectively aligning only the low-dimensional, task-relevant activity needed at their interface.

This is stronger and more specific than the earlier "mutual legibility" thesis. It predicts that REE should not necessarily seek high global similarity between E1, E2, hippocampal, `z_world`, or downstream consumer representations. Instead, it should identify whether a **consumer-relevant communication subspace** exists, whether the correct information enters it, whether its geometry matches the consumer's readout, and whether that relationship is stable or adaptively reconfigured across context, development, and sleep.

A second refinement is that static pointwise alignment may be insufficient. Temporal dynamics can provide constraints that recover a stable latent mapping even when instantaneous population coordinates drift.

## Evidence stream A — communication subspaces in brains

### Semedo et al. 2019 — foundational communication-subspace result

Semedo et al. showed that interactions between visual cortical areas can be captured by a low-dimensional **communication subspace**: only a subset of population activity patterns in the source area relates strongly to downstream activity, and this subset is distinct from the source area's largest internal fluctuations.

Reference: Semedo JD et al. *Cortical Areas Interact through a Communication Subspace*. Neuron 102, 249–259.e4 (2019). DOI: 10.1016/j.neuron.2019.01.026.

REE relevance:

- global representational variance is not equivalent to transmissible information;
- a source representation can contain abundant information outside the dimensions a consumer actually reads;
- "is the information in `z_world`?" and "is the information in the `z_world` → consumer communication subspace?" are different questions.

### Binish et al. 2026 — human prefrontal-to-motor communication subspace

Binish et al. used intracranial human recordings and identified a low-dimensional communication subspace embedded within high-dimensional prefrontal cortex activity. This subspace selectively relayed behaviourally relevant information to motor cortex and predicted context-dependent actions more strongly than activity in either region considered separately.

Reference: Binish N et al. *A communication subspace relays context-dependent actions from human prefrontal to motor cortex*. Nature Neuroscience 29, 1690–1698 (2026). DOI: 10.1038/s41593-026-02290-4.

This is especially close to REE's E3-facing problem because the source and receiver have visibly different computational roles: abstract context/rules versus action execution. The finding is not that prefrontal and motor cortex share one representation. The communication-relevant projection is embedded within the richer source dynamics.

REE implication:

> The correct assay may be a **task-conditioned source→consumer subspace**, not a whole-latent similarity metric.

### Gonzalez et al. 2026 — hippocampal–retrosplenial input/output rotations

This Nature paper is the strongest biological convergence found so far.

Large-scale simultaneous recordings across DG, CA3, CA2, CA1 and retrosplenial cortex identified low-dimensional communication subspaces using partial canonical correlation analysis. CA1's input- and output-related communication spaces could recruit overlapping neurons yet be strongly **rotated** relative to one another, with principal angles approaching orthogonality for different sender/receiver relationships.

The same physical neuronal pool can therefore participate in distinct channels through different coordinated activity patterns. The paper interprets this as selective routing through geometrically distinct input/output mappings rather than segregated populations.

Reference: Gonzalez J et al. *Subspace communication in the hippocampal–retrosplenial axis*. Nature 655, 192–201 (2026). DOI: 10.1038/s41586-026-10481-z.

Key REE consequences:

1. **Near-orthogonal functional channels can coexist in one representational substrate.** A latent does not need one globally consumer-friendly geometry.
2. **A bridge need not translate the entire source manifold.** It may only expose or rotate the task-relevant subspace.
3. **Shared units do not imply shared code.** The same dimensions/neurons can participate in different communication patterns depending on relational geometry.
4. **Interface selectivity can reduce interference.** Gonzalez et al. explicitly frame orthogonal rotations as a way to segregate readouts and reduce catastrophic interference.

This offers a biological analogue for keeping REE's specialised systems distinct while providing low-dimensional cross-system routes.

## Evidence stream B — communication subspaces adapt across context and sleep

Gonzalez et al. also tracked the same populations across distinct mazes. Communication subspaces showed context sensitivity while retaining a constrained circuit scaffold. The authors describe a multilevel system in which immediate geometric rotations provide flexible transformations over more stable anatomical/laminar structure.

During post-experience non-rapid-eye-movement (NREM) sleep, task-defined subspaces were reactivated. Importantly, the effect differed by interface:

- CA1–CA3 subspaces showed stronger post-learning alignment/reactivation, ripple-linked replay, and plasticity;
- CA1–retrosplenial subspaces were comparatively stable.

The paper explicitly proposes a plasticity–stability division of labour at the CA1 interface: fast intrahippocampal mappings remain malleable while hippocampal→cortical mappings provide a more stable scaffold.

This does **not** establish that sleep reduces mathematical bridge complexity. It does, however, materially strengthen a narrower REE hypothesis:

> Sleep may selectively reactivate and modify the communication geometry of some interfaces while protecting the stability of others.

That is more biologically grounded than predicting uniform post-sleep alignment improvement across every module pair.

## Evidence stream C — systems consolidation as temporally structured cross-system coupling

A 2026 Cell Reports study tracked hippocampal-prefrontal coupling during fear-memory consolidation and found a learning-related phase-amplitude relationship that re-emerged during sharp-wave-ripple-associated NREM events across days. Optogenetic disruption abolished remote fear-memory formation.

Reference: *Hippocampal-cortical coupling dynamics drive system consolidation of remote memory*. Cell Reports 45(8), 117810 (2026). DOI: 10.1016/j.celrep.2026.117810.

This adds an important constraint: interface effectiveness may depend not only on representational coordinates but on **when** cross-system states are coupled.

A related 2026 SLEEP paper reports ripple subtypes associated with different directions of hippocampus↔prefrontal coupling and different learning conditions, again suggesting that offline cross-system communication is multiplexed rather than a single generic replay channel.

Reference: Rayan A et al. *Deltas’ and Spindles’ Cross-Area Synchronization and Ripple Subtypes*. SLEEP (2026). DOI: 10.1093/sleep/zsag168.

## Evidence stream D — development can increase specialisation and integration together

Kember et al. (2026) mapped hippocampal functional systems in 471 participants aged 5–21. With development, the posterior hippocampal system became more topographically and functionally specialised: sharper boundaries and greater functional independence from other hippocampal systems. At the same time, its preferential connectivity with medial-parietal cortex increased with age and related to memory performance.

Reference: Kember J et al. *The hippocampus becomes topographically and functionally specialized along the longitudinal axis with development*. Nature Communications 17, 7699 (2026). DOI: 10.1038/s41467-026-74572-1.

This directly argues against an overly simple developmental prediction that better integration should mean increasingly similar representations.

A better REE prediction is:

> Development can increase **local differentiation** and **selective cross-system coupling** simultaneously.

This is highly compatible with E1/E2/hippocampal specialisation if the relevant communication subspaces become better formed or better gated over time.

## Evidence stream E — compressed hippocampal codes reconstructed by neocortex

Spens & Burgess (2026) present a computational account of hippocampo-neocortical interaction as compressive retrieval-augmented generation. Sequential experiences are represented in hippocampus in compressed conceptual form plus surprising details; a neocortical generative network reconstructs richer episodes and is trained by replay during consolidation.

Reference: Spens E, Burgess N. *Hippocampo-neocortical interaction as compressive retrieval-augmented generation*. Nature Communications 17, 7971 (2026). DOI: 10.1038/s41467-026-74357-6.

The useful principle for REE is not the large-language-model analogy itself. It is the functional asymmetry:

- hippocampal memory need not preserve a complete cortical state;
- it can preserve a **compressed code that is useful to the receiving generative system**;
- successful retrieval depends jointly on what is stored and what the receiver knows how to reconstruct.

This converges strongly with REE's existing compression/decompression concern and MECH-532: a compression ceiling cannot be interpreted without an adequate trained readout/decompression path.

It also supplies a warning: if retrieval depends on a receiver's learned priors, reconstruction can introduce systematic distortions. A "bridge" can therefore increase behavioural usefulness while reducing literal source-state fidelity.

## Evidence stream F — dynamics can identify alignment when snapshots cannot

Karpowicz et al. introduced Nonlinear Manifold Alignment with Dynamics (NoMAD) for stabilising brain-computer interfaces. The key contribution is using latent temporal dynamics as a constraint on unsupervised manifold alignment. Static manifold alignment methods performed substantially worse; incorporating dynamics preserved accurate decoding over weeks to months without supervised recalibration.

Reference: Karpowicz BM et al. *Stabilizing brain-computer interfaces through alignment of latent dynamics*. Nature Communications 16, 4662 (2025). DOI: 10.1038/s41467-025-59652-y.

This is not evidence about communication between two different biological areas, but it is methodologically important for REE.

A state bridge `B(z_t)` can look plausible pointwise yet destroy transition structure:

`B(z_t) -> plausible receiver state`

while

`B(z_{t+1})` is inconsistent with the receiver's own dynamics from `B(z_t)`.

For E1/E2 and hippocampal trajectories, a serious bridge assay should therefore include **dynamic consistency**, not only static reconstruction or downstream accuracy.

Candidate dependent variables:

- one-step receiver-dynamics error after bridging;
- multi-step trajectory divergence;
- preservation of local transition vectors/Jacobians;
- whether a bridge learned on one trajectory family generalises to held-out dynamics;
- bridge complexity needed when static states versus temporal windows are supplied.

## Evidence stream G — task-relevant dimensionality can be estimated separately from ambient dimensionality

Gulati et al. (2026) cast task-relevant latent dimensionality as an information-bottleneck problem: what bottleneck dimension preserves the mutual information needed for prediction? They also show that common bilinear/separable neural mutual-information estimators can inflate inferred dimensionality, motivating a more constrained hybrid estimator.

Reference: Gulati P et al. *Mutual Information and Task-Relevant Latent Dimensionality*. Proceedings of Machine Learning Research 326, 262–293 (2026).

This is directly useful for a **communication-subspace capacity assay** in REE:

> How many dimensions of `z_world` are actually required to preserve the information that a given consumer needs?

That is different from asking whether `world_dim=32` is globally large enough.

The current waypoint result already hints at this distinction: random 275→32 compression retains substantial directional decodability. A future assay could estimate the smaller **consumer-relevant dimension** and compare it with the effective rank of the actual consumer interface.

## Artificial-system cross-check — model stitching reinforces receiver-facing alignment

Mai et al. (CVPR 2026) systematically tested heterogeneous Vision Foundation Model stitching and found that conventional local feature matching or end-to-end task loss often struggled, especially at shallow stitch points. A surprisingly effective strategy was to train the stitch so that the resulting computation matched the **target model's penultimate representation**. Deep stitches could even outperform either constituent model.

Reference: Mai Z et al. *Revisiting Model Stitching In the Foundation Model Era*. CVPR 2026, pp. 41342–41351.

Traft (2026) similarly showed that large representational gaps can sometimes be crossed using nonlinear or bottleneck adapters, including across ResNet and Swin architectures.

Reference: Traft N. *Bridging Large Gaps in Neural Network Representations with Model Stitching*. PMLR 322, 129–139 (2026).

These results reinforce two cautions:

1. Bridge success depends on **where the receiver constrains the mapping**, not merely local source-target feature similarity.
2. Increasing bridge expressivity can rescue performance while simultaneously making mechanistic interpretation weaker.

Therefore bridge complexity should be treated as an experimental variable and regularised aggressively.

## REE crosswalk

### MECH-532 is almost exactly the minimal interface principle

MECH-532 already states that a designated compression site needs a trained decompression/readout stage before ceiling nulls there are interpretable. This tranche strengthens rather than replaces that claim.

The external literature suggests refining the experimental interpretation into three separable questions:

1. **capacity:** did task-relevant information survive compression?
2. **communication geometry:** does that information occupy dimensions the receiver can access?
3. **receiver dynamics/readout:** can the receiver transform those dimensions into its own valid computation?

### MECH-507 should not be read as demanding a universal shared latent

The richer reciprocal compression/decompression framing can remain compatible with specialised representations if the bridge is interpreted as a constrained communication interface rather than a demand that both systems converge globally.

### ARC-121 shared epistemic-state object — potential tension

ARC-121's literature record already contains a useful caveat: shared relational **format** is not the same as a single shared object instance, and uncertainty appears distributed across distinct systems.

The communication-subspace literature makes that distinction more important. A future review of ARC-121 should ask whether its function can be satisfied by:

- multiple specialised representations;
- a shared low-dimensional communication/readout format;
- typed interface contracts;
- rather than one physically unified epistemic-state object.

This is not presently evidence to weaken ARC-121; it is a competing implementation interpretation worth preserving.

### V3-EXQ-817a now has an even clearer reading

817a showed that improving consequence structure upstream did not improve behaviour through a collapsing downstream interface. Under the communication-subspace framing, that is exactly the expected failure if the improved information did not enter the receiver's effective communication/readout subspace.

The next discriminative question is therefore not simply "can a decoder recover consequence structure?" but:

> Does the consequence-bearing direction overlap the consumer's behaviourally effective subspace?

## Revised experimental programme

### Assay 1 — Consumer Communication Subspace (CCS) probe

For a frozen sender and consumer:

1. collect paired sender latent states and consumer pre-readout states/actions/outcomes;
2. estimate a low-dimensional sender→consumer predictive subspace using reduced-rank regression, partial canonical correlation analysis, canonical correlation analysis, or a carefully regularised linear map;
3. quantify effective rank/dimensionality;
4. identify whether the task variable of interest is represented inside or outside that subspace;
5. intervene specifically along in-subspace versus orthogonal sender directions.

Prediction:

- information can be linearly decodable from the full `z_world` while lying largely outside the subspace that predicts consumer activity.

That would be a clean "present but not communicable" phenotype.

### Assay 2 — Bridge-complexity ladder with receiver-manifold constraint

Keep the existing ladder:

1. orthogonal/Procrustes;
2. affine linear;
3. low-rank linear;
4. constrained nonlinear.

Add two independent criteria:

- **behavioural rescue**;
- **receiver-regime validity**, measured by distance/discriminator score against native receiver states and by receiver-dynamics consistency.

A bridge that rescues behaviour while creating out-of-distribution receiver states is a weaker mechanistic result than a simple map that lands inside the native communication subspace.

### Assay 3 — Static versus dynamic alignment

Compare mappings trained on state pairs alone with mappings constrained by transition windows.

Key prediction:

- E1/E2 interface alignment may be substantially easier or more stable when temporal dynamics are used, because the relevant meaning is encoded in how states evolve rather than in instantaneous coordinates alone.

### Assay 4 — Pre/post-sleep subspace assay

Do **not** ask only whether E1 and hippocampal representations become globally more similar after sleep.

Instead measure:

- communication-subspace rank;
- principal angles between sender and receiver task-relevant subspaces;
- correct-versus-mismatched pairing sensitivity;
- static and dynamical bridge complexity;
- stability of established interfaces;
- plasticity of recently learned interfaces.

The Gonzalez result motivates a differentiated prediction:

- some hippocampal/internal mappings may become more strongly reactivated/reconfigured;
- cortex-facing mappings may remain comparatively stable.

Thus "sleep improves every interface" is too crude and should be rejected in advance.

### Assay 5 — Developmental specialisation × legibility matrix

At repeated developmental checkpoints measure two orthogonal axes:

**local specialisation**
- within-module intrinsic dimension;
- clustering/separation;
- task-specific decoding;
- representational independence from other modules.

**cross-module legibility**
- communication-subspace rank;
- canonical correlations;
- bridge complexity;
- causal correct-vs-mismatched effect;
- cross-module dynamic consistency.

This directly tests the hypothesis that local differentiation and selective integration can increase together.

## New falsifiable hypotheses arising from tranche 3

### H1 — Communication-subspace hypothesis

The information required for at least one current V3 downstream behaviour is present in `z_world` but lies substantially outside the sender dimensions that predict the native consumer's activity.

**Falsifier:** task-relevant directions and consumer-predictive subspace already overlap strongly, yet behaviour still fails.

### H2 — Low-rank-interface hypothesis

The effective dimension required for a given REE sender→consumer interface is substantially lower than the sender's ambient latent dimension.

**Falsifier:** reliable consumer prediction/behaviour requires nearly full-rank source information even after careful estimation and held-out validation.

### H3 — Dynamics-first alignment hypothesis

A temporal/dynamics-constrained map will generalise across held-out trajectories better than a pointwise state-alignment map of similar capacity.

**Falsifier:** dynamics add no held-out benefit or systematically impair interface performance.

### H4 — Developmental differentiation-plus-integration hypothesis

During successful REE development, module-specific representational differentiation can increase while communication-subspace quality or causal cross-module legibility also increases.

**Falsifier:** improved behaviour consistently requires global representational homogenisation, or specialisation reliably degrades cross-module use.

### H5 — Selective sleep-interface plasticity hypothesis

Sleep/replay will modify recently learned internal communication subspaces more strongly than stable downstream scaffold interfaces.

**Falsifier:** changes are uniform across interfaces or occur independently of replay/sleep manipulation.

## Important methodological warning

Canonical correlation analysis, representational similarity, linear probes and bridge success are all observational unless paired with interventions.

A strong evidence sequence remains:

`encoded → in communication subspace → accessible → pairing-specific → causally used → behaviourally useful`.

At minimum, causal interface experiments should retain:

- correct paired state;
- deranged/mismatched paired state;
- zero;
- moment/covariance-matched random state;
- orthogonal-to-communication-subspace perturbation;
- in-communication-subspace perturbation.

The contrast between the final two is particularly attractive because it tests whether the estimated communication geometry is functionally real rather than merely correlational.

## Updated working thesis

The earlier thesis was:

> Cognitive development need not make specialised systems share a representation; it may make their different representations increasingly usable by one another.

Tranche 3 suggests a more precise form:

> **Specialised cognitive systems may preserve distinct high-dimensional internal representations while coordinating through low-dimensional, context-sensitive communication subspaces. Development can increase both local specialisation and selective inter-system legibility. Replay and sleep may differentially stabilise or reconfigure these interface subspaces according to their plasticity requirements, rather than globally homogenising representations.**

This remains a synthesis/hypothesis, not an established biological law.

## Most decision-relevant next work

1. Apply the communication-subspace framing explicitly to the current `z_world` → reader / E1–E2 failure loci.
2. Determine whether existing V3 telemetry is sufficient for an offline reduced-rank/CCA-style assay before adding substrate.
3. Review MECH-532, MECH-507 and ARC-121 under the distinction between global shared representation and low-dimensional shared communication format.
4. Mine the full Gonzalez 2026 and Binish 2026 methods for implementable null controls and dimension-selection procedures.
5. Examine whether current sleep/replay experiments preserve paired pre/post states at enough resolution to estimate interface geometry around forced sleep boundaries.

No architecture or claim status should change solely from this tranche.