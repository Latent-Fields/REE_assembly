#!/usr/bin/env python3
"""Trace-based architecture audit for REE interface wiring.

Inputs:
  - docs/architecture/interfaces.v1.yaml (JSON-compatible YAML)
  - docs/claims/interface_ownership.v1.yaml (JSON-compatible YAML)
  - docs/claims/claims.yaml
  - evidence/experiments/claim_evidence.v1.json

Outputs:
  - evidence/planning/architecture_trace_audit.v1.json
  - evidence/planning/ARCHITECTURE_TRACE_AUDIT.md
  - evidence/planning/claim_stub_suggestions.v1.json
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class ClaimRecord:
    claim_id: str
    claim_type: str
    status: str
    location: str
    depends_on: list[str]


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON: {path}: {exc}") from exc


def _load_json_compatible_yaml(path: Path, description: str) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing {description}: {path}") from exc

    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{path} must be JSON-compatible YAML (YAML 1.2 superset of JSON)."
        ) from exc

    if not isinstance(raw, dict):
        raise RuntimeError(f"{description} root must be an object: {path}")
    return raw


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        text = str(item).strip()
        if text:
            out.append(text)
    return out


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def _safe_id(token: str) -> str:
    cleaned = []
    for char in token.upper():
        if char.isalnum() or char in {"-", "_"}:
            cleaned.append(char)
        else:
            cleaned.append("-")
    value = "".join(cleaned).strip("-")
    return value or "UNKNOWN"


def _parse_inline_depends(raw: str) -> list[str]:
    text = raw.strip()
    if text == "[]":
        return []
    if text.startswith("[") and text.endswith("]"):
        inside = text[1:-1].strip()
        if not inside:
            return []
        parts = [part.strip() for part in inside.split(",")]
        return [part for part in parts if part]
    return []


def _parse_claim_registry(path: Path) -> dict[str, ClaimRecord]:
    """Parse docs/claims/claims.yaml with a lightweight deterministic parser."""
    claims: dict[str, ClaimRecord] = {}
    lines = path.read_text(encoding="utf-8").splitlines()

    current: dict[str, Any] | None = None
    in_depends = False

    def flush() -> None:
        nonlocal current
        if not current:
            return
        claim_id = str(current.get("id", "")).strip()
        if not claim_id:
            current = None
            return
        claims[claim_id] = ClaimRecord(
            claim_id=claim_id,
            claim_type=str(current.get("claim_type", "unknown")).strip() or "unknown",
            status=str(current.get("status", "unknown")).strip() or "unknown",
            location=str(current.get("location", "")).strip(),
            depends_on=list(current.get("depends_on", [])),
        )
        current = None

    for line in lines:
        if line.startswith("- id:"):
            flush()
            in_depends = False
            current = {
                "id": line.split(":", 1)[1].strip(),
                "claim_type": "unknown",
                "status": "unknown",
                "location": "",
                "depends_on": [],
            }
            continue

        if current is None:
            continue

        if line.startswith("  claim_type:"):
            current["claim_type"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue

        if line.startswith("  status:"):
            current["status"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue

        if line.startswith("  location:"):
            current["location"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue

        if line.startswith("  depends_on:"):
            in_depends = True
            raw = line.split(":", 1)[1].strip()
            current["depends_on"] = _parse_inline_depends(raw)
            continue

        if in_depends and line.startswith("    - "):
            dep_id = line[6:].strip()
            if dep_id:
                current["depends_on"].append(dep_id)
            continue

        if line.startswith("  ") and not line.startswith("    "):
            in_depends = False

    flush()
    return claims


def _claim_has_evidence(claim_id: str, matrix: dict[str, Any]) -> bool:
    claims = matrix.get("claims", {}) if isinstance(matrix, dict) else {}
    if not isinstance(claims, dict):
        return False
    entry = claims.get(claim_id)
    if not isinstance(entry, dict):
        return False
    source_counts = entry.get("source_counts", {})
    if not isinstance(source_counts, dict):
        return False
    exp_count = int(source_counts.get("experimental", 0))
    lit_count = int(source_counts.get("literature", 0))
    return (exp_count + lit_count) > 0


def _edge_owner_claims(edge: dict[str, Any], edge_ownership: dict[str, Any]) -> list[str]:
    owners = _string_list(edge.get("owner_claim_ids", []))
    ownership_extra = edge_ownership.get("owner_claim_ids", []) if isinstance(edge_ownership, dict) else []
    owners.extend(_string_list(ownership_extra))
    return _dedupe(owners)


def _node_owner_claims(node_id: str, ownership: dict[str, Any]) -> list[str]:
    node_map = ownership.get("nodes", {}) if isinstance(ownership, dict) else {}
    if not isinstance(node_map, dict):
        return []
    node_entry = node_map.get(node_id, {})
    if not isinstance(node_entry, dict):
        return []
    return _string_list(node_entry.get("owner_claim_ids", []))


def _open_section_owner_claims(open_id: str, open_section: dict[str, Any], ownership: dict[str, Any]) -> list[str]:
    owners = _string_list(open_section.get("owner_claim_ids", []))
    open_map = ownership.get("open_sections", {}) if isinstance(ownership, dict) else {}
    if isinstance(open_map, dict):
        open_entry = open_map.get(open_id, {})
        if isinstance(open_entry, dict):
            owners.extend(_string_list(open_entry.get("owner_claim_ids", [])))
    return _dedupe(owners)


def _has_dependency_relation(a: str, b: str, claims: dict[str, ClaimRecord]) -> bool:
    if a == b:
        return True
    claim_a = claims.get(a)
    claim_b = claims.get(b)
    if claim_a and b in claim_a.depends_on:
        return True
    if claim_b and a in claim_b.depends_on:
        return True
    return False


def _claim_location_for_suggestion(claim_ids: list[str], claims: dict[str, ClaimRecord], fallback: str) -> str:
    for claim_id in claim_ids:
        rec = claims.get(claim_id)
        if rec and rec.location:
            return rec.location.split("#", 1)[0]
    return fallback


def _build_stub_suggestions(
    claims: dict[str, ClaimRecord],
    issues: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    suggestions: list[dict[str, Any]] = []
    counter = 1

    def add_stub(
        *,
        claim_type: str,
        subject_hint: str,
        rationale: str,
        proposed_location: str,
        depends_on: list[str],
        source_issue_id: str,
    ) -> None:
        nonlocal counter
        suggestions.append(
            {
                "stub_id": f"STUB-{counter:04d}",
                "suggested_claim_type": claim_type,
                "subject_hint": subject_hint,
                "rationale": rationale,
                "proposed_location": proposed_location,
                "depends_on_candidates": _dedupe([dep for dep in depends_on if dep]),
                "source_issue_ids": [source_issue_id],
            }
        )
        counter += 1

    for item in issues.get("unowned_edges", []):
        edge_id = str(item.get("edge_id", ""))
        from_node = str(item.get("from_node", ""))
        to_node = str(item.get("to_node", ""))
        fallback_location = "docs/architecture/overview.md"
        add_stub(
            claim_type="architectural_commitment",
            subject_hint=f"interface.{from_node}_to_{to_node}".lower(),
            rationale="Edge has no claim owner and needs explicit architectural ownership.",
            proposed_location=fallback_location,
            depends_on=[],
            source_issue_id=str(item.get("issue_id", f"UNOWNED-{edge_id}")),
        )

    for item in issues.get("ambiguous_edges", []):
        edge_id = str(item.get("edge_id", ""))
        owners = _string_list(item.get("owner_claim_ids", []))
        add_stub(
            claim_type="open_question",
            subject_hint=f"interface.{edge_id}.ambiguity".lower(),
            rationale="Ambiguous edge fields need explicit resolution criteria.",
            proposed_location=_claim_location_for_suggestion(owners, claims, "docs/architecture/overview.md"),
            depends_on=owners,
            source_issue_id=str(item.get("issue_id", f"AMBIG-{edge_id}")),
        )

    for item in issues.get("open_sections_unowned", []):
        section_id = str(item.get("open_section_id", ""))
        doc = str(item.get("doc", "docs/architecture/overview.md"))
        add_stub(
            claim_type="open_question",
            subject_hint=f"open_section.{section_id}.ownership".lower(),
            rationale="Open architecture section is not linked to any claim owner.",
            proposed_location=doc,
            depends_on=[],
            source_issue_id=str(item.get("issue_id", f"OPEN-{section_id}")),
        )

    for item in issues.get("trace_breaks", []):
        node_id = str(item.get("node_id", ""))
        owners = _string_list(item.get("owner_claim_ids", []))
        add_stub(
            claim_type="mechanism_hypothesis",
            subject_hint=f"trace.continuation.{node_id}".lower(),
            rationale="Traced node has no non-terminal continuation edge.",
            proposed_location=_claim_location_for_suggestion(owners, claims, "docs/architecture/overview.md"),
            depends_on=owners,
            source_issue_id=str(item.get("issue_id", f"TRACE-{node_id}")),
        )

    return suggestions


def _write_markdown_report(path: Path, audit: dict[str, Any], suggestions: list[dict[str, Any]]) -> None:
    summary = audit.get("summary", {}) if isinstance(audit, dict) else {}
    trace = audit.get("trace", {}) if isinstance(audit, dict) else {}
    issues = audit.get("issues", {}) if isinstance(audit, dict) else {}

    lines: list[str] = []
    lines.append("# Architecture Trace Audit")
    lines.append("")
    lines.append(f"Generated: `{audit.get('generated_at_utc', '')}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Nodes traced from sensory roots: {trace.get('reachable_node_count', 0)}/{trace.get('total_nodes', 0)}")
    lines.append(f"- Edges traversed: {trace.get('traversed_edge_count', 0)}/{trace.get('total_edges', 0)}")
    lines.append(f"- Unowned edges: {summary.get('unowned_edges', 0)}")
    lines.append(f"- Ambiguous edges: {summary.get('ambiguous_edges', 0)}")
    lines.append(f"- Trace breaks: {summary.get('trace_breaks', 0)}")
    lines.append(f"- Open sections without owner claims: {summary.get('open_sections_unowned', 0)}")
    lines.append(f"- Suggested claim stubs: {len(suggestions)}")
    lines.append("")

    def render_issue_block(title: str, key: str, fields: list[str]) -> None:
        items = issues.get(key, []) if isinstance(issues, dict) else []
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("- _none_")
            lines.append("")
            return
        for item in items[:50]:
            issue_id = str(item.get("issue_id", ""))
            line = f"- `{issue_id}`"
            detail_parts: list[str] = []
            for field in fields:
                value = item.get(field)
                if isinstance(value, list):
                    if value:
                        detail_parts.append(f"{field}={', '.join(str(v) for v in value)}")
                elif value not in (None, "", []):
                    detail_parts.append(f"{field}={value}")
            if detail_parts:
                line += " " + "; ".join(detail_parts)
            lines.append(line)
        lines.append("")

    render_issue_block("Missing Dependency Targets", "missing_claim_dependency_targets", ["claim_id", "missing_dep_id"])
    render_issue_block("Dependency Link Gaps", "dependency_link_gaps", ["edge_id", "source_claim_ids", "target_claim_ids"])
    render_issue_block("Unowned Edges", "unowned_edges", ["edge_id", "from_node", "to_node"])
    render_issue_block("Ambiguous Edges", "ambiguous_edges", ["edge_id", "unknown_fields", "linked_open_questions"])
    render_issue_block("Trace Breaks", "trace_breaks", ["node_id", "owner_claim_ids"])
    render_issue_block("Open Sections Without Ownership", "open_sections_unowned", ["open_section_id", "doc"])
    render_issue_block("Owned Edges Without Evidence", "owned_edges_without_evidence", ["edge_id", "owner_claim_ids"])

    lines.append("## Stub Suggestions")
    lines.append("")
    if not suggestions:
        lines.append("- _none_")
    else:
        for item in suggestions[:100]:
            lines.append(
                "- "
                + f"`{item.get('stub_id', '')}` type=`{item.get('suggested_claim_type', '')}` "
                + f"subject=`{item.get('subject_hint', '')}` location=`{item.get('proposed_location', '')}`"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run architecture trace audit from explicit interface graph.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--interfaces",
        type=Path,
        default=None,
        help="Override path to interfaces.v1.yaml.",
    )
    parser.add_argument(
        "--ownership",
        type=Path,
        default=None,
        help="Override path to interface_ownership.v1.yaml.",
    )
    parser.add_argument(
        "--audit-json",
        type=Path,
        default=None,
        help="Output path for architecture_trace_audit.v1.json.",
    )
    parser.add_argument(
        "--audit-md",
        type=Path,
        default=None,
        help="Output path for ARCHITECTURE_TRACE_AUDIT.md.",
    )
    parser.add_argument(
        "--stub-json",
        type=Path,
        default=None,
        help="Output path for claim_stub_suggestions.v1.json.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    planning_root = repo_root / "evidence/planning"

    interfaces_path = args.interfaces.resolve() if args.interfaces else repo_root / "docs/architecture/interfaces.v1.yaml"
    ownership_path = args.ownership.resolve() if args.ownership else repo_root / "docs/claims/interface_ownership.v1.yaml"
    claim_registry_path = repo_root / "docs/claims/claims.yaml"
    matrix_path = repo_root / "evidence/experiments/claim_evidence.v1.json"

    audit_json_path = args.audit_json.resolve() if args.audit_json else planning_root / "architecture_trace_audit.v1.json"
    audit_md_path = args.audit_md.resolve() if args.audit_md else planning_root / "ARCHITECTURE_TRACE_AUDIT.md"
    stub_json_path = args.stub_json.resolve() if args.stub_json else planning_root / "claim_stub_suggestions.v1.json"

    interfaces = _load_json_compatible_yaml(interfaces_path, "interface graph")
    ownership = _load_json_compatible_yaml(ownership_path, "interface ownership")
    claims = _parse_claim_registry(claim_registry_path)
    matrix = _load_json(matrix_path)

    nodes_raw = interfaces.get("nodes", [])
    edges_raw = interfaces.get("edges", [])
    open_sections_raw = interfaces.get("open_sections", [])

    nodes: dict[str, dict[str, Any]] = {}
    for node in nodes_raw if isinstance(nodes_raw, list) else []:
        if not isinstance(node, dict):
            continue
        node_id = str(node.get("id", "")).strip()
        if not node_id:
            continue
        nodes[node_id] = node

    trace_roots = [r for r in _string_list(interfaces.get("trace_roots", []))]
    terminal_nodes = set(_string_list(interfaces.get("terminal_nodes", [])))

    issues: dict[str, list[dict[str, Any]]] = defaultdict(list)

    # Claim dependency validity checks.
    for claim_id, claim in sorted(claims.items()):
        for dep_id in claim.depends_on:
            if dep_id not in claims:
                issue_id = f"ISS-MISSING-DEP-{_safe_id(claim_id)}-{_safe_id(dep_id)}"
                issues["missing_claim_dependency_targets"].append(
                    {
                        "issue_id": issue_id,
                        "claim_id": claim_id,
                        "missing_dep_id": dep_id,
                    }
                )

    adjacency: dict[str, list[dict[str, Any]]] = defaultdict(list)
    traversable_edges: dict[str, dict[str, Any]] = {}

    edge_ownership_map = ownership.get("edges", {}) if isinstance(ownership.get("edges"), dict) else {}

    for edge in edges_raw if isinstance(edges_raw, list) else []:
        if not isinstance(edge, dict):
            continue
        edge_id = str(edge.get("id", "")).strip()
        if not edge_id:
            continue

        from_block = edge.get("from", {})
        to_block = edge.get("to", {})
        from_node = str(from_block.get("node", "")).strip() if isinstance(from_block, dict) else ""
        to_node = str(to_block.get("node", "")).strip() if isinstance(to_block, dict) else ""

        if from_node not in nodes or to_node not in nodes:
            issue_id = f"ISS-EDGE-REF-{_safe_id(edge_id)}"
            issues["edge_reference_errors"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "from_node": from_node,
                    "to_node": to_node,
                    "reason": "edge references unknown node",
                }
            )
            continue

        operation = str(edge.get("operation", "")).strip()
        stage = str(edge.get("stage", "")).strip()
        signal = str(edge.get("signal", "")).strip()
        status = str(edge.get("status", "defined")).strip().lower() or "defined"

        owners = _edge_owner_claims(edge, edge_ownership_map.get(edge_id, {}))
        unknown_owner_claims = [claim_id for claim_id in owners if claim_id not in claims]

        if unknown_owner_claims:
            issue_id = f"ISS-UNKNOWN-OWNER-{_safe_id(edge_id)}"
            issues["unknown_owner_claims"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "owner_claim_ids": owners,
                    "unknown_owner_claim_ids": unknown_owner_claims,
                }
            )

        if not owners:
            issue_id = f"ISS-UNOWNED-EDGE-{_safe_id(edge_id)}"
            issues["unowned_edges"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "from_node": from_node,
                    "to_node": to_node,
                }
            )

        if not operation or not signal or not stage:
            issue_id = f"ISS-UNDEFINED-FIELDS-{_safe_id(edge_id)}"
            issues["undefined_edges"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "missing_fields": [
                        field_name
                        for field_name, value in {
                            "operation": operation,
                            "signal": signal,
                            "stage": stage,
                        }.items()
                        if not value
                    ],
                }
            )

        if status in {"ambiguous", "candidate"}:
            ambiguity = edge.get("ambiguity", {}) if isinstance(edge.get("ambiguity"), dict) else {}
            issue_id = f"ISS-AMBIGUOUS-EDGE-{_safe_id(edge_id)}"
            issues["ambiguous_edges"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "status": status,
                    "owner_claim_ids": owners,
                    "unknown_fields": _string_list(ambiguity.get("unknown_fields", [])),
                    "linked_open_questions": _string_list(ambiguity.get("linked_open_questions", [])),
                }
            )

        source_claim_ids = _node_owner_claims(from_node, ownership)
        target_claim_ids = _node_owner_claims(to_node, ownership)
        if source_claim_ids and target_claim_ids:
            related = False
            for source_claim in source_claim_ids:
                for target_claim in target_claim_ids:
                    if _has_dependency_relation(source_claim, target_claim, claims):
                        related = True
                        break
                if related:
                    break
            if not related:
                issue_id = f"ISS-DEP-LINK-GAP-{_safe_id(edge_id)}"
                issues["dependency_link_gaps"].append(
                    {
                        "issue_id": issue_id,
                        "edge_id": edge_id,
                        "source_claim_ids": source_claim_ids,
                        "target_claim_ids": target_claim_ids,
                    }
                )

        if owners and not any(_claim_has_evidence(claim_id, matrix) for claim_id in owners if claim_id in claims):
            issue_id = f"ISS-NO-EVIDENCE-EDGE-{_safe_id(edge_id)}"
            issues["owned_edges_without_evidence"].append(
                {
                    "issue_id": issue_id,
                    "edge_id": edge_id,
                    "owner_claim_ids": owners,
                }
            )

        normalized_edge = {
            "id": edge_id,
            "from_node": from_node,
            "to_node": to_node,
            "operation": operation,
            "stage": stage,
            "signal": signal,
            "status": status,
            "owner_claim_ids": owners,
        }
        traversable_edges[edge_id] = normalized_edge
        adjacency[from_node].append(normalized_edge)

    # Node ownership checks.
    for node_id in sorted(nodes.keys()):
        owners = _node_owner_claims(node_id, ownership)
        if not owners:
            issue_id = f"ISS-UNOWNED-NODE-{_safe_id(node_id)}"
            issues["unowned_nodes"].append(
                {
                    "issue_id": issue_id,
                    "node_id": node_id,
                }
            )
            continue

        unknown = [claim_id for claim_id in owners if claim_id not in claims]
        if unknown:
            issue_id = f"ISS-UNKNOWN-NODE-OWNER-{_safe_id(node_id)}"
            issues["unknown_owner_claims"].append(
                {
                    "issue_id": issue_id,
                    "node_id": node_id,
                    "owner_claim_ids": owners,
                    "unknown_owner_claim_ids": unknown,
                }
            )

    # Open section ownership checks.
    for open_section in open_sections_raw if isinstance(open_sections_raw, list) else []:
        if not isinstance(open_section, dict):
            continue
        open_id = str(open_section.get("id", "")).strip()
        if not open_id:
            continue
        owners = _open_section_owner_claims(open_id, open_section, ownership)
        if not owners:
            issue_id = f"ISS-OPEN-UNOWNED-{_safe_id(open_id)}"
            issues["open_sections_unowned"].append(
                {
                    "issue_id": issue_id,
                    "open_section_id": open_id,
                    "doc": str(open_section.get("doc", "")).strip(),
                    "section": str(open_section.get("section", "")).strip(),
                }
            )
            continue

        unknown = [claim_id for claim_id in owners if claim_id not in claims]
        if unknown:
            issue_id = f"ISS-OPEN-UNKNOWN-OWNER-{_safe_id(open_id)}"
            issues["unknown_owner_claims"].append(
                {
                    "issue_id": issue_id,
                    "open_section_id": open_id,
                    "owner_claim_ids": owners,
                    "unknown_owner_claim_ids": unknown,
                }
            )

    # Trace from sensory roots.
    missing_roots = [root for root in trace_roots if root not in nodes]
    for root in missing_roots:
        issue_id = f"ISS-MISSING-ROOT-{_safe_id(root)}"
        issues["missing_trace_roots"].append(
            {
                "issue_id": issue_id,
                "node_id": root,
            }
        )

    visited_nodes: set[str] = set()
    traversed_edge_ids: set[str] = set()
    queue: deque[str] = deque([root for root in trace_roots if root in nodes])

    while queue:
        node_id = queue.popleft()
        if node_id in visited_nodes:
            continue
        visited_nodes.add(node_id)

        for edge in adjacency.get(node_id, []):
            traversed_edge_ids.add(edge["id"])
            to_node = edge["to_node"]
            if to_node not in visited_nodes:
                queue.append(to_node)

    for node_id in sorted(visited_nodes):
        if node_id in terminal_nodes:
            continue
        outgoing = adjacency.get(node_id, [])
        if not outgoing:
            issue_id = f"ISS-TRACE-BREAK-{_safe_id(node_id)}"
            issues["trace_breaks"].append(
                {
                    "issue_id": issue_id,
                    "node_id": node_id,
                    "owner_claim_ids": _node_owner_claims(node_id, ownership),
                }
            )

    total_nodes = len(nodes)
    total_edges = len(traversable_edges)
    unreachable_nodes = sorted(set(nodes.keys()) - visited_nodes)
    untraversed_edges = sorted(set(traversable_edges.keys()) - traversed_edge_ids)

    trace_summary = {
        "roots": trace_roots,
        "terminal_nodes": sorted(terminal_nodes),
        "missing_roots": missing_roots,
        "total_nodes": total_nodes,
        "reachable_node_count": len(visited_nodes),
        "reachable_nodes": sorted(visited_nodes),
        "unreachable_nodes": unreachable_nodes,
        "node_coverage_ratio": round((len(visited_nodes) / float(total_nodes)) if total_nodes else 0.0, 3),
        "total_edges": total_edges,
        "traversed_edge_count": len(traversed_edge_ids),
        "traversed_edges": sorted(traversed_edge_ids),
        "untraversed_edges": untraversed_edges,
        "edge_coverage_ratio": round((len(traversed_edge_ids) / float(total_edges)) if total_edges else 0.0, 3),
    }

    # Normalize issue map into stable sorted lists.
    normalized_issues: dict[str, list[dict[str, Any]]] = {}
    for key in sorted(issues.keys()):
        items = issues[key]
        items.sort(key=lambda item: str(item.get("issue_id", "")))
        normalized_issues[key] = items

    suggestions = _build_stub_suggestions(claims, normalized_issues)
    suggestions_doc = {
        "schema_version": "claim_stub_suggestions/v1",
        "generated_at_utc": _now_utc(),
        "source_audit": "evidence/planning/architecture_trace_audit.v1.json",
        "items": suggestions,
    }

    summary = {
        "issue_count": sum(len(items) for items in normalized_issues.values()),
        "missing_claim_dependency_targets": len(normalized_issues.get("missing_claim_dependency_targets", [])),
        "dependency_link_gaps": len(normalized_issues.get("dependency_link_gaps", [])),
        "unowned_edges": len(normalized_issues.get("unowned_edges", [])),
        "unowned_nodes": len(normalized_issues.get("unowned_nodes", [])),
        "ambiguous_edges": len(normalized_issues.get("ambiguous_edges", [])),
        "trace_breaks": len(normalized_issues.get("trace_breaks", [])),
        "open_sections_unowned": len(normalized_issues.get("open_sections_unowned", [])),
        "owned_edges_without_evidence": len(normalized_issues.get("owned_edges_without_evidence", [])),
        "suggested_claim_stubs": len(suggestions),
    }

    audit = {
        "schema_version": "architecture_trace_audit/v1",
        "generated_at_utc": _now_utc(),
        "inputs": {
            "interfaces": interfaces_path.as_posix(),
            "ownership": ownership_path.as_posix(),
            "claim_registry": claim_registry_path.as_posix(),
            "claim_evidence": matrix_path.as_posix(),
        },
        "trace": trace_summary,
        "summary": summary,
        "issues": normalized_issues,
    }

    audit_json_path.parent.mkdir(parents=True, exist_ok=True)
    audit_json_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    stub_json_path.parent.mkdir(parents=True, exist_ok=True)
    stub_json_path.write_text(json.dumps(suggestions_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    _write_markdown_report(audit_md_path, audit, suggestions)

    print(
        "Architecture trace audit complete: "
        + f"nodes={trace_summary['reachable_node_count']}/{trace_summary['total_nodes']}, "
        + f"edges={trace_summary['traversed_edge_count']}/{trace_summary['total_edges']}, "
        + f"issues={summary['issue_count']}, "
        + f"stubs={summary['suggested_claim_stubs']}."
    )
    print(f"Audit JSON: {audit_json_path.as_posix()}")
    print(f"Audit MD: {audit_md_path.as_posix()}")
    print(f"Stub suggestions: {stub_json_path.as_posix()}")


if __name__ == "__main__":
    main()
