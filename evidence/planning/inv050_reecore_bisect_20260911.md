# INV-050 ree_core substrate bisect -- f810969..17befb8c

**Date:** 2026-09-11T17:24:29Z
**Chip:** `chip-20260910-gflag0205-inv050-reecore-bisect` (owed residual of GFLAG-0205, resolved)
**Question:** which of the 11 `ree_core` commits between `f810969` and `17befb8c` moves the
INV-050 measurement behind V3-EXQ-861e's seed-271 HIGH-arm collapse
(mean MEL 2.8999705e-05 -> 2.2980323e-05, factor 0.884)?

## Verdict

**The mover is `6293b23`** -- "MECH-091: wire task-completion and commitment-boundary-crossing
triggers into `phase_reset()`" (full sha `6293b2395248524f243364b49ea0ce52298f4200`,
2026-08-17). Its parent is `5f64a53f14bb67c54d4c3239807fadb490f3d36c`.

**It is NOT `76cbf84`**, the candidate the registry had been carrying.

## Method

861e's `ARM_3_HIGH_ON` agent + env config (`_make_agent` / `_make_env`, copied verbatim) replayed
as a short WAKE-ONLY rollout against each commit pinned with
`ree-v3/experiments/_lib/substrate_pin.py` (`pin_ree_core`), comparing the per-step MEL producer
stream (`agent.update_residue(...)["e3_prediction_error"]`) **bitwise** (`%.17g`, sha256).

Two commits produce the same hash <=> their default-config execution path is bit-identical for
this workload. Divergence onset localizes the bisect.

## Result -- one clean divergence point, on every probe

| probe | pre-`6293b23` | `6293b23` onward |
|---|---|---|
| seed 271, 4 ep | 84 steps, `8b4b9ca83a36cb2e` | 53 steps, `36c5f97af9395ef2` |
| seed 271, 14 ep | 195 steps, `beb3a95c235cda69` | 197 steps, `c4151e3e0b937695` |
| seed 7, 6 ep | 222 steps, `45aa06c7b2f442ec` | 221 steps, `3e8fc333c7c3ac96` |
| seed 42, 6 ep | 122 steps, `3ce87e0514beb9df` | 114 steps, `283b5efbbd59e492` |

- Bit-identical to `f810969`: `6f46a70`, `bbc69c4`, `93d5d98`.
- Bit-identical to `6293b23`: `68173a7`, `76cbf84`, `692f852`, `775eb55`, `1a4b6be`, `e5b46af`,
  `0911574` (= the `17befb8c` endpoint state for `ree_core`).

## Why `76cbf84` is excluded -- four independent ways

1. **By code.** It adds `E1Config.contextmemory_write_usage_balancing`, default `False`. With the
   flag off, `selection_scores = mean_scores` and `min_idx = selection_scores.argmin()` reduces
   exactly to the old `scores.mean(0).argmin()`; `write_usage_ema` is `None` and no buffer is
   registered, so `named_buffers()` and RNG consumption are unchanged.
2. **By config.** 861e's `REEConfig.from_dims(...)` call passes **no ContextMemory write knob at
   all**, so the flag was at its default in the run that collapsed.
3. **By prior experiment.** Control leg V3-EXQ-861h already found the ContextMemory write-address
   lock **not load-bearing** for measured MEL; the portfolio verdict says the collapse is "not the
   write-address lock" -- which always sat in tension with naming `76cbf84` as the candidate.
4. **By this bisect.** It is bitwise inert on every probe.

The same four arguments apply to `692f852` (the default-off `refractory` write-selection mode).

## Mechanism -- author-documented, and already actioned elsewhere

`6293b23`'s own commit message states it, at authoring time:

> this change legitimately alters E3 tick cadence (its entire purpose), which **shifts the RNG
> draw sequence for any downstream fixed-seed live rollout**, even ones conceptually unrelated to
> `beta_gate`/`phase_reset`.

It broke two unrelated fixed-seed magic-number pins the same day (`test_q081_pair_reach_check.py`,
`test_q081_pair_reach_check_stream.py`), filed as `chip-20260817-q081-boundary-pin-shift-mech091`
and closed 2026-08-18 by **re-pinning** the counts -- i.e. the project has already once accepted
this commit's effect as a seed-realization shift rather than a defect.

This does not contradict H1/V3-EXQ-861f ("reseed isolation", NOT supported): 861f isolated
**measurement** RNG (re-drawing calibration). `6293b23` shifts the **rollout** trajectory RNG
sequence, which a measurement-level reseed does not undo.

## Scope -- what this does and does not establish

**Does:** localizes the execution-path divergence across the 11-commit range to a single commit,
replicated on 3 seeds and 2 rollout lengths, and excludes the standing candidate.

**Does NOT:** re-measure `mean_mel` under the full 861e protocol (training, 10 calibration draws,
sleep). Attributing the exact 0.884 factor to `6293b23` still wants **one pinned confirmation
cell** -- the 861e protocol at `5f64a53f` vs `6293b23`, seed 271 -- which is a
`/queue-experiment` job, not a desk bisect.

**Reading it suggests, not established:** if confirmed, 861e's seed-271 movement is a
tick-cadence seed-realization shift of the same class as the q081 pins, i.e. **not** evidence of a
regression in the MEL mechanism -- which would retire the registry's standing hedge that
`f810969`'s >1.0 reading "rode the pre-repair bug".
