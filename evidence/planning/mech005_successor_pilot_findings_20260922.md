# MECH-005 successor -- PRE-DESIGN PILOT findings, 2026-09-22

**Session:** `mech005-science-20260922-exq-1073`, campaign
`science-20260922-mech005-path-authority`, chip `chip-proposal-exp-0780-paced`.
**Status:** NOT QUEUED -- **STOPPED for a user decision**, not refused. No EXQ id was
consumed (V3-EXQ-1073 was claimed as a placeholder and is released if the decision
routes elsewhere).
**Why this record exists:** the orchestrator downgraded the pre-flight from GREEN to
AMBER with one named condition -- prove the margin DV is off its floor before
committing to the design. That condition is **discharged GREEN**. Running it surfaced
two *other* conditions, both written into MECH-005's own `what_would_answer`, that are
**not met at the trained operating point** -- one of them structurally.

Prior art this builds on:
`evidence/planning/exq1026_mech005_nu_path_authority_refusal_20260911.md` (V3-EXQ-1018
refused; F1 the frozen observation, F3 the unwritten decomp keys, F5 the clamp).

## Method

Two pilots, both on a **fully trained** agent (P0=12, P1=12, SD-070 zP0=8,
40 steps/episode, `alpha_world=0.9`, harm + affective-harm streams on) at seed 42, with
the **environment STEPPED and the selected action applied** -- the F1 fix the refusal
requires -- and `agent.e3.e3_score_decomp_enabled = True` -- the F3 fix.

* Pilot 1: `.scratch/pilot_mech005_margin_dv.py` -> `.json`, 5 arousal levels
  (`clock.beta_magnitude_scale` in {0.1, 0.5, 1.0, 2.0, 10.0}) x 300 ticks.
* Pilot 2: `.scratch/pilot2_mech005_decommit_leg.py` -> `.json`, 2 levels x 600 ticks,
  instrumented for criterion (3) directly.

## P1 -- THE AMBER CONDITION IS DISCHARGED: the margin DV is live

DV = `(second_min - min) / (median - min)` over `e3.last_scores`, read pre-sampling.

| scale | n fresh | mean | SD | CV | p05 | p50 | p95 | max | distinct | ==0 | >0.99 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1  | 266 | 0.1368 | 0.1259 | 0.92 | 0.00097 | 0.0997 | 0.374 | 0.569 | 266 | 0 | 0 |
| 0.5  | 274 | 0.1112 | 0.1097 | 0.99 | 0.00031 | 0.0863 | 0.314 | 0.506 | 274 | 0 | 0 |
| 1.0  | 244 | 0.1330 | 0.1253 | 0.94 | 0.00190 | 0.0940 | 0.370 | 0.577 | 244 | 0 | 0 |
| 2.0  | 272 | 0.1221 | 0.1163 | 0.95 | 0.00050 | 0.0865 | 0.343 | 0.559 | 272 | 0 | 0 |
| 10.0 | 276 | 0.1169 | 0.1181 | 1.01 | 0.00084 | 0.0819 | 0.349 | 0.591 | 276 | 0 | 0 |

**Every one of 1332 recorded values is distinct.** No exact zeros, nothing above 0.99,
and the normaliser was never degenerate (`n_denom_degenerate = 0` in all five arms).
The DV is not floor-pinned and is not quantised -- it is the one thing here that is
unambiguously healthy. This is the MECH-107 check the orchestrator asked for, and it
passes.

**Also favourable: stepping the env DISSOLVES the refusal's F1 sample-count artifact.**
`n_fresh_selects` is flat (244-276) across `e3_steps` 18 -> 5, so the arousal arms draw
comparable numbers of deliberation opportunities rather than ~45 vs ~180. The confound
that made V3-EXQ-1018 unattributable is gone.

No dose-response was visible at this single seed (means 0.137 / 0.111 / 0.133 / 0.122 /
0.117 -- non-monotonic; range 0.0255 against a pooled within-arm SD of 0.119, i.e.
0.21 SD). **That is a pilot observation, not a result** -- one seed, and the claim's gate
is on BETWEEN-seed SD. It is recorded only because it shows the falsifying branch is
live rather than foreclosed.

## P2 -- STRUCTURAL: the endogenous-`e3_steps` precondition cannot be satisfied

