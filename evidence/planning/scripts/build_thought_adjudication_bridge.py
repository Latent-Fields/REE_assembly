#!/usr/bin/env python3
"""Build a thought-to-adjudication bridge report.

This bridge highlights two classes of governance follow-up:
1) approved status recommendations that are not yet reflected in claims.yaml,
2) claims with processed thought-intake updates newer than the latest decision.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

RECOMMENDATION_TARGET_STATUS = {
    "promote_to_stable": "stable",
    "promote_to_provisional": "provisional",
    "demote_to_provisional": "provisional",
    "demote_to_candidate": "candidate",
    "demote_to_legacy": "legacy",
}

REASON_PRIORITY = {
    "approved_pending_apply": 0,
    "thought_newer_than_decision": 1,
    "no_decision_for_thought_enriched_claim": 2,
}

REASON_ACTION = {
    "approved_pending_apply": "apply_approved_decision_and_refresh_indexes",
    "thought_newer_than_decision": "refresh_decision_brief_and_record_adjudication_outcome",
    "no_decision_for_thought_enriched_claim": "open_decision_lane_for_thought_enriched_claim",
}


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path, *, required: bool) -> dict[str, Any]:
    if not path.exists():
        if required:
            raise SystemExit(f"Missing required file: {path}")
        return {}
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON at {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit(f"Expected JSON object at {path}")
    return loaded


def _parse_timestamp(raw: str) -> datetime | None:
    value = str(raw).strip()
    if not value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized).astimezone(timezone.utc)
    except ValueError:
        return None


def _parse_date(raw: str) -> date | None:
    value = str(raw).strip()
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _parse_date_from_filename(filename: str) -> date | None:
    token = str(filename).strip()
    if len(token) >= 10:
        return _parse_date(token[:10])
    return None


def _split_claim_blocks(lines: list[str]) -> list[list[str]]:
    starts = [idx for idx, line in enumerate(lines) if line.startswith("- id: ")]
    if not starts:
        return []
    blocks: list[list[str]] = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        blocks.append(lines[start:end])
    return blocks


def _parse_claims_with_sources(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Missing claims registry: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks = _split_claim_blocks(lines)
    claims: list[dict[str, Any]] = []

    for block in blocks:
        claim_id = ""
        claim_type = ""
        status = ""
        location = ""
        sources: list[str] = []
        in_source = False

        for line in block:
            if line.startswith("- id: "):
                claim_id = line.split(":", 1)[1].strip()
                continue
            if line.startswith("  source:"):
                in_source = True
                continue
            if in_source:
                if line.startswith("    - "):
                    src = line.split("-", 1)[1].strip()
                    if src:
                        sources.append(src)
                    continue
                if not line.startswith("    "):
                    in_source = False
            if line.startswith("  claim_type:"):
                claim_type = line.split(":", 1)[1].strip()
            elif line.startswith("  status:"):
                status = line.split(":", 1)[1].strip()
            elif line.startswith("  location:"):
                location = line.split(":", 1)[1].strip()

        if claim_id:
            claims.append(
                {
                    "claim_id": claim_id,
                    "claim_type": claim_type,
                    "status": status,
                    "location": location,
                    "sources": sources,
                }
            )
    return claims


def _build_thought_record_map(thought_sweep: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records_raw = thought_sweep.get("records", [])
    if not isinstance(records_raw, list):
        return {}
    out: dict[str, dict[str, Any]] = {}
    for raw in records_raw:
        if not isinstance(raw, dict):
            continue
        filename = str(raw.get("file", "")).strip()
        if not filename:
            continue
        filename_date = str(raw.get("filename_date", "")).strip()
        parsed_date = _parse_date(filename_date) or _parse_date_from_filename(filename)
        out[filename] = {
            "file": filename,
            "is_processed": bool(raw.get("is_processed", False)),
            "filename_date": filename_date,
            "parsed_date": parsed_date.isoformat() if parsed_date else "",
        }
    return out


def _build_items(
    claims: list[dict[str, Any]],
    thought_map: dict[str, dict[str, Any]],
    decision_state: dict[str, Any],
    governance_relevant_claim_ids: set[str],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    decisions_by_claim = decision_state.get("claims", {}) if isinstance(decision_state, dict) else {}
    if not isinstance(decisions_by_claim, dict):
        decisions_by_claim = {}

    items: list[dict[str, Any]] = []
    total_with_processed_thoughts = 0
    total_without_decisions = 0

    for claim in claims:
        claim_id = str(claim.get("claim_id", "")).strip()
        status = str(claim.get("status", "")).strip().lower()
        if not claim_id or status == "legacy":
            continue

        source_paths = claim.get("sources", [])
        if not isinstance(source_paths, list):
            source_paths = []
        thought_paths = [str(x).strip() for x in source_paths if str(x).strip().startswith("docs/thoughts/")]

        processed_thoughts: list[dict[str, Any]] = []
        for src in thought_paths:
            rec = thought_map.get(Path(src).name)
            if rec and bool(rec.get("is_processed", False)):
                processed_thoughts.append({"source_path": src, **rec})

        decision = decisions_by_claim.get(claim_id, {})
        if not isinstance(decision, dict):
            decision = {}
        decision_status = str(decision.get("decision_status", "")).strip().lower()
        recommendation = str(decision.get("recommendation", "")).strip()
        decision_ts_raw = str(decision.get("timestamp_utc", "")).strip()
        decision_ts = _parse_timestamp(decision_ts_raw)

        if processed_thoughts:
            total_with_processed_thoughts += 1
        if not decision_ts_raw:
            total_without_decisions += 1

        latest_processed = None
        latest_processed_date = None
        for thought in processed_thoughts:
            parsed = _parse_date(str(thought.get("parsed_date", "")))
            if parsed is None:
                continue
            if latest_processed_date is None or parsed > latest_processed_date:
                latest_processed_date = parsed
                latest_processed = thought

        reason = ""
        target_status = RECOMMENDATION_TARGET_STATUS.get(recommendation, "")
        if decision_status == "approved" and target_status and status != target_status:
            reason = "approved_pending_apply"
        elif latest_processed_date is not None:
            if decision_ts is None:
                reason = "no_decision_for_thought_enriched_claim"
            elif latest_processed_date > decision_ts.date():
                reason = "thought_newer_than_decision"

        if not reason:
            continue

        if reason != "approved_pending_apply":
            if governance_relevant_claim_ids and claim_id not in governance_relevant_claim_ids:
                continue

        item = {
            "claim_id": claim_id,
            "claim_type": str(claim.get("claim_type", "")).strip(),
            "status": str(claim.get("status", "")).strip(),
            "location": str(claim.get("location", "")).strip(),
            "reason": reason,
            "recommended_action": REASON_ACTION.get(reason, ""),
            "decision": {
                "decision_status": decision_status,
                "recommendation": recommendation,
                "timestamp_utc": decision_ts_raw,
            },
            "thought_signals": {
                "processed_source_count": len(processed_thoughts),
                "latest_processed_thought_file": str(latest_processed.get("file", "")) if latest_processed else "",
                "latest_processed_thought_date": latest_processed_date.isoformat()
                if latest_processed_date
                else "",
                "thought_sources": sorted({str(x.get("source_path", "")).strip() for x in processed_thoughts}),
            },
        }
        if reason == "approved_pending_apply":
            item["decision"]["target_status"] = target_status
        items.append(item)

    items.sort(
        key=lambda x: (
            REASON_PRIORITY.get(str(x.get("reason", "")), 99),
            str(x.get("claim_id", "")),
        )
    )

    reason_counts = Counter(str(item.get("reason", "")) for item in items)
    summary = {
        "items_total": len(items),
        "approved_pending_apply": int(reason_counts.get("approved_pending_apply", 0)),
        "thought_newer_than_decision": int(reason_counts.get("thought_newer_than_decision", 0)),
        "no_decision_for_thought_enriched_claim": int(
            reason_counts.get("no_decision_for_thought_enriched_claim", 0)
        ),
        "claims_with_processed_thought_sources": total_with_processed_thoughts,
        "claims_without_decision_timestamp": total_without_decisions,
        "governance_relevant_claim_ids": len(governance_relevant_claim_ids),
    }
    return items, summary


def _load_governance_relevant_claim_ids(path: Path) -> set[str]:
    loaded = _load_json(path, required=False)
    items_raw = loaded.get("items", [])
    if not isinstance(items_raw, list):
        return set()
    out: set[str] = set()
    for raw in items_raw:
        if not isinstance(raw, dict):
            continue
        claim_id = str(raw.get("claim_id", "")).strip()
        if claim_id:
            out.add(claim_id)
    return out


def _render_markdown(generated_at: str, items: list[dict[str, Any]], summary: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Thought Adjudication Bridge")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append(
        "This report surfaces claims where thought-intake progression likely needs adjudication refresh or direct"
    )
    lines.append("status-application follow-through.")
    lines.append("")
    lines.append("- total bridge items: " + f"`{summary.get('items_total', 0)}`")
    lines.append("- approved decisions pending apply: " + f"`{summary.get('approved_pending_apply', 0)}`")
    lines.append("- thought newer than latest decision: " + f"`{summary.get('thought_newer_than_decision', 0)}`")
    lines.append(
        "- thought-enriched claims lacking decision timestamp: "
        + f"`{summary.get('no_decision_for_thought_enriched_claim', 0)}`"
    )
    lines.append("")

    if not items:
        lines.append("No bridge candidates in this run.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Candidate Queue")
    lines.append("")
    lines.append("| claim_id | status | reason | latest_decision | latest_thought | action |")
    lines.append("|---|---|---|---|---|---|")
    for item in items:
        decision = item.get("decision", {})
        thought = item.get("thought_signals", {})
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item.get('claim_id', '')}`",
                    f"`{item.get('status', '')}`",
                    f"`{item.get('reason', '')}`",
                    f"`{decision.get('timestamp_utc', '')}`",
                    f"`{thought.get('latest_processed_thought_date', '')}`",
                    f"`{item.get('recommended_action', '')}`",
                ]
            )
            + " |"
        )
    lines.append("")

    lines.append("## Details")
    lines.append("")
    for item in items:
        lines.append(f"### {item.get('claim_id', '')}")
        lines.append(f"- claim_type: `{item.get('claim_type', '')}`")
        lines.append(f"- status: `{item.get('status', '')}`")
        lines.append(f"- reason: `{item.get('reason', '')}`")
        lines.append(f"- location: `{item.get('location', '')}`")
        lines.append(f"- recommended_action: `{item.get('recommended_action', '')}`")
        decision = item.get("decision", {})
        lines.append(
            "- decision: "
            + f"status=`{decision.get('decision_status', '')}` "
            + f"recommendation=`{decision.get('recommendation', '')}` "
            + f"timestamp=`{decision.get('timestamp_utc', '')}`"
        )
        target = str(decision.get("target_status", "")).strip()
        if target:
            lines.append(f"- target_status_if_applied: `{target}`")
        thought = item.get("thought_signals", {})
        lines.append(
            "- thought_signals: "
            + f"processed_source_count=`{thought.get('processed_source_count', 0)}` "
            + f"latest_file=`{thought.get('latest_processed_thought_file', '')}` "
            + f"latest_date=`{thought.get('latest_processed_thought_date', '')}`"
        )
        sources = thought.get("thought_sources", [])
        if isinstance(sources, list) and sources:
            lines.append("- thought_sources:")
            for src in sources:
                lines.append(f"  - `{src}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build bridge artifacts between thought-intake updates and adjudication lanes."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--claims-file",
        default="docs/claims/claims.yaml",
        help="Claim registry path (repo-relative).",
    )
    parser.add_argument(
        "--thought-sweep",
        default="docs/thoughts/thought_sweep.v1.json",
        help="Thought sweep JSON path (repo-relative).",
    )
    parser.add_argument(
        "--decision-state",
        default="evidence/decisions/decision_state.v1.json",
        help="Decision state JSON path (repo-relative).",
    )
    parser.add_argument(
        "--architecture-gap-register",
        default="evidence/planning/architecture_gap_register.v1.json",
        help="Architecture gap register JSON path (repo-relative). Used to scope governance-relevant claims.",
    )
    parser.add_argument(
        "--output-json",
        default="evidence/planning/thought_adjudication_bridge.v1.json",
        help="Bridge JSON output path (repo-relative).",
    )
    parser.add_argument(
        "--output-md",
        default="evidence/planning/THOUGHT_ADJUDICATION_BRIDGE.md",
        help="Bridge markdown output path (repo-relative).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    claims_path = (repo_root / args.claims_file).resolve()
    thought_sweep_path = (repo_root / args.thought_sweep).resolve()
    decision_state_path = (repo_root / args.decision_state).resolve()
    architecture_gap_register_path = (repo_root / args.architecture_gap_register).resolve()
    output_json_path = (repo_root / args.output_json).resolve()
    output_md_path = (repo_root / args.output_md).resolve()

    claims = _parse_claims_with_sources(claims_path)
    thought_sweep = _load_json(thought_sweep_path, required=True)
    decision_state = _load_json(decision_state_path, required=False)
    thought_map = _build_thought_record_map(thought_sweep)
    governance_relevant_claim_ids = _load_governance_relevant_claim_ids(architecture_gap_register_path)

    items, summary = _build_items(
        claims,
        thought_map,
        decision_state,
        governance_relevant_claim_ids,
    )
    generated_at = _now_utc()
    payload = {
        "schema_version": "thought_adjudication_bridge/v1",
        "generated_at_utc": generated_at,
        "inputs": {
            "claims_file": claims_path.as_posix(),
            "thought_sweep": thought_sweep_path.as_posix(),
            "decision_state": decision_state_path.as_posix(),
            "architecture_gap_register": architecture_gap_register_path.as_posix(),
        },
        "summary": summary,
        "items": items,
    }
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md_path.write_text(_render_markdown(generated_at, items, summary), encoding="utf-8")

    print(
        "Thought adjudication bridge built: "
        + f"items={summary.get('items_total', 0)}, "
        + f"approved_pending_apply={summary.get('approved_pending_apply', 0)}, "
        + f"thought_newer_than_decision={summary.get('thought_newer_than_decision', 0)}, "
        + "output_json="
        + output_json_path.as_posix()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
