# Diagnostic adjudication — V3-EXQ-784 (SD-074 probe_warmup de-saturation budget sweep)

**Generated:** 2026-07-19T04:51:30Z
**Session:** admiring-shaw-6af5a6 (V3-EXQ-784 SD-074 diagnostic adjudication)
**Scope:** single
**Status:** confirmed (user gate 2026-07-19)
**Target outcome:** PASS (adjudicated — not a FAIL autopsy)

---

## Why this run needed adjudication

V3-EXQ-784 is `experiment_purpose: diagnostic` with `claim_ids: []`. It weights no claim's
confidence and clears no gate by itself. Per the `/queue-experiment` diagnostic adjudication gate, a
diagnostic's self-routed `interpretation.label` is a **hypothesis, not a verdict**, and must be
adjudicated before it drives a governance action. The live action here is moving **SD-074**
(`probe.trained_enough_agent_warmup`, IMPLEMENTED 2026-07-18, ree-v3 `136aa54a97`) from its current
`status: candidate` / "NOT VALIDATED YET" to validated.

The self-routed label was `warmup_desaturates_landscape`, all 3 criteria true.

**Verdict: the label is upheld.** The PASS is not vacuous, both preconditions are genuinely met, and
the scope guard holds. The run additionally carries a *stronger and more robust* signal than the one
its own criteria tested — see "Durable basis" below.

---

## 1. Facts reconstructed

All figures below were **recomputed independently from the raw per-seed `d_means`**, not read from
the reported aggregates. Every author-reported number reproduced exactly (per-budget yields, regime
counts, informative-seed lists, and all three criteria).

| field | value |
|---|---|
| run_id | `v3_exq_784_sd074_probe_warmup_desaturation_budget_sweep_20260718T222045Z_v3` |
| queue_id | V3-EXQ-784 |
| outcome | PASS |
| `substrate_under_test` | SD-074 |
| `routed_by` | `failure_autopsy_MECH-063-777a-779a-cluster_2026-07-18` |
| claim_ids | `[]` (weights nothing) |
| design | 14 seeds x 4 budget checkpoints `[0, 4, 10, 25]` = 56 cells |
| readability | 56/56 readable, 56/56 `probe_stop_reason='floors_met'` |
| machine | ree-worker-1, `linux-x86_64-py3.10`, elapsed 7188.5 s |
| regime bands | `D_SAT_LOW=0.05`, `D_SAT_HIGH=0.95`; headroom = the closed band between |

**Recording provenance: complete.** `recording_schema`, `substrate_hash`
(`f8daed1e...a0d870f`), `machine`, `machine_class`, `elapsed_seconds`, full `config`, explicit
14-entry `seeds` list all present. **No recording gap** — a `substrate_ceiling`-style reading would
have been falsifiable here had one been warranted.

### Dose-response (recomputed)

| budget | ceiling | headroom | floor | informative yield |
|---|---|---|---|---|
| 0 | 7 | 5 | 2 | 0.3571 |
| 4 | 4 | 8 | 2 | 0.5714 |
| 10 | 1 | 10 | 3 | 0.7143 |
| 25 | 3 | 11 | 0 | 0.7857 |

Strictly monotone non-decreasing, four distinct values, spread 0.4286.

---

## 2. Check 1 — vacuous-pass: CLEAN

`interpretation.criteria_non_degenerate = {C1: true, C2: true, C3: true}`, confirmed present in the
manifest. This is **not** the V3-EXQ-621a aggregation-vacuity shape: the load-bearing criterion
`C1_majority_informative_at_some_budget` is the one that passed, and non-degeneracy is corroborated
by the data rather than only asserted by the flag — the per-budget yields take four distinct values
with a 0.4286 spread, so the C1/C2 spread test is operating on real variation.

| criterion | load_bearing | threshold | measured | recomputed | passed |
|---|---|---|---|---|---|
| C1_majority_informative_at_some_budget | **true** | 0.5 | 0.7857 | 0.7857 | true |
| C2_beats_777a_headroom_baseline_by_margin | false | 0.4571 | 0.7857 | 0.7857 | true |
| C3_control_reproduces_saturation | false | 0.5 | 0.6429 | 0.6429 | true |

---

## 3. Check 2 — preconditions: BOTH MET, indexer agrees with author

