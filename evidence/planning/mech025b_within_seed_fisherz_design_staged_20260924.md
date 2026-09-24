# MECH-025b within-seed Fisher-z re-estimator (EXP-1283) -- REFUSED at red-team; substrate gap, not an estimator gap

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

> **OUTCOME (2026-09-24, second pass).** The user answered the section-5 decision (option A,
> `C1_BAR = 0.10`) and the driver was built, validated and smoke-tested. It was then **REFUSED at
> /queue-experiment Step 4.5 (adversarial red-team, fable, BLOCKING)** on a finding that is about
> the SUBSTRATE and not the estimator: **MECH-025b's dependent variable has no precision input at
> all.** Sections 9-11 below carry the verification. `EXP-1283` is now
> `status: blocked_substrate`, `blocked_by: precision-weighted-residue-accumulation`,
> `route: implement_substrate` (REE_assembly `2ecc8c7b76`). Nothing was queued. Sections 1-8 are
> left exactly as first written -- they are the record of the decision that was asked and answered,
> and section 3's power analysis stays correct on its own terms.

Produced by headless science worker `science-20260924-orchb-mech025b-within-seed-fisherz`
(chip `chip-proposal-exp-1283`, orchestrator `orchestrate-20260924-b`, pre-flight AMBER).
No experiment script was written and nothing was appended to `experiment_queue.json` --
the session STOPPED at WWA P4 under the dispatch consent rule (see section 5).

## 1. Pre-conditions re-measured (all cleared)

| Check | Result |
|---|---|
| Open governance flag naming MECH-025b / EXP-1283 / this chip | **None.** 4 hits in `governance_flags.v1.json` (GFLAG-0151, -0152, -0314, -0328), all `status: resolved`. Denominator 463 items; canary GFLAG-0447 present. |
| Coordination-plane pause | clear (coordinator-queried, not the git fallback); umbrella `origin/master` fetched first |
| `chip-proposal-exp-1283` | `status: open`, `claimed_by: None` at claim time |
| `task_claim.py check` | whole-file contention on `experiment_queue.json` + `experiment_proposals.v1.json` from parallel orch0924-* EXQ authors; claimed narrowly (script path + `EXP-1283`) per the established sub-path pattern those workers use |

**Correction to a search of my own:** the first flag query read a non-existent `flags` key and
returned a clean `0 hits` with no error -- a false negative of exactly the shape CLAUDE.md's
negative-instrument rule describes. The table above is the re-run against the real `items` key,
with denominator and canary printed.

## 2. Substrate spot-check (pre-flight section 3 verified against live `ree-v3` `bbbef60c`)

- `precision_margin_norm = clamp(1 - commit_variance/effective_threshold, 0, 1)`,
  `e3_selector.py:4059-4064`. Set on every **world-variance-mode** tick only; the harm-variance
  branch (`:4030`) leaves it at the pre-seeded `-1.0`. 671b calls
  `agent.e3.select(candidates, temperature=1.0)` with no harm bridge, so the world-variance
  branch is the one that runs. **Confirmed live, as the pre-flight states.**
- For a COMMITTED tick `commit_variance < effective_threshold`, so the value is in `(0, 1]`
  and never hits the clamp. The clamp only bites on uncommitted ticks, which the analysis
  sample excludes anyway.
- `ResidueField` accumulation is `magnitude = |harm_magnitude| * accumulation_rate`, optionally
  scaled by `world_delta` (`residue/field.py:697-704`). **There is no precision term anywhere in
  the residue path.** The correlation under test is therefore genuinely emergent (precision ->
  action choice -> harm magnitude / world_delta), not a structural identity. Pre-flight
  section 4 confirmed.

## 3. NEW finding the pre-flight did not have: re-estimating 671b's own data

Applying WWA P3's estimator (per-seed Pearson r, seeds with <20 events excluded, Fisher-z
averaged with n-3 weights) to 671b's published per-seed table:

