# Failure autopsy -- V3-EXQ-1036 (EXT-002 lineage stage 2a: revisit-rate DV calibration)

**Run:** `v3_exq_1036_ext002_stage2_revisit_rate_dv_calibration_20260915T003319Z_v3`
**Generated:** 2026-09-17T10:07:04Z | **Status:** confirmed (user-gated) | **Purpose:** `baseline`, claim-free
**Machine-readable:** `failure_autopsy_V3-EXQ-1036_2026-09-17.json`

> **This run was cleared as reviewed before it was ever adjudicated** -- present in `review_tracker.json`
> under both `reviewed_run_ids` and `discussed_experiment_dirs`. Governance had moved on. The review
> marking has deliberately NOT been reverted.

---

## 1. Verdict in one line

The PASS is real and legitimate on its own terms, but it is a **procedural population-adequacy flag, not
evidence** -- and beneath it, **no usable stage-2 threshold is derivable from this run by any route.**

---

## 2. The decisive finding: effective n = 1

Two of the three "non-degenerate" pooled seeds produced **bit-identical revisit streams across both arms**:

| seed | n_revisits A0 | n_revisits A1 | `decline_rate_gap` | action divergence |
|---|---|---|---|---|
| 95973 | 31 | 31 | **exactly 0.0** | 0.00138 |
| 70497 | 55 | 55 | **exactly 0.0** | 0.00323 |
| 570199 | 288 | 281 | -0.0012937332778568018 | 0.25690 |

Every banked gap statistic is therefore a deterministic function of **one seed**. Recomputed from
`per_seed_dv` and reproduced independently by the Step 7c pass:

- mean `-0.0004312444259522673` = exactly one third of 570199's gap -- matches `readout.decline_rate_gap_mean`
- range `0.0012937332778568018` = |570199's gap| -- matches `readout.decline_rate_gap_range`
- population sd (ddof=0) `0.0006098717158794963` -- matches `readout.decline_rate_gap_sd`

**Effective n for the gap statistic is 1, not 3.**

### The degeneracy the guards could not see
The run's `revisit_population_non_degenerate` precondition -- red-team F2's own fix on this driver --
tests that **total revisit count** is non-zero in both arms. All three pooled seeds pass it (31, 55, 288).
It cannot see a seed whose counts are non-zero **and identical across arms**: a structural zero in a
*difference* DV, arriving through a door the count-based test does not cover. So
`calibration_population_adequate` (3.0 vs 1.5) passed legitimately while failing to certify what it was
written to certify -- that there is a population to characterise a range over.

---

## 3. Corrections forced by the Step 7c red-team pass

**Verdict: CONTESTED.** Model note: the skill prefers a *different* model from the drafter; the
cross-model spawn failed on a monthly spend limit (HTTP 429), so per the skill's fallback it was
re-spawned once and inherited the **session model (Opus 5)**. This is a valid pass but weaker than a
cross-model one -- it does not remove the drafter's shared priors. Recorded so this CONTESTED is not later
read as cross-model.

Two attacks the draft survived: criterion reachability (P(<2 survivors in 30 | p=0.125) = **0.09624**, so
"roughly 10%" was exact) and the collapsed-arm/cached-cell hypothesis (**refuted** --
`candidate_score_range_min` differs across arms on both suspect seeds; `run_cell` has no cache path).

Four assertions were **withdrawn or corrected**, each verified independently before acceptance:

1. **WITHDRAWN -- the fallback bar.** The draft called `control_arm_A1_decline_rate_range` (0.0012766870909924556)
   "sound at n=3" and named it as the fallback. **False.** Its endpoints are seed 95973 (max,
   A1 = 0.00045850527281063747) and seed 70497 (min, A1 = -0.0008181818181818182) -- *exactly the two
   zero-gap seeds* -- with 570199 strictly interior, contributing nothing. On both endpoints `A1` is
   numerically identical to `A0`, so it is not a control-arm statistic distinct from treatment at all.
   **No threshold is derivable from this run by any route.**
2. **CORRECTED -- "reaches the action stream".** 983a's confirmed autopsy buckets divergence as "changed
   executed actions in 5/8 seeds (0.12-0.57) and **none** in 3/8 (0.00-0.03)". The zero-gap seeds here are
   0.00138 and 0.00323 -- inside the *"not at all"* bucket. So they are not evidence of a DV sensitivity
   floor; they are evidence the manipulation did not reach executed behaviour. **MECHANISM becomes
   co-equal with MEASURES**, and registry leg `H-residue-written-not-read` is revived.
