# ree-cloud-4 preserved stash/backup triage -- 2026-08-19

**Chip:** `chip-20260819-cloud4-preserved-stash-triage`
**Verdict written:** 2026-08-19T20:48:37Z
**Box:** ree-cloud-4 (ree-worker-4, 91.99.68.94) -- this artifact is machine-local to that box only.

## Subject

On 2026-08-19T17:50Z, `chip-20260819-cloud4-orchestrator-veto-bootstrap-deadlock` needed to
bring ree-cloud-4's `REE_Working` umbrella checkout current (it was 522 commits behind), and
its `--ff-only` autosync was blocked by two uncommitted files. Before pulling, the working
uncommitted content was preserved two ways:

- `git stash` on that box: `stash@{0}`, message `cloud4 pre-pull preserve 20260819T1750Z
  chip-20260819-cloud4-orchestrator-veto-bootstrap-deadlock`
- A file copy at `/home/ree/_preserve_20260819T1750Z_chip20260819cloud4/` with
  `blob_hashes.txt` recording the two blob shas:
  - `scripts/chip_ledger.py` -> `147e46e7fb0569410da127f1acaf98e3c7507c12`
  - `scripts/task_claim.py` -> `dbd181bf5e3929432e73f6d81bdaea1061a023d5`

Neither blob matches any commit at that path in `REE_Working` history (confirmed via
`git log --all --follow` walking every commit that ever touched either path and comparing
tree blobs -- no match). `git rev-list --objects --all` does surface the two blob objects,
but only because `refs/stash` is included in `--all`; the objects are not reachable from any
branch/tag.

## What the content actually was

Both files are an in-progress, uncommitted continuation of the SAME feature ree-cloud-4 had
already been building that day: wiring `ree_commit.py`'s opt-in `--to-remote-tip` mode through
`task_claim.py` (open/close/amend) and `chip_ledger.py` (record/resolve/claim/amend-prompt/
amend-urgency). The box's own commit `2f29bfdf` ("wip: wire --to-remote-tip flag through
task_claim.py/chip_ledger.py (untested)", 2026-08-19T17:39:36Z) is an ancestor of the stash's
base commit (`f76bd229`) and of current `master` -- i.e. this was a second, further pass on
top of that WIP commit, refining docstrings and (per the stash diff) adding some structural
detail, still uncommitted when the pull was needed 11 minutes later.

## Why it is superseded, not real orphaned work

`master`'s current `scripts/task_claim.py` / `scripts/chip_ledger.py` already carry a complete,
tested implementation of the identical feature, landed via `307de8d3` ("task_claim/chip_ledger:
wire opt-in --to-remote-tip through open/close/amend and record/resolve/claim/amend-*"),
cherry-picked from `a53079e9e1c67a5437084a7050e0fae41e107b9a` -- a commit authored on another
box (author `REE Automation (Mac)`, object not present in this repo's local object store,
consistent with having been developed elsewhere and landed via the umbrella's normal
convergence path). Diffing the preserved blobs against current `master` HEAD
(`scripts/chip_ledger.py`: 441 diff lines; `scripts/task_claim.py`: 302 diff lines) shows:

1. **The core mechanism is functionally identical on both sides** -- `_REMOTE_TIP_SHA_RE` /
   `_parse_remote_tip_sha()`, the before/after-HEAD-diffing-can't-see-remote-tip-success
   reasoning, and the `to_remote_tip` threading through `mutate_and_commit()` /
   `commit()` / `ree_commit_once()` all exist on `master` too, independently arrived at with
   different wording.
2. **`master`'s version is strictly more complete.** It carries a same-day production-bug fix
   (`getattr(args, "to_remote_tip", False)` instead of `args.to_remote_tip`, fixing a live
   `AttributeError` caught within the hour by a running `hygiene_routine_tick.py` cycle,
   dispatch cycle 3138, `chip-20260819-chipledger-cmdresolve-toremotetip-namespace-attr`) that
   the preserved copy does not have.
3. **`master` also carries an entirely separate, later feature the preserved copy predates
   and knows nothing about**: `chip_ledger.py`'s fat-field archiving
   (`cmd_archive`, `archive_month_for`, `archived_field`, ~340 lines) -- landed later the same
   day per the umbrella `CLAUDE.md`'s own dated note ("added 2026-08-19"). Applying the
   preserved diff onto `master` as-is would delete this feature outright.
4. `master`'s version was verified with a dedicated test pass (`test_task_claim_remote_tip.py`
   14 tests, `test_chip_ledger_remote_tip.py` 7 tests, plus the full existing
   `test_task_claim_*.py` / `test_chip_ledger_*.py` suites and the three routine-tick suites
   green per the landing commit message). The preserved copy was never run past a smoke test
   (commit message on the box's own prior pass literally says "untested").

So the preserved stash and backup directory are a **superseded parallel draft**: real,
intentional work-in-progress, but overtaken by another host completing and landing the same
feature first, with a bugfix and a follow-on feature the local draft cannot know about.
Landing it would be a regression, not a contribution.

## Disposition

- **Stash**: archive-tagged locally on ree-cloud-4 as `stash-archive/20260819-<short-sha>`
  (local-only, per `CLAUDE.md`'s stash-triage recipe), then dropped.
- **Backup directory** `/home/ree/_preserve_20260819T1750Z_chip20260819cloud4/`: removed after
  this verdict document is committed and pushed (its content is fully preserved in git via the
  archive tag; the directory itself was only ever a second copy for the same content).
- **No code changes to `scripts/chip_ledger.py` / `scripts/task_claim.py`** -- `master`'s
  content is confirmed superior and nothing from the preserved copy needs to be merged in.

## Verification commands (for anyone re-auditing this)

```bash
# On ree-cloud-4:
git -C /home/ree/REE_Working stash list          # was: stash@{0} ...
git -C /home/ree/REE_Working tag -l 'stash-archive/20260819-*'
ls /home/ree/_preserve_20260819T1750Z_chip20260819cloud4/   # should no longer exist
```
