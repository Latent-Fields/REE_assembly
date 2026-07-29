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

## Open decision (not taken by this session)

Should either run be admitted into `evidence/experiments/` as live evidence?

Arguments for: both are real completed runs whose absence is purely an infrastructure
defect, and the corpus is supposed to hold every completed run.
Arguments against: admitting them changes ARC-110 and MECH-171 confidence without a
governance pass; the 673 manifest is thin and pre-dates the current schema; and 707c
already has a landed run reaching the same verdict.

Until that decision is made, these files stay here. They are byte-identical to what
was on the worker (verified by `git hash-object` on both sides).

## Related

- `evidence/planning/ree_v3_orphaned_autostash_triage.md` -- the `ree-v3` sibling of
  this exercise, and the source of the archive-tag convention and the containment
  method used here. Note that document covers a **different** stash label
  (`autostash`, taken by `git pull --rebase --autostash`) in a **different** repo;
  this one covers `runner-prepull-untracked` in `REE_assembly`.
- `REE_assembly/scripts/runner_git_health.py` -- the active probe that surfaced this.
  Fleet telemetry cannot see it: `runner_version` reads the `ree-v3` checkout, and
  this fault was in `REE_assembly`.
