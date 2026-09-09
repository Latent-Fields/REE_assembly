# SD-105 freeze/share API: converge the multiplier once, apply it as a shared constant

**Status:** DESIGN NOTE / REGISTRATION ONLY (2026-09-09). Not a build authorisation.
**Owner claim:** SD-105 (`control_plane.selection_entropy_headroom_floor`), registered 2026-09-04.
**Consumers:** V3-EXQ-963c (successor to V3-EXQ-963b, not yet authored), MECH-063 (ii), SD-069, SD-104.
**Node class:** `complicated (buildable)` -- the API shape is fully specified; the residual scientific unknown belongs to 963c, not to this build.
**Source of record:** `WORKSPACE_STATE.md` `2026-09-04T21:02:25Z -- campaign C2c` (DECISION OWED block); ree-v3 `d2104f88f4`, `experiments/v3_exq_963b_mech063ii_tonic_phasic_dissociation_retest.py` `:556-580` (F1), `:624-632` (successor requirement (a)).

## Problem

SD-105 is a LIVE closed-loop set-point controller on realised normalized E3 selection
entropy, and MECH-063 (ii)'s C1 reads a difference of arms in exactly that quantity, so the
controller manufactures its consumer's DV. V3-EXQ-963b armed it identically in all four arms
on the reasoning that a common lift cancels out of `dS_tonic`; the red-team refuted that and
the authoring session withdrew it -- a set-point controller applies a DIFFERENT lift per arm
precisely when arms start at different entropies. Verified against V3-EXQ-963a's own per-arm
data at `SEF_TARGET=0.12`: the controller would LIFT some arms and HOLD others on 4 of 5
seeds, and on seeds 23/29/37 it lifts exactly the TONIC-OFF arms while holding the TONIC-ON
arms -- compressing `dS_tonic` in the direction that destroys C1 (`:556-580`). The driver's
own R6 guard (`SEF_ARM_SPREAD_CEILING = 0.25` at `:735`, computed at `:1382-1400`) catches
this, which is the design's undoing rather than its defence: R6 failing routes to requeue, R6
passing means SD-105 was inert, so no outcome is productive. 963b landed UNQUEUED. The fix
its docstring names is to converge SD-105 ONCE during warmup and apply that single FROZEN,
SHARED multiplier across all arms in the read phase: a constant temperature offset that lifts
every arm off the floor without differentially compressing the contrast. SD-105 has no freeze
or share API today (`ree_core/regulators/selection_entropy_floor.py` exposes only `observe()`,
`apply_to_temperature()`, `reset()`, `get_state()`), so this is a substrate build, not a
config change. `claims.yaml` SD-105's `what_would_answer` was already
rewritten (2026-09-06) around the frozen form, and its `digestion_note` lists "the freeze/share
API is built or explicitly waived" as resolution step (2).

## API proposal

**(i) Converge-then-freeze.** Add `SelectionEntropyFloor.freeze()`: a one-way latch that
records `_frozen = True`, `_frozen_at_tick = self._lifetime_ticks`, `_frozen_source =
"converged"`, and leaves `_log_mult` at its converged value. After a freeze, `observe()`
still advances the diagnostic counters and the entropy EMA -- so a driver can see whether the
frozen multiplier HELD entropy at the floor -- but the integrator branch at
`selection_entropy_floor.py:296-313` is skipped. No `unfreeze()`: a one-way latch is the
auditable form. Optional `selection_entropy_floor_freeze_after_ticks: int = 0` (0 = off)
auto-freezes at `_lifetime_ticks >= N`, for a harness that cannot reach the agent at the
warmup boundary.

**(ii) Share.** Add `selection_entropy_floor_frozen_multiplier: Optional[float] = None`.
When set, the regulator is CONSTRUCTED already frozen (`_log_mult = log(m)`, `_frozen = True`,
`_frozen_at_tick = 0`, `_frozen_source = "config"`) and never integrates. This is the
arm-construction path: converge once on the warmup agent, read the multiplier out of
`get_state()`, build every arm of the contrast with that identical literal float. Setting both
`frozen_multiplier` and `freeze_after_ticks` is a `ValueError` (loud, not silent).

**(iii) Reporting.** `get_state()` (`:360-378`) gains `frozen: bool`, `frozen_multiplier:
Optional[float]` (None when unfrozen), `frozen_at_tick: Optional[int]`, `frozen_source:
"converged" | "config" | None`. The agent's `entropy_floor` control-vector dict
(`agent.py:12819-12833`) mirrors all four, so the per-cell manifest carries them and a driver
can ASSERT the multiplier is identical across arms instead of measuring how far it drifted.

## Invariants

1. **One-sidedness preserved.** A frozen multiplier is always `>= 1.0`; `< 1.0` raises
   `ValueError`. The floor may only ADD exploration (`:229-233`, `:305-306`).
2. **Cap honoured and still reported.** A value above `max_temperature_ratio` is rejected; a
   frozen value AT the cap must still report `saturated` True, so SD-105's uninformative-cell
   contract (`:338-343`) survives freezing.
3. **Bit-identical when off, and when on but unfrozen.** `use_selection_entropy_floor=False`
   instantiates nothing (`agent.py:1236-1258`); with the new knobs at defaults the live
   controller's trace must be unchanged -- verified DIFFERENTIALLY against `origin/main`, the
   way the original SD-104/SD-105 landing was, not asserted.
4. **MECH-094 untouched.** `simulation_mode=True` still returns the cached multiplier and
   advances nothing (`:275-277`); replay must never trigger a freeze nor move a frozen value.
