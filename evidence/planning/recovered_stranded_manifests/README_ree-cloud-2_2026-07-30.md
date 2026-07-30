# Stash triage + recovered manifest -- ree-cloud-2, 2026-07-30

**Triaged:** 2026-07-30T01:28Z -- 02:50Z, session `beautiful-elbakyan-245a58`
(chip `chip-20260729-cloud2-stash-triage`)
**Source:** `ree-cloud-2` (hcloud `ree-worker-2`, 116.203.216.181),
`~/REE_Working/REE_assembly` (17 stash entries) + `~/REE_Working/ree-v3` (1 entry).

Sibling exercise to [`README.md`](README.md) (ree-cloud-3, 2026-07-29). Method taken from
there; the **outcome is different in both directions** and both differences matter.

The worker was mid-run (`v3_exq_687a_mech313_committed_authority_dissociation`, PID 8141)
throughout. The runner was never stopped and nothing was pushed from the worker.

---

## Headline: the stashes were clean; the loss was somewhere nobody was looking

**All 18 stashes are fully contained on `origin/master` -- zero ABSENT-ON-ORIGIN across
21 (stash, path) pairs.** On ree-cloud-3, 2 of 31 pairs were the only surviving copies of
completed runs. Here, none were.

**But one genuinely stranded run manifest was found on the same worker, as an untracked
`.bak` file in the working tree -- not in any stash.** It is the manifest a 2026-05-30
failure autopsy declared **unrecoverable**, and its recovery answers the exact question
that autopsy said it could not answer. See "The recovered manifest" below.

The lesson to carry to `ree-cloud-4` / `DLAPTOP-4`: **grading the stash list is not the
same as grading the worker.** A stash-only triage on this box would have reported "all
clean" and closed, leaving the real loss in place. Check `git status --porcelain -u`
against `origin/master` as a first-class step, not as an afterthought.

---

## Containment grading -- all 21 (stash, path) pairs

All 18 stashes were archive-tagged **by SHA, in one pass, before anything was touched**
(`stash-archive/20260730-<short-sha>`, local-only on the worker; `stash@{N}` is racy
because the runner rewrites the list every ~62s). Tags:
`git -C ~/REE_Working/REE_assembly tag -l 'stash-archive/*'` (17) and the same in
`ree-v3` (1).

| Grade | Pairs | Meaning |
|---|---|---|
| SEMANTIC-IDENTICAL | 2 | same parsed JSON as origin |
| ORIGIN-SUPERSET | 8 | `stash_only=[]` and `changed=[]`; origin adds `queue_id` / `epistemic_category` / `evidence_direction_note`, which the phase3 writer and governance inject |
| CONTENT-DIFFERS | 11 | **all benign -- verified field by field, see below** |
| ABSENT-ON-ORIGIN | **0** | -- |

### Why all 11 CONTENT-DIFFERS are benign

This is the grade that could have hidden a loss, so it was checked by value rather than
by shape. In **every** case `stash_only=[]` -- nothing in the stash is missing from
origin -- and the sole changed key is `evidence_direction`, moving from the runner's raw
self-route to a **governance-applied** verdict:

| stash | run | stash `evidence_direction` | origin `evidence_direction` |
|---|---|---|---|
| `d16f6658cc` | 838 q081 cross-stream recording | `unknown` | `non_contributory` |
| `13b3df2110` | 836 mech476 dose-dependent consolidation | `mixed` | `non_contributory` |
| `b3269fff2e` | 822b sd082 head internals | `unknown` | `non_contributory` |
| `84b5927e29` | 824a q081 landmark removal | `unknown` | `non_contributory` |
| `8dbdc7d665` | 827a inv091 phase sync | `unknown` | `non_contributory` |
| `0e9eca7b1c` | 824 q081 landmark removal | `weakens` | `non_contributory` |
| `ba35d7e51c` | 822a sd078 rule selection | `unknown` | `non_contributory` |
| `fab9e5a977` | 673 mech171 x3 (`224744Z`, `010234Z`, `033246Z`) | `does_not_support` | `non_contributory` |

