#!/usr/bin/env python3
"""Run REE Governance Cycle non-decision steps and build a discussion agenda.

This helper executes deterministic maintenance steps and outputs a structured
agenda for human review checkpoints.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class StepResult:
    name: str
    command: list[str]
    returncode: int
    started_at_utc: str
    finished_at_utc: str
    stdout: str
    stderr: str

    @property
    def status(self) -> str:
        return "ok" if self.returncode == 0 else "failed"

    def to_json(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "command": self.command,
            "status": self.status,
            "returncode": self.returncode,
            "started_at_utc": self.started_at_utc,
            "finished_at_utc": self.finished_at_utc,
            "stdout": self.stdout,
            "stderr": self.stderr,
        }


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _run_step(name: str, command: list[str], cwd: Path) -> StepResult:
    started = _now_utc()
    proc = subprocess.run(command, cwd=str(cwd), capture_output=True, text=True)
    finished = _now_utc()
    return StepResult(
        name=name,
        command=command,
        returncode=proc.returncode,
        started_at_utc=started,
        finished_at_utc=finished,
        stdout=proc.stdout.strip(),
        stderr=proc.stderr.strip(),
    )


def _load_json_file(path: Path, warnings: list[str]) -> dict[str, Any]:
    if not path.exists():
        warnings.append(f"Missing file: {path.as_posix()}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        warnings.append(f"Invalid JSON ({path.as_posix()}): {exc}")
        return {}


def _strip_ticks(text: str) -> str:
    return text.strip().strip("`")


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
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        row = {header[i]: cells[i] for i in range(len(header))}
        first_cell = _strip_ticks(cells[0])
        if first_cell in {"_none_", "-", ""}:
            continue
        rows.append(row)
    return rows


def _read_conflicts(path: Path, warnings: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        warnings.append(f"Missing conflicts report: {path.as_posix()}")
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    section = _extract_section(lines, "## Conflict Queue")
    return _parse_markdown_table(section)


def _read_recommendations(path: Path, warnings: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        warnings.append(f"Missing recommendation report: {path.as_posix()}")
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    section = _extract_section(lines, "## Decision Queue")
    return _parse_markdown_table(section)


def _proposal_repo_summary(proposals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summary: dict[str, dict[str, Any]] = {}
    for item in proposals:
        repo = str(item.get("target_repo", "unknown"))
        proposal_type = str(item.get("proposal_type", "unknown"))
        slot = summary.setdefault(
            repo,
            {
                "target_repo": repo,
                "total": 0,
                "experimental": 0,
                "literature_review": 0,
            },
        )
        slot["total"] += 1
        if proposal_type in {"experimental", "literature_review"}:
            slot[proposal_type] += 1
    return sorted(summary.values(), key=lambda x: x["target_repo"])


def _build_agenda(
    repo_root: Path,
    steps: list[StepResult],
    warnings: list[str],
    generated_at: str,
) -> tuple[dict[str, Any], str]:
    thought_sweep = _load_json_file(repo_root / "docs/thoughts/thought_sweep.v1.json", warnings)
    backlog = _load_json_file(repo_root / "evidence/planning/evidence_backlog.v1.json", warnings)
    proposals = _load_json_file(repo_root / "evidence/planning/experiment_proposals.v1.json", warnings)
    architecture_gaps = _load_json_file(
        repo_root / "evidence/planning/architecture_gap_register.v1.json", warnings
    )
    structure_review_report = _load_json_file(
        repo_root / "evidence/planning/structure_review/latest/structure_review_report.v1.json",
        warnings,
    )
    claim_matrix = _load_json_file(repo_root / "evidence/experiments/claim_evidence.v1.json", warnings)

    conflicts = _read_conflicts(repo_root / "evidence/experiments/conflicts.md", warnings)
    recommendations = _read_recommendations(
        repo_root / "evidence/experiments/promotion_demotion_recommendations.md", warnings
    )

    thought_records = thought_sweep.get("records", []) if isinstance(thought_sweep, dict) else []
    thought_unprocessed = [
        rec for rec in thought_records if not bool(rec.get("is_processed", False))
    ]

    backlog_items = backlog.get("items", []) if isinstance(backlog, dict) else []
    high_backlog = [item for item in backlog_items if item.get("priority") == "high"]

    proposal_items = proposals.get("items", []) if isinstance(proposals, dict) else []
    high_proposals = [item for item in proposal_items if item.get("priority") == "high"]
    architecture_items = (
        architecture_gaps.get("items", []) if isinstance(architecture_gaps, dict) else []
    )
    structure_considerations = [
        item for item in architecture_items if bool(item.get("consider_new_structure", False))
    ]
    structure_review_items = (
        structure_review_report.get("items", []) if isinstance(structure_review_report, dict) else []
    )
    structure_review_total = int(
        structure_review_report.get("items_total", len(structure_review_items))
        if isinstance(structure_review_report, dict)
        else 0
    )
    structure_review_consider = int(
        structure_review_report.get(
            "consider_new_structure_total",
            sum(1 for item in structure_review_items if bool(item.get("consider_new_structure", False))),
        )
        if isinstance(structure_review_report, dict)
        else 0
    )

    unlinked_runs = claim_matrix.get("unlinked_runs", []) if isinstance(claim_matrix, dict) else []

    agenda = {
        "schema_version": "governance_agenda/v1",
        "generated_at_utc": generated_at,
        "cycle": {
            "name": "REE Governance Cycle",
            "repo_root": repo_root.as_posix(),
            "steps": [step.to_json() for step in steps],
        },
        "summary": {
            "step_failures": sum(1 for step in steps if step.status != "ok"),
            "warnings": len(warnings),
            "thought_unprocessed": len(thought_unprocessed),
            "conflicts": len(conflicts),
            "decision_queue_items": len(recommendations),
            "backlog_items": len(backlog_items),
            "backlog_high_priority": len(high_backlog),
            "proposal_items": len(proposal_items),
            "proposal_high_priority": len(high_proposals),
            "architecture_gap_items": len(architecture_items),
            "structure_considerations": len(structure_considerations),
            "structure_review_dossiers": structure_review_total,
            "structure_review_considerations": structure_review_consider,
            "unlinked_evidence_runs": len(unlinked_runs),
        },
        "warnings": warnings,
        "checkpoints": {
            "thought_intake": {
                "prompt": "Decide promote/defer/split for unprocessed thoughts.",
                "items": thought_unprocessed,
            },
            "conflict_resolution": {
                "prompt": "Resolve directional/source conflicts before status promotions.",
                "items": conflicts,
            },
            "governance_decisions": {
                "prompt": "Review promotion/demotion queue and record decisions.",
                "items": recommendations,
            },
            "architecture_structure": {
                "prompt": "Review structure-pressure signals and decide whether to draft architecture changes.",
                "consider_new_structure": structure_considerations,
                "register_total_items": len(architecture_items),
            },
            "structure_review_dossiers": {
                "prompt": "Review claim dossiers before deciding architecture changes.",
                "items_total": structure_review_total,
                "consider_new_structure_total": structure_review_consider,
                "items": structure_review_items,
                "index_path": "evidence/planning/structure_review/latest/INDEX.md",
            },
            "evidence_dispatch": {
                "prompt": "Approve export of high-priority proposals to execution repos.",
                "high_priority_proposals": high_proposals,
                "by_target_repo": _proposal_repo_summary(proposal_items),
            },
            "maintenance": {
                "prompt": "Address ingestion hygiene warnings and unlinked evidence runs.",
                "unlinked_runs": unlinked_runs,
            },
        },
    }

    lines: list[str] = []
    lines.append("# Governance Agenda")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("## Cycle Status")
    lines.append("")
    lines.append("| step | status | command |")
    lines.append("|---|---|---|")
    for step in steps:
        cmd = " ".join(step.command)
        lines.append(f"| `{step.name}` | `{step.status}` | `{cmd}` |")
    lines.append("")

    lines.append("## Discussion Checkpoints")
    lines.append("")
    lines.append(f"1. Thought Intake: {len(thought_unprocessed)} unprocessed thought(s).")
    if thought_unprocessed:
        for rec in thought_unprocessed:
            lines.append(f"- `{rec.get('file', '')}`")
    lines.append(f"2. Conflict Resolution: {len(conflicts)} conflict item(s).")
    if conflicts:
        for item in conflicts[:10]:
            claim_id = _strip_ticks(str(item.get("claim_id", "")))
            conflict_types = str(item.get("conflict_types", ""))
            lines.append(f"- `{claim_id}` conflict_types={conflict_types}")
    lines.append(
        f"3. Governance Decisions: {len(recommendations)} recommendation queue item(s)."
    )
    if recommendations:
        for item in recommendations[:10]:
            claim_id = _strip_ticks(str(item.get("claim_id", "")))
            decision_needed = str(item.get("decision_needed", ""))
            recommendation = _strip_ticks(str(item.get("recommendation", "")))
            lines.append(
                f"- `{claim_id}` decision={decision_needed}; recommendation=`{recommendation}`"
            )
    lines.append(
        "4. Architecture Structure: "
        + f"{len(structure_considerations)} consider-new-structure item(s), "
        + f"{len(architecture_items)} total register item(s)."
    )
    if structure_considerations:
        for item in structure_considerations[:10]:
            claim_id = _strip_ticks(str(item.get("claim_id", "")))
            conflict_ratio = str(item.get("conflict_ratio", "n/a"))
            trigger_signals = ",".join(str(x) for x in item.get("trigger_signals", []))
            lines.append(
                f"- `{claim_id}` conflict_ratio={conflict_ratio}; trigger_signals={trigger_signals}"
            )
    lines.append(
        "5. Structure Dossiers: "
        + f"{structure_review_total} dossier(s), "
        + f"{structure_review_consider} marked consider-new-structure."
    )
    lines.append("- dossier index: `evidence/planning/structure_review/latest/INDEX.md`")
    lines.append(
        f"6. Evidence Dispatch: {len(high_proposals)} high-priority proposal(s), {len(proposal_items)} total."
    )
    for slot in _proposal_repo_summary(proposal_items):
        lines.append(
            "- "
            + f"{slot['target_repo']}: total={slot['total']}, "
            + f"experimental={slot['experimental']}, literature_review={slot['literature_review']}"
        )
    lines.append(
        f"7. Maintenance: {len(unlinked_runs)} unlinked evidence run(s), {len(warnings)} warning(s)."
    )
    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")

    markdown = "\n".join(lines).rstrip() + "\n"
    return agenda, markdown


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run REE Governance Cycle maintenance steps and build discussion agenda."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--skip-thought-sweep",
        action="store_true",
        help="Skip docs/thoughts sweep step.",
    )
    parser.add_argument(
        "--skip-evidence-build",
        action="store_true",
        help="Skip evidence ingestion/index build step.",
    )
    parser.add_argument(
        "--skip-structure-review",
        action="store_true",
        help="Skip structure review dossier generation step.",
    )
    parser.add_argument(
        "--strict-thoughts",
        action="store_true",
        help="Use --check-unprocessed when running thought sweep.",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue remaining steps even if one step fails.",
    )
    parser.add_argument(
        "--agenda-json",
        type=Path,
        default=None,
        help="Output path for governance agenda JSON.",
    )
    parser.add_argument(
        "--agenda-md",
        type=Path,
        default=None,
        help="Output path for governance agenda markdown.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    planning_root = repo_root / "evidence/planning"
    agenda_json_path = (
        args.agenda_json.resolve()
        if args.agenda_json
        else planning_root / "governance_agenda.v1.json"
    )
    agenda_md_path = (
        args.agenda_md.resolve()
        if args.agenda_md
        else planning_root / "GOVERNANCE_AGENDA.md"
    )

    steps: list[StepResult] = []
    warnings: list[str] = []

    plan: list[tuple[str, list[str]]] = []
    if not args.skip_thought_sweep:
        thought_cmd = [str(sys.executable), "docs/thoughts/scripts/thought_sweep.py"]
        if args.strict_thoughts:
            thought_cmd.append("--check-unprocessed")
        plan.append(("thought_sweep", thought_cmd))

    if not args.skip_evidence_build:
        plan.append(
            (
                "evidence_build",
                [
                    str(sys.executable),
                    "evidence/experiments/scripts/build_experiment_indexes.py",
                ],
            )
        )
    if not args.skip_structure_review:
        plan.append(
            (
                "structure_review",
                [
                    str(sys.executable),
                    "evidence/planning/scripts/build_structure_review_dossiers.py",
                ],
            )
        )

    for name, command in plan:
        result = _run_step(name=name, command=command, cwd=repo_root)
        steps.append(result)
        if result.status != "ok":
            warnings.append(
                f"Step failed ({name}) returncode={result.returncode}: {result.stderr or result.stdout}"
            )
            if not args.continue_on_error:
                break

    generated_at = _now_utc()
    agenda, markdown = _build_agenda(repo_root, steps, warnings, generated_at)

    agenda_json_path.parent.mkdir(parents=True, exist_ok=True)
    agenda_md_path.parent.mkdir(parents=True, exist_ok=True)
    agenda_json_path.write_text(json.dumps(agenda, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    agenda_md_path.write_text(markdown, encoding="utf-8")

    print(
        "Governance cycle complete: "
        + f"steps={len(steps)}, failures={agenda['summary']['step_failures']}, "
        + f"warnings={agenda['summary']['warnings']}, "
        + f"thought_unprocessed={agenda['summary']['thought_unprocessed']}, "
        + f"decision_queue={agenda['summary']['decision_queue_items']}, "
        + f"structure_considerations={agenda['summary']['structure_considerations']}, "
        + f"structure_dossiers={agenda['summary']['structure_review_dossiers']}, "
        + f"backlog_high={agenda['summary']['backlog_high_priority']}."
    )
    print(f"Agenda JSON: {agenda_json_path.as_posix()}")
    print(f"Agenda MD: {agenda_md_path.as_posix()}")

    if agenda["summary"]["step_failures"] > 0 and not args.continue_on_error:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
