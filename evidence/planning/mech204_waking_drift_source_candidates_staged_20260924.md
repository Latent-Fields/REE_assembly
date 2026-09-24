**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# MECH-204 / SD-076 successor: candidate waking drift-source mechanisms

- Staged 2026-09-24T17:51:00Z by headless science session
  `metaworker-science-20260924-orchc-mech204-drift-source` (campaign
  `science-20260924-orchc-mech204-drift-source`, chip
  `chip-20260920-mech204-new-waking-drift-source`).
- **DESIGN PHASE ONLY. No `ree_core` code was written and none may be written until the
  choice below is ratified.** The chip's own TASK section mandates this: "This is a DESIGN
  choice that changes what gets measured -- present the candidate mechanism(s) to the user
  ... BEFORE writing ree_core code."
- Decision chip carrying this question into the consent lane:
  `chip-20260924-mech204-driftsource-choice`.
- Prior record this builds on, do not re-derive:
  `exq541d_redteam_blocking_refusal_staged_20260919.md` sections 7-8;
  manifest `v3_exq_794a_mech204_phase7_sd076_calibration_loop_2x2_20260724T063301Z_v3.json`.

---

## 1. Why a new mechanism is owed (re-measured, not assumed)

STOP-CHECK run 2026-09-24T17:47Z against live state:

| premise | verdict |
|---|---|
| Gap live at `ree-v3/ree_core/predictors/e3_selector.py:1027` ("SD-076: waking confidence-inflation source (asymmetric EMA)"), only the rv-floor headroom repair added since | CONFIRMED. Last three touches to that file are `52096b7` (SD-092), `9862ed6`/`6bac375` (ARC-029) -- none touch SD-076. |
| No new drift-source entry staged | CONFIRMED. `substrate_queue.json` has only `sd_waking_confidence_inflation_headroom` (the superseded repair) and the MECH-204 Phase 7 entry; 0 hits for MECH-204/SD-076 in `igw_routine_ledger.json` / `igw_assignments.json`. |
| No open governance flag reopening or reversing the disposition | CONFIRMED. 9 flags mention MECH-204/SD-076; all `resolved` or `superseded` (GFLAG-0206, -0279, -0349, -0369, -0377, -0379, -0384, -0385, -0391). |
| Resource arbitration | `ree-v3/ree_core/predictors/e3_selector.py` is owned right now by `metaworker-science-20260924-mech320-margin-hook` (claimed 17:06:20Z). **This design phase does not touch it.** The post-consent build must open its own claim and arbitrate then. |

V3-EXQ-794's own pre-registration is the routing authority: *"if C1 fails at BOTH levels the
route is NOT 'sweep higher': it is that the asymmetric-EMA form is the wrong drift source and
a different SD-076 mechanism is owed."* C1 failed at both LO 0.6 and HI 0.8. This document is
that different mechanism, at the design stage.

---

## 2. What 794a actually measured, and the structural reason it failed

DV: `overconfidence_score = log(true_error_ref / mean_rv)`; C1 requires `> +0.10` (i.e.
`mean_rv / true_error_ref <= 0.9048`) on `>= 2/3` seeds.

