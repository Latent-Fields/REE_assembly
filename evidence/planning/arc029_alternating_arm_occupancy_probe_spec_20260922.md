# ARC-029 -- alternating-arm occupancy + detrend-validity probe: pre-registration spec

Status: **DRAFT SPEC -- not queued, not implemented.**
Drafted 2026-09-22 by `/diagnose-errors` on V3-EXQ-1066, at user request.
Claim: ARC-029 (only). Purpose: **diagnostic** (excluded from confidence scoring).

This document is the DESIGN. It is upstream of `/queue-experiment`, which owns
writing the driver, the code-review pass, the smoke test, the Step 4.5 red-team
pass and the queue entry. Nothing here may be copied into `experiments/` without
going through that skill (REE_Working/CLAUDE.md, "Experiment Scripts").

**Blocked on a standing user gate.** `failure_autopsy_V3-EXQ-1070a_2026-09-22`
section 8 records: *"No further ARC-029 env run is queued until /governance
answers the open question."* This spec does not lift that gate. It exists so the
decision is made against a costed, concrete alternative rather than in the
abstract -- and because GFLAG-0416 (below) argues the open question is empirical
rather than definitional, which is a reason to release the gate TO this probe.

---

## 1. The one question

**Does the ARC-029 committed/uncommitted contrast survive on the ALTERNATING
arm at rung L1?**

Everything else ARC-029 needs at L1 is already measured and holds. The
alternating arm is the single unmeasured link between the current evidence and
a queueable successor to V3-EXQ-1066.

---

## 2. What is already established -- do NOT re-measure

From `v3_exq_1070a_arc029_env_operating_point_feasibility_20260920T155046Z_v3`
(`arm_results`, read directly; 30 cells, ree-cloud-2, 5h00m10s). **All six L1
cells, both seeds, all three quantiles:**

| seed | q | committed_step_fraction | mean_committed_run_length | bar_in_force | harm_snr |
|---|---|---|---|---|---|
| 0  | 0.25 | 0.2585 | 4.556 | 1.0 | 22.687 |
| 0  | 0.50 | 0.4691 | 5.667 | 1.0 | 20.468 |
| 0  | 0.75 | 0.6842 | 6.135 | 1.0 | 23.588 |
| 42 | 0.25 | 0.3008 | 6.067 | 1.0 | 14.960 |
| 42 | 0.50 | 0.4956 | 6.267 | 1.0 | 13.524 |
| 42 | 0.75 | 0.7317 | 6.618 | 1.0 | 14.484 |

Against the pre-registered bars (`v3_exq_1070a...py:499-517`, transcribed
verbatim, not re-derived): `P1_OCCUPANCY_BAND = (0.15, 0.85)`,
`P1_RUNLEN_FLOOR = 3.0`, `BAR_IN_FORCE_FLOOR = 0.95`, `P3_SNR_FLOOR = 10.0`,
`P3_ABS_HARM_FLOOR = 0.01` harm/step.

**P1 and P3 both hold in 6/6 L1 cells, on the static arm.** They also held
across a 1.89x within-rung realised-training-tick spread (seed 0 = 1091 ticks,
seed 42 = 2063), so the `training_tick_budget_equalised` violation that failed
1070a (2.2786 vs a 2.0 ceiling) does not erode them -- that gate disqualifies
comparing rungs to EACH OTHER, which this probe does not do.

**Do not re-run the ladder.** 1070a section 5 measures the env bind as
unresolvable along it: softening lengthens episodes, which shrinks the window's
span in episodes AND drives `harm_snr` toward the P3 floor. L1 is the interior
point, not a marginal one.

---

## 3. The two open questions, as measurables

### Q1 -- ARM (the real gap)

Every number in section 2 is the **static** arm: `breath_period = 0`, MECH-108
off (`v3_exq_1070a...py:679` asserts it). ARC-029's P1 is specified for the
alternating arm, and **no landed manifest has ever measured occupancy with the
BreathOscillator running on top of the variance-tracking bar.** This is the
third and only surviving ground on which
`failure_autopsy_V3-EXQ-1070a_2026-09-22` section 4 withdrew its L0/L1 residual.

Mechanism, verified at source 2026-09-22:

- `agent.py:7608` -> `sweep_reduction = clock.sweep_amplitude if clock.sweep_active else 0.0`,
  passed as `sweep_threshold_reduction` (`agent.py:9693`).
- `e3_selector.py:3971-3974` -- the variance-tracking bar REPLACES the absolute
  threshold first, and the sweep multiplies **that**:
  `effective_threshold = _vt_commit_bar`, then `* (1.0 - sweep_threshold_reduction)`.
