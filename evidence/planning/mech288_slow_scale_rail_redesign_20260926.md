# MECH-288 slow scale: magnitude-relative BOCPD trigger -- design (pre-build)

**Status: DESIGN, pre-build, red-teamed (section 9; findings folded in).** No `ree_core` file, claim field, queue entry or manifest was changed
while writing this. It is the design-first deliverable that substrate_queue row
`MECH288-SLOW-SCALE-BOCPD-RAIL-UNREACHABLE` requires before any `ree_core` edit, per the user's
governance decision rec-20260925-deedce42 / GFLAG-0474 option (a): *redesign the slow-scale BOCPD
rail detector-side with a magnitude-relative trigger*.

- Session: `igw-220-substrate-ready-mech288-slow-sca` (IGW-20260925-220, interactive, Mac)
- Written: 2026-09-26T11:19:15Z
- Against: ree-v3 `7f08512`, REE_assembly `af9a427719`
- Prior finding this answers: [`mech288_slow_scale_bocpd_rail_unreachable_20260924.md`](mech288_slow_scale_bocpd_rail_unreachable_20260924.md) (d46c032239)

## 1. What is actually broken -- three defects, not one

The 2026-09-24 record identified the absolute ~6.18 one-tick jump. Reading the detector again for
a fix shows that jump is one of **three independent** defects. Fixing only the one named in the
row title does not make the rail fire.

| # | Defect | Where | Consequence |
|---|---|---|---|
| D1 | **Absolute scale.** Short runs (n < 2) predict with `prior_var = 1.0` in raw `||z_goal||` units; the variance floor is `1e-6` absolute. | `event_segmenter.py:257-263` | On a stream whose values live in 0.04-0.26 and whose typical per-tick move is ~5e-4, a fresh run's predictive is ~2000 sd wide. Nothing is ever surprising to it. |
| D2 | **Scale-dependent implausibility cutoff.** The fast path tests `max(pred_log) < -20` on log-DENSITY, which shifts by `-0.5 ln var`. | `:303-312` | The cutoff means a different number of sigmas at every stream scale; with D1's broad young run always present it needs `d > 6.18` absolute. |
| D3 | **Dead posterior readout.** With constant hazard, `P(r_t = 0 \| x_1:t) == hazard` identically (the likelihoods cancel -- proved in the 09-24 record, sec. 1). | `:378-384` | `0.025 > 0.5` is never true. The Bayesian route cannot fire on ANY stream at any scale. This is a property of standard Adams-MacKay, not a bug in the port: BOCPD detections are read from the run-length posterior with a lag, never from `P(r_t=0)` at the current tick. |

## 2. What the in-agent z_goal stream actually looks like (measured, this session)

Probe: EXQ-830's live-z_goal configuration verbatim (`experiments/_lib/baselines/mech321_scale_resolved_probe`:
`env_kwargs`, `substrate_stack_flags()` incl. `z_goal_enabled=True`, `benefit_threshold=0.05`;
`use_event_segmenter=True`; explicit `agent.update_z_goal(...)` each step, kwargs-only), 3 seeds
(11/23/47) x 60 episodes x 24 steps, untrained agent, Mac torch 2.10.0. 3279 ticks total.

| seed | ticks | z_goal active | norm mean / max | slow fires (current) | fast fires |
|---|---|---|---|---|---|
| 11 | 1171 | 0.90 | 0.110 / 0.265 | **0** | 19 |
| 23 | 1213 | 0.96 | 0.081 / 0.186 | **0** | 17 |
| 47 | 895 | 0.54 | 0.044 / 0.137 | **0** | 10 |

The 09-24 finding reproduces live: 0 slow fires with a live stream on all three seeds.

**Structure of the stream.**

