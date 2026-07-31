# Thought intake: rational metareasoning and allocation of cognitive operations

**Date:** 2026-07-31  
**Status:** thought intake / architecture-pressure note; not yet a registered claim cluster  
**Proposed location:** `evidence/planning/thought_intake_2026-07-31_rational_metareasoning_cognitive_operations.md`  
**Primary trigger:** audit of the full V3–V6 programme after the competence-floor and conversion-ceiling campaigns  
**Related work:** control plane, dACC/aMCC adaptive control, operating modes, precision routing, frontopolar branching, goal deliberation V4, inference and belief-state V4, hippocampal planning V4, self-model V4, stuck-state detection, model disagreement, candidate diversity, architecture scaling needs, cognitive-architecture graveyard

---

## 1. Immediate trigger

REE already contains many mechanisms that regulate cognition:

```text
conflict monitoring
salience arbitration
operating-mode selection
precision modulation
candidate generation
candidate-diversity diagnostics
planning-depth controls
policy decomposition
stuck-state detection
model disagreement
commitment readiness
urgency interrupt
offline replay allocation
```

The forward architecture also plans richer cognitive operations:

```text
maintain multiple belief hypotheses
hold alternative goals
extend hippocampal rollouts
retrieve autobiographical episodes
simulate another agent
perform abstract relational inference
decompose or resume policies
switch representational level
```

The architecture therefore contains, or plans to contain, a growing repertoire of internal operations.

What is less clearly represented is a first-class answer to:

> Which internal operation should REE perform next, how much resource should it spend, and when should it stop thinking and act?

At present, much of this allocation appears distributed across local thresholds, operating modes, configured budgets, experiment-specific arms and mechanism-specific gates.

The missing possibility is not another cognitive faculty. It is an explicit, learned and inspectable policy over the use of faculties already present.

---

## 2. Core insight

An intelligent agent selects both external actions and internal cognitive operations.

Candidate internal operations include:

```text
generate another trajectory
extend a rollout horizon
retrieve another episode
construct another state hypothesis
inspect a causal alternative
reconsider a goal
decompose a policy
simulate another agent
seek another observation
ask for information
run offline integration
commit now
```

Each operation may improve a decision, but each also carries costs:

```text
time
compute or effort
opportunity loss
interference
delay under urgency
model-exploitation risk
false confidence from imagined evidence
```

The proposed architectural function is:

> **Rational metareasoning is the selection, budgeting and termination of internal cognitive operations according to their expected marginal contribution to decision quality.**

This should not be understood as a homunculus above the existing control plane. It may instead be a structured policy expressed through existing REE machinery: belief-state uncertainty, competence estimates, control costs, goal relevance, urgency, expected information gain, hippocampal proposal value, and E3 commitment consequences.

---

## 3. Relationship to existing REE architecture

### 3.1 Metareasoning versus the control plane

The control plane determines the regime under which shared machinery operates. Metareasoning asks which particular computation is worth performing, what it is expected to reveal, whether it would change the pending decision, how much should be spent on it, and when its marginal value has fallen below its cost.

The control plane may be the actuator through which a metareasoning policy changes cognition. The proposal may therefore belong as an extension of the control-plane and goal-deliberation roadmaps rather than as an independent module.

### 3.2 Metareasoning versus competence modelling

A competence model estimates:

```text
How reliable is this process in this domain?
```

Metareasoning uses that estimate to decide:

```text
Is it worth invoking the process now?
Should another process be used?
Should REE gather external evidence instead?
```

The V4 self-model may eventually represent process-specific competence. This intake concerns the use of that competence information, not a duplicate confidence model.

### 3.3 Metareasoning versus inference

Inference constructs and updates hypotheses about hidden state. Metareasoning decides whether another hypothesis is worth generating, whether existing hypotheses require discrimination, whether observation is more valuable than simulation, and whether uncertainty is decision-relevant.

Not every uncertainty warrants more inference.

