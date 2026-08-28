# chip_ledger.py mutation-lock fail-open: is the sweep structural, or luck?

**Investigation chip:** `chip-20260827-chipledger-lockfailopen-sweep-investigation`
**Session:** `rc-chipledger-lockfailopen-49ee8a` (Remote Control, DLAPTOP), 2026-08-28
**Subject:** `scripts/chip_ledger.py`, LEDGER MUTATION LOCK block (added 2026-08-15)

---

## The question

The chip records that, twice in one session on 2026-08-27, the ledger mutation
lock's 180-second fail-open let one session's commit carry along another
session's uncommitted, brand-new chip entry. Nothing was lost either time. The
chip asks whether that benign outcome is a **property of the design** or a
**coincidence of timing**.

## Verdict

**Luck.** The benign "sweep" and a silent total loss come out of the *same*
fail-open window, and which one you get is decided by where the timed-out
waiter's read lands inside the live holder's mutation. Nothing in the code
prefers the benign branch, nothing detects the lossy one, and every process
exits 0 in both cases.

Qualified honestly: **no loss has actually occurred yet.** 1204 `chips: record`
commits on `origin/master` since the lock landed (2026-08-15) all name a
chip_ref the ledger still holds, and 126 chip_refs the Mac's tick logs claim to
have written are all present. The mechanism is live; the damage is not.

---

## Method

Four independent lines, deliberately not all of one kind:

1. **Code reading** of the lock, `mutate_and_commit`, `merge_origin_into_local`,
   `_recover_orphaned_ledger_write`, `atomic_write_text`.
2. **Reproduction** with real concurrent `chip_ledger.py` subprocesses, real
   `ree_commit.py` commits and real git repos in tempdirs
   (`evidence/planning/scripts/chipledger_lock_failopen_repro.py`).
3. **Production log forensics** on `~/Library/Logs/ree_hygiene_tick.launchd.log`
   (Mac-local, not version controlled).
4. **Real-history scans** of `origin/master`'s `TASK_CHIPS.json` for commits that
   changed a chip_ref their own message never names, and for record-commits
   whose named ref is absent from the ledger.

---

## Findings

### 1. The lock works. The control arm is clean.

Four concurrent `record` processes, lock at its shipped 180s wait: **6/6 trials,
0 losses, 0 sweeps, one commit per writer.** Repeated on a deliberately
push-wedged fixture: **4/4 trials, still clean.** The serialised path is not the
problem and should not be touched.

### 2. Force a fail-open into a LIVE holder and a brand-new chip is lost, silently.

The realistic shape is one holder plus waiters that timed out (`--wedged
--asymmetric`): **6/6 trials lost at least one chip from origin AND from the
working tree, with every process exiting 0.** Repeated at holder head-starts of
0.35s / 1.5s / 3.0s: **4/4 lost at every setting** — so it is not a knife-edge
coincidence, it is what happens whenever a waiter fails open into a live holder.

The worst observed variant, trial 0 of the asymmetric run: a commit whose
subject and `chips-mutated:` trailer both say `record chip-repro-000-w0`, whose
diff contains `chip-repro-000-w1` **and not `w0` at all**. The writer's own
content was clobbered off disk between its `atomic_write_text` and
`ree_commit.py`'s hash of that path, so it committed a stranger's entry under
its own message and exited 0.

Symmetrically forcing *all* writers unlocked (`--wait 0`, i.e. the pre-lock
state) reproduces the 2026-08-15 incident directly: 4 writers, 1 commit, 3 chips
gone, 6/6 trials. That arm exists as a positive control on the harness.

### 3. The real fail-opens happened, and they happened *because of the wedge*.

Four `PROCEEDING UNLOCKED` warnings in the Mac's hygiene-tick log, all on the
evening of 2026-08-27, all inside the window in which
`/Users/dgolden/REE_Working/master` had been **refusing convergence since
2026-08-27T07:25:32Z** (118 ahead at the time). The log shows the mechanism
inline: every mutation's `commit()` was hitting

