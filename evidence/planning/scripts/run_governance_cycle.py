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


def _load_optional_json_file(path: Path, warnings: list[str]) -> dict[str, Any]:
    if not path.exists():
        return {}
    return _load_json_file(path, warnings)


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


def _step_status_map(steps: list[StepResult]) -> dict[str, str]:
    return {step.name: step.status for step in steps}


def _build_autonomy_triage_items(
    *,
    step_failures: int,
    warning_count: int,
    recommendations_count: int,
    conflicts_count: int,
    structure_considerations_count: int,
    external_precedence_count: int,
    anti_lock_in_reviews_count: int,
    high_proposals_count: int,
    cascade_actions_count: int,
    step_status: dict[str, str],
) -> list[dict[str, Any]]:
    maintenance_ok = step_failures == 0 and warning_count == 0
    queue_clear = recommendations_count == 0 and conflicts_count == 0
    architecture_clear = (
        structure_considerations_count == 0
        and external_precedence_count == 0
        and anti_lock_in_reviews_count == 0
    )

    items = [
        {
            "work_item": "governance_maintenance_pipeline",
            "tier": "AUTO",
            "gate_status": "PASS" if maintenance_ok else "FAIL",
            "recommendation": "execute" if maintenance_ok else "investigate_and_rerun",
            "rollback_ready": "yes",
            "decision_needed": "no",
            "rationale": (
                "All deterministic maintenance steps passed with no warnings."
                if maintenance_ok
                else "At least one deterministic step failed or emitted warnings."
            ),
        },
        {
            "work_item": "adjudication_cascade_application",
            "tier": "AUTO",
            "gate_status": "PASS"
            if step_status.get("adjudication_cascade", "skipped") != "failed"
            else "FAIL",
            "recommendation": (
                "execute"
                if cascade_actions_count > 0
                else "execute_no_pending_actions"
            ),
            "rollback_ready": "yes",
            "decision_needed": "no",
            "rationale": f"adjudication_cascade_step={step_status.get('adjudication_cascade', 'skipped')}; actions={cascade_actions_count}.",
        },
        {
            "work_item": "weekly_dispatch_export",
            "tier": "AUTO_WITH_APPROVAL",
            "gate_status": "PASS",
            "recommendation": (
                "approve_dispatch"
                if high_proposals_count > 0
                else "no_dispatch_this_cycle"
            ),
            "rollback_ready": "yes",
            "decision_needed": "yes" if high_proposals_count > 0 else "no",
            "rationale": f"high_priority_proposals={high_proposals_count}.",
        },
        {
            "work_item": "promotion_demotion_and_conflict_resolution",
            "tier": "HUMAN_ONLY",
            "gate_status": "PASS" if queue_clear else "FAIL",
            "recommendation": (
                "no_action_required"
                if queue_clear
                else "review_decision_queue_and_conflicts"
            ),
            "rollback_ready": "n/a",
            "decision_needed": "no" if queue_clear else "yes",
            "rationale": (
                "Decision queue and conflict queue are both empty."
                if queue_clear
                else f"decision_queue_items={recommendations_count}; conflicts={conflicts_count}."
            ),
        },
        {
            "work_item": "architecture_structure_adjudication",
            "tier": "HUMAN_ONLY",
            "gate_status": "PASS" if architecture_clear else "FAIL",
            "recommendation": (
                "no_action_required"
                if architecture_clear
                else "review_structure_dossiers_and_model_adjudication"
            ),
            "rollback_ready": "n/a",
            "decision_needed": "no" if architecture_clear else "yes",
            "rationale": (
                "No structure-pressure or external-precedence triggers present."
                if architecture_clear
                else "structure/external-precedence/anti-lock-in signals require explicit adjudication."
            ),
        },
    ]
    return items


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
    connectome_pull = _load_json_file(
        repo_root / "evidence/planning/connectome_literature_pull.v1.json", warnings
    )
    structure_review_report = _load_json_file(
        repo_root / "evidence/planning/structure_review/latest/structure_review_report.v1.json",
        warnings,
    )
    planning_criteria = _load_json_file(
        repo_root / "evidence/planning/planning_criteria.v1.yaml", warnings
    )
    carryover = _load_optional_json_file(
        repo_root / "evidence/planning/manual_carryover_items.v1.json",
        warnings,
    )
    adjudication_cascade_state = _load_json_file(
        repo_root / "evidence/decisions/adjudication_cascade_state.v1.json", warnings
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
    connectome_pull_items = (
        connectome_pull.get("items", []) if isinstance(connectome_pull, dict) else []
    )
    connectome_pull_high_priority = [
        item for item in connectome_pull_items if str(item.get("priority", "")) == "high"
    ]
    external_precedence_candidates = [
        item for item in architecture_items if bool(item.get("external_precedence_candidate", False))
    ]
    anti_lock_in_reviews = [
        item for item in architecture_items if bool(item.get("anti_lock_in_review_required", False))
    ]
    model_adjudication = (
        planning_criteria.get("model_adjudication", {}) if isinstance(planning_criteria, dict) else {}
    )
    allowed_conflict_outcomes_raw = model_adjudication.get("allowed_conflict_outcomes", [])
    allowed_conflict_outcomes = [
        str(x).strip() for x in allowed_conflict_outcomes_raw if str(x).strip()
    ]
    cascade_policy = model_adjudication.get("cascade_policy", {})
    temporary_override_mode = model_adjudication.get("temporary_override_mode", {})
    cascade_last_run = (
        adjudication_cascade_state.get("last_run", {})
        if isinstance(adjudication_cascade_state, dict)
        else {}
    )
    cascade_actions = (
        cascade_last_run.get("actions", [])
        if isinstance(cascade_last_run, dict)
        else []
    )
    cascade_claims_updated = (
        cascade_last_run.get("claims_updated", [])
        if isinstance(cascade_last_run, dict)
        else []
    )
    cascade_dependents_reopened = (
        cascade_last_run.get("dependents_reopened", [])
        if isinstance(cascade_last_run, dict)
        else []
    )
    step_status = _step_status_map(steps)
    autonomy_triage_items = _build_autonomy_triage_items(
        step_failures=sum(1 for step in steps if step.status != "ok"),
        warning_count=len(warnings),
        recommendations_count=len(recommendations),
        conflicts_count=len(conflicts),
        structure_considerations_count=len(structure_considerations),
        external_precedence_count=len(external_precedence_candidates),
        anti_lock_in_reviews_count=len(anti_lock_in_reviews),
        high_proposals_count=len(high_proposals),
        cascade_actions_count=len(cascade_actions),
        step_status=step_status,
    )
    autonomy_tier_counts = {
        "AUTO": sum(1 for item in autonomy_triage_items if item["tier"] == "AUTO"),
        "AUTO_WITH_APPROVAL": sum(
            1 for item in autonomy_triage_items if item["tier"] == "AUTO_WITH_APPROVAL"
        ),
        "HUMAN_ONLY": sum(1 for item in autonomy_triage_items if item["tier"] == "HUMAN_ONLY"),
    }
    autonomy_open_decisions = [
        item for item in autonomy_triage_items if item.get("decision_needed") == "yes"
    ]
    autonomy_failed_gates = [
        item for item in autonomy_triage_items if item.get("gate_status") != "PASS"
    ]

    unlinked_runs = claim_matrix.get("unlinked_runs", []) if isinstance(claim_matrix, dict) else []
    carryover_items = carryover.get("items", []) if isinstance(carryover, dict) else []
    open_carryover_items = [
        item for item in carryover_items if str(item.get("status", "open")).strip().lower() != "done"
    ]

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
            "connectome_pull_items": len(connectome_pull_items),
            "connectome_pull_high_priority": len(connectome_pull_high_priority),
            "external_precedence_candidates": len(external_precedence_candidates),
            "anti_lock_in_reviews": len(anti_lock_in_reviews),
            "adjudication_cascade_actions": len(cascade_actions),
            "adjudication_cascade_claims_updated": len(cascade_claims_updated),
            "adjudication_cascade_dependents_reopened": len(cascade_dependents_reopened),
            "unlinked_evidence_runs": len(unlinked_runs),
            "manual_carryover_items": len(carryover_items),
            "manual_carryover_open": len(open_carryover_items),
            "autonomy_triage_items": len(autonomy_triage_items),
            "autonomy_open_decisions": len(autonomy_open_decisions),
            "autonomy_failed_gates": len(autonomy_failed_gates),
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
            "connectome_literature_pull": {
                "prompt": "Review connectome-oriented literature pull queue for architecture-pressure claims.",
                "items_total": len(connectome_pull_items),
                "high_priority_total": len(connectome_pull_high_priority),
                "items": connectome_pull_items,
                "queue_path": "evidence/planning/CONNECTOME_LITERATURE_PULL.md",
            },
            "model_adjudication": {
                "prompt": (
                    "Resolve JEPA-vs-REE conflicts using explicit outcomes and apply cascade rules when REE claims are replaced."
                ),
                "external_precedence_enabled": bool(
                    model_adjudication.get("external_precedence_enabled", False)
                ),
                "default_conflict_outcome": str(
                    model_adjudication.get("default_conflict_outcome", "retain_ree")
                ),
                "allowed_conflict_outcomes": allowed_conflict_outcomes,
                "cascade_policy": {
                    "enabled": bool(cascade_policy.get("enabled", False)),
                    "trigger_outcomes": [
                        str(x).strip()
                        for x in cascade_policy.get("trigger_outcomes", [])
                        if str(x).strip()
                    ],
                    "dependency_reopen_status": str(
                        cascade_policy.get("dependency_reopen_status", "candidate")
                    ),
                    "require_followup_proposals": bool(
                        cascade_policy.get("require_followup_proposals", False)
                    ),
                },
                "temporary_override_mode": {
                    "enabled": bool(temporary_override_mode.get("enabled", False)),
                    "mode_id": str(temporary_override_mode.get("mode_id", "")),
                    "requirements": [
                        str(x).strip()
                        for x in temporary_override_mode.get("requirements", [])
                        if str(x).strip()
                    ],
                },
                "anti_lock_in_gate_enabled": bool(
                    model_adjudication.get("anti_lock_in_gate", {}).get("enabled", False)
                ),
                "external_precedence_candidates": external_precedence_candidates,
                "anti_lock_in_reviews": anti_lock_in_reviews,
            },
            "adjudication_cascade": {
                "prompt": (
                    "Apply approved/applied adjudication outcomes to claims registry and reopen dependents when cascade triggers fire."
                ),
                "last_run_generated_at_utc": str(cascade_last_run.get("generated_at_utc", "")),
                "decision_status_filters": [
                    str(x).strip()
                    for x in cascade_last_run.get("decision_status_filters", [])
                    if str(x).strip()
                ],
                "dry_run": bool(cascade_last_run.get("dry_run", False)),
                "actions_total": len(cascade_actions),
                "claims_updated_total": len(cascade_claims_updated),
                "dependents_reopened_total": len(cascade_dependents_reopened),
                "actions": cascade_actions,
                "patch_queue_path": "evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md",
            },
            "autonomy_triage": {
                "prompt": (
                    "Use this table to keep automation high while preserving explicit human ownership of architecture commitments."
                ),
                "tier_counts": autonomy_tier_counts,
                "open_decisions_total": len(autonomy_open_decisions),
                "failed_gates_total": len(autonomy_failed_gates),
                "items": autonomy_triage_items,
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
            "manual_carryover": {
                "prompt": "Carry forward unfinished manually-tracked governance items.",
                "items_total": len(carryover_items),
                "open_items_total": len(open_carryover_items),
                "items": open_carryover_items,
                "source_path": "evidence/planning/manual_carryover_items.v1.json",
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
    lines.append("### Autonomy Triage")
    lines.append("")
    lines.append("| work_item | tier | gate_status | recommendation | rollback_ready | decision_needed |")
    lines.append("|---|---|---|---|---|---|")
    for item in autonomy_triage_items:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['work_item']}`",
                    f"`{item['tier']}`",
                    f"`{item['gate_status']}`",
                    f"`{item['recommendation']}`",
                    f"`{item['rollback_ready']}`",
                    f"`{item['decision_needed']}`",
                ]
            )
            + " |"
        )
    lines.append("")
    if autonomy_open_decisions:
        lines.append(
            "Open decision items: "
            + ", ".join(f"`{item['work_item']}`" for item in autonomy_open_decisions)
            + "."
        )
    else:
        lines.append("Open decision items: none.")
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
        "4. Manual Carryover: "
        + f"{len(open_carryover_items)} open item(s), {len(carryover_items)} total."
    )
    lines.append("- source: `evidence/planning/manual_carryover_items.v1.json`")
    if open_carryover_items:
        for item in open_carryover_items[:10]:
            item_id = _strip_ticks(str(item.get("item_id", "")))
            owner = _strip_ticks(str(item.get("owner", "")))
            note = str(item.get("summary", ""))
            lines.append(
                f"- `{item_id}` owner=`{owner}` summary={note}"
            )
    lines.append(
        "5. Architecture Structure: "
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
        "6. Structure Dossiers: "
        + f"{structure_review_total} dossier(s), "
        + f"{structure_review_consider} marked consider-new-structure."
    )
    lines.append("- dossier index: `evidence/planning/structure_review/latest/INDEX.md`")
    lines.append(
        "7. Connectome Literature Pull: "
        + f"{len(connectome_pull_items)} queued claim(s), "
        + f"{len(connectome_pull_high_priority)} high-priority."
    )
    lines.append("- connectome queue: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`")
    if connectome_pull_high_priority:
        for item in connectome_pull_high_priority[:10]:
            claim_id = _strip_ticks(str(item.get("claim_id", "")))
            pull_id = _strip_ticks(str(item.get("pull_id", "")))
            lines.append(f"- `{claim_id}` pull_id=`{pull_id}`")
    lines.append(
        "8. Model Adjudication: "
        + f"{len(external_precedence_candidates)} external-precedence candidate(s), "
        + f"{len(anti_lock_in_reviews)} anti-lock-in review item(s)."
    )
    lines.append(
        "- allowed outcomes: "
        + ",".join(allowed_conflict_outcomes)
        if allowed_conflict_outcomes
        else "- allowed outcomes: (none configured)"
    )
    if bool(temporary_override_mode.get("enabled", False)):
        lines.append(
            "- temporary override mode: "
            + f"`{temporary_override_mode.get('mode_id', '')}`"
        )
    if external_precedence_candidates:
        for item in external_precedence_candidates[:10]:
            claim_id = _strip_ticks(str(item.get("claim_id", "")))
            confidence_split = item.get("confidence_split", {})
            delta = float(confidence_split.get("delta_lit_minus_exp", 0.0))
            lines.append(
                f"- `{claim_id}` external_precedence_candidate=yes; "
                + f"delta_lit_minus_exp={delta:.3f}"
            )
    lines.append(
        "9. Adjudication Cascade: "
        + f"{len(cascade_actions)} action(s), "
        + f"{len(cascade_claims_updated)} claim update(s), "
        + f"{len(cascade_dependents_reopened)} dependent reopen(s)."
    )
    lines.append("- patch queue: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`")
    if cascade_actions:
        for action in cascade_actions[:10]:
            claim_id = _strip_ticks(str(action.get("claim_id", "")))
            outcome = _strip_ticks(str(action.get("outcome", "")))
            reopened = action.get("dependents_reopened", [])
            lines.append(
                f"- `{claim_id}` outcome=`{outcome}`; reopened_dependents={len(reopened)}"
            )
    lines.append(
        f"10. Evidence Dispatch: {len(high_proposals)} high-priority proposal(s), {len(proposal_items)} total."
    )
    for slot in _proposal_repo_summary(proposal_items):
        lines.append(
            "- "
            + f"{slot['target_repo']}: total={slot['total']}, "
            + f"experimental={slot['experimental']}, literature_review={slot['literature_review']}"
        )
    lines.append(
        f"11. Maintenance: {len(unlinked_runs)} unlinked evidence run(s), {len(warnings)} warning(s)."
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
        "--skip-task-inbox-sync",
        action="store_true",
        help="Skip markdown checklist inbox sync into manual carryover items.",
    )
    parser.add_argument(
        "--task-inbox-dry-run",
        action="store_true",
        help="Run task inbox sync in dry-run mode.",
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
        "--skip-connectome-pull",
        action="store_true",
        help="Skip connectome literature pull queue generation step.",
    )
    parser.add_argument(
        "--skip-adjudication-cascade",
        action="store_true",
        help="Skip adjudication-cascade application step.",
    )
    parser.add_argument(
        "--adjudication-cascade-statuses",
        default="applied",
        help="Comma-separated decision statuses eligible for adjudication cascade application.",
    )
    parser.add_argument(
        "--adjudication-cascade-dry-run",
        action="store_true",
        help="Run adjudication-cascade step in dry-run mode.",
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
    if not args.skip_task_inbox_sync:
        inbox_cmd = [
            str(sys.executable),
            "evidence/planning/scripts/sync_task_inbox.py",
        ]
        if args.task_inbox_dry_run:
            inbox_cmd.append("--dry-run")
        plan.append(("task_inbox_sync", inbox_cmd))

    if not args.skip_thought_sweep:
        thought_cmd = [str(sys.executable), "docs/thoughts/scripts/thought_sweep.py"]
        if args.strict_thoughts:
            thought_cmd.append("--check-unprocessed")
        plan.append(("thought_sweep", thought_cmd))

    if not args.skip_adjudication_cascade:
        cascade_cmd = [
            str(sys.executable),
            "evidence/planning/scripts/apply_adjudication_cascade.py",
            "--decision-statuses",
            str(args.adjudication_cascade_statuses),
        ]
        if args.adjudication_cascade_dry_run:
            cascade_cmd.append("--dry-run")
        plan.append(("adjudication_cascade", cascade_cmd))
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
    if not args.skip_connectome_pull:
        plan.append(
            (
                "connectome_pull",
                [
                    str(sys.executable),
                    "evidence/planning/scripts/build_connectome_literature_pull.py",
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
        + f"connectome_pull={agenda['summary']['connectome_pull_items']}, "
        + f"external_precedence={agenda['summary']['external_precedence_candidates']}, "
        + f"cascade_actions={agenda['summary']['adjudication_cascade_actions']}, "
        + f"backlog_high={agenda['summary']['backlog_high_priority']}."
    )
    print(f"Agenda JSON: {agenda_json_path.as_posix()}")
    print(f"Agenda MD: {agenda_md_path.as_posix()}")

    if agenda["summary"]["step_failures"] > 0 and not args.continue_on_error:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