Both are FLOOR preconditions (`direction: "lower"`, pass = `measured >= threshold`). Recomputing
`met` from the numeric `measured`/`threshold` pair agrees with the author on both.

| precondition | measured | threshold | direction | author `met` | recomputed | agree |
|---|---|---|---|---|---|---|
| `desaturation_read_cells_readable_frac` | 1.0 | 0.8 | lower | true | true | yes |
| `budget0_control_reproduces_777a_saturation` | 0.6429 | 0.5 | lower | true | true | yes |

**The readiness anchor is well-constructed.** `readiness_anchor.guard = assert_anchor_reachable`
proved the control precondition *reachable at setup* by scoring V3-EXQ-777a's own recorded
`per_seed[].D_seed_mean` values (14 cells) through the shipped predicate, yielding 9/14 = 0.6429.
The budget-0 control then reproduced that figure exactly. So the instrument is demonstrably the same
one that produced 777a's saturation reading — the comparison is anchored, not assumed.

---

## 4. Check 3 — scope guard: HOLDS, and was actively enforced by the author

784 is **not** a V3-EXQ-777b and bears on **MECH-063 sub-claim (i) not at all**. Four independent
confirmations:

1. `claim_ids: []` — weights no claim's confidence.
2. **No control-axis quantity exists in the manifest.** The only per-cell measure is
   `d_action_mass_mean/std` (a saturation statistic). There is no `norm_v_score` or any authority
   term.
3. `interpretation.null_meaning` states outright: *"It says NOTHING about MECH-063: no control-axis
   quantity is measured here."*
4. **The strongest evidence — the author declined the flattering comparator.** `baseline_comparator`
   compares against 777a's **headroom** fraction (0.357), explicitly rejecting 777a's *informative*
   fraction (0.286) on the grounds that the latter embedded an authority (`norm_v_score` effect
   floor) check which this run does not compute. The recorded note observes that using 0.286 "would
   flatter this run by 0.071." The author actively refused the statistic that would have entangled
   784 with the control-axis question.

**Consistent with the re-derive brake.** `failure_autopsy_MECH-063-777a-779a-cluster_2026-07-18`
fired the brake on the 777 lineage (`upstream_substrate: SD-PROBE-WARMUP`, `routing:
implement-substrate`, user-confirmed "Fire on 777 lineage, exempt 779"). 784 is the **validation of
that mandated build**, which is precisely what the brake routes *to*. It is not the refused re-test.

---

## 5. Instrumentation provenance — expected, not a defect

The 784 script gained per-cell probe-budget fields and a `probe_budget` aggregate **after** this run
executed (ree-v3 `d46b3094430423b827da4c802e830f172dbc3398`, 2026-07-18T23:24Z). Confirmed absent
from this manifest: the `probe_budget` block, and per-cell `n_probe_env_steps` / `probe_floors_met`.

This is **not** a defect and **no re-run is warranted**. All 56 cells recorded
`probe_stop_reason='floors_met'` and 56/56 were `readable=True`, so the probe budget was
demonstrably clean and the newer code would have written `probe_budget_clean=True`. Only the
near-miss margin (how close a `floors_met` read came to the step cap) is unrecoverable for this run.

---

## 6. Findings beyond the three requested checks

### 6a. The load-bearing criterion is more threshold-dependent than the headline suggests

C1 is a thresholded read of a continuous statistic. Sweeping the readable band:

| band (HI/LO) | b0 | b4 | b10 | b25 | C1 pass | monotone |
|---|---|---|---|---|---|---|
| 0.99 / 0.01 | 0.429 | 0.786 | 0.857 | 1.000 | yes | yes |
| **0.95 / 0.05 (shipped)** | 0.357 | 0.571 | 0.714 | 0.786 | **yes** | yes |
| 0.90 / 0.10 | 0.071 | 0.429 | 0.429 | 0.571 | yes | yes |
| 0.85 / 0.15 | 0.071 | 0.357 | 0.286 | 0.500 | **no** | no |
| 0.80 / 0.20 | 0.071 | 0.357 | 0.214 | 0.357 | no | no |

C1 survives a 0.05 tightening of the band but **fails at a 0.10 tightening**. A moderate robustness
margin — not fragile, not bulletproof.

Per-seed regime labels are correspondingly unstable, because several seeds sit near a cut and
flicker across budgets:

