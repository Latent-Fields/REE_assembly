# TASK_CLAIMS/TASK_CHIPS working-tree + index skew: root-cause clustering and a narrow durable fix

**Status: AWAITING USER REVIEW**

Session `metaworker-learning-taskclaims-skew-20260828` (DLAPTOP), 2026-08-28.
Skill: `/metaworker-learning`. Source chips (both open at time of writing):
`chip-20260826-taskclaims-mm-skew-recurrence-cloud4`,
`chip-20260827-taskclaims-contamination-recurrence-cloud5`.

**Nothing in `scripts/` was modified by this session.** This is a design, gated on
Step 4's decision chip per the skill's no-exception rule.

---

## 0. Summary

| the chips' framing | verdict |
|---|---|
| "4-6 data points" | **Undercount.** Both chip prompts were amended repeatedly after spawning; the real total is **10**. |
| "same symptom, maybe same root cause" | **Two distinct root causes**, both independently over threshold. Not one bug. |
| Remedy (a): make the fallback re-stage against new HEAD | **Already exists** (`refresh_shared_index`, `ree_commit.py:699`) and is not the gap. |
| Remedy (b): task_claim.py auto-repairs a provably-safe stale index | **Right instinct, wrong layer.** The repair belongs in `check_head_worktree_skew`, and a deliberate documented refusal blocks the task_claim.py version. |
| "occurrence C has a different proximate trigger" | **Confirmed**, but the trigger is not the root cause -- C shares Cluster 1's root cause. |

One-sentence root causes:

* **Cluster 1** -- the skew repair's own safety guard tests the wrong pair of
  trees, so the `MM` shape is **unrepairable by construction**, forever.
* **Cluster 2** -- `--to-remote-tip` accepts a persistent-dirty residual on a
  premise ("something else will fast-forward local HEAD") that is **false by
  definition on a wedged checkout**, which since 2026-08-28 is exactly where the
  mode is guaranteed to be selected.

---

## 1. Evidence base

Four independent, read-only sources. No repo state was changed.

1. **The chip prompts themselves**, read in full including all amendments -- the
   durable occurrence log (`TASK_CHIPS.json`).
2. **Direct source reading** of `ree_commit.py`, `task_claim.py`,
   `chip_ledger.py`, `safe_adopt_ref.py`, `ref_convergence.py`, `claim_rescue.py`,
   with every load-bearing claim re-verified by hand at the cited line.
3. **A live occurrence on this box**, observed unprompted during this session's
   own `task_claim.py open` (section 3).
4. **`logs/index_lock_forensics.jsonl`** (675 records) -- used to *exclude* a
   competing hypothesis (section 5.3).

---

## 2. The ten occurrences

| # | when (UTC) | box | file | INDEX | WORKTREE | repair applied by hand | cluster |
|---|---|---|---|---|---|---|---|
| O1 | 08-26 12:41 | cloud-4 | both | stale | stale | reset+checkout+ff-pull | 2 |
| O2 | 08-26 22:35 | cloud-4 | CLAIMS | -- | stale (1 entry `done`->`active`) | `checkout HEAD --` | 2 |
| O3 | 08-27 04:4x | DLAPTOP | CLAIMS | -- | stale, missing **12** entries (~7h) | `checkout HEAD --` | 2 |
| O4 | 08-27 18:43 | cloud-4 | CLAIMS | **stale** | == HEAD | `git reset --` (index only) | 1 |
| O5 | 08-27 20:43 | cloud-4 | both | **stale** | == HEAD | `git reset -q` (index only) | 1 |
| O6 | 08-27 21:22 | cloud-5 | CLAIMS | **stale** (71 vs 77) | replay, byte-identical to HEAD | `checkout HEAD --` | 1 |
| O7 | 08-27 21:29 | cloud-5 | CHIPS | **stale** | == HEAD | `git reset -q` (index only) | 1 |
| O8 | 08-27 21:39 | cloud-4 | CLAIMS | stale | stale, 5 behind, **0 unique** | `checkout HEAD --` | 2 |
| O9 | 08-27 21:42 | cloud-4 | CHIPS | **stale** | == HEAD | `git reset -q` (index only) | 1 |
| O10 | 08-28 06:40 | DLAPTOP | CLAIMS | == HEAD | stale, 2 behind origin, **0 unique** | left as evidence | 2 |

