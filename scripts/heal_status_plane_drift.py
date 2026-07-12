#!/usr/bin/env python3
"""heal_status_plane_drift.py -- SHP-3 governance self-heal for status-plane drift.

status_history_plane:SHP-3 (see evidence/planning/status_history_plane_separation_design.md).

check_closure_drift.py's status-plane section DETECTS drift -- a collapsed
closure-plan node whose stored two-plane `live:` head no longer matches the
re-projection from the append-only event log (a new autopsy / PASS manifest /
decision landed, or the reconcile / brake state moved). It is warn-only: it never
re-stamps. That left an automation gap -- every governance cycle re-reported the
same drift until a human ran the re-stamp by hand.

This script CLOSES that gap. It re-detects status-plane drift via the ONE
projection path (calling check_closure_drift.status_plane_drift), groups the
drifted nodes by plan, and for each fully-collapsed drifted plan runs
shp2_collapse_plan.py to re-stamp the drifted `live:` heads IN PLACE. The
re-stamp regenerates `live:`+`join:` via the projector and replaces a node's
block only when it differs, so an up-to-date node is a byte-identical no-op.

Deliberate boundaries (matching governance.sh's derive-only + human-landing posture):

  * NO git add / commit. The re-stamp edits the plan .md file(s) in the working
    tree and leaves them there for a human to review + commit under a pathspec
    (the coordination-data-plane trunk-writer safety + the CLAUDE.md post-commit
    dropped-file discipline). governance.sh must never auto-commit a *_plan.md.

  * PROMOTES / DEMOTES NOTHING. It is a pure status-plane refresh: it rewrites
    only the derived `live:`+`join:` block, never `status:` / `severity:` / any
    hand-maintained field, and never claims.yaml.

  * Collapse-migration stays a HUMAN step. A drifted plan that ALSO still carries
    un-collapsed `phase:`/`owner_exq:`/`awaiting:` blob nodes is SKIPPED (never
    auto-collapsed) -- running the collapse tool on it could collapse a blob node
    (a migration, not a status refresh) or REFUSE on an un-lifted blob. Such
    plans are surfaced with the exact manual command instead (option-b fallback
    for that one plan). Today every collapsed plan is fully collapsed, so this
    guard is defensive; it protects the boundary if a future plan goes mixed.

It shells out to shp2_collapse_plan.py so there is ONE implementation of the
re-stamp (no divergence), mirroring shp2_collapse_and_verify.py.

Exit code is ALWAYS 0 (a governance hint, like check_closure_drift.py): a
re-stamp failure or a skipped mixed plan is surfaced but never aborts the
pipeline (governance.sh runs under `set -e`).

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/heal_status_plane_drift.py
    /opt/local/bin/python3 scripts/heal_status_plane_drift.py --dry-run
"""

import argparse
import os
import re
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

REPO_ROOT = os.path.dirname(_HERE)
PLANNING_DIR = os.path.join(REPO_ROOT, "evidence", "planning")
PY = sys.executable

import check_closure_drift as ccd  # noqa: E402  (shares the ONE projection path)

# node-indent blob line, same shape shp2_collapse_plan.py / _and_verify.py match.
_BLOB_RE = re.compile(r"^      (phase|owner_exq|awaiting):")
# "re-stamped collapsed nodes (N): a, b, c" line emitted by shp2_collapse_plan.py.
_RESTAMP_RE = re.compile(r"^re-stamped collapsed nodes \((\d+)\):\s*(.*)$")


def _plan_has_residual_blob(plan_basename):
    """True if the plan file still carries any un-collapsed
    phase:/owner_exq:/awaiting: node blob (i.e. it is not fully collapsed)."""
    path = os.path.join(PLANNING_DIR, plan_basename)
    try:
        with open(path, encoding="utf-8") as f:
            return any(_BLOB_RE.match(line.rstrip("\n")) for line in f)
    except OSError:
        return False


def _restamp_plan(plan_basename, dry_run):
    """Shell out to shp2_collapse_plan.py for one plan. Returns
    (rc, restamped_nodes:list[str], output:str)."""
    plan_rel = os.path.join("evidence", "planning", plan_basename)
    cmd = [PY, os.path.join(_HERE, "shp2_collapse_plan.py"), "--plan", plan_rel]
    if dry_run:
        cmd.append("--dry-run")
    p = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    restamped = []
    for line in out.splitlines():
        m = _RESTAMP_RE.match(line.strip())
        if m:
            names = m.group(2).strip()
            restamped = [n.strip() for n in names.split(",") if n.strip()]
            break
    return p.returncode, restamped, out


