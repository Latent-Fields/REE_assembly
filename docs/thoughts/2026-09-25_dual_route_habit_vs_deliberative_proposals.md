Status: processed
Intake: evidence/planning/thought_intake_2026-09-25_dual_route_habit_vs_deliberative_proposals.md
Registration pending: one candidate MECH drafted in the intake (section 6); claims.yaml was owned by another session at intake time -- /governance registers it from the intake's paste-ready block.

# Two proposal routes: one for habits, one for more complex behavioural additions

**Date:** 2026-09-25
**Origin:** live user remark in session orchestrate-20260924-breakthrough (coupled loop-repair campaign), captured verbatim by the orchestrator and routed to thought-intake worker bt0925-dualroute.

## Context

The orchestrator had explained that the coupled loop-repair campaign builds two proposal mechanisms, run head-to-head in A1:

- **Action-space proposals (ASP, row W1-alt):** a parameter-free search directly over the 5 one-hot environment moves (stratified one-hot first action plus per-class categorical CEM on the continuation). Landed on `integration/coupled-loop-repair` at ree-v3 `1a16595`.
- **Abstract action-object codec (row W1):** an encoder objective for `e2.action_object_head`, a tied `action_object_decoder`, and CEM in action-object space. Being built now.

## The user's words (verbatim)

Earlier in the session:

> "I hope the abstract space one wins. It seems more cognition like."

Then, on hearing the two mechanisms described side by side:

> "It seems a bit like both exist in my mind. One for habits and one for more complex behavioural additions"

## The orchestrator's gloss (to be checked against literature, not assumed)

Habitual control (dorsolateral striatum) runs over a small set of primitive, well-learned actions. It is cheap and close to motor output. Goal-directed control (dorsomedial striatum and PFC) runs over abstract action and outcome representations, which supports composition, chunking and novel combination. The two run concurrently and are arbitrated. With practice, behaviours migrate from goal-directed to habitual control. REE already has SD-081's dual-system split: the habit read at `dualsystem_habit_depth`, the planned read at a greater depth. Proposed mapping: ASP is the habit-route proposer (primitives, shallow); the codec is the deliberative-route proposer (structured, state-dependent, composable, planned depth).
