#!/usr/bin/env python3
"""Capture and manage persistent manual carryover items for governance agendas."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _default_doc() -> dict[str, Any]:
    now = _now_utc()
    return {
        "schema_version": "manual_carryover_items/v1",
        "generated_at_utc": now,
        "notes": (
            "Use this file for unfinished governance items that must persist across agenda regenerations. "
            "Items with status='done' are excluded from open agenda carryover."
        ),
        "items": [],
    }


def _load_doc(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_doc()
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return _default_doc()
    if not isinstance(data.get("items"), list):
        data["items"] = []
    data.setdefault("schema_version", "manual_carryover_items/v1")
    data.setdefault("notes", _default_doc()["notes"])
    return data


def _write_doc(path: Path, doc: dict[str, Any]) -> None:
    doc["generated_at_utc"] = _now_utc()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _next_item_id(items: list[dict[str, Any]]) -> str:
    max_n = 0
    for item in items:
        raw = str(item.get("item_id", ""))
        if raw.startswith("MCI-"):
            try:
                n = int(raw.split("-", 1)[1])
            except ValueError:
                continue
            max_n = max(max_n, n)
    return f"MCI-{max_n + 1:04d}"


def _cmd_add(args: argparse.Namespace) -> int:
    doc = _load_doc(args.file)
    items: list[dict[str, Any]] = list(doc.get("items", []))
    item_id = _next_item_id(items)
    now = _now_utc()
    item = {
        "item_id": item_id,
        "status": "open",
        "priority": args.priority,
        "owner": args.owner,
        "summary": args.summary,
        "source_ref": args.source_ref,
        "last_updated_utc": now,
    }
    if args.tags:
        item["tags"] = [t.strip() for t in args.tags.split(",") if t.strip()]
    items.append(item)
    doc["items"] = items

    if not args.dry_run:
        _write_doc(args.file, doc)
    print(f"added {item_id}: {args.summary}")
    if args.dry_run:
        print("dry-run: no file changes written")
    return 0


def _cmd_done(args: argparse.Namespace) -> int:
    doc = _load_doc(args.file)
    items: list[dict[str, Any]] = list(doc.get("items", []))
    for item in items:
        if str(item.get("item_id", "")) == args.item_id:
            item["status"] = "done"
            item["last_updated_utc"] = _now_utc()
            if args.note:
                item["completion_note"] = args.note
            if not args.dry_run:
                _write_doc(args.file, doc)
            print(f"marked done: {args.item_id}")
            if args.dry_run:
                print("dry-run: no file changes written")
            return 0
    print(f"item not found: {args.item_id}")
    return 1


def _cmd_list(args: argparse.Namespace) -> int:
    doc = _load_doc(args.file)
    items: list[dict[str, Any]] = list(doc.get("items", []))
    if args.open_only:
        items = [x for x in items if str(x.get("status", "open")).lower() != "done"]
    if not items:
        print("no carryover items")
        return 0
    for item in items:
        print(
            f"{item.get('item_id','?')} "
            f"status={item.get('status','?')} "
            f"priority={item.get('priority','?')} "
            f"owner={item.get('owner','')} "
            f"summary={item.get('summary','')}"
        )
    return 0


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("evidence/planning/manual_carryover_items.v1.json"),
        help="Path to manual carryover JSON file.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Add a new carryover item.")
    add.add_argument("--summary", required=True, help="Task summary.")
    add.add_argument("--priority", default="medium", choices=["low", "medium", "high"], help="Priority.")
    add.add_argument("--owner", default="", help="Owner label.")
    add.add_argument("--source-ref", default="", help="Optional source pointer.")
    add.add_argument("--tags", default="", help="Comma-separated tags.")
    add.add_argument("--dry-run", action="store_true", help="Preview only.")
    add.set_defaults(func=_cmd_add)

    done = sub.add_parser("done", help="Mark a carryover item as done.")
    done.add_argument("--item-id", required=True, help="Item id, e.g. MCI-0002")
    done.add_argument("--note", default="", help="Optional completion note.")
    done.add_argument("--dry-run", action="store_true", help="Preview only.")
    done.set_defaults(func=_cmd_done)

    ls = sub.add_parser("list", help="List carryover items.")
    ls.add_argument("--open-only", action="store_true", help="List only non-done items.")
    ls.set_defaults(func=_cmd_list)

    return parser


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
