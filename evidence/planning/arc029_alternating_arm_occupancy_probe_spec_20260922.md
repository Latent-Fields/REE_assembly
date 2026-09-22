# ARC-029 -- alternating-arm occupancy + detrend-validity probe: pre-registration spec

Status: **WITHDRAWN 2026-09-22 -- the manipulation this spec is built on cannot fire.**
See section 11. The MECH-108 sweep is structurally unreachable at rung L1, the
user's disposition was to drop the oscillator and treat the variance-tracking bar
alone as the manipulation, and that dissolves this probe rather than reshaping it
(V3-EXQ-1070a already answers every question it posed). NO experiment was queued;
EXQ id 1074 was reserved and released. Recorded as GFLAG-0421.
Sections 1-10 are kept as the design record, NOT as a live plan.

Original status: **DRAFT SPEC -- not queued, not implemented.**
**REFUSED at `/queue-experiment` Step 2.5c on 2026-09-22 (GFLAG-0418).** Two open
`severity: corrupting` substrate_queue rows (`mech005-betagate-decommit-counter-and-commit-ceiling`,
`mech005-endogenous-arousal-dynamic-range`) overlap `ree_core/agent.py` and
`ree_core/heartbeat/clock.py` at module level. EXQ id 1074 was reserved and released.
See section 10 for the refusal and the two corrections it produced.
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
occupancy at all depends entirely on the residual dispersion. **CORRECTED
2026-09-22: that quantity IS already recorded** -- `rv_residual_dispersion_sd`
0.0232-0.0318 across the six 1070a L1 cells, against which this section's
0.02/0.05/0.10 ladder spans 0.64/1.62/3.32 SD. See section 10.2. A sweep too
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
| arm | `STATIC` (a=0, `breath_period=0`), `ALT_010`, `ALT_020`, `ALT_040`, `ALT_100` | 5 |

= **45 measurement cells** on 3 trained agents.

Seeds 0 and 42 are 1070a's, kept deliberately so the STATIC arm is a direct
replication check against section 2's table. Seed 43 is added because 1070a's
n=2 made every within-rung split n=1 vs n=1 (its autopsy section 6, "Scale:
likely insufficient").

**Amplitudes are sized against the MEASURED residual dispersion, not against
GFLAG-0354's nominal band.** The sweep multiplies the bar by `(1 - a)`, which in
the bar's own log-residual space is a downward shift of `ln(1/(1-a))`; 1070a
records that space's dispersion directly (`rv_residual_dispersion_sd`, L1 seed
means 0.03138 / 0.02591 / 0.02391 at q = 0.25 / 0.50 / 0.75). In those units
GFLAG-0354's nominal 0.02-0.10 band spans 0.78 to 4.07 SD -- its top end is
total suppression, not a probe point. The corrected ladder, with **pre-registered
predicted in-sweep occupancy** under a normal-residual approximation:

| arm | a | shift | SD (q=0.50) | pred. in-sweep occ. q=0.25 / 0.50 / 0.75 |
|---|---|---|---|---|
| `ALT_010` | 0.010 | 0.0101 | 0.39 | 0.160 / 0.349 / 0.600 |
| `ALT_020` | 0.020 | 0.0202 | 0.78 | 0.094 / 0.218 / 0.432 |
| `ALT_040` | 0.040 | 0.0408 | 1.58 | 0.024 / 0.058 / 0.151 |
| `ALT_100` | 0.100 | 0.1054 | 4.07 | 0.000 / 0.000 / 0.000 |

`ALT_100` is retained deliberately as a **saturating positive control**: it must
drive in-sweep occupancy to ~0, which is what proves the readout can be moved at
all. It is not a candidate operating point. The normality assumption is the
prediction's, not the measurement's -- the driver records the empirical residual
CDF, and a systematic departure from this table is itself a Q2 finding.

