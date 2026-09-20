# ARC-029 / V3-EXQ-1066 -- pre-registration derivation record

- **Date:** 2026-09-19
- **Session:** `metaworker-science-20260919-arc029-p1p3-retest` (campaign `science-20260919-arc029-p1p3-retest`, box `ree-cloud-4`)
- **Chip:** `chip-20260916-arc029-p1p3-redesign-queue`
- **Authority:** user approval 2026-09-19T22:12:50Z via the orchestrate-20260919-2125 campaign lane --
  "Pre-register q, commit_threshold_quantile_window, precision_ema_alpha and e3_steps_per_tick FROM THE
  BUILD RECORD'S MEASURED (q, W) OCCUPANCY SURFACE, stating the rule used; sweep_amplitude and the
  G1/G2 floors as EXP-1394 / ARC-029 what_would_answer give them."
- **Sources, in precedence order:**
  1. `REE_assembly/docs/claims/claims.yaml` ARC-029 `what_would_answer` (P1/P2/P3, CONFIRMING, FALSIFYING)
  2. `REE_assembly/evidence/planning/experiment_proposals.v1.json` **EXP-1394** (G0-G2, C1-C4)
  3. `REE_assembly/evidence/planning/arc029_variance_tracking_commit_bar_build_20260918.md` (the measured surface)
  4. `ree-v3/ree_core/utils/config.py:1250-1310` (the lever's own registered semantics)

**STALE NOTE, recorded because a reader will otherwise stand down:** this chip's `claim_note` still
reads "BLOCKED on chip-20260918-arc029-p1-lever-operating-point ... P1 unsatisfiable as specified".
That is stale. The variance-tracking commit bar landed on `ree-v3` `origin/main`
(`6bac3753` -> `9862ed61` -> `3bb81276`), the blocking chip is `done`, and P1's occupancy half is
now satisfiable on every measured cell.

---

## D1 -- q, W, precision_ema_alpha, e3_steps_per_tick

**THE RULE (stated once, applied four times).** P1/G0 has two halves and they are chosen by
different criteria because the build surface constrains them differently:

- **Occupancy** (`committed_step_fraction` in [0.15, 0.85]) is satisfiable on *every* measured
  cell, so the free parameter is chosen to **maximise the minimum distance to the band edges**.
- **Mean committed-run length >= 3** clears on only one cell at the agent's default cadence
  (3.36, a 12% margin, on a synthetic stream, before any seed variation). So it is chosen to
  reach **>= 2x margin over the >= 3 floor using only DIRECTLY-MEASURED cells** -- no
  interpolation between measured points -- and using the levers the build record and
  `config.py` identify as the effective ones for run length.

### q = 0.50
Margin `min(f - 0.15, 0.85 - f)` over the nine measured (q, W) cells:

| q | W=50 | W=200 | W=500 |
|---|---|---|---|
| 0.25 | 0.19 | 0.12 | 0.12 |
| **0.50** | **0.33** | **0.32** | **0.30** |
| 0.75 | 0.16 | 0.16 | 0.09 |

The q=0.50 row dominates at every W. It is also the **only** q for which the build re-measured
the run-length response across the select()-to-env-tick ratio, so it is the only q whose
run-length lever is calibrated at all. -> **q = 0.50**.

### commit_threshold_quantile_window W = 200
`config.py:1265-1274` states, from measurement, that W does **not** control run length
(~3.2 -> ~3.4 across a 40x range, saturating by W~50); it controls the **warmup** (counted in
SELECT CALLS) and how much within-run drift the single linear detrend term must describe.
Occupancy margin within the q=0.50 row is 0.33 / 0.32 / 0.30 -- indistinguishable. So W is
chosen on its actual function, by a tie-break the pre-registration genuinely depends on:
**W=200 is the only window at which BOTH companion surfaces were measured** -- the estimator
negative controls (build sec 3C) and the MECH-108 amplitude response (sec 3D). Pre-registering
an amplitude ladder off sec 3D while running a different W would be quoting a surface that was
never measured. -> **W = 200** (warmup 200 select calls = 600 env ticks at the cadence below).

### e3_steps_per_tick = 3
Directly measured at q=0.50: mean committed-run length **10.41 / 6.10 / 3.36 / 2.60** at a
variance-update:select ratio of **1 / 3 / 10 (agent default) / 20**. The >= 2x-margin rule
selects the **largest (least-perturbing) measured ratio that clears 6.0**: ratio 3 -> 6.10
(2.03x). Ratio 1 gives more margin (10.41) but costs 10x the select() compute and is the
largest departure from the agent's default. -> **e3_steps_per_tick = 3**.

### precision_ema_alpha = 0.05 (the DEFAULT, explicitly held and pre-registered as held)
Two reasons, both binding:
1. The measured alpha cells are 0.5 / 0.05 / 0.001 -> 2.0 / 3.4 / 14.1 ticks. There is **no
   measured cell between 3.4 and 14.1**, so any alpha meeting the >= 2x rule would require
   INTERPOLATION, which the rule forbids. (The consistency check that validates the whole
   surface: alpha=0.05 -> 3.4 and cadence 10:1 -> 3.36 are the same measurement, so the two
   ladders agree at their shared point.)
2. `precision_ema_alpha` is the EMA constant on `running_variance`, hence directly on
   `current_precision = 1/(running_variance + 1e-6)` -- **the exact quantity G1 gates on**.
   Moving it off default changes the precision distribution the invariance gate is read
   against, in both arms. The cadence lever does not.
   A third, non-decisive reason worth recording: alpha -> 0.001 makes rv so sluggish that the
   window approaches the **all-equal degenerate case** red-team fix 1 guards (relative-spread
   guard returns None, the absolute bar comes back, saturation returns). Backing off the
   extreme alpha cell avoids walking toward that guard on purpose.

So the cadence carries the run-length requirement and alpha is held. -> **precision_ema_alpha = 0.05**.

**All four read off directly-measured cells. No decision chip is owed under the user's
escalation clause.**

---

## D2 -- sweep_amplitude: a pre-registered CALIBRATION, because that is what the claim asks for

ARC-029 P2's registered instruction is a **rule, not a number**: *"Set `sweep_amplitude` from the
run's own measured `rv` distribution, not from a guess."* Its worked numbers (`a > 0.18`,
`> 0.986`) are measured stale in both directions (GFLAG-0354, build sec 3D). The build supplies
the workable band on the quantile bar -- **a in [0.02, 0.10]** -- with its own caveat that the
steepness of that response is set by the residual spread, "a property of the synthetic stream
here", and must be re-measured on a real trained agent.

