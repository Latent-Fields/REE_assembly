**Status: AWAITING USER REVIEW.**

# ree-cloud-4: `REE_assembly_corrupt_backup_20260801T112859Z/` -- deletion recommendation

chip: `chip-20260826-cloud4-untracked-items-triage`
session: `metaworker-chip-20260826-cloud4-untracked-items-triage` (headless, ree-cloud-4)
date: 2026-08-26T18:47Z

## What this directory is

An untracked, 5.0 GB directory at `~/REE_Working/REE_assembly_corrupt_backup_20260801T112859Z/`
on `ree-cloud-4`. It is a full copy of a `REE_assembly` checkout, including a `.git/` directory.

## Identification (confirmed, not inferred)

`docs/workspace_state_archive/2026-08.md` line 613 (umbrella repo), entry timestamped
`2026-08-01T11:53Z`:

> **Fixed ree-cloud-4's corrupted git checkout (4 zero-byte loose objects in REE_assembly) and
> shipped fleet-wide detection for the failure class.** ... Root cause traced precisely via
> `journalctl --list-boots`: a boot session ran `2026-07-30 07:04:26Z`-`07:26:39Z` and the
> corrupt object's file mtime is `Jul 30 07:26` -- a hard VM crash-reboot mid-write ...
> **Repair:** backed up untracked working files, fresh-cloned `REE_assembly` into a side
> directory, verified `git fsck --full` clean + HEAD matched `origin/master`, atomically
> swapped it in, restored the untracked files -- confirmed via 5 consecutive clean runner pull
> cycles afterward, no disruption to the concurrently-running V3-EXQ-840b experiment.

This directory's name (`_corrupt_backup_20260801T112859Z`) and its `.git` ctime
(`2026-08-01 11:30:46 UTC`, `stat` output) match this incident almost exactly (backup taken
~24 min before the WORKSPACE_STATE entry was written, consistent with "atomically swapped it
in" happening after the backup rename). It is the pre-repair corrupted checkout, moved aside
before the fresh clone was swapped into its place -- not a deliberate archival snapshot.

**Directly confirmed corrupt**, not just corrupt-by-association: it contains exactly 4
zero-byte loose objects, matching the incident's "4 zero-byte loose objects" count exactly,
including object `de229fabc9644411c0b396b332516433cea638a5` -- the same hash the WORKSPACE_STATE
entry names elsewhere in the same paragraph as "ree-cloud-4 has a corrupted git object
(`de229fabc...`, empty blob, dated 2026-07-30)".

```
$ find REE_assembly_corrupt_backup_20260801T112859Z/.git/objects -type f -size 0
.../e1/09ae44ef85d57bca6b41042c584e1362ff26c7
.../de/229fabc9644411c0b396b332516433cea638a5
.../00/4154addfd3b294acdf7d5913c93b0d4050e68b
.../92/ab65260df1cdabd7a7832c4d1b6928f24bfa6d
```

## Current checkout health (confirmed 2026-08-26)

The live `~/REE_Working/REE_assembly` checkout -- the fresh clone that replaced this backup on
2026-08-01 -- is healthy:

- `find .git/objects -type f -size 0` -- 0 zero-byte objects.
- `git rev-parse HEAD` == `git rev-parse origin/master` (observed in sync during this session;
  `git status -sb` shows only the ordinary large set of untracked `evidence/experiments/*.json`
  result manifests any active REE_assembly checkout on this box carries, not a divergence).
  It is being actively written to by the sync_daemon/governance pipeline as of this session
  (`0b59cdf121 planning: scoring_excluded exp_count investigation findings`, landed minutes
  before this doc).
- 25 days of continuous fleet use since the repair (2026-08-01 to 2026-08-26) with no further
  corruption reported anywhere in `WORKSPACE_STATE.md` / the archive for `ree-cloud-4`.
- Today's own `metaworker-repair` Healer cycle on this box (`WORKSPACE_STATE.md`,
  `2026-08-26T18:37:44Z`) reports `ref_convergence.py --check on REE_assembly/ree-v3/REE_Working:
  all converging normally` and `audit_stashes.py --all: no orphans`.
- The proactive fix from the same incident (`_scan_zero_byte_loose_objects` in
  `experiment_runner.py`, `ree-v3 bbb25d2`) has been running on every `git_pull()` since
  2026-08-01 and would have logged a clean<->corrupt transition on this box's `runner_status/
  ree-cloud-4.json` if it recurred; nothing in this session's review found such a report.

## Recommendation

**Delete.** The backup was a safety net for the 2026-08-01 repair, the repair is verified
successful and has held for 25 days under continuous use, and the directory itself is
confirmed corrupt (not merely old) -- it has no forensic or recovery value; `REE_assembly`'s
full commit history already exists on `origin/master` and in the healthy local clone, and a
corrupted checkout preserves nothing origin does not already have.

Frees 5.0 GB on `ree-cloud-4` (`/` at 21G/75G used, 52G available -- not urgent, but the
directory serves no purpose):

```bash
rm -rf ~/REE_Working/REE_assembly_corrupt_backup_20260801T112859Z
```

This session did **not** run that command -- per its dispatch brief, a 5 GB irreversible
deletion is being surfaced for confirmation rather than executed unilaterally, even though the
purpose has now been confirmed. If this recommendation is accepted, no further action beyond
the `rm -rf` above is needed; nothing else references this path (confirmed by grep across
`WORKSPACE_STATE.md`, `TASK_CLAIMS.json`, `TASK_CHIPS.json` -- the only other mention is this
chip's own tldr).
