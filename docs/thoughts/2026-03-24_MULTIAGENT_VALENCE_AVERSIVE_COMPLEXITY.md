Status: processed

Processed in:
- MECH-135 (claims.yaml): e1.goal_context_conditioning -- E1 LSTM conditioning on z_goal_latent
- MECH-136 (claims.yaml): coherence.relational_harm -- harm-to-agent vs harm-to-agency (v4)
- MECH-137 (claims.yaml): curiosity.agent_novelty_typing -- world-state vs agent-policy novelty (v4)

Source: Design conversation, 2026-03-24 (Claude Code session)
Triggered by: analysis of axiom coverage gaps (INV-028, INV-029) and question of how
positive valence control plane signals interact with aversive gradient in multiagent world.

Related thought: 2026-03-24_empathy_multiagent_ethics.md (counterfactual empathic activation,
nth-order ethics problem -- distinct topic, complementary)

---

## 1. The Core Observation

Once positive valence control plane signals are in place (liking, wanting, curiosity/novelty,
goal-feedback E1<->E3), the aversive gradient changes character in a multiagent world. The
interaction effects are non-linear and require careful staged testing.

In a single-agent world:
  - Harm signal comes from the environment
  - Approach (wanting) and avoidance (harm) pull in mostly orthogonal directions
  - Curiosity/novelty signal rewards exploration of novel states

In a multiagent world:
  - The same other agent triggers MULTIPLE control plane axes simultaneously
  - Harm becomes relational -- what counts as harm depends on the other agent's goals
  - Curiosity creates chronic approach pressure toward the most unpredictable entity
  - The axes that were developed independently now compete on the same target

---

## 2. Single Other Agent: Simultaneous Multi-Axis Pull

A single other agent can simultaneously generate:

| Signal | Direction | Why the other agent triggers it |
|--------|-----------|--------------------------------|
| Wanting (MECH-112/116) | Approach | Source of connection / INV-029 benefit gradient |
| Curiosity / novelty (MECH-111) | Approach | Partially unpredictable agent = perpetual novelty |
| Goal-instrumental | Approach | Their behavior may be useful to your goal |
| Harm aversion (SD-010) | Avoidance | Their trajectory may conflict with yours |
| Residue curvature | Avoidance | Prior bad interaction leaves harm geometry |
| Mirror model (INV-005) | Complex | Their harm state activates your harm signal |

Before the positive valence signals exist, only the bottom two rows are active -- the agent is
a pure collision avoider. Once wanting, curiosity, and goal-feedback are in place, the same
other agent activates contradictory drives simultaneously. The aversive gradient doesn't get
"more complex" -- its meaning changes.

---

## 3. Harm Becomes Relational

In a single-agent world, harm is localised: contact with a hazard → harm signal. The residue
field records it, trajectory selection steers away.

In a multiagent world with goal representations, harm is relational:

  Whether your goal-pursuit constitutes harm to another agent depends on:
  - What their goal is (and whether yours obstructs it)
  - Whether they consented to the interaction
  - The social context and history
  - Whether the harm is to them directly vs to their goal-pursuit

The current harm architecture (SD-010 harm_bridge, E3 harm evaluation) does not distinguish
these cases. It produces a harm signal when the environment signals harm -- it cannot represent
"I harmed their agency by pursuing my goal" as distinct from "I harmed them physically."

This is a structural gap for multiagent testing: without other-agent goal modelling (identified
as a gap in the axiom coverage analysis), the harm signal in a multiagent setting will be
systematically incomplete. Collision avoidance will register; agency interference will not.

---

## 4. Curiosity/Novelty Contamination Risk

The curiosity/novelty signal (MECH-111) rewards approach toward high-information states.
Other agents are perpetually partially unpredictable -- their behavior is not fully determined
by observable state. This means:

  In a multiagent world, other agents are always among the highest-novelty targets.

Without a mechanism that distinguishes "interesting unfamiliar stimulus" from "unpredictable
agent whose next action may be harmful," the curiosity signal could:
  (a) Chronically pull toward the most dangerous entity in the environment
  (b) Compete with harm avoidance in a way that produces oscillatory approach-avoidance
  (c) Be trivially satisfied by adversarial agents that maintain surface unpredictability

This does not mean curiosity is wrong -- it means the novelty reward needs to be typed:
novelty about the world-state (safe to approach) vs novelty about another agent's policy
(requires social modelling before approach is safe). Currently no mechanism makes this
distinction.

---

## 5. Missing Architectural Piece: E1 <-> E3 Goal-Feedback Loop

MECH-112 notes (claims.yaml): "E1's LSTM hidden state serves as working memory substrate
for goal representation when conditioned on z_goal_latent."

This is a key architectural mechanism -- the frontal goal latent conditioning E1's recurrent
state so that goal context propagates into the predictive machinery, not just into the
trajectory evaluator. But there is no standalone mechanism claim for this bidirectional loop.

Current state:
  - MECH-112: goal latent z_goal as structured attractor (candidate, V3 pending)
  - MECH-116/117: wanting/liking dissociation (candidate)
  - ARC-030: D1/D2 commit threshold balance (candidate)
  - The E1<->E3 feedback loop: mentioned in MECH-112 notes, not a standalone claim

