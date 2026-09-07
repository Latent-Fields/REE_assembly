# Latent interface translation: evidence-gathering campaign

**Date:** 2026-09-07  
**Status:** research campaign / evidence intake; not a claim registration and not an architectural commitment  
**Trigger:** Mostik latent-communication report (WIRED, 2026-09-02) plus convergence with current V3 z_world/interface work  
**Scope:** external literature + REE internal evidence, leading to a later evidence-backed thought document

## Campaign question

> When independently learned representational systems cooperate, what task-relevant information survives, what remains recoverable but inconveniently organised, what transformations make it usable by another system, and how can we prove that the receiver causally uses the transmitted content rather than merely benefiting from the existence or statistics of a channel?

For REE this becomes a sharper family of questions:

- Did the observation -> z_world boundary destroy information?
- Is the information present in z_world but entangled or geometrically inconvenient?
- Can the relevant consumer access it with its native readout?
- Can a small frozen-endpoint bridge rescue it?
- Does behavioural rescue depend on the *correct paired content*, or only on generic channel activity?
- Do development, replay or sleep make independently useful representations more mutually legible?

The campaign should not assume that a universal common latent language is desirable. A competing hypothesis is that specialised systems may retain different representational geometries while learning low-complexity, causally effective translations between them.

## Why now: live REE convergence

Several current and prior REE results make this immediately decision-relevant.

### 1. z_world dimensional compression is not automatically information destruction

The 2026-09-07 waypoint-field DV-range probe (`ree-v3` f00402c9) measured pending-waypoint direction decodability on the V3-EXQ-1004 geometry:

- raw observation lift: +0.269
- random 275 -> 32 linear projection: +0.211 (78% retention)
- untrained SplitEncoder: +0.167 (62% retention)

The pre-registered zero-information null was therefore invalid: substantial directional information survives a severe random low-dimensional projection. A trained z_world must be judged against a random-projection floor rather than zero.

### 2. REE is already testing re-basing and consumer adequacy

V3-EXQ-1008 (`ree-v3` 14c44906) contains a task-agnostic 32-dimensional linear compression leg and a decision-relevant field-decode re-basing of frozen z_world. This is already close to an interface-translation assay and should be interpreted alongside the latent-communication literature rather than as an isolated local fix.

### 3. A prior direct test showed representation improvement without behavioural improvement

The representation->authority->selection correction (`REE_assembly` 0c125b0) records the V3-EXQ-817a result. The action-object bottleneck was successfully made consequence-structured with content controls, but behaviour did not improve. The analysis localised an open link at the downstream consumer/decoder: improving upstream geometry was not sufficient while the interface to action remained collapsing.

This is a key prior for the present campaign. REE must not treat "better representation" and "better use of representation" as the same intervention.

### 4. Existing REE thought already defines a representation contract

`docs/thoughts/2026-09-04_z_world_representation_contract.md` asks what information must survive observation -> z_world so downstream systems can learn a coherent actionable world. It explicitly treats downstream recoverability, rather than coordinate-wise interpretability or ontology labels, as the important criterion.

The present campaign should extend that thought by splitting **recoverability** into distinct levels: decodable, accessible by native consumer, bridgeable, causally used, behaviourally useful.

### 5. Existing replay/rebucketing thought already makes representational reorganisation a sleep question

`docs/thoughts/2026-08-31_replay_driven_rebucketing_decision_relevant_representation.md` argues that replay may revise equivalence classes and that sleep-like decoupling may allow safe maintenance of the representational coordinate system. The present campaign adds a narrower testable possibility: offline consolidation might alter not only representations themselves but the *translation complexity between specialised representations*.

This latter statement is currently a REE hypothesis, not an established neuroscience result.

## Working vocabulary: distinctions the campaign must preserve

The literature often conflates several different successes. The evidence matrix should code them separately.

