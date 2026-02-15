#!/usr/bin/env python3
"""Sync checklist tasks from task_inbox.md into manual carryover items."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CHECKBOX_RE = re.compile(r"^\s*-\s*\[(?P<state>[ xX])\]\s+(?P<text>.+?)\s*$")


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "schema_version": "manual_carryover_items/v1",
            "generated_at_utc": _now_utc(),
            "notes": (
                "Use this file for unfinished governance items that must persist across agenda regenerations. "
                "Items with status='done' are excluded from open agenda carryover."
            ),
            "items": [],
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {"schema_version": "manual_carryover_items/v1", "generated_at_utc": _now_utc(), "items": []}
    if not isinstance(data.get("items"), list):
        data["items"] = []
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    payload["generated_at_utc"] = _now_utc()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def _source_ref(text: str) -> str:
    digest = hashlib.sha1(_normalize(text).encode("utf-8")).hexdigest()[:12]
    return f"task_inbox:{digest}"


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


def _parse_inbox(path: Path) -> tuple[list[str], list[str]]:
    if not path.exists():
        return [], []
    open_tasks: list[str] = []
    done_tasks: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = CHECKBOX_RE.match(line)
        if not match:
            continue
        text = match.group("text").strip()
        state = match.group("state")
        if state == " ":
            open_tasks.append(text)
        else:
            done_tasks.append(text)
    return open_tasks, done_tasks


def _prune_done_from_inbox(path: Path) -> bool:
    if not path.exists():
        return False
    changed = False
    kept: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = CHECKBOX_RE.match(line)
        if match and match.group("state").lower() == "x":
            changed = True
            continue
        kept.append(line)
    if changed:
        path.write_text("\n".join(kept).rstrip() + "\n", encoding="utf-8")
    return changed


def sync(inbox_path: Path, carryover_path: Path, dry_run: bool, prune_completed: bool) -> dict[str, int]:
    doc = _load_json(carryover_path)
    items: list[dict[str, Any]] = list(doc.get("items", []))
    open_tasks, done_tasks = _parse_inbox(inbox_path)
    now = _now_utc()

    by_source_ref: dict[str, dict[str, Any]] = {}
    for item in items:
        ref = str(item.get("source_ref", "")).strip()
        if ref:
            by_source_ref[ref] = item

    added = reopened = marked_done = 0
    changed = False

    for task in open_tasks:
        ref = _source_ref(task)
        existing = by_source_ref.get(ref)
        if existing is None:
            item_id = _next_item_id(items)
            new_item = {
                "item_id": item_id,
                "status": "open",
                "priority": "medium",
                "owner": "",
                "summary": task,
                "source_ref": ref,
                "last_updated_utc": now,
                "tags": ["task_inbox"],
            }
            items.append(new_item)
            by_source_ref[ref] = new_item
            added += 1
            changed = True
            continue

        if str(existing.get("summary", "")) != task:
            existing["summary"] = task
            existing["last_updated_utc"] = now
            changed = True
        if str(existing.get("status", "open")).lower() == "done":
            existing["status"] = "open"
            existing["last_updated_utc"] = now
            reopened += 1
            changed = True

    for task in done_tasks:
        ref = _source_ref(task)
        existing = by_source_ref.get(ref)
        if existing is None:
            continue
        if str(existing.get("status", "open")).lower() != "done":
            existing["status"] = "done"
            existing["last_updated_utc"] = now
            marked_done += 1
            changed = True

    doc["items"] = items
    if changed and not dry_run:
        _write_json(carryover_path, doc)
    pruned = 0
    if prune_completed and not dry_run and _prune_done_from_inbox(inbox_path):
        pruned = 1

    open_count = sum(1 for i in items if str(i.get("status", "open")).lower() != "done")
    return {
        "inbox_open": len(open_tasks),
        "inbox_done": len(done_tasks),
        "added": added,
        "reopened": reopened,
        "marked_done": marked_done,
        "changed_records": int(changed),
        "pruned_completed": pruned,
        "carryover_open_total": open_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inbox",
        type=Path,
        default=Path("evidence/planning/task_inbox.md"),
        help="Markdown checklist file used as low-friction task inbox.",
    )
    parser.add_argument(
        "--carryover",
        type=Path,
        default=Path("evidence/planning/manual_carryover_items.v1.json"),
        help="Carryover JSON file to update.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write changes.")
    parser.add_argument(
        "--no-prune-completed",
        action="store_true",
        help="Keep completed checkbox lines in the inbox file instead of removing them.",
    )
    args = parser.parse_args()

    stats = sync(args.inbox, args.carryover, args.dry_run, prune_completed=not args.no_prune_completed)
    print(
        "task inbox sync: "
        + ", ".join(f"{k}={v}" for k, v in stats.items())
        + (", dry_run=true" if args.dry_run else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
