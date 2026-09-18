# ARC-029 P1 lever calibration finding -- the MECH-108 sweep is inert at the trained operating point

- **Date:** 2026-09-18
- **Session:** `metaworker-science-20260917-arc029-p1p3` (science campaign `science-20260917-arc029-p1p3`)
- **Chip:** `chip-20260916-arc029-p1p3-redesign-queue`
- **Status:** BLOCKED pending a user design decision. **Nothing was queued.** No experiment script was landed.
- **Box:** `ree-cloud-5`, torch 2.13.0+cpu, python 3.10.12.

## Why this exists

The chip asked for the ARC-029 redesign that satisfies the claim's own non-degeneracy
preconditions P1-P3 with EXISTING levers -- specifically a threshold-side, precision-invariant
mode driver via the MECH-108 `BreathOscillator` `effective_threshold` sweep, per ARC-029's
`what_would_answer` in `docs/claims/claims.yaml`.

Calibration measurement shows **that lever cannot produce uncommitted windows at the operating
point a trained agent actually occupies.** The design is not queueable as specified. This note
records the measurements so the next session does not re-pay for them.

## The mechanism, confirmed at runtime (not just in source)

- `ree_core/heartbeat/clock.py` computes the sweep; `ree_core/agent.py:7388` reads
  `clock.sweep_amplitude if clock.sweep_active`, forwards it at `:9423` as
  `sweep_threshold_reduction`, and `ree_core/predictors/e3_selector.py:3770-3772` applies
  `effective_threshold = commit_threshold * (1.0 - sweep_threshold_reduction)`.
- **Confirmed live:** with `breath_period=60, sweep_amplitude=0.5, sweep_duration=30`, the
  selector recorded `effective_threshold` 0.4 off-sweep and 0.2 on-sweep, while
  `_running_variance` stayed pinned at 0.5 (`current_precision` 2.0) throughout.
  **The sweep is genuinely threshold-side and does not touch precision** -- P2's stated
  mechanism is real.
- `commitment_threshold` defaults to **0.40** (`ree_core/utils/config.py:1107`, on `E3Config`),
  and `variance_commit_threshold()` is the identity, so `commit_threshold == 0.40`.
- `committed = commit_variance < effective_threshold`, and in this config
  `commit_variance == e3._running_variance` (no `conditional_predictive_variance` supplied) --
  so commitment and precision really are the same scalar, exactly as P2 warns.

## The blocking measurement: running_variance collapses ~5 orders below the threshold

`_running_variance` is the EMA of the **world-forward prediction MSE**
(`e3_selector.update_running_variance`). Training that forward model collapses it:

| training recipe | post-train `rv` | `precision` | amplitude needed to uncommit |
|---|---|---|---|
| phased (P0 encoder warmup -> P1 frozen-encoder heads), `alpha_world=0.9` | 4e-6 .. 1.6e-5 | 6e4 .. 2e5 | > 0.99996 |
| phased, `alpha_world=0.3` | 1e-6 | 5.1e5 | > 0.999997 |
| **joint (063a-style, encoder + world-forward together)** | **7e-6** (already 5e-6 by ep 5) | 1.3e5 | > 0.99998 |
| world-forward NOT trained | 0.5 -> 0.33 -> 0.01 during eval | 2 .. 100 | **> 0.18 (workable)** |

Since `effective_threshold = 0.40 * (1 - a)`, pushing an agent at `rv ~ 1e-6..1e-5` uncommitted
requires `a > 1 - rv/0.40`, i.e. **a > 0.99996**. Measured directly:

| `sweep_amplitude` | `effective_threshold` observed | `committed_step_fraction` |
|---|---|---|
| 0.50 | {0.2, 0.4} | **1.0000** (no uncommitted windows) |
| 0.999 | {0.0004, 0.4} | **1.0000** |
| 0.99999 | {4e-06, 0.4} | 0.7600 (committed run 9.5, uncommitted run 3.0) |

**P1 is reachable only at `a ~ 0.99999`**, where `effective_threshold` (4e-6) sits at the same
order of magnitude as `commit_variance` itself -- which was measured **drifting ~5x within a
single eval run** (1.2e-6 -> 1.1e-5). Occupancy is then set by where `rv` happens to drift
relative to a fixed bar, not by the manipulation. Between `a=0.999` and `a=0.99999` occupancy
swings 1.00 -> 0.76.

