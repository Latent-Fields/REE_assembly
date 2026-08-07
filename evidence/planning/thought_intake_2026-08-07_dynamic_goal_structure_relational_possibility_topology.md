# Thought Intake: Dynamic goal structure and relational possibility topology

**Date:** 2026-08-07
**Status:** Stage 2 structured analysis; no new claim IDs registered in this pass.
**Raw thought file:** `docs/thoughts/2026-08-07_dynamic_goal_structure_relational_possibility_topology.md`
**Origin:** User, developed in conversation and then reconciled against the existing REE architecture.
**Provenance rule:** Direct user quotations are primary evidence. Conceptual synthesis, literature comparison, repository reconciliation, and naming are secondary interpretation unless explicitly attributed otherwise.

---

## 1. Verbatim primary thought evidence

> “When pursuing a goal often something else is noticed. This creates a subgoal which itself must be completed before the overarching goal is completed. Or it may create or reveal a separate goal which the previously overarching goal is revealed as a subgoal of. Or indeed it may mark a goal which is somewhat orthogonal to the current goal and subgoal stack which may be useful to return to later when less is on one’s plate.”

The user then made the hippocampal/topological connection explicit:

> “And topology is something that the hippocampus is good at holding. Meanwhile there probably needs to be a level underneath which potential goals identified are not worth much attention though could still be part of the topology”

These quotations establish the historical core of the thought. The broader formulation below arose through subsequent dialogue and repository comparison and should not be treated as though it existed fully formed in the initial wording.

## 2. Core idea

Goal-directed action need not occur within a goal hierarchy that is fully known in advance. During pursuit, experience can reveal new relations in the structure of possible action:

1. **Downward discovery:** a newly encountered state is a prerequisite or subgoal that must be completed before the current goal can be completed.
2. **Upward discovery:** the current goal is revealed to be instrumental to, or a component of, a previously unrepresented superordinate goal.
3. **Lateral discovery:** an orthogonal possibility is recognised as potentially useful or valuable but does not deserve to interrupt current pursuit; it can be retained for later.

The important distinction is between **selecting a trajectory within a represented possibility space** and **revising the structure of that possibility space through action**.

This suggests that a fixed goal stack or tree is too restrictive as the fundamental representation. The active goal hierarchy may instead be a temporary, context-sensitive executive projection from a richer relational structure.

## 3. Possibility before goal

A represented possibility need not already be a goal. A useful conceptual ordering is:

`represented possibility -> significance -> goal candidacy -> active consideration -> intention -> commitment -> trajectory`

These need not become discrete implementation stages, but they should not be conceptually collapsed.

**possibility ≠ desirability ≠ goal candidacy ≠ intention ≠ commitment**

This distinction allows an agent to retain considerably more structure than it can actively deliberate over. Something noticed incidentally can remain represented at low executive weight without receiving sustained attention, forward simulation, or behavioural control.

The user’s “level underneath which potential goals identified are not worth much attention” is therefore better interpreted as **selective activation over retained structure**, not necessarily deletion below a single importance threshold.

## 4. Context-sensitive relevance

A possibility that is unimportant now may become highly relevant after a change in need, knowledge, commitment, environment, or available resources. The working secondary formulation is that current context imposes a **relevance field** over the larger stored topology.

That relevance should probably not be reduced to one scalar. Existing REE signals could jointly influence activation, including expected benefit, predicted harm, urgency, uncertainty, information value, effort, attainability, progress, existing commitment, recoverability, and contextual fit.

The architectural problem may therefore be primarily one of representation, retrieval, and integration rather than the addition of a separate “goal importance” module.

## 5. What is already represented in REE

A focused repository pass found substantial prior architecture adjacent to the thought. This constrains what should be treated as new.

| Existing REE element | Existing function relevant here | Relationship to this thought |
|---|---|---|
| `SD-004` | Action objects form the hippocampal map backbone; hippocampal proposal generation navigates a compressed world-effect/action-object space. | Strong existing support for a relational/path topology; do not claim hippocampal relational planning as new. |
| `SD-039` | Stores goal snapshots and associated metadata in dual-trace hippocampal anchors. | Existing persistence of goal-associated content outside the immediate goal state. |
| `MECH-292` | Ranked ghost-goal bank over stored hippocampal anchor traces. | Existing mechanism for retaining and ranking formerly goal-relevant possibilities. |
| `MECH-293` | Waking hippocampal probe search seeded by ghost goals. | Existing route by which inactive goal-associated traces can re-enter planning. |
| `MECH-189` | Persistent, cue-indexed super-ordinal goal memory across episodes. | REE already represents persistent superordinate goal structure; “superordinate goals” alone are not the new claim. |
| `SD-092`, `MECH-427`, `MECH-428` | Explicit parent↔subgoal relation and cross-level credit; subgoal attainment can reinforce or bootstrap a parent. | REE already has hierarchical parent/subgoal structure and upward credit propagation. |
| `SD-093`, `MECH-426` | Progress-velocity modulation of effort and persistence. | Existing machinery relevant to whether an active goal remains worth pursuing. |
| Commitment / control-plane mechanisms | Protect, release, and interrupt ongoing trajectories under defined conditions. | Existing machinery can potentially prevent every newly salient possibility from capturing behaviour. |
| E3 | Candidate trajectory evaluation and selection. | Remains the natural locus for selection; the hippocampal system need not become an executive value chooser. |

Therefore this intake should **not** be framed as discovering a need for hierarchical goals, persistent inactive goals, superordinate goals, parent/subgoal credit, or hippocampal reactivation of old goals. Those are already present to varying degrees.

## 6. Apparent novel remainder

The apparent extension is broader:

> **Parent/subgoal relations may be only one relation within a more general learned topology of possibilities, and goal hierarchy itself may be discovered and revised through action.**

