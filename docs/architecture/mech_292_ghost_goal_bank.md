# MECH-292 Ranked Ghost-Goal Bank

**Status (2026-04-27):** IMPLEMENTED. Pure-arithmetic derived view over the
SD-039 dual-trace anchor pool. Module: `ree-v3/ree_core/hippocampal/ghost_goal_bank.py`.
Wired into `HippocampalModule` behind `HippocampalConfig.use_mech292_ghost_bank`
(default False). Substrate prerequisite SD-039 (anchor goal-snapshot payload +
population layer) landed 2026-04-27 with V3-EXQ-494 6/6 PASS. Validation
diagnostic V3-EXQ-496 PASSed 5/5 sub-tests on 2026-04-27. MECH-292 is the
first downstream consumer of the SD-039 payload and the prerequisite for
MECH-293 (waking ghost-goal probe search) which wires
`HippocampalModule.propose_trajectories()` to consume the bank.

## Why this exists

A good agent should not treat all stale regions equally. Some stale regions
are still tied to currently-live goals (a blocked path to food I still want);
others are merely unresolved background (a corner I crossed once and never
revisited). Ranking by staleness alone (the MECH-284 path) collapses these
into one bucket and produces rumination over hopeless traces. Ranking by
goal-match alone misses the staleness signal that tells the agent *something
needs re-probing here*.

MECH-292 closes this gap with a derived view over the dual-trace anchor pool:
a ranked bank where each entry combines stored goal payload, current
motivational state, region staleness, and a coarse recoverability estimate.

This is the substrate MECH-293 will consume to seed waking ghost-goal probes
and that the V3 full-completion gate (V3-EXQ-495) will exercise as the
proposal-generation hook for the PLANNED arm of MECH-163's dual goal-directed
systems.

## What this lands

### New module

```
ree_core/hippocampal/ghost_goal_bank.py
```

Pure-arithmetic, non-trainable. No new state beyond a small per-tick cache;
the anchor pool itself remains the source of truth.

```python
@dataclass
class GhostGoalBankConfig:
    # Master flag wired through HippocampalConfig.use_mech292_ghost_bank.
    # Bank is a derived view -- per the MECH-292 claim notes, no separate
    # persistent store. Default OFF preserves bit-identical behaviour.

    # Ranking weights: ghost_priority = w_w * wanting
    #                                 + w_m * goal_match
    #                                 + w_s * staleness
    #                                 + w_r * recoverability
    # All clamped to non-negative; sum need not equal 1 (the absolute
    # magnitude is irrelevant; only ordering is consumed downstream).
    wanting_weight: float = 1.0
    goal_match_weight: float = 1.0
    staleness_weight: float = 0.5
    recoverability_weight: float = 0.5

    # Floor on goal_match before an anchor is admitted to the bank at all.
    # Anchors with stored z_goal_snapshot=None or with cosine below this
    # floor are treated as goal-irrelevant and excluded.
    goal_match_floor: float = 0.05

    # Cap on bank size returned per call. None -> no cap.
    top_k: Optional[int] = 32

    # Recoverability: if last_vs is None, treat as recoverable (1.0).
    # Otherwise recoverability = clamp_[0,1](last_vs).
    # last_vs near 1.0 = the region was confidently grounded when written;
    # near 0.0 = the region was already failing groundedness at preservation
    # time, so re-probing is unlikely to recover it.
    default_recoverability_when_unknown: float = 1.0

    # Filter: include inactive (dual-trace preserved) anchors? Default True.
    # MECH-293 ghost-goal probes work primarily over inactive traces, but
    # diagnostic / replay-prioritisation consumers may want active too.
    include_inactive: bool = True
    include_active: bool = False
    scale: Optional[str] = None  # optional scale filter ("fast", "slow")


@dataclass
class GhostGoalBankEntry:
    anchor: Anchor                  # reference to the source anchor
    ghost_priority: float           # composite rank
    components: Dict[str, float]    # per-term breakdown for diagnostics


class GhostGoalBank:
    """MECH-292: derived ranking view over the dual-trace anchor pool.

    Stateless across calls beyond a small diagnostics cache. Each rank()
    call walks the anchor pool, scores each anchor, and returns a sorted
    list. Implementation is intentionally a derived view, not a persistent
    store: SD-039 already preserves the per-anchor payload; MECH-292 just
    arranges the existing data.
    """

    def __init__(self, config: GhostGoalBankConfig, anchor_set: AnchorSet,
                 staleness_accumulator: Optional[StalenessAccumulator] = None):
        self.config = config
        self.anchor_set = anchor_set
        self.staleness_accumulator = staleness_accumulator
        self._last_diagnostics: Dict[str, Any] = {}

    def rank(self, current_z_goal: Optional[torch.Tensor]) -> List[GhostGoalBankEntry]:
        """Return the ranked ghost-goal bank for the current z_goal.

        Anchors with no stored z_goal_snapshot (payload-less or written
        outside any goal regime) are excluded by the goal_match_floor.
        Returns an empty list when current_z_goal is None or no anchor
        clears the floor.
        """

    def get_diagnostics(self) -> Dict[str, Any]:
        """Last-call summary: n_candidates_scanned, n_admitted, max_priority,
        mean_priority, plus per-component sums for sanity checks.
        """

    def reset(self) -> None:
        """Per-episode reset of the diagnostics cache."""
```

### Hippocampal integration

