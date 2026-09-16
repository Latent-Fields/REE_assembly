# Refwedge class, REE_assembly/master on DLAPTOP: root cause and durable fix (2026-09-16)

**Status: ACCEPTED 2026-09-16 (user, doc-review walk). Build F-A+F-C+rescue landed REE_Working b4a44af59 (12:32Z). Post-fix recurrence (g9, af9608e14 stranded 20:15Z) routed to chip-20260916-refwedge-g9-post-fix-strand; converge command to be refreshed there (section 7's sha list is stale).**

Skill: `/metaworker-learning`. Session: `metaworker-learning-refwedge-20260916` (interactive,
DLAPTOP, main checkout). Claim opened 2026-09-16T12:04:03Z. Decision chip: see section 8.
Trigger: the user's `/metaworker-learning` invocation, taking up the open decision chip
`chip-20260916-refwedge-dlaptop-reeassembly-learning-route-g8` (Option 1, "authorise a
/metaworker-learning session, DLAPTOP-capable") and the g8 finding
`chip-refwedge-dlaptop-ree-assembly-master-g8`, whose own text says "route this to
/metaworker-learning for a root-cause pass INSTEAD of re-fixing the instance".

Nothing in `scripts/` was modified by this session. The live g8 wedge was left as found
(section 7 gives the audited, ready-to-run instance-clear command).

---

## 0. One-paragraph summary

Every one of the 5 commits that ref_convergence cannot prove in the g8 range is a local
Mac commit whose two blobs are **byte-identical to a hub-authored commit landed on origin
seconds earlier**, built from a local base that was already behind origin. The tick makes
them because `commit_ledger_files` hands `[igw_routine_ledger.json, igw_assignments.json]`
to the coordinator CAS as one batch; when only one of the two changed, the other comes back
`degraded` (a silent "no-op vs origin"), the batch falls through to the git path, and
`ree_commit.py` diffs against the *stale local HEAD*, not origin, so it mints a commit that
re-lands origin's own content. `ree_commit`'s push-retry then correctly says "content
already on origin -- nothing to push", makes no cherry-pick, and never attempts convergence,
leaving a commit with no `-x` backref and a diff (from a stale base) whose patch-id cannot
match anything upstream. That commit wedges the checkout; the wedge keeps HEAD behind
origin; being behind is the precondition for the next stale-base re-commit. Self-feeding,
deterministic, one poison commit per "update"-only tick. The durable fix is not new code:
`ree_commit.py --to-remote-tip` (built 2026-08-18) already turns exactly this case into a
no-op with no local commit, and the 2026-08-28 investigation's held-out section named it as
"the already-built version" of the rule. The IGW tick never adopted it.

---

## 1. Occurrences: genuine recurrence of ONE root cause (Step 1)

Eight generations of `chip-refwedge-dlaptop-ree-assembly-master-g*` since 2026-09-08.
Counted from resolution notes, not chip existence; g5/g6 self-resolved on quiet-hysteresis
and are not occurrences. The generations with a per-commit audit all show the same shape:
**an automation on the Mac creates a local commit whose content already equals origin's
tip, from a base behind origin, and that commit is unprovable by construction.**

| gen | date | audited unproven commits | shape | what was done |
|---|---|---|---|---|
| g3 | 09-08 | `aaec010637`, `4bb43c3523` "ledger+assignment entries present on origin"; `17b4cea2ae` "all 3 files byte-identical to origin"; `7efec49986` genuine strand (240s timeout) | 3 of 4 = this class; 1 = timeout strand (since fixed, `chip-20260908-igw-tick-commit-ledger-push-retry-timeout`) | cleared; two symptom chips |
| g4 | 09-09 | 40 ahead, "0 stranded of 40, content already upstream" | this class | cleared |
| g7 | 09-15 | `bff7ef166f` workset regen "byte-identical to origin/master on both files" | this class, workset writer | fix A (skip-if-identical-to-origin) + hub-ownership gate, both **scoped to the workset writer only** |
| g8 | 09-16 | `5844f89d3a d605a540d9 384c1e55c4 bbeea9d72c 435c4e16ea`, all `igw-ledger: update` touching both JSON files | this class, ledger writer | this document |

Three audited generations, one mechanism, three different files. g7's fixes were correct for
the file they covered and could not have covered g8: they gate `commit_workset_files`, and g8
is `commit_ledger_files`. Threshold 2 is exceeded; this is a `/metaworker-learning` case.

Related but **distinct** classes, not folded in here: the ree-cloud-3 unmerged-path wedge
(`chip-20260916-cloud3-reeassembly-unmerged-wedge`, autostash-pop failure), the umbrella
`rotate_workspace_state.py` faithfulness-refusal strand
(`chip-20260911-wsrotate-push-refusal-strands-ahead`, a P3-class deliberate no-push), and
the R1 rate re-measurement (`chip-20260910-merge-refwedge-class`). Each has its own owner.

---

## 2. The mechanism, on data (not shape)

All measurements on DLAPTOP, `/Users/dgolden/REE_Working/REE_assembly`, 2026-09-16T12:00Z
to 12:15Z, against the live g8 wedge (ahead 34, behind 49, 5 unproven, refusing since
00:54:01Z).

### 2.1 Each unproven commit is a hub commit re-landed from a stale base

| local (Mac) | hub twin on origin | blobs equal (ledger, assignments) | local base | commits on origin between base and twin |
|---|---|---|---|---|
| `5844f89d3a` 00:52:30Z | `db2702111bb` 00:52:23Z | YES, YES | `e55cdb2a605` (on origin) | `3c09359f912`, `e72b351fd25` (hub, touched assignments) |
| `d605a540d9` 01:57:06Z | `ad4feeb68da` 01:56:59Z | YES, YES | | |
| `384c1e55c4` 03:01:53Z | `0e8b7a734c4` 03:01:47Z | YES, YES | | |
| `bbeea9d72c` 07:22:32Z | `40ab2c8a890` 07:22:25Z | YES, YES | `a5540f7cea` | |
| `435c4e16ea` 10:47:52Z | `cfb0e71cb46` 10:47:44Z | YES, YES | | |

`git rev-parse <local>:<path>` equals `git rev-parse <hub-twin>:<path>` for both files in all
five cases. The hub twin's body reads `session_id: igw_routine_tick / machine: DLAPTOP-4.local`:
it is the hub materializer landing **this Mac's own CAS submission**. There is no second IGW
tick on the hub (`systemctl list-timers` on ree-cloud-1 shows only the TASK_CLAIMS/CHIPS
materializer and git-sync-repair). The `ree_commit_intent/5844f89d3a....json` record confirms
the Mac commit was built by `ree_commit.py` with `base = e55cdb2a605`, message
`igw-ledger: update`, at 00:52:31Z.

Diff shape: the hub twin `db2702111bb` is "1 file changed, 21 insertions" (ledger only). The
Mac commit `5844f89d3a` is "2 files changed, 52 insertions, 4 deletions" -- it also carries
the assignments delta that origin commits `3c09359f912`/`e72b351fd25` had already made,
because its base predates them. That is why route A (patch-id) cannot match it, and why the
single-file IGW commits in the same range (log.md appends, spawn-only assignments) all
proved fine: their diffs from the stale base happen to equal one upstream commit's diff.

### 2.2 Why the tick mints it: the CAS batch and the false no-op premise

`igw_routine_tick.py` (main checkout, HEAD `8b5d0ac53`):

1. `commit_ledger_files()` (line ~861) passes `cas_rel = [ledger, assignments]` as ONE
   `_ree_commit` call (DP-3: a routed batch is all-or-nothing).
2. `_ree_commit()` (line ~740): `all_suppressed = True; for p in rel_paths: outcome =
   _coordinator_submit_cas(p, ...)`; any outcome other than `"suppressed"` clears the flag
   and the whole batch falls through to the git path.
3. `_coordinator_submit_cas()` (line ~650): the ledger differs from origin -> POST -> hub
   materializes -> suppress predicate on -> `"suppressed"` (the log line at 00:52 confirms
   `commit db2702111bb`). The assignments file did **not** change in this tick's update
   phase, so `_blob_at(base_sha, rel_path) == new_content` is true and it returns
   `"degraded"` **silently**, with the in-code comment `# no-op; the git path will also
   no-op`.
4. That premise is false whenever local HEAD != origin tip. `ree_commit.py`'s no-op
   short-circuit (`main()` line ~4175) compares the private-index tree against **HEAD's**
   tree, not origin's. On a checkout that is behind (the Mac's steady state: the hub
   materializer advances origin every few minutes, and the Mac only adopts origin after a
   *proven* push), both files differ from HEAD, so a real commit is built.
5. `--push` is rejected; `retry_push_via_worktree` (line ~2448) runs `git diff --quiet HEAD
   origin/master -- <paths>`, finds them equal, prints `content already on origin/master --
   nothing to push` and **returns True without cherry-picking and without calling
   `_converge_after_push`**. No `-x` twin is ever created.
6. ref_convergence: route B finds no backref; route A's patch-id differs (stale base, extra
   hunks); route C does not apply (`REGISTRY_SPECS` holds only TASK_CLAIMS/TASK_CHIPS).
   Unproven. Refuse. Wedge.
