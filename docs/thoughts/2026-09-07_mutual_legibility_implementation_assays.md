# Mutual legibility: implementation and assay companion

**Date:** 2026-09-07  
Status: processed
Intake: evidence/planning/thought_intake_2026-09-07_mutual_legibility.md
Claims registered: ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, INV-105

**Document type:** implementation thought / diagnostic design; not queued and not a claim registration
**Parent:** `2026-09-07_mutual_legibility_communication_subspaces.md`

## Purpose

This document translates the mutual-legibility thought into measurements, analysis code, controls, and possible later architectural options.

The first objective is **diagnosis without changing the organism**.

Bridges, projections, and communication-subspace models should initially be external instruments operating on frozen checkpoints and recorded trajectories. A successful diagnostic bridge is not evidence that REE should permanently contain that bridge.

The implementation programme should answer four questions in order:

1. **What information exists in the sender?**
2. **What portion of the sender is actually visible to the consumer?**
3. **Can a constrained transformation between frozen endpoints restore content-specific use?**
4. **Does the interface preserve the dynamics required by the consumer, not merely static decoding?**

---

## 1. Interface inventory

Candidate interfaces should be analysed as explicit producer -> consumer pairs rather than by naming modules globally.

### Tier A — immediately relevant to current V3 closure

1. `world_obs -> z_world`
2. `z_world -> E1` input/read pathway
3. `z_world -> E2` world/action pathway
4. `z_world -> current actor/policy reader` used in the 978/1002/1008 family
5. `ContextMemory write stream -> ContextMemory retrieval/consumer`
6. `E2 action-object representation O -> hippocampal CEM / decoder / eventual action`
7. `hippocampal candidate/proposal representation -> E3 score/selection`

### Tier B — developmental and sleep questions

8. `E1 predictive state -> E2/action consequence consumer`
9. `E2 predictive state -> E1/slow-model update` where a real consumer exists
10. `hippocampal replay state -> E1 consolidation update`
11. `hippocampal replay state -> self-model / schema / other sleep consumers`
12. `pre-sleep representation -> post-sleep consumer interface`

### Tier C — later architecture

13. object/token representations -> decision-facing state
14. social/agent representations -> attribution and ethical evaluation
15. language-facing latent -> internal state and vice versa

Do not infer a bidirectional interface merely because two modules coexist. Each analysis needs a concrete sender tensor, concrete receiver quantity, temporal alignment rule, and causal path.

---

## 2. Data capture contract

The first implementation should be a **read-only interface telemetry recorder**.

For each aligned timestep or candidate, record:

- `run_id`, seed, episode, timestep;
- environment state/condition identifiers suitable for held-out splitting;
- sender tensor before any proposed bridge;
- receiver input tensor at the actual consumption point;
- receiver preactivation/postactivation where feasible;
- candidate/action identity;
- relevant task targets, e.g. waypoint direction, resource direction, harm consequence, benefit consequence, action-conditioned delta;
- selected action / committed candidate;
- behaviour/outcome variables;
- provenance: observed vs replayed vs simulated/hypothesis;
- sleep/wake phase;
- checkpoint/hash of sender and receiver weights;
- any existing masks/gates/precision weights affecting the interface.

### Critical rule

The recorded `receiver` variable must be the **actual signal used by the live consumer**, not a convenient nearby tensor.

REE has repeatedly discovered failures where an intuitively named representation existed but the load-bearing path consumed a different quantity or consumed it before/after a collapsing transformation.

---

## 3. Held-out split doctrine

Interface analyses are unusually prone to leakage because adjacent timesteps are strongly correlated.

Do not randomly split individual rows.

Preferred hierarchy:

1. held-out environment/layout family;
2. held-out episode;
3. held-out contiguous trajectory blocks;
4. only if unavoidable, temporally blocked within-episode split.

For developmental or sleep comparisons, the evaluation set should be fixed across checkpoints when possible.

All transformation classes must receive the same training/evaluation split.

---

## 4. Baseline hierarchy

Before any trained bridge, establish the following.

### B0 — raw/richer-source ceiling

Can the target be decoded or behaviour be driven from the richer upstream source?

This establishes that the assay itself has range.

### B1 — native sender representation

Decode the task variable from the sender using the simplest predeclared probe appropriate to the target.

