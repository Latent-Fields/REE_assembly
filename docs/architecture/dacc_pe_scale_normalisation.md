---
title: "dacc-pe-scale-normalisation: adaptive-range normalisation of the dACC affective PE"
nav_exclude: true
status: implemented
status_asof: 2026-09-26
status_claim: MECH-268
---

# dacc-pe-scale-normalisation: normalise `dacc_pe` at its producer

**Substrate entry:** `dacc-pe-scale-normalisation` (`evidence/planning/substrate_queue.json`)
**Claim unblocked:** MECH-268 (dacc.conflict_saturation)
**Status:** IMPLEMENTED 2026-09-26, ree-v3 `c41f9d1` (design-first build, per user decision
`dec-20260923T185804-MECH-268`, option 2, `rec-20260925-02281b11`). Design red-teamed, revised, and
approved by the user before any `ree_core` edit. Record: ree-v3
`docs/substrate/SD-032b-amendment-dacc-pe-scale-normalisation.md`. Validation V3-EXQ-1089a: not yet
queued (chipped).
**Session:** `igw-219-substrate-ready-dacc-pe-scale-no` (IGW-20260925-219), 2026-09-26
**Depends on:** SD-032b (dACC adaptive control, IMPLEMENTED), MECH-258 (precision-weighted PE),
MECH-268 f_sat (IMPLEMENTED, `dacc_saturation_*`), SD-032a salience coordinator (IMPLEMENTED)
**Design context:** [`mech_268_dacc_saturation_form.md`](mech_268_dacc_saturation_form.md) (floor
analysis), `evidence/planning/failure_autopsy_V3-EXQ-1089_2026-09-25.md`

## Problem

MECH-268's saturation factor acts on the SD-032a mode register **only through its floor**
(`1/(1 + s*(W-G))`, 0.357 at the default `s=0.3`). The register reads `dacc_pe` against an absolute
critical value of about `external_task_bias = 1.0`. Whether the floor can release a stuck
`internal_planning` register is therefore decided by a coincidence between two independently chosen
numbers, and one of them -- `dacc_pe`'s operating scale -- moves with training and configuration:

| regime | `dacc_pe` (unsaturated) | source |
|---|---|---|
| untrained | p50 ~0.98 | form doc, Consumer B |
| 120-ep P0 warmup, seed 11 | p50 ~3.58 | form doc, probe 4 |
| V3-EXQ-1089 trained seeds 42-46 | p50 **2.12 / 3.21 / 4.18 / 5.61** (43,45,42,44) | 1089 autopsy |
| V3-EXQ-464d/467d config | ~16-17 | `salience_coordinator.py` comment |

1089's post-hoc floor-arm boundary replicated on 3/5 seeds; the two exceptions are both scale:
seed 43 (pe 2.12) releases even at `s=0.3`, seed 44 (pe 5.61) cannot release even at `s=0.5`
(`5.61 * 0.25 = 1.40 > 1.0`). **Any fixed floor is seed-fragile**, including raising the default to
0.5. The user chose to keep `dacc_saturation_strength = 0.3` and fix the scale at its source.

### Where the scale drift actually comes from

`DACCAdaptiveControl._affective_pe` computes

```
pe_u       = ||z_harm_a - z_harm_a_pred||          # raw affective PE (norm of z_harm_a if no pred)
prec_norm  = min(precision / dacc_precision_scale, 3.0)
pe_w       = pe_u * (1 + prec_norm)                # MECH-258 precision weighting
pe_capped  = min(pe_w, dacc_pe_cap)                # SD-034 closure clamp (None by default)
pe         = pe_capped * f_sat                     # MECH-268
```

Two independent factors drift:

