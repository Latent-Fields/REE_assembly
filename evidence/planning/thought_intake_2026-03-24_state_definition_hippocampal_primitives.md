# Thought Intake: State Definition and Hippocampal Map Primitives

**Date:** 2026-03-24
**Session type:** Design conversation (ChatGPT)
**Source article:** https://scitechdaily.com/scientists-reveal-the-brains-hidden-map-of-thought/
**Output:** `docs/architecture/state.md` written; candidate claims flagged (to be registered in governance)

---

## Prompt

Daniel forwarded a ChatGPT conversation spanning three topics:

1. The "Hidden Map of Thought" neuroscience paper — hippocampus as a general-purpose cognitive map for abstract thought, not just space
2. A formal translation of hippocampal system primitives into REE computational terms (StateNode, TransitionEdge, Path, graph operations)
3. A detailed definition of "state" as a computational unit — "situation as navigable from here"

---

## What's New vs. Existing REE Docs

| Topic | Status |
|-------|--------|
| Hippocampal path memory, replay, viability mapping | Already covered — ARC-007, ARC-018, hippocampal_systems.md |
| Trajectory as core unit, field vs. paths | Already covered — ARC-003, ARC-013, residue_geometry.md |
| E1/E2/E3 brain-region mapping table | Already covered — overview.md, e1.md, e2.md, e3.md |
| State as latent vector / L-space stack | Partially covered — ARC-004, l_space.md (latent stacks defined, not state as navigable unit) |
| Coherence as multi-constraint evaluation | Covered in today's prior intake (thought-intake-coherence-hippocampal-navigation) |
| **Formal definition of "state" as navigable unit** | **NEW — no state.md exists; state referenced throughout but never formally defined** |
| **State vs. representation distinction** | **NEW — representation prepared for transition search, not just encoded content** |
| **Multi-scale state nesting** | **NEW — motor / tactical / episodic / social / identity scale hierarchy** |
| **Failure modes from bad state abstraction** | **NEW — overmerge, oversplit, valence mis-tagging, missing context; psychiatric mapping** |
| **Ethical loading intrinsic to state structure** | **NEW — not pasted on; harm exposure, reversibility, betrayal risk as state components** |
| **"State must not be defined purely by sensory appearance" as invariant** | **NEW candidate** |

---

## Key Formulations from the Intake

### Core definition

> State = situation as navigable from here.

Longer version:

> A REE state is a compressed relational situation-model, integrating world, self, temporal position, goals, antigoals, constraints, and uncertainty, such that plausible transitions can be simulated and evaluated.

### State components S = {W, Self, T, G, A, C, U, R}

| Component | Content |
|-----------|---------|
| **W** | World configuration: objects, agents, relations, affordances, environmental conditions |
| **Self** | Agent configuration: energy, arousal, pain, uncertainty, action readiness, memory quality |
| **T** | Temporal position: where in an episode — beginning, mid-task, post-error, mid-repair |
| **G** | Goal relation: how the current situation stands relative to desired regions |
| **A** | Antigoal relation: proximity to avoided, prohibited, or identity-violating regions |
| **C** | Constraints: physical impossibility, social norms, task rules, identity rules, commitments |
| **U** | Uncertainty structure: not just beliefs but stability of beliefs, confidence in transitions |
| **R** | Transition readiness: which next moves are currently primed or blocked |

### State vs. representation

- **Representation**: encoded content
- **State**: representation *prepared for transition search*

The distinction matters: cortex may hold broad manifold content; the hippocampus indexes navigable states over parts of that manifold. A state is encoded content that has been organized into a unit suitable for transition evaluation.

### Multi-scale nesting

State is scale-relative. The same moment contains simultaneous valid state descriptions at different control scales:

- Motor: hand near cup
- Tactical: making tea
- Episodic: getting ready for work
- Social: navigating a morning after a difficult evening
- Identity: maintaining continuity as someone who functions

E3 evaluates paths across mixed scales. The correct scale for evaluation depends on which transitions are causally load-bearing for the trajectory under consideration.

### Ethical loading as intrinsic

Ethical salience is not external scoring pasted on top of a neutral state. It is part of the state description itself:

- Who may be harmed
- Uncertainty about harm
- Reversibility
- Commitment already made
- Betrayal risk
- Dignity threat
- Truth distortion risk
- Downstream residue likelihood

This is consistent with REE's core claim that ethics cannot be compiled away: the ethical texture is already in the state, not added by a separate evaluation layer.

---

## Failure Modes from Bad State Abstraction

| State abstraction failure | Cognitive/behavioral result | Psychiatric analogy |
|---------------------------|----------------------------|---------------------|
| Overmerge of distinct states | Rigid, inflexible response — same behavior across different situations | OCD, rigid schemas |
| Oversplit of same situation | Failure to generalize — learns each instance separately | Certain autism profiles |
| Loss of hidden context | Impulsive action — transition based on current appearance only | ADHD, impulsivity |
| Valence mis-tagging | Distorted path search — wrong states treated as safe or dangerous | Anxiety, trauma |
| Omission of social constraints | Norm-violating behavior despite adequate world model | Sociopathy, frontal damage |
| Collapse of uncertainty to false certainty | Overcommitment, poor error recovery | Mania, grandiosity |
| Failure to carry residue across transitions | No moral continuity; repeated harm without learning | Psychopathy |
| Threat tags spreading across state graph | Broad avoidance, narrow safe zone | Generalized anxiety |
| Certain states as attractor basins with fast salience | Rapid re-entry, replay dominance | PTSD |
| Commitment continuity fragile | State held only briefly before drift | ADHD, manic episode |