### B2 — dimensionality-matched random projection

For compressed representations such as `z_world`, compare against random linear projections of the richer source with the same dimension.

The waypoint-field result shows why this is mandatory: a severe random bottleneck can preserve substantial decodability.

Use multiple fixed projection seeds and report distribution, not one projection.

### B3 — native consumer performance

Measure what the actual consumer does without intervention.

### B4 — shuffled-label / shuffled-pair controls

Ensure the decode/bridge procedure cannot produce apparent signal on destroyed pairing.

---

## 5. Communication-subspace estimator

The primary initial method should be **cross-validated Reduced Rank Regression (RRR)** or an equivalent low-rank linear mapping from sender activity `X` to receiver activity `Y`.

### Why RRR

RRR directly estimates a low-dimensional sender subspace whose activity best predicts the receiver. It is therefore closer to the biological communication-subspace question than Principal Component Analysis (PCA) on the sender alone.

PCA asks:

> where does the sender vary most?

RRR asks:

> which sender directions matter for predicting this receiver?

Those can be very different.

### Model

Given centered matrices:

`X in R^(N x d_sender)`

`Y in R^(N x d_receiver)`

fit ranks `r = 1..r_max` under nested cross-validation.

Choose the smallest rank whose held-out predictive score is within a predeclared tolerance of the best rank or passes a predeclared receiver-prediction floor.

Report:

- held-out `R^2` / appropriate predictive metric;
- selected rank;
- variance in X explained by the communication subspace;
- variance in Y explained by mapped X;
- stability of subspace across seeds/checkpoints via principal angles;
- task-variable decodability inside vs orthogonal to the subspace.

### Essential comparison

Estimate:

`task information in full X`

versus

`task information in projection P_comm X`

versus

`task information in P_orth X`.

The critical phenotype is:

`target decodable from X` but `poorly decodable from P_comm X`.

That is evidence for routing/interface mismatch rather than sender information loss.

---

## 6. Subspace overlap metrics

For a task target `t`, fit a held-out linear decoder or define a target-relevant direction/subspace `S_task`.

Compare with communication subspace `S_comm` using:

- principal angles;
- squared projection overlap;
- canonical correlations;
- target decoding retained after projection into `S_comm`;
- target decoding retained in the orthogonal complement.

A simple interpretable metric:

`communication_retention = score(t | P_comm X) / score(t | X)`

with appropriate handling when the denominator is near zero.

Do not treat this ratio as universal evidence; report absolute scores alongside it.

---

## 7. Causal communication-subspace intervention

Correlation is insufficient.

Once `S_comm` is estimated, construct matched perturbations.

### Intervention A — remove task-relevant component within communication subspace

Project out the task-associated direction(s) from `P_comm X` while preserving other components as much as possible.

### Intervention B — matched removal outside communication subspace

Remove equal norm/variance from an orthogonal direction carrying comparable marginal sender variance.

### Intervention C — inject task direction into the communication subspace

Where safe and diagnostically meaningful, rotate or add the task-bearing component into `S_comm` without changing total dimensionality.

### Interpretation

- behaviour changes selectively under A but not B -> communication-subspace content is causally load-bearing;
- C rescues native failure -> strong routing/interface evidence;
- A and B have similar effects -> likely generic perturbation sensitivity;
- no intervention affects behaviour despite receiver prediction -> consumer computation may be downstream-limited.

Interventions should initially be evaluation-only with no learning.

---

## 8. Frozen-endpoint bridge ladder

When native access fails despite sender content, freeze sender and receiver parameters and fit increasingly expressive maps.

### L0 — identity/native

No bridge.

### L1 — orthogonal Procrustes

Fit `R` with `R^T R = I` between appropriately dimension-matched representations.

If dimensions differ, use a predeclared dimensional reduction/augmentation procedure rather than silently allowing arbitrary capacity.

Success at L1 is especially informative: mostly coordinate mismatch.

### L2 — affine linear

`y = Wx + b`

Regularise strongly and compare parameter count to data volume.

### L3 — low-rank affine

`W = UV^T`, rank constrained.

This is likely the most biologically/architecturally interpretable learned bridge class.

### L4 — constrained nonlinear

For example, one small multilayer perceptron with narrow bottleneck, explicit capacity limit, weight decay, and no recurrence.

