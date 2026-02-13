#!/usr/bin/env python3
"""Build experimental evidence indexes from Experiment Pack artefacts.

This script scans:
  evidence/experiments/**/runs/**/manifest.json

It regenerates:
  evidence/experiments/INDEX.md
  evidence/experiments/claim_evidence.v1.json
  evidence/experiments/<experiment_type>/INDEX.md
  evidence/experiments/<experiment_type>/experiment.md (auto Design implications block)
  evidence/experiments/TODOs.md

Dependencies: Python standard library only.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

START_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:START -->"
END_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:END -->"


@dataclass
class StopHit:
    metric: str
    op: str
    threshold: float
    value: float

    def render(self) -> str:
        return f"{self.metric} {self.op} {self.threshold} (value={_fmt_number(self.value)})"


@dataclass
class RunRecord:
    experiment_type: str
    run_id: str
    timestamp_raw: str
    timestamp: datetime
    manifest_path: Path
    metrics_path: Path
    summary_path: Path
    manifest_status: str
    final_status: str = "PASS"
    fail_hits: list[StopHit] = field(default_factory=list)
    failure_signatures: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    deltas: dict[str, float] = field(default_factory=dict)
    claim_ids_tested: list[str] = field(default_factory=list)
    evidence_class: str = "simulation"
    evidence_direction: str = "unknown"


def _fmt_number(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, int):
        return str(value)
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _fmt_delta(value: float | None) -> str:
    if value is None:
        return "n/a"
    sign = "+" if value >= 0 else ""
    return f"{sign}{_fmt_number(value)}"


def _parse_timestamp(raw: str | None, fallback_path: Path) -> tuple[str, datetime]:
    if raw:
        normalized = raw
        if normalized.endswith("Z"):
            normalized = normalized[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(normalized)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return raw, dt.astimezone(timezone.utc)
        except ValueError:
            pass
    mtime = datetime.fromtimestamp(fallback_path.stat().st_mtime, tz=timezone.utc)
    return mtime.isoformat().replace("+00:00", "Z"), mtime


def _normalize_direction(raw: str | None) -> str:
    allowed = {"supports", "weakens", "mixed", "unknown"}
    value = (raw or "unknown").strip().lower()
    return value if value in allowed else "unknown"


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON: {path}: {exc}") from exc


def _load_stop_criteria(path: Path) -> dict[str, Any]:
    """Load stop criteria from JSON-compatible YAML.

    The repository keeps YAML extension for readability/versioning, but parsing uses
    json.loads to stay within the standard library.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing stop criteria file: {path}") from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{path} must be JSON-compatible YAML (YAML 1.2 superset of JSON)."
        ) from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"Stop criteria root must be an object: {path}")
    return data


def _compare(value: float, op: str, threshold: float) -> bool:
    if op == ">":
        return value > threshold
    if op == ">=":
        return value >= threshold
    if op == "<":
        return value < threshold
    if op == "<=":
        return value <= threshold
    if op == "==":
        return value == threshold
    if op == "!=":
        return value != threshold
    raise RuntimeError(f"Unsupported stop criteria operator: {op}")


