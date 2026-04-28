# Theta Packaging Scales with Substrate Abstraction — Synthesis

Lit-pull commissioned 2026-04-28, fourth in the chain (after frontal_goal_grounding, hpc_type_prototype_substrate, action_policy_decomposition). Tests Daniel's architectural prediction: as the abstraction-substrate stack deepens (chunks, types, options), the unit of content packaged into a hippocampal theta cycle should scale with the agent's current substrate vocabulary.

Five entries, all PubMed-indexed. Mean confidence 0.84 (range 0.82-0.88).

## Entries

According to PubMed:

| Paper | Finding | Sub-question |
|---|---|---|
| Gupta et al. 2012 *Nat Neurosci* [DOI 10.1038/nn.3138](https://doi.org/10.1038/nn.3138) | Theta sequences segment experience into chunks; sequence length scales with running speed and theta cycle length / gamma count | (a) — adaptive packaging mechanism, direct |
| Gupta et al. 2010 *Neuron* [DOI 10.1016/j.neuron.2010.01.034](https://doi.org/10.1016/j.neuron.2010.01.034) | Replay constructs novel-path sequences; reflects available cognitive map, not literal experience | (d) — compositional / generative replay |
| Karlsson & Frank 2009 *Nat Neurosci* [DOI 10.1038/nn.2344](https://doi.org/10.1038/nn.2344) | Awake replay reactivates remote (non-current-environment) experiences as commonly as local; brief quiescent pauses are when this surfaces | (b) — waking vs sleep theta functional comparison |
| Bellmund et al. 2018 *Science* [DOI 10.1126/science.aat6766](https://doi.org/10.1126/science.aat6766) | Place / grid cell representational format generalises across non-spatial cognitive dimensions and hierarchical levels; theta sequences simulate trajectories through whatever cognitive space is active | (c) — multi-domain cognitive map framework |
| Carr, Karlsson & Frank 2012 *Neuron* [DOI 10.1016/j.neuron.2012.06.014](https://doi.org/10.1016/j.neuron.2012.06.014) | Slow gamma (20-50 Hz) synchrony coordinates CA3-CA1 during SWR replay; higher synchrony predicts higher replay quality | (e) — gamma as coordination clock |

## Primary verdict

### (i) Does theta packaging scale with substrate abstraction in the biology?

**Yes, with mechanism.** The Gupta 2012 finding is the load-bearing piece: theta sequence length is *adaptive* — it scales with running speed and acceleration, with theta cycle length, and with the number of gamma cycles within each theta cycle. The packaging mechanism is `theta cycle × gamma count = path length / number of items per packet`.

Generalised: the unit of content is whatever the cognitive-map machinery is currently navigating. When the map is spatial and the agent is running, units are spatial path segments. Bellmund 2018 grounds the architectural extension: the same theta-sequence machinery can navigate non-spatial cognitive maps (conceptual, social, task-graph, hierarchical-abstract). When REE adds chunk / type / option substrates, the cognitive map gains chunk-nodes, type-instance-nodes, and option-edges; theta sequences traverse those at the appropriate granularity without requiring new packaging machinery.

The mechanism is in place. The gap in the literature: a direct longitudinal demonstration that the packaging unit *changes* after the agent acquires a chunked behavioural skill. This would be the experiment we'd run to validate the prediction at the biological level. It exists in pieces (Frank lab hierarchical-task replay) but the clean version isn't yet a single canonical paper.

### (ii) Is sleep theta functionally distinct from waking theta in carrying higher-abstraction content?

**Less than the user's intuition predicted.** Karlsson & Frank 2009 directly weakens the simple "sleep = abstract, waking = concrete" reading. *Both* states reactivate stored representations including remote (non-current-environment) trajectories. The functional difference is contextual (sensory input present vs absent) and oscillatory (theta in REM has different statistics from awake theta), not categorical (different content domains).

Awake replay during brief quiescent pauses is when remote / non-current content surfaces. Sleep extends the reactivation but does not gate it. This converges with the Hennies 2017 / Schapiro 2016 findings from the type-prototype lit-pull: sleep enhances abstraction extraction but waking learning is sufficient for at least some forms of compositional / regularity-based abstraction.

Architectural inference for REE: do not gate the prototype-readout operator (MECH-296) or any new abstraction-scaling theta operator to sleep only. The substrate machinery that runs during sleep replay (MECH-272 routing gate, MECH-285 priority-weighted sampler) should also run during waking quiescent moments — possibly with different routing weights, but not gated off entirely.

### (iii) What new MECH(s) should be registered to capture this for REE?

Three candidates emerge cleanly from the synthesis:

1. **MECH-NNN: theta_cycle_content_scales_with_substrate_vocabulary** — refinement of MECH-089. The unit of content packaged into a theta cycle is the smallest reusable abstraction available in the agent's current substrate vocabulary. Atomic actions when only those exist; chunks when SD-045 is implemented; type-instance matches when SD-040/MECH-296 are implemented; option invocations when SD-042 is implemented. Mechanism: theta cycle × gamma count = number-of-vocabulary-units per E3 tick. Anchored on Gupta 2012 (adaptive packaging) plus Bellmund 2018 (multi-domain generalisation).

2. **MECH-NNN+1: cognitive_map_traversal_via_theta_at_active_abstraction_level** — sister claim. The cognitive map being traversed by theta sequences is the substrate vocabulary's currently-active level. Theta sequences don't have a fixed semantic content; they simulate trajectories through whatever map the substrate vocabulary defines. Anchored on Bellmund 2018 (cognitive maps for human thinking) plus Constantinescu 2016 (already in REE's lit index, conceptual grids).

3. **MECH-NNN+2: waking_replay_runs_during_quiescent_pauses** — refinement / generalisation of MECH-285. The priority-weighted anchor sampling that MECH-285 currently runs during sleep should also run during brief waking quiescent pauses, surfacing remote / non-current content for goal-directed retrieval. The gating is contextual (quiescent vs active behaviour, sensory input vs absence), not state-categorical (waking vs sleep). Anchored on Karlsson & Frank 2009 (awake remote replay) plus Gupta 2010 (compositional replay).

A fourth candidate — gamma-coordination-quality scales with content abstraction (Carr 2012 extension) — is plausible but not directly demonstrated by Carr 2012, which only establishes the coordination mechanism. Defer until empirical evidence accumulates.

### Scope

All three MECH candidates are V4 by default. None requires V3 implementation work because:

- MECH-089 / MECH-294 already specify the theta-gamma packaging primitive in V3.
- MECH-285 already runs priority-weighted anchor sampling in V3 (during sleep only).
- The substrate-vocabulary scaling is V4-conditional on at least one of {SD-045 action chunks, SD-040 type encoder, SD-042 option library} landing first — none of which are V3 implementations.

V3 PULL-FORWARD CONDITION applies to MECH-NNN+2 (waking quiescent replay): if EXQ-495 successors surface a need for more aggressive ghost-goal probe access during waking pauses than the current MECH-293 architecture provides, this is the lightest-touch extension to pull forward. Lifting the sleep-only gate on MECH-285 is implementation-cheap; the architectural commitment is what needs registration.

## Architectural recommendation summary

Register three new MECH claims as V4-default candidates:

| ID (provisional) | Title | Phase | Pull-forward |
|---|---|---|---|
| MECH-NNN | theta_cycle_content_scales_with_substrate_vocabulary | v4 | No (gated on SD-045 / SD-040 / SD-042 landing) |
| MECH-NNN+1 | cognitive_map_traversal_via_theta_at_active_abstraction_level | v4 | No (sister claim, same gating) |
| MECH-NNN+2 | waking_replay_runs_during_quiescent_pauses | v4 | Yes if EXQ-495 successors surface need |

Two of the three are V4-firm (gated on substrate availability that is itself V4). One is V3-conditional pull-forward and is the lightest touch — extending MECH-285 invocation to waking quiescent moments rather than gating to sleep only.

## Net aggregate

Mean confidence 0.84 across five entries. Verdict: Daniel's architectural prediction is biologically well-founded. Theta packaging is adaptive; the cognitive map machinery generalises across information domains and hierarchical levels; the same theta-sequence machinery navigates whatever map the substrate vocabulary currently defines. The user's intuition that sleep theta carries "higher-abstraction content" specifically is partly weakened — both waking and sleep replay reactivate stored content; sleep is enhancement, not gate.

The architectural shape this licenses: extend MECH-089 with substrate-scaling refinement (MECH-NNN), add a sister claim about cognitive-map traversal at active abstraction level (MECH-NNN+1), and lift the sleep-only gate on MECH-285 / add an explicit waking-quiescence claim (MECH-NNN+2). All V4-default; one V3-conditional pull-forward candidate. None V3-blocking.

This synthesis closes the four-pull chain begun 2026-04-28: frontal_goal_grounding → hpc_type_prototype_substrate → action_policy_decomposition → theta_abstraction_scaling. Total: 20 lit entries across the chain, 13 candidate claims registered (10 from pulls 1-3 already, 3 more proposed here for harvest).
