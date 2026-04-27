# MECH-293 Waking Ghost-Goal Probe Search

**Status (2026-04-27):** DESIGNED, NOT IMPLEMENTED. Substrate prerequisite SD-039
landed 2026-04-27; MECH-292 (ranked ghost-goal bank) is the immediate
prerequisite and is also designed-not-implemented (see `mech_292_ghost_goal_bank.md`).
This doc specifies the second consumer in the ghost-goal cluster: the
proposal-generation hook that turns a ranked ghost bank into actual probe
trajectories.

This is the substrate the V3 full-completion gate (V3-EXQ-495) calls as
the PLANNED-arm proposal hook in MECH-163's dual goal-directed systems
test. Without MECH-293, the gate's PLANNED arm has no mechanism distinct
from the HABIT arm and the experiment is uninformative.

## Why this exists

The current waking proposer (HippocampalModule.propose_trajectories) generates
value-flat candidates: CEM around the current terrain prior plus E1
world-prior conditioning. ARC-007 strict says this is correct — the
hippocampus does not own value computation. But "value-flat over the current
terrain" is a strong default that is biased toward CURRENT context. When the
agent has unresolved goals attached to non-current regions (a blocked path,
a deferred target, a remembered resource cache), the value-flat proposer
will not propose probes there; the only mechanism that re-surfaces those
regions is random exploration.

MECH-293 adds a second proposal branch: a minority budget of candidates
seeded around the highest-priority entries in the MECH-292 ghost-goal bank.
These probes are hypothesis-tagged (MECH-094) until they yield realized
outcomes — they explore, they don't commit the viability map.

In the dual-system framing of MECH-163: the value-flat HABIT arm scores
trajectories already on the table; the PLANNED arm uses MECH-293 to put
goal-relevant trajectories on the table that wouldn't otherwise be there.

## What this lands

### Module-level extension to HippocampalModule

```
ree_core/hippocampal/module.py:
  HippocampalModule.propose_trajectories(...) extended:

    candidates = self._propose_value_flat(z_world, e1_prior, ...)  # existing path

    if self.config.use_mech293_ghost_probes and self.ghost_goal_bank is not None:
      ghost_candidates = self._propose_ghost_seeded(
          current_z_goal=current_z_goal,
          n_total=self.config.n_candidates,
          ghost_fraction=self.config.mech293_ghost_fraction,
          z_world=z_world,
          e1_prior=e1_prior,
      )
      # Mix: keep n_total candidates total. Replace the bottom-ranked
      # value-flat candidates with ghost-seeded ones rather than expanding
      # the candidate pool. Preserves downstream E3 selection cost.
      candidates = self._mix_value_flat_with_ghost(candidates, ghost_candidates)

    return candidates


  HippocampalModule._propose_ghost_seeded(...) -> List[Trajectory]:
    """Generate ghost-seeded probe trajectories from the MECH-292 bank.

    1. n_ghost = max(1, int(round(n_total * ghost_fraction))) bounded by
       the number of available bank entries; if bank is empty, return [].
    2. Pull top n_ghost GhostGoalBankEntry items from rank(current_z_goal).
    3. For each entry, seed a CEM probe around the anchor's z_world rather
       than the agent's current z_world: action_object_mean is conditioned
       on (entry.anchor.z_world, e1_prior, residue_val_at_entry_z_world).
    4. Each generated trajectory is tagged hypothesis_tag=True (MECH-094)
       and labelled with provenance:
         trajectory.metadata = {
             "source": "mech293_ghost_probe",
             "anchor_key": entry.anchor.key,
             "ghost_priority": entry.ghost_priority,
             "goal_match": entry.components["goal_match"],
         }
    5. The trajectory is otherwise an ordinary CEM-refined sequence: E2
       rolls forward in action-object space, terrain scoring proceeds
       normally. The only differences are the seed z_world (anchor's,
       not current) and the hypothesis tag.
    """
```

### Ghost fraction and budget

The minority budget is the gate against rumination. Bench too high and the
proposer re-probes blocked goals at the expense of current-context
trajectories. Bench too low and ghost probes never escape the
random-exploration baseline.

Default: `mech293_ghost_fraction = 0.2`. So if `n_candidates = 16`, the
proposer emits 13 value-flat plus 3 ghost-seeded. The fraction is exposed
as a knob on `HippocampalConfig` so EXQ sweeps can probe the
recovery-vs-rumination tradeoff.

### Hypothesis tag preservation (MECH-094)

```
ghost trajectories carry hypothesis_tag=True throughout:
  - E2 rollout: hypothesis_tag forwarded to predictions
  - Terrain scoring: residue updates suppressed during ghost-probe
    rollouts (existing MECH-094 path)
  - Anchor writes: any tick_anchor_set call triggered during the rollout
    inherits hypothesis_tag=True so the anchor write skips waking-stream
    payload (already enforced by SD-039 population layer's
    simulation_mode argument)
  - Viability-map updates: blocked
```

The ghost probe is a *plan*, not a commitment. If E3 selects a ghost
probe and the agent acts on it, the actually-executed trajectory loses
the hypothesis tag at the commit boundary and behaves like any other
realized trajectory from that point forward (committed-trajectory
recording, backward credit sweep, etc., all proceed normally per
existing MECH-090 / MECH-290 paths).

### Config wiring

