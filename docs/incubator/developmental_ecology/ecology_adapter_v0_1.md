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

---

## 16. V3 channel exposure audit, 2026-09-14

**Scope.** Read-only code audit answering item 6 of the programme seed's immediate research programme: *"Determine whether V3 currently exposes the necessary intrinsic consequence and causal-attribution channels without adding programme-specific machinery to REE."* No `ree-v3` code was changed, no claim was registered, no experiment was queued. Sources read: `ree-v3/ree_core/environment/causal_grid_world.py` (5428 lines), `ree-v3/experiments/_lib/capability_contract.py`, `ree-v3/experiments/_lib/capability_eval.py`, `ree-v3/experiments/_lib/stream_recorder.py`, `ree-v3/experiments/_lib/trace_store.py`, `ree-v3/experiments/_lib/manifest_core.py`, `REE_assembly/evidence/planning/experimental_recording_standard_2026-07-12.md`, plus targeted searches across `ree_core/predictors/`, `ree_core/hippocampal/`, `ree_core/sleep/`, `ree_core/affect/`, `ree_core/comparator/`, `ree_core/attribution/`, `ree_core/pfc/`, `ree_core/goal.py` and `ree_core/agent.py`. All line numbers are approximate anchors as of the audit date, not stable API.

Legend for the **status** column: **exposed** = a live in-memory value with a named accessor exists and is exactly this channel; **derivable-from-recorded** = the value is not itself stored, but a driver-side `get_state()`/`get_metrics()`/`extras=` call already exists that would capture it into a manifest/trace with no core-code change; **absent** = neither the value nor an accessor exists. For every absent row, **gap type** distinguishes a **recording gap** (the value exists transiently at run time but nothing persists it) from a **substrate gap** (the computation itself does not exist), and **programme-specific?** states whether filling the gap would mean adding Developmental-Ecology-specific machinery to core REE (forbidden by the incubator boundary and by assay_001 section 23) versus ordinary adapter/harness/driver work (the intended, cheaper fix).

### 16.1 Compatibility-profile table (section 12), validated against source

| Adapter concept | ree-v3 source | What it emits | Status | Gap type | Programme-specific? |
|---|---|---|---|---|---|
| Self/body observation (`body_state`) | `ree_core/environment/causal_grid_world.py:3705` `_get_observation_dict()`; channel map `:3714-3760` | `[10]`/`[12]`/`[17]` float tensor: position, health, energy, footprint density, last-action, episode progress, harm/benefit EMA, optional limb damage | exposed | -- | -- |
| World observation (`world_state`) | same, `:3705`; layout `[200]`/`[250]`+ | 5x5x7 local one-hot view + contamination + hazard/resource proximity fields (+ optional landmark/scent/waypoint blocks) | exposed | -- | -- |
| Fast harm-relevant observation | `obs_dict["harm_obs"]`, built `causal_grid_world.py:3983-3987` | `[51]` float = hazard field view + resource field view + harm_exposure; SD-010 sensory-discriminative (Aδ-analog), forward-predictable | exposed | -- | -- |
| Slow affective harm state | `obs_dict["harm_obs_a"]`, built `:3992-4014` | `[7]` (limb damage mode) or `[50]` legacy EMA (alpha=0.05, persists across episodes); SD-011 affective-motivational (C-fibre analog), not forward-predicted | exposed | -- | -- |
| Benefit/homeostasis | `_consume_resource_at()` `:2187`; `info["total_benefit"]`, `info["energy"]` `:3299-3303` | per-step resource-contact benefit and energy-integrated consequence | exposed | -- | -- |
| Actions | `ACTIONS` dict `:113-115`; `action_dim` property `:1529` | `{0:up,1:down,2:left,3:right,4:stay}` (+ optional `5:consume` when `consummatory_act_enabled`, deliberately excluded from the world-rule-shift permutation) | exposed | -- | -- |
| Ground-truth event cause | `info["transition_type"]`, assigned throughout `step()`, surfaced `:3277` | per-step string class label from a fixed vocabulary incl. `env_caused_hazard` / `agent_caused_hazard`; optional `env_caused_multisource` widening exists **specifically for an agency-detection comparator** (`tag_env_caused_multisource_ttype`, default off) | exposed (auditor-only overlay must be applied by the adapter -- V3 does not itself withhold it from the agent) | -- | -- |
| Task/evaluator score | `experiments/_lib/capability_eval.py` -- `foraging_competence`, `survival_horizon`, `goal_reach_rate`, `planning_depth`, read from `info["transition_type"]=="resource"` and position traces, with oracle/random policy anchors | derivable-from-recorded (a wrapper computation over already-emitted `info`, not a stored field) | derivable | -- | -- |
| Checkpoint | not directly audited (out of the five files read; organism/world state save-load exists elsewhere in `ree_core`/experiment runner but was not traced to a symbol in this pass) | -- | **unaudited** | -- | flag for a follow-up pass, not this chip |