1. **Encoded** — information is statistically present in a representation.
2. **Decodable** — an external probe can recover the information.
3. **Natively accessible** — the system's existing consumer can recover/use it without a new trained bridge.
4. **Bridgeable** — a constrained mapping between frozen endpoints can make it usable.
5. **Pairing-specific** — the receiver benefits more from the correct sender state than a same-distribution state from another example.
6. **Causally used** — intervention on the specific content changes downstream computation/behaviour in the predicted direction.
7. **Behaviourally useful** — use of the content improves task performance or adaptive behaviour.
8. **Low-complexity translation** — a linear/orthogonal/low-rank bridge suffices.
9. **High-complexity translation** — only a nonlinear/high-capacity bridge suffices; this may indicate entanglement or permit a covert second computation.
10. **Representation alignment** — two systems share relational/geometric structure under an allowed transformation.
11. **Interface alignment** — the sender's representation and receiver's readout are mutually compatible at the actual consumption boundary.
12. **Channel dependence** — performance depends on the presence/statistics of a channel even if it does not depend on the correct example-specific content.

A core doctrine for the later thought should be:

> decodable != natively accessible != bridgeable != pairing-specific != causally used != behaviourally beneficial.

## Evidence stream A — Mostik

### Current public evidence

WIRED, Will Knight, 2026-09-02, "These Russian Mathematicians Taught AI Models How to Talk to Each Other Without Using Words."

Public claims include:

- direct interaction between models without producing an intermediate text output;
- a GLM-5.2 753B / Qwen-3.5 4B hybrid demonstration;
- reported hybrid cost around one-twentieth of full GLM inference;
- reported performance approximately halfway between the component models;
- an undisclosed ARC-AGI-3 system reported near the top of the competition;
- an explicit research framing around finding common mathematical structure between models.

### Evidence status

**Interesting but presently company-reported / incompletely disclosed.** The public article is sufficient to motivate the question, not to settle bridge architecture, generality, causal mechanism, or exact compute accounting.

### Information still needed

- exact transmitted tensor/state: hidden states, selected layers, KV cache, pooled activations, or another object;
- bridge architecture and parameter count;
- paired-data construction and training objective;
- where the bridge injects into the receiver;
- whether sender runs once per problem or at multiple points;
- ablations against text handoff, same-family handoff, random projection and trainable parameter-matched controls;
- correct-message vs mismatched-message controls;
- layer sensitivity;
- bridge generalisation across task domains;
- independent replication or code release;
- full ARC-AGI-3 method after competition disclosure.

## Evidence stream B — latent communication between artificial agents

### Interlat — Du et al., ACL 2026

**Source:** Du Z et al. *Enabling Agents to Communicate Entirely in Latent Space*. Proceedings of ACL 2026, pp. 27106-27129. DOI: 10.18653/v1/2026.acl-long.1248.

**Established by the paper:** continuous last hidden states can be used for direct inter-agent communication; learned compression can further reduce communication; experiments include heterogeneous models; reported acceleration reaches up to 24x while maintaining competitive performance.

**REE relevance:** establishes feasibility of cross-model latent communication and suggests that text serialisation can be an avoidable bottleneck. It does not by itself establish that an analogous bridge is needed between REE subsystems.

### StateBridge — Peng et al., COLM 2026

**Source:** Peng Y, Zhang DC, Wang X, Aletras N. *StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems*. arXiv:2608.13317; reported as COLM 2026.

**Method:** sender final-layer hidden states are aligned to receiver input-embedding space through closed-form orthogonal Procrustes alignment, norm calibration, and vocabulary anchoring; no learned projector is required.

**Reported result:** best or tied-best on 22/26 evaluated model-task pairs across four models from two families.

**REE relevance:** unusually important because it provides a *complexity ladder*. If a near-orthogonal coordinate transformation is enough, a failure can be an interface-coordinate problem rather than missing content. This motivates trying the least expressive bridge first.

### Model stitching / functional latent alignment

The model-stitching literature asks whether the lower part of one network can feed the upper part of another through an adapter. This is useful because it operationalises functional compatibility rather than merely representational similarity.

**REE relevance:** a frozen E1/z_world producer + frozen E2/E3 consumer with an adapter is effectively a stitching assay. Success measures functional interface compatibility; it must not immediately be interpreted as evidence that REE should permanently contain the adapter.

## Evidence stream C — causal audit and negative controls

