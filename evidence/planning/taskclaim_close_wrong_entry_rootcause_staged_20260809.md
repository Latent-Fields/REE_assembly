**Status: AWAITING USER REVIEW — investigation complete; the in-code fix is HANDED OFF, not applied (see §6).**

# task_claim.py `close` wrote one session's closure onto another entry — root cause & recommendation

Chip: `chip-20260809-taskclaim-close-wrote-wrong-entry`
Session: `metaworker-chip-20260809-taskclaim-close-wrote-wrong-entry` (headless)
Date: 2026-08-09

## 1. What happened (confirmed, not re-derived)

REE_Working commit `11161b55` ("claim: close metaworker-chip-20260809-flaky-stale-after-hours")
wrote flaky's closure fields onto the entry of a **different** session:

```
-      "status": "active"
+      "status": "done",
+      "closed_at": "2026-08-09T10:55:59Z",
+      "completion_note": "LANDED. De-flaked test_stale_after_hours_is_configurable ..."
```

The mutated entry's resources are `scripts/substrate_queue_writeback_drift.py` +
`...test_substrate_queue_writeback_drift.py` — they belong to
`metaworker-chip-20260809-sqdrift-postimpl-park-fp` (claimed_at 10:56:26Z), **not** to
flaky. The written `closed_at` (10:55:59Z) **predates** the victim's own `claimed_at`
(10:56:26Z) — impossible.

## 2. Root cause: the `--push` retry replayed a textual diff, not the semantics

`cmd_close.apply_fn` selects the entry by `session_id` and `die()`s on no match, so it
**cannot** write closure onto a non-matching entry given the file it read. The proof it
never ran against this base: **neither** the corrupt commit `11161b55` **nor** its parent
`a076baeb` contains a `flaky-stale-after-hours` entry at all. Had apply_fn seen that file
it would have aborted with "no claim found for session_id".

So the corruption happened **after** apply_fn and after the local commit, inside git's
**3-way merge during the `--push` retry**. At incident time that retry was
`git pull --rebase origin master` on the **shared** checkout (the `master` reflog around
10:55–11:59 shows empty-message ref moves — the rebase/ref-move signature). Rebasing
flaky's "`status: active` → `done` + closure" hunk onto an origin tip whose entry layout
had shifted transplanted the hunk onto the sqdrift entry, whose trailing lines
(`resources ]`, `status: active`, `}`) supplied matching merge context. Flaky's own entry
vanished from that line of history.

On `origin/master` flaky closed **correctly** (claimed 10:48:11Z → closed 10:55:59Z,
resources `scripts/test_chip_ledger_claim.py`). The corruption was local-only and was
reverted (`3f888fac`); sqdrift closed correctly by `22223094`. **No data repair is
needed** — this is about the mechanism.

## 3. This is ONE root cause with the sibling chip `taskclaim-retry-duplicate-commits`

Both are the `--push` retry path. `ree_commit` `cb822ab0` — landed **47 seconds after**
this incident — replaced the shared-checkout `git pull --rebase` with a cherry-pick onto
origin in a **throwaway worktree**. That commit is the retry-path rewrite; the
retry-duplicate-commits chip is about the same rewritten path. Fix these together, not as
two separate patches.

## 4. What `cb822ab0` already fixed, and the residual it did NOT

