#!/usr/bin/env python3
"""Run REE-v2 cutover readiness checks with adjudicated-divergence support."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REQUIRED_CLAIMS = ["MECH-056", "MECH-058", "MECH-059", "MECH-060"]
REQUIRED_V2_GATES = [
    "schema_validation",
    "seed_determinism",
    "hook_surface_coverage",
    "remote_export_import",
]

CLAIM_METRIC_DIRECTIONS: dict[str, dict[str, str]] = {
    "MECH-056": {
        "ledger_edit_detected_count": "lower",
        "explanation_policy_divergence_rate": "lower",
        "domination_lock_in_events": "lower",
        "commitment_reversal_rate": "lower",
    },
    "MECH-058": {
        "latent_prediction_error_mean": "lower",
        "latent_prediction_error_p95": "lower",
        "latent_rollout_consistency_rate": "higher",
        "e1_e2_timescale_separation_ratio": "higher",
        "representation_drift_rate": "lower",
    },
    "MECH-059": {
        "latent_prediction_error_mean": "lower",
        "latent_uncertainty_calibration_error": "lower",
        "precision_input_completeness_rate": "higher",
        "uncertainty_coverage_rate": "higher",
    },
    "MECH-060": {
        "pre_commit_error_signal_to_noise": "higher",
        "post_commit_error_attribution_gain": "higher",
        "cross_channel_leakage_rate": "lower",
        "commitment_reversal_rate": "lower",
    },
}


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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

    out: list[str] = []
    for line in lines[start_idx:]:
        if line.startswith("## "):
            break
        out.append(line)
    return out


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
        rows.append({header[i]: cells[i] for i in range(len(header))})
    return rows


def _parse_key_value_bullets(lines: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        body = stripped[2:]
        if ":" not in body:
            continue
        key, value = body.split(":", 1)
        out[key.strip()] = _strip_ticks(value.strip())
    return out


def _run_capture(command: list[str]) -> str:
    return subprocess.check_output(command, text=True)


def _parse_int(raw: str) -> int:
    try:
        return int(_strip_ticks(raw))
    except ValueError:
        return 0


def _direction_from_claim_summary_row(row: dict[str, str] | None) -> str:
    if row is None:
        return "unknown"

    supports = _parse_int(row.get("supports", "0"))
    weakens = _parse_int(row.get("weakens", "0"))
    mixed = _parse_int(row.get("mixed", "0"))
    unknown = _parse_int(row.get("unknown", "0"))

    if mixed > 0:
        return "mixed"
    if supports > 0 and weakens > 0:
        return "mixed"
    if supports > 0:
        return "supports"
    if weakens > 0:
        return "weakens"
    if unknown > 0:
        return "unknown"
    return "unknown"


def _parse_schema_versions(schema_version_set: str) -> set[str]:
    return {
        token.strip()
        for token in schema_version_set.split(",")
        if token.strip()
    }


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_handoff_snapshot(repo_name: str, repo_path: Path, rel_path: str, revision: str) -> dict[str, Any]:
    text = _run_capture(["git", "-C", str(repo_path), "show", f"{revision}:{rel_path}"])
    lines = text.splitlines()

    metadata = _parse_key_value_bullets(_extract_section(lines, "## Metadata"))
    contract_sync = _parse_key_value_bullets(_extract_section(lines, "## Contract Sync"))
    ci_rows = _parse_markdown_table(_extract_section(lines, "## CI Gates"))
    inventory_rows = _parse_markdown_table(_extract_section(lines, "## Run-Pack Inventory"))
    claim_rows = _parse_markdown_table(_extract_section(lines, "## Claim Summary"))

    claims: set[str] = set()
    for row in inventory_rows:
        for token in row.get("claim_ids_tested", "").split(","):
            claim_id = _strip_ticks(token)
            if claim_id and claim_id != "N/A":
                claims.add(claim_id)

    blockers = [
        line.strip()
        for line in _extract_section(lines, "## Open Blockers")
        if line.strip()
    ]

    return {
        "repo_name": repo_name,
        "repo_path": repo_path.as_posix(),
        "handoff_path": f"{repo_path.as_posix()}/{rel_path}",
        "revision": revision,
        "week_of_utc": metadata.get("week_of_utc", "unknown"),
        "generated_utc": metadata.get("generated_utc", "unknown"),
        "schema_version_set": contract_sync.get("schema_version_set", ""),
        "ci_gates": {row.get("gate", ""): _strip_ticks(row.get("status", "")) for row in ci_rows},
        "inventory_rows": inventory_rows,
        "claim_summary_rows": {
            _strip_ticks(row.get("claim_id", "")): row for row in claim_rows if row.get("claim_id", "")
        },
        "run_pack_claim_ids": sorted(claims),
        "open_blockers": blockers,
        "raw_text": text,
    }


def _load_latest_handoff_snapshots(
    repo_name: str,
    repo_path: Path,
    rel_path: str,
    max_count: int,
) -> list[dict[str, Any]]:
    revisions = _run_capture(
        ["git", "-C", str(repo_path), "log", "--format=%H", "--", rel_path]
    ).splitlines()
    snapshots: list[dict[str, Any]] = []
    for revision in revisions[:max_count]:
        snapshots.append(_load_handoff_snapshot(repo_name, repo_path, rel_path, revision))
    return snapshots


def _latest_ingestion_reports(repo_root: Path, max_count: int) -> list[dict[str, Any]]:
    report_paths = sorted(
        (repo_root / "evidence/planning/handoff_sync_reports").glob("*_handoff_sync_report.json"),
        reverse=True,
    )
    selected: list[dict[str, Any]] = []
    for path in report_paths:
        data = _load_json(path)
        if not data.get("ingestion_steps"):
            continue
        selected.append(
            {
                "file_path": path.as_posix(),
                "generated_at_utc": data.get("generated_at_utc"),
                "targets": data.get("targets", []),
                "repo_statuses": {
                    row.get("repo_name", "unknown"): row.get("status", "unknown")
                    for row in data.get("results", [])
                },
                "ingestion_step_statuses": [
                    {
                        "command": " ".join(step.get("command", [])),
                        "status": step.get("status", "unknown"),
                        "returncode": step.get("returncode", -1),
                    }
                    for step in data.get("ingestion_steps", [])
                ],
            }
        )
        if len(selected) >= max_count:
            break
    return selected


def _seed_from_row(row: dict[str, str]) -> int | None:
    raw = _strip_ticks(row.get("seed", ""))
    try:
        return int(raw)
    except ValueError:
        return None


def _claim_rows(snapshot: dict[str, Any], claim_id: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in snapshot.get("inventory_rows", []):
        claim_tokens = [
            _strip_ticks(token)
            for token in row.get("claim_ids_tested", "").split(",")
            if _strip_ticks(token)
        ]
        if claim_id in claim_tokens:
            rows.append(row)
    return rows


def _collect_conditions_and_seeds(snapshot: dict[str, Any], claim_id: str) -> tuple[set[str], set[int]]:
    conditions: set[str] = set()
    seeds: set[int] = set()
    for row in _claim_rows(snapshot, claim_id):
        condition = _strip_ticks(row.get("condition_or_scenario", ""))
        if condition:
            conditions.add(condition)
        seed = _seed_from_row(row)
        if seed is not None:
            seeds.add(seed)
    return conditions, seeds


def _load_metrics_for_row(repo_path: Path, row: dict[str, str]) -> dict[str, float]:
    pack_path = _strip_ticks(row.get("pack_path", ""))
    if not pack_path:
        return {}
    pack = Path(pack_path)
    if not pack.is_absolute():
        pack = repo_path / pack
    metrics_path = pack / "metrics.json"
    if not metrics_path.exists():
        return {}
    data = _load_json(metrics_path)
    values = data.get("values", {})
    if not isinstance(values, dict):
        return {}
    out: dict[str, float] = {}
    for key, value in values.items():
        if isinstance(value, (int, float)):
            out[str(key)] = float(value)
    return out


def _seed_metric_average(
    snapshot: dict[str, Any],
    claim_id: str,
    metric_key: str,
    seed: int,
    allowed_conditions: set[str],
) -> float | None:
    samples: list[float] = []
    repo_path = Path(snapshot["repo_path"])
    for row in _claim_rows(snapshot, claim_id):
        if _seed_from_row(row) != seed:
            continue
        condition = _strip_ticks(row.get("condition_or_scenario", ""))
        if allowed_conditions and condition not in allowed_conditions:
            continue
        metrics = _load_metrics_for_row(repo_path, row)
        if metric_key in metrics:
            samples.append(metrics[metric_key])
    if not samples:
        return None
    return sum(samples) / len(samples)


def _compare_metric(direction: str, v2_value: float, v1_value: float) -> bool:
    if direction == "higher":
        return v2_value > v1_value
    return v2_value < v1_value


def _evaluate_metric_improvement(
    claim_id: str,
    v2_snapshot: dict[str, Any],
    v1_snapshot: dict[str, Any],
) -> tuple[bool, dict[str, Any]]:
    metric_directions = CLAIM_METRIC_DIRECTIONS.get(claim_id, {})
    v2_conditions, v2_seeds = _collect_conditions_and_seeds(v2_snapshot, claim_id)
    v1_conditions, v1_seeds = _collect_conditions_and_seeds(v1_snapshot, claim_id)
    common_conditions = v2_conditions & v1_conditions
    common_seeds = sorted(v2_seeds & v1_seeds)

    metric_outcomes: dict[str, Any] = {}
    metrics_passing = 0

    for metric_key, direction in metric_directions.items():
        per_seed: dict[str, Any] = {}
        improved_seed_count = 0
        compared_seed_count = 0
        for seed in common_seeds:
            v2_value = _seed_metric_average(v2_snapshot, claim_id, metric_key, seed, common_conditions)
            v1_value = _seed_metric_average(v1_snapshot, claim_id, metric_key, seed, common_conditions)
            if v2_value is None or v1_value is None:
                per_seed[str(seed)] = {"compared": False}
                continue
            improved = _compare_metric(direction, v2_value, v1_value)
            per_seed[str(seed)] = {
                "compared": True,
                "v2": v2_value,
                "v1": v1_value,
                "improved": improved,
            }
            compared_seed_count += 1
            if improved:
                improved_seed_count += 1

        metric_pass = compared_seed_count >= 2 and improved_seed_count >= 2
        metric_outcomes[metric_key] = {
            "direction": direction,
            "compared_seed_count": compared_seed_count,
            "improved_seed_count": improved_seed_count,
            "passes_two_of_three_seed_rule": metric_pass,
            "per_seed": per_seed,
        }
        if metric_pass:
            metrics_passing += 1

    claim_pass = metrics_passing >= 3
    detail = {
        "common_conditions": sorted(common_conditions),
        "common_seeds": common_seeds,
        "metrics_passing": metrics_passing,
        "metric_outcomes": metric_outcomes,
        "passes_rule": claim_pass,
    }
    return claim_pass, detail


def _v2_governance_note_checks(v2_snapshot: dict[str, Any], claim_id: str) -> tuple[bool, dict[str, bool]]:
    text = v2_snapshot.get("raw_text", "")
    lines = [line.strip() for line in text.splitlines()]

    has_section = bool(
        re.search(r"^##\\s+Parity Delta Summary vs ree-v1-minimal\\b", text, flags=re.IGNORECASE | re.MULTILINE)
    )

    claim_line = next((line for line in lines if claim_id in line), "")
    has_adjudicated_marker = bool(
        claim_line and re.search(r"adjudicated|superior", claim_line, flags=re.IGNORECASE)
    )
    has_rationale = bool(
        re.search(rf"{re.escape(claim_id)}.*rationale|rationale.*{re.escape(claim_id)}", text, flags=re.IGNORECASE)
    )
    has_rollback_trigger = bool(
        re.search(
            rf"{re.escape(claim_id)}.*rollback trigger|rollback trigger.*{re.escape(claim_id)}",
            text,
            flags=re.IGNORECASE,
        )
    ) or bool(re.search(r"rollback trigger", text, flags=re.IGNORECASE))

    checks = {
        "has_parity_delta_section": has_section,
        "has_claim_adjudicated_marker": has_adjudicated_marker,
        "has_claim_rationale": has_rationale,
        "has_claim_rollback_trigger": has_rollback_trigger,
    }
    return all(checks.values()), checks


def _lab_has_unaddressed_p0_for_claim(lab_snapshot: dict[str, Any], claim_id: str) -> tuple[bool, list[str]]:
    hits = []
    for line in lab_snapshot.get("open_blockers", []):
        if claim_id in line and re.search(r"\bP0\b", line, flags=re.IGNORECASE):
            hits.append(line)
    return len(hits) > 0, hits


def _evaluate_overlap_gate(
    v2_snapshot: dict[str, Any],
    v1_snapshot: dict[str, Any],
    lab_snapshot: dict[str, Any],
    v2_ci_pass: bool,
    no_contract_drift: bool,
) -> tuple[bool, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    unresolved = 0

    for claim_id in REQUIRED_CLAIMS:
        v2_direction = _direction_from_claim_summary_row(v2_snapshot.get("claim_summary_rows", {}).get(claim_id))
        v1_direction = _direction_from_claim_summary_row(v1_snapshot.get("claim_summary_rows", {}).get(claim_id))
        same_direction = v2_direction == v1_direction

        v2_conditions, v2_seeds = _collect_conditions_and_seeds(v2_snapshot, claim_id)
        v1_conditions, v1_seeds = _collect_conditions_and_seeds(v1_snapshot, claim_id)
        schema_set_v2 = _parse_schema_versions(v2_snapshot.get("schema_version_set", ""))
        schema_set_v1 = _parse_schema_versions(v1_snapshot.get("schema_version_set", ""))

        protocol_matched = (
            len(v2_seeds & v1_seeds) >= 3
            and len(v2_conditions & v1_conditions) >= 2
            and schema_set_v2 == schema_set_v1
        )

        metric_improved, metric_detail = _evaluate_metric_improvement(claim_id, v2_snapshot, v1_snapshot)
        lab_has_p0, lab_p0_lines = _lab_has_unaddressed_p0_for_claim(lab_snapshot, claim_id)
        gov_note_ok, gov_note_checks = _v2_governance_note_checks(v2_snapshot, claim_id)

        adjudication_checks = {
            "matched_protocol_evidence": protocol_matched,
            "ree_v2_ci_gates_pass": v2_ci_pass,
            "ree_v2_metric_improvement_rule": metric_improved,
            "no_contract_drift_signatures": no_contract_drift,
            "no_unaddressed_lab_p0_falsification": not lab_has_p0,
            "governance_note_with_rationale_and_rollback_trigger": gov_note_ok,
        }
        adjudicated_v2_superior = all(adjudication_checks.values())

        status = "resolved"
        unresolved_conflict = False
        if same_direction:
            status = "resolved"
        elif adjudicated_v2_superior:
            status = "adjudicated_v2_superior"
        else:
            status = "unresolved_conflict"
            unresolved_conflict = True
            unresolved += 1

        rows.append(
            {
                "claim_id": claim_id,
                "ree_v2_direction": v2_direction,
                "ree_v1_direction": v1_direction,
                "delta": "same" if same_direction else "different",
                "status": status,
                "unresolved_conflict": unresolved_conflict,
                "adjudication_checks": adjudication_checks,
                "metric_improvement_detail": metric_detail,
                "lab_p0_falsification_lines": lab_p0_lines,
                "governance_note_checks": gov_note_checks,
                "protocol_match_detail": {
                    "v2_conditions": sorted(v2_conditions),
                    "v1_conditions": sorted(v1_conditions),
                    "v2_seeds": sorted(v2_seeds),
                    "v1_seeds": sorted(v1_seeds),
                    "v2_schema_versions": sorted(schema_set_v2),
                    "v1_schema_versions": sorted(schema_set_v1),
                },
            }
        )

    return unresolved == 0, rows


def _load_latest_lab_snapshot(repo_path: Path, rel_path: str) -> dict[str, Any]:
    rev = _run_capture(["git", "-C", str(repo_path), "log", "--format=%H", "--", rel_path]).splitlines()[0]
    return _load_handoff_snapshot("ree-experiments-lab", repo_path, rel_path, rev)


def _contract_signature_hits(repo_root: Path) -> list[dict[str, str]]:
    matrix_path = repo_root / "evidence/experiments/claim_evidence.v1.json"
    if not matrix_path.exists():
        return []
    matrix = _load_json(matrix_path)
    hits: list[dict[str, str]] = []
    for entry in matrix.get("entries", []):
        for signature in entry.get("failure_signatures", []) or []:
            if str(signature).startswith("contract:"):
                hits.append(
                    {
                        "claim_id": str(entry.get("claim_id", "")),
                        "run_id": str(entry.get("run_id", "")),
                        "signature": str(signature),
                    }
                )
    return hits


def _write_markdown_report(path: Path, report: dict[str, Any]) -> None:
    gates = report["gates"]
    overlap_rows = report["overlap_adjudication"]
    blockers = report["blockers"]
    inputs = report["inputs"]

    lines: list[str] = []
    lines.append("# REE-v2 Cutover Readiness Report")
    lines.append("")
    lines.append(f"Generated: `{report['generated_at_utc']}`")
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    lines.append(f"- decision: `{report['decision']}`")
    lines.append(f"- routing_change_applied: `{str(report['routing_change_applied']).lower()}`")
    lines.append("")
    lines.append("## Gate Results")
    lines.append("")
    lines.append("| gate_id | status |")
    lines.append("| --- | --- |")
    for gate in gates:
        lines.append(f"| `{gate['gate_id']}` | `{gate['status']}` |")
    lines.append("")

    lines.append("## Overlap Adjudication")
    lines.append("")
    lines.append("| claim_id | ree_v2_direction | ree_v1_direction | status |")
    lines.append("| --- | --- | --- | --- |")
    for row in overlap_rows:
        lines.append(
            f"| `{row['claim_id']}` | `{row['ree_v2_direction']}` | `{row['ree_v1_direction']}` | `{row['status']}` |"
        )
    lines.append("")

    lines.append("## Blockers (Prioritized)")
    lines.append("")
    if not blockers:
        lines.append("- none")
    else:
        for item in blockers:
            lines.append(f"### {item['priority']} - {item['blocker']}")
            lines.append("")
            lines.append("Evidence:")
            lines.append(f"- `{json.dumps(item['evidence'], ensure_ascii=True)}`")
            lines.append("Remediation actions:")
            for action in item["remediation"]:
                lines.append(f"- {action}")
            lines.append("")

    lines.append("## Input Snapshots Used")
    lines.append("")
    for snap in inputs["ree_v2_handoff_snapshots"]:
        lines.append(
            f"- ree-v2 handoff: `{snap['handoff_path']}` @ `{snap['revision'][:12]}` generated `{snap['generated_utc']}`"
        )
    for snap in inputs["ree_v1_handoff_snapshots"]:
        lines.append(
            f"- ree-v1-minimal handoff: `{snap['handoff_path']}` @ `{snap['revision'][:12]}` generated `{snap['generated_utc']}`"
        )
    lines.append(
        f"- ree-experiments-lab handoff: `{inputs['ree_lab_handoff_snapshot']['handoff_path']}` @ "
        f"`{inputs['ree_lab_handoff_snapshot']['revision'][:12]}` generated "
        f"`{inputs['ree_lab_handoff_snapshot']['generated_utc']}`"
    )
    for rpt in inputs["latest_thursday_ingestion_reports"]:
        lines.append(f"- ingestion report: `{rpt['file_path']}`")
    lines.append("")

    lines.append("## Rollback Instructions")
    lines.append("")
    for step in report["rollback_instructions"]:
        lines.append(f"- {step}")
    lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _append_cutover_changelog(changelog_path: Path, generated_at: str) -> None:
    date_label = generated_at[:10]
    section_lines = [
        f"## {date_label}: REE-v2 Qualification Routing Cutover",
        "",
        "### Overview",
        "",
        "Adopted adjudicated-divergence cutover policy and switched default experimental routing to `ree-v2` after",
        "all readiness gates passed.",
        "",
        "### What Changed",
        "",
        "- Updated planning routing default:",
        "  - `evidence/planning/planning_criteria.v1.yaml` (`experimental_default_repo=ree-v2`)",
        "- Generated cutover readiness artifacts:",
        "  - `evidence/planning/CUTOVER_REE_V2_READINESS.md`",
        "  - `evidence/planning/CUTOVER_REE_V2_READINESS.v1.json`",
        "",
    ]
    original = changelog_path.read_text(encoding="utf-8")
    if section_lines[0] in original:
        return
    changelog_path.write_text(original.rstrip() + "\n\n" + "\n".join(section_lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run REE-v2 cutover readiness checks with adjudicated-divergence mode."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--ree-v2-repo",
        type=Path,
        default=Path("/Users/dgolden/Documents/GitHub/ree-v2"),
        help="Path to ree-v2 repository.",
    )
    parser.add_argument(
        "--ree-v1-repo",
        type=Path,
        default=Path("/Users/dgolden/Documents/GitHub/ree-v1-minimal"),
        help="Path to ree-v1-minimal repository.",
    )
    parser.add_argument(
        "--ree-lab-repo",
        type=Path,
        default=Path("/Users/dgolden/Documents/GitHub/ree-experiments-lab"),
        help="Path to ree-experiments-lab repository.",
    )
    parser.add_argument(
        "--handoff-relative-path",
        default="evidence/planning/weekly_handoff/latest.md",
        help="Relative handoff path inside producer repositories.",
    )
    parser.add_argument(
        "--snapshots-per-repo",
        type=int,
        default=2,
        help="How many latest handoff snapshots to evaluate for v1/v2.",
    )
    parser.add_argument(
        "--ingestion-reports",
        type=int,
        default=2,
        help="How many latest ingestion reports to include.",
    )
    parser.add_argument(
        "--planning-criteria",
        default="evidence/planning/planning_criteria.v1.yaml",
        help="Planning criteria config path (JSON-in-YAML file).",
    )
    parser.add_argument(
        "--changelog",
        default="docs/changelog.md",
        help="Changelog file to append cutover note when cutover is applied.",
    )
    parser.add_argument(
        "--output-json",
        default="evidence/planning/CUTOVER_REE_V2_READINESS.v1.json",
        help="Readiness JSON output path.",
    )
    parser.add_argument(
        "--output-md",
        default="evidence/planning/CUTOVER_REE_V2_READINESS.md",
        help="Readiness markdown output path.",
    )
    parser.add_argument(
        "--apply-cutover",
        action="store_true",
        help="Apply routing cutover when all gates pass.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    output_json = (repo_root / args.output_json).resolve()
    output_md = (repo_root / args.output_md).resolve()
    planning_criteria_path = (repo_root / args.planning_criteria).resolve()
    changelog_path = (repo_root / args.changelog).resolve()

    v2_snapshots = _load_latest_handoff_snapshots(
        "ree-v2",
        args.ree_v2_repo.resolve(),
        args.handoff_relative_path,
        args.snapshots_per_repo,
    )
    v1_snapshots = _load_latest_handoff_snapshots(
        "ree-v1-minimal",
        args.ree_v1_repo.resolve(),
        args.handoff_relative_path,
        args.snapshots_per_repo,
    )
    lab_snapshot = _load_latest_lab_snapshot(args.ree_lab_repo.resolve(), args.handoff_relative_path)
    ingestion_reports = _latest_ingestion_reports(repo_root, args.ingestion_reports)

    if not v2_snapshots or not v1_snapshots:
        raise SystemExit("Missing required v2/v1 handoff snapshots.")

    v2_latest = v2_snapshots[0]
    v1_latest = v1_snapshots[0]

    v2_ci_failures: list[str] = []
    for snapshot in v2_snapshots:
        for gate in REQUIRED_V2_GATES:
            status = _strip_ticks(snapshot["ci_gates"].get(gate, "MISSING")).upper()
            if status != "PASS":
                v2_ci_failures.append(f"{snapshot['revision'][:12]}:{gate}={status}")
    gate_v2_ci = len(v2_ci_failures) == 0

    v2_claim_set = set(v2_latest["run_pack_claim_ids"])
    missing_claims = [claim for claim in REQUIRED_CLAIMS if claim not in v2_claim_set]
    gate_claim_coverage = len(missing_claims) == 0

    contract_hits = _contract_signature_hits(repo_root)
    gate_contract_drift = len(contract_hits) == 0

    p0_lines = [
        line
        for line in v2_latest["open_blockers"]
        if re.search(r"\bP0\b", line, flags=re.IGNORECASE)
    ]
    gate_no_p0_text = len(p0_lines) == 0

    overlap_gate_ok, overlap_rows = _evaluate_overlap_gate(
        v2_snapshot=v2_latest,
        v1_snapshot=v1_latest,
        lab_snapshot=lab_snapshot,
        v2_ci_pass=gate_v2_ci,
        no_contract_drift=gate_contract_drift,
    )

    gates = [
        {
            "gate_id": "v2_ci_gates_all_pass",
            "status": "PASS" if gate_v2_ci else "FAIL",
            "evidence": {
                "required_gates": REQUIRED_V2_GATES,
                "snapshots_checked": [item["revision"][:12] for item in v2_snapshots],
                "failures": v2_ci_failures,
            },
        },
        {
            "gate_id": "v2_required_claim_coverage",
            "status": "PASS" if gate_claim_coverage else "FAIL",
            "evidence": {
                "required_claims": REQUIRED_CLAIMS,
                "ree_v2_claims_present": sorted(v2_claim_set),
                "missing_claims": missing_claims,
            },
        },
        {
            "gate_id": "no_unresolved_contract_drift_signatures",
            "status": "PASS" if gate_contract_drift else "FAIL",
            "evidence": {
                "contract_signature_hit_count": len(contract_hits),
                "hits": contract_hits[:20],
            },
        },
        {
            "gate_id": "no_p0_blocker_text_in_latest_v2_handoff",
            "status": "PASS" if gate_no_p0_text else "FAIL",
            "evidence": {
                "p0_lines": p0_lines,
                "open_blockers": v2_latest["open_blockers"],
            },
        },
        {
            "gate_id": "overlap_sanity_adjudicated_or_resolved",
            "status": "PASS" if overlap_gate_ok else "FAIL",
            "evidence": {
                "overlap_adjudication": overlap_rows,
            },
        },
    ]

    all_pass = all(item["status"] == "PASS" for item in gates)
    decision = "CUTOVER_DONE" if all_pass and args.apply_cutover else "NO_CUTOVER"

    blockers: list[dict[str, Any]] = []
    unresolved_rows = [row for row in overlap_rows if row["status"] == "unresolved_conflict"]
    if unresolved_rows:
        blockers.append(
            {
                "priority": "P0",
                "blocker": (
                    "Unresolved overlap claims remain after adjudication checks. "
                    "Mismatches are allowed only when `adjudicated_v2_superior` criteria pass."
                ),
                "evidence": unresolved_rows,
                "remediation": [
                    "Run matched-seed and matched-condition parity cycles in ree-v2 and ree-v1-minimal.",
                    "Add per-claim parity adjudication notes in ree-v2 handoff with rationale and rollback trigger.",
                    "Re-run this cutover checker and require overlap gate PASS in two consecutive cycles before cutover.",
                ],
            }
        )
    if not gate_v2_ci:
        blockers.append(
            {
                "priority": "P0",
                "blocker": "Required ree-v2 CI gates are not all PASS.",
                "evidence": v2_ci_failures,
                "remediation": [
                    "Fix failing gate(s) in ree-v2 and regenerate weekly handoff evidence.",
                    "Re-run cutover checker after sync/ingestion refresh.",
                ],
            }
        )
    if not gate_claim_coverage:
        blockers.append(
            {
                "priority": "P0",
                "blocker": "ree-v2 latest handoff does not cover all required claims.",
                "evidence": {"missing_claims": missing_claims},
                "remediation": [
                    "Emit at least one contract-valid run pack for each missing claim in ree-v2.",
                    "Regenerate and validate weekly handoff.",
                ],
            }
        )
    if not gate_contract_drift:
        blockers.append(
            {
                "priority": "P0",
                "blocker": "Contract drift signatures detected in claim evidence matrix.",
                "evidence": contract_hits[:20],
                "remediation": [
                    "Repair producer schema/adapter emissions causing contract signatures.",
                    "Rebuild experiment indexes and verify zero contract:* signatures.",
                ],
            }
        )
    if not gate_no_p0_text:
        blockers.append(
            {
                "priority": "P0",
                "blocker": "Latest ree-v2 handoff includes P0 blockers.",
                "evidence": p0_lines,
                "remediation": [
                    "Resolve or explicitly downgrade P0 blockers before cutover.",
                    "Publish updated handoff state and re-run checker.",
                ],
            }
        )

    routing_change_applied = False
    rollback_steps = [
        "If routing is flipped and rollback is needed: set "
        "`repo_routing.experimental_default_repo` back to `ree-v1-minimal` in "
        "`evidence/planning/planning_criteria.v1.yaml`, then regenerate planning outputs.",
    ]
    if all_pass and args.apply_cutover:
        planning_criteria = _load_json(planning_criteria_path)
        repo_routing = planning_criteria.setdefault("repo_routing", {})
        repo_routing["experimental_default_repo"] = "ree-v2"
        planning_criteria_path.write_text(
            json.dumps(planning_criteria, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        _append_cutover_changelog(changelog_path, _now_utc())
        routing_change_applied = True
        rollback_steps = [
            "Set `repo_routing.experimental_default_repo` to `ree-v1-minimal` in "
            "`evidence/planning/planning_criteria.v1.yaml`.",
            "Run `python3 evidence/experiments/scripts/build_experiment_indexes.py`.",
            "Run `python3 evidence/planning/scripts/run_governance_cycle.py`.",
            "Run `python3 evidence/planning/scripts/emit_weekly_dispatches.py`.",
        ]

    report = {
        "schema_version": "ree_v2_cutover_readiness/v2",
        "generated_at_utc": _now_utc(),
        "decision": decision,
        "routing_change_applied": routing_change_applied,
        "required_claims": REQUIRED_CLAIMS,
        "inputs": {
            "ree_v2_handoff_snapshots": [
                {
                    "handoff_path": item["handoff_path"],
                    "revision": item["revision"],
                    "generated_utc": item["generated_utc"],
                    "week_of_utc": item["week_of_utc"],
                }
                for item in v2_snapshots
            ],
            "ree_v1_handoff_snapshots": [
                {
                    "handoff_path": item["handoff_path"],
                    "revision": item["revision"],
                    "generated_utc": item["generated_utc"],
                    "week_of_utc": item["week_of_utc"],
                }
                for item in v1_snapshots
            ],
            "ree_lab_handoff_snapshot": {
                "handoff_path": lab_snapshot["handoff_path"],
                "revision": lab_snapshot["revision"],
                "generated_utc": lab_snapshot["generated_utc"],
                "week_of_utc": lab_snapshot["week_of_utc"],
            },
            "latest_thursday_ingestion_reports": ingestion_reports,
        },
        "gates": gates,
        "overlap_adjudication": overlap_rows,
        "blockers": blockers,
        "rollback_instructions": rollback_steps,
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    _write_markdown_report(output_md, report)

    print(f"Wrote readiness JSON: {output_json}")
    print(f"Wrote readiness markdown: {output_md}")
    print(f"Decision: {decision}")
    for gate in gates:
        print(f"- {gate['gate_id']}: {gate['status']}")

    return 0 if (all_pass or not args.apply_cutover) else 1


if __name__ == "__main__":
    raise SystemExit(main())
