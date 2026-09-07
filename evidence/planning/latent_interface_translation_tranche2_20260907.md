# Latent interface translation — research tranche 2

**Date:** 2026-09-07  
**Status:** evidence intake / research notes; not a claim registration and not an architectural commitment  
**Parent campaign:** `evidence/planning/latent_interface_translation_campaign_20260907.md`

## Purpose

This tranche deepens five questions left open by the initial campaign:

1. What exactly do StateBridge and Interlat establish about cross-system alignment?
2. What failure modes make model-stitching success misleading?
3. What causal controls are strong enough to establish content-specific communication?
4. Is there neuroscience evidence that development or sleep changes cross-system representational compatibility?
5. What should REE measure before introducing any bridge as architecture?

The organizing distinction remains:

> encoded != decodable != natively accessible != bridgeable != pairing-specific != causally used != behaviourally useful.

---

## 1. StateBridge: important correction and narrower significance

### Source

Peng Y, Zhang DC, Wang X, Aletras N. *StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems*. arXiv:2608.13317; COLM 2026. Public repository: `YanwenPneg/StateBridge`.

### Correction

The first-pass description overstated StateBridge's heterogeneity evidence.

The released StateBridge system targets **homogeneous multi-agent systems in which agents share the same pretrained weights**. It is evaluated using several model families/scales, but sender and receiver within a given system are not independently pretrained heterogeneous models. The public repository explicitly lists heterogeneous sender-receiver transfer as future work.

This matters for REE interpretation: StateBridge does **not** yet prove that a closed-form orthogonal transformation can bridge independently learned representational systems analogous to E1 versus E2 or hippocampus versus cortex.

### What StateBridge does establish

The sender's final-layer hidden states are mapped into the receiver's input-embedding space using an orthogonal Procrustes transformation, followed by lightweight norm calibration and vocabulary anchoring. The aligned states are prepended as continuous input embeddings. No trainable projector or modification of transformer weights is required.

The public implementation/README reports an informative ablation pattern:

- full StateBridge outperforms a ridge-regression replacement despite ridge having lower pointwise reconstruction error;
- removing norm calibration or vocabulary anchoring reduces performance;
- a random-noise prefix collapses performance.

The reported interpretation is that preserving **relational geometry** can matter more than minimizing coordinate-wise reconstruction error.

### Evidence label

**Supported within a narrow homogeneous-model regime.**

### REE relevance

StateBridge still gives REE a useful diagnostic principle:

> Before concluding that information is absent, test whether a very low-complexity geometry-preserving transformation makes the existing consumer able to use it.

But it should be cited as evidence for **interface coordinate alignment**, not yet for cross-architecture cognitive translation.

---

## 2. Interlat: the stronger heterogeneous-model result

### Source

Du Z et al. *Enabling Agents to Communicate Entirely in Latent Space*. ACL 2026, pp. 27106–27129. DOI 10.18653/v1/2026.acl-long.1248. arXiv:2511.09149 v4.

### Mechanism

Interlat transmits temporally aligned last-layer hidden states corresponding to the sender's message. A learned communication adapter maps those states into a form the receiving actor can interpret. A second learned reasoning/compression system can reduce the latent sequence substantially while attempting to preserve task-relevant geometry.

This is not merely a fixed bridge. The receiver is trained to interpret communicated latents, including curriculum and alignment objectives.

### Heterogeneous evidence

The paper includes cross-family experiments in which Qwen-derived latent communications are consumed by a LLaMA-family actor without shared parameters or tokenizer vocabulary. The authors report improved performance in this setting.

This is substantially closer to the REE question than StateBridge because the sender and receiver belong to different pretrained model families.

### Strong ablations

Interlat's ablations are unusually relevant to REE:

- removing the communication adapter drops ALFWorld success close to zero in the reported actor experiment;
- removing the separation loss encourages shortcut behavior in which the receiver ignores the latent message and falls back toward the single-agent baseline;
- removing geometry-alignment loss substantially degrades compressed-latent performance;
- covariance-matched Gaussian replacements and random orthogonal rotations reduce performance;
- random rotation preserves first/second moments while scrambling higher-order/directional structure, so degradation argues against a pure channel-statistics explanation.

The paper also reports training dynamics in which the matched-versus-mismatched separation loss initially stays near chance and then falls after roughly 2,000 steps, interpreted as the actor learning to exploit task-relevant communicated latents.