def _scan_runs(base_dir: Path) -> dict[str, list[RunRecord]]:
    by_experiment: dict[str, list[RunRecord]] = defaultdict(list)
    for manifest_path in sorted(base_dir.glob("**/runs/**/manifest.json")):
        run_dir = manifest_path.parent
        if run_dir.parent.name != "runs":
            continue
        experiment_type = run_dir.parent.parent.name

        manifest = _load_json(manifest_path)
        run_id = str(manifest.get("run_id", run_dir.name))
        timestamp_raw, timestamp = _parse_timestamp(
            manifest.get("timestamp_utc"), manifest_path
        )

        artifacts = manifest.get("artifacts", {}) if isinstance(manifest, dict) else {}
        metrics_rel = artifacts.get("metrics_path", "metrics.json")
        summary_rel = artifacts.get("summary_path", "summary.md")

        metrics_path = run_dir / metrics_rel
        summary_path = run_dir / summary_rel

        metrics_doc = _load_json(metrics_path)
        values = metrics_doc.get("values", {}) if isinstance(metrics_doc, dict) else {}
        metrics: dict[str, float] = {}
        if isinstance(values, dict):
            for k, v in values.items():
                if isinstance(v, (int, float)):
                    metrics[k] = float(v)

        status = str(manifest.get("status", "UNKNOWN")).upper()
        signatures = manifest.get("failure_signatures", [])
        if not isinstance(signatures, list):
            signatures = []
        claim_ids_raw = manifest.get("claim_ids_tested", [])
        if not isinstance(claim_ids_raw, list):
            claim_ids_raw = []
        claim_ids_tested = [str(x).strip() for x in claim_ids_raw if str(x).strip()]
        evidence_class = str(manifest.get("evidence_class", "simulation")).strip() or "simulation"
        evidence_direction = _normalize_direction(manifest.get("evidence_direction"))

        by_experiment[experiment_type].append(
            RunRecord(
                experiment_type=experiment_type,
                run_id=run_id,
                timestamp_raw=timestamp_raw,
                timestamp=timestamp,
                manifest_path=manifest_path,
                metrics_path=metrics_path,
                summary_path=summary_path,
                manifest_status=status,
                failure_signatures=[str(x) for x in signatures],
                metrics=metrics,
                claim_ids_tested=claim_ids_tested,
                evidence_class=evidence_class,
                evidence_direction=evidence_direction,
            )
        )

    for runs in by_experiment.values():
        runs.sort(key=lambda r: (r.timestamp, r.run_id))
    return by_experiment


def _criteria_for_experiment(stop_criteria: dict[str, Any], experiment_type: str) -> dict[str, Any]:
    default = stop_criteria.get("default", {})
    experiments = stop_criteria.get("experiments", {})
    specific = experiments.get(experiment_type, {}) if isinstance(experiments, dict) else {}
    merged: dict[str, Any] = {"fail_if": []}

    default_fail_if = default.get("fail_if", []) if isinstance(default, dict) else []
    specific_fail_if = specific.get("fail_if", []) if isinstance(specific, dict) else []

    if isinstance(default_fail_if, list):
        merged["fail_if"].extend(default_fail_if)
    if isinstance(specific_fail_if, list):
        merged["fail_if"].extend(specific_fail_if)
    return merged


def _evaluate_runs(runs: list[RunRecord], criteria: dict[str, Any]) -> None:
    prev_metrics: dict[str, float] | None = None
    for run in runs:
        fail_hits: list[StopHit] = []
        for rule in criteria.get("fail_if", []):
            if not isinstance(rule, dict):
                continue
            metric = rule.get("metric")
            op = rule.get("op")
            threshold = rule.get("threshold")
            if not isinstance(metric, str) or not isinstance(op, str):
                continue
            if not isinstance(threshold, (int, float)):
                continue

            value = run.metrics.get(metric)
            if value is None:
                continue
            if _compare(value, op, float(threshold)):
                fail_hits.append(
                    StopHit(
                        metric=metric,
                        op=op,
                        threshold=float(threshold),
                        value=value,
                    )
                )

        run.fail_hits = fail_hits
        criteria_fail = bool(fail_hits)
        manifest_fail = run.manifest_status == "FAIL"
        run.final_status = "FAIL" if (criteria_fail or manifest_fail) else "PASS"

        if prev_metrics:
            for metric, value in run.metrics.items():
                if metric in prev_metrics:
                    run.deltas[metric] = value - prev_metrics[metric]
        prev_metrics = run.metrics

        if criteria_fail:
            for hit in fail_hits:
                sig = f"stop:{hit.metric}{hit.op}{_fmt_number(hit.threshold)}"
                if sig not in run.failure_signatures:
                    run.failure_signatures.append(sig)


