# Thought: Decision-Useful Counterfactual World Models Under Uncertainty

**Date:** 2026-09-02  
**Status:** Raw evidence-backed thought; hypothesis-generating; not ingested; no claim, version, build, or experiment is authorised by this document.  
**Scope:** Full Reflective–Ethical Engine (REE) lineage, with immediate relevance to the E1/E2/hippocampus/E3 interface and later relevance to continual learning and sleep.  
**Primary repositories:** `REE_assembly`, `ree-v3`  
**Nearby claims and contracts:** ARC-001, ARC-002, ARC-003, ARC-018, MECH-033, MECH-057, MECH-094, ARC-120, ARC-130, ARC-131, MECH-507, MECH-509, MECH-510, MECH-511, INV-103  

## Core question

What must REE preserve about possible futures for action selection to remain causally sensitive, uncertainty-aware, and behaviourally effective?

The answer may be narrower than "predict the world accurately" and broader than "assign a value to each action."

Three recent preprints suggest a useful three-part distinction:

1. a decision system may benefit from representing **what differs between candidate actions**, rather than spending all of its capacity predicting what will happen under every action;
2. under partial observability, prediction must preserve a **belief over compatible hidden continuations**, rather than silently collapsing uncertainty into one point estimate; and
3. even when a world model retains useful knowledge, the pathway that reads that knowledge into behaviour may fail.

For REE, these proposals converge on one architectural question:

> **Does the organism carry the action-relevant differences and residual uncertainty in its predictive state far enough through proposal, comparison, selection, commitment, and enactment to change what it actually does?**

This is not a proposal to add a generic world-model module. REE already has a typed predictive architecture. The possible refinement is to distinguish three predictive objects within that architecture:

- an **absolute predictive context** describing what the world is likely to do;
- a **counterfactual action-effect representation** describing what the organism's candidate actions change relative to one another; and
- a **belief structure** preserving unresolved alternatives and uncertainty while either object is projected forward.

The first is needed for perception, anomaly detection, safety monitoring, causal attribution, and learning. The second may be a compact decision-facing view. The third prevents both from becoming falsely determinate.

## Existing REE ownership boundaries must remain intact

The current architecture already separates responsibilities that much machine-learning literature calls collectively a "world model":

- **E1** is the persistent predictive substrate. It maintains slow world/self regularities, causal context, long-horizon structure, and unresolved hypotheses. It must not be reduced to a decision-only quotient.
- **E2** is the fast forward predictor. It supplies short-horizon action-conditioned transition structure and reafference expectations. It is not an explicit trajectory planner.
- **Hippocampal systems** chain local transition structure into explicit multi-step candidate trajectories, under E1 constraints and control-plane parameters.
- **E3** evaluates, selects, and commits. It does not generate the imagined trajectories it adjudicates.
- **The control plane** governs precision, eligibility, mode, gain, interruption, and write access. Predictive outputs do not acquire authority merely by existing.

This typed split is important because the external papers use broader terms. Their mechanisms should be translated into REE's ownership model rather than imported wholesale.

The strongest candidate mapping is:

| Predictive requirement | Probable REE owner | Important boundary |
|---|---|---|
| Persistent absolute context and action-independent dynamics | E1 | Must retain information that is irrelevant to the current choice but important to perception, anomaly detection, safety, later objectives, and learning |
| Short-horizon action-conditioned effect | E2 | Local transition/effect kernel, not multi-step planning or commitment |
| Multi-step branching futures | Hippocampal systems | Chains E2 kernels under E1 constraints; retains provenance and hypothesis status |
| Relative comparison and action ranking | E3 inputs and scoring | Derived decision-facing view; E3 remains selector, not predictor |
| Confidence, residual uncertainty, and eligibility | Control plane and typed prediction outputs | Uncertainty is not identical to prediction error magnitude or value |
| Behavioural expression | Commitment and downstream action-selection pathway | Internal selection is not yet ecological consequence |