### L5 — high-capacity upper bound

Only if necessary to establish whether the sender contains sufficient information in principle. Do not interpret L5 success as evidence of a plausible interface; the bridge may be performing new cognition.

### Required reporting

For every level:

- parameter count;
- training data volume;
- held-out receiver-state error;
- downstream behavioural effect;
- out-of-distribution receiver-state score;
- pairing-specific causal audit;
- dynamic-consistency score.

---

## 9. Receiver-manifold guard

A bridge can produce downstream success by driving the receiver with unnatural states.

Therefore map outputs should be compared against the receiver's native input/state distribution.

Candidate diagnostics:

- Mahalanobis distance under native receiver-state covariance;
- k-nearest-neighbour distance to native states;
- density under a simple held-out Gaussian mixture or normalising model if justified;
- norm and per-dimension distribution checks;
- Centered Kernel Alignment / representational neighbourhood checks as descriptive measures;
- receiver activation saturation rates;
- downstream hidden-state trajectory distance after one or more consumer steps.

Do not require exact in-distribution identity; a bridge may validly expose states not frequently visited natively. The guard is to detect extreme off-manifold shortcuts.

---

## 10. Pairing-specific causal audit

For a fitted bridge, evaluate at least:

1. **correct:** bridge the aligned sender state;
2. **mismatched:** bridge a sender state from another episode/context chosen from the same gross distribution;
3. **zero:** replace bridge input/output with zero at the defined boundary;
4. **moment-matched random:** preserve mean/variance or covariance as closely as practical while destroying content;
5. **optional same-action mismatch:** use another state sharing action label to distinguish action-class traffic from state-specific content;
6. **optional same-context mismatch:** preserve context while breaking exact state pairing.

This is particularly important for the action-object pathway, where prior work found representations dominated by action identity.

### Minimum interpretive categories

- `correct >> mismatched ~= random` -> pairing-specific content use;
- `correct ~= mismatched >> zero` -> generic channel/interface effect;
- `correct > mismatched > random/zero` -> mixed generic + content-specific contribution;
- `mismatched < zero` -> incorrect content is actively misleading;
- `correct ~= zero` -> channel is not load-bearing under this assay.

---

## 11. Dynamic compatibility assay

For predictive systems, pointwise alignment is insufficient.

### One-step test

Given sender state `x_t`, mapped receiver state `T(x_t)`, action/context `a_t`, and next sender state `x_(t+1)`:

compare:

`receiver_transition(T(x_t), a_t)`

with

`T(x_(t+1))`.

Metrics:

- latent transition error;
- cosine/directional transition agreement;
- local Jacobian similarity where feasible;
- preservation of action-conditioned ordering between alternatives;
- downstream rollout divergence over horizons 1, 2, 4, ...

### Multi-step test

Map only the initial state, then let the receiver evolve natively versus repeatedly mapping sender rollout states.

This separates a bridge that supplies a compatible starting condition from one that must continually correct incompatible dynamics.

### Interpretation

- good static + bad dynamic -> temporal/interface mismatch;
- good one-step + degrading long-horizon -> compounding dynamics mismatch;
- good dynamic but poor behaviour -> likely downstream valuation/selection issue.

---

## 12. Developmental mutual-legibility trajectory

At fixed developmental checkpoints, freeze snapshots and run the same assay battery.

Track:

- local subsystem competence;
- sender target decodability;
- communication-subspace effective rank;
- target overlap with communication subspace;
- minimal successful bridge class;
- minimal bridge rank/parameter count;
- pairing-specific content effect;
- dynamic compatibility;
- behavioural rescue.

### Desired signature

The strongest support for the developmental hypothesis is not merely decreasing bridge loss.

It is:

`local competence/specialisation improves`

while

`minimal interface complexity decreases or communication-subspace targeting improves`.

That would operationalise **specialisation up + mutual legibility up**.

---

## 13. Pre/post sleep interface assay

Use an identical evaluation dataset immediately before and after a controlled offline cycle.

Where possible use `REEAgent.force_sleep_cycle_at_eval_boundary` so the same organism and surrounding state can be sampled across the boundary.

Measure for each interface:

