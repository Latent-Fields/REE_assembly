#!/usr/bin/env python3
"""
IGW assignment ledger -- sole source of truth for "this IGW has been handed
to an agent (and which agent)".

Why a separate file from igw_routine_ledger.json:
- The routine ledger carries process state (worktree path, branch, screen
  session, task_claim session_id). That is specific to claude_local spawns.
- Manual assignments (Cursor / Codex / a teammate's session) have none of
  that -- they are just "I clicked Assign in the workset UI at time T".
- Both kinds need to feed the same "skip this IGW" check in the routine and
  the same chip on the UI. Hence one assignments file, two writers.

Schema (evidence/planning/igw_assignments.json):

    {
      "schema_version": "igw_assignments/v1",
      "agent_kinds": ["claude_local", "cursor", "codex", "other"],
      "entries": [
        {
          "event_id": "asn-20260525T201500Z-bfbc5eb3-claude_local",
          "stable_hash": "bfbc5eb3356f",      # from stable_hash_item(item)
          "igw_id_at_assign": "IGW-20260525-037",
          "agent": "claude_local",
          "agent_label": null,                 # free-text when agent=="other"
          "source": "igw_routine_tick",        # or "manual_ui" / "cli"
          "assigned_at": "2026-05-25T20:15:00Z",
          "released_at": null,
          "released_by": null,
          "released_reason": null,
          "note": null,
          "item_snapshot": {                   # tiny snapshot so the ledger
            "skill": "/queue-experiment",      # is human-readable years later
            "title": "Retest after substrate: ARC-062",
            "lane": "experiment",
            "priority": 28,
            "claim_ids": ["ARC-062"]
          }
        }
      ]
    }

Append-only. release() does NOT mutate the original entry; it adds a new
entry with the same stable_hash + agent and status=released and links back
via released_event_for. Active-set query collapses by (stable_hash, agent)
keeping the latest event.

ASCII-only output (REE_Working/CLAUDE.md rule).
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent  # REE_assembly/
ASSIGNMENTS = ROOT / "evidence" / "planning" / "igw_assignments.json"

VALID_AGENTS = {"claude_local", "cursor", "codex", "other"}
VALID_SOURCES = {"igw_routine_tick", "manual_ui", "cli", "import"}

# Conservative label sanitiser: ASCII, no control chars, max 80.
_LABEL_RE = re.compile(r"[^\x20-\x7e]")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def stable_hash_item(item: dict) -> str:
    """Identity hash for an IGW work package.

    MUST match scripts/igw_routine_tick.py:stable_hash(). Keyed on
    (skill, owner_exq, sorted gap_ids, sorted claim_ids). Survives the
    daily IGW-YYYYMMDD-NNN ID rotation.
    """
    key = {
        "skill": item.get("skill") or "",
        "owner_exq": item.get("owner_exq") or "",
        "gap_ids": sorted(item.get("gap_ids") or []),
        "claim_ids": sorted(item.get("claim_ids") or []),
    }
    blob = json.dumps(key, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(blob.encode("ascii")).hexdigest()[:12]


def _item_snapshot(item: dict) -> dict:
    return {
        "skill": item.get("skill"),
        "title": item.get("title"),
        "lane": item.get("lane"),
        "priority": item.get("priority"),
        "claim_ids": list(item.get("claim_ids") or []),
    }


def load() -> dict:
    if not ASSIGNMENTS.exists():
        return {
            "schema_version": "igw_assignments/v1",
            "generated_at": _now_iso(),
            "agent_kinds": sorted(VALID_AGENTS),
            "entries": [],
        }
    return json.loads(ASSIGNMENTS.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    data["generated_at"] = _now_iso()
    ASSIGNMENTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def active_entries(data: Optional[dict] = None) -> list[dict]:
    """Collapse the append-only log to current active assignments.

    For each (stable_hash, agent, agent_label) key, keep only the latest event
    (by assigned_at, breaking ties by event_id). Drop ones whose latest event
    is released. Returns list sorted by assigned_at desc.
    """
    if data is None:
        data = load()
    latest: dict[tuple[str, str, str], dict] = {}
    for ent in data.get("entries", []):
        key = (
            ent.get("stable_hash") or "",
            ent.get("agent") or "",
            ent.get("agent_label") or "",
        )
        prev = latest.get(key)
        if prev is None or (ent.get("assigned_at") or "") >= (prev.get("assigned_at") or ""):
            latest[key] = ent
    active = [e for e in latest.values() if not e.get("released_at")]
    active.sort(key=lambda e: e.get("assigned_at") or "", reverse=True)
    return active


def assignments_by_hash(data: Optional[dict] = None) -> dict[str, list[dict]]:
    """Active assignments keyed by stable_hash, for the generator merge."""
    out: dict[str, list[dict]] = {}
    for e in active_entries(data):
        out.setdefault(e["stable_hash"], []).append({
            "agent": e.get("agent"),
            "agent_label": e.get("agent_label"),
            "assigned_at": e.get("assigned_at"),
            "source": e.get("source"),
            "note": e.get("note"),
            "event_id": e.get("event_id"),
        })
    return out


def _validate_agent(agent: str, agent_label: Optional[str]) -> tuple[str, Optional[str]]:
    if agent not in VALID_AGENTS:
        raise ValueError(f"agent must be one of {sorted(VALID_AGENTS)}, got {agent!r}")
    label = None
    if agent == "other":
        if not agent_label or not agent_label.strip():
            raise ValueError("agent='other' requires non-empty agent_label")
        label = _LABEL_RE.sub("", agent_label.strip())[:80] or None
        if not label:
            raise ValueError("agent_label is empty after sanitisation")
    elif agent_label:
        # Allow optional descriptive label on enum agents (e.g. machine hint),
        # but sanitise and cap.
        label = _LABEL_RE.sub("", agent_label.strip())[:80] or None
    return agent, label


def assign(
    item: dict,
    *,
    agent: str,
    agent_label: Optional[str] = None,
    source: str,
    note: Optional[str] = None,
    now_iso: Optional[str] = None,
) -> dict:
    """Record a new active assignment. Returns the new entry."""
    if source not in VALID_SOURCES:
        raise ValueError(f"source must be one of {sorted(VALID_SOURCES)}, got {source!r}")
    agent, label = _validate_agent(agent, agent_label)
    stable = stable_hash_item(item)
    ts = now_iso or _now_iso()
    event_id = f"asn-{ts.replace(':', '').replace('-', '')}-{stable[:8]}-{agent}"
    if label:
        event_id += "-" + re.sub(r"[^a-z0-9]+", "-", label.lower())[:20].strip("-")
    entry = {
        "event_id": event_id,
        "stable_hash": stable,
        "igw_id_at_assign": item.get("id"),
        "agent": agent,
        "agent_label": label,
        "source": source,
        "assigned_at": ts,
        "released_at": None,
        "released_by": None,
        "released_reason": None,
        "note": note,
        "item_snapshot": _item_snapshot(item),
    }
    data = load()
    data.setdefault("entries", []).append(entry)
    save(data)
    return entry


def release(
    stable_hash_val: str,
    *,
    agent: str,
    agent_label: Optional[str] = None,
    released_by: str,
    reason: Optional[str] = None,
    now_iso: Optional[str] = None,
) -> Optional[dict]:
    """Release the active assignment for (stable_hash, agent, agent_label).

    Returns the new release entry, or None if there was no active assignment
    to release (idempotent no-op).
    """
    agent, label = _validate_agent(agent, agent_label)
    data = load()
    # Find the matching active entry to snapshot from.
    target = None
    for e in active_entries(data):
        if (
            e.get("stable_hash") == stable_hash_val
            and e.get("agent") == agent
            and (e.get("agent_label") or "") == (label or "")
        ):
            target = e
            break
    if target is None:
        return None
    ts = now_iso or _now_iso()
    event_id = f"rel-{ts.replace(':', '').replace('-', '')}-{stable_hash_val[:8]}-{agent}"
    entry = {
        "event_id": event_id,
        "stable_hash": stable_hash_val,
        "igw_id_at_assign": target.get("igw_id_at_assign"),
        "agent": agent,
        "agent_label": label,
        "source": target.get("source"),
        "assigned_at": ts,           # later-than original so collapse picks it
        "released_at": ts,
        "released_by": released_by,
        "released_reason": reason,
        "released_event_for": target.get("event_id"),
        "note": target.get("note"),
        "item_snapshot": target.get("item_snapshot"),
    }
    data.setdefault("entries", []).append(entry)
    save(data)
    return entry


def has_any_active_assignment(stable_hash_val: str, data: Optional[dict] = None) -> bool:
    """Used by the routine to skip already-handed IGWs (regardless of agent)."""
    for e in active_entries(data):
        if e.get("stable_hash") == stable_hash_val:
            return True
    return False


def recent_releases(
    hours: float = 24.0,
    data: Optional[dict] = None,
    now_iso: Optional[str] = None,
) -> list[dict]:
    """Release events whose released_at is within the last `hours`.

    Used by the workset "Recent activity" panel. Returns release entries
    (event_id starting "rel-") with released_at >= now - hours, sorted by
    released_at descending. The corresponding assign event is preserved
    in the ledger but not returned here -- the release entry's item_snapshot
    + assigned_at field carry everything the UI needs to render a row.
    """
    if data is None:
        data = load()
    now_s = now_iso or _now_iso()
    # ISO-8601 lexicographic comparison works for the strict UTC format we use.
    # Compute cutoff by parsing then formatting back.
    try:
        now_dt = datetime.strptime(now_s.rstrip("Z"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        now_dt = datetime.now(timezone.utc).replace(microsecond=0)
    from datetime import timedelta
    cutoff = (now_dt - timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    for ent in data.get("entries", []):
        rel = ent.get("released_at")
        if not rel:
            continue
        if rel < cutoff:
            continue
        out.append(ent)
    out.sort(key=lambda e: e.get("released_at") or "", reverse=True)
    return out


if __name__ == "__main__":  # pragma: no cover (smoke)
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "show"
    if cmd == "show":
        data = load()
        active = active_entries(data)
        print(f"entries:    {len(data.get('entries', []))}")
        print(f"active:     {len(active)}")
        for e in active:
            label = f" ({e['agent_label']})" if e.get("agent_label") else ""
            print(f"  {e.get('igw_id_at_assign'):25s}  {e['agent']}{label:20s}  "
                  f"{e.get('assigned_at')}  via {e.get('source')}")
    else:
        print(f"unknown cmd: {cmd}")
        sys.exit(2)