```
ree_core/hippocampal/module.py:
  HippocampalModule.__init__(...):
    if config.use_mech292_ghost_bank:
      assert config.use_anchor_sets,        "MECH-292 requires MECH-269 Phase 2 ii"
      assert config.use_sd039_anchor_payload, "MECH-292 requires SD-039 payload"
      self.ghost_goal_bank = GhostGoalBank(
          config=config.ghost_goal_bank_config,
          anchor_set=self.anchor_set,
          staleness_accumulator=self.staleness_accumulator,
      )

  HippocampalModule.rank_ghost_goals(current_z_goal) -> List[GhostGoalBankEntry]:
    if self.ghost_goal_bank is None: return []
    return self.ghost_goal_bank.rank(current_z_goal)

  HippocampalModule.reset() extension:
    if self.ghost_goal_bank is not None:
      self.ghost_goal_bank.reset()
```

### Config wiring

```
ree_core/utils/config.py:
  HippocampalConfig.use_mech292_ghost_bank: bool = False
  HippocampalConfig.ghost_goal_bank_config: GhostGoalBankConfig = factory()

REEConfig.from_dims():
  use_mech292_ghost_bank: bool = False  # master flag
  mech292_wanting_weight: float = 1.0
  mech292_goal_match_weight: float = 1.0
  mech292_staleness_weight: float = 0.5
  mech292_recoverability_weight: float = 0.5
  mech292_goal_match_floor: float = 0.05
  mech292_top_k: Optional[int] = 32
```

## Ranking formula

For each anchor `a` in the dual-trace pool that clears `goal_match_floor`:

```
wanting       = a.goal_payload.wanting_strength
goal_match    = a.goal_match(current_z_goal)           # SD-039 cosine helper
staleness     = staleness_accumulator.lookup(a.region_key) if accum present
                else (current_tick - a.last_accessed) / staleness_normaliser
recoverability = (a.goal_payload.last_vs                   if not None
                  else config.default_recoverability_when_unknown)

ghost_priority = ( config.wanting_weight       * wanting
                 + config.goal_match_weight    * goal_match
                 + config.staleness_weight     * staleness
                 + config.recoverability_weight * recoverability )
```

`staleness_accumulator` is the MECH-284 source of truth when present; the
fallback ensures MECH-292 still works in configurations where MECH-284 is
disabled (rare but possible — the anchor's own `last_accessed` tick gives a
weaker but workable proxy).

The ranking is utility-like (Mattar & Daw 2018) but **not** pure
low-`V_s` chasing. The `goal_match_floor` is the architectural commitment
that pure rumination is excluded: an anchor with no stored goal payload OR
with a goal_match below the floor is invisible to MECH-292 entirely. This
is the substrate-level guard against the depressive-rumination failure mode
flagged in the ghost-goal-search lit-pull.

## What MECH-292 does NOT do

- It does not own the per-anchor payload (SD-039 does).
- It does not generate trajectories (MECH-293 does).
- It does not gate write paths (MECH-094 / MECH-261 do).
- It does not modify the anchor pool — it is a read-only ranking view.

These boundaries keep MECH-292 small and falsifiable in isolation.

## Falsifiable signature

In a reward-relocation or blocked-corridor task:
- Anchors from the now-obstructed but still-valued path should rank above
  equally stale but goal-irrelevant anchors.
- Specifically: in a paired comparison of a goal-relevant inactive anchor
  vs a goal-irrelevant inactive anchor with matched staleness, the
  goal-relevant anchor's `ghost_priority` should be strictly higher in
  ≥ 4 / 7 seeds, with the gap dominated by the `goal_match` component.
- The `recoverability` term should keep anchors that have already failed
  V_s grounding from rising to the top despite high staleness.

## MECH-094

The bank is read-only over the existing anchor pool. There is no write
path to gate. SD-039's call-site scoping handles waking-vs-replay payload
provenance; MECH-292 inherits whatever provenance the source anchors carry.

## Phased training

None. Pure arithmetic, no trainable parameters.

## Validation experiment

`V3-EXQ-496` diagnostic with five sub-tests (PASSed 5/5 on Mac 2026-04-27,
~39s):

- UC1 module_importable
- UC2 master_off_no_op (`agent.hippocampal.ghost_goal_bank is None`)
- UC3 ranking_fires (after a goal-active episode, `rank()` returns a
  non-empty bank with `ghost_priority` strictly decreasing)
- UC4 goal_irrelevant_excluded (Phase A / Phase B episode design parallel
  to V3-EXQ-494 UC5 — Phase A anchors below `goal_match_floor` are absent
  from the bank)
- UC5 component_breakdown_consistent (per-entry `components` dict sums to
  `ghost_priority` within float-tolerance)

Behavioural validation lands as part of V3-EXQ-495 (V3 full-completion
gate, MECH-163 dual-system distinction) when MECH-293 consumes the bank.

## Dependencies

| Claim | Role |
|---|---|
| SD-039 | provides the per-anchor `goal_payload` MECH-292 ranks over |
| MECH-216 | populates `wanting_strength` (predictive wanting signal) |
| MECH-230 | provides the structured `z_goal` latent the cosine query uses |
| MECH-269 (Phase 2 ii) | dual-trace anchor substrate; bank pool source |
| MECH-269 Phase 1 / 2 iii | per-stream / per-region V_s feeding `last_vs` |
| MECH-284 | region staleness; preferred staleness source over the local proxy |

## What's next

1. Land MECH-292 substrate per this doc.
2. Land MECH-293 (`mech_293_ghost_goal_probe_search.md`) — the first
   consumer of `rank_ghost_goals()`.
3. Run V3-EXQ-495 (V3 full-completion gate) — MECH-293 is the
   proposal-generation hook the PLANNED arm calls; MECH-292 is what
   makes the call non-empty.