```
ree_commit: push rejected: ... (non-fast-forward)
ree_commit: cherry-pick TRANSPLANT DETECTED for TASK_CHIPS.json ... Refusing to push.
ree_commit: push-retry 1/3: ... could NOT be proven to preserve the box's intended edit
```

i.e. a full push attempt, a throwaway-worktree cherry-pick and a structural
faithfulness proof over the whole ledger, *per mutation*. Holds stretched past
180s and the waiters fell out of the lock.

**This is the property that makes the design uncomfortable: the two failure
modes are correlated.** The lock holds exactly when the box is healthy, and
fails open exactly when the box is wedged — which is also when writers pile up,
retries multiply, and a lost chip is hardest to notice.

### 4. The timing budget the lock was sized against no longer holds.

`TASK_CHIPS.json` is now **10.0 MB** (1958 live rows). The LEDGER MUTATION LOCK
block, `merge_origin_into_local`'s cost note, and `atomic_write_text`'s
docstring all still reason about **3.9 MB** — a 2.6x drift, and the archive
command strips *fields* while keeping *rows*, so the row count only grows.

Measured on this box, one `record` against a copy of the real ledger:

| fixture | total | time to the disk write | write -> process exit |
|---|---|---|---|
| healthy | 14.66 s | 5.44 s | 9.22 s |
| wedged  | 15.92 s | 4.06 s | 11.86 s |

Two consequences:

* The **pre-write phase is ~30% of every mutation** (4-5 s of 15 s). That is the
  phase in which a concurrent unlocked writer's write-back destroys the holder's
  entry. It is not a millisecond window, and **every CAS retry re-enters it**
  (`MAX_COMMIT_ATTEMPTS = 3`).
* 180 s is **only about twelve queued mutations deep**. The design comment's
  "180s covers a queue of several serialized slow holders" was written for a
  cheaper mutation; a metaworker-dispatch cycle plus a wedge exhausts it, which
  is exactly what the log shows.

### 5. Sweeps are routine, not a two-off.

Scanning `origin/master` for commits that changed a chip_ref their own message
never names, 2026-08-26 to 2026-08-28: **9 of 695** ledger-touching commits.
Excluding two hand-authored `wedge-repair:` batch landings and one `strip 26
archived chip(s)` bulk command (which declares nothing *by design* — see the
DECLARING THE MUTATION SET block), **6 are genuine `chip_ledger.py` sweeps**:

| commit | message | undeclared refs carried |
|---|---|---|
| `9b773a57aa` | `record chip-strandedwt-dlaptop-...-85a9166` | 1 |
| `554a516f28` | `record chip-gitsyncverdict-dlaptop-ree-assembly` | 2 |
| `610e8b64d0` | `resolve chip-20260826-nav-assign-6-...` | 1 |
| `5793d9e0ac` | `claim chip-20260814-queue-causal-sleep-matched-arm` | 4 |
| `56e0e16ab7` | `record chip-20260826-ingress-dispatch-architecture-decision` | 1 |
| `34ace06b0b` | `record chip-strandedwt-dlaptop-...-85a9166` | 1 |

So the chip's "confirmed twice" understates it; the sweep is the ordinary
behaviour of an unserialised whole-file write-back on this box.

### 6. Nothing has actually been lost — checked two ways.

* Every one of **1204** `chips: record <ref>` commits on `origin/master` since
  2026-08-15 names a ref present in the current ledger. **0 missing.**
* Every one of **126** distinct chip_refs the Mac's tick logs claim to have
  written is present. **1 miss**, `chip-igw-20260810-232` — dated 2026-08-10,
  i.e. *before the lock existed*, and an IGW-path chip; not attributable here.

The second check matters because the first cannot see the worst repro shape: a
mutation whose commit never lands at all ("content already in HEAD", exit 0)
leaves no commit to scan.

---

## What IS structurally safe (do not over-read the verdict)

Three properties hold unconditionally and should not be re-litigated:

* **A swept entry is never half-written.** `atomic_write_text` (temp file +
  `os.replace`) means a reader sees the whole old file or the whole new one, and
  a chip row is only ever produced whole by `apply_fn`. CLAUDE.md's
  read-modify-write remedy (b) — "if it looks half-written, stop and flag it" —
  cannot be triggered by this path.
