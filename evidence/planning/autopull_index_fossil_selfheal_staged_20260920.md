# Auto-pull index-fossil self-heal -- root cause, predicate, held-out replay

**Status: AWAITING USER REVIEW** (helper + tests landed INERT; wiring is decision chip `chip-20260920-autopull-fossil-reconcile-wiring-decision`)

- Staged: 2026-09-20 by `ml-autopull-fossil-selfheal-20260920` (`/metaworker-learning`)
- Work chip: `chip-20260920-ml-autopull-index-fossil-selfheal`
- Answers decision chip: `chip-20260920-ml-checkoutdiverged-dlaptop-ree-assembly-recurrence` (user, 2026-09-20T09:36Z: route to `/metaworker-learning`)
- Occurrences: `chip-checkoutdiverged-dlaptop-ree-assembly-master` (gen 1, 2026-09-18) and `-g2` (gen 2, 2026-09-20)

## 1. Summary

The recurrence is not "the auto-pull cannot self-heal dirt". It is narrower and self-inflicted:
**the Mac is blocked by its own pushed commit.** Since umbrella `b4a44af59` (2026-09-16),
`igw_routine_tick.py` lands `evidence/planning/igw_routine_log.md` with
`ree_commit.py --to-remote-tip`, which pushes the edit to origin **without moving the local
ref or index**. The path is left ` M` with working-tree bytes identical to origin's.
`land_at_remote_tip`'s docstring ("THE PERSISTENT-DIRTY TRADE") accepts this on the stated
assumption that "a plain `git pull`" clears it later. **That assumption is false**: git refuses a
fast-forward over a locally modified path *without comparing content*. So after every hourly
tick the next incoming range contains the box's own log commit, and both pullers refuse until an
unrelated `ree_commit`/`safe_adopt_ref` ref move happens to run the skew repair. In a quiet
period (overnight, no sessions committing) nothing does, the checkout stays behind for hours,
and the 2h `checkoutdiverged` detector fires.

A second, independent finding: **the launchd puller is inert on this repo.** Its pre-gate
refuses on *any* non-derived tracked dirt before it ever tries the fast-forward, and DLAPTOP's
non-owner workset regen keeps two files permanently dirty.

## 2. Measured mechanism

### 2.1 Two pullers, not one

| Puller | Cadence | Gate | REE_assembly syncs since 2026-09-16 |
|---|---|---|---|
| `serve.py:_pull_repo` (`git pull --ff-only`) | 5 min | git's own overlap check | 22 of the last 400 `master` reflog entries |
| `ree_git_sync_repair.sh` (launchd `com.ree.gitsyncrepair`) | 10 min | **any** tracked dirt outside `derived_re` blocks *before* `merge --ff-only` is attempted; `derived_re` is empty for REE_assembly | **0** `SYNCED`, 263 `BEHIND_NOT_SYNCED`, 184 `NEEDS_HUMAN`, 126 `OK` |

The other 372 of 400 reflog entries are message-less `update-ref` moves -- `ree_commit.py`
commits/convergences, whose post-move `check_head_worktree_skew()` is what has actually been
clearing the fossil. Healing therefore depends on *session activity*, which is why both
generations opened in quiet windows.

### 2.2 Dose-response on the adoption date

Launchd-puller cycles per day logging `BEHIND_NOT_SYNCED` and naming `igw_routine_log.md`
(`~/Library/Logs/ree_git_sync_repair.log`):

| 09-02 | 09-03 | 09-04 | 09-08 | 09-14 | 09-15 | **09-16** | 09-17 | 09-18 | 09-19 | 09-20 (to 10:30Z) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 4 | 1 | 6 | 6 | **12** | 29 | 40 | 25 | 50 |