### Compression result

Interlat distinguishes naïve truncation from learned compression. Naïve shortening eventually fails; trained compression reportedly maintains performance across much shorter latent sequences, with an 8-step communication setting yielding the headline near-24x latency reduction.

This is important conceptually: **representational redundancy and communication redundancy are separable from information absence.**

### Limitations

The authors themselves frame the work as a feasibility study. The main experiments remain relatively narrow: ALFWorld plus MATH, mostly two-agent systems, open/inspectable models, and learned receiver adaptation. Human interpretability of the latent channel is substantially reduced.

### Evidence label

**Strong feasibility evidence for learned cross-family latent communication, not evidence that arbitrary independently learned systems are naturally mutually legible.**

### REE relevance

Interlat suggests a useful upper-bound experiment: if a constrained trained adapter between frozen REE endpoints can rescue behavior, then information and a usable transformation exist somewhere in that interface. But because Interlat co-trains/adapts the consumer, it does not by itself tell REE whether its native downstream systems should already understand the representation.

---

## 3. Model stitching: useful instrument, dangerous similarity claim

### Positive evidence

Traft 2026 (*Bridging Large Gaps in Neural Network Representations with Model Stitching*, UniReps/PMLR) shows that low layers from one architecture can be connected to high layers of a very different architecture using adapters, including ResNet-to-Swin examples approaching original-model ImageNet accuracy when interpolation and more expressive nonlinear/bottleneck adapters are allowed.

Mai et al. 2026 (*Revisiting Model Stitching in the Foundation Model Era*, arXiv:2603.12433) likewise reports that heterogeneous vision foundation models can become reliably stitchable, but that success depends strongly on stitch point, loss and adapter design.

### Negative methodological evidence

Balogh & Jelasity 2025 (*How not to Stitch Representations to Measure Similarity*) is directly relevant. They show that task-loss-trained stitching can be a misleading representation-similarity measure. A stitch can optimize task performance by producing out-of-distribution receiver inputs, sometimes making distant layers appear more similar than corresponding layers.

Functional Latent Alignment and subsequent 2026 theoretical work make the same broad point from another direction: stitching measures **usable information under an adapter and objective**, not necessarily native representational equivalence.

### Evidence label

**Established methodological warning.**

### REE consequence

A bridge succeeding is not enough. REE bridge assays need two separate readouts:

1. **direct/geometry matching** — does the mapped representation remain within the receiver's native representational distribution and preserve source/receiver relational structure?
2. **task rescue** — does behaviour improve?

A high-capacity task-trained bridge that rescues behaviour while creating out-of-distribution receiver states should be treated as an upper-bound existence proof, not as evidence of a biologically/plausibly simple interface.

This strengthens the case for the bridge-complexity ladder:

1. native interface;
2. random-projection floor;
3. orthogonal Procrustes;
4. affine map;
5. low-rank linear map;
6. constrained nonlinear map;
7. high-capacity stitch only as an upper bound.

At every level, measure receiver-state distribution shift as well as behaviour.

---

## 4. Causal audits: the minimum standard for REE interface claims

### Cheng, Das & Ramnath 2026

*When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs* (arXiv:2608.04893).

The critical intervention is **derangement**: replace each example's communicated state with another example's state using a fixed-point-free permutation. This keeps the set/distribution of states unchanged while destroying correct pairing.

The paper distinguishes:

- true correctly paired state;
- deranged/mismatched state;
- zero state;
- moment-matched random state;
- sender deprived of private information;
- direct-text validity controls.

Under tasks where the receiver truly needs information private to the sender, correct-versus-deranged effects can be very large. Under ordinary tasks where the receiver already has the problem statement, correct and deranged channels can be statistically equivalent even though zeroing the channel is strongly harmful.

This yields the key doctrine:

> A large channel effect is not necessarily a pairing/content effect.

### Zhang & Emu 2026

*Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM* (arXiv:2607.26773) decomposes total performance effects into message presence, example-specific message content and additional-agent contribution. The relative components change across model scales and tasks.

### REE consequence

For any proposed information pathway, a governance-quality causal assay should distinguish at least:

- **presence effect:** correct vs zero;
- **pairing/content effect:** correct vs mismatched;
- **distribution effect:** mismatched vs moment-matched random;
- **sender-identity effect:** another subsystem's same-example state where meaningful;
- **task-necessity effect:** receiver given vs denied alternative access to the target information.

