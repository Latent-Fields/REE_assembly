#!/usr/bin/env python3
"""Append a human decision entry to evidence/decisions/decision_log.v1.jsonl."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_STATUS = {"pending_user", "discussing", "approved", "rejected", "applied"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Record a decision log entry.")
    parser.add_argument("--claim-id", required=True, help="Claim ID, e.g. MECH-056")
    parser.add_argument("--recommendation", required=True, help="Recommendation token")
    parser.add_argument("--decision-needed", required=True, help="Decision description")
    parser.add_argument(
        "--decision-status",
        required=True,
        choices=sorted(ALLOWED_STATUS),
        help="Decision lifecycle status",
    )
    parser.add_argument("--selected-option", default="", help="Chosen option text")
    parser.add_argument("--rationale", default="", help="Short rationale")
    parser.add_argument("--actor", default="user", help="Decision actor")
    parser.add_argument(
        "--source-file",
        default="evidence/experiments/promotion_demotion_recommendations.md",
        help="Source recommendation file",
    )
    parser.add_argument("--notes", default="", help="Optional notes")
    parser.add_argument(
        "--log-path",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "decisions" / "decision_log.v1.jsonl",
        help="Path to decision log JSONL",
    )

    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    entry = {
        "schema_version": "decision_log_entry/v1",
        "timestamp_utc": timestamp,
        "claim_id": args.claim_id.strip(),
        "decision_status": args.decision_status,
        "recommendation": args.recommendation.strip(),
        "decision_needed": args.decision_needed.strip(),
        "selected_option": args.selected_option.strip(),
        "rationale": args.rationale.strip(),
        "actor": args.actor.strip() or "user",
        "context": {
            "source_file": args.source_file.strip(),
            "notes": args.notes.strip(),
        },
    }

    if not entry["claim_id"]:
        raise SystemExit("--claim-id cannot be empty")
    if not entry["recommendation"]:
        raise SystemExit("--recommendation cannot be empty")
    if not entry["decision_needed"]:
        raise SystemExit("--decision-needed cannot be empty")

    log_path = args.log_path.resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")

    print(f"Appended decision entry for {entry['claim_id']} to {log_path}")


if __name__ == "__main__":
    main()
