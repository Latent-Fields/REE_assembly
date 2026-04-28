📄 REE Thought Intake

Title: Action-Policy Decomposition and Multi-Goal Parallel Maintenance

⸻

Provenance

Conversation thread 2026-04-28, follow-on to the type-prototype thought (`2026-04-28_action_object_type_abstraction.md`). After the type-prototype lit-pull settled, Daniel raised two further architectural questions: (a) "I bet nature has landed on a decomposition of [action representation] into very useful separate things" — yes-please-pull; and (b) when reviewing the type-V_s recommendation, "would this help when multiple goals are being held in place and would each goal-to-action workstream need its own set of hippocampal lookups?"

The first question was settled by the action-policy lit-pull (`evidence/literature/targeted_review_action_policy_decomposition/synthesis.md`). The second is captured here as architectural reasoning that the lit-pulls did not directly address.

⸻

Core Claim (action policy)

Biology has decomposed action representation into at minimum five separable levels with overlapping but functionally distinct substrates: motor primitives → action chunks → model-free habits → model-based goal-directed → hierarchical options. REE V3 covers level 4 well (planner: E2 + CEM + HippocampalModule + MECH-292/293), level 5 partially (SD-004 action-object decoder, continuous not indexable), and is missing levels 2 and 3 entirely.

Core Claim (multi-goal)

REE V3's `GoalState` is a singleton. Multi-goal parallel maintenance — the ability to hold competing goals simultaneously and arbitrate between them tick-by-tick — requires a substrate change: a multi-slot GoalState plus per-goal hippocampal lookup sets (one MECH-292 rank per slot, one MECH-293 probe budget per slot, parallel proposer trajectories, dACC-style arbitration). This connects directly to V3's monostrategy lock-in and to OCD-style over-binding pathology.

⸻

The action decomposition (what the lit-pull settled)

| # | Level | Substrate | Operator | Role | REE V3 |
|---|---|---|---|---|---|
| 1 | Motor primitives | Spinal cord + motor cortex | Force-field combination | Continuous limb output | Not needed (4 discrete actions) |
| 2 | Action chunks | Dorsolateral striatum | Phasic gate + cached sequence | Run well-learned routines as units | **MISSING** |
| 3 | Model-free habits | DLS + cortico-striatal loops | Cached state-action values | Fast retrospective selection | **MISSING** |
| 4 | Model-based goal-directed | PFC + DMS + HPC | Forward simulation | Flexible prospective planning | Covered (E2+E3+HPC+MECH-292/293) |
| 5 | Hierarchical options | Lateral + orbital PFC | Initiation + termination + policy | Compose temporally extended subroutines | Partial (action_object decoder is continuous, not a discrete library) |

Dolan & Dayan 2013 add the meta-constraint: levels 2-4 are not cleanly separated subsystems but a *spectrum* with shared circuitry and rich interactions. Architecturally that means any habit substrate added to REE should integrate *with* the existing planner, not as a parallel competing system.

⸻

The multi-goal architecture (raised in conversation, not directly settled by lit-pulls)

REE V3's current state:
- `GoalState` holds a single `z_goal`.
- `HippocampalModule.propose_trajectories(current_z_goal=...)` accepts one goal.
- MECH-292 ranks anchors by `goal_match(current_z_goal)` against that single z_goal.
- MECH-293 seeds ghost probes from that single z_goal.

Multi-goal parallel maintenance would need:
- **Multi-slot GoalState** — a small set of active goal slots (n=2-4 plausibly), each with its own `z_goal`, drive coupling, age, persistence parameters.
- **Per-slot MECH-292 ranking** — one ghost-bank rank per active goal, since `goal_match` is goal-specific.
- **Per-slot MECH-293 probe budget** — divide the proposer's exploration budget across active goals (with weighting by salience, drive, recency, etc.).
- **Parallel proposer trajectories** — each active goal generates its own candidate trajectories at proposal time.
- **dACC-style arbitration** — a tick-by-tick selector that picks which active goal's best trajectory wins this commitment cycle, governed by something like the Daw 2005 uncertainty-based arbitrator extended to multi-option selection.