### Cheng, Das & Ramnath 2026

**Source:** *When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs*. arXiv:2608.04893.

The key intervention is replacement of the transmitted cache with:

- correct paired cache;
- mismatched-example cache;
- zero cache;
- moment-matched random cache.

The paper shows why this matters. In one natural cell, zeroing the relay cost 14.7 points while a mismatched cache cost only 0.4 points. A large "cache effect" therefore need not be a pairing/content effect.

### Zhang & Emu 2026

**Source:** *Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM*. arXiv:2607.26773.

This decomposes aggregate task effects into message-presence, message-identity/example-specific content, and separate-agent contribution. Results differ by model scale and task, demonstrating that a single benchmark delta does not identify the mechanism.

### REE methodological consequence

Any bridge assay should include, where meaningful:

- correct paired source state;
- mismatched state drawn from another episode/context with matched gross statistics;
- zero state;
- moment/covariance-matched random state;
- optionally self-state substitution / sender-identity controls;
- source feature ablations when a feature-specific causal claim is made.

A bridge that improves behaviour but shows `correct ~= mismatched >> zero` is evidence for channel/interface dependence, not example-specific information transfer.

## Evidence stream D — representational alignment and geometry

### Cross-disciplinary representational alignment

Sucholutsky et al., *Getting aligned on representational alignment* (2023, arXiv:2310.13018) provides a useful cross-field vocabulary connecting cognitive science, neuroscience and machine learning. The campaign should use it to avoid treating every similarity metric as equivalent.

### Candidate metrics / transformations for REE

Ordered roughly from least to more permissive:

1. direct native readout;
2. dimensionality-matched random projection floor;
3. orthogonal Procrustes map;
4. affine linear map;
5. low-rank linear adapter;
6. regularised nonlinear adapter;
7. high-capacity nonlinear bridge only as an upper bound, not as primary mechanistic evidence.

Complementary descriptive metrics:

- Representational Similarity Analysis (RSA);
- Centered Kernel Alignment (CKA);
- local neighbourhood preservation;
- canonical-correlation-family measures where appropriate;
- task-conditioned decoding and causal intervention rather than similarity alone.

The key issue is not whether two spaces look similar globally, but whether the task-relevant relational structure can be translated at low complexity and used by the actual consumer.

## Evidence stream E — neuroscience

### Hyperalignment

Haxby et al. and subsequent work show that different brains can contain shared information in idiosyncratic neural coordinates and can be projected into a common high-dimensional information space. The conceptual point for REE is strong but limited: conserved *informational geometry* need not imply matching unit identities.

### Complementary Learning Systems (CLS)

CLS distinguishes rapid, sparse episodic learning from slower overlapping statistical learning. Schapiro et al. (2017) further show complementary computations within hippocampal pathways: dentate gyrus/CA3 emphasising separated episodic representations and the monosynaptic entorhinal-CA1 pathway supporting more overlapping/statistical structure.

Older computational formulations explicitly describe CA1 as helping to "translate" between sparse CA3 and more overlapping entorhinal representations. This is an intriguing architectural analogue, not evidence that REE's E1/E2 interfaces should literally reproduce CA1.

### Sleep and representational transformation

Evidence supporting representational change during offline periods includes:

- Maboudi et al., Nature 2024, *Retuning of hippocampal representations during sleep*: sleep ripple representations predicted future place fields on re-exposure, supporting offline representational retuning.
- Guo et al., Cell Reports 2024/2025 indexing, *Latent learning drives sleep-dependent plasticity in distinct CA1 subpopulations*: high-dimensional hippocampal state space develops a lower-dimensional manifold resembling environmental structure, associated with sleep reactivation.
- Liu et al., Communications Biology 2025, *Slow-wave sleep and REM sleep differentially contribute to memory representational transformation*: item-level representations decreased while category-level representations were preserved; REM/SWS balance related to this transformation.
- Neuron/Nature Neuroscience 2025 work on sleep-cycle transformation of memory ensembles: ensemble state evolves from acquisition-like toward recall-like representations over sleep/rest, with non-REM and REM contributing differently.
- 2026 evidence continues to support precisely timed hippocampal-neocortical dialogue as important for consolidation.