---

## Hippocampal Primitive Inventory (from the intake)

The intake proposed a minimal set of hippocampal primitives. Mapping to existing REE terms:

| Primitive | From intake | REE mapping |
|-----------|-------------|-------------|
| StateNode | id, representation_vector, valence_vector, uncertainty, memory_weight | z(t) in Gamma_i; hippocampal indexing |
| TransitionEdge | from/to state, probability, effort/time/risk cost, rule flags, prediction error | E2 action-consequence kernel; ARC-018 viability map entry |
| Path | states[], total cost, valence, time, uncertainty, coherence_score | Gamma_i episodic trace; trajectory tau |
| simulate_path | start, goal, constraints | Hippocampal counterfactual rollout (ARC-018) |
| replay_path | path | Hippocampal replay (ARC-007) |
| update_transition | edge, prediction_error | Viability map update via E3 harm/goal error (ARC-018) |
| prune_low_value_paths | | Sleep offline integration, residue_geometry.md |
| discover_shortcuts | | Pattern completion, ARC-018 |
| generalise_structure | | Successor representation; MECH-033 |

The primitive inventory is largely consistent with existing REE architecture. The main gap is the lack of a formal state definition tying these primitives together.

---

## Candidate Claims (for governance registration)

These are flagged here for evaluation and formal registration in a future governance session. They are not yet in claims.yaml.

### Candidate INV-0xx: State must not be defined purely by sensory appearance

> A REE state is not a raw observation. Two situations that are perceptually identical can constitute distinct states when they differ in temporal position, commitment, goal/antigoal relation, social context, or active constraints.

**Motivation:** Grounding the state definition as an invariant prevents implementors from collapsing state to perceptual embedding. This would silently break trajectory evaluation, viability mapping, and ethical reasoning.

**Claim type:** invariant
**Depends on:** ARC-004 (L-space), ARC-003 (trajectory selection)

---

### Candidate INV-0xx: State must support transition prediction, valence/antigoal tagging, and uncertainty representation

> A REE state is valid only if it is sufficient to estimate plausible next transitions, assign valence and antigoal loading, and represent uncertainty about those estimates.

**Motivation:** These are the minimal functional requirements for a navigable state. Without them, the hippocampal rollout cannot generate useful candidate trajectories and E3 cannot evaluate them.

**Claim type:** invariant
**Depends on:** ARC-007, ARC-018, ARC-003

---

### Candidate ARC-0xx or MECH-0xx: State abstraction failure modes map systematically to cognitive/psychiatric conditions

> When state abstraction goes wrong in specific ways (overmerge, oversplit, valence mis-tagging, context loss, uncertainty collapse), the resulting behavioral patterns closely correspond to identifiable psychiatric conditions. This suggests the psychiatric taxonomy can serve as a diagnostic frame for state-level architectural failures.

**Motivation:** This is both a scientific claim about the psychiatric taxonomy and a design claim about how to test state abstraction quality. If correct, behavioral tests drawn from psychiatric phenotypes become validity checks for the state machinery.

**Claim type:** mechanism_hypothesis
**Status candidate:** speculative — needs literature grounding before promotion
**Depends on:** INV-0xx (state definition), ARC-007, control_plane.md

---

## Cross-references

- `docs/architecture/hippocampal_systems.md` — ARC-007, ARC-018 (path memory, viability mapping)
- `docs/architecture/residue_geometry.md` — ARC-013 (field vs. paths; cognitive map)
- `docs/architecture/trajectory_selection.md` — ARC-003 (E3 trajectory selection)
- `docs/architecture/l_space.md` — ARC-004 (multi-timescale latent stack)
- `docs/architecture/e1.md`, `e2.md`, `e3.md` — core computational streams
- `docs/architecture/state.md` — **created this session** (formal state definition)
- Prior thought intake today: `thought-intake-coherence-hippocampal-navigation` session (WORKSPACE_STATE.md 2026-03-24)
- Historical note: REE "thoughts as journeys / hippocampal cognitive map" framing dates to `docs/thoughts/2026-02-08_residue_paths_cognitive_map.md` — predates the neuroscience article

---

## Notes

The ChatGPT conversation covered significant ground, but much of the hippocampal material is already well-represented in REE_assembly. The specific new contribution is:

1. The formal state definition as a standalone navigability unit (not just a latent vector)
2. The component decomposition S = {W, Self, T, G, A, C, U, R}
3. The failure mode taxonomy (bad abstraction → specific pathology)

These are captured in `docs/architecture/state.md`.

The hippocampal primitive inventory largely maps onto existing claims. No new architectural claims are created from that section — it reinforces ARC-007, ARC-018, MECH-033 rather than extending them.