7. The latch (2026-08-28 investigation section 3): wedged -> HEAD stays behind -> step 4
   fires on the next "update"-only tick. Five ticks in 11 hours, five poison commits.

The Mac log shows nothing for these commits: `_ree_commit` prints only on a non-zero exit,
and this path exits 0 ("nothing to push" is success). The 14 `ree_commit: committed` lines
in the log since 09-15 are all the rc=1 skew/reject cases; the poison commits are silent.

### 2.3 What the two 2026-09-15 fixes did and did not cover

- Fix A (`08fabdb21`, `_workset_materially_changed_vs(origin)`) is exactly the right idea
  -- "never mint a commit whose content is already origin's tip" -- implemented for
  `commit_workset_files` only.
- The ownership gate (`8b5d0ac53`) removed the Mac's workset commit entirely. Correct for the
  workset (a deterministic regen the hub also produces). It has no bearing on the ledger
  commit, which is the Mac tick's own bookkeeping of the sessions it spawns.

Both fixes are working as designed; g8 is the same class on a file they were not written
for. This is why a third per-file patch is the wrong response.

---

## 3. The durable fix: use the mode that was built for this (Step 3)

### 3.1 F-A (recommended): the IGW tick lands via `ree_commit.py --to-remote-tip`

`land_at_remote_tip()` (`ree_commit.py` line ~2564, 2026-08-18) builds the commit object on
the private index exactly as today, **does not** `update-ref` the local branch, fetches
origin, and:

- if `git diff --quiet <new_sha> origin/<branch> -- <paths>` is clean: prints
  `to-remote-tip: content already on origin -- nothing to push`, returns 0, and the commit
  object stays unreferenced. **No local commit, no orphan, no poison.** This is g8's case.
- otherwise cherry-picks `-x` onto origin's tip from a throwaway worktree and pushes;
  the local ref is untouched. No orphan either (this also removes the P4 amplifier: a
  wedged Mac stops manufacturing route-B orphans on every tick).
- on any non-success (fetch failure, lock contention, fatal conflict): falls back to
  today's local CAS commit, exit 1, "committed locally (fallback; not on origin yet)".

Change, in `scripts/igw_routine_tick.py::_ree_commit` only:

```python
if pushing:
    cmd += ["--push", "--to-remote-tip"]      # was: ["--push", "--retry-push-on-reject"]
```

(`--to-remote-tip` and `--retry-push-on-reject` are mutually exclusive by `ree_commit`'s
own argparse; `main()` sets `retry_push_on_reject = not to_remote_tip`.) The `committed`
detection string `"ree_commit: committed "` still matches (`committed <sha> ... [to-remote-tip:
not referenced by local HEAD]`), and `commit_ledger_files`' contract ("a COMMITTED entry
survives the spawned agent's rebase") is met more strongly: the entry is on origin, which is
what the agent's `pull --rebase` brings in.

This applies to all three `_ree_commit` callers (`commit_ledger_files`,
`commit_workset_files`, `_commit_proposals`); the two 2026-09-15 workset guards stay.

**One new hazard, and its mitigation, to ship in the same change.** Under the old flags a
SIGTERM at the tick's 240s ceiling after `update-ref` leaves a *referenced* local commit
(safe locally). Under `--to-remote-tip` a SIGTERM between `commit-tree` and the landing
leaves an **unreferenced** commit object, GC-eligible after `gc.pruneExpire`. The timeout
class is fixed (`chip-20260908-igw-tick-commit-ledger-push-retry-timeout`: zero TIMEOUT
lines since 2026-09-11T15:58Z vs 45 before), but the fallback must not depend on that:
`_ree_commit`'s `TimeoutExpired` handler already receives the child's partial stdout
(`exc.stdout`); parse the `ree_commit: committed <sha>` line and pin the sha with
`git update-ref refs/ree-rescue/igw/<sha> <sha>` (never a branch move; a rescue ref the
next tick or a human can land or drop), and say so in the log. ~15 lines, tested by
simulating `TimeoutExpired` with a canned stdout.