| Seed | n | per-seed r | in primary estimator? |
|---|---|---|---|
| 0 | 29 | +0.0505 | yes |
| 1 | 72 | +0.1017 | yes |
| 2 | 77 | +0.0651 | yes |
| 3 | 1 | 0.0000 (fill value) | **no** (P3 exclusion) |

- Fisher-z average **z = 0.0780**, back-transformed **r = +0.0778**
- SE = 1/sqrt(sum(n-3)) = 1/sqrt(169) = 0.0769
- **95% CI on r = [-0.073, +0.225] -- includes 0**

Two consequences:

1. The within-seed estimator **flips the headline sign** of the 2026-08-03 result (pooled
   -0.0446 -> within-seed +0.0778), which is what GFLAG-0151 and WWA P3 predicted. But it is
   **positive-and-inconclusive, not positive-and-confirming.**
2. **`>= 5 seeds` is necessary but NOT sufficient for the falsifier to be decidable.** For the
   CONFIRMING clause's "95% CI excluding 0" to be reachable at an effect of this size you need
   `sum(n-3) ~= 632`; 671b had 169. That is ~10 seeds at n~72, or ~18 seeds at n~40. At the
   WWA's literal 5 seeds x ~72 events (`sum(n-3) = 345`) the CI still spans 0, so the run would
   return inconclusive rather than either confirming or falsifying.

## 4. Second new finding: the mandated regressor is ceiling-compressed

`commitment_threshold = 0.40` and `variance_commit_threshold()` is the identity
(`e3_selector.py:285-294`), so with `current_precision = 1/(running_variance + 1e-6)`:

`precision_margin_norm = 1 - 2.5 / current_precision`

Against 671b's realised precision levels:

| `current_precision` | `precision_margin_norm` |
|---|---|
| 2.5 (bare commit) | 0.000000 |
| 426 (ARC-016 perturbed-env value) | 0.994131 |
| 718 (ARC-016 stable-env value) | 0.996518 |
| 160611 (671b seed-0 spread) | 0.999984 |

The committed population is compressed into roughly the top 0.6% of the regressor's range.
Pearson r is scale-invariant so this is not fatal, and float64 resolves it comfortably -- but
the transform is strongly nonlinear over a 4-5 order-of-magnitude `current_precision` range, so
**r on `precision_margin_norm` and r on per-seed z-scored `current_precision` are not
interchangeable**, even though WWA P3 offers them as alternatives in the same sentence.

Disposition taken (not a question, recorded as a decision): `precision_margin_norm` is the
**primary** regressor -- it is the pre-flight's NAMED CHANGE and is mandatory, it reflects the
scalar the commit gate actually compared including threshold modifiers, and it tames the extreme
right-skew of `1/running_variance` that would otherwise let one outlier tick dominate a
per-seed Pearson r. Per-seed z-scored `current_precision` is carried as a **pre-registered
secondary diagnostic**, reported per seed alongside the primary, never gating. A new P0 gate on
the within-seed spread of `precision_margin_norm` is added, because ceiling compression is a
degeneracy mode no prior run in this lineage could have detected (671a/671b gated on
`current_precision` spread, which is large precisely when the margin is most compressed).

## 5. THE BLOCKING DECISION -- WWA P4, the C1 pass bar

WWA P4 says the `C1 > 0.15` bar "has been carried unchanged from 671 through 671a to 671b and
was never derived from an expected effect size", and requires it be re-derived
"from a measured range-restriction correction or from a stated minimum practically-relevant
effect, and state it before the run."

**Both routes require one free input that no ratified document supplies: what magnitude of
within-seed precision/residue correlation counts as MECH-025b being supported.** That input
decides the verdict -- the within-seed point estimate from existing data is +0.078, so a bar of
0.15 is a near-certain FAIL and a bar of 0.05 is a likely PASS on the same substrate. Under the
dispatch consent rule that is the user's call ("the criteria"), not the worker's, and the
downside is live: the FALSIFYING branch routes MECH-025b to be narrowed to the mechanistic
reading or retired in favour of MECH-025 + MECH-256.

