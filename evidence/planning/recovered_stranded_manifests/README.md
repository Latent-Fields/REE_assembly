# Recovered stranded run manifests -- ree-cloud-3, 2026-07-29

**Recovered:** 2026-07-29T22:09:23Z, session `gallant-mclaren-4e5652`
**Source:** `ree-cloud-3` (hcloud `ree-worker-3`, 46.62.170.133),
`~/REE_Working/REE_assembly` -- 13 orphaned `runner-prepull-untracked` stash entries.

**These files are NOT live evidence and are deliberately parked OUTSIDE
`evidence/experiments/`.** The indexer
(`evidence/experiments/scripts/build_experiment_indexes.py`) scans
`evidence/experiments/{*.json, */*.json, **/runs/**/manifest.json}` and would score
anything dropped there, silently changing ARC-110 and MECH-171 confidence. Admitting
these two runs as evidence is a **governance decision that has not been taken** --
see "Open decision" below.

---

## Why they were stranded

`experiment_runner.py:_prepull_stash_blocking_untracked()` (`:608`) stashes untracked
flat manifests before every `git pull` of `REE_assembly` -- roughly once every 62
seconds. `_postpull_restore_prepull_stash()` (`:785`) pops it back.

The pop is called from **only the two success-return paths** of the pull
(`experiment_runner.py:992` and `:1029`). A pull that fails all three retries and
falls through past `:1039` **never pops**, so the entry is left behind permanently.
That function is deliberately never-drop-on-failure ("a stranded stash costs disk; a
dropped one costs an experiment"), so the leftovers accumulate rather than being lost
-- correct, but nothing ever reaps them, and nothing surfaced their existence. The
count reached 13 (11 of them holding the same recurring path).

The docstring at `experiment_runner.py:632` already cites the V3-EXQ-673 entry
recovered here -- it was identified on 2026-07-20 as "the only surviving copy of a
completed run" and was still stranded nine days later.

## Triage result (all 13 entries)

All 13 were archive-tagged on the worker before anything was touched
(`stash-archive/20260729-<short-sha>`, local-only, ref-reachable and therefore
prune-immune). Tags list: `git -C ~/REE_Working/REE_assembly tag -l 'stash-archive/*'`.

Across 31 (stash, path) pairs, containment against `origin/master` graded:

| Grade | Count | Meaning |
|---|---|---|
| SEMANTIC-IDENTICAL | 7 | same parsed JSON as origin; origin stores compact, worker pretty-printed |
| CONTENT-DIFFERS, origin is a strict SUPERSET | 12 | `stash_only=[]` and `changed=[]` in every case -- origin adds `queue_id` / `machine` / `evidence_direction_note`, which the coordinator's phase3 writer injects. Nothing in the stash is absent from origin. |
| ABSENT-ON-ORIGIN | 12 | only **2 distinct files** -- the two recovered here (the 707c manifest recurs in 11 entries as one identical blob, `af436ed57a`) |

The 12th ABSENT pair, `evidence/experiments/runner_commands/ree-cloud-3.json`
(`stash-archive/20260729-4edad02869`, 2026-06-12), is transient runner control data,
not evidence -- superseded on origin, preserved in the tag only.

Nothing was dropped before this containment was established.

## The two recovered files

### `v3_exq_707c_arc110_loop_segregation_c2_release_repair_20260722T041239Z_v3.json`

- blob `af436ed57a73b7febd9936ed21f3eb91fcf28c9e`, 33 keys
- `V3-EXQ-707c`, **FAIL**, `evidence_direction: weakens`, claim **ARC-110**
- ran on `ree-worker-3`, `elapsed_seconds = 147090.9` (**40.9 hours**)
- seeds `[42..49]`, `substrate_hash 2e3d7188d0...`

**A genuinely distinct run**, not a duplicate. `origin/master` carries a *different*
707c run, `..._20260723T151429Z_v3` (machine `ree-cloud-4`, elapsed 76400s = 21.2h,
`substrate_hash 172ba39e5e...`). Same seeds and the same verdict (FAIL / weakens
ARC-110); `metrics` block is identical, `result.arm_results`,
`result.acceptance_criteria` and `result.interpretation` differ.

The coordinator DB holds exactly **one** `results` row for `V3-EXQ-707c` -- the
ree-cloud-4 one (`received_at 2026-07-23T15:14:30Z`). The ree-cloud-3 run's result was
never accepted by the coordinator, which is why the manifest only ever existed as an
untracked file on that worker.

So this run corroborates the landed one rather than contradicting it. It is not
decision-flipping, but it is 41 hours of real compute that the corpus does not have.

### `v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T005615Z_v3.json`

- blob `1152cf546806877cadfad719a700183a8e02e6aa`, 14 keys
- **FAIL**, `evidence_direction: does_not_support`, claim **MECH-171**
- stranded since 2026-06-12; no `queue_id` and no `machine` field
- coordinator DB has **no** `results` row for `V3-EXQ-673` at all

`origin/master` carries six other runs of this experiment
(`20260611T224744Z`, `20260611T230231Z`, `20260612T010234Z`, `20260612T032233Z`,
`20260612T033246Z`, `20260612T044809Z`). This one sits between the 2nd and 3rd and is
absent. It is a **thin** manifest (14 top-level keys vs 33 for a current one) and may
not satisfy current manifest validators.

## DECISION TAKEN 2026-07-30: BOTH ADMITTED. Do not re-litigate.

Session `friendly-antonelli-b0f414`, chip `chip-20260729-admit-recovered-runs`.
Both runs are now live evidence. The copies in this directory are **retained as the
provenance record only** (they hold the as-emitted 673 `evidence_direction`, which the
admitted copy supersedes); they are byte-identical to what was on the worker (verified by
`git hash-object` on both sides). The live copies are:

| run | flat | pack (what the indexer scores) |
|---|---|---|
| 707c | `evidence/experiments/v3_exq_707c_..._20260722T041239Z_v3.json` | `evidence/experiments/v3_exq_707c_arc110_loop_segregation_c2_release_repair/runs/<run_id>/manifest.json` |
| 673 | `evidence/experiments/v3_exq_673_..._20260612T005615Z_v3.json` | `evidence/experiments/v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/<run_id>/manifest.json` |

### Why the "changes claim confidence without a governance pass" objection does not hold

It was measured, not assumed. **Both runs land in `scoring_excluded` buckets, so neither
moves any scored claim confidence** -- `claim_evidence.v1.json` for ARC-110 and MECH-171 is
**field-for-field identical** before and after (`experimental_confidence`,
`literature_confidence`, `overall_confidence`, `direction_counts`, `entries_total`,
`runs_total`, `exp_posterior`, `evidence_quadrant` -- all unchanged):

- **707c** carries `experiment_purpose: diagnostic`, and the indexer sets
  `scoring_excluded = "<purpose>_probe"` from that field alone
  (`build_experiment_indexes.py:2640`). Its landed twin already indexes as
  `scoring_excluded: diagnostic_probe`, so the exclusion was deterministic before the file
  was written. Admitted entry: `adjudication: verified`, `scoring_excluded: diagnostic_probe`.
- **673** was admitted with the existing `failure_autopsy_batch9_2026-06-12` disposition
  PROPAGATED (`does_not_support` -> `non_contributory`) plus the degeneracy limb set. That is
  **not a new decision**: three byte-shape-identical siblings recovered from the *same
  worker* in the *same fault class* on 2026-07-20 were admitted under exactly this
  treatment. Admitting it as-emitted (`does_not_support`) would have been the error -- it
  would have minted MECH-171's first *scored* experimental entry purely out of schema drift.
  Admitted entry: `scoring_excluded: degenerate`, `confidence: 0.0`.

The "thin manifest may not satisfy current validators" worry is also answered empirically:
three manifests of exactly this 14-key shape (no `queue_id`, no `machine`) are already live
and index correctly. Verified end to end: `Indexed 1606 -> 1608 run(s); FAIL 991 -> 993`,
`+2` entries, `0` removed.

### What DID move -- report this to governance

Isolated by re-running the indexer with the two files held aside and diffing (so the
`now`-dependent posterior decay and `decision_deadline_utc` churn are excluded):

- **`ARC-110.conflict_ratio` 1.0 -> 0.8**, which slides it from `AGR-0001` to `AGR-0011` in
  `ARCHITECTURE_GAP_REGISTER.md`. The gap register computes `conflict_ratio` from an
  **all-entries** direction count that does *not* honour `scoring_excluded`, so a second
  `weakens` on ARC-110 makes the evidence *less* perfectly split (2 vs 2 -> 2 vs 3) and the
  metric correctly falls. **The recommendation is UNCHANGED** (`mandatory_decision_checkpoint`)
  -- but note 0.8 now sits *exactly* on the `mandatory_decision_conflict_ratio: 0.80`
  threshold, which is `>=`, so **one further `weakens` entry on ARC-110 would drop it below
  and it would lose the checkpoint**. Also register-side only:
  `source_counts.experimental` 7 -> 8, `recent_targeted_batches` 7 -> 8,
  `experimental_confidence` 0.465 -> 0.471, `overall_confidence` 0.651 -> 0.654,
  `delta_lit_minus_exp` 0.372 -> 0.366. (These register-side `experimental_confidence`
  figures are a *different* statistic from the `claim_evidence.v1.json` one, which stays
  0.0; that divergence is pre-existing.)
- **`ARC-110.suggested_experiment_type`** now resolves to
  `v3_exq_707c_arc110_loop_segregation_c2_release_repair` instead of the stale
  `v3_exq_707_arc110_loop_segregation_validation` -- an improvement, not a regression.
- **MECH-171**: count increments only -- `entries_total` 10 -> 11,
  `source_counts.experimental` 6 -> 7, `recent_targeted_batches` 6 -> 7. No confidence, no
  `conflict_ratio`, no recommendation change; MECH-171 has no gap-register row at all.
- Both runs now appear in `pending_review.md` under **FAIL (action required)** -- correct and
  intended. `review_tracker.json` was deliberately **not** touched (that is `/governance`
  Step 5's call, not this session's).

### The scientific case for 707c, which is the real reason to admit it

Not "41 hours of compute we may as well keep". The recovered run is an **independent
replicate of the repaired instrument on a DIFFERENT substrate revision** (`2e3d7188d0`,
started ~2026-07-20T11:21Z on ree-worker-3) from the landed run (`172ba39e5e`, started
~2026-07-22T18:01Z on ree-cloud-4). All 10 readiness preconditions met on both
(`fresh_selects_sufficient` 987 here vs 922 there), 32/32 seeds on both, all
`criteria_non_degenerate` true on both, and the load-bearing
`C1_A1_loops_strict_above_A0_and_in_layer_null` FAILS on both with `C1_a1_n_seeds = 0` of 4
divergent. So the conclusion of `failure_autopsy_V3-EXQ-707c_2026-07-25` (confirmed,
user-gated) -- *the F-dominance conversion ceiling is INTRINSIC, not a single-arena-collapse
artefact* -- now holds **across two substrate revisions**. That is strictly more than the
corpus had, at zero confidence cost.

Two caveats recorded in the admitted manifest's `evidence_direction_note`:
`n_noise_lifts_over_a0` is 1 here vs 0 in the landed run (marginally the weaker null of the
two; `in_layer_null_live` still true, C1 still 0/4, decisive branch unaffected), and this
run must **not** be counted toward ARC-110's re-derive-brake tally, which stands at 3
(709/711/713).

### Form, and why it matters

**Flat + `runs/<run_id>/manifest.json`, both written.** A flat-only manifest is inert:
exactly one flat-only run exists in the corpus
(`v3_exq_516_mech302_suffering_derivative_integration_20260504T041122Z_v3`) and it produces
**no index entry at all**. Neither recovered run has a `metrics.json` / `summary.md` -- only
the manifest survived the stash -- so the pack manifest is a copy of the flat manifest,
which is the same form the 2026-07-20 recovered 673 siblings take. Neither run needed
`evidence_direction: superseded`: the two 707c runs are replicates, not a
corrected-iteration pair, and nothing supersedes the 673 run.

### Defect found in passing (NOT fixed here, NOT reproduced here)

The three 2026-07-20 recovered 673 siblings (`20260611T224744Z`, `20260612T010234Z`,
`20260612T033246Z`) each carry an `evidence_direction_note` asserting *"These three are NOT
[arm-degenerate] -- their arms differ -- so the degeneracy limb of the batch9 disposition
does NOT apply"*, and omit `degeneracy_reason` / `non_degenerate` on that basis. **That
assertion does not hold under measurement**: all three are arm-identical on
`slot_diversity`, `eval_harm` AND `late_pred_loss` for every seed (42/49/56), with
`late_pred_loss == 0.0` throughout -- the same signature as the committed trio that *does*
set both fields. Harmless for scoring (`degenerate` and `non_contributory` are both
`scoring_excluded`), so nothing was changed on origin. This run was admitted with **both**
limbs set, matching the data rather than copying the omission.

## Related

- `evidence/planning/ree_v3_orphaned_autostash_triage.md` -- the `ree-v3` sibling of
  this exercise, and the source of the archive-tag convention and the containment
  method used here. Note that document covers a **different** stash label
  (`autostash`, taken by `git pull --rebase --autostash`) in a **different** repo;
  this one covers `runner-prepull-untracked` in `REE_assembly`.
- `REE_assembly/scripts/runner_git_health.py` -- the active probe that surfaced this.
  Fleet telemetry cannot see it: `runner_version` reads the `ree-v3` checkout, and
  this fault was in `REE_assembly`.
