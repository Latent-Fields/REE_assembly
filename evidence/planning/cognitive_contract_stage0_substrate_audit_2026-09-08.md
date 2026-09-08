# Cognitive contract narrowing-stack programme — Stage 0 substrate audit

**Date:** 2026-09-08  
**Status:** completed Stage-0 audit / experiment-readiness note; not architecture and not a build instruction  
**Programme:** ARC-142 / GOV-CONTRACT-1 / MECH-545  
**Pre-registration:** `evidence/planning/cognitive_contract_narrowing_stack_preregistration_2026-09-08.md`  
**Audited implementation:** `Latent-Fields/ree-v3` `main` at `8e57e473496b2adda2f969a9c43058931745ab22`

---

## 1. Stage-0 verdict

**G0: CONDITIONAL PASS — instrumentation-light, not substrate-not-ready.**

The live V3 substrate already supplies:

- several genuinely different downstream consumer families;
- full-width latent taps at the relevant internal levels;
- a purpose-built per-step vector recorder with freshness/validity metadata;
- a canonical experiment harness that drives the split sensory/harm streams correctly;
- a generic content-addressed trace store for multidimensional arrays;
- an existing shared-latent gradient-coupling probe.

The principal remaining work before the first offline test is **experiment assembly and label/trace validation**, not architecture redesign.

There are, however, three constraints that make a direct “run the current stack and declare victory” invalid:

1. **The current live stack is not a monotonically narrowing hierarchy.** Default dimensions are `z_self=32`, `z_world=32`, `z_beta=64`, `z_theta=32`, `z_delta=32`. The first shared step therefore has 64 input dimensions and 64 beta dimensions before narrowing to 32. The narrowing hypothesis must initially be tested in the pre-registered auxiliary bottleneck harness rather than retroactively reading the current stack as its implementation.
2. **REE is asynchronous.** E1, E2, E3 and other streams update at different rates. Repeated stale values can manufacture apparent cross-stream structure unless freshness flags are respected.
3. **Not every candidate invariant has a clean V3 ground-truth label.** The first assay should use the subset that can be derived without inventing semantic supervision, and explicitly mark the rest not-yet-testable rather than creating labels to make the theory work.

---

## 2. Live latent substrate

`ree_core/latent/stack.py` declares the V3 split and module contract:

```text
body observation  -> z_self   [32 default]
world observation -> z_world  [32 default]

concat(z_self, z_world)
       -> z_beta              [64 default]
       -> z_theta             [32 default]
       -> z_delta             [32 default]
```

The shared channels have different intended roles:

- `z_beta`: affective/arousal-valence integration;
- `z_theta`: sequence/temporal context;
- `z_delta`: regime/motivation/long-horizon context.

Top-down conditioning also returns from the shared stack toward the split encoders, so this is a recurrently interacting hierarchy rather than a one-way encoder.

### Important negative conclusion

The current dimensions do **not** instantiate the proposed “fewer nodes at every higher level” design. That is useful: it prevents us from confusing an attractive interpretation of the current model with a test of the new hypothesis.

For the first experiment, progressive width restriction belongs in an **auxiliary frozen-source bottleneck**, as already pre-registered.

---

## 3. Distinct consumer families are already present

The G0 requirement was at least three heterogeneous consumers that can be specified without contract labels. V3 clears this comfortably at the conceptual/API level.

### Consumer family 1 — E1 persistent prediction

`ree_core/predictors/e1_deep.py`:

- reads concatenated `z_self + z_world`;
- predicts next `z_self + z_world` jointly;
- maintains recurrent hidden/context state;
- is trained on sensory prediction error.

This provides a slow/persistent predictive objective.

### Consumer family 2 — E2 action-conditioned forward structure

`ree_core/predictors/e2_fast.py` provides several distinct action-conditioned targets:

- `z_self_t + action -> z_self_{t+1}`;
- `z_world_t + action -> z_world_{t+1}` for causal attribution;
- `(z_world_t, action) -> action_object`, an explicit low-dimensional world-effect representation;
- counterfactual rollouts.

E2 therefore supplies transition/control information without being trained as a harm/value predictor.

### Consumer family 3 — E3 evaluation/commitment

`ree_core/predictors/e3_selector.py`:

- operates over `z_world`;
- evaluates harm and goal information;
- carries dynamic precision derived from prediction-error variance;
- distinguishes candidate trajectory selection from commitment.

This is substantially different from E1/E2 prediction.

### Consumer family 4 — hippocampal trajectory/action-object machinery

The hippocampal system consumes action-object/world structure for trajectory proposal, indexing, replay and related memory functions. This supplies a sequence/memory consumer distinct from the predictor losses.

### Additional consumers

Residue/world-delta accumulation and harm/benefit pathways can provide further downstream utility, but the first experiment does not need to inflate the consumer count. The cleanest initial E-arm should use a small set of genuinely distinct losses with transparent provenance.

**G0 consumer verdict:** PASS at the substrate/API level. Exact loss adapters still need to be frozen in the Stage-2 harness before training.

---

## 4. Recording readiness is much better than the old corpus suggests

The July experimental-recording audit correctly warned that the historical corpus was too sparse for many later latent questions. Crucially, the repository now contains a purpose-built remedy:

`experiments/_lib/stream_recorder.py`

Its own design rationale explicitly records the prior failure: scalar norms had collapsed a multi-dimensional latent and destroyed the configuration needed for cross-stream analysis. The recorder therefore uses:

> **VECTORS, NOT NORMS. Every latent stream is stored at full width.**

The implementation converts tensors to flat float32 vectors and stores fixed-width arrays per stream. Its primary snapshot includes:

- `z_self`;
- `z_world`;
- `z_beta`;
- `z_theta`;
- `z_delta`;
- `z_harm` when present;
- `z_harm_a` when present;
- plus E1 hidden state and a range of control/integration/commitment/event streams later in the recorder.

`z_goal` is also recorded when present, with an explicit warning that it remains flat unless the experiment loop calls `update_z_goal()`.

This corrects an earlier provisional assumption in this research session that only latent summary statistics were available. **Full vectors are already supported.**

---

## 5. Freshness metadata is load-bearing for this experiment

The recorder contains exactly the protection this programme needs against a serious false positive.

REE's components operate on different clocks. Some values are recomputed each environmental tick while others are held between E3 or other module updates. Naively correlating the recorded matrices would therefore detect strong regularity arising from **sample-and-hold cadence**, not cognitive organisation.

`StreamTraceRecorder` writes, for every signal:

- `<name>__fresh`;
- `<name>__valid`;
- a declared freshness derivation (`identity`, `clock`, `value`, or `event`).

Its documentation explicitly identifies the failure mode: repeated held E3 values can manufacture apparent cross-stream shared structure.

### Mandatory analysis rule

All geometry, cross-stream alignment and temporal-dependence analyses in this programme must either:

1. operate on genuinely fresh samples for the relevant stream pair; or
2. use a model that explicitly accounts for held/stale intervals.

Treating held values as independent observations invalidates the result.

This rule should be carried into the Stage-1/2 analysis code as an assertion, not merely noted in prose.

---

## 6. Canonical harness readiness

`experiments/_harness.py` already provides the load-bearing ordering needed for a clean trace:

1. `sense()` once;
2. record the prior transition;
3. advance the multi-rate clock / E1 tick / trajectory generation;
4. update `z_goal` where enabled;
5. update schema wanting where applicable;
6. sense hook;
7. select action;
8. action hook;
9. environment step;
10. residue/post-action update;
11. post-step hook;
12. rotate prior-state plumbing.

It passes `harm_obs`, `harm_obs_a` and `harm_history` into `sense()`, avoiding the silent-null problem of convenience `act()` paths.

This makes the canonical harness preferable to writing a bespoke cognitive-contract run loop.

---

## 7. Q-081 profile: useful instrumentation, but do not silently make it the cognitive-contract substrate

`experiments/_lib/q081_profile.py` can activate streams that are dark under stock defaults, including harm streams, salience coordinator, event segmentation/invalidation, TPJ comparator, sleep loop and `z_goal`.

This is highly useful for an **augmented observational arm**, but the file correctly declares such runs as **non-default substrate**.

The cognitive-contract experiment therefore needs two concepts kept separate:

### Canonical trace

Record whatever streams genuinely exist in the chosen canonical experimental configuration. Do not enable a mechanism merely because a desired probe needs a label.

### Augmented trace

