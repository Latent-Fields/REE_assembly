# Developmental Ecology Adapter v0.1

**Status:** incubator specification / design target  
**Version:** 0.1  
**Date:** 2026-09-02  
**Scope:** architecture-neutral contract with an initial REE-V3 compatibility profile  
**Not:** an REE architecture claim, task-reward wrapper, deployment API, or V3 closure requirement

## 1. Purpose

A Developmental Ecology Assay needs a stable boundary between an external world and a developing organism.

The adapter exists so that a world can be changed without silently changing what the organism is allowed to know, and so that different worlds can be compared through a common experimental instrument.

The central rule is:

> **The adapter translates observations, affordances and organism-relevant consequences. It does not tell the organism what the investigator wants it to achieve.**

This is important because the programme is interested in the goals and strategies that develop from bounded intrinsic sensitivities inside a world, not merely in optimising a designer-supplied score.

The contract should eventually support REE and non-REE probe organisms. REE V3 is the first compatibility target because it already separates self/world observation, harm-related streams, action-conditioned prediction and ground-truth causal labels in its current grid-world substrate.

---

## 2. Two-plane architecture

Every compliant adapter has two strictly separated information planes.

### 2.1 Agent-facing plane

The organism may receive only information that is part of its experimental sensorium or internal consequence state.

Examples:

- exteroceptive observations;
- proprioceptive/interoceptive state;
- public cues;
- available actions or affordances;
- intrinsic harm/integrity consequences;
- intrinsic benefit/homeostatic consequences;
- action failure when failure itself would be perceptible;
- ordinary temporal information when the ecology makes it perceptible.

### 2.2 Assay/auditor plane

The experimental harness may additionally record privileged information that must **never** be supplied to the organism unless a protocol explicitly declares it an observable channel.

Examples:

- hidden simulator state;
- true causal source of an event;
- true controllability of an event;
- task or business score;
- event identifiers;
- yoke-pair identifiers;
- intervention arm;
- counterfactual simulator state;
- RNG state;
- world-generation parameters not perceptible in-world;
- acceptance-test diagnostics;
- ground-truth labels used only for analysis.

### 2.3 Hard leakage rule

An adapter is invalid for confirmatory assay use if an agent-facing tensor, metadata object, timing artefact or reset pattern allows reliable direct inference of the hidden experimental arm when that information is not itself intended to be a learnable property of the world.

The assay should distinguish **learning the ecology** from **reading the experiment label**.

---

## 3. Value is not task score

The adapter must keep three concepts separate.

### Observable consequence

What happened in the world or body that the organism can perceive.

Example: energy decreased; an aversive pulse ceased; a container moved; a route became blocked.

### Intrinsic consequence

A bounded organism-relevant change that enters its harm, benefit, viability or other declared intrinsic channels.

Example: integrity loss, homeostatic resource gain, nociceptive exposure.

### Evaluator score

A number useful to the investigator, product owner or simulator designer.

Example: parcel delivered = +10; level completed = 1; throughput = 37 units/hour.

The evaluator score is **auditor-only by default**.

A domain designer may not declare `+10 for completing my desired task` to be intrinsic benefit merely to make the organism pursue that task. If a task outcome genuinely changes an intrinsic variable, the mapping must be explicit, justified and versioned.

This is the programme's practical implementation of the distinction:

> **intrinsic value channels constrain development; goals and strategies are allowed to emerge as contingent solutions.**

---

## 4. Minimal logical contract

A conceptual adapter presents the following operations. These names are illustrative rather than a required programming-language API.

```text
load(manifest) -> Adapter
reset(seed, organism_id, phase_id) -> AgentObservation
step(action) -> (AgentTransition, AuditTransition)
checkpoint() -> CheckpointRef
restore(checkpoint_ref) -> AgentObservation
close() -> RunSummary
```

### AgentObservation

Must contain only declared agent-facing channels.

```text
AgentObservation:
  sensory
  body_state
  intrinsic_state
  public_context?        # only if genuinely observable
  action_mask?           # only if affordance availability is observable
```

### AgentTransition

```text
AgentTransition:
  observation_next
  intrinsic_consequences
  done
  perceptible_event_flags?
```

There is deliberately no mandatory `reward` field.

Architectures that require a scalar training signal may obtain one through an **organism profile** that deterministically derives it from the same intrinsic channels available to the developmental protocol. Such a scalarisation must be recorded and must not contain evaluator-only information.

### AuditTransition

```text
AuditTransition:
  step_id
  phase_id
  world_state_ground_truth
  action_received
  event_id
  event_source
  true_controllability
  yoke_id?
  intrinsic_vector_ground_truth
  evaluator_metrics
  rng_state_ref
  adapter_diagnostics
```

The auditor plane may be richer than this. It may never be poorer than required to prove that the experimental manipulation and yoking actually occurred as specified.

---

## 5. Ecology manifest

Every assay world should be serialisable to a manifest resembling:

```yaml
ecology_id: dea-toy-controllability-001
adapter_version: 0.1
world_version: <immutable version/hash>
organism_profile: ree-v3-ecology-profile-0.1

observation_channels:
  - name: body_state
    plane: agent
    semantics: proprioceptive_interoceptive
  - name: world_state
    plane: agent
    semantics: exteroceptive

intrinsic_channels:
  - name: harm
    range: [0, 1]
    direction: adverse
  - name: benefit
    range: [0, 1]
    direction: beneficial

action_space:
  type: discrete
  actions: [up, down, left, right, stay]

phase_schedule:
  - calibration_or_childhood
  - transition
  - adulthood

episode_policy: <declared>
reset_policy: <declared>
offline_policy: <declared>
checkpoint_policy: <declared>

audit_channels:
  - true_event_source
  - true_controllability
  - event_id
  - yoke_id
  - evaluator_metrics

yoking: null   # or declared yoke protocol
```

The exact schema can become machine-readable later. Version 0.1 establishes the conceptual separation first.

---

## 6. Channel classes

The adapter should classify each agent-facing input according to the role it plays rather than merely its tensor shape.

### Exteroception

Information about the environment that an organism could in principle sense.

Examples: local geometry, nearby objects, gradients, public signals, visible state changes.

### Proprioception / interoception

Information about the organism's own state.

Examples: position relative to self-centred coordinates, health/integrity, energy, limb state, current action state.

### Intrinsic harm / benefit

Signals arising because an event changes organism-relevant state.

The mapping should specify latency, persistence, saturation and whether the signal is immediate or integrated over time.

### Affordance information

The organism may learn what actions exist from action experience. An explicit action mask should be supplied only when availability would itself be perceptible. Hidden feasibility belongs on the auditor plane.

### Public temporal/context signals

Clock time, phase, season or episode progress should be visible only when the ecology provides a sensory correlate or when the scientific protocol explicitly studies an organism endowed with that signal.

### Privileged labels

Never agent-facing by default: hazard class, causal source, controllability arm, optimal action, intended task, future event, counterfactual outcome, experiment group.

---

## 7. Temporal and developmental contract

A developmental assay is invalid if reset semantics silently erase or preserve the very history the assay claims to study.

Each manifest must therefore state separately what happens to:

1. **world state**;
2. **acute body state**;
3. **fast recurrent/working state**;
4. **learned model parameters**;
5. **hippocampal/episodic memory**;
6. **residue or other persistent value/history stores**;
7. **commitments and active goals**;
8. **offline/sleep state and replay buffers**;
9. **RNG state**.

The words `reset`, `new episode`, `new phase`, `adult transition` and `new lifetime` must not be treated as synonyms.

A phase transition may deliberately normalise acute physiology while preserving developmental learning. That operation must be named explicitly, hashed where possible, and acceptance-tested.

---

## 8. Checkpoint and cloning requirements

Reference-organism experiments depend on exact developmental branching.

A checkpoint used for branching should identify, at minimum:

- organism implementation/version;
- learned parameters;
- persistent internal stores;
- relevant recurrent state according to checkpoint type;
- world/adapter version;
- developmental age;
- RNG state or seed lineage;
- checksum/hash.

Two clone arms are considered matched only if all non-manipulated checkpoint state is identical at branch time.

For population assays, independent seed lineages should remain distinct and be reported rather than collapsed into one pooled pseudo-sample.

---

## 9. Yoking support

Some developmental manipulations require two organisms to receive identical outcome burdens while differing in causal contingency.

The adapter therefore needs a first-class yoking concept.

A yoke event record should contain:

```text
yoke_id
source_organism_id
target_organism_id
onset_step_or_relative_time
planned_max_duration
realised_duration
intensity_profile
termination_cause_source
termination_time_source
termination_time_target
integrated_intrinsic_harm_source
integrated_intrinsic_harm_target
```

For a strict controllability yoke, the source organism may terminate an event through its own behaviour. The paired target receives an event with the same realised onset, intensity and duration, but its own control action has no causal effect.

The acceptance criterion is outcome equivalence within a predeclared tolerance—not merely similar average exposure across a cohort.

---

## 10. Reproducibility requirements

Every assay run should record:

- adapter version;
- ecology/world hash;
- organism implementation revision;
- organism profile;
- all mapping/calibration constants;
- seed lineage;
- checkpoint hash;
- phase schedule;
- yoke assignment and event log;
- normalisation operations;
- software/runtime versions needed for deterministic replay where feasible;
- protocol deviations.

If exact deterministic replay is not technically possible, the manifest must say so and define the reproducibility level that is promised.

---

## 11. Adapter compliance tests

Before an ecology can support confirmatory interpretation, it should pass a small compliance suite.

### DEA-ADAPT-001 — privileged-channel leakage

