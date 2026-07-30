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

And the thing it must NOT do: fire on ordinary runner churn. A probe that
false-positives on normal worker state gets ignored -- the failure mode
`audit_vendored_copies.py`'s NOTE-vs-finding split exists to avoid. So a path
is a FINDING only when it has no counterpart on origin AND parses as a run
manifest (`run_id` + `outcome`). `*_per_tick.jsonl` is by-design local (ZERO
exist anywhere on origin/master -- verified 2026-07-30) and
`runner_status/*.bak.*` is transient telemetry; both are NOTEs, counted and
carried in --json, never printed as findings.

Exit status is 1 if any machine is WEDGED / SKEWED / gc-blocked, so this can
gate a scheduled check. Stranded manifests and stashes REPORT without changing
the exit status -- like the stash signal they are a "look at this now" flag for
a human, not a fault in the checkout, and this script chains. Power state is
NOT inferred -- `hcloud server list` is the authority (CLAUDE.md); an
unreachable host is reported as UNREACHABLE, not as healthy and not as broken.

The whole probe is READ-ONLY on the worker: it never writes, stashes, drops,
pulls or resets, and never touches a running experiment.

USAGE
-----
    python3 scripts/runner_git_health.py                # whole fleet
    python3 scripts/runner_git_health.py --host ree-cloud-2
    python3 scripts/runner_git_health.py --json
    python3 scripts/runner_git_health.py --no-untracked # skip the heavier pass
    python3 scripts/runner_git_health.py --selftest     # no ssh, no network
