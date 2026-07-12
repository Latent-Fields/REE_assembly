#!/usr/bin/env python3
"""shp2_collapse_and_verify.py -- one-plan collapse + all gates, hard-fail on any.

status_history_plane:SHP-2 (see evidence/planning/status_history_plane_separation_design.md).

The SHP-2 collapse of a closure plan is a fixed sequence -- backfill-lift, collapse,
then SIX verification gates -- that was run by hand, one command at a time, once per
plan. Running it by hand invites a skipped gate. This wrapper runs the whole sequence
for ONE plan and refuses to report success unless every gate passes (exit 1 on any
failure). It deliberately operates on a SINGLE plan (the "do not batch blindly" rule
of the design doc, sec 8): to collapse several plans, call it once per plan and read
each result -- it does not loop over plans.

The collapse step also RE-STAMPS any already-collapsed (two-plane, no-blob) node
whose stored `live:` has drifted from the projection, so a plan that is fully
collapsed but has stale heads (a new autopsy / PASS / decision landed) is refreshed
here and passes gate 4 rather than failing it. Re-stamp is a byte-identical no-op on
up-to-date nodes.

Gates (all must pass):
  1. frontmatter parses as YAML and still declares closure_plan.nodes
  2. body BELOW the frontmatter is byte-identical (collapse must touch ONLY frontmatter)
  3. zero residual `phase:`/`owner_exq:`/`awaiting:` blob lines remain in the frontmatter
  4. status-plane drift == 0 (every collapsed `live:` re-projects to its stored value)
  5. this plan has zero at-risk history refs left in the diff-vs-blob report

It shells out to the existing single-purpose tools so there is ONE implementation of
each step (no divergence): shp2_backfill_snapshot.py, shp2_collapse_plan.py,
check_closure_drift.py, project_status_head.py.

PROMOTES/DEMOTES NOTHING. Does NOT git-add or commit -- landing stays a human step so
the pathspec + post-commit dropped-file check (CLAUDE.md) are done deliberately.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/shp2_collapse_and_verify.py \
        --plan evidence/planning/goal_pipeline_plan.md \
        --by "SHP-2 <session-label>"
    # --dry-run previews backfill + collapse without writing and skips the gates.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
PY = sys.executable

_BLOB_RE = re.compile(r"^\s+(phase|owner_exq|awaiting):")


_NOISE_RE = re.compile(r"DeprecationWarning|utcnow|^\s*now_iso\b|warnings\.warn")


def _run(script, *args):
    """Run a sibling script; return (rc, combined-output-with-noise-filtered)."""
    cmd = [PY, os.path.join(HERE, script), *args]
    p = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    raw = (p.stdout or "") + (p.stderr or "")
    clean = "\n".join(l for l in raw.splitlines() if not _NOISE_RE.search(l))
    return p.returncode, clean


def _split_frontmatter(path):
    """Return (frontmatter_text, body_below_frontmatter_text). Raises if no frontmatter."""
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter (first line is not '---')")
    ends = [i for i, l in enumerate(lines) if l.strip() == "---"]
    if len(ends) < 2:
        raise ValueError("frontmatter not closed by a second '---'")
    fm_end = ends[1]
    return "".join(lines[1:fm_end]), "".join(lines[fm_end + 1:]), lines[1:fm_end]


def _body_sha(path):
    _, body, _ = _split_frontmatter(path)
    return hashlib.sha256(body.encode()).hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser(description="SHP-2 collapse + all gates for ONE plan.")
    ap.add_argument("--plan", required=True, help="repo-relative *_plan.md to collapse")
    ap.add_argument("--by", default="SHP-2 shp2_collapse_and_verify",
                    help="attribution string recorded in the snapshot log")
    ap.add_argument("--dry-run", action="store_true",
                    help="preview backfill + collapse; write nothing; skip gates")
    args = ap.parse_args()

    plan_rel = args.plan
    plan_abs = plan_rel if os.path.isabs(plan_rel) else os.path.join(REPO_ROOT, plan_rel)
    if not os.path.exists(plan_abs):
        print("FAIL: plan not found: %s" % plan_rel)
        return 1
    plan_base = os.path.basename(plan_abs)

    print("=== SHP-2 collapse+verify: %s ===" % plan_base)

    # --- backfill (append-only, idempotent) ---
    bf_args = ["--plan", plan_rel, "--by", args.by] + (["--dry-run"] if args.dry_run else [])
    rc, out = _run("shp2_backfill_snapshot.py", *bf_args)
    if rc != 0:
        print("FAIL: backfill exited %d\n%s" % (rc, out))
        return 1
    bf_line = next((l for l in out.splitlines() if "append" in l or "DRY RUN" in l), None)
    print("[backfill] %s" % (bf_line.strip() if bf_line else "ok"))

    # capture pre-body hash AFTER backfill (backfill never touches the plan file),
    # BEFORE collapse, so gate 2 compares like-for-like.
    try:
        pre_sha = _body_sha(plan_abs)
    except ValueError as e:
        print("FAIL: %s" % e)
        return 1

    # --- collapse ---
    col_args = ["--plan", plan_rel] + (["--dry-run"] if args.dry_run else [])
    rc, out = _run("shp2_collapse_plan.py", *col_args)
    if rc != 0:
        print("FAIL: collapse exited %d (REFUSE = un-lifted node)\n%s" % (rc, out))
        return 1
    for line in out.strip().splitlines():
        if (line.startswith("collapsed nodes") or line.startswith("re-stamped")
                or line.startswith("skipped")):
            print("[collapse] %s" % line)

    if args.dry_run:
        print("\n--- DRY RUN: nothing written, gates skipped ---")
        return 0

    # --- gates ---
    failures = []

    # gate 1: frontmatter parses + declares nodes
    try:
        import yaml  # noqa: E402 (only needed on the real path)
        fm_text, body_text, fm_lines = _split_frontmatter(plan_abs)
        doc = yaml.safe_load(fm_text)
        n_nodes = len(doc.get("closure_plan", {}).get("nodes", [])) if isinstance(doc, dict) else 0
        if n_nodes <= 0:
            failures.append("gate1: frontmatter parses but declares 0 closure_plan.nodes")
        print("[gate1] frontmatter parses OK, closure_plan.nodes=%d" % n_nodes)
    except Exception as e:  # noqa: BLE001
        failures.append("gate1: frontmatter parse error: %s" % e)
        body_text, fm_lines = None, []

    # gate 2: body byte-identical below frontmatter
    post_sha = _body_sha(plan_abs)
    if post_sha == pre_sha:
        print("[gate2] body byte-identical below frontmatter (sha %s)" % post_sha)
    else:
        failures.append("gate2: body CHANGED below frontmatter (pre %s -> post %s) -- "
                        "collapse must touch ONLY frontmatter" % (pre_sha, post_sha))

    # gate 3: zero residual blob lines
    resid = sum(1 for l in fm_lines if _BLOB_RE.match(l))
    if resid == 0:
        print("[gate3] 0 residual phase/owner_exq/awaiting blob lines")
    else:
        failures.append("gate3: %d residual blob line(s) remain in frontmatter" % resid)

    # gate 4: status-plane drift == 0 (re-projects every collapsed live:)
    rc, out = _run("check_closure_drift.py")
    m = re.search(r"status_plane_drift=(\d+)/(\d+)", out)
    if rc != 0:
        failures.append("gate4: check_closure_drift.py exited %d" % rc)
    elif not m:
        failures.append("gate4: could not find status_plane_drift in drift report")
    elif int(m.group(1)) != 0:
        failures.append("gate4: status-plane drift %s (a collapsed live: != its re-projection)"
                        % m.group(0).split("=")[1])
    else:
        print("[gate4] status-plane drift 0/%s" % m.group(2))

    # gate 5: this plan has zero at-risk history refs left
    rc, out = _run("project_status_head.py")
    if rc != 0:
        failures.append("gate5: project_status_head.py exited %d" % rc)
    else:
        report = os.path.join(REPO_ROOT, "scratch", "status_history_shadow", "diff_vs_blob.md")
        plan_at_risk = None
        if os.path.exists(report):
            in_section = False
            plan_at_risk = 0
            for l in open(report, encoding="utf-8"):
                if l.startswith("## "):
                    in_section = ("(`" in l and plan_base in l)
                elif in_section:
                    for mm in re.finditer(r"at_risk=(\d+)", l):
                        plan_at_risk += int(mm.group(1))
        if plan_at_risk is None:
            failures.append("gate5: diff-vs-blob report not found after re-projection")
        elif plan_at_risk != 0:
            failures.append("gate5: %d at-risk history ref(s) still on this plan" % plan_at_risk)
        else:
            print("[gate5] 0 at-risk history refs remain on %s" % plan_base)

    print("")
    if failures:
        print("*** RESULT: FAIL (%d gate failure(s)) ***" % len(failures))
        for f in failures:
            print("  - %s" % f)
        print("\nThe plan file + snapshot log are now modified on disk. Review, fix the "
              "cause, and re-run; do NOT commit a plan that fails a gate.")
        return 1

    print("*** RESULT: PASS -- all 5 gates green ***")
    print("Next (human step): land pathspec-limited --")
    print("  git commit -m \"...\" -- %s \\" % plan_rel)
    print("      evidence/planning/status_history/status_snapshot.v1.jsonl")
    print("  then: git show --stat HEAD  (verify exactly the files you intended)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