* **A swept entry is never dropped by the merge.** `merge_origin_into_local`'s
  `kept_local_only` bucket preserves a working-tree-only chip by design, and the
  function has no deletion path at all.
* **Skipping `_recover_orphaned_ledger_write()` when the lock was NOT taken is
  correct, and is not the defect.** Under the lock, `kept_local_only` implies a
  *dead* writer (no other mutation can be in its critical section), so
  committing it standalone is honest crash recovery. Unlocked, the same signal
  is ambiguous — the other writer may be alive and about to commit that content
  itself — and "recovering" it would race a live holder's CAS. The guard's own
  comment gives this reason and the reason is sound.

The loss is therefore **not** in the merge and **not** in the write. It is the
raw lost-update between two unserialised whole-file writers, which is precisely
what the lock exists to prevent and precisely what the fail-open reinstates.

## Why the two observed cases were benign

At the moment a waiter times out, the holder has been in its critical section
for at least 180 s. With a ~15 s mutation, a holder that old is overwhelmingly
likely to be stuck in the *post*-write phase — grinding through push rejection,
cherry-pick and the faithfulness proof — so the waiter reads a disk that already
carries the holder's complete entry and carries it along. That is the benign
sweep, and it is the *likely* branch.

It is likely, not guaranteed. A holder on a CAS retry is back in the pre-write
phase, and on a wedged box retries are the norm rather than the exception. The
observed outcome is the high-probability draw from a distribution whose other
tail is silent loss.

---

## The gap that makes the loss silent

**`claim` is the only mutating subcommand with post-commit verification.**
`verify_claim_on_origin()` re-fetches origin after the push and dies with a
dedicated exit code if the claim is not actually there. Its docstring already
states the general argument — "ree_commit.py's compare-and-swap guarantees the
commit is on the LOCAL branch; the push is a separate step".

`record`, `resolve`, `unclaim`, `attach`, `amend-prompt` and `declare-handoff` /
`verify-handoff` have **no equivalent check**. So the fail-open's entire
justification — quoted in the warning it prints, "refusing instead would lose
this command's own content" — is a property **nothing ever verifies**. In the
repro's worst variant the command lost its own content *and said it succeeded*.

The machinery to close this already exists, is small, and is production-proven
on the highest-stakes subcommand. It is not applied to the other six.

---

## Recommendations (chipped, not built here)

Chipped as `chip-20260828-chipledger-failopen-loss-fix` (urgent), because the
trigger condition — a ref wedge — is a recurring state on this box, not a
hypothetical.

1. **Post-write self-verification for every mutating subcommand.** After
   `commit()`, assert this call's own `mutated_refs` are present-and-as-intended
   in the resulting commit (local, cheap, always available), and separately warn
   if they are not yet on origin. Converts the silent exit-0 loss into a loud
   failure without changing the fail-open direction. Must distinguish "not on
   origin because the push was legitimately withheld, content safe locally" from
   "content is nowhere" — only the second is fatal.
2. **Do not fail open against a *live* holder.** The 180 s deadline fires
   regardless of whether anything still holds the lock; the warning it prints
   even tells a human to "check for a live chip_ledger.py". The code can make
   that check itself: with a live holder and a fresh lock mtime, keep waiting up
   to `LEDGER_LOCK_STALE_SECONDS`. Fail-open then fires only for a crashed or
   wedged holder — the case it was actually designed for — and the live-holder
   collision this document is about disappears entirely.
3. **Re-baseline the lock's timing comments against a 10 MB ledger**, and treat
   ledger *row* growth as a first-class cost: every mutation's pre-write phase,
   and therefore the vulnerable window, scales with it.
4. **Fix the wedge** (already owned by
   `chip-20260826-refwedge-class-recurrence-investigation`). It is the trigger
   for every fail-open observed. Not a substitute for 1 and 2 — a lock that is
   only safe on a healthy box is the finding, not the workaround.

