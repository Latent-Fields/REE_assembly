#!/usr/bin/env python3
"""check_authored_live_blocks.py -- catch a HAND-WRITTEN derived `live:`/`join:`
block on a collapsed closure-plan node, at authoring / commit time.

WHY THIS EXISTS
---------------
In evidence/planning/*_plan.md, a collapsed (two-plane) closure_plan node carries
a `live:` + `join:` block that is a DERIVED PROJECTION over the append-only event
log (failure_autopsy_*.json + PASS manifests + evidence/decisions/decision_log.v1.jsonl),
produced by the ONE projection path in scripts/project_status_head.py
(see STORED_LIVE_FIELDS) and re-stamped by scripts/heal_status_plane_drift.py
during governance.sh Step 3c-pre-heal.

It is NOT hand-authorable. On 2026-07-17 a session hand-wrote that block on
conversion_ceiling_campaign:GENERATION, setting `from:` to a planning .md doc
(which matches ZERO events, so no scope choice could ever project it), plus
`brake: not_fired` and `needs_review: false` -- both unreachable, since `brake`
is a derived count of substrate_ceiling events against a threshold and counts 42
under that node's scope. The healer correctly re-projected over all of it.
NOTHING WARNED ANYONE: not at authoring time, not at commit time, not in the
governance run. The cost was a silently-doomed edit plus a full investigation
session to adjudicate the contradiction (REE_assembly 417993abd0).

THE CHECKS (cheapest first)
---------------------------
  1. unprojectable_from  -- `live.from` names no event that exists in the log.
     This is the SHARP one: a `from` that matches no event id is never legitimate
     under any scope, so it is always an authoring error, never mere staleness.
     (This check alone would have caught the incident.)

  2. stored_live_drift   -- stored `live:` != stored_live_view(project_live(...)).
     Same computation check_closure_drift.status_plane_drift() already does; it is
     surfaced here so it reaches the author at COMMIT time rather than only inside
     a governance run. NOTE this one also fires on legitimate staleness (a new
     autopsy / PASS manifest landed since the last re-stamp), so it is reported
     separately and more softly than (1).

  3. join_scope_mismatch -- `join.scope_claims` differs from the node's effective
     INPUT scope (node-level `scope_claims:` if present, else the plan-level list).
     This was the second half of the same incident: the scope narrowing was written
     into the derived `join.scope_claims` instead of a node-level `scope_claims:`
     input field.

DESIGN CONSTRAINTS
------------------
  * WARN-ONLY by default. Exits 0 on findings, and exits 0 on ANYTHING ambiguous
    (no PyYAML, projector unavailable, unparseable frontmatter, missing file).
    These plan files are edited by many parallel sessions; this must not become a
    commit-blocking flake. `--strict` opts into exit 1 for a future gate.
  * Does NOT duplicate the projection logic -- it imports project_status_head and
    calls the same load_events / build_projections / stored_live_view entry points
    the collapse tool and the drift check use.
  * ASCII-only output (Windows cp1252 terminals).

USAGE
-----
    # all plans (default: this repo's evidence/planning)
    /opt/local/bin/python3 scripts/check_authored_live_blocks.py

    # only the plans touched by a commit
    /opt/local/bin/python3 scripts/check_authored_live_blocks.py \
        --only conversion_ceiling_campaign_plan.md

    # regression fixtures
    /opt/local/bin/python3 scripts/check_authored_live_blocks.py --self-test
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = Path(__file__).resolve().parent

# Import the ONE projection path. Everything below is a consumer of it.
sys.path.insert(0, str(SCRIPTS_DIR))
try:
    import yaml
except Exception:  # pragma: no cover - ambiguous -> stay silent
    yaml = None
try:
    import project_status_head as psh
except Exception:  # pragma: no cover - ambiguous -> stay silent
    psh = None


SKIP_EXIT = 0  # ambiguity is never a finding


# ---------------------------------------------------------------------------
# Frontmatter (stored blocks live in the raw YAML; psh.load_plans drops them)
# ---------------------------------------------------------------------------


def parse_plan_frontmatter(path: Path):
    """Return the parsed frontmatter dict, or None when unreadable / not a plan."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def effective_scope_claims(plan: dict, node: dict):
    """The node's INPUT scope, exactly as psh.load_plans resolves it: the
    node-level `scope_claims:` when present, else the plan-level list."""
    node_scope = node.get("scope_claims")
    if isinstance(node_scope, list) and node_scope:
        return [str(c) for c in node_scope]
    plan_scope = plan.get("scope_claims") or []
    return [str(c) for c in plan_scope] if isinstance(plan_scope, list) else []


