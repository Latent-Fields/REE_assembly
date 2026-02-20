#!/usr/bin/env python3
"""Build human-readable decision briefs for all human governance lanes.

This script generates per-claim decision briefs with mechanism context,
architecture role, metric definitions, and decision history so human
decision checkpoints are readable without reverse-engineering raw indexes.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _strip_ticks(text: str) -> str:
    return text.strip().strip("`")


def _load_json_file(path: Path, warnings: list[str], *, required: bool = True) -> dict[str, Any]:
    if not path.exists():
        if required:
            warnings.append(f"Missing JSON file: {path.as_posix()}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError as exc:
        warnings.append(f"Invalid JSON ({path.as_posix()}): {exc}")
        return {}


def _load_jsonl(path: Path, warnings: list[str]) -> list[dict[str, Any]]:
    if not path.exists():
        warnings.append(f"Missing JSONL file: {path.as_posix()}")
        return []
    rows: list[dict[str, Any]] = []
    for idx, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            warnings.append(f"Invalid JSONL entry ({path.as_posix()}:{idx}): {exc}")
            continue
        if isinstance(value, dict):
            rows.append(value)
    return rows


def _parse_claim_registry(path: Path, warnings: list[str]) -> dict[str, dict[str, Any]]:
    claims: dict[str, dict[str, Any]] = {}
    if not path.exists():
        warnings.append(f"Missing claim registry: {path.as_posix()}")
        return claims

    current: dict[str, Any] | None = None
    active_list_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("- id:"):
            if current and current.get("id"):
                claims[str(current["id"])] = current
            current = {
                "id": line.split(":", 1)[1].strip(),
                "claim_type": "",
                "subject": "",
                "status": "",
                "location": "",
                "depends_on": [],
            }
            active_list_key = None
            continue

        if current is None:
            continue

        if line.startswith("  claim_type:"):
            current["claim_type"] = line.split(":", 1)[1].strip()
            active_list_key = None
            continue
        if line.startswith("  subject:"):
            current["subject"] = line.split(":", 1)[1].strip()
            active_list_key = None
            continue
        if line.startswith("  status:"):
            current["status"] = line.split(":", 1)[1].strip()
            active_list_key = None
            continue
        if line.startswith("  location:"):
            current["location"] = line.split(":", 1)[1].strip()
            active_list_key = None
            continue
        if line.startswith("  depends_on:"):
            active_list_key = "depends_on"
            continue
        if line.startswith("  ") and not line.startswith("    - "):
            active_list_key = None
            continue
        if active_list_key == "depends_on" and line.startswith("    - "):
            dep = line.split("-", 1)[1].strip()
            if dep:
                cast = current.setdefault("depends_on", [])
                if isinstance(cast, list):
                    cast.append(dep)
            continue

    if current and current.get("id"):
        claims[str(current["id"])] = current

    dependents_by_claim: dict[str, list[str]] = defaultdict(list)
    for cid, meta in claims.items():
        deps = meta.get("depends_on", [])
        if not isinstance(deps, list):
            continue
        for dep in deps:
            token = str(dep).strip()
            if token:
                dependents_by_claim[token].append(cid)
    for cid in claims:
        claims[cid]["dependents"] = sorted(dependents_by_claim.get(cid, []))
    return claims


def _subject_label(subject: str) -> str:
    return subject.replace(".", " / ").replace("_", " ").strip()


def _claim_type_label(claim_type: str) -> str:
    labels = {
        "architectural_commitment": "architecture commitment",
        "mechanism_hypothesis": "mechanism hypothesis",
        "open_question": "open question",
        "implementation_note": "implementation note",
        "invariant": "invariant",
    }
    token = claim_type.strip()
    return labels.get(token, token or "claim")


def _extract_architecture_snippet(repo_root: Path, location: str, claim_id: str) -> list[str]:
    token = location.strip()
    if not token:
        return []

    if "#" in token:
        rel_path, anchor = token.split("#", 1)
    else:
        rel_path, anchor = token, ""
    doc_path = (repo_root / rel_path).resolve()
    if not doc_path.exists():
        return []

    lines = doc_path.read_text(encoding="utf-8").splitlines()
    start_idx = 0
    anchor = anchor.strip()
    claim_lower = claim_id.lower()
    if anchor:
        for idx, line in enumerate(lines):
            lower = line.lower()
            if f'<a id="{anchor.lower()}"></a>' in lower:
                start_idx = idx + 1
                break
            if f"(#{anchor.lower()})" in lower:
                start_idx = idx + 1
                break
            if f"({claim_lower})" in lower:
                start_idx = idx + 1
                break

    snippet: list[str] = []
    for line in lines[start_idx:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("<a id=") and snippet:
            break
        if stripped.startswith("## ") and snippet:
            break
        if stripped.startswith("---") and snippet:
            break

        cleaned = stripped.replace("**", "").replace("`", "")
        snippet.append(cleaned)
        if len(snippet) >= 5:
            break
    return snippet


def _parse_promotion_recommendations(path: Path, warnings: list[str]) -> dict[str, dict[str, Any]]:
    if not path.exists():
        warnings.append(f"Missing recommendations file: {path.as_posix()}")
        return {}

    details: dict[str, dict[str, Any]] = {}
    current_claim = ""
    mode = ""
    section_re = re.compile(r"^###\s+([A-Z0-9-]+)\s*$")
    why_re = re.compile(
        r"overall_conf=([0-9.]+),\s*conflict_ratio=([0-9.]+),\s*exp_entries=([0-9]+),\s*lit_entries=([0-9]+)"
    )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip("\n")
        m = section_re.match(line.strip())
        if m:
            current_claim = m.group(1)
            details[current_claim] = {
                "current_status": "",
                "decision_needed": "",
                "recommendation": "",
                "decision_status": "",
                "why_raw": "",
                "why_metrics": {},
                "options": [],
                "discussion_prompts": [],
                "last_logged_decision": "",
                "last_selected_option": "",
                "last_rationale": "",
            }
            mode = ""
            continue
        if not current_claim:
            continue
        item = details[current_claim]
        stripped = line.strip()
        if stripped.startswith("- Current status:"):
            item["current_status"] = _strip_ticks(stripped.split(":", 1)[1])
            mode = ""
            continue
        if stripped.startswith("- Decision needed:"):
            item["decision_needed"] = stripped.split(":", 1)[1].strip()
            mode = ""
            continue
        if stripped.startswith("- Recommendation:"):
            item["recommendation"] = _strip_ticks(stripped.split(":", 1)[1])
            mode = ""
            continue
        if stripped.startswith("- Decision status:"):
            item["decision_status"] = _strip_ticks(stripped.split(":", 1)[1])
            mode = ""
            continue
        if stripped.startswith("- Why this decision is needed:"):
            why = stripped.split(":", 1)[1].strip()
            item["why_raw"] = why
            match = why_re.search(why)
            if match:
                item["why_metrics"] = {
                    "overall_conf": float(match.group(1)),
                    "conflict_ratio": float(match.group(2)),
                    "exp_entries": int(match.group(3)),
                    "lit_entries": int(match.group(4)),
                }
            mode = ""
            continue
        if stripped == "- Options (pros/cons):":
            mode = "options"
            continue
        if stripped == "- Discussion scope with Codex:":
            mode = "discussion"
            continue
        if stripped.startswith("- Last logged decision:"):
            item["last_logged_decision"] = stripped.split(":", 1)[1].strip()
            mode = ""
            continue
        if stripped.startswith("- Last selected option:"):
            item["last_selected_option"] = stripped.split(":", 1)[1].strip()
            mode = ""
            continue
        if stripped.startswith("- Last rationale:"):
            item["last_rationale"] = stripped.split(":", 1)[1].strip()
            mode = ""
            continue
        if mode == "options" and stripped.startswith("- "):
            item["options"].append(stripped[2:].strip())
            continue
        if mode == "discussion" and stripped.startswith("- "):
            item["discussion_prompts"].append(stripped[2:].strip())
            continue
        mode = ""

    return details


def _extract_section(lines: list[str], heading: str) -> list[str]:
    start_idx = None
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            start_idx = idx + 1
            break
    if start_idx is None:
        return []
    collected: list[str] = []
    for line in lines[start_idx:]:
        if line.startswith("## "):
            break
        collected.append(line)
    return collected


def _parse_markdown_table(lines: list[str]) -> list[dict[str, str]]:
    table_lines = [line.strip() for line in lines if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return []
    header = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for raw in table_lines[2:]:
        cells = [cell.strip() for cell in raw.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        row = {header[i]: cells[i] for i in range(len(header))}
        rows.append(row)
    return rows


def _parse_conflicts(path: Path, warnings: list[str]) -> dict[str, dict[str, Any]]:
    if not path.exists():
        warnings.append(f"Missing conflicts report: {path.as_posix()}")
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    section = _extract_section(lines, "## Conflict Queue")
    rows = _parse_markdown_table(section)
    by_claim: dict[str, dict[str, Any]] = {}
    for row in rows:
        claim = _strip_ticks(str(row.get("claim_id", "")))
        if claim:
            by_claim[claim] = row
    return by_claim


def _load_structure_dossiers(
    report_path: Path, repo_root: Path, warnings: list[str]
) -> tuple[str, dict[str, dict[str, Any]], list[dict[str, Any]]]:
    report = _load_json_file(report_path, warnings, required=False)
    if not report:
        return "", {}, []
    cycle = str(report.get("cycle_date", "")).strip()
    items = report.get("items", [])
    if not isinstance(items, list):
        items = []
    dossier_by_claim: dict[str, dict[str, Any]] = {}
    filtered_items: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        claim_id = str(item.get("claim_id", "")).strip()
        if not claim_id:
            continue
        filtered_items.append(item)
        path_token = str(item.get("dossier_json_path", "")).strip()
        if not path_token:
            continue
        dossier_path = Path(path_token)
        if not dossier_path.is_absolute():
            dossier_path = (repo_root / path_token).resolve()
        dossier = _load_json_file(dossier_path, warnings, required=False)
        if dossier:
            dossier_by_claim[claim_id] = dossier
    return cycle, dossier_by_claim, filtered_items


def _group_decision_history(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in entries:
        claim = str(row.get("claim_id", "")).strip()
        if claim:
            grouped[claim].append(row)
    for claim in grouped:
        grouped[claim].sort(key=lambda x: str(x.get("timestamp_utc", "")))
    return grouped


def _write_metric_glossary(path: Path) -> None:
    lines = [
        "# Human Decision Metric Glossary",
        "",
        "Generated for human governance readability.",
        "",
        "## Core Metrics",
        "",
        "`conflict_ratio`",
        "- How split supporting vs weakening evidence is.",
        "- Formula: `2 * min(supports, weakens) / (supports + weakens)`.",
        "- `0` means one-direction evidence; `1` means maximal split conflict.",
        "- Source formula: `evidence/experiments/scripts/build_experiment_indexes.py:837`.",
        "",
        "`overall_confidence`",
        "- Combined confidence channel from experiment+literature evidence.",
        "- Built from consistency, evidence volume, recency, and evidence quality.",
        "- Source: `evidence/experiments/scripts/build_experiment_indexes.py:847`.",
        "",
        "`lit_non_support_ratio`",
        "- Fraction of literature evidence marked `weakens` or `mixed`.",
        "- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2146`.",
        "",
        "`delta_lit_minus_exp`",
        "- `literature_confidence - experimental_confidence`.",
        "- Positive means literature confidence currently exceeds experimental confidence.",
        "- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2176`.",
        "",
        "`recurring_failure_signatures`",
        "- Repeated failure tags aggregated from run-pack `failure_signatures`.",
        "- High counts indicate persistent mechanism failure modes, not one-off noise.",
        "- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2101`.",
        "",
        "`stale_ratio` (architecture epoch applicability)",
        "- Fraction of entries that do not satisfy current architecture epoch applicability.",
        "- Source report: `evidence/planning/architecture_epoch_applicability.v1.json`.",
        "",
        "## Evidence Labels",
        "",
        "`PASS` / `FAIL`",
        "- Derived from both run status and stop-criteria checks.",
        "- Source: `evidence/experiments/INTERFACE_CONTRACT.md:123`.",
        "",
        "`supports` / `weakens` / `mixed` / `unknown`",
        "- Directional evidence labels used for conflict and recommendation logic.",
        "",
        "`source_disagreement`",
        "- Experimental majority and literature majority point in opposite directions.",
        "- Source logic: `evidence/experiments/scripts/build_experiment_indexes.py:1745`.",
        "",
        "`mixed_evidence`",
        "- At least one `mixed` direction entry exists for a claim.",
        "- Source logic: `evidence/experiments/scripts/build_experiment_indexes.py:1759`.",
    ]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _claim_decision_lanes(
    claim_id: str,
    promotion: dict[str, dict[str, Any]],
    structure_items: dict[str, dict[str, Any]],
) -> list[str]:
    lanes: list[str] = []
    if claim_id in promotion:
        lanes.append("promotion_demotion_conflict_resolution")
    if claim_id in structure_items:
        lanes.append("architecture_structure_adjudication")
    return lanes


def _build_claim_brief(
    *,
    claim_id: str,
    cycle: str,
    repo_root: Path,
    output_path: Path,
    claim_registry: dict[str, dict[str, Any]],
    promotion: dict[str, dict[str, Any]],
    conflicts: dict[str, dict[str, Any]],
    structure_item: dict[str, Any] | None,
    dossier: dict[str, Any] | None,
    decision_state: dict[str, Any],
    decision_history: list[dict[str, Any]],
    allowed_outcomes: list[str],
) -> None:
    meta = claim_registry.get(claim_id, {})
    claim_type = _claim_type_label(str(meta.get("claim_type", "")))
    subject = _subject_label(str(meta.get("subject", "")))
    status = str(meta.get("status", "")).strip() or "unknown"
    location = str(meta.get("location", "")).strip()
    depends_on = meta.get("depends_on", [])
    if not isinstance(depends_on, list):
        depends_on = []
    dependents = meta.get("dependents", [])
    if not isinstance(dependents, list):
        dependents = []

    architecture_snippet = _extract_architecture_snippet(repo_root, location, claim_id)
    promotion_item = promotion.get(claim_id, {})
    conflict_item = conflicts.get(claim_id, {})
    state_item = decision_state.get(claim_id, {}) if isinstance(decision_state, dict) else {}
    structure_pressure = dossier.get("structure_pressure", {}) if isinstance(dossier, dict) else {}
    evidence_overview = dossier.get("evidence_overview", {}) if isinstance(dossier, dict) else {}

    lines: list[str] = []
    lines.append(f"# Human Decision Brief: {claim_id}")
    lines.append("")
    lines.append(f"Cycle: `{cycle}`")
    lines.append("")
    lines.append("## Mechanism / Claim Context")
    lines.append("")
    lines.append(f"- Claim type: `{claim_type}`")
    lines.append(f"- Current claim status: `{status}`")
    if subject:
        lines.append(f"- Subject: {subject}")
    if location:
        lines.append(f"- Architecture anchor: `{location}`")
    if depends_on:
        lines.append("- Upstream dependencies: " + ", ".join(f"`{token}`" for token in depends_on))
    if dependents:
        lines.append("- Downstream dependents: " + ", ".join(f"`{token}`" for token in dependents))
    lines.append("")
    if architecture_snippet:
        lines.append("## How It Functions In The Architecture")
        lines.append("")
        for snippet in architecture_snippet:
            lines.append(f"- {snippet}")
        lines.append("")

    lines.append("## Decision Lanes")
    lines.append("")
    if promotion_item:
        lines.append("### Promotion / Conflict Lane")
        lines.append("")
        if promotion_item.get("decision_needed"):
            lines.append(f"- Decision needed: {promotion_item['decision_needed']}")
        if promotion_item.get("recommendation"):
            lines.append(f"- Recommendation: `{promotion_item['recommendation']}`")
        if promotion_item.get("decision_status"):
            lines.append(f"- Decision status: `{promotion_item['decision_status']}`")
        if promotion_item.get("why_raw"):
            lines.append(f"- Why this lane is open: {promotion_item['why_raw']}")
        opts = promotion_item.get("options", [])
        if isinstance(opts, list) and opts:
            lines.append("- Options:")
            for opt in opts:
                lines.append(f"  - {opt}")
        lines.append("")

    if structure_item or structure_pressure:
        lines.append("### Architecture Structure Lane")
        lines.append("")
        if structure_item and structure_item.get("recommendation"):
            lines.append(f"- Lane recommendation: `{structure_item.get('recommendation', '')}`")
        if structure_pressure:
            lines.append(
                f"- Structure pressure recommendation: `{structure_pressure.get('recommendation', '')}`"
            )
            lines.append(
                f"- Conflict ratio: `{structure_pressure.get('conflict_ratio', 'n/a')}`; overall confidence: `{structure_pressure.get('overall_confidence', 'n/a')}`"
            )
            trigger_signals = structure_pressure.get("trigger_signals", [])
            if isinstance(trigger_signals, list) and trigger_signals:
                lines.append(
                    "- Trigger signals: "
                    + ", ".join(str(token) for token in trigger_signals if str(token).strip())
                )
            recurring = structure_pressure.get("recurring_failure_signatures", [])
            if isinstance(recurring, list) and recurring:
                lines.append("- Recurring failure signatures:")
                for token in recurring[:5]:
                    if not isinstance(token, dict):
                        continue
                    sig = str(token.get("signature", "")).strip()
                    count = token.get("count", "")
                    if sig:
                        lines.append(f"  - `{sig}` ({count})")
        lines.append("")

    lines.append("## Evidence Snapshot")
    lines.append("")
    if conflict_item:
        lines.append(
            "- Conflict report window: "
            + f"supports={conflict_item.get('supports', '')}, "
            + f"weakens={conflict_item.get('weakens', '')}, "
            + f"conflict_ratio={conflict_item.get('conflict_ratio', '')}, "
            + f"entries_considered={conflict_item.get('entries_considered', '')}."
        )
    if evidence_overview:
        direction_counts = evidence_overview.get("direction_counts", {})
        if isinstance(direction_counts, dict):
            lines.append(
                "- Dossier direction mix: "
                + f"supports={direction_counts.get('supports', 0)}, "
                + f"weakens={direction_counts.get('weakens', 0)}, "
                + f"mixed={direction_counts.get('mixed', 0)}, "
                + f"unknown={direction_counts.get('unknown', 0)}."
            )
        source_counts = structure_pressure.get("source_counts", {})
        if isinstance(source_counts, dict) and source_counts:
            lines.append(
                "- Source counts: "
                + f"experimental={source_counts.get('experimental', 0)}, "
                + f"literature={source_counts.get('literature', 0)}."
            )
    if state_item:
        lines.append(
            "- Latest decision state: "
            + f"status=`{state_item.get('decision_status', '')}`, "
            + f"recommendation=`{state_item.get('recommendation', '')}`, "
            + f"timestamp=`{state_item.get('timestamp_utc', '')}`."
        )
    if decision_history:
        lines.append("- Recent decision history:")
        for row in decision_history[-3:]:
            lines.append(
                "  - "
                + f"{row.get('timestamp_utc', '')}: "
                + f"status=`{row.get('decision_status', '')}`, "
                + f"recommendation=`{row.get('recommendation', '')}`, "
                + f"decision_needed={row.get('decision_needed', '')}"
            )
    lines.append("")

    lines.append("## Human Decision Prompt")
    lines.append("")
    if structure_item or structure_pressure:
        lines.append(
            "- Architecture adjudication outcome to select now: "
            + ", ".join(f"`{token}`" for token in allowed_outcomes)
        )
    if promotion_item and promotion_item.get("decision_needed"):
        lines.append(
            "- Promotion/conflict lane decision to resolve now: "
            + str(promotion_item.get("decision_needed", ""))
        )
    lines.append(
        "- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`."
    )
    lines.append("")

    lines.append("## Source Paths")
    lines.append("")
    lines.append("- Claim registry: `docs/claims/claims.yaml`")
    if location:
        lines.append(f"- Architecture anchor: `{location}`")
    if promotion_item:
        lines.append("- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`")
    if conflict_item:
        lines.append("- Conflict report: `evidence/experiments/conflicts.md`")
    if structure_item:
        md_path = str(structure_item.get("dossier_md_path", "")).strip()
        json_path = str(structure_item.get("dossier_json_path", "")).strip()
        if md_path:
            lines.append(f"- Structure dossier: `{Path(md_path).as_posix()}`")
        if json_path:
            lines.append(f"- Structure dossier JSON: `{Path(json_path).as_posix()}`")
    lines.append("- Decision state: `evidence/decisions/decision_state.v1.json`")
    lines.append("- Decision log: `evidence/decisions/decision_log.v1.jsonl`")

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _build_dispatch_brief(
    *,
    path: Path,
    proposals: dict[str, Any],
    high_proposals: list[dict[str, Any]],
) -> None:
    items = proposals.get("items", []) if isinstance(proposals, dict) else []
    by_repo: dict[str, dict[str, int]] = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        repo = str(item.get("target_repo", "unknown"))
        ptype = str(item.get("proposal_type", "unknown"))
        slot = by_repo.setdefault(repo, {"total": 0, "experimental": 0, "literature_review": 0})
        slot["total"] += 1
        if ptype == "experimental":
            slot["experimental"] += 1
        if ptype == "literature_review":
            slot["literature_review"] += 1

    lines: list[str] = []
    lines.append("# Human Decision Brief: Weekly Dispatch Export")
    lines.append("")
    lines.append("## Decision Context")
    lines.append("")
    lines.append(
        "- This is the `AUTO_WITH_APPROVAL` lane for exporting high-priority proposals into execution repos."
    )
    lines.append(
        "- Human decision asks: approve this cycle's dispatch export or defer."
    )
    lines.append("")
    lines.append("## Current Queue Snapshot")
    lines.append("")
    lines.append(f"- High-priority proposals: `{len(high_proposals)}`")
    lines.append(f"- Total proposals this cycle: `{len(items)}`")
    lines.append("")
    lines.append("| target_repo | total | experimental | literature_review |")
    lines.append("|---|---:|---:|---:|")
    for repo in sorted(by_repo.keys()):
        slot = by_repo[repo]
        lines.append(
            f"| `{repo}` | {slot['total']} | {slot['experimental']} | {slot['literature_review']} |"
        )
    lines.append("")
    lines.append("## What Approval Means")
    lines.append("")
    lines.append("- Export proposal packs to target repos and open execution work.")
    lines.append("- Human commitment: proposal direction is acceptable for this cycle.")
    lines.append("- Rollback path: hold/discard unstarted proposals next cycle if priorities change.")
    lines.append("")
    lines.append("## Source Paths")
    lines.append("")
    lines.append("- `evidence/planning/experiment_proposals.v1.json`")
    lines.append("- `evidence/planning/GOVERNANCE_AGENDA.md`")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build human-readable decision briefs for governance queues."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--structure-review-report",
        type=Path,
        default=Path("evidence/planning/structure_review/latest/structure_review_report.v1.json"),
        help="Path to structure review report JSON.",
    )
    parser.add_argument(
        "--promotion-recommendations",
        type=Path,
        default=Path("evidence/experiments/promotion_demotion_recommendations.md"),
        help="Path to promotion/demotion recommendations markdown.",
    )
    parser.add_argument(
        "--conflicts",
        type=Path,
        default=Path("evidence/experiments/conflicts.md"),
        help="Path to conflicts markdown.",
    )
    parser.add_argument(
        "--decision-state",
        type=Path,
        default=Path("evidence/decisions/decision_state.v1.json"),
        help="Path to decision state JSON.",
    )
    parser.add_argument(
        "--decision-log",
        type=Path,
        default=Path("evidence/decisions/decision_log.v1.jsonl"),
        help="Path to decision log JSONL.",
    )
    parser.add_argument(
        "--planning-criteria",
        type=Path,
        default=Path("evidence/planning/planning_criteria.v1.yaml"),
        help="Path to planning criteria JSON-compatible YAML file.",
    )
    parser.add_argument(
        "--proposals",
        type=Path,
        default=Path("evidence/planning/experiment_proposals.v1.json"),
        help="Path to proposal queue JSON.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("evidence/decisions/human_decision_briefs"),
        help="Output directory for generated briefs.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    warnings: list[str] = []

    structure_report_path = (
        args.structure_review_report
        if args.structure_review_report.is_absolute()
        else (repo_root / args.structure_review_report).resolve()
    )
    promotion_path = (
        args.promotion_recommendations
        if args.promotion_recommendations.is_absolute()
        else (repo_root / args.promotion_recommendations).resolve()
    )
    conflicts_path = (
        args.conflicts
        if args.conflicts.is_absolute()
        else (repo_root / args.conflicts).resolve()
    )
    decision_state_path = (
        args.decision_state
        if args.decision_state.is_absolute()
        else (repo_root / args.decision_state).resolve()
    )
    decision_log_path = (
        args.decision_log
        if args.decision_log.is_absolute()
        else (repo_root / args.decision_log).resolve()
    )
    planning_criteria_path = (
        args.planning_criteria
        if args.planning_criteria.is_absolute()
        else (repo_root / args.planning_criteria).resolve()
    )
    proposals_path = (
        args.proposals
        if args.proposals.is_absolute()
        else (repo_root / args.proposals).resolve()
    )
    output_root = (
        args.output_root
        if args.output_root.is_absolute()
        else (repo_root / args.output_root).resolve()
    )

    claims = _parse_claim_registry(repo_root / "docs/claims/claims.yaml", warnings)
    promotion = _parse_promotion_recommendations(promotion_path, warnings)
    conflicts = _parse_conflicts(conflicts_path, warnings)
    decision_state = _load_json_file(decision_state_path, warnings, required=False).get("claims", {})
    decision_log_rows = _load_jsonl(decision_log_path, warnings)
    decision_history = _group_decision_history(decision_log_rows)
    planning_criteria = _load_json_file(planning_criteria_path, warnings, required=False)
    proposals = _load_json_file(proposals_path, warnings, required=False)

    cycle, dossier_by_claim, structure_items_list = _load_structure_dossiers(
        structure_report_path,
        repo_root,
        warnings,
    )
    if not cycle:
        cycle = datetime.now(timezone.utc).date().isoformat()

    structure_items = {
        str(item.get("claim_id", "")).strip(): item
        for item in structure_items_list
        if isinstance(item, dict) and str(item.get("claim_id", "")).strip()
    }

    model_adjudication = (
        planning_criteria.get("model_adjudication", {}) if isinstance(planning_criteria, dict) else {}
    )
    allowed_outcomes = [
        str(x).strip()
        for x in model_adjudication.get("allowed_conflict_outcomes", [])
        if str(x).strip()
    ]
    if not allowed_outcomes:
        allowed_outcomes = ["retain_ree", "hybridize", "adopt_jepa_structure", "retire_ree_claim"]

    claim_ids = sorted(set(promotion.keys()) | set(structure_items.keys()))
    cycle_dir = output_root / cycle
    latest_dir = output_root / "latest"
    cycle_dir.mkdir(parents=True, exist_ok=True)
    latest_dir.mkdir(parents=True, exist_ok=True)

    index_rows: list[dict[str, Any]] = []
    for claim_id in claim_ids:
        lanes = _claim_decision_lanes(claim_id, promotion, structure_items)
        if not lanes:
            continue
        brief_path = cycle_dir / f"{claim_id}.md"
        _build_claim_brief(
            claim_id=claim_id,
            cycle=cycle,
            repo_root=repo_root,
            output_path=brief_path,
            claim_registry=claims,
            promotion=promotion,
            conflicts=conflicts,
            structure_item=structure_items.get(claim_id),
            dossier=dossier_by_claim.get(claim_id),
            decision_state=decision_state if isinstance(decision_state, dict) else {},
            decision_history=decision_history.get(claim_id, []),
            allowed_outcomes=allowed_outcomes,
        )
        index_rows.append(
            {
                "claim_id": claim_id,
                "lanes": lanes,
                "path": brief_path.as_posix(),
            }
        )

    high_proposals = []
    proposal_items = proposals.get("items", []) if isinstance(proposals, dict) else []
    if isinstance(proposal_items, list):
        high_proposals = [
            item for item in proposal_items if isinstance(item, dict) and str(item.get("priority", "")) == "high"
        ]
    dispatch_brief_path = cycle_dir / "WEEKLY_DISPATCH.md"
    _build_dispatch_brief(
        path=dispatch_brief_path,
        proposals=proposals,
        high_proposals=high_proposals,
    )

    glossary_path = repo_root / "evidence/decisions/HUMAN_DECISION_GLOSSARY.md"
    _write_metric_glossary(glossary_path)

    index_lines: list[str] = []
    index_lines.append("# Human Decision Brief Index")
    index_lines.append("")
    index_lines.append(f"Generated: `{_now_utc()}`")
    index_lines.append(f"Cycle: `{cycle}`")
    index_lines.append("")
    index_lines.append("These briefs are mandatory context for human-governed lanes.")
    index_lines.append("")
    index_lines.append(f"- Metric glossary: `{glossary_path.relative_to(repo_root).as_posix()}`")
    index_lines.append(f"- Dispatch brief: `{dispatch_brief_path.relative_to(repo_root).as_posix()}`")
    index_lines.append("")
    index_lines.append("| claim_id | lanes | brief |")
    index_lines.append("|---|---|---|")
    for row in index_rows:
        rel = Path(row["path"]).relative_to(repo_root).as_posix()
        lane_text = ",".join(row["lanes"])
        index_lines.append(f"| `{row['claim_id']}` | `{lane_text}` | `{rel}` |")
    if not index_rows:
        index_lines.append("| `_none_` | - | - |")
    index_lines.append("")
    index_lines.append("## Minimum Reading Requirement")
    index_lines.append("")
    index_lines.append(
        "Before recording a human decision, read the claim brief plus `HUMAN_DECISION_GLOSSARY.md`."
    )

    cycle_index_path = cycle_dir / "INDEX.md"
    cycle_index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    latest_index_path = latest_dir / "INDEX.md"
    latest_index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")

    report = {
        "schema_version": "human_decision_briefs/v1",
        "generated_at_utc": _now_utc(),
        "cycle_date": cycle,
        "claim_briefs_total": len(index_rows),
        "dispatch_brief_path": dispatch_brief_path.as_posix(),
        "index_path": cycle_index_path.as_posix(),
        "latest_index_path": latest_index_path.as_posix(),
        "items": index_rows,
        "source": {
            "structure_review_report": structure_report_path.as_posix(),
            "promotion_recommendations": promotion_path.as_posix(),
            "conflicts": conflicts_path.as_posix(),
            "decision_state": decision_state_path.as_posix(),
            "decision_log": decision_log_path.as_posix(),
            "proposals": proposals_path.as_posix(),
            "claims_registry": (repo_root / "docs/claims/claims.yaml").as_posix(),
        },
        "warnings": warnings,
    }
    report_path = cycle_dir / "human_decision_briefs_report.v1.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    latest_report_path = latest_dir / "human_decision_briefs_report.v1.json"
    latest_report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        "Human decision briefs generated: "
        + f"cycle={cycle}, claims={len(index_rows)}, "
        + f"index={cycle_index_path.as_posix()}, "
        + f"warnings={len(warnings)}"
    )
    if warnings:
        for warning in warnings:
            print(f"- {warning}")


if __name__ == "__main__":
    main()
