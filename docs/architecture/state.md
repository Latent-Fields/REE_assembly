# State

**Document type:** Architecture reference (standalone — no single Claim ID; anchors candidate INV/ARC claims pending governance)
**Depends on:** [L-space](l_space.md), [E3 trajectory selection](e3.md), [hippocampal systems](hippocampal_systems.md), [residue geometry](residue_geometry.md)
**See also:** [trajectory selection](trajectory_selection.md), [e1.md](e1.md), [e2.md](e2.md)

---

## Core Definition

> **State = situation as navigable from here.**

A REE state is not a raw observation and not a total world model. It is the minimum coherence-bearing situation description required for trajectory evaluation: a compressed relational package linking inferred world structure, agent condition, temporal position, valence, constraint, and uncertainty to the set of plausible next transitions.

Longer form:

> A REE state is a compressed relational situation-model, integrating world configuration, self configuration, temporal position, goal/antigoal relation, constraints, uncertainty, and transition readiness, such that plausible transitions can be simulated and evaluated.

---

## Why State Is Not Raw Perception

A state is not determined by sensory appearance alone. Situations that are perceptually identical can constitute distinct states when they differ in temporal position, active commitment, goal/antigoal relation, social context, or operative constraints.

Example: these situations may look visually identical — standing at a door — but constitute distinct states:

| Appearance | Actual state (differs in T, G, A, C) |
|-----------|--------------------------------------|
| Standing at a door | Leaving for work — low urgency, routine transition |
| Standing at a door | Fleeing danger — extreme urgency, avoidance dominant |
| Standing at a door | Just remembered I forgot my keys — active goal blocked |
| Standing at a door | Trying not to wake someone — strong constraint, inhibition |
| Standing at a door | Fire alarm — novel threat, rule override |

The perceptual content is the same. The state differs because the viable transitions, costs, antigoals, urgency, and commitment structure differ. Trajectory evaluation produces entirely different outputs.

This is a design invariant: **a state definition that collapses to perceptual embedding silently breaks trajectory evaluation, viability mapping, and ethical reasoning.**

---

## Required Components

A REE state S has eight components:

**S = {W, Self, T, G, A, C, U, R}**

| Component | Label | Content |
|-----------|-------|---------|
| **W** | World configuration | Inferred objects, agents, relations, spatial structure, affordances, environmental conditions |
| **Self** | Agent configuration | Energy, arousal, pain/nociception, uncertainty, action readiness, memory quality, injury/threat status |
| **T** | Temporal position | Where in an episode: beginning, mid-task, post-commitment, post-error, mid-repair, after social rupture |
| **G** | Goal relation | How the current situation stands relative to desired regions — close, drifting, blocked |
| **A** | Antigoal relation | Proximity to avoided, prohibited, identity-violating, or socially costly regions |
| **C** | Constraints | Active constraints: physical impossibility, social norms, task rules, identity rules, commitments already made, time/energy limits |
| **U** | Uncertainty structure | Not just what is believed but how stable those beliefs are — prediction confidence, memory reliability, rule conflict |
| **R** | Transition readiness | Which next moves are currently primed, blocked, or uncommitted |

None of these components is optional. A state missing T cannot support episodic integration. A state missing A cannot generate antigoal gradients. A state missing U cannot propagate uncertainty into path evaluation.

---

## State vs. Representation

These are distinct:

| | Representation | State |
|-|----------------|-------|
| What it is | Encoded content | Encoded content *prepared for transition search* |
| Where it lives | Cortical manifold (E1/L-space) | Hippocampal index + relational binding across components |
| Minimal requirement | Decodable | Supports transition prediction, valence/antigoal tagging, uncertainty |
| Role | Carries information | Enables navigation |

The cortex (E1/L-space) holds broad representational content. The hippocampus indexes navigable states over parts of that manifold. A state is not created by encoding — it is created by binding encoded content into a unit that can participate in trajectory search.

A representation that cannot support transition prediction, valence tagging, or uncertainty representation is not yet a state in the REE sense.

---

## Multi-Scale Nesting

State is scale-relative. The same moment contains multiple simultaneous valid state descriptions at different control scales:

| Scale | Example |
|-------|---------|
| Motor | Hand near cup |
| Tactical | Making tea |
| Episodic | Getting ready for work |
| Social | Navigating a morning after a difficult evening |
| Identity | Maintaining functioning under stress |

These are not cleanly separable. They are nested, and the correct scale for trajectory evaluation depends on which transitions are causally load-bearing for the current task.

E3 evaluates paths across mixed scales. The temporal structure of L-space (z_gamma / z_beta / z_theta / z_delta) provides partial scaffolding for this nesting — faster timescales carry motor and tactical states; slower timescales carry episodic and identity-level state components.

A well-formed state at the episodic scale includes pointers into the motor and tactical scales, not explicit copies of their full content. State carries handles to retrievable detail, not complete detail.

---

## Ethical and Social Loading

Ethical salience is not external scoring applied to a neutral state. It is part of the state description itself.

A state can include:

- Who may be harmed (specific agents, uncertainty over identity)
- Whether harm is reversible
- Whether a commitment has already been made (binding vs. still revocable)
- Betrayal risk (promise or expectation already established)
- Dignity threat to self or other
- Truth distortion risk (deception implications of available transitions)
- Downstream residue likelihood (trajectories whose consequences persist)

These components feed directly into E3 path evaluation via antigoal relations (A) and constraint flags (C). They are not an ethics module bolted onto a neutral planner. The ethical texture is already in the state before E3 evaluates anything.

This is consistent with REE's core claim that ethics cannot be compiled away: an agent reasoning from states that exclude ethical components has already made a silent ethical decision about what to attend to.

