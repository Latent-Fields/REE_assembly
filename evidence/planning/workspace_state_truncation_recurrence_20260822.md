# WORKSPACE_STATE.md truncation: a recurring failure, not a one-off (2026-08-22)

chip: `chip-20260822-workspacestate-truncated-6857-lines`

## Summary

`WORKSPACE_STATE.md` has been silently collapsed to a near-empty stub **three
times** in two months, each time by an innocuous-looking, correctly-formatted
"append my closing entry" commit that in fact discarded almost the entire
file:

| # | commit | date | author/kind | -lines | +lines | recovered by |
|---|---|---|---|---|---|---|
| 1 | `fa11db5b` | 2026-06-20T13:21:23+01:00 | interactive (`/governance` close, nooarche) | 5916 | 1 | `1a56a85e`, **41 seconds later**, same session |
| 2 | `d705aef0` | 2026-08-09T18:27:00+01:00 | interactive (V3-EXQ-906b review close, nooarche) | 2581 | 3 | `125a7280`, ~2h14m later, different session (bisected via `git log -S`) |
| 3 | `b0ce8359` | 2026-08-22T11:31:48+00:00 | headless (`metaworker-dispatch` cycle 3576, ree-cloud-5) | 6857 | 2 | `c77705c4`, ~1h28m later, different session (this chip) |

All three are pure coincidence-proof by signature: a commit message that
describes only the session's own (legitimate, small) piece of work, with a
diff stat showing thousands of deletions the message never mentions. None of
the three authoring sessions appear to have noticed at commit time.

**This is not specific to the "metaworker-dispatch writer"** — the chip that
opened this investigation assumed the automated dispatch cycle was the
culprit, but the first two incidents predate `metaworker-dispatch` entirely
and were triggered by ordinary *interactive* session closes (a `/governance`
close and a routine experiment-review close). The common factor is the
**close-time WORKSPACE_STATE.md append itself**, regardless of what kind of
session performs it.

## What #1 already diagnosed, and why it didn't prevent #2 or #3

The recovery commit for incident #1 states the mechanism directly:

> `fix: restore WORKSPACE_STATE.md history (prior close truncated it via
> open(w)-before-read bug; re-prepended 12:08Z entry onto full history)`

i.e. the close procedure effectively opened the file for writing (which
truncates it to zero length on open, standard POSIX `open(..., 'w')`
semantics) *before* it had captured the full existing content to prepend the
new entry onto — so the write that followed wrote back only the new entry
(plus, in this case, nothing at all) rather than new-entry + full history.

That diagnosis was correct and specific, but **it was never converted into a
structural fix** — no script, no guard, no test was added. It lived only as
a sentence in a recovery commit message, so it could not stop the same shape
from recurring: incident #2 (Aug 9) is a session-close truncation with the
identical signature (thousands of deletions, single-digit insertions, an
innocent commit message), and incident #3 (Aug 22, this chip) is the same
shape again, this time in an automated headless dispatch cycle rather than
an interactive session.

## Why this file specifically, and why it keeps recurring

`WORKSPACE_STATE.md` is the **one** standing coordination file that CLAUDE.md
tells *every* session — interactive or headless, human-directed or
dispatch-cycle — to append to at close, via a raw `Edit`/`Write` tool call,
with **no dedicated script**:

- `TASK_CLAIMS.json` is protected by `scripts/task_claim.py` (atomic
  open/close, compare-and-swap commit, arbitration).
- `TASK_CHIPS.json` is protected by `scripts/chip_ledger.py` (same pattern).
- `WORKSPACE_STATE.md`'s own *rotation* (moving old history to
  `docs/workspace_state_archive/`) is protected by
  `scripts/rotate_workspace_state.py`, which writes archives before
  truncating and refuses to write at all if a content-conservation check
  fails (see its module docstring) — used successfully on 2026-08-19
  (`79b94d49`, 10.77MB -> 2.28MB, "nothing deleted").
- **The ordinary per-session closing append has none of this.** It is a
  freeform `Edit`/`Write` against a large (multi-MB, thousands-of-lines)
  markdown file, performed by whatever LLM session is closing out, with no
  conservation check, no dedicated tool, and — notably — **`WORKSPACE_STATE.md`
  is not even listed among CLAUDE.md's own declared "Exposed files"**
  (`TASK_CLAIMS.json`, `experiment_queue.json`, `review_tracker.json`,
  `claims.yaml`, and everything under `evidence/planning/`) despite being
  edited by every single session that closes.

The file's size is exactly what makes the freeform edit fragile: all three
incidents landed while the file was large (multi-MB or several-thousand
lines) — incident #3 happened just three days after the 2026-08-19 rotation
brought it down to 2.28MB, and it had already regrown to 6867 lines by
2026-08-22 given the sheer commit velocity (thousands of dispatch cycles
across two resident boxes plus interactive sessions). A large file plus a
tool-call pattern that risks reconstructing "new entry + [something short]"
instead of "new entry + [everything]" is a reliable recipe for exactly this
failure, and nothing currently guards against it.

## What structurally would close this (not done in this chip — chipped separately)

The fix is the same shape already proven for `TASK_CLAIMS.json` /
`TASK_CHIPS.json` / the rotation script itself: replace the freeform
Edit/Write with a narrow, safe, scriptable append that:

1. Re-reads the live file fresh immediately before writing (no cached/stale
   copy — the "claim early, write late" rule already stated in CLAUDE.md's
   Concurrency Rules).
2. Appends (prepends) only the new entry text, structurally, never
   reconstructing the rest of the file by hand.
3. Runs a cheap conservation check before writing — at minimum, refuse to
   write if the new file is drastically shorter than the old one (e.g. new
   byte count < 50% of old byte count) unless a `--rotate` flag is
   explicitly passed, mirroring `rotate_workspace_state.py`'s own
   `conserve_check`.
4. Commits via `ree_commit.py` with an explicit path list, exactly like
   `task_claim.py`/`chip_ledger.py`.

This chip does not implement that script — it is scoped to finding and
documenting the root cause, per its own brief. The fix is tracked as a
separate follow-on chip (see `TASK_CHIPS.json` /
`chip-20260822-workspacestate-safe-append-tool`).

## Evidence trail (commands used, for anyone re-verifying)

```
git log --numstat --format='COMMIT %H %ad' --date=iso-strict -- WORKSPACE_STATE.md
# then: awk over the numstat output for deletions > 500 lines in a single commit
```

surfaces all four large-deletion events in the file's history: the three
truncations above plus the one legitimate rotation (`79b94d49`,
2026-08-19, via `rotate_workspace_state.py`, distinguishable by its own
commit message explicitly stating the conservation guarantee).
