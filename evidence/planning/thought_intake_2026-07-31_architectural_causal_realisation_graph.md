# Thought intake: architectural causal realisation, reachability, and executable claim-to-mechanism mapping

**Date:** 2026-07-31  
**Status:** thought intake / scientific-instrumentation and architecture-governance note; not yet a registered claim cluster  
**Proposed location:** `evidence/planning/thought_intake_2026-07-31_architectural_causal_realisation_graph.md`  
**Primary trigger:** V3-EXQ-830 autopsy and SD-084, where a named and instrumented mid-execution mechanism was found to be structurally unreachable  
**Related work:** claim registry, substrate decisions, experiment manifests, causal attribution, mechanism instrumentation, failure autopsies, supersession, contract tests, static lints, architecture specification, formal ancestor mapping, claim-document drift, development map, cross-plan roadmaps

---

## 1. Immediate trigger

REE has unusually strong scientific governance.

For a mechanism, the programme may record:

```text
claim text
implementation location
dependencies
experiment
criteria
result
interpretation
autopsy
supersession
confidence
provenance
```

However, V3-EXQ-830 revealed a gap between those layers.

The architecture contained:

```text
a named mechanism
an apparent implementation hook
experiment drivers
diagnostic counters
success criteria
governance interpretation
```

Yet the mid-execution hook had never been reachable because committed state was cleared before the later tick at which the hook needed to observe it.

The behavioural result therefore did not test a weak mechanism. It failed to instantiate the mechanism.

This suggests a missing scientific representation:

> an executable, intervention-aware mapping from a high-level architectural claim to the lower-level computational state transitions that are supposed to realise it.

---

## 2. Core insight

Component inspectability is not sufficient.

A reader may inspect every local function and still not know whether:

```text
the mechanism can activate
the intervention reaches it
the required state persists long enough
the measured mediator belongs to it
the behavioural effect flows through it
a sibling pathway produces the same effect
the high-level abstraction remains valid across implementation changes
```

The proposed function is:

> **Architectural causal realisation is an explicit mapping from a REE claim to its activation preconditions, implementation variables, temporal dependencies, intervention sites, mediators, expected invariances, downstream effects and invalidating observations.**

This is not a new cognitive faculty inside REE. It is a model of REE as a scientific object.

---

## 3. Relationship to existing governance

### 3.1 Realisation mapping versus claim dependencies

A dependency graph may state:

```text
MECH-B depends on SD-A
```

A realisation mapping states:

```text
which state in SD-A must exist
which operation creates it
when it must persist
which consumer reads it
which mediator should change
which downstream behaviour should follow
```

Dependency is necessary but not sufficient for realisation.

### 3.2 Realisation mapping versus contract tests

Contract tests establish local properties. They may show that a method returns the correct output, a flag is inert when disabled, or a state field can be written.

They do not necessarily show that the real agent loop reaches the method, preserves the state until consumption, activates the intended mediator, or produces the predicted causal effect.

### 3.3 Realisation mapping versus experiment manifests

A manifest records what ran, under which conditions, what was measured and how it was interpreted.

The realisation mapping records the causal structure that makes those measurements relevant. It can therefore be used before a run to ask whether the experiment is capable of testing the claim.

### 3.4 Realisation mapping versus architecture documentation

Documentation describes intended structure.

The proposed representation should be structured enough to support:

```text
reachability checks
temporal persistence checks
runtime activation checks
mediator checks
invariance tests
claim-to-code drift checks
alternative-path warnings
```

### 3.5 Realisation mapping versus cross-plan synthesis

The same principle applies beyond V3 mechanisms.

For example, the V4–V5 path:

```text
persistent object
    -> self-bound body
    -> stateful self
    -> represented other
    -> other-indexed ethical objective
```

may be documented across several plans.

A realisation graph could make the load-bearing interfaces explicit without requiring a new architectural organ.

---

## 4. Proposed object

A minimal representation could be:

```text
MechanismRealisation:
    claim_id
    claim_version
    high_level_function
    high_level_variables
    implementation_variables
    activation_preconditions
    temporal_preconditions
    producers
    consumers
    causal_edges
    intervention_sites
    mediators
    expected_downstream_effects
    expected_invariances
    alternative_pathways
    diagnostic_observables
    invalidating_observations
    implementation_refs
    experiment_refs
    provenance
```

Each entry should answer:

```text
What must be true for the mechanism to activate?
Which state variables realise it?
Who produces them?
Who consumes them?
When must they persist?
What intervention changes the mechanism?
What mediator should change first?
What behaviour should change later?
What should remain invariant?
What observation would show that the mechanism was not actually tested?
```

---

## 5. Example: mid-execution decomposition

A simplified entry could be:

```text
claim_id: MECH-321.R4

high_level_function:
    reconsider or decompose a committed programme during execution

activation_preconditions:
    committed programme exists
    programme was committed on a previous tick
    programme has remaining actions
    decomposition gate is open

temporal_preconditions:
    committed-program representation survives action execution
    next selection tick can access it

producer:
    E3 commitment entry

persistent_state:
    persistent_committed_program_handle

consumer:
    mid-execution decomposition gate

mediator:
    midexec_decomposition_candidates_evaluated

predicted_effect:
    improved recovery when a committed subgoal becomes invalid

invariances:
    uncomplicated intact trajectories are not decomposed unnecessarily
    precommit candidate generation remains unchanged

invalidating_observations:
    mediator count remains zero
    persistent state is destroyed before consumption
    behaviour changes without mediator activation
    intervention affects precommit only
```

The purpose is not to replace tests. It is to generate and organise the tests that establish actual realisation.

---

## 6. Example: intervention geometry and authority invariance

MECH-313 illustrates a second class of failure.

Suppose an intervention uniformly rescales candidate scores, while downstream commitment uses a hard argmin.

A realisation record should state:

```text
intervention:
    positive monotonic score scaling

downstream operator:
    hard argmin

expected invariance:
    selected committed action remains unchanged

valid effect surface:
    exploratory sampling or confidence may change

invalid dependent variable:
    committed-action identity under uniform scaling
```

This is not a reachability problem. It is a mismatch between intervention geometry, measurement geometry and decision authority.

A useful realisation framework must represent both structural and mathematical non-identifiability.

---

## 7. Cross-plan example: object, self and other

The revised body/self/other intake provides a useful higher-level example.

A cross-plan realisation map could specify:

```text
ARC-080 persistent object
    -> object token with parts and persistence

self_model_v4
    -> self-binding relations over one object token

mirror_modelling_v5
    -> other-self hypothesis over another object token

ethics_as_coherence_v5
    -> agent-indexed harm and goal terrain attached to that other token
```

Required invariants might include:

```text
self and other use homologous representational structure
self and other retain separate provenance
other-state inference does not overwrite self-state
ethical weighting refers to a stable represented agent
```

This would turn a distributed roadmap narrative into an inspectable integration contract.

---

## 8. Proposed representation levels

### Level 1: claim layer

```text
architectural commitment
mechanism hypothesis
invariant
substrate decision
```

### Level 2: computational abstraction layer

```text
state variables
objects
relations
operations
temporal phases
gates
memory structures
selection rules
```

### Level 3: implementation layer

```text
classes
methods
fields
config flags
runtime events
diagnostic counters
```

### Level 4: experimental layer

```text
intervention arms
mediators
dependent variables
criteria
non-degeneracy checks
failure signatures
```

### Level 5: cross-plan integration layer

```text
producer roadmap node
consumer roadmap node
shared object or interface
readiness gate
epistemic boundary
safety invariant
```

The purpose is not to collapse these levels. It is to make the relations between them explicit.

---

## 9. Proposed validation operations

### 9.1 Static reachability

Check whether producer–consumer paths can exist under the selected configuration.

Potential findings:

```text
dead consumers
impossible gate conjunctions
missing state writes
state destroyed before use
flags that cannot co-occur
consumer lacks a producer
```

### 9.2 Temporal validity

Check whether the state exists at the correct grain and duration.

Potential findings:

```text
per-tick state used as persistent state
episode state cleared at action boundary
late consumer reading an early transient
```

### 9.3 Dynamic activation

During smoke or calibration, verify:

```text
preconditions occurred
producer fired
state persisted
consumer read it
mediator changed
```

### 9.4 Intervention mediation

Test the intended sequence:

```text
intervention
    -> mediator
    -> downstream effect
```

rather than merely:

```text
intervention
    -> behavioural difference
```

### 9.5 Invariance tests

Specify what should not change. These are necessary to distinguish a specific mechanism from a global perturbation, sibling pathway or generic performance shift.

### 9.6 Alternative-path checks

Record known pathways that could mimic the predicted outcome. An experiment should sever them, measure them, or state that causal attribution remains ambiguous.

### 9.7 Cross-plan interface checks

Verify that a downstream plan consumes an actually existing upstream object or state.

Examples:

```text
other-indexed ethics requires an other-agent token
selfhood requires an object-bound referent
body-relative affordance requires an owned-body relation
repair requires an owned outcome and represented repair target
```

### 9.8 Drift checks

When implementation or roadmap interfaces change, flag affected realisation entries for review.

This should complement existing claim-document drift rather than duplicate it.

---

## 10. Strong competing explanations

Before building a new registry, test whether the need can be met by extending:

1. contract tests;
2. experiment preflight;
3. runtime causal tracing;
4. architecture documentation;
5. static lints;
6. formal ancestor mapping;
7. cross-plan dependency maps;
8. claim-document drift tooling.

A general realisation graph is justified only if it catches scientifically important failures that narrower instruments cannot catch economically.

The likely minimum may be:

```text
compact declarative realisation records
    +
generated preflight and trace checks
```

rather than a large manually curated knowledge graph.

---

## 11. Risks

### Governance mass

REE already carries substantial governance machinery. The realisation system must earn its cost by catching defects and reducing interpretation errors.

### False formality

A machine-readable causal graph can still encode a false theory. Entries remain hypotheses and require intervention.

### Hand-authored maintenance burden

If every code change requires extensive manual graph editing, the programme may reproduce the knowledge-engineering bottleneck described in the cognitive-architecture graveyard.

Implementation references and observed runtime edges should be generated automatically where possible.

### Canonising one implementation

A high-level mechanism may have multiple valid computational realisations.

The representation must support:

```text
alternative realisations
superseded realisations
equivalent implementations
partially realised claims
```

### Causal overclaiming

A mediator that changes after intervention does not establish unique causal responsibility. Alternative pathways and identification assumptions must remain explicit.

---

## 12. Proposed minimal pilot

Pilot only a small set of known cases:

```text
MECH-321 / SD-084
MECH-313 / V3-EXQ-687a
V3-EXQ-830 adjudication-path defect
object -> self -> other -> ethics cross-plan chain
```

For each:

1. reconstruct the intended causal pathway;
2. encode activation and temporal preconditions;
3. identify producer and consumer;
4. identify the mediator;
5. specify expected invariances;
6. specify alternative pathways;
7. run static and dynamic validation;
8. ask whether the representation would have predicted a known failure or integration gap.

Success criterion:

> The pilot catches or clearly anticipates multiple known scientific failure modes without relying on mechanism-specific code that simply restates the autopsy.

Failure criterion:

> The representation adds substantial manual work but discovers nothing beyond ordinary contracts, preflight, tracing or roadmap dependency checks.

---

## 13. Possible declarative form

```yaml
claim_id: MECH-321
component: R4

realisation:
  high_level_function:
    mid_execution_policy_decomposition

  preconditions:
    - committed_program_exists
    - committed_program_has_remaining_steps
    - commitment_originated_on_prior_tick

  temporal_requirements:
    - committed_program_persists_until_next_e3_tick

  producer:
    - E3Selector.commit

  consumer:
    - REEAgent.midexec_decomposition_gate

  mediator:
    - decomp_n_evaluated_midexec

  invariances:
    - precommit_candidate_count_unchanged
    - intact_trajectory_completion_not_reduced

  invalid_if:
    - mediator_never_activates
    - persistent_state_cleared_before_consumer
```

Tooling could generate:

```text
documentation
preflight checks
runtime assertions
coverage summaries
cross-plan interface reports
drift warnings
```

The declarative source should remain compact. Generated artifacts can be verbose.

---

## 14. Programme-level implications

### Scientific validity

Experiments become less likely to interpret null effects from unreachable mechanisms.

### Falsifiability

The programme states what observation invalidates the claimed realisation.

### External legibility

A sceptical reader can inspect the intended causal pathway without reconstructing it from code and distributed roadmap documents.

### Supersession quality

The programme can distinguish:

```text
same mechanism, new implementation
repaired reachability
modified mechanism
new mechanism
abandoned realisation
```

### Cross-generation coherence

The V4–V6 architecture can be checked as an actual dependency chain rather than a collection of individually sensible plans.

### Laboratory maturity

REE gains an explicit representation of the relation between:

```text
the theory REE states
the computation REE implements
the experiment REE runs
the behaviour REE observes
```

---

## 15. Proposed routing

1. Audit existing contract, preflight, tracing, formal-ancestor and drift systems for overlap.
2. Write the four pilot records manually.
3. Test retrospective predictive value against known autopsies and roadmap integration questions.
4. Keep the pilot outside the claims registry until it demonstrates scientific utility.
5. Determine whether the durable owner should be architecture governance, experiment instrumentation, claim schema, or a separate compact realisation registry.
6. Automate extraction of code references and runtime evidence wherever possible.
7. Do not assign a cognitive-generation label. This is cross-generation scientific infrastructure.

---

## 16. Working conclusion

REE is highly inspectable at the level of components and unusually disciplined at the level of evidence.

The unresolved gap lies between those levels.

The pressure can be stated simply:

> A mechanism has not been tested merely because code bearing its name ran. The programme must show that the intended causal computation was reachable, activated, measured and responsible for the observed effect.
