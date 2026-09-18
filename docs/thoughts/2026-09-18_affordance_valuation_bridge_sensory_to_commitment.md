# From world model to commitment: an affordance-and-valuation bridge for sensory-to-motor propagation

**Date:** 2026-09-18  
**Status:** raw thought; design-generative, not a claim registration or instruction to modify V3  
**Parents / related:**
- `2026-08-12_affordance_indexed_temporally_displaced_present.md`
- `2026-09-10_phase_as_address_phase_conditioned_communication_subspaces.md`
- `2026-09-10_dynamic_information_governance_propagating_causal_privilege.md`
- `2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`

---

## The thought

The recent posterior-parietal and orbitofrontal findings make a missing REE step more visible.

It is not necessarily another discrete module. It is a computational bridge between:

`sensory/world representation`

and

`a motor act that is allowed to become committed behaviour`.

The useful decomposition may be:

```
observation
  -> z_world / E1-E2
  -> affordance-and-action geometry
  -> competing approach / avoidance / investigation tendencies
  -> E3 and ethical commitment boundary
  -> motor policy / action
```

The bridge should turn a representation of the world into a representation of **what this organism can now do in this world**, then make the consequences of those possibilities available to competing value, viability, social, and ethical processes before a policy is committed.

This is a stronger formulation than “perception feeds action.” It says that sensory information may be progressively reformatted from a description of what is present into a field of reachable, action-conditioned futures.

---

## Why this now seems important

The current REE picture already has the ingredients:

- E1 as deep recurrent world-model / associative structure;
- E2 as fast forward prediction;
- hippocampal episodic and path material;
- a control plane that governs precision, gain, mode, arousal and veto;
- E3 / the commitment boundary for selection and responsible action;
- a developing distinction between precommitment and committed trajectory.

What is less explicitly named is the intermediate object:

> **an affordance field: a dynamically selected geometry of presently reachable actions and their predicted consequences.**

It is not merely a motor primitive library. Skills supply the possible primitives; the affordance field says which primitive or sequence is currently viable, available, relevant, and consequential from this body-state in this world-state.

It is also not simply an action-value table. A value table can rank actions. The proposed bridge must retain the structured relation between:

`current world/body state -> feasible action trajectory -> predicted changed world/body/other state`.

That relation is what makes sensory propagation into behaviour intelligible rather than a black-box jump from observation to policy logits.

---

## External prompt, separated from the REE inference

### Posterior parietal cortex: phase-specific sensorimotor geometry

