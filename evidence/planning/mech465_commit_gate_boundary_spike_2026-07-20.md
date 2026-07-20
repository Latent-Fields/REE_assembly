# MECH-465 stage-1 scoping spike: is a commit-gate BOUNDARY REGIME reachable by configuration?

- **Date:** 2026-07-20T20:08:34Z
- **Session:** `angry-gauss-b9d787` (MECH-465 commit-gate boundary spike)
- **Type:** SPIKE (`complex (probe-gated)` -> resolved). No experiment queued, no queue entry, no script in `ree-v3/experiments/`.
- **Substrate:** ree-v3 @ `d542f68cc7`
- **Claim:** MECH-465 (`candidate` / `substrate_conditional`)

## Verdict

**THIRD BRANCH.** The margin half of the boundary condition is reachable by pure
configuration; the usability half is **not**. Specifically:

| Condition | Reachable by config? |
|---|---|
| `commit_variance` within ~2x of `effective_threshold` (the stated definition) | **YES** -- `commit_threshold` ~0.0075-0.012 vs default 0.40 gives margin 1.2-1.95x |
| Commit rate away from BOTH 0 and 1 **across the urgency grid** (the stated precondition) | **NO** -- the gate is a step function; at most one grid level is non-saturated |

So MECH-465 is **not** answered by "set a smaller threshold". The gated quantity's
**dispersion is structurally too small for the manipulation to grade it**, and that
is a property of the signal, not of the threshold.

This routes to `/implement-substrate`, but to a **small, well-scoped build** (SD-063
wiring), not to the large z_world warmup. See Routing.

## Method

Direct probe of the live gate, `ree-v3` @ `d542f68cc7`. Agent/env construction copied
from `v3_exq_785a` (`CausalGridWorldV2(hazard_harm=0.5)`, harm + affective-harm streams
on, SD-056 contrastive candidates, finer channel gating). Per-tick `_running_variance`
recorded; 1500 ticks seed 0, 800 ticks seed 1.

**Design economy worth reusing.** The gate is a pure comparison of two recorded
scalars, so recording `_running_variance` per tick lets the commit rate for *any*
candidate `commit_threshold` x urgency combination be computed **offline from one
run**. The whole lever sweep cost one probe, not one run per candidate. The
`precision_ema_alpha` sweep was likewise done by inverting the EMA
(`e_t = (rv_t - (1-a)rv_{t-1})/a`) to recover the raw per-tick PE-MSE and
re-simulating -- no re-run.

Probe script: session scratchpad (not landed; it is a spike instrument, and
`/queue-experiment` owns anything that belongs in `experiments/`).

## Findings

### 1. The probe-vs-run discrepancy is a WARMUP-TRANSIENT artefact -- reconciled exactly

The open discrepancy was: the 785a header (lines 96-98) reports a 600-tick probe with
commit rate falling **1.000 -> 0.889**, while the scored run gave **0.9968 -> 0.9932**
(span 0.0099). Reconciled by computing commit rate over windows of a single run:

| window | u=0.04 | u=0.10 | u=0.16 | u=0.22 | u=0.28 | u=0.34 | span |
|---|---|---|---|---|---|---|---|
| ticks 0-60 | 0.917 | 0.714 | 1.000 | 0.786 | 0.900 | 0.700 | 0.300 |
| ticks 0-150 | 0.957 | 0.900 | 1.000 | 0.893 | 0.964 | **0.889** | **0.111** |
| ticks 0-600 | 0.990 | 0.977 | 1.000 | 0.970 | 0.991 | 0.974 | 0.030 |
| ticks 150-1500 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |

The `0-150` window **reproduces the header's 0.889 and its ~11-point span**. `rv` starts
at `precision_init` 0.5 and decays; it first clears the bound at tick **6** (u=0.04,
bound 0.384) and tick **15** (u=0.34, bound 0.264). Between those ticks the gate is
genuinely live and urgency genuinely gates -- that is the entire effect. Past tick ~150
the span is **0.000**.

Two corrections to the header's reading:
- The effect is a **transient of `rv` descending from `precision_init`**, not a
  steady-state property of the manipulation. It does **not** indicate a reachable
  boundary regime.