- **Fixed (the specific trigger):** the shared-checkout `pull --rebase` is gone. A
  cherry-pick that hits a real conflict is aborted and given up on cleanly (commit stays
  local, unpushed). Reproduced in a tempdir: the modify/delete shape of this incident now
  **conflicts** rather than silently mismerging (see the characterization test in
  `scripts/test_task_claim_close_transplant.py`). A reorder scenario cherry-picked
  **correctly** (git's 3-way merge used the unique `session_id`/`claimed_at` context).
- **Residual (unclosed):** a cherry-pick is still a 3-way merge over a repetitive
  multi-writer JSON file, so a **silent** mismerge onto the wrong entry is not
  structurally impossible. And — the real gap — **nothing verifies the pushed content
  still contains the operating session's own entry, closed with its own closure data.** A
  silent mismerge produces no conflict and no error.

## 5. The brief's proposed invariant is over-broad — held-out validation refutes it as a gate

The brief proposed: *"`closed_at` must not precede that entry's `claimed_at` — that single
check would have caught this at write time."* Two problems:

1. **It is not a write-time check.** The corruption is created **downstream** of apply_fn
   and the local commit, in the rebase/cherry-pick. A guard inside apply_fn/mutate runs
   **before** the corruption exists and cannot see it. The check must run on the
   **committed/pushed** content.
2. **As a hard gate it has a ~7:1 false-positive rate.** Run against the 8 entries that
   violate `closed_at < claimed_at` at `11161b55`: **only 1 is the corruption.** The other
   7 are legitimate — a claim closed `--from-commit` against a landing that predates the
   claim open (work found already done), or "landed the work, then opened/closed the
   claim." Each has a completion_note coherent with its own resources. A gate that fires
   on ordinary work gets ignored (the exact anti-pattern CLAUDE.md warns about). It
   survives only as an **INFO-level smell**, never a gate.

   Held-out cases (all legitimate, all flagged by the naive check):
   `sd-024-evidence-confirm`, `v3-exq-812-harness-repair` (×5, one long-running session),
   `mel-dose-sweep-inv-051` (×several), `mech075-cluster-requeue`,
   `autopsy-dryrun-coverage-gap`, `exciting-villani`.

   The **zero-FP separator is self-identity, not timing** — the incident's true tell was
   that the note/closure were **foreign** to the entry.

## 6. Recommendation (for the `task_claim.py` / `ree_commit.py` owners — HANDED OFF)

Both natural homes are under an active sibling claim right now
(`atomic-write-build-indexes` owns `scripts/task_claim.py`;
`taskclaim-retry-duplicate-commits` owns the `ree_commit` retry path), so this session did
**not** edit them — it would recreate the two-implementations-in-one-tree hazard this chip
exists to fix. Apply after coordinating with those owners:

**(a) Post-commit self-identity verification in `cmd_close` (primary, zero-FP).** After
`mutate_and_commit` returns (and, for `--push`, after the cherry-pick lands), re-read the
committed `TASK_CLAIMS.json` and assert **this** session's own entry is present, `done`,
and carries **this** call's own `closed_at` and `completion_note`. Fail loudly otherwise.
A tested reference implementation — `verify_close_landed()` — is in
`scripts/test_task_claim_close_transplant.py`; lift it into `task_claim.py` and call it
from `cmd_close` (and, by the same argument, `cmd_open` could assert its own entry
landed). This catches both the "my entry vanished" (11161b55) and "foreign closure on my
entry" variants without any timing heuristic.

**(b) Optional integrity check in `ree_commit`'s cherry-pick retry** (couple with the
retry-duplicate chip): after `git cherry-pick` and **before** push, for a named JSON path
that parses as `{"claims": [...]}`, confirm the cherry-picked delta touched only the
intended entry (e.g. the set of `(session_id, claimed_at)` keys and their `status` changed
exactly as the source commit intended). On mismatch, abort the pick and give up cleanly —
the same failure mode a conflict already takes.

**(c) `closed_at < claimed_at` as INFO only.** If surfaced anywhere (session-startup
audit, `prune_task_claims_done.py` WARN), label it a smell needing confirmation, never a
gate. Do **not** wire it as a blocking invariant.

## 7. Held-out check (GOV-HELDOUT-1) — recorded per CLAUDE.md General Rules

This edit proposes a standing check (a post-commit invariant). The held-out validation was
actually run and **changed the outcome**: it refuted the brief's proposed `closed_at !<
claimed_at` gate (6+ legitimate held-out cases give the wrong answer), and redirected the
fix to self-identity verification. Record this as a case where the held-out check caught an
over-broad rule before it shipped.

## 8. Deliverables landed by this session

- `scripts/test_task_claim_close_transplant.py` — reproduction, characterization of the
  current cherry-pick retry, executable held-out refutation, and the tested
  `verify_close_landed()` reference implementation. (5 tests, pass.)
- This document.

Not landed (handed off, §6): the in-code post-commit verification in `task_claim.py` and
the integrity check in `ree_commit.py`, both under active sibling claims.