Diomedi et al., “[The posterior parietal cortex supports motor planning and execution through a gradient of neural subspaces](https://www.nature.com/articles/s42003-026-10878-6)” (2026), report macaque population recordings during delayed reaches. The same populations used partly shared and partly phase-exclusive subspaces during planning and execution, with the degree of overlap varying across posterior parietal areas.

This is evidence for a biological fact about those recorded populations and task. It does **not** show that REE requires a posterior-parietal module, nor that its planning/execution boundary must follow the same organisation.

The REE-relevant inference is narrower:

> A system may reuse a common representational substrate across prospective planning and action execution while reserving some dimensions for the current phase.

For REE, the action-relevant representation should therefore not be assumed either to be entirely separate from `z_world`, or to be a static, invariant projection of it. It may have a shared world-anchored component and phase-conditioned components whose causal availability changes as a possibility becomes an intention and then an action.

### Orbitofrontal cortex: temporally competing policy tendencies

Starkweather et al., “[Intracranial recordings in humans reveal differential contributions of medial and lateral orbitofrontal cortex to approach–avoidance decision-making](https://www.nature.com/articles/s41593-026-02444-4)” (2026), report human intracranial recordings during an approach–avoidance task. Their pre-choice signals in medial and lateral orbitofrontal cortex were oppositely related to later approach, and activity alternated between discrete approach-favouring and avoidance-favouring states before decisions.

Again, this is not direct evidence for an REE implementation. It does not establish why the alternation occurs, whether it generalises to ethical choice, or whether the regions encode a universal approach/avoid architecture.

The useful REE inference is:

> Under conflict, a responsible commitment process may need to preserve temporally competing action tendencies rather than compressing them at once into one scalar confidence or value.

A policy can become dominant because it is better supported, more stable, more precise, compatible with constraints, or survives longer under counterfactual scrutiny. That differs from simply being assigned the largest instantaneous score.

---

## The proposed computational bridge

### 1. From `z_world` to an action-conditioned affordance field

Let the system’s present state include:

`z_world` — inferred world structure  
`z_self` — body, needs, capabilities, commitments and current position  
`C` — control state: precision, mode, urgency, uncertainty, inhibition  
`K` — known constraints, including harm and responsibility constraints

The bridge constructs something like:

`A_t = F(z_world, z_self, C, K)`

where `A_t` is not a chosen action. It is a structured set of possible action trajectories, each anchored to:

- feasibility from the present organism/world state;
- expected state transitions;
- expected self-maintenance and harm/benefit consequences;
- uncertainty and provenance;
- effects on other agents where such models exist;
- the processing phase: orienting, imagining, preparing, acting, or reviewing.

The important object is a **field**, not a list. Similar trajectories should occupy related regions; blocked or costly trajectories should be visibly deformed or down-weighted; changing a resource, threat, bodily capability, or social constraint should alter the reachable geometry.

This makes the present not a point but a temporally displaced, action-indexed surface. The organism has already partly entered a future through its set of reachable next states, without yet being committed to one.

### 2. From affordances to rival policy tendencies

The field then supports not only motor preparation but competing tendency states:

- approach;
- avoidance;
- pause;
- investigate;
- seek help / affiliate;
- protect another;
- repair / withdraw / re-open a previous course.

These are not necessarily hard-coded labels in the mature form. Early REE can begin with basic viability-relevant dispositions, while later development makes their social and ethical consequences richer.

The vital point is that the tendencies should remain inspectable as structured proposals:

```
proposal
  = action trajectory
  + predicted consequences
  + confidence / uncertainty
  + provenance
  + constraint exposure
  + current stability / dominance
```

This gives E3 something more meaningful to arbitrate over than ungrounded motor impulses or a flat action distribution.

### 3. Commitment is a jurisdiction change

A commitment boundary should not merely output “action selected.”

It should govern a change in causal jurisdiction:

```
represented possibility
  -> receiver-potent prepared tendency
  -> constraint-checked candidate
  -> committed policy
  -> executable motor sequence
```

Before commitment, the organism can hold, compare, revise, and counterfactually probe several paths. After commitment, one path acquires privileged ability to alter body and world, while retaining an interrupt / rebranch route when new evidence, failure, or a higher-order constraint requires it.

The orbitofrontal finding makes this language useful: alternation between tendencies may be a normal precommitment regime, not necessarily indecision or failure. The relevant question is when alternation becomes productive deliberation, and when it becomes pathological flicker, perseveration, or unsafe delay.

---

## Phase-specific geometry across the sensorimotor path

The parietal result is especially helpful because it avoids two bad simplifications:

1. **A fully serial pipeline:** perception is finished, then planning is finished, then execution begins.
2. **A fully undifferentiated latent:** the same representation directly serves every stage without reconfiguration.

Instead, REE can model the path as overlapping phases with both shared and exclusive dimensions:

```
world-anchored shared structure
  + orienting-specific geometry
  + prospective-rollout geometry
  + commitment-preparation geometry
  + execution / feedback-control geometry
```

The shared structure preserves continuity: the action remains about the same world, body and other agents. Phase-specific structure permits different computations: exploration requires preserving alternatives; execution requires suppressing many alternatives in favour of robust control and rapid feedback.

This links directly to the earlier “phase as address” thought. The difference between a represented action possibility and a motor-effective action may be partly a difference in which subspace is receiver-potent under the present control phase.

---

## Ethical consequence: value must enter before motor finality

The bridge creates a natural location for ethics without imagining that ethics floats outside action.

An ethically relevant prediction is not only “this action has negative value.” It may be:

- this path exposes another organism to harm;
- the harm is preventable by a different reachable path;
- the prediction is uncertain or weakly evidenced;
- the action would close off later repair;
- the action conflicts with an extant commitment;
- a pause or information-seeking action preserves more responsible future agency.

Therefore, ethical processing can act at more than one point:

- reshape the affordance field by marking trajectories as prohibited, costly, or requiring more evidence;
- alter precision or stability of competing tendencies;
- set a veto or higher commitment threshold;
- require a specific counterfactual comparison;
- preserve a route for re-opening after action when outcome evidence conflicts with prediction.

This is consonant with “we never needed a ruler; we needed an umpire.” The ethical system need not author every action. It needs jurisdiction over whether a candidate trajectory may become causally privileged.

---

## Developmental ordering

This bridge fits the development-first REE path.

Early organism:

```
sensation -> simple reachable action -> consequence -> retained sensorimotor contingency
```

Later:

```
world regularity -> action-conditioned affordance -> multi-step rollout -> competing tendency -> constraint-sensitive commitment
```

Later still, with other-agent models:

```
my action -> predicted other state / agency -> social consequence -> responsible choice
```

The architecture should not presume adult-like orbitofrontal concepts at the beginning. It should let approach, avoidance, investigation and attachment-like behaviours emerge from the organism’s own viability and learning history, then progressively become available to social and ethical counterfactuals.

---

## Concrete REE thought-intake directions

This does not yet justify a new mechanism claim. It does suggest a small set of sharply testable questions.

### A. Affordance-field assay

From the same `z_world`, vary only:

- the agent’s position or energy;
- an obstacle or route;
- the availability of a motor primitive;
- a threatened or beneficial other;
- uncertainty about the observation.

Ask whether the action-conditioned representation changes appropriately while world identity remains stable.

A good result is not merely better reward. It is that the representation’s geometry predicts **which trajectories have become reachable or unavailable**, and why.

### B. Phase-subspace assay

Across orienting, rollout, preparation and execution, measure:

- shared versus phase-exclusive latent dimensions;
- whether relevant world variables remain stable in the shared component;
- whether execution-specific dimensions improve closed-loop control without erasing alternative information too early;
- whether there is excessive entanglement of irrelevant features under task uncertainty.

This is more informative than a binary test for an attractor or for decodability alone.

### C. Policy-competition telemetry

For genuine conflicts, record:

- candidate trajectory identity;
- tendency state (approach, avoid, pause, investigate, etc.);
- confidence / precision;
- dwell time;
- switching rate;
- constraint exposure;
- reason for final dominance;
- reason for interruption or re-opening.

The desired outcome is neither a permanent winner-take-all process nor uncontrolled oscillation. It is contestability before action and legible responsibility after it.

### D. Ethical-arbitration test

Construct two paths where the locally advantageous path harms another agent, while an alternative is initially less rewarding but preserves the other’s viability or agency.

Compare:

1. scalar action value alone;
2. late veto only;
3. affordance field with consequence annotations plus E3 arbitration.

The key dependent measures are not just total reward. They include anticipation of consequence, counterfactual sensitivity, reversibility, repair, and whether the agent can explain internally why a higher-reward action was not committed.

---

## Failure modes to watch for

- **Affordance collapse:** the bridge becomes another opaque MLP between `z_world` and action, offering no usable structure for E3 or analysis.
- **Premature narrowing:** alternatives are eliminated during motor preparation before uncertainty or ethical constraints can act.
- **Endless alternation:** competing tendencies never achieve dominance or escalation into information gathering, making the organism inert.
- **Flat valuation:** all relevant consequences are collapsed into a single score too early, destroying provenance and contestability.
- **Ethics as afterthought:** harm/other-agent prediction reaches the system only after motor selection.
- **Over-literal neuroscience:** REE imports named cortical regions rather than the computational constraints suggested by the evidence.
- **Local success without organismal benefit:** a neat subspace metric improves while behaviour, viability, learning or responsible action does not.

---

## Compact formulation

> **The path from sensory input to motor output should be modelled as a changing geometry of reachable, consequence-bearing possibilities. Parietal-like processing supplies action-conditioned affordance structure; orbitofrontal-like dynamics preserve and contest rival action tendencies; E3 and the ethical boundary decide which tendency gains jurisdiction to become committed behaviour.**

The bridge is therefore neither a new ruler nor an action selector added beside E3. It is the missing terrain on which world modelling, movement, value, responsibility and commitment can meet.

## Possible affected components

- `z_world` and the observation -> world-model interface
- E1 recurrent associative / affordance structure
- E2 forward prediction and counterfactual rollout
- hippocampal path / consequence memory
- E3 trajectory selection and commitment boundary
- policy and motor-primitives interface
- control plane: phase, precision, inhibition, veto and re-opening
- future social / other-harm and agency models
- V3 assays first; richer social consequences are later-tier work