`sweep_duration` held at the default 5; `breath_period = 25`, so the sweep duty
cycle is 20%. **The duty cycle is a design parameter, not a default to inherit
silently** -- and see 5.2 R1, where it is the reason the run-mean cannot be the
discriminating readout.

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
- **G4 -- non-degeneracy, tested on R1a and NEVER on the run-mean.** At
  `ALT_100` the **in-sweep** occupancy must differ from the paired STATIC cell by
  more than the STATIC arm's own seed-to-seed spread at that q (predicted: to
  ~0.000, against a static 0.26-0.73 -- so this should pass by a wide margin, and
  a failure means the sweep is not reaching the bar at all). A null that fails G4
  is "inert sweep", not "sweep preserves occupancy" -- these are opposite
  findings and must not be allowed to read alike. **Applying G4 to the run-mean
  would defeat it**: 4.3's arithmetic shows the run-mean barely moves across the
  whole ladder, so a run-mean G4 could fail while the manipulation is in fact
  working perfectly.

### 5.2 PRIMARY READOUTS

- **R1 (Q1) -- CONDITIONED ON SWEEP PHASE. The run-mean is NOT the discriminating
  readout and must not be reported as though it were.** The driver records
  `clock.sweep_active` at every select call and partitions the cell three ways:
  - **R1a (DISCRIMINATING): in-sweep occupancy** -- `committed_step_fraction`
    over ticks with `sweep_active == True`, against the predicted ladder in 4.3.
  - **R1b: inter-sweep occupancy** -- the same over `sweep_active == False`. It
    should track the STATIC arm at that q; a departure means the oscillator is
    perturbing the bar outside its own sweep phase, which would be a finding.
  - **R1c: run-mean occupancy and `mean_committed_run_length`**, against
    `P1_OCCUPANCY_BAND` / `P1_RUNLEN_FLOOR`. This is ARC-029's formal P1 and is
    kept for that reason -- but it is **recorded as telemetry, not as the
    deliverable.**

  **Why R1c cannot carry the verdict, computed before the run.** At a 20% duty
  cycle the run-mean is `~0.8*F(q) + 0.2*F(q - shift)`, so on the ladder above it
  is predicted at 0.224-0.670 across every amplitude and every quantile --
  **inside `P1_OCCUPANCY_BAND` at all 12 combinations, including `ALT_100`, where
  in-sweep occupancy is 0.0000.** A readout that returns "P1 holds" identically
  for a well-behaved sweep and for one that annihilates commitment on every sweep
  phase has not measured the manipulation. **The deliverable is the amplitude
  band where R1a stays inside `P1_OCCUPANCY_BAND`**, with R1c reported alongside
  as the formal-P1 record.
- **R2 (Q2):** `|realised occupancy - q|` per cell, static and alternating,
  against the static baseline (max 0.0658 / mean 0.0298). Plus the recorded
  log-residual dispersion (already recorded by 1070a -- see section 10).
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

~61k env steps total (~54k measurement across 45 cells, ~7k training across 3
agents). Reference point: V3-EXQ-1063 ran 50k steps in 29 min.

**Book 120 minutes**, `machine_affinity: any`, priority to be set at queue time.
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

---

## 10. Step 2.5c refusal, and the two corrections it produced (2026-09-22)

**Refused at `/queue-experiment` Step 2.5c**, recorded as **GFLAG-0418** (ARC-029, MECH-005).
No driver was written and no queue entry added; EXQ id **1074** was reserved and released.

Two open `severity: corrupting` `substrate_queue.json` rows overlap this driver's modules:

| sd_id | overlapping substrate_paths |
|---|---|
| `mech005-betagate-decommit-counter-and-commit-ceiling` | `heartbeat/beta_gate.py::release`, `::should_admit_elevation`, `agent.py::select_action` |
| `mech005-endogenous-arousal-dynamic-range` | `heartbeat/clock.py::update_e3_rate_from_beta`, `regulators/phasic_surprise_burst.py` |

The probe exercises `agent.py::select_action` (the `sweep_reduction` site, `agent.py:7608`) and
`clock.py` (the BreathOscillator), so both match at module level and the gate fails toward
blocking, as it is written to.

