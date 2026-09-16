# Flat scalar readout recording gap -- corpus survey

**Generated:** 2026-09-09T02:24:13Z
**Origin:** chip `chip-20260909-1015-driver-scalar-readout-gap`, found while fixing the
flat->pack converter (REE_assembly `91ed465a64`).
**Scope:** measurement + recommendation only. One driver (V3-EXQ-1015) was fixed; nothing
else was rewritten.

## The mechanism

The runpack converter (`evidence/experiments/scripts/sync_v3_results.py`) builds a pack's
`metrics.json` `values` by harvesting a **flat scalar dict** from the flat manifest under one
of four spellings: `metrics`, `aggregates`, `summary_metrics`, `readout`. A readout recorded
as a dict **keyed by arm or by seed** matches none of them, so the pack scores with
`values == {}`. No converter change can fix that -- flattening nested dicts converter-side
would invent metric names that no `fail_if` rule or plan could ever have referenced. It is a
**driver-side recording gap**.

`build_experiment_indexes.py` reads only *numeric* entries of `metrics.values`
(`_is_number`, line 315, which excludes `bool` as an int subclass). With none, verified
against the source:

| Consequence | Where |
|---|---|
| No `fail_if` stop threshold can fire; `final_status` silently falls back to the manifest's self-declared status -- which is what `claim_evidence.v1.json` records and what drives auto-inferred evidence direction | `_evaluate_runs`, l.2512 / l.2542 |
| The duplicate-emission supersession fingerprint is skipped entirely, so a byte-identical re-emission is never auto-superseded and **both copies score** | l.2252 `if not run.metrics: continue  # cannot fingerprint without numeric metrics` |
| No deltas and no key-metrics columns in the index | `_select_key_metrics`, l.2578 |

## Measurement (2026-09-09, 2917 packs under `evidence/experiments/*/runs/*`)

**1101 of 2917 packs (38%) carry no numeric `metrics.values`.** Classified by what their
flat sibling actually holds, with config/provenance/threshold blocks (`config`, `thresholds`,
`env_kwargs`, `z_goal_stream`, `substrate_identity`, `enabled_default_off_flags`,
`interpretation`, `criteria`, ...) excluded as **not readouts** -- harvesting those would
pollute the score surface rather than repair it:

| Bucket | N | Meaning |
|---|---|---|
| `NESTED_ONLY` | **527** | Rich blocks exist, but every one is keyed by arm/seed. **The V3-EXQ-1015 shape.** Needs a driver-side flat block. |
| `NO_FLAT_SIBLING` | ~~305~~ **123** [^depth-amend] | Flat manifest no longer on disk. |
| `READOUT_UNDER_NEW_NAME` | 219 | A genuine flat scalar readout exists under an unrecognised key. Harvestable by widening the converter -- but see the caution below. |
| `STALE_HARVESTABLE` | 26 | Already harvestable under a recognised spelling; the pack simply predates the converter fix. Fixed by a re-convert, no code change. |
| `NO_READOUT_AT_ALL` | 24 | Nothing quantitative recorded anywhere. |

Within `NESTED_ONLY`, the nested blocks carrying the science are `arm_results` (210),
`summary` (84), `result` (68), `per_seed` (61), `per_seed_results` (57), `per_arm_gate` (44).
Only 38 have `arm_results` as their *sole* rich block.

### This is not a legacy backlog -- it is the current default

Unscored-pack rate by manifest month:

| month | packs | unscored | rate | NESTED_ONLY | NEW_NAME | NO_FLAT |
|---|---|---|---|---|---|---|
| 2026-03 | 360 | 32 | 9% | 8 | 0 | 20 |
| 2026-04 | 314 | 202 | 64% | 51 | 6 | 138 |
| 2026-05 | 241 | 203 | 84% | 99 | 18 | 80 |
| 2026-06 | 251 | 220 | 88% | 161 | 54 | 1 |
| 2026-07 | 226 | 180 | 80% | 119 | 61 | 0 |
| 2026-08 | 210 | 144 | 69% | 75 | 62 | 1 |
| 2026-09 | 46 | 30 | **65%** | 12 | 16 | 0 |

Roughly two thirds of packs produced *this month* score with no numeric metrics. The rate has
never recovered since April. So for most runs on the current substrate, the recorded verdict
is the driver's own self-declaration with no pipeline check able to contradict it, and a
re-emission is never auto-superseded.

## Recommendation

**Yes -- the Experimental Recording Standard should require a flat scalar readout block**, as
an always-core field alongside `recording_schema` / `substrate_hash` / `seeds`. Reasons:

1. The consumer is fixed and narrow: `values` must be a flat dict whose entries are numeric.
   Only the producer can decide *which* scalars the verdict turns on -- that is a design-time
   judgement, not something a converter can infer.
2. It is cheap. The V3-EXQ-1015 fix is ~50 lines, all projection of quantities the driver had
   already computed; no science change, no re-run needed for the fix itself.
3. It is the same whitelist-omission shape already fixed twice for `machine_class`
   (2026-07-16) and `enabled_default_off_flags` (2026-09-01) -- but here the omission
   disables a *check*, not just self-description.

Two encoding rules the standard should state explicitly, both learned from the 1015 fix:

- **Booleans must be emitted as 0/1 ints.** `_is_number` excludes `bool`, so a raw `True` is
  silently inert -- present in the manifest, invisible to the indexer.