This connects to:

- **MECH-269 monostrategy lock**: if the agent only ever holds one z_goal, behavioural strategy is structurally constrained to that goal's optimal path. Single-goal architecture is itself a contributor to mono-policy behavior.
- **OCD over-binding** (the ocd4 thought file): inability to release a current goal (washing) to maintain a competing goal (going to work) is a multi-goal-arbitration failure. Multi-slot GoalState with per-slot persistence/release dynamics is the substrate where over-binding pathology would live. SD-033 + SD-034 + MECH-266 already provide partial OCD machinery on the goal-release side; what's missing on that axis is the multi-slot side (without slots, there's nothing to release *to*).
- **MECH-266 asymmetric mode hysteresis**: currently mode-conditional (external_task vs internal_planning vs internal_replay etc.). Multi-goal would need per-goal hysteresis as a parallel dimension.

⸻

Falsifiable signatures (if substrates were added)

Action chunk substrate (level 2-3): in repeated-route foraging tasks, post-training trajectories should show shorter planning latency than first-exposure trajectories of the same trajectory length. Without a chunk substrate, planning latency stays flat across training (every tick rolls through CEM regardless of repetition). With a chunk substrate, planning latency drops on cached trajectories.

Multi-slot GoalState: in a dual-resource task where the agent must alternate between two distinct resource patches with different routes, single-slot architecture forces sequential goal-switching with full re-planning each switch. Multi-slot architecture maintains both goal representations and exhibits faster between-switch latency plus better between-switch route stability.

⸻

Cross-references

- Action-policy lit-pull: `evidence/literature/targeted_review_action_policy_decomposition/synthesis.md`
- Type-prototype lit-pull (precursor): `evidence/literature/targeted_review_hpc_type_prototype_substrate/synthesis.md`
- Frontal goal grounding lit-pull (predecessor): `evidence/literature/targeted_review_frontal_goal_grounding/synthesis.md`
- ocd4 thought file: `docs/thoughts/2026-04-20_ocd4.md` — over-binding-to-goal pathology framing.
- Type-prototype thought file: `docs/thoughts/2026-04-28_action_object_type_abstraction.md` — the precursor architectural conversation.

⸻

Architectural recommendation summary

Highest priority architectural extension: **action-chunk / habit cache substrate**, landing in the dorsolateral-loop slot of ARC-021. Connects to OCD modelling (Graybiel 2008 runaway-chunking failure mode), potential V3 monostrategy debugging contributor, and computational efficiency in V4. Default V4-scope, with pull-forward to late-V3 if EXQ-495 successors surface specific gaps that the existing planner-only architecture cannot express.

Second priority: **multi-slot GoalState** with per-goal hippocampal workstream. Default V4-scope, with pull-forward to V3 if monostrategy escape requires it (currently the most architecturally plausible pull-forward candidate given that V3 already debugs monostrategy actively).

Definitively V4-scope (no V3 pull-forward path):
- Type-encoder + prototype-readout operator + type-V_s extension (from type-prototype pull)
- Option library (Botvinick 2009)
- Thalamic-routing substrate (reuniens/MD analogue)
- vmPFC abstract task-structure encoding (Baram 2020)
- Motor-primitive substrate (continuous control only)
- Event-gated frontal write at goal-instantiation (Spellman 2015 hook)

⸻

Next steps

1. Register the candidate substrates as new SD/MECH claims with appropriate `implementation_phase` (v4 default; v3-conditional-pull-forward where flagged) so they enter the governance pipeline as candidates.
2. Hold pending V4 environment design for everything except the two pull-forward candidates (action-chunk cache, multi-slot GoalState).
3. Re-evaluate after EXQ-495 V3-full-completion-gate result lands — if monostrategy persists despite ghost-goal probes and V_s gating, that is the trigger to pull the action-chunk cache and/or multi-slot GoalState forward.