- sender representation drift;
- receiver representation drift;
- communication-subspace rotation (principal angles);
- effective rank;
- target overlap;
- bridge complexity;
- dynamic compatibility;
- pairing-specific causal effect;
- behaviour.

### Four possible sleep signatures

#### S1 — representational retuning

Sender changes; interface metrics change only because the sender changes.

#### S2 — interface recalibration

Sender/receiver local competence stable, but communication subspace or bridge complexity improves.

#### S3 — stable scaffold

Representations change while the interface mapping remains stable.

#### S4 — maladaptive homogenisation

Representations become more globally similar but local competence or task-specific differentiation worsens.

The hypothesis does not predict that all interfaces show S2. A plasticity/stability division of labour predicts different signatures at different boundaries.

---

## 14. Candidate first-pass loci

### Locus 1 — waypoint direction through z_world to the current actor/reader

Why first:

- the target variable and raw/random-projection floors are already established;
- five seeds and large sample counts already exist;
- current campaign asks exactly whether the trained `z_world` and downstream consumer preserve the field.

Questions:

1. trained `z_world` directional lift vs random-projection floor;
2. directional lift inside consumer communication subspace;
3. orthogonal complement lift;
4. native consumer sensitivity;
5. low-rank rotation rescue if needed.

### Locus 2 — V3-EXQ-817a action-object pathway

Why high value:

- clean prior case of representation grounding without behavioural benefit;
- known action-label dominance and decoder-collapse history;
- direct prediction of interface-first interpretation.

Questions:

1. does consequence information overlap the effective O -> decoder/planner communication subspace?
2. can a non-collapsing low-complexity readout expose it?
3. does correct state beat same-action mismatched state?

### Locus 3 — ContextMemory write -> retrieval consumer

Why valuable:

- current 970a/972a work already measures content in the write stream;
- clean opportunity to distinguish written, stored, retrieved, and used.

Questions:

1. content in write stream;
2. content in stored slots;
3. content in retrieval output;
4. content in actual downstream cue/action consumer;
5. causal effect of correct vs mismatched retrieved context.

### Locus 4 — pre/post sleep selected interface

Only after at least one waking interface metric is validated. Otherwise sleep analysis risks measuring an instrument rather than a biological/architectural property.

---

## 15. Suggested code shape

Keep diagnostics outside core behaviour initially.

Possible structure:

```text
analysis/
  latent_interfaces/
    capture.py
    datasets.py
    reduced_rank.py
    subspace_metrics.py
    bridges.py
    causal_replacements.py
    dynamics.py
    manifold_guard.py
    reports.py
```

Or equivalent experiment-local `_lib` modules if repository governance requires that location.

### Data objects

A minimal `InterfaceBatch` could contain:

```python
@dataclass
class InterfaceBatch:
    sender: Tensor
    receiver: Tensor
    target: Tensor | dict[str, Tensor]
    action: Tensor | None
    episode_id: Tensor
    timestep: Tensor
    context_id: Tensor | None
    provenance: list[str]
    metadata: dict
```

A `BridgeResult` should record:

```python
@dataclass
class BridgeResult:
    bridge_class: str
    rank: int | None
    n_parameters: int
    fit_metrics: dict
    heldout_metrics: dict
    manifold_metrics: dict
    dynamic_metrics: dict
    causal_audit_metrics: dict
```

Do not bake task-specific semantics such as `resource_direction` into the generic analysis layer.

---

## 16. Statistical discipline

### Nested model selection

Bridge class/rank selection must not use the final evaluation set.

Use:

- outer held-out episodes/environments for verdict;
- inner folds for rank/regularisation selection.

### Multiple seeds

Where interface geometry varies by seed, report both:

- within-seed result;
- cross-seed aggregate.

A bridge fitted across seeds can answer a different question from one fitted within each organism.

### Cross-organism bridge question

Later, explicitly test:

- within-checkpoint same-organism mapping;
- cross-seed mapping;
- cross-developmental-checkpoint mapping.

Success across seeds would indicate shared representational format; success only within an organism would still support mutual legibility without universal coordinates.

---

## 17. Failure signatures and routing

### F1 — sender target absent

Route to representation/training investigation. Do not build a consumer bridge.

### F2 — sender target present; communication subspace absent

Route to interface/routing investigation.

### F3 — communication subspace contains target; receiver behaviour insensitive

