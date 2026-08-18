# Umbrella ref-convergence wedge: why it RECURS (2026-08-18)

**Status: diagnosis + shipped fix. The fix (route C) is code in `scripts/ref_convergence.py`;
this file is the evidence behind it. Nothing here was written to `claims.yaml`.**

Chip: `chip-20260818-dispatch-registry-commit-rate-wedges-umbrella`.
Measured on `DLAPTOP`, `/Users/dgolden/REE_Working` (umbrella), `master`, 2026-08-18T07:2xZ,
during a continuously-running interactive metaworker-dispatch loop. Load average at the time
was **389** (31 concurrent `claude` processes) -- every git operation was slow, which is context
for the numbers, not a cause of the wedge.

## 1. The recurrence is real: four clearings in one morning

| time (UTC) | state | cleared by |
|---|---|---|
| ~03:59 | `[ahead 38, behind 44]`, 17 unproven | dispatched worker |
| ~04:57 | `[ahead 29, behind 71]`, 9 unproven | dispatched worker |
| ~06:49 | `[ahead 17]`, 10 unproven, 6 refusals | dispatched worker |
| ~07:28 | `[ahead 26, behind 67]`, 11 unproven | dispatched worker (during this session) |

Between clearings it rebuilds steadily (~15-20 commits/hour), it does not spike.
`--check` at 07:22Z: `severity=wedged`, `first_refused_at=05:54:51Z`, `refusal_count=8`.

## 2. Composition: 100% coordination bookkeeping

All 26 ahead commits at the 07:28Z wedge were authored `REE Automation (Mac)` and were
`chip_ledger.py` (`record`/`claim`/`resolve`/`amend-urgency`) or `task_claim.py`
(`open`/`close`) writes. Files: `TASK_CHIPS.json`, `TASK_CLAIMS.json`, `WORKSPACE_STATE.md`.
This part of the chip brief is confirmed unchanged.

## 3. WHAT THE BRIEF GOT WRONG, and it matters for the fix

The brief's model was: non-fast-forward push -> `retry_push_via_worktree` -> orphan duplicate
-> unproven ahead commit. That is only a **minority** of the mechanism here.

Measured over the 26 ahead commits (`git cherry` + `-x` backref scan over `master..origin/master`):

| | count |
|---|---|
| proven by route A (patch-id) | 8 |
| proven by route B (`-x` backref, i.e. really did go through push-retry) | 1 |
| **unproven** | **17** |

Of the 18 route-A-unproven commits, **17 carried NO `-x` backref on origin**. So they did not
land via the push-retry path at all. A per-commit content audit (parse the JSON, compare item
sets keyed by `chip_ref` / `(session_id, claimed_at)`) shows why:

* **13 of 18 have their content fully on origin already.** It got there inside a *different*
  session's whole-file read-modify-write. Worked example: local commits `ff5ede09`, `b7676333`,
  `c535b09b`, `f05acf56` (4 separate bookkeeping commits) correspond to a single upstream commit
  `266f2378` "stash triage 93c953009a: close claim, resolve chip, record 2 follow-on chips".
  One upstream commit, four local ones -> **no patch-id can ever match** (the documented
  "bundling" false-negative shape) and there is no backref because no cherry-pick happened.
* **5 were genuinely not upstream** -- all of them minted in the preceding ~25 minutes. Their
  content reaches origin shortly afterwards, carried by the next session's whole-file write.

**So the durable failure is not that content is lost. It is that PROOF lags permanently.**
Content converges upstream reliably by read-modify-write carry; routes A and B structurally
cannot see that. And because `converge()` is correctly all-or-nothing, one permanently-
unprovable commit refuses forever while the divergence grows underneath it -- exactly the
"A PERMANENT REFUSAL IS A WEDGE" section of `ref_convergence.py`'s own docstring, now measured
on the Mac rather than on `ree-cloud-5`.

Two amplifiers, both confirmed here:

* **Two dispatchers write the same origin.** `ree-cloud-5` runs a 5-minute dispatch timer
  against this same umbrella remote, so the Mac's shared checkout is essentially always
  `behind`, so essentially every local push is non-fast-forward.
* **The operator workaround for a wedge MANUFACTURES a permanently-unprovable item.** The
  single item that still refuses after the fix below is claim `lit-pull-q093-20260818`, whose
  upstream `completion_note` is the local note plus an appended sentence reading *"Closure
  landed via throwaway worktree: the umbrella checkout is pre-existing [ahead 14, behind 34] and
  the in-place close commit 9506de6d could not reach origin."* A session worked around the wedge
  by landing an amended copy from a throwaway worktree -- and that amendment is a value the
  local branch will never hold, so it deepens the wedge it was working around.

## 4. The fix that was shipped, and what was rejected

**ROUTE C -- registry net-item containment** (`scripts/ref_convergence.py`). For an allowlisted
whole-file JSON registry with a declared unique primary key, compare the **net effect of the
entire ahead range** (merge-base -> branch tip) at the level of parsed items, and require every
net-added/modified item's exact value to be present at `origin/<branch>` **or** exhibited by
some commit reachable from `origin/<branch>`; and every net-removed key to be absent at origin.
Any ahead commit touching a non-allowlisted path must still be proven by route A or B.

This is a **proof about parsed content**, not a heuristic about diff text -- which is the line
CLAUDE.md draws when it records that the reverse-apply (`git apply --check -R`) route was
designed and deliberately not shipped. It never pattern-matches, never uses diff context, and
refuses on any parse failure, duplicate key, null key, envelope change, or unlisted path.

Measured on the 07:28Z backlog (26 ahead, 17 unproven after A and B):

| proof set | unproven |
|---|---|
| A + B (today) | 17 |
| A + B + per-commit containment | 3 |
| A + B + **net-range containment** | 2 |
| A + B + **net-range containment, value exhibited anywhere upstream** (shipped) | **1** |

The residual 1 is the manufactured amendment in section 3. **Route C is a large reduction, not
a cure: one permanently-unprovable item still refuses the whole move, by design.** Stating that
plainly matters -- the recurrence rate should fall sharply because the *routine* shapes now
converge automatically, but a wedge remains possible and the operator path is unchanged.

**Rejected, with reasons:**

* **Prefix / superseded-value inference** (upstream's note is the local note plus a suffix, so
  treat it as containing it). This is the rejected reverse-apply heuristic wearing a different
  hat. A false positive is a silently dropped commit.
* **Proactive convergence on a timer** (chip option (b)). It adds nothing: `converge()` already
  runs on every push, and it refuses for reasons that do not change with when it is called.
  Timing was never the constraint; provability was.
* **Batching a cycle's `chip_ledger` writes** (chip option (c)). It lowers the *rate* at which
  the ahead count grows after a wedge forms, and does not prevent one. It also trades away the
  property the ledger exists for -- each write commits immediately so the entry survives its
  session being killed. Rejected as a primary fix.
* **Making bookkeeping writes commit onto `origin/<branch>` directly** (so no divergence is ever
  created). This is the only candidate that would remove the wedge class outright, and it is
  the right long-term direction. NOT attempted here: it changes `ree_commit.py`'s core contract
  on the commit path of every writer on every box, and this session could not validate a change
  of that blast radius. Recorded as follow-on.

## 5. Follow-on

* Commit bookkeeping writes onto `origin/<branch>`'s tip rather than local HEAD, so the shared
  checkout never diverges. Highest value, highest risk, needs its own chip and a green suite.
* The throwaway-worktree operator workaround should re-use the LOCAL text verbatim rather than
  amending it, or amend the local copy too, so it stops manufacturing unprovable items.
