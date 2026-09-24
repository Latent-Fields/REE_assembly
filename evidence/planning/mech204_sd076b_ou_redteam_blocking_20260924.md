**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry). The mechanism it describes is NOT on `main`.**

# SD-076b (OU log-multiplier) BUILT, then REFUSED at red-team -- and the refusal is the result

- 2026-09-24T19:0xZ, headless science session
  `metaworker-science-20260924-orchc-mech204-drift-source` (campaign
  `science-20260924-orchc-mech204-drift-source`, chip
  `chip-20260920-mech204-new-waking-drift-source`).
- **Code is parked on `ree-v3` branch `integration/sd076b-ou-drift-source`, NOT on `main`.**
- Predecessor: the design phase of this same session,
  `evidence/planning/mech204_waking_drift_source_candidates_staged_20260924.md`
  (REE_assembly `25c12040ea`). **Sections 4 and 8 of that document are WRONG and are
  corrected here** -- see section 3 below.
- User ratification being executed: 2026-09-24 AskUserQuestion via
  `orchestrate-20260924-1707` -- mechanism **(B) OU log-multiplier with a sigma=0 control
  arm** (`rec-20260924-eb679820`); H2 rider **(i) arm ARC-029's relative commit bar**
  (`rec-20260924-7ece79b9`).

---

## 1. What was built, and it works

`E3Config.waking_confidence_drift_source = "ou"` selects a mean-reverting log-multiplier
applied to the un-inflated symmetric reference:

```
u_t <- (1 - theta) * u_{t-1} + theta * mean_log_gain + sigma * xi_t
rv  <- exp(u_t) * _wci_symmetric_rv_ref
```

Default-OFF; the OFF path and the existing `asymmetric_ema` path are bit-identical (verified
by diff against `fa0a9046` and by two contracts that reconstruct the pre-change arithmetic
independently). Dedicated seeded `numpy.random.Generator`; unset sentinels on `theta` and
`seed` that RAISE; a counted clamp on `u`. 22 new contracts in
`ree-v3/tests/contracts/test_sd076_ou_drift_source.py`; that file plus the existing
`test_sd076_rv_floor_headroom.py` ran **39 passed** on the hub.

**And it delivers C1 decisively**, which was the first of the two things it was chosen for.
Independently simulated at the ratified dose (mean of five seeds):

| source | rv / true_error_ref | `overconfidence_score` | clears C1 (> +0.10) |
|---|---|---|---|
| `asymmetric_ema`, asym 0.8 | 0.949 | **+0.052** | no |
| `ou`, g = 0.65 | 0.671 | **+0.400** | **yes** |

---

## 2. Why it is refused anyway -- two findings, both re-measured by this session