Arm means (from the landed manifest's `aggregates`):

| arm | `mean_rv / true_error_ref` | `overconfidence_score` | clears C1 |
|---|---|---|---|
| `ARM_OFF_OFF` (no drift) | 1.245 | -0.192 | no |
| `ARM_INFL_LO` (asym 0.6) | 1.043 | -0.041 | no |
| `ARM_INFL_HI` (asym 0.8) | 1.023 | -0.023 | no |

Best single cell over all 18: `ARM_INFL_HI` seed 2, ratio **0.986** (score +0.0143) -- against
a required 0.9048. **Every readiness precondition passed** (`rv_live` 0.48-0.49,
`inflation_lowers_rv` 0.0014-0.0057, `dose_levels_separated` 1.27e-4 / 2.86e-4, no clamping).
The lever works. It is ~7x too weak, and the weakness is structural, not a tuning miss.

### 2a. The structural bound (this is the load-bearing finding)

The asymmetric EMA is a **conditional-gain modification of the same estimator**, applied to the
same realised per-tick squared error `e_t`. Its fixed point satisfies

```
(1 + asym) * E[(rv - e)+]  =  (1 - asym) * E[(e - rv)+]
```

i.e. `rv*` is the **expectile of the `e` distribution at level tau = (1 - asym) / 2**
(asym 0.6 -> tau 0.2; asym 0.8 -> tau 0.1). An expectile's displacement from the mean is
**proportional to the dispersion of `e`**. In a converged regime the per-tick squared
prediction error is tightly concentrated, so the displacement collapses -- and it collapses
exactly in the regime the item needs (section 7b of the refusal record selected the survivable
regime precisely because it makes rv CONVERGE).

The measured dose response is the evidence: halving tau from 0.2 to 0.1 bought **1.9%**
displacement (1.043 -> 1.023). The C1 bar needs **10.5%**. Remaining tau budget is 0.1, and
794 already ruled out sweeping higher.

> **Therefore: any mechanism whose steady state is a functional of the realised-`e`
> distribution alone inherits this bound.** The new mechanism must inject displacement whose
> magnitude is set by a CONFIG parameter rather than by the spread of `e`.

Stated as a limit rather than an extrapolation: the two measured points do not prove the
tau -> 0 asymptote, and this document does not claim they do. What they do establish is that
the marginal return per unit of tau is ~2% and the requirement is 10.5%, so the remaining
budget cannot plausibly cover it -- which is the same conclusion 794 pre-registered on
qualitative grounds.

### 2b. Family R -- REJECTED, and why it must be named

Rejected as inheriting the 2a bound: harsher asymmetry (`asym -> 1`), a sliding-window low
**quantile** tracker, a trimmed/winsorised estimator, a "believe the best of the last N ticks"
rule, or any other reweighting of the same `e` stream. Each is a different statistic of the
same distribution, so each is bounded by the same dispersion. Naming this family explicitly is
the point: it is the locally-reasonable next step, and taking it would produce a fifth
refusal on this item.

---

## 3. The bar every candidate must clear

- **C1 target:** `mean_rv / true_error_ref <= 0.9048` on `>= 2/3` seeds, at BOTH dose levels.
- **Base to displace from:** run the re-test in the 541d **survivable regime** (`proximity_harm_scale`
  0.01 + `contaminated_harm` 0.01), where section 7b measured `rv / realised-PE-variance = 1.0`
  in both arms. That makes the dose arithmetic exact: an applied multiplicative displacement
  `g` yields `overconfidence_score = -log(g)` directly. (794a ran in the non-survivable regime,
  where seed-level episode length 132-3529 ticks moved the OFF ratio between 1.000 and 1.667 --
  that spread, not the lever, is why its per-seed scores scattered.)
- **Dose ladder, pre-registered:** `g_LO = 0.80` (predicted score **+0.223**) and
  `g_HI = 0.65` (predicted **+0.431**). Both clear +0.10 with >= 2.2x margin on the converged
  base, and still clear on 794a's worst-measured seed base of 1.060 (+0.165 / +0.373).
- **Headroom guard stays ON** (`waking_confidence_rv_floor_relative_frac` 0.2,
  `waking_confidence_rv_floor_mode` "soft"). The guard caps overconfidence at
  `-log(0.2) = +1.609`, so it does not bind at either dose -- confirmed arithmetic, not an
  assumption.
- **Liveness instrument already exists:** `E3TrajectorySelector.wci_symmetric_rv_ref` is the
  counterfactual un-inflated rv. `1 - rv / wci_symmetric_rv_ref` reads the applied displacement
  directly, so a readiness precondition `drift_displacement_matches_dose` can assert the
  mechanism moved rv by the configured amount **independently of `e`'s dispersion** -- which is
  the exact property 2a says must hold. The field, its property accessor and its manifest
  reporting already exist; the build only has to advance it on the new drift path as well
  (today it advances only inside the `use_waking_confidence_inflation` asymmetric-EMA branch).

---

## 4. Candidates

All three are `E3Config` additions inside `update_running_variance`, gated on the existing
`use_waking_confidence_inflation` master flag plus their own no-op-default selector, so the
OFF path stays bit-identical. All three are orthogonal to (and composable with) the existing
asymmetry knob; the re-test would set `waking_confidence_inflation_asymmetry = 0.0` so the new
term is attributable alone.

### Candidate A -- deterministic leak (constant multiplicative discount)

**Mechanism.** Add a per-tick fractional leak pulling rv toward zero, balanced against the
EMA's pull toward `e`:

```
rv <- (1 - alpha) * rv + alpha * e_t          # existing
rv <- (1 - leak) * rv                          # NEW, leak in [0, 1)
```

Steady state `rv* = g * E[e]` with `g = (1 - leak) * alpha / (alpha + leak - alpha*leak)`,
i.e. an exactly-controllable multiplicative discount; inverting,
`leak = alpha * (1 - g) / (alpha + g * (1 - alpha))`. With `precision_ema_alpha = 0.05`:
`g = 0.80` needs `leak = 0.01235`; `g = 0.65` needs `leak = 0.02622`. Dose is solved in closed
form, so the predicted `overconfidence_score` can be stated in the queue entry BEFORE the run.

| param | type | default | purpose |
|---|---|---|---|
| `waking_confidence_drift_source` | str | `"asymmetric_ema"` | selector; `"leak"` picks this path |
| `waking_confidence_leak_rate` | float | 0.0 | per-tick fractional leak |

**Cost.** ~10 lines in `update_running_variance`, one config field pair, no new state, no RNG,
no new signal plumbed. Smallest blast radius of the three.

**Falsifier-runnability (Step 3h trace).**

| test | EVENT | DV | INSTRUMENT | verdict |
|---|---|---|---|---|
| 794a-style C1 (does the substrate express absolute overconfidence?) | every waking tick | `overconfidence_score` | existing 794a driver | **RUNNABLE** -- passes by construction at both doses |
| 794a-style C2 (Phase 7 broadcast corrects under drift) | `select_action()` | `d_broadcast_under_drift` | `broadcast_precision_pull`, target = F1 `_persistent_zero_point` (exogenous to rv) | **RUNNABLE** |
| 541d Option-A guard-ON falsifier (does recalibration DE-calibrate?) | REM WRITEBACK | relative displacement of rv | `recalibrate_precision_to`, target = EMA of `current_precision = 1/rv` | **NOT RUNNABLE.** A CONSTANT discount is absorbed: in steady state the target's EMA converges to `1/(g*E[e])`, which is rv itself, so recalibration stays near-idempotent -- section 7c's `[-0.15, +0.062]` finding applies unchanged. |

**This is the candidate's decisive weakness and the reason it is not an automatic pick.** It
would close the C1 half of the question cheaply and leave the Option-A half exactly where four
red-team passes left it.

### Candidate B -- stochastic (Ornstein-Uhlenbeck) log-multiplier

**Mechanism.** Maintain a mean-reverting log-multiplier and apply it to the estimator:

```
u_t  <- (1 - theta) * u_{t-1} + theta * log(g) + sigma * xi_t      # xi ~ N(0,1), seeded
rv   <- exp(u_t) * EMA_alpha(e)
```

Mean displacement `g` (the dose), fluctuation scale `sigma`, mean-reversion `theta`. This is
the form the chip's own H1 names ("an exogenous/stochastic drift term (e.g. OU-process ...)").

| param | type | default | purpose |
|---|---|---|---|
| `waking_confidence_drift_source` | str | `"asymmetric_ema"` | `"ou"` picks this path |
| `waking_confidence_ou_mean_log_gain` | float | 0.0 | `log(g)`; 0.0 = no-op |
| `waking_confidence_ou_sigma` | float | 0.0 | per-tick innovation sd |
| `waking_confidence_ou_theta` | float | 0.02 | mean reversion rate |
| `waking_confidence_ou_seed` | int | 0 | dedicated RNG stream |

**Falsifier-runnability (Step 3h trace).** C1 and C2 as for A (**RUNNABLE**). The 541d
Option-A falsifier becomes **RUNNABLE** as well: `u_t` is time-varying on a timescale set by
`theta`, so `1/rv` is non-stationary and its EMA target LAGS it persistently. The displacement
the falsifier scores is then a genuine, non-vanishing quantity whose magnitude is set by
`sigma` and `theta / alpha` rather than by the dispersion of `e`. **This is the only candidate
that makes both halves of the item firable at the same time.**

**Risks, stated rather than papered over.**
1. **New RNG stream.** Needs a dedicated, explicitly-seeded generator (never the global torch
   stream) or it perturbs every downstream draw and breaks bit-identity of unrelated arms. The
   CLAUDE.md cross-machine note applies: keep it on `numpy.random.Generator` / `torch.rand`
   (bit-identical across the fleet), never `multinomial`.
2. **Contaminates a live consumer.** `_rv_history` -> `_volatility_estimate` (Q-007) and the
   ARC-029 variance-tracking commit bar (`use_variance_tracking_commit_threshold`) both read
   the rv TRAJECTORY. Injected OU volatility is indistinguishable, at those consumers, from
   real environmental volatility. Either the re-test must keep ARC-029's relative bar OFF and
   say so, or it must carry a control arm at `sigma = 0` (which degenerates to Candidate A) to
   attribute the effect.
3. Seed variance in the DV goes up; `MIN_SEEDS_OVERCONF = 2/3` may need more seeds.

### Candidate C -- salience/reward-linked precision inflation

**Mechanism.** The form the `substrate_queue` entry originally spec'd ("recency/salience/
reward-driven precision inflation") and the one with the stated biological grounding
(optimism / positive-outcome bias):

```
s_t  <- bounded recent-success signal in [0, 1]   (reward EMA or salience/novelty readout)
rv   <- (1 - k * s_t) * EMA_alpha(e)               # k in [0, 1)
```

Confidence inflates after success and relaxes after failure -- an endogenous but
**non-PE-derived** source, so it escapes the 2a bound provided `s_t` is not a function of
prediction error.

| param | type | default | purpose |
|---|---|---|---|
| `waking_confidence_drift_source` | str | `"asymmetric_ema"` | `"salience"` picks this path |
| `waking_confidence_salience_gain` | float | 0.0 | `k`; 0.0 = no-op |
| `waking_confidence_salience_source` | str | `"reward_ema"` | which signal feeds `s_t` |
| `waking_confidence_salience_ema_alpha` | float | 0.05 | smoothing on `s_t` |

**Falsifier-runnability (Step 3h trace).** C1, C2 and the 541d Option-A falsifier are all
**RUNNABLE** (`s_t` is time-varying, so no absorption), *conditional on* `s_t` being genuinely
exogenous to PE.

**Risks.**
1. **Confound, and it is the serious one.** Reward and prediction error are correlated in this
   env. If `s_t` is reward-derived, "rv diverged from realised PE" is partly explicable by
   that correlation rather than by the mechanism, and C1 becomes attributionally weak. Needs
   either a yoked-control arm (`s_t` replayed from a matched but decorrelated trajectory) or a
   salience source provably independent of PE. That control arm is a real design cost.
2. **Largest blast radius.** `E3TrajectorySelector.update_running_variance` currently receives
   only `prediction_error`. A reward/salience signal has to be plumbed in from the agent loop --
   a new call-site contract, not a local edit, on a file another session currently owns.
3. Dose is not solvable in closed form (it depends on the realised distribution of `s_t`), so
   the pre-registered dose ladder has to be calibrated by smoke first.

---

## 5. Comparison

| | A: leak | B: OU | C: salience |
|---|---|---|---|
| Escapes the 2a dispersion bound | yes | yes | yes (if `s_t` independent of PE) |
| C1 passes at both doses, by construction | yes | yes | after smoke calibration |
| Makes the 541d Option-A falsifier fire | **no** | **yes** | yes |
| Dose solvable in closed form | yes | mean yes | no |
| New RNG stream | no | yes | no |
| Contaminates ARC-029 / Q-007 rv-trajectory consumers | no | **yes** | mildly |
| New signal plumbed into E3 | no | no | **yes** |
| Biological grounding of the SD-076 spec text | weak | weak | **strong** |
| Build cost | lowest | medium | highest |

---

## 6. u/h/s/n/w for the re-test, whichever candidate is chosen

- **(u)** Whether a waking drift source whose magnitude is set by CONFIG rather than by the
  dispersion of realised prediction error can make rv sit >= 10.5% below realised PE with the
  SD-076 headroom guard ON -- i.e. whether the "waking drift source" family can clear C1 at
  all, as opposed to the asymmetric-EMA FORM failing.
- **(h1)** A config-set exogenous displacement clears C1 at both doses and MECH-204's
  correction has something real to correct -> MECH-204 routes to REPAIRED / re-testable.
  **(h2)** Any displacement large enough to clear C1 violates a different pre-registered bound
  (see the rider in section 7) -> the family is structurally insufficient, not just this form.
  Different DVs on the same run.
- **(s)** If the chosen mechanism ALSO fails C1 at both doses despite a config-set displacement
  whose magnitude is directly verified by `drift_displacement_matches_dose`, the failure is no
  longer attributable to the drift FORM and MECH-204 routes to a structural block per 794's
  escalation logic. (Candidates A and B make this outcome close to arithmetically impossible,
  which is itself informative: it converts C1 from an open question into a readiness check and
  moves the real weight onto C2 / the Option-A falsifier.)
- **(n)** `_running_variance` -> `current_precision = 1/(rv + 1e-6)` (e3_selector.py:842-845)
  -> E3 commitment gate (`variance_commit_threshold`, "commitment fires when running_variance <
  threshold"). A live action-selection consumer, not a decoder-only readout.
- **(w)** V3-EXQ-794a tested the only drift source that exists (asymmetric EMA) and failed at
  both doses; no landed manifest measures any non-dispersion-bounded drift source, so
  GOV-REUSE-1 does not apply.

---

## 7. A rider the chosen candidate needs either way: H2 is currently UNFIRABLE

The chip's H2 ("any drift source strong enough to pass C1 ... destabilises the commit gate")
cannot fire as written. `commitment_threshold` is an ABSOLUTE 0.40 and the measured operating
point is rv ~= 0.0037 -- already ~100x below the bar, so the agent is permanently committed
before any drift is added and lowering rv further changes the gate not at all. `config.py`
records this directly: *"the consequence is not 'trained agents commit' but 'trained agents can
never STOP committing'"* (GFLAG-0346).

Two ways to make H2 real, and this is a choice the user should make alongside the mechanism:

- **(i) Arm ARC-029's relative bar** in the re-test (`use_variance_tracking_commit_threshold`
  with `commit_threshold_quantile` / `_window`), which makes the bar relative to the run's own
  rv distribution and therefore responsive to drift. **Recommended** -- it is the remedy
  `config.py` itself names, and it is already landed and default-off.
- **(ii) Re-express H2 on a different secondary bound** (e.g. realism / rv vs realised-PE
  over-shoot), and say explicitly that the commit gate is not the bound being tested.

Taking neither would re-create the exact defect that refused this item four times: a
pre-registered alternative that cannot fire.

---

## 8. Recommendation (a recommendation, not a decision)

**Candidate B (OU log-multiplier), with the section 7 rider (i), and a `sigma = 0` control
arm.**

Reasoning: B is the only candidate that makes BOTH open halves of this item firable in one
run -- C1 (does the substrate express absolute overconfidence) and the 541d Option-A falsifier
(can MECH-204's recalibration correct it). A is cheaper and would pass C1, but section 4's
trace shows its constant discount is absorbed by the guard-ON target, so it buys a C1 pass and
leaves the item exactly as stuck as it is now; that is the failure this item has repeated four
times. C is the most faithful to the SD-076 spec's biological grounding and is the right
eventual form, but its reward/PE confound needs a yoked control and its call-site change lands
on a file another session currently owns -- more risk than the question needs right now. The
`sigma = 0` arm of B IS candidate A, so choosing B subsumes A as its own control rather than
discarding it.

**What this does NOT decide, and what the build session must still do post-consent:** exact
`theta` / `sigma` calibration (by smoke against the dose ladder in section 3), the
`substrate_queue.json` entry, the SD doc, and the `/queue-experiment` pass that re-registers
the 541d criteria. None of those change what is measured; the choice in this document does.

---

## 9. Provenance

- Chip: `chip-20260920-mech204-new-waking-drift-source` (ratified by GFLAG-0391, the user's
  2026-09-20 AskUserQuestion via `orchestrate-20260920-1121`; date-hold to 2026-09-25 released
  early by `orchestrate-20260924-1707` under standing delegation, reason recorded in that
  orchestrator's QUESTIONS.md).
- All figures in sections 2-3 are read from the landed 794a manifest's `aggregates`,
  `per_seed_cells` and `thresholds`, and from live `ree-v3` source at
  `ree_core/predictors/e3_selector.py` / `ree_core/utils/config.py`. Nothing here is estimated.
- Red-team status: **NOT red-teamed.** The build's red-team pass belongs to the post-consent
  `/implement-substrate` session, which has a mechanism to review. This document deliberately
  does not pre-empt it.
