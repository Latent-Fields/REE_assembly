# SD-039 Dual-Trace Anchor Goal-Snapshot Payload

**Status (2026-04-26):** SUBSTRATE-SIDE LANDED. Module-level write-site
population deferred to a follow-on session.

## Why this exists

MECH-269's dual-trace anchor substrate (Phase 2 ii) preserves `z_world` and
active/inactive status. MECH-284's region-staleness scalar tells us *which*
regions are unresolved. Neither tells us *whether the unresolved region still
corresponds to a live goal*.

This is the gap the ghost-goal cluster (MECH-292 ranked ghost-goal bank,
MECH-293 waking ghost-goal probes, ARC-060 hybrid field+bank architecture)
needs closed before any of those mechanisms can rank or probe usefully.
Without a stored goal payload, MECH-292 has only staleness to rank by,
which collapses to "more stale = higher priority" and produces rumination
over hopeless traces rather than intelligent re-probing of blocked goals.

SD-039 is the substrate change that lets the broader cluster discriminate
"this stale region is still tied to my current goal" from "this stale
region is just unresolved background."

## What this lands

### Substrate (this session)

A compact motivational payload attached to each anchor at write, remap, or
invalidation time. The payload survives `mark_inactive`, so inactive anchors
remain queryable as ghost-goal traces.

```
ree_core/hippocampal/anchor_set.py:
  @dataclass class AnchorGoalPayload:
    z_goal_snapshot: Optional[torch.Tensor] = None
    wanting_strength: float = 0.0
    arousal_tag: float = 0.0
    last_vs: Optional[float] = None
    staleness_at_write: Optional[float] = None
    payload_written_step: int = 0

  Anchor.goal_payload: Optional[AnchorGoalPayload] = None
  Anchor.goal_match(current_z_goal) -> float  # clipped non-negative cosine

  AnchorSet.write_anchor(..., goal_payload=None)
  AnchorSet.mark_inactive(..., goal_payload=None)  # refresh on invalidate
  AnchorSet.reset_region(..., goal_payload=None)   # refresh on both traces
  AnchorSet.consume_boundary_events(..., goal_payload=None)
  AnchorSet.query_by_goal_match(current_z_goal, threshold=0.0,
                                 scale=None, active_only=False)
                                 -> List[Tuple[Anchor, float]]
```

Config flag: `AnchorSetConfig.use_sd039_anchor_payload` (default `False`).
The flag is the substrate-side toggle. With `False`, callers omit
`goal_payload` (or pass `None`), and behaviour is bit-identical to
pre-SD-039. The flag becomes the module-level conditional when the
write-site population layer lands.

### Refresh-on-invalidate semantic

The design choice in the claims.yaml SD-039 entry: payload should reflect
the most recent wanting/arousal at the point the trace is preserved. The
substrate implements this by:

1. `mark_inactive(..., goal_payload=p)` writes `p` onto the anchor BEFORE
   inactivating it. Existing payload is replaced; nothing is cleared on
   inactivation (the entire point of dual-trace preservation).
2. `reset_region(..., goal_payload=p)` writes `p` onto BOTH the outgoing
   trace (cause-of-blockage payload) AND the new active anchor (new
   motivational identity).
3. `consume_boundary_events(..., goal_payload=p)` forwards `p` to each
   per-event `write_anchor` call so anchors installed in response to a
   boundary tick share the current motivational context.

### Query helper

`query_by_goal_match` is the substrate hook MECH-292 will consume. It
scans the active + inactive dual-trace pool, scores each anchor against
the supplied `current_z_goal` via `Anchor.goal_match`, and returns
non-zero matches sorted descending. SD-039 itself does NOT rank; the
ranked-bank computation
`ghost_priority ~ wanting * goal_match * staleness * recoverability`
lives in MECH-292's module.

`active_only=True` restricts to the active half (legacy behaviour).
`threshold=-1.0` includes every payload-bearing anchor regardless of
match (diagnostic use).

## What this does NOT land

Deferred to a follow-on session:

1. **Module-level write-site population.** REEAgent / HippocampalModule
   should populate `goal_payload` from `GoalState` (`z_goal_snapshot`),
   `ResidueField` VALENCE_WANTING (`wanting_strength`), and amygdala
   arousal tags (`arousal_tag`) at every anchor write / remap / invalidate
   site. The substrate accepts the payload; the population layer is a
   separate, well-scoped change.