An adversarial red-team pass returned **BLOCKING**. Its two load-bearing findings were
**re-derived and re-measured independently** before being accepted (CLAUDE.md: do not take
an agent's report at face value). Both reproduce.

### F1 (BLOCKING). The OU source does NOT make the MECH-204 Option A falsifier fire. The entire reason for preferring B over A is arithmetically false.

The 541d F1 statistic is the **mean over cycles of a SIGNED** relative displacement,
`(|rv_after - R| - |rv_before - R|) / R`, bar `F1_MAX_RELATIVE_DECAL = 0.25`
(`ree-v3/experiments/v3_exq_541d_mech204_f1_coldstart_guard_validation.py:287,475-479`).
With `rv_before = x_k R` and the target's implied variance `H_k R`, both below `R`, it
reduces exactly to `step * (x_k - H_k)`.

`u` is **stationary and mean-reverting**, so `x_k - H_k` is mean-zero up to the Jensen gap
`E[x] - 1/E[1/x] = e^m (e^{V/2} - e^{-V/2}) ~ e^m V`. At the ratified dose
(`sigma` 0.05, `theta` 0.02, `Var[u]` 0.0631) that predicts `0.25 * 0.63 * 0.0631 = +0.0099`.

Measured (19 cycles x 200 ticks, recal step 0.25, zero-point EMA alpha 0.1, five seeds):

| arm | mean signed displacement | per-seed range | fires (>= 0.25) |
|---|---|---|---|
| g 0.80, sigma 0 (the control arm = candidate A) | -0.00006 | [-0.0001, -0.0001] | 0/5 |
| **g 0.80, sigma 0.05 (RATIFIED)** | **-0.00256** | [-0.0071, +0.0045] | **0/5** |
| **g 0.65, sigma 0.05 (RATIFIED)** | **-0.00044** | [-0.0083, +0.0065] | **0/5** |
| g 0.65, sigma 0.20 (4x over dose) | -0.01811 | [-0.0427, +0.0045] | 0/5 |
| g 0.65, sigma 0.40 (8x over dose) | -0.06648 | [-0.1738, +0.0131] | 0/5 |

The red-team's own wider sweep -- 6 sigmas x 6 thetas x 10 seeds -- fires **0/360**, largest
mean anywhere +0.0037. Its harness was validated against the prior record's published
figures (guard-ON no-drift -0.0015 vs the record's -0.001; the guard-OFF positive control
+2.094/+1.026/+0.354/+0.132/+0.039 vs the record's +2.029/+0.980/+0.319/+0.101/+0.009).

**This lands squarely back inside the `[-0.15, +0.062]` band that the fourth red-team pass
refused on 2026-09-20.** The design doc's claim that a time-varying multiplier "is NOT
absorbed" conflated *the per-cycle displacement is non-vanishing* (true) with *its MEAN
clears 0.25* (false). A zero-mean fluctuation contributes nothing to a mean-signed
statistic, however large each individual excursion is.

### F2 (BLOCKING). The OU write-site makes `_running_variance` MEMORYLESS, which sets 794a's C2 DV to exactly zero.

Under `source == "ou"`, `rv_new = exp(u_t) * _wci_symmetric_rv_ref` -- the branch **never
reads `self._running_variance`**. rv is therefore a pure function of `(u_t, ref_t)`, and
every external write to rv is erased at the next tick. Both MECH-204 write-sites are
external writes:

- `broadcast_precision_pull` runs at the TOP of `select_action` (`agent.py:7007-7011`);
  `update_running_variance` runs later in the same tick.
- `recalibrate_precision_to` runs at the sleep WRITEBACK.

Measured (40k ticks, anchor pulling rv down, gain 0.05, sampled as 794a samples):

| source | mean_rv, broadcast OFF | ON | `d_broadcast_under_drift` |
|---|---|---|---|
| `asymmetric_ema` | 0.00351191 | 0.00246858 | +0.00104333 |
| **`ou`** | 0.00248151 | 0.00248151 | **+0.00000000 exactly** |

So 794a's C2 criterion -- which the design doc marked RUNNABLE for candidate B -- can only
ever return one value. **A criterion with one reachable value is the unfirable-falsifier
defect this item has now hit five times.**

### F3 (BLOCKING, mechanical). A new **str** knob fails a pre-existing contract.

`waking_confidence_drift_source` is a str field on `E3Config` with no `from_dims` signature
entry, so `test_from_dims_flag_reachability.py::test_every_unreachable_str_knob_is_registered`
classifies it UNREACHABLE and fails. Its structurally identical sibling
`waking_confidence_rv_floor_mode` is registered in `REACHABLE_BY_ALTERNATIVE_IDIOM` for
exactly this reason. A one-line registration fixes it; it is recorded here because the build
must not land on `main` with a red contract, and because it is the reason the code is parked
on an `integration/` branch rather than trunk.

**CONFIRMED by the full suite**, which ran on the hub against the pre-fix tree and returned
`4 failed, 6757 passed, 53 skipped, 1 xfailed, 228 subtests in 2104.53s`, with the exact
assertion `assert not ['waking_confidence_drift_source']` at
`test_from_dims_flag_reachability.py:932`. The registration is on the parked branch.

The other three reds are **not attributable to this diff** -- two are shared-corpus-scan
accounting (`test_no_cross_driver_script_is_silently_unscanned`,
`test_scan_pays_no_extra_parse_for_the_escape_check`: 1756 parses for 1688 files, a count
that includes five other sessions' untracked drivers present in the shared checkout the
runner rsynced) and one is `test_runner_merge_peer_status_source.py`, a module this change
never touches. **Stated precisely: not attributable, NOT independently confirmed
pre-existing** -- confirming that would need a second 35-minute run on a clean base, which
this session did not spend.

### Is F2 fixable? Yes. Is F1? No. -- measured, because it decides the options below

A recursive write-site, `rv <- (1 - alpha) * rv + alpha * e * exp(u_t)`, has the same
steady state `g * E[e]` but keeps rv self-recursive, so an external write decays
geometrically instead of being erased:

| variant | C1 score (g 0.65) | `d_broadcast` | F1 mean signed displacement |
|---|---|---|---|
| `asymmetric_ema` | +0.052 | +1.04e-3 | (the 2026-09-20 refusal) |
| `ou` (as built) | +0.400 | **0.0 exactly** | -0.0004 |
| `ou_recursive` | +0.400 | **+1.27e-4** | **+0.00016** |

So the write-site change **rescues C2** -- but only to 1.27e-4 against 794a's own
`BROADCAST_MOVE_FLOOR` of 1e-4, a 1.3x margin, and 8x weaker than the asymmetric EMA's. It
does **not** rescue F1: ±0.003 against a 0.25 bar, unchanged. F1 is structural to *any*
stationary drift, not to this write-site.

---

## 3. Corrections owed to the design document (`..._candidates_staged_20260924.md`)

Stated plainly, because that document is on `origin/master` and a later session will read it:

1. **Section 4, candidate B's Step-3h trace, is WRONG.** It marks the 541d Option-A
   falsifier RUNNABLE for B. It is not, and F1 above measures why. **The correct row for B
   is the same NOT RUNNABLE row the document gives candidate A.**
2. **Section 4's C2 row for B is WRONG** at the write-site the build actually used. C2 is
   degenerate (exactly 0.0) unless the recursive write-site is adopted, and marginal even
   then.
3. **Section 8's recommendation therefore does not survive its own evidence.** B was
   recommended solely because it "is the only candidate that makes BOTH open halves firable
   in one run". It makes one half firable -- the same half A makes firable for ~10 lines,
   no RNG and no consumer contamination.
4. **Section 2a's stated CAUSE is imprecise** (reported by the red-team, confirmed as
   plausible here but not independently re-measured): `error_var =
   prediction_error.pow(2).mean()` averages over the latent dimension, which concentrates
   the statistic by ~1/sqrt(D) *regardless of regime*. The expectile derivation and the
   rejection of family R both stand -- only the attribution to "converged regime" is loose.

The expectile diagnosis itself (section 2a) was independently re-derived by the red-team and
**confirmed correct**: `tau = (1 - asym) / 2`, displacement proportional to dispersion,
2.6% at the calibrated spread vs 39% at 9x the spread. The build is not misdirected on that
axis -- it does exactly what the diagnosis said it would, and C1 is the proof.

---

## 4. Advisories recorded, not yet acted on

- The new contract file's `_selector()` hand-sets the three `__init__` attributes the build
  adds, so deleting those three lines leaves the file green ("a guard that supplies the
  thing it asserts is not a guard"). The failure would be a loud `AttributeError`, not a
  silent one, hence advisory.
- The lever is silently inert if `waking_confidence_drift_source="ou"` is set while the
  `use_waking_confidence_inflation` master flag is off. No error, no contract.
- The seed sentinel catches an *unset* seed but not a *shared explicit constant*, which
  produces byte-identical innovation streams across arms.
- The counted `u` clamp sits ~119 stationary sd away and is unreachable; the **rv floor**,
  which is the actual V3-EXQ-794 saturation path, is applied on top of the OU output and has
  **no counter**. Measured perturbation at the ratified dose is < 1% of E[rv/ref], so the
  science impact is small -- the defect is that the instrument is blind.
- `SPREAD_794A = 0.20` in the contracts is a one-parameter fit (it matches 794a's LO->HI
  separation, 1.7% vs 1.9%) on a **uniform** generator. An expectile depends on distribution
  SHAPE, not just spread: on an exponential or chi-square-1 stream the asymmetric EMA
  displaces 58-60% and would clear C1 easily. The contract's `assert old < C1_MARGIN` is
  therefore a property of the chosen synthetic shape as much as of the old form.
- `numpy.random.Generator` cross-machine bit-identity is asserted, not measured. The
  contracts correctly assert statistics rather than draws; a validation experiment would
  have no such protection against a numpy version bump.
- **Reported, NOT independently confirmed by this session:** the prior record
  (`exq541d_redteam_blocking_refusal_staged_20260919.md` sec 7c) says the F2 positive
  control "does not reproduce and is recorded as not-confirmed". The red-team reconstructs
  that 2.013 is the *cycle-1* value and the 19-cycle mean is ~+0.31-0.33, i.e. the control
  DOES reproduce but with a ~1.2-1.3x margin over its 0.25 bar rather than ~8x. If that is
  right it is a `stale_note` on a load-bearing liveness gate. It is recorded here rather
  than flagged, because this session did not re-measure it.

---

## 5. What this session did NOT do, and why

- **Did not land on `main`.** F3 is a red contract, and F1/F2 mean the mechanism does not
  yet do what it was ratified to do. The code is on `ree-v3` `integration/sd076b-ou-drift-source`
  per CLAUDE.md's one sanctioned multi-session parking exception (executable-code plane,
  would break if half-landed).
- **Did not queue a re-test.** Beyond F1/F2, the ratified H2 rider is separately blocked --
  see section 6.
- **Did not re-design around the refusal.** That is a STOP under this campaign's consent
  rule, and it is why section 7's options go to the user rather than into code.

---

## 6. The H2 rider (i) is separately blocked, exactly as the orchestrator's caution anticipated

Ratified rider (i) was "arm ARC-029's relative commit bar in the re-test". Arming it
requires choosing `commit_threshold_quantile` and `commit_threshold_quantile_window`, and:

- Both are **UNSET sentinels that RAISE** when the lever is armed
  (`config.py:1262-1320`), deliberately: *"WHICH quantile and WHAT window decide what a
  later ARC-029 experiment MEASURES ... That is the experiment's choice to pre-register,
  not this build's to smuggle in as a default."*
- **No landed record fixes them.** The only two landed runs that arm it, V3-EXQ-1070 and
  1070a, both **FAILED** with `substrate_not_ready_requeue`; `window` is 200 in both, but
  `q` is *swept*, not fixed. A failed readiness run is not a ratified operating point.
- **GFLAG-0472 (open)** states the same conclusion independently: *"re-testing MECH-029
  needs a governance/science decision on those parameters (or an alternative
  operationalization), not a silent driver fix."*
- **And arming it would confound this run's own primary DV.** `config.py` records that the
  quantile bar moves `precision_margin_norm` from ~0.999986 to ~0.032963 **by
  construction**, and that quantity is a live selection input via MECH-027
  `use_precision_scaled_commit_temperature`. Arming ARC-029 in the same run as a new drift
  source changes selection behaviour in the drift arms -- confounding the C1/C2 measurement
  the run exists for. This was not knowable when rider (i) was chosen.

---

## 7. The decision now owed (the user's call)

Carried into the consent lane as decision chip `chip-20260924-sd076b-ou-refused-next-step`.

- **(A) Accept C1-only and close MECH-204 Option A on the evidence in hand.** Land the OU
  source (or the cheaper deterministic leak, which buys the same C1 for ~10 lines) as a
  capability enabler, register that the Option A falsifier is unfirable against *any*
  stationary waking drift source, and route Option A to `/governance` on GFLAG-0379 +
  GFLAG-0384. This is option (C) of the 2026-09-20 refusal record, now with the measurement
  that rules the remaining route out.
- **(B) Adopt the recursive write-site and run the C1 + C2 half only.** Fixes F2, gets a
  live but marginal C2 (1.3x over its own readiness floor), leaves Option A closed as in
  (A). Costs one write-site change and a re-queue; buys a real Phase 7 broadcast test.
- **(C) Design a NON-STATIONARY drift source** -- one whose displacement has a consistent
  SIGN across a sleep cycle (e.g. monotone within-wake drift reset at sleep onset) -- which
  is what a mean-signed-displacement falsifier actually requires. This is a **new mechanism
  and a new consent gate**; it is named here because F1 identifies precisely what property
  was missing, not because this session is proposing to build it unasked.
- **(D) Change the FALSIFIER rather than the mechanism** -- score F1 on magnitude or as a
  paired within-cycle statistic instead of a mean signed displacement. Cheap, and the
  refusal record already made exactly this move for a different criterion on 2026-09-20.
  But it changes what is measured and is squarely the user's call.

**Recommendation: (A), with (D) considered only if a live Option A test is judged worth a
criterion change.** F1 is not a tuning shortfall; it is a property of every stationary drift
source, and this item has now spent five red-team passes discovering that its falsifier
cannot fire. (B) is defensible if the Phase 7 broadcast half is wanted on its own terms;
(C) is real work and should be scoped deliberately, not as a rescue for this run.

---

## 8. Provenance

- Code parked: `ree-v3` branch `integration/sd076b-ou-drift-source`.
- Every number in sections 1-2 was measured by this session, in
  `.scratch/`-hosted standalone simulations, after being reported by the red-team; the red
  team's own harness files are named in its report. Where a claim was NOT re-measured here
  it says so explicitly (section 3 item 4, section 4 last bullet).
- 794a figures are read from the landed manifest
  `evidence/experiments/v3_exq_794a_mech204_phase7_sd076_calibration_loop_2x2_20260724T063301Z_v3.json`.
