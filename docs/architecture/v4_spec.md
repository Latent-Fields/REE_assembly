# V4 Spec (initial deliberate spec, 2026-05-02)

> Initial spec-first phase for V4. Captures the substrate primitives V4
> needs to support, the claims that wait for them, and the migration
> shape from V3. Not a substrate implementation -- this is the planning
> artifact that should precede V4 substrate work.

## Purpose

Phase 3 wave 2 of the Option E lit/exp decoupling exposed a specific
sub-cohort of claims that cannot be tested with any reasonable V3
enrichment, even with the substrate roadmap (`substrate_roadmap.md`)
fully landed. These claims need a substrate generation that V3 cannot
incrementally become. V4 is that substrate.

The companion document for V3-tractable enrichment is
`docs/architecture/substrate_roadmap.md`. That document handles the
substrate features V3 *can* incrementally absorb. This document is for
the residue: what V3 cannot become.

For a map of the surrounding V4 planning documents, see
`docs/architecture/v4_planning_index.md`.

## V4 prerequisites (from V3)

V4 entry is gated on V3 completion. The current V3 completion gates
(per ree-v3/CLAUDE.md):

1. **First-paper gate**: SD-012 + EXQ-182a oracle + goal-lift
   experiment. Demonstrates goal representations are real and influence
   behavior. *SD-012 promoted to provisional 2026-05-02.*

2. **Full completion gate**: hippocampal multi-step trajectory planning
   validated (MECH-163 VTA/planned system). Required because V4 social
   extension requires planning trajectories that affect another agent's
   z_harm_a and benefit_exposure over time -- structurally inaccessible
   to 1-step greedy.

V3-EXQ-495 is the queued experiment for MECH-163 (per WORKSPACE_STATE
2026-04-30 entries). Until it lands, V4 substrate work should remain
spec-only.

## V4 scope (the five primitive additions)

### V4-0. Object/entity permanence and affordance schemas

The substrate must represent objects as persistent entities whose identity,
location, affordances, and causal powers survive partial observation,
occlusion, carrying, placement, and delayed re-encounter. V3 resources,
hazards, landmarks, and reef cells are useful task features, but they are not
yet entity slots with stable identity and intervention-derived affordance
bundles.

This is the bridge between the V3 single-agent world model and V4 social
ecology. Other agents are a special, harder case of persistent entity: they
have object permanence plus policy, welfare, body state, and goal dynamics.
V4 should not start multi-agent work until ordinary entity permanence is
measurable.

**Claims unblocked:**
- `ARC-059` scientist-agent developmental ordering cluster.
- `MECH-275` sleep-phase aggregation for stable schema formation.
- `MECH-276` scientist-agent principle / interventional closure.
- `MECH-277` action-space discovery.
- `MECH-278` object-schema formation via experimental action.
- V4-1 multi-agent ecology, because other-agent modelling presupposes
  persistent entity slots.

**Implementation surface:** the reserved harness is
`docs/architecture/v4_developmental_harness_spec.md`. It specifies a
MiniGrid-style object-affordance ladder: carry, push, place, use,
affordance bundles, confounder isolation, and sleep-aggregation ablation.
The likely implementation surface is a V4-reserved environment/harness first,
then the REEAgent changes needed to bind persistent entity slots into
`z_world`, hippocampal anchors, and E1 schemas.

**Open design questions:**
- Whether entity slots are explicit objects in the observation pipeline,
  hippocampal anchors, E1 schema memory, or a coordinated view across all
  three.
- How identity survives occlusion and carried-object transformations without
  hand-engineering the answer into `z_world`.
- Which affordance predictions are learned from passive observation versus
  experimental action.
- How sleep aggregation stabilises object schemas without overwriting
  episode-specific evidence.
- How entity permanence becomes agent permanence when the entity has its own
  action policy and affective state.

### V4-1. Multi-agent ecology

The substrate must represent more than one agent and the causal
interactions between them. Each agent has its own `z_self` /
`z_harm_a` / drive state / commitment chain. Agents perceive each
other through the same observation pipeline (potentially with
self-other distinguishability cues, depending on V4-2).

**Claims unblocked:**
- `Q-028` (`substrate_ceiling`) ethics.axiom_conflict_resolution --
  preserving self vs preserving other requires there to be an other
- `Q-029` (`substrate_ceiling`) ethics.loneliness_as_harm -- loneliness
  is unshared suffering; needs other agents to share or fail to share
  with