1. **The precision gain `(1 + prec_norm)`** runs from ~1 untrained to its cap of 4 once E3's running
   variance converges (1089's pilot: "precision_norm 3.0 = capped", rv ~1e-6). This is MECH-258
   doing what it is specified to do.
2. **The raw affective quantity `pe_u`**, whose scale is set by the learned norm of the `z_harm_a`
   encoder's output -- an arbitrary representational unit. Across 1089's trained seeds precision is
   capped on every seed (manifest `per_seed_training.precision_norm = 3.0` on all 5), so the whole
   2.1-5.6 spread is `pe_u` in ~0.53-1.40. On 464d/467d `pe_u ~ 4`.

   **On 1089-class configs `pe_u` is not a prediction error at all.** `z_harm_a_pred` is written only
   by `E2HarmAForward` (`agent.py` `_harm_a_pred_prev`), which exists only under `use_e2_harm_a`; the
   1089, 463b, 468 and 729 drivers never set it, so `_affective_pe` takes its no-prediction branch
   (`pe_u = ||z_harm_a||`) on every tick. There the seed spread is the spread of the harm latent's
   magnitude.

The seed-fragility the decision targets is factor 2. Factor 1 is a claimed mechanism.

## Design

### The statistic: a slow running mean of the raw affective PE, divisively applied

```
# NEW, when dacc_pe_norm_enabled:
k = "pred" if z_harm_a_pred is not None else "nopred"  # which statistic pe_u is this tick
if not frozen:
    n[k]     += 1
    a         = max(dacc_pe_norm_alpha, 1.0 / n[k])    # bias-corrected warm-up
    scale[k]  = (1 - a) * scale[k] + a * pe_u          # running mean of pe_u
pe_u_n = dacc_pe_norm_target * pe_u / max(scale[k], dacc_pe_norm_floor)
pe_w   = pe_u_n * (1 + prec_norm)                      # MECH-258 UNCHANGED, applied after
pe_capped, pe = ... unchanged ...
```

Five choices, each with its reason:

**(1) Normalise `pe_u`, BEFORE precision weighting -- not `pe_w`.** Normalising the raw affective
PE removes the arbitrary representational unit of `z_harm_a` (the seed-fragile factor) and leaves the
precision gain intact, so MECH-258 keeps its meaning: an untrained, low-precision agent still sees a
small `dacc_pe`, a trained, high-precision one a large one. Normalising after precision would divide
the precision gain out on the slow timescale, silently turning MECH-258 into a transient-only effect
-- a claimed mechanism quietly removed by a calibration lever. Rejected for that reason.

**(2) A running MEAN, not a z-score, running max, or percentile.** `pe_u >= 0` and the consumers read
it as a non-negative magnitude against a positive threshold. A z-score is zero-centred (half the
ticks would present negative conflict to the register) and divides by an SD that is tiny in the tight
trained regime (1089 pilot p10/p90 3.78/4.40), amplifying noise. A running max is set by single
outliers, including the first-tick `||z_harm_a||` value. A percentile needs a buffer and buys nothing
a mean does not for a distribution this tight. A mean is the Carandini-Heeger normalisation pool in
its simplest form.

**(3) Slow timescale: `dacc_pe_norm_alpha = 0.001` (~1000 ticks), bias-corrected warm-up.** The drift
being removed is between training regimes and seeds, which persists across thousands of ticks. The
dynamics MECH-268 and the foraging signal carry live on 8-tick (saturation window) and ~20-tick
(`_pe_ema`, alpha 0.05) timescales. The normaliser must be at least an order of magnitude slower than
both, or it becomes a second habituation mechanism confounded with the one under test. The
`max(alpha, 1/n)` warm-up makes the first `1/alpha` updates an exact cumulative mean, so the estimate
is not dominated by its first sample.

**(4) The estimator reads `pe_u` only -- never the capped or saturated value -- and keeps one scale per
statistic.** If it read the saturated value, saturation would shrink the scale and the division
would restore the attenuation: the normaliser would undo MECH-268. If it read the capped value, it
would slowly undo SD-034's post-closure clamp the same way. The division is applied *before* the cap
and `f_sat`, so both still attenuate. Ticks where `z_harm_a_pred is None` compute `||z_harm_a||`, a
different statistic from `||z_harm_a - pred||`, so each gets its own running mean (`nopred` /
`pred`) and is divided by its own. **The first draft excluded no-prediction ticks from the estimate;
the red-team showed that on the 1089 config every tick is a no-prediction tick** (probe: 23 fresh
dACC ticks, 0 with a prediction), so the estimator would never have updated and the ON path would
have been a fixed 5x rescale -- inert calibration by hand. On an `use_e2_harm_a` config the
`nopred` scale sees only the first tick after each reset and the `pred` scale carries the operating
point; on a 1089-class config the reverse.

**(5) A floor on the divisor: `dacc_pe_norm_floor = 0.1` (raw `pe_u` units).** Divisive normalisation
amplifies a near-zero stream. In a harm-free regime `pe_u` can sit at noise level; dividing noise by a
noise-sized mean would present full-scale conflict to the register. Below the floor the transform is
linear (`target/floor * pe_u`), so a quiet stream stays quiet. 0.1 sits well below every measured
operating scale (lowest: untrained p10 ~0.27 raw at unit precision).

### The target

`dacc_pe_norm_target = 0.5` (units of raw `pe_u`, i.e. before the precision gain).

At steady state `pe_u_n ~ target`, so the unsaturated `dacc_pe` is `target * (1 + prec_norm)`:

| regime | precision gain | unsaturated `dacc_pe` | at s=0.3 floor (x0.357) |
|---|---|---|---|
| untrained (E3 `precision_init 0.5` -> gain 1.004) | ~1 | ~0.5 | ~0.18 |
| trained, precision capped (1089 seeds, 464d/467d) | 4 | **~2.0** | **~0.71** |

With target 0.5 and a capped-precision agent, the release boundary on the `s=0.3` rung ladder
(`1.0, .769, .625, .526, .455, .400, .357` x 2.0 = `2.0, 1.54, 1.25, 1.05, 0.91, 0.80, 0.71`) falls
between `excess = 3` and `excess = 4` -- mid-ladder, with ~29% headroom below the ~1.0 critical value
at the floor, instead of seed 44's 40% overshoot above it. **This boundary is the same for every
trained seed**, which is the property the substrate entry's failure-record target asks for.

**The critical value is not 1.0 in general.** The internal_planning-vs-external_task margin is
`external_task_bias + drive - dacc_pe - dacc_foraging - 0.5*choice_difficulty - aic_salience` (plus
any pACC term); it collapses to ~1.0 only in the trained 1089 regime, where foraging is 0.002-0.2 and
difficulty is small (seed 42: release fraction 0.239 vs fraction of ticks with post-saturation pe
below 1.0, 0.261). An **untrained** agent already sits in `internal_planning` on 45/46 fresh ticks
today, because `choice_difficulty` (median 3.0) outweighs the bias -- so the normaliser does not
change the untrained regime's mode either way, and the first draft's "untrained stays external_task"
regression row was wrong and is withdrawn (red-team finding 4). Placement (1) rests on MECH-258
preservation alone.

**Red-team simulation of this estimator on 1089's per-tick SATOFF streams** (cold start, alpha 0.001,
1/n warm-up, `pe_u = pe_unsat/4`): normalised unsaturated `dacc_pe` p50 **2.07 / 1.98 / 2.01 / 2.19 /
2.21** (seeds 42-46) against raw 4.18 / 2.12 / 5.61 / 3.23 / 3.27; fraction of ticks with the
s=0.3-floor value below 1.0 = **1.00 / 1.00 / 1.00 / 1.00 / 0.99** against raw 0 / 1.00 / 0 / 0.22 /
0.09. That is the failure-record target stated as a number.