### Options

- **A (recommended) -- `r_bar >= 0.10`, a stated minimum practically-relevant effect.**
  WWA route 2. Conventional (Cohen "small"), a single number fixed in advance, and it sits
  *above* the +0.078 the existing data gives, so it is a real test rather than a rubber stamp.
  Significance stays with the WWA's own "95% CI excluding 0" requirement, which is where it
  belongs.
- **B -- `r_bar >= 0.05`, "small, attenuated by range restriction".** More permissive; a repeat
  of 671b's within-seed effect would PASS. Risks promoting the claim on an effect indistinguishable
  from noise.
- **C -- pre-register the Thorndike Case II formula with a target unrestricted `r_u = 0.10`, and
  compute the bar in-run from the measured S/s.** WWA route 1 taken literally. Costs only extra
  logging of uncommitted-tick margins. **Caveat measured this session:** the unrestricted margin
  distribution is unbounded below (uncommitted ticks give arbitrarily negative
  `1 - commit_variance/effective_threshold`), so S is set by an arbitrary tail rather than a
  stable population SD, and S/s is correspondingly ill-conditioned. A direct pilot measurement
  was attempted and abandoned -- see section 6.
- **D -- `r_bar` = 95th percentile of the within-seed label-permutation null of the Fisher-z
  statistic.** Fully measured, no free input, automatically absorbs range restriction and n.
  But it is a *significance* bar, so it duplicates the CI-excludes-0 requirement and does not
  answer P4's demand for an effect-size-grounded bar. Proposed as a reported control, not as
  the bar.

C2's bar is **not** in question: WWA P4 challenges `C1 > 0.15` only, and the CONFIRMING clause
re-states the ratio bar as 1.1 on `>= 4/5` qualifying seeds. It stays 1.1.

## 6. Pilot measurement attempted and abandoned (cost, recorded so it is not retried blindly)

To supply option C's S/s empirically, a scratch probe wrapped `E3TrajectorySelector.select`
(with `e3_score_decomp_enabled` forced on, to expose `effective_threshold` / `commit_variance`)
and re-ran 671b's own `_run_one_seed`.

- `warmup=10, eval=3, 1 seed`: 125 s. 6 e3 ticks total, **0 committed**.
- `warmup=60, eval=10, 1 seed`: ~1004 s. 12 e3 ticks in 60 training episodes,
  `residue_accum=0.100`, and again **0 committed steps** -- the running variance never falls
  below 0.40 at that training budget.

E3 ticks are sparse (~12 per 12,000 environment steps), and commitment needs 671b's full
`warmup=500`. Extrapolating the measured rate, a full-scale pilot is ~2 h/seed on this box --
i.e. a pilot costs about what the experiment costs. **Not run.** The correction was instead
derived analytically in section 4 from published 671b data plus the live threshold constant.

## 7. Decisions taken by the worker (stated for override in the same round trip)

1. **Regressor:** `precision_margin_norm` primary, per-seed z-scored `current_precision` as a
   non-gating secondary; new P0 gate on within-seed margin spread. (Section 4.)
2. **Discriminative-pair contract:** EXP-1283 carries `dispatch_mode: discriminative_pair` and
   "primary condition vs explicit ablation/control", but the WWA falsifier is a single-condition
   within-seed correlation, and the substrate has **no** discrete precision-mode knob (WWA
   INSTRUMENT NOTE; confirmed -- no `precision_mode` / `high_precision` / `action_precision` in
   `ree_core/`), so a forced high/low-precision arm is impossible. Resolution: the control arm is
   a **within-seed label permutation** of the regressor on the identical seeds -- it satisfies
   `matched_shared_seeds` and `min_shared_seeds: 2` by construction and adds no substrate
   condition, so it cannot change what the substrate measures.
   *Road not taken:* declaring the P1/P2 positive-control gates to be the "control" and leaving
   the pair contract nominally satisfied. Rejected -- those gates are preconditions, not a
   contrast, and EXP-1283's `exclude_broad_profile_sweeps` shows the contract means a real one.