A fixed pre-registered amplitude therefore cannot be honest. **Pre-register the procedure:**

- **Ladder (pre-registered, from the measured band plus its two shoulders):**
  `a in {0.005, 0.01, 0.02, 0.03, 0.05, 0.07, 0.10}`.
- **Calibration phase**, per seed, on the trained agent, on episodes DISJOINT from the measured
  ones: run each rung, record `committed_step_fraction`, the committed-run-length **histogram**,
  and `mean log10(current_precision)` against the ARM_STATIC control.
- **Selection rule:** take the **largest** `a` satisfying all three of
  (i) `committed_step_fraction` in **[0.20, 0.80]** (a margin-interior sub-band of P1's [0.15, 0.85]),
  (ii) mean committed-run length **>= 4.5** (1.5x P1's floor),
  (iii) `|mean log10(current_precision)(ALTERNATE) - (STATIC)| <= 0.20` decades (the G1 bound below).
  Largest, because the sweep IS the manipulation and a stronger drive gives a cleaner two-mode
  contrast; bounded by (iii) because a stronger threshold perturbation also has more room to
  mediate into precision through behaviour.
- **Failure branch:** if no rung satisfies all three on **>= 4/5 seeds**, the run is
  **`non_contributory`**, not evidence -- ARC-029's own instruction ("if occupancy or
  precision-invariance fails to gate cleanly, the run is `non_contributory`, not evidence").
- The gates are then **re-evaluated on the held-out measured episodes**. Selecting `a` on
  calibration data and testing on disjoint data is what keeps this from being a gate that
  passes by construction.

---

## D3 -- G2's harm floor: derived, not invented

EXP-1394's G2 is *"per-seed harm rate >= 10x the measurement floor"*; ARC-029 P3 is *"at least an
order of magnitude above the measurement floor"*. **Both are relative to a floor neither defines.**
P3's assertion that 063a's ~-0.055 harm/step is "a demonstrated workable operating point, so this
is a calibration requirement, not an open problem" is the stale part: the recalibrated env measures
**0.0025-0.0068** harm/step (build sec 5.3) and the dead session's real-length smoke measured
0.0056-0.0136 against a 0.01 absolute floor -- i.e. the DV sat BELOW its own gate.

The **measurement floor** of a rate estimated from discrete harm events over `N` steps is one
resolvable event: `1/N`. So G2's own registered wording resolves to:

> **G2 passes iff, per seed per condition, `harm_events >= 10`** (equivalently
> `harm_rate >= 10 / steps`), on >= 4/5 seeds.

No constant is invented, it scales with the episode budget, and at the measured 0.0025-0.0068
harm/step it is comfortably attainable. **This replaces the absolute 0.01 floor the dead session
tripped on -- which was never in EXP-1394 or the claim.**

**C1 IS NOT TOUCHED.** `max(0.5 * SD(per-seed paired delta), 0.002 harm/step)`, same sign on
>= 4/5 seeds, transcribed verbatim. The build record's section 6 *recommends* re-expressing C1
relatively; that is a governance act on a pre-registered falsifier and is explicitly a STOP for
this session. The driver instead **reports** the relative effect and the **seed variance of
harm/step** (the quantity the build record says nobody has measured and the re-queue must
supply) as pre-registered descriptive outputs, so governance can re-express C1 later on measured
ground. If C1 nulls, the pre-registered interpretation is stated with it: a null at 0.002 against
a base of `b` excludes relative effects `>= 0.002/b`.

---

## D4 -- G1's precision-invariance floor: derived from the confound it exists to exclude

EXP-1394 says *"below a pre-registered floor"* and names none. The quantity is
`current_precision = 1/(running_variance + 1e-6)`, which moves by orders of magnitude, so the
floor must be in **log10 units** or it is not scale-free -- the same defect that produced this
whole lineage.

**The magnitude G1 must exclude is measured.** V3-EXQ-063a forced `running_variance` to 0.50,
i.e. `precision = 2.0`, against an operating point measured at `rv ~= 0.00542` (V3-EXQ-794), i.e.
`precision ~= 184.5`. That fiat confound is `log10(184.5 / 2.0) = **1.97 decades**`. The dead
session's finding was precisely that a 0.50 ceiling *"could not distinguish genuine mediation from
V3-EXQ-063a's fiat confound"*.

**Rule: the floor is one tenth of the confound it exists to exclude -- a 10x discrimination
margin.** `1.97 / 10 = 0.197` -> **0.20 decades**.

> **G1 passes iff, per seed, BOTH `|Δ mean log10(current_precision)| <= 0.20` and
> `|Δ SD log10(current_precision)| <= 0.20` between ARM_ALTERNATE and ARM_STATIC, on >= 4/5
> seeds; AND (power condition) the across-seed SD of the paired mean delta is itself
> `<= 0.20` decades**, so an "equivalence" verdict cannot be bought with seed noise.
> **AND the source-level assert**: no direct assignment to `e3._running_variance` anywhere in
> the driver. That is the check V3-EXQ-063a would have failed, and it is the primary defence;
> the distributional test is the empirical backstop.

0.20 decades is a 1.58x ratio in precision. **The way this could be wrong, stated:** the
alternating arm changes which actions are committed, which changes behaviour, which changes
prediction error, which changes `rv` -- a REAL causal path that is mediation, not fiat. If
behavioural mediation exceeds 0.20 decades, G1 fails and the run is `non_contributory` rather
than evidence. That is a cost outcome, not a validity failure, and it returns the one number
nobody has: the size of the behavioural mediation. The calibration phase's condition (iii)
above is what makes that outcome unlikely rather than a lottery.

---

## What this session explicitly did NOT decide

- **C1's threshold** -- transcribed verbatim (a STOP under the dispatch brief).
- **Raising the env harm parameters** (`hazard_harm`, `proximity_harm_scale`) -- not applied;
  the build record's own recommendation (ii) is followed instead, and `/governance` owns the
  question of re-expressing C1.
- **The scale-free alternative manipulation** (modulate `q -> q - delta` instead of multiplying
  the bar). It is not built on `origin/main`, and ARC-029's P2 names the MECH-108 multiplicative
  `effective_threshold = base * (1 - sweep_amplitude)` as THE threshold-side driver. Building a
  different manipulation would change what is measured. It stays where the build record put it:
  a question for the user, recorded here and in the queue entry, not answered here.
- **`use_natural_commit_latch_hold`** -- NOT armed. It sustains commitment (built for the
  V3-EXQ-460i fragmentation failure, occupancy too SHORT); the measured failure is the opposite,
  saturation at 100% committed. GFLAG-0354 carries this; ARC-029's P1 text and 063a section 8
  both route there and both are stale on this point.

---

# ADDENDUM 2026-09-19T23:10Z -- MEASURED ON `ree-cloud-4`, AND THE RUN IS **NOT QUEUED**

The pre-registration above is sound as an exercise in reading the build record's
surface. **It does not survive contact with a real agent in the ARC-029 lineage's own
environment**, and the reason is not any of the four parameters the dispatch brief
scoped. Everything below was measured in this session, not argued.

Interpreter `/home/ree/.venv/ree/bin/python3`, torch 2.12.0+cpu, python 3.10.12,
`ree-v3` at `origin/main` 2be3c89a + this session's own `2adcad2063`.
Driver: `ree-v3/experiments/v3_exq_1066_arc029_commitment_mode_harm_variance_bar.py`
(committed, **NOT queued**, `V3-EXQ-1066` reservation closed `--not-landed`).

## M1. The lever is REACHABLE and its sentinels work (Step 2.5a probe, PASS)

`from_dims(use_variance_tracking_commit_threshold=True, commit_threshold_quantile=0.50,
commit_threshold_quantile_window=200)` arrives at all three wiring sites;
`config.e3.precision_ema_alpha` and `config.heartbeat.e3_steps_per_tick` are
sub-config fields (NOT `from_dims` parameters) and take effect
(`agent.clock.e3_steps_per_tick == 3`); the unset-sentinel `ValueError` fires when the
lever is armed without q/W. The commit window is built (`maxlen 200`) and is never
cleared by `agent.reset()`, so it persists for the life of the selector.

**One wiring fact that is not written down anywhere and silently zeroes the
instrument:** `last_score_diagnostics` is populated only under
`if self.e3_score_decomp_enabled:` (`e3_selector.py:4098`), which is an
INSTANCE attribute defaulting to `False` (`:639`), not a config field. Without
`agent.e3.e3_score_decomp_enabled = True` the dict is never written, and a driver
reading `committed` from it measures **0 selections out of ~120** and reports
occupancy 0.0 with no error. Measured directly.

## M2. THE BLOCKER -- episodes are 4-9 ENV STEPS at this lineage's env parameters

`CausalGridWorldV2` at V3-EXQ-125a's own kwargs (`size=12, hazard_harm=0.05,
proximity_harm_scale=0.15, proximity_benefit_scale=0.03, hazard_field_decay=0.5`),
25 episodes per row, random policy, `done_cause` recorded:

| `num_hazards` | mean episode length | min | max | mean reward/step | terminal cause |
|---|---|---|---|---|---|
| 3 (P1's LOW density) | **9.4** | 6 | 17 | -0.121 | `health_depleted` |
| 5 (the train density) | **6.2** | 4 | 11 | -0.178 | `health_depleted` |
| 7 (P1's HIGH density) | **4.4** | 3 | 7 | -0.261 | `health_depleted` |
| 8 (125a's own density) | 4.6 | 2 | 12 | -0.288 | `health_depleted` |

A TRAINED agent (P0a 20 + P0b/P1 60 episodes x 120 steps, SD-070 z_world warmup on,
`rv` 5.0e-01 -> 9.0e-03) does not escape it: measured 5 to 22 env steps per episode,
**4.9 to 7.3 SELECT CALLS per episode**.

### M2a. Consequence one: the bar NEVER TAKES FORCE, and saturation is reproduced

On the trained agent, across q in {0.25, 0.50, 0.75, 0.90} and sweep amplitudes
{0.0, 0.02, 0.10}, in **every** cell:

    bar_in_force = 0.000    committed_step_fraction = 1.0000    n_committed_runs = 1

The window never filled, so `_variance_tracking_commit_bar()` returned `None` on every
tick and the ABSOLUTE 0.40 bar stayed in force against `rv ~ 0.008`. **That is the
V3-EXQ-063a saturation defect, reproduced exactly, with the new lever armed.** It is
not a defect in the lever: W=200 is counted in SELECT CALLS, and at ~5-7 select calls
per episode the window needs **~30-40 EPISODES** to fill.

### M2b. Consequence two: the window is not a WITHIN-RUN distribution

Filling W=200 spans ~35 episode boundaries. The estimator's stated premise is that
"rv drifts ~5x WITHIN a single run" and that one linear term in log-space describes
that drift (`config.py:1241-1249`; build record sec 2). Pooled across ~35 resets it is
describing a between-episode ensemble instead. Every occupancy number on the build
record's (q, W) surface was measured on a 1200-tick CONTINUOUS synthetic stream, which
is a different object.

### M2c. Consequence three: P1's two halves are at the edge of arithmetic feasibility

P1 wants, within a single run, `committed_step_fraction` in [0.15, 0.85] AND mean
committed-run length >= 3. With E select calls per run, at least one committed run of
>= 3 requires `f * E >= 3`, i.e. `E >= 3/f`:

| f | required E | measured E (trained) |
|---|---|---|
| 0.85 | 3.5 | 4.9 - 7.3 |
| 0.50 | 6.0 | 4.9 - 7.3 |
| 0.15 | 20.0 | 4.9 - 7.3 |

So P1 is jointly satisfiable only in the UPPER part of its own occupancy band, with
roughly ONE committed run per episode -- i.e. "the episode is mostly committed, with
uncommitted ticks at its edges". That is an episode-phase contrast, not the within-run
two-operating-mode structure the claim asserts, and V3-EXQ-460i's finding is exactly
why P1's run-length half was made load-bearing.

## M3. Two further facts the pre-registration assumed and that do not hold

- **`e3_steps_per_tick` does NOT set the effective select cadence.** Configured at 3,
  the MEASURED env-steps-per-select is **1.0 to 3.6** across cells. MECH-091
  `phase_reset` forces an E3 tick on salient events and this env delivers a negative
  reward on essentially every step. So D1's run-length lever is not the lever the build
  record characterised, and NEITHER named run-length lever (`precision_ema_alpha`,
  `e3_steps_per_tick`) is usable as described.
- **P3's premise is inverted here.** ARC-029 P3 worries the harm DV sits too LOW.
  Measured mean reward/step is **-0.12 to -0.29**, i.e. 2-5x ABOVE 063a's -0.055 and
  20-100x above the build record's recalibrated 0.0025-0.0068. The env is lethal
  enough that the agent dies in 4-9 steps -- which is precisely what destroys P1.

## M4. The BIND, stated plainly

**P1 and P3 pull in opposite directions through the same parameter.** Softening the env
(fewer hazards / lower `hazard_harm` / lower `proximity_harm_scale` / more starting
health) lengthens episodes until a within-run two-mode structure exists -- and pushes
the harm DV back toward the floor P3 exists to keep it off (EXQ-227's ~100x cut).
Keeping the lineage env keeps the DV off the floor -- and leaves episodes too short for
the window to fill or for P1 to be met as a within-run property.

No value of q, `commit_threshold_quantile_window`, `precision_ema_alpha`,
`e3_steps_per_tick`, `sweep_amplitude`, or either of the G1/G2 floors resolves it. It
is an ENVIRONMENT question -- the lever the build record's sec 6 explicitly declined to
pull ("Both are therefore set at re-queue time, by the `/queue-experiment` unit, under
the user's eye") and whose recorded recommendation (do NOT raise env harm; re-express
C1 relatively) points the OPPOSITE way from what P1 now needs.

Shrinking W is not a third way out: W=50 is the smallest measured cell and still needs
~10 episodes, and below the rv EMA time constant (~1/alpha ~ 20 select calls) the bar
tracks rv almost instantaneously and committed runs degenerate towards a single tick --
the estimator's own documented failure mode (`config.py` window-width comment), which
fails P1's run-length half by construction.

## M5. Disposition

**NOT QUEUED. NO live `V3-EXQ-1066`.** The reservation claim was closed `--not-landed`
and the id is free. `EXP-1394` is left at `status: proposed`; the refusal is recorded
machine-readably as a governance flag (`evidence_discrepancy`, ARC-029) rather than as
prose only. The driver is committed for the successor to start from, carrying a
DO-NOT-QUEUE banner.

The choice is the user's and is raised as a `kind: decision` chip. **Recommendation:
do NOT spend a 5-seed evidence run on any of the three options. Spend one cheap
`diagnostic` run first** -- sweep the env harm parameters and measure, per setting,
(episode length, select calls per episode, |mean harm/step| and its SEM, and occupancy
+ committed-run-length histogram with the bar CONFIRMED in force at q in
{0.25, 0.50, 0.75}) -- and report the region, if any, where P1 and P3 are jointly
satisfiable. That is the measurement the build record sec 6a already says is owed
("the rv residual dispersion on a REAL trained agent, on which the whole
alternating-arm design's viability rests"). Its NEGATIVE outcome is already a
pre-registered disposition of the claim, so it cannot be wasted: ARC-029's own P1 says
"If P1 still fails with those armed, ARC-029 converts to `substrate_conditional` on
commitment-occupancy sustainment and this falsifier is not readable."

---

# ADDENDUM 2 -- 2026-09-20T00:55Z: OPTION C CHOSEN AND QUEUED

User decision 2026-09-19T23:52:40Z (real `AskUserQuestion` via the Orchestrator
`orchestrate-20260919-2125`) on `chip-20260919-arc029-p1p3-env-operating-point`:
**OPTION C -- one cheap diagnostic first, no evidence run.**

**QUEUED: `V3-EXQ-1070`** -- `ree-v3 d0c644f3e2` on `origin/main`, RECONCILED into the
coordinator DB (verified credential-free by snapshot survival: the entry is still present
after the `phase3-queue: snapshot 2026-09-20` re-materialisation `0b7efa6e`). Driver:
`ree-v3/experiments/v3_exq_1070_arc029_env_operating_point_feasibility.py`.

`EXP-1394` is deliberately left at `status: proposed`. This diagnostic does NOT execute
it; the evidence design it names is still the blocked one.

## Design, and the two facts that shaped it

A cross-product over the four env knobs the decision named would be ~16x the cells for no
extra information, because they all act on the SAME conserved quantity. Two measurements
made that concrete:

1. **`agent_health` is HARD-CODED to 1.0** (`causal_grid_world.py:1774, :2083, :2216`) and
   is drained by `abs(harm_signal)` per harm step (`:2642`). **There is no starting-health
   constructor parameter**, so "lengthen episodes without shrinking the DV" -- the one
   option that could have dissolved the bind -- is not reachable with existing levers.
2. **The bind is therefore an identity, not a tendency.** Measured over a 6x range of
   episode length (random policy, 30 episodes/rung): `episode_length x |mean reward/step|`
   = 1.02 / 1.10 / 1.09 / 1.25 / 1.27 / 1.42.

So the grid is a one-dimensional **lethality ladder**, pre-measured so it spans rather than
clusters: L0 (the V3-EXQ-125a lineage point, 6.2-step episodes) -> L1 (10.8) -> L2 (22.5)
-> L3 (29.5) -> L5_extreme (1 hazard; tests whether the ~30-step plateau is structural).
5 rungs x q in {0.25, 0.50, 0.75} x 2 seeds = 30 cells.

## What the red-team pass changed -- CONTESTED, six findings, all fixed

Run in the foreground on Fable (this session runs on Opus), one pass, not iterated to
CLEAR. Every finding was verified against source or against the driver's own dry-run
manifest before being acted on; none was dismissed.

| | finding | how it was confirmed | fix |
|---|---|---|---|
| F1 | the committed-run histogram walked the FLAT cross-episode sequence, so P1's run-length half was BLIND to episode length -- the very quantity the ladder manipulates and the verdict text blames | the driver's own dry-run manifest: `n_episodes 2`, `n_select_calls 14`, histogram `{'14': 1}` -- ONE run across both episodes | runs cut at episode boundaries; both views reported (now **7.0** per-episode vs **21.0** flat) |
| F2 | `|mean| >= 10 x SEM` is SCALE-INVARIANT, so it could certify a soft rung at a harm rate where C1's untouched 0.002 bar is a 25% relative effect -- the EXQ-227 floor regime P3 exists to exclude | arithmetic: scaling every harm parameter by k scales mean and SD alike | second conjunct `|mean| >= 0.002/0.20 = 0.01`, DERIVED from C1's own floor and the build record's own "excludes relative effects >= 20%"; plus an autocorrelation-corrected SEM (measured lag-1 rho **0.573**, which moves SNR 5.99 -> **3.12**); plus a fixed ENV-STEP denominator, since stopping on select calls alone handed the softer rungs up to 3.6x more samples |
| F3 | the harm DV was the NET signal, which carries BENEFIT (`:2410`), and the ladder drives `proximity_harm_scale` BELOW the fixed `proximity_benefit_scale` at soft rungs -- so a near-zero net there is CANCELLATION, not "harm on the floor" | source | P3 routes on `env.total_harm` deltas; net and benefit reported beside it |
| F4 | training was budgeted in EPISODES while `_train_all_on_agent` breaks on `done`, so training depth scaled ~5x along exactly the manipulated dimension -- corrupting both the rv-dispersion deliverable and the worst-cell readiness gate | dry run: 20 vs 15 ticks at identical episode budgets | per-rung episode counts derived from the pre-measured lengths to equalise TICKS (realised **1710-1740**, spread **1.02**), recorded, and gated by a new `training_tick_budget_equalised` precondition |
| F5 | D4's stated inference rule was foreclosed by this run's own warm budget: L0 will NOT reproduce the predecessor's saturation, because that was a 12-episode warm cap against a 200-select window | arithmetic: 200 / ~7 selects-per-episode ~ 29 episodes < the 250 cap | docstring corrected. **If L0 shows the bar in force, that is itself the finding** -- the predecessor's saturation was a warm-budget artifact, not an env property |
| F6 | the three q cells share one agent in a fixed order and `agent.reset()` does not clear residue | `agent.py:3586` | q order counterbalanced by seed; order recorded per cell |

Not re-spawned: the verdict was CONTESTED, not BLOCKING.

## Pre-registered disposition -- RECORDED BY THE RUN, NOT APPLIED

- **No jointly-feasible rung** -> ARC-029 converts to `substrate_conditional` on
  commitment-occupancy sustainment, per ARC-029's OWN P1 text.
- **A region found** -> the pre-registered V3-EXQ-063b design
  (`experiments/v3_exq_1066_arc029_commitment_mode_harm_variance_bar.py`) is re-queued at
  that setting, with C1 re-expressed if needed.

Both are user decisions. The run writes neither into `claims.yaml`; it emits the numbers
and the routing text. `manifest["disposition_rule_preregistered"]["applied_by_this_run"]`
is `False` by construction.

## Estimate caveat, stated rather than buried

`estimated_minutes: 330` is a central estimate from per-step cost measured on `ree-cloud-4`
(~214 ms/step eval, ~396 ms/step train-mode). Under sibling-session contention it may reach
5-6h, which is above the ~2-3h the option-C framing assumed. Two seeds were retained
because the feasibility predicate requires BOTH seeds -- at n=2 a "majority" is not a thing.
