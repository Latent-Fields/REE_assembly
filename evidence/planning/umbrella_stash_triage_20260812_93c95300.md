# Umbrella `REE_Working` stash triage -- `93c953009a` (2026-08-12)

**Repo:** `/Users/dgolden/REE_Working` (umbrella)
**Entry:** `stash@{0}` -> `93c953009afe43e72c23fec877c9d997e69249db`, taken 2026-08-12 19:20:59 +0100
**Stash message:** `On claude/recording-standard-provenance-mandatory-ace7b6: pre-merge-reconcile stash, magical-khorana-6133b9 worktree, 2026-08-12T18:2x`
**Archive tag:** `stash-archive/20260812-93c95300` (local-only, per the round-1/2 convention)
**Triaged:** 2026-08-18T06:04:04Z, session `metaworker-chip-stash-ree-working-93c953009a` (chip `chip-stash-ree-working-93c953009a`)
**Trunk at triage time:** `origin/master` = `57bde777`

---

## Verdict: **ALREADY-LANDED (proven)** -- nothing orphaned, nothing to restore

`audit_stashes.py` graded this **HAND-AUTHORED CONTENT** because all 8 paths fall outside its
derive-only allowlist. That grade is a pointer for a human, not a finding: it fires on path
identity, before any containment test. Every one of the 8 paths has now been graded
individually by the four-test method in `ree_v3_orphaned_autostash_triage.md`, and **all 8
resolve as contained, superseded, or regenerable.**

The entry is a **stale post-landing reconcile snapshot**, not lost work. The code it carries
landed on `origin/master` at **18:57Z and 19:01Z**; the stash was taken at **19:20Z**, i.e.
*after* its own content was already on trunk. It was a working-tree snapshot taken during a
merge reconcile, and the tree it snapshotted was already redundant with trunk.

**This entry was NOT an `autostash`** (0 autostash entries in the list) -- it was hand-taken
by a session doing a pre-merge reconcile, so the silent-runner-autostash defect that motivates
the triage doc is not implicated here.

### Why the umbrella was not being audited until now

`audit_stashes.py --all` enumerated the *children* of `REE_Working`, so the umbrella -- their
parent -- was excluded by construction and reachable only by naming it explicitly. This entry
sat unreported through many `/session-land` runs for 5.5 days as a result. The default set was
widened to include the umbrella on 2026-08-18 (see `CLAUDE.md` Session Startup Protocol step 7);
this triage is the first entry that widening surfaced.

---

## Per-path grading

| # | Path | Test that proved it | Result |
|---|---|---|---|
| 1 | `scripts/igw_routine_tick.py` | 3 (symbols) + 4 (line-exact) | **PROVEN** -- 0 of 58 session-added lines absent from `origin/master`; all 8 new symbols present |
| 2 | `scripts/test_igw_routine_tick_reap.py` | **2 (reverse-apply)** + 4 | **PROVEN** -- hunks reverse-apply cleanly into an index seeded from `origin/master`; 0 of 93 added lines absent |
| 3 | `WORKSPACE_STATE.md` | 4 (line-exact) | **PROVEN** -- 0 of 169 session-added lines absent |
| 4 | `TASK_CHIPS.json` | structural (`chip_ref` set) | **PROVEN** -- 0 in-stash-only; origin is a strict superset (932 vs 555) |
| 5 | `TASK_CLAIMS.json` | structural (`(session_id, claimed_at)` set) | **SUPERSEDED** -- see below |
| 6 | `docs/worktree_session_registry.md` | derived-artifact identity | **REGENERABLE** -- `Generated: 2026-08-12T17:55:10Z` |
| 7 | `worktree_session_registry.json` | derived-artifact identity | **REGENERABLE** -- `generated_at` 2026-08-12T17:55:10Z vs origin's 2026-08-18T01:44:36Z |
| 8 | `worktree_audit_20260812.md` | derived-artifact identity | **REGENERABLE** -- `Generated: 2026-08-12T17:54:50Z` |

### 1-2: the code half (the only part that could have been a real loss)

The stash carries a complete, coherent implementation of
`chip-20260812-igw-done-template-headless-session-land`: the split of
`_DONE_STEP_TEMPLATE` into `_DONE_STEP_HEADLESS_INTRO` / `_DONE_STEP_INTERACTIVE_INTRO` +
a shared `_DONE_STEP_BODY`, plus `write_start_here(..., headless=...)` and the
`headless=not human_reason` call site in `cmd_tick`, plus 104 lines of new test.

This is exactly the **coupled implementation-and-test pair** shape that CLAUDE.md remedy (a2)
warns about, so both halves were graded, not just the larger one. Both landed:

- `b8cb41af` `igw_routine_tick: split _DONE_STEP_TEMPLATE by headless vs launched_manual`
  (nooarche, 2026-08-12 18:57:19 +0100)
- `184b9cf4` same subject (REE Automation (Mac), 2026-08-12 19:01:19 +0100)

