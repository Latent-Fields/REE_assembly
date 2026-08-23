---
title: "SD-MEL-CONSUMER: sleep.adaptive_mel_sleep_cadence"
parent: "Sleep & Offline Integration"
grandparent: Architecture
nav_order: 10
---

# SD-MEL-CONSUMER: sleep.adaptive_mel_sleep_cadence

**Claim ID:** SD-MEL-CONSUMER
**Subject:** sleep.adaptive_mel_sleep_cadence
**Status:** IMPLEMENTED
**Registered:** 2026-07-07
**Implemented:** 2026-07-07
**Depends on:** SD-017 (sleep-phase architecture; SWS/REM passes), MECH-285/272/275/273 sleep-aggregation cluster (present)
**Blocks:** INV-050 (retest), MECH-180 (v3_pending)
**Plan node:** sleep_substrate:GAP-5b (`REE_assembly/evidence/planning/sleep_substrate_plan.md`)
**Substrate-queue id:** SD-MEL-CONSUMER (`evidence/planning/substrate_queue.json`)

## Problem

The SD-017 sleep loop enters offline (sleep) mode on a **deterministic K-episode
schedule** and runs a **fixed** number of SWS schema writes
(`sws_consolidation_steps`) and REM attribution rollouts (`rem_attribution_steps`)
per cycle. Neither the entry timing nor the cycle duration reads any signal about
how much learning the preceding wake period actually demanded.