# ---------------------------------------------------------------------------
# The checks
# ---------------------------------------------------------------------------


def check_plans(repo_root: Path, planning_dir: Path, only: list[str] | None):
    """Run all three checks. Returns (findings, n_checked, skip_note)."""
    if yaml is None:
        return [], 0, "PyYAML unavailable"
    if psh is None:
        return [], 0, "project_status_head unavailable"
    if not planning_dir.is_dir():
        return [], 0, "planning dir not found: %s" % planning_dir

    try:
        plans, _skipped = psh.load_plans(str(planning_dir))
        events, _counts = psh.load_events(str(repo_root))
        projections = psh.build_projections(plans, events, psh.DEFAULT_BRAKE_THRESHOLD)
    except Exception as e:  # pragma: no cover - defensive, ambiguity -> silent
        return [], 0, "projection failed: %s" % e

    known_eids = {ev.eid for ev in events if ev.eid}
    if not known_eids:
        # An empty event log means the log did not load (wrong repo root, checkout
        # skew, permissions) -- NOT that every stored head is unprojectable. Firing
        # here would flag every collapsed node at once. Ambiguity -> stay silent.
        return [], 0, "event log loaded 0 events (wrong --repo-root?)"

    findings = []
    n_checked = 0
    for path in sorted(planning_dir.glob("*_plan.md")):
        if only and path.name not in only:
            continue
        fm = parse_plan_frontmatter(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            continue
        for node in plan.get("nodes", []) or []:
            if not isinstance(node, dict):
                continue
            live_block = node.get("live")
            if not isinstance(live_block, dict):
                continue  # not collapsed -- nothing derived to check
            nid = node.get("id")
            pr = projections.get(nid)
            if pr is None:
                continue  # node not in the projection (ambiguous) -- skip
            n_checked += 1

            # --- 1. unprojectable `from` ---------------------------------
            stored_from = live_block.get("from")
            if isinstance(stored_from, str) and stored_from.strip() \
                    and stored_from not in known_eids:
                findings.append({
                    "kind": "unprojectable_from",
                    "plan": path.name,
                    "node_id": nid,
                    "detail": (
                        "live.from = %r matches NO event in the append-only log "
                        "(%d events). A derived head can only ever name an event id; "
                        "this block was hand-written and WILL be re-projected over by "
                        "the next governance run." % (stored_from, len(known_eids))
                    ),
                    "projected_from": psh.stored_live_view(pr["live"]).get("from"),
                })

            # --- 2. stored != projected ----------------------------------
            stored = {k: live_block.get(k) for k in psh.STORED_LIVE_FIELDS}
            if live_block.get("needs_review") and live_block.get("needs_review_reasons"):
                stored["needs_review_reasons"] = list(live_block["needs_review_reasons"])
            projected = psh.stored_live_view(pr["live"])
            diffs = _live_diff(stored, projected)
            if diffs:
                findings.append({
                    "kind": "stored_live_drift",
                    "plan": path.name,
                    "node_id": nid,
                    "detail": "; ".join(diffs),
                    "projected_from": projected.get("from"),
                })

            # --- 3. join.scope_claims vs the effective INPUT scope --------
            join_block = node.get("join")
            if isinstance(join_block, dict) and isinstance(
                    join_block.get("scope_claims"), list):
                stored_scope = {str(c) for c in join_block["scope_claims"]}
                eff_scope = set(effective_scope_claims(plan, node))
                if stored_scope != eff_scope:
                    missing = sorted(eff_scope - stored_scope)
                    extra = sorted(stored_scope - eff_scope)
                    findings.append({
                        "kind": "join_scope_mismatch",
                        "plan": path.name,
                        "node_id": nid,
                        "detail": (
                            "join.scope_claims differs from the node's effective input "
                            "scope (node-level scope_claims: if set, else plan-level). "
                            "dropped=%s added=%s. join.scope_claims is DERIVED -- a real "
                            "scope narrowing belongs in a node-level `scope_claims:` "
                            "input field." % (missing or "[]", extra or "[]")
                        ),
                        "projected_from": None,
                    })

    return findings, n_checked, None


def _live_diff(stored: dict, projected: dict) -> list[str]:
    """Field-level mismatches, same comparison semantics as
    check_closure_drift._live_diff (scalars as strings, needs_review as bool)."""
    fields = list(psh.STORED_LIVE_FIELDS) + ["needs_review_reasons"]
    diffs = []
    for f in fields:
        sv, pv = stored.get(f), projected.get(f)
        if f == "needs_review":
            if bool(sv) != bool(pv):
                diffs.append("%s: stored=%s projected=%s" % (f, bool(sv), bool(pv)))
        elif f == "needs_review_reasons":
            if list(sv or []) != list(pv or []):
                diffs.append("%s: stored=%s projected=%s" % (f, sv or [], pv or []))
        else:
            s = None if sv is None else str(sv)
            p = None if pv is None else str(pv)
            if s != p:
                diffs.append("%s: stored=%r projected=%r" % (f, sv, pv))
    return diffs


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"unprojectable_from": 0, "join_scope_mismatch": 1, "stored_live_drift": 2}