2. **MECH-292 ranked ghost-goal bank.** Priority computation, bank size
   bound, decay over time. The `query_by_goal_match` helper is the
   substrate input; the ranking lives in MECH-292.
3. **MECH-293 waking ghost-goal probes.** Probe-budget allocation in
   `HippocampalModule.propose_trajectories()` plus MECH-094 guardrail
   (ghost probes do not update the viability map until realized).
4. **ARC-060 hybrid field+bank architectural framing.** Documentation of
   the continuous-wanting-field plus discrete-ghost-bank duality.
5. **Validation EXQ.** The falsifiable test (after reward relocation or
   path blockage, inactive anchors on the formerly valid approach path
   retain non-zero `goal_match` against current `z_goal` while unrelated
   stale anchors do not) is observable only once population is wired.

## Why split substrate from population

Two reasons:

1. **The substrate is small, well-scoped, and testable in isolation.** The
   contract suite (10 tests) covers the surface completely without
   touching agent state. A clean substrate landing means MECH-292 /
   MECH-293 can be designed against a stable API while the population
   layer is being wired.
2. **The population layer touches multiple consumer files.** Each anchor
   write site (boundary events, hysteresis remap, FIFO eviction)
   currently calls `write_anchor` / `mark_inactive` without the new
   kwarg. Adding population is a sweep across `agent.py` and
   `hippocampal/module.py` that should be reviewed as its own unit of
   work, not folded into the substrate landing.

## Falsifiable test (when population lands)

From the SD-039 claim entry:

> after reward relocation or path blockage, inactive anchors on the
> formerly valid approach path should retain non-zero goal-match with
> the current `z_goal` while unrelated stale anchors do not.

The validation EXQ exercises this directly: write anchors at goal A,
relocate reward to goal B (or block path), check that the now-inactive
A-anchors retain non-zero `goal_match` against the original `z_goal_A`
while goal-irrelevant anchors do not. This is a substrate-landing
diagnostic; behavioural validation (does ghost-goal querying improve
recovery from blocked goals?) belongs to MECH-292/293's behavioural EXQ.

## Biological grounding

Lit-pull synthesis: `evidence/literature/targeted_review_ghost_goal_search/`.

- **Berridge 1998, Barch 2010** — persistent wanting / goal
  representations exist as a discrete substrate and are not subsumed by
  the continuous valence field.
- **Mattar & Daw 2018** — utility-prioritised replay; gives the
  normative argument for goal-relevance ranking over pure recency.
- **Pfeiffer & Foster 2013** — goal-biased forward path search during
  waking quiescence.
- **Gillespie 2021** — broad, non-current, non-recent trace
  reactivation; closest neural match for ghost-goal bank prioritisation.
- **Muessig 2019** — one sequence generator across waking and offline
  modes; supports a single substrate that MECH-292 / MECH-293 will share.
- **Berkowitz 1989** — frustration / unresolved goal persistence; the
  behavioural phenotype the substrate makes computationally tractable.

## Backward compatibility

`AnchorSet.write_anchor` / `mark_inactive` / `reset_region` /
`consume_boundary_events` all accept `goal_payload=None` as default.
Existing call sites that omit the kwarg are unchanged. Anchors carry
`goal_payload=None`. `query_by_goal_match` returns `[]` when no
payload-bearing anchors exist. The full contract suite (164/164) plus
preflight (7/7) pass with the SD-039 surface in place but unused.

## See also

- MECH-269 — dual-trace anchor substrate being extended
- MECH-216 — predictive wanting (input to `wanting_strength` population)
- MECH-230 — z_goal latent structure (`z_goal_snapshot` source)
- MECH-284 — region staleness (`staleness_at_write` source)
- MECH-292 — downstream ghost-goal bank consumer (deferred)
- MECH-293 — downstream waking ghost-goal probe consumer (deferred)
- ARC-060 — hybrid field+bank architectural framing (deferred)
- MECH-094 — call-site scoping for the population layer
- `docs/architecture/ghost_goal_search.md` — the umbrella ghost-goal
  cluster design doc this substrate sits inside