def _select_key_metrics(runs: list[RunRecord], criteria: dict[str, Any], limit: int = 6) -> list[str]:
    metrics: list[str] = []
    for rule in criteria.get("fail_if", []):
        metric = rule.get("metric") if isinstance(rule, dict) else None
        if isinstance(metric, str) and metric not in metrics:
            metrics.append(metric)

    counter: Counter[str] = Counter()
    for run in runs:
        counter.update(run.metrics.keys())

    for metric, _ in counter.most_common():
        if metric not in metrics:
            metrics.append(metric)
        if len(metrics) >= limit:
            break
    return metrics[:limit]


def _ensure_experiment_template(experiment_dir: Path, experiment_type: str) -> Path:
    doc_path = experiment_dir / "experiment.md"
    if doc_path.exists():
        return doc_path

    template = f"""# Experiment: {experiment_type}

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

{START_MARKER}
No generated implications yet.
{END_MARKER}
"""
    doc_path.write_text(template, encoding="utf-8")
    return doc_path


def _replace_between_markers(text: str, replacement: str) -> str:
    if START_MARKER in text and END_MARKER in text:
        before, rest = text.split(START_MARKER, 1)
        _, after = rest.split(END_MARKER, 1)
        return f"{before}{START_MARKER}\n{replacement}\n{END_MARKER}{after}"

    return text.rstrip() + f"\n\n{START_MARKER}\n{replacement}\n{END_MARKER}\n"


def _build_design_implications(runs: list[RunRecord], lookback_failures: int) -> tuple[str, list[str]]:
    failures = [r for r in runs if r.final_status == "FAIL"]
    if not failures:
        return "No recent FAIL runs. Keep monitoring key stop metrics.", []

    recent = failures[-lookback_failures:]
    signature_counter: Counter[str] = Counter()
    last_seen_run: dict[str, str] = {}

    for run in failures:
        for sig in run.failure_signatures:
            signature_counter[sig] += 1
            last_seen_run[sig] = run.run_id

    lines: list[str] = []
    lines.append("Recent failure runs:")
    for run in reversed(recent):
        signatures = ", ".join(run.failure_signatures) if run.failure_signatures else "none"
        lines.append(f"- `{run.run_id}` at `{run.timestamp_raw}` signatures: {signatures}")

    lines.append("")
    lines.append("Recurring signatures:")
    for sig, count in signature_counter.most_common(8):
        lines.append(f"- `{sig}` occurred in {count} FAIL run(s); latest `{last_seen_run[sig]}`")

    todo_items: list[str] = []
    for sig, count in signature_counter.most_common(6):
        todo_items.append(
            f"[ ] Investigate signature `{sig}` ({count} FAIL run(s), latest `{last_seen_run[sig]}`)."
        )

    lines.append("")
    lines.append("Suggested design TODOs:")
    lines.extend(f"- {todo}" for todo in todo_items)

    return "\n".join(lines), todo_items