**Measured, for whoever adjudicates it:** row 1's stated defect is `committed_tick_frac` pinned
at 1.000 with zero de-commits. Under the variance-tracking bar at L1 that does not obtain --
1070a records 30-89 committed runs per cell, occupancy 0.2585-0.7317, run length 4.56-6.62 and
`n_latched_ticks` 102-339 across all six L1 cells. Row 2 concerns arousal-modulated E3 cadence,
which this probe does not manipulate. Both rows are
`status: proposed_REGISTRATION_ONLY_not_a_build_authorisation`, `ready: false`, and name modules
essentially every V3 driver touches -- so while they stand open+corrupting the gate blocks the
whole corpus, not this probe. That is the governance question GFLAG-0418 poses.

### 10.1 CORRECTION -- the residual dispersion was already recorded

Sections 3 and 5.2 originally said no landed manifest carried the log-residual dispersion. **That
was wrong.** 1070a records it per cell:

| seed | q | `rv_residual_dispersion_sd` | `iqr` | occupancy | `n_committed_runs` | window span (eps) |
|---|---|---|---|---|---|---|
| 0  | 0.25 | 0.03175 | 0.04462 | 0.2585 | 45 | 29 |
| 0  | 0.50 | 0.02742 | 0.03585 | 0.4691 | 63 | 27 |
| 0  | 0.75 | 0.02459 | 0.03560 | 0.6842 | 89 | 30 |
| 42 | 0.25 | 0.03100 | 0.04895 | 0.3008 | 30 | 26 |
| 42 | 0.50 | 0.02439 | 0.03776 | 0.4956 | 45 | 24 |
| 42 | 0.75 | 0.02322 | 0.03601 | 0.7317 | 68 | 25 |

### 10.2 CORRECTION -- amplitude ladder and the R1 dilution defect (now APPLIED INLINE)

Both corrections this section originally carried have been **applied to sections
4.3, 5.1 (G4) and 5.2 directly**, so those sections are current and this is a
pointer, not a superseding note. In summary:

1. The 0.02/0.05/0.10 ladder was sized against GFLAG-0354's nominal band rather
   than the measured residual dispersion, putting its top rung at 4.07 SD --
   total suppression. Replaced by 0.010/0.020/0.040 with 0.100 retained as an
   explicit saturating positive control (4.3, with the predicted in-sweep ladder).
2. **The R1 readout could not discriminate.** At a 20% duty cycle the run-mean
   occupancy is predicted inside `P1_OCCUPANCY_BAND` at all 12 (amplitude x
   quantile) combinations -- including where in-sweep occupancy is 0.0000 -- so
   "P1 holds" would have been returned identically by a working sweep and by one
   that annihilates commitment. R1 is now partitioned on `clock.sweep_active`
   (R1a in-sweep is the deliverable, R1c run-mean is telemetry), and G4 is tested
   on R1a (5.1, 5.2).

Found by arithmetic on 1070a's own recorded dispersion, before any compute was
spent. Cell count 36 -> 45, budget 90 -> 120 minutes.

---

## 11. WITHDRAWN -- the oscillator cannot fire at L1 (2026-09-22, GFLAG-0421)

Found at `/queue-experiment` Step 2.5d, before any driver was written.

