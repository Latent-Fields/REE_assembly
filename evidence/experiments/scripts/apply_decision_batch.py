#!/usr/bin/env python3
"""Apply a JSON batch of human decisions to the persistent decision log."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALLOWED_STATUS = {"pending_user", "discussing", "approved", "rejected", "applied"}
DEFAULT_SOURCE_FILE = "evidence/decisions/human_decision_briefs/latest/INDEX.md"


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clean(value: Any) -> str:
    return str(value or "").strip()


def _load_batch(path: Path) -> dict[str, Any]:
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise ValueError(f"Batch file must be a JSON object: {path}")
    return loaded


def _normalize_entry(
    raw: dict[str, Any],
    *,
    index: int,
    actor_default: str,
    source_file_default: str,
) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError(f"items[{index}] must be a JSON object")

    claim_id = _clean(raw.get("claim_id"))
    recommendation = _clean(raw.get("recommendation"))
    decision_needed = _clean(raw.get("decision_needed"))
    decision_status = _clean(raw.get("decision_status")).lower()
    selected_option = _clean(raw.get("selected_option"))
    rationale = _clean(raw.get("rationale"))
    actor = _clean(raw.get("actor")) or actor_default
    source_file = _clean(raw.get("source_file")) or source_file_default
    notes = _clean(raw.get("notes"))
    timestamp_utc = _clean(raw.get("timestamp_utc")) or _now_utc()

    missing: list[str] = []
    if not claim_id:
        missing.append("claim_id")
    if not recommendation:
        missing.append("recommendation")
    if not decision_needed:
        missing.append("decision_needed")
    if not decision_status:
        missing.append("decision_status")
    if missing:
        missing_csv = ", ".join(missing)
        raise ValueError(f"items[{index}] missing required field(s): {missing_csv}")

    if decision_status not in ALLOWED_STATUS:
        allowed_csv = ", ".join(sorted(ALLOWED_STATUS))
        raise ValueError(
            f"items[{index}] has unsupported decision_status={decision_status!r}; allowed: {allowed_csv}"
        )

    return {
        "schema_version": "decision_log_entry/v1",
        "timestamp_utc": timestamp_utc,
        "claim_id": claim_id,
        "decision_status": decision_status,
        "recommendation": recommendation,
        "decision_needed": decision_needed,
        "selected_option": selected_option,
        "rationale": rationale,
        "actor": actor,
        "context": {
            "source_file": source_file,
            "notes": notes,
        },
    }


def _run_step(cmd: list[str], *, cwd: Path) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply a decision batch JSON to decision_log.v1.jsonl.")
    parser.add_argument("--input", required=True, type=Path, help="Path to decision_batch.v1.json")
    parser.add_argument(
        "--log-path",
        type=Path,
        default=Path("evidence/decisions/decision_log.v1.jsonl"),
        help="Decision log path (repo-relative by default)",
    )
    parser.add_argument(
        "--actor-default",
        default="user",
        help="Fallback actor when an item omits actor",
    )
    parser.add_argument(
        "--source-file-default",
        default=DEFAULT_SOURCE_FILE,
        help="Fallback source_file when an item omits source_file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and summarize without writing the decision log",
    )
    parser.add_argument(
        "--refresh-indexes",
        action="store_true",
        help="Run build_experiment_indexes.py after applying entries",
    )
    parser.add_argument(
        "--run-governance",
        action="store_true",
        help="Run run_governance_cycle.py after applying entries",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    input_path = args.input if args.input.is_absolute() else (repo_root / args.input).resolve()
    log_path = args.log_path if args.log_path.is_absolute() else (repo_root / args.log_path).resolve()

    if not input_path.exists():
        raise SystemExit(f"--input file not found: {input_path}")

    batch = _load_batch(input_path)
    raw_items = batch.get("items", [])
    if not isinstance(raw_items, list):
        raise SystemExit(f"`items` must be a JSON array in {input_path}")
    if not raw_items:
        raise SystemExit(f"No items found in decision batch: {input_path}")

    normalized_items: list[dict[str, Any]] = []
    errors: list[str] = []
    for idx, raw in enumerate(raw_items, start=1):
        try:
            normalized_items.append(
                _normalize_entry(
                    raw,
                    index=idx,
                    actor_default=_clean(args.actor_default) or "user",
                    source_file_default=_clean(args.source_file_default) or DEFAULT_SOURCE_FILE,
                )
            )
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        print("Decision batch validation failed:")
        for msg in errors:
            print(f"- {msg}")
        raise SystemExit(1)

    if args.dry_run:
        claim_ids = [entry["claim_id"] for entry in normalized_items]
        print(f"Validated {len(normalized_items)} decision item(s): {', '.join(claim_ids)}")
        return

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        for entry in normalized_items:
            handle.write(json.dumps(entry, sort_keys=True) + "\n")

    print(f"Appended {len(normalized_items)} decision item(s) to {log_path}")

    if args.refresh_indexes:
        _run_step(
            [sys.executable, str(repo_root / "evidence/experiments/scripts/build_experiment_indexes.py")],
            cwd=repo_root,
        )

    if args.run_governance:
        _run_step(
            [sys.executable, str(repo_root / "evidence/planning/scripts/run_governance_cycle.py")],
            cwd=repo_root,
        )


if __name__ == "__main__":
    main()