def main():
    ap = argparse.ArgumentParser(
        description="SHP-3 governance self-heal: re-stamp status-plane-drifted "
                    "collapsed closure-plan nodes in place (no commit).")
    ap.add_argument("--dry-run", action="store_true",
                    help="detect + report what WOULD be re-stamped; write nothing.")
    args = ap.parse_args()

    drifted, n_checked, note = ccd.status_plane_drift()

    print("heal_status_plane_drift.py (SHP-3) -- status-plane self-heal")
    if note:
        print("  SKIP: %s" % note)
        return 0
    if not drifted:
        print("  status-plane drift 0/%d -- nothing to heal." % n_checked)
        return 0

    # group drifted nodes by plan (basename)
    by_plan = {}
    for d in drifted:
        by_plan.setdefault(d["plan"], []).append(d.get("node_id") or "?")
    print("  status-plane drift: %d node(s) across %d plan(s) (of %d collapsed)."
          % (len(drifted), len(by_plan), n_checked))

    restamped_plans = []   # (plan, [nodes])
    skipped_mixed = []     # plan basenames with residual blobs
    failed = []            # (plan, rc, first_error_line)

    for plan in sorted(by_plan):
        drift_nodes = sorted(set(by_plan[plan]))
        if _plan_has_residual_blob(plan):
            # Mixed plan: collapse-migration is a human step -- do NOT auto-touch.
            skipped_mixed.append(plan)
            print("  [skip] %s -- has un-collapsed blob node(s); re-stamp deferred "
                  "to a human (see manual command below). drifted: %s"
                  % (plan, ", ".join(drift_nodes)))
            continue
        rc, restamped, out = _restamp_plan(plan, args.dry_run)
        if rc != 0:
            first_err = next((l for l in out.splitlines() if l.strip()), "")
            failed.append((plan, rc, first_err))
            print("  [FAIL] %s -- shp2_collapse_plan.py exited %d: %s"
                  % (plan, rc, first_err))
            continue
        verb = "would re-stamp" if args.dry_run else "re-stamped"
        print("  [%s] %s -- %s %d node(s): %s"
              % ("dry-run" if args.dry_run else "heal", plan, verb,
                 len(restamped), ", ".join(restamped) or "(none -- already current)"))
        if restamped:
            restamped_plans.append((plan, restamped))

    # --- verification: re-detect drift on the healed plans -------------------
    if not args.dry_run and restamped_plans:
        post_drifted, post_checked, post_note = ccd.status_plane_drift()
        healed = {p for p, _ in restamped_plans}
        residual_on_healed = sorted(
            {d["plan"] for d in post_drifted if d["plan"] in healed})
        if post_note:
            print("  [verify] SKIP re-check: %s" % post_note)
        elif residual_on_healed:
            print("  [verify] WARNING: residual drift remains on re-stamped plan(s): %s"
                  % ", ".join(residual_on_healed))
        else:
            print("  [verify] OK: 0 residual status-plane drift on re-stamped plan(s) "
                  "(post-heal drift %d/%d overall)."
                  % (len(post_drifted), post_checked))

    # --- summary -------------------------------------------------------------
    print("")
    if args.dry_run:
        print("  DRY-RUN: nothing written.")
    if restamped_plans and not args.dry_run:
        plan_rels = ["evidence/planning/%s" % p for p, _ in restamped_plans]
        print("  RE-STAMPED (uncommitted, in working tree -- review + commit as a "
              "human, pathspec-limited):")
        for p, nodes in restamped_plans:
            print("    - %s (%d node(s): %s)" % (p, len(nodes), ", ".join(nodes)))
        print("  Suggested pathspec commit:")
        print("    git commit -m \"SHP-3: re-stamp status-plane-drifted live: heads\" -- \\")
        print("        %s" % " \\\n        ".join(plan_rels))
        print("    then: git show --stat HEAD  (verify exactly the files you intended)")
    if skipped_mixed:
        print("  SKIPPED (mixed -- un-collapsed blobs; collapse is a human step). "
              "Re-stamp each manually once collapsed:")
        for p in skipped_mixed:
            print("    scripts/shp2_collapse_and_verify.py --plan evidence/planning/%s" % p)
    if failed:
        print("  FAILED re-stamp (surfaced, not aborted):")
        for p, rc, err in failed:
            print("    - %s (rc=%d): %s" % (p, rc, err))
    print("  PROMOTES/DEMOTES NOTHING; edits only derived live:/join: blocks; "
          "no git add/commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
