#!/usr/bin/env python3
"""Build a convergence intake queue from promotion packet JSON files."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from glob import glob
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

PLACEHOLDER_EVIDENCE_TOKENS = ("todo", "needs evidence", "example.org")


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _format_error_path(path_parts: list[object]) -> str:
    if not path_parts:
        return "<root>"
    return ".".join(str(x) for x in path_parts)


def _resolve(repo_root: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return repo_root / path


def _relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _glob_paths(repo_root: Path, pattern: str) -> list[Path]:
    full_pattern = pattern if Path(pattern).is_absolute() else (repo_root / pattern).as_posix()
    return [Path(p) for p in sorted(glob(full_pattern))]


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        token = str(item).strip()
        if token and token not in out:
            out.append(token)
    return out


def _contains_placeholder_evidence_token(text: str) -> bool:
    lowered = text.lower()
    return any(token in lowered for token in PLACEHOLDER_EVIDENCE_TOKENS)


def _placeholder_evidence_hits(packet: dict[str, Any]) -> list[str]:
    hits: list[str] = []
    source = packet.get("source", {}) if isinstance(packet.get("source"), dict) else {}
    evidence = packet.get("evidence_summary", {}) if isinstance(packet.get("evidence_summary"), dict) else {}
    deltas = packet.get("deltas", []) if isinstance(packet.get("deltas"), list) else []
    falsification = packet.get("falsification", {}) if isinstance(packet.get("falsification"), dict) else {}

    for link in _string_list(source.get("primary_links")):
        if _contains_placeholder_evidence_token(link):
            hits.append(f"source.primary_links: {link}")

    evidence_notes = str(evidence.get("notes", "")).strip()
    if evidence_notes and _contains_placeholder_evidence_token(evidence_notes):
        hits.append("evidence_summary.notes")

    for index, delta in enumerate(deltas):
        if not isinstance(delta, dict):
            continue
        for link in _string_list(delta.get("evidence_links")):
            if _contains_placeholder_evidence_token(link):
                hits.append(f"deltas[{index}].evidence_links: {link}")

    for ref in _string_list(falsification.get("test_plan_refs")):
        if _contains_placeholder_evidence_token(ref):
            hits.append(f"falsification.test_plan_refs: {ref}")

    return hits


def _packet_gate_evaluation(packet: dict[str, Any]) -> tuple[bool, list[str], bool, list[str]]:
    evidence = packet.get("evidence_summary", {})
    gates = packet.get("promotion_gates", {})
    touchpoints = packet.get("ree_touchpoints", {})
    controls = packet.get("governance_controls", {})
    falsification = packet.get("falsification", {})
    decisions = packet.get("decisions", {})
    if not isinstance(evidence, dict) or not isinstance(gates, dict):
        return False, ["evidence_or_gate_structure_missing"], False, []
    if not isinstance(touchpoints, dict):
        touchpoints = {}
    if not isinstance(controls, dict):
        controls = {}
    if not isinstance(falsification, dict):
        falsification = {}
    if not isinstance(decisions, dict):
        decisions = {}

    failures: list[str] = []

    if not bool(evidence.get("primary_sources_verified")):
        failures.append("primary_sources_verified=false")
    if not bool(gates.get("separation_tests_defined")):
        failures.append("separation_tests_defined=false")
    if not bool(gates.get("falsifiability_defined")):
        failures.append("falsifiability_defined=false")
    if not bool(controls.get("conflict_review_completed")):
        failures.append("conflict_review_completed=false")

    claim_ids = _string_list(touchpoints.get("claim_ids"))
    if not claim_ids:
        failures.append("touchpoints.claim_ids_empty")

    falsification_disconfirming = _string_list(falsification.get("could_be_wrong_if"))
    falsification_test_refs = _string_list(falsification.get("test_plan_refs"))
    if not str(falsification.get("claim_under_test", "")).strip():
        failures.append("falsification.claim_under_test_missing")
    if not falsification_disconfirming:
        failures.append("falsification.could_be_wrong_if_empty")
    if not falsification_test_refs:
        failures.append("falsification.test_plan_refs_empty")

    blast_radius = str(controls.get("blast_radius", "")).strip()
    rollback_conditions = _string_list(controls.get("rollback_conditions"))
    try:
        probation_window_days = int(controls.get("probation_window_days", 0))
    except (TypeError, ValueError):
        probation_window_days = 0
        failures.append("governance_controls.probation_window_days_invalid")

    if blast_radius in {"interface", "architecture"}:
        if probation_window_days < 1:
            failures.append("non_lexical_requires_probation_window_days>=1")
        if not rollback_conditions:
            failures.append("non_lexical_requires_rollback_conditions")
        if not bool(gates.get("rollback_plan_defined")):
            failures.append("non_lexical_requires_rollback_plan_defined=true")

    if blast_radius == "architecture":
        if str(evidence.get("evidence_status", "")).strip() != "sufficient":
            failures.append("architecture_requires_evidence_status=sufficient")
        if not bool(decisions.get("anti_lock_in_review_required")):
            failures.append("architecture_requires_anti_lock_in_review")
        if probation_window_days < 7:
            failures.append("architecture_requires_probation_window_days>=7")

    placeholder_hits = _placeholder_evidence_hits(packet)
    placeholder_found = len(placeholder_hits) > 0
    if placeholder_found:
        failures.append("placeholder_evidence_detected")

    return len(failures) == 0, failures, placeholder_found, placeholder_hits


def _validate_packet(
    path: Path,
    validator: Draft202012Validator,
) -> tuple[bool, list[str], dict[str, Any]]:
    try:
        payload = _load_json(path)
    except json.JSONDecodeError as exc:
        return False, [f"<root>: JSON parse error: {exc}"], {}

    if not isinstance(payload, dict):
        return False, ["<root>: top-level JSON value must be an object"], {}

    errors = sorted(validator.iter_errors(payload), key=lambda e: list(e.path))
    if not errors:
        return True, [], payload

    formatted = [f"{_format_error_path(list(err.path))}: {err.message}" for err in errors]
    return False, formatted, payload


def _build_valid_item(packet: dict[str, Any], packet_path: Path, repo_root: Path) -> dict[str, Any]:
    source = packet.get("source", {}) if isinstance(packet.get("source"), dict) else {}
    evidence = packet.get("evidence_summary", {}) if isinstance(packet.get("evidence_summary"), dict) else {}
    touchpoints = packet.get("ree_touchpoints", {}) if isinstance(packet.get("ree_touchpoints"), dict) else {}
    gates = packet.get("promotion_gates", {}) if isinstance(packet.get("promotion_gates"), dict) else {}
    falsification = packet.get("falsification", {}) if isinstance(packet.get("falsification"), dict) else {}
    controls = packet.get("governance_controls", {}) if isinstance(packet.get("governance_controls"), dict) else {}
    deltas = packet.get("deltas", []) if isinstance(packet.get("deltas"), list) else []

    delta_scopes = []
    for delta in deltas:
        if not isinstance(delta, dict):
            continue
        scope = str(delta.get("target_scope", "")).strip()
        if scope:
            delta_scopes.append(scope)

    impact_areas = _string_list(touchpoints.get("impact_areas")) + delta_scopes
    impact_areas = _string_list(impact_areas)
    gate_ready, gate_failures, placeholder_evidence_found, placeholder_evidence_hits = _packet_gate_evaluation(packet)

    return {
        "packet_id": str(packet.get("packet_id", "")).strip(),
        "status": str(packet.get("status", "proposed")).strip(),
        "blast_radius": str(controls.get("blast_radius", "")).strip(),
        "source_repo": str(source.get("repo_name", "")).strip(),
        "source_system_id": str(source.get("source_system_id", "")).strip(),
        "snapshot_ref": str(source.get("snapshot_ref", "")).strip(),
        "intake_path": str(source.get("intake_path", "")).strip(),
        "evidence_status": str(evidence.get("evidence_status", "")).strip(),
        "primary_sources_verified": bool(evidence.get("primary_sources_verified", False)),
        "falsification_status": str(falsification.get("status", "")).strip(),
        "conflict_review_completed": bool(controls.get("conflict_review_completed", False)),
        "probation_window_days": int(controls.get("probation_window_days", 0) or 0),
        "gate_ready": gate_ready,
        "gate_failures": gate_failures,
        "placeholder_evidence_found": placeholder_evidence_found,
        "placeholder_evidence_hits": placeholder_evidence_hits,
        "owner": str(gates.get("owner", "")).strip(),
        "decision_due_utc": str(gates.get("decision_due_utc", "")).strip(),
        "delta_count": len(deltas),
        "impact_areas": impact_areas,
        "claim_ids": _string_list(touchpoints.get("claim_ids")),
        "packet_path": _relative(packet_path, repo_root),
        "validation_errors": [],
    }


def _render_markdown(queue: dict[str, Any], output_path: Path) -> None:
    summary = queue.get("summary", {}) if isinstance(queue.get("summary"), dict) else {}
    items = queue.get("items", []) if isinstance(queue.get("items"), list) else []
    invalid_items = queue.get("invalid_items", []) if isinstance(queue.get("invalid_items"), list) else []

    lines: list[str] = []
    lines.append("# Convergence Intake Queue")
    lines.append("")
    lines.append(f"Generated: `{queue.get('generated_at_utc', '')}`")
    lines.append(f"Source glob: `{queue.get('source_glob', '')}`")
    lines.append(f"Schema: `{queue.get('schema_path', '')}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total packets: `{summary.get('total_packets', 0)}`")
    lines.append(f"- Valid packets: `{summary.get('valid_packets', 0)}`")
    lines.append(f"- Invalid packets: `{summary.get('invalid_packets', 0)}`")
    lines.append(f"- Gate-ready packets: `{summary.get('gate_ready_packets', 0)}`")
    lines.append(f"- Packets with gate failures: `{summary.get('gate_failure_packets', 0)}`")
    lines.append(f"- Packets with placeholder evidence: `{summary.get('placeholder_evidence_packets', 0)}`")
    lines.append("")

    by_status = summary.get("by_status", {})
    if isinstance(by_status, dict) and by_status:
        lines.append("### Status Counts")
        lines.append("")
        for status_key in sorted(by_status):
            lines.append(f"- `{status_key}`: `{by_status[status_key]}`")
        lines.append("")

    by_impact = summary.get("by_impact_area", {})
    if isinstance(by_impact, dict) and by_impact:
        lines.append("### Impact-Area Counts")
        lines.append("")
        for area_key in sorted(by_impact):
            lines.append(f"- `{area_key}`: `{by_impact[area_key]}`")
        lines.append("")

    by_blast = summary.get("by_blast_radius", {})
    if isinstance(by_blast, dict) and by_blast:
        lines.append("### Blast-Radius Counts")
        lines.append("")
        for radius_key in sorted(by_blast):
            lines.append(f"- `{radius_key}`: `{by_blast[radius_key]}`")
        lines.append("")

    lines.append("## Valid Packets")
    lines.append("")
    lines.append("| Packet | Status | Blast | Source | Evidence | Gate Ready | Gate Failures | Deltas | Claims | Owner | Due | Path |")
    lines.append("|---|---|---|---|---|---|---:|---:|---:|---|---|---|")
    if items:
        for item in items:
            lines.append(
                "| "
                f"`{item.get('packet_id','')}` | "
                f"`{item.get('status','')}` | "
                f"`{item.get('blast_radius','')}` | "
                f"`{item.get('source_system_id','')}` | "
                f"`{item.get('evidence_status','')}` | "
                f"`{str(item.get('gate_ready', False)).lower()}` | "
                f"{len(_string_list(item.get('gate_failures', [])))} | "
                f"{item.get('delta_count', 0)} | "
                f"{len(item.get('claim_ids', []))} | "
                f"`{item.get('owner','')}` | "
                f"`{item.get('decision_due_utc','')}` | "
                f"`{item.get('packet_path','')}` |"
            )
    else:
        lines.append("| _none_ | - | - | - | - | - | - | - | - | - | - | - |")
    lines.append("")

    gate_failure_items = [
        item
        for item in items
        if _string_list(item.get("gate_failures"))
    ]
    if gate_failure_items:
        lines.append("### Gate Failure Details")
        lines.append("")
        for item in gate_failure_items:
            packet_id = str(item.get("packet_id", "")).strip()
            lines.append(f"- `{packet_id}`")
            for reason in _string_list(item.get("gate_failures")):
                lines.append(f"  - {reason}")
            if bool(item.get("placeholder_evidence_found", False)):
                for hit in _string_list(item.get("placeholder_evidence_hits"))[:10]:
                    lines.append(f"  - placeholder_hit: {hit}")
    lines.append("")

    lines.append("## Invalid Packets")
    lines.append("")
    if invalid_items:
        for item in invalid_items:
            lines.append(f"- `{item.get('packet_path', '')}`")
            for err in item.get("validation_errors", []):
                lines.append(f"  - {err}")
    else:
        lines.append("- None")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schema",
        default="evidence/planning/schemas/v1/convergence_promotion_packet.schema.json",
        help="Schema path (absolute or repo-relative).",
    )
    parser.add_argument(
        "--input-glob",
        default="evidence/planning/convergence_packets/inbox/*.json",
        help="Glob pattern for packet JSON files (absolute or repo-relative).",
    )
    parser.add_argument(
        "--output-json",
        default="evidence/planning/convergence_intake_queue.v1.json",
        help="Output queue JSON path (absolute or repo-relative).",
    )
    parser.add_argument(
        "--output-md",
        default="evidence/planning/CONVERGENCE_INTAKE_QUEUE.md",
        help="Output markdown report path (absolute or repo-relative).",
    )
    parser.add_argument(
        "--fail-on-invalid",
        action="store_true",
        help="Return non-zero if any packet is invalid.",
    )
    args = parser.parse_args()

    schema_path = _resolve(repo_root, args.schema)
    output_json_path = _resolve(repo_root, args.output_json)
    output_md_path = _resolve(repo_root, args.output_md)

    if not schema_path.exists():
        raise SystemExit(f"Schema not found: {schema_path}")

    schema = _load_json(schema_path)
    validator = Draft202012Validator(schema)

    packet_paths = _glob_paths(repo_root, args.input_glob)
    valid_items: list[dict[str, Any]] = []
    invalid_items: list[dict[str, Any]] = []

    for packet_path in packet_paths:
        is_valid, validation_errors, payload = _validate_packet(packet_path, validator)
        if not is_valid:
            invalid_items.append(
                {
                    "packet_path": _relative(packet_path, repo_root),
                    "validation_errors": validation_errors,
                }
            )
            continue
        valid_items.append(_build_valid_item(payload, packet_path, repo_root))

    valid_items.sort(key=lambda x: (str(x.get("status", "")), str(x.get("packet_id", ""))))

    status_counts: Counter[str] = Counter()
    impact_counts: Counter[str] = Counter()
    blast_counts: Counter[str] = Counter()
    gate_ready_count = 0
    gate_failure_count = 0
    placeholder_evidence_count = 0
    for item in valid_items:
        status_counts.update([str(item.get("status", "")).strip() or "unknown"])
        impact_counts.update(_string_list(item.get("impact_areas")))
        blast_counts.update([str(item.get("blast_radius", "")).strip() or "unknown"])
        if bool(item.get("gate_ready", False)):
            gate_ready_count += 1
        if _string_list(item.get("gate_failures")):
            gate_failure_count += 1
        if bool(item.get("placeholder_evidence_found", False)):
            placeholder_evidence_count += 1

    queue = {
        "schema_version": "convergence_intake_queue/v1",
        "generated_at_utc": _now_utc(),
        "source_glob": args.input_glob,
        "schema_path": _relative(schema_path, repo_root),
        "summary": {
            "total_packets": len(packet_paths),
            "valid_packets": len(valid_items),
            "invalid_packets": len(invalid_items),
            "gate_ready_packets": gate_ready_count,
            "gate_failure_packets": gate_failure_count,
            "placeholder_evidence_packets": placeholder_evidence_count,
            "by_status": dict(sorted(status_counts.items())),
            "by_impact_area": dict(sorted(impact_counts.items())),
            "by_blast_radius": dict(sorted(blast_counts.items())),
        },
        "items": valid_items,
        "invalid_items": invalid_items,
    }

    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.write_text(json.dumps(queue, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _render_markdown(queue, output_md_path)

    print(f"Wrote: {output_json_path}")
    print(f"Wrote: {output_md_path}")
    print(
        "Queue summary: "
        f"total={len(packet_paths)} valid={len(valid_items)} invalid={len(invalid_items)}"
    )

    if args.fail_on_invalid and invalid_items:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