MECH-005's `what_would_answer` requires, verbatim: *"the arousal levels must sit off the
`clock.py t=min(1,max(0,||z_beta||*scale))` clamp so `e3_steps` varies with endogenous
`||z_beta||`"*.

Measured: `e3_steps_n_distinct == 1` in **all five arms**, including the three
(0.1 / 0.5 / 1.0) where the clamp is *interior*, not saturated. So the refusal's F5
diagnosis ("operating a saturated clamp") is incomplete -- the real cause is upstream.

**Endogenous `||z_beta||` has almost no dynamic range.** Over all 1500 measured ticks:
min 0.701772, max 0.708161 -- a spread of **0.006389, i.e. 0.91% of its mean**, despite
taking 298-300 *distinct* values per arm. It varies in the fourth decimal.

The clock (`ree_core/heartbeat/clock.py:200-222`) computes, with
`beta_rate_max_steps=20`, `beta_rate_min_steps=5`:

```
t          = clamp(||z_beta|| * scale, 0, 1)
e3_steps   = int(20 - 15*t)
```

so the within-arm integer swing available from endogenous variation is `15 * scale *
0.006389`:

| scale | 0.1 | 0.5 | 1.0 | 1.4 | 1.425 |
|---|---|---|---|---|---|
| achievable within-arm integer steps | 0.010 | 0.048 | 0.096 | 0.134 | 0.137 |

* A **1-integer within-arm swing needs `scale >= 10.4`**.
* The **clamp saturates (`t=1`) at `scale >= 1/0.7018 = 1.425`.**

**The two intervals are disjoint by a factor of 7.3.** There is therefore **no value of
`beta_magnitude_scale` at which `e3_steps` tracks endogenous `||z_beta||`** -- this is
closed-form, not a calibration miss. Setting the scale sets a per-arm *constant*
`e3_steps` (measured: 18 / 14 / 9 / 5 / 5).

Consequence for attribution: the manipulation is **exogenous-equivalent**. The
"ENDOGENOUS z_beta" framing is what distinguishes a successor from V3-EXQ-505 (which
injected a synthetic `z_beta` into a bare `MultiRateClock`), and on this measurement it
is not earned. The across-arm separation is real and large; only the within-arm
endogeneity is unreachable.

## P3 -- MEASURED: confirming criterion (3) is starved on BOTH signals the claim names

Criterion (3), verbatim: *"the fraction of post-commit E2 world prediction-error spikes
(above the running-variance threshold) that produce a de-commit (`beta_gate.release` /
`committed_trajectory` cleared) is higher under high nu than low nu"*.

Pilot 2 instrumented exactly this, counting **both** named de-commit signals (pilot 1
had measured only the `beta_gate` one). Per arm, 600 ticks:

| scale | PE spikes | post-commit spikes | committed tick frac | de-commit: beta_gate | de-commit: committed_trajectory | **crit-3 numerator** | crit-3 fraction |
|---|---|---|---|---|---|---|---|
| 0.1 | 124 | 124 | **1.000** | 1 | **0** | **1** | 0.0081 |
| 1.0 | 207 | 207 | **1.000** | 1 | **0** | **1** | 0.0048 |

Three separate problems, all measured:

1. **The numerator is 1 per arm per 600 ticks.** A *fraction* compared across arms needs
   tens of events per cell to discriminate. At this rate ~30 events needs ~18,000 ticks
   per cell (~4.5 h of fleet compute for 3 arms x 3 seeds), and the rate is not known to
   be linear in ticks.
2. **`e3._committed_trajectory` is NEVER cleared** -- 0 transitions in 1200 ticks. The
   second de-commit signal the claim offers as an alternative does not fire at all.
3. **`committed_tick_frac == 1.000`.** The agent is in a committed state on 100% of
   ticks, so the "post-commit" qualifier selects everything and carries no information.
   Pilot 1 saw the same thing from the other side: `n_committed_true == n_fresh_selects`
   *exactly* in all five arms (266/266, 274/274, 244/244, 272/272, 276/276) -- the E3
   `committed` diagnostic is pinned at True.

Item 3 is the **MECH-107 shape** (`committed_step_fraction` floor-pinned at 1.0 at the
trained operating point) reproduced on a different field. MECH-005's own degeneracy
clause names `n_committed == 0` as the failure mode to watch; the realised failure is
the opposite ceiling, which the clause does not cover.

