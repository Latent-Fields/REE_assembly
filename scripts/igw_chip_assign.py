#!/usr/bin/env python3
"""Register / release a "spawned_task" assignment for an end-of-skill chip.

When a project skill or /session-land Phase 3 spawns a `spawn_task` chip for
follow-on work that corresponds to a current workset / IGW item, run this to
mirror it into the cross-agent assignment ledger (igw_assignments.json) under
agent kind "spawned_task". That makes the chipped work legible on the same
"assigned" surfaces everything else uses (workset.html + /igw) AND lets the
IGW auto-spawn routine skip it (its eligibility gate skips items with any
active assignment), so a chipped item is not duplicated by a headless spawn.

spawn_task is a Claude Code MCP tool with no callback, so this bridge is an
explicit step -- there is nothing to auto-detect the chip. Pair it with the
chip lifecycle:
  - on spawn_task  -> igw_chip_assign.py assign  --igw <ID> [--chip-title ...]
  - on dismiss_task -> igw_chip_assign.py release --igw <ID> --reason dismissed

The item is resolved from evidence/planning/inter_governance_workset.v1.json
by IGW id (exact) or by claim id (must match exactly one ready item). The
assignment is keyed by the item's stable_hash, which survives IGW-id churn
across workset regenerations.

Stdlib-only; ASCII-only stdout (REE_Working/CLAUDE.md rule).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # REE_assembly/
WORKSET = ROOT / "evidence" / "planning" / "inter_governance_workset.v1.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import igw_assignments_lib as ial  # noqa: E402

AGENT = "spawned_task"
SOURCE = "session_land_chip"


def _load_items() -> list:
    if not WORKSET.exists():
        return []
    try:
        data = json.loads(WORKSET.read_text(encoding="utf-8"))
    except Exception:
        return []
    items = data.get("items") if isinstance(data, dict) else None
    return items if isinstance(items, list) else []


def _resolve(igw_id, claim):
    """Return (item, error_str). Exactly one of igw_id / claim is used."""
    items = _load_items()
    if not items:
        return None, "workset is empty or unreadable (run /inter-governance-brief first)"
    if igw_id:
        for it in items:
            if it.get("id") == igw_id:
                return it, None
        return None, f"no workset item with id {igw_id!r}"
    # claim path
    matches = [it for it in items if claim in (it.get("claim_ids") or [])]
    if not matches:
        return None, f"no workset item tagged claim {claim!r}"
    if len(matches) > 1:
        ids = ", ".join(
            f"{m.get('id')} ({m.get('skill')}: {m.get('title')})" for m in matches
        )
        return None, (
            f"claim {claim!r} matches {len(matches)} items; pass --igw to disambiguate. "
            f"candidates: {ids}"
        )
    return matches[0], None


def _stable_hash_for(item) -> str:
    return item.get("stable_hash") or ial.stable_hash_item(item)


def cmd_assign(args) -> int:
    item, err = _resolve(args.igw, args.claim)
    if err:
        print("ERROR: " + err)
        return 2
    note_bits = []
    if args.chip_title:
        note_bits.append(f"chip:{args.chip_title}")
    if args.chip_id:
        note_bits.append(f"id:{args.chip_id}")
    note = " ".join(note_bits) or None
    stable = _stable_hash_for(item)
    if ial.has_any_active_assignment(stable):
        # Already assigned (to anyone). Surface it -- do not double-write.
        existing = ial.assignments_by_hash().get(stable, [])
        who = ", ".join(f"{a.get('agent')}({a.get('source')})" for a in existing)
        print(f"NOOP: {item.get('id')} already has an active assignment: {who}")
        return 0
    entry = ial.assign(item, agent=AGENT, source=SOURCE, note=note)
    print(
        f"ASSIGNED {item.get('id')} -> spawned_task "
        f"(stable_hash={stable[:12]} event={entry['event_id']})"
    )
    return 0


def cmd_release(args) -> int:
    if args.hash:
        stable = args.hash
        label = stable
    else:
        item, err = _resolve(args.igw, args.claim)
        if err:
            print("ERROR: " + err)
            return 2
        stable = _stable_hash_for(item)
        label = item.get("id")
    entry = ial.release(
        stable,
        agent=AGENT,
        released_by=args.released_by,
        reason=args.reason,
    )
    if entry is None:
        print(f"NOOP: no active spawned_task assignment for {label}")
        return 0
    print(f"RELEASED {label} (spawned_task, reason={args.reason or 'none'})")
    return 0


def cmd_list(args) -> int:
    active = [e for e in ial.active_entries() if e.get("agent") == AGENT]
    if not active:
        print("no active spawned_task assignments")
        return 0
    print(f"{len(active)} active spawned_task assignment(s):")
    for e in active:
        snap = e.get("item_snapshot") or {}
        print(
            f"  {e.get('igw_id_at_assign')}  hash={e.get('stable_hash', '')[:12]}  "
            f"{snap.get('skill', '')}: {snap.get('title', '')}  "
            f"assigned_at={e.get('assigned_at')}  note={e.get('note')}"
        )
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd")

    pa = sub.add_parser("assign", help="register a spawned_task assignment")
    g = pa.add_mutually_exclusive_group(required=True)
    g.add_argument("--igw", help="IGW id (exact match)")
    g.add_argument("--claim", help="claim id (must match exactly one ready item)")
    pa.add_argument("--chip-title", help="spawn_task chip title (for the note)")
    pa.add_argument("--chip-id", help="spawn_task task_id (for the note)")
    pa.set_defaults(func=cmd_assign)

    pr = sub.add_parser("release", help="release a spawned_task assignment")
    gr = pr.add_mutually_exclusive_group(required=True)
    gr.add_argument("--igw", help="IGW id (exact match)")
    gr.add_argument("--claim", help="claim id (must match exactly one ready item)")
    gr.add_argument("--hash", help="stable_hash directly (use when the item left the workset)")
    pr.add_argument("--released-by", default="session_land", help="who released")
    pr.add_argument("--reason", help="release reason, e.g. dismissed / work_landed")
    pr.set_defaults(func=cmd_release)

    pl = sub.add_parser("list", help="list active spawned_task assignments")
    pl.set_defaults(func=cmd_list)

    args = p.parse_args()
    if not getattr(args, "func", None):
        p.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
