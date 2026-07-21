# Thought Intake — Multiple relational graph organisations in hippocampal cognition

**Date of thought:** 2026-07-19
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-19_multiple_relational_graph_organisations_in_hippocampal_cognition.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Source:** *A Coding Implementation on Spatial Graph Neural Networks for Urban Function Inference* (city2graph / OSMnx / PyG) — an implementation tutorial, **not** primary biological evidence. Classified as software inspiration.
**Status:** structured intake written; candidate claims NOT yet registered (concurrent session held the `claims.yaml` claim).
**Promotes/demotes:** nothing.

## Authorship note

The raw thought is the user's, including the repository-grounded correction and — the sharpest move — the explicit **organisational / representational separation** that keeps the whole thing honest. This intake supplies the claim-level cross-reference and the routing.

## The load-bearing distinction (verbatim)

> Organisational claim: cognition depends on several distinct relational structures
> Representational claim: those structures should be implemented as explicit graphs
>
> The first may be true even if the second is false.

This is the guard that stops the thought becoming "replace the hippocampal module with a GNN." The raw thought states that non-goal explicitly: *"This thought does not justify replacing the current hippocampal representation with a graph neural network."* Any downstream work must carry that guard forward.

## Already owned — cross-reference, do NOT re-assert

REE's hippocampal architecture is one of the most densely claimed areas of the registry, and most of the relation types the thought enumerates are **already instantiated under other names**:

| Relation type in the thought | Existing claim(s) |
|---|---|
| Spatial / latent proximity | **MECH-238** (pairwise distance relations in the `z_world` manifold), **MECH-143** (value-free dorsal CA1 spatial mapping) |
| Action transition / traversability | **SD-004** (action objects as map backbone), **SD-001** (CEM trajectory search in HippocampalModule), **MECH-242** (pattern completion vs constructive mechanisms) |
| Temporal succession | **MECH-239** (time cells tiling a temporal dimension), **MECH-148** (pure time cells for E3 credit assignment), **MECH-156** (theta sequential traversal) |
| Event membership / nesting | **MECH-288** (two-level hierarchical event segmenter with monotonic nested ids), **MECH-321** |
| Causal dependency / outcome | **SD-003** (counterfactual self-attribution), **ARC-033**, **MECH-290** (backward temporal credit sweep at trajectory completion) |
| Shared goal relevance | **MECH-236** (proposals conditioned on `z_goal`), **MECH-237**, **MECH-292/293** (ghost-goal bank: inactive anchors whose preserved goal payload matches the current goal), **MECH-339** (composite retrieval cue), **MECH-325/326** (cue-indexed library + PFC retrieval gate) |
| Harm / benefit / valence structure | **ARC-036** + **SD-014** (explicit 4-component valence vector on map nodes), **MECH-233** (asymmetric threat/approach pathways), **MECH-208** (valence-asymmetric replay) |
| Motivational significance / wanting | **MECH-216/218** (predictive wanting), **ARC-051**, **MECH-329** |
| Social / agent-relative | **ARC-083** (others-as-object, token-keyed slots), **MECH-184** (other-directed hippocampal harm avoidance) |
| Semantic / schema abstraction | **MECH-211** (schema consolidation as search grammar), **MECH-166** (context slot formation), **MECH-429** (schema congruence), **INV-039**, **MECH-316** (cross-episode regularity / successor-representation analog) |
| Staleness / invalidation | **MECH-283/284/287** (V_s recognition gate, residual staleness accumulator, dual-component invalidation), **MECH-269** (per-stream / per-region V_s), **MECH-297** (per-type V_s) |
| Scale / granularity tagging | **SD-040** (type-prototype vector in the AnchorSet), **MECH-296**, **MECH-299/300** (theta content scales with abstraction vocabulary) |
| Dual / inactive traces | **SD-039** (dual-trace anchors) |
| Subregion specialisation | **MECH-143/144** (dorsal vs ventral CA1), **MECH-147** (DG pattern separation), **MECH-149** (CA1 mismatch), **MECH-362** (subtractive developmental sparsification), **ARC-040** |

So the thought's own conclusion is right and is confirmed here: **REE already contains several distinct relational semantics.** The registry has the *relations*. What it does not have is the *cross-cutting readout*.

## Genuinely new — three things

### N1. The typed relations are implicit and never read out as topology (the actual gap)

Every relation type above is realised as a **payload field, a gate, or a scoring term** — a property of an anchor or of a proposal. None is exposed as an **edge type over the anchor set**, and nothing in the registry tests whether the *topology* carries functional information beyond the local anchor features.

The thought's test is clean and cheap:

```
local anchor features alone
  vs  topology alone
  vs  local features + topology
  vs  heterogeneous typed topology
```

against held-out functional labels (goal-supporting region, harm-associated region, recurrent trap, bottleneck, completion route, stale/invalidated region, repair opportunity, reactivation candidate, likely interruption point).

**If topology adds predictive value, the existing architecture contains relational information it is not currently reading.** That is a genuinely new, retrospective, substrate-free claim — and it is the strongest thing in this thought, because a PASS immediately implies a cheap capability gain (read what is already there) rather than a build.

### N2. Functional identity from relational position, not local content

A corollary but worth separating: an anchor's functional role (gateway, bottleneck, recurrent trap, interruption point, repair opportunity) may be **inferable from its position** in the relational structure even when its local payload is incomplete. This is the practically valuable version, because it bears directly on open question 12 — *could topology identify which inactive anchor should be reactivated during goal pursuit?* — which is a live, already-built consumer (MECH-292/293 ghost-goal ranking currently ranks on payload match; a topological term would be a drop-in comparison arm).