Train or script a simple diagnostic classifier against agent-facing observations at phase entry. Experimental arm must not be directly recoverable above the predeclared tolerance unless arm identity is intentionally encoded in the observable ecology.

### DEA-ADAPT-002 — action-map integrity

Each declared action produces the documented actuator request. No hidden remapping varies by group unless that remapping is the experimental manipulation and is itself documented.

### DEA-ADAPT-003 — intrinsic-channel provenance

Every intrinsic signal must be derivable from declared organism/world state transitions. Evaluator score must not contribute unless explicitly permitted by the organism profile.

### DEA-ADAPT-004 — deterministic replay / reproducibility level

Restore the same checkpoint and world seed and verify the promised replay properties.

### DEA-ADAPT-005 — reset/phase-transition semantics

Verify which state fields are reset, preserved and transformed.

### DEA-ADAPT-006 — strict-yoke equality

For yoked protocols, integrated exposure and event timing must satisfy the declared matching tolerance for every pair used in confirmatory analysis.

### DEA-ADAPT-007 — metadata isolation

`group`, `yoke_id`, optimal-policy information, hidden causal source and evaluator metrics must be inaccessible through the agent API and logs consumed by the organism.

### DEA-ADAPT-008 — bounded intrinsic scales

Intrinsic channels remain finite, calibrated and non-saturating across the intended assay range.

Failure of a compliance test invalidates confirmatory interpretation until repaired and rerun.

---

## 12. REE V3 compatibility profile 0.1

This profile maps the abstract contract onto the current V3 substrate without redefining V3.

Current `CausalGridWorld` already exposes a useful split:

- `body_state` → self/proprioceptive-interoceptive input;
- `world_state` → exteroceptive input;
- optional proxy-field mode adds harm/benefit exposure to body state and hazard/resource field views to world state;
- `harm_obs` provides a sensory-discriminative harm-related stream;
- `harm_obs_a` provides a slower affective-motivational harm-related stream;
- ground-truth transition types already distinguish agent-caused and environment-caused hazards for experimental analysis;
- canonical actions are up/down/left/right/stay, with a separately gated consume action in some configurations.

The adapter must **not** expose the ground-truth transition label as an oracle to the organism merely because the environment code computes it.

### Proposed initial mapping

| Adapter concept | V3 profile 0.1 |
|---|---|
| Self/body observation | `body_state` |
| World observation | `world_state` |
| Fast harm-relevant observation | declared subset/path through `harm_obs` |
| Slow affective harm state | declared subset/path through `harm_obs_a` |
| Benefit/homeostasis | existing resource/energy consequences where protocol-compatible |
| Actions | movement 0–4 initially |
| Ground-truth event cause | auditor-only transition/event metadata |
| Task score | auditor-only; not mapped to V3 intrinsic benefit |
| Checkpoint | wrapper around existing organism/world state, with explicit preserved/reset fields |

### Compatibility warning

`CausalGridWorld` contains numerous experiment-specific flags and historical compatibility behaviours. Adapter v0.1 should therefore use an explicitly pinned profile rather than assume that “default grid world” has timeless semantics.

The first assay should add as little machinery as possible and should prefer a wrapper-level ecology manipulation over changing core V3 architecture.

---

## 13. Phenotype recording contract

An adapter run is not complete merely because the agent terminates.

It should emit a standard longitudinal record from which an **ecological phenotype report** can be derived.

Minimum behavioural record:

- action trajectory;
- visited states/regions;
- intrinsic harm/benefit time series;
- event encounters;
- effective versus ineffective control attempts where ground truth is available;
- phase boundaries;
- episode boundaries;
- terminal cause.

For instrumented organisms such as REE, an optional internal record may include prediction, attribution, candidate/selection, commitment, replay, residue and other declared states. Those readouts must be observational unless a separate intervention is performed.

---

## 14. What v0.1 deliberately does not solve

This specification does not yet define:

- a universal ontology of intrinsic value;
- a universal scalar reward for cross-architecture comparison;
- real-world sensor or actuator interfaces;
- social/multi-agent semantics;
- language interfaces;
- welfare thresholds for later, more ambiguous organisms;
- commercial licensing;
- a complete machine-readable schema;
- certification that an adapter is scientifically valid across domains.

Those should be earned after a toy assay demonstrates that the abstraction is useful.

---

## 15. v0.1 acceptance gate

Adapter v0.1 has succeeded if it is sufficient to implement Assay 001 while satisfying all of the following:

1. controllability can differ without changing matched intrinsic harm burden;
2. hidden arm identity and causal ground truth remain auditor-only;
3. childhood and adulthood can be separated with explicit state-preservation semantics;
4. a naïve checkpoint can be cloned reproducibly into matched developmental arms;
5. both REE V3 and at least one conventional recurrent reinforcement-learning comparator can consume equivalent agent-facing information;
6. the resulting run can produce a phenotype report without relying on investigator narratives.

If those conditions cannot be met cleanly, the adapter should be revised before a larger programme is built.