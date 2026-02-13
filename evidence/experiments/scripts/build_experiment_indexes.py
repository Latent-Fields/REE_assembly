#!/usr/bin/env python3
"""Build evidence indexes from experimental and literature artefacts.

This script scans:
  evidence/experiments/**/runs/**/manifest.json
  evidence/literature/**/entries/**/record.json

It regenerates:
  evidence/experiments/INDEX.md
  evidence/experiments/claim_evidence.v1.json
  evidence/experiments/conflicts.md
  evidence/experiments/promotion_demotion_recommendations.md
  evidence/experiments/environment_status.v1.json
  evidence/experiments/environment_drift.md
  evidence/decisions/decision_state.v1.json
  evidence/planning/evidence_backlog.v1.json
  evidence/planning/experiment_proposals.v1.json
  evidence/experiments/<experiment_type>/INDEX.md
  evidence/experiments/<experiment_type>/experiment.md (auto Design implications block)
  evidence/experiments/TODOs.md
  evidence/literature/INDEX.md

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
    source_repo_name: str = "unknown"
    source_repo_commit: str = ""
    source_repo_branch: str = ""
    scenario_name: str = ""
    scenario_seed: str = ""
    scenario_config_hash: str = ""
    environment: dict[str, str] = field(default_factory=dict)
    environment_declared: bool = False
    environment_status: str = "unknown"
    environment_missing_fields: list[str] = field(default_factory=list)
    environment_missing_metrics: list[str] = field(default_factory=list)
    environment_fail_hits: list[StopHit] = field(default_factory=list)
    producer_capabilities: dict[str, bool] = field(default_factory=dict)
    producer_capabilities_declared: bool = False


@dataclass
class LiteratureRecord:
    literature_type: str
    entry_id: str
    timestamp_raw: str
    timestamp: datetime
    record_path: Path
    summary_path: Path
    claim_ids_tested: list[str] = field(default_factory=list)
    evidence_class: str = "review"
    evidence_direction: str = "unknown"
    confidence: float = 0.5
    confidence_rationale: str = ""
    failure_signatures: list[str] = field(default_factory=list)


@dataclass
class DecisionLogEntry:
    claim_id: str
    decision_status: str
    recommendation: str
    decision_needed: str
    timestamp_utc: str
    selected_option: str = ""
    rationale: str = ""
    actor: str = "user"


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


def _parse_timestamp_only(raw: str) -> datetime:
    normalized = raw
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _normalize_direction(raw: str | None) -> str:
    allowed = {"supports", "weakens", "mixed", "unknown"}
    value = (raw or "unknown").strip().lower()
    return value if value in allowed else "unknown"


def _normalize_confidence(raw: Any, default: float = 0.5) -> float:
    value = default
    if isinstance(raw, (int, float)):
        value = float(raw)
    value = max(0.0, min(1.0, value))
    return round(value, 3)


def _prefix_class(source_type: str, evidence_class: str) -> str:
    token = (evidence_class or "unclassified").strip()
    prefix = "exp" if source_type == "experimental" else "lit"
    if token.startswith(f"{prefix}:"):
        return token
    return f"{prefix}:{token}"


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON: {path}: {exc}") from exc


def _load_json_compatible_yaml(path: Path, description: str) -> dict[str, Any]:
    """Load JSON-compatible YAML using stdlib json parser.

    Files keep .yaml extension for readability/versioning while remaining JSON-compatible.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing {description} file: {path}") from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{path} must be JSON-compatible YAML (YAML 1.2 superset of JSON)."
        ) from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"{description} root must be an object: {path}")
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
        source_repo = manifest.get("source_repo", {})
        source_repo_name = "unknown"
        source_repo_commit = ""
        source_repo_branch = ""
        if isinstance(source_repo, dict):
            source_repo_name = str(source_repo.get("name", "unknown")).strip() or "unknown"
            source_repo_commit = str(source_repo.get("commit", "")).strip()
            source_repo_branch = str(source_repo.get("branch", "")).strip()

        scenario = manifest.get("scenario", {})
        scenario_name = ""
        scenario_seed = ""
        scenario_config_hash = ""
        if isinstance(scenario, dict):
            scenario_name = str(scenario.get("name", "")).strip()
            seed_raw = scenario.get("seed", "")
            scenario_seed = str(seed_raw).strip()
            scenario_config_hash = str(scenario.get("config_hash", "")).strip()

        has_environment_field = isinstance(manifest, dict) and "environment" in manifest
        environment_raw = manifest.get("environment") if isinstance(manifest, dict) else None
        environment_declared = bool(has_environment_field and isinstance(environment_raw, dict))
        environment: dict[str, str] = {}
        if environment_declared and isinstance(environment_raw, dict):
            for key, value in environment_raw.items():
                env_key = str(key).strip()
                if not env_key:
                    continue
                environment[env_key] = str(value).strip()

        has_capability_field = isinstance(manifest, dict) and "producer_capabilities" in manifest
        capabilities_raw = manifest.get("producer_capabilities") if isinstance(manifest, dict) else None
        producer_capabilities: dict[str, bool] = {}
        producer_capabilities_declared = False
        if has_capability_field and isinstance(capabilities_raw, dict):
            producer_capabilities_declared = True
            for key, value in capabilities_raw.items():
                cap_key = str(key).strip()
                if not cap_key:
                    continue
                if isinstance(value, bool):
                    producer_capabilities[cap_key] = value
                elif isinstance(value, (int, float)):
                    producer_capabilities[cap_key] = bool(value)
        elif has_capability_field and isinstance(capabilities_raw, list):
            producer_capabilities_declared = True
            for value in capabilities_raw:
                cap_key = str(value).strip()
                if cap_key:
                    producer_capabilities[cap_key] = True

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
                source_repo_name=source_repo_name,
                source_repo_commit=source_repo_commit,
                source_repo_branch=source_repo_branch,
                scenario_name=scenario_name,
                scenario_seed=scenario_seed,
                scenario_config_hash=scenario_config_hash,
                environment=environment,
                environment_declared=environment_declared,
                producer_capabilities=producer_capabilities,
                producer_capabilities_declared=producer_capabilities_declared,
            )
        )

    for runs in by_experiment.values():
        runs.sort(key=lambda r: (r.timestamp, r.run_id))
    return by_experiment


def _scan_literature(literature_root: Path) -> dict[str, list[LiteratureRecord]]:
    by_literature: dict[str, list[LiteratureRecord]] = defaultdict(list)
    if not literature_root.exists():
        return by_literature

    for record_path in sorted(literature_root.glob("**/entries/**/record.json")):
        entry_dir = record_path.parent
        if entry_dir.parent.name != "entries":
            continue
        literature_type = entry_dir.parent.parent.name

        record = _load_json(record_path)
        entry_id = str(record.get("entry_id", entry_dir.name))
        timestamp_raw, timestamp = _parse_timestamp(record.get("timestamp_utc"), record_path)

        claim_ids_raw = record.get("claim_ids_tested", [])
        if not isinstance(claim_ids_raw, list):
            claim_ids_raw = []
        claim_ids_tested = [str(x).strip() for x in claim_ids_raw if str(x).strip()]

        evidence_class = str(record.get("evidence_class", "review")).strip() or "review"
        evidence_direction = _normalize_direction(record.get("evidence_direction"))
        confidence = _normalize_confidence(record.get("confidence"), default=0.6)
        confidence_rationale = str(record.get("confidence_rationale", "")).strip()

        signatures = record.get("failure_signatures", [])
        if not isinstance(signatures, list):
            signatures = []

        summary_rel = str(record.get("summary_path", "summary.md"))
        summary_path = entry_dir / summary_rel

        by_literature[literature_type].append(
            LiteratureRecord(
                literature_type=literature_type,
                entry_id=entry_id,
                timestamp_raw=timestamp_raw,
                timestamp=timestamp,
                record_path=record_path,
                summary_path=summary_path,
                claim_ids_tested=claim_ids_tested,
                evidence_class=evidence_class,
                evidence_direction=evidence_direction,
                confidence=confidence,
                confidence_rationale=confidence_rationale,
                failure_signatures=[str(x) for x in signatures],
            )
        )

    for entries in by_literature.values():
        entries.sort(key=lambda e: (e.timestamp, e.entry_id))
    return by_literature


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