Route downstream to consumer computation, valuation, candidate diversity, or commitment.

### F4 — simple bridge rescues static receiver but not dynamics

Route to transition geometry / predictive-interface work.

### F5 — nonlinear high-capacity bridge alone rescues

Treat as upper-bound evidence only. Investigate whether bridge learned new task computation.

### F6 — correct ~= mismatched >> zero

Route as generic channel effect. Do not claim content transmission.

### F7 — correct >> mismatched but mapped states are grossly off-manifold

Bridge is causally informative but architecturally suspect; seek lower-capacity/in-distribution solution.

---

## 18. Architectural options only if diagnostics support them

### Option A — trained readout pairing

At designated compression sites, train the consumer/decompression stage jointly or in a phased schedule with the representation. This is the narrowest implication and aligns with MECH-532.

### Option B — low-rank consumer projection

Each consumer receives a small learned projection from a rich shared latent. Private sender dimensions remain unconstrained.

### Option C — context-gated communication subspaces

Different contexts select or rotate the low-rank projection used by a consumer.

This is more expressive and should not be introduced in V3 unless simpler diagnostics fail and evidence specifically motivates context dependence.

### Option D — offline interface recalibration

Freeze or partially freeze local representations while sleep/replay updates only selected interface projections.

This directly tests a plasticity/stability division of labour.

### Option E — dynamics-aware interface loss

Train an interface not only to match states but to preserve action-conditioned transition geometry.

### Option F — stable core + private dimensions

Explicitly partition a representation into:

- a small consumer-facing invariant/communication core;
- private specialised dimensions.

This is conceptually attractive but risks over-structuring the latent ontology. Prefer demonstrating an emergent low-rank communication subspace before hard-coding such a split.

---

## 19. Anti-shortcut safeguards

Any permanent or experimental bridge must respect:

- **no privileged environment labels at inference** unless the experiment is explicitly a supervised upper bound;
- **no hypothesis/replay state counted as external evidence**;
- **no backpropagation into frozen endpoints** in diagnostic bridge assays;
- **no bridge access to future outcomes**;
- **no action label leakage** when testing state-specific consequence information;
- **no per-arm RNG/model-construction asymmetry** that changes unrelated untrained paths;
- **same evaluation data across bridge classes**;
- **same parameter budget controls where architecture claims depend on bridge form**;
- **explicit out-of-distribution checks**;
- **correct-vs-mismatched causal control** before content-transmission claims.

---

## 20. Minimal viable diagnostic

If the full programme is too expensive initially, the cheapest useful version is:

1. capture sender and actual consumer tensors on the existing waypoint dataset;
2. fit cross-validated RRR ranks 1..min(16, dims);
3. measure waypoint-direction decode in full sender, communication subspace, and orthogonal complement;
4. fit orthogonal/low-rank bridge to consumer input;
5. compare native vs bridged consumer behaviour/score on held-out episodes;
6. run correct-vs-mismatched-vs-zero bridge inputs;
7. report mapped-state norm and nearest-native-state distance.

This single assay can already separate:

- missing sender content;
- routing mismatch;
- shallow coordinate mismatch;
- generic channel effect;
- downstream consumer insensitivity.

---

## 21. What should not be done yet

- Do not add a universal `LatentBridge` module to `ree_core`.
- Do not train all modules toward global CKA/RSA similarity.
- Do not optimise communication-subspace rank toward being as small as possible without a competence constraint.
- Do not treat a successful nonlinear bridge as proof the upstream representation was adequate.
- Do not use probe success as a substitute for causal content tests.
- Do not queue a sleep mutual-legibility experiment until the waking interface metric itself has demonstrated stability and range.

---

## 22. Immediate implementation recommendation

The highest-value first engineering task is a **read-only communication-subspace analysis harness** attached to a current, already well-characterised `z_world -> consumer` dataset.

It should produce one report containing:

- raw/rich source target decode;
- trained sender decode;
- random-projection floor;
- RRR receiver-prediction curve by rank;
- task-target retention in communication and orthogonal subspaces;
- principal-angle/subspace stability across seeds;
- bridge ladder results;
- receiver-manifold diagnostics;
- correct/mismatched/zero causal audit;
- interpretation category F1-F7.

Only after this report exists should REE decide whether a new architectural mechanism is warranted.