Origin is the **reviewed, authoritative** version in all 11; the stash holds the
pre-review raw. Each origin copy also carries an `evidence_direction_note` explaining
the disposition. Dropping the stashes therefore discards a strictly staler copy.

Two grading traps worth repeating, both hit here:

- **Untracked stash content lives in `stash@{N}^3`, not in the stash commit's tree.**
  All 16 `runner-prepull-untracked` entries hold their manifest *only* in `^3`;
  resolving `<sha>:<path>` returns the tracked version and grades everything wrong.
- **Match by basename across the whole `origin/master` tree, then verify the path.**
  `evidence/experiments/runner_commands/ree-cloud-2.json` first graded CONTENT-DIFFERS
  against `contributors/machines/ree-cloud-2.json` -- a pure basename collision. The
  real path *does* exist on origin (`changed=['commands']`, transient control data).

### The three 673 entries were already recovered once

The origin copies of the three `v3_exq_673_mech171_*` manifests carry
`recovered_from: "Recovered 2026-07-20 from ree-cloud-3/ree-cloud-2 untracked working
tree"`. Cloud-2's copies were pulled in on 2026-07-20 and landed; the stash is residue of
that same event. Independent confirmation that the containment grading is right.

### `ree-v3` stash `c8ad002db9` (2026-05-28, `autostash`)

Holds `experiment_queue.json` only: 1 item (`V3-EXQ-611b`) vs 4 on `origin/main`. The
queue is **DB-authoritative**, and the coordinator has `V3-EXQ-611b` as `completed`
(`claimed_by_machine=DLAPTOP-4.local`). A two-month-old queue snapshot carries no
recoverable state. No evidence content in this stash.

---

## The recovered manifest

### `v3_exq_490h_mech295_cascade_gap4_tier1_20260529T214607Z_v3.json`

Recovered from `evidence/experiments/v3_exq_490h_mech295_cascade_gap4_tier1/…json.bak.20260530`
-- **untracked in the working tree, not in any stash**. Verified byte-identical on both
sides: `git hash-object` = `a7bc91427bb010c6ed237e11342eececa03b0298`.

- `V3-EXQ-490h`, **FAIL**, `evidence_direction: weakens`, claim **MECH-295**
- `supersedes: V3-EXQ-490g`; ran on `ree-cloud-2`; `elapsed_seconds = 5661.46` (1.57h)
- 15 top-level keys, 6 `per_run` entries, complete `acceptance` block
- Coordinator DB: `experiments.status = completed`, **zero** `results` rows
- `origin/master`: **no 490h path at all** (only the autopsy docs mention the id)

**This is the manifest [`failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30`](../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md)
declared unrecoverable.** That autopsy states:

> "Per-claim behavioural autopsy on MECH-295 (490h) or MECH-090 R-c (592b) **cannot
> proceed** because the per-condition acceptance metrics are unrecoverable."

and, on the five-row interpretation grid, "Without knowing which mode fired, autopsy
would have to fabricate an interpretation." The manifest carries exactly that grid, and
the `elapsed_seconds` matches the runner sentinel's `5661.5s` to the decimal, confirming
it is the advertised run and not a partial write:

```
C1_cue_fires            true
C2_dacc_bias            false     <-- the mode that fired
C3_approach_commit      true
C3_lift_vs_baseline     false     <-- and this one
C3_lift_count           0
C3_lift_metric          goal_norm_peak_delta
C4_goal_active          true
pass                    false
```

So the autopsy's load-bearing "unrecoverable" premise has been **false since
2026-05-30**, and the `.bak` was created *after* it was written (file mtime
`May 30 18:56`, autopsy generated `06:02Z`) -- i.e. the cleanup that produced the backup
ran after the autopsy had already concluded the data was gone.