This could prevent a large class of false positives in REE where a side channel changes gain, norm, entropy or attention without transmitting the purported variable.

---

## 5. Development: evidence for increasing specialization and coupling, not yet translation-complexity reduction

### Hippocampal specialization during development

Kember et al. 2026, *The hippocampus becomes topographically and functionally specialized along the longitudinal axis with development* (Nature Communications), reports substantial remodeling across childhood and adolescence, including increasing functional specialization and sharper boundaries within hippocampal organization.

### Early hippocampal-cortical coupling

Audrain et al. 2026, *The Development of Hippocampal-Cortical Functional Connectivity Across the First Two Years of Life*, traces early maturation of hippocampal-cortical coupling along the hippocampal long axis.

### Interpretation boundary

These studies support the idea that cognitive development includes changing **specialization plus inter-regional coupling**, rather than simple convergence onto one homogeneous code.

However, the present tranche still does not identify a study directly measuring a decreasing mathematical mapping complexity between two representational spaces over development.

### REE hypothesis retained

A developmental REE assay can therefore ask a new question without pretending neuroscience has already answered it:

> As E1, E2 and hippocampal representations specialize, does the minimal transformation required for one system to make use of another become simpler, harder, or merely more task-specific?

Possible outcomes are informative:

- falling bridge complexity -> increasing mutual legibility;
- rising bridge complexity with improving behaviour -> productive specialization plus stronger learned interfaces;
- rising complexity with falling behaviour -> representational/interface drift;
- stable complexity but higher pairing effect -> same geometry, more task-relevant content.

---

## 6. Sleep: stronger evidence for coordinated communication, still no direct proof of geometric alignment

### 2026 cross-area sleep evidence

A 2026 SLEEP paper on delta/spindle cross-area synchronization and ripple subtypes reports distinct hippocampal ripple classes associated with different directions of hippocampus-prefrontal coupling and different forms of memory consolidation. Learning increased coupling between hippocampal delta/spindle events and cortical counterparts, increasing ripple synchronization with cortical oscillations.

This supports a mechanistic picture in which sleep creates structured windows for **directional inter-system exchange** rather than merely replaying an isolated hippocampal trace.

### Replay as transformation rather than copying

Barry & Love's neural-network account of replay/consolidation (Cerebral Cortex 2023) shows that generative replay at latent levels can improve category generalization and that replay usefulness depends on where in the hierarchy it occurs. More recent work continues to show offline retuning, manifold formation and representational transformation.

### Important negative/constraint from artificial replay

Kim 2025 reports that internal replay in continual learning can increase representational overlap and reduce task-specific differentiation even while reducing catastrophic forgetting. Thus "more aligned" or "more overlapping" is not automatically better.

This is a useful warning for REE: consolidation may need to preserve **functional complementarity**, not maximize representational similarity.

### Current evidence boundary

No source found in this tranche directly demonstrates:

> sleep/replay minimizes the bridge complexity between two independently specialized systems.

The strongest defensible neuroscience-backed statement is narrower:

> Sleep supports coordinated hippocampal-cortical exchange and can transform representations; whether one function of that transformation is improved mutual legibility is open.

---

## 7. Heterogeneous latent replay in artificial systems: surprisingly sparse evidence

Continual-learning "latent replay" usually stores/replays intermediate activations inside one network. A key constraint is representational drift: if lower layers change too much, stored latent activations become stale. Pellegrini et al. address this by slowing learning below the replay layer.

This is informative for REE because it reveals a general **address stability problem**:

> A memory stored in one representational coordinate system can become unusable if the producer's geometry changes without a corresponding remapping of the memory/consumer interface.

The present search did not find mature work in which two independently evolving neural subsystems explicitly learn and maintain a replay-driven translation map between their changing latent spaces. That gap appears real enough to keep as a targeted search item.

---

## 8. Updated evidence hierarchy for the eventual thought document

### Established / strong support

- continuous latent states can carry task-relevant information between artificial agents;
- learned adapters can make heterogeneous model families communicate in latent space;
- same-model hidden/input spaces can sometimes be aligned with a simple orthogonal transformation;
- adapter choice and geometry preservation matter;
- task-trained stitching can create misleading out-of-distribution solutions;
- zero-channel effects do not establish example-specific content use;
- mismatch/derangement controls are required for causal communication claims;
- sleep supports coordinated hippocampal-cortical exchange and representational transformation;
- development changes hippocampal specialization and hippocampal-cortical coupling.