- `MECH-102` (`substrate_ceiling`) violence-as-terminal-error-correction
  -- the "all other channels fail" framing requires multiple coping
  channels which in social context include negotiation, withdrawal,
  cooperation, etc.
- `MECH-095` (`substrate_ceiling`) -- agency detection becomes more
  tractable when "other" is structurally distinct from "environment"
- `INV-064` self-model integration sub-claims that depend on
  representing other selves

**Implementation surface:** new env class
`MultiAgentCausalGridWorldV4` (or similar). Each agent has its own
REEAgent instance; the env arbitrates concurrent actions, computes
inter-agent observations, handles collisions / cooperative state
changes. Substantial -- this is a new substrate generation, not a V3
extension.

**Open design questions:**
- Synchronous vs asynchronous agent ticks
- How agents perceive each other (full state? body-state only?)
- Communication primitive (shared signal channel? action-as-signal?)
- Cooperative state changes (joint resource consumption? joint hazard?)

### V4-2. Self-model integration (DR-10..DR-14 from ree-v3 CLAUDE.md)

Five architectural gaps already enumerated in ree-v3/CLAUDE.md "V4
scope (self-model integration)":

- **DR-10:** z_self in E3 trajectory scoring. score_trajectory()
  currently evaluates entirely in z_world space; bodily state must
  modulate viability.
- **DR-11:** z_self-domain goal representation. z_goal currently lives
  in z_world; self-state goals (energy restoration, pain avoidance)
  cannot be represented.
- **DR-12:** E2 prediction error -> E3 confidence modulation. E3
  trusts E2 unconditionally; PE-magnitude must signal trajectory
  unreliability.
- **DR-13:** z_self temporal depth. Current z_self is single hidden
  layer + EMA; needs recurrence or E1 feedback for temporal self-model.
- **DR-14:** Environment must dissociate proxy from hedonic content.
  CausalGridWorldV2 conflates location with reward; MECH-214 addiction
  failure mode is structurally invisible.

**Claims unblocked:**
- `MECH-214` goal-referent E1-representability (by DR-11)
- `MECH-215` self-model prerequisite for agentive prediction
  (by DR-10 + DR-12)
- `INV-064` (overall maturational sequence)

**Implementation surface:** changes to E3.score_trajectory, GoalState,
E2 forward-PE wiring, z_self encoder; env-side: SD-022-style
body-state extension generalised. Some of this is V3-tractable (DR-12
is partly addressable in V3), but the cohort coheres around the V4
self-model.

### V4-3. Long-horizon dynamics + persistent identity

Episodes that span thousands of agent-substrate cycles, with
identity / memory / damage state persisting across what V3 calls
"episode boundaries." Shifts from "an agent in a single episode" to
"an agent across a lifetime."

**Claims unblocked:**
- `INV-049` waking-vs-offline necessity at full timescale
- Chronic phenomena (sensitisation, allostasis, sleep debt
  accumulation): SD-037 orexin override sustained dynamics, MECH-260
  bias-suppression long-horizon
- `MECH-214` developmental sequence (the maturational architecture
  needs longitudinal data, not single-episode probes)

This overlaps the substrate_roadmap.md "Long-horizon regime" item;
the V3-side fix is calibration + sleep aggregation + checkpointing
the existing substrate. V4 generalisation: persistent agent identity
across what was previously a hard reset boundary.

**Implementation surface:** REEAgent.reset() distinguishes episode
boundary vs lifetime boundary; substrate flags for persistent state.

### V4-4. Richer action repertoire (V3-lite extension also possible)

V3 has 4 cardinal moves + noop = 5 actions. V4 needs structurally
distinct action *modes* that capture meaningful coping channels:

- **Movement** (current 4 cardinal + noop)
- **Communication-analog** (signal-emission to other agents)
- **Manipulation-analog** (effecting non-locomotion change in
  environment)
- **Withdrawal-analog** (committed disengagement, distinct from noop)

Some of this is V3-tractable (substrate_roadmap.md item #5 is the
V3-lite version: extend action space without requiring multi-agent).
The V4 version requires multi-agent context for the
communication-analog to make sense.

**Claims unblocked:**
- `MECH-102` full ethical-channels framing (V4 version vs V3-lite from
  the roadmap)
- `MECH-099` agency attribution under richer action causation
- Several of the ethics axiom claims (INV-028 / INV-029) where
  intervention modes matter