Target is not tied to `external_task_bias` at run time. The red-team recommended expressing it as a
ratio of `external_task_bias` to remove the "move the target when you move the bias" footgun; not
adopted, because the dACC module does not see the salience coordinator's config, the plumbing that
would make it do so is the start of option 3 of the decision (which was not chosen), and the relation
is not a single-threshold one (difficulty and foraging enter too). The relation
`target * 4 * floor(s) < critical < target * 4` for capped precision is recorded here and in the
config comment instead.

### Scale-invariance property (the contract the build must satisfy)

For any constant `k > 0` with the scale above the floor, multiplying the whole `pe_u` stream by `k`
leaves the normalised output stream unchanged (exactly, once the estimator has warmed up on the scaled
stream). This is what "stable operating scale across seeds" means operationally, and it is testable
without training.

### What it deliberately does NOT do

- **It does not change `f_sat`** -- form, referent, rung set or floor. `dacc_saturation_strength` stays
  0.3. The count-vs-run defect in the form doc is untouched and still waits behind the floor.
- **It does not remove within-regime structure.** Phasic PE excursions above/below the running mean
  pass through proportionally; only the slow operating point is fixed.
- **It does not make the Shenhav EVC consumer responsive.** Normalised `pe` flows to
  `control_required` too (normalising at the producer means every consumer sees one signal), which
  changes the effort term's magnitude when ON, but that consumer's argmin-invariance is the effort
  proxy's problem (SD-032b amendment `4cce9b8`), not the scale's.
