# Staged-revert skew audit -- DLAPTOP `REE_Working`, 2026-08-18

**Status: REPORT-ONLY. Nothing was repaired, reverted, reset or written to any
registry by this audit.** The reported condition had already cleared before the
audit began; the only change this session made to a shared file is its own
`TASK_CLAIMS.json` entry.

- Chip: `chip-stagedskew-dlaptop-ree-working` (origin `hygiene_tick`, kind `work`)
- Recorded: 2026-08-18T19:26:51Z (umbrella `a01195e1`)
- Claimed:  2026-08-18T19:28:05Z
- Audited:  2026-08-18T19:29Z-19:34Z (session `metaworker-chip-stagedskew-dlaptop-ree-working`)
- Box: `DLAPTOP` (canonical; `machine_identity.canonical_machine_name`)

---

## 1. Verdict

**No skew present, and no data was lost.** The chip reported one path,
`TASK_CLAIMS.json`, staged as an `M ` revert in the umbrella `REE_Working`
checkout, with the staged blob PROVEN stale. By the time the dispatched session
read the checkout, the condition was gone.

Measured at 19:29Z, before this session touched anything:

```
git -C /Users/dgolden/REE_Working status --porcelain -- TASK_CLAIMS.json   -> (empty)
git -C /Users/dgolden/REE_Working status --porcelain | grep -vE "^(\?\?| M)" -> (nothing staged)
```

Entry-set comparison (the check that actually matters -- the incident this
detector was built from carried a `TASK_CLAIMS.json` missing 27 entries):

