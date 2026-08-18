#!/usr/bin/env python3
"""Steward daily T0 auto-fix sweep -- the deliberate session that runs `--fix`.

WHY THIS IS A SEPARATE SCHEDULED JOB AND NOT PART OF governance.sh
=====================================================================
USER DECISION 2026-08-17: option (ii), a separate scheduled sweep, DAILY. The
rationale is recorded here rather than only in a chip so it survives, because
the obvious "simplification" is to add `--fix` to governance.sh Step 3m and that
is the option that was rejected:

  * It keeps governance READ-ONLY, which is what README.md "Wiring" already
    requires verbatim: "No --fix ... applying them changes what the morning
    digest reports. That is a governance-visible action for a session running
    --fix on purpose." A purpose-built daily job IS that session. A side-effect
    of a regen is not, and calling it one would make the sentence false rather
    than satisfied.
  * There is also an ORDERING CONFLICT that makes (i) not merely impure but
    broken. Steward sits at Step 3m precisely because D-010 must audit
    closure_status.md AFTER Step 3c-bis regenerates it. A `--fix` at 3m mutates
    plan frontmatter that 3c-bis has already read, so the snapshot 3c-bis just
    wrote is stale the moment the fix lands -- needing either a second regen or
    a re-order that breaks D-010's placement constraint.
  * "Run it by hand when the digest complains" was rejected because it relies on
    someone remembering, and the morning digest currently fires ~9 times in 39
    weekdays, so the noticing mechanism is itself unreliable.

WHY DAILY AND NOT HOURLY. D-008 accrues ~1-3 findings/week (the 20 fixed on
2026-08-16 had accumulated over roughly a quarter; drift gaps 1-52 days, median
~5). Daily keeps drift under 24h. Hourly would be 24x the commits for no
additional freshness at that arrival rate.

WHAT IT DOES, AND THE FOUR GATES IT PASSES THROUGH
=====================================================================
  1. PIN. Capture the local branch and its upstream (D-102's RefPin) BEFORE
     anything is read, so "has the tree shifted under us" is answerable.
  2. PREVIEW, then GUARD, then APPLY -- in that order, deliberately. The preview
     is a full `--fix --dry-run` run that writes NOTHING, and the ref guard fires
     between it and the applying run. So a moving ref aborts BEFORE a single
     byte is written, and the sweep can never leave half-applied edits dirtying
     a shared checkout for the next run's `_dirty_paths` guard to stall on. The
     cost is running the detectors twice (~17s/day). That is the right trade: the
     alternative orderings all end with "and then revert someone's file", which
     is the operation this repo spends most of its concurrency rules avoiding.
  3. VALIDATE. `check_plan_frontmatter.py --strict` must pass before anything is
     committed. This is the strict `yaml.safe_load` the live explorer uses; a
     plan that fails it renders as an empty "frontmatter pending" card.
  4. COMMIT via scripts/ree_commit.py, NEVER plain git. The 2026-08-16 D-008
     fix committed with plain git and drew the pre-push warning "touches managed
     path(s) ... but was not built by ree_commit.py (race-prone idiom)".
     evidence/planning/ is a multi-writer tree; `git commit -- <pathspec>`
     commits the WORKING-TREE content at commit time and ignores the index, so
     any concurrent writer landing in that gap silently wins. ree_commit reads
     each path once, builds a private index, and compare-and-swaps the ref.

AUTHORED AS THE BOT IDENTITY, ALWAYS. Not a convenience: `clinical_hours_guard`
blocks personal-identity commits during HSE clinical hours because REE is
developed outside that employment, and an unattended job asserting an off-duty
attestation on the operator's behalf is exactly the provenance claim the guard
exists to prevent. `--bot` is passed unconditionally and there is no flag to
turn it off.

SCOPE. T0 only, and only what run_detectors.py's own FIXABLE lane offers --
D-006 (duplicate governance flag, annotate) and D-008 (plan frontmatter
last_updated, forward-only line edit). It commits exactly the paths those
fixers report having written, plus the steward ledger. It does NOT regenerate
the closure snapshot, touch claims.yaml, change a node status, or queue
anything: those are governance's and a scheduled writer must not acquire them
by being convenient.

EXIT CODES (a launchd log is read by grep, so they are distinguishable):
    0  clean -- fixes applied and committed, or nothing to fix
    1  error -- something failed that needs a human
    3  aborted by a gate -- ref moved, frontmatter invalid, no branch to pin

Usage:
    /opt/local/bin/python3 scripts/steward/steward_sweep.py
    /opt/local/bin/python3 scripts/steward/steward_sweep.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from detectors import _gitlane as G  # noqa: E402
from detectors._common import repo_root_from_here  # noqa: E402
from detectors.d102_moving_ref_guard import _pin_refs_for, guard  # noqa: E402

LEDGER_REL = "scripts/steward/state/steward_ledger.jsonl"
COMMIT_PREFIX = "steward-sweep:"

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_ABORTED = 3


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _log(msg: str) -> None:
    """ASCII-only, timestamped, unbuffered -- this is read out of a launchd log."""
    print("[%s] steward-sweep: %s" % (_utc_now(), msg), flush=True)


def ree_commit_path(repo_root: Path) -> Path:
    """scripts/ree_commit.py in the umbrella checkout that holds REE_assembly.

    Derived from repo_root rather than hardcoded so this works from a test
    fixture and from either machine layout. REE_COMMIT overrides it.
    """
    env = os.environ.get("REE_COMMIT")
    if env:
        return Path(env).resolve()
    return (repo_root.parent / "scripts" / "ree_commit.py").resolve()


def run_detectors(repo_root: Path, apply: bool) -> dict:
    """One run_detectors.py invocation -> its report dict.

    `apply=False` passes --dry-run, which implies --no-write: the preview pass
    must not touch state, the ledger, or the report, or an aborted sweep would
    still have moved the escalation ratchet.
    """
    # --repo-root / --state-dir / --report are all passed EXPLICITLY. Without
    # them run_detectors.py infers each from its OWN location, which is only the
    # same tree by coincidence -- and the coincidence breaks in exactly the two
    # cases that matter: a test fixture, and a checkout swept from elsewhere.
    # The ledger is the sharp edge: append_ledger() writes to
    # repo_root/LEDGER_REL, so a detector run writing its `run` line to a
    # different state dir would split one sweep's audit trail across two files.
    steward_dir = repo_root / "scripts" / "steward"
    cmd = [sys.executable, str(_HERE / "run_detectors.py"),
           "--repo-root", str(repo_root),
           "--state-dir", str(steward_dir / "state"),
           "--report", str(steward_dir / "reports" / "steward_report.json"),
           "--fix", "--json"]
    if not apply:
        cmd.append("--dry-run")
    proc = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("run_detectors.py exited %d: %s"
                           % (proc.returncode, proc.stderr.strip()[-2000:]))
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("run_detectors.py --json did not produce JSON: %s" % exc)


def planned_fixes(report: dict) -> list[dict]:
    """Fix records that would actually be written.

    A record carrying `skipped` was refused by apply_fixes' own dirty-path guard
    (another session has that file open); one carrying `error` failed. Neither
    is a fix, and counting either would make the sweep commit paths nothing
    wrote to.
    """
    return [r for r in (report.get("autofixes") or [])
            if not r.get("skipped") and not r.get("error")]


def applied_fixes(report: dict) -> list[dict]:
    return [r for r in (report.get("autofixes") or []) if r.get("applied")]


def fix_paths(records: list[dict]) -> list[str]:
    return sorted({r["path"] for r in records if r.get("path")})


def validate_frontmatter(repo_root: Path) -> tuple[bool, str]:
    """The strict parse the live explorer uses. --strict exits 1 on any failure."""
    checker = repo_root / "scripts" / "check_plan_frontmatter.py"
    if not checker.exists():
        # Unknown is not the same as invalid, and a fixture without the checker
        # must still be sweepable. Say so rather than silently passing.
        return True, "checker absent at %s -- validation skipped" % checker
    proc = subprocess.run([sys.executable, str(checker), "--strict"],
                          cwd=str(repo_root), capture_output=True, text=True)
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()[-4000:]


def revert(repo_root: Path, paths: list[str]) -> None:
    """Restore exactly `paths` from HEAD, and nothing else.

    Safe here for one specific reason and only that reason: apply_fixes REFUSES
    to write a path that had uncommitted changes, so every path it reports as
    applied was clean before the sweep touched it and therefore has no local
    version to lose. This is the same narrow-restore reasoning CLAUDE.md gives
    for the `D `/` D` skew repair -- and, exactly as there, a broad
    `git checkout -- .` would destroy other sessions' in-flight work and must
    never be substituted for it.
    """
    if not paths:
        return
    subprocess.run(["git", "-C", str(repo_root), "checkout", "HEAD", "--", *paths],
                   capture_output=True, text=True)


def append_ledger(repo_root: Path, record: dict) -> None:
    path = repo_root / LEDGER_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")


def commit(repo_root: Path, paths: list[str], message: str,
           push: bool) -> tuple[bool, str]:
    """Commit `paths` through ree_commit.py. Never plain git -- see the header."""
    script = ree_commit_path(repo_root)
    if not script.exists():
        return False, "ree_commit.py not found at %s" % script
    cmd = [sys.executable, str(script), "--repo", str(repo_root),
           "--bot", "-m", message]
    if push:
        cmd += ["--push", "--retry-push-on-reject"]
    cmd += ["--"] + paths
    proc = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True)
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()[-4000:]


def sweep(repo_root: Path, push: bool = True, dry_run: bool = False) -> int:
    t0 = time.time()
    now = _utc_now()
    base = {"action": "autofix", "source": "steward_sweep", "ts": now,
            "repo": str(repo_root), "dry_run": bool(dry_run)}

    def finish(rc: int, **kw) -> int:
        rec = dict(base)
        rec.update(kw)
        rec["duration_s"] = round(time.time() - t0, 3)
        rec["exit_code"] = rc
        if not dry_run:
            append_ledger(repo_root, rec)
        _log(json.dumps({k: v for k, v in rec.items()
                         if k not in ("repo",)}, sort_keys=True))
        return rc

    # --- gate 1: pin ------------------------------------------------------
    if not G.is_git_repo(repo_root):
        _log("ABORT: %s is not a git repository" % repo_root)
        return finish(EXIT_ABORTED, aborted="not_a_git_repo", applied=0)
    refs = _pin_refs_for(repo_root)
    if not refs:
        # Detached HEAD, or a branch with no resolvable name. The D-102 gate is
        # mandatory for a WRITER, so an unpinnable checkout is a refusal rather
        # than an ungated write.
        _log("ABORT: no branch ref to pin (detached HEAD?) -- the D-102 gate is "
             "mandatory for a writing job, so this is a refusal, not a warning")
        return finish(EXIT_ABORTED, aborted="no_ref_to_pin", applied=0)
    pin = G.RefPin.capture(repo_root, refs)
    base["pinned"] = dict(pin.shas)
    base["base"] = pin.shas.get(refs[0], "")
    _log("pinned %s" % ", ".join("%s=%s" % (r, s[:12])
                                 for r, s in sorted(pin.shas.items())))

    # --- gate 2: preview (writes nothing), then re-guard, then apply ------
    try:
        preview = run_detectors(repo_root, apply=False)
    except RuntimeError as exc:
        _log("ERROR: %s" % exc)
        return finish(EXIT_ERROR, error=str(exc), applied=0)

    planned = planned_fixes(preview)
    skipped = [r for r in (preview.get("autofixes") or []) if r.get("skipped")]
    _log("preview: %d fix(es) available, %d skipped (target dirty)"
         % (len(planned), len(skipped)))
    if not planned:
        return finish(EXIT_OK, applied=0, skipped=len(skipped),
                      committed=False, note="nothing to fix")

    try:
        guard(repo_root, pin.shas)
    except G.RefMoved as exc:
        # Nothing has been written yet -- this is the whole point of previewing
        # first. Next run re-derives against the new tree.
        _log("ABORT: %s -- nothing was written; next run re-derives" % exc)
        return finish(EXIT_ABORTED, aborted="ref_moved", applied=0,
                      moves=exc.moves)

    if dry_run:
        _log("dry-run: would fix %s" % ", ".join(fix_paths(planned)))
        return finish(EXIT_OK, applied=0, would_fix=fix_paths(planned),
                      committed=False, note="dry run")

    try:
        report = run_detectors(repo_root, apply=True)
    except RuntimeError as exc:
        _log("ERROR: %s" % exc)
        return finish(EXIT_ERROR, error=str(exc), applied=0)

    applied = applied_fixes(report)
    paths = fix_paths(applied)
    if not paths:
        _log("nothing applied on the second pass (tree changed between passes)")
        return finish(EXIT_OK, applied=0, committed=False,
                      note="nothing applied on the applying pass")
    _log("applied %d fix(es): %s" % (len(applied), ", ".join(paths)))

    # --- gate 3: validate before committing -------------------------------
    ok, detail = validate_frontmatter(repo_root)
    if not ok:
        revert(repo_root, paths)
        _log("ABORT: check_plan_frontmatter.py --strict FAILED; the %d applied "
             "edit(s) were reverted (each was provably clean before the sweep "
             "wrote it). %s" % (len(paths), detail))
        return finish(EXIT_ABORTED, aborted="frontmatter_invalid", applied=0,
                      reverted=paths, detail=detail)

    # --- gate 4: commit via ree_commit.py ---------------------------------
    changes = "; ".join(r.get("change", "") for r in applied)[:600]
    message = (
        "%s %d T0 repair(s) applied by the daily sweep\n\n"
        "%s\n\n"
        "Applied by scripts/steward/steward_sweep.py (launchd com.ree.steward,\n"
        "StartInterval 86400). T0 only -- run_detectors.py's FIXABLE lane\n"
        "(D-006 annotate, D-008 forward-only last_updated bump). Gated on the\n"
        "D-102 moving-ref guard and on check_plan_frontmatter.py --strict.\n"
        "No claims.yaml, no node status, no closure snapshot regen.\n"
        "Audit record: %s" % (COMMIT_PREFIX, len(applied), changes, LEDGER_REL))

    # The ledger record goes in BEFORE the commit so the sweep's own audit trail
    # lands in the same commit as the edits it describes. It therefore cannot
    # carry the resulting sha; it carries `base` instead, and the commit is the
    # child of that base -- `git log <base>..` finds it deterministically.
    rec = dict(base)
    rec.update({"applied": len(applied), "skipped": len(skipped),
                "paths": paths,
                "changes": [r.get("change") for r in applied],
                "committed": True, "pushed": bool(push),
                "commit_prefix": COMMIT_PREFIX,
                "duration_s": round(time.time() - t0, 3),
                "exit_code": EXIT_OK})
    append_ledger(repo_root, rec)

    ok, detail = commit(repo_root, paths + [LEDGER_REL], message, push)
    if not ok:
        # Deliberately NOT reverted. A commit failure means CAS lost or the push
        # was rejected in a way ree_commit could not resolve; the edits are
        # correct and a human should land them, not have them silently undone.
        _log("ERROR: commit failed, edits LEFT IN PLACE for a human. %s" % detail)
        return finish(EXIT_ERROR, applied=len(applied), paths=paths,
                      committed=False, error=detail[-1500:])

    _log("committed%s: %s" % (" and pushed" if push else "", ", ".join(paths)))
    for line in detail.splitlines():
        _log("  %s" % line)
    return EXIT_OK


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Steward daily T0 auto-fix sweep.")
    ap.add_argument("--repo-root", default=None,
                    help="REE_assembly root (default: inferred from this file)")
    ap.add_argument("--no-push", action="store_true",
                    help="commit locally without pushing")
    ap.add_argument("--dry-run", action="store_true",
                    help="run the gates and report what would be fixed; "
                         "writes nothing and commits nothing")
    args = ap.parse_args(argv)
    repo_root = Path(args.repo_root).resolve() if args.repo_root \
        else repo_root_from_here()
    return sweep(repo_root, push=not args.no_push, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
