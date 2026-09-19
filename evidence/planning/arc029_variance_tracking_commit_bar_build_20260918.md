# ARC-029 (D): the variance-tracking commitment bar -- build record

- **Date:** 2026-09-18
- **Session:** `metaworker-science-20260918-arc029-variance-tracking-threshold` (campaign `science-20260918-arc029-variance-tracking-threshold`)
- **Chip:** `chip-20260918-arc029-variance-tracking-threshold`
- **Authority:** user decision 2026-09-18, option (D), answering `chip-20260918-arc029-p1-lever-operating-point`
- **Box:** `ree-cloud-4`, torch 2.12.0+cpu, python 3.10.12
- **Landed:** `ree-v3` -- see "Landing" below.

## 1. What was built

`E3Config.use_variance_tracking_commit_threshold` (default **False**). When armed, the
commit gate's BASE bar stops being the absolute `commitment_threshold` (0.40) and becomes a
**quantile of the run's own commit-gate-variance distribution** over a fixed-width sliding
window. Occupancy is then ~q at any absolute rv scale, which is what survives the measured
five-order collapse.

It is deliberately the **base**, computed before every existing modulation, so the MECH-108
sweep, SD-011 urgency and SD-093/MECH-426 velocity terms all keep multiplying it with
unchanged semantics.

Two companion parameters, `commit_threshold_quantile` and
`commit_threshold_quantile_window`, have **UNSET sentinels (-1.0 / -1) and construction
RAISES** if the lever is armed without them. This is deliberate and is the build's main
concession to the consent rule: the quantile IS the target commitment occupancy, and the
window decides whether committed runs have length structure at all. Both change what a
later ARC-029 experiment measures, so they belong to that experiment's pre-registration,
not to a default smuggled in here. The sentinel has a second job: `REEConfig.from_dims`
silently swallows unknown kwargs, and a raising sentinel converts that silent swallow into
a loud construction error.

Wired at all **three** sites -- dataclass field, `from_dims` signature, `config.e3` mirror --
and asserted by contract, not assumed.

## 2. The estimator, and why it is not the obvious one

**This is the part most likely to have been got wrong, so it is stated first.**

The obvious reading of "a quantile of the run's own rv distribution" is the plain q-quantile
of a trailing window. **Measured at build time, that reading does not work.** A trailing
window is centred half a window BEHIND the tick it judges, so under the measured within-run
drift the current sample sits systematically to one side of it. On the same stream, at a
requested q of 0.75, it delivered occupancy **0.205**. A quantile over an EXPANDING window
(the other obvious reading) is the same failure over a longer baseline: **0.017**.

Both would have looked correct -- the quantile is computed, the bar exists, the diagnostics
populate -- while the gate did not do what the lever was built for. That is exactly the
"structurally present but functionally inert" failure this codebase has been producing.

Shipped instead: over the window, fit a least-squares line to **log**(gate variance) against
tick index, take the q-quantile of the **residuals** about that line, and evaluate the line
one tick PAST the window's end. Bar = `exp(trend_at_now + quantile_q(residuals))`.

- log space because rv is a positive scale quantity moving by orders of magnitude; drift is multiplicative.
- the linear fit absorbs the within-run drift, so the residual distribution is drift-free and its q-quantile is an unbiased occupancy target.
- extrapolating to the current tick is what removes the half-window lag.
- at zero drift the slope is ~0 and it reduces to the plain quantile, so nothing is lost in the easy case.

Both naive variants are pinned as **negative controls** in the contract file. If detrending
ever stops beating them, that test says so and the complexity should be removed.

## 3. Measured: the ON path leaves saturation

Selector-level demonstration driving the **real** `select()` gate and the **real**
`update_running_variance` EMA. Only the prediction-error stream is synthetic, calibrated to
the measured post-training band (rv 1.2e-6 -> 1.1e-5, the measured ~5x within-run drift);
`precision_init` sets the trained initial condition and rv then evolves through the real EMA.
1200 ticks.

**This is not an end-to-end trained-agent run.** It shows that the bar change removes
saturation at the measured operating point. End-to-end confirmation belongs to the re-queued
experiment.

### A. OFF -- the defect, reproduced