### 16.2 Internal REE readouts (assay_001 section 13), mapped to source

| Readout | ree-v3 source | Status | Gap type | Programme-specific? |
|---|---|---|---|---|
| E1/E2 action-conditioned prediction of event **continuation/termination** | E1 (`predictors/e1_deep.py:880` `predict_long_horizon`) and E2 (`predictors/e2_fast.py:201`, `e2_world.py:235`, etc.) are action-conditioned **next-latent-state** models only; no `done`/`gamma`/continuation head exists anywhere in `predictors/` | **absent** | substrate gap | yes -- a continuation/termination head is new mechanism, not a wrapper; do not add it to core REE for this assay |
| Self-vs-world agency attribution around control attempts | `TPJComparator.compare()` `comparator/tpj_comparator.py:91` -> `(agency_signal in (0,1), is_self_caused: bool)`; also `E2WorldForward.comparator_residual()` `predictors/e2_world.py:279` (per-dim vector) and the trained 3-way `event_logits` classifier `latent/stack.py:1005`/`agent.py:11122` | exposed (TPJ signal) / derivable-from-recorded (`StreamTraceRecorder` already reads `agent._tpj_last_agency_signal` as stream `e2_self_pe`, `stream_recorder.py:337-345`, gated on `use_tpj_comparator`) | -- | -- |
| Prediction error when control succeeds/fails | `E3TrajectorySelector.post_action_update()` `predictors/e3_selector.py:4389` returns `{prediction_error, running_variance, dynamic_precision, residue_updated}`; `get_commitment_state()` `:4691` is what `StreamTraceRecorder` records as stream `e3_commitment` | exposed | -- | -- |
| Counterfactual candidate **differences** | `pfc/frontopolar_analog.py:287 compute_counterfactual_value()` is an explicit **STUB**; the only counterfactual generator anywhere is a single deterministic alternative action, `agent.py:~4355 a_cf = one_hot((a_idx+1) % n_act)`; `attribution/scientist_attribution_buffer.py:141` carries a `counterfactual_contrast` scalar against that one alternative | **absent** (no candidate set/bank, one alternative only) | substrate gap (a real counterfactual-candidate bank does not exist) | yes for a general bank; the existing single-alternative contrast (`mech276_counterfactual_backed_fraction`, `get_metrics()` `:290`) is already derivable-from-recorded and may be sufficient for DEA-001's binary control-affordance case |
| E3 proposal and selection frequencies around the control affordance | Proposal: `predictors/e2_fast.py:767 generate_candidates_random`, `hippocampal/module.py:1944 propose_trajectories`. Selection: `SelectionResult` `e3_selector.py:114`, per-tick `last_scores`/`last_precommit_probs`/`last_score_decomp`. **No cumulative selection-frequency histogram exists** -- `E3ScoreDiversity.get_state()` `e3_score_diversity.py:363` counts mechanism firings, not per-candidate picks | per-tick score: exposed; **cumulative frequency: absent** | recording gap (per-tick data exists; a driver-side histogram over `last_selected_idx`/action class is ordinary aggregation, not new mechanism) | no -- this is aggregation a driver can do without touching core |
| Commitment formation, persistence, release | Formation: `SelectionResult.committed` `e3_selector.py:130`, `commit_readiness.get_state()` `policy/commit_readiness.py:366`. Persistence: `BetaGate.get_state()` `heartbeat/beta_gate.py:306` (incl. `committed_run_length`). Release: `commit_maintenance_release.get_state()` `policy/commit_maintenance_release.py:385`, `natural_commit_urgency.get_state()` `policy/natural_commit_urgency.py:360`, de-commit lever `pfc/frontopolar_analog.py:453` | exposed (each stage has its own `get_state()`/`get_commitment_state()`, all documented as manifest-ready) | -- | -- |
| Harm sensory vs affective stream trajectories | `harm_obs` / `harm_obs_a` (16.1 above); `z_harm_s` vs `z_harm_a` latents; `HarmSuffering Accumulator.get_state()` `affect/harm_suffering_accumulator.py:297` | exposed | -- | -- |
| Residue/history state | `ResidueField.get_statistics()` `residue/field.py:1147`, `get_coverage_telemetry()` `:1159`; `agent.update_residue()` `agent.py:10657` is the main per-step metrics dict | exposed | -- | -- |
| Hippocampal retrieval associated with earlier control episodes | `AnchorSet.query_by_goal_match()` `hippocampal/anchor_set.py:529`; `GhostGoalBank.rank()`/`get_diagnostics()` `hippocampal/ghost_goal_bank.py:184/334`; `EventSegmenter.step()` -> `BoundaryEvent` `hippocampal/event_segmenter.py:519`, incl. `posterior` strength | derivable-from-recorded (`StreamTraceRecorder`'s `hippocampal_proposals`/`boundary_events` streams already capture the shape of this; **no readout exists that is indexed by "earlier control episode" specifically** -- that indexing is a DEA-specific query the driver must build over the existing anchor/segment IDs) | recording gap for the DEA-specific index; the underlying retrieval machinery itself is exposed | the query-by-control-episode indexing is adapter/driver work, not new REE mechanism |
| Sleep/replay frequency and content for control-related episodes | `SleepReplaySampler.get_metrics()` `sleep/replay_sampler.py:212`; `agent.run_sws_schema_pass()`/`run_rem_attribution_pass()` `agent.py:12357/12606` both return flat metrics dicts | derivable-from-recorded (frequency and generic content are exposed; filtering "control-related" specifically is a driver-side query over anchor/segment metadata, same caveat as the row above) | recording gap for the DEA-specific filter | driver work, not new REE mechanism |
| Confidence/precision/controllability-related variables | Confidence/precision: `e3_selector.py:815/825/830/840`, `e2_world_uncertainty.py:488/512/533` -- exposed. **Controllability: no agent-side estimator of controllability from experience exists** (`escapability` is a scalar the agent is *told*, not learned; see 16.3) | confidence/precision: exposed; controllability-as-learned-estimate: **absent** | substrate gap for a learned controllability estimator | yes for a general learned estimator; the DEA-001 design does not require one (H1 asks about a *behavioural* phenotype, not whether REE internally estimates controllability) |

### 16.3 DEA-001-specific channels not covered above

| Channel | ree-v3 source | Status | Gap type | Programme-specific? |
|---|---|---|---|---|
| True controllability (`true_controllability` in the adapter's `AuditTransition`) | No symbol named `controllability` exists in `ree_core/`. Nearest constructs: `escapability` (a scalar **input** to `HarmSufferingAccumulator.update()`, `affect/harm_suffering_accumulator.py:195`, sourced via `agent._resolve_harm_suffering_escapability()` `agent.py:4039` in one of three modes -- `constant` default 1.0, `avoidance_efficacy`, or `external` via `agent.py:3985 set_harm_suffering_escapability()`) and the learned neighbour `InstrumentalAvoidanceGate.effective_efficacy()` `pfc/infralimbic_avoidance_gate.py:183` | **absent as a ground-truth auditor label**; the `external` escapability seam exists to be *driven by* an adapter's true controllability, not to compute it | recording gap once an adapter supplies the value (the seam exists); substrate gap for V3 to derive controllability from its own manipulation | no -- DEA-001's job is exactly to supply this from the adapter/harness side through the existing `external` seam; that is the intended division of labour, not new REE machinery |
| Yoking (`yoke_id`, yoke event record) | No `yoke`/`yoking`/`yoked` symbol anywhere in `ree_core/` (only experiment *filenames* use the word) | **absent** | substrate gap relative to core REE, but **this is expected** -- assay_001 section 23 states the implementation boundary explicitly: yoking is adapter/harness ecology machinery, not a V3 mechanism | no -- yoking belongs in the adapter/harness layer by design; it should never be added to `ree_core/` |
| Event id | Not found as a distinct field in `causal_grid_world.py`'s `info` dict (`transition_type` is a class label, not an instance id) | **absent** | recording gap -- a driver can mint a per-event id from `(episode_index, global_step, transition_type)` without touching core | no |
| Evaluator/task score (auditor-only) | `experiments/_lib/capability_eval.py` metrics (16.1) | derivable-from-recorded | -- | -- |
| Action-outcome contingency / learned-helplessness constructs | Explicit absences confirmed by search: no `self_efficacy`, no `action_outcome_contingency`, no `learned_helpless*` symbol anywhere in `ree_core/` | **absent** | substrate gap | yes if added to core; DEA-001 does not need REE to have this construct internally -- it is exactly what the assay's *behavioural* endpoint (AdultHarm_AUC) is designed to reveal externally |

### 16.4 The main recording risk, stated for the record

Almost every "exposed" or "derivable" channel above exists only as transient in-memory state or a `get_state()`/`get_metrics()` dict that **a driver must explicitly call and persist**; `manifest_core.stamp_recording_core()` captures provenance only, never scientific channels automatically. `StreamTraceRecorder` (`experiments/_lib/stream_recorder.py`) is the only per-timestep multi-stream writer in the corpus and is used by roughly a dozen drivers out of the full experiment set; its trace blobs are stored machine-local content-addressed and are not readable from a different machine (`trace_store.py:152-157`). Per `experimental_recording_standard_2026-07-12.md`, the flat-scalar-readout and criteria-re-derivability checks are warn-only even in strict mode, and as of 2026-09-09 roughly two-thirds of that month's run-packs score with no numeric `metrics.values` at all. **Conclusion: DEA-001 should treat every channel in 16.1-16.3 as needing an explicit driver-side recording obligation, not assume the existing corpus or its defaults already carry them.**

### 16.5 Answer to the research-programme question

V3 already exposes, without any new programme-specific core-REE machinery: the full observation split (body/world, sensory/affective harm), the ground-truth agent-caused-vs-environment-caused causal label (`transition_type`, including a comparator-oriented variant built for exactly this kind of use), two independent self-vs-world agency signals, commitment formation/persistence/release at every stage, confidence/precision, residue, and prediction-error-on-control-failure -- all reachable through existing driver-side `get_state()`/`get_metrics()`/`StreamTraceRecorder` calls. It does **not** expose, and would need either adapter/harness-layer work (in scope, not a REE change) or genuine new REE mechanism (out of scope for this assay) for: yoking (adapter-layer by design, per assay_001 section 23), a ground-truth controllability/true-controllability label (the `external` escapability seam exists for the adapter to supply this), event ids (trivial driver-side derivation), a real counterfactual-candidate bank (substrate gap; the existing single-alternative contrast may suffice for DEA-001's binary affordance case), and an event-continuation/termination prediction head (substrate gap, not required by DEA-001's design, which measures a downstream behavioural harm burden rather than reading the prediction directly). No item found here requires revising the adapter contract or the V3 substrate before Assay 001 can proceed; the open items are driver-side recording obligations plus the harness-layer yoking machinery assay_001 already scopes as its own work.