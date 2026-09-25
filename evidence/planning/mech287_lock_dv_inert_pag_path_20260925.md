# MECH-287 lock DV (option C) is INERT against the MECH-287 manipulation: REFUSED at /queue-experiment Step 2.5d

- Session: `orch0925-mech287-lockdv` (a subagent of orchestrate-20260924-breakthrough)
- Chip: `chip-20260925-mech287-lock-dv-experiment` (/queue-experiment)
- Governing decision: user option C, rec-20260925-b23d15b9 (claims.yaml MECH-287 ADDENDUM 2026-09-25)
- Substrate read: ree-v3 origin/main `2ce89ce1b9` (the instrument commit `13c3d3a54b` is an ancestor)
- Written: 2026-09-25T07:52:44Z
- **No script written. No queue entry. No EXQ id reserved.**

## 1. What the step asks, and what fails

Step 2.5d asks whether the falsifier's EVENT, DV and INSTRUMENT exist and can MOVE. Option C made the DV
the lock itself: freeze duration, lock persistence and time-to-first-release (censored at episode
end), on a comparator that reproduces the V3-EXQ-475 lock. EVENT, DV and INSTRUMENT all exist. Freeze
duration and time-to-first-release are not stored in `PAGEpisodeRecord`, but a driver can poll them per
env step from `pag_freeze_gate.last_output`. The failure is a fourth element, the one family 1 of the
red-team table names: **the manipulation has no path to the DV.** The shape is INERT: the lock cannot
be moved by the thing the claim says releases it.

## 2. Source trace (verified at `2ce89ce1b9`)

1. **PAG exit reads three inputs, and none of them is downstream of anchor invalidation.**
   `PAGFreezeGate.tick()` releases on `z_harm_a_norm < theta_freeze * override_factor * gaba_tone`
   (`ree_core/pag/freeze_gate.py`, entry/exit block).
   - `pag_z_norm` = `||z_harm_a||` (`agent.py` ~10952-10983; the LPB and MECH-219 redirect branches
     are off in this lineage).
   - `z_harm_a` = `AffectiveHarmEncoder(harm_obs_a, harm_history)`, blended with its own previous value
     (`latent/stack.py` 1610-1665). Its inputs are environment observations only, with no hippocampal
     input.
   - `gaba_tone` is constant at 1.0. `set_gaba_tone` has no caller anywhere in `ree_core`.
   - `override_signal` is 0.0 because `BroadcastOverrideRegulator` (SD-037) is not constructed in this
     lineage.
2. **While frozen, the emitted action is forced to the no-op class, whatever E3 selects.** The
   PAG constraint is applied at the action-constraint site AFTER selection (`agent.py` ~11009-11030).
   The SD-058 escape hatch (`instrumental_avoidance`) is not constructed. On non-E3 ticks
   `select_action` returns `_last_action` (`agent.py:8121`), which is that same no-op.
3. **The MECH-287 chain terminates upstream of that constraint.** The chain runs broadcast ->
   `apply_invalidation_broadcasts_to_regions` -> `anchor_set.mark_inactive` -> the
   `use_vs_commit_release` hook (`agent.py` ~7942-7959), which calls `beta_gate.release()`. That
   releases the E3 COMMITMENT, not the PAG freeze. A fresh E3 selection then gets overwritten by the
   freeze no-op.

So during a lock there is **no path** from trigger / accumulator / anchor reset to any input of the
PAG exit. The only routes by which the arms could differ on the lock DV are:
(a) **warmup-trajectory divergence.** The arms act differently while unfrozen in warmup, so the harm
encoder is trained on different data and `||z_harm_a||` differs at eval. That is a training-history
confound, not online anchor invalidation.
(b) **pre-commit behaviour at episode start.** The data below show there is no pre-commit window in
this regime.

Either way a positive result would be unattributable to MECH-287. A null result is fixed by
construction, which would make it a vacuous "FALSIFYING" reading.

## 3. The recorded lock, re-read (V3-EXQ-475 episode log)

