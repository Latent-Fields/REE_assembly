# SD-039 Dual-Trace Anchor Goal-Snapshot Payload

**Status (2026-04-27):** IMPLEMENTED. Both the substrate-side surface
(2026-04-26) and the module-level write-site population layer (2026-04-27)
have landed. V3-EXQ-494 6/6 PASS confirms the falsifiable signature
(goal-relevant vs goal-irrelevant dissociation) and dual-trace preservation
of the populated payload.

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

### Module-level write-site population (this session, 2026-04-27)

`HippocampalModule.build_goal_payload(latent_state, goal_state, residue_field,
bla_output, current_step, simulation_mode=False)` constructs an
`AnchorGoalPayload` once per `agent.sense()` tick from the current
waking-stream signals:

```
z_goal_snapshot     <- goal_state.z_goal.detach().clone()  (None when inactive)
wanting_strength    <- ResidueField.evaluate_valence(z_world)[..., VALENCE_WANTING].mean()
arousal_tag         <- bla_output.arousal_tag              (0.0 when BLA off)
last_vs             <- mean(per_stream_vs.values())        (None when empty)
staleness_at_write  <- max(staleness_accumulator.snapshot().values())
                                                           (None when accumulator off)
payload_written_step <- agent._step_count                  (anchor_set._tick fallback)
```

`build_goal_payload` returns `None` (skipping population entirely) when:

- the AnchorSet substrate is disabled,
- `AnchorSetConfig.use_sd039_anchor_payload` is `False` (master flag OFF),
- `simulation_mode=True` (MECH-094 gate -- replay / DMN paths must NOT
  populate payloads from waking signals).

`REEAgent.sense()` calls `build_goal_payload` after the MECH-269 Phase 1
`update_per_stream_vs` step and forwards the result as `goal_payload=...`
to both `tick_anchor_set` (the boundary-event-driven write/remap site)
and `apply_invalidation_broadcasts_to_regions` (the MECH-287
broadcast-driven mark_inactive site). Hysteresis-fired `mark_inactive`
inside `tick_hysteresis` does not refresh the payload -- the prior
payload is preserved as the cause-of-blockage trace per dual-trace
semantics.

`use_sd039_anchor_payload` is wired through `REEConfig.from_dims(...)`
and propagated to `config.hippocampal.anchor_set.use_sd039_anchor_payload`,
so experiments can enable the substrate via the standard factory.

### Items still deferred to follow-on sessions

1. **MECH-292 ranked ghost-goal bank.** Priority computation, bank size
   bound, decay over time. `query_by_goal_match` is the substrate input;
   the ranking lives in MECH-292.
2. **MECH-293 waking ghost-goal probes.** Probe-budget allocation in
   `HippocampalModule.propose_trajectories()` plus MECH-094 guardrail
   (ghost probes do not update the viability map until realized).
3. **ARC-060 hybrid field+bank architectural framing.** Documentation of
   the continuous-wanting-field plus discrete-ghost-bank duality.

## Why the substrate landed before the population layer

1. **The substrate is small, well-scoped, and testable in isolation.** The
   contract suite (10 tests) covers the surface completely without
   touching agent state. A clean substrate landing meant MECH-292 /
   MECH-293 could be designed against a stable API while the population
   layer was being wired.
2. **The population layer touches multiple consumer files.** Each anchor
   write site (boundary events, broadcast-driven invalidation) calls
   into `consume_boundary_events` / `mark_inactive`; the population
   layer (this session) threaded a single shared `goal_payload` argument
   through both paths.

## Falsifiable test (V3-EXQ-494, 6/6 PASS 2026-04-27)

From the SD-039 claim entry:

> after reward relocation or path blockage, inactive anchors on the
> formerly valid approach path should retain non-zero goal-match with
> the current `z_goal` while unrelated stale anchors do not.

V3-EXQ-494 exercises this with six sub-tests:

- UC1: substrate-side classes / methods accessible (PASS).
- UC2: master OFF, anchors carry no payload, query returns `[]` (PASS).
- UC3: master ON, anchors carry populated payload, query returns
  non-zero `goal_match` (PASS, 7/7 anchors match >= 0.99).
- UC4: dual-trace preservation -- inactive anchors retain payload
  across `mark_inactive` (PASS, 6 inactive + 1 active, all carry payload).
- UC5: goal-relevant vs goal-irrelevant dissociation (PASS): mean
  `goal_match` on Phase A (goal-inactive) anchors = 0.0; mean on
  Phase B (goal-active) anchors = 0.998; 3/3 above 0.3.
- UC6: MECH-094 simulation gate -- replay-path writes do NOT populate
  payloads from waking signals (PASS).

UC5 is the substrate-level falsifiable signature. Behavioural validation
(does ghost-goal querying improve recovery from blocked goals?) belongs
to MECH-292 / MECH-293's behavioural EXQ.

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
