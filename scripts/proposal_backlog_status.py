#!/usr/bin/env python3
"""
Report how many V3-relevant experiment proposals are still outstanding.

"V3-relevant" = proposal_type == "experimental" and target_repo is ree-v3 (or
unset, which defaults to ree-v3 for experimental proposals) -- i.e. items that
would actually route through /queue-experiment, as opposed to literature
proposals (which route through /lit-pull and are reported separately so they
are not silently swept).

"Outstanding" = status == "proposed" -- not yet gated / blocked_substrate /
executed / any other disposition.

Usage (from REE_assembly root):
    python scripts/proposal_backlog_status.py
    python scripts/proposal_backlog_status.py --priority medium
    python scripts/proposal_backlog_status.py --json

Reads evidence/planning/experiment_proposals_index.v1.json (the lightweight
index -- do not read the full experiment_proposals.v1.json for this, it
exceeds the Read tool's size limit and is unnecessary for a status count).
"""
import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = REPO_ROOT / "evidence" / "planning" / "experiment_proposals_index.v1.json"

PRIORITY_ORDER = ["high", "medium", "low"]


def is_v3_relevant(item):
    if item.get("proposal_type") != "experimental":
        return False
    target_repo = item.get("target_repo")
    return target_repo in (None, "", "ree-v3") or str(target_repo).startswith("ree-v3")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--priority", choices=PRIORITY_ORDER, help="filter to one priority tier")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON instead of text")
    args = ap.parse_args()

    with open(INDEX_PATH) as f:
        data = json.load(f)
    items = data["items"] if isinstance(data, dict) else data

    v3_outstanding = [it for it in items if it.get("status") == "proposed" and is_v3_relevant(it)]
    lit_outstanding = [it for it in items if it.get("status") == "proposed" and not is_v3_relevant(it)]
    all_status_counts = Counter(it.get("status") for it in items)

    if args.priority:
        v3_outstanding = [it for it in v3_outstanding if it.get("priority") == args.priority]

    by_priority = defaultdict(list)
    for it in v3_outstanding:
        by_priority[it.get("priority", "unknown")].append(it)

    if args.json:
        out = {
            "total_v3_outstanding": len(v3_outstanding),
            "by_priority": {p: len(by_priority.get(p, [])) for p in PRIORITY_ORDER},
            "literature_outstanding_not_v3": len(lit_outstanding),
            "all_status_counts": dict(all_status_counts),
            "items": [
                {
                    "claim_id": it.get("claim_id"),
                    "proposal_id": it.get("proposal_id"),
                    "backlog_id": it.get("backlog_id"),
                    "priority": it.get("priority"),
                }
                for it in v3_outstanding
            ],
        }
        print(json.dumps(out, indent=2))
        return

    print(f"V3-relevant outstanding (proposed) proposals: {len(v3_outstanding)}")
    print(f"  (proposal_type=experimental, target_repo=ree-v3-or-unset, status=proposed)")
    print()
    for p in PRIORITY_ORDER:
        rows = sorted(by_priority.get(p, []), key=lambda it: it.get("claim_id") or "")
        if args.priority and p != args.priority:
            continue
        print(f"-- {p} ({len(rows)}) --")
        for it in rows:
            print(f"  {it.get('claim_id'):<12} {it.get('proposal_id') or '':<10} backlog_id={it.get('backlog_id')}")
        if not rows:
            print("  (none)")
        print()

    print(f"Literature proposals outstanding (not V3-relevant, route via /lit-pull): {len(lit_outstanding)}")
    print()
    print("All proposals by status (any priority, any type):")
    for status, count in sorted(all_status_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {status:<20} {count}")

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