- "**monotone in the tail**" does not survive. The 0-150 profile is
  0.957 / 0.900 / 1.000 / 0.893 / 0.964 / 0.889 -- noisy with a slight drift, not
  monotone. That was small-sample noise over a handful of live ticks.

### 2. Five config levers, not one (the brief said four; the fifth is the interesting one)

| # | Lever | Where | Effect on the gate |
|---|---|---|---|
| 1 | `commitment_threshold` (0.40) | `config.py:482` | scales the bound directly |
| 2 | `breath_sweep_amplitude` (0.25) | `config.py:2103` | **binary** on/off square wave, not continuous |
| 3 | `precision_init` (0.5) | `config.py:484` | sets only the transient start point |
| 4 | `precision_ema_alpha` (0.05) | `config.py:483` | smoothing -> rv dispersion |
| 5 | `use_conditional_precision_gate` (False) | `config.py:523` | **replaces the gated quantity entirely** (SD-063) |

Also relevant: `urgency_max` 0.5, `use_waking_confidence_inflation` (SD-076, adds an
asymmetric-EMA drift source with an `rv` floor of 0.01).

### 3. The binding constraint: gated-quantity dispersion is ~30x too narrow

Urgency modulates the bound by `(1-u)`, a range of `0.96/0.66 = **1.455x**` over the
785a grid. To grade the commit rate, `rv`'s distribution must spread comparably. It
does not:

| seed | warmed rv mean | CV | p99/p1 |
|---|---|---|---|
| 0 | 0.006140 | 0.0123 | **1.069x** |
| 1 | 0.005590 | 0.0062 | **1.024x** |

(The warmed mean reproduces the scored 785a manifest's `commit_variance_mean`
0.0054-0.0098 -- the probe is measuring the same regime.)

**`precision_ema_alpha` does not rescue this.** Re-simulating from recovered raw PE:

| alpha | p99/p1 | grid levels with commit rate in (0.05, 0.95) |
|---|---|---|
| 0.05 (default) | 1.069 | 1/6 |
| 0.20 | 1.151 | 1/6 |
| 0.40 | 1.187 | 1/6 |
| **1.00 (no smoothing at all)** | **1.200** | **1/6** |

Even with the EMA fully disabled -- `rv` = the raw per-tick PE-MSE -- dispersion reaches
only 1.20x against a 1.455x manipulation. **The smoothing is not the cause; the
underlying prediction-error signal is itself near-stationary** (warmed raw PE-MSE
CV = 0.030). This is the load-bearing measurement.

Consequence, the offline threshold sweep (warmed phase, seed 0):

| `commit_threshold` | margin T/rv | cr @ u=0.04 | cr @ u=0.34 |
|---|---|---|---|
| 0.40 (default) | 65.1 | 1.000 | 1.000 |
| 0.0120 | 1.95 | 1.000 | 1.000 |
| 0.0090 | 1.47 | 1.000 | 0.000 |
| 0.0075 | 1.22 | 1.000 | 0.000 |
| 0.0065 | 1.06 | 0.931 | 0.000 |
| 0.0061 | 0.99 | 0.000 | 0.000 |

The margin passes through the <2x band, but the commit rate goes 1 -> 0 with no
graded interval. There is no threshold at which the six grid levels spread out.

### 4. The MECH-108 sweep gives a staircase, not a gradient

`sweep_active` is binary (`clock.py:108`) with fixed amplitude, so it contributes two
threshold values, not an oscillation across the `rv` band. Combined with urgency
(measured `rv`, duty 0.5, T=0.0075): **0.50 / 0.50 / 0.48 / 0.00 / 0.00 / 0.00**.

Commit rate does sit away from both 0 and 1 at three levels -- so the precondition is
*locally* satisfiable -- but the profile is a **flat plateau then a cliff**. A Spearman
rho over that is tie-dominated and degenerate. This is a usable *operating point*, not
a usable *dose-response*.

### 5. Non-stationarity: real, but milder than the brief anticipated

`rv` drifts **81x (seed 0) / 89x (seed 1)** from `precision_init` to asymptote --
consistent with the SD-074 ~54x figure quoted in the brief. But the drift is
**front-loaded and then flat**: 0.500 -> 0.0069 by tick ~150, then 0.00603-0.00641 from
tick 150 to 1500.