Both are reachable from `origin/master`. All 8 stash-introduced symbols
(`_DONE_STEP_HEADLESS_INTRO`, `_DONE_STEP_INTERACTIVE_INTRO`, `_DONE_STEP_BODY`,
`_DONE_STEP_TEMPLATE_HEADLESS`, `_DONE_STEP_TEMPLATE_INTERACTIVE`, `headless: bool`,
`headless=not human_reason`) resolve on `origin/master` today.

**A trap worth recording for the next triage.** Diffing the stash *blob* against the tip
reports `82 insertions, 794 deletions` on `igw_routine_tick.py` and **54 of 82 "added" lines
absent from trunk** -- which reads as major loss and is entirely an artifact. The file grew
3360 -> 4119 lines on trunk in the six days since; the stash blob is an *older base* plus a
small edit, so the diff is dominated by trunk's own evolution and the "absent" lines are
pre-existing code trunk has since refactored. The correct test is the stash's **own** diff
(`git diff <stash>^ <stash> -- <path>`), scoped to the lines the session actually added. That
gives 0 of 58 absent. Grading on the blob-vs-tip diff would have produced a false
GENUINELY-ORPHANED verdict on content that was already on trunk.

**Second trap: `git show <stash-sha>:<path>` silently returns the COMMIT, not the blob.** A
stash is a merge commit (here an octopus, 3 parents: `0f76618e`, `ebcf374f`, `8ac1bd87`), and
`git show` on it prints the commit object rather than resolving the path. It exits 0, so a
redirect captures the commit text and every downstream line count and containment check is
silently wrong. Use `git rev-parse <stash>:<path>` to get the blob sha and then
`git cat-file blob <sha>`.

### 5: `TASK_CLAIMS.json` -- all 66 stash entries absent from origin, none of them lost

Origin carries 74 entries; the stash carries 66; the intersection is **empty**. That is pure
turnover on a file whose `done` entries expire after 24h, not deletion:

- **62 were `status: done`** at stash time -- removed on schedule by
  `prune_task_claims_done.py`.
- **4 were `status: active`** and needed individual proof. All four were opened on trunk
  (`claim: open ...` commits reachable from `origin/master`) and all four were removed by a
  single later prune commit `cf44044e` (`prune done entries older than 24h`). Since that
  script only ever removes `done` entries, their presence in it proves they reached `done`
  first. Confirmed directly at `cf44044e^`, each with `closed_at` **and** `completion_note`:

  | session_id | closed_at | completion_note (head) |
  |---|---|---|
  | `sd-016-h3-algorithm-3370cd` | 2026-08-12T18:14:38Z | `ree-v3 78e9630 (main): sync_daemon._materialize_sidefiles ...` |
  | `mech357-pressure-scoping-11e9c9` | 2026-08-12T18:07:50Z | `REE_Working master 0c31682a: split igw_routine_tick.py's _DONE_STEP_TEMPLATE ...` |
  | `pensive-franklin-1e285b` | 2026-08-12T18:11:27Z | `REE_Working master (merge 5124dbf8): scripts/audit_retest_staleness.py ...` |
  | `pensive-franklin-1e285b-report` | 2026-08-12T18:12:02Z | `REE_assembly master c9ef24f62c: retest_staleness_audit_report.md ...` |

  The second row is the corroborating detail: `mech357-pressure-scoping-11e9c9` is the session
  that **authored the stashed code change**, and it closed its own claim at 18:07:50Z naming
  the landing commit -- 73 minutes before the stash was taken. The stash's `active` status for
  these four is simply older than their closures.

### 6-8: the three derived snapshots

All three carry an explicit generation timestamp and are rebuilt by
`sync_worktree_session_registry.py` / `worktree_audit_report.py`. Their in-stash-only content
is worktree slugs since GC'd (14 of them) and commit lines since scrolled off -- a point-in-time
report whose value has expired, with the underlying facts still in git history. Regenerating
today produces today's snapshot by design, not this one. Note `worktree_session_registry.*` is
additionally **machine-scoped** (Mac-owned) as of 2026-08-16, so a stale copy of it is expected
rather than anomalous.

---

## Actions taken

1. Archive-tagged `stash-archive/20260812-93c95300` -> `93c953009afe...`, and verified all 8
   blobs resolve through the tag **before** touching the entry.
2. Re-verified `stash@{0}` still resolved to `93c953009a` immediately before dropping (the
   entry is positional and moves under you).
3. Dropped `stash@{0}`.
4. Re-verified after the drop that all 8 paths still resolve through the tag.

**Residual, stated rather than papered over:** the archive tag is **local-only** by the
established convention, so the sole surviving copy of this content lives in the Mac's umbrella
`.git`. That is the same exposure every prior `stash-archive/*` tag carries and was not changed
here unilaterally; it is worth a decision at some point whether these tags should be pushed.

## Coverage note

`audit_stashes.py`'s grade is deliberately conservative and **cannot** be read as a finding on
its own -- a HAND-AUTHORED grade means "no automated test applies, a human must read it", and
in this case a human-equivalent read found the entry fully contained. The grade did its job:
it stopped an automated drop of an entry carrying a real coupled code/test pair, and the pair
turned out to be already on trunk.
