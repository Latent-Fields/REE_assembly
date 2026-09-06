#!/usr/bin/env python3
"""Deterministic thought sweep for docs/thoughts.

Scans markdown files in docs/thoughts, classifies them by processing status,
and writes machine + human readable sweep outputs.

A processed thought is expected to carry a BACK-LINK to wherever it was
processed. Four marker forms are recognised (checked in this order; the first
that yields a link wins and is recorded as ``link_form``):

  legacy         a ``Processed in:`` line followed by a ``- <target>`` bullet block
  intake_header  a ``Intake: <path>`` (or ``**Intake:** <path>``) header line
  frontmatter    YAML frontmatter with ``intake:``, ``claims_registered:`` or
                 ``related_claims:``
  superseded     a ``Superseded by: <path>`` header line (the canonical copy of
                 a duplicated thought stands in for an intake)

``Status: processed`` detection is unchanged (first 25 lines, case-insensitive).
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
# ``Intake: <path>`` / ``**Intake:** <path>`` / ``**Intake**: <path>``. The first
# whitespace-delimited token after the colon is the link; trailing prose is ignored.
# ``Intake class:`` and ``Thought Intake:`` deliberately do NOT match (anchored,
# and the word must be followed directly by the colon or closing bold marker).
INTAKE_HEADER_RE = re.compile(
    r"^\s*(?:\*\*)?Intake(?:\*\*)?\s*:\s*(?:\*\*)?\s*(?P<path>\S+)", re.IGNORECASE
)
SUPERSEDED_RE = re.compile(
    r"^\s*(?:\*\*)?Superseded by(?:\*\*)?\s*:\s*(?:\*\*)?\s*(?P<path>\S+)", re.IGNORECASE
)
FRONTMATTER_LINK_KEYS = ("intake", "claims_registered", "related_claims")
# Header-form markers must sit near the top of the file (frontmatter excluded).
HEADER_WINDOW = 40
LINK_FORMS = ("legacy", "intake_header", "frontmatter", "superseded")
# Reports and machine outputs that live in docs/thoughts but are not thoughts.
EXCLUDED = {
    "README.md",
    "SWEEP_REPORT.md",
    "INTAKE_AUDIT_REPORT.md",
    "thought_sweep.v1.json",
    "thought_intake_audit.v1.json",
}
REPORT_NAME_RE = re.compile(r"^[A-Z0-9_]+_REPORT\.md$")


@dataclass
class ThoughtFile:
    path: Path
    status: str
    is_processed: bool
    processed_in_links: list[str]
    filename_date: str
    link_form: str = "none"

    def to_json(self) -> dict[str, object]:
        return {
            "file": self.path.name,
            "status": self.status,
            "is_processed": self.is_processed,
            "processed_in_links": self.processed_in_links,
            "link_form": self.link_form,
            "filename_date": self.filename_date,
        }


def _extract_status(lines: list[str]) -> str:
    # Deterministic rule: only first 25 lines may declare sweep status.
    for line in lines[:25]:
        match = STATUS_RE.match(line)
        if match:
            return match.group("status").strip().lower()
    return "unprocessed"


def _strip_link(token: str) -> str:
    return token.strip().strip("`").rstrip(",.;:)")


def _frontmatter_span(lines: list[str]) -> tuple[int, int] | None:
    """Return (start, end) line indexes of a leading YAML frontmatter block, else None."""
    if not lines or lines[0].strip() != "---":
        return None
    for idx in range(1, min(len(lines), 200)):
        if lines[idx].strip() == "---":
            return (0, idx)
    return None


def _extract_legacy_links(lines: list[str]) -> list[str]:
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


def _extract_header_links(lines: list[str], pattern: re.Pattern[str]) -> list[str]:
    span = _frontmatter_span(lines)
    start = span[1] + 1 if span else 0
    links: list[str] = []
    for line in lines[start : start + HEADER_WINDOW]:
        match = pattern.match(line)
        if match:
            link = _strip_link(match.group("path"))
            if link and link not in links:
                links.append(link)
    return links


def _extract_frontmatter_links(lines: list[str]) -> list[str]:
    span = _frontmatter_span(lines)
    if span is None:
        return []
    links: list[str] = []
    current_key: str | None = None
    for line in lines[span[0] + 1 : span[1]]:
        if not line.strip():
            continue
        if not line[0].isspace():
            key, sep, value = line.partition(":")
            key = key.strip().lower()
            current_key = key if sep and key in FRONTMATTER_LINK_KEYS else None
            if current_key and value.strip():
                link = _strip_link(value)
                if link and link not in links:
                    links.append(link)
        elif current_key and line.strip().startswith("- "):
            link = _strip_link(line.strip()[2:])
            if link and link not in links:
                links.append(link)
    return links


def _extract_processed_links(lines: list[str]) -> tuple[list[str], str]:
    """Return (links, link_form). Forms are tried in LINK_FORMS order; first hit wins."""
    extractors = {
        "legacy": lambda: _extract_legacy_links(lines),
        "intake_header": lambda: _extract_header_links(lines, INTAKE_HEADER_RE),
        "frontmatter": lambda: _extract_frontmatter_links(lines),
        "superseded": lambda: _extract_header_links(lines, SUPERSEDED_RE),
    }
    for form in LINK_FORMS:
        links = extractors[form]()
        if links:
            return links, form
    return [], "none"


def _is_thought_file(path: Path) -> bool:
    if path.name in EXCLUDED:
        return False
    if REPORT_NAME_RE.match(path.name):
        return False
    return True


def _scan(root: Path) -> list[ThoughtFile]:
    records: list[ThoughtFile] = []
    for path in sorted(root.glob("*.md")):
        if not _is_thought_file(path):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        status = _extract_status(lines)
        processed_links, link_form = _extract_processed_links(lines)
        date_match = DATE_RE.match(path.name)
        filename_date = date_match.group("date") if date_match else ""

        records.append(
            ThoughtFile(
                path=path,
                status=status,
                is_processed=(status == "processed"),
                processed_in_links=processed_links,
                filename_date=filename_date,
                link_form=link_form,
            )
        )
    return records


def _link_form_counts(processed: list[ThoughtFile]) -> dict[str, int]:
    counts = {form: 0 for form in LINK_FORMS}
    counts["none"] = 0
    for rec in processed:
        counts[rec.link_form] = counts.get(rec.link_form, 0) + 1
    return counts


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
            "link_forms": _link_form_counts(processed),
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
    lines.append(f"| processed missing back-links | {len(processed_missing_links)} |")
    lines.append("")
    lines.append("Back-link forms among processed thoughts:")
    lines.append("")
    for form, count in _link_form_counts(processed).items():
        lines.append(f"- `{form}`: {count}")
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
            f"- `{rec.path.name}` ({len(rec.processed_in_links)} link(s), form=`{rec.link_form}`)"
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
    form_counts = _link_form_counts([r for r in records if r.is_processed])
    print("Back-link forms: " + ", ".join(f"{k}={v}" for k, v in form_counts.items()))

    if args.check_unprocessed and unprocessed > 0:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