The proposed topology would not contain only goals. It could contain represented possibilities and learned relations such as:

- requires;
- enables;
- is part of;
- prevents;
- conflicts with;
- substitutes for;
- provides information about;
- may become useful under another context.

Some represented possibilities may carry motivational significance. Others may encode only that something is possible or related to something else. Their place in the topology can be retained without elevating them to active goals.

The active goal/subgoal structure would then be a **temporary executive projection** of the subset currently relevant enough to guide deliberation and commitment.

## 7. Proposed division of labour

A provisional architectural interpretation is:

- **Hippocampal/path-memory substrate:** preserve and retrieve relational possibility structure and propose traversals through it.
- **Goal/relevance machinery:** determine which represented possibilities acquire sufficient current significance for goal candidacy or renewed retrieval.
- **E3:** evaluate and select candidate trajectories.
- **Commitment/control plane:** protect ongoing pursuit from inappropriate capture and release it when warranted.
- **Learning/replay:** revise relational structure and its contextual associations over time.

The hippocampal analogue should therefore not itself determine what ought to control behaviour. Its proposed extension is representational and generative: preserve topology and make relevant structure available.

## 8. Key formulation

A provisional formulation emerging from the discussion is:

> **Goal pursuit is simultaneously traversal of, and learning about, the relational structure of possible action.**

While acting toward a goal, the agent may discover prerequisites below it, purposes above it, alternatives beside it, conflicts with other commitments, or possibilities that are currently insignificant but may later become useful.

The agent therefore learns not only routes to already-known goals, but also how possible actions and purposes relate to one another.

In this view, the active goal/subgoal hierarchy is not necessarily the fundamental representation. It is a **temporary, context-sensitive executive projection from a larger learned topology of possibilities**.

## 9. Epistemic significance

This extends REE’s epistemic humility beyond uncertainty about which route best reaches a known goal. A viable agent may also need to remain uncertain about:

- whether it has understood the goal correctly;
- what the goal depends on;
- whether the goal is part of something broader;
- whether another represented possibility has become relevant;
- whether the relationships among its current purposes are themselves incomplete or mistaken.

Action thus becomes one of the mechanisms by which the organisation of purpose is discovered and corrected.

## 10. Affected existing claims / mechanisms

The most immediate architectural interfaces are `SD-004`, `SD-039`, `MECH-292`, `MECH-293`, `MECH-189`, `SD-092`, `MECH-427`, `MECH-428`, `SD-093`, and `MECH-426`, together with E3 and the commitment/control-plane family.

No existing claim is edited or reinterpreted by this intake. The point of the repository reconciliation is to avoid duplicate claims and identify the narrower residual question that remains genuinely open.

## 11. Candidate claim-shaped ideas — not registered in this pass

No new claim IDs are created here. The following are prose-level candidates for later digestion and literature review:

1. **General relational possibility topology:** REE may require a representation in which parent/subgoal is one relation among a wider family of learned relations between possible states/actions/purposes.
2. **Context-dependent promotion:** represented possibilities may persist below active goal status and become candidates for pursuit when contextual relevance changes, without requiring rediscovery.
3. **Topology revision during action:** goal pursuit may modify the represented topology upward, downward, and laterally rather than merely choosing a route through a fixed hierarchy.

These may turn out to be one architectural claim, several mechanisms, or an interpretation of existing hippocampal/goal machinery. Registration should wait for dedicated comparison against the literature and a concrete discriminative design.

## 12. Open questions / critique targets

- What qualifies a newly perceived state, affordance, or relation for durable representation?
- Which relation types must be explicit, and which can emerge from learned geometry?
- How should low-relevance possibilities decay, consolidate, or be pruned?
- What causes a previously quiet possibility to return to active consideration?
- How are mistaken upward interpretations (“this goal serves H”) revised?
- How are conflicting or mutually exclusive structures represented?
- Can the existing anchor/ghost-goal machinery be generalised without conflating formerly valued goals with merely represented possibilities?
- Is `SD-092` the beginning of the general topology, or should it remain a specialised parent/subgoal consumer of a broader substrate?
- How much belongs in hippocampal geometry versus explicit GoalState structure?
- How can the proposal be falsified without merely implementing a symbolic graph planner and calling it hippocampal?

## 13. Next steps

1. Conduct a dedicated literature pull spanning hippocampal/entorhinal relational maps and cognitive maps, goal reasoning and intention reconsideration, hierarchical and opportunistic planning, affordances, and hierarchical reinforcement learning/subgoal discovery.
2. Determine whether a general relational substrate can reuse `SD-004`/anchor machinery or requires an explicit extension.
3. Specify discriminative tests that distinguish a revisable possibility topology from a fixed hierarchical goal tree plus ordinary replanning.
4. Only after those steps, decide whether the residual idea warrants one or more formal claim registrations.

## 14. Provenance note

The historical sequence matters.

The thought did **not** begin as the phrase “relational possibility topology.” It began with the user’s observation that pursuing one goal can reveal (a) a necessary subgoal, (b) a superordinate goal within which the present goal becomes subordinate, or (c) an orthogonal possible goal worth retaining for later.

The user then explicitly added the hippocampal/topological connection and the requirement that low-priority potential goals remain represented without necessarily receiving much attention.

The broader notions of possibility-before-goal, context-sensitive relevance, temporary executive projection, and a general relational possibility topology were developed through subsequent dialogue and repository reconciliation.

Future archaeology should therefore preserve the distinction between:

- **primary conceptual evidence:** the verbatim user quotations in section 1;
- **dialogue-assisted elaboration:** the topology/relevance/executive-projection synthesis;
- **repository-derived reconciliation:** the identification of existing REE mechanisms and isolation of the apparent novel remainder.