- **Non-finite and `None` values must be dropped, not emitted.** A `nan` *is* numeric to the
  indexer and would pollute a delta; an absent key correctly reads as unmeasured.

**Caution on the 219 `READOUT_UNDER_NEW_NAME` packs: do NOT reflexively widen the converter
to a fifth spelling.** The candidate names are long-tailed and mostly experiment-specific
(`summary` 35, `headline` 17, `per_arm_train_forage_recent` 13, `per_dv_frac` 11, then a tail
of 1-5). `summary` in particular is a *prose* key in other drivers, so harvesting it by name
would inject strings into a surface that expects metrics. Widening is a per-name judgement;
the standard is the general fix.

## Not done here (deliberately)

- The already-emitted `v3_exq_1015_..._20260908T202858Z_v3` pack is **not** retro-fixed. The
  driver change affects future emissions only.
- No re-run was queued. V3-EXQ-1015's own recorded routing says more power is "a fourth seed
  or a WARM1600 rung ... not a re-run of this design", so re-running it purely to improve
  recording is not warranted; a future lettered successor will record correctly.
- The other ~526 nested-only drivers were not rewritten. Chipped instead.

## Amendment (2026-09-16) -- `NO_FLAT_SIBLING` was a lookup-depth artifact [^depth-amend]

**Origin:** chip `chip-20260910-merge-runpack-provenance` (merged 2026-09-10 from
`chip-20260909-survey-no-flat-sibling-bucket-artifact`), triggered by the same
three-depth lookup issue `readout_name_adjudication_20260909.md`'s own "Method
note" flagged for the `READOUT_UNDER_NEW_NAME` bucket -- applied here, to
`NO_FLAT_SIBLING`, for the first time.

**Method.** The original 305 was measured against a **top-level-only** flat lookup
(`evidence/experiments/<run_id>.json`). Re-measured against the same corpus using
`build_experiment_indexes._resolve_flat_sibling` -- the PRODUCTION resolver
actually used by the indexer and by `sync_v3_results.py`'s own `_flat_candidates()`,
which checks the top level FIRST and `evidence/experiments/<experiment_type>/<run_id>.json`
as a fallback (see that function's docstring). This is deliberately narrower than a
full `rglob`: a flat living only at a third depth (`<type>/<sub>/`) is invisible to
the real pipeline either way, so it would not change what is actually recoverable.

**Corpus at re-measurement:** 2964 packs (was 2917 on 2026-09-09; +47, ordinary
corpus growth -- the RE-SCOPE note in the triggering chip covers this). Unscored
count is **unchanged at 1101**, which is itself a useful check that "unscored"
and "flat-sibling-present" are being measured consistently across the two
sessions.

| | top-level-only (the survey's original method) | all-depth (`_resolve_flat_sibling`, production-authoritative) |
|---|---|---|
| `NO_FLAT_SIBLING` | 317 (was 305 on 2026-09-09; +12 corpus growth) | **123** |

**194 of the 317 (61%) are a lookup-depth artifact**, not missing flats -- confirming
the chip's hypothesis. The corrected, genuine `NO_FLAT_SIBLING` count is **123**.

**The recovered 194 reclassify into the survey's other buckets.** Best-effort only
-- this session did not recover the survey's original exclusion/nested-block
detection logic byte-for-byte (same caveat `readout_name_adjudication_20260909.md`
made for its own re-measurement: "I did not reconstruct their exclusion set
exactly, and deliberately did not try"), so these are directionally reliable, not
a replacement for a full re-run of the original classifier:

| bucket | recovered count | revised bucket total (old + recovered) |
|---|---|---|
| `NO_READOUT_AT_ALL` | 107 | ~131 (was 24) |
| `NESTED_ONLY` | 85 | ~612 (was 527) |
| `READOUT_UNDER_NEW_NAME` | 2 | ~221 (was 219) |
| `STALE_HARVESTABLE` | 0 | 26 (unchanged) |

The largest shift is into `NO_READOUT_AT_ALL` (107) and `NESTED_ONLY` (85) -- i.e.
most of the previously "no longer on disk" packs actually have a flat sibling that
simply carries nothing quantitative, or carries it nested-only. Neither changes the
recommendation: both buckets already route to "needs a driver-side flat block" /
"nothing to harvest", the same disposition `NO_FLAT_SIBLING` implicitly carried.

**What this does NOT establish.** The corrected 123 is still measured the same way
the original 305 was (unscored packs lacking a flat sibling under the production
resolver) -- it says nothing about WHY those 123 lack one (never written vs.
deleted), which is a distinct question with its own split, now available in
`runpack_always_core_heal_20260909.md` section 8 (chip-20260910-merge-runpack-
provenance item 2, same session). The month histogram for the genuine 123 (64
undated by run_id, 20 in 2026-03, 32 in 2026-04, 7 in 2026-05) is consistent with
the original "almost entirely 2026-03/04" read, now on the corrected population --
the ORIGINAL claim's DIRECTION held, only its MAGNITUDE was wrong.

**Section 3b recommendation is unchanged** by this amendment -- it was never about
`NO_FLAT_SIBLING` in the first place.

[^depth-amend]: See the Amendment section above. `NO_FLAT_SIBLING`'s "not a live
    defect" framing survives (these are still genuinely absent flats, now correctly
    counted), but the count itself was wrong by lookup depth, not by drift.
