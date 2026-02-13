#!/usr/bin/env python3
"""Backfill legacy experiment packs with environment and capability metadata.

This script updates manifest files under:
  evidence/experiments/**/runs/**/manifest.json

It can run in dry-run mode (default) or apply mode.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_ENV_FIELDS = (
    "env_id",
    "env_version",
    "dynamics_hash",
    "reward_hash",
    "observation_hash",
    "config_hash",
    "tier",
)

KNOWN_CAPABILITIES = (
    "trajectory_integrity_channelized_bias",
    "mech056_dispatch_metric_set",
    "mech056_summary_escalation_trace",
)

MECH056_REQUIRED_METRICS = {
    "trajectory_commit_channel_usage_count",
    "perceptual_sampling_channel_usage_count",
    "structural_consolidation_channel_usage_count",
    "precommit_semantic_overwrite_events",
    "structural_bias_magnitude",
    "structural_bias_rate",
}

MECH056_CHANNEL_METRICS = {
    "trajectory_commit_channel_usage_count",
    "perceptual_sampling_channel_usage_count",
    "structural_consolidation_channel_usage_count",
}


@dataclass
class RunBackfillRecord:
    manifest_path: Path
    run_id: str
    experiment_type: str
    changed_fields: list[str] = field(default_factory=list)
    ambiguities: list[str] = field(default_factory=list)
    environment: dict[str, str] = field(default_factory=dict)
    producer_capabilities: dict[str, bool] = field(default_factory=dict)


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(raw, dict):
        raise RuntimeError(f"Manifest root must be an object: {path}")
    return raw


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _slug(value: str) -> str:
    token = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return token or "unknown"


def _stable_hash(label: str, basis: str, length: int = 12) -> str:
    digest = hashlib.sha256(f"{label}|{basis}".encode("utf-8")).hexdigest()
    return digest[:length]


def _scan_manifest_paths(experiments_root: Path) -> list[Path]:
    manifest_paths: list[Path] = []
    for path in sorted(experiments_root.glob("**/runs/**/manifest.json")):
        if path.parent.parent.name == "runs":
            manifest_paths.append(path)
    return manifest_paths


def _infer_tier(experiment_type: str, run_id: str, scenario_name: str) -> tuple[str, str | None]:
    text = " ".join([experiment_type, run_id, scenario_name]).lower()

    stress_tokens = ("stress", "adversarial", "perturb", "ablation", "worstcase", "worst-case")
    toy_tokens = ("toy", "dummy", "smoke", "probe", "minimal")

    if any(token in text for token in stress_tokens):
        return "stress", None
    if any(token in text for token in toy_tokens) or experiment_type.startswith("claim_probe"):
        return "toy", None
    return "legacy", "tier inferred as `legacy` because no toy/stress indicators were found"


def _infer_environment(manifest: dict[str, Any], manifest_path: Path) -> tuple[dict[str, str], list[str]]:
    ambiguities: list[str] = []

    experiment_type = str(manifest.get("experiment_type", manifest_path.parent.parent.parent.name)).strip()
    run_id = str(manifest.get("run_id", manifest_path.parent.name)).strip()

    scenario = manifest.get("scenario", {})
    scenario_name = ""
    scenario_seed = ""
    scenario_config_hash = ""
    if isinstance(scenario, dict):
        scenario_name = str(scenario.get("name", "")).strip()
        scenario_seed = str(scenario.get("seed", "")).strip()
        scenario_config_hash = str(scenario.get("config_hash", "")).strip()

    source_repo = manifest.get("source_repo", {})
    repo_name = ""
    repo_commit = ""
    repo_branch = ""
    if isinstance(source_repo, dict):
        repo_name = str(source_repo.get("name", "")).strip()
        repo_commit = str(source_repo.get("commit", "")).strip()
        repo_branch = str(source_repo.get("branch", "")).strip()

    basis = "|".join(
        [
            f"experiment_type={experiment_type or 'unknown_experiment'}",
            f"run_id={run_id or manifest_path.parent.name}",
            f"scenario_name={scenario_name or 'unknown_scenario'}",
            f"scenario_seed={scenario_seed or 'unknown_seed'}",
            f"repo_name={repo_name or 'unknown_repo'}",
            f"repo_commit={repo_commit or 'unknown_commit'}",
            f"repo_branch={repo_branch or 'unknown_branch'}",
        ]
    )

    env_id = f"legacy-{_slug(experiment_type or 'unknown_experiment')}"
    if scenario_name:
        env_id += f"-{_slug(scenario_name)}"

    if repo_commit:
        env_version = f"legacy-{repo_commit[:12]}"
    else:
        env_version = "legacy-unknown"
        ambiguities.append("source_repo.commit missing; env_version set to `legacy-unknown`")

    if scenario_config_hash:
        config_hash = scenario_config_hash
    else:
        config_hash = f"legacy-{_stable_hash('config', basis)}"
        ambiguities.append("scenario.config_hash missing; config_hash derived from deterministic placeholder")

    tier, tier_note = _infer_tier(experiment_type, run_id, scenario_name)
    if tier_note:
        ambiguities.append(tier_note)

    environment = {
        "env_id": env_id,
        "env_version": env_version,
        "dynamics_hash": f"legacy-{_stable_hash('dynamics', basis)}",
        "reward_hash": f"legacy-{_stable_hash('reward', basis)}",
        "observation_hash": f"legacy-{_stable_hash('observation', basis)}",
        "config_hash": config_hash,
        "tier": tier,
    }

    return environment, ambiguities


def _read_metric_keys(manifest: dict[str, Any], run_dir: Path) -> tuple[set[str], list[str]]:
    ambiguities: list[str] = []
    artifacts = manifest.get("artifacts", {})
    metrics_rel = "metrics.json"
    if isinstance(artifacts, dict):
        candidate = artifacts.get("metrics_path")
        if isinstance(candidate, str) and candidate.strip():
            metrics_rel = candidate.strip()

    metrics_path = run_dir / metrics_rel
    if not metrics_path.exists():
        ambiguities.append(f"metrics file missing: {metrics_rel}")
        return set(), ambiguities

    try:
        payload = json.loads(metrics_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        ambiguities.append(f"metrics file invalid JSON: {metrics_rel}")
        return set(), ambiguities

    values = payload.get("values", {}) if isinstance(payload, dict) else {}
    if not isinstance(values, dict):
        ambiguities.append(f"metrics.values missing object shape: {metrics_rel}")
        return set(), ambiguities

    return {str(key).strip() for key in values.keys() if str(key).strip()}, ambiguities


def _read_summary_text(manifest: dict[str, Any], run_dir: Path) -> tuple[str, list[str]]:
    ambiguities: list[str] = []
    artifacts = manifest.get("artifacts", {})
    summary_rel = "summary.md"
    if isinstance(artifacts, dict):
        candidate = artifacts.get("summary_path")
        if isinstance(candidate, str) and candidate.strip():
            summary_rel = candidate.strip()

    summary_path = run_dir / summary_rel
    if not summary_path.exists():
        ambiguities.append(f"summary file missing: {summary_rel}")
        return "", ambiguities

    return summary_path.read_text(encoding="utf-8").lower(), ambiguities


def _infer_capabilities(manifest: dict[str, Any], manifest_path: Path) -> tuple[dict[str, bool], list[str]]:
    run_dir = manifest_path.parent
    metric_keys, metric_notes = _read_metric_keys(manifest, run_dir)
    summary_text, summary_notes = _read_summary_text(manifest, run_dir)

    capabilities = {capability: False for capability in KNOWN_CAPABILITIES}
    ambiguities: list[str] = []
    ambiguities.extend(metric_notes)
    ambiguities.extend(summary_notes)

    claims_raw = manifest.get("claim_ids_tested", [])
    claims = {
        str(claim).strip()
        for claim in claims_raw
        if str(claim).strip()
    } if isinstance(claims_raw, list) else set()

    if MECH056_CHANNEL_METRICS.issubset(metric_keys):
        capabilities["trajectory_integrity_channelized_bias"] = True

    if MECH056_REQUIRED_METRICS.issubset(metric_keys):
        capabilities["mech056_dispatch_metric_set"] = True

    if all(token in summary_text for token in ("trajectory_commit", "perceptual_sampling", "structural_consolidation")):
        capabilities["mech056_summary_escalation_trace"] = True

    if "MECH-056" in claims:
        missing = sorted(MECH056_REQUIRED_METRICS - metric_keys)
        if missing:
            ambiguities.append(
                "MECH-056 run missing some dispatch metrics; leaving related capability flags false: "
                + ", ".join(f"`{metric}`" for metric in missing)
            )
        if not capabilities["mech056_summary_escalation_trace"]:
            ambiguities.append(
                "MECH-056 summary lacks explicit channel escalation tokens; `mech056_summary_escalation_trace` set false"
            )

    return capabilities, ambiguities


def _unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def _backfill_manifest(manifest: dict[str, Any], manifest_path: Path) -> RunBackfillRecord | None:
    run_id = str(manifest.get("run_id", manifest_path.parent.name)).strip()
    experiment_type = str(
        manifest.get("experiment_type", manifest_path.parent.parent.parent.name)
    ).strip()
    record = RunBackfillRecord(
        manifest_path=manifest_path,
        run_id=run_id,
        experiment_type=experiment_type,
    )

    inferred_environment, env_notes = _infer_environment(manifest, manifest_path)

    existing_environment = manifest.get("environment")
    if not isinstance(existing_environment, dict):
        manifest["environment"] = inferred_environment
        record.changed_fields.append("environment")
        record.environment = inferred_environment
    else:
        changed_subfields: list[str] = []
        for field_name in REQUIRED_ENV_FIELDS:
            if not str(existing_environment.get(field_name, "")).strip():
                existing_environment[field_name] = inferred_environment[field_name]
                changed_subfields.append(field_name)
        if changed_subfields:
            manifest["environment"] = existing_environment
            record.changed_fields.extend(
                [f"environment.{field_name}" for field_name in changed_subfields]
            )
            record.environment = {
                field_name: str(existing_environment.get(field_name, ""))
                for field_name in REQUIRED_ENV_FIELDS
            }

    producer_capabilities = manifest.get("producer_capabilities")
    if not isinstance(producer_capabilities, dict):
        inferred_caps, cap_notes = _infer_capabilities(manifest, manifest_path)
        manifest["producer_capabilities"] = inferred_caps
        record.changed_fields.append("producer_capabilities")
        record.producer_capabilities = inferred_caps
        record.ambiguities.extend(cap_notes)

    record.ambiguities.extend(env_notes)
    record.ambiguities = _unique_preserve_order(record.ambiguities)

    if not record.changed_fields:
        return None
    return record


def _write_report(
    report_path: Path,
    generated_at: str,
    dry_run: bool,
    scanned_count: int,
    changed_count: int,
    applied_count: int,
    records: list[RunBackfillRecord],
) -> None:
    lines: list[str] = []
    mode = "dry-run" if dry_run else "apply"

    lines.append("# Experiment Pack Backfill Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append(f"Mode: `{mode}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Manifest files scanned: {scanned_count}")
    lines.append(f"- Manifest files requiring backfill: {changed_count}")
    lines.append(f"- Manifest files written: {applied_count}")
    lines.append("")

    lines.append("## Per-Run Changes")
    lines.append("")

    if not records:
        lines.append("No run manifests required backfill changes.")
    else:
        for record in records:
            rel_path = record.manifest_path.as_posix()
            lines.append(f"### `{record.run_id}`")
            lines.append("")
            lines.append(f"- Manifest: `{rel_path}`")
            lines.append(f"- Experiment type: `{record.experiment_type}`")
            lines.append(
                "- Changed fields: " + ", ".join(f"`{field}`" for field in record.changed_fields)
            )
            if record.environment:
                lines.append("- Environment values:")
                for field_name in REQUIRED_ENV_FIELDS:
                    lines.append(
                        f"  - `{field_name}` = `{record.environment.get(field_name, '')}`"
                    )
            if record.producer_capabilities:
                lines.append("- Producer capabilities:")
                for key in KNOWN_CAPABILITIES:
                    value = bool(record.producer_capabilities.get(key, False))
                    lines.append(f"  - `{key}` = `{str(value).lower()}`")
            if record.ambiguities:
                lines.append("- Unresolved ambiguities:")
                for note in record.ambiguities:
                    lines.append(f"  - {note}")
            else:
                lines.append("- Unresolved ambiguities: none")
            lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Backfill legacy experiment pack manifests with environment/capability metadata."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes only (default mode).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write inferred changes back to manifest files.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Optional output path for BACKFILL_REPORT.md.",
    )
    args = parser.parse_args()

    dry_run = not args.apply or args.dry_run

    repo_root = args.repo_root.resolve()
    experiments_root = repo_root / "evidence/experiments"
    report_path = (
        args.report.resolve()
        if args.report
        else experiments_root / "BACKFILL_REPORT.md"
    )

    manifest_paths = _scan_manifest_paths(experiments_root)

    changed_records: list[RunBackfillRecord] = []
    applied_count = 0

    for manifest_path in manifest_paths:
        manifest = _load_json(manifest_path)
        record = _backfill_manifest(manifest, manifest_path)
        if record is None:
            continue

        changed_records.append(record)
        if not dry_run:
            _write_json(manifest_path, manifest)
            applied_count += 1

    generated_at = _now_utc()
    _write_report(
        report_path=report_path,
        generated_at=generated_at,
        dry_run=dry_run,
        scanned_count=len(manifest_paths),
        changed_count=len(changed_records),
        applied_count=applied_count,
        records=changed_records,
    )

    print(
        "Backfill complete: "
        + f"mode={'dry-run' if dry_run else 'apply'}, "
        + f"scanned={len(manifest_paths)}, "
        + f"changed={len(changed_records)}, "
        + f"written={applied_count}."
    )
    print(f"Report: {report_path.as_posix()}")


if __name__ == "__main__":
    main()