- Commit rule is `committed = variance < threshold`, so the sweep LOWERS the bar
  -> STRICTER -> forces uncommitted windows. That is its stated job
  (`agent.py:7605-7607`).
- `clock.py:94-113` -- `breath_period` is the TOTAL cycle; the sweep fires during
  the last `sweep_duration` steps of each cycle (`sweep_duration` default 5).

**The quantitative reason this needs measuring rather than arguing.** The bar is
`exp(trend_now + quantile_q(residuals))` (`e3_selector.py:975-994`), so
multiplying by `(1 - a)` is a DOWNWARD SHIFT OF `ln(1/(1-a))` IN LOG-RESIDUAL
UNITS: 0.0202 at a=0.02, 0.0513 at a=0.05, 0.1054 at a=0.10. Whether that moves
occupancy at all depends entirely on the residual dispersion, which is a
property of the trained run and is not currently recorded anywhere. A sweep too
small is inert; too large drives occupancy to ~0. GFLAG-0354 puts the workable
band at a ~ 0.02-0.10 and records ARC-029's own registered amplitudes (> 0.18,
derived at a pre-training rv) as **measured stale** on this bar.

### Q2 -- DETREND VALIDITY

Does one least-squares log-linear detrend adequately describe a window spanning
~27 episode resets? This is the question GFLAG-0416 leaves open after
establishing (at source) that the estimator is cross-episode BY CONSTRUCTION --
a bounded deque built once (`e3_selector.py:529/536`, lazily `:3959-3964`),
appended every select call (`:4090`), **never cleared**, with no
episode-boundary reset anywhere in `ree_core`.

**The statistic: `|realised occupancy - q|`.** A perfect detrend gives
occupancy = q exactly; residual structure the single linear term fails to absorb
shows up as deviation. Section 2's static-arm cells already supply the baseline:
max deviation **0.0658** (q=0.75, seed 0), mean |deviation| 0.0298, with a mild
compression toward 0.5. At L1 that is measured across a 26.8-episode window span.

This is NOT tautological with the estimator's contract pin. The contract
(`tests/contracts/test_commit_threshold_variance_tracking.py`) pins the bar's
behaviour in a controlled setting; across live episode resets it COULD have
diverged and did not. The probe extends that reading to the alternating arm,
where the sweep perturbs the very trajectory the residuals are computed from.

### Q3 -- IS THE OSCILLATOR EVEN REQUIRED? (record, do not decide)

ARC-029's `what_would_answer` reads, verbatim: *"Manipulation: Threshold-side
alternation only -- the variance-tracking quantile commitment bar, **or** a
MECH-108 BreathOscillator sweep calibrated to the run's own measured variance
distribution."* The **or** is load-bearing: the bar alone is a sanctioned
manipulation.

And section 2 shows the bar alone ALREADY produces within-run alternation at
L1 q=0.50 -- occupancy 0.469/0.496 with mean committed-run length 5.67/6.27,
i.e. both regimes occupied, comfortably inside P1. The oscillator's registered
purpose (`agent.py:7605-7607`) is to *"create periodic uncommitted windows even
when running_variance has converged below base commit_threshold after
training"* -- the saturation failure that the variance-tracking bar independently
solves by construction (occupancy ~ q at any absolute rv scale).

**So the oscillator may be redundant at L1.** The probe RECORDS the data that
settles this and does not act on it. Deciding it is section 9's construct
question, which belongs to `/governance`, not to this probe and not to its
author.

---

## 4. Design

### 4.1 Structure -- within-agent, which dissolves the gate that killed 1070a

Train **one agent per seed**. Run every measurement arm on that same trained
agent, counterbalanced in order.

This is the structural point of the design. 1070a's fatal precondition was
realised-training-tick spread across cells; here the arm contrast is
**within-agent**, so training depth is identical by construction and cannot
confound it. Realised ticks are still recorded as telemetry, and
`TRAIN_TICK_SPREAD_CEILING` is **not** re-used as a gate -- not relaxed, but
inapplicable, because no between-cell training comparison is made. State this
explicitly in the driver docstring so it does not read as a quiet relaxation of
a pre-registered bar (1070a's autopsy section 2 forbids relaxing it, and this is
not that).

`REEAgent` is not deepcopy-able (V3-EXQ-1066 `_run_cell`), so cell isolation is
by window-clear + per-episode reset + counterbalanced arm order, exactly as 1066
established.

### 4.2 The quantile is read LIVE -- one trained agent serves all three q