3. **Seeds / scale:** 10 seeds at 671b's per-seed scale (`warmup=500`, `eval=50`, `steps=200`),
   chosen from the section-3 power calculation rather than from the WWA's literal `>= 5`.
   This is ~2.5x 671b's compute. Flagged explicitly because it is a fleet cost, and because
   running at 5 seeds would make the falsifier formally satisfiable but statistically unable to
   return either of its two verdicts.

## 8. What the next session should do

With the section-5 answer in hand, the remaining work is a single `/queue-experiment` pass:
`v3_exq_<id>_mech025b_within_seed_fisherz.py`, forked from
`ree-v3/experiments/v3_exq_671b_mech025b_precision_responsibility.py`, retaining that driver's
four instrument fixes and both positive-control gates (P1 residue accumulation, P2 within-seed
precision variance) unchanged, and replacing **only** the statistics layer
(`pooled_precision.extend(...)` at `:699-715`) with the within-seed Fisher-z estimator. Nothing
in the warmup/eval pipeline needs to change except recording
`last_score_diagnostics["precision_margin_norm"]` alongside `current_precision` at `:445`.


---

# SECOND PASS (2026-09-24, after the user's option-A decision)

## 9. The decision was answered, and the driver was built

User decision (orchestrator decision lane, chip `chip-20260924-mech025b-c1-bar`): **option A** --
`C1_BAR = 0.10` pre-registered as a stated minimum practically-relevant effect
(what_would_answer P4 route 2); the 95%-CI-excludes-0 requirement stays as the separate
significance test; C2 stays 1.1 on >= 4/5 qualifying seeds; the three worker decisions in
section 7 stand as taken.

Built as `V3-EXQ-671c` (slot reserved, `supersedes` V3-EXQ-671b). It passed
`validate_experiments.py --strict` (0 warnings, after fixing the two it initially raised) and a
`--dry-run` smoke (rc=0, manifest + runner sentinel written, all six criteria evaluated,
`margin_availability = 1.0`). Beyond WWA P1-P4 it also fixed two instrument defects found by
source-tracing while authoring:

- **Commit-time capture.** `REEAgent.update_residue()` -- which 671b calls after every
  `env.step()` -- reaches `E3.post_action_update` (`agent.py:11070`) and thence
  `update_running_variance`, so `current_precision` moves on EVERY env tick while `select()`
  fires only on an E3 tick (~1 in 10; `config.py:1281` states the asymmetry, and it measured
  10.5 steps/selection here). 671b therefore read its regressor up to ~10 ticks AFTER the commit
  decision and AFTER the harm's own prediction error had been folded into the EMA -- and since
  harm raises prediction error, raises variance and so LOWERS precision, that contamination has a
  negative sign, which is the direction 671b's pooled estimate reported.
- **Commit-window sampling.** 671b's `held_committed` latch persists across the ~10 steps between
  E3 ticks, so two harm events in one window counted as two independent observations of one
  selection. 671c emits one observation per fresh committed selection and records
  `n_selections` / `n_commit_windows` / `n_latched_ticks` so the denominator is auditable.

A derived joint-satisfiability bound was added: C1's two halves are simultaneously reachable only
above `W = (1.96/atanh(C1_BAR))^2 = 382` total Fisher weight, gated as a `dv_headroom` precondition.

## 10. THE BLOCKING FINDING -- the DV has no precision input (verified from source)

Red-team verdict **BLOCKING**. Every load-bearing claim was re-verified directly against
`ree_core` before being accepted:

| Fact | Source | Verified |
|---|---|---|
| `ResidueField.accumulate` computes `magnitude = abs(harm_magnitude) * accumulation_rate`, optionally `* world_delta`. No precision, variance or commitment term. It is the ONLY write site for `total_residue`. | `ree_core/residue/field.py:697-704` | yes (first pass, section 2) |
| Owned harm is a CONSTANT. `agent_caused_hazard` sets `harm_signal = -self.contaminated_harm`, default **0.4**. The driver's `hazard_harm=0.02` is a DIFFERENT parameter, applying to `env_caused_hazard`, which the `owned` filter excludes. | `ree_core/environment/causal_grid_world.py:2647`, `:274` | yes |
| The only other contributor accumulates a **hardcoded** `harm_magnitude=1.0`, gated on a held committed trajectory -- binary, never graded by precision. | `ree_core/predictors/e3_selector.py:4691-4694` | yes |
| `accumulation_rate` default `0.1` | `ree_core/utils/config.py:3379` | yes |

With `world_delta=None` (the driver passes it), the per-window DV therefore reduces **exactly** to

```
dv = w_residue / w_harm = (0.04*m + 0.10*I) / (0.4*m) = 0.1 + 0.25 * I/m
```

where `I in {0,1}` is whether the commit tick itself landed on an owned-harm step and `m` is the
owned-harm count in the window. **Precision cannot enter this expression.**

Consequences, and why this is BLOCKING rather than a caveat:

- **A PASS would be unattributable.** `dv` varies only through `I` and `m`, i.e. through the
  timing of the commit tick relative to harm and the harm density of the window. Precision
  influences behaviour and therefore influences `m`, so a nonzero within-seed `r` is reachable --
  but it would record a commit-tick timing coincidence, not "precision scales residue weight".
  The verdict grid would nonetheless stamp it `supports` /
  `precision_scales_residue_weight_within_seed`.
- **A null would not be claim pressure.** It would record that the substrate has no
  precision-weighted residue path -- the same class as V3-EXQ-671's original
  `residue pinned at 0` defect, which governance correctly ruled `non_contributory`. The grid
  would stamp it `weakens`, which is what the FALSIFYING clause says should narrow or retire
  MECH-025b.
- This also **re-reads section 3**: 671b's per-seed `r` of +0.05/+0.10/+0.07 and ratios of
  0.92/1.13/1.15 are what a two-valued `{0.04, 0.14}` per-step DV produces. The within-seed
  re-estimate of +0.0778 in section 3 is arithmetically correct and remains the right way to read
  671b's numbers, but it is a re-estimate of a quantity with no mechanism behind it. **The pooled
  vs within-seed confound (GFLAG-0151) is real and is NOT the whole story** -- fixing the
  estimator alone could never have answered this claim.

## 11. Secondary red-team findings (recorded; not independently re-verified in full)

Dispositions, since they matter to whoever picks this up:

1. **Episode length (CONTESTED, independently corroborated).** The reviewer measured episodes
   dying in 1-3 steps under this env config. This session's own cadence probe saw the same thing
   before the red-team ran -- 21 env steps across 10 episodes on an untrained agent -- and the
   shipped smoke shows 38 of 100 configured steps. The docstring's "~1000 selections per seed"
   was `200/10` arithmetic, not a measurement. **Any successor needs an episode-length readiness
   gate**; without one the run cannot distinguish "no effect" from "no episodes".
2. **Verdict-grid over-reach (CONTESTED, accepted).** The `else -> weakens` branch fires on ANY of
   {C1a fail, C1b fail, C2 fail}, but the registered FALSIFYING clause requires a null/negative
   correlation AND a majority ratio failure. Worse, at the effect the design is powered for
   (r = +0.078, W ~ 632) the CI excludes 0 while r < 0.10 -- so the run would label a
   **significantly positive** correlation `weakens`. That is a real design defect independent of
   finding 10 and must be fixed before any re-run.