- seed 41: C -> H -> C -> H
- seed 19: C -> C -> H -> C
- seed 13: C -> H -> H -> C
- seed 3: H -> C -> H -> H

At budget 25, **3 of 14 seeds sit within 0.02 of the ceiling cut** (0.965, 0.957, 0.951) and 6 of 14
within 0.05.

### 6b. The paired design carries a far more robust result, which the criteria never used

`sd074_note` records that cells within a seed share **one incrementally-trained agent** (valid
because `measure_action_mass` is non-destructive). Budget 0 vs budget 25 is therefore a **paired**
comparison, and the criteria did not exploit it.

| transition | n | seeds |
|---|---|---|
| saturated@0 -> headroom@25 (**rescued**) | **6** | 11, 23, 29, 41, 61, 83 |
| headroom@0 -> saturated@25 (**lost**) | **0** | — |
| headroom@0 -> headroom@25 (retained) | 5 | 3, 17, 37, 53, 71 |

6 discordant pairs, all in one direction: exact two-sided sign test **p = 0.031**.

**And this asymmetry is threshold-independent**, unlike C1:

| band (HI/LO) | rescued | lost | net |
|---|---|---|---|
| 0.99 / 0.01 | 8 | **0** | +8 |
| 0.95 / 0.05 | 6 | **0** | +6 |
| 0.90 / 0.10 | 7 | **0** | +7 |
| 0.85 / 0.15 | 6 | **0** | +6 |
| 0.80 / 0.20 | 4 | **0** | +4 |

At every band tested, **not one seed was ever lost from the readable band**. That directional
asymmetry — not the yield fraction — is the durable evidence that warmup de-saturates the landscape,
and it survives exactly the threshold variation that breaks C1.

### 6c. Honest caveat — de-saturation is not a one-way flow

Warmup does not monotonically move every seed toward the readable band:

- **seed 5**: 0.000 (F) -> 0.000 (F) -> 0.000 (F) -> **0.965 (C)**. It transits from the floor
  *past* the readable band into the opposite saturation mode.
- **3 seeds remain ceiling-pinned at budget 25** (5, 13, 19), so budget 25 does not clear the
  landscape.

Consumers must not assume a warmed-up agent is guaranteed readable on a given seed; the guarantee is
population-level.

---

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | Both halves of SD-074 are directly demonstrated: a non-degenerate E3 landscape before collection, and the realised per-seed saturation distribution recorded (56 per-cell records with `saturation_regime` + D mean/std) so yield is auditable rather than inferred. |
| Biological reference | n/a | SD-074 is a `design_decision` (harness-level training-regime enrichment), not a mechanism claim. No biological existence proof is at issue and none is required. |
| Prerequisites | present | `depends_on: []`. Composes landed modules (`goal_pipeline_tier1.warmup_train`, `baselines/maturation_curriculum`, `sample_driv...`). |
| Implementation completeness | **complete** | `experiments/_lib/probe_warmup.py`; harness-level only, nothing under `ree_core/` touched, no config default moved. Functional role demonstrated, not merely symbolic. |
| Environment adequacy | adequate | 8x8, 2 hazards, 3 resources — same env as 777a, confirmed by the budget-0 control reproducing 777a exactly. |
| Measurement adequacy | **adequate with a caveat** | The continuous D statistic is sound; the *thresholded regime label* is boundary-noisy (6a). Prefer continuous D downstream. |
| Integration adequacy | coupled | Non-destructive read verified by the checkpoint design working across 4 budgets on one agent. |
| Scale / capacity | **partially adequate** | Budget 25 leaves 3/14 ceiling-pinned; the sweep does not establish the budget at which the landscape fully clears. |

**Recommended `epistemic_category`: not applicable** — this is a validated substrate build, not a
failure. No `substrate_ceiling` reading is warranted.

---

## 8. Brake and recurrence checks

- **Re-derive brake: DOES NOT FIRE.** Zero prior `failure_autopsy_*.json` documents tag SD-074
  (`grep -l "SD-074"` over the planning dir returns nothing). Count including this autopsy: 0
  substrate_ceiling/non_contributory readings.
- **Granularity-debt recurrence trigger: DOES NOT FIRE.** This is the first autopsy on SD-074.
- **GOV-FANOUT-1: not applicable.** No discrimination between rival hypotheses is at issue — this is
  a single-build validation.