A regression test belongs **with the fix**, asserting the loss does not happen.
The harness landed here demonstrates the defect and is deliberately kept out of
`scripts/` so `run_scripts_tests.sh` never collects a red-by-design file.

---

## Artifacts

* `REE_assembly/evidence/planning/scripts/chipledger_lock_failopen_repro.py` —
  the reproduction harness (control / pre-lock / real-shape arms).
* Real-history scans and the log cross-check are one-off scripts; their
  procedures and results are stated in full above so they can be re-derived.

## Held-out check (GOV-HELDOUT-1)

Not applicable: this document changes no standing rule, skill or workflow. It
records a measurement and chips a code fix. The rule-facing consequence — if any
— belongs to the fix chip, and should carry its own held-out check there.

---

## Addendum, 2026-08-28T06:35Z -- interaction with the remote-tip wedge gate

Recorded after the fact by the same session, from a handover by
`rc-remotetip-gate-20260828` (the session that owned `scripts/chip_ledger.py`
at the time and shipped the gate change). It **corrects the emphasis of
recommendation 4 above**, so read the two together.

Recommendation 4 said "fix the wedge; not a substitute for 1 and 2". That is
right but under-specified about *how much* of the exposure the wedge accounts
for. The owner's mechanism-level answer, which agrees with finding 3 and then
bounds it honestly:

* **What the gate change does.** `remote_tip_is_default()` in both
  `chip_ledger.py` and `task_claim.py` now gates on
  `_local_branch_is_ahead() and not _checkout_is_wedged()` (new module-level
  predicate, lazy-guarded `import ref_convergence`, reading the same
  `wedge_report()` entry point `--check` exits 4 on, failing closed to `False`
  on any "cannot tell"). On a wedged box every mutation currently takes
  push-reject -> cherry-pick -> faithfulness proof; the gate removes exactly
  that path, so hold times on a wedged box should collapse toward the unwedged
  case. Confirmed live on DLAPTOP at the time of writing: master ahead 43,
  8.3 h, `ref_convergence` reports wedged, and the new predicate returns True
  in both modules -- so the latch this removes was real on this box.
* **What it does NOT do, and this is the part not to lose.** It does not touch
  the 180 s bound, the 10.0 MB / ~15 s-per-`record` cost, the ~30% clobberable
  pre-write window, or the clobber mechanism itself. A busy *unwedged* box with
  enough queued mutations still reaches the timeout, and the reproduction above
  would still be 6/6. **It should cut the trigger RATE for one trigger. It
  changes nothing about the loss being reachable.**

**So the correct reading of finding 3 is now:** the wedge is very likely why all
four observed fail-opens landed inside it, and removing the wedge-driven latch
is worth having on its own -- but "no fail-opens observed" after this lands is
evidence about **how much of the exposure was wedge-driven**, not evidence that
the lock is safe. Recommendations 1 and 2 stand unchanged.

### Re-measurement this licenses (owned by this investigation, not by the fix)

Once the gate change is on `origin/master`, re-run the production half of the
method above and compare against this document's baseline:

```bash
/usr/bin/grep -c "PROCEEDING UNLOCKED" ~/Library/Logs/ree_hygiene_tick.launchd.log
```

Baseline here: **4**, all on 2026-08-27, all inside the wedge. A later count
that stays at 4 over a comparable busy period is the wedge-driven-exposure
result; a count that keeps rising on an unwedged box is direct evidence for
recommendation 2 (do not fail open against a live holder) and should be
attached to that chip. Note the log is Mac-local and rotating, so record the
observation window alongside the count rather than treating the number as
cumulative.

### Two testing notes handed over with it, both worth acting on

1. **A machine-state-dependent test existed and passed by luck.**
   `RemoteTipAheadGateTest` stubbed only `_local_branch_is_ahead`, so once a
   second predicate was added the class read the **real umbrella repo** and
   passed or failed depending on whether the box happened to be wedged. Now
   stubbed. Generalises: **when adding a predicate to one of these resolution
   paths, stub every predicate the path consults**, or the suite silently
   becomes a function of the machine it runs on.