| | |
|---|---|
| rv over the run | 1.195e-06 .. 1.281e-05 (drift 10.7x) |
| `committed_step_fraction` | **1.0000** |
| committed runs | **1** run of 1200 ticks |

Matches the finding's measured 1.0000. This is the negative control for everything below.

### B. ON -- response surface over (q, window), post-warmup

| q | W | `committed_step_fraction` | mean committed-run length | n runs |
|---|---|---|---|---|
| 0.25 | 50 | 0.3400 | 5.3 | 74 |
| 0.25 | 200 | 0.2730 | 7.0 | 39 |
| 0.25 | 500 | 0.2714 | 5.1 | 37 |
| 0.50 | 50 | 0.5200 | 7.3 | 82 |
| 0.50 | 200 | 0.4690 | 11.2 | 42 |
| 0.50 | 500 | 0.5514 | 11.0 | 35 |
| 0.75 | 50 | 0.6904 | 10.6 | 75 |
| 0.75 | 200 | 0.6890 | 12.5 | 55 |
| 0.75 | 500 | 0.7600 | 17.7 | 30 |

**Occupancy** is inside P1's [0.15, 0.85] on every cell; it was outside on all of them
before (it was 1.0000). **Run length is the weaker half, and the table above overstates it.**
The contract harness calls `update_running_variance` once per `select()`; the agent calls it
every env tick while `select()` fires only on E3 ticks (`e3_steps_per_tick`, default 10).
Re-measured across that ratio at q=0.50, mean committed-run length is 10.41 at 1:1 (the
harness), 6.10 at 3:1, **3.36 at 10:1 (the agent's default)** and 2.60 at 20:1 -- and at
q=0.25 at the agent default it is **2.22, BELOW P1's >= 3-tick criterion**. So P1's occupancy
half is now satisfiable and its run-length half is satisfiable only at higher q or with the
run-length levers moved. Those levers are **`precision_ema_alpha`** (measured mean run length
~2.0 / ~3.4 / ~14.1 ticks at alpha 0.5 / 0.05 (default) / 0.001) and **`e3_steps_per_tick`** --
NOT the window width, which moves run length only ~3.2 -> ~3.4 ticks across a 40x range.
**A re-queue must pre-register alpha and the E3 cadence, not just q and W.**

### C. Estimator controls, same stream

| q | expanding window | plain trailing window | **detrended (shipped)** |
|---|---|---|---|
| 0.25 | 0.0000 | 0.0040 | **0.2730** |
| 0.50 | 0.0010 | 0.0370 | **0.4690** |
| 0.75 | 0.0170 | 0.2050 | **0.6890** |

### D. The MECH-108 sweep regains dynamic range -- at MODEST amplitude (q=0.50, W=200)

| `sweep_amplitude` | `committed_step_fraction` | mean run length |
|---|---|---|
| 0.0 | 0.4690 | 11.2 |
| 0.005 | 0.4490 | 10.7 |
| 0.01 | 0.4260 | 9.1 |
| 0.02 | 0.3880 | 8.8 |
| 0.05 | 0.2940 | 7.2 |
| 0.10 | 0.1190 | 3.6 |
| 0.20 | 0.0030 | 3.0 |

The finding measured this sweep INERT (1.0000 at amplitude 0.999). It is now graded and
usable.

**A THIRD stale calibration artefact, found here.** ARC-029's worked amplitudes are stale in
the *other* direction too: its `a > 0.18` would now drive occupancy to ~0. **The workable
band on the quantile bar is roughly `a` in [0.02, 0.10]**, which keeps occupancy in
[0.12, 0.39] with run length >= 3. A re-queue must calibrate amplitude there, not at 0.18+.

*(Caveat: the steepness of this response is a property of the residual spread, which is set
by rv's fluctuation-to-drift ratio. That ratio is a property of the synthetic stream here and
should be re-measured on a real trained agent before amplitudes are pre-registered.)*

## 4. Bit-identity

The build constraint asks for identity proven **where the new code runs**, not only where it
is skipped. `test_arming_the_lever_while_warming_is_bit_identical` does that: the lever is
**armed** (window appended every tick, bar helper called every tick) but the window is wider
than the run, so the bar never takes force. Scores, committed flags, the parameter
fingerprint and the **torch RNG state** are all identical to default-OFF.

**The cross-REVISION check was also run, by the red-team pass, and it passed.** An earlier
draft of this document said it had not been; that is corrected here. Method:
`git archive origin/main | tar -x` into a scratch tree, then 400 ticks of the real `select()`
driven on both revisions with identical seeds, hashing scores, selected actions, committed
flags, the full torch RNG state and every parameter. **Identical SHA256 on pristine
`origin/main` and on this HEAD at default.**

## 5. Disposition of the 063a autopsy's "no new substrate is needed"

**This build does contradict that line, and the contradiction is real rather than verbal.**
`failure_autopsy_V3-EXQ-063a_2026-09-14` section 7.3 says claims.yaml's `what_would_answer`
"already specifies a complete, ready-to-queue redesign spec ... using existing REEConfig
levers -- route to that spec directly", and section 8 routes P1 to arming
`use_natural_commit_latch_hold` and P2 to the MECH-108 sweep.

**Why the new measurement supersedes it, in the honest form:**

1. **063a reached its conclusion against an operating point nobody had measured.** Its claim
   is a SOURCE-level judgment -- the lever exists, it is threshold-side, it is upstream of the
   gate -- and every part of that remains TRUE. What was never checked is the lever's
   **dynamic range against where a trained agent actually sits**. The five-order collapse is
   new information, not a disagreement with 063a's reasoning.
2. **063a's own P1 remedy is inapplicable, and provably so.**
   `use_natural_commit_latch_hold` *sustains* commitment; it was built for the V3-EXQ-460i
   fragmentation failure (occupancy too SHORT). The failure measured here is the opposite --
   saturation at 100% committed, needing uncommitted windows. Arming it cannot help.
3. **063a's P3 bullet is stale in the same way.** It says "063a's ~-0.055 harm/step is a
   demonstrated workable operating point -- a calibration requirement already met, not an open
   problem." At the pre-flight's recalibrated env, harm/step measures 0.0025-0.0068. Two of
   063a's three P-bullets were written against operating points that no longer hold; this is a
   systematic staleness in section 8, not a one-off.
4. **This build SERVES 063a's actual learning rather than overturning it.** Section 7.2's
   learning is that an ablation must "manipulate a driver *upstream* of the gate ... so the
   gate's own decision logic is genuinely exercised". A quantile bar is still a threshold-side,
   precision-invariant driver upstream of the gate. It satisfies 063a's requirement *better*
   than the fixed bar does, because the fixed bar cannot produce the two-sided occupancy that
   requirement presupposes. 063a's substantive finding -- that a same-scalar ablation cannot
   isolate commitment mode -- is untouched and remains correct.

**On reading 063a in full, it does not foreclose this build.** What it forecloses is
re-queuing `v3_exq_125a` unmodified and re-using the `_running_variance`-forcing ablation
vehicle; this build does neither.

**Owed follow-on (governance, not this session):** 063a section 8's P1 and P3 bullets should
be marked stale, so a future session routing off that autopsy does not re-derive the
inapplicable remedy. Recorded here and named in the closing note; GFLAG-0346 already carries
the ARC-029 evidence discrepancy.

## 6. P3 -- the second, independent blocker: which of the two, and why

The decision chip's condition was that if (A), (B) or (D) is chosen, the env harm parameters
must **also** be raised, **or** C1's bar re-expressed relative. Measured harm/step at the
converged point is 0.0025-0.0068, under the 0.01 floor that makes the pre-registered 0.002
absolute bar a <=20% relative effect.

**Neither was applied in this session, and that is a sequencing judgment, not a dodge.**
Both levers were checked and **neither is a substrate lever**:

- `hazard_harm` and `proximity_harm_scale` are **constructor arguments of
  `CausalGridWorld`** (`ree_core/environment/causal_grid_world.py:273,339`), set per
  experiment. Changing their defaults would silently re-scope every experiment on the fleet.
- C1's bar lives in ARC-029's **pre-registered criteria**. Rewriting a pre-registered
  falsifier is a governance act, and not one a headless substrate build may perform
  unilaterally.

Both are therefore set at re-queue time, by the `/queue-experiment` unit, under the user's
eye. What this session owes is a recommendation with its reasoning, which is:

**RECOMMEND (ii): re-express C1's bar as a RELATIVE effect, with an absolute admissibility
floor -- and do NOT raise the env harm parameters.** Reasons:

1. **It is the same lesson as this build.** ARC-029 has now been bitten twice in one
   experiment by an ABSOLUTE bar against a quantity whose scale is set by training or by
   parameters: the 0.40 commitment bar, and the 0.002 harm/step bar. Fixing one and leaving
   the other absolute leaves the identical defect live.
2. **Raising env harm perturbs the quantity the P1 fix just stabilised.** More harm changes
   the prediction-error statistics, hence rv, hence the very distribution the quantile bar is
   taken over. That is a confound-generating move made *to fix a confound*.
3. **It preserves comparability.** A relative criterion is comparable across operating points,
   which is precisely what made the 063a evidence hard to attribute. Raising the env moves
   away from the pre-flight-recalibrated environment and would require re-measuring P2's
   precision-invariance calibration and the 063a comparison baseline.

**The contingency, stated because it is the way this recommendation could be wrong:** a
relative effect on a small absolute base can be noise-dominated. At harm/step 0.0025-0.0068,
a 25% relative bar needs a difference of 0.0006-0.0017, which must be compared against the
**seed variance of harm/step** -- a quantity nobody has measured. **The re-queue must measure
that variance first.** If the relative effect is noise-dominated, fall back to (i) and raise
the env harm parameters, accepting the re-calibration cost. The admissibility floor exists for
the same reason: below some absolute harm/step the comparison should be declared inadmissible
rather than reported as a null.

## 6a. Red-team pass, and what it changed

An adversarial review was run in the foreground against the diff, with instructions to break
the bit-identity, inertness, estimator, test-vacuity, wiring and interaction claims. It could
NOT break: OFF-path bit-identity (it ran the cross-revision check above), estimator
robustness (it drove the real estimator over ramp-up, ramp-down, flat, decay-then-plateau,
step-up, step-down, log random walk and a 1000x spike -- occupancy stayed within 0.10 of q on
all but the random walk at q=0.75), test non-vacuity (6 mutants of the estimator, every one
caught), or the config wiring. It found no deserialization path that could fire the sentinel
spuriously.

**It did find real defects. Six were FIXED in this build before landing:**

1. **A degenerate all-equal window was an absorbing UNCOMMITTED state.** The quantile of a
   constant is that constant, so `v < bar` reduced to a 1-ulp `exp(log(v))` round-trip --
   independent of q, and measured at occupancy 0.0000 at every q. This build would have
   replaced "permanently committed" with "permanently *un*committed", silently. Reachable:
   a driver that never calls `post_action_update` leaves rv pinned at `precision_init`
   forever (V3-EXQ-925a documents exactly that), which is the E3-level harness shape ARC-029
   work uses. **Fixed:** a relative-spread guard returns None so the absolute bar stays in
   force; distinguishable from warmup by `commit_gate_window_fill`.
2. **The window-width guidance was empirically false** -- and it was baked into a user-facing
   `ValueError` and was the build's stated reason for refusing a default. **Fixed:** the
   comment and the error text now name `precision_ema_alpha` and `e3_steps_per_tick` as the
   run-length levers, state the warmup in SELECT CALLS rather than env ticks, and say what
   the window actually controls.
3. **`get_commitment_state()` was a SECOND, disagreeing commit predicate** -- still comparing
   against the absolute bar, measured at **53.7% disagreement** with the `select()` gate at
   q=0.50. Not merely telemetry: `REEAgent` feeds `committed_now` into
   `compute_agent_persistence_appraisal`, and V3-EXQ-942 / 059 / 059b / 921 instrument
   commitment through it -- a driver reading that dict would have recorded this lever as
   completely inert. **Fixed:** it now reports the bar the gate actually had in force (cached,
   so it agrees exactly), plus a new `commit_threshold_absolute` key. Unchanged when OFF.
4. **One NaN or inf sample corrupted the bar for a whole window.** **Fixed:** non-finite
   samples are dropped, not appended.
5. **The window append was not gated on `simulation_mode`,** unlike every other accumulator in
   `select()`. Latent (no live caller passes it) but it is the one thing that would pollute
   the bar with counterfactual samples. **Fixed.**
6. **Arming the lever post-construction was silently inert** (`agent.config.e3.<field> = ...`
   is an existing idiom in the corpus), so the loud-failure defence covered only the
   `from_dims` swallow. **Fixed:** the window is built lazily at the gate, with the same
   validation.

Also fixed: the three `from_dims` parameters were inserted mid-signature, violating the
convention documented at `config.py` ("immediately before `**kwargs` so no existing positional
argument index moves"). Harmless today, now correct.

**Two findings are NOT code defects and are handed to the ARC-029 pre-registration**, because
each changes what a re-queued experiment would measure:

- **`precision_margin_norm` inverts when this lever is armed.** It is
  `1 - commit_variance/effective_threshold`, which is ~1 by construction under the absolute
  bar and ~0 by construction under a quantile bar, since the bar now sits AT a quantile of the
  same scalar. Measured mean **0.999986 -> 0.032963**. It is a live selection input via
  MECH-027 `use_precision_scaled_commit_temperature` (so arming BOTH levers flips the
  committed pick from effectively-hard-argmin to maximally-soft), and it is the DV of
  V3-EXQ-981/981a, whose design text assumes a baseline saturated near 1. Documented in
  `config.py`; not changed, because redefining it would itself change what 981 measures.
- **Every MULTIPLICATIVE modulation of the bar now has a much smaller usable range, set by an
  UNMEASURED quantity.** Sweep, SD-011 urgency and SD-093 velocity all shift the LOG bar by
  log(1-a) against a residual spread that is an uncontrolled property of the run. Measured
  collapse by amplitude 0.25 -- which is `breath_sweep_amplitude`'s own DEFAULT -- and SD-011
  urgency drives occupancy to 0.974 at `urgency_applied` ~0.2, well under its 0.5 cap, i.e.
  the absorbing state returns. Worse, the residual spread in the demonstration above is an
  artefact of the synthetic stream's jitter: at a tighter jitter even a 0.05 sweep collapses
  occupancy to 0.0000. **So section 3D's "the sweep regains dynamic range" is sound as to the
  MECHANISM and NOT as to the NUMBERS.** The occupancy-at-zero-sweep result is robust to that
  jitter (0.465-0.509 across a 40x range), which is why the build's central claim stands.

  **A scale-free alternative exists and was deliberately NOT built: modulate the QUANTILE
  (q -> q - delta) rather than multiplying the bar.** That would make the sweep's dynamic
  range independent of the residual spread, and it is probably what an alternating-arm ARC-029
  design wants. It is not built here because it changes what the MANIPULATION IS, which is the
  experiment's call under the consent rule, not this build's. **It should be put to the user at
  re-queue time**, along with the cheap prerequisite measurement nobody has made: the rv
  residual dispersion on a REAL trained agent, on which the whole alternating-arm design's
  viability rests.

## 7. Landing and tests

- 19 contract tests in `ree-v3/tests/contracts/test_commit_threshold_variance_tracking.py`, all passing.
- `remote_pytest.sh` returned **exit 4 (routing condition, not a red)**: the hub was already
  running a suite, and `ree-worker-2/3/4` refused this host's ssh credentials (a credential
  fault on `ree-cloud-4`, not a fleet outage). Per the wrapper's own guidance, the suite was
  run **locally on `ree-cloud-4`, which is itself a cloud worker** -- a sanctioned gate, not a
  laptop run. Interpreter: `/home/ree/.venv/ree/bin/python3` (torch 2.12.0+cpu).

## 8. What this session did NOT do

- **Did not re-queue the experiment.** That is a separate `/queue-experiment` unit, per the
  chip. `V3-EXQ-1056` was reserved and RELEASED and its id is free; 1051-1055 are consumed;
  the next id must be re-derived at write time from the live file and `git log`.
- **Did not touch `claims.yaml`, `substrate_queue.json` or ARC-029's criteria.**
- **Did not change any default.** No existing run's behaviour moves.
