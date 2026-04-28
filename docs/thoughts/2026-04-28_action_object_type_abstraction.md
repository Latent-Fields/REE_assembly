📄 REE Thought Intake

Title: Action Primitives, Object Types, and Sleep-Driven Type Abstraction

⸻

Provenance

Conversation thread 2026-04-28. Daniel raised the architectural question after we finished the frontal_goal_grounding lit-pull (`evidence/literature/targeted_review_frontal_goal_grounding/`). The frontal-goal pull resolved that PFC consumes goal information through a phase-dependent compact-handle path (Ito 2015 PFC→reuniens→HPC) plus an event-gated rich-write at encoding (Spellman 2015 HPC→PFC) plus a structural-graph encoding capacity in vmPFC/EC (Baram 2020). That answered the original "should SD-033a/b read an E1-keyed readout?" question (no — biological rich store is hippocampal anchors + EC structural graph, not the sensory predictor).

Daniel's follow-on, captured here:

> Part of sleep would be identifying primitives of action types (are these policies?) and ensuring broad recombination of simulated consequences in different places and goal-seekings or harm-avoidances improves the general representation of the action space or policies for encoding in hippocampus. The hippocampus appears to hold very high level representations of many things which can be used to call up significant sets of representations that can be filtered by verisimilitude to identify the currently observed version of the universal principle for that object or action type. The specifics of the type and the buckets differentiating objects and actions need representation just like the reuniens for trajectories of objects and the effects of action.

⸻

Core Claim

REE V3 has substrates for the trajectory / location side of hippocampal function (residue field, anchor set, ghost-goal bank, per-region V_s) but lacks substrates for the type / category side (concept-cell-analogue prototypes, action-policy library, sleep operator that extracts types from compositional recombination). The biology supports this as a separable architectural layer; REE collapses it into the encoder + anchor-mixture key.

⸻

Minimal Form

Anchors are *where you've been*. Types are *what you've been a particular instance of*. REE has the first; the second is implicit at best.

⸻

What's biologically well-supported

1. **Sleep does compositional recombination → abstraction.** Lewis & Durrant 2011 (overlapping replay extracts rules); Schapiro et al. 2017 (sleep extracts statistical regularities); Liu et al. 2019 (non-spatial replay generalises structure in human MEG); Stickgold & Walker 2013 (gist extraction).

2. **Hippocampus encodes high-level concept types.** Quiroga 2005 concept cells (Jennifer Aniston neurons — multimodal, abstract, instance-invariant); Schapiro 2013 (HPC learns temporal community structure); Constantinescu et al. 2016 (grid-cell-like organisation in *conceptual* space); Theves et al. 2019; Bellmund 2018 (cognitive-map generalisation).

3. **Action primitives / options are real**, but distributed across BG (procedural cache), SMA / pre-SMA (sequence templates), PFC (abstract options) — not primarily HPC-resident. Sutton-Precup-Singh 1999; Botvinick et al. 2009; Ribas-Fernandes et al. 2011; Cushman 2013. HPC contributes via temporal-sequence encoding but is not the primary policy store.

⸻

Where the framing slightly conflates

1. "Reuniens for trajectories of objects and effects of actions" — reuniens carries goal-directed action-trajectory context (PFC→HPC, per Ito 2015). It does not carry "object motion trajectories" in a perceptual sense; that's lateral temporal / parietal territory. The reuniens analogy is right for PFC pushing goal-context down, not for "objects move and HPC tracks them."

2. Object permanence and object typing are different problems. Permanence = persistence under occlusion (DLPFC + parietal + HPC). Typing = categorical abstraction (lateral temporal + HPC concept cells). MECH-269 V_s "snapshot held when stream misaligned" already addresses *permanence* implicitly — when a stream's V_s drops, its last verified snapshot persists rather than being overwritten by garbage. Typing is the separate, currently-missing substrate.

⸻

What V3 currently has (relevant inventory)

- **Trajectory side**: residue field, anchor set (MECH-269 Phase 2 ii), ghost-goal bank (MECH-292), waking ghost-goal probes (MECH-293), per-region V_s (MECH-269 Phase 2 iii).
- **Implicit type representation in observation**: 5×5×7 entity-type one-hot in `world_obs`; HarmEncoder / ResourceEncoder produce category-like latents (z_harm, z_resource), but no compressed *prototype* representation that survives across instances.
- **Action-object representation**: SD-004 action-object space O; HippocampalModule.action_object_decoder. The closest existing thing to "action primitive" — but it's a learned decoder over a fixed `action_object_dim`, not a discrete library of named options.
- **Sleep recombination substrate**: MECH-285 (sleep replay sampler weighted by staleness), MECH-275 (Bayesian aggregator over per-region posteriors), MECH-273 (E2_harm_s offline gradient pass), MECH-272 (sleep routing gate). Recombination occurs; explicit type-extraction does not.
- **Anchor pool stream_mixture key**: anchors are clustered implicitly by which streams co-vary at write time. This is a *type-like signature* — it's the closest existing analogue of a category. But there's no operator that *extracts* prototypes from the anchor pool by clustering across the stream_mixture dimension.