2. **`python3 scripts/test_task_claim_remote_tip.py` reports "Ran 15 tests OK"
   where pytest collects 24 and fails one.** This is exactly the first vacuity
   trap CLAUDE.md documents for the umbrella corpus ("Do not build a runner on
   `python3 <file>`"), met in the wild on a file nobody had flagged. Use
   `scripts/run_scripts_tests.sh` from the MAIN CHECKOUT; a green script-exec
   run of that file is not a verdict. The one pytest failure needs attributing
   to pre-existing-vs-introduced before it is read either way.

---

## Second addendum, 2026-08-28T14:2xZ -- a DIFFERENT defect found while landing the above

Recorded by the same session. This is **not** the fail-open bug; it is a second
defect in the same file, found by accident while amending this investigation's
own chips, and it is tracked and owned elsewhere. It is noted here because a
reader of this document is exactly the person who needs to know it exists.

**Observed.** `d4a867e5` (13:43:19Z) landed an `amend-prompt` to
`chip-20260828-chipledger-failopen-loss-fix` -- that row's `prompt` 7961 ->
11081 chars. `fbf03cb0f` (13:45:33Z), a
`chips: recover orphaned working-tree write (crash recovery)` commit, silently
reverted it to 7961. Both exited 0. Nothing was lost (the content was still in
`d4a867e5`, restored structurally as `233c7332b2`), but the reverting commit
came from `_recover_orphaned_ledger_write()` -- the function added 2026-08-18
to *rescue* orphaned writes.

**Mechanism, confirmed by direct test.** `--to-remote-tip` (the default since
2026-08-23) cherry-picks the commit onto origin's tip in a throwaway worktree
and deliberately leaves the local checkout untouched, so it leaves disk
carrying content local HEAD lacks **by construction**:

```
DISK        prompt = 8725 chars   (carries the amendment)
local HEAD  prompt = 4930 chars   (does not)
git status --porcelain TASK_CHIPS.json  ->  " M TASK_CHIPS.json"
```

`_recover_orphaned_ledger_write()`'s stage-1 trigger *is* "disk differs from
HEAD". So on every remote-tip landing it fires on an ordinary healthy checkout
rather than on a crash, and hands the decision to stage 2's merge.

**Note the trap this created for the investigation itself**, since it is the
reusable lesson: an earlier hypothesis -- that `ree_commit.py`'s private-index
commit leaves the working tree un-updated -- was **refuted** by measuring a
blank `git status` after a mutation, and that refutation was correct *for the
path it measured*. There are **two landing paths**: local-landing (the
fallback) leaves `disk == HEAD`; remote-tip leaves `disk != HEAD`. Both
measurements were right; generalising from the first to all mutations was not.
**Anyone re-testing this must record which path the mutation took.**

**Scale, stated so it is not overread:** 11 crash-recovery commits exist in
`origin/master..master` (local-only, this wedged box); **1** of them reverted
committed content; **0** crash-recovery commits have reached `origin/master`
since 2026-08-18, so shared history is untouched. The framing that matters is
**trigger common, misfire rare** -- 1-in-11 is the *misfire* rate, not the
exposure, and the trigger is structural on every remote-tip write.

**Dated risk worth checking before any rate comparison:** the remote-tip wedge
gate (`f0eab5fc`, landed 2026-08-28T12:37Z) makes remote-tip the routine
landing path on wedged boxes, i.e. it plausibly increased the population of
`disk != HEAD` states fleet-wide about an hour before the observed misfire.
That is **not** a causal claim about this instance, and it is **not** an
argument for reverting that gate -- but do not compare misfire rates naively
across the 12:37Z boundary.

**Owner:** `chip-20260828-chipledger-noop-record-committed-destructive-delete`
(agreed with `ree-working-7f`), whose prompt now carries the full evidence, the
confirmed mechanism, the refuted hypothesis, and the two open questions --
should stage 1 exclude the remote-tip case by asking whether the diverged
content is already on origin, and why did stage 2's merge resolve toward the
stale side in the one case it did.
