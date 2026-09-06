#!/usr/bin/env python3
"""Fleet git-health prober -- makes a WEDGED worker visible from outside.

WHY THIS EXISTS
---------------
On 2026-07-18T05:21Z ree-cloud-2's REE_assembly checkout wedged: a
`git pull --rebase --autostash` hit a conflict restoring its own autostash and
left stranded unmerged index entries. The runner retried every ~85 seconds and
logged "unresolved conflict" EVERY TIME -- for TWO DAYS -- and nobody noticed.
It was found by accident on 2026-07-20 by a session looking at something else.

The two days are the point. The worker did not look broken from anywhere an
operator actually watches:

  * It kept heartbeating (`state=running`, fresh `last_tick_utc`).
  * It kept claiming queue items and running experiments to PASS.
  * Its RESULTS kept reaching origin -- under Phase 3 those travel by the
    coordinator spool (`POST /result` -> phase3_git_writer), NOT by the
    worker's own git push, so a totally wedged git checkout does not
    interrupt the evidence plane.

What it actually cost: the worker executed increasingly stale `ree_core` /
experiment code (218 commits behind when found), and its local `evidence/`
writes stranded on disk.

WHY THE EXISTING TELEMETRY CANNOT DETECT THIS (both verified, do not retry)
--------------------------------------------------------------------------
The obvious fix -- derive staleness from the heartbeat's `runner_version`
field -- DOES NOT WORK, for two independent reasons:

1. WRONG REPO. `runner_version` comes from `_git_code_version()`, which reads
   `REPO_ROOT` == the **ree-v3** checkout (ree-v3 experiment_runner.py ~L713).
   The cloud-2 wedge was in **REE_assembly**. ree-v3 pulled fine throughout
   ("git pull ree-v3: Already up to date" every tick, all through the wedge).
   No telemetry field carries REE_assembly pull health at all.

2. THE FIELD LAGS BY DESIGN. `_refresh_runner_version()` is called BETWEEN
   PASSES, never per-tick (ree-v3 experiment_runner.py ~L749), deliberately, so
   a running experiment is never disturbed by a git subprocess. During a
   multi-hour experiment the reported version sits frozen at its last-pass
   value while the checkout on disk keeps advancing. Measured 2026-07-20:
   cloud-2 reported `r4075 5bb69cd 2026-07-20` (a 05:19Z commit) on a 10:44Z
   heartbeat while pulling ree-v3 successfully every ~60s. So version lag is
   NOT code lag, and a detector keying on it produces false positives.

And a third trap worth stating, for anyone tempted by heartbeat freshness:

3. `last_tick_utc` STALENESS IS NOT A FAULT SIGNAL. Since 2026-06-23 the
   phase3 heartbeat writer commits on STATE-CHANGES ONLY (the 30-minute
   liveness tick was retired to stop REE_assembly history bloat -- see
   CLAUDE.md). A healthy worker mid-experiment has an intentionally stale
   heartbeat on origin/master. Keying on freshness produces false alarms and
   re-creates the pressure to restore the tick.

WHAT THIS DOES INSTEAD
----------------------
Actively probes each worker over ssh and reads the git state that no telemetry
carries. Per machine, per repo it reports:

  unmerged   -- count of unmerged index entries. >0 means WEDGED: every
                subsequent `git pull` aborts with "Pulling is not possible
                because you have unmerged files". THE cloud-2 signature.
  behind     -- commits behind the upstream tracking ref.
  skew       -- HEAD/worktree skew (porcelain ' D' AND 'D ' -- both forms;
                see CLAUDE.md, the 'D ' variant is pre-staged and lands
                deletions on a bare commit).
  gc.log     -- present means git has DISABLED automatic gc on that repo.
  stashes    -- stranded autostash entries. These have held the only surviving
                copy of completed-run evidence before (cloud-3, V3-EXQ-673).
  untracked  -- UNTRACKED working-tree files graded against the upstream ref.
                A run manifest with no counterpart on origin at ANY path is a
                real, silent evidence loss. See below.

WHY UNTRACKED FILES ARE GRADED, NOT JUST STASHES (added 2026-07-30)
-------------------------------------------------------------------
The stash count is not a proxy for "this worker is holding something
irreplaceable", and on 2026-07-30 it pointed the wrong way. This probe
reported `ree-cloud-2  REE_assembly  OK - 17 stash entry(ies)`. A full triage
of those 17 found ZERO stranded content -- all 21 (stash, path) pairs were
already on origin/master. Meanwhile the SAME worker's working tree held

  evidence/experiments/v3_exq_490h_mech295_cascade_gap4_tier1/
    v3_exq_490h_mech295_cascade_gap4_tier1_20260529T214607Z_v3.json.bak.20260530

as a plain UNTRACKED file: a FAIL / weakens / MECH-295 result, 5661.46s of
compute, `experiments.status = completed` in the coordinator DB with ZERO rows
in `results`, absent from origin/master at every path -- the manifest that
`evidence/planning/failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md`
declared unrecoverable. Recovered at REE_assembly 579ac6361e.

So the pre-2026-07-30 signal was misleading in the DANGEROUS direction: it drew
attention to 17 harmless stashes while the actual loss sat somewhere the probe
did not look at all, and a stash-only triage of that box would have closed it
"all clean".

Three things this grading has to get right, all learned from that file:

  * BASENAME, not exact path. The same manifest legitimately lives at a flat
    `evidence/experiments/<run_id>.json` and at a pack
    `evidence/experiments/<exp>/runs/<run_id>/manifest.json`, and cloud-2 also
    held copies inside experiment subdirectories. Grading a local path against
    only its own path on origin would report every one of those as stranded.
  * PARSED JSON, not bytes. The phase3 git writer stores compact JSON and
    INJECTS `queue_id` / `machine` / `epistemic_category` /
    `evidence_direction_note`, so origin is routinely a strict superset of a
    semantically identical local file. A byte compare calls those stranded.
  * STRIP BACKUP SUFFIXES (`.bak.<date>`, `.bak.phantom-clean`) and re-check
    the stem. That is precisely what made the 490h file findable.

ONE CAVEAT ON A WORKER, distinct from the Mac's noise classes below: a manifest
reaches origin via the coordinator spool (`POST /result` -> phase3_git_writer),
which takes on the order of a minute or more. A run that finished seconds ago
therefore grades as stranded and is not. Observed live 2026-07-30T17:32Z on
ree-cloud-2: `v3_exq_842_..._20260730T173047Z_v3`, PASS, ~85 seconds old at
probe time.

THE DISCRIMINATOR IS THE COORDINATOR DB, and it is the exact inverse of the
phantom-completion signature. An IN-FLIGHT manifest has a `results` row with
`received_at` set and `committed_at` NULL -- the spool has it, the git writer
has not landed it yet, and it will land on its own:

    SELECT queue_id, outcome, received_at, committed_at
      FROM results WHERE queue_id LIKE '%<id>%';

A genuine STRAND is `experiments.status = completed` with ZERO rows in
`results` -- nothing ever reached the spool, so nothing will ever land. Check
that before triaging any worker finding whose run_id timestamp is within a few
minutes of the probe. The Mac's automatic re-check does not close this window
(a second pass seconds later is still inside it) and a sleep would make the
probe unchainable -- re-run the probe, or query the DB.

And the thing it must NOT do: fire on ordinary runner churn. A probe that
false-positives on normal worker state gets ignored -- the failure mode
`audit_vendored_copies.py`'s NOTE-vs-finding split exists to avoid. So a path
is a FINDING only when it has no counterpart on origin AND parses as a run
manifest (`run_id` + `outcome`). `*_per_tick.jsonl` is by-design local (ZERO
exist anywhere on origin/master -- verified 2026-07-30) and
`runner_status/*.bak.*` is transient telemetry; both are NOTEs, counted and
carried in --json, never printed as findings.

THE LOCAL MAC IS A TARGET TOO (added 2026-07-30)
------------------------------------------------
`FLEET` carried only `ree-cloud-1..4` until 2026-07-30, so DLAPTOP-4 was graded
only by hand. Both halves of the Mac's manual grade close on the same sentence:
nothing automated will notice its next stranded manifest or orphaned autostash.
`DLAPTOP-4` is now an ordinary target, probed IN-PROCESS (no ssh) against
`/Users/dgolden/REE_Working`.

But the Mac is not a worker with a different address, and treating it as one
produces a probe nobody can use. ~18 concurrent Claude sessions hold live
uncommitted work in that checkout, so THE GIT STATE CANNOT DISTINGUISH A STRAND
FROM LIVE WORK. Three discriminators, all learned from the manual grades:

  claims     `TASK_CLAIMS.json` is the discriminator git does not have. An
             untracked path covered by an ACTIVE claim is another session's
             in-flight work and grades as a NOTE, never a finding. Worked
             example: `ree-v3/coordinator/deploy/runner-prestart-pull.sh` was
             untracked, absent from origin/main AND absent from all history --
             a finding by every git-visible test -- and was committed minutes
             later by claim `friendly-antonelli-b0f414`.
  dry-run    `pack_writer.write_flat_manifest` prefixes `_dry_` and sets
             `dry_run: true` when smoking a driver. That residue is manifest-
             shaped, is NOT evidence, and self-clears. It produced the one
             false positive of the 2026-07-30 grade
             (`_dry_v3_exq_748a_..._v3.json`, FAIL, 17.4s), gone by the re-run.
  re-check   a multi_session target is graded TWICE when the first pass finds
             anything, and only findings that survive both are reported. The
             rest are counted as `transient`. This is the write-up's "re-run
             once before acting on any finding whose timestamp is minutes old",
             made automatic instead of advisory.

Plus one blind spot the Mac exposed: `*.bak` is gitignored in REE_assembly
(`.gitignore:13`), and git reports ignored paths as `!! `, never `?? ` -- so the
untracked pass cannot see a plain-`.bak` file at all. `--ignored` grades that
class into a SEPARATE, lower-severity bucket. The blind spot is narrower than it
looks and that is why the cloud finds still worked: `*.bak` matches only names
ENDING in `.bak`, so `foo.json.bak.20260530` -- the actual stranded class --
stays plainly visible as `?? `.

Exit status is 1 if any machine is WEDGED / SKEWED / gc-blocked, so this can
gate a scheduled check. Stranded manifests and stashes REPORT without changing
the exit status -- like the stash signal they are a "look at this now" flag for
a human, not a fault in the checkout, and this script chains. Power state is
NOT inferred -- `hcloud server list` is the authority (CLAUDE.md); an
unreachable host is reported as UNREACHABLE, not as healthy and not as broken.

The probe is READ-ONLY on every target: it never writes, stashes, drops, pulls
or resets, and never touches a running experiment. The ONE exception is
deliberate and local-only: a local target is `git fetch`ed first (`--no-fetch`
to skip), because a RUNNING worker pulls every ~60s while the Mac has no such
loop and its refs can be days old. A fetch updates remote-tracking refs only --
not HEAD, not the index, not the working tree.

EVERY FINDING IS RELATIVE TO THE REF THE BOX CAN SEE, and that ref is not
always current. "A worker pulls every ~60s" holds only while it is RUNNING: a
powered-off or wedged box keeps whatever ref it had, and anything that landed
since then reads as stranded. Confirmed 2026-07-30T17:41Z -- a just-woken
ree-cloud-4 reported `v3_exq_614_..._20260529T191318Z_v3` as a stranded
manifest against an `origin/master` NINE HOURS old, while that run sat on the
real origin/master in both flat and pack form, recovered earlier the same day.
So the graded ref's age is measured on each box and printed beside any finding
older than REF_STALE_WARN. The workers are deliberately NOT fetched -- that
would be a write to a box that may be mid-experiment, against the promise
above, and the runner's own `pull --rebase --autostash` is already contending
for those refs. Labelling the staleness is the honest fix; silently grading
against a stale ref is not.

LABELLING IS NOT THE SAME AS RESOLVING, and for the v3_exq_614 shape it did
not have to stop there (added 2026-07-31). A fresher ref exists without
fetching the worker: the Mac's OWN checkout tracks the same origin, and this
script already fetches it (remote-tracking refs only) before every local
self-grade. So a worker's STRANDED finding is cross-checked, before it is
finalised, against `build_parent_index()` -- a fresh `flat_runs`/`pack_runs`
set built from the PARENT (Mac) checkout's own `REPO_REFS` ref, after running
`_fetch_local` on it. A run_id present there in either flat or pack form is
downgraded from a finding to a `parent_cleared` note rather than reported as a
false-positive strand -- exactly the v3_exq_614 case: STRANDED against
ree-cloud-4's own nine-hour-old ref, present on the REAL origin/master (both
forms) the whole time. This reads ONLY the Mac's own checkout -- never the
worker -- so the read-only promise toward workers is unaffected; the one
non-read-only step anywhere in this file is still the local `git fetch`
documented above. Fails open: an unbuilt or repo-absent parent index leaves
every finding exactly as before (`crosscheck_stranded_against_parent`).

SCOPE. This is primarily the working-tree / untracked half. Full stash
containment grading (arbitrary stash content, not only prepull entries; hunk
reverse-apply; symbol-level containment) is
`REE_Working/scripts/audit_stashes.py`, which is step 7 of the Session
Startup Protocol -- but it runs LOCAL `git` only and covers just the Mac's two
repos. `runner-prepull-untracked` entries specifically (added 2026-07-31) ARE
graded here, fleet-wide, via `grade_prepull_stashes` in the worker-side
`UNTRACKED_PY` grader (containment against the worktree file or `upstream`,
same predicate ree-v3's own reaper uses -- see grade_prepull_stashes'
docstring). That is deliberately the ONE stash class graded here: it is the
one class with a known provenance (the 2026-07-18 orphaned-autostash leak)
and a known remedy, it is small in practice (a handful of entries), and it is
the class this file's own history shows has actually held irreplaceable
evidence (cloud-3, V3-EXQ-673 and V3-EXQ-707c/ARC-110). The generic `stashes`
count remains a bare count and a pointer to `audit_stashes.py` for a Mac
session -- that tool's fuller grading is not reproduced here, and nothing
plays its role for a remote worker.

WHY LITERATURE EVIDENCE ENTRIES ARE GRADED TOO (added 2026-08-19)
-------------------------------------------------------------------
Until this chip, `grade_path`'s only identity test was a run manifest's
`run_id` + `outcome`. A literature evidence entry
(`evidence/literature/<review>/entries/<slug>/record.json` + `summary.md`,
see `evidence/literature/README.md`) has neither, so an untracked one fell
through to the generic basename step -- whose `MAX_CANDIDATES` cap essentially
never happens to try the right one of the ~2200 origin `record.json`/
`summary.md` files -- and ended up a silent `no_counterpart_other` NOTE.
Confirmed (chip-20260819-githealth-untracked-literature-blindspot): a
complete, schema-valid GOV-BEHADJ-1/SD-005/ARC-010 entry sat untracked on the
Mac for 6 days while this probe printed "0 stranded run manifest(s)" and "All
probed checkouts structurally clean." Worse, `build_experiment_indexes.py`'s
literature indexer globs the WORKING TREE, so a regen on that box bakes the
untracked entry into committed derived artifacts as a permanent citation --
see `audit_dangling_citations.py`, which catches the citation half of that
(cited but untracked) but is structurally blind to this half (untracked and
NOT yet cited by anything), since after a later regen on a different box drops
the row again the entry is cited nowhere either.

Identity is the entry SLUG -- the directory name under `entries/` -- rather
than a run_id, graded the same way: present anywhere on origin (any review,
mirroring how a run manifest is graded across flat/pack form) means `clear`;
present under a different slug-review pairing with the SAME slug but
DIFFERENT content is `lit_divergent` (the literature analogue of a phantom-
completion); absent everywhere is `lit_finding`, a genuine strand. Reported in
its OWN count line -- see `literature grading` in the summary -- deliberately
not folded into "stranded run manifest(s)", so that line can never again read
as "nothing is stranded" while a literature entry sits untracked beside it.
Slug uniqueness (the assumption both this and `audit_dangling_citations.py`
rest on) was measured 2213 slugs, 0 collisions across `origin/master`,
2026-08-18.

Deliberately NOT extended to the `--ignored` bucket beyond the generic
dispatch already in `grade_path` (no `.gitignore` rule in REE_assembly matches
`record.json` or `summary.md`, unlike the `*.bak` rule that motivated that
bucket for run manifests) and NOT cross-checked against the PARENT-checkout
staleness correction (`crosscheck_stranded_against_parent`) that run manifests
get: literature entries are authored on the Mac by governance / `/lit-pull`
sessions, never written by a cloud worker's ~60s pull loop, so the stale-
worker-ref shape that correction exists for (`v3_exq_614`, a worker's own ref
being merely OLD) has no literature-entry analogue to correct.

USAGE
-----
    python3 scripts/runner_git_health.py                # whole fleet + the Mac
    python3 scripts/runner_git_health.py --host ree-cloud-2
    python3 scripts/runner_git_health.py --host mac     # DLAPTOP-4, no ssh
    python3 scripts/runner_git_health.py --json
    python3 scripts/runner_git_health.py --ignored      # + gitignored bucket
    python3 scripts/runner_git_health.py --no-untracked # skip the heavier pass
    python3 scripts/runner_git_health.py --selftest     # no ssh, no network
"""

import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
from collections import namedtuple

# One TARGET record per box. This was `{name: (ip, role)}` with the path layout
# hardcoded into PROBE and into build_probe's grader argv; that is exactly what
# kept the Mac ungradeable, because the Mac differs from a worker in BOTH
# dimensions -- no ssh hop, and a different checkout root. Carrying `base` and
# `ip` on the record means neither dimension needs a per-call-site branch: the
# only place transport is decided is probe()'s two-line dispatch.
#
#   name          affinity / hostname, as used by --host and by the heartbeats
#   role          display label only
#   base          directory CONTAINING the repo checkouts (base/REE_assembly, ...)
#   ip            ssh host, or None for a target probed in-process
#   multi_session True when many writers share the checkout -- see below
Target = namedtuple("Target", "name role base ip multi_session")

REMOTE_BASE = "/home/ree/REE_Working"
LOCAL_BASE = "/Users/dgolden/REE_Working"

# Affinity name -> record. Mirrors the table in CLAUDE.md ("Workers may need
# waking"). ree-cloud-1 is the HUB (coordinator + sync_daemon); it is probed
# read-only like any other, but never act on it without care -- its writers are
# the coordination-data plane for the whole fleet.
#
# DLAPTOP-4 is the Mac. It was absent from this table until 2026-07-30, so it
# was the one box in the fleet graded ONLY by manual one-off write-ups
# (evidence/planning/recovered_stranded_manifests/README_DLAPTOP-4_2026-07-30.md
# and README_DLAPTOP-4_stash_2026-07-30.md, whose closing sections both name
# this gap). Nothing automated would have noticed its next stranded manifest.
FLEET = {
    "ree-cloud-1": Target("ree-cloud-1", "hub", REMOTE_BASE, "91.98.130.117", False),
    "ree-cloud-2": Target("ree-cloud-2", "worker", REMOTE_BASE, "116.203.216.181", False),
    "ree-cloud-3": Target("ree-cloud-3", "worker", REMOTE_BASE, "46.62.170.133", False),
    "ree-cloud-4": Target("ree-cloud-4", "worker", REMOTE_BASE, "91.99.68.94", False),
    "DLAPTOP-4": Target("DLAPTOP-4", "local", LOCAL_BASE, None, True),
}

# `--host mac` / `--host local` / `--host dlaptop-4` all mean the Mac. Matching
# is case-insensitive on top of this, because the hostname is spelled
# `DLAPTOP-4` in heartbeats and `DLAPTOP-4.local` by the OS.
HOST_ALIASES = {"mac": "DLAPTOP-4", "local": "DLAPTOP-4",
                "dlaptop-4.local": "DLAPTOP-4"}

# Where the shared claim registry lives. Read-only, and only consulted for a
# multi_session target -- see claims_for_target().
CLAIMS_PATH = os.path.join(LOCAL_BASE, "TASK_CLAIMS.json")

# Upstream ref per repo -- what an untracked file is graded AGAINST. These are
# the default branches from CLAUDE.md's push table, not `@{u}`, because a
# worker's HEAD can be detached or on a stale branch and the question being
# asked is "does this content exist on the trunk everyone else reads".
REPO_REFS = {
    "REE_assembly": "origin/master",
    "ree-v3": "origin/main",
}
REPOS = tuple(REPO_REFS)

# A worker pulls every ~60s, so a healthy checkout is within a handful of
# commits of origin. This threshold only drives the advisory BEHIND label --
# WEDGED / SKEW / GC-BLOCKED are structural and are never threshold-based.
BEHIND_WARN = 50

# Hours after which the GRADED REF is called out beside any finding it could
# explain. A running worker pulls every ~60s, so its ref is minutes old; two
# hours therefore only ever fires on a box that was powered off or wedged --
# which is exactly when a "stranded" manifest is most likely to be a landed one
# the box has not seen yet. See classify() for the confirmed incident.
REF_STALE_WARN = 2.0

# Probe script. Emits one "repo|k=v|..." line per repo. Kept POSIX-sh simple
# and read-only: it must never mutate any target's tree. `$REE_BASE` and
# `$REE_REPOS` are prepended by shell_probe() from the TARGET RECORD -- they
# were hardcoded to /home/ree/REE_Working until 2026-07-30, which is what made
# a local target impossible to express.
PROBE = r'''
for r in $REE_REPOS; do
  d=$REE_BASE/$r
  if [ ! -d "$d/.git" ]; then echo "$r|missing=1"; continue; fi
  cd "$d" || { echo "$r|missing=1"; continue; }
  unmerged=$(git ls-files -u 2>/dev/null | awk '{print $4}' | sort -u | wc -l | tr -d ' ')
  # BOTH skew forms: ' D' (mixed reset, unstaged) and 'D ' (soft/update-ref,
  # PRE-STAGED -- a bare commit lands the deletions immediately).
  skew=$(git status --porcelain 2>/dev/null | grep -cE '^( D|D )' | tr -d ' ')
  gclog=$([ -f .git/gc.log ] && echo 1 || echo 0)
  stashes=$(git stash list 2>/dev/null | wc -l | tr -d ' ')
  # Prepull entries specifically: residue of the orphaned-stash leak fixed
  # 2026-07-30 (experiment_runner.git_pull popped from only 3 of 5 exit
  # paths). These are the ones that have actually held irreplaceable run
  # manifests, so they are worth calling out by name rather than folding
  # into the generic stash count.
  prepull=$(git stash list --format='%gs' 2>/dev/null | grep -c 'runner-prepull-untracked' | tr -d ' ')
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  behind=$(git rev-list --count HEAD..@{u} 2>/dev/null || echo -1)
  first=$(git ls-files -u 2>/dev/null | awk '{print $4}' | sort -u | head -1)
  echo "$r|branch=$branch|unmerged=$unmerged|behind=$behind|skew=$skew|gclog=$gclog|stashes=$stashes|prepull=$prepull|first=$first"
done
'''