def _write_experiment_index(
    experiment_dir: Path,
    experiment_type: str,
    runs: list[RunRecord],
    key_metrics: list[str],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append(f"# Experiment Index: {experiment_type}")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("- Experiment profile: `experiment.md`")
    lines.append("- Stop criteria: `../../stop_criteria.v1.yaml`")
    lines.append("")

    if not runs:
        lines.append("No runs discovered.")
    else:
        lines.append("## Runs")
        lines.append("")
        lines.append(
            "| run_id | timestamp_utc | status | key metrics | deltas vs previous | stop-criteria hits | summary |"
        )
        lines.append(
            "|---|---|---|---|---|---|---|"
        )

        for run in reversed(runs):
            status = f"**{run.final_status}**" if run.final_status == "FAIL" else run.final_status
            key_values = []
            delta_values = []
            for metric in key_metrics:
                if metric in run.metrics:
                    key_values.append(f"{metric}={_fmt_number(run.metrics[metric])}")
                if metric in run.deltas:
                    delta_values.append(f"{metric}:{_fmt_delta(run.deltas[metric])}")

            stop_hits = "; ".join(hit.render() for hit in run.fail_hits) if run.fail_hits else "-"
            summary_rel = run.summary_path.relative_to(experiment_dir).as_posix()
            metrics_rel = run.metrics_path.relative_to(experiment_dir).as_posix()
            manifest_rel = run.manifest_path.relative_to(experiment_dir).as_posix()

            summary_link = f"[`summary`]({summary_rel})"
            summary_link += f" / [`manifest`]({manifest_rel}) / [`metrics`]({metrics_rel})"

            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{run.run_id}`",
                        f"`{run.timestamp_raw}`",
                        status,
                        "<br>".join(key_values) if key_values else "-",
                        "<br>".join(delta_values) if delta_values else "-",
                        stop_hits,
                        summary_link,
                    ]
                )
                + " |"
            )

    lines.append("")
    (experiment_dir / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _write_top_level_index(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Experimental Evidence Index")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("This index is generated by `scripts/build_experiment_indexes.py`.")
    lines.append("")
    lines.append("| experiment_type | latest status | latest run | fails / total | links |")
    lines.append("|---|---|---|---|---|")

    for exp_type in sorted(by_experiment.keys()):
        runs = by_experiment[exp_type]
        total = len(runs)
        fails = sum(1 for r in runs if r.final_status == "FAIL")
        latest = runs[-1] if runs else None
        latest_status = latest.final_status if latest else "n/a"
        latest_status_rendered = (
            f"**{latest_status}**" if latest_status == "FAIL" else latest_status
        )
        latest_run = f"`{latest.run_id}`" if latest else "-"
        links = f"[`INDEX`](./{exp_type}/INDEX.md) / [`profile`](./{exp_type}/experiment.md)"
        lines.append(
            f"| `{exp_type}` | {latest_status_rendered} | {latest_run} | {fails}/{total} | {links} |"
        )

    if not by_experiment:
        lines.append("| _none_ | - | - | - | - |")

    lines.append("")
    lines.append("- TODO queue: `TODOs.md`")
    lines.append("- Stop criteria config: `stop_criteria.v1.yaml`")
    lines.append("- Claim-evidence matrix: `claim_evidence.v1.json`")

    (base_dir / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _write_claim_evidence_matrix(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    generated_at: str,
) -> None:
    runs = [run for exp_runs in by_experiment.values() for run in exp_runs]
    runs.sort(key=lambda r: (r.timestamp, r.experiment_type, r.run_id))

    matrix: dict[str, Any] = {
        "schema_version": "claim_evidence_matrix/v1",
        "generated_at_utc": generated_at,
        "source_root": "evidence/experiments",
        "claims": {},
        "entries": [],
        "unlinked_runs": [],
    }

    for run in runs:
        inferred_direction = run.evidence_direction
        if inferred_direction == "unknown":
            inferred_direction = "supports" if run.final_status == "PASS" else "weakens"

        if not run.claim_ids_tested:
            matrix["unlinked_runs"].append(
                {
                    "experiment_type": run.experiment_type,
                    "run_id": run.run_id,
                    "timestamp_utc": run.timestamp_raw,
                    "status": run.final_status,
                }
            )
            continue

        for claim_id in run.claim_ids_tested:
            entry = {
                "claim_id": claim_id,
                "experiment_type": run.experiment_type,
                "run_id": run.run_id,
                "timestamp_utc": run.timestamp_raw,
                "status": run.final_status,
                "evidence_class": run.evidence_class,
                "evidence_direction": inferred_direction,
                "failure_signatures": run.failure_signatures,
            }
            matrix["entries"].append(entry)

            claim = matrix["claims"].setdefault(
                claim_id,
                {
                    "runs_total": 0,
                    "pass_runs": 0,
                    "fail_runs": 0,
                    "latest_run_id": "",
                    "latest_timestamp_utc": "",
                    "direction_counts": {
                        "supports": 0,
                        "weakens": 0,
                        "mixed": 0,
                        "unknown": 0,
                    },
                    "evidence_class_counts": {},
                    "recent_entries": [],
                },
            )
            claim["runs_total"] += 1
            if run.final_status == "PASS":
                claim["pass_runs"] += 1
            else:
                claim["fail_runs"] += 1
            claim["latest_run_id"] = run.run_id
            claim["latest_timestamp_utc"] = run.timestamp_raw
            claim["direction_counts"][inferred_direction] = (
                claim["direction_counts"].get(inferred_direction, 0) + 1
            )
            class_counts = claim["evidence_class_counts"]
            class_counts[run.evidence_class] = class_counts.get(run.evidence_class, 0) + 1
            claim["recent_entries"].append(entry)

    for claim_id in sorted(matrix["claims"].keys()):
        recent = matrix["claims"][claim_id]["recent_entries"]
        recent.sort(key=lambda e: (e["timestamp_utc"], e["run_id"]))
        matrix["claims"][claim_id]["recent_entries"] = recent[-5:]

    matrix["entries"].sort(
        key=lambda e: (e["timestamp_utc"], e["claim_id"], e["experiment_type"], e["run_id"])
    )
    matrix["unlinked_runs"].sort(
        key=lambda e: (e["timestamp_utc"], e["experiment_type"], e["run_id"])
    )

    (base_dir / "claim_evidence.v1.json").write_text(
        json.dumps(matrix, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_todos(base_dir: Path, todos_by_experiment: dict[str, list[str]], generated_at: str) -> None:
    lines: list[str] = []
    lines.append("# Experiment-Driven TODO Queue")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("Auto-generated from FAIL signatures in Experiment Pack runs.")
    lines.append("")

    if not todos_by_experiment:
        lines.append("No active failure-driven TODO items.")
    else:
        for exp_type in sorted(todos_by_experiment.keys()):
            lines.append(f"## {exp_type}")
            lines.append("")
            for item in todos_by_experiment[exp_type]:
                lines.append(f"- {item}")
            lines.append("")

    (base_dir / "TODOs.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build experiment evidence indexes.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to evidence/experiments",
    )
    parser.add_argument(
        "--lookback-failures",
        type=int,
        default=3,
        help="How many most recent FAIL runs to include in design implications.",
    )
    args = parser.parse_args()

    base_dir = args.root.resolve()
    stop_criteria = _load_stop_criteria(base_dir / "stop_criteria.v1.yaml")
    by_experiment = _scan_runs(base_dir)

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    todos_by_experiment: dict[str, list[str]] = {}

    for experiment_type, runs in by_experiment.items():
        criteria = _criteria_for_experiment(stop_criteria, experiment_type)
        _evaluate_runs(runs, criteria)

        key_metrics = _select_key_metrics(runs, criteria)
        experiment_dir = base_dir / experiment_type
        profile_path = _ensure_experiment_template(experiment_dir, experiment_type)

        design_text, todos = _build_design_implications(runs, args.lookback_failures)
        profile_text = profile_path.read_text(encoding="utf-8")
        profile_text = _replace_between_markers(profile_text, design_text)
        profile_path.write_text(profile_text, encoding="utf-8")

        if todos:
            todos_by_experiment[experiment_type] = todos

        _write_experiment_index(experiment_dir, experiment_type, runs, key_metrics, generated_at)

    _write_top_level_index(base_dir, by_experiment, generated_at)
    _write_todos(base_dir, todos_by_experiment, generated_at)
    _write_claim_evidence_matrix(base_dir, by_experiment, generated_at)

    total_runs = sum(len(runs) for runs in by_experiment.values())
    total_fail = sum(1 for runs in by_experiment.values() for r in runs if r.final_status == "FAIL")
    print(f"Indexed {total_runs} run(s) across {len(by_experiment)} experiment type(s); FAIL={total_fail}.")


if __name__ == "__main__":
    main()