**An invariant holds across all ten: the working tree never carried content that
was not already on origin or HEAD.** Structural key-compare on `(session_id,
claimed_at)` showed zero unique worktree entries every time it was run (O6, O8,
O10 explicitly). No occurrence ever risked *losing* content. The risk was the
opposite -- silently *re-committing a stale snapshot* and dropping foreign
entries (O3: 12 entries; O6: 6 entries including a then-live ACTIVE claim
`hopeful-torvalds-28fb9a`).

That invariant is what makes a narrow automated repair possible at all, and it is
also why every hand repair was safe.

---

## 3. The live occurrence (O10), measured during this session

This session's own `task_claim.py open` landed via `--to-remote-tip`, printing
`to-remote-tip sha=83b636e2d2 (local checkout untouched)`. Immediately after:

```
 M TASK_CLAIMS.json
HEAD eb1cc28c19;  master...origin/master  [ahead 49, behind 117]
worktree vs HEAD : +10 lines  (this session's own claim)
index    vs HEAD : (empty)
TASK_CLAIMS.json entries -- worktree 65, HEAD 64, origin/master 67
structural key-compare: in origin but MISSING from worktree = 2
                        in worktree but NOT on origin       = 0
```

Ahead-commit composition: 21 `chips:`, 16 `claim:`, 4 `WORKSPACE_STATE`, 4
`recommendation`, 2 `TASK_CLAIMS.json`, 1 `session-land`, 1 `hooks` -- **37 of 49
(76%) minted by `chip_ledger.py` / `task_claim.py` themselves**, matching the
sibling refwedge investigation's independent finding.

This is the O8 shape reproduced live and smaller. It is the ` M` precursor state
that `ree_commit.py:2354-2371` documents as expected; it becomes `MM` the instant
anything moves HEAD by a bare ref move.

---

## 4. Cluster 1 -- the index fossil that no repair path can unstick

**Occurrences: O4, O5, O6, O7, O9 (5) -- threshold is 2.**
Signature: index stale; `git diff HEAD -- <path>` **empty** (worktree already
equals HEAD). Every one was repaired by hand with an index-only `git reset -q`.

### 4.1 Mechanism, verified

`check_head_worktree_skew()` (`ree_commit.py:968`) correctly *detects* an index
older than HEAD -- it diffs `--cached ... --diff-filter=M` at `:1000`. Detection
is not the gap. The gap is the verifier it then consults,
`_verify_stale_adoption()` (`ree_commit.py:829`), whose first clause is:

```python
# ree_commit.py:850-852
out, rc, _ = git(repo, "diff", "--name-only", "--", path, check=False)
if rc != 0 or out.strip():
    return None                      # (1) live unstaged work on top
```

`git diff -- <path>` with no revision compares the **working tree against the
INDEX**. In the `MM` shape that diff is non-empty *by construction* -- that is
precisely what the second `M` means. So:

* `git diff HEAD -- p` -> empty (worktree is correct)
* `git diff --cached HEAD -- p` -> non-empty -> `p` enters `mod_skew`
* `_verify_stale_adoption` -> `None` at `:852`
* `p` appended to `mod_unverified` (`:1045`), printed as *"staged modification(s)
  left UNTOUCHED"* (`:1058-1082`)
* **`mod_unverified` is deliberately excluded from the return value**
  (`:1059-1061`), so the function returns `True` -- "clean" -- with the staged
  revert still armed.

The same guard is mirrored at `_verify_deletion_skew` (`:935-937`) and
`repair_own_paths_after_converge` (`:1358-1361`), so **all three** repair paths
decline. The correct repair for this sub-case, `git reset -q -- <path>`, appears
in `ree_commit.py` **only as stderr advice text** (`:1080`, `:2556`) and is never
executed by any code path.

Consequence: once the index goes stale on a file that a whole-file writer keeps
rewriting, the state is a **fixed point**. Every automated repair refuses forever,
and only a human or a Healer running the advice by hand clears it. That is
precisely what happened five times.

### 4.2 Why the guard is right about the case it was written for