# Worker-side UNTRACKED grader. Shipped as source and executed on the worker so
# only the summary crosses the wire (an `ls-tree -r` of REE_assembly is tens of
# thousands of paths). Kept as a standalone program taking `<base> <repo>:<ref>
# ...` on argv so that --selftest can run THIS EXACT SOURCE against a temp git
# repo locally -- a grader that has only ever run against healthy trees is
# unverified, which is how the 490h manifest stayed hidden for two months.
#
# READ-ONLY. Every git call here is status / ls-tree / show.
UNTRACKED_PY = r'''
import hashlib, json, os, re, subprocess, sys, time

MAX_FINDINGS = 25
MAX_BYTES = 8 * 1024 * 1024
MAX_CANDIDATES = 8
MAX_OTHER_PATHS = 10
# Ignored entries are only reachable via --ignored and are bounded separately:
# the bucket exists to catch a manifest hiding behind a *.bak-style rule, not to
# enumerate a tree. Anything past the cap is counted, never silently dropped.
MAX_IGNORED_SCAN = 500
# Prepull stash grading (added for the containment report -- see
# grade_prepull_stashes below). A prepull entry has historically held 1-3
# files; these bound a pathological box without ever silently dropping a
# path -- anything past the cap is counted (`beyond_scan_cap`) and the entry
# fails CLOSED to "at_risk", never silently cleared.
MAX_PREPULL_ENTRIES = 50
MAX_PREPULL_PATHS = 25
PREPULL_LABEL = "runner-prepull-untracked"

# By-design-local paths. Verified 2026-07-30 against origin/master: ZERO
# *_per_tick.jsonl blobs exist there, so their absence from origin is the
# design and not a loss. runner_status / runner_commands / runner_heartbeats
# are transient telemetry; the three dirs were retired from origin 2026-09-06 and
# nothing materialises them any more -- still graded as noise, not findings.
# These become NOTES, never findings -- see the module docstring on why a
# probe that false-positives on ordinary runner churn gets ignored.
#
# _runner_signals/<QUEUE_ID>.json is the entry that is NOT merely noise-
# suppression: those files carry BOTH `run_id` and `outcome`, so the manifest
# test below grades them as run manifests. They are runner EXIT SIGNALS that
# POINT at a manifest via `manifest_path` -- never the manifest itself. On the
# Mac the directory is .gitignore'd (so inert), but anywhere it is untracked
# rather than ignored the grader emits up to MAX_FINDINGS spurious findings
# plus a truncated tail. Confirmed 2026-07-30 (DLAPTOP-4, 40 files); write-up
# in evidence/planning/recovered_stranded_manifests/README_DLAPTOP-4_2026-07-30.md.
BYDESIGN = (
    (re.compile(r"_per_tick\.jsonl$"), "per_tick"),
    (re.compile(r"(^|/)runner_status/"), "runner_status"),
    (re.compile(r"(^|/)runner_commands/"), "runner_commands"),
    (re.compile(r"(^|/)runner_heartbeats/"), "runner_heartbeats"),
    (re.compile(r"(^|/)_runner_signals/"), "runner_signals"),
)
CHURN = re.compile(
    r"(^|/)(__pycache__|\.mypy_cache|\.pytest_cache|node_modules|\.venv)(/|$)"
    r"|\.pyc$|(^|/)\.DS_Store$")
# ".bak.20260530", ".bak.phantom-clean", plain ".bak". Greedy, so the LAST
# ".bak" splits -- stripping this is what made the 490h manifest findable.
BAK = re.compile(r"^(.*)\.bak(?:\..*)?$")

# A literature evidence entry: evidence/literature/<review>/entries/<slug>/
# (record.json|summary.md). The slug (group 1) is graded like a run manifest's
# run_id -- see the module docstring's "WHY LITERATURE EVIDENCE ENTRIES ARE
# GRADED TOO" -- because it, not the path, is what audit_dangling_citations.py
# and the claim_evidence indexer both key on, and it is globally unique across
# reviews (2213 slugs, 0 collisions, verified 2026-08-18).
LIT_ENTRY = re.compile(
    r"^evidence/literature/[^/]+/entries/([^/]+)/(record\.json|summary\.md)$")

# --dry-run smoke residue. TWO independent signals, both set by
# ree-v3 experiments/pack_writer.py:520 / :341 under `dry_run`: the filename
# gets a `_dry_` prefix and the manifest doc gets `dry_run: true`. Either is
# sufficient; both are checked because a driver can write its own manifest.
# A dry-run manifest is by CONSTRUCTION not evidence (one seed, toy episodes --
# see experiment_protocol._relocate_dry_run_manifest), so it is a note whatever
# its duration. The sub-20s `elapsed_seconds` of the 2026-07-30 false positive
# is corroborating, not the discriminator: keying on it would have to guess a
# threshold, and a slow smoke is still a smoke.
DRY_PREFIX = "_dry_"


def git(cwd, *args):
    p = subprocess.run(("git",) + args, cwd=cwd,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", "replace")


def as_json(text):
    try:
        return json.loads(text)
    except Exception:
        return None


def is_superset(origin, local):
    """True if every key/value of `local` is present and equal in `origin`.

    The phase3 git writer stores compact JSON and INJECTS queue_id / machine /
    epistemic_category / evidence_direction_note, so origin is routinely a
    strict superset of a semantically identical local file. A byte compare
    would call every one of those stranded.
    """
    if not isinstance(origin, dict) or not isinstance(local, dict):
        return origin == local
    for k, v in local.items():
        if k not in origin or origin[k] != v:
            return False
    return True


def load_local(root, rel):
    """(raw_text, parsed_doc) for one working-tree path. Never raises."""
    full = os.path.join(root, rel)
    raw = None
    doc = None
    try:
        if os.path.isfile(full) and os.path.getsize(full) <= MAX_BYTES:
            with open(full, "rb") as fh:
                raw = fh.read().decode("utf-8", "replace")
            doc = as_json(raw)
    except Exception:
        pass
    return raw, doc


def grade_path(root, ref, rel, idx):
    """Decide ONE working-tree path against origin.

    Returns ``("clear", None)``, ``("finding", {...})``, ``("divergent",
    {...})`` or ``("note", tag)``. `finding` is "this run exists nowhere on
    origin"; `divergent` is "it does, but not as this content" -- kept apart
    because the remedy differs and because the strand text asserts, truthfully,
    that a strand has NO counterpart at any path.

    Factored out of grade_repo's loop on 2026-07-30 so the --ignored bucket
    grades by exactly the same rules rather than by a second, drifting copy --
    a gitignored manifest is the same loss as an untracked one, and a bucket
    that graded it more loosely would be worse than not having it.
    """
    if CHURN.search(rel):
        return "ignored", None
    base = rel.rsplit("/", 1)[-1]
    m = BAK.match(base)
    stem = m.group(1) if m else None

    raw, doc = load_local(root, rel)

    run_id = ""
    if isinstance(doc, dict) and doc.get("run_id") and doc.get("outcome"):
        run_id = str(doc["run_id"])

    # 0) A BYDESIGN path is NEVER graded as a run manifest, however
    #    manifest-shaped it looks. Dropping run_id here (rather than
    #    relying on the tag scan at the bottom) is what actually
    #    suppresses it: the finding branch below fires FIRST, so a
    #    _runner_signals/*.json -- run_id + outcome, but only a POINTER to
    #    a manifest -- would otherwise never reach that scan.
    forced = ""
    if run_id:
        for rx, name in BYDESIGN:
            if rx.search(rel):
                run_id, forced = "", name
                break
    # 0b) ...and neither is --dry-run smoke residue, on either signal.
    if run_id and (base.startswith(DRY_PREFIX)
                   or (isinstance(doc, dict) and doc.get("dry_run") is True)):
        run_id, forced = "", "dry_run"

    # 1) Run-manifest grading. A run whose id is on origin ANYWHERE -- flat
    #    `<run_id>.json` or pack `.../runs/<run_id>/manifest.json` -- is not
    #    stranded, whatever the local copy happens to be called. Note the index
    #    is built from a whole-tree `ls-tree -r`, so this also clears a copy
    #    parked outside the live evidence paths (the recovery procedure files
    #    them under evidence/planning/recovered_stranded_manifests/, deliberately
    #    outside evidence/experiments/ so the indexer cannot score them).
    #
    #    Membership is NOT sufficient to clear. Matching the run_id and then
    #    returning without reading either file cannot distinguish "already
    #    landed" from "landed as something else" -- and the second is the
    #    worse case, since two divergent manifests for one run_id is the
    #    phantom-completion / partial-write shape. Verify content first.
    if run_id and (run_id in idx["flat_runs"] or run_id in idx["pack_runs"]):
        cands = idx.get("runpaths", {}).get(run_id, ())
        if origin_match(root, ref, doc, raw, cands) is not False:
            return "clear", None
        # content_sha256 of the LOCAL copy, not the origin one -- this is what
        # lets a future run recognise "the exact bytes a human already
        # adjudicated benign", so an adjudication can never silently swallow a
        # genuinely NEW divergence on the same run_id (only a byte-identical
        # re-report of the one already reviewed). None when the file could not
        # be read, so an unreadable local file can never spuriously match.
        return "divergent", {
            "path": rel,
            "run_id": run_id,
            "outcome": str(doc.get("outcome"))[:40],
            "elapsed_seconds": doc.get("elapsed_seconds"),
            "bytes": len(raw or ""),
            "origin_paths": list(cands)[:MAX_CANDIDATES],
            "content_sha256": (hashlib.sha256(raw.encode("utf-8")).hexdigest()
                                if raw is not None else None),
        }

    # 1L) LITERATURE-ENTRY grading. Same shape as step 1, keyed on the entry
    #     SLUG instead of a run_id (see module docstring, "WHY LITERATURE
    #     EVIDENCE ENTRIES ARE GRADED TOO"). Deliberately intercepts BEFORE
    #     step 2: basename "record.json"/"summary.md" is shared by every
    #     entry in the corpus (~2200 each), so step 2's MAX_CANDIDATES cap
    #     would almost never happen to try this entry's own origin path --
    #     that gap is exactly what let a real stranded entry read as an
    #     un-triageable "no_counterpart_other" note for 6 days.
    m_lit = LIT_ENTRY.match(rel)
    if m_lit:
        slug = m_lit.group(1)
        same_slug = idx.get("lit_paths", {}).get(slug, ())
        cands = [p for p in same_slug if p.rsplit("/", 1)[-1] == base]
        for p in cands[:MAX_CANDIDATES]:
            blob = git(root, "show", "%s:%s" % (ref, p))
            if blob is None:
                continue
            if base == "record.json":
                odoc = as_json(blob)
                if doc is not None and odoc is not None and is_superset(odoc, doc):
                    return "clear", None
            elif raw is not None and blob == raw:
                return "clear", None
        if cands:
            # The slug AND this exact filename both exist on origin, but no
            # candidate's content matched -- a rewritten / re-classified
            # entry, not a strand. Same shape as run-manifest DIVERGENT: one
            # of the two copies disagrees and which is right is not knowable
            # from here.
            return "lit_divergent", {
                "path": rel,
                "slug": slug,
                "kind": base,
                "bytes": len(raw or ""),
                "origin_paths": cands[:MAX_CANDIDATES],
                "content_sha256": (hashlib.sha256(raw.encode("utf-8")).hexdigest()
                                    if raw is not None else None),
            }
        if same_slug:
            # The slug exists on origin (its OTHER file landed) but not this
            # one -- a partial landing, not a full strand; the missing half
            # is more precise than "stranded".
            return "note", "literature_partial"
        return "lit_finding", {
            "path": rel, "slug": slug, "kind": base, "bytes": len(raw or ""),
        }

    # 2) Basename grading, on the name AND on the de-.bak'd stem.
    cands = list(idx["byname"].get(base, ()))
    if stem:
        cands += idx["byname"].get(stem, ())
    for p in cands[:MAX_CANDIDATES]:
        blob = git(root, "show", "%s:%s" % (ref, p))
        if blob is None:
            continue
        odoc = as_json(blob)
        if doc is not None and odoc is not None:
            if is_superset(odoc, doc):
                return "clear", None
        elif raw is not None and blob == raw:
            return "clear", None

    # FINDING only for a real run manifest with no counterpart anywhere.
    if run_id:
        return "finding", {
            "path": rel,
            "run_id": run_id,
            "outcome": str(doc.get("outcome"))[:40],
            "elapsed_seconds": doc.get("elapsed_seconds"),
            "bytes": len(raw or ""),
        }

    tag = forced
    if not tag:
        tag = "no_counterpart_other"
        for rx, name in BYDESIGN:
            if rx.search(rel):
                tag = name
                break
    return "note", tag


def build_index(tree):
    """Origin-side lookup tables: basename -> paths, and the two run-id sets.

    `runpaths` (run_id -> the origin paths that carry it) exists so step 1 of
    grade_path can COMPARE CONTENT before clearing. The two sets alone answer
    "does this run_id exist on origin", which is not the same question as "is
    the local copy the same run".

    `lit_paths` (slug -> the origin paths -- record.json AND/OR summary.md --
    that carry it) is the literature-entry counterpart, keyed on LIT_ENTRY's
    slug rather than a run_id, for the same reason and the same shape.
    """
    byname = {}
    flat_runs = set()
    pack_runs = set()
    runpaths = {}
    lit_paths = {}
    for p in tree:
        b = p.rsplit("/", 1)[-1]
        byname.setdefault(b, []).append(p)
        if b.endswith(".json"):
            flat_runs.add(b[:-5])
            runpaths.setdefault(b[:-5], []).append(p)
        i = p.find("/runs/")
        if i != -1:
            rest = p[i + 6:]
            j = rest.find("/")
            if j > 0:
                pack_runs.add(rest[:j])
                runpaths.setdefault(rest[:j], []).append(p)
        m = LIT_ENTRY.match(p)
        if m:
            lit_paths.setdefault(m.group(1), []).append(p)
    return {"byname": byname, "flat_runs": flat_runs, "pack_runs": pack_runs,
            "runpaths": runpaths, "lit_paths": lit_paths}


def origin_match(root, ref, doc, raw, paths):
    """Tri-state: True some candidate matches, False all differ, None unknown.

    None is the fail-SAFE value and is treated as a match by every caller: an
    unreadable or unparseable candidate is not evidence of divergence, and this
    module's usefulness rests entirely on not manufacturing findings it cannot
    stand over (module docstring; the BYDESIGN and --dry-run suppressions exist
    for the same reason).

    Uses is_superset, not a byte compare, for the same reason step 2 does --
    the phase3 writer injects fields, so origin is routinely a strict superset
    of a semantically identical local file.
    """
    decided = False
    for p in list(paths)[:MAX_CANDIDATES]:
        blob = git(root, "show", "%s:%s" % (ref, p))
        if blob is None:
            continue
        odoc = as_json(blob)
        if doc is not None and odoc is not None:
            decided = True
            if is_superset(odoc, doc):
                return True
        elif raw is not None and blob == raw:
            return True
    return False if decided else None


def grade_ignored(root, ref, idx):
    """Grade GITIGNORED paths into a separate, lower-severity bucket.

    Why this exists: the untracked pass takes only `?? ` entries, and git
    reports an ignored path as `!! `. `REE_assembly/.gitignore:13` is `*.bak`,
    so EVERY plain-`.bak` file is invisible to that pass in this repo. The
    2026-07-30 Mac grade had to enumerate the 47-file ignored set by hand to
    say anything about the class; it found no run manifests, but "graded once,
    by hand" is not coverage.

    Deliberately does NOT descend into an ignored DIRECTORY. git collapses one
    to a single `dir/` entry, and on the Mac `.claude/` alone is ~50 worktrees.
    The motivating rule is a FILE pattern, so file-level is the honest scope --
    and the directories skipped are counted and reported rather than implied
    covered.
    """
    st = git(root, "status", "--porcelain", "-uall", "--ignored=matching", "-z")
    if st is None:
        return {"error": "git status --ignored failed"}
    entries = [e[3:] for e in st.split("\0") if e[:3] == "!! "]
    findings = []
    divergent = []
    dirs = 0
    scanned = 0
    beyond_cap = 0
    for rel in entries:
        if rel.endswith("/"):
            dirs += 1
            continue
        if scanned >= MAX_IGNORED_SCAN:
            beyond_cap += 1
            continue
        scanned += 1
        kind, payload = grade_path(root, ref, rel, idx)
        if kind == "finding" and len(findings) < MAX_FINDINGS:
            findings.append(payload)
        # Carried rather than dropped: this bucket exists BECAUSE `*.bak` made
        # a whole class invisible, so silently discarding a second class here
        # would repeat the defect it was built to fix.
        elif kind == "divergent" and len(divergent) < MAX_FINDINGS:
            divergent.append(payload)
    return {"entries": len(entries), "files_graded": scanned, "dirs_skipped": dirs,
            "beyond_cap": beyond_cap, "findings": findings,
            "divergent": divergent}


def ref_age_hours(root, ref):
    """Age of the graded ref, computed on the box that holds it.

    Everything here is graded against `ref`, so a STALE ref manufactures
    strands out of content that landed after it. The age is computed locally
    (both `git log` and the clock are on the same box) so cross-machine clock
    skew cannot distort it, and it is returned as a NUMBER so the reporting
    side stays time-independent and testable.

    Returns None when it cannot be determined -- absence is reported, never
    silently treated as fresh.
    """
    txt = git(root, "log", "-1", "--format=%ct", ref)
    try:
        return round((time.time() - int((txt or "").strip())) / 3600.0, 2)
    except Exception:
        return None


def _stash_list_entries(root):
    """[(ref, subject), ...] for every stash entry, newest first. Never raises.

    %gs is the reflog SUBJECT, e.g. "On master: runner-prepull-untracked" --
    the same substring the shell probe's PROBE script greps for, so the two
    counts agree by construction.
    """
    out = git(root, "stash", "list", "--format=%gd\x1f%gs")
    if out is None:
        return []
    entries = []
    for line in out.splitlines():
        parts = line.split("\x1f")
        if len(parts) != 2:
            continue
        entries.append((parts[0], parts[1]))
    return entries


def _stash_untracked_paths(root, stash_ref):
    """Repo-relative paths held in a `-u` stash's untracked THIRD-PARENT commit.

    A stash made with --include-untracked stores the untracked files in a
    THIRD parent commit, `<stash_ref>^3` -- invisible to `git stash show`,
    which reports only the tracked diff. Since a runner-prepull-untracked
    stash holds nothing BUT untracked files, `^3` is the only place its
    content is reachable. Mirrors ree-v3 experiment_runner.py's
    `_stash_untracked_paths` (4028f06) -- same shape, ported rather than
    imported because this repo has no cross-repo import path onto ree-v3 (the
    vendored-copy rule in CLAUDE.md: it works on the Mac and breaks on a
    worker that never cloned ree-v3 at that path).

    Returns None (not []) when `^3` cannot be enumerated at all -- e.g. a
    stash taken WITHOUT --include-untracked, which the label alone cannot
    rule out. That distinguishes "not a -u stash" from "a -u stash with
    nothing in it", and the caller reports the two differently.
    """
    out = git(root, "ls-tree", "-r", "--name-only", "%s^3" % stash_ref)
    if out is None:
        return None
    return [ln for ln in out.splitlines() if ln]


def _path_contained(root, stash_ref, upstream, rel):
    """Is `rel`'s stashed content (`<stash_ref>^3:<rel>`) PROVABLY already
    carried by the worktree file at that path, or by `upstream`?

    Two places are checked, either sufficient -- the worktree file is what a
    real collision lands on, `upstream` is what the fleet actually reads.
    CONTAINMENT, not equality, same predicate as `is_superset` /
    ree-v3's `_json_content_contained`: a governance-reviewed landed copy
    adds a reviewer note / changed `evidence_direction` on top of what the
    worker wrote, so an equality test would leave every reviewed run's entry
    graded at_risk forever. Fails CLOSED: unreadable stash content, or no
    match anywhere, is NOT contained.
    """
    stashed = git(root, "show", "%s^3:%s" % (stash_ref, rel))
    if stashed is None:
        return False
    stashed_doc = as_json(stashed)

    full = os.path.join(root, rel)
    try:
        if os.path.isfile(full):
            with open(full, "rb") as fh:
                local_raw = fh.read().decode("utf-8", "replace")
            if local_raw == stashed:
                return True
            local_doc = as_json(local_raw)
            if (stashed_doc is not None and local_doc is not None
                    and is_superset(local_doc, stashed_doc)):
                return True
    except Exception:
        pass

    up = git(root, "show", "%s:%s" % (upstream, rel))
    if up is not None:
        if up == stashed:
            return True
        up_doc = as_json(up)
        if (stashed_doc is not None and up_doc is not None
                and is_superset(up_doc, stashed_doc)):
            return True
    return False


def grade_prepull_stashes(root, upstream):
    """GRADE each runner-prepull-untracked stash entry for containment.

    Replaces a bare count with a per-entry verdict: "redundant" (every path
    is provably already carried by the worktree or by `upstream`, so the
    entry is a safe retirement candidate) vs "at_risk" (at least one path is
    proven nowhere else, so it may be the ONLY copy). This is the read-only,
    fleet-wide counterpart to the ree-v3 runner's own reaper
    (experiment_runner.py, commit 4028f06 "retire a collided prepull stash
    entry whose content already landed"), which acts on the identical
    predicate but only on the box it is running on and only at pop time. No
    equivalent runs on a powered-off or pre-fix worker, which is exactly the
    box this probe is for.

    REPORTING ONLY. Never pops, drops, archives, or otherwise mutates a
    stash -- this module's whole contract is read-only (module docstring).
    """
    entries = [(r, s) for r, s in _stash_list_entries(root) if PREPULL_LABEL in s]
    truncated_entries = max(0, len(entries) - MAX_PREPULL_ENTRIES)
    graded = []
    for stash_ref, _subject in entries[:MAX_PREPULL_ENTRIES]:
        paths = _stash_untracked_paths(root, stash_ref)
        if paths is None:
            graded.append({"ref": stash_ref, "verdict": "unreadable",
                           "reason": "could not enumerate %s^3" % stash_ref})
            continue
        if not paths:
            graded.append({"ref": stash_ref, "verdict": "unreadable",
                           "reason": "no untracked (^3) parent -- not a "
                                     "--include-untracked stash"})
            continue
        scanned = paths[:MAX_PREPULL_PATHS]
        beyond = len(paths) - len(scanned)
        unproven = [rel for rel in scanned
                    if _path_contained(root, stash_ref, upstream, rel) is not True]
        entry = {"ref": stash_ref, "paths": len(paths)}
        # Any path beyond the scan cap is UNPROVEN by construction -- fail
        # closed rather than clear an entry on the strength of paths it never
        # actually checked.
        redundant = not unproven and beyond == 0
        entry["verdict"] = "redundant" if redundant else "at_risk"
        if unproven:
            entry["unproven_paths"] = unproven[:MAX_CANDIDATES]
        if beyond:
            entry["beyond_scan_cap"] = beyond
        graded.append(entry)

    out = {
        "count": len(entries),
        "graded_count": len(graded),
        "redundant": sum(1 for g in graded if g["verdict"] == "redundant"),
        "at_risk": sum(1 for g in graded if g["verdict"] == "at_risk"),
        "unreadable": sum(1 for g in graded if g["verdict"] == "unreadable"),
        "entries": graded,
    }
    if truncated_entries:
        out["truncated_entries"] = truncated_entries
    return out


def grade_repo(root, ref, do_ignored=False):
    st = git(root, "status", "--porcelain", "-uall", "-z")
    if st is None:
        return {"error": "git status failed"}
    untracked = [e[3:] for e in st.split("\0") if e[:3] == "?? "]

    tree_txt = git(root, "ls-tree", "-r", "--name-only", "-z", ref)
    if tree_txt is None:
        # No such ref (detached / never fetched). Say so rather than declaring
        # every untracked path stranded against a tree we could not read.
        return {"error": "ref not readable: " + ref, "untracked": len(untracked)}
    tree = [p for p in tree_txt.split("\0") if p]
    idx = build_index(tree)

    findings = []
    divergent = []
    lit_findings = []
    lit_divergent = []
    notes = {}
    other_paths = []
    ignored = 0
    truncated = 0
    lit_truncated = 0
    for rel in untracked:
        kind, payload = grade_path(root, ref, rel, idx)
        if kind == "clear":
            continue
        if kind == "ignored":
            ignored += 1
            continue
        if kind == "divergent":
            if len(divergent) < MAX_FINDINGS:
                divergent.append(payload)
            continue
        if kind == "lit_divergent":
            if len(lit_divergent) < MAX_FINDINGS:
                lit_divergent.append(payload)
            continue
        if kind == "finding":
            if len(findings) >= MAX_FINDINGS:
                truncated += 1
                continue
            findings.append(payload)
            continue
        if kind == "lit_finding":
            if len(lit_findings) >= MAX_FINDINGS:
                lit_truncated += 1
                continue
            lit_findings.append(payload)
            continue
        notes[payload] = notes.get(payload, 0) + 1
        # NAME the un-attributable ones (bounded). They stay NOTES -- not run
        # manifests, so not the loss class this fires on -- but a bare count is
        # not triageable, and the first live run turned up two planning docs
        # (evidence/planning/sd037_consumer_input_distributions_*.md on
        # ree-cloud-4) absent from origin. Carried in --json only, so the
        # default output's noise budget is unchanged.
        if payload == "no_counterpart_other" and len(other_paths) < MAX_OTHER_PATHS:
            other_paths.append(rel)

    out = {"untracked": len(untracked), "ignored": ignored,
           "findings": findings, "divergent": divergent,
           "truncated": truncated, "notes": notes,
           "literature_findings": lit_findings,
           "literature_divergent": lit_divergent,
           "literature_truncated": lit_truncated,
           "no_counterpart_other_paths": other_paths,
           "ref": ref, "ref_age_hours": ref_age_hours(root, ref),
           "prepull": grade_prepull_stashes(root, ref)}
    if do_ignored:
        out["gitignored"] = grade_ignored(root, ref, idx)
    return out


def main():
    argv = sys.argv[1:]
    do_ignored = "--ignored" in argv
    # --index-only: emit just the origin-side run_id index (flat_runs /
    # pack_runs from build_index) instead of a full grade_repo() pass. Added
    # so the PARENT (Mac) checkout can hand its own fresh index back to the
    # top-level driver for cross-checking a WORKER's STRANDED finding --
    # reusing build_index() itself rather than a second, drifting copy of the
    # flat/pack membership test grade_path's step 1 already applies.
    index_only = "--index-only" in argv
    rest = [a for a in argv if not a.startswith("--")]
    base = rest[0]
    out = {}
    for spec in rest[1:]:
        repo, _, ref = spec.partition(":")
        root = os.path.join(base, repo)
        if not os.path.isdir(os.path.join(root, ".git")):
            continue
        if index_only:
            tree_txt = git(root, "ls-tree", "-r", "--name-only", "-z", ref)
            if tree_txt is None:
                out[repo] = {"error": "ref not readable: " + ref}
                continue
            tree = [p for p in tree_txt.split("\0") if p]
            idx = build_index(tree)
            out[repo] = {"flat_runs": sorted(idx["flat_runs"]),
                         "pack_runs": sorted(idx["pack_runs"])}
        else:
            out[repo] = grade_repo(root, ref, do_ignored=do_ignored)
    sys.stdout.write("UNTRACKED_JSON " + json.dumps(out, sort_keys=True) + "\n")


main()
'''