- **Its direction essentially never changes.** `cos(z_goal(t), z_goal(t-20))` has 1st percentile
  0.990-0.997. There is no "goal switch" in the direction of z_goal at this configuration (the
  untrained encoder's z_world shares a dominant direction). A direction-based detector would have
  nothing to find; the norm is the informative scalar here. (It is an open question whether a
  trained encoder changes this -- section 7.)
- **Its norm has two regimes, cleanly separated.** On decay-only ticks the relative per-tick change
  is exactly `decay_goal = 0.005`. On benefit-write ticks it is 0.17-1.8 (p99 0.17-0.30, max up to
  1.80) -- 35x to 360x the decay-tick move.
- **Writes come in short bursts** (median 3-4 ticks, max 10), 22 bursts over 3 seeds, **28-130 ticks
  apart** (p10/p50 onset gaps 28/63, 72/120, 83/130). That is Verdict 2's slow/schema range
  (~20-100 steps).
- **Every burst onset is within 3 ticks of an env-emitted `transition_type == "resource"` event
  (22/22).** The converse does not hold: only 32 of 105 resource events are followed by a write,
  because the benefit gate filters them.

So the stream DOES carry a slow-scale event that is independently groundable in env labels: the
onset of a goal-write burst after consummation. The detector cannot see it only because of D1-D3.

## 3. The redesign

Keep the claim's commitment literally: **BOCPD-Gaussian latent change-point on `||z_goal||`**, same
stream, same hazard (1/40), same top-k, same `min_segment_length` (15), same Gaussian
unknown-mean model. Change only the three scale/readout defects, each behind its own no-op-default
field so every piece can be ablated.

### 3a. Relative scale (fixes D1)

Maintain a running estimate of the stream's typical per-tick displacement,

```
s_t = (1 - a) * s_{t-1} + a * |x_t - x_{t-1}|        a = bocpd_scale_alpha (0.05)
```

updated **after** the tick's predictive is computed (predictive, not post-hoc). Fresh runs (n < 2)
and degenerate-variance runs predict with

```
prior_var_t = (k * max(s_t, rel_floor * |x_t|, eps))^2     k = bocpd_prior_scale_k (6.0)
```

and the run-variance floor becomes `1e-12` in place of the absolute `1e-6` (relative mode only; the
`rel_floor * |x|` term already bounds the prior variance away from zero on any non-zero stream).
The whole detector is then exactly scale-equivariant: multiplying the stream by 1000 gives
bit-identical fire ticks (measured).

### 3b. Scale-free implausibility backstop (fixes D2)

In relative mode, the fast path tests the **standardised residual** instead of log-density:

```
fire if  min_i (x - mu_i)^2 / var_i  >  z_cut^2      z_cut = bocpd_implausible_z (6.0)
```

-- "every live run hypothesis finds this observation more than 6 sd away". Same semantics as the
intended -20-nat rule, now meaning the same thing at every scale. Absolute mode keeps -20 nats.

### 3c. Lagged short-run readout (fixes D3)

Fire when the posterior mass on short run lengths exceeds the threshold:

```
strength_t = P(r_t <= L | x_1:t)        L = bocpd_readout_lag (3)
fire if strength_t > posterior_threshold (0.5, unchanged)
```

held off for `L + 1` observations after stream start AND after every implausibility reseed
(**burn-in**: immediately after either, every surviving run is short, so the mass is 1 by
construction -- without the guard this produced a spurious fire at tick 1 on every seed, and
repeat fires on onset+1..+3 that only `min_segment_length` was hiding). This is the standard way BOCPD detections are read out. `BoundaryEvent.posterior`
carries `strength_t`. **It is graded in principle but mostly saturated in practice:** on the
in-agent traces 20 of 21 delivered fires carry 1.0 (the backstop route). Do not read this build as
having made MECH-287's graded-broadcast commitment testable.

### 3d. Config surface (all defaults = current behaviour, bit-identical)

`EventSegmenterScaleConfig` (+ mirrored `Scale` fields, + pass-through at `hippocampal/module.py:335-350`):

| field | type | default | relative-trigger value |
|---|---|---|---|
| `bocpd_scale_mode` | str | `"absolute"` | `"relative"` |
| `bocpd_prior_scale_k` | float | 6.0 | 6.0 |
| `bocpd_scale_alpha` | float | 0.05 | 0.05 |
| `bocpd_rel_floor` | float | 1e-3 | 1e-3 |
| `bocpd_implausible_z` | float | 6.0 | 6.0 (relative mode only) |
| `bocpd_readout` | str | `"p0"` | `"short_run_mass"` |
| `bocpd_readout_lag` | int | 3 | 3 |

One ergonomic experiment-facing switch in `REEConfig.from_dims`:
`event_segmenter_slow_relative_trigger: bool = False` -> sets the slow scale's `bocpd_scale_mode`
and `bocpd_readout` together. **All three sites** (dataclass field, `from_dims` signature, and the
post-construction apply) -- `from_dims` silently swallows unknown kwargs (MECH-307 precedent).

The fast scale and every existing consumer are untouched at defaults.

**Relative mode is scoped to `input_stream="observation"` only** (red-team item 5, verified):
`EventSegmenter.__init__` builds BOTH streams' detectors from the same `Scale`
(`event_segmenter.py:435-438`), and the MECH-321 scale-resolved probe feeds the SAME
`current_z_goal` up to 8 times per candidate per tick on the rollout stream
(`hippocampal/module.py:1024-1045`). Repeated identical samples collapse run variance, so every
next real move becomes 'impossible': replaying each trace value 8x gives 1332 fires / 21624
(the `min_segment_length` ceiling). `_build_detector` therefore takes the stream and builds the
rollout detector absolute regardless of the scale's mode. Extending relative mode to the rollout
stream needs its own measurement first.

## 4. Measured behaviour of the redesign (offline, on the recorded in-agent traces)

Final config (k=6, a=0.05, z_cut=6, L=3, burn-in after start and every reseed), fed exactly as
`agent.sense()` feeds it (including the pre-seeding all-zero stretch, and with the detector reset
at every episode start as `agent.reset()` -> `reset_event_segmenter()` does), with
`min_segment_length=15`:

**What this table is and is not.** The write onsets are defined as a relative jump > 0.01 in the
SAME scalar the detector reads, so 21/22 is a **liveness demonstration** (the rail now reaches
the event the stream carries), not CONFIRMING (a) evidence. The env `resource` label is not fully
independent either -- writes are causally triggered by consummation, and 22-39% of ticks lie within
+-3/+-6 of some resource event, so chance alignment is high. Any MECH-288 test must carry the
claim's own rate-matched shuffled-label baseline (section 6).

| | current | redesign |
|---|---|---|
| write-burst onsets detected (3 seeds) | 0 / 22 | **21 / 22** |
| fires outside a write burst (+3 ticks) | 0 | **0** (also 0 of 52 raw fires with `min_segment_length` disabled) |
| onset-to-fire latency | -- | **0-1 tick** (17 at 0, 4 at 1) |
| fires within +-3 of an env `resource` event | 0 | 30 / 105 (ceiling set by the benefit gate) |
| route taken | -- | 15 via 3b backstop, 6 via 3c posterior |

**Each fix is load-bearing, and the band is not knife-edge:**

- Relative scale alone with the old `p0` readout fires only via the backstop (17/22).
- Posterior readout alone (no backstop, `z_cut=None`) at k=5-6: 21/22, 0 off-onset -- the Bayesian
  route works on its own once D1 is fixed.
- Sweep k in {3,4,5,6,8,12} x a in {0.02,0.05,0.2}: **k in [4, 12] at a <= 0.05 gives 20-21/22 with
  0 off-onset fires.** k=3 fails by firing every 15 ticks through decay stretches (a young run with
  a too-narrow prior tracks the geometric-decay trend better than the long run does). k=6 sits in
  the middle of the clean band.

**Synthetic nulls and positives** (2000 ticks each, same config):

| stream | fires | reading |
|---|---|---|
| white noise, level 0.1, sd 0.001 | 2 | ~1 per 1000 ticks |
| EXQ-757 smooth arm (level 5, sd 0.02) | 2 | stays near-silent where 757's smooth arm was |
| pure geometric decay (0.995/tick) | 0 | the in-agent between-write stream |
| EXQ-757-like planted levels (gaps >= 10) | 17 / 17 true cps hit | still fires where 757 fired |
| planted 10-30% relative level shifts at 0.1 scale | 14 / 14 hit | fires where the old rail cannot |
| same trace x1000 | identical fire ticks | exact scale invariance |

**Known hazard, stated rather than papered over.** A relative detector flags any move that is
surprising relative to the stream's own typical displacement. On streams with that property it
fires more: a random walk (sd 0.001) 74/2000, decay plus additive noise (sd 1e-4) 43/2000,
heavy-tailed t3 noise 32/2000. The in-agent z_goal has no additive noise between writes -- decay is
deterministic -- so in-agent fires coincide with write onsets **at `benefit_threshold=0.05`**. That
specificity is a property of this configuration's burst structure, not of the detector: benefit is
non-zero on ~40% of ticks (468/1171, seed 11), so a lower `benefit_threshold` or a
`z_goal_seeding_gain`/`drive_weight` > 1 turns the stream into exactly the noisy trend that fires
more. But a future caller feeding the slow
scale a noisy, trending stream (e.g. a trained-encoder z_goal, or the rollout stream) should expect
this, and **the false-positive ceiling for any MECH-288 test must be measured on that stream, not
imported** (see 6).

## 5. What this changes about what MECH-288 IS -- flagged for governance, not decided here

- The stream, model family and hazard are unchanged, so the claim's text ("BOCPD-Gaussian latent
  change-point on the slow scale (z_goal)") stays literally true in relative mode.
- **But the in-agent referent of a slow boundary is now concrete, and narrower than the claim
  wording.** At this configuration a slow boundary means "onset of a goal-write burst after a
  benefit-gated consummation", not "goal switch": the direction of z_goal never switches. Whether
  that counts as the "high-level task transition" MECH-288's CONFIRMING (a) names is a governance
  reading. This design does not take it.
- Circularity conjunct (4) of `what_would_answer`: env `transition_type == "resource"` is emitted by
  the env and is not a quantity the detector consumes; the detector reads `||z_goal||`, which the
  benefit signal drives causally. Causal chain, not derivation -- but a validation run should
  report alignment against resource events BOTH gated (followed by a write) and ungated, so the
  benefit-gate ceiling is visible rather than read as detector misses.

## 6. Falsifier-runnability trace (GOV-UNWRITTEN-1, /implement-substrate 3h)

**MECH-288, precondition (1) "boundary fires > 0 on BOTH scales" and CONFIRMING (a)/(b):**

- **EVENT** -- goal-write burst onset after consummation. Provided by env + GoalState **only at a
  live-z_goal configuration** (`z_goal_enabled=True`, `benefit_threshold=0.05`, explicit
  `update_z_goal` call per step). At `from_dims` defaults z_goal is None (09-24 Part 1, F1).
- **DV** -- slow-scale fire count; fire-to-env-resource-event alignment within the claim's +-2-tick
  tolerance (latency measured 0-1) **against a rate-matched shuffled-label baseline** (FALSIFYING
  (b)); false-positive rate on decay-only stretches.
- **INSTRUMENT** -- this build (relative trigger) + the per-tick BoundaryEvent queue already
  surfaced at `agent.py:6746`.
- **Shape: INERT at defaults, by design.** The shipped default is the current absolute detector
  (must be no-op). **The validation run MUST set `event_segmenter_slow_relative_trigger=True` AND
  the live-z_goal configuration above** -- either alone reproduces 0 slow fires.
- The successor to EXP-1388 must also carry the two GFLAG-0468 corrections folded into this row:
  the fast/inner scale's construction floor is measured in-agent (0.4-0.8% in Part 1; 1.1-1.6% here
  over 3279 ticks, 46 fires), not the stale ~15%; and the false-positive ceiling cannot anchor on V3-EXQ-757's
  C288_silence (non_contributory by construction) -- it must be measured on the in-agent decay-only
  stretches.