`b4a44af59` landed 2026-09-16T12:32Z. Stuck runs of >= 60 min since then: 16, longest 280 min
(2026-09-20T05:20Z..10:02Z -- a **third** episode, after gen 2 was healed at 04:49Z; it cleared
only when a session's `ree_commit` landed at 10:05Z).

### 2.3 Generation 1 (2026-09-18, first unreached 15:01Z, 5 behind)

Healer resolution note: skew repair after `safe_adopt_ref.py` "cleared 1 MM index fossil on
igw_routine_log.md (index-only reset -- worktree already matched new HEAD)". The note attributes
the block to the two workset regen files; that is true of the *launchd* gate (section 2.1) but
not of `serve.py`'s pull, for which those files block only if the incoming range touches them.
The fossil is the common factor with gen 2.

### 2.4 Generation 2 (2026-09-20, first unreached 02:07Z, 6 behind)

Mac tick ran 01:42:02Z..01:45:36Z and pushed `0c3a298b0f6` ("igw-ledger: update", author REE
Automation (Mac), touches `igw_routine_log.md`). Local `master` reflog has **no** entry for it
(last move 01:25:31Z `pull --ff-only`, next 04:48Z = the Healer's adopt). Launchd log: `OK` at
01:34Z and 01:45Z, `BEHIND_NOT_SYNCED` naming `igw_routine_log.md` from 01:55Z continuously to
04:39Z. Healer: ` M` before the move, `MM` fossil after it, index-only reset, no content touched;
the three other dirty files "were untouched by the incoming range".

### 2.5 Why git blocks (verified, scratch repo, git 2.x on DLAPTOP)

Working tree `l1\nl2`, index == HEAD `l1`, origin tip `l1\nl2` (hash-identical to the working
tree): `git merge --ff-only origin/master` -> `error: Your local changes to the following files
would be overwritten by merge: log.md`. Pinned as
`test_native_ff_really_is_blocked_by_a_content_identical_path`.

## 3. The predicate (Question 2)

Let `T` = the sha `origin/<branch>` resolves to, read once. Preconditions, else
`NOT_APPLICABLE`: HEAD on `<branch>`; no rebase/merge/cherry-pick/revert/bisect marker; no
`ree_adopt_repair_incomplete` sentinel; **ahead == 0**; behind > 0.

`overlap = (tracked paths in git status) & (paths in HEAD..T)`. A path is a **pre-pull fossil**
iff ALL of:

1. status is exactly ` M` (index == HEAD -- anything staged, deleted, renamed, unmerged is out);
2. `T` holds it as a regular blob (100644/100755) and the stage-0 index mode equals it;
3. it is a regular file on disk (lstat), not a symlink;
4. `git hash-object -- <p>` == `T:<p>`;
5. `git diff --quiet T -- <p>` exits 0.

**Content equality is against the INCOMING TIP `T`**, not HEAD and not an ancestor. Clause 5 is
literally the question `check_head_worktree_skew()` already asks (`git diff --quiet HEAD -- p`),
with `T` in place of `HEAD`: the pre-pull fossil is the pre-move twin of the post-move `MM`
fossil -- "working tree equals the ref that is/becomes HEAD". 4 and 5 are redundant on purpose.
No ancestry search, no reverse-apply, no heuristic: it is a hash equality.

**Failure direction: CLOSED, and all-or-nothing.** Any git error, unreadable file or false clause
-> UNPROVEN. One unproven overlap path -> nothing is reconciled, including provable fossils
("partial proof is not proof"), because the fast-forward cannot succeed anyway and a half-staged
index on a behind checkout is worse than today. The verdict names fossils and unproven paths
separately -- that naming IS the discriminator: `UNPROVEN` = genuinely dirty, needs a human;
`RECONCILED` = was only ever a fossil.

## 4. The reconcile (Question 1)

```
git update-index --cacheinfo <mode>,<T:p blob>,<p>     # per fossil
git merge --ff-only T
# on refusal: git reset -q -- <fossil paths>           (index-only rollback)
```

- The index entry is written **from the target blob id, never from the working tree**. No
  working-tree byte of a fossil path is written at any point.
- git's two-way merge keeps an index entry that already equals the target and does not touch the
  file. So a live edit landing between proof and merge is neither staged nor overwritten -- it
  comes out as ` M` against the new HEAD. Verified by hand and pinned
  (`test_live_edit_arriving_after_the_proof_survives`).
- Every other path is adjudicated by git's own fast-forward exactly as today. The tool never
  stashes, checks out, resets a working-tree file, or moves a ref by hand; with ahead == 0 no
  commit can be dropped. **Nothing that is discarded today changes, and nothing new is
  discarded.** Genuinely dirty overlaps sit exactly as they do now.
- Chosen over "pre-prove, then `safe_adopt_ref.py`": a bare ref move skews *every* path in the
  incoming range and relies on the repair to materialise them (the 2026-08-18 interrupted-repair
  hazard); a native fast-forward writes them itself and remains the final gate.

Constraints honoured: no hook, no ref-move/pre-push guard anywhere (hub/workers untouched); not a
proof route for `ref_convergence` (ahead > 0 is `NOT_APPLICABLE` by construction; no
reverse-apply); no `git checkout -- .`, no broad reset.

## 5. What landed in-session (inert)

- `scripts/ff_fossil_reconcile.py` -- `--repo --branch [--dry-run] [--json]`; verdicts
  `IN_SYNC` / `WOULD_RECONCILE` / `RECONCILED` / `UNPROVEN` / `NO_OVERLAP` / `NOT_APPLICABLE` /
  `FF_REFUSED`.
- `scripts/test_ff_fossil_reconcile.py` -- 14 tests, real repos + real filesystem remote; written
  first and seen failing (12 F / 1 E) before the script existed; 14/14 green after. 9 of 14 are
  negative controls asserting HEAD, `ls-files -s`, `git status` and every file byte are unchanged.

**Nothing calls it.** Landing it changes no behaviour on any box.

## 6. Held-out replay

The design was written from gen 1 and gen 2. Both reconstruct as pure fossils (in-sample, for the
record): gen 1 at the adopt (HEAD `74bd9c16d1`, T `7860cdb27c`, ahead 0 / behind 21) and gen 2
(HEAD `1a5b04c996`, T `8e81e1106e`, ahead 0 / behind 2) -- in each, `igw_routine_log.md` is the
ONLY path in `HEAD..T` that was dirty, and `T:log` is blob-identical to the last Mac tick's
content (`ae7f857f` / `6a03dc85`).

**Reconstruction method and its one assumption.** HEAD and T come from the `master` and
`origin/master` reflogs at the instant; the dirty set from the launchd puller's log line (names
at most 5 paths); the working-tree log is taken to be the last Mac-authored log commit at or
before T. That assumption is measured, not guessed: `REE Automation (Mac)` authored 132 of the
133 commits touching the file since 2026-09-16, and the tick lands exactly what it wrote to disk.
Probe: scratchpad `fossil_replay_probe.py` (not landed; every input is in git + the log).

### 6.1 Non-degenerate cases (old = blocked for an hour or more; new = RECONCILED on the first cycle)

| # | Window (UTC) | Old outcome | HEAD..T | Modified paths in range | New verdict |
|---|---|---|---|---|---|
| H1 | 09-16T23:35 .. 09-17T01:39 | blocked 130 min | `adfc3b5629..8a8efa4bb9`, 0 ahead / 2 behind | log only (+4 added manifests) | RECONCILED |
| H2 | 09-17T02:51 .. 04:54 | blocked 130 min | `e95574ca7f..8530e26e0d`, 0 / 2 | log only (+4 added manifests) | RECONCILED |
| H3 | 09-17T05:56 .. 06:57 | blocked 70 min | `4ec9c7f6f4..eebec95ae6`, 0 / 1 | log only | RECONCILED |
| H4 | 09-19T23:41 .. 09-20T01:24 | blocked 110 min | `c20c29561a..f6b6f67783`, 0 / 1 | log only | RECONCILED |
| H5 | 09-20T05:20 .. 10:02 (the third episode, after gen 2 was healed) | blocked 280 min | `e3e6f13bdd..4c8fa85cdb`, 0 / 2 | log only; full dirty set known (4 paths), overlap = {log} | RECONCILED |

In all five the only *modified* incoming path is the Mac's own log; added files cannot be
tracked-dirty locally. So nothing else could have blocked `pull --ff-only`, and that it WAS
blocked for 70-280 min is itself the confirmation that the fossil was the blocker.

### 6.2 Indeterminate from history (stated, not fabricated)

Three windows (09-17T07:58, 09-18T02:10, 09-18T07:19; also 09-19T01:22 with
`experiment_proposals.v1.json`) have `igw_assignments.json` and `igw_routine_ledger.json` in the
incoming range as well, with Hub-authored commits interleaved. Whether the Mac's working-tree
JSON equalled T cannot be reconstructed. The tool would have either reconciled (all equal) or
returned UNPROVEN naming the exact JSON path. Both beat a silent multi-hour block, but these do
NOT count as evidence the reconcile fires. This is what made all-or-nothing plus per-path naming
part of the design rather than an afterthought.

### 6.3 Negative controls (old and new give the SAME call -- degenerate for GOV-HELDOUT-1 purposes, listed because they are the fail-closed check)

| Incident | Shape | Clause that stops the tool | Call |
|---|---|---|---|
| 2026-09-04 ree-v3 `experiment_queue.json` "blocks ff pull" (WORKSPACE_STATE) | `MM`; HEAD 0 items / index 2 (another session's staged addition) / worktree 6 (matches no commit in 600) | clause 1 (status not ` M`) | UNPROVEN, untouched -- correct, a human was needed |
| 2026-09-20 ree-cloud-5 REE_assembly, 78-commit pull blocked by 10 stale regen files | worktree superseded by a later upstream regen, i.e. != T | clause 4 | UNPROVEN, untouched; the Healer's stash + archive-tag route stands |
| 2026-09-10 / 09-17..19 live work under `MM`/` M` (`claim_evidence.v1.json`, `igw_routine_log.md` carrying uncommitted appends) | worktree != HEAD and != T | clause 1 or 4 | untouched; live bytes never read-for-write |
| 2026-08-28 O10 DLAPTOP `TASK_CLAIMS.json` (same `land_at_remote_tip` trade) | ` M` but `[ahead 49, behind 117]`, worktree != origin | precondition ahead == 0 | NOT_APPLICABLE |
| 2026-07-30 relaxed-montalcini dropped IGW commits (A-72/A-73) | `[ahead 3, behind 1]` + bare `update-ref` | precondition ahead == 0; the tool never moves a ref by hand | NOT_APPLICABLE -- the dropped-commit class cannot arise |
| 2026-09-15 update-docs reverted 18 live files (A-95) | `git checkout HEAD --` on foreign dirt | the tool contains no checkout/restore of any kind | n/a by construction |
| 2026-09-02 DLAPTOP umbrella `TASK_CLAIMS.json` blocking ff (R2) | stale render, != T | clause 4 | UNPROVEN -- hash equality is NARROWER than R2's per-row subsumption and does not replace it |

**Outcome of the check (record for the edit):** passed on 5 non-degenerate cases; it also
*changed the proposal* -- 6.2 is why a partial proof reconciles nothing and why the verdict
names paths, and the 2026-08-18 regression incident (A-05: a fossil left in place became a later
writer's read-modify-write source) is why "leave it and wait" is not treated as the safe default.

**Counterweight.** This cost one background research pass (~196k subagent tokens) plus the
replay. And the fix is symptomatic: it clears the fossil one puller cycle after
`--to-remote-tip` creates it; it does not stop it being created (option C below does).

## 7. Question 3 -- detector / Healer cadence

**No change recommended.** With the reconcile wired, the fossil class clears within one puller
cycle (5 min), far inside the detector's 2h threshold. What remains for the detector is the
genuinely-dirty class, which needs a human however often it is sampled; a faster cadence would
only mint more chips about the same live session. The measurable to watch instead: count of
`ff_fossil_reconcile` `UNPROVEN` verdicts per day, by path.

## 8. Second finding, NOT built: the launchd puller's pre-gate

`ree_git_sync_repair.sh` exits `BEHIND_NOT_SYNCED` on any non-derived tracked dirt *before*
trying `git merge --ff-only`. On REE_assembly that is always (non-owner workset regen), hence 0
`SYNCED` in five days. The script's own 2026-08-22 comment already argues the principle for
derived paths ("lets `git merge --ff-only` adjudicate ... Nothing is ever discarded to make
room"). Extending that to "only dirt that OVERLAPS the incoming range blocks" discards nothing
either -- but it changes when a fast-forward is attempted on six repos, so it is put to the user
in the decision chip rather than built.

## 9. Test plan

Landed: `scripts/test_ff_fossil_reconcile.py` (14; in the corpus runner: 1 selected / 1 passed).
For the wiring, if approved:
1. `serve.py`: unit-test `_pull_repo` with a stub helper -- RECONCILED clears `stuck_since`;
   UNPROVEN / NOT_APPLICABLE / missing helper / helper timeout all print today's line unchanged.
2. `scripts/test_ree_git_sync_repair.sh`: fossil-only case -> SYNCED; fossil + genuinely dirty
   overlap -> BEHIND_NOT_SYNCED with both named; the wedged (`reset --hard`) gate byte-unchanged.
3. Live acceptance on DLAPTOP: after the next hourly tick, `--dry-run` reports
   `WOULD_RECONCILE fossils=[evidence/planning/igw_routine_log.md]`; then one real cycle; then
   `git status` shows only the workset/steward dirt and 0 behind.
4. Seven-day readback: stuck runs >= 60 min in `ree_git_sync_repair.log` for REE_assembly
   (baseline: 16 in 4.5 days); `checkoutdiverged-dlaptop-ree-assembly` generations (baseline: 2,
   plus one unchipped 280-min episode).

## 10. Decision requested

`chip-20260920-autopull-fossil-reconcile-wiring-decision` (kind: decision):
- **A (recommended)** -- wire the helper into `serve.py:_pull_repo`'s dirty branch (shell-out,
  gated on the file existing, so a box without the umbrella behaves exactly as today) AND into
  `ree_git_sync_repair.sh`'s behind path; correct `land_at_remote_tip`'s docstring.
- **B** -- `serve.py` only (the one effective puller on this repo).
- **C** -- source-side: `igw_routine_tick.py` calls the helper at tick end, right after the
  landing that creates the fossil (heals even when the Explorer is not running). Can be combined
  with A or B.
- **D** -- hold; helper stays inert.
- Separate yes/no: make the launchd pre-gate overlap-aware (section 8).