UNTRACKED_MARKER = "UNTRACKED_JSON "


def grader_specs():
    return [f"{r}:{ref}" for r, ref in sorted(REPO_REFS.items())]


def shell_probe(base):
    """PROBE with its base and repo list bound from the target record."""
    return (f"REE_BASE={base}\nREE_REPOS='{' '.join(REPOS)}'\n" + PROBE)


def build_probe(base, untracked=True, ignored=False):
    """Assemble the remote script. One ssh, one `sh -s`, read-only throughout.

    The grader is base64'd rather than heredoc'd: the script itself arrives on
    the worker's stdin, and a heredoc would then have to be read from that same
    stream. base64 keeps it a single argument with no quoting hazards.

    Used only for an SSH target. A local target runs the two pieces directly
    (see _probe_local) rather than round-tripping through base64 -- macOS's BSD
    `base64` historically spells decode `-D`, not `-d`, so reusing this form
    locally would work on the workers and fail on the one box it was added for.
    """
    if not untracked:
        return shell_probe(base)
    blob = base64.b64encode(UNTRACKED_PY.encode("utf-8")).decode("ascii")
    args = " ".join(grader_specs()) + (" --ignored" if ignored else "")
    return (
        shell_probe(base)
        + f"printf '%s' '{blob}' | base64 -d | python3 - {base} {args}\n"
    )


def parse_probe_output(stdout):
    """Split the probe's stdout into (per-repo dict, grader dict)."""
    out = {}
    graded = {}
    for line in stdout.splitlines():
        if line.startswith(UNTRACKED_MARKER):
            try:
                graded = json.loads(line[len(UNTRACKED_MARKER):])
            except Exception:
                graded = {}
            continue
        parts = line.strip().split("|")
        if len(parts) < 2:
            continue
        d = {}
        for kv in parts[1:]:
            if "=" in kv:
                k, _, v = kv.partition("=")
                d[k] = v
        out[parts[0]] = d
    return out, graded


def _attach(out, graded):
    for repo, info in (graded or {}).items():
        if repo in out and isinstance(info, dict):
            out[repo]["untracked"] = info
    return out


def probe(target, timeout=180, untracked=True, ignored=False, fetch=True,
          recheck=True):
    """Probe one target. Returns (repos_dict, error_or_None).

    Transport is decided HERE and nowhere else: a target with no `ip` is graded
    in-process. Every other difference between the Mac and a worker rides on
    the record (`base`, `multi_session`).
    """
    if target.ip is None:
        return _probe_local(target, timeout, untracked, ignored, fetch, recheck)
    return _probe_ssh(target, timeout, untracked, ignored)