⸻

What's actually missing

1. **No explicit type-prototype store.** A concept-cell-analogue substrate where "hazard," "resource," "wall," "self-caused-harm-event," "goal-locked-corridor" each live as a compressed prototype with associated z_world / z_harm / z_self signatures and a confidence score. Current observation should be matchable against the prototype library by similarity; the top-k matched types should modulate downstream consumers.

2. **No explicit option / policy library.** E3 proposes trajectories via CEM seeded by terrain prior; there is no library of "approach-resource," "avoid-hazard," "loop-back-to-anchor" stored as named options that can be invoked compositionally. The biology says these live partly in BG / pre-SMA, not solely in HPC — so an REE option library would not be hippocampal-resident in the same sense as the prototype library.

3. **No sleep operator that extracts types from recombination.** MECH-285 samples anchors weighted by staleness; MECH-275 aggregates per-region posteriors; MECH-273 trains E2_harm_s on synthetic batches. None of these produces "this cluster of anchors share a structural signature that constitutes the prototype for category-X." That extraction step is what Daniel's framing implies, and it is biologically the operation Lewis & Durrant 2011 / Schapiro 2017 describe.

⸻

Architectural shape if pursued

This would be roughly:

- **SD-N (object/action-type prototype substrate)**: a learned codebook over the anchor-pool (or over LatentState clusters), where each codebook entry is a prototype with associated z_world / z_harm / z_self signatures and a confidence score. Vector-quantised, possibly. Updated during sleep.
- **MECH-N (sleep type-extraction operator)**: a sleep pass that recombines anchors across goal/context dimensions and extracts the invariant structural signature, writing/updating codebook entries.
- **MECH-N+1 (waking verisimilitude-on-types match)**: at runtime, current LatentState is cosine-matched against the codebook, and the top-k matched types modulate downstream consumers (proposer, frontal substrates, residue write valence selection).

Cross-cutting touchpoints: MECH-269 (V_s gating — adds a third level of V_s on stored types), MECH-292 / MECH-293 (anchor-pool consumers), SD-039 (anchor payload — anchors might carry a type-tag), sleep cluster (MECH-272-275, MECH-285), SD-016 (ContextMemory diversification — already has the right shape for prototype storage, as Daniel intuited).

⸻

Falsifiable signature (if the substrate were added)

If REE has only an implicit type representation (current state), then post-sleep-recombination performance on a "type generalisation" task — e.g. resource at a never-visited location with a different surface signature but the same structural relationship to harm fields — should be comparable to non-sleep baseline. If REE has the explicit type-prototype substrate, post-sleep performance should be measurably higher specifically on type-generalisation tasks but not on instance-recall tasks.

This is a non-trivial experiment to construct in V3's grid-world (the environment doesn't currently support type-instance dissociation richly) — it might be a V4 experiment that gates V4 environment design.

⸻

Cross-references

- Frontal goal grounding lit-pull (precursor): `evidence/literature/targeted_review_frontal_goal_grounding/synthesis.md`
- ARC-007 strict (Q-020): hippocampal proposer is value-flat — terrain sensitivity is a consequence of navigating residue-shaped z_world, not a separate hippocampal value computation. Type-prototype store would need to respect this constraint: it's a *passive lookup substrate*, not a value-augmented one.
- SD-016 (ContextMemory diversification): the EXQ-418e diversification loss already pushes toward distinct prototype-like slots in ContextMemory. That substrate is not currently treated as a type-prototype store, but it has the right shape — the missing piece is an explicit sleep operator that *organises* the slots into a type-codebook.
- MECH-269 Phase 2 ii (anchor stream_mixture key): anchors are already clustered implicitly by stream_mixture. A type-prototype substrate could be derived from this clustering during sleep without adding a new storage layer.

⸻

Next step

Commission a follow-up lit-pull: **"Are HPC concept cells / categorical prototype representations functionally distinct from anchor / place-cell representations, and is there evidence sleep extracts type prototypes from compositional replay?"**

Anchor literature: Quiroga 2005, Schapiro 2013, Schapiro 2017, Lewis & Durrant 2011, Liu 2019, Constantinescu 2016, Bellmund 2018, Theves 2019.

The pull should clarify whether the type-prototype substrate is biologically *separate* from the anchor pool, or whether anchors-with-stream-mixture-keys are already biologically the type substrate (in which case REE has it, just under-exploited and missing the sleep extraction operator).

Pending the lit-pull verdict, two architectural extensions are on the table:
1. SD-N type-prototype substrate (if separate)
2. MECH-N sleep type-extraction operator (regardless — the extraction is the missing operation)

Both are V4 candidates unless behavioural evidence in V3 surfaces a need (e.g. type-generalisation failure modes in the EXQ-495 V3-full-completion-gate or successors).
