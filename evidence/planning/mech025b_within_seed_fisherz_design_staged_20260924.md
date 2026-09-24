# MECH-025b within-seed Fisher-z re-estimator (EXP-1283) -- design findings, BLOCKED on one decision

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

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