V3-EXQ-677 (MECH-180 novelty sleep-upregulation probe) measured
`cumulative_sws_writes` and `cumulative_rem_rollouts` across graded-novelty arms
and found them **pinned** -- SWS=80 / REM=60 with **zero cross-arm variance** --
because those counts are set entirely by config, not by novelty / prediction-error
load. MECH-180 ("novel / high-MEL episodes adaptively upregulate the learning drive
of sleep") is therefore **untestable** on the K-episode substrate and is held
`v3_pending`.

INV-050's third drive -- the **Model Error Load (MEL)** / learning-demand drive --
is the drive that "determines whether the overnight update phase is sufficient for
the error burden generated during waking." Its measurability precondition is
**demonstrated**: V3-EXQ-701c (confirmed `failure_autopsy_V3-EXQ-701c_2026-06-30`)
showed MEL (accumulated per-step e3 prediction error) is **measurable and monotone
in graded waking novelty** on a converged recon-only base (NONE 2.03e-5 < LOW < MED
< HIGH 2.71e-5; relative spread 0.33 > 0.25). What was missing was the **consumer**:
a scheduler that reads accumulated waking MEL and modulates the offline phase.

That consumer is this SD.

### Instrument-floor learning (from 701c)

`ABS_MEL_FLOOR = 1e-4` in the 701c measurability instrument was inherited from
701b's ~2e-3 PE regime and is **~5x the entire converged-base MEL magnitude**
(~2e-5). On a converged frozen world-forward, requiring an absolute between-arm MEL
*difference* of 1e-4 is structurally unreachable no matter how strongly novelty
modulates MEL. The consumer and its validation test-bed therefore use a **relative**
(scale-free) MEL response with only a small `relative_floor` (~1e-6) to guard against
divide-by-near-zero -- never a 1e-4-scale absolute spread gate.

## Solution

A new module `ree_core/sleep/mel_consumer.py` and a small amount of wiring.

### Read path (MEL accumulation)

MEL is the mean per-step **e3 prediction error** over the wake period -- the same
signal the 701c instrument reads. `REEAgent.update_residue()` (the canonical waking
post-action step) already computes `e3.post_action_update()` and surfaces its
`prediction_error` as `e3_prediction_error`. When `use_mel_consumer` is on and the
step is a **waking** step (`hypothesis_tag=False`), that per-step PE is fed to a
`WakingMELAccumulator` (running sum + count). No new encoder, no new latent field.

### Consumer (duration lever -- primary)

At episode end (`SleepLoopManager._run_cycle`), the consumer computes a **relative,
scale-free duration factor**:

```
mel   = accumulator.mean()                       # mean per-step waking PE this window
ref   = reference (fixed set-point, or slow EMA)  # guarded by max(ref, relative_floor)
factor = clamp(1 + mel_gain * (mel / ref - 1), duration_factor_min, duration_factor_max)
```

The cycle's `sws_consolidation_steps` and `rem_attribution_steps` are scaled by
`factor` (rounded, floored at 1) for the duration of `run_sleep_cycle()`, then
restored. Higher MEL (more novelty / prediction error during wake) -> a longer
offline phase -> more `sws_n_writes` + `rem_n_rollouts` -- exactly the DV V3-EXQ-677
found pinned. `mel_scale_sws` / `mel_scale_rem` select which lever(s) scale.

### Consumer (entry-timing lever -- secondary)

When `use_mel_entry` is on, `notify_episode_end` fires a cycle as soon as
accumulated MEL crosses `mel_entry_threshold` (with a K-episode ceiling as a
safety backstop), instead of firing strictly every K episodes. High-MEL wake
periods trigger sleep sooner. Default off; the duration lever is the primary
validated mechanism.

### Reference set-point modes

- `mel_reference_mode="fixed"` (default): a constant homeostatic set-point
  (`mel_reference`; 0.0 sentinel = auto-calibrate to the first cycle's MEL). Correct
  for the graded-novelty ablation -- between-arm MEL differences are preserved
  because the reference does not adapt within a run.
- `mel_reference_mode="ema"`: a slow EMA of per-cycle MEL (`mel_ema_alpha`). The
  biologically faithful long-run homeostatic set-point (sleep pressure relative to
  recent baseline). Available but not the ablation default (an in-run EMA would
  partly normalise away the between-arm signal the falsifier tests).

### Config (all no-op default; master switch OFF -> byte-identical)

| Param | Default | Purpose |
|---|---|---|
| `use_mel_consumer` | False | master switch |
| `mel_gain` | 1.0 | duration sensitivity (inert unless master on) |
| `mel_reference` | 0.0 | fixed MEL set-point (per-step PE); 0.0 = auto (first cycle) |
| `mel_reference_mode` | "fixed" | "fixed" \| "ema" |
| `mel_ema_alpha` | 0.1 | EMA rate for "ema" mode |
| `mel_duration_factor_min` | 0.5 | saturation clamp (lower) |
| `mel_duration_factor_max` | 3.0 | saturation clamp (upper) |
| `mel_relative_floor` | 1e-6 | guards ref ~ 0 (recalibrated from mis-scaled 1e-4) |
| `mel_scale_sws` | True | scale SWS duration |
| `mel_scale_rem` | True | scale REM duration |
| `use_mel_entry` | False | secondary entry-timing lever |
| `mel_entry_threshold` | 0.0 | accumulated-MEL entry threshold |

## Architecture Context

- **Distinct from GAP-5 / MECH-286 / SD-037.** The existing
  `sleep/sleep_onset_gate.py` (MECH-286 override-gated entry) is the SD-037
  arousal/homeostatic entry drive = `sleep_substrate:GAP-5` (V4-deferred). This SD is
  the INV-050 **third / learning-demand** drive = `sleep_substrate:GAP-5b`. They
  modulate the same offline phase from orthogonal signals (arousal vs MEL) and
  compose (the MEL duration factor applies to a cycle the MECH-286 gate permitted).
- Sits inside the SD-017 sleep-aggregation cluster (Phases A-E). It scales the
  *duration* of the existing SWS/REM passes; it does not add new offline content.

## What This SD Enables

- **INV-050 retest** -- the third-drive functional-sufficiency question ("does MEL
  drive adaptive sleep cadence?"), untestable while cadence was K-deterministic.
- **MECH-180** -- the adaptive-upregulation mechanism; the pinned V3-EXQ-677 DV
  (`cumulative_sws_writes` / `cumulative_rem_rollouts`) now varies with MEL.

## MECH-094 compliance

Compliant by construction. The consumer **reads** waking prediction error only
(gated `hypothesis_tag=False`) and writes nothing to memory during non-waking
states. It only changes *how many* existing SWS/REM passes run; those passes keep
their own MECH-094 tags (REM attribution replay runs `hypothesis_tag=True`). No new
memory-write path is introduced.

## Phased training

Not applicable -- the consumer adds no learned parameters / no new encoder head. It
reads an existing scalar (e3 PE) and scales existing step-count config. The
validation experiment still requires a **converged base** so the PE signal lives at
converged scale (per 701c), but that is a base-warmup requirement, not P0/P1/P2
encoder-head phasing.

## Related Claims

- INV-050 (three-drive sleep regulation; MEL is the third drive) -- `emergent_from: SD-017`
- MECH-180 (novelty-adaptive sleep upregulation) -- `depends_on: INV-050, MECH-121, MECH-122, MECH-120`
- SD-017 (sleep-phase architecture)
- MECH-286 / SD-037 (arousal entry; the SD-037 sibling drive, GAP-5, V4)

## Validation

V3-EXQ-718 (diagnostic; PROMOTES NOTHING) queued 2026-07-07
(`v3_exq_718_sdmelconsumer_adaptive_cadence_validation`): recon-only converged
base + graded-novelty arms (NONE/LOW/MED/HIGH) x 3 seeds with `use_mel_consumer=True`
+ 1 matched-novelty consumer-OFF control;
DV = `cumulative_sws_writes` + `cumulative_rem_rollouts` (the exact V3-EXQ-677 pinned
DV) + `mel_duration_factor`; PASS = high-MEL arms produce measurably more offline
updates, monotone across arms on >=2/3 seeds, with a `use_mel_consumer=False` control
arm confirming the 677 pinning reproduces. Recalibrated relative floor (~1e-6), not
1e-4. On PASS: /governance clears INV-050 (retest) and MECH-180 (v3_pending).