### Supported but scope-limited

- relational geometry may be more important than pointwise reconstruction for interface compatibility;
- highly compressed latent messages can retain task utility when compression is trained;
- cross-family latent communication can work without shared tokenizer/weights when the receiver/adapter is trained appropriately.

### Plausible REE extrapolations

- some current z_world/E1/E2 failures may be interface-coordinate failures rather than information-loss failures;
- bridge complexity can serve as a diagnostic measure of interface compatibility;
- replay-driven representational change creates a need to preserve or update memory/readout mappings.

### REE hypotheses — not established externally

1. Development improves mutual legibility among E1/E2/hippocampal systems.
2. Sleep/replay reduces the mapping complexity required between specialized REE representations.
3. Some representational systems should become *more different* while their interfaces become *more effective*.
4. Interface quality may be a distinct developmental variable from representation quality.
5. A failure to update interfaces during representational rebucketing may produce cognition-like failure modes even when each subsystem remains locally competent.

---

## 9. Updated assay design constraints

### A. Frozen-endpoint requirement

For the primary locus assay, freeze sender and receiver. Train only the bridge. Otherwise a positive result cannot localize whether the sender, receiver or bridge adapted.

### B. In-distribution receiver-state check

For every bridge, record distance/distribution diagnostics comparing mapped states with native states normally consumed at that boundary. A bridge that produces highly out-of-distribution states can rescue a task while being a poor explanation of natural interface compatibility.

### C. Complexity ladder

Do not begin with a multilayer perceptron. Test in ascending permissiveness:

1. identity/native;
2. orthogonal;
3. affine;
4. low-rank;
5. regularized nonlinear.

The simplest successful bridge is itself a dependent variable.

### D. Pairing audit

Once a bridge succeeds, repeat the behavioural test using correct, mismatched, zero and moment-matched random source states.

### E. Content-specific feature intervention

If a claim names a particular variable (waypoint direction, harm, controllability, object identity), manipulate that content while preserving as much of the rest of the state as possible.

### F. Development/sleep longitudinal version

Measure the same bridge-complexity and pairing-specificity metrics:

- early vs late development;
- immediately pre-sleep vs post-sleep;
- sleep-enabled vs sleep-ablated controls;
- waking-replay vs sleep-replay where feasible.

The primary sleep result should not simply be "post-sleep representations are more similar." A stronger metric is whether the native consumer or a *simpler* bridge can use the correct paired content after consolidation.

---

## 10. Most decision-relevant implication for current V3

V3-EXQ-817a already showed that improving a compressed representation can fail to improve behaviour when the downstream interface remains collapsing. The 2026 latent-communication literature independently demonstrates that interface readability can be a separate engineering problem from information content.

Together with the 2026-09-07 random-projection waypoint result, this strengthens an interface-first diagnostic sequence:

1. establish raw-source information availability;
2. establish z_world decodability relative to random-projection floor;
3. establish native consumer accessibility;
4. if native accessibility fails, test the least-complex frozen bridge;
5. if bridge rescues, perform correct-vs-mismatched causal audit;
6. only then decide whether the problem is representation, interface, consumer training, or generic channel dependence.

This sequence is diagnostic doctrine, not yet an architectural prescription.

---

## 11. Next targeted searches

1. Mostik technical disclosure/code/paper and ARC-AGI-3 post-competition disclosure.
2. Independent replications of Interlat cross-family transfer.
3. StateBridge heterogeneous extension or external reproduction.
4. Neural studies measuring cross-region representational geometry before/after sleep rather than only functional connectivity.
5. Developmental studies with representational similarity/hyperalignment measures across hippocampus-cortex.
6. Continual-learning systems that remap stale latent memories after representation drift.
7. Biological work on reconsolidation/reindexing after cortical representational change.
8. Formal measures linking bridge complexity to conditional mutual information / usable information.

## Provisional synthesis after tranche 2

The evidence increasingly supports a two-variable view:

> **representation quality** and **interface legibility** are separable.

A cognitive architecture can therefore fail in at least four distinct ways:

- relevant information was never encoded;
- information was encoded but inaccessible to the consumer;
- information was accessible only through an implausibly complex translation;
- the channel was active and influential, but behaviour did not depend on the intended content.

The eventual REE thought should treat mutual legibility as a measurable property of relationships between systems, not as a synonym for representational similarity.