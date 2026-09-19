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