## 8b. Step 9b (frozen hypothesis ledger): SKIPPED CLEANLY

No `fanout_recommendation` is emitted and no pre-registered leg is adjudicated. The registry's 9
questions contain zero references to SD-074 / warmup / de-saturation. In particular 784 does **not**
resolve any leg of `control_plane_rank`: it computes no control-axis quantity by design (§4), so it
cannot bear on that question. Nothing to pre-register, nothing to resolve — `initial_frozen_count`
and all surviving counts are untouched by this autopsy.

---

## 9. Learning extracted

1. **SD-074 works as specified.** Warmup raises the readable-seed fraction from 0.357 (untrained) to
   0.786 at 25 episodes, with a paired rescue of 6 seeds and zero losses.
2. **The durable statistic is the paired rescue asymmetry, not the yield fraction.** The yield
   criterion is threshold-sensitive (breaks at a 0.85/0.15 band); the rescued>0 / lost=0 asymmetry
   holds at every band from 0.80 to 0.99. Future SD-074 consumers and any re-validation should assert
   the paired asymmetry.
3. **Checkpoint-within-seed designs should test paired.** The pairing was built into the design (one
   incrementally-trained agent per seed) but the criteria tested only marginal per-budget fractions,
   discarding the statistical power the design had already paid for. A cheap generalisable lesson for
   future budget-sweep scripts.
4. **Thresholded regime labels are a lossy DV when the underlying statistic clusters near the cut.**
   3/14 seeds sat within 0.02 of the ceiling boundary at b25. Record and prefer the continuous D.
5. **The instrument anchor pattern is worth propagating.** Proving the control precondition reachable
   at setup by scoring the *reference run's own recorded values* through the *shipped predicate*
   (`assert_anchor_reachable`) is what makes the budget-0 control interpretable rather than assumed.
6. **Declining a flattering comparator is a scope guard.** `baseline_comparator`'s explicit refusal of
   777a's authority-gated 0.286 in favour of the like-for-like 0.357 is what keeps this run clear of
   MECH-063. Worth citing as the pattern for future substrate-validation runs routed by a braked cluster.

---

## 10. Routing and recommended governance action

**Routing: `governance-promotion`** (no re-queue, no substrate build, no lit pull).

Recommended action: **SD-074 `status: candidate` -> validated**, and rewrite the `notes` field, which
currently reads "NOT VALIDATED YET -- status candidate, validation experiment pending. The only
de-saturation reading so far is a smoke-level sanity indication at n=1 seed and a toy budget ... that
is NOT evidence." That sentence is now superseded by V3-EXQ-784.

**Draft `evidence_quality_note` for governance to write (exact text):**

> VALIDATED 2026-07-19 by V3-EXQ-784 (diagnostic, run_id
> v3_exq_784_sd074_probe_warmup_desaturation_budget_sweep_20260718T222045Z_v3; 14 seeds x 4 budget
> checkpoints [0,4,10,25] = 56 cells, 56/56 readable, all cells probe_stop_reason='floors_met';
> substrate_hash f8daed1e...). Informative-seed yield rises monotonically 0.357 -> 0.571 -> 0.714 ->
> 0.786; the untrained budget-0 control reproduces V3-EXQ-777a's saturation exactly (9/14 = 0.643
> saturated, 5/14 = 0.357 headroom) against an assert_anchor_reachable guard scored on 777a's own
> recorded per-seed D values, so the instrument is anchored rather than assumed. THE LOAD-BEARING
> EVIDENCE IS THE PAIRED WITHIN-SEED ASYMMETRY, NOT THE YIELD FRACTION: cells within a seed share one
> incrementally-trained agent, and budget 0 -> 25 rescues 6 saturated seeds into the readable band
> while losing 0 (exact two-sided sign test p=0.031). That asymmetry is threshold-INDEPENDENT
> (rescued 4-8, lost exactly 0, at every band from 0.80/0.20 to 0.99/0.01), whereas the C1 yield
> criterion is threshold-dependent and fails under a 0.85/0.15 band. CAVEATS: per-seed regime labels
> are boundary-noisy (3/14 seeds within 0.02 of the ceiling cut at budget 25; seeds 41/19/13/3 flicker
> across budgets), so downstream consumers should use the continuous D rather than the thresholded
> regime; budget 25 does NOT clear the landscape (3/14 still ceiling-pinned) and the sweep does not
> establish the budget at which it would; and de-saturation is not a one-way flow (seed 5 transits
> floor -> ceiling, skipping the readable band). SCOPE: 784 tags no claims, computes no control-axis
> quantity, and bears on MECH-063 NOT AT ALL -- its baseline_comparator deliberately uses 777a's
> like-for-like headroom fraction (0.357) rather than 777a's authority-gated informative fraction
> (0.286). Instrumentation provenance: this manifest predates the probe_budget block added in ree-v3
> d46b3094; absence is expected and not a defect, since 56/56 cells reported floors_met. Only the
> near-miss margin is unrecoverable for this run; no re-run warranted.

