---
title: "SD-097: typed multi-relation possibility topology"
nav_exclude: true
status: candidate/substrate_conditional
status_asof: 2026-09-17
status_claim: SD-097
---

# SD-097: typed multi-relation possibility topology

**Claim ID:** SD-097
**Subject:** goal.general_relational_possibility_topology
**Registered:** 2026-08-07
**Status:** FIRST SLICE BUILT (2026-09-17, `enables` only -- see Implementation)
**Depends on:** SD-004, SD-039, MECH-292, MECH-293, MECH-189, SD-092, MECH-427,
MECH-428 (all eight have landed substrate; the substrate_queue entry's
`depends_on_unresolved` list is stale and its own `origin` field says so --
GFLAG-0331)
**Blocks:** SD-098 (read-time relational goal-ness)
**Design session:** eloquent-jepsen-5f6242 (research + design), commissioned via
Orchestrator orchestrate-20260917-1532
**Build session:** substrate-build-20260917-sd097 (first slice, concurrent with
this document)

---

## Problem

SD-097 as registered names **eight** relation types -- `requires`, `enables`,
`is_part_of`, `prevents`, `conflicts_with`, `substitutes_for`,
`provides_information_about`, `may_become_useful_under_context` -- and asserts
that possibilities must be connected by explicit relation TYPES, not merely by a
scalar relevance value.

A triage pass found the blocking defect: **the eight types had no semantics and
no consumer.** Nothing in E3 or in `HippocampalModule.propose_trajectories`
reads a relation type. Built as written, SD-097 would be inert substrate that no
experiment could exercise -- the failure mode where a claim's implementation
lands, passes its contract tests, and cannot produce a single line of evidence.

This document answers, for each of the eight, the three questions that decide
whether it is real: what would read it, what behaviour changes when something
does, and whether it is distinct from a relation or a scalar that already
exists.

### Two facts the research turned up that reshape the claim

