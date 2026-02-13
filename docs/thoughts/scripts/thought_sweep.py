#!/usr/bin/env python3
"""Deterministic thought sweep for docs/thoughts.

Scans markdown files in docs/thoughts, classifies them by processing status,
and writes machine + human readable sweep outputs.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

STATUS_RE = re.compile(r"^\s*Status\s*:\s*(?P<status>[A-Za-z0-9_-]+)\s*$", re.IGNORECASE)
DATE_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})_")
EXCLUDED = {
    "README.md",
    "SWEEP_REPORT.md",
    "thought_sweep.v1.json",
}


@dataclass
class ThoughtFile:
    path: Path
    status: str
    is_processed: bool
    processed_in_links: list[str]
    filename_date: str

    def to_json(self) -> dict[str, object]:
        return {
            "file": self.path.name,
            "status": self.status,
            "is_processed": self.is_processed,
            "processed_in_links": self.processed_in_links,
            "filename_date": self.filename_date,
        }


def _extract_status(lines: list[str]) -> str:
    # Deterministic rule: only first 25 lines may declare sweep status.
    for line in lines[:25]:
        match = STATUS_RE.match(line)
        if match:
            return match.group("status").strip().lower()
    return "unprocessed"


def _extract_processed_links(lines: list[str]) -> list[str]:
    links: list[str] = []
    marker_idx = None
    for idx, line in enumerate(lines):
        if line.strip().lower() == "processed in:":
            marker_idx = idx
            break
    if marker_idx is None:
        return links

    for line in lines[marker_idx + 1 :]:
        stripped = line.strip()
        if not stripped:
            if links:
                break
            continue
        if not stripped.startswith("- "):
            if links:
                break
            continue
        links.append(stripped[2:].strip())
    return links


def _scan(root: Path) -> list[ThoughtFile]:
    records: list[ThoughtFile] = []
    for path in sorted(root.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        status = _extract_status(lines)
        processed_links = _extract_processed_links(lines)
        date_match = DATE_RE.match(path.name)
        filename_date = date_match.group("date") if date_match else ""

        records.append(
            ThoughtFile(
                path=path,
                status=status,
                is_processed=(status == "processed"),
                processed_in_links=processed_links,
                filename_date=filename_date,
            )
        )
    return records


def _write_json(output_path: Path, records: list[ThoughtFile], generated_at: str) -> None:
    processed = [r for r in records if r.is_processed]
    unprocessed = [r for r in records if not r.is_processed]
    processed_missing_links = [r for r in processed if not r.processed_in_links]
    payload = {
        "schema_version": "thought_sweep/v1",
        "generated_at_utc": generated_at,
        "root": output_path.parent.as_posix(),
        "summary": {
            "total": len(records),
            "processed": len(processed),
            "unprocessed": len(unprocessed),
            "processed_missing_links": len(processed_missing_links),
        },
        "records": [r.to_json() for r in records],
    }
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_report(output_path: Path, records: list[ThoughtFile], generated_at: str) -> None:
    processed = [r for r in records if r.is_processed]
    unprocessed = [r for r in records if not r.is_processed]
    processed_missing_links = [r for r in processed if not r.processed_in_links]

    lines: list[str] = []
    lines.append("# Thought Sweep Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("| metric | count |")
    lines.append("|---|---|")
    lines.append(f"| total thought files | {len(records)} |")
    lines.append(f"| processed | {len(processed)} |")
    lines.append(f"| unprocessed | {len(unprocessed)} |")
    lines.append(f"| processed missing `Processed in` links | {len(processed_missing_links)} |")
    lines.append("")
    lines.append("## Unprocessed Queue")
    lines.append("")
    if not unprocessed:
        lines.append("- _none_")
    else:
        for rec in unprocessed:
            date_prefix = f"`{rec.filename_date}` " if rec.filename_date else ""
            lines.append(f"- {date_prefix}`{rec.path.name}` (status=`{rec.status}`)")
    lines.append("")
    lines.append("## Processed Missing Links")
    lines.append("")
    if not processed_missing_links:
        lines.append("- _none_")
    else:
        for rec in processed_missing_links:
            lines.append(f"- `{rec.path.name}`")
    lines.append("")
    lines.append("## Processed Snapshot")
    lines.append("")
    for rec in processed:
        lines.append(
            f"- `{rec.path.name}` ({len(rec.processed_in_links)} link(s) in `Processed in`)"
        )

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run deterministic thought sweep.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to docs/thoughts",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=None,
        help="Output JSON path (default: <root>/thought_sweep.v1.json)",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=None,
        help="Output markdown path (default: <root>/SWEEP_REPORT.md)",
    )
    parser.add_argument(
        "--check-unprocessed",
        action="store_true",
        help="Exit non-zero if unprocessed thought files are present.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    output_json = args.output_json.resolve() if args.output_json else root / "thought_sweep.v1.json"
    output_md = args.output_md.resolve() if args.output_md else root / "SWEEP_REPORT.md"

    records = _scan(root)
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    _write_json(output_json, records, generated_at)
    _write_report(output_md, records, generated_at)

    processed = sum(1 for r in records if r.is_processed)
    unprocessed = len(records) - processed
    missing_links = sum(1 for r in records if r.is_processed and not r.processed_in_links)
    print(
        "Thought sweep: "
        + f"total={len(records)}, processed={processed}, unprocessed={unprocessed}, "
        + f"processed_missing_links={missing_links}"
    )

    if args.check_unprocessed and unprocessed > 0:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
