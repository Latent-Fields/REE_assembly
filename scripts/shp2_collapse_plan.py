#!/usr/bin/env python3
"""shp2_collapse_plan.py -- SHP-2 two-plane collapse (design sec 4a).

status_history_plane:SHP-2. AFTER the node blobs have been lifted append-only by
`shp2_backfill_snapshot.py` (the razor, design sec 5), this collapses each closure
-plan node's hand-written `phase:` / `owner_exq:` / `awaiting:` blobs to the
two-plane `live:` + `join:` schema. `live:` is taken verbatim from the projector
(`project_status_head.stored_live_view`) so the SHP-2 status-plane drift check
(projected `live` == stored `live`) is green immediately after collapse.

It is a purely TEXTUAL, line-based edit: every field in these nodes is a single
physical YAML line, so it removes exactly the three blob lines per node and inserts
the live/join block after `severity:` (else `status:`). It never round-trips the
YAML (which would reformat the whole hand-maintained file) and touches nothing
outside the target plan's frontmatter node lines. All other fields (title, status,
severity, assembly_status, cross_plan_link, *_note_* annotations) are preserved
byte-for-byte.

Refuses to run unless every target node is already lifted (safety: never collapse
an un-archived blob). PROMOTES/DEMOTES NOTHING.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/shp2_collapse_plan.py \
        --plan evidence/planning/conversion_ceiling_campaign_plan.md [--dry-run]
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import project_status_head as P  # noqa: E402

REPO_ROOT = os.path.dirname(HERE)
SNAPSHOT_LOG = os.path.join(REPO_ROOT, "evidence", "planning", "status_history",
                            "status_snapshot.v1.jsonl")

_NODE_ID_RE = re.compile(r'^    - id:\s*"?([^"\n]+?)"?\s*$')
_BLOB_RE = re.compile(r'^      (phase|owner_exq|awaiting):\s')
_FIELD_RE = re.compile(r'^      (\w+):')


def _lifted_node_ids():
    done = set()
    if not os.path.exists(SNAPSHOT_LOG):
        return done
    for line in open(SNAPSHOT_LOG, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if r.get("kind") == "shp2_backfill_lift" and r.get("node_id"):
            done.add(r["node_id"])
    return done


def _live_join_lines(stored_live, bears_on, scope_claims):
    lines = ["      live:"]
    for k in P.STORED_LIVE_FIELDS:
        lines.append("        %s: %s" % (k, json.dumps(stored_live.get(k))))
    if stored_live.get("needs_review_reasons"):
        lines.append("        needs_review_reasons: %s"
                     % json.dumps(stored_live["needs_review_reasons"]))
    lines.append("      join:")
    lines.append("        bears_on: %s" % json.dumps(bears_on))
    lines.append("        scope_claims: %s" % json.dumps(scope_claims))
    return lines


def main():
    ap = argparse.ArgumentParser(description="SHP-2 two-plane collapse (design sec 4a).")
    ap.add_argument("--plan", required=True, help="repo-relative *_plan.md to collapse")
    ap.add_argument("--dry-run", action="store_true", help="write nothing; report only")
    args = ap.parse_args()

    plan_file = args.plan if os.path.isabs(args.plan) else os.path.join(REPO_ROOT, args.plan)
    planning_dir = os.path.join(REPO_ROOT, "evidence", "planning")
    all_plans, _ = P.load_plans(planning_dir)
    plan_id = None
    for p in all_plans:
        if os.path.abspath(os.path.join(REPO_ROOT, p["file"])) == os.path.abspath(plan_file):
            plan_id = p["plan_id"]
            break
    if plan_id is None:
        raise SystemExit("could not resolve plan_id for %s" % plan_file)
    target_plans = [p for p in all_plans if p["plan_id"] == plan_id]
    events, _ = P.load_events(REPO_ROOT)
    projections = P.build_projections(target_plans, events, P.DEFAULT_BRAKE_THRESHOLD)
    plan_scope = target_plans[0]["scope_claims"]

    lifted = _lifted_node_ids()

    text = open(plan_file, encoding="utf-8").read()
    lines = text.splitlines()

    # frontmatter bounds
    if lines[0].strip() != "---":
        raise SystemExit("no frontmatter")
    fm_end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")

    out = []
    i = 0
    collapsed = []
    skipped = []
    while i < len(lines):
        line = lines[i]
        m = _NODE_ID_RE.match(line) if i < fm_end else None
        if not m:
            out.append(line)
            i += 1
            continue
        nid = m.group(1)
        # gather this node's lines [i, j)
        j = i + 1
        while j < fm_end and not _NODE_ID_RE.match(lines[j]):
            j += 1
        node_lines = lines[i:j]

        has_blob = any(_BLOB_RE.match(nl) for nl in node_lines)
        pr = projections.get(nid)
        if not has_blob or pr is None:
            out.extend(node_lines)
            skipped.append((nid, "no blob" if not has_blob else "no projection"))
            i = j
            continue
        if nid not in lifted:
            raise SystemExit("REFUSE: node %s not lifted to snapshot log; run "
                             "shp2_backfill_snapshot.py first (razor sec 5)." % nid)

        sl = P.stored_live_view(pr["live"])
        lj = _live_join_lines(sl, pr["join_bears_on"], plan_scope)

        # emit node with blob lines removed and live/join inserted after severity
        # (else after status, else after the last field before the blobs).
        kept = [nl for nl in node_lines if not _BLOB_RE.match(nl)]
        anchor = None
        for idx, nl in enumerate(kept):
            fm2 = _FIELD_RE.match(nl)
            if fm2 and fm2.group(1) == "severity":
                anchor = idx
        if anchor is None:
            for idx, nl in enumerate(kept):
                fm2 = _FIELD_RE.match(nl)
                if fm2 and fm2.group(1) == "status":
                    anchor = idx
        if anchor is None:
            anchor = 0  # after the id line at least
        new_node = kept[:anchor + 1] + lj + kept[anchor + 1:]
        out.extend(new_node)
        collapsed.append(nid)
        i = j

    new_text = "\n".join(out) + ("\n" if text.endswith("\n") else "")

    print("plan: %s" % plan_id)
    print("collapsed nodes (%d): %s" % (len(collapsed), ", ".join(collapsed)))
    if skipped:
        print("skipped nodes: %s" % ", ".join("%s(%s)" % s for s in skipped))
    if args.dry_run:
        print("\n--- DRY RUN: nothing written ---")
        return 0
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("wrote %s" % os.path.relpath(plan_file, REPO_ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
