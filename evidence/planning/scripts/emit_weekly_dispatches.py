#!/usr/bin/env python3
"""Generate weekly outbound dispatch bundles from experiment proposals."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _priority_rank(priority: str, order: list[str]) -> int:
    normalized = priority.strip().lower()
    for idx, token in enumerate(order):
        if normalized == token.strip().lower():
            return idx
    return len(order) + 1


def _format_dispatch_md(
    repo_name: str,
    items: list[dict[str, Any]],
    generated_at: str,
    contract_path: str,
    current_epoch: str,
    epoch_start_utc: str,
    planning_criteria_path: str,
) -> str:
    lines: list[str] = []
    lines.append(f"# Weekly Dispatch - {repo_name}")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("## Context")
    lines.append("")
    lines.append("- Source: `evidence/planning/experiment_proposals.v1.json`")
    lines.append(f"- Target repo: `{repo_name}`")
    lines.append(f"- Contract reference: `{contract_path}`")
    if current_epoch:
        lines.append(f"- Architecture epoch: `{current_epoch}`")
        if epoch_start_utc:
            lines.append(f"- Epoch start (UTC): `{epoch_start_utc}`")
        lines.append(f"- Epoch policy source: `{planning_criteria_path}`")
    lines.append("")
    lines.append("## Proposals")
    lines.append("")
    lines.append("| proposal_id | claim_id | priority | experiment_type | dispatch_mode | decision_deadline_utc | objective | acceptance_checks |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for item in items:
        pid = str(item.get("proposal_id", ""))
        claim = str(item.get("claim_id", ""))
        priority = str(item.get("priority", ""))
        exp_type = str(item.get("suggested_experiment_type", "n/a"))
        dispatch_mode = str(item.get("dispatch_mode", "targeted_probe"))
        decision_deadline = str(item.get("decision_deadline_utc", "")).strip() or "n/a"
        objective = str(item.get("objective", "")).replace("|", "\\|")
        checks = "; ".join(str(x) for x in item.get("acceptance_checks", []))
        checks = checks.replace("|", "\\|")
        lines.append(
            f"| `{pid}` | `{claim}` | `{priority}` | `{exp_type}` | `{dispatch_mode}` | `{decision_deadline}` | {objective} | {checks} |"
        )
    lines.append("")
    lines.append("## Copy/Paste Prompt")
    lines.append("")
    lines.append("```md")
    lines.append(f"You are Codex operating in `{repo_name}`.")
    lines.append("")
    lines.append(
        "Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs."
    )
    lines.append("")
    lines.append("Required work items:")
    for item in items:
        pid = str(item.get("proposal_id", ""))
        claim = str(item.get("claim_id", ""))
        exp_type = str(item.get("suggested_experiment_type", "n/a"))
        dispatch_mode = str(item.get("dispatch_mode", "targeted_probe"))
        deadline = str(item.get("decision_deadline_utc", "")).strip()
        outcomes = item.get("decision_required_outcomes", [])
        outcomes_text = ""
        if isinstance(outcomes, list) and outcomes:
            outcomes_text = "|".join(str(x) for x in outcomes if str(x).strip())
        suffix_bits: list[str] = [f"mode={dispatch_mode}"]
        if deadline:
            suffix_bits.append(f"deadline={deadline}")
        if outcomes_text:
            suffix_bits.append(f"required_outcomes={outcomes_text}")
        lines.append(f"- `{pid}` / `{claim}` / `{exp_type}` ({'; '.join(suffix_bits)})")
    lines.append("")
    lines.append("Contract to follow exactly:")
    lines.append(f"- `{contract_path}`")
    lines.append("")
    if current_epoch:
        lines.append("Epoch tagging requirements:")
        lines.append(f"- Stamp every new run `manifest.json` with `\"architecture_epoch\": \"{current_epoch}\"`.")
        if epoch_start_utc:
            lines.append(f"- Keep `timestamp_utc` aligned with the current epoch window (`>= {epoch_start_utc}`).")
        lines.append("")
    lines.append("Acceptance checks per proposal:")
    if any(str(item.get("dispatch_mode", "")) == "discriminative_pair" for item in items):
        lines.append("- Use discriminative pairs (primary vs explicit ablation/control), not broad profile sweeps.")
        lines.append("- Use matched shared seeds across pair conditions and pre-register thresholds before execution.")
    lines.append("- At least 2 additional runs with distinct seeds unless stricter pair checks are specified in proposal acceptance checks.")
    lines.append("- Experiment Pack validates against v1 schema.")
    if current_epoch:
        lines.append(f"- Each emitted manifest includes `architecture_epoch={current_epoch}`.")
    lines.append("- Result links to claim_ids_tested and updates matrix direction counts.")
    lines.append("")
    lines.append("Output required:")
    lines.append("- concise run table: run_id, seed, status, key metrics, evidence_direction")
    lines.append("- list of generated run pack paths")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit weekly dispatch markdown bundles.")
    parser.add_argument(
        "--config",
        default="evidence/planning/cadence_automation.v1.json",
        help="Path to cadence automation config.",
    )
    parser.add_argument(
        "--proposals",
        default="evidence/planning/experiment_proposals.v1.json",
        help="Path to experiment proposals JSON.",
    )
    parser.add_argument(
        "--planning-criteria",
        default="evidence/planning/planning_criteria.v1.yaml",
        help="Path to planning criteria (JSON-compatible YAML).",
    )
    parser.add_argument(
        "--date",
        default="auto",
        help="Date label for output folder (YYYY-MM-DD) or 'auto'.",
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=[],
        help="Explicit target repos; defaults to producer_repo_order in config.",
    )
    parser.add_argument(
        "--max-items-per-repo",
        type=int,
        default=0,
        help="Override max proposals per repo (0 = config default).",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    config_path = repo_root / args.config
    proposals_path = repo_root / args.proposals
    planning_criteria_path = repo_root / args.planning_criteria
    config = _load_json(config_path)
    proposals = _load_json(proposals_path)
    planning_criteria = _load_json(planning_criteria_path)
    evidence_applicability = (
        planning_criteria.get("evidence_applicability", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(evidence_applicability, dict):
        evidence_applicability = {}
    current_epoch = str(evidence_applicability.get("current_architecture_epoch", "")).strip()
    epoch_start_utc = str(evidence_applicability.get("epoch_start_utc", "")).strip()

    dispatch_cfg = config.get("dispatch", {}) if isinstance(config, dict) else {}
    out_root_rel = str(dispatch_cfg.get("default_output_root", "evidence/planning/outbound_dispatches"))
    out_root = repo_root / out_root_rel
    max_items = int(dispatch_cfg.get("max_items_per_repo", 8))
    if args.max_items_per_repo > 0:
        max_items = args.max_items_per_repo

    priority_order = [str(x) for x in dispatch_cfg.get("priority_order", ["high", "medium", "low"])]
    default_repo_order = [
        str(x)
        for x in dispatch_cfg.get(
            "producer_repo_order",
            ["ree-v2", "ree-experiments-lab", "ree-v1-minimal"],
        )
    ]
    target_repos = list(args.repos) if args.repos else default_repo_order

    if args.date == "auto":
        date_label = date.today().isoformat()
    else:
        date_label = args.date

    out_dir = out_root / date_label
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_at = _now_utc()

    items = proposals.get("items", []) if isinstance(proposals, dict) else []
    experimental_items = [
        item for item in items if str(item.get("proposal_type", "")).strip() == "experimental"
    ]

    report: dict[str, Any] = {
        "schema_version": "weekly_dispatch_report/v1",
        "generated_at_utc": generated_at,
        "output_dir": out_dir.as_posix(),
        "current_architecture_epoch": current_epoch,
        "epoch_start_utc": epoch_start_utc,
        "planning_criteria_path": planning_criteria_path.as_posix(),
        "targets": [],
    }

    contract_path = "evidence/experiments/INTERFACE_CONTRACT.md"
    for repo_name in target_repos:
        filtered = [
            item
            for item in experimental_items
            if str(item.get("target_repo", "")).strip() == repo_name
        ]
        filtered.sort(
            key=lambda item: (
                _priority_rank(str(item.get("priority", "low")), priority_order),
                str(item.get("proposal_id", "")),
            )
        )
        selected = filtered[:max_items]
        out_path = out_dir / f"{repo_name}_weekly_dispatch.md"
        out_path.write_text(
            _format_dispatch_md(
                repo_name=repo_name,
                items=selected,
                generated_at=generated_at,
                contract_path=contract_path,
                current_epoch=current_epoch,
                epoch_start_utc=epoch_start_utc,
                planning_criteria_path=args.planning_criteria,
            ),
            encoding="utf-8",
        )
        report["targets"].append(
            {
                "repo_name": repo_name,
                "proposal_count": len(selected),
                "output_path": out_path.as_posix(),
            }
        )

    report_path = out_dir / "dispatch_report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote dispatch bundles: {out_dir}")
    print(f"Wrote report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
