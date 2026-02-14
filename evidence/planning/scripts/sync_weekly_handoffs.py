#!/usr/bin/env python3
"""Pull weekly handoffs from producer repos and import run packs.

Designed for local scheduled execution (cron/launchd) in REE_assembly.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


WEEKDAYS = [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


@dataclass
class RepoConfig:
    name: str
    path: Path
    handoff_globs: list[str]


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _run(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def _extract_section(lines: list[str], heading: str) -> list[str]:
    start = None
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            start = idx + 1
            break
    if start is None:
        return []
    collected: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        collected.append(line)
    return collected


def _parse_markdown_table(lines: list[str]) -> list[dict[str, str]]:
    table_lines = [line.strip() for line in lines if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return []
    header = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    out: list[dict[str, str]] = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        row = {header[i]: cells[i] for i in range(len(header))}
        out.append(row)
    return out


def _latest_handoff(repo: RepoConfig) -> Path | None:
    candidates: list[Path] = []
    for glob_pat in repo.handoff_globs:
        candidates.extend(repo.path.glob(glob_pat))
    files = [p for p in candidates if p.is_file()]
    if not files:
        return None
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0]


def _status_is_fail(status: str) -> bool:
    return status.strip().upper() == "FAIL"


def _normalize_cell(cell: str) -> str:
    return cell.strip().strip("`")


def _validate_handoff(
    handoff_path: Path,
    required_ci_gates: list[str],
    required_columns: list[str],
) -> tuple[bool, list[str], list[dict[str, str]]]:
    issues: list[str] = []
    lines = handoff_path.read_text(encoding="utf-8").splitlines()

    ci_rows = _parse_markdown_table(_extract_section(lines, "## CI Gates"))
    if not ci_rows:
        issues.append("missing or invalid CI Gates table")
    else:
        row_map = {_normalize_cell(r.get("gate", "")): r for r in ci_rows}
        for gate in required_ci_gates:
            row = row_map.get(gate)
            if row is None:
                issues.append(f"missing CI gate row: {gate}")
                continue
            status = _normalize_cell(row.get("status", ""))
            if _status_is_fail(status):
                issues.append(f"CI gate failed: {gate}")

    run_rows = _parse_markdown_table(_extract_section(lines, "## Run-Pack Inventory"))
    if not run_rows:
        issues.append("missing or invalid Run-Pack Inventory table")
        return False, issues, []

    present_cols = set(run_rows[0].keys())
    missing_cols = [col for col in required_columns if col not in present_cols]
    if missing_cols:
        issues.append("missing required columns: " + ", ".join(missing_cols))

    for idx, row in enumerate(run_rows, start=1):
        pack_path = _normalize_cell(row.get("pack_path", ""))
        run_id = _normalize_cell(row.get("run_id", ""))
        if not pack_path:
            issues.append(f"row {idx} missing pack_path (run_id={run_id})")

    return len(issues) == 0, issues, run_rows


def _import_pack(
    repo: RepoConfig,
    run_row: dict[str, str],
    assembly_root: Path,
    *,
    overwrite: bool,
) -> tuple[bool, str]:
    exp_type = _normalize_cell(run_row.get("experiment_type", ""))
    run_id = _normalize_cell(run_row.get("run_id", ""))
    pack_path_cell = _normalize_cell(run_row.get("pack_path", ""))
    if not exp_type or not run_id or not pack_path_cell:
        return False, "row missing experiment_type/run_id/pack_path"

    src = Path(pack_path_cell)
    if not src.is_absolute():
        src = repo.path / src
    if not src.exists():
        return False, f"pack_path not found: {src}"

    dest = assembly_root / "evidence" / "experiments" / exp_type / "runs" / run_id
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        if not overwrite:
            return True, f"already exists, skipped: {dest}"
        shutil.rmtree(dest)

    shutil.copytree(src, dest)
    return True, f"imported: {dest}"


def _read_repo_configs(config: dict[str, Any]) -> dict[str, RepoConfig]:
    repos: dict[str, RepoConfig] = {}
    for entry in config.get("producer_repos", []):
        name = str(entry.get("name", "")).strip()
        path = Path(str(entry.get("path", "")).strip())
        globs = [str(x) for x in entry.get("handoff_globs", []) if str(x).strip()]
        if not name or not globs or not str(path):
            continue
        repos[name] = RepoConfig(name=name, path=path, handoff_globs=globs)
    return repos


def _repos_for_day(config: dict[str, Any], day_name: str) -> list[str]:
    cadence = config.get("staggered_cadence", {})
    if not isinstance(cadence, dict):
        return []
    repos = cadence.get(day_name.upper(), [])
    if isinstance(repos, list):
        return [str(x) for x in repos if str(x).strip()]
    return []


def _write_report(report_path: Path, data: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync weekly handoffs into REE_assembly.")
    parser.add_argument(
        "--config",
        default="evidence/planning/cadence_automation.v1.json",
        help="Path to cadence automation config.",
    )
    parser.add_argument(
        "--day",
        default="auto",
        help="Weekday name override (MONDAY..SUNDAY) or 'auto'.",
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=[],
        help="Explicit repo names to sync; overrides day mapping.",
    )
    parser.add_argument(
        "--skip-git-pull",
        action="store_true",
        help="Skip git pull in producer repos.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing imported run directories.",
    )
    parser.add_argument(
        "--run-ingestion",
        action="store_true",
        help="Run ingestion and governance after imports.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and plan only; do not copy files or run ingestion.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    config_path = repo_root / args.config
    if not config_path.exists():
        print(f"Missing config: {config_path}", file=sys.stderr)
        return 2
    config = _load_json(config_path)
    repos = _read_repo_configs(config)

    if args.repos:
        target_repo_names = list(args.repos)
    else:
        if args.day.lower() == "auto":
            day_name = WEEKDAYS[date.today().weekday()]
        else:
            day_name = args.day.upper()
        target_repo_names = _repos_for_day(config, day_name)

    required_cols = [str(x) for x in config.get("required_handoff_columns", [])]
    required_gates = [str(x) for x in config.get("required_ci_gates", [])]

    report: dict[str, Any] = {
        "schema_version": "handoff_sync_report/v1",
        "generated_at_utc": _now_utc(),
        "repo_root": repo_root.as_posix(),
        "config_path": config_path.as_posix(),
        "targets": target_repo_names,
        "dry_run": bool(args.dry_run),
        "results": [],
    }

    for repo_name in target_repo_names:
        entry: dict[str, Any] = {"repo_name": repo_name}
        repo_cfg = repos.get(repo_name)
        if repo_cfg is None:
            entry["status"] = "error"
            entry["error"] = "repo not in config"
            report["results"].append(entry)
            continue

        entry["repo_path"] = repo_cfg.path.as_posix()
        if not repo_cfg.path.exists():
            entry["status"] = "error"
            entry["error"] = "repo path missing"
            report["results"].append(entry)
            continue

        if not args.skip_git_pull:
            rc, out, err = _run(["git", "pull", "--ff-only"], cwd=repo_cfg.path)
            entry["git_pull"] = {"returncode": rc, "stdout": out, "stderr": err}
            if rc != 0:
                entry["status"] = "error"
                entry["error"] = "git pull failed"
                report["results"].append(entry)
                continue

        handoff = _latest_handoff(repo_cfg)
        if handoff is None:
            entry["status"] = "error"
            entry["error"] = "no handoff file found"
            report["results"].append(entry)
            continue
        entry["handoff_path"] = handoff.as_posix()

        ok, issues, rows = _validate_handoff(
            handoff,
            required_ci_gates=required_gates,
            required_columns=required_cols,
        )
        entry["handoff_issues"] = issues
        if not ok:
            entry["status"] = "skipped"
            entry["reason"] = "handoff validation failed"
            report["results"].append(entry)
            continue

        imports: list[dict[str, Any]] = []
        for row in rows:
            if args.dry_run:
                imports.append(
                    {
                        "run_id": _normalize_cell(row.get("run_id", "")),
                        "experiment_type": _normalize_cell(row.get("experiment_type", "")),
                        "ok": True,
                        "message": "dry-run",
                    }
                )
                continue
            ok_i, msg = _import_pack(
                repo_cfg,
                row,
                repo_root,
                overwrite=bool(args.overwrite),
            )
            imports.append(
                {
                    "run_id": _normalize_cell(row.get("run_id", "")),
                    "experiment_type": _normalize_cell(row.get("experiment_type", "")),
                    "ok": ok_i,
                    "message": msg,
                }
            )
        entry["imports"] = imports
        entry["status"] = "ok"
        report["results"].append(entry)

    ingestion_steps: list[dict[str, Any]] = []
    if args.run_ingestion and not args.dry_run:
        commands = [
            ["python3", "evidence/experiments/scripts/build_experiment_indexes.py"],
            ["python3", "evidence/planning/scripts/run_governance_cycle.py"],
        ]
        for cmd in commands:
            rc, out, err = _run(cmd, cwd=repo_root)
            ingestion_steps.append(
                {
                    "command": cmd,
                    "returncode": rc,
                    "stdout": out,
                    "stderr": err,
                    "status": "ok" if rc == 0 else "failed",
                }
            )
    report["ingestion_steps"] = ingestion_steps

    reports_dir = repo_root / "evidence" / "planning" / "handoff_sync_reports"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = reports_dir / f"{timestamp}_handoff_sync_report.json"
    _write_report(report_path, report)
    print(f"Wrote report: {report_path}")

    failures = [
        r for r in report["results"] if r.get("status") in {"error", "skipped"}
    ]
    ingestion_failures = [s for s in ingestion_steps if s.get("status") != "ok"]
    return 1 if (failures or ingestion_failures) else 0


if __name__ == "__main__":
    raise SystemExit(main())