Where a scientifically justified non-default mechanism is already an accepted experimental substrate, it may be enabled in a separately declared arm to make additional candidate relations observable.

No result from the augmented arm may be presented as evidence that the default organism already encoded a relation.

This distinction is especially important for `z_goal`, harm streams, source-monitoring events and sleep-phase markers.

---

## 8. Candidate-probe feasibility in V3

The Stage-0 question is not whether every Tier-1 candidate can be tested immediately. It is whether a non-contaminating first assay exists.

### Green — clean first-wave candidates

#### Predictive relational topology / transition structure

**Best primary target.** The gridworld gives externally derivable adjacency, action-conditioned transitions, short-horizon reachability and empirical successor-like structure. E2 already models action-conditioned state transitions and action objects. No cognitive-contract label needs to enter training.

#### Temporal order / persistence

Timestep, episode structure and trajectory order are native to the experiment. Tests can ask whether temporal/transition order remains recoverable under narrowing and surface remapping.

#### Causal/control relation

Actual action, predicted next states, counterfactual E2 world projections and observed world deltas provide a route to control/causal probes. Care is needed not to define the probe circularly from the exact representation being tested.

#### Branch / update / commitment status

E2 trajectories already carry a `hypothesis_tag`, and E3 exposes candidate/committed distinctions and confidence/precision. This is one of the cleanest places to test whether represented content can retain “what status does this representation have?” independently of its content.

#### Epistemic confidence / precision

E3 dynamic precision and commitment-state quantities provide observable metacognitive/control targets. The experiment should ask whether a narrower shared representation makes them recoverable, not train the bottleneck to predict a hand-labelled `CONFIDENCE` token.

### Amber — feasible, but needs a careful generator

#### Token continuity / identity

A simple gridworld has persistent locations/resources/hazards, but entity identity may be partly confounded with position. A clean token-continuity assay should use an environment manipulation in which identity and instantaneous location/features can be dissociated. Do not count “same cell coordinate” as evidence for a general identity relation.

#### Equivalence / similarity

Needs a controlled same/different or structural-analogy task with novel fillers. The base foraging task does not automatically provide a strong abstract-equivalence label.

#### Provenance / source / ownership

There are promising internal tags (`hypothesis_tag`, event provenance, self/world separation), but a clean factorial source assay needs a declared generator distinguishing externally constrained, self-generated/counterfactual and retrieved/replayed content without simply reading back the tag that was used to create the representation.

### Red/second-wave

#### General non-obtaining / negation

The ordinary environment supplies omissions and prediction errors, but a controlled expected-X/omitted-X assay should be added before interpreting this as a general non-obtaining representation.

#### Viability versus signed value

Testable, but requires a designed resource/harm rescaling or changed homeostatic mapping. It should not be squeezed into the first topology experiment.

#### Human-like kind/part, exact modality, grammatical categories

Not needed for V3 and deliberately outside the first-wave contract test.

---

## 9. Recommended first dataset

The cheapest scientifically useful next artefact is **not an architecture modification**. It is a dedicated trace dataset made with existing components.

### Dataset A — canonical V3 contract-observability trace

Use the canonical harness and `StreamTraceRecorder` on a frozen V3 configuration.

Record at minimum:

- full `z_self`, `z_world`, `z_beta`, `z_theta`, `z_delta` vectors;
- E1 hidden state if recorder default remains enabled;
- clock/freshness/valid flags;
- actions;
- reward/harm/benefit/resource and terminal information already available as ordinary experimental outcomes;
- positions/world state needed to derive transition topology;
- E3 candidate/commit/precision information when present on the selected canonical configuration;
- environment seed, agent seed, episode and timestep;
- exact repo commit and full config.

No new cognitive-contract training target is added.

### Dataset B — optional augmented observability trace

A separately declared run may use the Q-081 profile or an existing accepted enriched profile to expose additional harm/goal/source/sleep streams. It must never be merged invisibly with A.

### Why record rather than immediately retrain

One high-quality trace can support:

- current-latent geometry audit;
- held-out probe construction;
- nuisance-label discovery;
- frozen-source A–E bottleneck training;
- width sweeps;
- multiple probe families;
- positive-control validation;

without rerunning the organism for every analysis decision.

---

## 10. Stage-1 retrospective geometry audit can begin as soon as Dataset A exists

Pre-registered analyses:

- effective rank / participation ratio by latent;
- eigenspectrum and variance concentration;
- relational-topology decodability;
- temporal-order decodability;
- content versus meta-relational decodability;
- cross-episode / cross-environment probe transfer;
- nuisance-content decodability;
- source/status/commitment probes where the trace contains valid generators;
- linear primary probe, capacity-matched nonlinear diagnostic secondary probe;
- fresh-sample-aware analysis only.

This stage does **not** test the narrowing hypothesis by itself. It establishes what information exists in the source representation and which probes are non-degenerate before width is manipulated.

---

## 11. Stage-2 implementation footprint

If Dataset A validates the probes, the direct narrowing test can be implemented entirely as an **offline auxiliary model** consuming frozen latent vectors.

Minimal components:

```text
Frozen source vector
      |
      v
Encoder / bottleneck(width)
      |
      +--> consumer head 1: persistent/next-state prediction
      +--> consumer head 2: action-conditioned transition prediction
      +--> consumer head 3: sequence/trajectory objective
      +--> consumer head 4: evaluation/commitment-relevant target where available
      +--> reconstruction into >=2 target spaces
```

The candidate contract probes remain outside the optimiser.

The imposed relational-bottleneck positive-control arm is implemented in this auxiliary harness, not by modifying `LatentStack`.

### Strong recommendation

Do **not** initially alter `beta_dim`, `theta_dim` or `delta_dim` in the live organism to create the narrowing hierarchy. That would entangle the hypothesis with numerous existing architectural roles and make a negative result uninterpretable.

---

## 12. Existing shared-latent gradient probe should be reused

`ree_core/utils/shared_latent_probe.py` already implements a probe for whether multiple module losses genuinely couple to a shared latent and whether their gradients conflict.

This is directly relevant to the E-arm. Before calling a bottleneck “multi-consumer”, require:

- nonzero gradient from each declared consumer;
- report pairwise gradient cosine / conflict;
- distinguish beneficial shared pressure from a representation one task effectively owns while the others barely touch it.

A multi-consumer claim without this readiness check would be weaker than what V3 already knows how to measure.

---

## 13. G0 checklist

| Requirement | Verdict | Reason |
|---|---|---|
| Frozen V3 commit | **PASS** | `8e57e473496b2adda2f969a9c43058931745ab22` |
| >=3 heterogeneous consumer families | **PASS** | E1 prediction, E2 action/transition, E3 evaluation/commit; hippocampal family additionally available |
| Full-vector latent taps | **PASS** | `StreamTraceRecorder` stores vectors, not norms |
| Per-stream stale/fresh accounting | **PASS** | explicit freshness/validity flags and derivation types |
| Canonical run-loop support | **PASS** | `_harness.py` drives sense/action/update ordering and harm kwargs |
| Generic multidimensional trace storage | **PASS** | trace-store path already used by stream recorder |
| Current live stack is the narrowing experiment | **FAIL — expected** | default widths 32+32 -> 64 -> 32 -> 32; hypothesis must be tested separately |
| Every Tier-1 probe label already cleanly available | **NO — expected** | topology/time/control/status are strongest first-wave; identity/equivalence/provenance need dedicated generators |
| Existing historical recordings guaranteed sufficient | **UNPROVEN** | recorder exists now, but do not assume a suitable completed trace without inspecting an actual artefact |
| Architecture modification required for first direct test | **NO** | frozen-source auxiliary Stage 2 is sufficient |

**Overall G0 decision: CONDITIONAL PASS.** Proceed to a dedicated trace + Stage-1 probe-validity run; do not move the bottleneck into the organism yet.

---

## 14. The scientifically safest next move

Before Thought 2, one more concrete step is now justified:

> **Specify the Dataset-A trace and Stage-1 analysis manifest precisely enough that it can be handed to the experiment machinery without another conceptual design pass.**

That document should freeze:

- canonical V3 config/profile;
- seeds/episodes/steps;
- exact recorded streams/extras;
- primary topology labels;
- first-wave held-out probe generators;
- freshness filters;
- train/validation/held-out environment split;
- surface/schema remap used for generalisation;
- pass/fail criteria for whether Stage 2 is informative.

Once that is frozen, the programme will have moved from an interesting theory to a genuinely executable, non-contaminating experiment without having altered REE's architecture to fit the theory.