**Mechanism, at source.** `Clock.reset()` sets `_breath_phase_step = 0`
(`ree-v3 ree_core/heartbeat/clock.py:231`, its own comment: *"MECH-108: reset
breath cycle state across episodes"*). `REEAgent.reset()` calls it
(`agent.py:3718`). Every driver in this family calls `agent.reset()` per episode.
The sweep is active only while `_breath_phase_step >= breath_period -
sweep_duration` (`clock.py:120`), and the counter advances once per env step
(`clock.py:170`). **So the sweep fires only if an EPISODE is long enough to reach
that phase.**

**Measured at L1**, from 1070a's own `arm_results`: mean episode length
**7.99-13.97 env steps** across the six cells (`min_episode_length` 5-6), against
a sweep that at this spec's `breath_period=25 / sweep_duration=5` begins at phase
step **20**. It is never reached. A run would have reported "alternating arm
indistinguishable from static" -- a confident null on a manipulation that never
happened.

**This is not a parameter typo.** `breath_period` must be shorter than the
episode, but L1 episodes are only **7.0-8.8 select calls** long while 1070a's
`mean_committed_run_length` is already **4.56-6.62** -- a committed run fills most
of an episode, leaving no room for a within-episode alternation between two
regimes of >= 3 ticks. Shrinking `sweep_duration` far enough to fire turns the
sweep into isolated de-committed SELECTIONS rather than the uncommitted WINDOWS
ARC-029's text describes. **It is the section-5 P1/P3 bind of
`failure_autopsy_V3-EXQ-1070a_2026-09-22`, reappearing in the ARM rather than the
bar:** the env that keeps `harm_snr` above the P3 floor has episodes too short to
host the oscillation.

### 11.1 Disposition, and why this spec is withdrawn rather than repaired

**User decision 2026-09-22: drop the oscillator; the variance-tracking bar alone
is the manipulation.** ARC-029's `what_would_answer` permits it -- *"the
variance-tracking quantile commitment bar, **or** a MECH-108 BreathOscillator
sweep"*. That makes GFLAG-0416's open construct question load-bearing rather than
incidental: **governance must rule on the "or"** before an ARC-029 successor is
designed.

With the oscillator gone, every question sections 1-5 pose is already answered by
1070a -- Q1 is moot, Q3 is answered (P1 holds 6/6 at L1), Q2 is substantially
answered (`|occupancy - q| <= 0.0658`, dispersion recorded), and R3 is not
testable because bar-alone has no non-degenerate control (see 9.2). So the probe
dissolves. **Nothing was queued.**

### 11.2 What IS unmeasured -- the actual gap a successor should close

1070a carries `mean_harm_per_step`, `harm_snr` and `sd_harm_per_step` but **no
committed-vs-uncommitted split**: `harm_per_step_committed`,
`harm_per_step_uncommitted`, `n_steps_committed` and `n_steps_uncommitted` are all
absent from every cell.

**ARC-029's C1 -- "committed windows carry lower harm per step than uncommitted
windows in the stable env" -- has never been measured at an operating point where
P1 and P3 both hold.** `v3_exq_1066_...py`'s `_Roll.harm_by_state` already
computes it, so the successor is a short derivation. But it is an EVIDENCE run,
and it is blocked on two things: the "or" ruling above, and the control-arm gap in
**9.2** (under bar-alone the natural control is the static ABSOLUTE threshold,
which is degenerate at a trained operating point -- occupancy 1.0000, the measured
V3-EXQ-063a defect).

### 11.3 Two instrument facts banked for that successor

- **`e3_score_decomp_enabled` defaults `False`** (`e3_selector.py:639`) and gates
  the entire `last_score_diagnostics` block (`:4099`). A driver that omits it
  measures occupancy **0.0, silently**. Reproduced live in this session's probe:
  **0 select calls recorded while the commit window filled to 200/200.** 1066 sets
  it at `:481` and `:717`; any derivation must keep both.
- **`commit_threshold_quantile` IS read live per bar computation**
  (`e3_selector.py:985`). Confirmed by mutating it on a built agent: bars
  1.809e-03 / 2.967e-03 / 4.498e-03, monotone in q, window fill unchanged at 200.
  **One trained agent can serve every quantile** -- a 3x training saving for any
  successor that sweeps q.
- Also measured, and a warning for any ladder sized off 1070a's numbers: the
  log-residual dispersion is **0.719 untrained** vs **0.0232-0.0318 trained**. Any
  amplitude or threshold ladder calibrated in SD units needs a P0 readiness assert
  on the TRAINED dispersion, or it lands in a different regime than designed.