The loop matters because:
  - Without it, goal context only reaches E3 (trajectory evaluation)
  - E1's predictions remain goal-agnostic -- the world model doesn't "know" what you're
    trying to achieve, so it can't generate goal-relevant predictions
  - For multiagent interaction, E1 needs to predict how other agents' behavior relates to
    your goal -- impossible without goal conditioning in the prediction layer

Flag as candidate claim: MECH-1xx (e1_goal_conditioning) -- E1 LSTM hidden state is
conditioned on z_goal_latent such that predictive trajectories generated by E1 are
goal-context-shaped, not goal-agnostic.

---

## 6. Staged Dependency Chain Before Multiagent Testing is Valid

Testing multiagent approach-avoidance interaction effects requires building up in order:

  Level 0: SD-005 z_self/z_world split                    [done, V3 PASS]
            SD-010 harm_bridge                             [V3, EXQ-093/094 running]
       |
  Level 1: MECH-112 z_goal wanting signal                 [V3 pending, EXQ-091 running]
            MECH-111 curiosity / novelty                  [candidate]
            MECH-116/117 wanting/liking dissociation      [candidate]
       |
  Level 2: E1 <-> E3 goal-feedback conditioning          [not yet a standalone claim]
            Single-agent approach-avoidance balance       [gated by Level 1]
            INV-033 second-order self-monitoring wired    [gap]
       |
  Level 3: Other-agent goal modelling                    [structural gap -- no claim]
            Harm-to-agency vs harm-to-agent distinction  [no mechanism]
            Novelty typing (world novelty vs agent novelty) [no mechanism]
       |
  Level 4: Multiagent experiment design                  [V4 or late V3]
            Valid multiagent ethics testing

Level 3 is a hard prerequisite. Multiagent experiments run before Level 3 mechanisms exist
will test collision avoidance, not ethics. The results will look like ethical behavior
(no harm events) while missing the relational harm dimension entirely.

---

## 7. Implications for Test Design (When Level 3 is Reached)

When the time comes, multiagent experiments will need:

(a) Staged environment complexity
    - Start: shared goal, non-competitive, no trajectory conflicts
    - Then: misaligned goals, competitive resource access
    - Then: conflicting goals where helping one agent requires cost to another
    - Finally: adversarial agents that exploit novelty-seeking

(b) Isolation of mechanism contributions
    - Ablations across wanting / liking / curiosity independently
    - Separate harm-to-agent vs harm-to-agency metrics
    - Measure whether E1 predictions are goal-conditioned (not just E3 evaluation)

(c) Qualitative success criteria
    - Not just "no harm events" -- harm avoidance alone passes that
    - Must distinguish: cooperation / support / conflict navigation / principled refusal
    - The ethical quality of interaction should be measurable, not just harm count

(d) Adversarial coverage
    - Agent that presents as high novelty while being harmful
    - Agent that exploits approach drives (connection, curiosity) to extract cooperation
      that serves their goal at cost to yours

---

## 8. Claims Touched

### Existing claims supported / context

- INV-028 (others as co-inhabitants): this analysis deepens the gap -- harm-to-agency
  requires other-agent goal modelling, not covered by mirror harm alone
- INV-029 (love / approach drive): ARC-030 / MECH-112/116/117 are necessary preconditions
  before any of this can be tested
- MECH-111 (curiosity): curiosity typing problem identified -- novelty about world vs agent
- MECH-112 (z_goal): E1<->E3 feedback loop is mentioned but not claimed
- MECH-125 (multiconstraint viability): in multiagent world, the constraint spaces interact
  with another agent's constraint evaluation -- not currently represented

### New candidate claims to flag

(A) MECH-1xx: E1 goal-conditioning (e1.goal_context_conditioning)
    "E1's LSTM hidden state is conditioned on z_goal_latent such that predictive
    trajectories generated by E1 are goal-context-shaped. Without this, E3 evaluates
    trajectories in a goal-conditioned way while E1 generates them goal-agnostically --
    a type mismatch in the prediction-evaluation pipeline."
    Depends on: MECH-112, ARC-003, SD-005
    Implementation phase: v3 (prerequisite for goal-informed multiagent prediction)

(B) MECH-1xx: Relational harm definition (coherence.relational_harm)
    "In a multiagent world, harm must be defined relationally: harm-to-agent (direct
    physical/cost signal) and harm-to-agency (obstruction of another agent's goal-pursuit)
    are distinct signal types requiring distinct representations. The current harm_bridge
    (SD-010) captures only harm-to-agent."
    Depends on: INV-028, INV-005, MECH-112, SD-010
    Implementation phase: v4 (requires other-agent goal modelling at Level 3)

(C) MECH-1xx: Novelty typing (curiosity.agent_novelty_typing)
    "Curiosity-driven approach must distinguish world-state novelty from agent-policy
    novelty. Untyped novelty reward creates chronic approach pressure toward partially
    unpredictable agents regardless of harm risk."
    Depends on: MECH-111, INV-028, MECH-095
    Implementation phase: v4

---

## 9. Processing Targets (when processed)

- docs/claims/claims.yaml: register MECH-1xx (E1 goal-conditioning) as candidate, v3
- docs/claims/claims.yaml: register MECH-1xx (relational harm) as candidate, v4
- docs/claims/claims.yaml: register MECH-1xx (novelty typing) as candidate, v4
- docs/architecture/e1.md (if exists): add note on goal-conditioning interface gap
- evidence/planning/: add multiagent experiment design staging as a planning note
  (not for immediate queuing -- Level 3 prerequisites are not yet met)
