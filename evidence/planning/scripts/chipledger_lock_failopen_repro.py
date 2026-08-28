#!/opt/local/bin/python3
"""Reproduction harness for chip_ledger.py's LEDGER MUTATION LOCK fail-open.

Landed 2026-08-28 by chip-20260827-chipledger-lockfailopen-sweep-investigation.
Findings write-up: REE_assembly/evidence/planning/
chipledger_lock_failopen_investigation_20260828.md

WHAT IT DOES. Builds a throwaway umbrella-shaped git repo (optionally already
push-WEDGED, the state the real fail-opens fired in), runs N REAL concurrent
chip_ledger.py `record` processes against it, and reports two things per trial:

  LOSS  -- a brand-new chip_ref that reached NEITHER origin NOR the working
           tree, while its process exited 0. This is the silent loss.
  SWEEP -- a commit carrying a chip_ref its own message never names. This is
           the benign-looking symptom that motivated the investigation.

WHY IT IS NOT A TEST (and must not be turned into one without the fix landing
first). It DEMONSTRATES A DEFECT: the loss arm is red by design today. A
regression test belongs with the fix, asserting the loss does NOT happen.
Kept here, out of scripts/, so run_scripts_tests.sh never collects it.

ARMS (see the write-up for the measured numbers):
  --wait 180                       control: the lock working. 0 loss, 0 sweep.
  --wait 0                         all writers unlocked (the PRE-lock state).
  --wedged --asymmetric --wait 0   the REAL shape: one lock holder plus
                                   waiters that timed out and proceeded.

ASCII-only output. Never touches the real REE_Working checkout.

Usage:
  chipledger_lock_failopen_repro.py --trials 6 --writers 4 --wait 180
  chipledger_lock_failopen_repro.py --trials 6 --writers 3 --wait 0 \
      --wedged --asymmetric [--waiter-delay 1.5]
  chipledger_lock_failopen_repro.py ... --seed-from /path/to/TASK_CHIPS.json
"""

import argparse, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

# Overridable so this runs on a cloud box too; children get REE_WORKING_ROOT
# pointed at the throwaway repo, never at the real checkout.
SCRIPTS = Path(os.environ.get("REE_UMBRELLA_SCRIPTS",
                              "/Users/dgolden/REE_Working/scripts"))


def run(argv, **kw):
    return subprocess.run(argv, capture_output=True, text=True, **kw)


def git(repo, *a):
    p = run(["git", "-C", str(repo)] + list(a))
    return p


def build_repo(tmp, seed_path, with_origin):
    repo = tmp / "REE_Working"
    repo.mkdir()
    run(["git", "-C", str(repo), "init", "-q", "-b", "master"])
    run(["git", "-C", str(repo), "config", "user.name", "Test"])
    run(["git", "-C", str(repo), "config", "user.email", "t@example.com"])
    os.symlink(str(SCRIPTS), str(repo / "scripts"))
    (repo / ".git" / "info").mkdir(parents=True, exist_ok=True)
    (repo / ".git" / "info" / "exclude").write_text("scripts\n")
    if seed_path:
        shutil.copyfile(seed_path, repo / "TASK_CHIPS.json")
    else:
        (repo / "TASK_CHIPS.json").write_text(
            json.dumps({"schema_version": "task_chips/v1", "chips": []}, indent=2) + "\n")
    run(["git", "-C", str(repo), "add", "TASK_CHIPS.json"])
    run(["git", "-C", str(repo), "commit", "-q", "-m", "seed"])
    origin = None
    if with_origin:
        origin = tmp / "origin.git"
        run(["git", "init", "-q", "--bare", "-b", "master", str(origin)])
        run(["git", "-C", str(repo), "remote", "add", "origin", str(origin)])
        run(["git", "-C", str(repo), "push", "-q", "origin", "master"])
        run(["git", "-C", str(repo), "branch", "--set-upstream-to=origin/master", "master"])
    return repo, origin


def chips_of(text):
    if not (text or "").strip():
        return {}
    d = json.loads(text)
    return {c.get("chip_ref"): c for c in (d.get("chips") or []) if c.get("chip_ref")}


def make_wedged(repo, tmp, n):
    """Put the checkout in the shape the real DLAPTOP box was in when the
    fail-opens fired: local branch AHEAD of origin and origin AHEAD of local,
    so every ree_commit push is rejected and falls into the slow
    cherry-pick-onto-origin + faithfulness-proof path."""
    other = tmp / ("other%d" % n)
    run(["git", "clone", "-q", str(tmp / "origin.git"), str(other)])
    run(["git", "-C", str(other), "config", "user.name", "Other"])
    run(["git", "-C", str(other), "config", "user.email", "o@example.com"])
    (other / "OTHER.txt").write_text("origin moved on\n")
    run(["git", "-C", str(other), "add", "OTHER.txt"])
    run(["git", "-C", str(other), "commit", "-q", "-m", "origin moves ahead"])
    run(["git", "-C", str(other), "push", "-q", "origin", "master"])
    # local moves ahead too, on an unrelated path
    (repo / "LOCAL.txt").write_text("local ahead\n")
    run(["git", "-C", str(repo), "add", "LOCAL.txt"])
    run(["git", "-C", str(repo), "commit", "-q", "-m", "local ahead"])


