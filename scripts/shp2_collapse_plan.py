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

RE-STAMP path (SHP-2 status-plane refresh): a node that is ALREADY collapsed (a
two-plane `live:` block, no `phase:`/`owner_exq:`/`awaiting:` blob) is re-projected
in place when a new event has made its stored `live:` head stale vs the projection
(the `status_plane_drift` the drift check flags). The stored `live:`+`join:` block
is regenerated via the ONE projection path and replaced only when it differs, so an
up-to-date node is a byte-identical no-op and the body below the frontmatter is
never touched (the wrapper's gate 2). This is the sanctioned re-stamp for
already-collapsed drifted nodes -- there is no blob to lift (the history was lifted
at the original collapse), so the not-lifted REFUSE does not apply to it.

Refuses to run unless every target node with a blob is already lifted (safety:
never collapse an un-archived blob). PROMOTES/DEMOTES NOTHING.

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


def _live_join_lines(stored_live, stored_join):
    """Render the two-plane block from the two STORED views. Both come from the
    ONE projection path (P.stored_live_view / P.stored_join_view), so what is
    written here is exactly what the drift check re-projects and compares."""
    lines = ["      live:"]
    for k in P.STORED_LIVE_FIELDS:
        lines.append("        %s: %s" % (k, json.dumps(stored_live.get(k))))
    if stored_live.get("needs_review_reasons"):
        lines.append("        needs_review_reasons: %s"
                     % json.dumps(stored_live["needs_review_reasons"]))
    lines.append("      join:")
    for k in P.STORED_JOIN_FIELDS:
        lines.append("        %s: %s" % (k, json.dumps(stored_join.get(k))))
    return lines


def _live_join_span(node_lines):
    """Locate the existing machine-written `live:`+`join:` block within an
    already-collapsed node's lines. Returns (start, end) indices (end exclusive)
    or None if the node carries no `live:` block.

    The block is written by `_live_join_lines` with `live:`/`join:` keys at 6-space
    indent and their children at 8-space indent, so the span is: the `      live:`
    line, its 8-space children, then (optionally) the `      join:` line and its
    8-space children. A shallower / differently-indented line ends the block, so a
    hand-edited or absent block leaves the span unmatched (safe: no re-stamp)."""
    ls = None
    for idx, nl in enumerate(node_lines):
        if nl == "      live:":
            ls = idx
            break
    if ls is None:
        return None
    n = len(node_lines)
    idx = ls + 1
    while idx < n and node_lines[idx].startswith("        "):  # live: children
        idx += 1
    if idx < n and node_lines[idx] == "      join:":
        idx += 1
        while idx < n and node_lines[idx].startswith("        "):  # join: children
            idx += 1
    return ls, idx


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
    # NOTE: the stored `join.scope_claims` comes from the PROJECTION
    # (P.stored_join_view -> pr["node_scope_claims"]), which is the node's
    # EFFECTIVE scope. This previously stamped the plan-level list onto every
    # node, which silently ignored a node-level `scope_claims:` override and
    # would have written a join block that disagreed with the projection that
    # produced the node's own live head. No node sets one today, so the fix is
    # a no-op on the current tree -- but node-level scope_claims is the
    # sanctioned way to narrow a single face (see the GENERATION adjudication,
    # master 417993abd0), so this had to be correct before anyone uses it.

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
    restamped = []
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
        if pr is None:
            out.extend(node_lines)
            skipped.append((nid, "no projection"))
            i = j
            continue

        if not has_blob:
            # Already-collapsed node: re-project (re-stamp) the two-plane block if
            # its stored `live:` head has drifted from the projection. Pure
            # status-plane refresh -- regenerate via the ONE projection path and
            # replace ONLY when it differs, so an up-to-date node is a byte-identical
            # no-op and the body below the frontmatter is untouched. No blob to lift
            # (the history was lifted at the original collapse), so the not-lifted
            # REFUSE does not apply here.
            span = _live_join_span(node_lines)
            if span is None:
                out.extend(node_lines)
                skipped.append((nid, "no blob"))
                i = j
                continue
            ls, le = span
            sl = P.stored_live_view(pr["live"])
            new_block = _live_join_lines(sl, P.stored_join_view(pr))
            if node_lines[ls:le] == new_block:
                out.extend(node_lines)
                skipped.append((nid, "collapsed, current"))
            else:
                out.extend(node_lines[:ls] + new_block + node_lines[le:])
                restamped.append(nid)
            i = j
            continue

        if nid not in lifted:
            raise SystemExit("REFUSE: node %s not lifted to snapshot log; run "
                             "shp2_backfill_snapshot.py first (razor sec 5)." % nid)

        sl = P.stored_live_view(pr["live"])
        lj = _live_join_lines(sl, P.stored_join_view(pr))

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
    print("re-stamped collapsed nodes (%d): %s"
          % (len(restamped), ", ".join(restamped)))
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