**Boundary on inference:** these studies support offline representational transformation, replay, retuning and cross-region dialogue. The campaign has not yet found direct evidence that sleep specifically reduces the *mathematical complexity of a mapping between two independently specialised representational spaces*. That statement should remain labelled **REE hypothesis** unless stronger evidence is found.

## Evidence stream F — REE internal crosswalk

### Existing precursor documents

1. `docs/thoughts/2026-09-04_z_world_representation_contract.md`
   - information should survive if downstream systems need it;
   - auxiliary supervision is a probe, not an ontology commitment;
   - developmental representations should split/merge/reweight.

2. `docs/thoughts/2026-08-31_replay_driven_rebucketing_decision_relevant_representation.md`
   - decision consequences can provide pressure on representational sufficiency;
   - replay supports retrospective split/merge/reweighting;
   - sleep-like decoupling may permit safe maintenance of the representational coordinate system.

3. `evidence/planning` representation->authority->selection work (2026-08-26)
   - prior negative evidence from SD-004/SD-080/V3-EXQ-817a;
   - representation improvement without behavioural benefit when the consumer interface remained collapsing;
   - explicit interface-first vs differentiate-first ordering question.

### Current experiment families to cross-reference

- V3-EXQ-948: raw observation / latent / local-field positive demonstration.
- SD-018 + V3-EXQ-978: directional resource field through z_world.
- V3-EXQ-1008: compression + field-decode re-basing of frozen z_world.
- W4-S2 waypoint-field DV-range probe f00402c9.
- V3-EXQ-970a / 972a: ContextMemory write content and held-out linear decodability.
- MECH-135 / E1 rollout interface work: examples of information/action differentiation being crushed at a consumer transition.
- sleep/replay substrate including `force_sleep_cycle_at_eval_boundary` (de26949) and prior SWS/REM intervention experiments.

## Proposed REE assay family

### Assay 1 — Frozen Latent-Bridge Locus Assay

Freeze sender and receiver. Choose a known decision-relevant variable and compare:

- native interface;
- orthogonal Procrustes bridge;
- affine linear bridge;
- low-rank bridge;
- modest nonlinear bridge as an upper-bound arm.

Use held-out episodes/environments. Do not backpropagate through either endpoint.

Interpretation:

- native fails, orthogonal succeeds -> shallow coordinate mismatch;
- affine/low-rank required -> accessible content with more structured mismatch;
- only nonlinear succeeds -> content may be highly entangled; architectural interpretation becomes weaker;
- no bridge succeeds but richer source observation succeeds -> stronger evidence of upstream information loss.

### Assay 2 — Pairing-specific causal audit

For the best bridge from Assay 1 compare correct, mismatched, zero and moment-matched random source states.

Interpretation:

- correct >> mismatched ~= random -> example-specific causal information use;
- correct ~= mismatched >> zero -> generic channel/interface effect;
- correct ~= zero -> bridge/channel not load-bearing;
- mismatched actively harms -> receiver is content-sensitive but may be poorly calibrated.

### Assay 3 — Translation-complexity developmental trajectory

At matched checkpoints during development, estimate the minimum bridge class/capacity required for a fixed set of cross-system tasks. Possible measurements:

- native consumer score;
- Procrustes rescue;
- affine rescue;
- low-rank rank required;
- nonlinear rescue ceiling;
- correct-vs-mismatched pairing effect.

Hypothesis: useful subsystem co-development may increase native accessibility or reduce translation complexity even if the underlying representations remain specialised.

### Assay 4 — Pre/post replay or sleep interface-legibility assay

Measure the same frozen-endpoint alignment/bridgeability metrics immediately before and after a controlled replay/sleep intervention, separating:

- sender representation change;
- receiver representation/readout change;
- interface compatibility change;
- behavioural change.

A strong version of the REE hypothesis would predict that replay/sleep can improve correct-pair functional transfer or reduce required bridge complexity beyond what is explained by independent endpoint competence gains.

This assay must include a no-sleep/time-matched control and, where possible, replay-content controls.