def _probe_ssh(target, timeout, untracked, ignored):
    try:
        r = subprocess.run(
            ["ssh", "-o", "ConnectTimeout=15", "-o", "BatchMode=yes",
             f"ree@{target.ip}", "sh -s"],
            input=build_probe(target.base, untracked, ignored),
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None, "probe timed out"
    except Exception as exc:                      # pragma: no cover - defensive
        return None, f"probe failed: {exc}"
    if r.returncode != 0:
        return None, (r.stderr or "").strip().splitlines()[-1] if r.stderr else "ssh failed"
    out, graded = parse_probe_output(r.stdout)
    return _attach(out, graded), None


def _fetch_local(base, timeout=120):
    """Refresh remote-tracking refs. The one non-read-only step, local only.

    A worker pulls every ~60s, so its `origin/master` is current by
    construction. The Mac's can be days stale, and every untracked path is
    graded AGAINST that ref -- a stale ref reports content that landed
    yesterday as stranded. Updates remote-tracking refs only: not HEAD, not the
    index, not the working tree, so it is safe beside ~18 live sessions.

    Returns a list of human-readable failures; a failure is reported, never
    fatal (offline is normal, and a stale-ref grade is still worth having as
    long as its staleness is stated).
    """
    problems = []
    for repo, ref in sorted(REPO_REFS.items()):
        root = os.path.join(base, repo)
        if not os.path.isdir(os.path.join(root, ".git")):
            continue
        remote, _, branch = ref.partition("/")
        try:
            r = subprocess.run(["git", "-C", root, "fetch", "-q", remote, branch],
                               capture_output=True, text=True, timeout=timeout)
            if r.returncode != 0:
                tail = (r.stderr or "").strip().splitlines()
                problems.append(f"{repo}: {tail[-1] if tail else 'fetch failed'}")
        except Exception as exc:
            problems.append(f"{repo}: fetch failed ({exc})")
    return problems


def _run_grader_local(base, ignored, timeout):
    """Execute UNTRACKED_PY in-process-adjacent -- same source, no ssh, no base64."""
    args = [sys.executable, "-", base] + grader_specs()
    if ignored:
        args.append("--ignored")
    r = subprocess.run(args, input=UNTRACKED_PY, capture_output=True,
                       text=True, timeout=timeout)
    _, graded = parse_probe_output(r.stdout)
    return graded


def _run_index_local(base, timeout):
    """UNTRACKED_PY's --index-only mode against `base` -- no ssh, no base64.

    Returns ``{repo: {"flat_runs": [...], "pack_runs": [...]}}``, or an entry
    missing / shaped as ``{"error": ...}`` for a repo whose ref could not be
    read. Reuses build_index() from the exact source the fleet-wide grader
    runs (see UNTRACKED_PY main()'s --index-only branch) rather than a
    second, drifting copy of the run_id-extraction logic.
    """
    args = [sys.executable, "-", base] + grader_specs() + ["--index-only"]
    r = subprocess.run(args, input=UNTRACKED_PY, capture_output=True,
                       text=True, timeout=timeout)
    _, idx = parse_probe_output(r.stdout)
    return idx


def build_parent_index(base=LOCAL_BASE, fetch=True, timeout=120):
    """Fresh origin-side run_id index for the PARENT (Mac) checkout at `base`.

    Exists to cross-check a WORKER's STRANDED finding against a ref newer
    than the worker's own -- see the module docstring's "LABELLING IS NOT THE
    SAME AS RESOLVING" paragraph and the confirmed 2026-07-30T17:41Z
    ree-cloud-4/v3_exq_614 incident it names. The Mac's checkout tracks the
    same origin as every worker, and unlike a worker it is fetched (remote-
    tracking refs only, via `_fetch_local` -- no HEAD/index/worktree write)
    before grading, specifically so its own ref is not itself stale.

    Read-only toward the PARENT: `_fetch_local` is the one non-read-only step
    (documented in the module docstring), and `_run_index_local` only runs
    `git ls-tree` against the fetched ref. Never touches a WORKER -- the
    read-only promise toward those is unaffected; this function only ever
    opens `base` (the Mac's own checkout).

    Fails OPEN: returns `{}` (not None, not an exception) when the parent
    checkout is absent, unfetchable, or the grader subprocess errors, so a
    caller finding no entry for a repo just leaves that repo's findings
    exactly as graded -- same "absence is reported, never treated as
    informative" contract as `ref_age_hours`.
    """
    if not os.path.isdir(base):
        return {}
    if fetch:
        _fetch_local(base, timeout=timeout)
    try:
        idx = _run_index_local(base, timeout)
    except Exception:
        return {}
    return idx if isinstance(idx, dict) else {}


def crosscheck_stranded_against_parent(graded, parent_index):
    """Downgrade a STRANDED finding to a `parent_cleared` note when the
    PARENT (Mac) checkout's own fresh index shows the run_id on origin.

    `graded` is `{repo: untracked_dict}` -- the same shape `apply_claims`
    mutates in place, and this runs the same way: findings whose run_id
    appears in `parent_index[repo]["flat_runs"]` or `["pack_runs"]` move from
    `info["findings"]` to `info["parent_cleared"]`, tagged with which form
    cleared them.

    Deliberately does NOT re-verify CONTENT the way `grade_path`'s
    `origin_match` does. The worker's actual file bytes never cross the wire
    -- only the finding's summary fields (run_id / outcome / elapsed_seconds
    / bytes) do -- so there is nothing to diff against here. Presence of the
    run_id in the parent's fresh flat/pack sets is exactly the fact the
    confirmed incident turned on (v3_exq_614 sat on the real origin/master
    "in both flat and pack form"), and is exactly what CLEARS a run_id in
    grade_path's own step 1 before content is even considered. A downgrade
    here reads as "look again, cleared against a fresher ref" -- not a claim
    the two copies are byte-identical; a worker's ref being merely OLDER,
    never divergent, is what the "EVERY FINDING IS RELATIVE TO THE REF THE
    BOX CAN SEE" paragraph documents as the actual failure mode.

    Fails OPEN, per-repo: a missing/malformed `parent_index[repo]` (no
    parent checkout, that repo absent there, ls-tree failed) leaves every
    finding for that repo untouched -- the existing conservative STRANDED
    text stands exactly as before this cross-check existed.
    """
    if not parent_index:
        return graded
    for repo, info in (graded or {}).items():
        if not isinstance(info, dict):
            continue
        pidx = parent_index.get(repo)
        if not isinstance(pidx, dict):
            continue
        flat = set(pidx.get("flat_runs") or ())
        pack = set(pidx.get("pack_runs") or ())
        findings = info.get("findings") or []
        if not findings:
            continue
        kept, cleared = [], []
        for f in findings:
            rid = f.get("run_id")
            if rid and (rid in flat or rid in pack):
                d = dict(f)
                d["parent_form"] = "flat" if rid in flat else "pack"
                cleared.append(d)
            else:
                kept.append(f)
        if cleared:
            info["findings"] = kept
            info["parent_cleared"] = cleared
            info.setdefault("notes", {})["parent_cleared"] = len(cleared)
    return graded


def _probe_local(target, timeout, untracked, ignored, fetch, recheck):
    if not os.path.isdir(target.base):
        return None, f"local base not found: {target.base}"
    fetch_problems = _fetch_local(target.base) if fetch else []
    try:
        r = subprocess.run(["sh", "-s"], input=shell_probe(target.base),
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, "probe timed out"
    except Exception as exc:                      # pragma: no cover - defensive
        return None, f"probe failed: {exc}"
    out, _ = parse_probe_output(r.stdout)
    if not out:
        tail = (r.stderr or "").strip().splitlines()
        return None, tail[-1] if tail else "local probe produced no output"

    graded = {}
    if untracked:
        try:
            graded = _run_grader_local(target.base, ignored, timeout)
        except Exception as exc:                  # pragma: no cover - defensive
            graded = {name: {"error": f"grader failed: {exc}"} for name in REPOS}
        if recheck and target.multi_session:
            graded = _recheck(target, graded, ignored, timeout)

    # Record fetch outcome PER REPO. A fetch that failed for ree-v3 says
    # nothing about REE_assembly's refs, and marking both stale would push a
    # reader toward discounting a real finding.
    failed = {p.split(":", 1)[0]: p.split(":", 1)[1].strip()
              for p in fetch_problems}
    for repo, info in (graded or {}).items():
        if not isinstance(info, dict):
            continue
        if repo in failed:
            info["fetch_error"] = failed[repo]
        elif fetch:
            info["fetched"] = True
    return _attach(out, graded), None


def _recheck(target, graded, ignored, timeout):
    """Re-grade once and keep only findings that SURVIVE both passes.

    A multi_session checkout produces manifest-shaped files that exist for
    seconds: the 2026-07-30 Mac grade's single finding was a live driver's
    --dry-run output, gone by the next run. The write-up's conclusion was
    "re-run once before acting on any finding whose timestamp is minutes old";
    this makes that automatic rather than a thing the reader has to remember.

    Only runs when the first pass found something, so a clean box pays nothing.
    A finding that vanished is not silently dropped -- it is counted as
    `transient` and reported as a note.
    """
    if not any(isinstance(v, dict) and v.get("findings") for v in graded.values()):
        return graded
    try:
        second = _run_grader_local(target.base, ignored, timeout)
    except Exception:                             # pragma: no cover - defensive
        return graded
    for repo, info in graded.items():
        if not isinstance(info, dict) or not info.get("findings"):
            continue
        still = {f.get("path") for f in (second.get(repo, {}) or {}).get("findings", [])}
        kept = [f for f in info["findings"] if f.get("path") in still]
        gone = len(info["findings"]) - len(kept)
        if gone:
            info["transient"] = gone
            info.setdefault("notes", {})["transient"] = gone
        info["findings"] = kept
        info["rechecked"] = True
    return graded


# --- TASK_CLAIMS cross-check -------------------------------------------------
# On a multi_session checkout, git state alone CANNOT tell a strand from live
# work: an untracked file absent from origin at every path and absent from all
# history is the signature of both. TASK_CLAIMS.json is the discriminator.
#
# Deliberately NOT an import of REE_Working/scripts/task_claim.py. That is a
# different repo, present only on the Mac; a cross-repo sys.path import works
# here and breaks on the hub and the workers, which is precisely the failure
# CLAUDE.md's vendored-copy rule exists to prevent. The matching below mirrors
# task_claim.normalise_resource ("./a/b/" -> "a/b") and its directory-
# containment test; if that semantics ever changes, this is the copy to update.


def normalise_resource(res):
    if not isinstance(res, str):
        return ""
    return res.strip().lstrip("./").rstrip("/")


def load_active_claims(path=CLAIMS_PATH):
    """Active claims as [(session_id, claimed_at, [resources])]. Fails open."""
    try:
        with open(path, "r") as fh:
            data = json.load(fh)
    except Exception:
        return []
    out = []
    for c in (data or {}).get("claims", []):
        if not isinstance(c, dict) or c.get("status") != "active":
            continue
        res = [normalise_resource(r) for r in (c.get("resources") or [])]
        out.append((str(c.get("session_id") or "?"),
                    str(c.get("claimed_at") or "?"),
                    [r for r in res if r]))
    return out


def claim_covering(claims, repo, rel):
    """The first active claim whose resources cover `<repo>/<rel>`, or None.

    Containment is one-directional: a claim on a directory covers files under
    it. A claim on `ree-v3/experiments` must NOT cover
    `ree-v3/experiments_old/x.json`, which is why the test is on `res + "/"`
    and not on a bare string prefix.

    Age is NOT filtered. A stale-but-active claim on an untracked file is still
    far better evidence of live work than git has, and the consequence of a
    match is only note-instead-of-finding with the claim NAMED -- the reader
    can judge a 9-hour-old claim for themselves, which they cannot do if the
    path is presented as a strand with no attribution.
    """
    key = f"{repo}/{rel}"
    for sid, at, resources in claims:
        for res in resources:
            if key == res or key.startswith(res + "/"):
                return {"session_id": sid, "claimed_at": at, "resource": res}
    return None


def apply_claims(graded, claims):
    """Downgrade claim-covered findings to notes, in place."""
    if not claims:
        return graded
    for repo, info in (graded or {}).items():
        if not isinstance(info, dict):
            continue
        kept, covered = [], []
        for f in info.get("findings") or []:
            c = claim_covering(claims, repo, f.get("path", ""))
            if c:
                d = dict(f)
                d["claim"] = c
                covered.append(d)
            else:
                kept.append(f)
        if covered:
            info["findings"] = kept
            info["claim_covered"] = covered
            info.setdefault("notes", {})["claim_covered"] = len(covered)

        # Literature-entry findings get the identical treatment -- a slug
        # covered by an active claim is another session's in-flight
        # /lit-pull (or similar) work, not a strand. Mirrors the run-manifest
        # branch immediately above; kept as a separate list (not merged into
        # `findings`/`claim_covered`) for the same reason grade_repo keeps
        # literature_findings separate -- see its own count line.
        lkept, lcovered = [], []
        for f in info.get("literature_findings") or []:
            c = claim_covering(claims, repo, f.get("path", ""))
            if c:
                d = dict(f)
                d["claim"] = c
                lcovered.append(d)
            else:
                lkept.append(f)
        if lcovered:
            info["literature_findings"] = lkept
            info["literature_claim_covered"] = lcovered
            info.setdefault("notes", {})["literature_claim_covered"] = len(lcovered)
        # ...and the same for the named `no_counterpart_other` paths, so an
        # in-flight planning doc or script is attributed rather than left as an
        # anonymous "absent from origin" line for someone to chase.
        other = info.get("no_counterpart_other_paths") or []
        attributed = {}
        for rel in other:
            c = claim_covering(claims, repo, rel)
            if c:
                attributed[rel] = c["session_id"]
        if attributed:
            info["no_counterpart_other_claimed"] = attributed
    return graded


def claims_for_target(target, enabled=True):
    """Claims apply only to the checkout the registry actually describes."""
    if not enabled or not target.multi_session:
        return []
    return load_active_claims()


ADJUDICATIONS_PATH = os.path.join(
    LOCAL_BASE, "REE_assembly", "evidence", "planning",
    "git_health_adjudicated_divergences.json")


def load_adjudicated_divergences(path=ADJUDICATIONS_PATH):
    """Human-confirmed-benign same-run_id-different-content verdicts. Fails open.

    Each record is keyed on (host, repo, run_id, content_sha256) -- ALL FOUR,
    not run_id alone -- so a record only ever downgrades the EXACT byte
    content a human already reviewed. A future edit to the untracked copy, or
    a genuinely different phantom-completion that happens to share a run_id,
    produces a different content_sha256 and is never silently suppressed; see
    the module docstring's remedy (a) -- "never drop on a judgement call"
    applies equally to never SUPPRESSING on one.

    A record missing any of the four keys is dropped rather than loaded with
    a None standing in for a wildcard -- adjudication_covering() already
    refuses a None content_sha256, but failing closed here too means a
    malformed record can never accidentally match everything.
    """
    try:
        with open(path, "r") as fh:
            data = json.load(fh)
    except Exception:
        return []
    out = []
    for a in (data or {}).get("adjudications", []):
        if not isinstance(a, dict):
            continue
        if not (a.get("host") and a.get("repo") and a.get("run_id")
                and a.get("content_sha256")):
            continue
        out.append(a)
    return out


def adjudication_covering(records, host, repo, run_id, content_sha256):
    """The adjudication record matching this exact divergent finding, or None.

    All four of host/repo/run_id/content_sha256 must match. A hash-only match
    would ignore which box the review was actually about; a host/repo/run_id
    match without the hash is exactly the failure mode this whole mechanism
    exists to avoid (see load_adjudicated_divergences docstring).
    """
    if not content_sha256:
        return None
    for a in records:
        if (a.get("host") == host and a.get("repo") == repo
                and a.get("run_id") == run_id
                and a.get("content_sha256") == content_sha256):
            return a
    return None


def apply_adjudications(host, graded, records):
    """Downgrade adjudicated-benign divergent findings to notes, in place.

    Mirrors apply_claims: MUTATES the `divergent` list (both the top-level
    untracked bucket and, when present, the nested gitignored bucket) so
    every downstream consumer -- main()'s fleet-wide summary count,
    classify()'s escalation text -- sees the downgrade automatically rather
    than needing to know about a second bucket.

    Motivating case (2026-08-09): a confirmed-benign divergence for
    v3_exq_850 on ree-cloud-2 re-triggered the identical "diff both before
    deleting EITHER" escalation on every probe run, forever, with no way to
    record "this was already looked at". See
    evidence/planning/recovered_stranded_manifests/README_ree-cloud-2_2026-08-09.md
    section 2.
    """
    if not records:
        return graded

    def _split(repo, divergent):
        kept, adjudicated = [], []
        for f in divergent or []:
            a = adjudication_covering(records, host, repo,
                                       f.get("run_id", ""),
                                       f.get("content_sha256"))
            if a:
                d = dict(f)
                d["adjudication"] = a
                adjudicated.append(d)
            else:
                kept.append(f)
        return kept, adjudicated

    for repo, info in (graded or {}).items():
        if not isinstance(info, dict):
            continue
        kept, adjudicated = _split(repo, info.get("divergent"))
        if adjudicated:
            info["divergent"] = kept
            info["adjudicated_divergent"] = adjudicated
        g = info.get("gitignored")
        if isinstance(g, dict):
            gkept, gadjudicated = _split(repo, g.get("divergent"))
            if gadjudicated:
                g["divergent"] = gkept
                g["adjudicated_divergent"] = gadjudicated
    return graded


def resolve_hosts(hosts):
    """Selected targets, or None when a name matched nothing.

    Case-insensitive, plus HOST_ALIASES, because the Mac answers to three
    spellings (`DLAPTOP-4` in the heartbeats, `DLAPTOP-4.local` from the OS,
    and "the mac" in every write-up that describes it).
    """
    if not hosts:
        return dict(FLEET)
    lower = {k.lower(): k for k in FLEET}
    out = {}
    for h in hosts:
        key = h.strip().lower()
        key = HOST_ALIASES.get(key, lower.get(key, ""))
        if key in FLEET:
            out[key] = FLEET[key]
    return out or None


def classify(d):
    """Return (status, [reasons]). Structural faults first, advisory last."""
    if d.get("missing") == "1":
        return "MISSING", ["checkout absent"]
    reasons = []
    status = "OK"

    def _int(k):
        try:
            return int(d.get(k, 0))
        except ValueError:
            return 0

    if _int("unmerged") > 0:
        status = "WEDGED"
        first = d.get("first") or "?"
        reasons.append(f"{_int('unmerged')} unmerged path(s) -- pulls ABORT (e.g. {first})")
    if _int("skew") > 0:
        status = "WEDGED" if status == "WEDGED" else "SKEW"
        reasons.append(f"{_int('skew')} HEAD/worktree skew path(s) -- files in HEAD never written to disk")
    if d.get("gclog") == "1":
        if status == "OK":
            status = "GC-BLOCKED"
        reasons.append("gc.log present -- automatic gc DISABLED on this repo")
    behind = _int("behind")
    if behind < 0:
        reasons.append("no upstream tracking ref")
    elif behind > BEHIND_WARN:
        if status == "OK":
            status = "BEHIND"
        reasons.append(f"{behind} commits behind upstream")
    if _int("prepull") > 0:
        # Named separately from the generic stash count because these have a
        # known provenance and a known remedy. Two of ree-cloud-3's 13 held
        # the only surviving copy of a completed run (V3-EXQ-707c / ARC-110,
        # 40.9 hours of compute). The runner reaps these itself from
        # 2026-07-30 on (ree-v3 4028f06), so a NON-ZERO count now means either
        # a worker still running pre-fix code, or entries whose pop keeps
        # colliding on content the reaper could NOT prove redundant -- both
        # need a human, neither is self-healing.
        #
        # GRADED, not a bare count, whenever the untracked pass ran (it holds
        # the per-entry containment verdict -- see grade_prepull_stashes).
        # This replaces the single blanket "treat every one as the ONLY copy"
        # warning: a redundant entry (content already lands via the worktree
        # or origin -- e.g. a governance-reviewed manifest, a strict superset
        # of what the stash holds) is a retirement candidate, not a loss risk,
        # and burying that inside an undifferentiated count is what let 13
        # entries on ree-cloud-3 sit unexamined while two of them were the
        # real thing. An at_risk entry keeps the original, conservative
        # wording. Falls back to the old blanket text when detailed grading
        # was not run at all (--no-untracked, or the untracked pass errored
        # for this repo) -- absence of a verdict is never treated as "safe".
        u0 = d.get("untracked")
        pg = u0.get("prepull") if isinstance(u0, dict) else None
        if isinstance(pg, dict) and pg.get("count", 0) > 0:
            reasons.append(
                f"{pg['count']} runner-prepull-untracked stash entry(ies) "
                f"GRADED: {pg.get('redundant', 0)} redundant (content already "
                f"carried by the worktree or origin -- safe retirement "
                f"candidate(s)), {pg.get('at_risk', 0)} at-risk (hold content "
                f"proven nowhere else -- DO NOT drop), "
                f"{pg.get('unreadable', 0)} unreadable (could not enumerate "
                f"or verify -- treat as at-risk)")
            for e in pg.get("entries", []):
                if e.get("verdict") == "redundant":
                    continue
                up = e.get("unproven_paths") or []
                bits = []
                if up:
                    bits.append("unproven: " + ", ".join(up[:3])
                                + (" ..." if len(up) > 3 else ""))
                if e.get("beyond_scan_cap"):
                    bits.append(f"+{e['beyond_scan_cap']} path(s) beyond scan cap")
                if e.get("reason"):
                    bits.append(e["reason"])
                reasons.append(
                    f"    {e.get('ref', '?')} {e.get('verdict', '?').upper()}"
                    + (f" -- {'; '.join(bits)}" if bits else ""))
            if pg.get("truncated_entries"):
                reasons.append(
                    f"    (+{pg['truncated_entries']} more prepull entries "
                    f"beyond the grading cap -- use --json)")
        else:
            reasons.append(
                f"{_int('prepull')} runner-prepull-untracked stash entry(ies) -- "
                f"orphaned-stash leak residue; detailed containment grading "
                f"unavailable for this repo (run with untracked grading "
                f"enabled). Treat as holding the ONLY copy of completed runs "
                f"until graded. Inspect with `git stash show -p <ref>` and "
                f"recover before dropping ANY of them")
    other = _int("stashes") - _int("prepull")
    if other > 0:
        reasons.append(f"{other} other stash entry(ies) -- may strand evidence; inspect before dropping")

    # STRANDED UNTRACKED MANIFESTS. Deliberately does NOT change `status`: like
    # the stash signal this is a "look at this now" flag for a human, not a
    # fault in the checkout, and the script chains (exit 0). It is listed LAST
    # but read FIRST -- on 2026-07-30 the OK-with-17-stashes line above was the
    # misleading part and this was the real loss. See module docstring.
    u = d.get("untracked")
    if isinstance(u, dict):
        if u.get("error"):
            reasons.append(f"untracked grading unavailable -- {u['error']}")
        if u.get("fetch_error"):
            reasons.append(
                f"remote-tracking refs NOT refreshed -- {u['fetch_error']}; "
                f"graded against a possibly stale origin ref, so a 'stranded' "
                f"path here may simply have landed since the last fetch")
        # Claim-covered paths, dry-run residue and transients are all reported
        # BELOW findings and never as findings. Each is a case where the git
        # state looks exactly like a strand and is not one -- see the module
        # docstring. Naming them is what keeps the probe usable on a box with
        # ~18 concurrent sessions instead of being ignored as noisy.
        covered = u.get("claim_covered") or []
        if covered:
            reasons.append(
                f"{len(covered)} untracked run manifest(s) covered by an ACTIVE "
                f"TASK_CLAIMS entry -- live work, NOT a strand; do not touch")
            for f in covered[:3]:
                c = f.get("claim") or {}
                reasons.append(
                    f"    {f.get('run_id', '?')} -- {f.get('path', '?')} "
                    f"(claim {c.get('session_id', '?')} on {c.get('resource', '?')})")
        # PARENT-CLEARED: this box's own ref said stranded; the Mac's fresher
        # ref (fetched fresh every run, per the module docstring) says the
        # run_id is on origin after all -- the v3_exq_614 shape. Reported
        # beside claim_covered, for the same reason: it looks exactly like a
        # strand and is not one, so it is named rather than silently dropped.
        pcleared = u.get("parent_cleared") or []
        if pcleared:
            reasons.append(
                f"{len(pcleared)} untracked run manifest(s) CLEARED against the "
                f"PARENT (Mac) checkout's own freshly-fetched {u.get('ref', 'origin')} "
                f"index -- present there in flat or pack form, so NOT a strand; "
                f"this box's own graded ref was likely just stale, and this "
                f"already resolves it -- no further action needed")
            for f in pcleared[:3]:
                reasons.append(
                    f"    {f.get('run_id', '?')} -- {f.get('path', '?')} "
                    f"(present on the parent's origin as {f.get('parent_form', '?')})")
        notes = u.get("notes") or {}
        if notes.get("dry_run"):
            reasons.append(
                f"{notes['dry_run']} --dry-run smoke manifest(s) present "
                f"(_dry_ prefix / dry_run:true) -- not evidence, self-clearing")
        if u.get("transient"):
            reasons.append(
                f"{u['transient']} finding(s) present in the first pass and GONE "
                f"in the re-check -- transient, not reported as strands")
        strand = u.get("findings") or []
        # A STALE graded ref is the one thing that can turn a landed run into
        # an apparent strand, so it is stated HERE, immediately above the
        # findings it would explain -- not buried in --json. Confirmed
        # 2026-07-30T17:41Z: a just-woken ree-cloud-4 reported
        # v3_exq_614_..._20260529T191318Z_v3 as stranded against an
        # origin/master 9 hours old; the run was on the real origin/master in
        # BOTH flat and pack form, recovered earlier the same day.
        age = u.get("ref_age_hours")
        if strand and age is None:
            reasons.append(
                f"NOTE: could not date {u.get('ref', 'the graded ref')} -- a "
                f"stale ref would make landed runs look stranded")
        elif strand and isinstance(age, (int, float)) and age > REF_STALE_WARN:
            reasons.append(
                f"CHECK THE REF FIRST: {u.get('ref', 'the graded ref')} on this "
                f"box is {age:.1f}h old (a running worker pulls every ~60s, so "
                f"this box was probably powered off). Anything that landed since "
                f"then reads as stranded. Re-check each run_id against the REAL "
                f"origin before triaging")
        if strand:
            n = len(strand) + int(u.get("truncated") or 0)
            reasons.append(
                f"{n} STRANDED untracked run manifest(s) -- parse as run "
                f"manifests and have NO counterpart on origin at ANY path "
                f"(flat, pack, or de-.bak'd stem). This is real evidence loss, "
                f"invisible to the stash count. RECOVER BEFORE any reset/clean/gc")
            for f in strand[:5]:
                el = f.get("elapsed_seconds")
                el = f" / {el}s compute" if isinstance(el, (int, float)) else ""
                reasons.append(
                    f"    {f.get('run_id', '?')} [{f.get('outcome', '?')}]{el} "
                    f"-- {f.get('path', '?')}")
            if len(strand) > 5:
                reasons.append(f"    ... and {len(strand) - 5} more (use --json)")
            if u.get("truncated"):
                reasons.append(
                    f"    (+{u['truncated']} beyond the report cap -- use --json)")

        # ADJUDICATED-BENIGN DIVERGENCE: a human already reviewed this EXACT
        # byte content (content_sha256 match, not just run_id) and confirmed
        # it is not a phantom-completion / partial-write -- reported as a
        # quiet note naming that review, never re-escalated as if new. A
        # divergence whose content has since changed is NOT covered by this
        # and still reports in full below.
        adjudicated = u.get("adjudicated_divergent") or []
        if adjudicated:
            reasons.append(
                f"{len(adjudicated)} untracked run manifest(s) with a "
                f"same-run_id-different-content divergence ALREADY ADJUDICATED "
                f"BENIGN by a prior human review -- not re-escalated; the match "
                f"is on exact byte content, so a NEW divergence on the same "
                f"run_id still reports in full below")
            for f in adjudicated[:3]:
                a = f.get("adjudication") or {}
                reasons.append(
                    f"    {f.get('run_id', '?')} -- {f.get('path', '?')} "
                    f"(adjudicated {a.get('adjudicated_at', '?')}, see "
                    f"{a.get('reference', '?')})")

        # DIVERGENT: the run_id IS on origin, but not carrying this content.
        # Reported separately from a strand because the remedy is the opposite:
        # a strand needs recovering, this needs ADJUDICATING -- one of the two
        # copies is wrong and which one is not knowable from here. Until
        # 2026-07-30 this cleared silently on run_id membership alone, so the
        # one case that most wants a human read produced no output at all.
        div = u.get("divergent") or []
        if div:
            reasons.append(
                f"{len(div)} untracked run manifest(s) whose run_id IS on origin "
                f"but with DIFFERENT content -- not a strand and not a duplicate. "
                f"Two divergent manifests for one run_id is the phantom-completion "
                f"/ partial-write shape. Diff both before deleting EITHER; do not "
                f"assume the origin copy is the good one")
            for f in div[:5]:
                op = (f.get("origin_paths") or ["?"])[0]
                reasons.append(
                    f"    {f.get('run_id', '?')} [{f.get('outcome', '?')}] "
                    f"-- {f.get('path', '?')} vs origin {op}")
            if len(div) > 5:
                reasons.append(f"    ... and {len(div) - 5} more (use --json)")

        # LITERATURE-ENTRY strand / claim-cover / divergence. Same three-way
        # split as a run manifest, keyed on the entry SLUG instead of run_id
        # -- see module docstring, "WHY LITERATURE EVIDENCE ENTRIES ARE
        # GRADED TOO" (chip-20260819-githealth-untracked-literature-
        # blindspot). Reported in its OWN lines, never folded into the run-
        # manifest counts above, so "0 stranded run manifest(s)" can no
        # longer be misread as "nothing here is stranded".
        lit_covered = u.get("literature_claim_covered") or []
        if lit_covered:
            reasons.append(
                f"{len(lit_covered)} untracked literature evidence entry(ies) "
                f"covered by an ACTIVE TASK_CLAIMS entry -- live work, NOT a "
                f"strand; do not touch")
            for f in lit_covered[:3]:
                c = f.get("claim") or {}
                reasons.append(
                    f"    {f.get('slug', '?')} -- {f.get('path', '?')} "
                    f"(claim {c.get('session_id', '?')} on {c.get('resource', '?')})")
        lit_strand = u.get("literature_findings") or []
        if lit_strand:
            n = len(lit_strand) + int(u.get("literature_truncated") or 0)
            reasons.append(
                f"{n} STRANDED literature evidence entry(ies) -- parse as "
                f"evidence/literature/*/entries/*/(record.json|summary.md) "
                f"and have NO counterpart on origin under this slug, at any "
                f"review path. A regen that globs the working tree "
                f"(build_experiment_indexes.py's literature indexer) can bake "
                f"this in as a permanent dangling citation the moment it runs "
                f"on this box -- see audit_dangling_citations.py. RECOVER "
                f"BEFORE any reset/clean/gc")
            for f in lit_strand[:5]:
                reasons.append(
                    f"    {f.get('slug', '?')} [{f.get('kind', '?')}] "
                    f"-- {f.get('path', '?')}")
            if len(lit_strand) > 5:
                reasons.append(f"    ... and {len(lit_strand) - 5} more (use --json)")
            if u.get("literature_truncated"):
                reasons.append(
                    f"    (+{u['literature_truncated']} beyond the report cap -- use --json)")
        lit_div = u.get("literature_divergent") or []
        if lit_div:
            reasons.append(
                f"{len(lit_div)} untracked literature evidence entry(ies) "
                f"whose slug IS on origin but with DIFFERENT content -- not a "
                f"strand and not a duplicate. Diff both before deleting EITHER")
            for f in lit_div[:5]:
                op = (f.get("origin_paths") or ["?"])[0]
                reasons.append(
                    f"    {f.get('slug', '?')} [{f.get('kind', '?')}] "
                    f"-- {f.get('path', '?')} vs origin {op}")
            if len(lit_div) > 5:
                reasons.append(f"    ... and {len(lit_div) - 5} more (use --json)")

        # GITIGNORED bucket (--ignored). Separate and lower-severity on
        # purpose: an ignored path is ignored deliberately, so the prior is
        # much weaker than for an untracked one. But `*.bak` being ignored in
        # REE_assembly is exactly why this class was never machine-graded, and
        # a run manifest is a run manifest wherever it sits.
        g = u.get("gitignored")
        if isinstance(g, dict):
            if g.get("error"):
                reasons.append(f"gitignored grading unavailable -- {g['error']}")
            gf = g.get("findings") or []
            if gf:
                reasons.append(
                    f"{len(gf)} run manifest(s) in GITIGNORED path(s) with no "
                    f"counterpart on origin -- lower severity than a stranded "
                    f"untracked file (the path is ignored on purpose), but a "
                    f"gitignored manifest is invisible to every other check")
                for f in gf[:3]:
                    reasons.append(
                        f"    {f.get('run_id', '?')} [{f.get('outcome', '?')}] "
                        f"-- {f.get('path', '?')}")
            gadj = g.get("adjudicated_divergent") or []
            if gadj:
                reasons.append(
                    f"{len(gadj)} GITIGNORED run manifest(s) with a "
                    f"same-run_id-different-content divergence ALREADY "
                    f"ADJUDICATED BENIGN -- not re-escalated")
                for f in gadj[:3]:
                    a = f.get("adjudication") or {}
                    reasons.append(
                        f"    {f.get('run_id', '?')} -- {f.get('path', '?')} "
                        f"(adjudicated {a.get('adjudicated_at', '?')}, see "
                        f"{a.get('reference', '?')})")
            gd = g.get("divergent") or []
            if gd:
                reasons.append(
                    f"{len(gd)} run manifest(s) in GITIGNORED path(s) whose "
                    f"run_id is on origin with DIFFERENT content -- adjudicate, "
                    f"do not delete on the assumption it is a stale backup")
                for f in gd[:3]:
                    reasons.append(
                        f"    {f.get('run_id', '?')} [{f.get('outcome', '?')}] "
                        f"-- {f.get('path', '?')}")
            if g.get("beyond_cap"):
                reasons.append(
                    f"    ({g['beyond_cap']} ignored file(s) beyond the scan cap "
                    f"were NOT graded)")
    return status, reasons


def selftest():
    """Assert classify() on RECORDED real fleet states. No ssh, no network.

    These are not synthetic: case 1 is ree-cloud-2 exactly as found on
    2026-07-20 (the two-day wedge), case 2 is the SD-068 pre-staged-skew
    signature. A detector that has only ever seen healthy checkouts is
    unverified, so this pins the states it MUST fire on.
    """
    cases = [
        ("ree-cloud-2 as found 2026-07-20 (real 2-day wedge)", "WEDGED",
         dict(branch="master", unmerged="1", behind="218", skew="0", gclog="1",
              stashes="1", first="evidence/experiments/v3_exq_779_..._v3.json")),
        ("pre-staged 'D ' skew (SD-068 signature)", "SKEW",
         dict(branch="master", unmerged="0", behind="0", skew="12", gclog="0",
              stashes="0", first="")),
        ("healthy worker", "OK",
         dict(branch="main", unmerged="0", behind="1", skew="0", gclog="0",
              stashes="0", first="")),
        # A stranded stash must be REPORTED but must NOT fail the fleet: it is
        # a "look at this" signal, not a fault. cloud-3 carried one holding the
        # only surviving copy of a completed V3-EXQ-673 run.
        ("stranded stash only (cloud-3 673 case)", "OK",
         dict(branch="master", unmerged="0", behind="2", skew="0", gclog="0",
              stashes="2", first="")),
        ("gc disabled only", "GC-BLOCKED",
         dict(branch="master", unmerged="0", behind="3", skew="0", gclog="1",
              stashes="0", first="")),
        # ree-cloud-3 as found 2026-07-29: 13 orphaned PREPULL entries, plus
        # the gc.log that the same leak's churn produced (~6 unreachable
        # objects per 62s tick -> 20,326 loose objects / 84 MiB tripped git's
        # unreachable-object guard, and gc.log's mere presence then disables
        # automatic gc indefinitely). Like any stash, the entries themselves
        # must REPORT without failing the fleet -- the GC-BLOCKED verdict here
        # comes from gc.log, not from them.
        ("ree-cloud-3 as found 2026-07-29 (prepull-stash leak)", "GC-BLOCKED",
         dict(branch="master", unmerged="0", behind="4", skew="0", gclog="1",
              stashes="13", prepull="13", first="")),
        ("missing checkout", "MISSING", dict(missing="1")),
        # ree-cloud-2 as found 2026-07-30. THE case this grading exists for:
        # the checkout is structurally fine and its 17 stashes were all fully
        # contained on origin, while an untracked .bak held the only copy of a
        # completed run. Must REPORT loudly and must NOT fail the fleet.
        ("ree-cloud-2 as found 2026-07-30 (stranded 490h manifest)", "OK",
         dict(branch="master", unmerged="0", behind="2", skew="0", gclog="0",
              stashes="17", first="", untracked=dict(
                  untracked=41, ignored=6, truncated=0,
                  notes={"per_tick": 3, "runner_status": 2},
                  findings=[dict(
                      path=("evidence/experiments/"
                            "v3_exq_490h_mech295_cascade_gap4_tier1/"
                            "v3_exq_490h_mech295_cascade_gap4_tier1_"
                            "20260529T214607Z_v3.json.bak.20260530"),
                      run_id=("v3_exq_490h_mech295_cascade_gap4_tier1_"
                              "20260529T214607Z_v3"),
                      outcome="FAIL", elapsed_seconds=5661.46, bytes=8214)]))),
    ]
    failed = 0
    for name, want, d in cases:
        got, reasons = classify(d)
        ok = got == want
        failed += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {got:11s} (want {want:11s}) {name}")
        if not ok:
            for r in reasons:
                print(f"           - {r}")
    # the stash case must still SURFACE the stash even though it stays OK
    _, reasons = classify(cases[3][2])
    if not any("stash" in r for r in reasons):
        print("  [FAIL] stranded stash was not reported")
        failed += 1
    else:
        print("  [PASS] stranded stash reported without failing the fleet")
    # prepull entries must be named as such -- the generic count is what let
    # 13 of them sit unexamined on cloud-3 while two held irreplaceable runs.
    _, reasons = classify(cases[5][2])
    if not any("runner-prepull-untracked" in r for r in reasons):
        print("  [FAIL] prepull stash entries were not called out by name")
        failed += 1
    elif any("other stash entry" in r for r in reasons):
        print("  [FAIL] prepull entries were double-counted as 'other' stashes")
        failed += 1
    else:
        print("  [PASS] prepull stash entries named, not double-counted")
    # ...and a plain stash list must NOT be mislabelled as prepull residue.
    _, reasons = classify(cases[3][2])
    if any("runner-prepull-untracked" in r for r in reasons):
        print("  [FAIL] non-prepull stashes reported as prepull residue")
        failed += 1
    else:
        print("  [PASS] non-prepull stashes not mislabelled")
    # the stranded manifest must name its run_id -- a bare count is exactly the
    # signal that failed here, and the run_id is what makes it actionable.
    _, reasons = classify(cases[7][2])
    blob = " ".join(reasons)
    if "STRANDED" not in blob:
        print("  [FAIL] stranded untracked manifest was not reported")
        failed += 1
    elif "v3_exq_490h_mech295_cascade_gap4_tier1_20260529T214607Z_v3" not in blob:
        print("  [FAIL] stranded manifest reported without naming its run_id")
        failed += 1
    else:
        print("  [PASS] stranded untracked manifest named, fleet not failed")
    # ...and a clean untracked pass must stay silent.
    _, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="",
        untracked=dict(untracked=38, ignored=12, truncated=0, findings=[],
                       notes={"per_tick": 4, "runner_status": 2,
                              "no_counterpart_other": 9})))
    if reasons:
        print("  [FAIL] ordinary untracked churn produced output: %s" % reasons)
        failed += 1
    else:
        print("  [PASS] ordinary untracked churn is silent (notes are --json only)")

    # ...and the local-target note classes must all be visible without ever
    # being promoted to a strand. Recorded from the 2026-07-30 Mac grade: one
    # transient _dry_ finding, one claim-covered in-flight file.
    status, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=dict(
            untracked=2, ignored=0, truncated=0, findings=[], transient=1,
            notes={"dry_run": 1, "transient": 1},
            claim_covered=[dict(path="coordinator/deploy/x.sh",
                                run_id="live_v3", outcome="FAIL",
                                claim={"session_id": "friendly-antonelli-b0f414",
                                       "claimed_at": "2026-07-30T07:45:37Z",
                                       "resource": "ree-v3/coordinator/deploy"})],
            gitignored=dict(entries=47, files_graded=19, dirs_skipped=28,
                            beyond_cap=0, findings=[]))))
    blob = " ".join(reasons)
    if status != "OK":
        print(f"  [FAIL] Mac note classes changed the status to {status}")
        failed += 1
    elif "STRANDED" in blob:
        print("  [FAIL] a note class was reported as a stranded manifest")
        failed += 1
    elif not all(k in blob for k in ("ACTIVE", "dry-run", "re-check")):
        print(f"  [FAIL] a note class went unreported: {reasons}")
        failed += 1
    else:
        print("  [PASS] claim-covered / dry-run / transient all REPORT and "
              "none is promoted to a strand")

    # A STALE graded ref must be called out beside the findings it could
    # explain -- recorded from ree-cloud-4, 2026-07-30T17:41Z, whose 9h-old
    # origin/master made an already-recovered run look stranded. The age is a
    # NUMBER supplied by the grader, so this case is time-independent.
    def _with_ref(age):
        return dict(branch="master", unmerged="0", behind="0", skew="0",
                    gclog="0", stashes="0", first="", untracked=dict(
                        untracked=1, ignored=0, truncated=0, notes={},
                        ref="origin/master", ref_age_hours=age,
                        findings=[dict(
                            path="evidence/experiments/v3_exq_614_x_v3.json.bak.20260530",
                            run_id="v3_exq_614_x_v3", outcome="FAIL",
                            elapsed_seconds=1.0, bytes=10)]))
    stale = " ".join(classify(_with_ref(9.1))[1])
    fresh = " ".join(classify(_with_ref(0.02))[1])
    undated = " ".join(classify(_with_ref(None))[1])
    if "CHECK THE REF FIRST" not in stale or "9.1h" not in stale:
        print(f"  [FAIL] a 9.1h-stale graded ref was not called out: {stale}")
        failed += 1
    elif "STRANDED" not in stale:
        print("  [FAIL] a stale ref suppressed the finding instead of "
              "labelling it -- it might still be real")
        failed += 1
    elif "CHECK THE REF FIRST" in fresh:
        print("  [FAIL] a fresh ref produced the stale-ref caveat")
        failed += 1
    elif "could not date" not in undated:
        print("  [FAIL] an undatable ref was treated as fresh")
        failed += 1
    else:
        print("  [PASS] stale graded ref is labelled beside the finding, a "
              "fresh one is silent, an undatable one is reported")
    # ...and the caveat must never appear on a box with nothing to explain.
    if any("CHECK THE REF" in r for r in classify(dict(
            branch="master", unmerged="0", behind="0", skew="0", gclog="0",
            stashes="0", first="", untracked=dict(
                untracked=3, ignored=0, truncated=0, notes={}, findings=[],
                ref="origin/master", ref_age_hours=48.0)))[1]):
        print("  [FAIL] stale-ref caveat printed with no findings to explain")
        failed += 1
    else:
        print("  [PASS] stale-ref caveat is silent when there is no finding")

    # A parent-cleared finding must read as CLEARED, not as a strand, and
    # must not resurrect the CHECK THE REF FIRST caveat -- that caveat exists
    # to tell a human to go verify a stale ref; a parent_cleared entry IS that
    # verification, already done. Recorded from the exact confirmed shape:
    # ree-cloud-4, 2026-07-30T17:41Z, v3_exq_614 stranded against a 9.1h-old
    # ref, present on the real origin/master in flat form.
    status, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=dict(
            untracked=1, ignored=0, truncated=0, notes={},
            ref="origin/master", ref_age_hours=9.1, findings=[],
            parent_cleared=[dict(
                path="evidence/experiments/v3_exq_614_x_v3.json.bak.20260530",
                run_id="v3_exq_614_x_v3", outcome="FAIL",
                parent_form="flat")])))
    blob = " ".join(reasons)
    if status != "OK":
        print(f"  [FAIL] a parent-cleared finding changed status to {status}")
        failed += 1
    elif "STRANDED" in blob:
        print("  [FAIL] a parent-cleared finding was still reported as STRANDED")
        failed += 1
    elif "CHECK THE REF FIRST" in blob:
        print("  [FAIL] CHECK THE REF FIRST fired with nothing left to check "
              "(the parent cross-check already resolved it)")
        failed += 1
    elif "v3_exq_614_x_v3" not in blob or "CLEARED" not in blob:
        print(f"  [FAIL] parent-cleared finding not reported: {reasons}")
        failed += 1
    else:
        print("  [PASS] parent-cleared finding reads as CLEARED (names the "
              "run_id and form), not as STRANDED, and does not re-trigger "
              "CHECK THE REF FIRST")
    # ...and a parent-cleared entry must coexist with a genuine survivor:
    # clearing one finding must never hide another that the parent index
    # does NOT vouch for.
    _, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=dict(
            untracked=2, ignored=0, truncated=0, notes={},
            findings=[dict(path="evidence/experiments/real_strand_v3.json",
                           run_id="real_strand_v3", outcome="FAIL")],
            parent_cleared=[dict(
                path="evidence/experiments/v3_exq_614_x_v3.json.bak.20260530",
                run_id="v3_exq_614_x_v3", outcome="FAIL",
                parent_form="pack")])))
    blob = " ".join(reasons)
    if "real_strand_v3" not in blob or "STRANDED" not in blob:
        print("  [FAIL] a genuine strand was hidden beside a parent-cleared one")
        failed += 1
    elif "v3_exq_614_x_v3" not in blob:
        print("  [FAIL] the parent-cleared entry vanished beside a real strand")
        failed += 1
    else:
        print("  [PASS] a parent-cleared entry and a genuine strand are both "
              "reported, independently")

    # LITERATURE-ENTRY reporting (chip-20260819-githealth-untracked-
    # literature-blindspot). A stranded literature entry must show up as its
    # OWN reported line, must coexist with a genuine run-manifest strand
    # without either hiding the other, and must never itself flip status.
    status, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=dict(
            untracked=3, ignored=0, truncated=0, notes={},
            findings=[dict(path="evidence/experiments/real_strand_v3.json",
                           run_id="real_strand_v3", outcome="FAIL")],
            literature_findings=[dict(
                path=("evidence/literature/targeted_review_arc_032/entries/"
                      "2026-03-29_arc_032_frontal_theta_hippocampus_reward_"
                      "hyman2010/record.json"),
                slug="2026-03-29_arc_032_frontal_theta_hippocampus_reward_hyman2010",
                kind="record.json")])))
    blob = " ".join(reasons)
    if status != "OK":
        print(f"  [FAIL] a stranded literature entry changed status to {status}")
        failed += 1
    elif "STRANDED literature evidence entry" not in blob:
        print("  [FAIL] a stranded literature entry was not reported")
        failed += 1
    elif "arc_032_frontal_theta_hippocampus_reward_hyman2010" not in blob:
        print("  [FAIL] stranded literature entry reported without naming its slug")
        failed += 1
    elif "real_strand_v3" not in blob or "STRANDED untracked run manifest" not in blob:
        print("  [FAIL] a run-manifest strand was hidden beside a literature strand")
        failed += 1
    else:
        print("  [PASS] a stranded literature entry is reported in its OWN "
              "line, names its slug, coexists with a run-manifest strand, "
              "and does not change status")

    # ...and a literature entry covered by an active TASK_CLAIMS entry must
    # read as live work, never as a strand -- mirrors _selftest_claims()'s
    # run-manifest case, applied via apply_claims to literature_findings.
    graded = {"REE_assembly": {"untracked": 1, "literature_findings": [
        {"path": ("evidence/literature/targeted_review_x/entries/"
                  "2026-08-19_inflight_entry/record.json"),
         "slug": "2026-08-19_inflight_entry", "kind": "record.json"},
    ], "notes": {}}}
    apply_claims(graded, [("lit-pull-live-9f3a2b", "2026-08-19T09:00:00Z",
                           ["REE_assembly/evidence/literature/targeted_review_x"])])
    info = graded["REE_assembly"]
    if info.get("literature_findings"):
        print(f"  [FAIL] literature claims: a claim-covered entry stayed a "
              f"finding: {info['literature_findings']}")
        failed += 1
    elif not info.get("literature_claim_covered"):
        print("  [FAIL] literature claims: no literature_claim_covered entry "
              "was produced")
        failed += 1
    elif info["literature_claim_covered"][0]["claim"]["session_id"] != "lit-pull-live-9f3a2b":
        print("  [FAIL] literature claims: the covered entry does not NAME its claim")
        failed += 1
    else:
        status, reasons = classify(dict(
            branch="master", unmerged="0", behind="0", skew="0", gclog="0",
            stashes="0", first="", untracked=info))
        blob = " ".join(reasons)
        if status != "OK" or "STRANDED literature" in blob:
            print(f"  [FAIL] literature claims: claim-covered entry still "
                  f"read as a strand (status={status}): {reasons}")
            failed += 1
        elif "lit-pull-live-9f3a2b" not in blob:
            print("  [FAIL] literature claims: covering session not named in the report")
            failed += 1
        else:
            print("  [PASS] literature claims: a claim-covered entry becomes "
                  "a NOTE naming its session, never a strand")

    failed += _selftest_grader()
    failed += _selftest_literature_grader()
    failed += _selftest_prepull_grading()
    failed += _selftest_local_target()
    failed += _selftest_claims()
    failed += _selftest_adjudicated_divergence()
    failed += _selftest_parent_crosscheck()
    failed += _selftest_recheck_and_host_resolution()
    failed += _selftest_fetch_is_local_only()
    print()
    print("selftest: %d case(s) FAILED" % failed if failed else "selftest: all cases pass")
    return 1 if failed else 0