"""

import argparse
import base64
import json
import os
import subprocess
import sys

# Affinity name -> ip. Mirrors the table in CLAUDE.md ("Workers may need
# waking"). ree-cloud-1 is the HUB (coordinator + sync_daemon); it is probed
# read-only like any other, but never act on it without care -- its writers are
# the coordination-data plane for the whole fleet.
FLEET = {
    "ree-cloud-1": ("91.98.130.117", "hub"),
    "ree-cloud-2": ("116.203.216.181", "worker"),
    "ree-cloud-3": ("46.62.170.133", "worker"),
    "ree-cloud-4": ("91.99.68.94", "worker"),
}

# Upstream ref per repo -- what an untracked file is graded AGAINST. These are
# the default branches from CLAUDE.md's push table, not `@{u}`, because a
# worker's HEAD can be detached or on a stale branch and the question being
# asked is "does this content exist on the trunk everyone else reads".
REPO_REFS = {
    "REE_assembly": "origin/master",
    "ree-v3": "origin/main",
}
REPOS = tuple(REPO_REFS)
REMOTE_BASE = "/home/ree/REE_Working"

# A worker pulls every ~60s, so a healthy checkout is within a handful of
# commits of origin. This threshold only drives the advisory BEHIND label --
# WEDGED / SKEW / GC-BLOCKED are structural and are never threshold-based.
BEHIND_WARN = 50

# Probe script. Emits one "repo|k=v|..." line per repo. Kept POSIX-sh simple
# and read-only: it must never mutate a worker's tree.
PROBE = r'''
for r in REE_assembly ree-v3; do
  d=/home/ree/REE_Working/$r
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
import json, os, re, subprocess, sys

MAX_FINDINGS = 25
MAX_BYTES = 8 * 1024 * 1024
MAX_CANDIDATES = 8
MAX_OTHER_PATHS = 10

# By-design-local paths. Verified 2026-07-30 against origin/master: ZERO
# *_per_tick.jsonl blobs exist there, so their absence from origin is the
# design and not a loss. runner_status / runner_commands / runner_heartbeats
# are transient telemetry, materialised on origin only by the phase3 writers.
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


def grade_repo(root, ref):
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

    byname = {}
    flat_runs = set()
    pack_runs = set()
    for p in tree:
        b = p.rsplit("/", 1)[-1]
        byname.setdefault(b, []).append(p)
        if b.endswith(".json"):
            flat_runs.add(b[:-5])
        i = p.find("/runs/")
        if i != -1:
            rest = p[i + 6:]
            j = rest.find("/")
            if j > 0:
                pack_runs.add(rest[:j])

    findings = []
    notes = {}
    other_paths = []
    ignored = 0
    truncated = 0
    for rel in untracked:
        if CHURN.search(rel):
            ignored += 1
            continue
        base = rel.rsplit("/", 1)[-1]
        m = BAK.match(base)
        stem = m.group(1) if m else None

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

        run_id = ""
        if isinstance(doc, dict) and doc.get("run_id") and doc.get("outcome"):
            run_id = str(doc["run_id"])

        # 0) A BYDESIGN path is NEVER graded as a run manifest, however
        #    manifest-shaped it looks. Dropping run_id here (rather than
        #    relying on the BYDESIGN tag loop at the bottom) is what actually
        #    suppresses it: the finding branch below fires FIRST, so a
        #    _runner_signals/*.json -- run_id + outcome, but only a POINTER to
        #    a manifest -- would otherwise never reach that loop.
        if run_id:
            for rx, _name in BYDESIGN:
                if rx.search(rel):
                    run_id = ""
                    break

        # 1) Run-manifest grading. A run whose id is on origin ANYWHERE -- flat
        #    `<run_id>.json` or pack `.../runs/<run_id>/manifest.json` -- is not
        #    stranded, whatever the local copy happens to be called.
        if run_id and (run_id in flat_runs or run_id in pack_runs):
            continue

        # 2) Basename grading, on the name AND on the de-.bak'd stem.
        cands = list(byname.get(base, ()))
        if stem:
            cands += byname.get(stem, ())
        matched = False
        for p in cands[:MAX_CANDIDATES]:
            blob = git(root, "show", "%s:%s" % (ref, p))
            if blob is None:
                continue
            odoc = as_json(blob)
            if doc is not None and odoc is not None:
                if is_superset(odoc, doc):
                    matched = True
                    break
            elif raw is not None and blob == raw:
                matched = True
                break
        if matched:
            continue

        # FINDING only for a real run manifest with no counterpart anywhere.
        if run_id:
            if len(findings) >= MAX_FINDINGS:
                truncated += 1
                continue
            findings.append({
                "path": rel,
                "run_id": run_id,
                "outcome": str(doc.get("outcome"))[:40],
                "elapsed_seconds": doc.get("elapsed_seconds"),
                "bytes": len(raw or ""),
            })
            continue

        tag = "no_counterpart_other"
        for rx, name in BYDESIGN:
            if rx.search(rel):
                tag = name
                break
        notes[tag] = notes.get(tag, 0) + 1
        # NAME the un-attributable ones (bounded). They stay NOTES -- not run
        # manifests, so not the loss class this fires on -- but a bare count is
        # not triageable, and the first live run turned up two planning docs
        # (evidence/planning/sd037_consumer_input_distributions_*.md on
        # ree-cloud-4) absent from origin. Carried in --json only, so the
        # default output's noise budget is unchanged.
        if tag == "no_counterpart_other" and len(other_paths) < MAX_OTHER_PATHS:
            other_paths.append(rel)

    return {"untracked": len(untracked), "ignored": ignored,
            "findings": findings, "truncated": truncated, "notes": notes,
            "no_counterpart_other_paths": other_paths}


def main():
    base = sys.argv[1]
    out = {}
    for spec in sys.argv[2:]:
        repo, _, ref = spec.partition(":")
        root = os.path.join(base, repo)
        if not os.path.isdir(os.path.join(root, ".git")):
            continue
        out[repo] = grade_repo(root, ref)
    sys.stdout.write("UNTRACKED_JSON " + json.dumps(out, sort_keys=True) + "\n")


main()
'''

UNTRACKED_MARKER = "UNTRACKED_JSON "


def build_probe(untracked=True):
    """Assemble the remote script. One ssh, one `sh -s`, read-only throughout.

    The grader is base64'd rather than heredoc'd: the script itself arrives on
    the worker's stdin, and a heredoc would then have to be read from that same
    stream. base64 keeps it a single argument with no quoting hazards.
    """
    if not untracked:
        return PROBE
    blob = base64.b64encode(UNTRACKED_PY.encode("utf-8")).decode("ascii")
    specs = " ".join(f"{r}:{ref}" for r, ref in sorted(REPO_REFS.items()))
    return (
        PROBE
        + f"printf '%s' '{blob}' | base64 -d | python3 - {REMOTE_BASE} {specs}\n"
    )


def probe(ip, timeout=180, untracked=True):
    """Run the probe on one host. Returns (repos_dict, error_or_None)."""
    try:
        r = subprocess.run(
            ["ssh", "-o", "ConnectTimeout=15", "-o", "BatchMode=yes",
             f"ree@{ip}", "sh -s"],
            input=build_probe(untracked), capture_output=True, text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None, "probe timed out"
    except Exception as exc:                      # pragma: no cover - defensive
        return None, f"probe failed: {exc}"
    if r.returncode != 0:
        return None, (r.stderr or "").strip().splitlines()[-1] if r.stderr else "ssh failed"
    out = {}
    graded = {}
    for line in r.stdout.splitlines():
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
    for repo, info in (graded or {}).items():
        if repo in out and isinstance(info, dict):
            out[repo]["untracked"] = info
    return out, None


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
        # 2026-07-30 on, so a NON-ZERO count now means either a worker still
        # running pre-fix code, or entries whose pop keeps colliding -- both
        # need a human, neither is self-healing.
        reasons.append(
            f"{_int('prepull')} runner-prepull-untracked stash entry(ies) -- "
            f"orphaned-stash leak residue; these have held the ONLY copy of "
            f"completed runs. Inspect with `git stash show -p <ref>` and "
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
        strand = u.get("findings") or []
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

    failed += _selftest_grader()
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
        # notes must be EXACTLY the per_tick one: any 'no_counterpart_other'
        # here means the basename / stem / superset / byte-compare clearing
        # failed for a file that plainly does exist on origin.
        want_notes = {"per_tick": 1, "runner_signals": 1}
        if got.get("notes") != want_notes:
            print(f"  [FAIL] notes {got.get('notes')} != {want_notes} "
                  f"-- a file present on origin was not cleared, or a "
                  f"by-design path was mis-graded")
            bad += 1
        else:
            print("  [PASS] grader: _per_tick.jsonl and a run_id-bearing "
                  "_runner_signals/ exit signal are NOTES, not findings; "
                  "superset + byte-compare clearing verified")
        if got.get("ignored") != 1:
            print(f"  [FAIL] __pycache__ churn not ignored: {got.get('ignored')}")
            bad += 1
        else:
            print("  [PASS] grader: build churn ignored outright")
        return bad
    except Exception as exc:                      # pragma: no cover - defensive
        print(f"  [FAIL] grader selftest errored: {exc}")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(
        description="Probe fleet workers for wedged / skewed / gc-blocked git checkouts.")
    ap.add_argument("--host", action="append",
                    help="limit to this affinity name (repeatable), e.g. ree-cloud-2")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--no-untracked", action="store_true",
                    help="skip grading untracked working-tree files against "
                         "origin (faster, but blind to the 2026-07-30 "
                         "stranded-manifest class -- see module docstring)")
    ap.add_argument("--selftest", action="store_true",
                    help="assert classify() and the untracked grader against "
                         "recorded real states (no ssh, no network)")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    targets = {k: v for k, v in FLEET.items()
               if not args.host or k in args.host}
    if not targets:
        print(f"no such host; known: {', '.join(sorted(FLEET))}")
        return 2

    report = {}
    bad = False
    stranded = 0
    graded = 0
    for name, (ip, role) in sorted(targets.items()):
        repos, err = probe(ip, untracked=not args.no_untracked)
        if err:
            report[name] = {"role": role, "ip": ip, "error": err}
            continue
        report[name] = {"role": role, "ip": ip, "repos": {}}
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
            # authority on power state.
            print(f"  {tag:26s} UNREACHABLE -- {e['error']}")
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
              "manifests would not be visible in this run")
    else:
        print(f"untracked grading: {graded} untracked path(s) graded against "
              f"origin, {stranded} stranded run manifest(s)")
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
        print("ACTION: a worker is holding run manifest(s) that exist NOWHERE")
        print("  on origin. Under Phase 3 a completed experiment reaches origin")
        print("  via the coordinator spool, so a manifest that never got there")
        print("  is lost the moment that worker is reset, cleaned, gc'd or")
        print("  destroyed -- and the checkout looks perfectly healthy.")
        print("  Recover FIRST (scp the file off; the coordinator DB signature")
        print("  is experiments.status=completed with ZERO rows in results),")
        print("  then land it. Worked example:")
        print("  evidence/planning/recovered_stranded_manifests/")
        print("    README_ree-cloud-2_2026-07-30.md")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
