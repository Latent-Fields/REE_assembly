# MECH-468 Edge-Type Inventory Spike

**Status:** Scoping spike, not a probe. No experiment proposal is minted by this
document (per MECH-468's own claims.yaml note). Session:
`chip-20260902-mech468-edge-type-inventory-spike`, 2026-09-02.

## 1. Why this exists, and what it does NOT do

MECH-468 asserts hippocampal anchor **topology** carries functional information not
present in local anchor payloads. Its falsifier needs six typed edge projections over
the anchor set (A latent proximity, B action transition, C shared event, D shared
goal/valence, E causal/outcome, F heterogeneous typed) to predict held-out functional
labels. Before any experiment can be proposed, this spike answers a narrower question:
**for each relation type, is the edge derivable at all today, and if so, from what --
live objects only, or logged telemetry too?**

This is explicitly a readout question, not a design proposal. Per MECH-468's own guard
(carried forward verbatim): "cognition depends on several distinct relational
structures" (organisational claim, asserted) is separate from "those structures should
be implemented as explicit graphs" (representational claim, NOT asserted). Nothing
here proposes replacing the hippocampal representation with a GNN, asserts the brain
stores graph data structures, or merges this line with DLIF.

**Downstream order.** MECH-470 (cheap applied consumer) and MECH-469 (typed-vs-collapsed
ablation) are both gated behind this spike; MECH-470's proposal EXP-1107 is already
`blocked_substrate` in `experiment_proposals.v1.json` with `blocked_by: MECH-468`, and
this spike is what the block names as the owed next move. A PASS on MECH-470 alone
would still be strictly weaker evidence for MECH-468 than a PASS on the full six-type
inventory + F-vs-collapsed ablation -- one consumer improving does not establish that
topology carries functional information generally. That asymmetry should travel with
any future MECH-470-only result.

**Do not queue an experiment for MECH-468 off this document.** The paced proposal
backlog (`proposal_tick_massmint_triage_20260901.md`) carries EXP-1103 /
`chip-proposal-exp-1103`, auto-minted by `proposal_tick` over MECH-468's explicit
"no experiment proposal is minted" instruction. That framing is wrong for this claim.
If EXP-1103 / `chip-proposal-exp-1103` is re-minted, this spike supersedes it -- the
correct next move is the recording-change work item in Section 4, not a queued
experiment.

## 2. What was already established before this spike (verify, don't re-derive)

`chip-proposal-exp-1107-paced` (2026-09-02, `/queue-experiment` Step 2.5 stop on
MECH-470) probed the substrate live and established two facts, reconfirmed here by
reading the same code:

**(a) Zero relational fields on Anchor; zero adjacency accessors on AnchorSet.**
`ree_core/hippocampal/anchor_set.py` -- `Anchor` (line 111) carries exactly
`(key, z_world, active, created_at, last_accessed, below_threshold_streak,
goal_payload)`. `AnchorSet`'s query surface (`active_anchors`, `all_anchors`,
`all_with_dual_trace`, `query_by_goal_match`, line ~507 onward) returns flat lists or
`(anchor, score)` pairs -- no `neighbours()`, `path()`, `distance()`, or edge-typed
accessor exists anywhere on the class. The only "adjacency" hit in `ree_core` is a
grid-placement comment in `ree_core/environment/causal_grid_world.py` (confirmed by
this spike's own STOP-CHECK grep, no other hit). SD-091 "coalition topology" is a star
topology over *subsystems*, not anchors, and its own scope statement excludes edge-
level graphs -- reconfirmed, no `MECH-468`/`MECH-469`/`MECH-470` hit in
`substrate_queue.json` and no typed-edge machinery hit outside
`causal_grid_world.py`'s comment.

**(b) GhostGoalBank telemetry is aggregate-only; 0 of 4 ghost-related manifests carry
per-anchor identity.** `GhostGoalBank._last_diagnostics` (`ghost_goal_bank.py` line
317-330) is `{n_candidates_scanned, n_no_payload, n_below_floor, n_below_persistence,
persistence_license, n_admitted, n_returned, max_priority, mean_priority,
component_sums, reason}` -- counts and sums, no `anchor_key` / `segment_id` /
`anchor_id`. Reconfirmed directly against
`v3_exq_868_mech292_ghost_priority_relevance_confirmer_20260802T035413Z_v3.json`: a
grep for `anchor_key|segment_id|anchor_id` returns nothing anywhere in the manifest,
including `per_seed_results[*].relevant_diagnostics` / `component_sums`, which are the
same aggregate shape as `get_diagnostics()`.

This spike's job is the remaining work: the full six-type inventory, not the
already-answered yes/no on typed-path distance specifically.

## 3. Per-relation-type table

Legend for column 2 (live-derivable) and column 3 (log-recoverable):
**YES** = the value/edge exists today without new code; **PARTIAL** = a proxy exists
but is not the literal relation MECH-468 names; **NO** = does not exist today.

| # | Relation (MECH-468 letter) | 1. Live-derivable today? | 2. Log-recoverable today? | 3. Minimal recording change | 4. Non-degeneracy floor |
|---|---|---|---|---|---|
| A | Latent proximity | **YES.** `Anchor.z_world` is a live detached tensor on every anchor (`anchor_set.py:132`); `AnchorSet.all_anchors()`/`active_anchors()` give the pool. Pairwise distance (cosine or L2) over `z_world` is a direct live computation -- `Anchor.goal_match()` already does the analogous cosine-with-baseline pattern for `z_goal_snapshot`, so the same recipe applies to `z_world`. | **NO.** Nothing writes an anchor's `z_world` (or any derived pairwise distance) into a manifest. `z_world` never leaves the live `AnchorSet`/`Anchor` object. | Emit a per-anchor row `{anchor_key, created_at, last_accessed}` plus EITHER a bounded pairwise-distance matrix (n^2 floats, n = pool size at dump time) OR a low-dim projection of `z_world` (avoid dumping the full latent -- manifests are meant to stay bounded). Natural emission site: a new `AnchorSet.dump_relational_snapshot()` called from the same place `GhostGoalBank.rank()` is called, so the snapshot shares a tick with the D/E dumps below. | Distance is a DENSE relation by construction (every pair has *some* distance) -- degenerate as "fully connected" unless thresholded into edges via a proximity cutoff. Need: (i) anchor-count floor per scale (>= ~15-20 distinct anchors in the trace window -- measured pools in the ghost-bank manifests run 6-24 anchors per call, so this is the realistic middle, not a made-up number); (ii) after thresholding, an edge-density floor in a healthy band (e.g. 10-70% of pairs pass cutoff) -- either 0% (representation collapsed, all anchors indistinguishable) or 100% (cutoff too loose) self-routes `substrate_not_ready`. |
| B | Action transition | **NO, as stated.** `Anchor`/`AnchorSet` never receive or store an action or action-object. `write_anchor`/`consume_boundary_events`/`tick_anchor_set` (`module.py:3715`) take `latent_state` and `BoundaryEvent`s only -- no action argument on the call path from `REEAgent.sense()`. SD-004 action-objects (`E2.action_object(z_world, a)`, `e2_fast.py`) live entirely on the CEM proposal/trajectory side (`e3_selector.py`, `Trajectory` in `e2_fast.py`) and never reference an `Anchor` or `AnchorKey` -- grep for "anchor" in `e3_selector.py` returns zero hits outside unrelated uses of the word "anchor" (margin anchoring, additive-authority anchoring). The only proxy today is temporal succession within a `(scale, stream_mixture)` family (`created_at` ordering as `write_anchor`/`reset_region` install successive anchors on remap) -- that is a temporal-adjacency signal, not an action-identified one; it says *that* a transition happened, not *which* action caused it. | **NO.** No action or action-object is attached to any Anchor or logged anywhere near anchor lifecycle events. | Largest build of the six: thread the last executed action (or its `action_object` embedding) into `tick_anchor_set`'s call site in `REEAgent.sense()`/`act()`, attach it to the outgoing `Anchor` at `mark_inactive`/`reset_region` time (mirrors how `AnchorGoalPayload` is already attached at write/remap/invalidate -- same three sites), and emit `{anchor_key_from, anchor_key_to, action_object, t}` at manifest time. This is a genuine substrate change, not a read-side dump -- flag as the one relation type that cannot be answered by instrumentation alone. | An action-transition edge is a **directed successor** relation (one edge per anchor swap) -- structurally sparse by construction (out-degree <= 1 per family), so the risk is the opposite of A: too sparse to be a graph at all unless multiple `(scale, stream_mixture)` families are pooled together, which then raises the question of whether cross-family action edges are meaningful. Floor: need successor edges pooled across enough families that the resulting node set (>= ~15 anchors, matching A) has out-degree > 0 for a majority of non-terminal anchors -- otherwise it degenerates to isolated chains too short to test. |
| C | Shared event | **YES.** `BoundaryEvent` (`event_segmenter.py:54`) carries `segment_id_old`, `segment_id_new`, `scale`, `sources`, `t` for every fired boundary; `consume_boundary_events` (`anchor_set.py:459`) installs one anchor per event per `(scale, stream_mixture)` family in the SAME call, so two anchors across different families that were written from events sharing `t` (and ideally `scale`) share the causing event live, in memory, for the duration of that tick. | **PARTIAL / mostly NO.** `BoundaryEvent`s are drained via `drain_boundary_events()`/queued internally but this spike found no manifest that records the boundary-event stream itself (as opposed to its downstream effects, e.g. staleness). Would need to check whether any experiment's `recording_schema` opts into boundary-event logging -- none of the ghost-bank manifests checked in Section 2 do, and this is a distinct telemetry surface from the ghost-bank diagnostics, so treat as NO until a targeted grep of `recording_schema` values proves otherwise (out of scope for this spike to exhaustively enumerate every experiment's schema). | Emit `{t, scale, segment_id_old, segment_id_new, sources}` per `BoundaryEvent` at the point `drain_boundary_events()` is called, tagged with the set of `anchor_key`s installed/remapped by that event (available synchronously inside `consume_boundary_events`, which already iterates `events` and calls `write_anchor` per event -- the installed `Anchor.key` is the return value). Cheapest of the six to log because the event object already exists and is walked exactly once per tick. | "Shared event" edges cluster into event-sized groups, not pairs -- degenerate if every event only ever touches one family (star-of-one, no sharing to test) or if `slow`-scale events fire so rarely that most anchors never co-occur with anything. Floor: need events that fire across >= 2 concurrently-active `stream_mixture` families often enough that a non-trivial fraction (not ~0%, not ~100%) of anchors have at least one shared-event partner. |
| D | Shared goal/valence | **YES, and mostly already built.** `Anchor.goal_match()` (`anchor_set.py:139`) computes exactly this: cosine similarity between two anchors' `goal_payload.z_goal_snapshot` (via a shared `current_z_goal` query today; anchor-to-anchor is the same call with one anchor's snapshot substituted for `current_z_goal`), plus `wanting_strength`/`arousal_tag` on `AnchorGoalPayload` (`anchor_set.py:60`) for the valence-sharing sub-case. `GhostGoalBank.rank()` already walks the full pool and computes `goal_match` per anchor against the live goal -- extending it to anchor-vs-anchor is a small change to an existing computation, not new machinery. | **NO** -- same finding as Section 2(b): the walk happens, the per-anchor `goal_match` values are computed, but only aggregated into `component_sums`/`max_priority`/`mean_priority` before being discarded. The per-anchor scores that would make this an edge list are computed and then thrown away every call. | Cheapest fix of the six in relative terms, since the values already exist mid-computation: in `GhostGoalBank.rank()` (`ghost_goal_bank.py:301`, where `GhostGoalBankEntry(anchor=anchor, ghost_priority=..., components=...)` is already built per anchor), also record `{anchor_key, goal_match, wanting_strength, arousal_tag}` into a per-anchor list attached to `_last_diagnostics` (or a sibling structure) instead of only the aggregate. No new computation, only retaining what is already produced. | `goal_match` is bounded to non-negative cosine and most anchors in a pool share a common `z_goal` context, so this is the type most at risk of being **near-fully-connected** at a loose threshold (the SD-079 background note in `anchor_set.py:154-164` records a measured case where uncentered `z_goal` gave pairwise cosine >= 0.9878 across 24 anchors -- i.e. every anchor "shared goal" with every other one before centering was added). Floor: after SD-079 centering (which is the design fix for exactly this), require a spread check -- e.g. the pairwise `goal_match` distribution's IQR clears a minimum width -- before trusting this as a non-degenerate edge type, not just "did centering run". |
| E | Causal/outcome | **PARTIAL.** MECH-287's `InvalidationTrigger` emits `BroadcastEvent{source_scale, source_segment_id_old, source_segment_id_new, source_sources, strength, targets}` (`invalidation_trigger.py:70`); `StalenessAccumulator.integrate()` (`staleness_accumulator.py:77`) already computes a genuine one-to-many directed credit assignment from one source region to every OTHER active anchor's region, weighted by `attribution_weight` (`"stream_overlap"` mode gives per-anchor weight `|source_sources & stream_mixture| / |source_sources|`, i.e. a real, non-uniform anchor-to-anchor edge weight computed live). This is the richest live structure of the six-minus-D. HOWEVER: the mechanism that actually fires today (`HippocampalModule.apply_invalidation_broadcasts_to_regions`, `module.py:3536`) only resets the SOURCE anchor's own region -- it does not currently route a broadcast's effect onto a *different* target anchor's payload/state, so the "outcome" half of this edge (does the target's own state change) is not wired end-to-end even though the attribution weight is computed. | **NO, and not just missing -- destroyed by construction.** `StalenessAccumulator.get_stats()` returns only `{n_integrations, n_leak_ticks}`; `snapshot()` returns the post-leak, post-accumulation scalar staleness PER REGION, with the per-event edges that produced it already summed and decayed away. Even in principle, you cannot recover "this region's staleness came 60% from broadcast X, 40% from broadcast Y" from the accumulator's own state after the fact -- the information is gone the tick after `integrate()` runs, not merely unlogged. | Log each `integrate()` call's per-anchor increment BEFORE it is folded into `self._staleness` -- i.e. inside `StalenessAccumulator.integrate()`'s inner loop (`staleness_accumulator.py:124`), emit `{t, source_scale, source_segment_id_old, target_anchor_key, attribution_weight, strength}` per non-zero increment. This is the one relation type where the read-side fix must live INSIDE the accumulating function itself, not at a downstream dump site, because the edge-level information does not survive past that loop. | Under `attribution_mode="equal"` (weight `1/N` for every active anchor, `staleness_accumulator.py:108-110`) this relation is **provably fully-connected by construction** -- every broadcast reaches every active anchor with positive weight, which is exactly MECH-468's named degenerate case. Only `attribution_mode="stream_overlap"` can be non-degenerate (zero weight when `source_sources` and an anchor's `stream_mixture` don't intersect) -- **this spike's recommendation is that any future E-type probe must run with `attribution_mode="stream_overlap"`, not the default "equal"**, plus a floor on the fraction of anchor pairs with nonzero overlap sitting in a healthy middle band. |
| F | Heterogeneous typed | **PARTIAL, and gated on B/E's builds.** A/C/D can already be computed from the SAME live tick (a single `AnchorSet` snapshot exposes `z_world`, boundary-event co-membership, and `goal_payload` simultaneously, all keyed on the same `AnchorKey`) -- so a 3-type heterogeneous graph (A+C+D) is live-derivable today with no new substrate, only the dump work already listed for A/C/D. A full 5-type graph additionally needs B (action transition, a real build) and a genuinely wired E (see E's live-derivable caveat above). | **NO.** No relation type is currently logged at anchor granularity (Section 2(b) + this table), so there is no existing trace with even one type recorded, let alone several sharing a common per-anchor key. | Not a separate build -- F's minimal change is that A/C/D/E's per-anchor dumps (above) must be emitted from ONE shared snapshot call keyed by the SAME `anchor_key`, so a downstream consumer can join them into one heterogeneous graph rather than reconstructing alignment after the fact from independently-timed dumps. Recommend a single new method (e.g. `AnchorSet`-adjacent, called once per tick or per manifest-write) that calls into the A/C/D (and later E) dump logic and returns one `{anchor_key: {relation_type: ...}}` structure. | Needs every constituent type's OWN floor cleared simultaneously on the SAME trace window, plus a further check specific to F: the typed-vs-collapsed ablation (MECH-469) is vacuous if, in practice, only one relation type is ever populated on a given trace (collapsing types that are already trivial changes nothing) -- so F's floor is "at least 2 of A/C/D/E individually clear their own non-degeneracy floor on the same window," not just "the dump code runs." |