---

## Failure Modes from Bad State Abstraction

When state abstraction is wrong, trajectory evaluation fails systematically. These failure modes have psychiatric analogues, which suggests the taxonomy can serve as a diagnostic frame for state-level implementation errors:

| Abstraction failure | Behavioral result | Psychiatric analogy | Evidence level |
|--------------------|-------------------|---------------------|----------------|
| Overmerge: distinct states collapsed to one | Context-inappropriate responses; source monitoring failure | Schizophrenia, thought disorder | **Strongly supported** — DG pattern separation failure + CA3 completion excess (PMID 35853896, 39567329, 20810471) |
| Valence spreading across state graph | Broad avoidance; threat assigned to non-threatening states | Generalized anxiety | **Strongly supported** — hippocampal pattern completion extends threat neighborhood (PMID 27794690; Lissek 2021) |
| Attractor basin with fast salience | Rapid re-entry to threat state despite safety context | PTSD intrusive reinstatement | **Strongly supported** — safety attractor inaccessible in PTSD (PMC 7554263, PMC 10728304) |
| Context loss: T and C components absent | Appearance-driven impulsive action; temporal discounting | ADHD, impulse control | **Well supported** — PFC-hippocampal-cerebellar temporal circuits (PMC 11325328, PMC 2894421) |
| Uncertainty collapse: U treated as zero | Overcommitment, reduced exploration, false confidence | Mania, grandiosity | **Theoretically grounded** — empirical evidence developing (PMID 32860285, 39828236) |
| Narrow capacity / negative G tagging | Approach failure, anhedonia, inflated path costs | Depression | **Multiply supported** — synapse loss sufficient (PMID 39569353); learning asymmetry (PMC 5828520) |
| Oversplit: each context treated as unique | Failure to transfer across structurally equivalent situations | ASD generalization failure | **Supported behaviorally** — generalization weakness (PMC 4573235); excess pattern separation (PMC 7907419) |
| Residue not propagated across transitions | Harm repeated without accumulation; no moral continuity | Psychopathy | Literature pull pending |
| Social/identity constraints omitted from C | Norm violation despite intact world model | Frontal damage | Literature pull pending |

This failure-mode taxonomy is registered as **MECH-126** (`state_abstraction.failure_modes_psychiatric_analogs`). The claim is structural analogy, not identity — REE state components are not identical to empirical constructs, and causal direction between abstraction failure and psychiatric syndrome is not resolved for most tracks. Cross-track convergence: the hippocampus appears centrally in all six grounded tracks; the DG/CA3 pattern separation/completion balance is the primary organizing parameter across schizophrenia, anxiety, PTSD, and ASD.

---

## Relationship to REE Components

| Component | Role relative to state |
|-----------|----------------------|
| **E1** | Fills the W and Self components with temporally coherent predictions; provides latent content for indexing |
| **E2** | Supplies transition kernels over action-consequence space; populates R (transition readiness) |
| **E3** | Evaluates candidate paths through state space; uses G, A, C, U to score trajectories |
| **Hippocampal systems** | Indexes states as navigable units; stores episodic traces (Gamma_i) as paths through state space; enables replay and counterfactual rollout |
| **Residue field phi(z)** | Provides persistent curvature over the space states occupy; ethical cost is encoded in the field, not in individual state objects |
| **Control plane** | Modulates precision on U (uncertainty weighting) and gate behavior for R (transition readiness under arousal/threat) |
| **Basal ganglia / commit gate** | Determines whether a state transition becomes an actual commitment, converting a rollout state into a lived transition |

States are the nodes. The residue field is the terrain the nodes sit in. Hippocampal traces are the paths. E3 is the navigator.

---

## Registered Invariants

<a id="inv-035"></a>
**INV-035** — State must not be defined purely by sensory appearance.

> Two perceptually identical situations that differ in temporal position, active commitment, goal/antigoal relation, social context, or operative constraints constitute distinct states. A state definition that collapses to perceptual embedding silently breaks trajectory evaluation, viability mapping, and ethical reasoning.

<a id="inv-036"></a>
**INV-036** — State must support transition prediction, valence/antigoal tagging, and uncertainty representation.

> A representation is a valid REE state only if it (1) grounds plausible next-transition estimates (R), (2) carries goal-relation and antigoal-relation fields (G, A), and (3) represents structured uncertainty (U). Lacking any of these, it cannot participate in hippocampal rollout or E3 path evaluation.

Both registered in claims.yaml 2026-03-24. Status: candidate.

---

## Open Questions

These are unresolved and worth tracking:

**Q: When does a representation become a state?**
Probably when it is bound into a transition-usable frame — i.e., when W, Self, and T are jointly indexed and G/A/C are resolved enough to permit path search. The threshold is functional, not structural.

**Q: Do goals belong inside state (G component) or outside as selectors over state?**
Probably both: goals are partially embedded in the state (as G: goal relation) and partially maintained externally as active task frames (prefrontal WM, z_goal substrate, MECH-116). The state carries the relational component; the external frame carries the target specification.

**Q: How many simultaneous state descriptions can coexist?**
Probably several, across competing scales and framings. The hippocampal system may maintain multiple active state hypotheses simultaneously, with E3 selecting among them during path evaluation. This relates to MECH-022 (hippocampal hypothesis injection) and ARC-018 (counterfactual rollout).

**Q: Is self always explicit in a state?**
Probably not in full detail, but self-relevance likely always modulates state organization. The Self component is a compressed summary, not a full self-model, with context handles into deeper self-representations as needed.

---

## Source

Thought intake: `evidence/planning/thought_intake_2026-03-24_state_definition_hippocampal_primitives.md`