## Evidence thread 1: predict what choices change

Chen, Wang and Li's 2026 preprint, *Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does*, asks whether a decision system needs a full prediction of each action-conditioned future.

Their Counterfactual Quotient Model (CQM) treats two sets of action-conditioned futures as decision-equivalent when they differ only by a component shared across every action. A centred representation removes this common component while preserving pairwise action comparisons for the modelled reward family. In the most general formulation, the retained object is a signed successor measure with zero total mass: it records which future events become more or less likely under one intervention relative to the action baseline.

The central insight is not simply dimensionality reduction. It is a change in the learned target:

> **Predict the action effect directly, rather than predict several absolute futures and subtract them only after approximation.**

Using synchronized counterfactual branches with common random numbers, the method cancels action-independent stochastic variation before function approximation. In four controlled DeepMind Control Suite domains augmented with high-dimensional common dynamics, the model improved held-out action ranking and normalized regret relative to equally sized absolute-future and successor-feature predictors. The advantage was large in Cartpole and Reacher, smaller in Cheetah, and narrow with overlapping uncertainty in Walker. Walker is therefore an important stress result: targeting the quotient did not compensate for inadequate representational capacity.

The authors explicitly limit the claim. Their experiments use state observations, simulated action-independent dynamics, random linear reward queries, and resettable synchronized branches. They do not establish native-task control, pixel-level robustness, multi-agent performance, or real-world learning. The practical finite feature representation is exact only for rewards within the selected feature family. The quotient also deliberately discards action-independent information needed for other functions.

### REE interpretation

This is not evidence that E1 should become an action-effect quotient. E1 must preserve much of what CQM intentionally removes.

It does suggest that the E2-to-hippocampus-to-E3 path may benefit from a **derived centred action-effect view** alongside absolute predictions. In a state `s`, with candidate action set `A`, a simple finite form would resemble:

`effect(s, a) = future_features(s, a) - sum_b rho(b|s) future_features(s, b)`

where `rho` is a declared action baseline. The exact form is less important than the separation:

- absolute prediction asks, "what is likely to happen?";
- effect prediction asks, "what changes because of this candidate?"

That distinction is directly relevant to self-attribution, reafference, and the commitment boundary. A system can model environmental evolution accurately while remaining poor at estimating its own causal contribution. Conversely, an action-effect representation can support choice while being an impoverished world model.

### Important REE caution: synchronized branches are privileged supervision

The strongest CQM results depend on resetting the same starting state and reusing exogenous randomness across candidate actions. REE's simulator can provide such branches experimentally, but the organism normally receives only the realized branch.

Accordingly, synchronized quotient targets should initially be treated as an **oracle or ceiling condition**, useful for asking whether a clean action-effect representation would improve downstream comparison. They cannot establish that REE can learn the same representation endogenously from ordinary experience.

A later production-path test would need to determine whether approximate action effects can be learned from:

- ordinary experienced trajectories;
- E2 reafference residuals;
- matched or near-matched episodic anchors;
- intervention-aware replay whose provenance remains explicit; or
- a learned generative model whose own bias is measured rather than hidden.

This distinction aligns with INV-103 and with the causal-reach doctrine: an externally supplied counterfactual can test downstream sensitivity without proving endogenous competence.

## Evidence thread 2: preserve uncertainty through imagination

Radha and Goktas's 2026 preprint, *UWM-JEPA: Predictive World Models That Imagine in Belief Space*, addresses a different failure. Under partial observability, one observation history may remain compatible with several hidden states and future continuations. A single vector prediction can achieve a low training loss while averaging away precisely the uncertainty needed for counterfactual action reasoning.

Their Unitary World Model Joint Embedding Predictive Architecture (UWM-JEPA) represents the latent as a density matrix and advances it using unitary dynamics. This supplies an exact joint-state non-dissipation property: the predictor cannot itself erase the joint latent's spectrum, purity, or entropy during blind rollout.

The empirical separation is more useful than the specific quantum-inspired parameterisation:

- teacher-forced targets allowed the learned action term to collapse because the target encoder had already observed the future;
- counterfactual targets restored action sensitivity;
- the proposed predictor preserved more short-horizon information during blind rollout than the tested vector predictors;
- a held-out context probe found no meaningful encoder advantage, locating the difference in latent geometry and predictor dynamics rather than initial context encoding; and
- both model families degraded at longer horizons, so the paper does not establish durable long-horizon belief preservation.

The authors also do not claim calibrated Bayesian posteriors over the true hidden state. Their "belief state" is operational: a structured latent capable of carrying unresolved modes and correlations through prediction.

### REE interpretation

The density-matrix implementation should not be imported merely because it preserves a mathematical invariant. REE already permits unresolved hypotheses in E1 and already requires uncertainty provenance and calibration in its Joint Embedding Predictive Architecture reference contract.

The transferable requirement is narrower:

> **A predictive state used for counterfactual action comparison should not become more certain merely because it has been rolled forward without new evidence.**

This suggests several REE checks:

- Does an E2 local transition preserve action sensitivity when the future observation is unavailable?
- When hippocampal systems chain transitions, does uncertainty widen, remain calibrated, or collapse silently?
- Can two candidate trajectories remain behaviourally distinguishable when they share the same expected endpoint but differ in uncertainty, hidden-mode composition, harm tail, or reversibility?
- Does confidence have declared provenance, rather than being an alias for residual magnitude or latent norm?
- Does teacher forcing let E2 ignore the candidate action while still attaining low predictive loss?

This thread reinforces the need to distinguish expected future content from uncertainty about that content. It also supports MECH-510's separation between generative precision and prediction-error precision: a predictor can be unsure which future applies while a subsequently observed discrepancy is highly reliable, or vice versa.

## Evidence thread 3: retained knowledge can fail to become behaviour

Nijjer's 2026 preprint, *The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based Reinforcement Learning*, localizes catastrophic forgetting in a small Dreamer-family agent trained across MiniGrid task chains.

With a never-cleared replay buffer, component probes found preserved reward discrimination, values, and termination structure for earlier tasks while behavioural performance collapsed. Under a frozen world model and identical imagined data, standard reinforcement learning in imagination recovered the lost skill in zero of three seeds; supervised self-imitation from graded imagined trajectories recovered it in three of three seeds. Interleaved dream rehearsal retained four-task and eight-task chains in all three reported seeds, while the plain replay baseline failed the four-task chain in all three.

The paper is unusually explicit about scope and failure analysis. It uses a 17-million-parameter agent, MiniGrid chains, and three seeds. It reports latent drift despite preservation by co-trained world-model heads: "world-model memory" does not mean a frozen geometry. Its strongest finding is therefore not a general law that actors always forget. It is a component-level dissociation within one replay-maintained regime.

### REE interpretation

This is direct external support for a diagnostic principle already present in ARC-120, ARC-130, and ARC-131:

> **Retained representation is not retained behavioural competence.**

For REE, the relevant chain is more differentiated than "world model to actor":

`representation -> endogenous recruitment -> local prediction/proposal -> competitive authority -> selection -> fresh commitment -> execution -> ecological consequence -> retention/generalisation`

A predictive substrate may remain competent while any downstream edge fails. An experiment that measures only E1/E2 loss or hippocampal rollout fidelity can therefore report a false green while the organism has lost the corresponding behaviour.

The paper's dream self-imitation mechanism should not be imported directly. Training an action pathway on model-generated trajectories creates a live tension with MECH-094, which prevents imagined content from being written as committed experience. REE may need offline rehearsal to preserve access or authority without confusing imagination with occurrence, but the safe update target and provenance rules remain unresolved.

Possible distinctions include:

- rehearsal of **policy accessibility** without writing the imagined episode as autobiographical fact;
- rehearsal of **ranking or readout mappings** while retaining a hypothesis tag;
- consolidation from previously realized successful trajectories, rather than from model-only success;
- model-generated candidates used to probe competence, with durable update gated by later real evidence; and
- sleep-phase updates to confidence or eligibility rather than direct reinforcement of imagined outcomes.

The external result therefore sharpens a question; it does not answer REE's write-governance problem.

## Combined proposal: two predictive views, one uncertainty-bearing path

The three papers together suggest a possible refinement:

> **REE may require both an absolute world-predictive view and a centred action-effect view, with residual uncertainty preserved through the path that converts either view into explicit trajectories and committed behaviour.**

The action-effect view is not a second world. It is a quotient or contrast derived from action-conditioned predictions. It should remain linked to:

- the absolute prediction from which it was derived;
- the candidate action and continuation policy;
- the action baseline used for centring;
- the uncertainty and hidden-mode structure of each branch;
- provenance: experienced, inferred, replayed, simulated, or externally injected;
- the reward, harm, goal, identity, and responsibility query under which the comparison is valid; and
- the eventual realized branch, so attribution can be recalibrated.

Without those links, an efficient quotient could become epistemically dangerous. It might rank the current actions accurately while becoming blind to shared hazards, anomalous environmental changes, another agent's independently evolving state, or a later change in objectives.

The safest architectural reading is therefore asymmetric:

- **E1 preserves the richer absolute and causal context.**
- **E2 may expose both absolute local predictions and centred action-conditioned deltas.**
- **Hippocampal systems may chain these while retaining branching uncertainty and provenance.**
- **E3 may consume relative comparisons without owning their generation.**
- **The control plane decides how much authority a prediction earns, not the predictor itself.**

## What is genuinely new for REE

Most of the combined argument is already owned in pieces:

- E1/E2/hippocampus/E3 responsibility boundaries already exist.
- `action_conditioned_delta_error` already appears in the Joint Embedding Predictive Architecture integration contract.
- MECH-507 already proposes explicit compression/decompression.
- MECH-509 already proposes an E1-conditioned pre-rollout possibility field.
- MECH-510 already separates generative precision from error precision.
- MECH-094 already distinguishes simulated from experienced content.
- ARC-120, ARC-130, and ARC-131 already separate representation, competence, authority, throughput, and installability.

The narrow additive synthesis is:

1. **Action-effect quotient as a named derived predictive object.** REE has action-conditioned predictions and delta metrics, but may not yet explicitly distinguish a learned decision-sufficient contrast from the richer absolute predictor.
2. **Uncertainty non-dissipation as a rollout property.** Calibration at input is insufficient if prediction dynamics silently collapse alternative hidden continuations.
3. **A matched three-way validation.** Representation quality, decision usefulness, and behavioural reach should be measured separately in the same experiment.
4. **A productive conflict with simulation-write governance.** Dream-based behavioural preservation may be useful, but only if REE can preserve access without converting imagination into falsely experienced history.

This does not presently justify a new module. It may justify a refinement of ARC-002/MECH-033 interface language, a literature-backed experiment design, or an open question about whether an action-effect view should be learned directly or derived at comparison time.

## Discriminating experiment family

No new scoreboard is required. The experiment should reuse existing REE prediction, uncertainty, commitment, and causal-reach telemetry.

### Experiment A: absolute prediction versus action-effect targeting

Train matched-capacity predictors on the same environment histories:

- **ABS:** predicts absolute local future features for each action;
- **DELTA-DERIVED:** predicts absolute futures, then centres them across candidate actions;
- **DELTA-DIRECT:** learns the centred action effect directly from synchronized branches;
- **VALUE:** predicts the current task's scalar action value as a task-specific upper comparator.

Introduce high-variance action-independent dynamics that are perceptible but do not change across the candidate first action. Measure:

- existing `action_conditioned_delta_error`;
- pairwise action-ranking accuracy;
- normalized decision regret;
- calibration under action perturbation;
- absolute-future error as a negative-control trade-off;
- E3 candidate-score spread and chosen-action changes;
- fresh commitment and ecological outcome; and
- preservation of anomaly/safety sensitivity through the absolute channel.