5. **Freeze survives `reset()`.** Like the EMA and integrator (`:348-358`): a multiplier that
   unfroze at an episode boundary would reintroduce the V3-EXQ-779b episode-length confound.
   Extend `continuity_note` accordingly.
6. **Purity.** No RNG, no torch, no gradient -- unchanged regulator category.

## Files touched

- `ree-v3/ree_core/regulators/selection_entropy_floor.py` -- config dataclass `:171-197`,
  `observe()` `:256-315`, `get_state()` `:360-378`, new `freeze()`. Substantially the whole build.
- `ree-v3/ree_core/utils/config.py` -- knobs alongside `:4503-4519`; `from_dims` signature
  `:7432-7437`; assignment `:8866-8873`.
- `ree-v3/ree_core/agent.py` -- construction `:1236-1258`; telemetry `:12819-12833`; optional
  `Agent.freeze_selection_entropy_floor()`. Application site `:8741-8783` unchanged.
- `ree-v3/tests/test_flag_inertness.py` -- `PROBED` (cf. `use_selection_entropy_floor` at
  `:2330`). `test_flag_registry_is_current` (`:3221`) scans `use_*` / `*_enabled` only, so
  `selection_entropy_floor_freeze_after_ticks` evades it; register anyway -- three landings in
  a month left trunk red by skipping this (`chip-20260907-selection-entropy-floor-flag-registry`).
- `ree-v3/tests/contracts/test_sd104_sd105_burst_decay_and_entropy_headroom.py` -- extend the
  B-series (B1-B10, `:335-466`).
- Docs: `ree-v3/docs/substrate/SD-104-sd-105-phasic-burst-refractory-duty.md`,
  `REE_assembly/docs/architecture/sd_105_selection_entropy_headroom_floor.md`.

## Contract tests to write

- **B11 `test_freeze_latches_the_multiplier_and_stops_integration`** -- after `freeze()`,
  further `observe()` calls far below target leave `temperature_multiplier` bit-identical
  while `n_observations` advances.
- **B12 `test_frozen_multiplier_is_identical_across_two_independently_constructed_agents`** --
  the SHARE contract: same configured float, same emitted multiplier and same lifted
  temperature, on divergent entropy streams.
- **B13 `test_frozen_multiplier_below_one_or_above_cap_is_rejected`** -- one-sidedness and cap.
- **B14 `test_defaults_are_bit_identical_to_the_unfrozen_controller`** -- differential trace
  vs `origin/main`, both the OFF and the on-but-unfrozen paths.
- **B15 `test_freeze_state_survives_reset`**; **B16
  `test_simulation_mode_neither_freezes_nor_moves_a_frozen_multiplier`**; **B17
  `test_get_state_and_agent_control_vector_report_the_frozen_fields`**; **B18
  `test_frozen_at_cap_still_reports_saturated`**; **B19
  `test_frozen_multiplier_and_freeze_after_ticks_together_raise`**.

## How 963b's successor uses it

Per seed: warm the T0P0 baseline arm with the live controller; at the warmup boundary read
`get_state()`, assert `saturated is False`, take `m* = temperature_multiplier`. Construct all
four read-phase arms with `selection_entropy_floor_frozen_multiplier = m*`, and record `m*`,
`frozen`, `frozen_source`, `frozen_at_tick` per cell. **R6 then changes kind**: from a spread
TOLERANCE that self-routes requeue to a design ASSERTION -- `max(mult) - min(mult) == 0.0`
across the four arms of a seed, `frozen` True everywhere -- so a violation is a harness bug
(abort/ERROR), not a scientific outcome, and F1's "no productive outcome" trap is gone. The
frozen design's OWN validation is `claims.yaml` SD-105 `what_would_answer` leg (ii):
`dS_tonic` under the frozen multiplier must be paired-indistinguishable from `dS_tonic` with
the multiplier off. That needs a multiplier-OFF paired arm set (4 arms -> 8, or a cheaper
dedicated 2-arm probe), and it is the load-bearing half -- a run reporting only "headroom
restored" has certified its own subject.

## Open questions

1. **Per-seed or fleet-constant `m*`?** Recommend per-seed -- one constant across seeds
   absorbs seed-level confidence differences into a fixed offset.
2. **Which arm converges it?** Warm caches are per-arm (963b F5), so a T0P0-converged `m*`
   comes from an agent whose weights differ from the other three, and a more confident P1 arm
   may stay below `E_SAT_LOW` under it. The alternative -- `m* = max` over the four arms'
   independently converged multipliers -- keeps every arm off the floor at the cost of
   over-lifting T0P0. Not resolvable from the desk; measure it.
3. **Does raising the temperature at all compress `dS_tonic`?** If yes, the autopsy's second
   branch (re-derive R5's band) is the only one left. The API cannot answer this; 963c does.
4. **Keep or drop `freeze_after_ticks`?** Dropping it keeps the new surface to one float.
5. **Freeze mid-episode?** Boundary-only by convention, pinned by contract, not by code.
6. **Claim id:** amend SD-105, do not mint SD-105a -- its `what_would_answer` is already
   written for the frozen form.

**Separately owed, NOT designed here:** V3-EXQ-963b's C2 magnitude leg must be re-derived
against the statistic it actually routes on (the 4th-largest per-seed magnitude, 0.0087, a
2.3x shortfall against the 0.02 bar) or withdrawn -- `v3_exq_963b...py:582-592`.