The guard is not a bug in general. `MM` genuinely *is* "someone's live work" in
the common case, and clobbering it would destroy uncommitted work. Two recorded
negative controls confirm this:

* `chip-20260820-maincheckout-hygienetick-skew` -- genuine never-committed WIP on
  `scripts/hygiene_routine_tick.py`; correct action was to do nothing, and at
  least two prior sessions independently reached that conclusion.
* `chip-20260819-mm-skew-repair-content-check` -- `MM` where the worktree half
  was **real appended work** on `steward_ledger.jsonl`; a blanket repair would
  have truncated it.

`MM`-is-never-repaired is additionally *pinned by four tests*
(`test_ree_commit_skew_modification.py:130`,
`test_pre_push_skew_modification.py:140`,
`test_hygiene_routine_tick.py:3346`, `test_ref_convergence.py:1555`).

**Any proposal here must survive both negative controls and keep all four green.**

### 4.3 The proposed change -- a strictly narrower predicate

The guard conflates two states that `git` can tell apart cheaply:

| | worktree vs index | worktree vs HEAD | is there anything to lose? |
|---|---|---|---|
| live work on a stale index | differs | **differs** | **YES -- never touch** |
| the fossil (O4/O5/O6/O7/O9) | differs | **EMPTY** | **NO -- worktree already == HEAD** |

Add one branch to `check_head_worktree_skew`'s modification loop
(`ree_commit.py:1041-1050`), *before* falling through to `mod_unverified`:

```
for p in mod_skew:
    if git diff --quiet HEAD -- p:        # worktree ALREADY equals HEAD
        git reset -q -- p                 # index only; worktree untouched
        -> record as `mod_index_only_repaired`, report it
        continue
    base = _verify_stale_adoption(...)     # unchanged from here down
```

Properties:

* **Provably lossless.** The repair runs only when the worktree is byte-identical
  to HEAD, so an index-only reset cannot discard anything: it makes
  index == HEAD == worktree.
* **Touches no file content**, ever. `git reset -q -- <path>` is an index
  operation. This is the same `D `/`M ` asymmetry CLAUDE.md already draws.
* **Strictly narrower than today's refusal** -- it repairs a proper subset of what
  is currently declined, and changes nothing else.
* **Needs no ancestry proof**, which sidesteps the documented
  `ANCESTRY_SCAN_COMMITS = 100` window (~12h on `TASK_CLAIMS.json` at ~218
  commits/day, per `chip-stagedskew-dlaptop-ree-working`) that makes the existing
  verifier fail on exactly the busiest files.
* **CLAUDE.md already prescribes this action.** Its `M `/`MM` three-way verdict
  says: *"Clear only the staged revert with `git reset -q -- "<path>"` (index
  only, worktree untouched)"*. The rule exists; the code does not implement it.

### 4.4 Held-out check (GOV-HELDOUT-1)

Old behaviour: **every** `MM` declined, no repair.
New behaviour: `MM` **where `git diff HEAD -- <path>` is empty** -> index-only
reset; all other `MM` unchanged.

Non-degeneracy requires old and new to give *different* answers.

| # | held-out case (not written from) | old | new | differ? | right call? |
|---|---|---|---|---|---|
| 1 | `WORKSPACE_STATE.md:160`, 2026-08-27T16:46Z cloud-4 -- reproduced 3/3 on push-retry commits; worktree byte-identical to new HEAD | declined; human ran reset | auto-repaired | **YES** | **Yes** -- identical to what the Healer did after verifying |
| 2 | `chip-stagedskew-dlaptop-ree-working` -- blob beyond the 100-commit ancestry window | declined (window exceeded) | repaired (no ancestry proof needed) | **YES** | **Yes** -- fixes the documented ~12h-window failure |
| 3 | `chip-20260814-convergence-skew-wedges-registry-writers` -- index holds a *foreign/pre-commit* blob, so `repair_own_paths_after_converge`'s "must be the blob this call hashed" gate declines | declined | repaired when worktree == HEAD | **YES** | **Yes** -- and strictly narrower than the broader proven-commit-set repair that chip deliberately **rejected** |
| 4 | `WORKSPACE_STATE.md:1145`, 2026-08-25T18:19Z -- *"Worktree already == HEAD, so `git reset -q -- TASK_CHIPS.json` was lossless"* | declined; human ran reset | auto-repaired | **YES** | **Yes** -- the session states the safety argument in the same terms |
| N1 | `chip-20260820-maincheckout-hygienetick-skew` -- genuine uncommitted WIP | no repair | **no repair** (worktree != HEAD) | no (degenerate) | negative control **passes** |
| N2 | `chip-20260819-mm-skew-repair-content-check` -- real appended work on `steward_ledger.jsonl` | no repair | **no repair** (worktree != HEAD) | no (degenerate) | negative control **passes** |
| N3 | `test_ree_commit_skew_modification.py:130` -- worktree holds `"MY LIVE UNCOMMITTED WORK"` | no repair | **no repair** (worktree != HEAD) | no (degenerate) | test **stays green** |