## Architectural risk controls

A bridge should initially be an **instrument**, not production architecture.

Risks if installed too early:

- covert oracle / privileged information path;
- bridge becomes a second world model;
- high-capacity adapter memorises task mappings rather than aligning representations;
- apparent rescue masks a genuinely inadequate sender representation;
- behavioural success becomes uninterpretable because endpoints and bridge co-adapt;
- a new shortcut undermines developmental or biological constraints being tested.

Safeguards:

- frozen endpoints;
- parameter/capacity limits;
- low-complexity-first hierarchy;
- held-out layouts and contingencies;
- mismatched-message causal controls;
- explicit provenance;
- bridge removed after diagnostic where feasible.

## Provisional evidence grades

### Established / strong external support

- latent states can support communication across heterogeneous artificial models;
- some cross-model representations can be aligned by surprisingly simple transformations;
- text/token communication can be a severe interface bottleneck in some settings;
- benchmark benefit or zero-ablation sensitivity does not prove correct example-specific latent information is used;
- biological representations can share information geometry despite idiosyncratic coordinates;
- sleep/replay can transform and retune memory representations.

### Supported but scope-dependent

- low-complexity transformations can reveal functionally compatible representations across independently trained systems;
- specialised systems can cooperate without sharing identical internal coordinates;
- receiver/interface failure can mask an upstream representation improvement (supported directly by REE's V3-EXQ-817a lineage, though mechanism-specific).

### Plausible REE hypotheses

- E1, E2, hippocampal and decision-facing representations may be intentionally different yet mutually translatable;
- developmental progress may include improved mutual legibility between specialised systems;
- replay may train or recalibrate cross-system mappings in addition to changing representations;
- sleep may preferentially reduce translation complexity or repair representational interfaces while immediate sensorimotor demands are relaxed.

### Not established

- that Mostik's specific bridge method generalises beyond its reported demonstrations;
- that REE currently needs a permanent latent bridge;
- that there is a single universal latent geometry shared across all useful systems;
- that sleep biologically exists to align representational spaces;
- that increased representational similarity necessarily improves behaviour.

## Search gaps for the next research tranche

1. Full Mostik technical disclosure, code, patents, talks or post-competition ARC-AGI-3 description.
2. Detailed Interlat ablations, especially heterogeneous-model projector structure and content controls.
3. StateBridge failure cases: which model/task pairs resist orthogonal alignment and why.
4. Model-stitching literature distinguishing representational similarity from functional compatibility.
5. Causal representation-alignment studies where similarity changes but downstream behaviour does not.
6. Neuroscience explicitly measuring cross-region representational alignment before/after sleep or consolidation.
7. Developmental neuroscience on changing inter-area representational correspondence.
8. Hippocampal-neocortical interface models that treat translation/coordinate transformation explicitly.
9. Computational work on replay learning mappings between heterogeneous latent systems.
10. Security / alignment implications of opaque latent channels, including integrity and sensitive-information leakage.

## Candidate thesis for the eventual thought document

**Provisional only:**

> A cognitive system need not converge on one universal internal representation. Specialised systems may maintain different but partially compatible representational geometries. Part of successful cognition may therefore lie in preserving and learning low-complexity, causally effective translations between those systems. Development and offline consolidation may improve not only each representation, but their mutual legibility.

The thought document should not be drafted as if this thesis is already established. It should be built as an evidence-backed argument with explicit negative evidence, alternative explanations, and falsifiers.

## Decision rule for moving from campaign to thought

Draft the detailed thought when the campaign has enough evidence to answer, with explicit uncertainty:

1. What kinds of cross-system translation are empirically possible?
2. How simple can the transformations be?
3. When does alignment imply functional compatibility, and when does it not?
4. What causal controls demonstrate that transmitted content is actually used?
5. What biological analogues are genuinely supported rather than metaphorical?
6. Which existing REE results are better explained as information-loss failures versus consumer/interface failures?
7. Does the evidence justify a new REE hypothesis around development/replay/sleep and mutual legibility?
8. What discriminative experiments would falsify that hypothesis without installing a new architectural shortcut?