## 4. Verdict

**MECH-468's full falsifier (A-F + the F-vs-collapsed ablation) is NOT buildable
today from logged telemetry, and for two of six types (B, E) not even fully
buildable from LIVE objects without new substrate wiring.** Per type:

- **A (latent proximity), C (shared event), D (shared goal/valence):** live-derivable
  today with no new substrate change -- only a recording/dump gap. These three are
  the cheap tier: the falsifier's read-side claim ("read what is already there")
  holds for them specifically.
- **E (causal/outcome):** live-derivable in part (the attribution-weight computation
  already exists and is genuinely non-uniform under `stream_overlap` mode) but the
  end-to-end "outcome on a distinct target anchor" wiring is not there, and the edge
  information is actively destroyed (not merely unlogged) by the accumulator's
  summing/leak design -- the fix has to live inside the accumulating loop.
- **B (action transition):** not derivable from live objects at all today. This is
  the one type needing an actual substrate change (threading action identity onto
  the anchor-lifecycle call path) before any recording question is even reachable.
- **F (heterogeneous typed):** inherits the ceiling of its slowest constituent (B),
  but a reduced 3-type version (A+C+D) is reachable purely through recording changes.

**Recommendation: the minimal recording change is real, scoped, and worth proposing
to `substrate_queue.json` as a single implementation entry** covering the A/C/D
per-anchor dumps (the cheap tier) plus the E accumulator-internal edge log, with B
explicitly called out as a separate, larger substrate item (not bundled, since it is
a different kind of change -- new plumbing on the action/decision path, not a
read-side dump). A proposed entry shape (not written to `substrate_queue.json` by
this spike -- scope call below):

