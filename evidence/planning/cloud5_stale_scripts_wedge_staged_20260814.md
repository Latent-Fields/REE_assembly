**Status: AWAITING USER REVIEW.**

# ree-cloud-5 shared-checkout wedge: why a landed guard never ran, and the verified repair

Session: `metaworker-chip-20260814-cloud5-stale-scripts-disabled-orphan-guard` (headless
metaworker chip, dispatched on `ree-cloud-5`).
Chip: `chip-20260814-cloud5-stale-scripts-disabled-orphan-guard`.
Written 2026-08-14T20:19Z. All measurements taken on `ree-cloud-5`
(`/home/ree/REE_Working`, reached as `/Users/dgolden/REE_Working` via the `/Users/dgolden
-> /home/ree` symlink).

**The repair itself was NOT performed. It is permission-gated and needs an authorised
operator — see "The repair" below. Everything needed to execute it safely, including the
content-loss audit and a backup branch, is done and recorded here.**

---

## 1. The finding, in one paragraph

`chip-20260814-taskclaim-close-orphan-guard` landed the orphaned-close push guard on
2026-08-14 (`REE_Working` `ffe127d779`: `entry_is_orphaned` + `make_orphan_push_gate`, 14
differential tests). It is correct and it is on `origin/master`. It has never executed on
the box that needs it. `ree-cloud-5`'s shared umbrella checkout — the dispatch box for
every headless metaworker chip, and the tree whose `scripts/*.py` every chip session
invokes by absolute path — is wedged behind origin and **cannot converge**, so its working
copy of `scripts/task_claim.py` is frozen at a pre-guard revision. This is a **deployment
failure, not a logic failure**, and it has a property that makes it much worse than
ordinary staleness: **the wedge is self-sustaining, and no change landed on `origin` can
ever reach a wedged checkout.** That last clause is why the obvious code-level fixes are
all circular (§4).

## 2. Measured state

| measurement | value |
|---|---|
| `master` vs `origin/master`, 20:02Z | `[ahead 228, behind 360]` |
| same, 20:19Z (17 min later) | `[ahead 233, behind 365]` |
| `git merge-base --is-ancestor ffe127d779 HEAD` | **NO** |
| `grep -c entry_is_orphaned scripts/task_claim.py` (worktree) | **0** |
| same, `git show origin/master:scripts/task_claim.py` | 15 |
| `scripts/task_claim.py` diff, local -> origin | +399 / -9 |
| `scripts/chip_ledger.py` | +133 / -3 |
| `scripts/ree_commit.py` | +127 / -4 |
| `ref_convergence.py --dry-run` | **refuses**: 43 of 228 ahead commits unproven |

The +5 ahead in 17 idle minutes is the spiral running live.

**Live reproduction of the incident's precondition.** This session's own
`task_claim.py open` at 20:02:22Z failed to push, and `task_claim.py`'s post-commit
self-check reported it verbatim: `[origin/master] no entry for session_id
metaworker-chip-20260814-cloud5-stale-scripts-disabled-orphan-guard claimed_at
2026-08-14T20:02:22Z ... this open did not land, so nothing is protecting the claimed
resources`. That is exactly the state in which the 19:53Z corruption occurred: an `open`
absent upstream, followed later by a `close` whose push-retry transplants onto whatever
entry the context diff happens to match.

## 3. Mechanism — a closed causal loop

1. The checkout is behind origin, so **every** push of a registry commit
   (`TASK_CLAIMS.json`, `TASK_CHIPS.json`) is non-fast-forward and is rejected.
2. `ree_commit.py`'s `retry_push_via_worktree()` cherry-picks the caller's own HEAD onto
   `origin/master` in a throwaway worktree. (Verified: this box's copy *does* already pass
   `-x` and *does* call `_converge_after_push` — so route B is armed. The stale copy is not
   the cause of step 3; the divergence is.)
3. Against a whole-file JSON registry whose two histories are 365 commits apart, that
   cherry-pick has two bad outcomes and no good one:
   - **conflict** -> aborted, `fatal`, content **stranded**; or
   - **applies as a context diff against the wrong entry** -> the transplanted closure.
     This is the 19:53Z corruption: origin `7241ae05` marked a live sibling session's
     ACTIVE claim (`metaworker-chip-20260814-queue-causal-sleep-matched-arm`) `done` under
     a foreign `completion_note`.
4. Either way the local commit remains on `master` -> **+1 ahead**.
5. A *stranded* commit has no upstream patch-id (route A fails) and no upstream
   `(cherry picked from commit ...)` backref (route B fails), so it is **permanently
   unprovable**.