3. **The W >= 382 gate out-ranks the falsifier's own minimum (CONTESTED, accepted).** The
   registered FALSIFYING precondition is >= 5 seeds x >= 20 events, i.e. W = 85. The gate would
   route a clean null meeting the claim's own stated sufficiency to `non_contributory`. The gate's
   premise ("cannot PASS below W=382") also holds only at r ~ C1_BAR: at r = 0.30, W = 100 passes
   both halves. Needs re-scoping, not deletion.
4. **`precision_margin_norm` is affine in `rv` within a seed (NOTE, correct).**
   `margin = 1 - rv/0.40`, and Pearson is affine-invariant, so within a seed
   `r(margin, dv) = -r(rv, dv)` exactly. The scale-free fix buys comparability ACROSS seeds (real,
   and the point of P3) but changes nothing within-seed. Section 4's ceiling-compression concern
   is the same observation from the other side.
5. **Window autocorrelation (NOTE, plausible, unverified).** `precision_ema_alpha = 0.05` against
   ~10-step windows leaves consecutive windows correlated, so the `(n-3)` Fisher weights, the CI
   and the permutation null all assume more independence than the data have. Would need an
   effective-n correction.
6. **`agent.eval()` dropped (verified).** 671b calls it at its line 392; the 671c eval loop as
   written does not. A genuine regression introduced in this rewrite, and it breaks the
   "comparability with 671b" claim for the legacy per-step diagnostic. Noted in the withheld
   driver's header.

## 12. What is owed, in order

1. **A substrate item: precision-weighted residue accumulation.** Registered as the blocker on
   EXP-1283 (`blocked_by: precision-weighted-residue-accumulation`, `route: implement_substrate`).
   It has **no `substrate_queue.json` entry yet** -- deliberately named anyway so it lands in the
   standing audit's `UNOWNED` bucket, which is the signal to register it. Note this is a
   design question, not a mechanical build: making residue depend on commit precision is exactly
   what MECH-025b asserts, so the mechanism must be motivated independently of the claim it would
   then be used to test, or the test becomes circular. That is a `/governance` + `/implement-substrate`
   conversation, not a queue-experiment one.
2. **An episode-length readiness gate** for this env config (finding 11.1).
3. **Only then** the within-seed estimator, which is preserved and reusable at
   `REE_assembly/evidence/planning/mech025b_671c_withheld_driver_20260924.py` -- with fixes for
   findings 11.2, 11.3 and 11.6 applied first.

## 13. Gate dispositions recorded on the way (all cleared, all measured)

- **Step 2.4 (GOV-REUSE-1):** NOT RECOVERABLE. Three prior runs carry
  `precision_residue_correlation`, but all predate `precision_margin_norm` (landed 2026-09-02) and
  none persisted raw per-sample values, so the within-seed estimate on the correct regressor is not
  derivable post-hoc.
- **Step 2.5b (re-derive brake):** count 1 against a threshold of 2 -- not braked. (551 autopsy
  artifacts scanned, 3 targets found for MECH-025b.)
- **Step 2.5c (substrate-path overlap):** two OPEN `corrupting` entries name files this driver
  imports; both were measured unreachable rather than argued away.
  `contextmemory-write-path-addressing-degeneracy` needs `sd016_writepath_mode`, which defaults
  `"off"` and is never set here -- measured 0 of 16 slots occupied across 3 seeds x 1200 `sense()`
  calls. `SD-PP-B5` names `compute_world_interventional_loss`, which has zero callers anywhere in
  `ree_core`. Several `degrading` entries overlap and were to be noted in the queue entry.
- **Step 2.5a:** `precision_margin_norm` is populated without `e3_score_decomp_enabled` and takes
  7 distinct values in (0,1] across the commit boundary; `margin = 1 - rv/0.40` matched the
  analytic prediction exactly at every probed point.
- **Step 2.6 (ethics preflight):** all flags false, `decision: allow` (SENT-0, V3 pre-ethical
  instrumentation).