### 3.4 Metareasoning versus curiosity

Curiosity concerns novelty, rarity, learning progress or epistemic value. Metareasoning is broader. The appropriate cognitive action may be to explore, retrieve, simulate, simplify, ask, act immediately, or stop searching.

A rational metareasoning policy must sometimes suppress curiosity when delay or model unreliability dominates.

### 3.5 Metareasoning versus goal deliberation

Goal deliberation selects and structures what matters. Metareasoning selects how cognition should be used in service of those goals.

```text
goal deliberation:
    what objective or commitment should govern behaviour?

metareasoning:
    what cognitive operation is worth performing before deciding?
```

---

## 4. Why this may matter for REE’s current bottleneck

The conversion-ceiling work suggests that additional mechanisms and additional candidate generation do not automatically yield competence.

Possible failure modes include:

```text
planning too shallowly
planning too deeply with an inaccurate model
generating many redundant candidates
retrieving irrelevant episodes
continuing deliberation after the decision is stable
failing to observe when simulation is unreliable
allocating replay to familiar or harm-dominated traces
using a cognitive process outside its demonstrated domain
relying on researcher-configured regimes rather than autonomous allocation
```

The relevant bottleneck may therefore be partly allocational:

> REE may possess useful cognitive machinery without yet having learned when each operation is worth invoking.

This becomes more important as the architecture advances from V4 individual cognition to V5 social modelling and V6 language. Without cognitive-resource allocation, richer faculties may increase computational and interaction cost faster than competence.

---

## 5. Proposed representational surface

A minimal inspectable representation could be:

```text
CognitiveOperation:
    operation_type
    target
    expected_decision_change
    expected_uncertainty_reduction
    expected_information_gain
    estimated_process_reliability
    goal_relevance
    welfare_relevance
    time_cost
    effort_or_compute_cost
    opportunity_cost
    urgency_cost
    model_exploitation_risk
    stopping_condition
    provenance
```

Possible operations:

```text
ROLLOUT
EXTEND_ROLLOUT
RETRIEVE_EPISODE
GENERATE_HYPOTHESIS
DISCRIMINATE_HYPOTHESES
DECOMPOSE_POLICY
RECONSIDER_GOAL
SIMULATE_OTHER
SEEK_OBSERVATION
REQUEST_INFORMATION
OFFLINE_INTEGRATE
COMMIT_NOW
```

This need not be a new globally central object. Equivalent typed bids could be produced by existing systems and arbitrated through the control plane or E3, provided the terms remain inspectable.

---

## 6. Candidate decision principle

A minimal policy would estimate:

```text
expected cognitive value
    =
expected improvement in downstream decision quality
    - time cost
    - effort or compute cost
    - opportunity cost
    - delay cost
    - risk introduced by the operation
```

The important commitment is not one exact scalar equation. The important commitment is that REE can distinguish why an internal operation is or is not selected.

For example:

```text
rejected because unlikely to change decision
rejected because generating model is unreliable
rejected because urgency makes delay unsafe
selected because it discriminates load-bearing hypotheses
selected because an observation is cheaper than another rollout
```

A single opaque “thinking value” would not provide sufficient scientific leverage.

---

## 7. Architectural options

### Option A: cognitive operations as E3 candidates

Internal operations and external actions enter a shared selection surface.

Advantages:

```text
minimal new arbitration machinery
ordinary commitment and urgency rules apply
```

Risks:

```text
internal and external actions may require different temporal semantics
recursive proposal generation
```

### Option B: distributed operation bids into the control plane

Hippocampus, inference, self-model and goal-deliberation systems emit bids for additional processing.

Advantages:

```text
fits existing regime-control architecture
preserves distributed ownership
```

Risks:

```text
global value may remain implicit
local bids may be incomparable or self-serving
```

### Option C: bounded meta-controller

A small learned policy chooses among a restricted set of cognitive operations.

Advantages:

```text
easy to test
clear matched-compute comparisons
```

Risks:

```text
hand-waved configurator
new central bottleneck
duplication of E3 or frontopolar control
```

The first experiment should discriminate among these rather than assuming Option C.

---

## 8. Strong competing explanations

Before registering a new claim, test whether the proposed function is already adequately represented by:

1. the existing operating-mode and precision control plane;
2. V4 frontopolar and goal-deliberation machinery;
3. belief-state uncertainty combined with E3 commitment readiness;
4. hippocampal candidate-allocation policies;
5. simple learned local budget controllers;
6. competence-aware information-seeking without a general operation ontology.

A new architectural claim is warranted only if the existing machinery cannot learn transferable, inspectable and matched-compute cognitive allocation.

---

## 9. Proposed minimal experiment

Use tasks in which the value of additional cognition varies independently of immediate reward.

Conditions:

```text
A. additional rollout strongly improves choice
B. additional rollout does not change the best choice
C. deeper rollout becomes misleading because the model is biased
D. observation is more useful than simulation
E. urgency makes delay costly
F. episode retrieval is useful but rollout is not
```

Compare:

```text
fixed computation budget
uncertainty-triggered budget
difficulty-triggered budget
distributed control-plane allocation
learned cognitive-operation policy
```

Measurements:

```text
operation selected
marginal decision improvement
compute spent
time spent
stopping point
information-seeking frequency
model-exploitation failures
decision quality under matched compute
transfer to unseen task variants
```

The decisive result is not “more thinking improves reward.” It is:

> REE selectively spends cognition where its expected marginal value is positive and stops when further cognition is unhelpful, unsafe or misleading.

---

## 10. Failure and falsification conditions

The broad proposal is weakened if:

```text
fixed budgets perform equally well
existing operating modes learn the same allocation
the policy merely tracks generic difficulty
estimated operation value fails to predict actual decision improvement
the agent manufactures uncertainty to obtain more compute
the mechanism adds complexity without matched-compute transfer
```

The general cognitive-operation ontology should be rejected if one or two local learned budget controllers achieve equal performance and inspectability.

---

## 11. Safety and architecture risks

### Recursive deliberation

The system must not create unlimited “thinking about thinking.” Metareasoning depth should be bounded, and the selection policy should not recursively propose unrestricted copies of itself.

### Self-justifying cognition

An operation must not earn value merely by generating more internal activity. Value estimates should be calibrated against subsequent real-world decision improvement.

### Urgency neglect

Uncertainty must not automatically trigger more cognition. Delay and opportunity costs must be represented.

### Imagined-evidence inflation

Internally generated evidence must retain model provenance and reliability. Simulation should not acquire the epistemic authority of observation.

### Central-controller accretion

The proposal should strengthen existing shared machinery where possible rather than introduce a new hand-waved configurator.

---

## 12. Proposed routing

1. Audit control-plane, goal-deliberation, self-model and hippocampal-planning roadmaps for existing ownership.
2. Run a targeted literature pull on value of computation, expected value of control, bounded metareasoning and adaptive stopping.
3. Define a minimal operation set:
   - `EXTEND_ROLLOUT`
   - `RETRIEVE_EPISODE`
   - `SEEK_OBSERVATION`
   - `COMMIT_NOW`
4. Compare E3-candidate, distributed-bid and bounded-controller implementations.
5. Register a claim only if a distinct transferable function remains after that comparison.

**Provisional generation:** likely V4, but generation and ownership should remain unset until the duplication audit determines whether this belongs to the control plane, goal deliberation or a cross-plan integration layer.

---

## 13. Working conclusion

REE contains many cognitive operations and many signals about uncertainty, conflict and competence.

The unresolved question is whether those signals are integrated into an autonomous policy over the use of cognition.

The architectural pressure can be stated simply:

> A mind must choose not only what to do, but what to think about, how deeply to think, and when thinking should stop.
