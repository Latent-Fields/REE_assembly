#!/usr/bin/env python3
"""Build the public REE Development Map data projection.

The map is a reader-facing projection, not a second roadmap. It joins the
current-front, progress, claim/dependency, and operational-archive records and
never changes a claim, status, weight, or schedule.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PROGRESS = DOCS / "assets" / "data" / "progress.v1.json"
DEPENDENCIES = DOCS / "assets" / "data" / "claim_dependency_process.v1.json"
CURRENT_FRONT = DOCS / "CURRENT_FRONT.md"
ROADMAP = DOCS / "roadmap.md"
OUT = DOCS / "assets" / "data" / "development_map.v1.json"

SCHEMA_VERSION = "development_map/v1"
MAX_NODES_PER_BUCKET = 10
CLOSED_STATUSES = {"stable", "resolved", "retired", "retiring", "legacy", "superseded", "candidate_resolved"}
ACTIVE_STATUSES = {"active", "provisional", "implemented", "candidate_substrate_landed"}
BUCKETS = (("active", "Active / under review"), ("closed", "Closed record"), ("planned", "Planned / conditional"))
TRACKS = (
    ("foundations", "Foundations", "Invariants and premises carried into the programme."),
    ("architecture", "Architecture", "System commitments and mechanism-level design."),
    ("substrate", "Substrate", "Implementation and test-bed work that makes a question testable."),
    ("evidence", "Evidence", "V3 claims being exposed to an experimental verdict."),
    ("future", "Future shape", "Later phases and conditional work, not a promised schedule."),
)


def read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit("Development Map input is unavailable: %s (%s)" % (path, exc))
    if not isinstance(payload, dict):
        raise SystemExit("Development Map input must be a JSON object: %s" % path)
    return payload


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit("Development Map input is unavailable: %s (%s)" % (path, exc))


def clean_text(value: Any) -> str:
    return " ".join(str(value or "").split())


def status_bucket(status: Any) -> str:
    normalised = clean_text(status).lower()
    if normalised in CLOSED_STATUSES:
        return "closed"
    if normalised in ACTIVE_STATUSES:
        return "active"
    return "planned"


def track_for(row: dict[str, Any]) -> str:
    phase = clean_text(row.get("phase")).lower()
    claim_class = clean_text(row.get("class")).lower()
    lifecycle = clean_text(row.get("lifecycle")).lower()
    if phase in {"v4", "v5", "v6", "post_v5"} or claim_class.startswith("horizon_"):
        return "future"
    if lifecycle == "substrate_implementation_active" or claim_class in {"substrate_gap_marked", "substrate_or_design"}:
        return "substrate"
    if claim_class == "active_v3_closure":
        return "evidence"
    if claim_class == "invariant_or_foundation":
        return "foundations"
    return "architecture"


def serialise_claim(row: dict[str, Any]) -> dict[str, Any]:
    dependencies = [clean_text(dep) for dep in row.get("depends_on") or [] if clean_text(dep)]
    return {
        "id": clean_text(row.get("id")),
        "title": clean_text(row.get("title")) or "Untitled claim",
        "status": clean_text(row.get("status")) or "unclassified",
        "phase": clean_text(row.get("phase")) or "unspecified",
        "claim_class": clean_text(row.get("class")) or "other",
        "lifecycle": clean_text(row.get("lifecycle")) or "unclassified",
        "attention_rank": int(row.get("attention_rank") or 0),
        "incoming_dependencies": int(row.get("incoming_dependency_count") or 0),
        "depends_on": dependencies[:8],
        "additional_dependencies": max(0, len(dependencies) - 8),
    }


def claim_sort_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (-int(row.get("attention_rank") or 0), -int(row.get("incoming_dependency_count") or 0), clean_text(row.get("id")))


def build_tracks(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped = {key: {bucket: [] for bucket, _label in BUCKETS} for key, _title, _summary in TRACKS}
    for row in rows:
        if clean_text(row.get("id")):
            grouped[track_for(row)][status_bucket(row.get("status"))].append(row)

    tracks = []
    for key, title, summary in TRACKS:
        bucket_payload = []
        for bucket, label in BUCKETS:
            source_rows = sorted(grouped[key][bucket], key=claim_sort_key)
            selected = source_rows[:MAX_NODES_PER_BUCKET]
            bucket_payload.append({
                "key": bucket,
                "label": label,
                "count": len(source_rows),
                "more_count": max(0, len(source_rows) - len(selected)),
                "nodes": [serialise_claim(row) for row in selected],
            })
        tracks.append({"id": key, "title": title, "summary": summary, "total": sum(item["count"] for item in bucket_payload), "buckets": bucket_payload})
    return tracks


def parse_current_front(text: str) -> dict[str, str | None]:
    live_block = re.search(r"^## The one live front\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    block = live_block.group(1) if live_block else ""
    headline = next((clean_text(line) for line in block.splitlines() if clean_text(line) and not clean_text(line).startswith(("-", ">"))), None)
    if headline and "could not derive" in headline.lower():
        headline = None
    gate_match = re.search(r"^- \*\*The gate:\*\*\s*(.+)$", block, re.M)
    return {"headline": headline, "gate": clean_text(gate_match.group(1)) if gate_match else None}


def progress_metrics(progress: dict[str, Any]) -> list[dict[str, str]]:
    needles = progress.get("needles") or {}
    build, prove = needles.get("build") or {}, needles.get("prove") or {}
    narrow, decide = needles.get("narrow") or {}, needles.get("decide") or {}
    return [
        {"label": "Build", "value": "%s / %s" % (build.get("built_modules", "?"), build.get("total_modules", "?")), "detail": "modules recorded as built"},
        {"label": "Prove", "value": "%s%%" % prove.get("closure_pct", "?"), "detail": "weighted closure, not an overall score"},
        {"label": "Narrow", "value": "%s / %s" % (narrow.get("total_surviving", "?"), narrow.get("total_initial_at_registration", "?")), "detail": "rival explanations still standing"},
        {"label": "Decide", "value": str(decide.get("ready", "?")), "detail": "design choices currently recorded as ready"},
    ]


def serialise_question(question: dict[str, Any]) -> dict[str, Any]:
    convergence = question.get("convergence") or {}
    return {
        "id": clean_text(question.get("qid")),
        "title": clean_text(question.get("short_title") or question.get("title")) or "Open investigation",
        "claims": [clean_text(claim) for claim in question.get("claims") or [] if clean_text(claim)],
        "surviving": question.get("surviving"),
        "initial": question.get("initial_frozen_count"),
        "convergence": clean_text(convergence.get("convergence_class")) or "unclassified",
        "is_hero": bool(question.get("is_hero")),
    }


def snapshot_dates(roadmap: str) -> list[str]:
    dates = re.findall(r"^## Status Snapshot \((\d{4}-\d{2}-\d{2})(?:T[^)]*)?\)", roadmap, re.M)
    return list(dict.fromkeys(dates))


def build_payload() -> dict[str, Any]:
    progress = read_json(PROGRESS)
    dependencies = read_json(DEPENDENCIES)
    rows = dependencies.get("claim_rows") or []
    questions = progress.get("questions") or []
    if not isinstance(rows, list) or not isinstance(questions, list):
        raise SystemExit("Development Map inputs do not have their expected list fields")

    serialised_questions = [serialise_question(question) for question in questions if isinstance(question, dict)]
    serialised_questions.sort(key=lambda question: (not question["is_hero"], question["id"]))
    snapshots = snapshot_dates(read_text(ROADMAP))
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": progress.get("generated_at") or dependencies.get("generated_at_utc"),
        "contract": "Derived public index only. Claim state, evidence, and schedules remain canonical in the cited repository records.",
        "sources": ["docs/CURRENT_FRONT.md", "docs/assets/data/progress.v1.json", "docs/assets/data/claim_dependency_process.v1.json", "docs/roadmap.md"],
        "frontier": {**parse_current_front(read_text(CURRENT_FRONT)), "questions": serialised_questions},
        "metrics": progress_metrics(progress),
        "tracks": build_tracks([row for row in rows if isinstance(row, dict)]),
        "record_counts": dict(Counter(status_bucket(row.get("status")) for row in rows if isinstance(row, dict))),
        "archive": {"snapshot_count": len(snapshots), "latest": snapshots[0] if snapshots else None, "earliest": snapshots[-1] if snapshots else None, "recent_dates": snapshots[:10]},
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload.get("schema_version") != SCHEMA_VERSION or len(payload.get("tracks") or []) != len(TRACKS):
        raise SystemExit("Development Map payload is incomplete")
    for track in payload["tracks"]:
        for bucket in track["buckets"]:
            for node in bucket["nodes"]:
                if not node.get("id") or not node.get("title"):
                    raise SystemExit("Development Map emitted a node without an id and title")


def render(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the checked-in output is stale")
    args = parser.parse_args()
    payload = build_payload()
    validate_payload(payload)
    output = render(payload)
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != output:
            print("Development Map output is stale: run python3 scripts/build_development_map.py")
            return 1
        print("Development Map output is current: %s" % OUT.relative_to(ROOT))
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output, encoding="utf-8")
    selected = sum(len(bucket["nodes"]) for track in payload["tracks"] for bucket in track["buckets"])
    print("Wrote %s (%d selected map nodes, %d snapshot dates)" % (OUT.relative_to(ROOT), selected, payload["archive"]["snapshot_count"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