## Why this is a STOP rather than a design decision

MECH-005 confirms on **(1) AND (3)**. Criterion (1) is measurable now on a healthy DV.
Criterion (3) is not measurable at any budget this session can justify. Queueing the
design as pre-registered would produce a run that **cannot record the confirming
outcome** -- so a non-confirmation would be unattributable, against a claim that
currently has **zero** experimental evidence (`claim_evidence.v1.json`:
`genuine_exp_count = 0`, 5 literature entries, `evidence_quadrant:
plausible_unproven`). That is the same unattributable-under-every-outcome shape that got
V3-EXQ-1018 refused on 2026-09-11, relocated to a different criterion.

Choosing among the options below changes the **criteria and the falsifier**, which the
science lane's consent rule reserves to the user.

## Options put to the user

**A -- Queue a NARROWED experiment: criterion (1) only.** Margin vs >=3 arousal levels,
>=3 seeds, one trained substrate per seed with `capture/restore_agent_surface` between
arms; record criterion (3) as `substrate_not_ready` with the numbers above. ~1.5-2 h
fleet. Buys the first experimental evidence MECH-005 has ever had, on the healthy leg.
Cost: a PASS is *partial* support only (the claim as written is not confirmed), and P2
means the evidence must be recorded as an exogenous-equivalent manipulation.

**B -- Route to `/implement-substrate` instead.** Two measured, named build items:
(i) endogenous `||z_beta||` dynamic range is ~0.9%, so the MECH-093 arousal path cannot
be driven endogenously at all; (ii) the commit channel is ceiling-pinned
(`committed_frac` 1.000, ~1 de-commit / 600 ticks). Reclassifies MECH-005 from
"testable now / complicated (buildable)" to substrate-blocked.

**C -- Queue the full pre-registered design with a ~18,000-tick/cell budget** to try to
rescue criterion (3). ~4.5 h+ fleet on an unverified linearity assumption.

**D -- Amend MECH-005's `what_would_answer`** (governance) to replace criterion (3) with
a de-commit proxy that is live at this operating point, then queue the full design.

**Recommended: A, with B's two findings registered alongside it.** It banks the half
that is genuinely measurable against a zero-evidence claim, and routes the half that is
not, rather than spending 4.5 h on C's assumption or stalling the measurable leg behind
B's build. The risk to state plainly: under A the run can only ever *partially* support
MECH-005, and the evidence entry must say so.

## Reproduction

```
# P1 -- the DV is live, and e3_steps is a per-arm constant:
/opt/local/bin/python3 /Users/dgolden/REE_Working/.scratch/pilot_mech005_margin_dv.py

# P2 -- the closed-form disjointness, from the recorded JSON:
#   1-step swing needs scale >= 1/(15*0.006389) = 10.4
#   clamp saturates at scale >= 1/0.701772       = 1.425

# P3 -- criterion (3) on BOTH named signals:
/opt/local/bin/python3 /Users/dgolden/REE_Working/.scratch/pilot2_mech005_decommit_leg.py
```

## Substrate gate (Step 2.5c) -- measured CLEAR, recorded for reuse

The open-`corrupting` `substrate_queue.json` set has grown from 4 (at the 2026-09-11
measurement) to 11. Re-measured on the actual constructed agent plus a 120-tick stepped
run (`.scratch/probe_mech005_substrate_gate.py`):

* `ContextMemory.write` **0 calls** / `read` **240** -- `e1.sd016_writepath_mode` is
  `'off'`. Same verdict as 2026-09-11.
* `modulatory-bias-selection-authority` (the newly-open entry that sits on
  `E3.select`, and so directly on this DV's path): `score_bias` was **None on 14/14**
  selects and `score_bias_channels` None on 14/14. The composition site is never fed at
  this configuration.
* No `TonicVigor` / `BlockedAgency` / `SelectionEntropyFloor` / `DACCtoE3Adapter`
  instance is held anywhere on the agent; `lateral_pfc_train_rule_bias_head = False`,
  `contextmemory_write_addressing_loss_weight = 0.0`.

So the substrate gate is clear on a function-granular, measured basis. It is **not** what
blocks this item.
