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
  evidence/decisions/decision_state.v1.json
  evidence/planning/evidence_backlog.v1.json
  evidence/planning/experiment_proposals.v1.json
  evidence/planning/architecture_gap_register.v1.json
  evidence/planning/ARCHITECTURE_GAP_REGISTER.md
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
from typing import Any, Callable

START_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:START -->"
END_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:END -->"

ADAPTER_SCHEMA_VERSION = "jepa_adapter_signals/v1"
ADAPTER_REQUIRED_PE_FIELDS = {"mean", "p95"}
ADAPTER_REQUIRED_SIGNAL_METRICS = {
    "latent_prediction_error_mean",
    "latent_prediction_error_p95",
    "latent_residual_coverage_rate",
    "precision_input_completeness_rate",
}
ADAPTER_ALLOWED_UNCERTAINTY = {"none", "dispersion", "ensemble", "head"}


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
    architecture_epoch: str = ""
    adapter_signals_path: Path | None = None
    adapter_contract_status: str = "n/a"
    adapter_contract_errors: list[str] = field(default_factory=list)


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
    architecture_epoch: str = ""
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


def _scan_runs(base_dir: Path, planning_criteria: dict[str, Any]) -> dict[str, list[RunRecord]]:
    by_experiment: dict[str, list[RunRecord]] = defaultdict(list)

    applicability = (
        planning_criteria.get("evidence_applicability", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(applicability, dict):
        applicability = {}
    current_epoch = str(applicability.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(applicability.get("epoch_start_utc", "")).strip()
    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

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
        architecture_epoch = str(manifest.get("architecture_epoch", "")).strip()
        if not architecture_epoch and current_epoch and epoch_start and timestamp >= epoch_start:
            architecture_epoch = current_epoch

        artifacts = manifest.get("artifacts", {}) if isinstance(manifest, dict) else {}
        metrics_rel = artifacts.get("metrics_path", "metrics.json")
        summary_rel = artifacts.get("summary_path", "summary.md")
        adapter_signals_rel = artifacts.get("adapter_signals_path")

        metrics_path = run_dir / metrics_rel
        summary_path = run_dir / summary_rel
        adapter_signals_path: Path | None = None
        if isinstance(adapter_signals_rel, str) and adapter_signals_rel.strip():
            adapter_signals_path = run_dir / adapter_signals_rel.strip()

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
                architecture_epoch=architecture_epoch,
                adapter_signals_path=adapter_signals_path,
            )
        )

    for runs in by_experiment.values():
        runs.sort(key=lambda r: (r.timestamp, r.run_id))
    return by_experiment


def _scan_literature(
    literature_root: Path,
    planning_criteria: dict[str, Any],
) -> dict[str, list[LiteratureRecord]]:
    by_literature: dict[str, list[LiteratureRecord]] = defaultdict(list)
    if not literature_root.exists():
        return by_literature

    applicability = (
        planning_criteria.get("evidence_applicability", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(applicability, dict):
        applicability = {}
    current_epoch = str(applicability.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(applicability.get("epoch_start_utc", "")).strip()
    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

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
        architecture_epoch = str(record.get("architecture_epoch", "")).strip()
        if not architecture_epoch and current_epoch and epoch_start and timestamp >= epoch_start:
            architecture_epoch = current_epoch
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
                architecture_epoch=architecture_epoch,
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


def _adapter_signature_for_errors(errors: list[str]) -> str:
    detail = " ".join(errors).lower()
    if "missing file" in detail:
        return "contract:jepa_adapter_signals_missing"
    if "schema_version" in detail:
        return "contract:jepa_adapter_signals_version"
    return "contract:jepa_adapter_signals_invalid"


def _validate_jepa_adapter_signals(run: RunRecord) -> tuple[str, list[str]]:
    if run.adapter_signals_path is None:
        return "n/a", []

    path = run.adapter_signals_path
    if not path.exists():
        return "FAIL", [f"missing file: {path.name}"]

    try:
        doc = _load_json(path)
    except RuntimeError as exc:
        return "FAIL", [str(exc)]

    errors: list[str] = []

    if not isinstance(doc, dict):
        return "FAIL", ["root must be an object"]

    if doc.get("schema_version") != ADAPTER_SCHEMA_VERSION:
        errors.append(f"schema_version must be `{ADAPTER_SCHEMA_VERSION}`")

    run_id = str(doc.get("run_id", "")).strip()
    if run_id != run.run_id:
        errors.append(f"run_id mismatch (`{run_id}` != `{run.run_id}`)")

    experiment_type = str(doc.get("experiment_type", "")).strip()
    if experiment_type != run.experiment_type:
        errors.append(
            f"experiment_type mismatch (`{experiment_type}` != `{run.experiment_type}`)"
        )

    adapter = doc.get("adapter")
    if not isinstance(adapter, dict):
        errors.append("adapter object missing")
    else:
        if not str(adapter.get("name", "")).strip():
            errors.append("adapter.name missing")
        if not str(adapter.get("version", "")).strip():
            errors.append("adapter.version missing")

    stream_presence = doc.get("stream_presence")
    if not isinstance(stream_presence, dict):
        errors.append("stream_presence object missing")
        stream_presence = {}

    for key in ("z_t", "z_hat", "pe_latent", "trace_context_mask_ids"):
        if stream_presence.get(key) is not True:
            errors.append(f"stream_presence.{key} must be true")

    uncertainty_present = bool(stream_presence.get("uncertainty_latent"))
    trace_action_token = stream_presence.get("trace_action_token")
    if not isinstance(trace_action_token, bool):
        errors.append("stream_presence.trace_action_token must be boolean")

    pe_latent_fields = doc.get("pe_latent_fields")
    if not isinstance(pe_latent_fields, list):
        errors.append("pe_latent_fields must be an array")
        pe_latent_fields = []
    pe_fields = {str(x) for x in pe_latent_fields}
    missing_pe = sorted(ADAPTER_REQUIRED_PE_FIELDS - pe_fields)
    if missing_pe:
        errors.append(f"pe_latent_fields missing: {', '.join(missing_pe)}")

    uncertainty_estimator = str(doc.get("uncertainty_estimator", "")).strip()
    if uncertainty_estimator not in ADAPTER_ALLOWED_UNCERTAINTY:
        errors.append(
            "uncertainty_estimator must be one of: "
            + ", ".join(sorted(ADAPTER_ALLOWED_UNCERTAINTY))
        )
    if uncertainty_present and uncertainty_estimator == "none":
        errors.append("uncertainty_latent=true requires uncertainty_estimator != none")

    signal_metrics = doc.get("signal_metrics")
    if not isinstance(signal_metrics, dict):
        errors.append("signal_metrics object missing")
        signal_metrics = {}

    missing_metrics = sorted(ADAPTER_REQUIRED_SIGNAL_METRICS - set(signal_metrics.keys()))
    if missing_metrics:
        errors.append(f"signal_metrics missing: {', '.join(missing_metrics)}")

    for metric in ADAPTER_REQUIRED_SIGNAL_METRICS:
        value = signal_metrics.get(metric)
        if not isinstance(value, (int, float)):
            errors.append(f"signal_metrics.{metric} must be numeric")

    for bounded in ("latent_residual_coverage_rate", "precision_input_completeness_rate"):
        value = signal_metrics.get(bounded)
        if isinstance(value, (int, float)) and not (0.0 <= float(value) <= 1.0):
            errors.append(f"signal_metrics.{bounded} must be in [0,1]")

    if uncertainty_present:
        value = signal_metrics.get("latent_uncertainty_calibration_error")
        if not isinstance(value, (int, float)):
            errors.append(
                "signal_metrics.latent_uncertainty_calibration_error required when uncertainty_latent=true"
            )

    return ("FAIL", errors) if errors else ("PASS", [])


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

        adapter_status, adapter_errors = _validate_jepa_adapter_signals(run)
        run.adapter_contract_status = adapter_status
        run.adapter_contract_errors = adapter_errors
        if adapter_status == "FAIL":
            run.final_status = "FAIL"
            sig = _adapter_signature_for_errors(adapter_errors)
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
            "| run_id | timestamp_utc | status | key metrics | deltas vs previous | stop-criteria hits | adapter contract | summary |"
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
            adapter_status = run.adapter_contract_status
            if adapter_status == "FAIL":
                adapter_status = "**FAIL**"
                if run.adapter_contract_errors:
                    adapter_status += "<br>" + "<br>".join(run.adapter_contract_errors[:2])
            elif adapter_status == "PASS":
                adapter_status = "PASS"
            else:
                adapter_status = "-"
            summary_rel = run.summary_path.relative_to(experiment_dir).as_posix()
            metrics_rel = run.metrics_path.relative_to(experiment_dir).as_posix()
            manifest_rel = run.manifest_path.relative_to(experiment_dir).as_posix()
            adapter_rel = (
                run.adapter_signals_path.relative_to(experiment_dir).as_posix()
                if run.adapter_signals_path
                else None
            )

            summary_link = f"[`summary`]({summary_rel})"
            summary_link += f" / [`manifest`]({manifest_rel}) / [`metrics`]({metrics_rel})"
            if adapter_rel:
                summary_link += f" / [`adapter`]({adapter_rel})"

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
                        adapter_status,
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
    architecture_gap_count: int,
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
    lines.append("- TODO queue: `TODOs.md`")
    lines.append("- Stop criteria config: `stop_criteria.v1.yaml`")
    lines.append("- Decision criteria config: `decision_criteria.v1.yaml`")
    lines.append("- JEPA adapter signal schema: `schemas/v1/jepa_adapter_signals.v1.json`")
    lines.append("- Claim-evidence matrix: `claim_evidence.v1.json`")
    lines.append("- Conflicts report: `conflicts.md`")
    lines.append("- Promotion/demotion recommendations: `promotion_demotion_recommendations.md`")
    lines.append(f"- Literature index: `../literature/INDEX.md` ({sum(len(v) for v in by_literature.values())} entries)")
    lines.append(f"- Persistent decision log: `../decisions/decision_log.v1.jsonl` ({decision_log_count} entries)")
    lines.append("- Decision state snapshot: `../decisions/decision_state.v1.json`")
    lines.append(f"- Evidence backlog: `../planning/evidence_backlog.v1.json` ({backlog_count} item(s))")
    lines.append(f"- Experiment proposals: `../planning/experiment_proposals.v1.json` ({proposal_count} item(s))")
    lines.append(
        f"- Architecture gap register: `../planning/architecture_gap_register.v1.json` ({architecture_gap_count} item(s))"
    )

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
            }
            if run.architecture_epoch:
                entry["architecture_epoch"] = run.architecture_epoch
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
            if lit.architecture_epoch:
                entry["architecture_epoch"] = lit.architecture_epoch
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


def _is_inactive_claim_status(status: str) -> bool:
    return str(status).strip().lower() in {"legacy"}


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


def _default_planning_criteria() -> dict[str, Any]:
    return {
        "schema_version": "planning_criteria/v1",
        "thresholds": {
            "low_overall_confidence": 0.55,
            "conflict_ratio_alert": 0.40,
            "candidate_min_experimental_entries": 2,
            "provisional_min_literature_entries": 2,
            "consider_new_structure_conflict_ratio": 0.70,
            "consider_new_structure_min_failure_signature_repeats": 3,
            "consider_new_structure_min_distinct_signatures": 2,
            "consider_new_structure_min_literature_entries": 2,
            "consider_new_structure_literature_non_support_ratio": 0.50,
            "external_precedence_conflict_ratio": 0.55,
            "external_precedence_min_confidence_delta": 0.05,
            "external_precedence_min_total_entries": 6,
            "external_precedence_min_experimental_entries": 4,
            "external_precedence_min_literature_entries": 4,
            "external_precedence_min_recurring_signatures": 2,
            "proposal_saturation_conflict_ratio": 0.70,
            "proposal_saturation_min_experimental_entries": 16,
            "proposal_saturation_recent_window": 12,
            "proposal_saturation_min_recent_entries": 8,
            "proposal_saturation_max_unique_signature_sets": 2,
            "proposal_saturation_max_directions": 2,
            "escalation_min_conflict_ratio": 0.75,
            "escalation_min_experimental_entries": 24,
            "escalation_min_recurring_signatures": 2,
            "escalation_min_max_signature_count": 8,
        },
        "model_adjudication": {
            "external_precedence_enabled": True,
            "allowed_conflict_outcomes": [
                "retain_ree",
                "hybridize",
                "adopt_jepa_structure",
                "retire_ree_claim",
            ],
            "default_conflict_outcome": "retain_ree",
            "cascade_policy": {
                "enabled": True,
                "trigger_outcomes": ["adopt_jepa_structure", "retire_ree_claim"],
                "dependency_reopen_status": "candidate",
                "require_followup_proposals": True,
            },
            "temporary_override_mode": {
                "enabled": True,
                "mode_id": "jepa_internal_proxy_override",
                "requirements": [
                    "explicit_proxy_provenance",
                    "calibration_metrics_present",
                    "rollback_trigger_documented",
                ],
            },
            "anti_lock_in_gate": {
                "enabled": True,
                "description": (
                    "If matched JEPA evidence repeatedly outperforms REE assumptions, force adjudication "
                    "rather than schema-preserving tuning."
                ),
            },
        },
        "repo_routing": {
            "experimental_default_repo": "ree-v2",
            "exploratory_repo": "ree-experiments-lab",
            "literature_owner": "REE_assembly",
        },
        "evidence_applicability": {
            "enabled": True,
            "current_architecture_epoch": "",
            "epoch_start_utc": "",
            "source_types": ["*"],
            "stale_if_timestamp_before_epoch_start": True,
            "require_epoch_tag_for_new_evidence": False,
        },
    }


def _load_planning_criteria(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_planning_criteria()
    data = _load_json_compatible_yaml(path, "planning criteria")
    defaults = _default_planning_criteria()
    for key, value in defaults.items():
        data.setdefault(key, value)
    thresholds = data.get("thresholds")
    if not isinstance(thresholds, dict):
        data["thresholds"] = dict(defaults["thresholds"])
    else:
        for key, value in defaults["thresholds"].items():
            thresholds.setdefault(key, value)
    routing = data.get("repo_routing")
    if not isinstance(routing, dict):
        data["repo_routing"] = dict(defaults["repo_routing"])
    else:
        for key, value in defaults["repo_routing"].items():
            routing.setdefault(key, value)
    applicability = data.get("evidence_applicability")
    if not isinstance(applicability, dict):
        data["evidence_applicability"] = dict(defaults["evidence_applicability"])
    else:
        for key, value in defaults["evidence_applicability"].items():
            applicability.setdefault(key, value)
    adjudication = data.get("model_adjudication")
    if not isinstance(adjudication, dict):
        data["model_adjudication"] = dict(defaults["model_adjudication"])
    else:
        for key, value in defaults["model_adjudication"].items():
            adjudication.setdefault(key, value)
        cascade_policy = adjudication.get("cascade_policy")
        if not isinstance(cascade_policy, dict):
            adjudication["cascade_policy"] = dict(defaults["model_adjudication"]["cascade_policy"])
        else:
            for key, value in defaults["model_adjudication"]["cascade_policy"].items():
                cascade_policy.setdefault(key, value)
        override_mode = adjudication.get("temporary_override_mode")
        if not isinstance(override_mode, dict):
            adjudication["temporary_override_mode"] = dict(
                defaults["model_adjudication"]["temporary_override_mode"]
            )
        else:
            for key, value in defaults["model_adjudication"]["temporary_override_mode"].items():
                override_mode.setdefault(key, value)
        anti_lock_in = adjudication.get("anti_lock_in_gate")
        if not isinstance(anti_lock_in, dict):
            adjudication["anti_lock_in_gate"] = dict(defaults["model_adjudication"]["anti_lock_in_gate"])
        else:
            for key, value in defaults["model_adjudication"]["anti_lock_in_gate"].items():
                anti_lock_in.setdefault(key, value)
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
        if _is_inactive_claim_status(current_status):
            continue
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


def _build_applicability_filter(
    planning_criteria: dict[str, Any],
) -> tuple[str, Callable[[dict[str, Any]], bool]]:
    cfg = planning_criteria.get("evidence_applicability", {}) if isinstance(planning_criteria, dict) else {}
    if not isinstance(cfg, dict) or not bool(cfg.get("enabled", False)):
        return "all_entries", lambda _entry: True

    epoch = str(cfg.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(cfg.get("epoch_start_utc", "")).strip()
    source_types_raw = cfg.get("source_types", ["experimental"])
    stale_before_cutoff = bool(cfg.get("stale_if_timestamp_before_epoch_start", True))
    require_epoch_tag_for_new = bool(cfg.get("require_epoch_tag_for_new_evidence", False))

    source_types: set[str] = set()
    if isinstance(source_types_raw, list):
        source_types = {str(x).strip().lower() for x in source_types_raw if str(x).strip()}
    elif isinstance(source_types_raw, str):
        value = source_types_raw.strip().lower()
        if value:
            source_types = {value}
    all_sources = "*" in source_types or not source_types

    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

    scope_bits: list[str] = ["current_epoch_applicable"]
    if epoch:
        scope_bits.append(f"epoch={epoch}")

    def _is_applicable(entry: dict[str, Any]) -> bool:
        source_type = str(entry.get("source_type", "")).strip().lower()
        if not all_sources and source_type not in source_types:
            return True

        entry_epoch = str(entry.get("architecture_epoch", "")).strip()
        if entry_epoch:
            if epoch and entry_epoch != epoch:
                return False
            return True

        ts_raw = str(entry.get("timestamp_utc", "")).strip()
        ts: datetime | None = None
        if ts_raw:
            try:
                ts = _parse_timestamp_only(ts_raw)
            except ValueError:
                ts = None

        if epoch_start and stale_before_cutoff and ts and ts < epoch_start:
            return False
        if epoch_start and require_epoch_tag_for_new and ts and ts >= epoch_start:
            return False
        return True

    return ",".join(scope_bits), _is_applicable


def _collect_conflicts(
    matrix: dict[str, Any],
    planning_criteria: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
) -> tuple[list[dict[str, Any]], str]:
    scope_label, is_applicable = _build_applicability_filter(planning_criteria)
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not isinstance(entry, dict):
            continue
        if not is_applicable(entry):
            continue
        entries_by_claim[str(entry.get("claim_id"))].append(entry)

    conflicts: list[dict[str, Any]] = []
    for claim_id in sorted(entries_by_claim.keys()):
        current_status = str(claim_registry.get(claim_id, {}).get("status", "unknown"))
        if _is_inactive_claim_status(current_status):
            continue
        claim_entries = entries_by_claim.get(claim_id, [])
        if not claim_entries:
            continue
        claim_entries.sort(key=lambda e: (str(e.get("timestamp_utc", "")), str(e.get("run_id", ""))))
        direction_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in claim_entries)
        supports = int(direction_counts.get("supports", 0))
        weakens = int(direction_counts.get("weakens", 0))
        mixed = int(direction_counts.get("mixed", 0))

        direction_conflict = supports > 0 and weakens > 0

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
                "conflict_ratio": _direction_conflict_ratio(direction_counts),
                "latest": str(claim_entries[-1].get("run_id", "")),
                "entries_considered": len(claim_entries),
            }
        )
    return conflicts, scope_label


def _write_conflicts_report(
    base_dir: Path,
    matrix: dict[str, Any],
    planning_criteria: dict[str, Any],
    conflicts: list[dict[str, Any]],
    conflict_scope: str,
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Evidence Conflict Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append(f"Conflict scope: `{conflict_scope}`")
    lines.append("")

    _, is_applicable = _build_applicability_filter(planning_criteria)
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if isinstance(entry, dict) and is_applicable(entry):
            entries_by_claim[str(entry.get("claim_id"))].append(entry)

    lines.append("## Conflict Queue")
    lines.append("")
    lines.append("| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |")
    lines.append("|---|---|---|---|---|---|---|")

    if not conflicts:
        lines.append("| _none_ | - | 0 | 0 | 0 | - | 0 |")
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
                        str(item.get("entries_considered", 0)),
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

            lines.append("- Suggested resolution actions:")
            lines.append("  - Run one targeted adjudication experiment with narrower stop criteria.")
            lines.append("  - Add one replication run with seed sweep to reduce variance ambiguity.")
            lines.append("  - If disagreement persists, split claim scope into separable subclaims.")
            lines.append("")

    (base_dir / "conflicts.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def _priority_rank(priority: str) -> int:
    return {"high": 0, "medium": 1, "low": 2}.get(priority, 3)


def _backlog_urgency_rank(item: dict[str, Any]) -> tuple[int, float, int, str]:
    reasons = {str(r) for r in item.get("reasons", [])}
    signals = item.get("signals", {})
    conflict_ratio = float(signals.get("conflict_ratio", 0.0))
    entries_total = int(signals.get("entries_total", 0))
    # Lower rank is more urgent.
    # 0: architecture-pressure conflict triage, 1: active conflicts, 2+: evidence-coverage gaps.
    if "escalate_architecture_decision" in reasons:
        tier = 0
    elif "anti_lock_in_review_required" in reasons or "external_precedence_pressure" in reasons:
        tier = 0
    elif "consider_new_structure" in reasons:
        tier = 1
    elif "active_conflict" in reasons or "directional_conflict_alert" in reasons:
        tier = 2
    elif "missing_experimental_evidence" in reasons:
        tier = 3
    elif "missing_literature_evidence" in reasons:
        tier = 4
    else:
        tier = 5
    return (tier, -conflict_ratio, -entries_total, str(item.get("claim_id", "")))


def _priority_from_reasons(reasons: list[str]) -> str:
    high_markers = {
        "escalate_architecture_decision",
        "directional_conflict_alert",
        "active_conflict",
        "missing_experimental_evidence",
        "consider_new_structure",
        "external_precedence_pressure",
        "anti_lock_in_review_required",
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


def _write_planning_outputs(
    planning_root: Path,
    matrix: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
    conflicts: list[dict[str, Any]],
    latest_decisions: dict[str, DecisionLogEntry],
    planning_criteria: dict[str, Any],
    generated_at: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    thresholds = planning_criteria.get("thresholds", {})
    routing = planning_criteria.get("repo_routing", {})
    adjudication = planning_criteria.get("model_adjudication", {})

    low_conf_threshold = float(thresholds.get("low_overall_confidence", 0.55))
    conflict_alert_threshold = float(thresholds.get("conflict_ratio_alert", 0.40))
    candidate_min_exp = int(thresholds.get("candidate_min_experimental_entries", 2))
    provisional_min_lit = int(thresholds.get("provisional_min_literature_entries", 2))
    consider_conflict_ratio = float(thresholds.get("consider_new_structure_conflict_ratio", 0.70))
    consider_min_sig_repeats = max(
        1, int(thresholds.get("consider_new_structure_min_failure_signature_repeats", 3))
    )
    consider_min_distinct_sigs = max(
        1, int(thresholds.get("consider_new_structure_min_distinct_signatures", 2))
    )
    consider_min_lit_entries = max(
        1, int(thresholds.get("consider_new_structure_min_literature_entries", 2))
    )
    consider_lit_non_support_ratio = float(
        thresholds.get("consider_new_structure_literature_non_support_ratio", 0.50)
    )
    external_precedence_conflict_ratio = float(
        thresholds.get("external_precedence_conflict_ratio", 0.55)
    )
    external_precedence_min_conf_delta = float(
        thresholds.get("external_precedence_min_confidence_delta", 0.05)
    )
    external_precedence_min_total_entries = max(
        1, int(thresholds.get("external_precedence_min_total_entries", 6))
    )
    external_precedence_min_exp_entries = max(
        1, int(thresholds.get("external_precedence_min_experimental_entries", 4))
    )
    external_precedence_min_lit_entries = max(
        1, int(thresholds.get("external_precedence_min_literature_entries", 4))
    )
    external_precedence_min_recurring = max(
        1, int(thresholds.get("external_precedence_min_recurring_signatures", 2))
    )
    saturation_conflict_ratio = float(thresholds.get("proposal_saturation_conflict_ratio", 0.70))
    saturation_min_exp_entries = max(
        1, int(thresholds.get("proposal_saturation_min_experimental_entries", 16))
    )
    saturation_recent_window = max(
        1, int(thresholds.get("proposal_saturation_recent_window", 12))
    )
    saturation_min_recent_entries = max(
        1, int(thresholds.get("proposal_saturation_min_recent_entries", 8))
    )
    saturation_max_signature_sets = max(
        1, int(thresholds.get("proposal_saturation_max_unique_signature_sets", 2))
    )
    saturation_max_directions = max(
        1, int(thresholds.get("proposal_saturation_max_directions", 2))
    )
    escalation_min_conflict_ratio = float(thresholds.get("escalation_min_conflict_ratio", 0.75))
    escalation_min_exp_entries = max(
        1, int(thresholds.get("escalation_min_experimental_entries", 24))
    )
    escalation_min_recurring = max(
        1, int(thresholds.get("escalation_min_recurring_signatures", 2))
    )
    escalation_min_signature_count = max(
        1, int(thresholds.get("escalation_min_max_signature_count", 8))
    )

    default_exp_repo = str(routing.get("experimental_default_repo", "ree-v2"))
    exploratory_repo = str(routing.get("exploratory_repo", "ree-experiments-lab"))
    literature_owner = str(routing.get("literature_owner", "REE_assembly"))

    external_precedence_enabled = bool(adjudication.get("external_precedence_enabled", True))
    allowed_conflict_outcomes_raw = adjudication.get("allowed_conflict_outcomes", [])
    allowed_conflict_outcomes = [
        str(x).strip()
        for x in allowed_conflict_outcomes_raw
        if str(x).strip()
    ]
    if not allowed_conflict_outcomes:
        allowed_conflict_outcomes = [
            "retain_ree",
            "hybridize",
            "adopt_jepa_structure",
            "retire_ree_claim",
        ]
    default_conflict_outcome = str(adjudication.get("default_conflict_outcome", "retain_ree"))
    cascade_policy = adjudication.get("cascade_policy", {})
    cascade_enabled = bool(cascade_policy.get("enabled", True))
    cascade_trigger_outcomes_raw = cascade_policy.get(
        "trigger_outcomes", ["adopt_jepa_structure", "retire_ree_claim"]
    )
    cascade_trigger_outcomes = [
        str(x).strip()
        for x in cascade_trigger_outcomes_raw
        if str(x).strip()
    ]
    dependency_reopen_status = str(cascade_policy.get("dependency_reopen_status", "candidate"))
    cascade_followup_required = bool(cascade_policy.get("require_followup_proposals", True))
    override_mode = adjudication.get("temporary_override_mode", {})
    override_mode_enabled = bool(override_mode.get("enabled", True))
    override_mode_id = str(override_mode.get("mode_id", "jepa_internal_proxy_override"))
    override_requirements_raw = override_mode.get("requirements", [])
    override_requirements = [
        str(x).strip()
        for x in override_requirements_raw
        if str(x).strip()
    ]
    anti_lock_in_gate = adjudication.get("anti_lock_in_gate", {})
    anti_lock_in_enabled = bool(anti_lock_in_gate.get("enabled", True))

    conflicts_by_claim = {str(item.get("claim_id")): item for item in conflicts}
    matrix_claims = matrix.get("claims", {})
    claim_ids = sorted(set(claim_registry.keys()) | set(matrix_claims.keys()))
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        claim_key = str(entry.get("claim_id", "")).strip()
        if claim_key:
            entries_by_claim[claim_key].append(entry)

    backlog_items: list[dict[str, Any]] = []
    architecture_items: list[dict[str, Any]] = []
    for claim_id in claim_ids:
        registry_meta = claim_registry.get(claim_id, {})
        current_status = str(registry_meta.get("status", "unknown"))
        if _is_inactive_claim_status(current_status):
            continue
        claim_type = str(registry_meta.get("claim_type", "unknown"))
        claim_meta = matrix_claims.get(claim_id)
        claim_entries = entries_by_claim.get(claim_id, [])

        reasons: list[str] = []
        evidence_needed: set[str] = set()
        signals: dict[str, Any] = {
            "current_status": current_status,
            "claim_type": claim_type,
        }
        overall_conf = 0.0
        exp_count = 0
        lit_count = 0
        conflict_ratio = 0.0
        entries_total = 0
        experimental_confidence = 0.0
        literature_confidence = 0.0
        confidence_delta_lit_minus_exp = 0.0
        external_precedence_candidate = False
        anti_lock_in_review_required = False
        saturation_guard_engaged = False
        escalate_architecture_decision = False
        saturation_signal_details: dict[str, Any] = {}

        signature_counts: Counter[str] = Counter()
        for entry in claim_entries:
            for sig in entry.get("failure_signatures", []):
                token = str(sig).strip()
                if token:
                    signature_counts[token] += 1
        recurring_signatures = [
            {"signature": sig, "count": count}
            for sig, count in signature_counts.most_common()
            if count >= consider_min_sig_repeats
        ]
        max_recurring_signature_count = (
            int(recurring_signatures[0].get("count", 0)) if recurring_signatures else 0
        )

        exp_entries = [
            entry
            for entry in claim_entries
            if str(entry.get("source_type", "")) == "experimental"
        ]
        exp_entries.sort(key=lambda x: (str(x.get("timestamp_utc", "")), str(x.get("run_id", ""))))
        recent_exp_entries = exp_entries[-saturation_recent_window:]
        if not recent_exp_entries:
            recent_exp_entries = exp_entries
        recent_direction_set = {
            str(entry.get("evidence_direction", "unknown")) for entry in recent_exp_entries
        }
        unique_signature_sets: set[tuple[str, ...]] = set()
        for entry in recent_exp_entries:
            sigs = {
                str(sig).strip() for sig in entry.get("failure_signatures", []) if str(sig).strip()
            }
            if not sigs:
                sigs = {"__none__"}
            unique_signature_sets.add(tuple(sorted(sigs)))

        lit_direction_counts: Counter[str] = Counter()
        for entry in claim_entries:
            if str(entry.get("source_type", "")) != "literature":
                continue
            lit_direction_counts.update([str(entry.get("evidence_direction", "unknown"))])
        lit_total = int(sum(lit_direction_counts.values()))
        lit_non_support = int(
            lit_direction_counts.get("weakens", 0) + lit_direction_counts.get("mixed", 0)
        )
        lit_non_support_ratio = round((lit_non_support / lit_total), 3) if lit_total else 0.0

        decision_entry = latest_decisions.get(claim_id)
        decision_state = {
            "decision_status": decision_entry.decision_status if decision_entry else "none",
            "timestamp_utc": decision_entry.timestamp_utc if decision_entry else "",
            "recommendation": decision_entry.recommendation if decision_entry else "",
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
            entries_total = int(claim_meta.get("entries_total", 0))
            experimental_confidence = float(claim_meta.get("experimental_confidence", 0.0))
            literature_confidence = float(claim_meta.get("literature_confidence", 0.0))
            confidence_delta_lit_minus_exp = literature_confidence - experimental_confidence
            conflict_ratio = _direction_conflict_ratio(claim_meta.get("direction_counts", {}))

            signals.update(
                {
                    "overall_confidence": round(overall_conf, 3),
                    "source_counts": {
                        "experimental": exp_count,
                        "literature": lit_count,
                    },
                    "confidence_split": {
                        "experimental_confidence": round(experimental_confidence, 3),
                        "literature_confidence": round(literature_confidence, 3),
                        "delta_lit_minus_exp": round(confidence_delta_lit_minus_exp, 3),
                    },
                    "entries_total": entries_total,
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
                # Directional conflict requires new experimental discrimination first.
                # Ask for literature only when no literature is present yet.
                evidence_needed.add("experimental")
                if lit_count == 0:
                    evidence_needed.add("literature")
            if current_status == "candidate" and exp_count < candidate_min_exp:
                reasons.append("insufficient_experimental_replication")
                evidence_needed.add("experimental")
            if current_status == "provisional" and lit_count < provisional_min_lit:
                reasons.append("insufficient_literature_grounding")
                evidence_needed.add("literature")

            if claim_id in conflicts_by_claim:
                reasons.append("active_conflict")
                # Conflict claims should always get experimental follow-up.
                # Requiring literature again when it already exists causes an infinite
                # re-proposal loop and task churn.
                evidence_needed.add("experimental")
                if lit_count == 0:
                    evidence_needed.add("literature")

        structure_signals: list[str] = []
        if conflict_ratio >= consider_conflict_ratio:
            structure_signals.append("high_conflict_ratio")
        if len(recurring_signatures) >= consider_min_distinct_sigs:
            structure_signals.append("recurring_failure_signatures")
        if (
            lit_total >= consider_min_lit_entries
            and lit_non_support_ratio >= consider_lit_non_support_ratio
        ):
            structure_signals.append("literature_non_support_pressure")

        if (
            external_precedence_enabled
            and conflict_ratio >= external_precedence_conflict_ratio
            and entries_total >= external_precedence_min_total_entries
            and lit_count >= external_precedence_min_lit_entries
            and exp_count >= external_precedence_min_exp_entries
            and len(recurring_signatures) >= external_precedence_min_recurring
            and confidence_delta_lit_minus_exp >= external_precedence_min_conf_delta
        ):
            structure_signals.append("external_precedence_pressure")
            external_precedence_candidate = True
            reasons.append("external_precedence_pressure")
            evidence_needed.add("experimental")
            if lit_count == 0:
                evidence_needed.add("literature")

            if anti_lock_in_enabled and current_status in {"candidate", "provisional", "active", "stable"}:
                anti_lock_in_review_required = True
                reasons.append("anti_lock_in_review_required")

        consider_new_structure = len(structure_signals) >= 3
        if consider_new_structure:
            reasons.append("consider_new_structure")
            evidence_needed.add("experimental")
            if lit_count == 0:
                evidence_needed.add("literature")

        if (
            conflict_ratio >= saturation_conflict_ratio
            and exp_count >= saturation_min_exp_entries
            and len(recurring_signatures) >= consider_min_distinct_sigs
            and len(recent_exp_entries) >= saturation_min_recent_entries
            and len(unique_signature_sets) <= saturation_max_signature_sets
            and len(recent_direction_set) <= saturation_max_directions
        ):
            saturation_guard_engaged = True
            saturation_signal_details = {
                "recent_window_used": len(recent_exp_entries),
                "unique_signature_sets": len(unique_signature_sets),
                "unique_directions": len(recent_direction_set),
            }
            signals["proposal_saturation"] = dict(saturation_signal_details)
            reasons.append("saturation_guard_hold")

        if (
            consider_new_structure
            and conflict_ratio >= escalation_min_conflict_ratio
            and exp_count >= escalation_min_exp_entries
            and len(recurring_signatures) >= escalation_min_recurring
            and max_recurring_signature_count >= escalation_min_signature_count
        ):
            escalate_architecture_decision = True
            signals["escalation_required"] = True
            reasons.append("escalate_architecture_decision")

        # Saturation guard prevents infinite re-dispatch loops for stale experimental probes.
        if saturation_guard_engaged and "experimental" in evidence_needed:
            evidence_needed.discard("experimental")
        # Escalation guard routes repeated-failure claims to architecture decisions before more routine reruns.
        if escalate_architecture_decision and "experimental" in evidence_needed:
            evidence_needed.discard("experimental")

        if claim_meta is not None and (structure_signals or recurring_signatures):
            architecture_items.append(
                {
                    "gap_id": "",
                    "claim_id": claim_id,
                    "claim_type": claim_type,
                    "current_status": current_status,
                    "overall_confidence": round(overall_conf, 3),
                    "conflict_ratio": round(conflict_ratio, 3),
                    "source_counts": {
                        "experimental": exp_count,
                        "literature": lit_count,
                    },
                    "literature_direction_counts": {
                        "supports": int(lit_direction_counts.get("supports", 0)),
                        "weakens": int(lit_direction_counts.get("weakens", 0)),
                        "mixed": int(lit_direction_counts.get("mixed", 0)),
                        "unknown": int(lit_direction_counts.get("unknown", 0)),
                    },
                    "literature_non_support_ratio": lit_non_support_ratio,
                    "confidence_split": {
                        "experimental_confidence": round(experimental_confidence, 3),
                        "literature_confidence": round(literature_confidence, 3),
                        "delta_lit_minus_exp": round(confidence_delta_lit_minus_exp, 3),
                    },
                    "external_precedence_candidate": external_precedence_candidate,
                    "anti_lock_in_review_required": anti_lock_in_review_required,
                    "saturation_guard_engaged": saturation_guard_engaged,
                    "escalate_architecture_decision": escalate_architecture_decision,
                    "saturation_signal_details": saturation_signal_details,
                    "recurring_failure_signatures": recurring_signatures[:5],
                    "trigger_signals": sorted(set(structure_signals)),
                    "consider_new_structure": consider_new_structure,
                    "recommendation": (
                        "escalate_architecture_decision"
                        if escalate_architecture_decision
                        else "consider_new_structure"
                        if consider_new_structure
                        else "monitor_and_collect_targeted_evidence"
                    ),
                    "adjudication_policy": {
                        "default_conflict_outcome": default_conflict_outcome,
                        "allowed_conflict_outcomes": allowed_conflict_outcomes,
                        "cascade_policy": {
                            "enabled": cascade_enabled,
                            "trigger_outcomes": cascade_trigger_outcomes,
                            "dependency_reopen_status": dependency_reopen_status,
                            "require_followup_proposals": cascade_followup_required,
                        },
                        "temporary_override_mode": {
                            "enabled": override_mode_enabled,
                            "mode_id": override_mode_id,
                            "requirements": override_requirements,
                        },
                        "anti_lock_in_gate_enabled": anti_lock_in_enabled,
                    },
                    "latest_decision": decision_state,
                }
            )

        if not reasons:
            continue

        priority = _priority_from_reasons(reasons)
        if not evidence_needed and not (
            saturation_guard_engaged or escalate_architecture_decision
        ):
            evidence_needed.add("experimental")

        next_action = "Run targeted experimental probe."
        if evidence_needed == {"literature"}:
            next_action = "Run targeted literature extraction and claim linkage."
        elif evidence_needed == {"experimental", "literature"}:
            next_action = "Run paired experiment + literature cycle before status change."
        if "consider_new_structure" in reasons:
            next_action = (
                "Draft architecture options for this claim, then run one adjudication experiment "
                "and one targeted literature extraction."
            )
        if "external_precedence_pressure" in reasons:
            next_action = (
                "Run matched-protocol adjudication and choose conflict outcome: "
                "retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim."
            )
        if "anti_lock_in_review_required" in reasons:
            next_action = (
                "Run anti-lock-in review and forbid schema-preserving tuning without selecting a "
                "recorded conflict outcome."
            )
        if "saturation_guard_hold" in reasons:
            next_action = (
                "Pause repetitive low-information reruns and require either a materially different "
                "protocol variation or an architecture decision before new experimental dispatch."
            )
        if "escalate_architecture_decision" in reasons:
            next_action = (
                "Escalate to architecture decision queue now (retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim) "
                "and hold additional routine reruns until the decision is recorded."
            )

        backlog_items.append(
            {
                "backlog_id": "",
                "claim_id": claim_id,
                "priority": priority,
                "reasons": sorted(set(reasons)),
                "signals": signals,
                "evidence_needed": sorted(evidence_needed),
                "recommendation": (
                    "escalate_architecture_decision"
                    if escalate_architecture_decision
                    else "consider_new_structure"
                    if consider_new_structure
                    else "collect_targeted_evidence"
                ),
                "next_action": next_action,
                "adjudication_context": {
                    "default_conflict_outcome": default_conflict_outcome,
                    "allowed_conflict_outcomes": allowed_conflict_outcomes,
                    "external_precedence_candidate": external_precedence_candidate,
                    "anti_lock_in_review_required": anti_lock_in_review_required,
                    "saturation_guard_engaged": saturation_guard_engaged,
                    "escalate_architecture_decision": escalate_architecture_decision,
                    "saturation_signal_details": saturation_signal_details,
                    "cascade_policy": {
                        "enabled": cascade_enabled,
                        "trigger_outcomes": cascade_trigger_outcomes,
                        "dependency_reopen_status": dependency_reopen_status,
                        "require_followup_proposals": cascade_followup_required,
                    },
                    "temporary_override_mode": {
                        "enabled": override_mode_enabled,
                        "mode_id": override_mode_id,
                        "requirements": override_requirements,
                    },
                },
                "latest_decision": decision_state,
                "status": "open",
            }
        )

    backlog_items.sort(
        key=lambda item: (
            _priority_rank(str(item.get("priority", "low"))),
            _backlog_urgency_rank(item),
        )
    )
    for idx, item in enumerate(backlog_items, start=1):
        item["backlog_id"] = f"EVB-{idx:04d}"

    architecture_items.sort(
        key=lambda item: (
            0 if bool(item.get("consider_new_structure", False)) else 1,
            -float(item.get("conflict_ratio", 0.0)),
            str(item.get("claim_id", "")),
        )
    )
    for idx, item in enumerate(architecture_items, start=1):
        item["gap_id"] = f"AGR-{idx:04d}"

    proposals: list[dict[str, Any]] = []
    proposal_counter = 1
    for item in backlog_items:
        claim_id = str(item["claim_id"])
        reasons = [str(r) for r in item.get("reasons", [])]
        signals = item.get("signals", {})
        conflict_ratio = float(signals.get("conflict_ratio", 0.0))
        needed = set(item.get("evidence_needed", []))

        if "experimental" in needed:
            target_repo = exploratory_repo if conflict_ratio >= 0.7 else default_exp_repo
            exp_type = _suggest_experiment_type(claim_id, matrix)
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
                    "required_pack_contract": {
                        "manifest": ["claim_ids_tested", "evidence_class", "evidence_direction"],
                        "metrics": "stable numeric keys only",
                        "summary": "include scenario and interpretation",
                    },
                    "acceptance_checks": [
                        "At least 2 additional runs with distinct seeds.",
                        "Experiment Pack validates against v1 schema.",
                        "Result links to claim_ids_tested and updates matrix direction counts.",
                    ],
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
    architecture_gap_doc = {
        "schema_version": "architecture_gap_register/v1",
        "generated_at_utc": generated_at,
        "criteria_version": str(planning_criteria.get("schema_version", "planning_criteria/v1")),
        "source": {
            "claim_matrix": "evidence/experiments/claim_evidence.v1.json",
            "conflicts": "evidence/experiments/conflicts.md",
            "backlog": "evidence/planning/evidence_backlog.v1.json",
        },
        "thresholds": {
            "consider_new_structure_conflict_ratio": consider_conflict_ratio,
            "consider_new_structure_min_failure_signature_repeats": consider_min_sig_repeats,
            "consider_new_structure_min_distinct_signatures": consider_min_distinct_sigs,
            "consider_new_structure_min_literature_entries": consider_min_lit_entries,
            "consider_new_structure_literature_non_support_ratio": consider_lit_non_support_ratio,
            "external_precedence_conflict_ratio": external_precedence_conflict_ratio,
            "external_precedence_min_confidence_delta": external_precedence_min_conf_delta,
            "external_precedence_min_total_entries": external_precedence_min_total_entries,
            "external_precedence_min_experimental_entries": external_precedence_min_exp_entries,
            "external_precedence_min_literature_entries": external_precedence_min_lit_entries,
            "external_precedence_min_recurring_signatures": external_precedence_min_recurring,
            "proposal_saturation_conflict_ratio": saturation_conflict_ratio,
            "proposal_saturation_min_experimental_entries": saturation_min_exp_entries,
            "proposal_saturation_recent_window": saturation_recent_window,
            "proposal_saturation_min_recent_entries": saturation_min_recent_entries,
            "proposal_saturation_max_unique_signature_sets": saturation_max_signature_sets,
            "proposal_saturation_max_directions": saturation_max_directions,
            "escalation_min_conflict_ratio": escalation_min_conflict_ratio,
            "escalation_min_experimental_entries": escalation_min_exp_entries,
            "escalation_min_recurring_signatures": escalation_min_recurring,
            "escalation_min_max_signature_count": escalation_min_signature_count,
        },
        "model_adjudication": {
            "external_precedence_enabled": external_precedence_enabled,
            "allowed_conflict_outcomes": allowed_conflict_outcomes,
            "default_conflict_outcome": default_conflict_outcome,
            "cascade_policy": {
                "enabled": cascade_enabled,
                "trigger_outcomes": cascade_trigger_outcomes,
                "dependency_reopen_status": dependency_reopen_status,
                "require_followup_proposals": cascade_followup_required,
            },
            "temporary_override_mode": {
                "enabled": override_mode_enabled,
                "mode_id": override_mode_id,
                "requirements": override_requirements,
            },
            "anti_lock_in_gate_enabled": anti_lock_in_enabled,
        },
        "items": architecture_items,
    }

    (planning_root / "evidence_backlog.v1.json").write_text(
        json.dumps(backlog_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "experiment_proposals.v1.json").write_text(
        json.dumps(proposals_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "architecture_gap_register.v1.json").write_text(
        json.dumps(architecture_gap_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    arch_lines: list[str] = []
    arch_lines.append("# Architecture Gap Register")
    arch_lines.append("")
    arch_lines.append(f"Generated: `{generated_at}`")
    arch_lines.append("")
    arch_lines.append(
        "This register highlights claims under structural pressure and flags where the evidence pattern "
        "suggests a **consider new structure** decision."
    )
    arch_lines.append("")
    arch_lines.append(
        "| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |"
    )
    arch_lines.append("|---|---|---|---|---|---|---|---|---|---|")
    if not architecture_items:
        arch_lines.append("| _none_ | - | - | - | - | - | - | - | - | - |")
    else:
        for item in architecture_items:
            confidence_split = item.get("confidence_split", {})
            arch_lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item['gap_id']}`",
                        f"`{item['claim_id']}`",
                        f"`{item['current_status']}`",
                        _fmt_number(float(item.get("conflict_ratio", 0.0))),
                        _fmt_number(float(item.get("literature_non_support_ratio", 0.0))),
                        _fmt_number(float(confidence_split.get("delta_lit_minus_exp", 0.0))),
                        str(len(item.get("recurring_failure_signatures", []))),
                        "yes" if bool(item.get("consider_new_structure", False)) else "no",
                        "yes" if bool(item.get("external_precedence_candidate", False)) else "no",
                        f"`{item['recommendation']}`",
                    ]
                )
                + " |"
            )

    consider_items = [item for item in architecture_items if item.get("consider_new_structure")]
    arch_lines.append("")
    arch_lines.append("## Consider New Structure Queue")
    arch_lines.append("")
    if not consider_items:
        arch_lines.append("No claims currently trigger a consider-new-structure recommendation.")
    else:
        for item in consider_items:
            trigger_signals = ", ".join(item.get("trigger_signals", []))
            arch_lines.append(
                f"- `{item['claim_id']}` triggers={trigger_signals}; "
                + f"conflict_ratio={_fmt_number(float(item.get('conflict_ratio', 0.0)))}; "
                + f"lit_non_support_ratio={_fmt_number(float(item.get('literature_non_support_ratio', 0.0)))}."
            )
            rec_sigs = item.get("recurring_failure_signatures", [])
            if rec_sigs:
                formatted = ", ".join(
                    f"`{sig.get('signature', '')}`({int(sig.get('count', 0))})"
                    for sig in rec_sigs
                )
                arch_lines.append(f"  - recurring_signatures: {formatted}")
            if bool(item.get("external_precedence_candidate", False)):
                confidence_split = item.get("confidence_split", {})
                arch_lines.append(
                    "  - external_precedence_candidate: yes; "
                    + f"delta_lit_minus_exp={_fmt_number(float(confidence_split.get('delta_lit_minus_exp', 0.0)))}"
                )
            if bool(item.get("saturation_guard_engaged", False)):
                sat = item.get("saturation_signal_details", {})
                arch_lines.append(
                    "  - saturation_guard: engaged; "
                    + f"recent_window_used={_fmt_number(float(sat.get('recent_window_used', 0)))}, "
                    + f"unique_signature_sets={_fmt_number(float(sat.get('unique_signature_sets', 0)))}, "
                    + f"unique_directions={_fmt_number(float(sat.get('unique_directions', 0)))}"
                )
            if bool(item.get("escalate_architecture_decision", False)):
                arch_lines.append(
                    "  - escalation_required: yes; route directly to architecture decision checkpoint."
                )

    (planning_root / "ARCHITECTURE_GAP_REGISTER.md").write_text(
        "\n".join(arch_lines).rstrip() + "\n",
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
    index_lines.append(
        "- Architecture gap register: "
        + f"`architecture_gap_register.v1.json` ({len(architecture_items)} item(s), "
        + f"consider_new_structure={len(consider_items)})"
    )
    index_lines.append("- Planning criteria: `planning_criteria.v1.yaml`")
    (planning_root / "INDEX.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    return backlog_items, proposals, architecture_items


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
    planning_criteria = _load_planning_criteria(planning_root / "planning_criteria.v1.yaml")
    claim_registry = _load_claim_registry(repo_root / "docs/claims/claims.yaml")
    decision_log_entries = _load_decision_log(decision_log_path)
    latest_decisions = _latest_decision_by_claim(decision_log_entries)

    by_experiment = _scan_runs(base_dir, planning_criteria)
    by_literature = _scan_literature(literature_root, planning_criteria)

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

    _write_todos(base_dir, todos_by_experiment, generated_at)
    _write_literature_index(literature_root, by_literature, generated_at)
    _write_decision_state(decisions_dir, latest_decisions, generated_at)

    matrix = _write_claim_evidence_matrix(base_dir, by_experiment, by_literature, generated_at)
    conflicts, conflict_scope = _collect_conflicts(matrix, planning_criteria, claim_registry)
    backlog_items, proposals, architecture_items = _write_planning_outputs(
        planning_root,
        matrix,
        claim_registry,
        conflicts,
        latest_decisions,
        planning_criteria,
        generated_at,
    )
    _write_conflicts_report(base_dir, matrix, planning_criteria, conflicts, conflict_scope, generated_at)
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
        architecture_gap_count=len(architecture_items),
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
