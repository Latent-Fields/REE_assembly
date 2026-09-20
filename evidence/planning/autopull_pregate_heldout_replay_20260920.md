# Launchd puller pre-gate: overlap-aware -- held-out replay and build record

**Status: BUILT + LANDED 2026-09-20** (user decision YES, Orchestrator decision lane
`orchestrate-20260919-2125`, answering `chip-20260920-autopull-fossil-reconcile-wiring-decision`).

- Written: 2026-09-20T11:26:54Z by `vigilant-colden-ac4766`
  (`chip-20260920-autopull-fossil-reconcile-wiring-build`)
- Companion to `autopull_index_fossil_selfheal_staged_20260920.md` (section 8 is the finding this
  builds; sections 3-6 are the fossil predicate and ITS replay, not repeated here).

## 1. What changed

`scripts/ree_git_sync_repair.sh`, non-wedged behind path only:

| | Before | After |
|---|---|---|
| Pre-gate | ANY tracked dirt outside `derived_re` (and not R2-proven) blocks before `git merge --ff-only` is attempted | only dirt that **overlaps `HEAD..origin/<branch>`** blocks the attempt |
| Adjudicator | git | git (unchanged) -- it refuses to overwrite a modified path and leaves non-overlapping modified files byte-untouched |
| Overlapping dirt | `BEHIND_NOT_SYNCED` | ask `ff_fossil_reconcile.py`; only RECONCILED **and** git agreeing `behind == 0` becomes `SYNCED`; otherwise the same `BEHIND_NOT_SYNCED` line, now naming genuinely-dirty vs provable-fossil paths |
| Wedged (`reset --hard`) gate | all non-derived dirt is precious | **unchanged** -- neither the overlap test nor the helper is consulted there (test W1) |

Fail-closed points: the incoming range cannot be listed -> every dirty path counts as overlapping
(the old gate); a status line that cannot be compared by plain string equality (rename `a -> b`,
quoted path) counts as overlapping (test G4); helper/python absent, timeout, or any verdict other
than RECONCILED changes nothing (tests F4-F6). Nothing is stashed, checked out, reset or discarded
on any path.

## 2. Held-out replay (GOV-HELDOUT-1 shape; no standing-rule text changed, recorded anyway)

Section 8's finding was written from ONE observation: REE_assembly, 2026-09-16..20, 0 `SYNCED`.
The replay below uses every `BEHIND_NOT_SYNCED` line in
`~/Library/Logs/ree_git_sync_repair.log` since the verdict existed (2026-08-22), all repos.

**Method.** For each cycle: HEAD and `origin/<branch>` are read from the two reflogs at the line's
timestamp; the incoming range is `git diff --name-only --no-renames HEAD T`; the dirty set is the
line's own named paths. Consecutive cycles with the same (repo, HEAD, call, names) collapse to one
window. **Stated limit:** the log names at most 5 paths, so a window naming exactly 5 with no
overlap is INDETERMINATE (the set may be truncated), not counted either way. Probe: scratchpad
`pregate_replay_probe.py` (read-only, not landed; every input is in git reflogs + the log).

| Repo | NEW = attempt ff (old != new) | NEW = block (old == new, degenerate) | Indeterminate |
|---|---|---|---|
| REE_Working | **42** windows | 13 | 11 |
| ree-v3 | **17** windows | 22 | 5 |
| REE_assembly | 29 windows | 28 + 10 log-only (fossil route) | 33 |

**Non-degenerate, held-out (not REE_assembly, not the motivating window) -- 59 windows.** Four,
spread across the period:

| # | Repo, window (UTC) | Dirty (complete set) | Incoming range touches it? | Old | New |
|---|---|---|---|---|---|
| P1 | REE_Working 2026-08-29T13:16 | `scripts/hygiene_routine_tick.py` | no (behind 3) | blocked | ff attempted; git has nothing to refuse; edit stays ` M` |
| P2 | REE_Working 2026-09-06T20:24..20:45 (3 cycles) | 4 paths incl. `scripts/autopsy_staging_tick.py` | no (behind 1) | blocked 3 cycles | synced on the first |
| P3 | ree-v3 2026-09-04T20:04..22:17 (4 windows) | `.ua/fingerprints.json`, `.ua/knowledge-graph.json`, `.ua/meta.json` | no | blocked each time | synced each time |
| P4 | REE_Working 2026-09-02T11:43 | `TASK_CLAIMS.json` (the R2 motivating shape) | **no** | blocked | synced, no R2 proof needed |

**Negative controls (old == new; listed because they are the fail-closed check).**

| Incident | Replay call |
|---|---|
| ree-v3 `experiment_queue.json` "blocks ff pull", 2026-09-03T11:29 .. 09-04T03:28 (the `MM` shape; 6 windows, up to 25 cycles) | BLOCK every window -- the queue file is in the incoming range; untouched |
| REE_Working `TASK_CLAIMS.json` / `TASK_CHIPS.json` with the registry in the range (13 windows, e.g. 2026-08-26T21:46 behind 16) | BLOCK; R2's per-row proof still decides the exemption, and git still refuses to overwrite |
| REE_assembly, log-only overlap (10 windows) | BLOCK at the gate -> handed to the fossil helper (sec 6.1 of the companion doc) |

**Outcome of the check (record for the edit):** passed -- old and new differ on 88 windows, 59 of
them on repos/dates the finding was not written from, and the new call discards nothing in any of
them. **It also changed the build:** P4 showed R2's exemption was only ever *effective* when the
registry was OUTSIDE the incoming range -- exactly the case the overlap gate now passes without a
proof -- and that with the registry INSIDE the range git refused anyway while the old script logged
the false `NEEDS_HUMAN (ff-only refused with a clean tree)`. That line is now an accurate
`BEHIND_NOT_SYNCED ... would overwrite exempted dirty path(s)` (test R2a2). R2 itself is left in
place, not removed: it is harmless, and removing it is a separate decision.

**Counterweight.** A fast-forward now lands under a session's uncommitted edits whenever the two do
not collide. No byte of that edit changes, but the files AROUND it do -- the same thing
`serve.py`'s `git pull --ff-only` has always done to REE_assembly and ree-v3 every 5 minutes, and
what any `git pull` in the session itself would do. Umbrella sessions work in worktrees, so the
main checkout's exposure is small; it is not zero.

## 3. Tests

`scripts/test_ree_git_sync_repair.sh` -- 128 checks, 0 failed; 14 of them FAIL against the
pre-change script (seen failing first). New: G1-G4 (gate), F1-F6 (helper wiring), W1 (wedged gate
unmoved), R2a2. Re-founded on OVERLAPPING dirt, because their old fixtures only blocked via the
blanket gate: 2, 5, 8, R2b, R2c, R2d, B6.

## 4. Activation (nothing here is live until these are run)

- launchd puller: `bash /Users/dgolden/REE_Working/scripts/install_gitsyncrepair_timer.sh` (copies
  the script to `~/.local/bin`; the running copy is otherwise still the old one).
- `serve.py`: restart the Explorer.
- `igw_routine_tick.py`: live on the next hourly tick once the umbrella checkout has the commit.
- Kill switches: `REE_GIT_SYNC_NO_FOSSIL=1` (puller), `REE_IGW_NO_FOSSIL_RECONCILE=1` (tick).

## 5. Readback (companion doc sec 9 item 4, extended)

Seven days after activation: REE_assembly `SYNCED` verdicts per day in
`ree_git_sync_repair.log` (baseline 0 in five days); stuck runs >= 60 min (baseline 16 in 4.5
days); `fossil-check UNPROVEN` lines by path; `checkoutdiverged-dlaptop-ree-assembly` generations.