So the brief's worry ("any value giving a ~2x margin early is ~50x off late") is
**correct for a run that includes warmup, and moot for a warmed run**. A static
threshold *can* hold a boundary regime post-warmup; it cannot hold one through warmup.
A discard-first-N-ticks burn-in is sufficient -- a variance-tracking threshold is **not**
required. That is a weaker conclusion than the brief's third branch allowed for, and it
is the one the data supports.

### 6. Root-cause candidate -- FLAGGED, NOT ESTABLISHED

`v3_exq_785a` calls `agent.eval()` and contains **no optimizer, no `backward`, no loss**
(verified by grep). The whole 785a driver family runs an **untrained** agent, so
`z_world` is a frozen random projection -- and a frozen random encoder plausibly yields
the near-stationary PE-MSE (CV 0.030) measured above. This is the same condition
V3-EXQ-737 found in the x734/737 family (0 of 61 `latent_stack` tensors move).

**This is a hypothesis, not a finding.** Whether a *trained* `z_world` widens PE
dispersion enough to clear 1.455x is untested and untestable in this driver --
`sd_zworld_warmup_optimizer_group` is `implemented_pending_validation` and would be
what makes the counterfactual runnable. Per the brief's caution: **do not read this as
an established substrate ceiling.** What is measured is a reachability failure *under
the current configuration space*, with an identified and testable candidate cause.

### 7. A second structural fact: neither gate input is wired into the agent

- `update_running_variance()` has **no caller in `ree_core`** (785a header line 198;
  confirmed) -- the driver must drive it.
- `conditional_predictive_variance` (lever 5) is **never passed by `agent.py`**;
  `E2WorldUncertaintyHead` has no call site there at all. Its only appearance outside
  `e3_selector` is a usage example in its own docstring, which requires the driver to
  construct the head, give it an optimizer, and train it.

So both routes to a live commit gate are driver-supplied. Lever 5 is a **build**, not a
config flip -- but it is a *small* one, and it is the lever most likely to work, because
`predictive_variance` is by construction state-dependent ("HIGH exactly where THIS
prediction is about to be wrong"), which is precisely the dispersion the EMA lacks.

## Routing

**MECH-465 is substrate-gated** -- but by a small wiring build, not by the large z_world
question.

Recommended substrate entry (preferred): **wire and train `E2WorldUncertaintyHead` in a
driver and supply `conditional_predictive_variance` to `E3.select`, with
`use_conditional_precision_gate=True`.** SD-063 already exists and is unwired. The
stage-2 spike is then cheap and well-posed: measure that head's per-input predictive
variance dispersion and check it against the 1.455x bar. If it clears, MECH-465 becomes
directly testable and the follow-on is a `/queue-experiment` run of the 785a
exogenous-urgency design with **commit rate** as the load-bearing DV.

Secondary: validating `sd_zworld_warmup_optimizer_group` would let the frozen-encoder
hypothesis in Finding 6 be tested on the EMA path.

Not queued. Per the brief, the follow-on experiment is **not** queued -- its mandatory
precondition (median gate margin < 2x AND commit rate away from 0 and 1 across the
grid) is **not currently satisfiable**, which is exactly this spike's finding.

## Tension with the 2026-07-20 autopsies -- surfaced deliberately

Both 2026-07-20 autopsies set `recommended_substrate_queue_entry.action: none`. That
verdict is sound for the **variance-geometry** framing they addressed. It does **not**
hold for the **commit-gate** framing: this spike measures a concrete, small, and
well-specified substrate gap (lever 5 unwired) that blocks MECH-465 from being tested
at all. **This is new information relative to those autopsies** and should not be
treated as already adjudicated by them.

## Limitations

- Two seeds, single environment (`CausalGridWorldV2`, `hazard_harm=0.5`), untrained
  agent. The dispersion finding replicates across both seeds and in the direction that
  strengthens it (seed 1 narrower), but a trained-agent dispersion measurement is the
  open question and is what Finding 6 defers.
- The offline lever sweep assumes the gate is a pure comparison of the two recorded
  scalars. That is exactly what `e3_selector.py:2786-2792` does on this path
  (`use_harm_variance_commit` off, conditional gate off), so the assumption is
  structural rather than approximate -- but it would not transfer to the harm-variance
  branch.