### N3. Higher-order structure: metapaths, hyperedges, simplicial relations

Some functions may be properties of **typed multistep paths**, not nodes or pairwise edges:

```
current state -> available action -> transition region -> predicted hazard -> repair opportunity -> goal completion
inactive anchor -> shared event -> similar goal state -> successful historical trajectory -> candidate reactivation
```

Nothing in the registry represents anything above a pairwise relation. Whether REE needs hypergraph/simplicial structure is `complex (probe-gated)` — the probe is N1's projection F (heterogeneous typed topology) versus a metapath-aware readout.

### Also new, and worth keeping as a discipline note

**Graph construction is an epistemic commitment.** A proximity graph asserts nearness matters; a causal graph asserts intervention matters. So the top-down question — *which relations must be preserved for viable prediction, planning, commitment, causal attribution, residue-sensitive learning and generalisation?* — is architectural and precedes the mathematics. This is a good general principle and belongs in the hippocampal architecture doc regardless of whether any claim is registered.

## Explicitly NOT proposed

- Replacing the hippocampal representation with a GNN.
- Asserting the brain stores software-style graph data structures (the raw thought forbids it).
- Merging with the DLIF line. The relationship is a *pipeline boundary* — `distributed latent dynamics -> anchors -> typed relational projections -> functional inference -> action` — and useful projections would **not** establish that the native substrate is graph-like. Cross-reference only; DLIF as a unifying mathematical object is already answered-negative in the registry.

## Candidate claims (for registration at digestion)

1. **Hippocampal anchor topology carries functional information not present in local anchor payloads.** *Candidate, diagnostic, retrospective-testable.* Build typed projections (A latent proximity, B action transition, C shared event, D shared goal/valence, E causal/outcome, F heterogeneous typed) over existing anchor traces and predict held-out functional labels. PASS if `features + topology` beats `features alone` by a margin scaled on the SD of the delta plus an absolute floor, **and** heterogeneous typed topology (F) beats the collapsed single-adjacency ablation. *Non-degeneracy guard:* the anchor set must be non-trivial in the traces used — a floor on distinct anchors and on edge density per type; a projection where one relation type is empty or fully connected tests nothing and self-routes `substrate_not_ready`. *Type:* diagnostic over existing substrate, no build. *Cross-ref:* MECH-238, MECH-239, MECH-288, SD-004, SD-039, MECH-292/293, ARC-036/SD-014, MECH-269/283/284.

2. **Relation types are not collapsible to one adjacency structure.** *Candidate.* The direct ablation from candidate 1: collapsing all edge types into a single adjacency, or removing event / goal-motivational edges, or removing action-transition directionality, degrades functional-label recovery. *Falsifier:* the ablation series in the raw thought, plus the two control ablations that separate content from position — **randomise topology while preserving node payloads** and **preserve topology while shuffling payloads**. *Non-degeneracy guard:* at least one ablation must move the metric measurably. *Type:* mechanism/architectural. *Cross-ref:* MECH-069 (incommensurability — the same non-collapsibility argument one level down), MECH-035, candidate 1.

3. **(Applied, highest practical value) Topological position improves ghost-goal reactivation ranking.** *Candidate.* MECH-292/293 rank inactive anchors by preserved-goal-payload match; adding a topological term (relational distance to the current anchor along typed paths) improves reactivation precision. *Falsifier:* a ranking-quality comparison, payload-only vs payload+topology, on existing ghost-bank traces. *Non-degeneracy guard:* the ghost bank must be non-empty and the baseline ranking non-degenerate (not all-ties) across arms. *Type:* mechanism refinement of a built consumer. *Cross-ref:* MECH-292, MECH-293, MECH-339, SD-039.

4. **(Deferred, probe-gated) Higher-order relational structure (metapaths / hyperedges / simplicial) is required.** Register only as a `substrate_conditional` open question gated on candidate 1 projection F. Do NOT build.

5. **(Literature, out-of-domain leg) Does the biological hippocampal system support multiple partially distinct relational organisations across subregions, axes, inputs and replay regimes?** This is an empirical question whose test domain is neuroscience, not REE. Route to `/lit-pull` and register as `research_anchor` / `out_of_domain` if registered at all — **not** as a REE mechanism claim. The seven candidate biological predictions in the raw thought are the search brief.

## Routing

- **Answer open questions 1–3 first — they are a scoping spike, not a probe.** *What are the current explicit and implicit edge types? Are spatial/temporal/causal/action/event/goal/harm relations currently distinguishable in the logs? Are some stored only indirectly in trajectories or payloads?* The table above is the paper answer; the spike is confirming which of those are recoverable from **logged telemetry** rather than only from live objects. `complicated (buildable)`.
- **Then candidate 1** as a retrospective analysis on existing traces. No substrate change, no V3 critical-path impact.
- **Candidate 3 is the one with a built consumer** and is the cheapest thing that could change behaviour — consider it ahead of candidate 1 if a fast win is wanted, though it is strictly weaker evidence for the general claim.
- **`/lit-pull`:** the six search families (subregion specialisation; cognitive maps beyond physical space incl. successor representation / predictive maps; multiple map systems; replay across relation types; graph & topological analyses of hippocampus; hippocampal–prefrontal transformation). Note the successor-representation thread connects directly to **MECH-316**, which is already registered — check for overlap before pulling.
- **DLIF:** cross-reference at the projection boundary only.

## Next steps

1. Register candidates 1–3 (4 and 5 as gated / out-of-domain). **Deferred from this session.**
2. Mark the raw thought `Status: processed` once (1) lands.
3. Edge-type inventory spike against logged telemetry.
4. `/lit-pull` on subregion specialisation + multiple-map-systems.
