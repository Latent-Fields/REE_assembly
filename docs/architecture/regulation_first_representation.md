---
title: "Regulation-First Representation (ARC-138, INV-104, GOV-MATCHAUX-1)"
parent: "Perception, Representation & Dynamics"
grandparent: Architecture
nav_order: 7
status: candidate
status_asof: 2026-09-04
status_claim: ARC-138
---

# Regulation-First Representation

**Registered:** 2026-09-04
**Source thoughts:** the 2026-09-04 regulation-first cluster (index:
[`docs/thoughts/2026-09-04_regulation_first_fanout_index.md`](../thoughts/2026-09-04_regulation_first_fanout_index.md))
and the literature-bounded trio (Pezzulo 2026; Jiang 2026; Rafiuddin & Sen 2026).
**Intakes:**
[`thought_intake_2026-09-04_regulation_first_organizing_subjective_experience.md`](../../evidence/planning/thought_intake_2026-09-04_regulation_first_organizing_subjective_experience.md),
[`thought_intake_2026-09-04_causal_compression_grounded_development.md`](../../evidence/planning/thought_intake_2026-09-04_causal_compression_grounded_development.md).

> **DOC + GOVERNANCE ONLY.** No substrate, no experiments, no V3 behaviour change. Every claim here
> is `candidate`. The cluster's own strongest challenger -- that generic predictive compression
> already preserves every behaviourally relevant distinction -- is registered alongside as the null
> each claim must beat, not argued away.

---

## The thesis

> **Constraints come first; meaning follows.** The machine constrains things first. It functions
> before it knows. Experience is organized through regulation, and knowledge is what that organized
> experience can become.

REE's live v3 wall is the observation -> `z_world` -> E1/E2 interface
(`evidence/planning/cross_plan_root_cause_synthesis_20260902.md`). The 2026-08-26
[selection-relevant representation](selection_relevant_representation.md) cluster asked whether the
world should be carved by *why things matter* (ARC-133, rival to MECH-278). This cluster asks the
developmental form of the same question: not "how should an agent represent the external world" but
"how does a regulated, vulnerable, acting machine organise experience according to its own enduring
constraints, such that a detached world model becomes *reachable* at all". Two independent routes
reached the same preservation requirement on the same day -- the user's introspective cluster written
against the wall, and three external papers -- which is recorded, not counted as evidence.

What REE has already measured bounds the cluster: V3-EXQ-978 showed directional resource information
is PRESENT in `z_world` (r2 0.71-0.86) and yet unused; the open branch is consumer (H-B) vs geometry
(H-C), routed to V3-EXQ-1002. Nothing here re-opens that; the experiment the cluster proposes is
gated behind it.

---

## ARC-138 -- regulation-first representational organisation {#arc-138}

The developmental ordering **machine -> regulation -> interaction -> organised experience ->
knowledge**: a mature, detached, portable world model is a developmental achievement, reached only
through interaction that the organism's own regulatory constraints (continued existence, structural
integrity, internal-state regulation, vulnerability, ability to effect change, control, attachment,
causal uncertainty) generate and select; the earliest useful organising axes of `z_world` are
relations between external regularities and those constraints (what changes me / what I can change /
what predicts harm or benefit / what is controllable / what persists / what belongs together).