The synchronized DELTA-DIRECT arm is an oracle/ceiling condition. A later arm must attempt the same learning from ordinary trajectories before endogenous competence can be claimed.

### Experiment B: point prediction versus uncertainty-preserving prediction

Use a partially observable environment in which identical visible states correspond to multiple hidden continuations. Compare matched predictors that differ only in whether the rollout state can preserve multimodality or ensemble dispersion.

Measure:

- existing `latent_uncertainty_calibration_error`;
- existing `latent_rollout_consistency_rate`;
- action sensitivity under counterfactual perturbation;
- uncertainty change with rollout horizon in the absence of evidence;
- hidden-mode probe retention;
- candidate diversity and premature branch collapse;
- commitment timing, reversal, and interrupt rate; and
- whether encoder quality is matched while predictor dynamics differ.

The claim is weakened if a simpler calibrated ensemble or mixture representation performs as well as a structurally richer belief state. The density-matrix construction has no privileged status.

### Experiment C: retained predictive competence versus behavioural access

After the agent learns several sequential regimes or tasks, probe separately:

- E1/E2 predictive retention;
- hippocampal proposal quality;
- E3 ranking and selection;
- competitive authority relative to other scoring terms;
- fresh commitment rather than hold/stale continuation;
- executed behaviour; and
- ecological outcome.

Where behaviour fails despite retained prediction, intervene at progressively later edges. A downstream rescue localizes the broken path but does not certify endogenous reach.

Any rehearsal intervention must preserve MECH-094 provenance. Simulated trajectories must not silently become committed autobiographical experience.

## Support conditions

The combined proposal would gain support if:

- direct action-effect learning improves relative action geometry or regret specifically when common-mode dynamics dominate, under matched parameter and data budgets;
- the improvement reaches E3 selection, fresh commitment, and ecological performance rather than remaining a probe-only effect;
- absolute prediction remains available for safety, anomaly detection, and later objectives;
- a structured or ensemble belief state preserves calibrated action-relevant uncertainty better than a point latent during blind rollout;
- the uncertainty advantage lies in the predictor path rather than a stronger encoder;
- production-path learning approximates the oracle action-effect ceiling without requiring privileged synchronized branches; and
- offline rehearsal preserves behavioural access without erasing simulated/experienced provenance.

## Falsifiers and boundary findings

The proposal should be revised or rejected if:

- centred action effects add no decision benefit over an equally sized absolute predictor in environments with genuine common-mode variation;
- apparent gains disappear when the evaluation uses native objectives, unseen action sets, changed continuation policies, or non-linear reward queries;
- quotient targeting removes shared information needed to detect hazards or model another process and the parallel absolute channel does not protect it;
- uncertainty-preserving structure gives no advantage over a simpler calibrated ensemble or mixture;
- belief uncertainty remains mathematically present but is inaccessible to E3 or the control plane;
- counterfactual targets improve probes but do not change action ranking or commitment;
- the world model retains task information but the proposed readout repair still fails, locating the problem elsewhere;
- dream rehearsal works only by allowing imagined outcomes to acquire the same write authority as experienced outcomes; or
- the new view duplicates existing E2 delta computation without changing prediction, attribution, commitment, or behaviour.

Several nulls would be useful boundary findings rather than failures of REE. For example, quotient targeting may help only when action-independent dynamics dominate representational capacity; belief preservation may matter only beyond a threshold of partial observability; and behavioural-access failure may arise only under particular continual-learning regimes.

## Version and governance routing

This thought concerns the full lineage. It should not silently pull a new representation into V3.

