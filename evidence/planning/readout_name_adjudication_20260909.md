# READOUT_UNDER_NEW_NAME -- per-name adjudication

**Generated:** 2026-09-09T07:42:11Z
**Origin:** chip `chip-20260909-readout-unrecognised-name-adjudication`, following the corpus
survey [`flat_scalar_readout_recording_gap_20260909.md`](flat_scalar_readout_recording_gap_20260909.md)
(REE_assembly `ee12f52cee`) and section 3b of
[`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md).
**Scope:** adjudication only. **No converter change was made.**

## Verdict

**NO NAME PASSES. `sync_v3_results.py`'s harvest chain stays at four spellings**
(`metrics` -> `aggregates` -> `summary_metrics` -> `readout`).

The survey cautioned against reflexively widening to a fifth spelling on the strength of one
name (`summary` is prose in other drivers). That caution holds, and generalises: the objection
is not specific to `summary`, and it is not primarily about prose. **Every candidate name fails
on at least one of four independent grounds, and the two names that survive the mechanical
screens fail on the semantic one.** The 219 `READOUT_UNDER_NEW_NAME` packs are a driver-side
recording gap, already governed by standard §3b, and they stay there.

## Re-measurement (2026-09-09, this session)

The survey's 219 was measured 2026-09-09; re-measured today against 2917 packs:

| | survey (02:24Z) | this session (07:3xZ) |
|---|---|---|
| unscored packs (no finite numeric `metrics.values`) | 1101 | **1079** |
| with a flat sibling and no recognised block | -- | **1075** |
| carrying *some* flat numeric dict under an unrecognised key | 219 (after exclusions) | **672** (before exclusions) |

The bucket has **not** materially shrunk. The 672-vs-219 difference is the exclusion list, not
drift: the survey excluded config/provenance/threshold blocks and elided the tail behind a
"`...`". I did not reconstruct their exclusion set exactly, and deliberately did not try: it turns out
to be **part of the adjudication rather than a precondition for it** (see ground 2), so the
unfiltered 672 is the more useful number here and every name is adjudicated on its merits below. The four names
the survey reported reproduce exactly under my index -- `summary` 35, `headline` 17,
`per_arm_train_forage_recent` 13, `per_dv_frac` 11 -- which is the check that my measurement
and theirs are counting the same thing.

> **Method note, recorded because it silently produced wrong numbers first.** Flat manifests
> live at **three** depths under `evidence/experiments/` (1015 at the top level, 802 at
> `<type>/`, 295 at `<type>/<sub>/`). A first pass globbing only `*/*.json` resolved a third of
> the packs' siblings and reported `NO_FLAT_SIBLING` 762 with a *completely different* name
> histogram -- plausible-looking and wrong. Any future re-measurement must index by `run_id`
> across `rglob`, and should reproduce the four names above as its calibration.

## The four grounds

### Ground 1 -- name-meaning collision (the survey's objection, confirmed and quantified)

The decisive question per the chip: does the key mean ONE thing across the whole corpus?
Profiled over **every** occurrence in **all** flat manifests, not just the bucket:

| name | occurrences | prose/string | mixed str+num | nested | flat all-numeric |
|---|---|---|---|---|---|
| `summary` | 177 | **48** | 4 | 92 | 33 |
| `acceptance_criteria` | 124 | **31** | 0 | 4 | 22 |
| `acceptance` | 171 | 4 | 22 | **89** | 34 |
| `registered_thresholds` | 148 | 4 | 9 | 3 | 132 |
| `config_summary` | 84 | 0 | 37 | 35 | 12 |
| `headline` | 43 | 0 | 0 | **26** | 17 |
| `pass_criteria_summary` | 88 | 0 | 6 | **78** | 4 |

`summary` is confirmed exactly as the survey warned -- 48 of 177 occurrences are a **prose
string**, e.g. `v3_exq_266_..._v3.json`: *"Discriminative pair for Q-020 Resolution A (co-true:
ARC-007 + MECH-073)..."*. Harvesting it by name injects that string into a surface that expects
metrics. But it is **not** the only one: `acceptance_criteria` is prose in 31 of 124, and the
converter's existing chain tests only `isinstance(dict) and non-empty`, so it would also adopt
the 92 *nested* `summary` blocks and the 89 nested `acceptance` blocks -- putting nested dicts
into `values`, which `_is_number` then reads as zero numeric entries anyway. The harvest would
be inert where it wasn't harmful.

### Ground 2 -- a pre-registered bar is not a measurement

The highest-frequency candidates are not readouts at all. `registered_thresholds` (77 packs),
`pre_registered_thresholds` (55), `pre_registered_gates` (25), `reference_band` (22),
`acceptance_thresholds`, `robustness_bar`, `denominators` (30), `observation_dims`,
`seeding_regime`, `phase_budget`, `config_summary` (48), `params`, `bridge_config` -- these are
**bars, denominators and configuration**, and several are mechanically spotless (`reference_band`:
22 occurrences, 22 flat all-numeric, zero prose, zero collisions).

Harvesting them would write *the threshold* into `values` as though it were *the measurement*.
The index's deltas and key-metrics columns would then be computed between successive runs' bars
-- a surface that looks scored and reports the wrong quantity. This is why "mechanically clean"
is not sufficient, and why the exclusion list is a judgement rather than a preprocessing step.

### Ground 3 -- harvesting a thin block ARMS the supersession fingerprint, and it misfires

This is the ground that was not anticipated, and it inverts the survey's cost model.

The survey frames the empty `values` as disabling three things. Two of those turn out not to be
live benefits, and the third is a hazard:

- **`fail_if` stop thresholds.** `evidence/experiments/stop_criteria.v1.yaml` defines exactly
  one global rule (`fatal_error_count > 0`) plus six `experiments:` entries, all V1/V2-era
  `claim_probe_*` / audit types. **No `v3_exq_*` experiment_type has any rule beyond the global
  one**, and `fatal_error_count` appears as an inner key of **zero** candidate blocks. So for
  the packs in this bucket, harvesting arms no check that exists.
- **Deltas / key-metrics columns.** Real but cosmetic.
- **The duplicate-emission supersession fingerprint** (`build_experiment_indexes.py` l.2252) is
  `sha1(sorted(run.metrics.items()))` scoped by `queue_id`, and all but the newest of a colliding
  group is set `evidence_direction = "superseded"` -- which the indexer treats as **inactive**,
  so it stops counting toward claim confidence and conflict ratios.

Harvesting a **thin or coarse** block activates that fingerprint on runs it was previously
skipped for. Simulated against the corpus, three candidate names collide, and **all three
collisions are false** -- genuinely distinct runs whose coarse block happens to match:

| name | colliding pair | block (identical) | but these differ |
|---|---|---|---|
| `per_dv_frac` | `v3_exq_861f_..._20260823T210058Z` / `..._20260824T023853Z` | `{sws_power: 0.667, spindle_density: 0.0, replay_rate: 0.667}` | 15 top-level keys incl. `arm_results`, `per_seed`, `discrimination`, `substrate_commit`, `machine` |
| `pass_count_by_criterion` | `v3_exq_249_..._1775525563` / `..._1775528989` | `{c1: 5, c2: 5, both: 5}` -- saturated at n_seeds | `mean_z_goal_norm`, `per_seed_results` |
| `baseline_A` | `v3_exq_254_..._1775580022` / `..._1775724484` | `{mean_z_goal_norm: 0.2509..., mean_behavioral_gap: 0.0}` | `per_condition`, `recovery_fractions` |

The `per_dv_frac` case is the sharpest, because it is one of the survey's four named
candidates: a 3-entry block of fractions over 3 seeds is inherently coarse, so two distinct
runs of one `queue_id` land on the same signature and one is silently marked inactive.
`pass_count_by_criterion` is the cleanest illustration of the mechanism -- the block is
*saturated* (5 of 5 on every criterion), so it carries no discriminating information at all,
while `mean_z_goal_norm` and `per_seed_results` show the runs genuinely differ.

**An auto-superseded pack is strictly worse than an unscored one.** Unscored still scores and
still reads as honestly unmeasured; superseded is dropped from confidence and conflict scoring
altogether. So for a coarse block, widening trades a visible gap for a silent loss.

### Ground 4 -- the blocks are fragments of the verdict, not the verdict (the decisive one)

Standard §3b requires the flat block to be *"the pre-registered scalars the verdict actually
turns on -- each criterion's measured value AND its bar"*. Tested directly: for every candidate
pack that declares its own criteria (`interpretation.criteria_non_degenerate` / `criteria`),
does the union of **all** its harvestable blocks' keys contain those criteria?

| | packs | share |
|---|---|---|
| block covers **ALL** declared criteria | 26 | 7% |
| block covers **SOME** | 9 | 2% |
| block covers **NONE** -- pure fragment | **362** | **91%** |
| *(candidate packs declaring criteria; 672 candidates, 397 declare)* | 397 | |

And the 7% is an artifact: the only name that fully covers its criteria at any volume is
**`criteria` itself** (22 of the 26), which is trivially self-satisfying and is on the survey's
exclusion list. The remainder is `acceptance` (3) and `summary` (1), both prose-poisoned.

The worked case is `per_arm_train_forage_recent` -- the one name that passes every *mechanical*
screen (13 occurrences, 13 flat all-numeric, zero prose, zero nesting, zero collisions, and one
pack per `queue_id`). In `v3_exq_754_mech457_hcurriculum_goal_frontier`, the block is
`{sparse_zw: 1.22, sparse_raw: 1.72}`, while the manifest's verdict turns on
`local_view_clears_floor_at_d3`, `oracle_clears_floor_at_d3`,
`hcurriculum_vs_sparse_vs_anchor_spread` -- **none of which are in it**. The manifest carries 14
other structured blocks (`headline`, `readiness`, `reference_band`, `denominators`, `per_arm`,
`arm_results`, `portfolio`, ...), and all 13 manifests using this name carry richer nested
science elsewhere. The run's own `outcome` is FAIL, and nothing in the harvested block could
reach that.

Harvesting a fragment marks the pack **scored** while the verdict scalars remain unrecorded.
That is worse than `values == {}`: the empty block is a truthful "unmeasured" signal, and it is
exactly the signal the §3b WARN linters, the survey, and this bucket's own definition are built
to detect. A fragment silently satisfies the detector without repairing the gap.

## Per-name verdict table

Ordered by packs in the bucket. `falseSup` = pack pairs that would be auto-superseded, all
verified false where non-zero.

| name | packs | prose | nested | falseSup | verdict | ground |
|---|---|---|---|---|---|---|
| `z_goal_stream` | 136 | 0 | 0 | 2 | **DO NOT HARVEST** | 2 -- provenance block (survey-excluded) |
| `thresholds` | 125 | 0 | 8 | 14 | **DO NOT HARVEST** | 2 -- bar |
| `substrate_identity` | 111 | 0 | 0 | 0 | **DO NOT HARVEST** | 2 -- provenance |
| `env_kwargs` | 83 | 0 | 0 | 4 | **DO NOT HARVEST** | 2 -- config |
| `registered_thresholds` | 77 | 4 | 3 | 20 | **DO NOT HARVEST** | 1, 2, 3 -- bar; prose in 4 |
| `pre_registered_thresholds` | 55 | 3 | 10 | 0 | **DO NOT HARVEST** | 1, 2 |
| `acceptance` | 54 | 4 | 89 | 1 | **DO NOT HARVEST** | 1 -- 89 nested, 4 prose |
| `scaffold_curriculum` | 52 | 1 | 3 | 1 | **DO NOT HARVEST** | 2 -- curriculum config; 40 mixed str+num |
| `config_summary` | 48 | 0 | 35 | 1 | **DO NOT HARVEST** | 2 -- config |
| `enabled_default_off_flags` | 41 | 0 | 0 | 0 | **DO NOT HARVEST** | 2 -- provenance (survey-excluded) |
| `summary` | 35 | **48** | 92 | 2 | **DO NOT HARVEST** | 1 -- the survey's named case, confirmed |
| `denominators` | 30 | 0 | 1 | 0 | **DO NOT HARVEST** | 2 -- denominators are inputs |
| `config` | 27 | 2 | 703 | 1 | **DO NOT HARVEST** | 2 -- config (survey-excluded) |
| `readiness` | 27 | 0 | 11 | 0 | **DO NOT HARVEST** | 2, 4 -- gate state, not measurement |
| `pre_registered_gates` | 25 | 1 | 4 | 1 | **DO NOT HARVEST** | 2 -- bar |
| `criteria` | 22 | 0 | 82 | 3 | **DO NOT HARVEST** | 2 -- survey-excluded; the 7% artifact above |
| `reference_band` | 22 | 0 | 0 | 0 | **DO NOT HARVEST** | 2 -- mechanically clean, but a *band* |
| `acceptance_criteria` | 20 | **31** | 4 | 5 | **DO NOT HARVEST** | 1, 2 |
| `acceptance_checks` | 19 | 1 | 18 | 12 | **DO NOT HARVEST** | 1, 3 |
| `headline` | 17 | 0 | 26 | 0 | **DO NOT HARVEST** | 1, 4 -- no prose, but 26 of 43 nested; fragment |
| `params` | 14 | 0 | 41 | 4 | **DO NOT HARVEST** | 2 -- config |
| `per_arm_train_forage_recent` | 13 | 0 | 0 | 0 | **DO NOT HARVEST** | **4** -- passes every mechanical screen; fragment (worked case above) |
| `per_dv_frac` | 11 | 0 | 0 | 1 | **DO NOT HARVEST** | **3** -- coarse block, false supersession |
| `pass_criteria_summary` | 10 | 0 | 78 | 1 | **DO NOT HARVEST** | 1 |
| *tail: 379 further names, <10 packs each* | -- | -- | -- | -- | **DO NOT HARVEST** | 5 (below) |

## Ground 5 -- there is no convention to widen *to*

Even setting every objection above aside, the arithmetic does not support widening. Harvesting
**every** unrecognised flat-numeric block, with no exclusions at all, repairs **672 of 1075**
candidate packs -- 23% of the 2917-pack corpus -- and requires **403 distinct names**, of which
**293 (73%) appear in exactly one pack**. Only 24 names reach 10 packs, and those 24 are
precisely the prose-poisoned and bar/config blocks in the table above.

The structural signature is in the `packs` / `queue_id` columns: for nearly every candidate,
**packs ≈ experiment_types ≈ queue_ids** (`per_arm_train_forage_recent` 13/13/13,
`reference_band` 22/22/22, `denominators` 30/28/30). These are not a shared spelling that the
converter failed to recognise -- they are each driver inventing its own key once. A fifth
spelling would not be a fifth convention; it would be the first entry in an unbounded list, and
it would change the converter's contract from "four canonical spellings, prefer `readout`" into
"four spellings plus whatever names we have blessed so far" -- which is precisely the surface
§3b was amended to remove.

## What happens to these packs instead

They are a **driver-side gap**, and standard §3b already governs them: the driver emits a flat
scalar `readout` block carrying the pre-registered verdict scalars, with booleans as 0/1 ints
and non-finite/`None` dropped. Enforcement is the two WARN-only linters
(`validate_experiments.flat_scalar_readout_lint` at authoring,
`validate_recording.check_flat_scalar_readout` on a written manifest). Driver backfill is
`chip-20260909-backfill-flat-readout-recent-drivers`, scoped to `ree-v3/experiments/` and
claimed by another session; nothing here touches drivers.

Ground 4 sharpens one thing for that backfill: **the blocks these drivers already emit are not
the ones to promote.** 91% of them do not contain the manifest's own declared criteria, so
renaming an existing block to `readout` would satisfy the linter while leaving the verdict
scalars unrecorded. The backfill has to project the criteria, not relabel a fragment.

## Boundaries of this finding

- **It is scoped to the converter**, not to the standard. §3b is unchanged and unchallenged;
  this document is the record of *why the converter is not the place to fix these 219 packs*.
- **It is a decision record, not a new standing rule**, so it carries no GOV-HELDOUT-1 check --
  no wording in `CLAUDE.md` or any `SKILL.md` changed. If the no-widening conclusion is ever
  promoted into a standing rule, that check is owed at that point.
- **Ground 3 is the one worth re-testing if the corpus changes.** It depends on the current
  `stop_criteria.v1.yaml` having no `v3_exq_*` rules. If `fail_if` rules are ever written for
  V3 experiment types, the benefit side of the ledger changes and the ground-3 arithmetic (not
  grounds 1, 2, 4 or 5) should be redone.
- **Re-litigation guard.** Grounds 1-2 are about *which* names; grounds 3-5 are about the
  *shape* of the fix and do not depend on the name list. A future proposal to widen should
  address ground 4 (91% fragments) and ground 5 (403 names) first -- a proposal that only shows
  a candidate name is prose-free has answered ground 1 alone and does not reach the decision.