3. **WITHDRAWN -- "the first divergence-vs-sensitivity data".** 983a already supplied both the bucketing
   and the remedy (learning #4: *"the successor should gate per seed on divergence > 0"*).
4. **CORRECTED -- "nobody had listed it".** `THRESH_C4_MIN_REVISITS = 20` was listed
   (`v3_exq_983a...py:452`), and `min_across_pooled_cells_revisits_early = 18.0` breaches it.

Plus one heavy qualification: **the survival-rate "surprise" is largely definitional.** 1014's ~1/8 is
completion-gate *and* divergence/diversity gates; 1036's 3/5 is completion-gate *only*. Not the same
predicate. The gate-matched comparator is 983a's 2/8 = 0.25, against which 3/5 is unremarkable. It is
recorded as a note, **not** routed at `ext002_lineage_survival_lever`'s registered decision_question.

---

## 4. The dropped handoff -- and the number that settles it

983a's confirmed autopsy recommended the successor gate per seed on divergence. 1036 explicitly declined,
on a calibration-vs-evidence-run distinction: *"No P7-style DV freedom ... certification and no
action-stream-divergence / action-class-diversity GATES."* The precise defect that gate prevents then
occurred, on 2 of 3 pooled seeds.

The magnitude, verified: 983a's ratified `FLOOR_REVISIT_HETEROGENEITY = 0.10`
(`v3_exq_983a...py:614`, a `PreconditionSpec`). `revisit_outcome_heterogeneity` across **all ten**
`arm_results` cells of this run:

`[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05556, 0.05882, 0.09091, 0.08333]` -- **max 0.0909 < 0.10.**

**983a's already-ratified screen would have rejected 100% of this run's population.**

---

## 5. What this run cannot settle

Bit-identical revisit streams under a residue-freeze ablation are consistent with **both**:

- (i) residue is written but never read on the re-approach pathway (`H-residue-written-not-read`), and
- (ii) the revisit-rate DV cannot resolve a manipulation of this magnitude.

Given the divergence values sit in 983a's "did not reach behaviour" bucket, **(i) is now better
supported** -- but V3-EXQ-1036 cannot *discriminate* them. That is the observation bottleneck.

**Nested-arm ordering gate (free instrument check):** `A1_RESIDUE_FROZEN` is an ablation nested in
`A0_INTACT`, so an ordering expectation is available. But with 2 of 3 cells structurally tied, the test
has effective n=1 and **cannot discriminate an instrument defect from a real effect in either direction.**
Recorded so the single negative cell is not read directionally.

**Monostrategy signature, recorded not adjudicated:** `executed_action_classes` = 1.0 in 6 of 10 cells.
The same signature appears independently in V3-EXQ-899 in this batch (`policy_entropy` = -1.0e-09 and
~94% held in all 6 trained cells) under the shared `actor_adequacy_monostrategy` token. Note a discrepancy
flagged but not resolved: `action_class_diversity_by_seed` reports 3/3/5 (probe-side) against
`executed_action_classes` 1-3 (training-side) -- different quantities.

**Recording:** the flat manifest's always-core is complete. Scope correction from the red-team: the **run
pack** -- what the indexer scores -- omits `per_seed_dv`, `arm_results` and `criteria`, carries
`source_repo.commit: ""`, and names `causal_grid_world_v3` while the config is `CausalGridWorldV2`.
Reported as recording hygiene against the pack writer, not this driver.

---

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []` by design; no claim-layer verdict available or owed |
| Biological reference | n/a | calibration pass, no mechanism under test |
| Prerequisites | present | inherits 983a's red-teamed helpers; `substrate_stable_across_run: true` |
| Implementation | **partial** | on the zero-gap seeds the ablation did not reach executed behaviour |
| Environment | partial | 2/5 completion-gate casualties; early-revisit min 18 below 983a's own floor of 20 |
| Measurement | **under-instrumented** | difference DV structurally zero on 2 of 3 pooled seeds |
| Integration | isolated | calibration by design |
| Scale | likely insufficient | effective n = 1 |

**Failure-location (GOV-FAILLOC-1): MIXED** -- MECHANISM and MEASURES co-equal, partial ENVIRONMENT
contribution. `ree: false`. **Not chargeable to REE**, and not a claim-layer verdict of any kind.
(Revised from a MEASURES-only reading after the red-team pass.)

**Re-derive brake: not applicable** -- `claim_ids` is empty, so there is no claim to count ceiling hits
against. Stated explicitly so the absence is not read as an unstamped target.

---

## 7. Routing (user-confirmed at the Step 8 gate, 2026-09-17)

**`queue-experiment`**, with no substrate build owed.

The stage-2 evidence run must apply the two screens **983a already ratified**, rather than inventing a new
precondition:

- (a) `revisit_outcome_heterogeneity >= FLOOR_REVISIT_HETEROGENEITY` (0.10) -- the ratified
  `PreconditionSpec` at `v3_exq_983a...py:614`
- (b) per-seed action-stream divergence > 0 -- per 983a autopsy learning #4

Both are **outcome-independent** and both are already in code. This replaces the draft's own
recommendation to "require `decline_rate_gap != 0`", which the red-team correctly identified as
**selection on the outcome** -- it would inflate any banked bar by construction.

**No threshold is to be taken from V3-EXQ-1036 by any route, including the control-arm statistic.**
Raising the draw target alone is explicitly insufficient: the ratified screens would have rejected all
five draws, so a larger draw under the same screening mostly adds rejected seeds.

**Not chipped from here** -- the routing is a proposal until `/governance` Step 2b ratifies it.

---

## 8. Learning extracted

1. For any A-minus-B **difference** DV, a non-degeneracy precondition denominated on **per-arm** counts
   cannot see a cell whose counts are non-zero but identical across arms.
2. A precondition denominated on the DV's own value is **selection on the outcome** and inflates any
   threshold banked from the survivors. A screen for a calibration run must be outcome-independent.
3. A calibration run banking a range should report the **effective n** of that range alongside the
   pooled-seed count. Here they differed 3x and only the pooled-seed count reached the criteria block.
4. When a range is offered as a fallback bar, **check which cells define its endpoints.** Here the
   "control-arm" fallback was defined entirely by the two cells the primary finding had just condemned --
   invisible to any check reading only the aggregate.
5. **Dropped handoff.** A prior autopsy's recommendation declined by a successor deserves an explicit
   recorded justification engaging the specific failure mode, not a category distinction.
6. **The screen that would have caught this already existed and was already coded.** Before recommending a
   new precondition, check whether the lineage has already ratified one.