**MECH-287 (broadcast downstream of MECH-288 boundaries):** EVENT = a slow-scale BoundaryEvent
(now reachable); DV = broadcast count and `broadcast_strength` on slow-scale boundaries; INSTRUMENT
= `InvalidationTrigger.step` (existing). Runnable once the same two conditions hold. The graded
readout (3c) matters here: MECH-287's no-binary-threshold commitment was untestable while every
slow fire had posterior 1.0.

## 7. Open, not decided by this design

- **Episode length vs the slow timescale (red-team item 2d, verified).** `agent.reset()` resets the
  segmenter every episode (`agent.py:4515-4520`) while `GoalState` persists. At EXQ-830's 24-step
  episodes the outer index returns to 0 every 24 ticks, so Verdict 2's ~20-100-step slow segments
  cannot exist as segment ids whatever the detector does. A validation run must use episodes long
  enough to hold several slow segments (write-onset gaps measured 28-130 ticks). Whether the
  segmenter should reset on episode boundaries at all, given z_goal does not, is a MECH-288 design
  question for governance; this build does not change reset semantics.

- Whether a TRAINED encoder's z_goal switches direction, which would make a vector-displacement or
  direction observation worth adding. Not needed for the rail to fire; out of scope.
- Whether MECH-288's CONFIRMING (a) should be re-worded to "goal-write onset" in-agent (section 5).
- Alternatives considered and rejected: a raw relative-jump threshold without BOCPD (drops the
  claim's BOCPD commitment); log-norm observation (pure decay is still a trend in log space);
  per-tick displacement as the observation (fine for write onsets, but changes the stream the claim
  names); keeping absolute scale and only replacing the readout (D1 keeps the young run too broad
  for either route to fire).

## 8. Build plan once approved

1. `event_segmenter.py`: `Scale` fields; `_BOCPDGaussianDetector` relative mode, z-cut backstop,
   short-run readout, burn-in (start + every reseed); `_build_detector(scale, stream)` builds the
   rollout detector absolute. The absolute path stays the untouched existing code.
2. `hippocampal/module.py:335-350`: pass the new fields from `EventSegmenterScaleConfig` to `Scale`.
3. `utils/config.py`: `EventSegmenterScaleConfig` fields; `from_dims` knob with all three sites.
4. Contract tests (`tests/contracts/test_mech288_relative_bocpd.py`): default bit-identity against a
   recorded stream; D3 identity (`p0 == hazard`) still holds in absolute mode; scale invariance
   (x1000); planted relative shift fires within 1 tick; decay-only stream silent; burn-in suppresses
   tick-1 and post-reseed fires; rollout-stream detector stays absolute with the knob ON;
   `from_dims` knob actually reaches the slow scale (not swallowed).
5. Liveness (b2): ON vs OFF slow-fire count on a real in-agent rollout at the live-z_goal config.
6. Validation experiment via `/queue-experiment` (diagnostic, ON/OFF pair, live-z_goal config,
   episodes long enough for several slow segments, rate-matched shuffled-label baseline).

## Reproducing

Probe + analysis scripts were session scratch (not committed); they are ~60 + ~100 lines:
record `agent.goal_state.z_goal`, `obs benefit`, `info["transition_type"]` and per-tick
BoundaryEvents at the EXQ-830 configuration above, then replay `||z_goal||` through a standalone
port of `_BOCPDGaussianDetector` with the three changes switchable.

## 9. Red-team record (2026-09-26, adversarial pass on a different model, every leg re-verified)

| # | finding | verdict | disposition |
|---|---|---|---|
| 1 | `p0 == hazard` exact only up to top-k renormalisation (measured 0.025-0.025045); short-run readout saturates for L ticks after EVERY reseed, not just at start | MINOR | wording fixed; burn-in extended to every reseed (3c) |
| 2 | scratch port floored variance differently from the doc; bit-identity must be pinned against `event_segmenter.py`, not the port; `agent.reset()` resets the segmenter every episode | MINOR (+ 2d escalated) | doc floor corrected (3a); contract test pins ree_core; per-episode reset replayed (21/22 holds) and the timescale consequence raised in section 7 |
| 3 | onsets defined on the detector's own scalar -> 21/22 near-tautological; resource label causally coupled, chance alignment high | CONTESTED | reframed as liveness, not confirming evidence; rate-matched shuffled baseline made mandatory (sections 4, 6) |
| 4 | "0 off-onset fires" partly `min_segment_length` masking | MINOR | re-measured with the mask off: 0 of 52 raw fires outside a write burst |
| 5 | rollout stream inherits relative mode; repeated identical z_goal samples -> 1332 fires at 8x repeat, driving decomposition latch release | CONTESTED, BLOCKING for any EXQ-830-like config | relative mode scoped to the observation stream (3d) |
| 6 | specificity depends on `benefit_threshold=0.05` burst structure | CONTESTED | stated in section 4 |
| 7 | bit-identity holds only if the build keeps the 1e-6 floor, first-tick 1.0, `total<=0` branch, -20 nats, p0 in absolute mode | MINOR | build plan item 1 keeps absolute mode as the untouched code path |

MECH-287 tonic guardrail and the cross-scale rule: checked, no effect (<= 1 slow event per 15 ticks).