**PROMOTES/DEMOTES NOTHING ELSE.** MECH-063 is untouched. No claim confidence changes.

### Substrate-queue update owed (corrected 2026-07-19)

**Correction.** An earlier draft of this autopsy recorded that `SD-PROBE-WARMUP` / SD-074 had **no**
`substrate_queue.json` row. **That was false** — an artifact of a bad search (the queue lives under
the top-level key `queue`, and the search iterated `d.get('items', d)`, which silently matched
nothing). SD-074 **does** have a complete, high-quality row, added by session `confident-tesla-badc6b`
with `priority: 1`, the V3-EXQ-777a failure record, and a detailed `implemented_note`. The claim that
the build -> validate loop closed outside the queue is withdrawn; no governance decision on
brake-routed substrates is owed on this evidence.

What is actually owed is an **update** to that existing row, since V3-EXQ-784 is its validation run:

| field | current | should become |
|---|---|---|
| `status` | `implemented_pending_validation` | `implemented_validated` |
| `validation_exq` | `null` | `V3-EXQ-784` |
| `ready` | `false` | `true` |
| `metric_trajectory` | absent | add, with the 777a and 784 readings |

The row's own `failure_record` already carries 777a's 4/14 informative yield against the target
"majority of seeds with `D_action_mass_mean` strictly inside (0.05, 0.95)" — which is exactly the
quantity 784 moved to 11/14. The metric trajectory is therefore directly expressible, and the schema
notes explicitly want it ("the zero-readings and failures are the most informative part of the
trajectory").

Note this write is **normally governance's**, not this skill's — `/failure-autopsy` is analysis-and-
handoff only and does not touch `substrate_queue.json`. It was applied here under explicit user
instruction.

---

## Appendix: repair of 12 staged-deleted evidence files (incidental to this autopsy)

While locating the 784 manifest this session found it absent from the worktree. Root cause was **12
evidence files staged for deletion** in `REE_assembly`'s shared index, covering three complete run
packs — V3-EXQ-779b, V3-EXQ-784, V3-EXQ-785 (flat manifest + `runs/<run_id>/{manifest,metrics,summary}`
each). All were intact in HEAD and on `origin/master`; the run-pack directories had never been
materialised on disk. The stash was empty, so this was **not** the runner-heartbeat autostash hazard.
Reflog shows a `reset: moving to c7c0016136`.

**This is a HEAD/worktree-skew variant that the documented guard does not detect.** CLAUDE.md's
detector is `git status --porcelain | grep "^ D"` and its remedy is `git ls-files --deleted -- :/ |
xargs -0 git checkout --`. Both read the **index**. In this variant the paths were removed from the
index as well, so the status code is `D ` (staged deletion), not ` D` (unstaged). Running both
documented commands returned **zero** while 12 evidence files were missing — a false all-clear. The
`git checkout --` remedy would also have failed here, since it restores from the index and these
paths have no index entry.

Correct remedy for this variant, restoring index *and* worktree from HEAD:

```bash
git -C <repo> checkout HEAD -- <paths>
```

Consequence had it gone unnoticed: the next plain `git commit` in `REE_assembly` would have landed
all 12 deletions, and `build_experiment_indexes.py` would have rebuilt with three runs silently
absent — including this autopsy's own target. That is the silent-evidence-loss mode CLAUDE.md warns
about, reached by a path its check does not cover.

Content was fully recoverable and was restored from HEAD. The entire adjudication above was performed
read-only from HEAD blobs and does not depend on the repair.