```json
{
  "sd_id": "mech468-anchor-relational-dump",
  "title": "Per-anchor relational-edge recording: latent proximity (A), shared-event co-membership (C), shared goal/valence (D), and staleness-attribution edges (E) at anchor granularity",
  "status": "candidate",
  "priority": "low",
  "design_doc": null,
  "implementation_hint": "Add a per-tick relational snapshot keyed by AnchorKey: (i) A -- pairwise z_world distance or a bounded low-dim projection, emitted alongside created_at/last_accessed; (ii) C -- per-BoundaryEvent {t, scale, segment_id_old, segment_id_new, sources} tagged with the anchor_key(s) it installed, read inside consume_boundary_events; (iii) D -- retain GhostGoalBank.rank()'s already-computed per-anchor goal_match/wanting/arousal instead of discarding into component_sums only; (iv) E -- log StalenessAccumulator.integrate()'s per-anchor attribution_weight*strength increment before it is folded into self._staleness, and require attribution_mode=stream_overlap (not equal) for any future E-type probe since equal-mode is fully-connected by construction. Each type carries its own non-degeneracy floor -- see mech468_edge_type_inventory_spike.md Section 3 -- and a probe must check its floor before treating an empty or saturated result as evidence.",
  "depends_on_unresolved": [],
  "unblocks_claims": ["MECH-468", "MECH-469", "MECH-470"],
  "added_session": "chip-20260902-mech468-edge-type-inventory-spike"
}
```

**Why this spike does not write that entry itself:** the exact field-level shape (in
particular, whether A's projection is a distance matrix or a reduced embedding, and
whether C's event tagging lives in `consume_boundary_events` or a wrapper) is an
implementation decision that `/implement-substrate` should make against the live
design docs, not something this scoping spike should freeze. The entry above is a
proposal for a human or a follow-on `/implement-substrate` session to register, not
a committed queue item.

**B is out of scope for that entry.** Recommend a second, separate `candidate`
`substrate_queue.json` entry for B (action-identity-on-anchor-lifecycle) only after
someone confirms it is worth building ahead of a concrete consumer -- unlike A/C/D/E,
which are cheap reads of data that already exists, B is new computation on a
different subsystem boundary (the action/decision path) and should not be bundled
into a "just expose what's already there" ticket.