## V4-bound claim cohort summary

From the Phase 3 wave 2 walk and prior surveys:

| claim | epistemic_category | V4 primitive needed |
|---|---|---|
| ARC-059 | (V4-roadmap) | V4-0 developmental ordering / object-schema harness |
| MECH-275 | (V4-roadmap) | V4-0 object-schema sleep aggregation |
| MECH-276 | (V4-roadmap) | V4-0 interventional closure |
| MECH-277 | (V4-roadmap) | V4-0 action-space discovery |
| MECH-278 | (V4-roadmap) | V4-0 object-schema formation via experimental action |
| Q-028 | substrate_ceiling | V4-1 multi-agent |
| Q-029 | substrate_ceiling | V4-1 multi-agent |
| Q-038 | substrate_conditional | V4-2 (ARC-053/055 substrate, related) |
| Q-039 | substrate_conditional | V4-2 (ARC-053/055 substrate, related) |
| MECH-095 | substrate_ceiling | V4-1 multi-source / V4-4 richer ecology (V4-lite plausible) |
| MECH-102 | substrate_ceiling | V4-1 multi-agent + V4-4 channels |
| MECH-099 | (untagged, similar) | V4-1 + V4-4 |
| MECH-214 | (V4-roadmap) | V4-2 self-model |
| MECH-215 | (V4-roadmap) | V4-2 self-model |
| INV-064 | (V4-roadmap) | V4-2 + V4-3 longitudinal |
| ARC-031 | (V4-roadmap) | V4-2 z_self navigation |
| MECH-118 / MECH-119 | (V4-roadmap, gated on Q-022) | V4-2 self-model |

About 17 claims explicitly wait for V4 substrate or its developmental
harness.

## What V4 is NOT for

To keep scope honest:

- **Out-of-domain claims** (Q-031, Q-032 pharmacology) are not V4-
  bound. No substrate at any level helps them. These belong as
  `research_anchor` / `literature_synthesis` claim types if/when those
  are added.
- **Derivational claims** (Q-025, Q-026, partly Q-027) are not V4-
  bound. They want axiom-system work, not substrate.
- **V3-tractable enrichments** (substrate_roadmap.md items 1-7)
  belong in V3. Don't roll them into V4 just because V4 is also a
  larger substrate.

## Migration shape (sketch)

V4 substrate is additive; V3 substrate continues to exist for V3
claims. Sketch:

1. Build `MultiAgentCausalGridWorldV4` as a new env class. Inherits
   nothing from V3 substrate; allowed to be its own ecology. Before the
   multi-agent version, build the V4-0 object/entity permanence harness
   so persistent entities and affordance schemas are validated in the
   single-agent case.
2. REEAgent extension: factor out the per-agent state so a single env
   instance can own N REEAgent instances each with their own state.
3. New experiment-script template for V4 (multi-agent loops aren't
   compatible with the V3 single-agent template).
4. Indexer + governance: V4 evidence carries a distinct
   `architecture_epoch` (e.g. `ree_multi_agent_v1` parallel to V3's
   `ree_hybrid_guardrails_v1`). Existing epoch machinery handles this.
5. Migration of self-model integration (DR-10..DR-14): some changes
   (DR-12 PE-confidence) can land in V3 first; others (DR-11 z_goal
   self-domain) wait for V4-1 multi-agent context.

## Process gating

V4 spec work proceeds in phases:

- **Phase A (this document):** spec-first. Write down what V4 needs.
- **Phase B0 (can be specified before V3 closes):** object/entity
  permanence harness freeze. Implementation remains V4-reserved unless
  governance explicitly authorises a V3-scale L0/L1 probe.
- **Phase B (gated on V3 completion):** substrate prototyping.
  `MultiAgentCausalGridWorldV4` first, then per-agent REEAgent factor.
- **Phase C:** V4-1 contract tests, claim-cohort migration.
- **Phase D:** V4-2 self-model integration; DR-10..DR-14 enacted.
- **Phase E:** V4-3 long-horizon work.
- **Phase F:** V4-4 richer action repertoire (lite version may
  precede in V3 per substrate_roadmap.md item 5).

Proceeding past Phase A requires:
- V3 full completion gate cleared (MECH-163 PASS)
- A claim explicitly authorising V4 substrate work (governance
  decision)

## Status

**Phase A draft, 2026-05-02.** No substrate work has started. This is
the deliberate spec-first artifact preceding V4 substrate decisions.