Per that autopsy's own routing table, C2 false routes to dACC wiring and C3-lift false
to a distinct remedy -- so this is not merely a corroborating copy. **Whether to reopen
the 490h autopsy on this evidence is a governance decision this session did not take.**
Note the re-run `V3-EXQ-490i` did land (`20260530T184434Z`, on origin), so the question
is whether 490h's fired-mode changes the 490i reading, not whether MECH-295 lacks
evidence.

**`592b` remains genuinely unrecoverable.** It ran on `DLAPTOP-4.local`; the Mac holds no
`.bak`, no untracked 592b file, and nothing on origin. The autopsy's claim is wrong for
490h and correct for 592b.

### Also preserved (no evidence value, kept rather than judged)

`v3_exq_612_phase3_cutover_smoke_20260528T{173646,175356}Z_v3.json.bak.20260530` --
two phase3-cutover smoke tests, `claim_ids: []`, `elapsed_seconds` 0.145 and 0.146,
absent from origin. Origin already carries two other 612 smoke runs. Retained only
because "never drop on a judgement call"; they are not evidence and should not be
admitted.

---

## Not stranded, deliberately left in place on the worker

- **Three `_per_tick.jsonl` files** (785, 785a, 787; 20.8 MB + 1.3 MB + 13.1 MB).
  **Zero** `_per_tick.jsonl` files exist anywhere on `origin/master`, so these are
  by-design local diagnostic side artifacts, not stranded evidence. Left alone.
- **`629c` and `812` manifests** duplicated inside their experiment subdirectories --
  both SEMANTIC-IDENTICAL to the flat form on origin. Contained.
- **`runner_status/ree-cloud-2.json.bak.phantom-clean`** -- backup of transient
  telemetry; the live path is on origin. Not evidence.

None of these four classes can block a `git pull`, which is why none of them ever
entered the stash list.

---

## Why the mechanism here differs from ree-cloud-3

On ree-cloud-3, **one** recurring untracked manifest was stashed and popped every ~62s,
regrowing the stash list and generating ~20,000 unreachable loose objects that
eventually tripped a gc block; removing that file was the durable fix.

**Cloud-2 has no such stuck file.** Each of the 16 `runner-prepull-untracked` entries
holds a **different** manifest, captured on 16 separate occasions between 2026-07-24 and
2026-07-29 when a `git pull` failed all three retries and fell through past
`experiment_runner.py:1039` without ever calling
`_postpull_restore_prepull_stash()`. Consistent with that reading:

- `git count-objects -vH`: **2183 loose objects, 24.88 MiB** (healthy), `garbage: 0`
- **no `.git/gc.log`** -- gc has never been blocked here
- one stash per pull-failure occasion, newest 2026-07-29T17:39Z, oldest 2026-07-24T16:01Z

So the ree-cloud-3 durable fix (remove the stuck file) **does not apply**. The residual
defect on cloud-2 is the un-popped-on-failure path itself, which is fleet-wide and
already documented in [`README.md`](README.md); nothing worker-local needs changing.

---

## Disposition

Archive tags were created before any inspection and are ref-reachable, therefore
prune-immune. After containment was established on all 21 pairs -- and only then -- the
18 stash entries were dropped. Nothing was dropped on a judgement call, and the three
`.bak` files were copied off the worker before anything else.

## Related

- [`README.md`](README.md) -- ree-cloud-3 (2026-07-29), the method this follows
- [`../ree_v3_orphaned_autostash_triage.md`](../ree_v3_orphaned_autostash_triage.md) --
  archive-tag convention and containment method
- [`../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md`](../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md)
  -- the autopsy whose "unrecoverable" premise this recovery falsifies for 490h
- `REE_assembly/scripts/runner_git_health.py` -- the active probe that surfaced the
  stash counts. It reports stash **counts** only; it cannot tell a contained stash from
  a stranded one, and it does not look at untracked files at all.