6. `_converge_after_push()` requires **every** discarded commit to be proven — "partial
   proof is not proof", correctly. One permanently-unprovable commit therefore **refuses
   the ref move forever**.
7. The ref never moves -> the checkout stays behind -> go to 1.

**Differential confirmation, same box, same minute, same tooling.** Pushing this very
artifact to `REE_assembly` — which was independently diverged at `[ahead 27, behind 75]`
on `ree-cloud-5` — went through the identical rejected-push -> cherry-pick-retry path and
then **converged automatically**: `_converge_after_push()` proved all 27 ahead commits,
`safe_adopt_ref.py` moved the ref, and the post-move skew repair discarded 16 staged
reverts and ~30 staged deletions. `REE_assembly` is now `## master...origin/master`, clean.
So the machinery is not broken and the box is not at fault — the umbrella repo's refusal is
caused *specifically* by its stranded, permanently-unprovable commits. That isolates the
cause to step 5 below and rules out the alternatives.

**The load-bearing asymmetry:** orphans accrue continuously, but proof is all-or-nothing.
A single stranded commit converts a transient divergence into a permanent wedge. After
that, `scripts/` is frozen at whatever revision HEAD held at that moment, and **every guard
landed after that date is silently undeployed on the dispatch box** — which is precisely
what happened to `ffe127d779`.

The refusal is not hidden — `ref_convergence` prints it — but it goes to stderr in a
headless session log nobody reads, and `_converge_after_push` is deliberately fail-open, so
nothing escalates. **The wedge is loud once and then silent forever.**

## 4. Why the three options in the chip brief do not all work

- **(a) Converge the checkout and keep it converged — CORRECT, and the only one that can
  work.** Blocked on authorisation, not on knowledge; §5 and §6.
- **(b) Have the dispatcher resolve `scripts/` from a fresh worktree at `origin/master`
  per session — CIRCULAR.** The dispatcher is itself repo code living on the wedged box.
  Landing it on `origin` does not deploy it.
- **(c) A start-of-session staleness assertion — CIRCULAR, for the same reason.** The
  assertion would live in a file the wedged checkout never receives. Compare
  `audit_worktree_skills.py`, which the brief rightly points at: that one works because
  its delivery channel (`.claude/settings.json`, gitignored, pushed out by
  `sync_worktree_settings.py`) is *outside* the frozen tree. There is no equivalent
  out-of-band channel for `scripts/`.

**General statement, and the reusable lesson: no change landed on `origin` can take effect
on a checkout that is wedged behind `origin`.** The wedge must be cleared out-of-band
first. A corollary worth stating plainly, because it bounds what this class of chip can
ever achieve: **a headless session running on the wedged box cannot ship the fix for its
own wedge.** (b) and (c) remain worth building — but strictly as *recurrence* prevention,
after (a), and they must not be mistaken for a fix to the current incident.

## 5. Content-loss audit — the discard is verified safe

> **This section is the MANDATORY method, not a courtesy this session happened to perform.**
> Before any sha is acknowledged with `safe_adopt_ref.py --allow-discard`, every unproven
> commit must be audited **by content**, per-commit. A **shape** argument — "these are
> `TASK_CHIPS`/`TASK_CLAIMS` bookkeeping, i.e. the known `ref_convergence` false-negative
> shape, therefore they are content-safe" — is **not** a content check and must never stand
> in for one. The inversion is the bug: the whole-file-JSON shape explains why route A
> **cannot prove** a commit; it says nothing about whether that commit's content reached
> origin.
>
> **This was measured, twice, with opposite results.** 2026-08-14 on the `ree-cloud-5`
> umbrella: 42 of 46 ahead commits proved and all four refusals were verified false
> negatives — zero stranded. 2026-08-15, same box, same repo: of 33 unproven, **15 (45%)
> were genuinely absent from origin** (7 whole `TASK_CLAIMS` entries + their 8 open/close
> commits, a chip resolution origin still showed `open`, and 50 of 53 lines of a
> `WORKSPACE_STATE.md` block). The decision chip
> `chip-20260815-cloud5-umbrella-reconverge-authorised` had asserted "all 32 are
> content-safe to discard" on exactly the shape argument above; executed as written it would
> have dropped those 15 permanently, the local branch being their only copy. A third,
> earlier audit (2026-08-14T07:45Z, same backlog) had already found 3 of route A's 10
> refusals stranded. **Treat a refusal as roughly a coin flip.** Full record:
> `REE_Working` `WORKSPACE_STATE.md` 2026-08-15T19:46Z (`aa40abe94c`) and `CLAUDE.md`
> Session Startup Protocol step 4.
>
> The audit is cheap — roughly 40 lines of python, minutes of wall clock, and on 2026-08-15
> it separated 15 stranded commits from 18 false negatives. The recipe is at the end of this
> section.

