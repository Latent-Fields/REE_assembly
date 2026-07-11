#!/usr/bin/env python3
"""promote_status_history.py -- SHP-3 governance promoter for the status-plane.

status_history_plane:SHP-3 (see evidence/planning/status_history_plane_separation_design.md).

SHP-1 built the read-only projector (`project_status_head.py`) that emits shadow
`live:`+`join:` blocks, per-plan `*_history.md` sidecars, and the diff-vs-blob
report to the git-ignored `scratch/status_history_shadow/` tree. SHP-2 collapsed
every closure-plan blob to the two-plane `live:`+`join:` schema. SHP-3 PROMOTES
the two regenerable-yet-durable artifacts out of scratch into committed,
governance-owned files, and is wired into `governance.sh` so every cycle keeps
them current:

  1. status_snapshot/v1 projection log (contract term 4).
     For every node the projector heads, append a `kind: status_projection`
     record -- the derived `live` head at this run's timestamp -- onto the SAME
     append-only log the SHP-2 backfill lifts wrote to
     (`evidence/planning/status_history/status_snapshot.v1.jsonl`). This makes
     "what did we believe the front was on DATE" answerable.

     Append is CHANGE-ONLY: a node's snapshot is written only when its projected
     `stored_live_view` differs from the most recent `status_projection` record
     for that node (or none exists yet). A stable governance run with no new
     events appends ZERO records -- deliberately, mirroring the state-change-only
     heartbeat design that retired the git-history-bloating liveness tick. A
     change-point timeline still answers the DATE query (take the newest record
     whose projected_utc <= DATE).

  2. Committed per-plan `<plan>_history.md` sidecars.
     Regenerated each run from the SAME projection (via the shared
     `project_status_head.write_history_sidecars`) into the committed
     `evidence/planning/status_history/history/` tree (server-free human view).

This promoter PROMOTES/DEMOTES NO CLAIM. It only appends history events and
regenerates the sidecar index; it edits no `*_plan.md` and no claims.yaml. It is
idempotent: a second run with the same event log appends nothing and rewrites the
sidecars byte-identically.

The `serve.py` query API (Q2=both) reads BOTH the collapsed-plan `live:` head and
this appended history slice; see `/api/status_history`.
"""

import argparse
import json
import os
import sys
from datetime import datetime

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import project_status_head as psh  # noqa: E402  (shares the ONE projection code path)

SNAPSHOT_SCHEMA = "status_snapshot/v1"
PROJECTION_KIND = "status_projection"


def read_last_projection_per_node(log_path):
    """Return {node_id: live_dict} for the most recent `status_projection` record
    per node in the append-only log. Ignores `shp2_backfill_lift` (and any other)
    records. Returns {} when the log is absent."""
    last = {}
    if not os.path.exists(log_path):
        return last
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("kind") != PROJECTION_KIND:
                continue
            nid = d.get("node_id")
            if nid:
                last[nid] = d.get("live") or {}
    return last


def build_snapshot_records(plans, projections, last_by_node, now_iso, projected_by):
    """Return the list of change-only `status_projection` records to append.

    One record per node whose projected `stored_live_view` differs from the last
    recorded projection (or that has none yet). Records are ordered plan-major,
    node-order-within-plan, for a stable, reviewable append block."""
    records = []
    for plan in plans:
        for node in plan["nodes"]:
            nid = node["id"]
            pr = projections.get(nid)
            if pr is None:
                continue
            live = psh.stored_live_view(pr["live"])
            if last_by_node.get(nid) == live:
                continue  # unchanged since last projection -- append nothing
            records.append({
                "schema_version": SNAPSHOT_SCHEMA,
                "kind": PROJECTION_KIND,
                "projected_utc": now_iso,
                "projected_by": projected_by,
                "plan_id": plan["plan_id"],
                "plan_file": plan["file"],
                "node_id": nid,
                "status": node.get("status"),
                "severity": node.get("severity"),
                "live": live,
            })
    return records


def append_records(log_path, records):
    """Append records as one JSON object per line. Append-only: never rewrites
    an existing line. Ensures the parent dir exists."""
    if not records:
        return
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, sort_keys=False) + "\n")


def main():
    ap = argparse.ArgumentParser(
        description="SHP-3 status-history promoter: append change-only status "
                    "projection snapshots + regenerate committed history sidecars.")
    ap.add_argument("--repo-root", default=os.path.dirname(_HERE),
                    help="REE_assembly repo root (default: parent of scripts/).")
    ap.add_argument("--threshold", type=int, default=psh.DEFAULT_BRAKE_THRESHOLD,
                    help="substrate_ceiling count at/above which the brake is fired.")
    ap.add_argument("--log", default=None,
                    help="Append-only snapshot log (default: "
                         "<repo>/evidence/planning/status_history/status_snapshot.v1.jsonl).")
    ap.add_argument("--history-dir", default=None,
                    help="Committed per-plan sidecar dir (default: "
                         "<repo>/evidence/planning/status_history/history).")
    ap.add_argument("--dry-run", action="store_true",
                    help="Compute + report but write NOTHING (no append, no sidecars).")
    args = ap.parse_args()

    repo_root = os.path.abspath(args.repo_root)
    log_path = args.log or os.path.join(
        repo_root, "evidence", "planning", "status_history", "status_snapshot.v1.jsonl")
    history_dir = args.history_dir or os.path.join(
        repo_root, "evidence", "planning", "status_history", "history")
    planning_dir = os.path.join(repo_root, "evidence", "planning")
    now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    projected_by = "SHP-3 governance.sh / promote_status_history.py"

    plans, skipped = psh.load_plans(planning_dir)
    events, event_counts = psh.load_events(repo_root)
    projections = psh.build_projections(plans, events, args.threshold)

    last_by_node = read_last_projection_per_node(log_path)
    records = build_snapshot_records(plans, projections, last_by_node,
                                     now_iso, projected_by)

    n_nodes = sum(len(p["nodes"]) for p in plans)
    print("promote_status_history.py (SHP-3) -- status-plane promotion")
    print("  plans=%d nodes=%d  events: autopsy=%d manifest_PASS=%d decision=%d"
          % (len(plans), n_nodes, event_counts["autopsy"],
             event_counts["manifest_PASS"], event_counts["decision"]))
    seeded = sum(1 for r in records if r["node_id"] not in last_by_node)
    changed = len(records) - seeded
    if args.dry_run:
        print("  DRY-RUN: would append %d status_projection record(s) "
              "(%d newly-seeded, %d changed); sidecars NOT written."
              % (len(records), seeded, changed))
        print("  log: %s" % log_path)
        print("  sidecars: %s" % history_dir)
        return

    append_records(log_path, records)
    psh.write_history_sidecars(
        history_dir, plans, projections, repo_root,
        generated_note="Generated by governance.sh (status_history_plane:SHP-3)")

    print("  appended %d status_projection record(s) (%d newly-seeded, %d changed)"
          % (len(records), seeded, changed))
    print("  -> %s" % os.path.relpath(log_path, repo_root))
    print("  wrote %d per-plan history sidecar(s)" % len(plans))
    print("  -> %s/" % os.path.relpath(history_dir, repo_root))
    if skipped:
        print("  skipped plans (YAML parse): %s" % ", ".join(f for f, _ in skipped))
    print("  PROMOTES/DEMOTES NOTHING; edits no *_plan.md, no claims.yaml.")


if __name__ == "__main__":
    main()