def _selftest_grader():
    """Run the REAL worker-side grader source against a temp git repo.

    Everything above tests classify(), i.e. the presentation of a finding. This
    tests the part that decides whether there IS one -- which is the part that
    was missing entirely until 2026-07-30, and which cannot be exercised by
    hand-written dicts. No ssh, no network; builds a throwaway repo in a
    tempdir and executes UNTRACKED_PY exactly as the worker does.

    The four cases are the four ways the 490h triage could have gone wrong.
    """
    import shutil
    import tempfile

    def flat(run_id, outcome="PASS"):
        return {"run_id": run_id, "outcome": outcome, "elapsed_seconds": 12.5}

    tmp = tempfile.mkdtemp(prefix="rgh-selftest-")
    try:
        root = os.path.join(tmp, "REE_assembly")
        ev = os.path.join(root, "evidence", "experiments")
        os.makedirs(ev)

        def run(*args):
            subprocess.run(("git",) + args, cwd=root, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        def write(rel, obj, compact=False):
            p = os.path.join(root, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as fh:
                json.dump(obj, fh, separators=(",", ":") if compact else None)

        run("init", "-q")
        run("config", "user.email", "selftest@local")
        run("config", "user.name", "selftest")

        # COMMITTED (a) flat manifest in the writer's form: compact, and with
        # the fields the phase3 writer injects. (b) a pack-form manifest.
        kept = flat("kept_run_v3")
        origin_kept = dict(kept)
        origin_kept.update(queue_id="V3-EXQ-001", machine="ree-cloud-2",
                           epistemic_category="mechanism",
                           evidence_direction_note="")
        write("evidence/experiments/kept_run_v3.json", origin_kept, compact=True)
        write("evidence/experiments/someexp/runs/pack_run_v3/manifest.json",
              flat("pack_run_v3"), compact=True)
        # (c) a NON-manifest json and a non-json file, to exercise the basename
        #     + de-.bak'd-stem path on its own. The manifest cases above all
        #     clear at the run_id step, so without these the superset and
        #     byte-compare branches would never run in this test.
        write("evidence/experiments/summary_index.json", {"a": 1, "b": 2})
        # (d) a recovered manifest PARKED outside the live evidence paths --
        #     the real recovery procedure files these under evidence/planning/
        #     recovered_stranded_manifests/ so the indexer cannot score them.
        #     Graded via case 6b below.
        write("evidence/planning/recovered_stranded_manifests/parked_run_v3.json",
              flat("parked_run_v3"), compact=True)
        os.makedirs(os.path.join(root, "docs"), exist_ok=True)
        with open(os.path.join(root, "docs", "notes.txt"), "w") as fh:
            fh.write("plain text\n")
        run("add", "-A")
        run("commit", "-q", "-m", "base")

        # UNTRACKED, one per hazard:
        #  1. a .bak of a manifest whose origin copy is a strict SUPERSET
        #     (writer-injected fields) -- byte compare would call this stranded
        write("evidence/experiments/kept_run_v3.json.bak.20260530", kept)
        #  2. a flat copy of a manifest that only exists on origin in PACK form
        #     -- exact-path grading would call this stranded
        write("evidence/experiments/pack_run_v3.json", flat("pack_run_v3"))
        #  3. THE 490h SHAPE: a .bak inside an experiment subdirectory whose
        #     run exists nowhere on origin. The one real finding.
        write("evidence/experiments/lostexp/lost_run_v3.json.bak.20260530",
              flat("lost_run_v3", outcome="FAIL"))
        #  3b. non-manifest .bak whose origin copy is a superset, spelled with
        #      the OTHER real backup suffix form -- clears only if basename,
        #      stem-stripping and superset all work
        write("evidence/experiments/summary_index.json.bak.phantom-clean",
              {"a": 1})
        #  3c. non-json .bak, byte-identical to origin
        with open(os.path.join(root, "docs", "notes.txt.bak"), "w") as fh:
            fh.write("plain text\n")
        #  4. by-design / churn that must never be a finding
        os.makedirs(os.path.join(ev, "lostexp"), exist_ok=True)
        with open(os.path.join(ev, "lostexp", "x_per_tick.jsonl"), "w") as fh:
            fh.write('{"tick": 1}\n{"tick": 2}\n')
        os.makedirs(os.path.join(root, "__pycache__"), exist_ok=True)
        with open(os.path.join(root, "__pycache__", "z.pyc"), "wb") as fh:
            fh.write(b"\x00\x01")
        #  4b. --dry-run smoke residue, BOTH signals, each on its own file so a
        #      single check cannot cover for the other. These are manifest-
        #      shaped and absent from origin -- a finding by every other test.
        #      The `_dry_`-prefixed one is the exact shape of the 2026-07-30
        #      Mac false positive.
        write("evidence/experiments/_dry_smoke_run_v3.json",
              flat("smoke_run_v3", outcome="FAIL"))
        write("evidence/experiments/otherexp/plainnamed_run_v3.json",
              dict(flat("plainnamed_run_v3", outcome="FAIL"), dry_run=True))
        #  5. runner EXIT SIGNAL: carries run_id + outcome, so it grades as a
        #     stranded manifest unless BYDESIGN suppresses it BEFORE the
        #     manifest test. Its run_id is deliberately one that exists
        #     nowhere on origin -- exactly the shape that fired 40 spurious
        #     findings on DLAPTOP-4 on 2026-07-30. Note case 3's lost_run_v3
        #     is the control: same shape, ordinary path, still a finding.
        write("evidence/experiments/_runner_signals/V3-EXQ-999.json",
              {"queue_id": "V3-EXQ-999", "run_id": "signal_run_v3",
               "outcome": "FAIL", "exit_reason": "clean",
               "manifest_path": "evidence/experiments/signal_run_v3.json",
               "pid": 1234, "schema_version": 1, "script": "x.py",
               "emitted_at": "2026-07-30T00:00:00Z"})
        #  6. DIVERGENT: run_id IS on origin (`kept_run_v3`, committed above)
        #     but this copy DISAGREES on a value rather than merely omitting
        #     writer-injected keys. Until 2026-07-30 step 1 cleared on run_id
        #     membership alone, so this -- the phantom-completion /
        #     partial-write shape -- produced no output whatsoever. Case 1 is
        #     the paired control: same run_id, genuinely a subset, still clear.
        write("evidence/experiments/kept_run_v3.json.bak.divergent",
              dict(kept, outcome="FAIL", elapsed_seconds=999.0))
        #  6b. and the parked-recovery shape the 2026-07-30 chip was raised
        #      for: a manifest whose ONLY origin copy sits outside the live
        #      evidence paths, under evidence/planning/recovered_stranded_
        #      manifests/ (committed above). It must CLEAR -- the index is
        #      whole-tree -- and it is pinned here because a future narrowing
        #      of build_index to evidence/experiments/ would silently re-strand
        #      every already-recovered run.
        write("evidence/experiments/oldexp/parked_run_v3.json.bak.20260530",
              flat("parked_run_v3"))

        r = subprocess.run(
            [sys.executable, "-", tmp, "REE_assembly:HEAD"],
            input=UNTRACKED_PY, capture_output=True, text=True, timeout=120)
        line = [x for x in r.stdout.splitlines()
                if x.startswith(UNTRACKED_MARKER)]
        if not line:
            print("  [FAIL] grader emitted no result (%s)"
                  % (r.stderr or "").strip()[-300:])
            return 1
        got = json.loads(line[0][len(UNTRACKED_MARKER):]).get("REE_assembly", {})

        bad = 0
        ids = sorted(f["run_id"] for f in got.get("findings", []))
        if ids != ["lost_run_v3"]:
            print(f"  [FAIL] grader findings {ids} != ['lost_run_v3']")
            bad += 1
        else:
            print("  [PASS] grader: stranded .bak found; superset, pack-form "
                  "and churn all correctly cleared")
        # notes must be EXACTLY these: any 'no_counterpart_other' here means
        # the basename / stem / superset / byte-compare clearing failed for a
        # file that plainly does exist on origin. dry_run is 2 -- one per
        # signal (filename prefix, and the doc flag) -- so a regression that
        # kept only one of the two shows up as a count, not as a silent pass.
        want_notes = {"per_tick": 1, "runner_signals": 1, "dry_run": 2}
        if got.get("notes") != want_notes:
            print(f"  [FAIL] notes {got.get('notes')} != {want_notes} "
                  f"-- a file present on origin was not cleared, or a "
                  f"by-design path was mis-graded")
            bad += 1
        else:
            print("  [PASS] grader: _per_tick.jsonl, a run_id-bearing "
                  "_runner_signals/ exit signal and BOTH --dry-run signals "
                  "are NOTES, not findings; superset + byte-compare verified")
        if got.get("ignored") != 1:
            print(f"  [FAIL] __pycache__ churn not ignored: {got.get('ignored')}")
            bad += 1
        else:
            print("  [PASS] grader: build churn ignored outright")
        # The three branches of the run_id step, asserted together because each
        # is the other two's control: same-run_id-subset CLEARS (case 1),
        # same-run_id-different-value is DIVERGENT (case 6), and a run whose
        # only origin copy is PARKED outside evidence/experiments/ also CLEARS
        # (case 6b). Asserting divergence alone would pass a grader that had
        # simply stopped clearing on run_id at all.
        dids = sorted(f["run_id"] for f in got.get("divergent", []))
        if dids != ["kept_run_v3"]:
            print(f"  [FAIL] divergent {dids} != ['kept_run_v3'] -- a same-"
                  f"run_id manifest with DIFFERENT content was cleared "
                  f"silently, or a subset/parked copy was wrongly flagged")
            bad += 1
        else:
            print("  [PASS] grader: same run_id + different content is "
                  "DIVERGENT, while the writer-superset copy and a copy parked "
                  "in recovered_stranded_manifests/ both still clear")
        dpaths = [p for f in got.get("divergent", [])
                  for p in (f.get("origin_paths") or [])]
        if dpaths != ["evidence/experiments/kept_run_v3.json"]:
            print(f"  [FAIL] divergent origin_paths {dpaths} -- the finding "
                  f"must name the origin copy it disagrees with, or it is not "
                  f"triageable")
            bad += 1
        else:
            print("  [PASS] grader: divergent finding names its origin copy")
        # content_sha256 is what a later adjudication matches on -- a missing
        # or wrong hash here means an adjudication could never fire (silent,
        # not a crash), so it is pinned by comparing against the LOCAL
        # untracked bytes computed the same way (raw dict -> json.dump ->
        # sha256), not a hardcoded literal that would drift with the fixture.
        exp_hash = hashlib.sha256(
            json.dumps(dict(kept, outcome="FAIL", elapsed_seconds=999.0)).encode(
                "utf-8")).hexdigest()
        dhashes = [f.get("content_sha256") for f in got.get("divergent", [])]
        if dhashes != [exp_hash]:
            print(f"  [FAIL] divergent content_sha256 {dhashes} != [{exp_hash}] "
                  f"-- an adjudication keyed on this hash could never match")
            bad += 1
        else:
            print("  [PASS] grader: divergent finding carries the LOCAL "
                  "copy's content_sha256, matching a direct hash of its bytes")
        bad += _selftest_ignored_bucket(tmp, root)
        return bad
    except Exception as exc:                      # pragma: no cover - defensive
        print(f"  [FAIL] grader selftest errored: {exc}")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _selftest_literature_grader():
    """Run the REAL worker-side grader source against literature evidence
    entries -- the class this chip adds
    (chip-20260819-githealth-untracked-literature-blindspot). Same method as
    _selftest_grader: build a throwaway git repo and execute UNTRACKED_PY
    exactly as the worker does, because the predicate under test is exactly
    the one that let a real GOV-BEHADJ-1/SD-005/ARC-010 entry sit untracked
    and unreported (as a silent `no_counterpart_other` note) for 6 days -- a
    hand-written dict cannot exercise the git plumbing that hid it.

    Six cases, one per way the literature grading could go wrong:
      1. committed content, untracked at a DIFFERENT review path, byte-
         identical -- CLEAR (a re-classified/duplicated entry; exercises the
         JSON-equal branch for record.json and the raw-byte branch for
         summary.md in one case).
      2. committed record.json is a SUPERSET of the untracked copy at a
         different review -- CLEAR (mirrors the run-manifest writer-injected-
         field pattern; exercises is_superset specifically, not mere byte
         equality).
      3. same slug tracked under one review, untracked under a DIFFERENT
         review with DISAGREEING content -- lit_divergent.
      4. slug absent from origin entirely, both files untracked -- TWO
         lit_findings (record.json AND summary.md graded independently; this
         is the real chip's own observed shape -- 2 STRANDED entries from 1
         orphaned entry).
      5. record.json committed, summary.md for the SAME slug + review
         untracked and absent from origin -- a NOTE (literature_partial),
         not a finding.
      6. a literature-tree file that is NOT record.json/summary.md under
         entries/<slug>/ (a review-level README) -- must fall through to the
         pre-existing no_counterpart_other note, proving LIT_ENTRY is scoped
         to the two real filenames only and does not over-match the tree.
    """
    import shutil
    import tempfile

    def record(entry_id, **extra):
        doc = {"schema_version": "literature_evidence/v1", "entry_id": entry_id,
               "confidence": 0.7}
        doc.update(extra)
        return doc

    tmp = tempfile.mkdtemp(prefix="rgh-lit-selftest-")
    try:
        root = os.path.join(tmp, "REE_assembly")
        os.makedirs(root)
        LIT = "evidence/literature/"

        def run(*args):
            subprocess.run(("git",) + args, cwd=root, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        def write(rel, obj_or_text, is_json=True):
            p = os.path.join(root, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as fh:
                if is_json:
                    json.dump(obj_or_text, fh)
                else:
                    fh.write(obj_or_text)

        run("init", "-q")
        run("config", "user.email", "selftest@local")
        run("config", "user.name", "selftest")

        # COMMITTED
        write(LIT + "targeted_review_a/entries/2026-01-01_kept/record.json",
              record("2026-01-01_kept", reviewer_note="landed"))
        write(LIT + "targeted_review_a/entries/2026-01-01_kept/summary.md",
              "kept summary\n", is_json=False)
        write(LIT + "targeted_review_a/entries/2026-01-02_superset_subset/record.json",
              record("2026-01-02_superset_subset", extra_field="origin_only"))
        write(LIT + "targeted_review_a/entries/2026-01-01_divergent/record.json",
              record("2026-01-01_divergent", confidence=0.9))
        write(LIT + "targeted_review_a/entries/2026-01-01_partial/record.json",
              record("2026-01-01_partial"))
        run("add", "-A")
        run("commit", "-q", "-m", "base")

        # UNTRACKED
        # 1. same slug, DIFFERENT review, byte-identical
        write(LIT + "targeted_review_b/entries/2026-01-01_kept/record.json",
              record("2026-01-01_kept", reviewer_note="landed"))
        write(LIT + "targeted_review_b/entries/2026-01-01_kept/summary.md",
              "kept summary\n", is_json=False)
        # 2. same slug, DIFFERENT review, local is a SUBSET of origin
        write(LIT + "targeted_review_c/entries/2026-01-02_superset_subset/record.json",
              record("2026-01-02_superset_subset"))
        # 3. same slug, DIFFERENT review, DISAGREEING content
        local_divergent = record("2026-01-01_divergent", confidence=0.5)
        write(LIT + "targeted_review_d/entries/2026-01-01_divergent/record.json",
              local_divergent)
        # 4. slug absent from origin at every path -- the real finding
        write(LIT + "targeted_review_a/entries/2026-01-03_orphan/record.json",
              record("2026-01-03_orphan"))
        write(LIT + "targeted_review_a/entries/2026-01-03_orphan/summary.md",
              "orphan summary\n", is_json=False)
        # 5. slug's record.json is committed; its summary.md is not, and does
        #    not exist on origin under this slug at any path
        write(LIT + "targeted_review_a/entries/2026-01-01_partial/summary.md",
              "partial summary\n", is_json=False)
        # 6. control: literature-tree file that is NOT an entries/<slug>/
        #    record.json or summary.md
        write(LIT + "targeted_review_a/README.md", "just a readme\n", is_json=False)

        r = subprocess.run(
            [sys.executable, "-", tmp, "REE_assembly:HEAD"],
            input=UNTRACKED_PY, capture_output=True, text=True, timeout=120)
        line = [x for x in r.stdout.splitlines()
                if x.startswith(UNTRACKED_MARKER)]
        if not line:
            print("  [FAIL] literature grader emitted no result (%s)"
                  % (r.stderr or "").strip()[-300:])
            return 1
        got = json.loads(line[0][len(UNTRACKED_MARKER):]).get("REE_assembly", {})

        bad = 0
        lit_findings = got.get("literature_findings") or []
        find_slugs = sorted(f.get("slug") for f in lit_findings)
        find_kinds = sorted(f.get("kind") for f in lit_findings)
        if find_slugs != ["2026-01-03_orphan", "2026-01-03_orphan"] or \
                find_kinds != ["record.json", "summary.md"]:
            print(f"  [FAIL] literature findings {lit_findings} -- want exactly "
                  f"the orphan slug's record.json AND summary.md, each its own "
                  f"finding, and nothing else")
            bad += 1
        else:
            print("  [PASS] literature grader: an orphaned entry absent from "
                  "origin at every path produces TWO findings (record.json + "
                  "summary.md graded independently), matching the real "
                  "2026-08-19 incident shape")

        lit_div = got.get("literature_divergent") or []
        if len(lit_div) != 1 or lit_div[0].get("slug") != "2026-01-01_divergent":
            print(f"  [FAIL] literature divergent {lit_div} != exactly "
                  f"['2026-01-01_divergent'] -- a same-slug entry with "
                  f"DIFFERENT content was cleared silently, or a subset/"
                  f"identical copy was wrongly flagged")
            bad += 1
        else:
            d = lit_div[0]
            exp_hash = hashlib.sha256(
                json.dumps(local_divergent).encode("utf-8")).hexdigest()
            want_path = LIT + "targeted_review_a/entries/2026-01-01_divergent/record.json"
            if d.get("origin_paths") != [want_path]:
                print(f"  [FAIL] literature divergent origin_paths {d.get('origin_paths')} "
                      f"-- must name the origin copy it disagrees with")
                bad += 1
            elif d.get("content_sha256") != exp_hash:
                print(f"  [FAIL] literature divergent content_sha256 "
                      f"{d.get('content_sha256')} != {exp_hash}")
                bad += 1
            else:
                print("  [PASS] literature grader: same slug + DIFFERENT "
                      "content is lit_divergent, naming the origin copy and "
                      "the LOCAL copy's content_sha256")

        notes = got.get("notes") or {}
        if notes.get("literature_partial") != 1:
            print(f"  [FAIL] literature grader: literature_partial note count "
                  f"{notes.get('literature_partial')} != 1 -- a slug whose "
                  f"OTHER file already landed must not be graded a full strand")
            bad += 1
        elif notes.get("no_counterpart_other") != 1:
            print(f"  [FAIL] literature grader: no_counterpart_other count "
                  f"{notes.get('no_counterpart_other')} != 1 -- a non-entry "
                  f"literature-tree file (README.md) either over-matched "
                  f"LIT_ENTRY or was mis-cleared")
            bad += 1
        else:
            print("  [PASS] literature grader: a slug whose sibling file "
                  "already landed is literature_partial (not a strand), and a "
                  "review-level README (not an entries/<slug>/ file) is "
                  "untouched by LIT_ENTRY and falls through as ordinary noise")

        cleared_slugs = {f.get("slug") for f in lit_findings} | \
                        {f.get("slug") for f in lit_div}
        if "2026-01-01_kept" in cleared_slugs or "2026-01-02_superset_subset" in cleared_slugs:
            print("  [FAIL] literature grader: a byte-identical or subset "
                  "copy at a different review path was reported instead of "
                  "clearing")
            bad += 1
        else:
            print("  [PASS] literature grader: a byte-identical copy and a "
                  "content-subset copy, each at a DIFFERENT review path than "
                  "origin, both CLEAR (re-classification / duplication is "
                  "not a strand)")

        if got.get("literature_truncated"):
            print(f"  [FAIL] unexpected literature_truncated "
                  f"{got.get('literature_truncated')}")
            bad += 1
        return bad
    except Exception as exc:                      # pragma: no cover - defensive
        print(f"  [FAIL] literature grading selftest errored: {exc}")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _selftest_prepull_grading():
    """GRADE each runner-prepull-untracked stash entry -- the containment
    report this chip added. Runs the REAL grader source (UNTRACKED_PY)
    against a throwaway repo carrying real `git stash push --include-
    untracked` entries, not hand-written dicts, for the same reason
    `_selftest_grader` does: the predicate under test is exactly the one that
    left 13 prepull entries on ree-cloud-3 unexamined behind a bare count,
    and a grader that has only ever seen fixtures it was designed around is
    unverified.

    Three entries, three outcomes:
      redundant   stashed content is a STRICT SUBSET of what the worktree
                  file now holds -- the shape a governance-reviewed landed
                  manifest takes (extra `queue_id` / reviewer fields on top
                  of what the worker wrote). Must grade "redundant", not
                  merely "byte-identical", or every reviewed run is
                  unretirable forever (module docstring / CLAUDE.md).
      at_risk     stashed content exists NOWHERE else -- not on disk, not on
                  origin. The genuine orphan shape; must stay named as
                  at-risk with its unproven path, never silently cleared.
      (excluded)  an ordinary, non-prepull stash must not be swept into the
                  graded set at all -- the label match is substring-exact.
    """
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="rgh-prepull-selftest-")
    try:
        root = os.path.join(tmp, "REE_assembly")
        os.makedirs(os.path.join(root, "evidence", "experiments"))

        def run(*args):
            subprocess.run(("git",) + args, cwd=root, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        def write(rel, text):
            p = os.path.join(root, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as fh:
                fh.write(text)

        run("init", "-q")
        run("config", "user.email", "selftest@local")
        run("config", "user.name", "selftest")
        write("README.md", "base\n")
        run("add", "-A")
        run("commit", "-q", "-m", "base")

        redundant_rel = "evidence/experiments/redundant_run_v3.json"
        atrisk_rel = "evidence/experiments/atrisk_run_v3.json"
        stashed_content = json.dumps(
            {"run_id": "redundant_run_v3", "outcome": "PASS"})
        # The landed copy is a SUPERSET, not a byte match -- the reviewed-
        # manifest shape the containment predicate exists for.
        landed_content = json.dumps(
            {"run_id": "redundant_run_v3", "outcome": "PASS",
             "queue_id": "V3-EXQ-001", "machine": "ree-cloud-2",
             "evidence_direction_note": "reviewed"})

        # Entry 1: stash it, then land a SUPERSET back into the worktree AND
        # commit it -- the shape of a collided pop whose content already
        # reached origin by another route. Committing (rather than leaving it
        # untracked) is deliberate: `git stash push --include-untracked`
        # sweeps up EVERY untracked path, not just the one just written, so an
        # untracked "landed" file here would get re-swept into entry 2's
        # stash below and silently vanish from the worktree before grading.
        write(redundant_rel, stashed_content)
        run("stash", "push", "--include-untracked", "-m",
            "runner-prepull-untracked")
        write(redundant_rel, landed_content)
        run("add", "-A")
        run("commit", "-q", "-m", "landed")

        # Entry 2: stash it and never recreate it anywhere -- the real
        # orphan shape (cloud-3's V3-EXQ-707c / ARC-110).
        write(atrisk_rel, json.dumps(
            {"run_id": "atrisk_run_v3", "outcome": "FAIL"}))
        run("stash", "push", "--include-untracked", "-m",
            "runner-prepull-untracked")

        # An ordinary stash, unrelated label -- must NOT be swept in.
        write("evidence/experiments/unrelated.json", "{}")
        run("stash", "push", "--include-untracked", "-m", "unrelated churn")

        r = subprocess.run(
            [sys.executable, "-", tmp, "REE_assembly:HEAD"],
            input=UNTRACKED_PY, capture_output=True, text=True, timeout=120)
        line = [x for x in r.stdout.splitlines()
                if x.startswith(UNTRACKED_MARKER)]
        if not line:
            print("  [FAIL] prepull grader emitted no result (%s)"
                  % (r.stderr or "").strip()[-300:])
            return 1
        got = json.loads(line[0][len(UNTRACKED_MARKER):]).get("REE_assembly", {})
        pg = got.get("prepull") or {}

        bad = 0
        if pg.get("count") != 2:
            print(f"  [FAIL] prepull count {pg.get('count')} != 2 -- the "
                  f"unrelated stash leaked in, or a real entry was missed")
            bad += 1
        else:
            print("  [PASS] prepull grader: exactly the 2 "
                  "runner-prepull-untracked entries counted, the unrelated "
                  "stash excluded by label")

        verdicts = [e.get("verdict") for e in pg.get("entries", [])]
        if sorted(verdicts) != ["at_risk", "redundant"]:
            print(f"  [FAIL] prepull verdicts {verdicts} -- want exactly one "
                  f"redundant and one at_risk")
            bad += 1
        else:
            print("  [PASS] prepull grader: superset-landed entry graded "
                  "redundant, orphaned entry graded at_risk")

        at_risk = next((e for e in pg.get("entries", [])
                        if e.get("verdict") == "at_risk"), {})
        if atrisk_rel not in (at_risk.get("unproven_paths") or []):
            print(f"  [FAIL] at-risk entry did not name its unproven path: "
                  f"{at_risk}")
            bad += 1
        else:
            print("  [PASS] prepull grader: at-risk entry names its "
                  "unproven path")
        return bad
    except Exception as exc:                      # pragma: no cover - defensive
        print(f"  [FAIL] prepull grading selftest errored: {exc}")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _selftest_ignored_bucket(tmp, root):
    """The --ignored bucket, on the exact rule that hid the class: `*.bak`.

    Reuses the repo built by _selftest_grader. Pins three things:
      * a plain-.bak run manifest is INVISIBLE to the untracked pass (this is
        the blind spot, asserted as a fact rather than assumed),
      * --ignored finds it, in a SEPARATE bucket (never in `findings`, which
        would silently raise the severity of a deliberately-ignored path),
      * an ignored DIRECTORY is counted, not descended into. On the Mac that
        is `.claude/` = ~50 worktrees; a bucket that walked it would be the
        "probe nobody runs" outcome the module docstring warns about.
    """
    def write(rel, obj):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            json.dump(obj, fh)

    # `*.bak` is REE_assembly/.gitignore:13 verbatim. `hidden_dir/` stands in
    # for `.claude/`.
    with open(os.path.join(root, ".gitignore"), "w") as fh:
        fh.write("*.bak\nhidden_dir/\n")
    subprocess.run(("git", "add", ".gitignore"), cwd=root, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(("git", "commit", "-q", "-m", "ignore"), cwd=root, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    write("evidence/experiments/hidden_run_v3.json.bak",
          {"run_id": "hidden_run_v3", "outcome": "FAIL", "elapsed_seconds": 99.0})
    write("hidden_dir/deep/another_run_v3.json",
          {"run_id": "another_run_v3", "outcome": "FAIL"})

    def run_grader(*extra):
        r = subprocess.run(
            [sys.executable, "-", tmp, "REE_assembly:HEAD"] + list(extra),
            input=UNTRACKED_PY, capture_output=True, text=True, timeout=120)
        line = [x for x in r.stdout.splitlines() if x.startswith(UNTRACKED_MARKER)]
        if not line:
            return None
        return json.loads(line[0][len(UNTRACKED_MARKER):]).get("REE_assembly", {})

    bad = 0
    plain = run_grader()
    if plain is None:
        print("  [FAIL] grader emitted no result for the ignored-bucket case")
        return 1
    if any(f["run_id"] == "hidden_run_v3" for f in plain.get("findings", [])):
        print("  [FAIL] a gitignored .bak appeared in the UNTRACKED findings")
        bad += 1
    elif "gitignored" in plain:
        print("  [FAIL] the gitignored bucket ran without --ignored")
        bad += 1
    else:
        print("  [PASS] grader: a gitignored *.bak manifest is invisible to "
              "the untracked pass (the documented blind spot, asserted)")

    ign = run_grader("--ignored")
    g = (ign or {}).get("gitignored") or {}
    hits = sorted(f["run_id"] for f in g.get("findings", []))
    if hits != ["hidden_run_v3"]:
        print(f"  [FAIL] --ignored bucket findings {hits} != ['hidden_run_v3']")
        bad += 1
    elif any(f["run_id"] == "hidden_run_v3" for f in ign.get("findings", [])):
        print("  [FAIL] the gitignored hit was promoted into `findings`")
        bad += 1
    elif g.get("dirs_skipped") != 1:
        print(f"  [FAIL] ignored directory not counted as skipped: {g}")
        bad += 1
    elif any(f["run_id"] == "another_run_v3" for f in g.get("findings", [])):
        print("  [FAIL] the bucket descended into an ignored DIRECTORY")
        bad += 1
    else:
        print("  [PASS] grader: --ignored finds it in a SEPARATE bucket, and "
              "ignored directories are counted, not walked")
    return bad


def _selftest_local_target():
    """The local (Mac) target: path layout from the record, and NO ssh.

    Two things this must prove, because both were structurally impossible
    before 2026-07-30 and a regression to either silently un-grades the Mac:

      1. the checkout root comes from the TARGET RECORD -- the probe text for
         the Mac must not contain a worker path, and vice versa;
      2. probing a local target never shells out to ssh. Asserted by recording
         every subprocess argv for the duration of a REAL local probe against a
         throwaway repo, not by reading the dispatch and trusting it.
    """
    import shutil
    import tempfile

    bad = 0
    mac = FLEET.get("DLAPTOP-4")
    if mac is None or mac.ip is not None:
        print("  [FAIL] no local (ip-less) DLAPTOP-4 target in FLEET")
        return 1
    if mac.base != LOCAL_BASE or not mac.multi_session:
        print(f"  [FAIL] DLAPTOP-4 record wrong: {mac}")
        bad += 1
    else:
        print("  [PASS] local target: DLAPTOP-4 present, ip-less, multi_session")

    worker = FLEET["ree-cloud-2"]
    mac_probe = build_probe(mac.base)
    w_probe = build_probe(worker.base)
    if LOCAL_BASE not in mac_probe or REMOTE_BASE in mac_probe:
        print("  [FAIL] the Mac's probe does not carry the Mac's base path")
        bad += 1
    elif REMOTE_BASE not in w_probe or LOCAL_BASE in w_probe:
        print("  [FAIL] the worker's probe does not carry the worker base path")
        bad += 1
    else:
        print("  [PASS] local target: checkout root comes from the record, "
              "not from a hardcoded path")

    # 2. a real local probe, with every subprocess argv recorded.
    calls = []
    real_run = subprocess.run

    class _Recorder(object):
        def __getattr__(self, k):
            return getattr(subprocess, k)

        def run(self, args, **kw):
            calls.append(list(args) if isinstance(args, (list, tuple)) else [args])
            return real_run(args, **kw)

    tmp = tempfile.mkdtemp(prefix="rgh-local-")
    saved = globals()["subprocess"]
    try:
        root = os.path.join(tmp, "REE_assembly")
        os.makedirs(os.path.join(root, "evidence", "experiments"))
        for a in (("init", "-q"), ("config", "user.email", "s@l"),
                  ("config", "user.name", "s")):
            real_run(("git",) + a, cwd=root, check=True,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(os.path.join(root, "README.md"), "w") as fh:
            fh.write("x\n")
        real_run(("git", "add", "-A"), cwd=root, check=True,
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        real_run(("git", "commit", "-q", "-m", "base"), cwd=root, check=True,
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # The grader reads REPO_REFS' ref (origin/master), not @{u} -- so the
        # ref has to EXIST for this to grade anything. Without it grade_repo
        # returns "ref not readable" and reports no findings at all, which is
        # correct behaviour (better than declaring every path stranded against
        # a tree it could not read) but would make this case vacuous.
        real_run(("git", "update-ref", "refs/remotes/origin/master", "HEAD"),
                 cwd=root, check=True,
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # One genuine strand, so this exercises the WHOLE local chain --
        # shell probe, grader, merge, classify -- rather than only proving a
        # clean tree stays quiet. A transport that silently dropped the
        # grader's findings would otherwise pass every case above.
        with open(os.path.join(root, "evidence", "experiments",
                               "lost_v3.json"), "w") as fh:
            json.dump({"run_id": "lost_v3", "outcome": "FAIL",
                       "elapsed_seconds": 5661.46}, fh)

        local = Target("selftest-local", "local", tmp, None, True)
        globals()["subprocess"] = _Recorder()
        # fetch OFF: there is no remote here, and the point of the case is the
        # transport, not the refresh (which _selftest_fetch_is_local_only pins).
        repos, err = probe(local, timeout=120, untracked=True, fetch=False)
    finally:
        globals()["subprocess"] = saved
        shutil.rmtree(tmp, ignore_errors=True)

    if err:
        print(f"  [FAIL] local probe errored: {err}")
        return bad + 1
    sshed = [c for c in calls if c and str(c[0]).endswith("ssh")]
    if sshed:
        print(f"  [FAIL] local probe shelled out to ssh: {sshed[0]}")
        bad += 1
    elif not calls:
        print("  [FAIL] local probe ran no subprocess at all")
        bad += 1
    else:
        print(f"  [PASS] local target: probed in-process, 0 ssh invocations "
              f"across {len(calls)} subprocess call(s)")

    d = (repos or {}).get("REE_assembly")
    if not isinstance(d, dict):
        print(f"  [FAIL] local probe returned no REE_assembly row: {repos}")
        return bad + 1
    if d.get("unmerged") != "0" or d.get("missing") == "1":
        print(f"  [FAIL] local probe mis-read a clean checkout: {d}")
        bad += 1
    elif not isinstance(d.get("untracked"), dict) or d["untracked"].get("error"):
        print(f"  [FAIL] local probe did not attach a usable grader result: {d}")
        bad += 1
    else:
        print("  [PASS] local target: shell probe and grader both ran and "
              "their results merged on the same repo row")
        found = [f.get("run_id") for f in (d["untracked"].get("findings") or [])]
        status, reasons = classify(d)
        blob = " ".join(reasons)
        if found != ["lost_v3"]:
            print(f"  [FAIL] local probe lost the strand: findings {found}")
            bad += 1
        elif "lost_v3" not in blob or "STRANDED" not in blob:
            print(f"  [FAIL] the strand did not reach the report: {reasons}")
            bad += 1
        elif status != "OK":
            print(f"  [FAIL] a strand changed the checkout status to {status}")
            bad += 1
        elif not d["untracked"].get("rechecked"):
            print("  [FAIL] a multi_session target was not re-checked")
            bad += 1
        else:
            print("  [PASS] local target: a real strand survives the re-check "
                  "and reaches the report END TO END, without failing the box")
    # ree-v3 is absent from this base -- it must be reported missing, not
    # silently dropped, or a Mac with a deleted checkout would grade 'clean'.
    if (repos or {}).get("ree-v3", {}).get("missing") != "1":
        print("  [FAIL] an absent repo was not reported as missing")
        bad += 1
    else:
        print("  [PASS] local target: an absent repo is MISSING, not skipped")
    return bad


def _selftest_claims():
    """TASK_CLAIMS cross-check: live work must not grade as a strand.

    Case 1 is the real one. `ree-v3/coordinator/deploy/runner-prestart-pull.sh`
    was untracked, absent from origin/main and absent from ALL history on
    2026-07-30 -- a finding by every git-visible test -- and was in-flight work
    under claim `friendly-antonelli-b0f414`, committed minutes later. On this
    box git CANNOT make that call; the claims file is the only discriminator.
    """
    import tempfile

    claims_doc = {
        "schema_version": "v1",
        "stale_after_hours": 6,
        "claims": [
            {"session_id": "friendly-antonelli-b0f414",
             "claimed_at": "2026-07-30T07:45:37Z", "status": "active",
             "resources": ["ree-v3/experiment_runner.py",
                           "ree-v3/coordinator/deploy"]},
            {"session_id": "quirky-mayer-ee5ad2",
             "claimed_at": "2026-07-30T06:54:47Z", "status": "active",
             "resources": ["./ree-v3/experiments/"]},
            {"session_id": "closed-session-aaaaaa",
             "claimed_at": "2026-07-29T00:00:00Z", "status": "done",
             "resources": ["REE_assembly/evidence/experiments"]},
        ],
    }
    fd, path = tempfile.mkstemp(prefix="rgh-claims-", suffix=".json")
    with os.fdopen(fd, "w") as fh:
        json.dump(claims_doc, fh)
    try:
        claims = load_active_claims(path)
    finally:
        os.unlink(path)

    bad = 0
    if len(claims) != 2:
        print(f"  [FAIL] a non-active claim was loaded: {claims}")
        bad += 1
    else:
        print("  [PASS] claims: only ACTIVE entries shield; a `done` one does not")

    checks = [
        # (repo, path, expected covering session or None, what it pins)
        ("ree-v3", "coordinator/deploy/runner-prestart-pull.sh",
         "friendly-antonelli-b0f414", "directory claim covers a file under it"),
        ("ree-v3", "experiments/v3_exq_748a_mech457_hrep_zworldp0_rederivation.py",
         "quirky-mayer-ee5ad2", "'./x/' normalises to 'x' before matching"),
        ("ree-v3", "experiment_runner.py", "friendly-antonelli-b0f414",
         "exact file claim"),
        # the trap: a bare string prefix would match this, and it is a
        # DIFFERENT directory. Every finding under a sibling dir would be
        # silently downgraded and never looked at again.
        ("ree-v3", "coordinator/deploy_old/x.json", None,
         "a sibling directory is NOT covered"),
        ("ree-v3", "experiment_runner.py.bak", None,
         "a longer filename sharing a prefix is NOT covered"),
        # scoped to the right repo: same relative path, wrong repo.
        ("REE_assembly", "experiment_runner.py", None,
         "matching is repo-qualified"),
        ("REE_assembly", "evidence/experiments/x_v3.json", None,
         "a `done` claim's resource does not cover anything"),
    ]
    for repo, rel, want, what in checks:
        got = claim_covering(claims, repo, rel)
        sid = got["session_id"] if got else None
        if sid != want:
            print(f"  [FAIL] claims: {repo}/{rel} -> {sid}, want {want} ({what})")
            bad += 1
    if not bad:
        print(f"  [PASS] claims: all {len(checks)} containment cases correct "
              f"(incl. sibling-directory and prefix traps)")

    # ...and the downgrade itself: finding -> claim_covered, never both.
    graded = {"ree-v3": {"untracked": 2, "findings": [
        {"path": "coordinator/deploy/runner-prestart-pull.sh",
         "run_id": "live_run_v3", "outcome": "FAIL"},
        {"path": "evidence/orphan_run_v3.json",
         "run_id": "orphan_run_v3", "outcome": "FAIL"},
    ], "notes": {}}}
    apply_claims(graded, claims)
    info = graded["ree-v3"]
    left = [f["run_id"] for f in info["findings"]]
    cov = [f["run_id"] for f in info.get("claim_covered", [])]
    if left != ["orphan_run_v3"] or cov != ["live_run_v3"]:
        print(f"  [FAIL] claims: downgrade wrong -- findings {left}, covered {cov}")
        bad += 1
    elif info["claim_covered"][0]["claim"]["session_id"] != "friendly-antonelli-b0f414":
        print("  [FAIL] claims: the covered finding does not NAME its claim")
        bad += 1
    else:
        print("  [PASS] claims: a claim-covered manifest becomes a NOTE naming "
              "its session; an unclaimed one stays a FINDING")

    # a claim-covered path must NOT read as a strand in the printed report...
    status, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=info))
    blob = " ".join(reasons)
    if status != "OK":
        print(f"  [FAIL] claims: claim-covered path changed status to {status}")
        bad += 1
    elif "friendly-antonelli-b0f414" not in blob:
        print("  [FAIL] claims: the covering session is not named in the report")
        bad += 1
    elif "orphan_run_v3" not in blob or "STRANDED" not in blob:
        print("  [FAIL] claims: the genuine strand stopped being reported")
        bad += 1
    else:
        print("  [PASS] claims: report names the covering session AND still "
              "reports the genuine strand beside it")

    # ...and claims must be scoped to the box the registry describes: a worker
    # has its own checkout, so the Mac's claims say nothing about it.
    if claims_for_target(FLEET["ree-cloud-2"]):
        print("  [FAIL] claims applied to a remote worker")
        bad += 1
    elif claims_for_target(FLEET["DLAPTOP-4"], enabled=False):
        print("  [FAIL] --no-claims did not disable the cross-check")
        bad += 1
    else:
        print("  [PASS] claims: applied to the multi-session local target only")

    # fail-open: an unreadable registry must never turn into an exception or
    # into 'everything is claimed'.
    if load_active_claims("/nonexistent/TASK_CLAIMS.json") != []:
        print("  [FAIL] claims: a missing registry did not fail open")
        bad += 1
    else:
        print("  [PASS] claims: a missing/unreadable registry fails open")
    return bad


def _selftest_adjudicated_divergence():
    """Adjudicated-benign divergence cross-check (chip
    chip-20260809-githealth-adjudicated-divergence-note).

    The real case (README_ree-cloud-2_2026-08-09.md section 2): v3_exq_850's
    untracked cloud-2 copy diverges from origin's packed copy, confirmed
    benign by a structural diff. Without this, the SAME finding re-escalates
    on every future probe forever. The three branches this must get right:
    an exact-content match downgrades to a note; the SAME run_id with
    DIFFERENT content (the untracked copy edited again, or a genuinely new
    phantom-completion) must NOT be silently swallowed by a stale
    adjudication; and with no adjudication record at all, behaviour is
    unchanged from before this chip.
    """
    import tempfile

    kept_hash = hashlib.sha256(
        json.dumps({"run_id": "v3_exq_850_x_v3", "outcome": "FAIL"}).encode(
            "utf-8")).hexdigest()
    drifted_hash = hashlib.sha256(
        json.dumps({"run_id": "v3_exq_850_x_v3", "outcome": "FAIL",
                    "edited": True}).encode("utf-8")).hexdigest()

    adjudications_doc = {
        "schema_version": 1,
        "adjudications": [
            {"host": "ree-cloud-2", "repo": "REE_assembly",
             "run_id": "v3_exq_850_x_v3", "content_sha256": kept_hash,
             "adjudicated_at": "2026-08-09T20:07:00Z",
             "reference": ("evidence/planning/recovered_stranded_manifests/"
                           "README_ree-cloud-2_2026-08-09.md")},
            # malformed -- missing content_sha256 -- must be DROPPED at load,
            # not loaded with a None standing in for "matches anything".
            {"host": "ree-cloud-3", "repo": "REE_assembly",
             "run_id": "some_other_run_v3"},
        ],
    }
    fd, path = tempfile.mkstemp(prefix="rgh-adjudications-", suffix=".json")
    with os.fdopen(fd, "w") as fh:
        json.dump(adjudications_doc, fh)
    try:
        records = load_adjudicated_divergences(path)
    finally:
        os.unlink(path)

    bad = 0
    if len(records) != 1:
        print(f"  [FAIL] a malformed (no content_sha256) record was loaded: "
              f"{records}")
        bad += 1
    else:
        print("  [PASS] adjudications: a record missing content_sha256 is "
              "dropped at load, not loaded as a wildcard")

    checks = [
        # (host, repo, run_id, sha, want_matched, what)
        ("ree-cloud-2", "REE_assembly", "v3_exq_850_x_v3", kept_hash, True,
         "exact host/repo/run_id/hash match"),
        ("ree-cloud-3", "REE_assembly", "v3_exq_850_x_v3", kept_hash, False,
         "same content on a DIFFERENT host is not covered"),
        ("ree-cloud-2", "ree-v3", "v3_exq_850_x_v3", kept_hash, False,
         "same content in a DIFFERENT repo is not covered"),
        ("ree-cloud-2", "REE_assembly", "v3_exq_850_x_v3", drifted_hash, False,
         "the SAME run_id with DIFFERENT content is NOT covered by a stale "
         "adjudication"),
        ("ree-cloud-2", "REE_assembly", "v3_exq_850_x_v3", None, False,
         "a missing local content_sha256 never matches (fails closed)"),
        ("ree-cloud-2", "REE_assembly", "unrelated_run_v3", kept_hash, False,
         "a different run_id is not covered"),
    ]
    for host, repo, run_id, sha, want, what in checks:
        got = adjudication_covering(records, host, repo, run_id, sha)
        if (got is not None) != want:
            print(f"  [FAIL] adjudication_covering({host}, {repo}, {run_id}, "
                  f"...) matched={got is not None}, want {want} ({what})")
            bad += 1
    if not bad:
        print(f"  [PASS] adjudications: all {len(checks)} host/repo/run_id/"
              f"content-hash containment cases correct")

    # ...the downgrade itself: divergent -> adjudicated_divergent, never both,
    # and the SAME run_id at a DIFFERENT content hash must stay a live finding
    # beside it -- the confound this whole mechanism exists to avoid.
    graded = {"REE_assembly": {"divergent": [
        {"path": "evidence/experiments/v3_exq_850_x_v3.json",
         "run_id": "v3_exq_850_x_v3", "outcome": "FAIL",
         "content_sha256": kept_hash},
        {"path": "evidence/experiments/v3_exq_850_x_v3.json.bak.new",
         "run_id": "v3_exq_850_x_v3", "outcome": "FAIL",
         "content_sha256": drifted_hash},
    ]}}
    apply_adjudications("ree-cloud-2", graded, records)
    info = graded["REE_assembly"]
    left = [f["content_sha256"] for f in info["divergent"]]
    adj = [f["run_id"] for f in info.get("adjudicated_divergent", [])]
    if left != [drifted_hash] or adj != ["v3_exq_850_x_v3"]:
        print(f"  [FAIL] adjudications: downgrade wrong -- divergent left "
              f"{left}, adjudicated {adj}")
        bad += 1
    elif info["adjudicated_divergent"][0]["adjudication"]["reference"] != (
            "evidence/planning/recovered_stranded_manifests/"
            "README_ree-cloud-2_2026-08-09.md"):
        print("  [FAIL] adjudications: the downgraded entry does not NAME "
              "its adjudicating write-up")
        bad += 1
    else:
        print("  [PASS] adjudications: the exact-content match becomes a "
              "NOTE naming its adjudication; the drifted-content sibling "
              "with the SAME run_id stays a live divergent finding")

    # ...on a DIFFERENT host, the identical content must NOT downgrade --
    # host-scoping is load-bearing, not incidental.
    graded2 = {"REE_assembly": {"divergent": [
        {"path": "evidence/experiments/v3_exq_850_x_v3.json",
         "run_id": "v3_exq_850_x_v3", "outcome": "FAIL",
         "content_sha256": kept_hash},
    ]}}
    apply_adjudications("ree-cloud-3", graded2, records)
    if graded2["REE_assembly"].get("adjudicated_divergent"):
        print("  [FAIL] adjudications: downgraded on the WRONG host")
        bad += 1
    else:
        print("  [PASS] adjudications: identical content on a different "
              "host does not downgrade")

    # ...and the printed report: an adjudicated entry reads as a quiet note
    # naming the review, a genuinely new divergence beside it still escalates
    # in full -- mirrors the claim_covered / real-strand coexistence pattern.
    status, reasons = classify(dict(
        branch="master", unmerged="0", behind="0", skew="0", gclog="0",
        stashes="0", first="", untracked=dict(
            untracked=2, ignored=0, truncated=0, notes={},
            findings=[], divergent=[
                {"path": "evidence/experiments/v3_exq_850_x_v3.json.bak.new",
                 "run_id": "v3_exq_850_x_v3", "outcome": "FAIL",
                 "origin_paths": ["evidence/experiments/v3_exq_850_x_v3.json"]},
            ],
            adjudicated_divergent=[
                {"path": "evidence/experiments/v3_exq_850_x_v3.json",
                 "run_id": "v3_exq_850_x_v3",
                 "adjudication": {
                     "adjudicated_at": "2026-08-09T20:07:00Z",
                     "reference": ("evidence/planning/"
                                   "recovered_stranded_manifests/"
                                   "README_ree-cloud-2_2026-08-09.md")}},
            ])))
    blob = " ".join(reasons)
    if status != "OK":
        print(f"  [FAIL] adjudications: an adjudicated divergence changed "
              f"status to {status}")
        bad += 1
    elif "ADJUDICATED" not in blob or "README_ree-cloud-2_2026-08-09.md" not in blob:
        print("  [FAIL] adjudications: the adjudicated note does not name "
              "its review write-up in the report")
        bad += 1
    elif "Diff both before deleting EITHER" not in blob:
        print("  [FAIL] adjudications: the genuinely-still-divergent sibling "
              "stopped being escalated")
        bad += 1
    else:
        print("  [PASS] adjudications: report names the adjudicating review "
              "for the settled entry AND still escalates the live divergent "
              "sibling beside it")

    # fail-open: an unreadable registry must never turn into an exception or
    # a downgrade of everything.
    if load_adjudicated_divergences("/nonexistent/adjudications.json") != []:
        print("  [FAIL] adjudications: a missing registry did not fail open")
        bad += 1
    else:
        print("  [PASS] adjudications: a missing/unreadable registry fails "
              "open")

    # --no-adjudications parity: an empty records list must be a true no-op,
    # never touching the input at all.
    graded3 = {"REE_assembly": {"divergent": [
        {"path": "x", "run_id": "v3_exq_850_x_v3",
         "content_sha256": kept_hash}]}}
    apply_adjudications("ree-cloud-2", graded3, [])
    if "adjudicated_divergent" in graded3["REE_assembly"]:
        print("  [FAIL] adjudications: an empty records list still downgraded")
        bad += 1
    else:
        print("  [PASS] adjudications: an empty records list "
              "(--no-adjudications) is a true no-op")
    return bad


def _selftest_parent_crosscheck():
    """The v3_exq_614 false-positive fix: a WORKER's STRANDED finding cleared
    against the PARENT (Mac) checkout's own fresh index.

    Two layers, mirroring the split the rest of this file already uses
    (classify() vs the real grader): the downgrade logic
    (crosscheck_stranded_against_parent) is asserted against hand-built
    dicts first, then build_parent_index() is asserted END TO END against a
    REAL temp git repo -- a parent-index builder that has only ever run
    against a dict is exactly as unverified as a grader that has only ever
    seen a healthy tree (see _selftest_grader's docstring).
    """
    bad = 0

    # 1. The downgrade itself: flat match, pack match, and a genuinely absent
    #    run_id that must stay a finding.
    graded = {"REE_assembly": {"findings": [
        {"path": "evidence/experiments/flat_v3.json.bak.20260530",
         "run_id": "flat_v3", "outcome": "FAIL"},
        {"path": "evidence/experiments/pack_v3.json.bak.20260530",
         "run_id": "pack_v3", "outcome": "FAIL"},
        {"path": "evidence/experiments/genuinely_lost_v3.json.bak.20260530",
         "run_id": "genuinely_lost_v3", "outcome": "FAIL"},
    ], "notes": {}}}
    parent_index = {"REE_assembly": {"flat_runs": ["flat_v3"],
                                     "pack_runs": ["pack_v3"]}}
    crosscheck_stranded_against_parent(graded, parent_index)
    info = graded["REE_assembly"]
    left = sorted(f["run_id"] for f in info["findings"])
    cleared = {f["run_id"]: f["parent_form"]
               for f in info.get("parent_cleared", [])}
    if left != ["genuinely_lost_v3"]:
        print(f"  [FAIL] parent crosscheck: findings left {left}, want only "
              f"the genuine strand")
        bad += 1
    elif cleared != {"flat_v3": "flat", "pack_v3": "pack"}:
        print(f"  [FAIL] parent crosscheck: cleared {cleared}, want "
              f"flat_v3=flat pack_v3=pack")
        bad += 1
    elif info["notes"].get("parent_cleared") != 2:
        print(f"  [FAIL] parent crosscheck: notes count wrong: {info['notes']}")
        bad += 1
    else:
        print("  [PASS] parent crosscheck: flat- and pack-form matches both "
              "clear, a genuinely absent run_id stays a finding")

    # fail-open: a repo missing from the parent index, or an empty index
    # outright, must leave every finding exactly as graded.
    graded2 = {"REE_assembly": {"findings": [
        {"path": "evidence/experiments/x_v3.json.bak", "run_id": "x_v3",
         "outcome": "FAIL"}], "notes": {}}}
    crosscheck_stranded_against_parent(graded2, {"ree-v3": {"flat_runs": ["x_v3"]}})
    left2 = [f["run_id"] for f in graded2["REE_assembly"]["findings"]]
    if graded2["REE_assembly"].get("parent_cleared") or left2 != ["x_v3"]:
        print("  [FAIL] parent crosscheck: a repo absent from the parent "
              "index was not left untouched")
        bad += 1
    else:
        print("  [PASS] parent crosscheck: repo absent from the parent "
              "index fails open (findings untouched)")
    graded3 = {"REE_assembly": {"findings": [
        {"path": "evidence/experiments/y_v3.json.bak", "run_id": "y_v3",
         "outcome": "FAIL"}], "notes": {}}}
    crosscheck_stranded_against_parent(graded3, {})
    left3 = [f["run_id"] for f in graded3["REE_assembly"]["findings"]]
    if graded3["REE_assembly"].get("parent_cleared") or left3 != ["y_v3"]:
        print("  [FAIL] parent crosscheck: an empty parent index did not "
              "fail open")
        bad += 1
    else:
        print("  [PASS] parent crosscheck: an empty parent index fails open")

    # 2. build_parent_index() end to end, against a REAL temp git repo -- the
    #    v3_exq_614 shape exactly: a run committed in BOTH flat and pack
    #    form, so its run_id lands in both flat_runs and pack_runs.
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="rgh-parentidx-")
    try:
        root = os.path.join(tmp, "REE_assembly")
        os.makedirs(os.path.join(root, "evidence", "experiments", "someexp",
                                 "runs", "v3_exq_614_x_v3"))

        def run(*args):
            subprocess.run(("git",) + args, cwd=root, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        run("init", "-q")
        run("config", "user.email", "selftest@local")
        run("config", "user.name", "selftest")
        manifest = {"run_id": "v3_exq_614_x_v3", "outcome": "FAIL"}
        with open(os.path.join(root, "evidence", "experiments",
                               "v3_exq_614_x_v3.json"), "w") as fh:
            json.dump(manifest, fh)
        with open(os.path.join(root, "evidence", "experiments", "someexp",
                               "runs", "v3_exq_614_x_v3", "manifest.json"),
                 "w") as fh:
            json.dump(manifest, fh)
        run("add", "-A")
        run("commit", "-q", "-m", "base")
        # No real remote in this throwaway repo -- point origin/master at
        # HEAD directly, exactly as _selftest_local_target does, and build
        # WITHOUT fetching (there is nothing to fetch from).
        run("update-ref", "refs/remotes/origin/master", "HEAD")

        idx = build_parent_index(base=tmp, fetch=False)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    ri = idx.get("REE_assembly", {})
    if "v3_exq_614_x_v3" not in (ri.get("flat_runs") or []):
        print(f"  [FAIL] build_parent_index: flat_runs missing the run: {ri}")
        bad += 1
    elif "v3_exq_614_x_v3" not in (ri.get("pack_runs") or []):
        print(f"  [FAIL] build_parent_index: pack_runs missing the run: {ri}")
        bad += 1
    else:
        print("  [PASS] build_parent_index: a real committed run reaches "
              "both flat_runs and pack_runs via a real ls-tree + "
              "build_index pass")

    # ...and END TO END: the exact confirmed incident, wired through both
    # layers -- a worker's STRANDED finding for v3_exq_614, cleared by the
    # parent index just built from a REAL repo, not a hand-built dict.
    worker_graded = {"REE_assembly": {"findings": [
        {"path": ("evidence/experiments/v3_exq_614_x_v3"
                  "_20260529T191318Z_v3.json.bak.20260530"),
         "run_id": "v3_exq_614_x_v3", "outcome": "FAIL"}], "notes": {}}}
    crosscheck_stranded_against_parent(worker_graded, idx)
    info = worker_graded["REE_assembly"]
    if info["findings"] or not info.get("parent_cleared"):
        print(f"  [FAIL] the confirmed v3_exq_614 shape did not clear end "
              f"to end: {info}")
        bad += 1
    else:
        status, reasons = classify(dict(
            branch="master", unmerged="0", behind="0", skew="0", gclog="0",
            stashes="0", first="",
            untracked=dict(untracked=1, ignored=0, truncated=0,
                           notes=info["notes"], ref="origin/master",
                           ref_age_hours=9.1, findings=info["findings"],
                           parent_cleared=info["parent_cleared"])))
        blob = " ".join(reasons)
        if status != "OK" or "STRANDED" in blob or "v3_exq_614_x_v3" not in blob:
            print(f"  [FAIL] end-to-end confirmed shape did not reach the "
                  f"report cleanly: status={status} reasons={reasons}")
            bad += 1
        else:
            print("  [PASS] END TO END: a worker's STRANDED v3_exq_614-"
                  "shaped finding is cleared by a REAL parent index and "
                  "reaches the report as CLEARED, not STRANDED")

    # fail-open at the build layer: a nonexistent base must return {}, never
    # raise, so a caller can always treat the result as "no cross-check
    # available" rather than crashing the whole probe over it.
    if build_parent_index(base="/nonexistent-rgh-parent-base", fetch=False) != {}:
        print("  [FAIL] build_parent_index did not fail open on a missing base")
        bad += 1
    else:
        print("  [PASS] build_parent_index: a missing parent base fails "
              "open ({})")
    return bad


def _selftest_recheck_and_host_resolution():
    """The re-check intersection, and --host alias resolution."""
    bad = 0
    calls = []

    def fake_grader(base, ignored, timeout):
        calls.append(base)
        # second pass: the _dry_-shaped transient is gone, the real one stays.
        return {"REE_assembly": {"findings": [
            {"path": "evidence/real_v3.json", "run_id": "real_v3"}]}}

    graded = {"REE_assembly": {"findings": [
        {"path": "evidence/real_v3.json", "run_id": "real_v3"},
        {"path": "evidence/_dry_x_v3.json", "run_id": "x_v3"},
    ]}}
    saved = globals()["_run_grader_local"]
    globals()["_run_grader_local"] = fake_grader
    try:
        out = _recheck(FLEET["DLAPTOP-4"], graded, False, 60)
        clean = _recheck(FLEET["DLAPTOP-4"], {"REE_assembly": {"findings": []}},
                         False, 60)
    finally:
        globals()["_run_grader_local"] = saved

    info = out["REE_assembly"]
    if [f["run_id"] for f in info["findings"]] != ["real_v3"]:
        print(f"  [FAIL] recheck kept the wrong findings: {info['findings']}")
        bad += 1
    elif info.get("transient") != 1:
        print(f"  [FAIL] the vanished finding was not counted: {info}")
        bad += 1
    elif len(calls) != 1:
        print(f"  [FAIL] recheck ran {len(calls)} extra pass(es), want 1")
        bad += 1
    elif clean["REE_assembly"].get("rechecked"):
        print("  [FAIL] recheck ran a second pass on a clean first pass")
        bad += 1
    else:
        print("  [PASS] recheck: only findings surviving BOTH passes are "
              "reported, vanished ones are counted, a clean pass costs nothing")

    for spelling in ("mac", "MAC", "local", "DLAPTOP-4", "dlaptop-4",
                     "dlaptop-4.local"):
        got = resolve_hosts([spelling])
        if list(got or {}) != ["DLAPTOP-4"]:
            print(f"  [FAIL] --host {spelling} -> {list(got or {})}")
            bad += 1
            break
    else:
        print("  [PASS] --host: every spelling of the Mac resolves to DLAPTOP-4")
    if resolve_hosts(["nope"]) is not None:
        print("  [FAIL] --host: an unknown name did not report as unknown")
        bad += 1
    elif len(resolve_hosts(None)) != len(FLEET):
        print("  [FAIL] --host: the default no longer selects the whole fleet")
        bad += 1
    else:
        print("  [PASS] --host: unknown names rejected, default is whole fleet")
    return bad


def _selftest_fetch_is_local_only():
    """`git fetch` must run for a local target and NEVER for a worker.

    The fetch is the one write-ish step in the whole probe. A regression that
    let it run over ssh would be a network write to a box that may be
    mid-experiment, against the promise in the module docstring.
    """
    bad = 0
    fetched = []
    saved = globals()["_fetch_local"]
    globals()["_fetch_local"] = lambda base, timeout=120: fetched.append(base) or []
    real_run = subprocess.run
    saved_sub = globals()["subprocess"]

    class _Blocked(object):
        def __getattr__(self, k):
            return getattr(saved_sub, k)

        def run(self, args, **kw):
            if args and str(args[0]).endswith("ssh"):
                # do not actually reach the network from a selftest
                raise AssertionError("ssh attempted")
            return real_run(args, **kw)

    try:
        globals()["subprocess"] = _Blocked()
        probe(FLEET["ree-cloud-2"], timeout=1, untracked=False)
    except AssertionError:
        pass                                       # expected: ssh was attempted
    except Exception:
        pass                                       # any other failure is fine here
    finally:
        globals()["subprocess"] = saved_sub
        globals()["_fetch_local"] = saved

    if fetched:
        print(f"  [FAIL] fetch ran for a REMOTE target: {fetched}")
        bad += 1
    else:
        print("  [PASS] fetch: never runs for an ssh target")

    fetched = []
    globals()["_fetch_local"] = lambda base, timeout=120: fetched.append(base) or []
    try:
        probe(Target("t", "local", "/nonexistent-base", None, True))
        if fetched:
            print("  [FAIL] fetch ran against a base that does not exist")
            bad += 1
        else:
            print("  [PASS] fetch: skipped when the local base is absent")
        here = Target("t", "local", os.path.dirname(os.path.abspath(__file__)),
                      None, True)
        probe(here, timeout=30, untracked=False, fetch=False)
        if fetched:
            print("  [FAIL] --no-fetch did not disable the fetch")
            bad += 1
        else:
            print("  [PASS] fetch: --no-fetch disables it")
        # ...and the positive: a local target IS fetched by default. Without
        # this the whole suite would pass with the fetch deleted, and the Mac
        # would grade against whatever origin/master it last happened to see.
        probe(here, timeout=30, untracked=False)
        if fetched != [here.base]:
            print(f"  [FAIL] fetch did not run for a local target: {fetched}")
            bad += 1
        else:
            print("  [PASS] fetch: runs by default for a local target")
    finally:
        globals()["_fetch_local"] = saved
    return bad


def main():
    ap = argparse.ArgumentParser(
        description="Probe fleet workers for wedged / skewed / gc-blocked git checkouts.")
    ap.add_argument("--host", action="append",
                    help="limit to this target (repeatable), e.g. ree-cloud-2; "
                         "'mac' / 'local' resolve to DLAPTOP-4")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--no-untracked", action="store_true",
                    help="skip grading untracked working-tree files against "
                         "origin (faster, but blind to the 2026-07-30 "
                         "stranded-manifest class -- see module docstring)")
    ap.add_argument("--ignored", action="store_true",
                    help="also grade GITIGNORED files into a separate, "
                         "lower-severity bucket (*.bak is ignored in "
                         "REE_assembly, so that class is otherwise unexamined)")
    ap.add_argument("--no-fetch", action="store_true",
                    help="do not refresh remote-tracking refs on a LOCAL "
                         "target first (a stale origin ref manufactures "
                         "strands out of content that already landed)")
    ap.add_argument("--no-recheck", action="store_true",
                    help="do not re-grade a multi-session target to drop "
                         "findings that vanish between passes")
    ap.add_argument("--no-claims", action="store_true",
                    help="do not cross-check findings against active "
                         "TASK_CLAIMS entries (they are what distinguishes a "
                         "strand from another session's live work)")
    ap.add_argument("--no-adjudications", action="store_true",
                    help="do not downgrade a divergent finding that exactly "
                         "matches a recorded adjudicated-benign verdict "
                         "(evidence/planning/git_health_adjudicated_divergences"
                         ".json) -- every divergence reports in full")
    ap.add_argument("--no-parent-crosscheck", action="store_true",
                    help="do not cross-check a WORKER's STRANDED finding "
                         "against the PARENT (Mac) checkout's own freshly-"
                         "fetched index (this is what clears the v3_exq_614 "
                         "false-positive shape -- see module docstring); "
                         "never touches a worker, only re-reads the Mac's own "
                         "checkout")
    ap.add_argument("--selftest", action="store_true",
                    help="assert classify(), the untracked grader, local "
                         "target resolution and the claim cross-check against "
                         "recorded real states (no ssh, no network)")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    targets = resolve_hosts(args.host)
    if targets is None:
        print(f"no such host; known: {', '.join(sorted(FLEET))} "
              f"(aliases: {', '.join(sorted(HOST_ALIASES))})")
        return 2

    report = {}
    bad = False
    stranded = 0
    divergent = 0
    adjudicated_hits = 0
    graded = 0
    gitignored_hits = 0
    lit_stranded = 0
    lit_divergent = 0
    # Loaded at most once per run -- the file is small and host-scoped inside
    # apply_adjudications, so re-reading it per target would be pure overhead
    # for no additional freshness within a single invocation.
    adjudications = [] if args.no_adjudications else load_adjudicated_divergences()
    # Built at most once per run, lazily -- only once a WORKER target (t.ip is
    # not None) actually needs it, so a Mac-only invocation (`--host mac`)
    # never pays for it. Shared across every worker target in this run: the
    # parent's own ref does not change target-to-target, and a second
    # `_fetch_local` per worker would be redundant network/subprocess cost
    # for no additional freshness. See build_parent_index() / the module
    # docstring's "LABELLING IS NOT THE SAME AS RESOLVING" paragraph.
    parent_index = None
    for name, t in sorted(targets.items()):
        repos, err = probe(t, untracked=not args.no_untracked,
                           ignored=args.ignored, fetch=not args.no_fetch,
                           recheck=not args.no_recheck)
        if err:
            report[name] = {"role": t.role, "ip": t.ip, "base": t.base,
                            "error": err}
            continue
        claims = claims_for_target(t, enabled=not args.no_claims)
        apply_claims({r: repos[r].get("untracked") for r in repos
                      if isinstance(repos[r].get("untracked"), dict)}, claims)
        apply_adjudications(name, {r: repos[r].get("untracked") for r in repos
                      if isinstance(repos[r].get("untracked"), dict)}, adjudications)
        # Parent-index cross-check: WORKER targets only (t.ip is not None).
        # The Mac's own findings are already graded against this exact ref
        # (freshly fetched by _probe_local), so cross-checking them against
        # themselves would be a no-op at best.
        if (t.ip is not None and not args.no_untracked
                and not args.no_parent_crosscheck):
            if parent_index is None:
                parent_index = build_parent_index(fetch=not args.no_fetch)
            crosscheck_stranded_against_parent(
                {r: repos[r].get("untracked") for r in repos
                 if isinstance(repos[r].get("untracked"), dict)},
                parent_index)
        report[name] = {"role": t.role, "ip": t.ip, "base": t.base,
                        "repos": {}}
        for repo in REPOS:
            d = repos.get(repo)
            if d is None:
                continue
            status, reasons = classify(d)
            if status in ("WEDGED", "SKEW", "GC-BLOCKED", "MISSING"):
                bad = True
            u = d.get("untracked")
            if isinstance(u, dict) and not u.get("error"):
                graded += int(u.get("untracked") or 0)
                stranded += len(u.get("findings") or [])
                stranded += int(u.get("truncated") or 0)
                divergent += len(u.get("divergent") or [])
                adjudicated_hits += len(u.get("adjudicated_divergent") or [])
                lit_stranded += len(u.get("literature_findings") or [])
                lit_stranded += int(u.get("literature_truncated") or 0)
                lit_divergent += len(u.get("literature_divergent") or [])
                g = u.get("gitignored")
                if isinstance(g, dict):
                    gitignored_hits += len(g.get("findings") or [])
                    divergent += len(g.get("divergent") or [])
                    adjudicated_hits += len(g.get("adjudicated_divergent") or [])
            report[name]["repos"][repo] = {
                "status": status, "reasons": reasons, "raw": d,
            }

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1 if bad else 0

    print("Fleet git health (active probe -- telemetry cannot see this; see module docstring)")
    print()
    for name in sorted(report):
        e = report[name]
        tag = f"{name} ({e['role']})"
        if "error" in e:
            # UNREACHABLE is deliberately NOT a failure: workers are powered
            # off routinely by the cloud-scaler. `hcloud server list` is the
            # authority on power state. A LOCAL target cannot be "powered off",
            # so the power-state hint would be actively misleading there -- an
            # unreachable local base means the path is wrong or the checkout is
            # gone, which is worth acting on immediately.
            print(f"  {tag:26s} UNREACHABLE -- {e['error']}")
            if e.get("ip") is None:
                print(f"  {'':26s}   (local target: check {e.get('base', '?')} exists)")
            else:
                print(f"  {'':26s}   (may simply be powered off; check `hcloud server list`)")
            continue
        for repo, r in e["repos"].items():
            print(f"  {tag:26s} {repo:14s} {r['status']}")
            for reason in r["reasons"]:
                # Paths come off a remote filesystem; keep stdout ASCII-safe
                # (CLAUDE.md: printed output must survive a cp1252 terminal).
                reason = reason.encode("ascii", "replace").decode("ascii")
                print(f"  {'':26s} {'':14s}   - {reason}")
        tag = ""
    print()
    # State the coverage explicitly even when clean -- otherwise there is no
    # way to tell a probe that looked and found nothing from one that did not
    # look, which is exactly the ambiguity this pass was added to remove.
    if args.no_untracked:
        print("untracked grading: SKIPPED (--no-untracked) -- stranded run "
              "manifests AND literature evidence entries would not be "
              "visible in this run")
    else:
        adj_suffix = (f" ({adjudicated_hits} more already adjudicated benign "
                      f"and not re-escalated)" if adjudicated_hits else "")
        print(f"untracked grading: {graded} untracked path(s) graded against "
              f"origin, {stranded} stranded run manifest(s), "
              f"{divergent} same-run_id-different-content{adj_suffix}, "
              f"{lit_stranded} stranded literature evidence entry(ies), "
              f"{lit_divergent} same-slug-different-content")
    if args.ignored:
        print(f"gitignored grading: {gitignored_hits} run manifest(s) found in "
              f"gitignored path(s) (ignored DIRECTORIES are not descended into)")
    else:
        print("gitignored grading: SKIPPED (pass --ignored) -- *.bak is "
              "gitignored in REE_assembly, so plain-.bak files are not visible "
              "to the untracked pass")
    if bad:
        print()
        print("ACTION: at least one checkout is WEDGED / SKEWED / gc-blocked.")
        print("  A WEDGED worker keeps heartbeating, claiming and PASSing while")
        print("  executing stale code -- it will NOT surface on its own.")
        print("  Repair: clear the unmerged state, then re-run the skew check")
        print("  (CLAUDE.md 'HEAD/worktree skew'). Preserve any file not on")
        print("  origin BEFORE resetting -- stranded stashes have held the only")
        print("  surviving copy of completed-run evidence.")
    else:
        print("All probed checkouts structurally clean.")
    if stranded:
        print()
        print("ACTION: a box is holding run manifest(s) that exist NOWHERE")
        print("  on origin. Under Phase 3 a completed experiment reaches origin")
        print("  via the coordinator spool, so a manifest that never got there")
        print("  is lost the moment that checkout is reset, cleaned, gc'd or")
        print("  destroyed -- and it looks perfectly healthy.")
        print("  Recover FIRST (scp the file off; the coordinator DB signature")
        print("  is experiments.status=completed with ZERO rows in results),")
        print("  then land it. Worked example:")
        print("  evidence/planning/recovered_stranded_manifests/")
        print("    README_ree-cloud-2_2026-07-30.md")
        # Only when a MULTI-SESSION box actually holds one -- the hint is about
        # how to act on a finding there, and printing it for a worker's strand
        # would tell the reader their finding was claim-checked when it was not.
        if any(n in FLEET and FLEET[n].multi_session
               and any((r["raw"].get("untracked") or {}).get("findings")
                       for r in (e.get("repos") or {}).values())
               for n, e in report.items()):
            print()
            print("  On DLAPTOP-4 specifically: a finding here has ALREADY been")
            print("  checked against active TASK_CLAIMS and re-graded once. If")
            print("  it survived both, treat it as real -- but still confirm no")
            print("  session opened a claim in between, and NEVER `git checkout")
            print("  -- .` on that tree (other sessions' live work).")
    if lit_stranded:
        print()
        print("ACTION: a box is holding literature evidence entry(ies) that")
        print("  exist NOWHERE on origin under their slug. A regen that globs")
        print("  the working tree (build_experiment_indexes.py's literature")
        print("  indexer) can bake this in as a permanent dangling citation")
        print("  the moment it runs on this box -- see audit_dangling_")
        print("  citations.py. Land it BEFORE any reset/clean/gc/regen.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