- **It does not fix 1089's other readiness gaps** (fresh-tick-denominated eval, per-seed headroom,
  disjoint pilot). Those belong to V3-EXQ-1089a's design.

## Implementation plan (default-off, three config sites)

| site | change |
|---|---|
| `DACCConfig` (`cingulate/dacc.py`) | `dacc_pe_norm_enabled: bool = False`, `dacc_pe_norm_target: float = 0.5`, `dacc_pe_norm_alpha: float = 0.001`, `dacc_pe_norm_floor: float = 0.1` |
| `DACCAdaptiveControl` | buffers `_pe_norm_scale` [2] and `_pe_norm_count` [2] (index 0 = `nopred`, 1 = `pred`), **registered unconditionally** and never updated when OFF, with a `_load_from_state_dict` override that fills them from the live module when a loaded dict lacks them. So: an ON-trained snapshot strict-loads into an OFF arm and vice versa (1089a needs a normaliser-OFF arm off a shared snapshot -- red-team finding 2; conditional registration made that impossible), and every pre-existing checkpoint without the keys still strict-loads. `freeze_pe_norm(frozen=True)` runtime method; `pe_norm_scale` property; `reset()`, `reset_episode_pe()` and `reset_outcome_history()` do **not** clear the scale (it is a cross-episode operating-point estimate, not episode state) |
| `_affective_pe` | the transform above, between `pe_u` and the precision gain. OFF path is the literal existing expression |
| `forward()` bundle | when ON only: `pe_prenorm_unsaturated` (raw `pe_w` pre-norm, pre-cap), `pe_norm_scale` (the divisor used this tick), `pe_norm_updates` (the count for this tick's statistic, so a readiness gate can assert the estimator actually moved). OFF bundle keys unchanged |
| `REEConfig` (`utils/config.py`) | the four fields, `from_dims()` signature entries, and assignments -- all three sites (from_dims swallows unknown kwargs; MECH-307 lesson) |
| `REEAgent.__init__` (`agent.py`) | propagate the four knobs into `DACCConfig` next to the `dacc_saturation_*` block |
| `tests/test_flag_inertness.py` | register `dacc_pe_norm_enabled` in PROBED with an ON/OFF probe |

`dacc_pe_cap`, when a closure sets it, is compared against the post-precision value, which is in
normalised units when ON. `pe_cap_after_closure` defaults None; a design that sets it with the
normaliser ON should size it in normalised units.

### Contract tests (`tests/contracts/test_dacc_pe_scale_normalisation.py`)

1. **OFF is byte-identical**: bundle values and keys equal a build without the knobs over a scripted
   stream, and the norm buffers stay at zero.
2. **Scale invariance**: streams `k * x` for `k in {0.5, 1, 3.6, 16}` give normalised outputs equal to
   within float tolerance after warm-up.
3. **Steady state**: a constant `pe_u` stream converges to `target * (1 + prec_norm)`.
4. **Saturation not undone**: with a filled same-class FIFO, `pe == target*(1+prec)*floor(s)`, and the
   scale is identical to the saturation-OFF run on the same stream (estimator reads pre-saturation).
5. **Cap not undone**: with `dacc_pe_cap` set, the scale matches the cap-free run.
6. **Floor**: a stream below `dacc_pe_norm_floor` maps linearly (`target/floor * pe_u`), not to target.
7. **Per-statistic scales**: an all-no-prediction stream (the 1089 shape) updates the `nopred` scale
   and converges; a mixed stream keeps the two scales separate.
8. **Persistence**: `reset()`, `reset_episode_pe()`, `reset_outcome_history()` leave the scale;
   `state_dict` round-trip into a fresh ON module restores it (strict load); ON snapshot -> OFF module
   and a key-less (pre-build) dict -> ON module both strict-load; `freeze_pe_norm()` stops updates.
9. **Three-site plumbing**: `REEConfig.from_dims(dacc_pe_norm_enabled=True, ...)` reaches
   `agent.dacc.config`.
10. **Seed-spread property** (the failure record, synthetic): four streams at the 1089 seeds'
    measured `pe_u` levels (2.12/3.21/4.18/5.61 divided by the capped gain 4) all put the `s=0.3`
    release boundary on the same rung.

### Liveness (skill Step 5 b2)

Live consumer: `SalienceCoordinator.tick()` reads `dacc_bundle["pe"]` into `dacc_pe` (affinity and
salience paths) and `foraging_value`. The probe drives a real `REEAgent` rollout ON vs OFF and must
show `salience._input_signals["dacc_pe"]` differ, and -- on a config whose raw `pe_u` is far from the
target -- the operating-mode vector differ.

## Falsifier-runnability trace (GOV-UNWRITTEN-1)

MECH-268's registered purpose: saturation lets a stuck mode register relax without an explicit closure.

- **EVENT** -- a trained agent sitting in `internal_planning` while one outcome class recurs (the FIFO
  fills). Provided by the existing substrate on a trained agent (1089: SATOFF occupancy 1.0 on every
  seed). Present.
- **DV** -- release of `internal_planning` occupancy (argmax of the soft mode vector) at the floor arm,
  and the floor-arm boundary contrast `s=0.5` vs `s=0.3`. Present and recorded by the 1089 driver.
- **INSTRUMENT** -- the 1089 driver's per-arm release fractions. Present.
- **Status: INERT at the shipped default, by construction.** (Note: on this config the normalised
  quantity is the harm-latent magnitude, not a prediction error -- see "Where the scale drift comes
  from".) With `dacc_pe_norm_enabled=False` nothing
  changes and the DV stays seed-fragile. The configuration at which the DV CAN move uniformly is
  `dacc_pe_norm_enabled=True` with the default target 0.5 at `s=0.3`, on a precision-capped trained
  agent. V3-EXQ-1089a must run that configuration (and should keep a normaliser-OFF arm to show the
  fragility it removes). Three carry-overs from the red-team for 1089a: **freeze the scale at eval
  start** (`freeze_pe_norm()` after loading the snapshot) -- P0 warms it over ~6000 training steps on
  TRAIN_HAZARDS=3, but eval runs on EVAL_HAZARDS=6 and latched seeds get only 138-301 fresh ticks, so
  an unfrozen estimator would drift by different amounts per seed and let the seed-inconsistency back
  in; **log `pe_norm_scale` at snapshot and per arm** and gate readiness on `pe_norm_updates > 0`;
  and add the `dacc_pe_norm_*` keys to the driver's `_config_slice` so the arm cell hash changes.
  Also expect a small negative bias in the first ~8 ticks after each `agent.reset()` (the `z_harm_a`
  norm ramps up from ~0.3). Under the normaliser the prediction becomes sharper and falsifiable per seed:
  the `s=0.3` floor arm releases on every trained, ready seed.

## Engineering notes (ML parallels -- counsel, not authority)

- **Divisive / running normalisation** (Carandini & Heeger 2012; batch-renorm and PopArt-style running
  statistics in RL value targets, van Hasselt et al. 2016). The engineering hazard PopArt exists for is
  exactly this one: a downstream threshold or learning rate calibrated to a target whose scale drifts.
  REE's adaptation differs: there is no learned downstream weight to rescale, so only the "Art"
  (adaptive rescaling) half applies, and it is applied to a control-plane signal, not a regression
  target.
- **Known failure modes defended**: amplification of a near-zero pool (divisor floor); the normaliser
  absorbing the very modulation under test (estimator reads pre-cap, pre-saturation `pe_u`; timescale
  >= 10x slower than the fastest dynamics it must not touch); cold-start bias (warm-up); checkpoint
  loss of running statistics (buffers).
- **Biological grounding**: adaptive coding of prediction error to the range of recent outcomes --
  Tobler, Fiorillo & Schultz 2005 (dopamine PE scaled to the expected reward range); Diederen & Schultz
  2015 (PE scaling to reward variability in humans); Padoa-Schioppa 2009 (range adaptation in OFC
  value coding). These support scaling PE to the recent RANGE of the *raw error*, while leaving
  separately-computed gains such as precision in place -- which is placement choice (1). **This
  grounding applies only on `use_e2_harm_a` configs.** On 1089-class configs the normalised quantity is
  the harm-latent magnitude, and the justification is the engineering one (removing an arbitrary
  representational unit), not range-adapted PE coding.

## Red-team record

Cross-model red-team (fable; draft on Opus 5.5), 2026-09-26, read-only against the live tree and the
1089 manifest. Verdict on the first draft: **UNSOUND as written, SOUND-WITH-FIXES after two changes.**
All findings verified by this session before revision.

| # | finding | class | disposition |
|---|---|---|---|
| 1 | Estimator skipped no-prediction ticks; the 1089 config has no `E2HarmAForward`, so every tick is one -> scale never updates, ON = fixed 5x rescale | BLOCKING | FIXED: one running mean per statistic (`nopred` / `pred`); `pe_norm_updates` exposed; grounding caveat added |
| 2 | Buffers registered only when enabled + shared snapshot + strict load cannot host a normaliser-OFF arm | BLOCKING | FIXED: unconditional buffers + missing-key-tolerant `_load_from_state_dict` |
| 3 | Numerics check out once (1) lands: precision capped on all 5 seeds; untrained gain 1.004; simulated p50 1.98-2.21, floor-release 0.99-1.00 on every seed | ADVISORY | recorded above |
| 4 | "Untrained stays external_task" row false (`choice_difficulty` already drives untrained agents to `internal_planning`); critical value is a multi-term margin | ADVISORY | row withdrawn, margin stated |
| 5 | Train/eval scale shift, latched seeds cannot re-warm | ADVISORY | 1089a carry-over: freeze at eval, log, readiness gate |
| 6 | Other consumers: only salience, `control_required`/`effort_term`, and `_pe_ema` read `pe`; 17 drivers read `pe_unsaturated` with the flag OFF; no test pins dACC state_dict keys | ADVISORY | no change; 1089a `_config_slice` note |
| 7 | Target as a ratio of `external_task_bias` | ADVISORY | not adopted (reason in "The target") |