**(1) SD-092's "parent/subgoal edge" does not exist as an edge.** SD-097's own
framing -- "not merely the existing parent/subgoal edge" -- presupposes an edge
to generalise. `ree_core/goal.py` implements SD-092 as an **EMA pull between two
latent vectors** (`_z_goal` and a lazily-allocated `_z_goal_parent`) behind
`use_hierarchical_goal_credit` (goal.py:320-352, 930, 969-1030). There is no
node identity, no pair, nothing to traverse. This matters directly for the
falsifier: ARM 2 as literally worded in `what_would_answer` ("a model built only
from SD-092's parent/subgoal edge plus MECH-292's ghost-goal ranking") **cannot
be built**, because there is no edge to expand. Section "The three arms" below
specifies the faithful substitute.

**(2) A relation type is only doing work if its WRITE EVENT distinguishes it
from every other type.** This is the spine of the whole analysis and it is the
constraint that collapses five of the eight. The read side is cheap -- any
number of consumers can be written to branch on a string. The expensive half is
the **observation** that licenses stamping one type rather than another onto an
edge. Where two types would be written from the same observation, they are not
two types; they are one edge read two ways, and the "type" is a label the
substrate cannot earn.

The first shipped slice illustrates the hazard rather than escaping it: the
anchor-remap succession writer records `A enables B` when anchor B replaces
anchor A as the active anchor of a `(scale, stream_mixture)` family. That single
event is **equally consistent** with `A conflicts_with B` -- A and B cannot both
hold the family's one active slot, so the remap is a displacement as much as a
succession. The shipped `enables` edge is therefore under-determined by its own
write event. Nothing is broken by this today (one relation, one consumer), but it
sets the bar every further relation must clear.

---

## Solution: three relation types, not eight

The honest result of this research is a **narrowing**. Collapsing a relation is
a result, not a failure, and five of the eight collapse:

| # | Relation | Verdict | Where it goes |
|---|----------|---------|---------------|
| 1 | `enables` | **DISTINCT -- shipped** | ghost-probe seeding (GhostGoalBank.rank) |
| 2 | `provides_information_about` | **DISTINCT -- ship next** | MECH-482 epistemic-deficit routing |
| 3 | `conflicts_with` | **DISTINCT -- third** | negative admission / seed-batch diversity |
| 4 | `requires` | COLLAPSE (read direction) | `predecessors()` of `enables`; a *necessity* writer is separately probe-gated |
| 5 | `prevents` | HELD -- `complex (probe-gated)` | needs negative evidence the anchor stream does not emit |
| 6 | `is_part_of` | COLLAPSE (already in the key) | AnchorKey `scale` + `"outer.inner"` segment_id |
| 7 | `substitutes_for` | COLLAPSE (already a scalar) | `goal_match` ranking against the same `current_z_goal` |
| 8 | `may_become_useful_under_context` | COLLAPSE (arity + already built) | MECH-339 composite-cue context channel |

Detailed argument for each is in "The eight, one by one" below.

The substrate SD-097 actually owes is therefore: **a relation-generic typed edge
store over AnchorKeys, carrying three relations whose consumers are distinct from
one another, plus the three-arm falsifier that decides whether the types earn
their keep.** The generic store is the right shape and is built; the eight-type
ambition is not, and the substrate_queue entry should be narrowed to say so.

---

## The node primitive, and where it stops generalising

The build session chose **`AnchorKey = (scale, segment_id, stream_mixture)`**
(`ree_core/hippocampal/anchor_set.py:17,116`, constructed at :297 and :365) over
the two alternatives (SuperOrdinalGoalMemory slots, E2 action objects). The
reason is correct and worth restating: AnchorKey is the only one of the three
that is **already a hashable identity with a live read-time consumer ranging over
the same pool** -- `GhostGoalBank.rank()` walks every anchor on every call. The
other two would have required inventing the consumer alongside the topology,
which is the inert-substrate failure again.

**It does not generalise to all eight, and the way it fails is informative:**

| Relation | Does AnchorKey support it? | Failure mode |
|----------|---------------------------|--------------|
| `enables` | YES | -- |
| `provides_information_about` | YES, with a key-mapping cost | MECH-482 targets are z_world points, not AnchorKeys; needs a nearest-anchor lookup |
| `conflicts_with` | YES | -- (family contention is directly observed) |
| `requires` (as necessity) | NO | polarity of evidence -- needs non-occurrence counting |
| `prevents` | NO | polarity of evidence -- needs counterfactual/extinction evidence |
| `is_part_of` | REDUNDANT | the key already encodes it |
| `substitutes_for` | NO | wrong level of abstraction -- anchors are PLACES, substitutability is a property of MEANS |
| `may_become_useful_under_context` | NO | wrong ARITY -- needs `(src, dst, context)`, the store is 2-ary |

Four distinct failure modes, only one of which (polarity of evidence) is about
the anchor stream being thin. **The `substitutes_for` failure is the one that
would force a node-primitive change**: if a future consumer genuinely needs
means-level substitutability, the right node is the rejected alternative -- the
E2 action object -- and that is a separate build, not an extension of this one.
The rejection of action objects was right *for `enables`*; it is not a
permanent verdict.

---

## The eight, one by one

### 1. `enables` -- DISTINCT, SHIPPED

**(a) Consumer.** `GhostGoalBank.rank()` ->
`GhostGoalBank._admit_relational_successors()` ->
`HippocampalModule._propose_ghost_seeded()` (module.py:2731-2860), which seeds
CEM probes from `rank()[:n_ghost]` anchors' `z_world`. Real, live, and already
ranging over the AnchorKey pool before SD-097 existed.

**(b) Behaviour change.** An anchor that cleared `goal_match_floor` on its own
vouches for its `enables` successors, which are admitted **with the floor
waived** -- their relevance arrives through the relation rather than through a
direct goal-match -- scored on their own channels plus
`relation_weight * edge.weight * parent_goal_match`, and sorted into the same
list. Because the seed set changes, **the agent probes regions of z_world it
would otherwise never reach**. Depth is one hop; no transitive closure.

**(c) Distinct.** Yes, by construction -- it is the reference relation. Note
carefully that *distinct* here means "distinct from the scalar baseline", and
with only one relation registered it is NOT distinct from an untyped edge. See
"The single-relation trap" below: this slice is necessary infrastructure and is
**by construction unable to produce SD-097 evidence on its own.**

### 2. `provides_information_about` -- DISTINCT, SHIP NEXT

**(a) Consumer.** `ree_core/policy/epistemic_deficit.py` --
**MECH-482 EpistemicDeficitAccumulator (SD-102)**, already live. It maintains
persistent deficit state "keyed by WHERE in z_world space the deficit was
observed (a 'target')", and its READOUT scores this tick's K CEM candidates by
their nearest persistent target, returning the
`per_candidate_learning_progress` vector `StructuredCuriosity.compute_score_bias`
consumes. This is a real consumer that exists today and needs no invention.

**(b) Behaviour change -- and this is the strongest type-does-work argument in
the whole set.** Today, deficit accumulated at region B biases candidates
**near B**. An edge `A provides_information_about B` routes B's deficit into a
probe bonus at **A** -- "go to A in order to learn about B" -- where A may be
arbitrarily far from B in z_world. **No monotone function of per-region scalars
can produce this.** A scalar field assigns value to a place; it cannot express
that one place is informative *about a different place*. That is precisely the
gap `what_would_answer` demands the typed model fill and the scalar model fail.

**(c) Distinct.** Unambiguously. Different consumer, different direction of
information flow, and it is the only one of the three whose read is not "admit
this successor".

**Write event (distinguishable, and cheap).** MECH-482's deficit already RISES
and QUENCHES on its own persistent targets. The observation is a **quench at
target B temporally coincident with recent occupancy at anchor A** -- no
counterfactual, no non-occurrence counting, no similarity inference. It is the
same class of event as the remap succession writer: something observably
happened. Size estimate: ~120-180 lines (a second writer on the topology + a
nearest-anchor key mapping + a readout hook in `epistemic_deficit.py`), plus
wiring and contracts.

**Honest caveat.** MECH-482 keys on z_world points, not AnchorKeys, so the
nearest-anchor lookup is real work and introduces an approximation (two deficit
targets can map to one anchor). It is small, but it is not free, and it should
be measured rather than assumed harmless.

### 3. `conflicts_with` -- DISTINCT, THIRD

**(a) Consumer.** Two candidates, of increasing cost.
*(i) Cheap, in scope:* the same admission site, as a **within-batch exclusion** --
do not seed two conflicting probes in one `rank()` call, spend the budget
elsewhere. One clause in `_admit_relational_successors`.
*(ii) Expensive, crosses a module boundary:* E3's eligibility mask. E3 already
has a rich per-candidate No-Go architecture (`elig_mask`, safety No-Go, the
MECH-260 per-candidate suppression axes, `e3_selector.py:1978-2059`) and a
learned lateral-inhibition matrix `W_lat` (:698). **The bridge exists**: ghost
trajectories carry `traj.metadata["anchor_key"]` (module.py:2840), so an
anchor-keyed relation CAN reach an E3 candidate. But E3's conflict substrate is
over candidate slots and is *learned*, not stored, so this is a 150-250 line
build that also has to argue it is not duplicating `W_lat`. **Ship (i), not (ii).**

**(b) Behaviour change.** Seed-batch diversity: the probe budget stops being
spent on mutually-exclusive variants of one option.

**(c) Distinct -- and specifically NOT the same relation as `prevents` with a
sign flipped.** The chip's hypothesis was reasonable and it does not survive
contact with the two definitions:

| | `conflicts_with` | `prevents` |
|---|---|---|
| symmetry | symmetric | directed |
| tense | simultaneous ("cannot both be pursued now") | future ("A closes off B") |
| consumer | within-batch diversity | veto on future admission |
| write event | family contention -- **directly observed** | extinction of a previously-observed succession -- **not observed** |

They share only a polarity. The store's `RelationSpec.directed` flag exists for
exactly this asymmetry. The minimal build ships **one** negative relation, and it
must be `conflicts_with`, because it is the one whose write event the substrate
actually emits: `AnchorSet` enforces one active anchor per
`(scale, stream_mixture)` family, so every remap **is** an observed displacement.

**And that is exactly why it must be sequenced third, not second.** The remap
event currently writes `enables`; the same event would write `conflicts_with`.
Registering both without first disambiguating them would ship two relation names
over one indistinguishable observation -- the failure this document's spine
warns against. Disambiguating requires either a second signal at the remap site
(did B's segment follow A's contiguously, or interrupt it?) or a separate write
site. **Resolve that before registering it.**

### 4. `requires` -- COLLAPSE into a read direction

**(a) Consumer.** `PossibilityTopology.predecessors()` already exists and
nothing reads it; the module docstring is explicit that it is "the reverse query
a future `requires` consumer wants". A plausible real consumer is the same
ghost-seeding site running BACKWARD: when a goal-relevant anchor is itself the
destination rather than a reachable probe target, admit its **predecessors** as
seeds -- probe the precondition, not the goal.

**(b) Behaviour change.** Genuinely different from `enables`: forward expansion
FROM a floor-clearing anchor versus backward expansion TO one.

**(c) Distinct? NO, at the storage layer.** With the anchor-remap succession
writer, `A enables B` and `B requires A` are **written from the same observation
and stored in the same pair of indexes** (`_out` / `_in` hold the same edge
objects). Registering `requires` as a second relation name would create a second
edge carrying no information the first does not. **Recommendation: implement
backward expansion as a `direction=` option on the seeding consumer, NOT as a
relation type.** That gets the behaviour at a fraction of the cost and without
a type the substrate cannot earn.

`requires` becomes a genuinely distinct relation only under a different writer --
a **necessity** observation (B never occurred without A having occurred) rather
than a succession observation. Succession is not necessity. That writer needs
non-occurrence counting over anchor families, which is the same negative-evidence
problem that gates `prevents`; see below.

### 5. `prevents` -- HELD, `complex (probe-gated)`

**(a) Consumer.** The strongest available is the E3 No-Go path described under
`conflicts_with` (ii): a hard veto rather than a ranking penalty. That is a real
qualitative difference -- a scalar priority can always be outvoted; a No-Go
cannot -- and it is the most compelling read-side story of the eight.

**(b) Behaviour change.** Candidates get dropped, not down-weighted.

**(c) The blocker is the WRITE side, and it is not a matter of effort.** "A
prevents B" means: after A, B stopped being reachable. That is an **extinction /
non-occurrence** observation. The anchor stream emits events (remaps, boundary
pulses); it does not emit non-events, and the density of anchor families over an
episode is not obviously sufficient to estimate "B never followed A" against a
sensible null. Whether it is estimable at all on this substrate is an **open
empirical question, not a build task** -- which is what `complex (probe-gated)`
means. The probe is specified under "node_class recommendation" below.

A harm-tagged shortcut is available and should be named so it is not mistaken
for the real thing: "A was followed by B and B carried a hazard event" is
cheaply observable (hazard_field / harm_exposure / HarmSufferingAccumulator all
exist) -- but that is `A leads_to_harm B`, an outcome tag on a succession, not
`prevents`. It would be a fourth relation with a fourth consumer story, and it
should be registered under its own name or not at all.

### 6. `is_part_of` -- COLLAPSE into the key

**(a) Consumer.** None, and none needed. **The AnchorKey already encodes
containment.** `segment_id` is generated by the MECH-288 event segmenter in
nested `"outer.inner"` form (`event_segmenter.py:4,57,399-403,423`), under an
explicit cross-scale rule: a slow (outer) fire increments `outer` and resets
`inner`; every other scale increments `inner` only. So every fast anchor with
`segment_id` `"k.j"` is, by construction, contained in outer segment `k` -- and
`scale` is the first field of the key. Part-of is **parseable from the key
string** with no store, no writer, and no edge.

**(b) Behaviour change from storing it: none** that a read-time derivation could
not give, at strictly higher cost and with a consistency hazard (a stored edge
can disagree with the key it was derived from).

**(c) Verdict: do NOT register.** If a consumer ever needs part-of, add a derived
`parts_of(key)` query over the anchor pool. Storing this relation would be the
canonical inert-substrate failure -- an edge type whose entire content is a
re-encoding of data the node identity already carries.

### 7. `substitutes_for` -- COLLAPSE into ranking

**(a) Consumer.** None exists. The nearest candidates are seed-budget dedup
(if X substitutes for Y and Y is admitted, drop X) or
`_mix_value_flat_with_ghost`'s eviction ordering (module.py:2862+).

**(b)/(c) It is already a scalar, and the scalar is already computed.** "X
substitutes for Y" over anchors means "X and Y lead to comparable satisfaction
of the current goal" -- which the bank **already measures**, as `goal_match`
against the same `current_z_goal`. Two anchors with near-equal `goal_match` ARE
substitutes, computed fresh each tick, with no staleness risk. A stored edge
would add exactly one thing the scalar lacks: **contextual** substitutability
(X substitutes for Y only under context C) -- and that is relation 8 wearing a
different hat, with relation 8's arity problem.

**Verdict: do NOT register.** If a real need appears it is a **tie-break rule
over `goal_match`**, not an edge type.

### 8. `may_become_useful_under_context` -- COLLAPSE (and it is already built)

**(a) Consumer.** The chip's guess was that this is the ghost bank's
`recoverability` term. Close, but the more exact match is a different existing
channel. `recoverability` is `last_vs`-derived (was this anchor healthy when
preserved -- `ghost_goal_bank.py:617-632`), which is a *condition* fact, not a
*context* fact. The real existing analogue is **MECH-339's composite-cue /
outshining context channel** (`ghost_goal_bank.py:24-46`):

```
context_salience = 1 - exp(-arousal_tag / arousal_scale)
gate             = clip_[0,1]((outshine_pivot - goal_match) / outshine_pivot)
context_term     = context_weight * gate * context_salience
```

which is precisely "this anchor becomes salient when the context matches, even
though its direct goal-match is weak" -- and is outshone by a strong direct
match, which is the correct behaviour for a may-become-useful signal.

**(b)/(c) It is ALREADY IMPLEMENTED as a gated scalar channel**, and promoting it
to an edge type would require an **arity change**: `(src, dst, context)`. The
store is 2-ary (`relation -> src -> dst -> TopologyEdge`), so this is a schema
change, not a registration.

**Verdict: do NOT register.** Re-open only if 3-ary contextualised edges are
independently motivated by some other consumer -- at which point it is its own
claim with its own falsifier, not a line item under SD-097.

---

## The single-relation trap

**The shipped `enables` slice cannot, by construction, produce SD-097 evidence.**
This is the most operationally important consequence in this document and it
should be stated plainly rather than discovered by a confused experiment session.

`what_would_answer` requires showing that representing the relation **TYPE**
is what makes the behaviour work, against a model with the same relevance
signals and no types. With exactly **one** relation registered, erasing the type
labels leaves **one unlabelled relation** -- and the typed model and the untyped
model compute the identical function. ARM 1 and ARM 2 are literally the same
program. There is no experiment to run.

**The gate is not relation COUNT -- it is consumer DISTINCTNESS.** Two relations
that feed the *same* consumer (e.g. `enables` plus `requires`, both admitting
probe seeds) are still scalar-collapsible: a single channel with a signed weight
reproduces both, and the untyped arm wins the ablation. The falsifier becomes
runnable only when **two relations feed two different consumers**, so that the
untyped arm must route both through one channel and is forced into a choice
that is wrong for at least one of them.

This is the precise reason `provides_information_about` -- not `requires`, and
not `conflicts_with` -- is the correct second relation. It is the only remaining
candidate that clears all three bars simultaneously:

1. it has an **existing live consumer** (MECH-482), so nothing has to be invented;
2. it has a **distinguishable write event** requiring no counterfactual evidence;
3. its consumer is **different from `enables`'**, which is the precondition for
   ARM 1 / ARM 2 separability.

Nothing else in the eight clears all three.

---

## The three arms

The falsifier is a three-arm comparison. All three must be specified, and the
`what_would_answer` verdict turns on ARM 1 vs ARM 2; ARM 3 decides only whether
the whole apparatus was *necessary*.

### ARM 1 -- typed topology (the build)

Topology ON, with **at least two relations feeding two different consumers**:
`enables` -> ghost-probe seeding; `provides_information_about` -> MECH-482
deficit routing. `use_possibility_topology=True`, both writers armed.

### ARM 2 -- untyped topology (the type-ablation; THIS is the decisive arm)

**ARM 2 as literally worded in `what_would_answer` cannot be built** -- SD-092's
parent/subgoal "edge" is an EMA pull between two latent vectors, with no node
identity to expand (see Problem, fact 1). The faithful substitute, which honours
the intent (the strongest possible baseline carrying the same information and
the same relevance signals, minus the types), is:

> **The same store, the same write path, and all edges collapsed to ONE
> unlabelled relation, admitted through a single tuned scalar weight --
> with SD-092's `use_hierarchical_goal_credit` ON so the hierarchical-credit
> signal is genuinely present, and MECH-292's ranking unchanged.**

This is a *type*-ablation, not a *structure*-ablation: ARM 2 keeps every edge
ARM 1 has and every scalar signal ARM 1 reads. It differs in exactly one thing --
it cannot tell the two relations apart, so it must route both through one
channel.

There is precedent for this arm shape in this codebase: **SD-091/MECH-481's Arm 3
("untyped coalition")** is the same ablation applied to coalition control, and
`CoalitionController`'s guardrails are written against it explicitly.

**Tuning is mandatory and is part of the arm, not an optimisation.**
`what_would_answer` says "tuned on the same relevance signals". ARM 2 must be
given a genuine sweep over its single mixture weight (a grid over
`relation_weight`, plus the mixture between probe-seeding and deficit routing),
and ARM 1 must be compared against ARM 2's **best** setting, not its default.
An ARM 2 run at one default value is not a baseline; it is a straw man, and a
result obtained against it should not be recorded as evidence.

**The predicted ARM 1 / ARM 2 dissociation, stated in advance.** ARM 2's single
channel must send every edge somewhere. Its three options are:
- route everything to probe-seeding -> the epistemic behaviour is lost (it never
  goes to A to learn about B);
- route everything to deficit routing -> the reachability behaviour is lost;
- a tuned blend -> a single mixture that is wrong for both, and can be made right
  only by adding a per-edge discriminator, **which is a type**.

That third branch is `what_would_answer`'s "ad hoc special case per new relation
type" clause, made concrete and measurable.

### ARM 3 -- Kinny & Georgeff scalar-commitment baseline

A "bold" agent with **no stored relational structure at all**: topology OFF,
ghost-goal retention OFF, and a single scalar policy for how many plan-steps to
execute before reconsidering.

Both knobs this arm needs are already live:

- **Dynamism (K&G's gamma, rate of world change relative to the agent's clock):**
  `ree_core/environment/causal_grid_world.py` exposes `env_drift_interval`
  (default 5) and `env_drift_prob` (default 0.3). Sweeping these IS the gamma
  sweep.
- **Reconsideration rate:** the existing commitment machinery --
  `NaturalCommitUrgencyRelease` / `commit_maintenance_release` / policy chunk
  length -- is the bold/cautious axis.

ARM 3 must be swept over dynamism, not run at one setting. K&G's result is that
at LOW dynamism a bold agent achieves E ~ 1 with no machinery whatsoever; a
single-dynamism comparison would either flatter or slander the topology
depending entirely on which point was picked.

---

## Discovery leg vs retention leg -- which arm tests which

K&G's limit is precise and load-bearing, and the design must respect it rather
than treat ARM 3 as a general-purpose skeptic:

> Kinny & Georgeff's agents **have no analogue of retaining an inactive
> possibility across time for later reactivation.** Reconsideration there means
> re-planning from the current state, not consulting a persistent structure.
> (The entry's own summary says so, and grades the evidence `mixed`, conf 0.55,
> for exactly this reason.)

So the falsifier has two legs and they are adjudicated differently:

| Leg | What it tests | ARM 1 vs | ARM 3's role |
|-----|---------------|----------|--------------|
| **DISCOVERY / RECONSIDERATION** -- clause (a) of CONFIRMED: discover mid-episode a possibility related by a non-parent/subgoal relation | whether typed structure beats a reconsideration-rate scalar | ARM 2 **and** ARM 3 | **Full competitor.** If ARM 1 beats ARM 3 only at high dynamism, and by a margin a tuned reconsideration rate also reaches, the topology is unnecessary for this leg. |
| **RETENTION / REACTIVATION** -- clauses (b) and (c): retain at sub-goal salience without acting, then retrieve and act when context changes | whether the relation TYPE is needed to hold and re-surface an inactive possibility | ARM 2 only | **Floor, not competitor.** K&G has no analogue of this job. ARM 3 enters only to show the task is non-trivial. |

**The error this table exists to prevent:** reading an ARM-3-competitive result
on the discovery leg as falsification of the whole claim. It is not. It is
falsification of the discovery leg, which is the only leg K&G's evidence
reaches.

**And the symmetric honesty requirement:** a design in which K&G's single scalar
explains everything has **not shown the typed topology wrong -- it has shown it
unnecessary**, which is the FALSIFIED condition and must be recorded as such
rather than explained away.

---

## Non-degeneracy, and two measured traps

`what_would_answer` carries an explicit NON-DEGENERACY PRECONDITION: the
baseline must be shown to be genuinely exercised -- "live cross-seed variance in
which possibilities get revisited" -- before concluding the typed extension adds
function. Concretely, before any ARM 1 vs ARM 2 verdict is recorded:

1. **ARM 2 must actually admit relational successors.** Report
   `n_relational_admits > 0` with cross-seed variance, not a constant. An arm
   whose relational channel never fires is not a baseline.
2. **ARM 2's tuning sweep must be real** (see ARM 2 above).
3. **Both arms must show cross-seed variance in WHICH anchors get revisited.** A
   degenerate arm that always revisits the same anchor makes the typed model look
   necessary when it is merely the only one that was tested.

### Trap 1: do not put the DV at the end of a long untrained rollout

**V3-EXQ-881 measured this directly** and its design note is load-bearing here.
`e2.world_forward` is an untrained (random-init) recurrent transition function
and is **expansive/chaotic at this scale**: a seed-point separation of norm
~0.03-0.07 grows to endpoint norms of ~300 within a few rollout steps, and by
step 1 the ghost-vs-value-flat separation is already statistically
indistinguishable from noise (8-15x amplification in one step). A raw
endpoint-distance DV at `horizon=30` reports which way an exploding random system
happened to wobble, not whether the relation did work.

**Consequence for SD-097's DV design.** The primary DVs belong at the
**admission / seed / routing** level, where the relation's effect is direct and
uncontaminated:

- **Discovery leg:** did the non-parent/subgoal successor enter the ranked bank
  at all, and with what provenance (`GhostGoalBankEntry.relation_provenance`
  carries `relation`, `parent_key`, `edge_weight`, `parent_goal_match` -- it is
  already built for exactly this)?
- **Retention leg:** did the admitted-but-not-acted-on entry persist across the
  context shift, and did its rank rise after the shift?
- **Epistemic leg (ARM 1 only):** did a candidate near A receive a
  `per_candidate_learning_progress` bonus sourced from a deficit target near B?

A behavioural leg over long rollouts is legitimate **only on a trained
substrate**, and if included must use V3-EXQ-881's within-episode
scatter-normalised form (compare cluster means relative to the value-flat
population's own scatter) rather than an absolute distance.

### Trap 2: the write event must be disambiguated before a second relation is registered

Restated here because it is an experiment-design hazard and not only a build
one: the remap event currently licenses `enables`, and would equally license
`conflicts_with`. If both are registered off the same event, ARM 2 collapses
them correctly and ARM 1 gains nothing -- and the experiment will report a true
negative about a build defect, which is an expensive way to learn it.

---

## Staging order

| Stage | Relation | Consumer | Status | Why here |
|-------|----------|----------|--------|----------|
| 1 | `enables` | ghost-probe seeding | **BUILT 2026-09-17** | Only relation with a pre-existing live consumer over the same pool. Infrastructure; cannot produce evidence alone. |
| 2 | `provides_information_about` | MECH-482 epistemic-deficit routing | **NEXT** | The only remaining relation with an existing consumer, a counterfactual-free write event, AND a consumer distinct from stage 1's. Stage 2 is what makes the falsifier runnable at all. |
| 2b | -- | -- | **THE FALSIFIER** | Three-arm experiment, queued via `/queue-experiment` once stage 2 lands. |
| 3 | `conflicts_with` | within-batch seed exclusion | AFTER a CONFIRMED 2b | Requires disambiguating the remap write event from `enables` first. |
| 4 | `prevents` | E3 No-Go veto | **HELD -- probe-gated** | Needs negative/extinction evidence the anchor stream does not emit. |
| -- | `requires` | backward seed expansion | Implement as `direction=` on the stage-1 consumer | Same edge, reverse index. Not a relation. |
| -- | `is_part_of`, `substitutes_for`, `may_become_useful_under_context` | -- | **DO NOT BUILD** | Collapsed -- see the table in Solution. |

**Answer to "which ships next after `enables`":** `provides_information_about`,
and the reason is not that it is the most interesting relation but that it is
the only one that makes SD-097 testable. Shipping `requires` or `conflicts_with`
second would add a second relation name without adding a second consumer, and
the falsifier would stay unrunnable.

---

## Implementation (stage 1, built 2026-09-17)

Built by session `substrate-build-20260917-sd097`, concurrent with this
document. Read-only summary -- this design session did not touch `ree_core/`.

- **New module `ree-v3/ree_core/hippocampal/possibility_topology.py`** (498 lines).
  `RelationSpec` / `RelationRegistry` (a description is **required**; an
  undescribed relation is not registerable -- the store enforces the defect this
  claim was triaged for), `TopologyEdge`, `PossibilityTopologyConfig`,
  `PossibilityTopology` with `relation -> src -> dst` forward and reverse
  indexes, `successors()` / `predecessors()` / `add_edge()` / `note_transition()`
  / `stats()` / `reset()`. Deterministic ordering (strongest edge, then
  observation count, then key) because the consumer takes a prefix of the list.
  `default_registry()` registers **only** `enables`; `requires` and `is_part_of`
  are deliberately NOT pre-registered.
- **Write path:** `AnchorSet.write_anchor` calls `note_transition()` on an
  observed family remap, provenance `anchor_remap_succession`. No similarity
  computation anywhere -- the event is the remap itself. MECH-094 holds by
  construction (`write_anchor` is reached only from
  `HippocampalModule.tick_anchor_set` on the waking path).
  `AnchorSet.reset()` clears the topology when `reset_with_anchor_set` is True
  (the default), because `segment_id` counters are recycled per episode and
  retained edges would alias.
- **Read path:** `GhostGoalBank.rank()` ->
  `_admit_relational_successors()`; the `goal_match_floor` is **waived** for a
  relational admit (that is the point), the MECH-340 persistence license is
  **not** (a relation is not a reason to override a global disengagement gate).
  Caps: `max_successors_per_parent` (2), `max_relational_admits` (8).
  `GhostGoalBankEntry.relation_provenance` is set only on relationally-admitted
  entries.
- **No-op default:** `PossibilityTopologyConfig.enabled` defaults False and a
  topology is constructed only when asked for. With none attached (the default
  everywhere), `AnchorSet` and `GhostGoalBank` take literally the pre-SD-097 code
  paths -- no extra keys, no extra dict allocations. **SD-098 depends on that OFF
  path staying bit-identical.**
- **SD-098 constraint honoured:** there is **no stored node-type field** (no
  goal / subgoal / possibility tag on a node). A stored node type is precisely
  SD-098's comparison arm, and SD-098's read-time falsifier is being queued
  concurrently. Relational admission keys on the PARENT's read-time
  `goal_match` and on the edge; the successor's own nature is never consulted.
  **This constraint binds every future stage in this document too.**

### Config wiring -- CLOSED 2026-09-17 (`ree-v3` `eabecb2`)

This section recorded an open debt when first written, a few hours before it was
discharged; it is kept as the resolved record rather than deleted, because the
form the fix took is architecturally load-bearing for every later stage.

**The debt.** `HippocampalConfig.use_possibility_topology` did not exist --
`ree_core/utils/config.py` was held by a concurrent session at build time, so
`HippocampalModule.__init__` resolved the flag through `getattr(..., False)` and
the block was inert, reachable only via the interim
`HippocampalModule.attach_possibility_topology()`.

**How it was closed, and why NOT as a nested config object.** The obvious fix --
a `possibility_topology_config: PossibilityTopologyConfig` field mirroring
`ghost_goal_bank_config` -- is **impossible**: `possibility_topology` imports
`AnchorKey` from `anchor_set`, which imports `config`, so a nested field would
close a circular import. `eabecb2` therefore lands **FIVE FLAT SCALARS** on
`HippocampalConfig` and has `HippocampalModule` assemble the dataclass itself:

| knob | default |
|---|---|
| `use_possibility_topology` | `False` |
| `possibility_topology_seed_relation` | `"enables"` |
| `possibility_topology_relation_weight` | `0.5` |
| `possibility_topology_max_successors_per_parent` | `2` |
| `possibility_topology_max_relational_admits` | `8` |
| `possibility_topology_write_on_anchor_remap` | `True` |

threaded through `REEConfig.from_dims` (config.py:8147-8150, :9699-9701).

**Consequence for later stages -- read this before adding a second relation.**
The import cycle is a property of the node primitive, not of this one relation:
any relation keyed on `AnchorKey` inherits it. So **stage 2 and stage 3 knobs
must also be flat scalars on `HippocampalConfig`**, not a growing nested config
object, and a stage that wants structured per-relation configuration has to
solve the cycle first (or accept a flat namespace per relation). Do not
"tidy" the flat knobs into a nested field later; it will not import.

**Contract coverage** (`ree-v3/tests/contracts/test_sd_097_possibility_topology.py`,
18 tests, 30 passed on `ree-worker-4` with the MECH-293 neighbour): O1-O4 pin the
OFF path including disabled-with-edges **bit-identity** -- the property SD-098's
live falsifier reads; W1/W2 pin the flat-knob construction and the
`use_anchor_sets` precondition raise; S1 pins that **no stored node-type field**
exists anywhere, which is SD-098's comparison arm; R1 pins that `requires` and
`is_part_of` are reachable with one `register_relation()` call and no schema
change.

The stage-2b falsifier's configuration prerequisite is therefore **met**.

---

## substrate_queue.json write-back (REPORTED, not applied)

This session does not write `evidence/planning/substrate_queue.json` --
governance tooling and a `governance.sh` scope lock touch that tree. The
recommended edits to the `SD-097` entry:

```json
{
  "design_doc": "docs/architecture/sd_097_possibility_topology.md",
  "node_class": "complicated (buildable)",
  "status_phase": "build_in_progress",
  "depends_on_unresolved": [],
  "implementation_hint": "NARROWED by the design doc from 8 relation types to 3 distinct ones (enables [BUILT 2026-09-17], provides_information_about [next], conflicts_with [third]); requires collapses to a read direction, prevents is probe-gated, is_part_of/substitutes_for/may_become_useful_under_context collapse into existing structure. Stage 2 (provides_information_about -> MECH-482 epistemic-deficit routing) is the prerequisite for the falsifier: a single-relation topology cannot separate ARM 1 from ARM 2."
}
```

`depends_on_unresolved` should be emptied: all eight depends_on claims have
landed substrate (GFLAG-0331), and the entry's own `origin` field records that
the list was copied verbatim and never classified.

## node_class recommendation

**Keep `complicated (buildable)` for the entry as a whole, and record a
`complex (probe-gated)` sub-node for two relations.** The split, in the
project's debt vocabulary
(`docs/architecture/work_graph_debt_vocabulary.md`):

- **`complicated (buildable)`** -- the generic store, `enables` (done),
  `provides_information_about`, `conflicts_with`, the `requires` read direction,
  the config knob, and the three-arm falsifier. Every one of these is buildable
  on demand: the consumer exists, the write event is observable, the work is
  known.
- **`complex (probe-gated)`** -- `prevents`, and `requires` in its *necessity*
  (rather than reverse-index) sense. Both need **negative evidence** -- a
  non-occurrence or extinction observation -- and whether the anchor stream can
  supply it at usable density is an open empirical question, not a build task.

  **The probe (a REE diagnostic, ~1 session):** over live episodes with anchors
  on, measure (i) whether family remaps carry any signal separating succession
  from displacement, and (ii) the density of anchor-family co-occurrence counts,
  against the null needed to assert "B never followed A".
  - Counts are dense enough -> resolves to **`puzzle (known rules)`**: the
    missing item is a threshold/estimator choice, and the build proceeds.
  - Counts are structurally absent -> resolves to **`mystery (known data)`**:
    the anchor stream does not carry negative evidence at all, and the answer is
    to **reframe** (a different node primitive, or drop these two relations),
    not to gather more data.

Preferring the probe-gated sub-node over simply queueing `prevents` as more
execution backlog is deliberate: only the reducible unknown converts effort into
information.

---

## Validation

**Stage 1 (built):** contract tests owned by the build session, including the
relation-registry extensibility contract (a new relation is registerable with one
`register_relation()` call and no change to the store, the edge dataclass, or any
query) and the OFF-path bit-identity contract SD-098 depends on.

**Stage 2b (the falsifier) -- not yet queued.** Three arms as specified above,
queued via `/queue-experiment` once stage 2 and the config knob land. It is
CONFIRMED on the `what_would_answer` conjunction -- discovery of a
non-parent/subgoal-related possibility, retention at sub-goal salience without
action, later retrieval and action after a context shift, AND an ARM 1 > ARM 2
separation that ARM 2 can close only by adding a per-edge discriminator -- and
FALSIFIED if ARM 3's scalar reproduces the behaviour across the dynamism sweep.

**Recorded in advance, because it is the most likely outcome and should not be
allowed to look like a surprise:** the discovery leg may well go to ARM 3 at low
dynamism. K&G's result predicts it. That would falsify the discovery leg only,
and the retention leg -- which ARM 3 cannot attempt at all -- would still stand
or fall on ARM 1 vs ARM 2.