**Four non-degenerate differing cases, all giving the right call; three negative
controls, all correctly excluded.** This clears the >=3 bar without needing the
escape hatch.

**The honest counterweight, not dropped:** this check cost roughly 40 minutes of
a session that had already done the mechanism work, and it was affordable only
because the case corpus already existed in `TASK_CHIPS.json` resolution notes and
`WORKSPACE_STATE.md`. It also changed the design -- the first draft would have
repaired `MM` on a structural key-compare proof, which N2 falsifies. Recording
that as one GOV-HELDOUT-1 data point: **the check caught an over-broad rule before
it shipped.**

### 4.5 Tests the change would need

Alongside `scripts/test_ree_commit_skew_modification.py` (real git repos in
tempdirs, time-independent, matching that file's existing conventions):

* the fossil is repaired when worktree == HEAD, worktree byte-unchanged after;
* `test_live_unstaged_edit_on_top_is_never_repaired` still passes verbatim;
* a `steward_ledger.jsonl`-shaped append (N2) is **not** repaired;
* the repair fires with **no** reachable ancestor blob (the O4/O5/O7/O9 shape,
  where the staged blob is a local orphan's);
* `check_head_worktree_skew` return value semantics unchanged for every other shape.

---

## 5. Cluster 2 -- the stale worktree on a checkout that cannot fast-forward

**Occurrences: O1, O2, O3, O8, O10 (5) -- threshold is 2.**
Signature: the worktree holds a snapshot older than origin, with zero unique content.

### 5.1 Mechanism, verified

`land_at_remote_tip()` (`ree_commit.py:2300`) documents its own residual as **THE
PERSISTENT-DIRTY TRADE** (`:2354-2371`): on success the shared index and HEAD are
untouched, so the path shows ` M`

> "until something ELSE next fast-forwards local HEAD past this push (a plain
> `git pull`, /session-land housekeeping, a later ordinary commit)."

`main()` returns at `:3590`, above both `refresh_shared_index` (`:3618`) and
`check_head_worktree_skew` (`:3624`); the two success returns inside
`land_at_remote_tip` (`:2419`, `:2427`) call neither. Only `_fallback` does
(`:2396-2397`) -- **the failure path is defended and the success path is not.**

**The resolution premise is false on a wedged checkout.** A wedged checkout is
*defined* by being unable to fast-forward, so the event the residual waits for
cannot occur. The only HEAD advance available is a bare `update-ref` via
`safe_adopt_ref.py:405`, which moves the pointer and leaves index and worktree
behind -- converting ` M` into `MM` (Cluster 1's input) or, across a range, into
the several-commits-behind worktree of O3/O8.

### 5.2 The interaction with R1, which landed today

The trade was accepted when `--to-remote-tip` was **opt-in**, and its own
docstring defers the question: *"recorded so a future caller-side integration
(task_claim.py / chip_ledger.py) can weigh it explicitly rather than discover
it."* The mode became the **default** for both writers on 2026-08-23
(`chip-20260823-remotetip-flip-ledger-writer-defaults`); that flip's record does
not appear to contain the deferred weighing.

R1 (`chip-20260828-remotetip-gate-ahead-and-not-wedged`, landed today) then
extended the gate so remote-tip stays **ON when wedged**. R1 is correct on its own
terms -- it breaks the latch that made the ahead-count grow. But it also means the
persistent-dirty residual is now **guaranteed on exactly the checkouts
structurally unable to absorb it**.

> **Falsifiable prediction, recorded as one.** Cluster-2 occurrences per box-day
> **rise** after 2026-08-28 unless the residual is addressed, even as the wedge
> *cost* metrics R1 predicts improve. Re-measure on R1's own ~7-day check
> (`refwedge_class_recurrence_investigation_20260826.md` section 9 item 5). If
> Cluster-2 frequency is flat or falls, this analysis is wrong and should be
> revised, not defended.

### 5.3 One hypothesis excluded

`refresh_shared_index()` has a loud give-up path that writes an
`event: "blocked"` forensics record when `.git/index.lock` defeats it. On DLAPTOP,
`logs/index_lock_forensics.jsonl` holds **675 records and zero `blocked` events**
(326 `cleared`, 349 `first_sighting`). So lock contention did **not** produce the
DLAPTOP occurrences. *Evidence gap, stated rather than papered over:* the cloud
boxes keep their own logs and were unreachable from here (WireGuard tunnel down),
so O4/O5/O7/O9 were not checked this way.

### 5.4 Recommendation for Cluster 2: HOLD, do not build yet

Three reasons, none of them "it's fine":

1. **R1 landed hours ago and changes this cluster's dynamics.** Building a second
   fix on top of an unmeasured one risks attributing R1's effect to this change,
   or vice versa. The 7-day re-measure already exists; use it.
2. **`scripts/task_claim.py` is claimed right now** by `rc-remotetip-gate-20260828`
   for the R1 work. The obvious remedy touches that file.
3. **The chips' remedy (b) collides with a documented, reasoned refusal.**
   `task_claim.py:946-977` and `chip_ledger.py:1608-1618` both deliberately
   *decline* to auto-repair skew, on the grounds that a claim helper silently
   mutating a high-contention shared file at startup is a new hazard in its own
   right -- and both scope that refusal to the *deleted-path* case, where the
   repair is unconditionally safe. Cluster 1's fix is compatible with that policy
   (it changes no file content, and lives in `ree_commit.py`'s post-commit guard,
   not in a registry helper's startup path). A Cluster 2 fix that rewrites the
   worktree is **not**, and needs its own argument rather than inheriting Cluster
   1's.

The existing **stale-read guard is already doing the load-bearing safety work** for
Cluster 2: it refused correctly in O2, O3 and O8 and prevented every threatened
data loss. What it does not do is repair, so the checkout stays dirty until a
human or Healer intervenes. That is a real cost, but it is a *toil* cost, not a
correctness one -- which is why it can wait for a measurement.

---

## 6. What was deliberately not done

* **No `scripts/` file was modified.** Both clusters are designs pending Step 4.
* **The live DLAPTOP skew (O10) was left exactly as found**, as evidence,
  consistent with how the sibling refwedge investigation handled its wedge.
* **No unified fix was forced.** The launch prompt explicitly warned against this
  and it would have been wrong: the two clusters have different mechanisms,
  different layers, and different risk profiles.
* **Agent 1's proposed "smallest correct fix" was rejected on inspection** --
  calling `refresh_shared_index()` on `land_at_remote_tip`'s success returns.
  `git reset -q -- <p>` resets the index *to HEAD*, and on that path HEAD has not
  moved, so the index is already at HEAD and the call is a **no-op** in the
  dominant case. The `MM` is created later, by the bare ref move. The fix belongs
  at the repair site (Cluster 1), not the remote-tip site. It would help only a
  pre-existing-fossil sub-case.
* **No change to `ref_convergence.py`'s refusal semantics** and no third proof
  route -- out of bounds, and still correctly rejected in that module's docstring.

---

## 7. Recommended follow-on

1. **Decision chip for Cluster 1** (Step 4, this session) -- the narrow
   index-only repair. Recommendation: **proceed**.
2. **Cluster 2: hold and re-measure** on R1's existing 7-day check, with the
   section 5.2 prediction recorded as a falsifier.
3. **A `/metaworker-repair` procedure gap, worth its own chip:** the Healer skill
   that keeps *finding* this at cycle start has no documented procedure for it.
   The verify-then-`git reset --` recipe currently lives only in
   `WORKSPACE_STATE.md` prose and individual chip resolution notes, which is why
   it was re-derived by hand at least five times.
