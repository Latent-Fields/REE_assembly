# Frontal Goal Grounding — Synthesis

Lit-pull commissioned 2026-04-28 to settle a V3/V4 architectural question raised in conversation: do prefrontal goal-encoding subdivisions (vmPFC, dlPFC, lateral OFC, dACC) consume rich associative goal representations resident in posterior/temporal cortex via top-down query/retrieval, or do they hold compact "goal-handle" representations decoded into action only at downstream sites?

Five entries pulled, all PubMed-indexed. The verdict is decisively **both** — and the resolution is that the answer is **directional and phase-dependent**, not a single architecture.

## The four entries that settle the directionality

According to PubMed:

| Paper | Finding | Direction |
|---|---|---|
| Spellman et al. 2015 *Nature* [DOI 10.1038/nature14445](https://doi.org/10.1038/nature14445) | vCA1 → mPFC required for cue ENCODING, not maintenance or retrieval; gamma-coherent | HPC → PFC, encoding-only |
| Ito et al. 2015 *Nature* [DOI 10.1038/nature14396](https://doi.org/10.1038/nature14396) | mPFC → reuniens → CA1 required for trajectory-dependent CA1 firing; CA3 (no reuniens input) shows no trajectory coding | PFC → HPC, goal-directed retrieval |
| Schmitt et al. 2017 *Nature* [DOI 10.1038/nature22073](https://doi.org/10.1038/nature22073) | Mediodorsal thalamus does NOT relay rule content; it amplifies local PFC connectivity to sustain rule-specific sequences | PFC-local content with thalamic gain |
| Hallock et al. 2016 *J Neurosci* [DOI 10.1523/JNEUROSCI.0991-16.2016](https://doi.org/10.1523/JNEUROSCI.0991-16.2016) | Reuniens inactivation selectively abolishes SWM-specific HPC-PFC synchrony; bidirectional task-conditional gate | Demand-conditional thalamic routing |

## The fifth entry that pins down the rich-content reading

Baram et al. 2020 *Neuron* [DOI 10.1016/j.neuron.2020.11.024](https://doi.org/10.1016/j.neuron.2020.11.024). vmPFC and entorhinal cortex preserve representational geometry across surface-different RL problems if and only if task structure is preserved. vmPFC carries a **rich abstract structural representation** — not a compact handle — but the rich content is the *task-graph topology*, not "the goal as a feature vector."

## Primary verdict

**The compact-handle vs rich-readout question is malformed as a binary.** The biological architecture is:

1. **Encoding events** (Spellman 2015): rich content flows HPC → PFC. New goal cues are written into PFC representations using rich hippocampal associative content during gamma-synchronous windows. This is the closest match to the user's "frontal reads richer associative store" intuition.

2. **Goal-directed retrieval / trajectory generation** (Ito 2015): compact handle flows PFC → reuniens → HPC. PFC has cached the goal context; reuniens routes that compact handle to CA1; CA1 then constructs the rich trajectory representation under PFC top-down bias.

3. **Maintenance** (Schmitt 2017): PFC representations are properly local-to-PFC compact codes, but their persistence requires external thalamic amplification gain (MD for rules; reuniens for goal trajectories).

4. **Demand-conditional gating** (Hallock 2016): thalamic routing is opened/closed by cognitive demand. The HPC ↔ PFC interface is not always-on.

5. **Abstract structural encoding** (Baram 2020): vmPFC and EC additionally carry generalisable graph-structure representations that preserve across surface-different problems. The rich content vmPFC carries is the task-graph itself — vmPFC IS the rich store for structural-relational information, not a reader of an external rich store.

So the answer to the user's question — should SD-033a/b consume an E1-keyed readout, or stay on compact-handle inputs? — is: **stay on compact handles for the routine path, and consider an event-gated rich-write at goal-instantiation moments.** The rich associative store the user was reaching for is not E1; it is the hippocampal anchor pool (already in REE) plus a structural-graph encoding capacity (not yet in REE).

## Architectural recommendations for REE

### Pursued or partially pursued in V3

- **PFC → HPC compact-handle routing** (Ito 2015 mapping): already implemented as `GoalState.z_goal → HippocampalModule.propose_trajectories`, refined by MECH-293 ghost-goal probes that bias the proposer toward anchors whose `z_goal_snapshot` cosine-matches `current z_goal`. This is functionally close to what reuniens does biologically. **No refactor required.**

- **Demand-conditional gating** (Hallock 2016 mapping): partially captured by `SalienceCoordinator.write_gate("sd_033a"/"sd_033b")` which gates when frontal substrates update. The biology has the gate at a *thalamic* node (reuniens) on the HPC ↔ PFC interface specifically, not on each consumer. REE's per-consumer gating is a coarse functional substitute and is probably good enough for V3.

### Worth scoping for V4

- **Event-gated rich-write at goal-instantiation moments** (Spellman 2015 mapping): when a new goal is encoded — i.e. when `GoalState` transitions from inactive to active, or when `z_goal` changes substantially — REE should perform a high-bandwidth one-shot transfer of LatentStack content into the frontal-resident representations. SD-033a `rule_state` and SD-033b `state_code` currently update via slow EMA gated by write_gate. The biology suggests an additional **fast-write event** at goal-creation (analogous to Spellman's gamma-synchronous encoding window). MECH-288 boundary events on the slow scale (z_goal regime change via BOCPD) are already firing at the right moments — the missing piece is a frontal write hook on those events.

- **Abstract task-structure encoding in vmPFC analogue** (Baram 2020 mapping): ARC-035 / SD-033c currently does not encode a generalisable graph-structural representation. The MECH-292 anchor pool has the geometry to support it (each anchor is a node, anchor pairs define structural relations), but no current substrate compresses the anchor pool into a structural code that preserves across different specific goals with the same structural shape. This is a V4 extension when REE handles richer environments where structural generalisation actually pays off.

- **Explicit thalamic-routing substrate** (Schmitt 2017 + Hallock 2016 + Ito 2015 combined): a dedicated MD/reuniens-analogue node where "PFC sends compact handle, thalamus gates and amplifies, HPC/PFC receives" is explicit. Currently abstracted into the GoalState → HippocampalModule call chain; making it explicit would be a new SD covering frontal-thalamo-hippocampal routing. Whether worth doing depends on whether V3 dynamics suffer from its absence — the EXQ-490 / EXQ-490b factorial on V_s gating is a more pressing path before this becomes architecturally load-bearing.

### Not warranted

- **Refactor SD-033a/b to consume E1-keyed readouts.** The biological rich-content store on the HPC ↔ PFC axis is not the sensory predictor — it is hippocampal CA1 (anchored, residue-shaped) and entorhinal cortex (structural-graph). E1 in REE is the sensory deep predictor; mapping it to the HPC/EC role would be a category mistake. The user's intuition that "E1 holds rich associations the frontal systems should read" is correct in spirit but wrong in target — the rich store is hippocampal, and the existing SD-039/MECH-292/MECH-293 substrate is already the right architectural layer.

## Net aggregate

Mean confidence 0.80 across five entries (range 0.74-0.85). Convergent on the directional/phase-dependent reading; divergent enough on which subdivision does what to make it clear that monolithic "PFC consumes X" or "PFC holds Y" claims are over-strong. The user's architectural framing was on the right track but pointed at the wrong rich store; the biology says the rich store is hippocampal anchors + EC structural graph, which REE already has substrates for (MECH-292, MECH-269). The architectural extensions worth scoping are (1) event-gated frontal writes at goal-instantiation moments, and (2) V4 vmPFC structural-graph encoding capacity. Both are flagged for governance review, neither is V3-blocking.