### 3.2 F-C (ship alongside): stop the CAS batch from lying about its no-op

`_coordinator_submit_cas` returns `"degraded"` for two different things: transport off /
verdict not applied (git path must run) and **content already equals origin** (nothing to
land anywhere). Split the second into `"noop"`, and in `_ree_commit` let a batch whose
outcomes are all in `{"suppressed", "noop"}` return without invoking `ree_commit` at all.
Corrects the false comment in place and saves one subprocess per tick. ~10 lines plus two
tests in `test_igw_routine_tick_cas_wiring.py` (existing `_RepoFixture`, bare remote).

### 3.3 Alternatives considered

- **F-B: an origin-tip identity guard inside `ree_commit.py`'s default path** (before
  building any commit, when `--push` is set: fetch, compare every named path's blob to
  origin's tip, no-op if all equal). Covers every caller, not just the tick -- but it is a
  second implementation of half of what `--to-remote-tip` already does, on the primitive
  every writer on every box runs through, with a new fetch on every commit. Held in reserve:
  if a second *caller* shows this shape after F-A, that is the trigger to generalise at the
  primitive, and the measurement to justify it will exist by then.
- **A route-D "tip-blob identity" proof in `ref_convergence.py`** (prove a commit when every
  blob it touched equals origin's tip blob and it touched nothing else). Exact, not the
  rejected reverse-apply heuristic -- but it is proof-after-the-fact for a commit that
  should not exist, it widens the one module CLAUDE.md item 4 fences, and prevention makes
  it moot. Not proposed; recorded so it is not re-derived.
- **Calling `_converge_after_push` from the "nothing to push" branch.** Would not help:
  the commit is still unprovable by routes A/B/C.
- **Extending the hub-ownership gate to the ledger.** Wrong: the ledger records the Mac's
  own spawns; there is no hub tick producing it.

---

## 4. Held-out check (GOV-HELDOUT-1)

Old = `--push --retry-push-on-reject` (commit locally, then try to push; on "already on
origin", keep the local commit). New = `--push --to-remote-tip` (build, land on origin's
tip, never move the local ref). Only cases where old and new give **different** calls count.
None of these was written from g8.

1. **g3, 2026-09-08, `aaec010637` / `4bb43c3523`** ("ledger+assignment entries present on
   origin"): old minted two unprovable orphans; new -> `content already on origin -- nothing
   to push`, no commit. **Different, and right.**
2. **g3, 2026-09-08, `17b4cea2ae`** (three files byte-identical to origin): same. **Different,
   right.**
3. **g7, 2026-09-15, `bff7ef166f`** (workset regen identical to origin): old minted the
   orphan that wedged the box; new -> no commit. Fix A now also prevents it, so today this is
   belt-and-braces; on 2026-09-15 morning it would have been the only defence. **Different,
   right.**
4. **2026-09-07 rebase-abort-loop class** (`chip-20260907-igw-workset-rebase-abort-loop`:
   Mac and hub both committed identical workset regens with identical subjects, 23
   recurrences since 07-29): under new the Mac's identical regen is a no-op vs origin and
   no local commit is created, so there is nothing for its `pull --rebase` to conflict on.
   The ownership gate has since removed it another way. **Different, right.**
5. **g3, 2026-09-08, `7efec49986`** (a GENUINE strand: five log lines committed locally when
   the push retry hit the 240s SIGTERM): old left a referenced local commit that a later
   audit cherry-picked upstream. New, without 3.1's rescue ref, could leave that content
   as an unreferenced object. **Different, and WORSE unless the rescue ref ships with it.**
   This is the case that puts the rescue ref in the plan rather than in a footnote.

Negative controls (old and new agree; listed to show the rule is not over-broad):
the four `EVB-1368` / `governance-flag` / `update-docs attestation` commits in the g8 range
carry content that was NOT on origin at commit time; both old and new land them via the
`-x` cherry-pick and both are proven by route B (ref_convergence lists all four as proven).

**Outcome: 4 differing cases with the right call, 1 differing case that exposed a hazard the
plan now covers. Passed, with a finding.**

**Counterweight, stated not skipped:** the check cost about an hour of reading across four
prior audits and two resolution notes; the rescue-ref addition is ~15 lines that would not
exist without case 5. Cheap relative to eight instance repairs, but not free.

---

## 5. What this does NOT fix (so it is not over-read)

- **P3-class deliberate strands** (a faithfulness refusal that correctly leaves a commit
  local, e.g. `rotate_workspace_state.py` on WORKSPACE_STATE.md, or the log.md
  "cannot be merged per-entry" refusals visible in the Mac tick log at lines ~12317/12350).
  Those are genuine strands with real content; they need the R5 wiring
  (`reconcile_wedge_content.py`), owned by `chip-20260911-wsrotate-push-refusal-strands-ahead`.
- **Other writers with the same shape.** F-A covers the IGW tick. `chip_ledger.py` and
  `task_claim.py` are coordinator-authoritative for their registries now and already carry
  the R1 remote-tip gate for their degraded path; no other Mac automation was found minting
  content-equals-origin commits in the g8 range (the `update-docs` attestation and
  `governance_flag` commits all proved). If one appears, F-B is the generalisation.
- **Clearing g8.** Section 7.

---

## 6. Tests and landing plan (only after the decision chip is answered)

- `scripts/test_igw_routine_tick_push.py`: assert the pushing command carries
  `--to-remote-tip` and not `--retry-push-on-reject`; assert non-pushing is unchanged.
- `scripts/test_igw_routine_tick_cas_wiring.py`: `"noop"` outcome; a `{suppressed, noop}`
  batch makes no `ree_commit` call; a `{suppressed, degraded}` batch still does.
- New `scripts/test_igw_ledger_commit_origin_wedge.py`, same bare-remote `_RepoFixture` shape
  as `test_igw_workset_commit_origin_wedge.py`: checkout one commit behind origin, ledger
  content equal to origin tip, CAS off -> `commit_ledger_files("update")` produces **no**
  local commit and the checkout is not ahead; ledger content NEW -> lands on origin, local
  ref untouched, `ref_convergence --check` clean.
- Rescue-ref test: simulated `TimeoutExpired` with stdout containing `committed <sha>` ->
  `refs/ree-rescue/igw/<sha>` exists.
- Run `scripts/run_scripts_tests.sh --changed` from the MAIN checkout (a worktree run is not
  a trunk verdict), then land on `REE_Working` master via `ree_commit.py --repo
  /Users/dgolden/REE_Working --push`. Verify on origin. Watch the next two natural launchd
  ticks (`~/Library/Logs/ree_igw_routine.launchd.log`) for `to-remote-tip` lines and confirm
  `git status -sb` in REE_assembly stops gaining `igw-ledger: update` ahead commits.

---

## 7. The g8 instance: audited and ready to clear (human-run)

Two Healer audits (03:40Z, 11:38Z) and this session's blob-level audit of the five unproven
shas agree: every ahead commit's content is on origin (byte-identical or, for the two
`failure_autopsy_V3-EXQ-964b` files, a strict subset of origin's later confirmed version).
`safe_adopt_ref.py` recomputes the discard set itself and refuses on any sha not listed, so
the command is safe to re-run after re-auditing anything new. As of 12:12Z (ahead 34):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/safe_adopt_ref.py --repo REE_assembly --branch master --allow-discard 866e30bcb8 97616b330c d44227cacf f4de99a7cf 08d076e4e5 89f1dcb867 c743b8aef7 3554bcb80e a5540f7cea 34fc176c33 89a6aea1d5 4d55341bfc f47c226c75 0e33c9eb5c b3f1519cd7 51ccb2869d 9a28bbcd6f 2d61dc89ea 5ebe63f304 f2195fc874 40073cdc59 483a61227c e9265760ee 6ca7bb3282 c40d454f64 ccdfa24d66 63a259910b fb48fb80c0 e18bd3d566 435c4e16ea bbeea9d72c 384c1e55c4 d605a540d9 5844f89d3a
```

Per `/metaworker-repair` Step 4 the ref move itself is human-run. Two live ` M` edits
(`evidence/decisions/decision_state.v1.json`, `evidence/experiments/INDEX.md`) are another
session's work and are untouched by the move. Until it runs, the Mac's REE_assembly tree
stays frozen at its 00:54Z revision and the wedge grows by one poison commit per
"update"-only tick.

---

## 8. Decision

Recorded as a `kind: decision` chip (ref in the closing report). Options: (1) proceed with
F-A + F-C + rescue ref as in sections 3 and 6; (2) constrain to F-C only (stops the
subprocess, does not stop the class -- a stale-base re-commit can still arise from a
non-CAS path); (3) proceed with F-B at the `ree_commit.py` primitive instead; (4) hold.
Recommendation: (1).
