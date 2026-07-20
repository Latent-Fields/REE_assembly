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

Exit status is 1 if any machine is WEDGED / SKEWED / gc-blocked, so this can
gate a scheduled check. Power state is NOT inferred -- `hcloud server list` is
the authority (CLAUDE.md); an unreachable host is reported as UNREACHABLE, not
as healthy and not as broken.

USAGE
-----
    python3 scripts/runner_git_health.py                # whole fleet
    python3 scripts/runner_git_health.py --host ree-cloud-2
    python3 scripts/runner_git_health.py --json
"""

import argparse
import json
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

REPOS = ("REE_assembly", "ree-v3")
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
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  behind=$(git rev-list --count HEAD..@{u} 2>/dev/null || echo -1)
  first=$(git ls-files -u 2>/dev/null | awk '{print $4}' | sort -u | head -1)
  echo "$r|branch=$branch|unmerged=$unmerged|behind=$behind|skew=$skew|gclog=$gclog|stashes=$stashes|first=$first"
done
'''


def probe(ip, timeout=45):
    """Run the probe on one host. Returns (repos_dict, error_or_None)."""
    try:
        r = subprocess.run(
            ["ssh", "-o", "ConnectTimeout=15", "-o", "BatchMode=yes",
             f"ree@{ip}", "sh -s"],
            input=PROBE, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None, "probe timed out"
    except Exception as exc:                      # pragma: no cover - defensive
        return None, f"probe failed: {exc}"
    if r.returncode != 0:
        return None, (r.stderr or "").strip().splitlines()[-1] if r.stderr else "ssh failed"
    out = {}
    for line in r.stdout.splitlines():
        parts = line.strip().split("|")
        if len(parts) < 2:
            continue
        d = {}
        for kv in parts[1:]:
            if "=" in kv:
                k, _, v = kv.partition("=")
                d[k] = v
        out[parts[0]] = d
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
    if _int("stashes") > 0:
        reasons.append(f"{_int('stashes')} stash entry(ies) -- may strand evidence; inspect before dropping")
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
        ("missing checkout", "MISSING", dict(missing="1")),
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
    print()
    print("selftest: %d case(s) FAILED" % failed if failed else "selftest: all cases pass")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(
        description="Probe fleet workers for wedged / skewed / gc-blocked git checkouts.")
    ap.add_argument("--host", action="append",
                    help="limit to this affinity name (repeatable), e.g. ree-cloud-2")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--selftest", action="store_true",
                    help="assert classify() against recorded real states (no ssh)")
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
    for name, (ip, role) in sorted(targets.items()):
        repos, err = probe(ip)
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
                print(f"  {'':26s} {'':14s}   - {reason}")
        tag = ""
    print()
    if bad:
        print("ACTION: at least one checkout is WEDGED / SKEWED / gc-blocked.")
        print("  A WEDGED worker keeps heartbeating, claiming and PASSing while")
        print("  executing stale code -- it will NOT surface on its own.")
        print("  Repair: clear the unmerged state, then re-run the skew check")
        print("  (CLAUDE.md 'HEAD/worktree skew'). Preserve any file not on")
        print("  origin BEFORE resetting -- stranded stashes have held the only")
        print("  surviving copy of completed-run evidence.")
    else:
        print("All probed checkouts clean.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