**The claim's own calibration recipe is written against a stale operating point.** ARC-029's
`what_would_answer` gives worked amplitudes for `rv ~ 0.33` (`a > 0.18`) and `rv ~ 0.0054`
(`a > 0.986`); the `commitment_threshold` comment in `config.py:1100-1107` likewise assumes
"trained agents commit (variance ~0.33 < 0.40)". A trained world-forward model puts `rv` five
orders of magnitude below that.

**The claim's remedy ladder addresses the wrong failure direction.** `what_would_answer` says a
failing P1 "is met by arming `use_natural_commit_latch_hold`" (+ the two macro-program flags).
Those levers *sustain* commitment -- they were built for the V3-EXQ-460i fragmentation failure
(occupancy too short). The failure measured here is the opposite: **saturation at 100%
committed**, needing uncommitted windows. Arming them cannot help.

## Two further constraints, measured, that nothing documents

1. **`clock.reset()` zeroes `_breath_phase_step` on every episode reset**
   (`ree_core/heartbeat/clock.py`), and the sweep fires only at
   `phase_step >= breath_period - sweep_duration`. An episode shorter than that prefix
   **never sweeps at all** -- silently, with no error. An early probe here showed
   `effective_threshold == 0.4` at every amplitude for exactly this reason.
   `steps_per_episode` must span whole breath cycles.
2. **`e3_score_decomp_enabled` is a selector INSTANCE attribute** (`e3_selector.py:614`),
   **not** a config field. Setting `config.e3.e3_score_decomp_enabled = True` silently creates a
   stray attribute and the `effective_threshold` / `commit_variance` diagnostics are never
   recorded. It must be set on `agent.e3` after construction. (Same shape as
   `reference-reeconfig-from-dims-silent-kwargs`.)
3. `select_action` returns the held action on non-E3 ticks, so `last_score_diagnostics` latches.
   Measured latched:fresh ratio ~9:1 at `e3_steps_per_tick=10`. Any driver must clear the latch
   before each call and emit `n_latched_ticks`.

## P2 and P3 status (measured, for whoever resumes this)

- **P2 looks clean and the ceiling can now be re-derived from data.** At the collapsed operating
  point, `log10(current_precision)` was ALTERNATING 5.168 (sd 0.213) vs STATIC 5.225 (sd 0.233):
  a paired difference of **0.057 log10** against a within-arm sd of ~0.21-0.30. For scale, the
  V3-EXQ-063a fiat confound pinned precision at 2.0 (10^0.3) against ~10^4.7-10^5.3 here, a
  separation of **~4.4-5.0 log10**. A ceiling expressed in log10 space (order 0.3) would sit
  ~1.5x the within-arm sd and ~15x below the confound magnitude -- i.e. it would genuinely
  discriminate, which is what the chip asked for. Note the previously-recorded "0.50 ceiling vs
  ~1.97 log10 separation" figures do not match this operating point; re-derive, do not reuse.
- **P3 FAILS as currently parameterised.** At the pre-flight's recalibrated env
  (`hazard_harm=0.05`, `proximity_harm_scale=0.10`), harm/step measured **0.0025 - 0.0068** at
  the converged operating point -- below the 0.01 floor that makes the claim's pre-registered
  `0.002 harm/step` absolute bar a <=20% relative effect. (In the un-converged regime it ran
  0.013-0.063, above the floor.) This reproduces, and slightly worsens, the earlier
  0.0056-0.0136 measurement recorded on the chip.

## What is blocked, and why only a human can unblock it

Every route to a workable P1 changes the operating point, and therefore changes **what
"committed mode" means** for this experiment -- which in turn decides whether a null harm
difference is a genuine ARC-029 **falsification** or a **non_contributory** instrument failure.
That is the exact distinction the V3-EXQ-063a autopsy said was missing, so it is not a choice
this session may make by default. Options are set out in the decision chip
`chip-20260918-arc029-p1p lever-operating-point`.

## Provenance

Measured with a throwaway probe under the session worktree (not landed; not under
`experiments/`). No queue entry was written; no EXQ id was consumed
(`V3-EXQ-1056` was reserved and released). Prior record cited by the chip: EXQ-125
(weakens/mixed), V3-EXQ-227 / 630 / 063a (non_contributory).