- If current V3 closure already requires a discriminative action-effect signal or uncertainty-preserving rollout, the relevant minimum follows the dependency into V3.
- Rich learned quotient representations, belief-structured latent dynamics, changed action sets, multi-object consequences, and dream-based behavioural rehearsal appear more naturally aligned with later substrate unless a current gate proves them necessary.
- Social action effects must not subtract away another agent's independent evolution merely because it is shared across the current action set. V5 social attribution will need an explicit distinction between "unchanged by me" and "irrelevant."
- No claim should be registered or promoted until the novelty and conflict audit is completed against ARC-002, MECH-033, MECH-094, MECH-507-511, ARC-130, and ARC-131.

## Candidate harvests for later intake

These are candidate formulations only.

### Candidate interface refinement

> E2 may expose a centred action-effect representation derived from its action-conditioned local predictions, while E1 retains the richer absolute and action-independent predictive context. The derived view is decision-facing and must not replace the source world model.

This is likely an ARC-002/MECH-033 refinement or implementation hypothesis, not a new engine.

### Candidate rollout requirement

> Prediction without new evidence must not gain unjustified certainty. Action-relevant uncertainty and alternative hidden continuations should remain recoverable through the predictive path for as long as they remain unresolved.

This may already be substantially covered by the uncertainty fields in the Joint Embedding Predictive Architecture integration contract and MECH-510. A duplication audit is required.

### Candidate experimental doctrine

> Predictive retention, decision usefulness, and behavioural reach are separable outcomes and should be measured independently in world-model experiments.

This likely belongs as an application of ARC-130/ARC-131 rather than as a new claim.

### Candidate open question

> Can REE use imagined trajectories to preserve behavioural access without granting simulated content the autobiographical or reinforcement authority of experienced events?

This should remain an open question until reconciled with MECH-094 and the sleep/write-governance architecture.

## Provisional formulation

> **A useful REE predictor must preserve more than an expected future and less than an exhaustive simulation. E1 must retain the absolute causal context; E2 must expose how immediate candidate actions alter it; hippocampal systems must carry those differences and their unresolved uncertainty through explicit trajectories; E3 must compare rather than generate them; and the committed organism must remain able to turn retained predictive competence into behaviour. What matters is not merely whether the future was represented, but whether the action-relevant difference survived approximation, uncertainty survived imagination, and both survived the path into lived consequence.**

## Primary sources

1. Chen J, Wang R, Li J. *Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does*. arXiv:2608.22092, 2026. https://arxiv.org/abs/2608.22092
2. Radha SK, Goktas O. *UWM-JEPA: Predictive World Models That Imagine in Belief Space*. arXiv:2605.25313, 2026. https://arxiv.org/abs/2605.25313
3. Nijjer G. *The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based Reinforcement Learning*. arXiv:2607.19749, 2026. https://arxiv.org/abs/2607.19749

All three are preprints. Their evidential role here is mechanism generation, boundary sharpening, and experiment design—not validation of REE.

## Internal references

- `docs/architecture/e1.md`
- `docs/architecture/e2.md`
- `docs/architecture/e3.md`
- `docs/architecture/hippocampal_systems.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `docs/architecture/trajectory_selection.md`
- `docs/architecture/state.md`
- `docs/architecture/causal_reach_and_installability.md`
- `docs/architecture/reafference_comparator_family.md`
- `docs/thoughts/2026-02-09_e2_hpc_interface.md`
- `docs/thoughts/2026-08-12_affordance_indexed_temporally_displaced_present.md`
- `docs/thoughts/2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`
- `evidence/planning/thought_intake_2026-08-24_compression-decompression-prospective-attractors-barrett-miller-convergence.md`

## Possible affected components and processes

- E2 local action-conditioned prediction and delta outputs
- E2-to-hippocampal kernel handoff
- hippocampal candidate generation under partial observability
- E3 candidate comparison and commitment telemetry
- reafference and self-attribution
- uncertainty provenance and precision routing
- MECH-094 simulation/experience write separation
- ARC-130 causal-reach traces
- ARC-131 installability testing
- continual-learning and sleep-phase behavioural-access preservation
- future social attribution and self/other causal-effect separation