Convergence discards the local ahead commits. Every one was checked, and **nothing of
substance is lost**:

- **`TASK_CHIPS.json`** — local 664 entries, origin 664, **zero** `chip_ref` keys present
  only locally. Fully upstream.
- **All non-registry paths touched by any ahead commit** — the union is
  `CLAUDE.md`, `WORKSPACE_STATE.md`, `scripts/ree_commit.py`, `scripts/ref_convergence.py`,
  `scripts/test_ref_convergence.py`, `scripts/hygiene_routine_tick.py`,
  `scripts/check_deferral_exit.py`, `scripts/install_literature_commit_gate.py`,
  `scripts/test_*` and the two `governance/SKILL.md` copies. Each was diffed local-vs-origin
  line by line. `ref_convergence.py`, `test_ref_convergence.py` and the untouched-on-origin
  files have **zero** local-only lines (origin is a strict superset). The handful of
  local-only lines in `ree_commit.py`, `CLAUDE.md`, `hygiene_routine_tick.py` and
  `WORKSPACE_STATE.md` were each confirmed to be **earlier revisions of text origin has
  since expanded**, not lost content — e.g. `def retry_push_via_worktree` and
  `def _converge_after_push` both exist on origin with changed signatures, and the
  `WORKSPACE_STATE.md` `2026-08-14T05:35Z` Recent Work entry is present on origin verbatim.
- **`TASK_CLAIMS.json`** — 34 `(session_id, claimed_at)` keys exist only locally:
  - **30 dated 2026-08-13** — already pruned from origin by `prune_task_claims_done.py`
    (done entries older than 24h). Discarding them is correct; re-landing them would be
    wrong.
  - **3 dated 2026-08-14, status `done` with real completion notes** —
    `metaworker-chip-20260814-deferral-detector-worktree-path-misresolve` (14:08:48Z),
    `...-lit-cache-poisons-on-transport-failure` (09:21:29Z), and
    `metaworker-chip-ledgerint-claimnote-chip-20260814-converge-diverged-umbrella-oneoff`
    (07:59:34Z). Their *work* landed (the notes name landed commits in other repos); only
    the closure record is local-only. Small audit-trail loss, and they fall out of the
    24h prune window on 2026-08-15 anyway.
  - **1 active claim** — this session's own (20:02:22Z). Must be re-opened after the move.

A backup branch preserving all of it already exists on the box and costs nothing to keep:

    backup/pre-converge-20260814T2015Z  =  31294d65

### 5a. The audit recipe (reusable; this is what the §5 bullets above were produced by)

For each unproven sha, compare what the commit **added** against origin's current copy of
the same path. Compare **identity keys**, never the textual diff — a re-serialised whole-file
JSON diff is noise, and the commit SUBJECT grepped against the file body is how one earlier
session got this wrong.

| Path | Identity key to compare |
|---|---|
| `TASK_CLAIMS.json` | `(session_id, claimed_at)` per entry |
| `TASK_CHIPS.json` | `chip_ref` per entry |
| `WORKSPACE_STATE.md`, `CLAUDE.md`, other prose | the set of **added lines** (`git show <sha>` `+` lines), stripped and compared as a set |
| executable code | added-line set, then read the residue by hand — an "absent" line is often an earlier draft origin has since rewritten |

The three revisions to read per sha are `git show <sha>^:<path>` (before), `git show <sha>:<path>`
(after), and `git show origin/<default>:<path>` (origin now). The commit's contribution is the
key-set difference between the first two; it is **upstream** iff every one of those keys is
present in the third.

```python
# sketch: TASK_CLAIMS.json / TASK_CHIPS.json, run from the repo root
import json, subprocess
def show(rev, path):
    return json.loads(subprocess.run(["git","show",f"{rev}:{path}"],
                                     capture_output=True, text=True, check=True).stdout)
def keys(doc, kind):
    items = doc["claims"] if kind == "claims" else doc["chips"]
    return {(i["session_id"], i["claimed_at"]) if kind == "claims" else i["chip_ref"]
            for i in items}
def verdict(sha, path, kind, default="origin/master"):
    added = keys(show(sha, path), kind) - keys(show(sha + "^", path), kind)
    missing = added - keys(show(default, path), kind)
    return ("UPSTREAM" if not missing else "STRANDED"), sorted(missing)
```

Three outcomes, and the middle one is the trap:

- **UPSTREAM** — every added key is on origin. Route-A false negative; safe to `--allow-discard`.
- **DIFFERS but origin is NEWER / strictly AHEAD** — the key is there but the entry has moved on
  (already closed with a real completion note, or deliberately unclaimed later). **Not stranded,
  and re-landing it would REVERT origin.** `676903c6d0` (2026-08-14) is the worked example: route A
  proved it, the content check flagged it, and re-applying it would have re-claimed a chip a later
  origin commit had deliberately released. A flag must be diagnosed, never acted on directly.
- **STRANDED** — genuinely absent. Land it before the move: `git cherry-pick -x` oldest-first from a
  throwaway worktree at `origin/<default>`, resolving whole-file JSON conflicts by re-applying the
  commit's **structural** intent (the added/changed entry) onto origin's current content, never by
  taking a side. The `-x` backref then lets route B prove it, so convergence may clear by itself.

## 6. The repair (needs an authorised operator)

Attempted this session and **blocked by the harness permission classifier** — correctly:
discarding 233 local commits on a shared checkout is exactly the irreversible class that
should need a human. Run from `/home/ree/REE_Working` on `ree-cloud-5`:

> **PRECONDITION, not optional: §5's per-commit content audit must have been re-run against
> the CURRENT `origin/<default>` before this command.** The `--allow-discard $(git rev-list ...)`
> form below acknowledges every ahead sha in one shot, so it is only as safe as the audit
> behind it — and on 2026-08-15 an unaudited version of exactly this command would have
> destroyed 15 genuinely-stranded commits. Land the STRANDED ones first (§5a), then discard
> only what the audit proved upstream or proved superseded-by-origin. If hours have passed
> since the audit, re-run it: origin moves.

```bash
BASE=/home/ree/REE_Working
cd "$BASE"
git branch backup/pre-converge-$(date -u +%Y%m%dT%H%MZ) master   # (one already exists)
git fetch -q origin master
/opt/local/bin/python3 scripts/safe_adopt_ref.py --repo "$BASE" --branch master \
  --allow-discard $(git rev-list origin/master..master)
```

`safe_adopt_ref.py` independently recomputes the discard set and refuses (exit 3) on any
sha not acknowledged, so a commit landing between the `rev-list` and the move aborts the
operation rather than being silently dropped — re-run if that happens. It performs the
mandatory narrow post-move HEAD/worktree skew repair itself, which is what materialises
the current `scripts/` onto disk.

**Acceptance check, in order:**

```bash
grep -c entry_is_orphaned scripts/task_claim.py          # expect 15, currently 0
git merge-base --is-ancestor ffe127d779 HEAD && echo DEPLOYED
/opt/local/bin/python3 scripts/test_task_claim_close_orphan_guard.py   # expect green
```

Then re-open any claim lost by the move (this session's, if still active), and optionally
re-append the three 2026-08-14 `done` entries from §5 for the audit record — via a
throwaway worktree at `origin/master`, **not** via `task_claim.py`, since its push-retry is
the mechanism under repair.

## 7. Recurrence prevention (chip-worthy; do NOT attempt before §6)

1. **Escalate a permanent wedge.** The real defect is that one stranded commit refuses
   convergence forever while the refusal is a single stderr line in a log nobody reads.
   `ref_convergence` should distinguish transient from permanent — e.g. surface a signal
   when the ahead count exceeds a threshold or refusal has persisted past N hours — so the
   wedge is *durably* visible rather than loud-once-then-silent. This is the highest-value
   follow-on.
2. **Refuse to dispatch from a stale checkout.** Options (b)/(c) from the brief, as
   *recurrence* prevention only: the metaworker dispatcher should compare its `scripts/`
   against `origin/master` before spawning chip sessions and refuse (or converge) rather
   than spawning sessions that will silently run frozen guards.
3. **Reconsider whole-file JSON registries under cherry-pick retry.** Step 3 of §3 has no
   good branch. A retry that can either strand content or transplant it onto a neighbouring
   entry is not a safe recovery path for `TASK_CLAIMS.json`; the orphan guard patches the
   worst symptom but the underlying "apply an append as a context diff" mechanism remains.

## 8. What this session did and did not do

**Did:** diagnosed the mechanism with live measurements; reproduced the incident's
precondition on itself; audited every ahead commit for content loss and found the discard
safe; created the backup branch `backup/pre-converge-20260814T2015Z` (`31294d65`); wrote
this artifact.

**Did not:** move the ref (permission-gated); therefore did **not** deploy the guard and
did **not** meet the chip's behavioural acceptance test, which is unreachable from a
session running on the wedged box. The chip is left open.