HEADLINE = {
    "unprojectable_from":
        "HAND-WRITTEN derived block (live.from names no event) -- ALWAYS an error",
    "join_scope_mismatch":
        "join.scope_claims hand-narrowed (derived field used as an input)",
    "stored_live_drift":
        "stored live: != projection (hand-written OR simply stale vs new events)",
}


def report(findings, n_checked, skip_note, stream=sys.stderr) -> None:
    if skip_note:
        stream.write("check_authored_live_blocks: skipped (%s)\n" % skip_note)
        return
    if not findings:
        stream.write(
            "check_authored_live_blocks: OK -- %d collapsed node(s), no hand-authored "
            "derived blocks.\n" % n_checked)
        return
    by_kind = {}
    for f in findings:
        by_kind.setdefault(f["kind"], []).append(f)
    stream.write(
        "\ncheck_authored_live_blocks: %d finding(s) across %d collapsed node(s).\n"
        % (len(findings), n_checked))
    stream.write(
        "  `live:` and `join:` are DERIVED outputs of scripts/project_status_head.py\n"
        "  over the append-only event log. They are not hand-authorable -- governance\n"
        "  re-projects over any hand-written value. WARN-ONLY; nothing is blocked.\n\n")
    for kind in sorted(by_kind, key=lambda k: SEVERITY_ORDER.get(k, 9)):
        stream.write("  [%s] %s\n" % (kind, HEADLINE.get(kind, "")))
        for f in by_kind[kind]:
            stream.write("    - %s :: %s\n" % (f["plan"], f["node_id"]))
            stream.write("      %s\n" % f["detail"])
            if f.get("projected_from"):
                stream.write("      projected head would be: %s\n" % f["projected_from"])
        stream.write("\n")
    stream.write(
        "  Fix: do not hand-write these blocks. Re-stamp via\n"
        "  scripts/shp2_collapse_plan.py --plan <plan>  (or let governance.sh Step\n"
        "  3c-pre-heal / scripts/heal_status_plane_drift.py do it), and put any real\n"
        "  scope change in a node-level `scope_claims:` INPUT field.\n\n")


# ---------------------------------------------------------------------------
# Self-test -- regression fixtures pinned to the 2026-07-17 incident
# ---------------------------------------------------------------------------

FIXTURE_COMMIT = "03d8e2fcf9"
FIXTURE_PLAN = "conversion_ceiling_campaign_plan.md"
FIXTURE_NODE = "conversion_ceiling_campaign:GENERATION"


