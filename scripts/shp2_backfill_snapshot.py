#!/usr/bin/env python3
"""shp2_backfill_snapshot.py -- SHP-2 non-destructive lift (the razor, design sec 5).

status_history_plane:SHP-2 (see evidence/planning/status_history_plane_separation_design.md).

Before a closure-plan node's hand-written `phase:` / `owner_exq:` / `awaiting:`
blobs are collapsed to the two-plane `live:` + `join:` schema, this tool LIFTS
them -- verbatim -- into an append-only status-snapshot log so no history bit is
destroyed by the collapse (design sec 5, step 2). It writes ONE
`status_snapshot/v1` record per node to:

    evidence/planning/status_history/status_snapshot.v1.jsonl   (append-only)

Each record archives the FULL raw node dict verbatim (`archived_node`), plus the
genuinely non-derivable provenance the diff-vs-blob report flags as *at risk* --
governance-applied `master <hash>` commit ids, annotated with their git subject
(these map an autopsy to the REE_assembly commit that applied it; that mapping
lives only in git + the plan prose, never in the autopsy JSON). It also records
the projector's `live` head at lift time for provenance.

This tool:
  * NEVER edits an existing log line (append-only).
  * NEVER edits any *_plan.md (the collapse is a separate, reviewable manual edit).
  * Is IDEMPOTENT: a node already lifted (same node_id, kind shp2_backfill_lift)
    is skipped, so re-running is safe.
  * PROMOTES/DEMOTES NOTHING.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/shp2_backfill_snapshot.py \
        --plan evidence/planning/conversion_ceiling_campaign_plan.md \
        --by "SHP-2 <session-label>"
    # add --dry-run to preview without writing.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import project_status_head as P  # noqa: E402  (shares the ONE projection code path)

REPO_ROOT = os.path.dirname(HERE)
SNAPSHOT_DIR = os.path.join(REPO_ROOT, "evidence", "planning", "status_history")
SNAPSHOT_LOG = os.path.join(SNAPSHOT_DIR, "status_snapshot.v1.jsonl")

# governance-applied commit ids: "... master 65940b83b5 ..." (the un-derivable bit).
_MASTER_COMMIT_RE = re.compile(r"\bmaster ([0-9a-f]{7,40})\b")
# blob/annotation fields whose prose we scan for at-risk commit provenance.
_HISTORY_FIELDS_HINT = ("phase", "owner_exq", "awaiting")


def _git_subject(commit):
    try:
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "-1", "--format=%s", commit],
            capture_output=True, text=True, timeout=10)
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def _raw_nodes(plan_file):
    """Parse the plan frontmatter and return the RAW node dicts (verbatim), so the
    archive preserves every field, not just the three collapsible blobs."""
    text = open(plan_file, encoding="utf-8").read()
    fm = P.extract_frontmatter(text)
    if fm is None:
        raise SystemExit("no YAML frontmatter in %s" % plan_file)
    import yaml
    meta = yaml.safe_load(fm)
    cp = (meta or {}).get("closure_plan") or {}
    return cp, cp.get("nodes") or []


def _at_risk_commits(raw_node):
    """Extract governance-apply commit provenance from every string field of the
    raw node (the diff-vs-blob `at_risk` commit tokens). Deduped, git-annotated."""
    found = {}
    for field, val in raw_node.items():
        if not isinstance(val, str):
            continue
        for m in _MASTER_COMMIT_RE.finditer(val):
            h = m.group(1)
            if h not in found:
                found[h] = field
    bits = []
    for h, field in found.items():
        bits.append({
            "kind": "commit", "token": h,
            "git_subject": _git_subject(h),
            "first_seen_field": field,
            "meaning": "REE_assembly master commit named in the plan prose "
                       "(governance-apply / build provenance not recorded in any "
                       "autopsy/manifest/decision event).",
        })
    return bits


def _already_lifted(node_ids):
    """Set of node_ids that already have an shp2_backfill_lift record."""
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
        if r.get("kind") == "shp2_backfill_lift" and r.get("node_id") in node_ids:
            done.add(r["node_id"])
    return done


def main():
    ap = argparse.ArgumentParser(description="SHP-2 non-destructive lift (razor sec 5).")
    ap.add_argument("--plan", required=True,
                    help="repo-relative path to the *_plan.md to lift")
    ap.add_argument("--node", default=None,
                    help="only lift nodes whose id contains this substring")
    ap.add_argument("--by", default="SHP-2", help="lifted_by label")
    ap.add_argument("--dry-run", action="store_true",
                    help="print records, write nothing")
    args = ap.parse_args()

    plan_file = args.plan if os.path.isabs(args.plan) else os.path.join(REPO_ROOT, args.plan)
    plan_rel = os.path.relpath(plan_file, REPO_ROOT)
    cp, raw_nodes = _raw_nodes(plan_file)
    plan_id = cp.get("id") or os.path.basename(plan_file).replace("_plan.md", "")

    # projector `live` per node (the SAME code path the drift check re-runs)
    planning_dir = os.path.join(REPO_ROOT, "evidence", "planning")
    all_plans, _skipped = P.load_plans(planning_dir)
    target_plans = [p for p in all_plans if p["plan_id"] == plan_id]
    if not target_plans:
        raise SystemExit("plan_id %r not found via load_plans" % plan_id)
    events, _counts = P.load_events(REPO_ROOT)
    projections = P.build_projections(target_plans, events, P.DEFAULT_BRAKE_THRESHOLD)

    now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    node_ids = {n.get("id") for n in raw_nodes if isinstance(n, dict) and n.get("id")}
    already = _already_lifted(node_ids)

    records = []
    for rn in raw_nodes:
        if not isinstance(rn, dict) or not rn.get("id"):
            continue
        nid = rn["id"]
        if args.node and args.node not in nid:
            continue
        if nid in already:
            print("skip (already lifted): %s" % nid)
            continue
        # Lift every node the collapse will process. The collapse detects a
        # "blob" by the presence of a phase/owner_exq/awaiting physical LINE
        # (any value type -- incl. integer `phase: 3` and `owner_exq: null`),
        # so lift-eligibility must be keyed on field PRESENCE, not on the value
        # being a non-empty string. Otherwise the collapse REFUSES an un-lifted
        # node whose blob is a scalar/null (razor sec 5). The whole raw node is
        # archived verbatim regardless, so lifting a trivial `phase: 3` is
        # harmless and preserves the field for provenance.
        if not any(f in rn for f in _HISTORY_FIELDS_HINT):
            print("skip (no phase/owner_exq/awaiting field): %s" % nid)
            continue
        pr = projections.get(nid)
        live_view = P.stored_live_view(pr["live"]) if pr else {}
        rec = {
            "schema_version": "status_snapshot/v1",
            "kind": "shp2_backfill_lift",
            "lifted_utc": now_iso,
            "lifted_by": args.by,
            "plan_id": plan_id,
            "plan_file": plan_rel,
            "node_id": nid,
            "scope_claims": rn.get("scope_claims") or cp.get("scope_claims") or [],
            "reason": ("SHP-2 non-destructive collapse (design sec 5): archived the "
                       "hand-written phase/owner_exq/awaiting + annotation blobs "
                       "verbatim BEFORE the two-plane live:+join: collapse. "
                       "Append-only; never edits an existing event."),
            "at_risk_history_bits": _at_risk_commits(rn),
            "archived_node": rn,
            "projected_live_at_lift": live_view,
        }
        records.append(rec)

    if not records:
        print("nothing to lift (all nodes already lifted or blob-free).")
        return 0

    for rec in records:
        n_bits = len(rec["at_risk_history_bits"])
        print("lift: %s  (%d at-risk commit bit(s))" % (rec["node_id"], n_bits))

    if args.dry_run:
        print("\n--- DRY RUN (nothing written). Sample record: ---")
        print(json.dumps(records[0], indent=2, default=str)[:1600])
        return 0

    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    with open(SNAPSHOT_LOG, "a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
    print("\nappended %d record(s) to %s"
          % (len(records), os.path.relpath(SNAPSHOT_LOG, REPO_ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