def _environment_label(run: RunRecord) -> str:
    env_id = run.environment.get("env_id", "").strip()
    env_version = run.environment.get("env_version", "").strip()
    tier = run.environment.get("tier", "").strip()

    parts: list[str] = []
    if env_id:
        parts.append(env_id)
    if env_version:
        parts.append(f"v={env_version}")
    if tier:
        parts.append(f"tier={tier}")
    if not parts:
        parts.append("unknown")

    status = run.environment_status
    status_token = {
        "environment_qualified": "qualified",
        "missing_environment_metadata": "missing-metadata",
        "missing_environment_metrics": "missing-metrics",
        "environment_unqualified": "unqualified",
    }.get(status, status)
    return f"{' '.join(parts)} ({status_token})"


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
    lines.append("- Environment qualification: `../../environment_qualification.v1.yaml`")
    lines.append("")

    if not runs:
        lines.append("No runs discovered.")
    else:
        lines.append("## Runs")
        lines.append("")
        lines.append(
            "| run_id | timestamp_utc | status | environment | key metrics | deltas vs previous | stop-criteria hits | summary |"
        )
        lines.append(
            "|---|---|---|---|---|---|---|---|"
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
                        _environment_label(run),
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
    by_literature: dict[str, list[LiteratureRecord]],
    decision_log_count: int,
    backlog_count: int,
    proposal_count: int,
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
    lines.append("## Cross-Evidence Outputs")
    lines.append("")
    all_runs = [run for runs in by_experiment.values() for run in runs]
    qualified_runs = sum(1 for run in all_runs if run.environment_status == "environment_qualified")
    declared_env_runs = sum(1 for run in all_runs if run.environment_declared)
    lines.append("- TODO queue: `TODOs.md`")
    lines.append("- Stop criteria config: `stop_criteria.v1.yaml`")
    lines.append("- Decision criteria config: `decision_criteria.v1.yaml`")
    lines.append("- Environment qualification config: `environment_qualification.v1.yaml`")
    lines.append("- Claim-evidence matrix: `claim_evidence.v1.json`")
    lines.append("- Conflicts report: `conflicts.md`")
    lines.append("- Promotion/demotion recommendations: `promotion_demotion_recommendations.md`")
    lines.append("- Environment status: `environment_status.v1.json`")
    lines.append("- Environment drift report: `environment_drift.md`")
    lines.append(
        f"- Environment-qualified runs: {qualified_runs}/{len(all_runs)} (metadata declared in {declared_env_runs}/{len(all_runs)} runs)"
    )
    lines.append(f"- Literature index: `../literature/INDEX.md` ({sum(len(v) for v in by_literature.values())} entries)")
    lines.append(f"- Persistent decision log: `../decisions/decision_log.v1.jsonl` ({decision_log_count} entries)")
    lines.append("- Decision state snapshot: `../decisions/decision_state.v1.json`")
    lines.append(f"- Evidence backlog: `../planning/evidence_backlog.v1.json` ({backlog_count} item(s))")
    lines.append(f"- Experiment proposals: `../planning/experiment_proposals.v1.json` ({proposal_count} item(s))")

    (base_dir / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _write_literature_index(
    literature_root: Path,
    by_literature: dict[str, list[LiteratureRecord]],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Literature Evidence Index")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("| literature_type | latest entry | total entries | links |")
    lines.append("|---|---|---|---|")

    if not by_literature:
        lines.append("| _none_ | - | 0 | - |")
    else:
        for literature_type in sorted(by_literature.keys()):
            entries = by_literature[literature_type]
            latest = entries[-1]
            latest_link = latest.record_path.relative_to(literature_root).as_posix()
            summary_rel = latest.summary_path.relative_to(literature_root).as_posix()
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{literature_type}`",
                        f"[`{latest.entry_id}`]({latest_link})",
                        str(len(entries)),
                        f"[`summary`]({summary_rel})",
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("This index is generated by `evidence/experiments/scripts/build_experiment_indexes.py`.")
    literature_root.mkdir(parents=True, exist_ok=True)
    (literature_root / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _environment_series_id(run: RunRecord) -> str:
    env = run.environment
    env_id = env.get("env_id", "unknown") or "unknown"
    env_version = env.get("env_version", "unknown") or "unknown"
    dynamics_hash = env.get("dynamics_hash", "unknown") or "unknown"
    reward_hash = env.get("reward_hash", "unknown") or "unknown"
    observation_hash = env.get("observation_hash", "unknown") or "unknown"
    config_hash = env.get("config_hash", run.scenario_config_hash or "unknown") or "unknown"
    scenario_name = run.scenario_name or "unknown_scenario"
    return (
        f"{run.experiment_type}|{scenario_name}|{env_id}|{env_version}|"
        f"{dynamics_hash}|{reward_hash}|{observation_hash}|{config_hash}"
    )


def _pick_drift_metrics(
    experiment_type: str,
    runs: list[RunRecord],
    environment_qualification: dict[str, Any],
) -> list[str]:
    drift_cfg = environment_qualification.get("drift", {})
    metric_cfg = {}
    if isinstance(drift_cfg, dict):
        metric_cfg = drift_cfg.get("key_metrics_per_experiment", {})
    if isinstance(metric_cfg, dict) and isinstance(metric_cfg.get(experiment_type), list):
        metrics = _string_list(metric_cfg.get(experiment_type, []))
        if metrics:
            return metrics

    counter: Counter[str] = Counter()
    for run in runs:
        counter.update(run.metrics.keys())
    return [metric for metric, _ in counter.most_common(6)]


def _write_environment_outputs(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    environment_qualification: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    all_runs = [run for runs in by_experiment.values() for run in runs]
    all_runs.sort(key=lambda run: (run.timestamp, run.experiment_type, run.run_id))

    status_counts: Counter[str] = Counter(run.environment_status for run in all_runs)
    declared_env_runs = sum(1 for run in all_runs if run.environment_declared)
    required_fields = _string_list(
        environment_qualification.get("required_manifest_environment_fields", [])
    )
    drift_cfg = environment_qualification.get("drift", {})
    min_runs = int(drift_cfg.get("min_runs_per_series", 2)) if isinstance(drift_cfg, dict) else 2
    rel_threshold = (
        float(drift_cfg.get("warn_if_relative_change_gt", 0.25))
        if isinstance(drift_cfg, dict)
        else 0.25
    )
    warn_if_direction_flip = bool(
        drift_cfg.get("warn_if_direction_flip", True) if isinstance(drift_cfg, dict) else True
    )

    per_experiment: dict[str, dict[str, Any]] = {}
    series_map: dict[str, list[RunRecord]] = defaultdict(list)
    for experiment_type, runs in by_experiment.items():
        counts: Counter[str] = Counter(run.environment_status for run in runs)
        per_experiment[experiment_type] = {
            "runs_total": len(runs),
            "environment_declared": sum(1 for run in runs if run.environment_declared),
            "status_counts": dict(counts),
        }
        for run in runs:
            series_map[_environment_series_id(run)].append(run)

    series_items: list[dict[str, Any]] = []
    drift_alerts: list[dict[str, Any]] = []
    for series_id in sorted(series_map.keys()):
        series_runs = sorted(series_map[series_id], key=lambda run: (run.timestamp, run.run_id))
        if len(series_runs) < max(2, min_runs):
            continue

        baseline = series_runs[0]
        latest = series_runs[-1]
        experiment_type = latest.experiment_type
        metrics = _pick_drift_metrics(experiment_type, series_runs, environment_qualification)

        metric_deltas: list[dict[str, Any]] = []
        alerts: list[str] = []
        for metric in metrics:
            base = baseline.metrics.get(metric)
            current = latest.metrics.get(metric)
            if base is None or current is None:
                continue
            delta = current - base
            denom = max(abs(base), 1e-9)
            relative_change = abs(delta) / denom
            metric_deltas.append(
                {
                    "metric": metric,
                    "baseline": round(float(base), 6),
                    "latest": round(float(current), 6),
                    "delta": round(float(delta), 6),
                    "relative_change": round(float(relative_change), 6),
                }
            )
            if relative_change > rel_threshold:
                alerts.append(
                    f"metric_drift:{metric} relative_change={_fmt_number(relative_change)}>{_fmt_number(rel_threshold)}"
                )

        baseline_dir = baseline.evidence_direction
        latest_dir = latest.evidence_direction
        if (
            warn_if_direction_flip
            and baseline_dir in {"supports", "weakens"}
            and latest_dir in {"supports", "weakens"}
            and baseline_dir != latest_dir
        ):
            alerts.append(f"direction_flip:{baseline_dir}->{latest_dir}")

        repo_commits = sorted(
            {
                run.source_repo_commit
                for run in series_runs
                if run.source_repo_commit
            }
        )
        commit_changed = len(repo_commits) >= 2

        item = {
            "series_id": series_id,
            "experiment_type": experiment_type,
            "run_count": len(series_runs),
            "first_run_id": baseline.run_id,
            "first_timestamp_utc": baseline.timestamp_raw,
            "latest_run_id": latest.run_id,
            "latest_timestamp_utc": latest.timestamp_raw,
            "scenario_name": latest.scenario_name,
            "env": {
                "env_id": latest.environment.get("env_id", ""),
                "env_version": latest.environment.get("env_version", ""),
                "tier": latest.environment.get("tier", ""),
                "dynamics_hash": latest.environment.get("dynamics_hash", ""),
                "reward_hash": latest.environment.get("reward_hash", ""),
                "observation_hash": latest.environment.get("observation_hash", ""),
                "config_hash": latest.environment.get("config_hash", ""),
            },
            "repo_commits": repo_commits,
            "commit_changed": commit_changed,
            "metric_deltas": metric_deltas,
            "alerts": alerts,
        }
        series_items.append(item)
        if alerts:
            drift_alerts.append(item)

    status_doc = {
        "schema_version": "environment_status/v1",
        "generated_at_utc": generated_at,
        "required_manifest_environment_fields": required_fields,
        "coverage": {
            "total_runs": len(all_runs),
            "environment_declared_runs": declared_env_runs,
            "status_counts": dict(status_counts),
            "qualified_runs": int(status_counts.get("environment_qualified", 0)),
            "missing_metadata_runs": int(status_counts.get("missing_environment_metadata", 0)),
            "missing_metric_runs": int(status_counts.get("missing_environment_metrics", 0)),
            "unqualified_runs": int(status_counts.get("environment_unqualified", 0)),
        },
        "experiments": per_experiment,
        "drift": {
            "series_count": len(series_items),
            "alert_count": len(drift_alerts),
            "warn_if_relative_change_gt": rel_threshold,
            "warn_if_direction_flip": warn_if_direction_flip,
            "alerts": drift_alerts,
            "series": series_items,
        },
    }
    (base_dir / "environment_status.v1.json").write_text(
        json.dumps(status_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines: list[str] = []
    lines.append("# Environment Drift Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Total runs: {len(all_runs)}")
    lines.append(f"- Runs with `environment` metadata: {declared_env_runs}")
    lines.append(f"- Environment-qualified runs: {status_counts.get('environment_qualified', 0)}")
    lines.append(f"- Missing environment metadata: {status_counts.get('missing_environment_metadata', 0)}")
    lines.append(f"- Missing environment metrics: {status_counts.get('missing_environment_metrics', 0)}")
    lines.append(f"- Environment-unqualified (metric violations): {status_counts.get('environment_unqualified', 0)}")
    lines.append("")
    lines.append("## Drift Alerts")
    lines.append("")

    if not drift_alerts:
        lines.append("No environment drift alerts detected for current series thresholds.")
    else:
        for alert in drift_alerts[:30]:
            lines.append(
                f"- `{alert['experiment_type']}` series `{alert['series_id']}` "
                + f"runs={alert['run_count']} alerts={', '.join(alert['alerts'])}"
            )

    (base_dir / "environment_drift.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )
    return status_doc


def _experimental_entry_confidence(run: RunRecord, inferred_direction: str) -> tuple[float, str]:
    confidence = 0.6
    rationale_bits: list[str] = []

    if inferred_direction == "mixed":
        confidence = 0.5
        rationale_bits.append("mixed direction")
    elif inferred_direction == "unknown":
        confidence = 0.45
        rationale_bits.append("unknown direction")
    elif inferred_direction == "supports" and run.final_status == "PASS":
        confidence = 0.75
        rationale_bits.append("PASS with supporting direction")
    elif inferred_direction == "weakens" and run.final_status == "FAIL":
        confidence = 0.75
        rationale_bits.append("FAIL with weakening direction")
    else:
        confidence = 0.55
        rationale_bits.append("direction/status mismatch")

    if run.fail_hits and inferred_direction in {"mixed", "unknown", "supports"}:
        confidence = max(0.4, confidence - 0.1)
        rationale_bits.append("stop criteria triggered")

    return _normalize_confidence(confidence), "; ".join(rationale_bits)


def _recency_score(entries: list[dict[str, Any]], now: datetime, horizon_days: int) -> float:
    if not entries:
        return 0.0
    latest_ts = max(_parse_timestamp_only(str(e["timestamp_utc"])) for e in entries)
    age_days = max(0.0, (now - latest_ts).total_seconds() / 86400.0)
    score = max(0.0, 1.0 - (age_days / float(horizon_days)))
    return round(score, 3)


def _direction_conflict_ratio(direction_counts: dict[str, int]) -> float:
    supports = int(direction_counts.get("supports", 0))
    weakens = int(direction_counts.get("weakens", 0))
    directional_total = supports + weakens
    if directional_total == 0:
        return 0.0
    # 0.0 => no conflict, 1.0 => perfectly split support/weakening evidence.
    return round((2.0 * min(supports, weakens)) / float(directional_total), 3)


def _compute_claim_confidence(
    entries: list[dict[str, Any]],
    now: datetime,
) -> tuple[float, float, float, str]:
    exp_entries = [e for e in entries if e.get("source_type") == "experimental"]
    lit_entries = [e for e in entries if e.get("source_type") == "literature"]

    exp_conf = 0.0
    lit_conf = 0.0

    if exp_entries:
        exp_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in exp_entries)
        directional = exp_counts.get("supports", 0) + exp_counts.get("weakens", 0)
        if directional:
            consistency = abs(exp_counts.get("supports", 0) - exp_counts.get("weakens", 0)) / directional
        else:
            consistency = 0.4
        volume = min(1.0, len(exp_entries) / 5.0)
        recency = _recency_score(exp_entries, now, horizon_days=90)
        quality = sum(float(e.get("confidence", 0.5)) for e in exp_entries) / len(exp_entries)
        exp_conf = _normalize_confidence(
            0.45 * consistency + 0.25 * volume + 0.20 * recency + 0.10 * quality,
            default=0.0,
        )

    if lit_entries:
        lit_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in lit_entries)
        directional = lit_counts.get("supports", 0) + lit_counts.get("weakens", 0)
        if directional:
            consistency = abs(lit_counts.get("supports", 0) - lit_counts.get("weakens", 0)) / directional
        else:
            consistency = 0.5
        volume = min(1.0, len(lit_entries) / 4.0)
        recency = _recency_score(lit_entries, now, horizon_days=365)
        quality = sum(float(e.get("confidence", 0.5)) for e in lit_entries) / len(lit_entries)
        lit_conf = _normalize_confidence(
            0.50 * quality + 0.20 * consistency + 0.20 * volume + 0.10 * recency,
            default=0.0,
        )

    weights = 0.0
    weighted_sum = 0.0
    if exp_entries:
        w = min(3.0, float(len(exp_entries)))
        weighted_sum += exp_conf * w
        weights += w
    if lit_entries:
        w = min(3.0, float(len(lit_entries)))
        weighted_sum += lit_conf * w
        weights += w
    overall = _normalize_confidence((weighted_sum / weights) if weights else 0.0, default=0.0)

    rationale = (
        f"exp={len(exp_entries)} entry(s), lit={len(lit_entries)} entry(s), "
        f"exp_conf={_fmt_number(exp_conf)}, lit_conf={_fmt_number(lit_conf)}"
    )
    return exp_conf, lit_conf, overall, rationale


def _write_claim_evidence_matrix(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    by_literature: dict[str, list[LiteratureRecord]],
    generated_at: str,
) -> dict[str, Any]:
    exp_runs = [run for exp_runs in by_experiment.values() for run in exp_runs]
    exp_runs.sort(key=lambda r: (r.timestamp, r.experiment_type, r.run_id))

    lit_entries = [entry for lit_runs in by_literature.values() for entry in lit_runs]
    lit_entries.sort(key=lambda e: (e.timestamp, e.literature_type, e.entry_id))

    matrix: dict[str, Any] = {
        "schema_version": "claim_evidence_matrix/v1",
        "generated_at_utc": generated_at,
        "source_root": "evidence",
        "claims": {},
        "entries": [],
        "unlinked_runs": [],
    }

    claim_to_entries: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for run in exp_runs:
        inferred_direction = run.evidence_direction
        if inferred_direction == "unknown":
            inferred_direction = "supports" if run.final_status == "PASS" else "weakens"

        entry_confidence, entry_confidence_rationale = _experimental_entry_confidence(run, inferred_direction)

        if not run.claim_ids_tested:
            matrix["unlinked_runs"].append(
                {
                    "source_type": "experimental",
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
                "source_type": "experimental",
                "experiment_type": run.experiment_type,
                "run_id": run.run_id,
                "timestamp_utc": run.timestamp_raw,
                "status": run.final_status,
                "evidence_class": _prefix_class("experimental", run.evidence_class),
                "evidence_direction": inferred_direction,
                "confidence": entry_confidence,
                "confidence_rationale": entry_confidence_rationale,
                "failure_signatures": run.failure_signatures,
                "source_repo": {
                    "name": run.source_repo_name,
                    "commit": run.source_repo_commit,
                    "branch": run.source_repo_branch,
                },
                "environment": {
                    "env_id": run.environment.get("env_id", ""),
                    "env_version": run.environment.get("env_version", ""),
                    "tier": run.environment.get("tier", ""),
                    "status": run.environment_status,
                },
            }
            matrix["entries"].append(entry)
            claim_to_entries[claim_id].append(entry)

    for lit in lit_entries:
        if not lit.claim_ids_tested:
            matrix["unlinked_runs"].append(
                {
                    "source_type": "literature",
                    "experiment_type": lit.literature_type,
                    "run_id": lit.entry_id,
                    "timestamp_utc": lit.timestamp_raw,
                    "status": "SOURCE",
                }
            )
            continue

        for claim_id in lit.claim_ids_tested:
            entry = {
                "claim_id": claim_id,
                "source_type": "literature",
                "experiment_type": lit.literature_type,
                "run_id": lit.entry_id,
                "timestamp_utc": lit.timestamp_raw,
                "status": "SOURCE",
                "evidence_class": _prefix_class("literature", lit.evidence_class),
                "evidence_direction": lit.evidence_direction,
                "confidence": lit.confidence,
                "confidence_rationale": lit.confidence_rationale,
                "failure_signatures": lit.failure_signatures,
            }
            matrix["entries"].append(entry)
            claim_to_entries[claim_id].append(entry)

    now = _parse_timestamp_only(generated_at)
    for claim_id in sorted(claim_to_entries.keys()):
        entries = claim_to_entries[claim_id]
        entries.sort(key=lambda e: (e["timestamp_utc"], e["run_id"]))

        direction_counts = {
            "supports": 0,
            "weakens": 0,
            "mixed": 0,
            "unknown": 0,
        }
        evidence_class_counts: dict[str, int] = {}
        source_counts = {"experimental": 0, "literature": 0}

        pass_runs = 0
        fail_runs = 0

        for entry in entries:
            direction = str(entry.get("evidence_direction", "unknown"))
            direction_counts[direction] = direction_counts.get(direction, 0) + 1

            evidence_class = str(entry.get("evidence_class", "unclassified"))
            evidence_class_counts[evidence_class] = evidence_class_counts.get(evidence_class, 0) + 1

            source = str(entry.get("source_type", "experimental"))
            source_counts[source] = source_counts.get(source, 0) + 1

            status = str(entry.get("status", "PASS"))
            if status == "PASS":
                pass_runs += 1
            if status == "FAIL":
                fail_runs += 1

        exp_conf, lit_conf, overall_conf, rationale = _compute_claim_confidence(entries, now)

        latest = entries[-1]
        matrix["claims"][claim_id] = {
            "runs_total": len(entries),
            "entries_total": len(entries),
            "pass_runs": pass_runs,
            "fail_runs": fail_runs,
            "latest_run_id": latest["run_id"],
            "latest_timestamp_utc": latest["timestamp_utc"],
            "direction_counts": direction_counts,
            "evidence_class_counts": evidence_class_counts,
            "source_counts": source_counts,
            "experimental_confidence": exp_conf,
            "literature_confidence": lit_conf,
            "overall_confidence": overall_conf,
            "confidence_rationale": rationale,
            "recent_entries": entries[-5:],
        }

    matrix["entries"].sort(
        key=lambda e: (e["timestamp_utc"], e["claim_id"], e["experiment_type"], e["run_id"])
    )
    matrix["unlinked_runs"].sort(
        key=lambda e: (e["timestamp_utc"], e["source_type"], e["experiment_type"], e["run_id"])
    )

    (base_dir / "claim_evidence.v1.json").write_text(
        json.dumps(matrix, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return matrix


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


def _load_claim_registry(path: Path) -> dict[str, dict[str, str]]:
    """Parse claim id/status/type from docs/claims/claims.yaml.

    This parser intentionally handles the repository's simple YAML pattern and avoids non-stdlib deps.
    """
    registry: dict[str, dict[str, str]] = {}
    current_id: str | None = None
    current_status: str | None = None
    current_type: str | None = None

    if not path.exists():
        return registry

    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("- id:"):
            if current_id:
                registry[current_id] = {
                    "status": current_status or "unknown",
                    "claim_type": current_type or "unknown",
                }
            current_id = line.split(":", 1)[1].strip()
            current_status = None
            current_type = None
            continue

        if current_id and line.startswith("  status:"):
            current_status = line.split(":", 1)[1].strip()
            continue

        if current_id and line.startswith("  claim_type:"):
            current_type = line.split(":", 1)[1].strip()
            continue

    if current_id:
        registry[current_id] = {
            "status": current_status or "unknown",
            "claim_type": current_type or "unknown",
        }
    return registry


def _default_decision_criteria() -> dict[str, Any]:
    return {
        "schema_version": "decision_criteria/v1",
        "decision_status_default": "pending_user",
        "thresholds": {
            "candidate_to_provisional": {
                "min_overall_confidence": 0.62,
                "min_experimental_entries": 2,
                "max_conflict_ratio": 0.35,
            },
            "provisional_to_stable": {
                "min_overall_confidence": 0.80,
                "min_experimental_entries": 4,
                "min_literature_entries": 2,
                "max_conflict_ratio": 0.20,
            },
            "demote_on_conflict": {
                "min_total_entries": 3,
                "min_conflict_ratio": 0.55,
                "max_overall_confidence": 0.55,
            },
        },
    }


def _load_decision_criteria(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_decision_criteria()
    data = _load_json_compatible_yaml(path, "decision criteria")
    if "thresholds" not in data:
        data["thresholds"] = _default_decision_criteria()["thresholds"]
    if "decision_status_default" not in data:
        data["decision_status_default"] = "pending_user"
    return data


def _default_environment_qualification() -> dict[str, Any]:
    return {
        "schema_version": "environment_qualification/v1",
        "required_manifest_environment_fields": [
            "env_id",
            "env_version",
            "dynamics_hash",
            "reward_hash",
            "observation_hash",
            "config_hash",
            "tier",
        ],
        "qualification_metrics": {
            "default": [
                {
                    "metric": "environment_shortcut_leakage_events",
                    "op": "==",
                    "threshold": 0,
                },
                {
                    "metric": "environment_unobservable_critical_state_rate",
                    "op": "<=",
                    "threshold": 0.05,
                },
            ],
            "experiments": {},
        },
        "drift": {
            "min_runs_per_series": 2,
            "warn_if_relative_change_gt": 0.25,
            "warn_if_direction_flip": True,
            "key_metrics_per_experiment": {},
        },
        "dispatch": {
            "required_manifest_fields": [
                "environment",
            ],
            "required_environment_fields": [
                "env_id",
                "env_version",
                "dynamics_hash",
                "reward_hash",
                "observation_hash",
                "config_hash",
                "tier",
            ],
            "required_environment_tiers_by_priority": {
                "high": ["toy", "stress"],
                "medium": ["toy"],
                "low": [],
            },
        },
    }


def _load_environment_qualification(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_environment_qualification()
    data = _load_json_compatible_yaml(path, "environment qualification")
    defaults = _default_environment_qualification()

    for key in ("required_manifest_environment_fields", "qualification_metrics", "drift", "dispatch"):
        if key not in data:
            data[key] = defaults[key]
    return data


def _environment_metric_rules_for_experiment(
    environment_qualification: dict[str, Any], experiment_type: str
) -> list[dict[str, Any]]:
    metrics_cfg = environment_qualification.get("qualification_metrics", {})
    default_rules = []
    experiment_rules = []
    if isinstance(metrics_cfg, dict):
        if isinstance(metrics_cfg.get("default"), list):
            default_rules = metrics_cfg.get("default", [])
        experiments = metrics_cfg.get("experiments", {})
        if isinstance(experiments, dict) and isinstance(experiments.get(experiment_type), list):
            experiment_rules = experiments.get(experiment_type, [])
    merged: list[dict[str, Any]] = []
    for rule in [*default_rules, *experiment_rules]:
        if isinstance(rule, dict):
            merged.append(rule)
    return merged


def _evaluate_environment_quality(
    runs: list[RunRecord], environment_qualification: dict[str, Any], experiment_type: str
) -> None:
    required_fields = _string_list(
        environment_qualification.get("required_manifest_environment_fields", [])
    )
    rules = _environment_metric_rules_for_experiment(environment_qualification, experiment_type)

    for run in runs:
        missing_fields: list[str] = []
        if not run.environment_declared:
            missing_fields = list(required_fields)
        else:
            for field_name in required_fields:
                value = run.environment.get(field_name, "")
                if not str(value).strip():
                    missing_fields.append(field_name)

        missing_metrics: list[str] = []
        metric_fail_hits: list[StopHit] = []
        for rule in rules:
            metric = rule.get("metric")
            op = rule.get("op")
            threshold = rule.get("threshold")
            if not isinstance(metric, str) or not isinstance(op, str):
                continue
            if not isinstance(threshold, (int, float)):
                continue

            value = run.metrics.get(metric)
            if value is None:
                missing_metrics.append(metric)
                continue
            if _compare(value, op, float(threshold)):
                metric_fail_hits.append(
                    StopHit(
                        metric=metric,
                        op=op,
                        threshold=float(threshold),
                        value=float(value),
                    )
                )

        run.environment_missing_fields = missing_fields
        run.environment_missing_metrics = sorted(set(missing_metrics))
        run.environment_fail_hits = metric_fail_hits

        if missing_fields:
            run.environment_status = "missing_environment_metadata"
        elif metric_fail_hits:
            run.environment_status = "environment_unqualified"
        elif missing_metrics:
            run.environment_status = "missing_environment_metrics"
        else:
            run.environment_status = "environment_qualified"

def _default_conflict_adjudication() -> dict[str, Any]:
    return {
        "schema_version": "conflict_adjudication/v1",
        "default": {
            "resolution_actions": [
                "Run one targeted adjudication experiment with narrower stop criteria.",
                "Add one replication run with seed sweep to reduce variance ambiguity.",
                "If disagreement persists, split claim scope into separable subclaims.",
            ],
            "adjudication_criteria": [],
            "evidence_targets": [],
            "dispatch_requirements": {
                "manifest_fields": [],
                "metrics_required_keys": [],
                "required_capabilities": [],
                "summary_must_include": [],
                "extra_acceptance_checks": [],
            },
        },
        "claims": {},
    }


def _string_list(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    cleaned: list[str] = []
    for value in values:
        text = str(value).strip()
        if text:
            cleaned.append(text)
    return cleaned


def _merge_unique(base: list[str], extra: list[str]) -> list[str]:
    merged: list[str] = []
    for token in [*base, *extra]:
        text = str(token).strip()
        if text and text not in merged:
            merged.append(text)
    return merged


def _load_conflict_adjudication(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_conflict_adjudication()

    data = _load_json_compatible_yaml(path, "conflict adjudication")
    defaults = _default_conflict_adjudication()
    if "default" not in data:
        data["default"] = defaults["default"]
    if "claims" not in data:
        data["claims"] = {}
    if "schema_version" not in data:
        data["schema_version"] = defaults["schema_version"]
    return data


def _conflict_policy_for_claim(conflict_adjudication: dict[str, Any], claim_id: str) -> dict[str, Any]:
    default_policy = (
        conflict_adjudication.get("default", {})
        if isinstance(conflict_adjudication.get("default"), dict)
        else {}
    )
    claims = conflict_adjudication.get("claims", {})
    claim_policy = {}
    if isinstance(claims, dict) and isinstance(claims.get(claim_id), dict):
        claim_policy = claims.get(claim_id, {})

    resolution_actions = _string_list(
        claim_policy.get("resolution_actions", default_policy.get("resolution_actions", []))
    )
    if not resolution_actions:
        resolution_actions = _string_list(
            _default_conflict_adjudication()["default"]["resolution_actions"]
        )

    adjudication_criteria = _string_list(
        claim_policy.get("adjudication_criteria", default_policy.get("adjudication_criteria", []))
    )
    evidence_targets = _string_list(
        claim_policy.get("evidence_targets", default_policy.get("evidence_targets", []))
    )
    summary = str(claim_policy.get("summary", "")).strip()

    default_dispatch = (
        default_policy.get("dispatch_requirements", {})
        if isinstance(default_policy.get("dispatch_requirements"), dict)
        else {}
    )
    claim_dispatch = (
        claim_policy.get("dispatch_requirements", {})
        if isinstance(claim_policy.get("dispatch_requirements"), dict)
        else {}
    )
    dispatch_requirements = {
        "manifest_fields": _merge_unique(
            _string_list(default_dispatch.get("manifest_fields", [])),
            _string_list(claim_dispatch.get("manifest_fields", [])),
        ),
        "metrics_required_keys": _merge_unique(
            _string_list(default_dispatch.get("metrics_required_keys", [])),
            _string_list(claim_dispatch.get("metrics_required_keys", [])),
        ),
        "required_capabilities": _merge_unique(
            _string_list(default_dispatch.get("required_capabilities", [])),
            _string_list(claim_dispatch.get("required_capabilities", [])),
        ),
        "summary_must_include": _merge_unique(
            _string_list(default_dispatch.get("summary_must_include", [])),
            _string_list(claim_dispatch.get("summary_must_include", [])),
        ),
        "extra_acceptance_checks": _merge_unique(
            _string_list(default_dispatch.get("extra_acceptance_checks", [])),
            _string_list(claim_dispatch.get("extra_acceptance_checks", [])),
        ),
    }

    return {
        "summary": summary,
        "resolution_actions": resolution_actions,
        "adjudication_criteria": adjudication_criteria,
        "evidence_targets": evidence_targets,
        "dispatch_requirements": dispatch_requirements,
    }


def _default_planning_criteria() -> dict[str, Any]:
    return {
        "schema_version": "planning_criteria/v1",
        "thresholds": {
            "low_overall_confidence": 0.55,
            "conflict_ratio_alert": 0.40,
            "candidate_min_experimental_entries": 2,
            "provisional_min_literature_entries": 2,
        },
        "repo_routing": {
            "experimental_default_repo": "ree-v1-minimal",
            "exploratory_repo": "ree-experiments-lab",
            "literature_owner": "REE_assembly",
        },
        "capability_gating": {
            "fail_closed": True,
        },
    }


def _load_planning_criteria(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_planning_criteria()
    data = _load_json_compatible_yaml(path, "planning criteria")
    defaults = _default_planning_criteria()
    if "thresholds" not in data:
        data["thresholds"] = defaults["thresholds"]
    if "repo_routing" not in data:
        data["repo_routing"] = defaults["repo_routing"]
    if "capability_gating" not in data:
        data["capability_gating"] = defaults["capability_gating"]
    return data


def _load_decision_log(path: Path) -> list[DecisionLogEntry]:
    if not path.exists():
        return []

    entries: list[DecisionLogEntry] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue

        claim_id = str(obj.get("claim_id", "")).strip()
        decision_status = str(obj.get("decision_status", "")).strip()
        recommendation = str(obj.get("recommendation", "")).strip()
        decision_needed = str(obj.get("decision_needed", "")).strip()
        timestamp_utc = str(obj.get("timestamp_utc", "")).strip()
        if not claim_id or not decision_status or not timestamp_utc:
            continue

        entries.append(
            DecisionLogEntry(
                claim_id=claim_id,
                decision_status=decision_status,
                recommendation=recommendation,
                decision_needed=decision_needed,
                timestamp_utc=timestamp_utc,
                selected_option=str(obj.get("selected_option", "")).strip(),
                rationale=str(obj.get("rationale", "")).strip(),
                actor=str(obj.get("actor", "user")).strip() or "user",
            )
        )
    return entries


def _latest_decision_by_claim(entries: list[DecisionLogEntry]) -> dict[str, DecisionLogEntry]:
    latest: dict[str, DecisionLogEntry] = {}
    for entry in entries:
        existing = latest.get(entry.claim_id)
        if existing is None:
            latest[entry.claim_id] = entry
            continue
        if entry.timestamp_utc >= existing.timestamp_utc:
            latest[entry.claim_id] = entry
    return latest


def _write_decision_state(
    decisions_dir: Path,
    latest_by_claim: dict[str, DecisionLogEntry],
    generated_at: str,
) -> None:
    state = {
        "schema_version": "decision_state/v1",
        "generated_at_utc": generated_at,
        "source": "evidence/decisions/decision_log.v1.jsonl",
        "claims": {},
    }
    for claim_id in sorted(latest_by_claim.keys()):
        entry = latest_by_claim[claim_id]
        state["claims"][claim_id] = {
            "decision_status": entry.decision_status,
            "recommendation": entry.recommendation,
            "decision_needed": entry.decision_needed,
            "selected_option": entry.selected_option,
            "rationale": entry.rationale,
            "actor": entry.actor,
            "timestamp_utc": entry.timestamp_utc,
        }

    decisions_dir.mkdir(parents=True, exist_ok=True)
    (decisions_dir / "decision_state.v1.json").write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _recommendation_for_claim(
    claim_id: str,
    claim_meta: dict[str, Any],
    current_status: str,
    claim_type: str,
    criteria: dict[str, Any],
) -> dict[str, Any]:
    thresholds = criteria.get("thresholds", {})
    t_candidate = thresholds.get("candidate_to_provisional", {})
    t_stable = thresholds.get("provisional_to_stable", {})
    t_demote = thresholds.get("demote_on_conflict", {})

    direction_counts = claim_meta.get("direction_counts", {})
    conflict_ratio = _direction_conflict_ratio(direction_counts)
    overall_conf = float(claim_meta.get("overall_confidence", 0.0))
    exp_entries = int(claim_meta.get("source_counts", {}).get("experimental", 0))
    lit_entries = int(claim_meta.get("source_counts", {}).get("literature", 0))
    total_entries = int(claim_meta.get("entries_total", 0))

    decision_needed = "No immediate status change"
    recommendation = "hold"
    rationale = (
        f"overall_conf={_fmt_number(overall_conf)}, conflict_ratio={_fmt_number(conflict_ratio)}, "
        f"exp_entries={exp_entries}, lit_entries={lit_entries}"
    )

    if current_status == "candidate":
        meets_promote = (
            overall_conf >= float(t_candidate.get("min_overall_confidence", 0.62))
            and exp_entries >= int(t_candidate.get("min_experimental_entries", 2))
            and conflict_ratio <= float(t_candidate.get("max_conflict_ratio", 0.35))
        )
        if meets_promote:
            decision_needed = "Promotion review: candidate -> provisional"
            recommendation = "promote_to_provisional"
        elif conflict_ratio > float(t_candidate.get("max_conflict_ratio", 0.35)):
            decision_needed = "Conflict resolution before promotion"
            recommendation = "hold_candidate_resolve_conflict"

    elif current_status == "provisional":
        meets_stable = (
            overall_conf >= float(t_stable.get("min_overall_confidence", 0.8))
            and exp_entries >= int(t_stable.get("min_experimental_entries", 4))
            and lit_entries >= int(t_stable.get("min_literature_entries", 2))
            and conflict_ratio <= float(t_stable.get("max_conflict_ratio", 0.2))
        )
        demote_trigger = (
            total_entries >= int(t_demote.get("min_total_entries", 3))
            and conflict_ratio >= float(t_demote.get("min_conflict_ratio", 0.55))
            and overall_conf <= float(t_demote.get("max_overall_confidence", 0.55))
        )
        if meets_stable:
            decision_needed = "Promotion review: provisional -> stable"
            recommendation = "promote_to_stable"
        elif demote_trigger:
            decision_needed = "Demotion review: provisional -> candidate"
            recommendation = "demote_to_candidate"

    elif current_status in {"active", "stable"}:
        demote_trigger = (
            total_entries >= int(t_demote.get("min_total_entries", 3))
            and conflict_ratio >= float(t_demote.get("min_conflict_ratio", 0.55))
            and overall_conf <= float(t_demote.get("max_overall_confidence", 0.55))
        )
        if demote_trigger:
            target = "provisional" if current_status == "stable" else "candidate"
            decision_needed = f"Demotion review: {current_status} -> {target}"
            recommendation = f"demote_to_{target}"

    elif claim_type == "open_question" and total_entries >= 2 and conflict_ratio < 0.35:
        decision_needed = "Question narrowing review"
        recommendation = "narrow_open_question"

    option_set = {
        "promote_to_provisional": [
            "Promote now (faster convergence, risk premature lock-in)",
            "Hold until one additional confirming run (better robustness, slower progress)",
            "Hold and request targeted literature triangulation (better external grounding, extra delay)",
        ],
        "promote_to_stable": [
            "Promote now (clear canonical status, risk under-tested edge cases)",
            "Hold pending stress-test replication (better stress confidence, slower closure)",
            "Split claim scope before promotion (clearer boundaries, added doc work)",
        ],
        "demote_to_candidate": [
            "Demote now (reduces false certainty, destabilizes current roadmap references)",
            "Hold and run conflict-resolution suite first (more data, temporary ambiguity)",
            "Split into subclaims (isolates conflict, increases registry complexity)",
        ],
        "demote_to_provisional": [
            "Demote now (acknowledges uncertainty, may disrupt dependent docs)",
            "Hold and run adjudication experiments (better confidence, slower correction)",
            "Constrain claim scope instead (preserves momentum, might hide deeper conflict)",
        ],
        "hold_candidate_resolve_conflict": [
            "Keep candidate and run conflict-resolution experiments (most balanced)",
            "Promote despite conflict (speed, high lock-in risk)",
            "Demote to legacy (conservative, may discard useful partial mechanism)",
        ],
        "narrow_open_question": [
            "Narrow the question into testable sub-questions (higher tractability)",
            "Keep broad question (flexibility, weaker experiment planning)",
            "Convert one branch into candidate mechanism (progress, possible overcommitment)",
        ],
        "hold": [
            "No status change (stable governance)",
            "Request additional evidence anyway (higher confidence, extra cost)",
            "Force a status vote now (faster decision, weak evidential basis)",
        ],
    }

    discussion_prompts = [
        "Which uncertainty source dominates: model variance, threshold choice, or claim scope?",
        "What single additional experiment or literature extraction would most reduce uncertainty?",
        "If this decision is wrong, what downstream architecture risk is largest?",
    ]

    return {
        "claim_id": claim_id,
        "current_status": current_status,
        "decision_needed": decision_needed,
        "recommendation": recommendation,
        "rationale": rationale,
        "options": option_set.get(recommendation, option_set["hold"]),
        "discussion_prompts": discussion_prompts,
        "decision_status": str(criteria.get("decision_status_default", "pending_user")),
    }


def _write_promotion_demotion_recommendations(
    base_dir: Path,
    matrix: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
    decision_criteria: dict[str, Any],
    latest_decisions: dict[str, DecisionLogEntry],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Promotion / Demotion Recommendations")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("This file proposes decisions only. No claim status changes are applied automatically.")
    lines.append("Use this as the human-in-the-loop review queue.")
    lines.append("")

    recommendations: list[dict[str, Any]] = []
    for claim_id in sorted(matrix.get("claims", {}).keys()):
        claim_meta = matrix["claims"][claim_id]
        registry_meta = claim_registry.get(claim_id, {})
        current_status = str(registry_meta.get("status", "unknown"))
        claim_type = str(registry_meta.get("claim_type", "unknown"))

        rec = _recommendation_for_claim(
            claim_id=claim_id,
            claim_meta=claim_meta,
            current_status=current_status,
            claim_type=claim_type,
            criteria=decision_criteria,
        )

        prior = latest_decisions.get(claim_id)
        rec["last_decision"] = None
        if prior is not None:
            rec["last_decision"] = {
                "decision_status": prior.decision_status,
                "recommendation": prior.recommendation,
                "decision_needed": prior.decision_needed,
                "timestamp_utc": prior.timestamp_utc,
                "selected_option": prior.selected_option,
                "rationale": prior.rationale,
                "actor": prior.actor,
            }
            if prior.recommendation == rec["recommendation"]:
                rec["decision_status"] = prior.decision_status
            else:
                rec["decision_status"] = str(
                    decision_criteria.get("decision_status_default", "pending_user")
                )
                rec["status_note"] = (
                    "Prior decision exists but recommendation changed; needs fresh review."
                )

        # Only surface items requiring explicit review.
        if rec["recommendation"] == "hold" and rec["decision_needed"] == "No immediate status change":
            continue
        recommendations.append(rec)

    lines.append("## Decision Queue")
    lines.append("")
    lines.append("| claim_id | current_status | decision_needed | recommendation | decision_status |")
    lines.append("|---|---|---|---|---|")

    if not recommendations:
        lines.append("| _none_ | - | No status changes recommended | - | - |")
    else:
        for rec in recommendations:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{rec['claim_id']}`",
                        f"`{rec['current_status']}`",
                        rec["decision_needed"],
                        f"`{rec['recommendation']}`",
                        f"`{rec['decision_status']}`",
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("## Decision Details")
    lines.append("")

    if not recommendations:
        lines.append("No pending promotion/demotion decisions from current evidence.")
    else:
        for rec in recommendations:
            claim_id = rec["claim_id"]
            claim_meta = matrix["claims"].get(claim_id, {})
            supports = int(claim_meta.get("direction_counts", {}).get("supports", 0))
            weakens = int(claim_meta.get("direction_counts", {}).get("weakens", 0))
            mixed = int(claim_meta.get("direction_counts", {}).get("mixed", 0))
            unknown = int(claim_meta.get("direction_counts", {}).get("unknown", 0))
            conflict_ratio = _direction_conflict_ratio(claim_meta.get("direction_counts", {}))

            lines.append(f"### {claim_id}")
            lines.append(f"- Current status: `{rec['current_status']}`")
            lines.append(f"- Decision needed: {rec['decision_needed']}")
            lines.append(
                "- Why this decision is needed: "
                + f"{rec['rationale']}; directions supports={supports}, weakens={weakens}, mixed={mixed}, unknown={unknown}, conflict_ratio={_fmt_number(conflict_ratio)}"
            )
            lines.append(f"- Recommendation: `{rec['recommendation']}`")
            lines.append("- Options (pros/cons):")
            for option in rec["options"]:
                lines.append(f"  - {option}")
            lines.append("- Discussion scope with Codex:")
            for prompt in rec["discussion_prompts"]:
                lines.append(f"  - {prompt}")
            lines.append(f"- Decision status: `{rec['decision_status']}`")
            if rec.get("status_note"):
                lines.append(f"- Status note: {rec['status_note']}")
            if rec.get("last_decision"):
                prior = rec["last_decision"]
                lines.append(
                    "- Last logged decision: "
                    + f"`{prior['decision_status']}` by `{prior['actor']}` at `{prior['timestamp_utc']}`"
                )
                if prior.get("selected_option"):
                    lines.append(f"- Last selected option: {prior['selected_option']}")
                if prior.get("rationale"):
                    lines.append(f"- Last rationale: {prior['rationale']}")
            lines.append("")

    (base_dir / "promotion_demotion_recommendations.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def _majority_direction(entries: list[dict[str, Any]], source_type: str) -> str:
    subset = [e for e in entries if e.get("source_type") == source_type]
    counts = Counter(str(e.get("evidence_direction", "unknown")) for e in subset)
    directional = {"supports": counts.get("supports", 0), "weakens": counts.get("weakens", 0)}
    if directional["supports"] == directional["weakens"]:
        return "tie"
    return "supports" if directional["supports"] > directional["weakens"] else "weakens"


def _collect_conflicts(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        entries_by_claim[str(entry.get("claim_id"))].append(entry)

    conflicts: list[dict[str, Any]] = []
    for claim_id in sorted(matrix.get("claims", {}).keys()):
        claim_meta = matrix["claims"][claim_id]
        supports = int(claim_meta.get("direction_counts", {}).get("supports", 0))
        weakens = int(claim_meta.get("direction_counts", {}).get("weakens", 0))
        mixed = int(claim_meta.get("direction_counts", {}).get("mixed", 0))

        direction_conflict = supports > 0 and weakens > 0

        claim_entries = entries_by_claim.get(claim_id, [])
        exp_majority = _majority_direction(claim_entries, "experimental")
        lit_majority = _majority_direction(claim_entries, "literature")
        source_conflict = (
            exp_majority in {"supports", "weakens"}
            and lit_majority in {"supports", "weakens"}
            and exp_majority != lit_majority
        )

        if not (direction_conflict or source_conflict):
            continue

        conflict_types: list[str] = []
        if direction_conflict:
            conflict_types.append("directional")
        if source_conflict:
            conflict_types.append("source_disagreement")
        if mixed > 0:
            conflict_types.append("mixed_evidence")

        conflicts.append(
            {
                "claim_id": claim_id,
                "conflict_types": conflict_types,
                "supports": supports,
                "weakens": weakens,
                "conflict_ratio": _direction_conflict_ratio(claim_meta.get("direction_counts", {})),
                "latest": claim_meta.get("latest_run_id", ""),
            }
        )
    return conflicts


def _write_conflicts_report(
    base_dir: Path,
    matrix: dict[str, Any],
    conflicts: list[dict[str, Any]],
    generated_at: str,
    conflict_adjudication: dict[str, Any],
) -> None:
    lines: list[str] = []
    lines.append("# Evidence Conflict Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")

    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        entries_by_claim[str(entry.get("claim_id"))].append(entry)

    lines.append("## Conflict Queue")
    lines.append("")
    lines.append("| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |")
    lines.append("|---|---|---|---|---|---|")

    if not conflicts:
        lines.append("| _none_ | - | 0 | 0 | 0 | - |")
    else:
        for item in conflicts:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item['claim_id']}`",
                        ", ".join(item["conflict_types"]),
                        str(item["supports"]),
                        str(item["weakens"]),
                        _fmt_number(item["conflict_ratio"]),
                        f"`{item['latest']}`",
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("## Conflict Details")
    lines.append("")

    if not conflicts:
        lines.append("No active evidence conflicts detected.")
    else:
        for item in conflicts:
            claim_id = item["claim_id"]
            claim_meta = matrix["claims"][claim_id]
            claim_entries = entries_by_claim.get(claim_id, [])
            claim_entries.sort(key=lambda e: (e["timestamp_utc"], e["run_id"]))
            recent = claim_entries[-5:]
            policy = _conflict_policy_for_claim(conflict_adjudication, claim_id)

            signature_counts: Counter[str] = Counter()
            for entry in claim_entries:
                for sig in entry.get("failure_signatures", []):
                    signature_counts[str(sig)] += 1

            lines.append(f"### {claim_id}")
            lines.append(f"- Conflict types: {', '.join(item['conflict_types'])}")
            lines.append(
                "- Evidence breakdown: "
                + f"supports={item['supports']}, weakens={item['weakens']}, conflict_ratio={_fmt_number(item['conflict_ratio'])}, "
                + f"overall_confidence={_fmt_number(claim_meta.get('overall_confidence', 0.0))}"
            )
            lines.append("- Recent entries:")
            for entry in recent:
                lines.append(
                    f"  - `{entry['timestamp_utc']}` `{entry['source_type']}` `{entry['experiment_type']}` "
                    + f"direction=`{entry['evidence_direction']}` confidence={_fmt_number(entry.get('confidence', 0.0))}"
                )

            if signature_counts:
                lines.append("- Recurring failure signatures:")
                for sig, count in signature_counts.most_common(5):
                    lines.append(f"  - `{sig}` ({count})")

            if policy["summary"]:
                lines.append(f"- Claim-specific framing: {policy['summary']}")

            lines.append("- Suggested resolution actions:")
            for action in policy["resolution_actions"]:
                lines.append(f"  - {action}")

            if policy["adjudication_criteria"]:
                lines.append("- Adjudication criteria:")
                for criterion in policy["adjudication_criteria"]:
                    lines.append(f"  - {criterion}")

            if policy["evidence_targets"]:
                lines.append("- Evidence targets:")
                for target in policy["evidence_targets"]:
                    lines.append(f"  - {target}")
            lines.append("")

    (base_dir / "conflicts.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def _priority_rank(priority: str) -> int:
    return {"high": 0, "medium": 1, "low": 2}.get(priority, 3)


def _priority_from_reasons(reasons: list[str]) -> str:
    high_markers = {
        "directional_conflict_alert",
        "active_conflict",
        "missing_experimental_evidence",
    }
    medium_markers = {
        "low_overall_confidence",
        "insufficient_experimental_replication",
        "insufficient_literature_grounding",
        "missing_literature_evidence",
    }
    if any(reason in high_markers for reason in reasons):
        return "high"
    if any(reason in medium_markers for reason in reasons):
        return "medium"
    return "low"


def _suggest_experiment_type(claim_id: str, matrix: dict[str, Any]) -> str:
    counts: Counter[str] = Counter()
    for entry in matrix.get("entries", []):
        if entry.get("claim_id") == claim_id and entry.get("source_type") == "experimental":
            counts.update([str(entry.get("experiment_type", "claim_probe"))])
    if counts:
        return counts.most_common(1)[0][0]
    return f"claim_probe_{claim_id.lower().replace('-', '_')}"


def _suggest_literature_type(claim_id: str, matrix: dict[str, Any]) -> str:
    counts: Counter[str] = Counter()
    for entry in matrix.get("entries", []):
        if entry.get("claim_id") == claim_id and entry.get("source_type") == "literature":
            counts.update([str(entry.get("experiment_type", "targeted_review"))])
    if counts:
        return counts.most_common(1)[0][0]
    return f"targeted_review_{claim_id.lower().replace('-', '_')}"


def _extract_markdown_section_items(path: Path, heading: str) -> list[str]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            start = idx + 1
            break
    if start is None:
        return []

    items: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        stripped = line.strip()
        if stripped.startswith("- "):
            token = stripped[2:].strip()
            if token:
                items.append(token)
    return items


def _experiment_profile(experiments_root: Path, experiment_type: str) -> dict[str, Any]:
    profile_path = experiments_root / experiment_type / "experiment.md"
    what_it_tests = _extract_markdown_section_items(profile_path, "## What it tests")
    failure_modes = _extract_markdown_section_items(profile_path, "## Failure modes it detects")
    return {
        "profile_path": profile_path,
        "what_it_tests": what_it_tests,
        "failure_modes": failure_modes,
    }


def _repo_capability_snapshots(by_experiment: dict[str, list[RunRecord]]) -> dict[str, dict[str, Any]]:
    runs = [run for exp_runs in by_experiment.values() for run in exp_runs]
    runs.sort(key=lambda r: (r.timestamp, r.experiment_type, r.run_id))
    snapshots: dict[str, dict[str, Any]] = {}

    for run in runs:
        repo = run.source_repo_name.strip() or "unknown"
        if repo == "unknown":
            continue
        if not run.producer_capabilities_declared:
            continue
        snapshots[repo] = {
            "repo": repo,
            "timestamp_utc": run.timestamp_raw,
            "run_id": run.run_id,
            "experiment_type": run.experiment_type,
            "capabilities": dict(run.producer_capabilities),
        }
    return snapshots


def _environment_dispatch_requirements(
    environment_qualification: dict[str, Any], experiment_type: str, priority: str
) -> dict[str, list[str]]:
    dispatch_cfg = (
        environment_qualification.get("dispatch", {})
        if isinstance(environment_qualification.get("dispatch"), dict)
        else {}
    )
    required_manifest_fields = _string_list(dispatch_cfg.get("required_manifest_fields", []))
    required_environment_fields = _string_list(dispatch_cfg.get("required_environment_fields", []))

    tiers_cfg = dispatch_cfg.get("required_environment_tiers_by_priority", {})
    required_tiers: list[str] = []
    if isinstance(tiers_cfg, dict):
        required_tiers = _string_list(tiers_cfg.get(priority, []))

    required_metric_keys: list[str] = []
    for rule in _environment_metric_rules_for_experiment(environment_qualification, experiment_type):
        metric = rule.get("metric")
        if isinstance(metric, str) and metric not in required_metric_keys:
            required_metric_keys.append(metric)

    return {
        "required_manifest_fields": required_manifest_fields,
        "required_environment_fields": required_environment_fields,
        "required_environment_tiers": required_tiers,
        "required_environment_metrics": required_metric_keys,
    }


def _write_planning_outputs(
    planning_root: Path,
    by_experiment: dict[str, list[RunRecord]],
    matrix: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
    conflicts: list[dict[str, Any]],
    latest_decisions: dict[str, DecisionLogEntry],
    planning_criteria: dict[str, Any],
    conflict_adjudication: dict[str, Any],
    environment_qualification: dict[str, Any],
    generated_at: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    thresholds = planning_criteria.get("thresholds", {})
    routing = planning_criteria.get("repo_routing", {})

    low_conf_threshold = float(thresholds.get("low_overall_confidence", 0.55))
    conflict_alert_threshold = float(thresholds.get("conflict_ratio_alert", 0.40))
    candidate_min_exp = int(thresholds.get("candidate_min_experimental_entries", 2))
    provisional_min_lit = int(thresholds.get("provisional_min_literature_entries", 2))

    default_exp_repo = str(routing.get("experimental_default_repo", "ree-v1-minimal"))
    exploratory_repo = str(routing.get("exploratory_repo", "ree-experiments-lab"))
    literature_owner = str(routing.get("literature_owner", "REE_assembly"))
    capability_cfg = planning_criteria.get("capability_gating", {})
    fail_closed = bool(capability_cfg.get("fail_closed", True))

    repo_caps = _repo_capability_snapshots(by_experiment)
    experiments_root = planning_root.parent / "experiments"

    conflicts_by_claim = {str(item.get("claim_id")): item for item in conflicts}
    matrix_claims = matrix.get("claims", {})
    claim_ids = sorted(set(claim_registry.keys()) | set(matrix_claims.keys()))

    backlog_items: list[dict[str, Any]] = []
    for claim_id in claim_ids:
        registry_meta = claim_registry.get(claim_id, {})
        current_status = str(registry_meta.get("status", "unknown"))
        claim_type = str(registry_meta.get("claim_type", "unknown"))
        claim_meta = matrix_claims.get(claim_id)

        reasons: list[str] = []
        evidence_needed: set[str] = set()
        signals: dict[str, Any] = {
            "current_status": current_status,
            "claim_type": claim_type,
        }

        if claim_meta is None:
            if claim_type == "open_question":
                reasons.append("no_evidence_for_open_question")
                evidence_needed.update({"experimental", "literature"})
                signals.update(
                    {
                        "overall_confidence": 0.0,
                        "source_counts": {"experimental": 0, "literature": 0},
                        "conflict_ratio": 0.0,
                    }
                )
            else:
                continue
        else:
            overall_conf = float(claim_meta.get("overall_confidence", 0.0))
            source_counts = claim_meta.get("source_counts", {})
            exp_count = int(source_counts.get("experimental", 0))
            lit_count = int(source_counts.get("literature", 0))
            conflict_ratio = _direction_conflict_ratio(claim_meta.get("direction_counts", {}))

            signals.update(
                {
                    "overall_confidence": round(overall_conf, 3),
                    "source_counts": {
                        "experimental": exp_count,
                        "literature": lit_count,
                    },
                    "conflict_ratio": conflict_ratio,
                }
            )

            if overall_conf < low_conf_threshold:
                reasons.append("low_overall_confidence")
            if exp_count == 0:
                reasons.append("missing_experimental_evidence")
                evidence_needed.add("experimental")
            if lit_count == 0:
                reasons.append("missing_literature_evidence")
                evidence_needed.add("literature")
            if conflict_ratio >= conflict_alert_threshold:
                reasons.append("directional_conflict_alert")
                evidence_needed.update({"experimental", "literature"})
            if current_status == "candidate" and exp_count < candidate_min_exp:
                reasons.append("insufficient_experimental_replication")
                evidence_needed.add("experimental")
            if current_status == "provisional" and lit_count < provisional_min_lit:
                reasons.append("insufficient_literature_grounding")
                evidence_needed.add("literature")

            if claim_id in conflicts_by_claim:
                reasons.append("active_conflict")
                evidence_needed.update({"experimental", "literature"})

        if not reasons:
            continue

        priority = _priority_from_reasons(reasons)
        if not evidence_needed:
            evidence_needed.add("experimental")

        decision_entry = latest_decisions.get(claim_id)
        decision_state = {
            "decision_status": decision_entry.decision_status if decision_entry else "none",
            "timestamp_utc": decision_entry.timestamp_utc if decision_entry else "",
            "recommendation": decision_entry.recommendation if decision_entry else "",
        }

        next_action = "Run targeted experimental probe."
        if evidence_needed == {"literature"}:
            next_action = "Run targeted literature extraction and claim linkage."
        elif evidence_needed == {"experimental", "literature"}:
            next_action = "Run paired experiment + literature cycle before status change."

        backlog_items.append(
            {
                "backlog_id": "",
                "claim_id": claim_id,
                "priority": priority,
                "reasons": sorted(set(reasons)),
                "signals": signals,
                "evidence_needed": sorted(evidence_needed),
                "next_action": next_action,
                "latest_decision": decision_state,
                "status": "open",
            }
        )

    backlog_items.sort(
        key=lambda item: (
            _priority_rank(str(item.get("priority", "low"))),
            str(item.get("claim_id", "")),
        )
    )
    for idx, item in enumerate(backlog_items, start=1):
        item["backlog_id"] = f"EVB-{idx:04d}"

    proposals: list[dict[str, Any]] = []
    proposal_counter = 1
    for item in backlog_items:
        claim_id = str(item["claim_id"])
        reasons = [str(r) for r in item.get("reasons", [])]
        signals = item.get("signals", {})
        conflict_ratio = float(signals.get("conflict_ratio", 0.0))
        needed = set(item.get("evidence_needed", []))

        if "experimental" in needed:
            exp_type = _suggest_experiment_type(claim_id, matrix)
            policy = _conflict_policy_for_claim(conflict_adjudication, claim_id)
            dispatch_req = policy.get("dispatch_requirements", {})
            env_req = _environment_dispatch_requirements(
                environment_qualification=environment_qualification,
                experiment_type=exp_type,
                priority=str(item.get("priority", "low")),
            )
            required_capabilities = _string_list(dispatch_req.get("required_capabilities", []))
            manifest_fields = _merge_unique(
                ["claim_ids_tested", "evidence_class", "evidence_direction"],
                _string_list(dispatch_req.get("manifest_fields", [])),
            )
            manifest_fields = _merge_unique(manifest_fields, env_req.get("required_manifest_fields", []))
            metric_keys = _string_list(dispatch_req.get("metrics_required_keys", []))
            metric_keys = _merge_unique(metric_keys, env_req.get("required_environment_metrics", []))
            summary_requirements = _string_list(dispatch_req.get("summary_must_include", []))
            required_environment_fields = env_req.get("required_environment_fields", [])
            required_environment_tiers = env_req.get("required_environment_tiers", [])
            target_repo = exploratory_repo if conflict_ratio >= 0.7 else default_exp_repo
            routing_reasons: list[str] = []
            if conflict_ratio >= 0.7:
                routing_reasons.append(
                    f"conflict_ratio={_fmt_number(conflict_ratio)} >= 0.7, using exploratory repo"
                )

            default_snapshot = repo_caps.get(default_exp_repo)
            default_capabilities = (
                default_snapshot.get("capabilities", {}) if isinstance(default_snapshot, dict) else {}
            )
            missing_capabilities: list[str] = []
            if required_capabilities:
                if default_snapshot is None and fail_closed:
                    missing_capabilities = list(required_capabilities)
                    routing_reasons.append(
                        f"no capability declaration found for `{default_exp_repo}` (fail_closed=true)"
                    )
                else:
                    for capability in required_capabilities:
                        if not bool(default_capabilities.get(capability, False)):
                            missing_capabilities.append(capability)
                    if missing_capabilities:
                        routing_reasons.append(
                            "missing required capabilities on default repo: "
                            + ", ".join(f"`{cap}`" for cap in missing_capabilities)
                        )
                if missing_capabilities:
                    target_repo = exploratory_repo
                    routing_reasons.append(f"capability gate fallback to `{exploratory_repo}`")

                target_snapshot = repo_caps.get(target_repo)
                if target_snapshot is None:
                    routing_reasons.append(
                        f"no capability declaration found yet for selected target repo `{target_repo}`"
                    )
                else:
                    unresolved_target_caps = [
                        capability
                        for capability in required_capabilities
                        if not bool(target_snapshot.get("capabilities", {}).get(capability, False))
                    ]
                    if unresolved_target_caps:
                        routing_reasons.append(
                            "selected target repo still missing declared capabilities: "
                            + ", ".join(f"`{cap}`" for cap in unresolved_target_caps)
                        )

            capability_gate = {
                "default_repo": default_exp_repo,
                "required_capabilities": required_capabilities,
                "missing_capabilities": missing_capabilities,
                "fail_closed": fail_closed,
                "default_repo_snapshot": default_snapshot or {},
            }

            required_pack_contract: dict[str, Any] = {
                "manifest": manifest_fields,
                "metrics": "stable numeric keys only",
                "summary": "include scenario and interpretation",
            }
            if metric_keys:
                required_pack_contract["required_metric_keys"] = metric_keys
            if summary_requirements:
                required_pack_contract["summary_must_include"] = summary_requirements
            if required_capabilities:
                required_pack_contract["required_capabilities"] = required_capabilities
            if required_environment_fields:
                required_pack_contract["environment_required_fields"] = required_environment_fields
            if required_environment_tiers:
                required_pack_contract["environment_required_tiers"] = required_environment_tiers

            acceptance_checks = [
                "At least 2 additional runs with distinct seeds.",
                "Experiment Pack validates against v1 schema.",
                "Result links to claim_ids_tested and updates matrix direction counts.",
            ]
            if required_environment_fields:
                acceptance_checks.append(
                    "manifest `environment` block includes required fields: "
                    + ", ".join(f"`{field}`" for field in required_environment_fields)
                    + "."
                )
            if required_environment_tiers:
                acceptance_checks.append(
                    "Run set covers required environment tiers: "
                    + ", ".join(f"`{tier}`" for tier in required_environment_tiers)
                    + "."
                )
            if metric_keys:
                acceptance_checks.append(
                    "Required metric keys are present in metrics.json for each run: "
                    + ", ".join(f"`{key}`" for key in metric_keys)
                    + "."
                )
            acceptance_checks = _merge_unique(
                acceptance_checks,
                _string_list(dispatch_req.get("extra_acceptance_checks", [])),
            )

            profile = _experiment_profile(experiments_root, exp_type)
            exp_runs = by_experiment.get(exp_type, [])
            latest_run = exp_runs[-1] if exp_runs else None
            brief = {
                "profile_path": profile["profile_path"].as_posix(),
                "what_it_tests": profile["what_it_tests"],
                "failure_modes": profile["failure_modes"],
                "latest_run": (
                    {
                        "run_id": latest_run.run_id,
                        "timestamp_utc": latest_run.timestamp_raw,
                        "status": latest_run.final_status,
                        "source_repo": latest_run.source_repo_name,
                    }
                    if latest_run
                    else {}
                ),
            }

            proposal_id = f"EXP-{proposal_counter:04d}"
            proposal_counter += 1
            proposals.append(
                {
                    "proposal_id": proposal_id,
                    "backlog_id": item["backlog_id"],
                    "claim_id": claim_id,
                    "proposal_type": "experimental",
                    "priority": item["priority"],
                    "target_repo": target_repo,
                    "objective": f"Reduce uncertainty for {claim_id} via targeted experiment runs.",
                    "suggested_experiment_type": exp_type,
                    "why_now": reasons,
                    "routing_rationale": routing_reasons,
                    "capability_gate": capability_gate,
                    "required_pack_contract": required_pack_contract,
                    "acceptance_checks": acceptance_checks,
                    "experiment_brief": brief,
                    "status": "proposed",
                }
            )

        if "literature" in needed:
            lit_type = _suggest_literature_type(claim_id, matrix)
            proposal_id = f"LIT-{proposal_counter:04d}"
            proposal_counter += 1
            proposals.append(
                {
                    "proposal_id": proposal_id,
                    "backlog_id": item["backlog_id"],
                    "claim_id": claim_id,
                    "proposal_type": "literature_review",
                    "priority": item["priority"],
                    "target_repo": literature_owner,
                    "objective": f"Improve literature grounding and confidence for {claim_id}.",
                    "suggested_literature_type": lit_type,
                    "why_now": reasons,
                    "required_record_contract": {
                        "record": [
                            "claim_ids_tested",
                            "evidence_class",
                            "evidence_direction",
                            "confidence",
                            "confidence_rationale",
                        ],
                        "summary": "include caveats and mapping limits",
                    },
                    "acceptance_checks": [
                        "At least 1 structured literature entry linked to claim_ids_tested.",
                        "Confidence explicitly justified in confidence_rationale.",
                        "Direction is supports/weakens/mixed/unknown and reflected in matrix.",
                    ],
                    "status": "proposed",
                }
            )

    planning_root.mkdir(parents=True, exist_ok=True)

    backlog_doc = {
        "schema_version": "evidence_backlog/v1",
        "generated_at_utc": generated_at,
        "source": {
            "claim_matrix": "evidence/experiments/claim_evidence.v1.json",
            "conflicts": "evidence/experiments/conflicts.md",
            "recommendations": "evidence/experiments/promotion_demotion_recommendations.md",
        },
        "criteria_version": str(planning_criteria.get("schema_version", "planning_criteria/v1")),
        "items": backlog_items,
    }
    proposals_doc = {
        "schema_version": "experiment_proposals/v1",
        "generated_at_utc": generated_at,
        "source_backlog": "evidence/planning/evidence_backlog.v1.json",
        "items": proposals,
    }

    (planning_root / "evidence_backlog.v1.json").write_text(
        json.dumps(backlog_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "experiment_proposals.v1.json").write_text(
        json.dumps(proposals_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    brief_lines: list[str] = []
    brief_lines.append("# Experiment Dispatch Briefs")
    brief_lines.append("")
    brief_lines.append(f"Generated: `{generated_at}`")
    brief_lines.append("")
    brief_lines.append("Human-readable briefs for high-priority experimental proposals, including routing and capability-gate context.")
    brief_lines.append("")

    experimental_proposals = [
        p
        for p in proposals
        if p.get("proposal_type") == "experimental" and p.get("priority") == "high"
    ]
    if not experimental_proposals:
        brief_lines.append("No experimental proposals in current planning output.")
    else:
        for proposal in experimental_proposals:
            proposal_id = str(proposal.get("proposal_id", ""))
            claim_id = str(proposal.get("claim_id", ""))
            target_repo = str(proposal.get("target_repo", ""))
            exp_type = str(proposal.get("suggested_experiment_type", ""))
            brief = proposal.get("experiment_brief", {}) if isinstance(proposal.get("experiment_brief"), dict) else {}
            what_it_tests = brief.get("what_it_tests", []) if isinstance(brief.get("what_it_tests"), list) else []
            failure_modes = brief.get("failure_modes", []) if isinstance(brief.get("failure_modes"), list) else []
            latest_run = brief.get("latest_run", {}) if isinstance(brief.get("latest_run"), dict) else {}
            required_pack = (
                proposal.get("required_pack_contract", {})
                if isinstance(proposal.get("required_pack_contract"), dict)
                else {}
            )

            brief_lines.append(f"## {proposal_id} — {claim_id}")
            brief_lines.append("")
            brief_lines.append(f"- Target repo: `{target_repo}`")
            brief_lines.append(f"- Experiment type: `{exp_type}`")
            brief_lines.append(f"- Objective: {proposal.get('objective', '')}")
            routing_rationale = proposal.get("routing_rationale", [])
            if isinstance(routing_rationale, list) and routing_rationale:
                brief_lines.append("- Routing rationale:")
                for token in routing_rationale:
                    brief_lines.append(f"  - {token}")

            if what_it_tests:
                brief_lines.append("- What it tests:")
                for token in what_it_tests:
                    brief_lines.append(f"  - {token}")
            if failure_modes:
                brief_lines.append("- Failure modes:")
                for token in failure_modes:
                    brief_lines.append(f"  - {token}")

            required_metric_keys = required_pack.get("required_metric_keys", [])
            if isinstance(required_metric_keys, list) and required_metric_keys:
                brief_lines.append("- Required metric keys:")
                for key in required_metric_keys:
                    brief_lines.append(f"  - `{key}`")

            environment_required_fields = required_pack.get("environment_required_fields", [])
            if isinstance(environment_required_fields, list) and environment_required_fields:
                brief_lines.append("- Required environment fields:")
                for field_name in environment_required_fields:
                    brief_lines.append(f"  - `{field_name}`")

            environment_required_tiers = required_pack.get("environment_required_tiers", [])
            if isinstance(environment_required_tiers, list) and environment_required_tiers:
                brief_lines.append("- Required environment tiers across run set:")
                for tier in environment_required_tiers:
                    brief_lines.append(f"  - `{tier}`")

            summary_must_include = required_pack.get("summary_must_include", [])
            if isinstance(summary_must_include, list) and summary_must_include:
                brief_lines.append("- Summary must include:")
                for token in summary_must_include:
                    brief_lines.append(f"  - {token}")

            required_capabilities = required_pack.get("required_capabilities", [])
            if isinstance(required_capabilities, list) and required_capabilities:
                brief_lines.append("- Required producer capabilities:")
                for capability in required_capabilities:
                    brief_lines.append(f"  - `{capability}`")

            if latest_run:
                brief_lines.append(
                    "- Latest observed run context: "
                    + f"`{latest_run.get('run_id', '')}` status=`{latest_run.get('status', '')}` "
                    + f"timestamp=`{latest_run.get('timestamp_utc', '')}` source_repo=`{latest_run.get('source_repo', '')}`"
                )

            profile_path = str(brief.get("profile_path", "")).strip()
            if profile_path:
                brief_lines.append(f"- Experiment profile: `{profile_path}`")

            brief_lines.append("")

    (planning_root / "EXPERIMENT_BRIEFS.md").write_text(
        "\n".join(brief_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    index_lines: list[str] = []
    index_lines.append("# Planning Index")
    index_lines.append("")
    index_lines.append(f"Generated: `{generated_at}`")
    index_lines.append("")
    index_lines.append(
        f"- Evidence backlog: `evidence_backlog.v1.json` ({len(backlog_items)} item(s))"
    )
    index_lines.append(
        f"- Experiment proposals: `experiment_proposals.v1.json` ({len(proposals)} item(s))"
    )
    index_lines.append("- Experiment dispatch briefs: `EXPERIMENT_BRIEFS.md`")
    index_lines.append("- Planning criteria: `planning_criteria.v1.yaml`")
    (planning_root / "INDEX.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    return backlog_items, proposals


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
    repo_root = base_dir.parent.parent
    evidence_root = base_dir.parent
    literature_root = evidence_root / "literature"
    decisions_dir = evidence_root / "decisions"
    decision_log_path = decisions_dir / "decision_log.v1.jsonl"
    planning_root = evidence_root / "planning"

    stop_criteria = _load_json_compatible_yaml(base_dir / "stop_criteria.v1.yaml", "stop criteria")
    decision_criteria = _load_decision_criteria(base_dir / "decision_criteria.v1.yaml")
    conflict_adjudication = _load_conflict_adjudication(base_dir / "conflict_adjudication.v1.yaml")
    environment_qualification = _load_environment_qualification(
        base_dir / "environment_qualification.v1.yaml"
    )
    planning_criteria = _load_planning_criteria(planning_root / "planning_criteria.v1.yaml")
    claim_registry = _load_claim_registry(repo_root / "docs/claims/claims.yaml")
    decision_log_entries = _load_decision_log(decision_log_path)
    latest_decisions = _latest_decision_by_claim(decision_log_entries)

    by_experiment = _scan_runs(base_dir)
    by_literature = _scan_literature(literature_root)

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    todos_by_experiment: dict[str, list[str]] = {}

    for experiment_type, runs in by_experiment.items():
        criteria = _criteria_for_experiment(stop_criteria, experiment_type)
        _evaluate_runs(runs, criteria)
        _evaluate_environment_quality(runs, environment_qualification, experiment_type)

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

    _write_todos(base_dir, todos_by_experiment, generated_at)
    _write_literature_index(literature_root, by_literature, generated_at)
    _write_decision_state(decisions_dir, latest_decisions, generated_at)
    _write_environment_outputs(base_dir, by_experiment, environment_qualification, generated_at)

    matrix = _write_claim_evidence_matrix(base_dir, by_experiment, by_literature, generated_at)
    conflicts = _collect_conflicts(matrix)
    backlog_items, proposals = _write_planning_outputs(
        planning_root,
        by_experiment,
        matrix,
        claim_registry,
        conflicts,
        latest_decisions,
        planning_criteria,
        conflict_adjudication,
        environment_qualification,
        generated_at,
    )
    _write_conflicts_report(base_dir, matrix, conflicts, generated_at, conflict_adjudication)
    _write_promotion_demotion_recommendations(
        base_dir,
        matrix,
        claim_registry,
        decision_criteria,
        latest_decisions,
        generated_at,
    )
    _write_top_level_index(
        base_dir,
        by_experiment,
        by_literature,
        decision_log_count=len(decision_log_entries),
        backlog_count=len(backlog_items),
        proposal_count=len(proposals),
        generated_at=generated_at,
    )

    total_runs = sum(len(runs) for runs in by_experiment.values())
    total_fail = sum(1 for runs in by_experiment.values() for r in runs if r.final_status == "FAIL")
    total_lit = sum(len(entries) for entries in by_literature.values())
    print(
        "Indexed "
        + f"{total_runs} run(s) across {len(by_experiment)} experiment type(s); "
        + f"FAIL={total_fail}; literature entries={total_lit}; "
        + f"backlog items={len(backlog_items)}; proposals={len(proposals)}."
    )


if __name__ == "__main__":
    main()