def _self_test() -> int:
    """Two anchors:
      * POSITIVE -- the pre-fix blob at 03d8e2fcf9 (the hand-written GENERATION
        live: block) MUST be flagged unprojectable_from.
      * NEGATIVE -- the current working-tree planning dir must NOT flag
        unprojectable_from on any node (status-plane drift was verified 0/99 on
        2026-07-18).
    Skips (exit 0, reported) if git or the fixture commit is unavailable.
    """
    failures = []

    def check(name, cond):
        if cond:
            print("  ok   %s" % name)
        else:
            failures.append(name)
            print("  FAIL %s" % name)

    # --- NEGATIVE: current tree is clean of the sharp signal -----------------
    findings, n_checked, note = check_plans(
        REPO_ROOT, REPO_ROOT / "evidence" / "planning", None)
    if note:
        print("  skip (current tree): %s" % note)
    else:
        sharp = [f for f in findings if f["kind"] == "unprojectable_from"]
        check("current tree: no unprojectable_from (%d collapsed nodes checked)"
              % n_checked, not sharp)
        if sharp:
            for f in sharp:
                print("       unexpected: %s :: %s" % (f["plan"], f["node_id"]))

    # --- POSITIVE: the pre-fix fixture fires --------------------------------
    try:
        blob = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "show",
             "%s:evidence/planning/%s" % (FIXTURE_COMMIT, FIXTURE_PLAN)],
            capture_output=True, timeout=60)
    except Exception as e:
        print("  skip (fixture): git unavailable (%s)" % e)
        blob = None
    if blob is None or blob.returncode != 0:
        if blob is not None:
            print("  skip (fixture): commit %s not available" % FIXTURE_COMMIT)
    else:
        tmp = tempfile.mkdtemp(prefix="authored_live_fixture_")
        try:
            # Copy the whole planning dir so the projection (and the umbrella pass)
            # sees the same plan set, then overwrite the one plan with the pre-fix
            # blob. repo_root stays the REAL repo so the event log is the real one.
            src = REPO_ROOT / "evidence" / "planning"
            dst = Path(tmp) / "planning"
            dst.mkdir()
            for p in src.glob("*_plan.md"):
                shutil.copy2(p, dst / p.name)
            (dst / FIXTURE_PLAN).write_bytes(blob.stdout)
            f_findings, f_checked, f_note = check_plans(REPO_ROOT, dst, [FIXTURE_PLAN])
            if f_note:
                print("  skip (fixture): %s" % f_note)
            else:
                hits = [f for f in f_findings
                        if f["kind"] == "unprojectable_from"
                        and f["node_id"] == FIXTURE_NODE]
                check("fixture %s: GENERATION flagged unprojectable_from "
                      "(%d nodes checked)" % (FIXTURE_COMMIT, f_checked), bool(hits))
                if hits:
                    print("       %s" % hits[0]["detail"])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print("SELF-TEST FAILED: %d failure(s): %s" % (len(failures), ", ".join(failures)))
        return 1
    print("SELF-TEST PASSED")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Warn-only check for hand-authored derived live:/join: blocks "
                    "on collapsed closure-plan nodes.")
    ap.add_argument("--repo-root", default=str(REPO_ROOT),
                    help="REE_assembly repo root (event log source)")
    ap.add_argument("--planning-dir", default=None,
                    help="plans dir (default: <repo-root>/evidence/planning)")
    ap.add_argument("--only", action="append", default=None, metavar="PLAN.md[,PLAN.md]",
                    help="restrict to these plan basenames. Repeatable AND accepts a "
                         "comma-separated list, so a caller can always pass a SINGLE "
                         "quoted argument -- the hook relies on this, because unquoted "
                         "word-splitting is shell-dependent (zsh does not split).")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on findings (default: warn-only, always exit 0)")
    ap.add_argument("--sharp-only", action="store_true",
                    help="report only unprojectable_from + join_scope_mismatch "
                         "(suppress stored_live_drift, which also fires on ordinary "
                         "staleness). Intended for the commit-time hook.")
    ap.add_argument("--self-test", action="store_true", help="run regression fixtures")
    args = ap.parse_args()

    if args.self_test:
        return _self_test()

    repo_root = Path(os.path.abspath(args.repo_root))
    planning_dir = Path(args.planning_dir) if args.planning_dir \
        else repo_root / "evidence" / "planning"

    only = None
    if args.only:
        only = [p.strip() for chunk in args.only for p in chunk.split(",") if p.strip()]
        only = only or None

    findings, n_checked, note = check_plans(repo_root, planning_dir, only)
    if args.sharp_only:
        findings = [f for f in findings if f["kind"] != "stored_live_drift"]
    report(findings, n_checked, note)

    if note:
        return SKIP_EXIT
    return 1 if (findings and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