| revision | claim entries `(session_id, claimed_at)` |
|---|---|
| `a936f5cb` (HEAD at chip claim) | 122 |
| `HEAD` (after this session's own claim) | 123 |
| working tree | 123 |

- entries in chip-time HEAD but **missing** from the worktree: **0**
- entries in the worktree but not in chip-time HEAD: **1** -- this session's own claim
- worktree key set **== HEAD key set**: yes

Re-running the live detector across all seven repos at 19:33Z:

```
findings: 0   meta: {'scan_ok': True, 'scanned': 7, 'skewed_repos': 0}
REE_assembly / ree-v3 / ree-v2 / ree-v1-minimal / REE_convergence /
REE_OpenClaw / REE_Working:  pure_M=[]  all_staged=[]
```

The two paths still dirty in that checkout (`worktree_session_registry.json`,
`docs/worktree_session_registry.md`) are unstaged ` M`, not `M `. That is the
machine-scoped registry-regen dirt CLAUDE.md already documents, not skew, and it
was deliberately left alone.

## 2. What cleared it, and when -- bounded to a 30-second window

The repair happened between **19:26:51Z** (`a01195e1`, the tick's own chip-record
commit) and **19:27:13Z** (`065ca944`).

The upper bound is hard, and comes from an accident of timing that doubles as a
demonstration of the hazard. `065ca944` is a **merge commit**, and a merge
records the whole index tree. Had `TASK_CLAIMS.json` still been staged as a
revert at 19:27:13Z, that merge would have carried the reverted blob and
`git show --stat 065ca944` would list it. It lists only `WORKSPACE_STATE.md`
(2 insertions). So the index was provably already clean.

Note what that means if the repair had *not* landed first: an unrelated merge of
`claude/f-variance-saturation-substrate-228824`, touching one line of
`WORKSPACE_STATE.md`, would have silently committed a revert of the claims
registry. `git merge` only refuses on a staged path it needs to *update*; it
does not refuse on an unrelated one.

Entry counts across the whole window confirm nothing was lost at any point:
`6b374af8` 121 -> `9d06e4bc` 122 -> `3d02b1cc` 122 -> `a01195e1` 122 ->
`065ca944` 122 -> `a936f5cb` 122 -> `ad589250` 123, with zero removals at every
step.

## 3. Root cause: the detector and the repairer race, and the repairer wins

`ree_commit.check_head_worktree_skew()` runs **after every commit**, on every
path staged-modified against HEAD that the call did not itself declare, and
repairs the ones `_verify_stale_adoption()` can prove stale. On the umbrella
repo during a metaworker dispatch cycle that is every few seconds
(218 commits touched `TASK_CLAIMS.json` on 2026-08-18 alone).

`hygiene_routine_tick.py` collects this finding at line 4013 and records its
chips via `chip_ledger.cmd_record` at line 4039 -- **in the same process, after
the scan**. `cmd_record` writes `TASK_CHIPS.json` through `ree_commit`, which
declares only that path, sees `TASK_CLAIMS.json` as undeclared staged-modified,
and repairs it. The tick therefore raises a chip and then, seconds later,
destroys the evidence for it with its own bookkeeping commit.

Reproduced directly (throwaway repo, HEAD `v3`, index+worktree `v1`,
`ree_commit` declaring only an unrelated path):

```
ree_commit: committed d8091b9b5d (1 file(s), verified)
ree_commit: HEAD/worktree skew repaired -- discarded 1 staged REVERT(s) ...
    f.json  (staged content = this path at 0523786db9)
-> status clean, f.json == v3
```

## 4. The finding worth keeping: the two proofs have different reach

The detector and the repairer do not use the same staleness proof, and the
detector's is strictly wider.

| | proof | bound |
|---|---|---|
| `hygiene_routine_tick._staged_blob_is_historical` | `git log --all --reflog --find-object` | unbounded |
| `ree_commit._verify_stale_adoption` | `git log -n 100 <base> -- <path>` (`ANCESTRY_SCAN_COMMITS = 100`) | 100 commits **of that path** |

On `TASK_CLAIMS.json` at current write rates, 100 commits of that path reaches
back to **2026-08-18 08:33** -- about **12 hours**.

Confirmed differentially in a second throwaway repo, staged blob 105 commits back:

```
ree_commit: staged modification(s) left UNTOUCHED -- could not prove they are
stale adoption lag:  f.json
-> status still "M  f.json", worktree v1, HEAD v105

hygiene_routine_tick._staged_blob_is_historical(f.json) -> True
```

So a chip of this class has exactly two fates:

1. **Staged blob within the repairer's window** (this case) -- cleared by the
   next `ree_commit` call in that repo, frequently the tick's own. The chip is
   stale before it is ever claimed, and a session dispatched to it correctly
   finds nothing. Not a false positive: the condition was real when scanned.
2. **Staged blob beyond the window** -- `ree_commit` refuses and says so, the
   skew genuinely persists, and the chip is exactly right. This is the case the
   detector exists for, and it remains uncovered by anything else.

Both are worth raising. The distinction is not currently visible from the chip.

## 5. Proposal -- AWAITING USER REVIEW, not applied

Nothing below was implemented. It is a suggestion for whoever next touches
`hygiene_routine_tick.py`, offered because the diagnosis above cost a dispatched
session a full cycle to reach.

Have `_staged_revert_skew_findings` record, per proven path, whether
`ree_commit._verify_stale_adoption` would *also* prove it (a direct call, no
reimplementation), and say so in the chip prompt -- e.g. *"the staged blob is
within ree_commit's 100-commit window, so the next commit to this repo will
likely repair it before you arrive; verify first"* versus *"beyond the window --
ree_commit has already refused this and will keep refusing; the repair is
yours"*. That routes fate-1 chips to a 30-second confirmation and reserves the
manual per-path procedure for fate 2.

Deliberately **not** proposed: widening `ANCESTRY_SCAN_COMMITS`, or pointing
`_verify_stale_adoption` at the wider `--all --reflog` search. The narrow
ancestor-of-HEAD proof is what makes the unattended repair safe, and CLAUDE.md's
`adoption_bases` block is explicit that widening it is the shape that turns a
dropped local commit into permanent loss. The asymmetry is a feature; only its
invisibility is the defect.

## 6. Reproduction commands

```bash
BASE=/Users/dgolden/REE_Working
git -C "$BASE" status --porcelain | grep -vE "^ M" || echo "(nothing staged -- clean)"
/opt/local/bin/python3 -c "
import sys; sys.path.insert(0,'$BASE/scripts')
import hygiene_routine_tick as h
print(h._staged_revert_skew_findings())"
git -C "$BASE" show --stat --format='' 065ca944     # merge that bounds the repair window
```