**Non-redundant empirical content** (the cluster's predictions 6 and 7): agents with matched sensory
statistics but different vulnerabilities or affordances should develop systematically different
latent organisations of the same environment; if objective scene structure suffices, vulnerability
changes should leave latent organisation unchanged once observations are matched.

**Distinct from** ARC-133 (a criterion for individuating objects at maturity; makes no
vulnerability-matched prediction; says nothing about ordering), INV-030/031 (viability is the *goal*
of cognition, not the developmental *ordering* of representation), ARC-059 / ARC-122 (order the
*training curriculum*; ARC-138 supplies the rationale they share -- later representations remain
answerable to earlier organism-world relations). **Counter-constraint:** MECH-520 (predictive
obligation) -- a representation carved by regulatory relevance alone collapses to a value projection;
ARC-138 depends on it rather than competing with it.

`substrate_conditional`, v4. DO NOT build in V3; DO NOT queue.

---

## INV-104 -- organism-relevant distinction preservation across compression {#inv-104}

Any compression, abstraction, or consolidation step on the observation -> `z_world` -> E1/E2 path
(and any offline schema-compression of episodes) must preserve, or leave recoverable through its
dynamics, the distinctions that are consequential to the organism across time. Five preservation
classes, drawn from three sources:

1. **consequence and opportunity/threat** -- harmful / beneficial / neutral / uncertain effects; which
   future interactions a state affords, not merely where things are;
2. **controllability and agency** -- outcomes the organism can influence vs cannot; self-caused /
   potentially-self-caused / externally-caused change; internal-state consequence not visible in the
   external scene;
3. **persistence and temporal relation** -- what remains the same entity / relation / source across
   changing observations; enough temporal structure to separate coincidence from regularity;
4. **causal ancestry / intervention handles** (from the C3T / Jiang thought) -- agent identity or
   type, action class, contextual preconditions, uncertainty over causal contribution -- so a
   compressed schema can later be queried counterfactually;
5. **independently evolving trajectories** (from Pezzulo) -- evidence that an entity's behaviour
   cannot be compressed as a static affordance or moving obstacle.

These are **preservation requirements, not latent dimensions**: the invariant is satisfied when
downstream systems can recover the distinction when it is needed, not when a coordinate encodes it.
A step that destroys access to one of them is a developmental regression *regardless of
reconstruction or prediction loss*. Auxiliary heads that enforce a class during training are
**scaffolds**: a scaffold should be removable without destroying the acquired organisation, and the
ontology within a class must remain free to split, merge and reweight over development (MECH-496 /
INV-101).

**Distinct from** INV-035 (which *situations* count as distinct states -- the state-level cousin);
MECH-100 / SD-009 and SD-018 (single-class scaffolds of exactly this kind: event-type; resource
proximity); SD-070 (the measured precedent that `z_world` collapses); MECH-520 (why the constraint
cannot be value alone). **Adjudication frame recorded for class 2:** agency is (a) derivable from
generic prediction + action input, (b) a downstream planning variable that should NOT be forced into
`z_world`, or (c) reducible to intervention-sensitivity (SD-056's primitive) with "self" emerging later
-- three rivals, not wording variants.

`substrate_conditional`, v3 (the path it constrains is the live wall; class 1's directional row has
already been probed) -- flagged for a `/governance` routing decision.

---

## GOV-MATCHAUX-1 -- matched-auxiliary-control and scaffold-removal admissibility {#gov-matchaux-1}

**Rule.** A result is admissible as evidence that a representation objective (auxiliary head,
anchoring target, contrastive shaping, or any added loss) *organises* a latent in a specific way --
rather than that extra supervision helps -- only if it was obtained against BOTH:

1. a **matched arbitrary-auxiliary control**: same head capacity, loss budget, update frequency,
   training examples and, as far as practical, target dimensionality and entropy, with a target that
   has learnable structure but no organism-relevant content (a nuisance feature or an action-irrelevant
   transform of the observation); if entropy or difficulty cannot be matched, the mismatch is
   *reported*, never silently accepted; and
2. an **evaluation with the auxiliary head removed** (no privileged variable at inference), scored on
   downstream organism-level measures -- rollout quality at consequential transitions, behavioural
   competence, transfer when consequences change but sensory statistics do not, counterfactual
   separability, perturbation recovery -- never on the objective's own probe accuracy or loss.

The same rule in its **offline-mechanism form** (the routing note's Gate C): adopt a durable
sleep / replay / compression mechanism only on held-out causal attribution, intervention choice,
transfer or calibration, not on training loss or replay reconstruction.

**Motivating incident** (V3-EXQ-978, autopsy section 4): the SD-018 ON-vs-OFF manipulation was a ~1.5x
*reweighting* of a field `reconstruction_weight = 10.0` already supervised, the label ladder never
consulted the OFF arm's r2, and the pre-registered null table was the only thing that stopped the
result being read as supervision-vs-none. **Candidate held-out cases for the GOV-HELDOUT-1 check owed
before this becomes a skill rule** (old and new wording must give DIFFERENT calls for a case to
count): V3-EXQ-817a's grounding contrast (run through a collapsing interface -- MECH-517); MECH-100's
event-type CE (accepted as `stable` without an arbitrary-auxiliary control); V3-EXQ-978 itself.

**What it is not.** Not a claim about REE; a warn-only member of the routing-standard family
(GOV-PATHVALID-1, GOV-FAILLOC-1, GOV-REUSE-1, GOV-FANOUT-1). It changes no claim's status. Adopting it
into `/queue-experiment` or `/failure-autopsy` is a separate standing-rule change.

---

## Sequencing (nothing here authorises V3 work)

- V3-EXQ-1002 (campaign C1) decides H-B vs H-C first.
- Only then: the three-condition comparison (A perceptual / B matched arbitrary auxiliary / C
  regulatory anchoring) as a NEW question under INV-104 / ARC-138 / GOV-MATCHAUX-1, never under
  INV-088 / MECH-457 (re-derive brake fired on both). Chip
  `chip-20260904-regulatory-anchoring-matched-aux` carries the design and both stop conditions.
- Second-stage arms (agency anchoring, developmental staging, replay sensitivity) only if the first
  comparison shows signal against the matched control.
