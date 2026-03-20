#!/usr/bin/env python3
"""
Generate pending_review.md — lists experiment runs not yet reviewed in a session.

Usage (from REE_assembly root):
    python scripts/generate_pending_review.py

After reviewing, add newly-reviewed run IDs to evidence/experiments/review_tracker.json
and re-run this script to confirm the list clears.

Run as step 3 of the governance pipeline:
    python scripts/sync_v3_results.py
    python scripts/build_experiment_indexes.py
    python scripts/generate_pending_review.py
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"
CLAIM_EVIDENCE = EVIDENCE_DIR / "claim_evidence.v1.json"
REVIEW_TRACKER = EVIDENCE_DIR / "review_tracker.json"
OUTPUT = EVIDENCE_DIR / "pending_review.md"


def load_reviewed_run_ids() -> set:
    if not REVIEW_TRACKER.exists():
        print(f"[warn] review_tracker.json not found — all runs treated as pending", file=sys.stderr)
        return set()
    with open(REVIEW_TRACKER) as f:
        tracker = json.load(f)
    return set(tracker.get("reviewed_run_ids", []))


def load_pending_entries(reviewed: set) -> list[dict]:
    if not CLAIM_EVIDENCE.exists():
        print(f"[error] claim_evidence.v1.json not found — run build_experiment_indexes.py first", file=sys.stderr)
        sys.exit(1)
    with open(CLAIM_EVIDENCE) as f:
        data = json.load(f)
    entries = [
        e for e in data.get("entries", [])
        if e.get("source_type") == "experimental"
        and e.get("run_id") not in reviewed
    ]
    # Deduplicate by run_id (multiple claims per run → group them)
    by_run: dict[str, dict] = {}
    for e in entries:
        run_id = e["run_id"]
        if run_id not in by_run:
            by_run[run_id] = {
                "run_id": run_id,
                "timestamp_utc": e.get("timestamp_utc", ""),
                "status": e.get("status", "?"),
                "claims": [],
                "failure_signatures": [],
            }
        by_run[run_id]["claims"].append(e.get("claim_id", "?"))
        by_run[run_id]["failure_signatures"].extend(e.get("failure_signatures", []))
    runs = sorted(by_run.values(), key=lambda r: r["timestamp_utc"])
    return runs


def write_pending_review(runs: list[dict], last_review_utc: str) -> None:
    passes = [r for r in runs if r["status"] == "PASS"]
    fails = [r for r in runs if r["status"] != "PASS"]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "# Pending Experiment Review",
        "",
        f"Generated: `{now}`  ",
        f"Last review: `{last_review_utc}`  ",
        f"Pending: **{len(runs)}** run(s) — {len(passes)} PASS, {len(fails)} FAIL",
        "",
    ]

    if not runs:
        lines += [
            "All experiments reviewed. Nothing pending.",
            "",
        ]
    else:
        if fails:
            lines += ["## FAIL (action required)", ""]
            lines += ["| Run ID | Timestamp | Claims | Failure signatures |",
                      "|--------|-----------|--------|--------------------|"]
            for r in fails:
                claims = ", ".join(sorted(set(r["claims"])))
                sigs = ", ".join(sorted(set(r["failure_signatures"])))[:80] or "—"
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} | {sigs} |")
            lines.append("")

        if passes:
            lines += ["## PASS (verify & close)", ""]
            lines += ["| Run ID | Timestamp | Claims |",
                      "|--------|-----------|--------|"]
            for r in passes:
                claims = ", ".join(sorted(set(r["claims"])))
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} |")
            lines.append("")

    lines += [
        "---",
        "",
        "## How to mark runs as reviewed",
        "",
        "Add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`,",
        "update `last_review_utc`, then re-run this script to confirm the list clears.",
        "",
        "```bash",
        "python scripts/generate_pending_review.py",
        "```",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Written {OUTPUT.relative_to(ROOT)} — {len(runs)} pending run(s)")


def main():
    reviewed = load_reviewed_run_ids()
    last_review_utc = "unknown"
    if REVIEW_TRACKER.exists():
        with open(REVIEW_TRACKER) as f:
            last_review_utc = json.load(f).get("last_review_utc", "unknown")

    runs = load_pending_entries(reviewed)
    write_pending_review(runs, last_review_utc)


if __name__ == "__main__":
    main()