`_variance_tracking_commit_bar` reads `q = float(self.config.commit_threshold_quantile)`
on **every bar computation** (`e3_selector.py:985`), not at window-build time.
The window itself holds raw rv samples and is q-independent. So
`config.e3.commit_threshold_quantile` may be mutated between measurement arms on
one trained agent. This is a **3x saving on training** and is the reason the
probe is ~90 minutes rather than ~5 hours.

The driver MUST assert this rather than trust it: after mutating q, assert the
bar value changes and `commit_gate_window_fill` does not reset.

### 4.3 Cells

| axis | values | n |
|---|---|---|
| env rung | **L1 only** -- `num_hazards=4, hazard_harm=0.04, proximity_harm_scale=0.10` (`v3_exq_1070a...py:478`) | 1 |
| seed | 0, 42, 43 | 3 |
| quantile q | 0.25, 0.50, 0.75 | 3 |
| arm | `STATIC` (a=0, `breath_period=0`), `ALT_002`, `ALT_005`, `ALT_010` | 4 |

= **36 measurement cells** on 3 trained agents.

Seeds 0 and 42 are 1070a's, kept deliberately so the STATIC arm is a direct
replication check against section 2's table. Seed 43 is added because 1070a's
n=2 made every within-rung split n=1 vs n=1 (its autopsy section 6, "Scale:
likely insufficient").

Amplitudes span GFLAG-0354's measured workable band (0.02-0.10) at its two ends
and its midpoint. `sweep_duration` held at the default 5; `breath_period` set so
the sweep duty cycle is ~20% -- i.e. `breath_period = 25`. **Derive and state
the duty cycle in the driver**: the arm's realised occupancy is a time-weighted
mix of bar and swept-bar regimes, so duty cycle is a design parameter, not a
default to inherit silently.

### 4.4 Held fixed (from 1070a, transcribed)

`COMMIT_WINDOW = 200` select calls; `E3_STEPS_PER_TICK = 3`;
`PRECISION_EMA_ALPHA = 0.05`; `TARGET_ZWORLD_P0_TICKS = 400` (SD-070: without it
z_world stays a frozen random projection and rv never collapses);
`TARGET_P0_TICKS = 400`; `TARGET_P1_TICKS = 900`; `MEAS_ENV_STEP_TARGET = 900`;
`MEAS_SELECT_MIN = 250`; `WARM_EPISODE_CAP = 250`.

**`WARM_EPISODE_CAP` must stay at 250, not 30.** V3-EXQ-1066's `WARM_EPISODE_CAP = 30`
against L1's measured 26.8-episode window span is one of the three reasons that
driver cannot be re-queued as written.

---

## 5. Readouts and what routes what

### 5.1 GATES (route the verdict)

- **G1 -- no writes to `running_variance`.** Source-level invariant, asserted at
  runtime, exactly as V3-EXQ-1066 `_assert_no_running_variance_writes()`. This
  is the V3-EXQ-063a confound and is non-negotiable.
- **G2 -- bar in force.** `bar_in_force_fraction >= 0.95` and the window fills,
  in every cell. Distinguishes "the lever did nothing" from "the lever did
  something null".
- **G3 -- STATIC-arm replication.** The STATIC cells at seeds 0/42 must
  reproduce section 2's occupancy within 0.10 absolute. A miss means the probe's
  harness differs from 1070a's and NOTHING else in the run is interpretable.
- **G4 -- non-degeneracy.** The oscillator must actually move something: at
  a=0.10, realised occupancy must differ from the paired STATIC cell by more
  than the STATIC arm's own seed-to-seed spread at that q. A null that fails G4
  is "inert sweep", not "sweep preserves occupancy" -- these are opposite
  findings and must not be allowed to read alike.

### 5.2 PRIMARY READOUTS

- **R1 (Q1):** per-cell `committed_step_fraction` and `mean_committed_run_length`
  under each amplitude, against `P1_OCCUPANCY_BAND` and `P1_RUNLEN_FLOOR`.
  **The deliverable is the amplitude band, if any, where P1 still holds.**
- **R2 (Q2):** `|realised occupancy - q|` per cell, static and alternating,
  against the static baseline (max 0.0658 / mean 0.0298). Plus the recorded
  log-residual dispersion, which no landed manifest currently carries.
- **R3 (P2, precision invariance):** paired per-seed `current_precision`
  distributions, alternating vs static. ARC-029 requires these
  indistinguishable. **The oscillator cannot write `running_variance` directly,
  but it changes which actions are committed, hence the trajectory, hence
  prediction errors, hence rv** -- so P2 is a real empirical risk here, not a
  formality, and a successor is not queueable until it is measured.
- **R4 (Q3):** whether STATIC alone satisfies P1. Recorded, not routed.

### 5.3 NO THRESHOLD IS REGISTERED FOR R2 OR R4

R2 and R4 are **telemetry with no pre-registered bar**. R2 has no prior
distribution to set one against; R4 is a construct question for `/governance`.
Registering a threshold either would be inventing a bar to clear.

---

## 6. What this probe does NOT do

- It does **not** run the ARC-029 harm contrast (C1). It establishes whether the
  contrast is RUNNABLE. C1 is the successor's job.
- It does **not** promote or weaken ARC-029. Diagnostic; `evidence_direction`
  `non_contributory` by design.
- It does **not** revive V3-EXQ-1066. That driver needs three independent fixes
  regardless: `WARM_EPISODE_CAP` 30 -> 250, env kwargs parameterised by rung
  rather than hard-coded to the lineage, and P3 restated as SNR rather than a
  harm-EVENT count.
- It does **not** repeat V3-EXQ-1070b, the pilot-repair ladder rerun the 1070a
  autopsy declined. That offer was declined on three grounds, of which two
  survive GFLAG-0416 (contract-pinning and static-arm) and remain good reasons
  not to run it. This probe is one rung, not a ladder.
- It does **not** relax `TRAIN_TICK_SPREAD_CEILING`. See 4.1.

---

## 7. Budget

~50k env steps total (~43k measurement across 36 cells, ~7k training across 3
agents). Reference point: V3-EXQ-1063 ran 50k steps in 29 min.

**Book 90 minutes**, `machine_affinity: any`, priority to be set at queue time.
The cadence at L1 (measured 1.43 env steps per select call) differs from 1063's,
so the reference is an order-of-magnitude check, not a transferable timing.
`/queue-experiment` must re-derive this from a smoke run.

---

## 8. Provenance -- everything verified at source 2026-09-22

| Fact | Where |
|---|---|
| Sweep multiplies the vt bar, after it replaces the absolute one | `ree-v3 ree_core/predictors/e3_selector.py:3971-3974` |
| `sweep_reduction` origin and plumbing | `ree_core/agent.py:7608`, `:9693` |
| `breath_period` = total cycle; sweep = last `sweep_duration` steps | `ree_core/heartbeat/clock.py:94-113` |
| Bar formula `exp(trend_now + quantile_q(residuals))` | `e3_selector.py:975-994` |
| Quantile read LIVE per bar computation | `e3_selector.py:985` |
| Window built once, appended every select, never cleared | `e3_selector.py:529/536/3959-3964/4090` |
| L1 rung kwargs; pre-registered bars; budgets | `ree-v3 experiments/v3_exq_1070a_...py:478, :499-517, :523-548` |
| L1 per-cell measurements | `1070a` manifest `arm_results` |
| Amplitude band a ~ 0.02-0.10; ARC-029's own >0.18 stale | GFLAG-0354 |
| Estimator is cross-episode by construction | GFLAG-0416 |
| Standing gate; withdrawn residual and its three grounds | `failure_autopsy_V3-EXQ-1070a_2026-09-22.md` sec 4, 8 |

---

## 9. The construct question this probe does NOT resolve

`failure_autopsy_V3-EXQ-1070a_2026-09-22` section 8 asks whether ARC-029's
commitment bar is a within-run drift-tracking quantile or a cross-episode one.
**GFLAG-0416 argues that question is already answered at the substrate level**
(the estimator is cross-episode by construction; ARC-029's own text asks for
"the run's own measured variance distribution" -- run, not episode), and that
what remains is the VALIDITY question this probe measures as R2.

What `/governance` still owes, and what this probe deliberately only feeds:

1. **Is the vt bar alone an acceptable ARC-029 manipulation, or is MECH-108
   required?** ARC-029's text says "or". V3-EXQ-1066 chose to read C1 in the
   alternating arm. R4 supplies the data; the reading is governance's.
2. **If the bar alone qualifies, what is the control arm?** V3-EXQ-1066 read
   "a static-threshold arm" as the non-oscillating quantile bar. Under the
   bar-alone reading the natural control is the static ABSOLUTE threshold --
   which is degenerate at a trained operating point (occupancy 1.0, the measured
   063a defect). That is a genuine construct gap, not a drafting oversight, and
   it should be settled before the successor is designed rather than after.

**If (1) resolves to "the bar alone qualifies", this probe's Q1 becomes moot and
the successor can be designed straight off section 2.** That outcome would make
the probe unnecessary -- which is an argument for putting (1) to `/governance`
FIRST and only then queueing, not for skipping the probe on a guess.