def trial(n, writers, seed_path, with_origin, wait, wedged=False, asymmetric=False,
          waiter_delay=0.35):
    tmp = Path(tempfile.mkdtemp(prefix="failopen_repro_"))
    try:
        repo, origin = build_repo(tmp, seed_path, with_origin)
        if wedged and with_origin:
            make_wedged(repo, tmp, n)
        base_refs = set(chips_of((repo / "TASK_CHIPS.json").read_text()))
        refs = ["chip-repro-%03d-w%d" % (n, i) for i in range(writers)]
        procs = []
        for i, r in enumerate(refs):
            env = dict(os.environ)
            env["REE_WORKING_ROOT"] = str(repo)
            # asymmetric: writer 0 holds the lock normally; the rest fail open
            # immediately -- the REAL shape (one holder + N waiters that timed out).
            env["REE_CHIP_LEDGER_LOCK_WAIT_SECONDS"] = "180" if (asymmetric and i == 0) else str(wait)
            procs.append((r, subprocess.Popen(
                [sys.executable, str(SCRIPTS / "chip_ledger.py"), "record",
                 "--origin", "proposal_tick", "--kind", "work",
                 "--chip-ref", r, "--title", "t", "--tldr", "t",
                 "--prompt", "go [chip_ref: %s]" % r],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)))
            if asymmetric and i == 0:
                import time as _t; _t.sleep(waiter_delay)   # holder head start
        results = []
        for r, p in procs:
            out, err = p.communicate(timeout=900)
            results.append((r, p.returncode, out, err))

        head = chips_of(git(repo, "show", "HEAD:TASK_CHIPS.json").stdout)
        disk = chips_of((repo / "TASK_CHIPS.json").read_text())
        org = {}
        if with_origin:
            org = chips_of(git(repo, "show", "origin/master:TASK_CHIPS.json").stdout)

        lost_head = [r for r in refs if r not in head]
        lost_disk = [r for r in refs if r not in disk]
        lost_origin = [r for r in refs if with_origin and r not in org]
        failopen = [r for r, rc, o, e in results if "PROCEEDING UNLOCKED" in e]
        nonzero = [(r, rc) for r, rc, o, e in results if rc != 0]

        # sweep detection: walk commits added by this trial
        walk_ref = "origin/master" if with_origin else "HEAD"
        log = git(repo, "log", "--format=%H", walk_ref, "--", "TASK_CHIPS.json").stdout.split()
        sweeps = []
        prev = None
        commits = list(reversed(log))
        for sha in commits:
            pp = git(repo, "rev-parse", sha + "^")
            par = pp.stdout.strip()
            if pp.returncode != 0 or not par:
                continue
            a = chips_of(git(repo, "show", par + ":TASK_CHIPS.json").stdout)
            b = chips_of(git(repo, "show", sha + ":TASK_CHIPS.json").stdout)
            changed = {k for k in b if k not in a or a[k] != b[k]} | {k for k in a if k not in b}
            msg = git(repo, "log", "-1", "--format=%B", sha).stdout
            undeclared = sorted(c for c in changed if c not in msg)
            if undeclared:
                sweeps.append((sha[:10], git(repo, "log", "-1", "--format=%s", sha).stdout.strip(), undeclared))
        return {
            "lost_head": lost_head, "lost_disk": lost_disk, "lost_origin": lost_origin,
            "failopen": failopen, "nonzero": nonzero, "sweeps": sweeps,
            "n_commits": len(commits) - 1,
            "stderr": {r: e for r, rc, o, e in results},
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=5)
    ap.add_argument("--writers", type=int, default=3)
    ap.add_argument("--wait", default="0")
    ap.add_argument("--seed-from", default=None)
    ap.add_argument("--no-origin", action="store_true")
    ap.add_argument("--wedged", action="store_true")
    ap.add_argument("--asymmetric", action="store_true")
    ap.add_argument("--waiter-delay", type=float, default=0.35)
    a = ap.parse_args()
    with_origin = not a.no_origin
    print("failopen_repro: trials=%d writers=%d lock_wait=%ss origin=%s wedged=%s asymmetric=%s seed=%s"
          % (a.trials, a.writers, a.wait, with_origin, a.wedged, a.asymmetric,
             a.seed_from or "(empty ledger)"))
    n_lost = n_sweep = n_failopen = 0
    for i in range(a.trials):
        r = trial(i, a.writers, a.seed_from, with_origin, a.wait, a.wedged, a.asymmetric, a.waiter_delay)
        lost = bool(r["lost_origin"] if with_origin else r["lost_head"])
        n_lost += lost
        n_sweep += bool(r["sweeps"])
        n_failopen += bool(r["failopen"])
        print("trial %2d: commits=%d failopen=%d/%d LOST_ON_ORIGIN=%s (disk=%s) sweeps=%d nonzero=%s"
              % (i, r["n_commits"], len(r["failopen"]), a.writers,
                 r["lost_origin"] or "-", r["lost_disk"] or "-",
                 len(r["sweeps"]), r["nonzero"] or "-"))
        for sha, subj, und in r["sweeps"]:
            print("      SWEEP %s %-50s carried undeclared: %s" % (sha, subj[:50], ", ".join(und)))
        if lost:
            for ref in (r["lost_origin"] if with_origin else r["lost_head"]):
                print("      LOST %s -- stderr tail:" % ref)
                print("        " + "\n        ".join(r["stderr"][ref].strip().splitlines()[-12:]))
    print("SUMMARY: %d/%d trials had a LOSS; %d/%d had a SWEEP; %d/%d saw a fail-open"
          % (n_lost, a.trials, n_sweep, a.trials, n_failopen, a.trials))


if __name__ == "__main__":
    main()