`evidence/experiments/v3_exq_475_sd036_decay_unlocks_exq471/..._20260422T173839Z_episode_log.json`, all
3 seeds x 5 eval episodes x 200 steps:

- **Action class 0 on every eval step of every episode**, from t=0. The freeze commits on the
  episode's first gate tick, so the pre-commit window is zero.
- **The positions show what "frozen" means in this substrate.** Seed 0 ep 0 goes
  (6,3)@t0 -> (5,3)@t1 -> (4,3)@t2 -> (3,3)@t3 -> (2,3)@t4 -> (1,3)@t5 and then stays put. The same
  pattern holds on every episode inspected: one cell per step toward row 1, then pinned.

## 4. Secondary finding (a substrate defect, independent of MECH-287): the freeze "no-op" is UP

`REEConfig.pag_freeze_noop_action_class` defaults to `0` (`utils/config.py:7119`). Its comment says
this is "typically a stay-in-place action in CausalGridWorldV2". It is not.
`CausalGridWorldV2.ACTIONS = {0: (-1,0) up, 1: down, 2: left, 3: right, 4: (0,0) stay}`
(`environment/causal_grid_world.py:247-248`). Every MECH-279 freeze under default config therefore
drives the agent UP into the top wall instead of holding it still. SD-099 defensive orienting
deliberately reuses the same knob, so it inherits the defect. This bears on MECH-279's own evidence
and on how any "catatonic lock" reading is interpreted: the lock's location is set by the wall, and
its z_harm_a exposure is whatever the top row delivers. It is recorded here and flagged, not fixed:
correcting it is a behaviour change that needs its own /implement-substrate pass and makes
freeze-gate runs non-comparable across the fix.

## 5. Lineage-scale probe: attempted, abandoned for cost

A throwaway probe was attempted: the 1097 helpers, A_BOTH_OFF, seed 0, 60 warmup + 5 eval, 2 threads.
The question was whether today's substrate still reproduces the lock. At 12.5 min wall-clock it had
not passed warmup episode 20, so it was stopped: the Mac is shared, and a smoke test must stay well
under 10 minutes. At 2 warmup episodes `||z_harm_a||` was ~0.35, below the 0.4 duration input
threshold, with no commits and short episodes.
**Whether the lock reproduces on today's substrate is UNMEASURED.** That is a cannot-determine result,
not a negative one. It does not change the Step 2.5d conclusion, which rests on source plus the
recorded 475 log. It does bear on sizing: the 1097 driver's "~20 min per seed" lineage estimate is
off by at least an order of magnitude on today's substrate (5 arms x 3 seeds would be many
worker-hours).

## 6. The decision owed (it changes what gets measured, so this session stopped)

- **A. Re-anchor the lock DV on a quantity the anchor chain CAN reach.** Examples: E3 commitment
  perseveration (beta-gate elevated duration, time-to-commit-release), or avoid-mode monostrategy
  (the EXQ-471 regime, `use_pag_freeze_gate=False`). This drops the PAG freeze as the DV. It is the
  closest to what MECH-287's functional_restatement actually argues ("the proposer keeps drawing
  trajectories from the original anchor").
- **B. Build the missing path**: a MECH-287 broadcast / anchor reset -> PAG exit coupling, e.g. a
  broadcast-driven raise of `exit_threshold` analogous to SD-037's override. This is a claim-level
  architectural commitment (LC phasic -> vlPAG) and needs /implement-substrate plus a design doc. Until
  it exists, the PAG lock is outside MECH-287's reach.
- **C. Accept that the 475 lock is not a MECH-287 phenotype.** MECH-287's "EXQ-475 unlock" falsifier
  would then be withdrawn, and only the four-arm dissociation on a reachable readout would remain.

In every option, fix `pag_freeze_noop_action_class` (0 -> 4 for CausalGridWorldV2, or an
env-derived default) before any freeze-gate run is read behaviourally.

EXP-0371 stays blocked. The re-scoped DV exists, but it is INERT against the manipulation.
