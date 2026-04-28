# Action-Policy Decomposition Substrates — Synthesis

Lit-pull commissioned 2026-04-28. Daniel's intuition: "I bet nature has landed on a decomposition of this idea into very useful separate things." The pull tested that intuition and asked which biological levels REE V3 covers vs. is missing.

Five entries, all PubMed-indexed.

## Entries

According to PubMed:

| Paper | Decomposition level | Substrate |
|---|---|---|
| Mussa-Ivaldi & Bizzi 2000 *Phil Trans R Soc B* [DOI 10.1098/rstb.2000.0733](https://doi.org/10.1098/rstb.2000.0733) | Motor primitives (lowest) | Spinal cord force-field modules + motor cortex |
| Graybiel 2008 *Annu Rev Neurosci* [DOI 10.1146/annurev.neuro.29.051605.112851](https://doi.org/10.1146/annurev.neuro.29.051605.112851) | Action chunks / habits | Basal ganglia, dorsolateral striatum (task-bracketing cells) |
| Daw, Niv & Dayan 2005 *Nat Neurosci* [DOI 10.1038/nn1560](https://doi.org/10.1038/nn1560) | Model-based goal-directed vs model-free habit | PFC + dorsomedial striatum (model-based); dorsolateral striatum (model-free) |
| Botvinick, Niv & Barto 2009 *Cognition* [DOI 10.1016/j.cognition.2008.08.011](https://doi.org/10.1016/j.cognition.2008.08.011) | Hierarchical options (subroutines) | Dorsolateral + orbital PFC |
| Dolan & Dayan 2013 *Neuron* [DOI 10.1016/j.neuron.2013.09.007](https://doi.org/10.1016/j.neuron.2013.09.007) | Goals/habits as a spectrum, not a discrete dichotomy | Shared cortico-striatal circuitry with rich interactions |

Mean confidence 0.82 (range 0.78-0.85).

## Primary verdict — the canonical biological decomposition

Daniel's intuition is correct. The biological decomposition is **at minimum five levels**, with substrates that overlap in circuitry but differ in functional role:

| # | Level | Substrate | Operator | Role |
|---|---|---|---|---|
| 1 | **Motor primitives** | Spinal cord modules + motor cortex | Force-field combination | Generate continuous limb output from compact commands |
| 2 | **Action chunks** | Dorsolateral striatum (task-bracketing) | Phasic gate + run cached sequence | Execute well-learned multi-step routines as units |
| 3 | **Model-free habits** | Dorsolateral striatum + cortico-striatal loops | Cached state-action values | Fast retrospective action selection without rollout |
| 4 | **Model-based goal-directed** | PFC + dorsomedial striatum + HPC | Forward simulation through internal model | Flexible prospective planning under novel conditions |
| 5 | **Hierarchical options** | Dorsolateral + orbital PFC | Initiation set + termination function + internal policy | Compose temporally extended subroutines for skilled multi-step behaviour |

Dolan & Dayan 2013 add an important meta-constraint: the levels above are *not cleanly separated subsystems*. They share circuitry, interact richly, and may be better understood as parametric variations on a shared substrate than as fully independent controllers.

## Mapping REE V3 onto the five levels

| Level | REE V3 component | Coverage |
|---|---|---|
| 1. Motor primitives | None | Not needed (4 discrete grid actions; no continuous control) |
| 2. Action chunks | None | **MISSING** — no cached action-sequence substrate |
| 3. Model-free habits | None | **MISSING** — no state-action value cache |
| 4. Model-based goal-directed | E2 transition model + E3 CEM proposer + HippocampalModule.propose_trajectories + MECH-292 / MECH-293 | Covered |
| 5. Hierarchical options | SD-004 action_object decoder (continuous, not discrete library) | **PARTIAL** — has the shape but not the indexability |

REE V3 covers level 4 well and level 5 partially. It is missing levels 2 and 3 entirely. Level 1 is environmentally not relevant in V3.

## Architectural verdict

### What's biologically real and currently missing

**A habit / action-chunk substrate is the architecturally load-bearing missing piece.** It would land within ARC-021's three-loop framework, in the dorsolateral-loop slot. The substrate would be:

- A small dictionary of cached action sequences indexed by (state-signature, expected-outcome-signature)
- Each entry executable as a unit without re-rolling through E2 + CEM
- Updated by reinforcement from MECH-290 backward credit sweep on completed committed trajectories
- Gated by task-bracketing-analogue signals that mark chunk start and end

This is the substrate where Daniel's two architectural concerns converge:

1. **OCD-style automaticity / runaway chunking** (Graybiel 2008): without a habit cache, REE cannot model the failure mode where action chunks become rigid and self-reinforcing.
2. **Monostrategy lock-in** (current V3 issue): some part of monostrategy may be a missing-habit-cache issue, not just a goal-substrate issue. With no habit cache, every action goes through model-based planning, which means the planner's monostrategy bias is the *only* contributor to behavioural rigidity. Adding a habit cache might *worsen* monostrategy if the cache reinforces successful trajectories, or might *improve* it by off-loading repetition from the planner and freeing cognitive resources for strategy exploration.

**SD-vs-MECH for the habit substrate:** SD. New encoder + new storage + new operator = new substrate. Pattern matches SD-016, SD-039.

### What's biologically real but not currently load-bearing

**An option library** (Botvinick 2009 framework) is the next-most-architecturally-significant missing level. It would be a discrete codebook of named options (initiation set + termination function + internal policy), distinct from SD-004's continuous action_object decoder.

But: at V3 episode lengths (200-500 steps) and 4-action granularity, options provide limited additional capacity over the existing CEM proposer. The option substrate becomes load-bearing in V4 when the environment supports tools, social coordination, hierarchical task structure. **Defer to V4 unless V3 needs surface a specific use case.**

### What's NOT warranted

**A motor-primitive substrate** below SD-004. V3's discrete action space doesn't need it. V4 if and when REE moves to continuous control.

### Architectural pattern from Dolan & Dayan 2013

The canonical reading is now spectrum-with-shared-circuitry, not two-discrete-systems. Implication for REE: the habit substrate, when added, should integrate *with* the existing planner — e.g., as a cached lookup that `HippocampalModule.propose_trajectories` queries *before* falling through to CEM rollout — rather than as a parallel competitor. ARC-021's three-loop framework is well-positioned for this; the habit substrate fills the dorsolateral-loop slot within the existing scaffold.

## Recommended substrate plan

Based on the five-level decomposition and REE V3's coverage map:

| Priority | Proposed substrate | Type | Justification | When |
|---|---|---|---|---|
| 1 | **Habit / action-chunk cache** (provisional SD-N) | SD | OCD modelling; potential monostrategy contributor; Graybiel substrate; clear architectural slot in ARC-021 dorsolateral loop | Late-V3 if monostrategy escape requires; V4 by default |
| 2 | **Option library** (provisional SD-N+1) | SD | Hierarchical action composition; richer ghost-probe seeding; frontopolar / lateral PFC substrate | V4 — gridworld too simple to validate |
| 3 | Motor primitives | SD | Continuous control | V4 environment-only; not before |

A new MECH cluster would accompany each SD: chunk-extraction-from-experience operator (MECH-N), chunk-retrieval-by-state-match operator (MECH-N+1), credit-update operator (MECH-N+2). Sleep involvement at the chunk level is empirically supported (Walker & Stickgold motor-skill consolidation literature; not pulled here but a candidate follow-up if the SD lands).

## Net aggregate

Mean confidence 0.82 across five entries. Verdict: Daniel's intuition is correct — biology has decomposed action representation into ~5 separable levels, REE V3 covers two of them well (level 4 fully, level 5 partially) and is missing two (levels 2 and 3) with a clear architectural slot for each. Level 1 is environmentally not needed.

The single highest-priority architectural extension is a **habit / action-chunk substrate (SD)** sitting in the dorsolateral-loop slot of ARC-021, integrating with the existing planner rather than competing with it. This connects to OCD modelling, V3 monostrategy debugging, and computational efficiency in V4. The option library and motor primitives are V4-deferred.

None of this is V3-blocking. The substrate plan above is V4-default with V3-conditional pull-forward if EXQ-495 successors surface specific gaps that the existing planner-only architecture cannot express.