```
HippocampalConfig:
  use_mech293_ghost_probes: bool = False
  mech293_ghost_fraction: float = 0.2
  mech293_min_ghost_candidates: int = 1   # floor when bank has entries
  mech293_max_ghost_candidates: int = 8   # cap regardless of fraction
  mech293_replace_lowest_ranked: bool = True
    # True: ghost candidates replace bottom value-flat candidates,
    # preserving total candidate count.
    # False: ghost candidates are appended (raises n_candidates by
    # n_ghost). Used only for diagnostics / EXQ-487-style ablations.

REEConfig.from_dims():
  use_mech293_ghost_probes: bool = False  # master flag
  mech293_ghost_fraction: float = 0.2
```

Precondition (raised on `__init__`): `use_mech293_ghost_probes=True`
requires `use_mech292_ghost_bank=True` AND
`use_sd039_anchor_payload=True` AND `use_anchor_sets=True`. Without
those upstream flags, the bank is empty and ghost probes are silent —
the precondition makes the misconfiguration loud rather than silent.

## Diagnostics

Per-tick `propose_trajectories` extension records on
`HippocampalModule._last_propose_diagnostics`:

```python
{
  "mech293_n_ghost_proposed": int,
  "mech293_n_ghost_admitted": int,    # post-mix
  "mech293_max_ghost_priority": float,
  "mech293_mean_goal_match_at_seed": float,
}
```

Captured in run-pack manifests by experiments that opt in.

## What MECH-293 does NOT do

- It does not commit. Ghost probes go into E3 the same way value-flat
  candidates do; if E3 ranks them low, they don't leave the head.
- It does not modify the bank ranking. MECH-292 is upstream.
- It does not bypass MECH-094. Hypothesis tag stays True through the
  rollout; only commit / execution loses it.
- It does not violate ARC-007 strict. The proposer is still
  proposing trajectories without a value head; the ghost-seeded ones
  are biased BY LOCATION (the anchor's z_world) not by an internal
  value computation. Goal-match enters via MECH-292's ranking, which
  consults stored payloads — that ranking lives outside HippocampalModule.

## Falsifiable signature

Versus a random-probe control with the same total candidate count:
- Ghost-seeded probes should show higher mean `goal_match` of the
  seed location than random probes (the bank is doing its job).
- After a goal becomes blocked at a previously-pursued location,
  ghost-seeded recovery (mean steps to re-acquire benefit) should be
  faster than random-probe recovery in ≥ 4 / 7 seeds.
- Revisitation rate of fully incoherent stale regions (high
  staleness, low goal-match, low recoverability — anchors that the
  bank's `goal_match_floor` filters out) should be lower under
  MECH-293 than under uniform random probing. This is the
  rumination-suppression signature.

The behavioural test that exercises both is V3-EXQ-495 paradigm A
(detour) — see `v3_exq_495_mech163_planned_system_gate.py`.

## MECH-094

Three call-site checks already exist in the substrate:
1. `_propose_ghost_seeded` sets hypothesis_tag=True on every emitted
   trajectory before returning.
2. The CEM rollout path in HippocampalModule already forwards
   hypothesis_tag through E2 calls (existing MECH-094 wiring).
3. SD-039 population layer's `build_goal_payload(..., simulation_mode=True)`
   returns None, so any anchor write triggered during a ghost-probe
   rollout writes goal_payload=None (the rollout cannot retroactively
   author a populated payload from its hypothetical state).

No new MECH-094 plumbing required.

## Phased training

None. Pure routing logic; ghost-probe generation reuses the existing
CEM machinery, just with a different seed z_world.

## Validation experiment

`V3-EXQ-XXX` (placeholder; assign next free number after MECH-293
lands) diagnostic with five sub-tests:

- UC1 module_importable
- UC2 master_off_no_op (`propose_trajectories` returns the same
  candidate count and provenance as pre-MECH-293 baseline)
- UC3 ghost_branch_fires (with non-empty bank, at least one
  trajectory has `metadata["source"] == "mech293_ghost_probe"`;
  bank-empty -> zero ghost trajectories)
- UC4 hypothesis_tag_preserved (every ghost trajectory carries
  hypothesis_tag=True; any anchor write triggered during the rollout
  records goal_payload=None)
- UC5 budget_respected (n_ghost matches `ceil(n_candidates * ghost_fraction)`
  bounded by `[min_ghost_candidates, max_ghost_candidates]` and by
  the bank size)

Behavioural validation = V3-EXQ-495 V3 full-completion gate.

## Dependencies

| Claim | Role |
|---|---|
| SD-039 | provides per-anchor payload (transitive via MECH-292) |
| MECH-292 | provides the ranked bank `_propose_ghost_seeded` consumes |
| ARC-007 strict | constraint: no value head; MECH-293 stays compliant by routing through MECH-292's external ranking |
| ARC-018 | hippocampal trajectory proposal / evaluation loop being modified |
| ARC-032 | goal-biased sequence generation (MECH-293 is one instantiation) |
| MECH-089 | theta-packaged waking E3 updates (architectural context) |
| MECH-094 | hypothesis-tag invariant (preserved by call-site scoping) |
| MECH-269 | anchor / probe substrate (transitive via MECH-292) |
| MECH-291 | mode-sensitive sequence generator framing (one generator across waking and offline modes; MECH-293 is the waking arm) |

## What's next

1. Land MECH-292 (`mech_292_ghost_goal_bank.md`).
2. Land MECH-293 per this doc.
3. Run V3-EXQ-495 V3 full-completion gate
   (`ree-v3/experiments/v3_exq_495_mech163_planned_system_gate.py`).
   The PLANNED arm uses `use_mech293_ghost_probes=True`; HABIT arm
   uses `use_mech293_ghost_probes=False` with `goal_weight > 0`
   (EXQ-327 setup); ABLATED arm has neither. Paradigms A (detour) and
   B (novel context) run in a single script.
