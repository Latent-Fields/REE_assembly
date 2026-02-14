#!/usr/bin/env python3
"""Apply adjudication outcomes and cascade dependent-claim reopening.

This script turns applied governance outcomes into concrete registry updates:
- marks adjudicated claims with explicit outcomes,
- reopens dependent claims when configured cascade triggers fire,
- emits a human-readable architecture/doc patch queue.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class DecisionEntry:
    claim_id: str
    timestamp_utc: str
    decision_status: str
    recommendation: str
    selected_option: str
    rationale: str
    actor: str


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON at {path}: {exc}") from exc


def _load_json_compatible_yaml(path: Path, description: str) -> dict[str, Any]:
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


def _load_decision_log(path: Path) -> list[DecisionEntry]:
    if not path.exists():
        return []

    out: list[DecisionEntry] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue
        claim_id = str(obj.get("claim_id", "")).strip()
        timestamp_utc = str(obj.get("timestamp_utc", "")).strip()
        decision_status = str(obj.get("decision_status", "")).strip()
        recommendation = str(obj.get("recommendation", "")).strip()
        if not claim_id or not timestamp_utc or not decision_status or not recommendation:
            continue
        out.append(
            DecisionEntry(
                claim_id=claim_id,
                timestamp_utc=timestamp_utc,
                decision_status=decision_status,
                recommendation=recommendation,
                selected_option=str(obj.get("selected_option", "")).strip(),
                rationale=str(obj.get("rationale", "")).strip(),
                actor=str(obj.get("actor", "user")).strip() or "user",
            )
        )
    return out


def _latest_decision_by_claim(entries: list[DecisionEntry]) -> dict[str, DecisionEntry]:
    latest: dict[str, DecisionEntry] = {}
    for entry in entries:
        prior = latest.get(entry.claim_id)
        if prior is None or entry.timestamp_utc >= prior.timestamp_utc:
            latest[entry.claim_id] = entry
    return latest


def _split_claim_blocks(lines: list[str]) -> tuple[list[str], list[dict[str, Any]]]:
    starts = [i for i, line in enumerate(lines) if line.startswith("- id: ")]
    if not starts:
        return lines, []

    preamble = lines[: starts[0]]
    blocks: list[dict[str, Any]] = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        block_lines = lines[start:end]
        claim_id = block_lines[0].split(":", 1)[1].strip()
        blocks.append({"claim_id": claim_id, "lines": block_lines})
    return preamble, blocks


def _block_get_scalar(block_lines: list[str], key: str) -> str:
    prefix = f"  {key}:"
    for line in block_lines:
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return ""


def _block_parse_depends_on(block_lines: list[str]) -> list[str]:
    deps: list[str] = []
    in_depends = False
    for line in block_lines:
        if line.startswith("  depends_on:"):
            in_depends = True
            continue
        if in_depends and line.startswith("    - "):
            token = line.split("-", 1)[1].strip()
            if token:
                deps.append(token)
            continue
        if in_depends and (not line.startswith("    ")):
            in_depends = False
    return deps


def _block_drop_key(block_lines: list[str], key: str) -> list[str]:
    prefix = f"  {key}:"
    out: list[str] = []
    i = 0
    while i < len(block_lines):
        line = block_lines[i]
        if line.startswith(prefix):
            i += 1
            while i < len(block_lines) and block_lines[i].startswith("    - "):
                i += 1
            continue
        out.append(line)
        i += 1
    return out


def _block_insert_index(block_lines: list[str], anchor_keys: list[str]) -> int:
    for key in anchor_keys:
        prefix = f"  {key}:"
        for idx, line in enumerate(block_lines):
            if line.startswith(prefix):
                j = idx + 1
                while j < len(block_lines) and block_lines[j].startswith("    - "):
                    j += 1
                return j
    return 1


def _block_set_scalar(block_lines: list[str], key: str, value: str, anchor_keys: list[str]) -> list[str]:
    updated = _block_drop_key(block_lines, key)
    insert_idx = _block_insert_index(updated, anchor_keys)
    updated.insert(insert_idx, f"  {key}: {value}")
    return updated


def _normalize_outcome(recommendation: str, allowed_outcomes: set[str]) -> str:
    token = recommendation.strip()
    if token in allowed_outcomes:
        return token
    if token.startswith("adjudicate_"):
        mapped = token[len("adjudicate_") :]
        if mapped in allowed_outcomes:
            return mapped
    return ""


def _render_patch_queue(
    run_generated_at: str,
    run_state: dict[str, Any],
    claims_location: dict[str, str],
) -> str:
    lines: list[str] = []
    lines.append("# Adjudication Cascade Patch Queue")
    lines.append("")
    lines.append(f"Generated: `{run_generated_at}`")
    lines.append("")
    lines.append(
        "This queue is generated from applied adjudication outcomes. Use it to patch architecture narrative/docs after"
    )
    lines.append("claim-registry updates and dependency re-open actions.")
    lines.append("")

    actions = run_state.get("actions", [])
    if not actions:
        lines.append("No adjudication-cascade actions in this run.")
        lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    lines.append("| claim_id | outcome | status_before | status_after | dependents_reopened |")
    lines.append("|---|---|---|---|---:|")
    for action in actions:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{action.get('claim_id', '')}`",
                    f"`{action.get('outcome', '')}`",
                    f"`{action.get('status_before', '')}`",
                    f"`{action.get('status_after', '')}`",
                    str(len(action.get("dependents_reopened", []))),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Required Doc Patches")
    lines.append("")
    for action in actions:
        claim_id = str(action.get("claim_id", ""))
        outcome = str(action.get("outcome", ""))
        location = claims_location.get(claim_id, "")
        lines.append(f"### {claim_id} ({outcome})")
        if location:
            lines.append(f"- Primary claim anchor: `{location}`")
        lines.append("- Patch tasks:")
        lines.append("  - Update architecture text to reflect adjudication outcome and rationale.")
        lines.append("  - Ensure dependent-claim references reflect reopened status or supersession.")
        reopened = action.get("dependents_reopened", [])
        if reopened:
            lines.append("- Reopened dependents:")
            for dep in reopened:
                dep_loc = claims_location.get(dep, "")
                if dep_loc:
                    lines.append(f"  - `{dep}` at `{dep_loc}`")
                else:
                    lines.append(f"  - `{dep}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply adjudication-cascade outcomes to claims registry and emit patch queue."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly root.",
    )
    parser.add_argument(
        "--decision-log",
        default="evidence/decisions/decision_log.v1.jsonl",
        help="Decision log JSONL path (repo-relative).",
    )
    parser.add_argument(
        "--claims-file",
        default="docs/claims/claims.yaml",
        help="Claims registry YAML path (repo-relative).",
    )
    parser.add_argument(
        "--planning-criteria",
        default="evidence/planning/planning_criteria.v1.yaml",
        help="Planning criteria path (JSON-compatible YAML).",
    )
    parser.add_argument(
        "--state-json",
        default="evidence/decisions/adjudication_cascade_state.v1.json",
        help="State file output path (repo-relative).",
    )
    parser.add_argument(
        "--patch-queue-md",
        default="evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md",
        help="Patch queue markdown output path (repo-relative).",
    )
    parser.add_argument(
        "--decision-statuses",
        default="applied",
        help="Comma-separated decision statuses that are eligible for application (default: applied).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Ignore state guard and reapply matching decisions.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute actions and write state/queue without changing claims.yaml.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    decision_log_path = (repo_root / args.decision_log).resolve()
    claims_path = (repo_root / args.claims_file).resolve()
    planning_criteria_path = (repo_root / args.planning_criteria).resolve()
    state_path = (repo_root / args.state_json).resolve()
    patch_queue_path = (repo_root / args.patch_queue_md).resolve()

    eligible_statuses = {
        token.strip()
        for token in args.decision_statuses.split(",")
        if token.strip()
    }
    if not eligible_statuses:
        raise SystemExit("No eligible decision statuses provided.")

    planning_criteria = _load_json_compatible_yaml(planning_criteria_path, "planning criteria")
    adjudication = planning_criteria.get("model_adjudication", {})
    allowed_outcomes = {
        str(token).strip()
        for token in adjudication.get("allowed_conflict_outcomes", [])
        if str(token).strip()
    }
    if not allowed_outcomes:
        allowed_outcomes = {
            "retain_ree",
            "hybridize",
            "adopt_jepa_structure",
            "retire_ree_claim",
        }
    cascade_policy = adjudication.get("cascade_policy", {})
    cascade_enabled = bool(cascade_policy.get("enabled", True))
    cascade_triggers = {
        str(token).strip()
        for token in cascade_policy.get("trigger_outcomes", [])
        if str(token).strip()
    }
    if not cascade_triggers:
        cascade_triggers = {"adopt_jepa_structure", "retire_ree_claim"}
    dependency_reopen_status = str(cascade_policy.get("dependency_reopen_status", "candidate"))

    decisions = _load_decision_log(decision_log_path)
    latest = _latest_decision_by_claim(decisions)

    claims_text = claims_path.read_text(encoding="utf-8")
    original_lines = claims_text.splitlines()
    preamble, blocks = _split_claim_blocks(original_lines)
    block_by_id = {str(block["claim_id"]): block for block in blocks}

    depends_map: dict[str, list[str]] = {}
    dependents: dict[str, list[str]] = {}
    claim_locations: dict[str, str] = {}
    for block in blocks:
        claim_id = str(block["claim_id"])
        block_lines = block["lines"]
        deps = _block_parse_depends_on(block_lines)
        depends_map[claim_id] = deps
        claim_locations[claim_id] = _block_get_scalar(block_lines, "location")
        for dep in deps:
            dependents.setdefault(dep, []).append(claim_id)
    for dep in dependents:
        dependents[dep].sort()

    prior_state = _load_json(state_path)
    processed_claims = prior_state.get("processed_claims", {})
    if not isinstance(processed_claims, dict):
        processed_claims = {}

    run_generated_at = _now_utc()
    run_actions: list[dict[str, Any]] = []
    claims_touched: set[str] = set()
    dependents_reopened_all: set[str] = set()

    target_entries: list[DecisionEntry] = []
    for claim_id, entry in latest.items():
        if entry.decision_status not in eligible_statuses:
            continue
        outcome = _normalize_outcome(entry.recommendation, allowed_outcomes)
        if not outcome:
            continue
        target_entries.append(entry)
    target_entries.sort(key=lambda e: (e.timestamp_utc, e.claim_id))

    for entry in target_entries:
        claim_id = entry.claim_id
        outcome = _normalize_outcome(entry.recommendation, allowed_outcomes)
        if not outcome:
            continue
        block = block_by_id.get(claim_id)
        if block is None:
            continue

        fingerprint = f"{entry.timestamp_utc}|{entry.decision_status}|{outcome}|{entry.recommendation}"
        prior = processed_claims.get(claim_id, {})
        if (not args.force) and isinstance(prior, dict):
            if str(prior.get("decision_fingerprint", "")) == fingerprint:
                continue

        block_lines = list(block["lines"])
        status_before = _block_get_scalar(block_lines, "status") or "unknown"
        status_after = status_before
        if outcome in {"retire_ree_claim", "adopt_jepa_structure"}:
            status_after = "legacy"

        block_lines = _block_set_scalar(
            block_lines,
            "status",
            status_after,
            anchor_keys=["polarity", "subject", "claim_type"],
        )
        block_lines = _block_set_scalar(
            block_lines,
            "lifecycle_stage",
            "adjudicated",
            anchor_keys=["status", "polarity", "claim_type"],
        )
        block_lines = _block_set_scalar(
            block_lines,
            "adjudication_outcome",
            outcome,
            anchor_keys=["lifecycle_stage", "status"],
        )
        block_lines = _block_set_scalar(
            block_lines,
            "adjudicated_at_utc",
            entry.timestamp_utc,
            anchor_keys=["adjudication_outcome", "lifecycle_stage"],
        )
        block_lines = _block_set_scalar(
            block_lines,
            "adjudication_decision_status",
            entry.decision_status,
            anchor_keys=["adjudicated_at_utc", "adjudication_outcome"],
        )
        block_lines = _block_set_scalar(
            block_lines,
            "adjudication_recommendation",
            entry.recommendation,
            anchor_keys=["adjudication_decision_status", "adjudicated_at_utc"],
        )

        block["lines"] = block_lines
        block_by_id[claim_id] = block
        claims_touched.add(claim_id)

        reopened_dependents: list[str] = []
        if cascade_enabled and outcome in cascade_triggers:
            for dep_claim_id in dependents.get(claim_id, []):
                dep_block = block_by_id.get(dep_claim_id)
                if dep_block is None:
                    continue
                dep_lines = list(dep_block["lines"])
                dep_status_before = _block_get_scalar(dep_lines, "status") or "unknown"
                if dep_status_before == "legacy":
                    continue
                dep_lines = _block_set_scalar(
                    dep_lines,
                    "status",
                    dependency_reopen_status,
                    anchor_keys=["polarity", "subject", "claim_type"],
                )
                dep_lines = _block_set_scalar(
                    dep_lines,
                    "lifecycle_stage",
                    "reopened_by_cascade",
                    anchor_keys=["status", "polarity", "claim_type"],
                )
                dep_lines = _block_set_scalar(
                    dep_lines,
                    "reopened_due_to_claim",
                    claim_id,
                    anchor_keys=["lifecycle_stage", "status"],
                )
                dep_lines = _block_set_scalar(
                    dep_lines,
                    "reopened_by_outcome",
                    outcome,
                    anchor_keys=["reopened_due_to_claim", "lifecycle_stage"],
                )
                dep_lines = _block_set_scalar(
                    dep_lines,
                    "reopened_at_utc",
                    run_generated_at,
                    anchor_keys=["reopened_by_outcome", "reopened_due_to_claim"],
                )
                dep_block["lines"] = dep_lines
                block_by_id[dep_claim_id] = dep_block
                claims_touched.add(dep_claim_id)
                reopened_dependents.append(dep_claim_id)
                dependents_reopened_all.add(dep_claim_id)

        run_actions.append(
            {
                "claim_id": claim_id,
                "outcome": outcome,
                "decision_status": entry.decision_status,
                "recommendation": entry.recommendation,
                "decision_timestamp_utc": entry.timestamp_utc,
                "status_before": status_before,
                "status_after": status_after,
                "dependents_reopened": sorted(reopened_dependents),
            }
        )
        processed_claims[claim_id] = {
            "decision_fingerprint": fingerprint,
            "outcome": outcome,
            "decision_status": entry.decision_status,
            "decision_timestamp_utc": entry.timestamp_utc,
            "applied_at_utc": run_generated_at,
            "dependents_reopened": sorted(reopened_dependents),
        }

    claims_changed = len(claims_touched) > 0
    if claims_changed and not args.dry_run:
        output_lines = list(preamble)
        for block in blocks:
            output_lines.extend(block_by_id[str(block["claim_id"])]["lines"])
        claims_path.write_text("\n".join(output_lines).rstrip() + "\n", encoding="utf-8")

    run_state = {
        "schema_version": "adjudication_cascade_state/v1",
        "generated_at_utc": run_generated_at,
        "source_decision_log": args.decision_log,
        "decision_status_filters": sorted(eligible_statuses),
        "dry_run": bool(args.dry_run),
        "actions_applied_count": len(run_actions),
        "claims_updated": sorted(claims_touched),
        "dependents_reopened": sorted(dependents_reopened_all),
        "actions": run_actions,
    }
    state_doc = {
        "schema_version": "adjudication_cascade_state/v1",
        "generated_at_utc": run_generated_at,
        "source_decision_log": args.decision_log,
        "processed_claims": processed_claims,
        "last_run": run_state,
    }

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    patch_queue_path.parent.mkdir(parents=True, exist_ok=True)
    patch_queue_path.write_text(
        _render_patch_queue(run_generated_at, run_state, claim_locations),
        encoding="utf-8",
    )

    print(
        "Adjudication cascade complete: "
        + f"eligible_decisions={len(target_entries)}, actions={len(run_actions)}, "
        + f"claims_updated={len(claims_touched)}, dependents_reopened={len(dependents_reopened_all)}, "
        + f"dry_run={str(bool(args.dry_run)).lower()}."
    )
    print(f"State JSON: {state_path.as_posix()}")
    print(f"Patch queue: {patch_queue_path.as_posix()}")
    if claims_changed:
        if args.dry_run:
            print(f"Claims file unchanged (dry-run): {claims_path.as_posix()}")
        else:
            print(f"Claims file updated: {claims_path.as_posix()}")
    else:
        print("No claim registry changes applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
