#!/usr/bin/env python3
"""Ground-truth audit of BOTH thought-intake paths.

The two-stage thought pipeline (see docs/thoughts/README.md) has one automated
check today -- thought_sweep.py -- and it only covers Stage 1 (raw capture in
this folder), by a marker convention (`Status: processed`). Two gaps that
motivated this script:

1. Stage 2 (structured analysis at evidence/planning/thought_intake_*.md) has
   NO automated check at all. A structured intake can carry a fully-written
   "Candidate claims" section that was never actually registered into
   claims.yaml, and nothing surfaces that except a full manual re-read.

2. A marker/keyword convention over-states orphans in both directions: a file
   can say "REGISTERED" and be wrong (stale after a claim was renamed or
   retracted), or lack the word and be fully processed some other way (folded
   into a canonical doc, per the README's own "not every thought needs a
   structured intake" allowance). The only ground truth is whether the claim
   ID actually exists in claims.yaml right now.

This script checks BOTH stages against that ground truth:

- Stage 1: for every raw thought file's `Processed in:` links, extract any
  claim-shaped ID and confirm it still exists in claims.yaml. A link that
  named a real claim at write time but now points at nothing (renamed,
  merged, retracted) is flagged -- thought_sweep.py cannot see this, since it
  only checks that a `Processed in:` block exists, never that its targets are
  still real.
- Stage 2: for every structured intake's "Candidate claims"-shaped section,
  extract any claim-shaped ID and classify the file as all-registered,
  partially-registered, fully-orphaned, no-ids-named (prose-only candidates --
  needs a human read), or no-candidate-section (nothing to check).

Read-only against claims.yaml and both thought-intake trees; writes only its
own report files (no claim required to run it -- see docs/thoughts/README.md).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from thought_sweep import _extract_processed_links, _extract_status  # noqa: E402

CLAIM_ID_RE = re.compile(r"\b((?:ARC|MECH|INV|Q|SD)-[0-9]{2,4}[a-z]?)\b")
CANDIDATE_HEADER_RE = re.compile(r"(?im)^(#{1,4})\s*.*candidate claims?.*$")
NOT_REGISTERED_RE = re.compile(
    r"(?i)not\s+(?:yet\s+)?registered|for future (?:session|registration)|not\s+registered"
)


def _load_claim_ids(claims_yaml: Path) -> set[str]:
    text = claims_yaml.read_text(encoding="utf-8")
    return set(re.findall(r"^- id:\s*([A-Za-z]+-[0-9]+[a-z]?)", text, re.M))


def _candidate_section(text: str) -> str | None:
    match = CANDIDATE_HEADER_RE.search(text)
    if not match:
        return None
    level = len(match.group(1))
    section = text[match.start() : match.start() + 8000]
    # Only a SIBLING or SHALLOWER header ends the section -- a DEEPER header
    # (e.g. "### ARC-120: ..." under a "## Candidate Claims" parent) is a
    # sub-item of this candidate list, not the start of the next section.
    next_header_re = re.compile(r"\n#{1," + str(level) + r"}(?!#)\s")
    nxt = next_header_re.search(section[1:])
    if nxt:
        section = section[: nxt.start() + 1]
    return section


@dataclass
class Stage1Finding:
    file: str
    broken_ids: list[str] = field(default_factory=list)


@dataclass
class Stage2Record:
    file: str
    classification: str
    ids_named: list[str] = field(default_factory=list)
    missing_ids: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, object]:
        return {
            "file": self.file,
            "classification": self.classification,
            "ids_named": self.ids_named,
            "missing_ids": self.missing_ids,
        }


def _audit_stage1(thoughts_root: Path, claim_ids: set[str]) -> list[Stage1Finding]:
    findings: list[Stage1Finding] = []
    excluded = {"README.md", "SWEEP_REPORT.md", "thought_sweep.v1.json"}
    for path in sorted(thoughts_root.glob("*.md")):
        if path.name in excluded:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        status = _extract_status(lines)
        if status != "processed":
            continue
        links = _extract_processed_links(lines)
        broken: list[str] = []
        for link in links:
            for cid in CLAIM_ID_RE.findall(link):
                if cid not in claim_ids:
                    broken.append(cid)
        if broken:
            findings.append(Stage1Finding(file=path.name, broken_ids=sorted(set(broken))))
    return findings


def _classify_stage2(text: str, claim_ids: set[str]) -> tuple[str, list[str], list[str]]:
    section = _candidate_section(text)
    if section is None:
        return "no_candidate_section", [], []

    ids_named = sorted(set(CLAIM_ID_RE.findall(section)))
    explicit_not_registered = bool(NOT_REGISTERED_RE.search(section))

    if not ids_named:
        if explicit_not_registered:
            return "not_registered_no_ids", [], []
        return "no_ids_named", [], []

    missing = sorted(i for i in ids_named if i not in claim_ids)
    if not missing:
        return "all_registered", ids_named, []
    if len(missing) == len(ids_named):
        return "fully_orphaned", ids_named, missing
    return "partially_registered", ids_named, missing


def _audit_stage2(planning_root: Path, claim_ids: set[str]) -> list[Stage2Record]:
    records: list[Stage2Record] = []
    for path in sorted(planning_root.glob("thought_intake_*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        classification, ids_named, missing = _classify_stage2(text, claim_ids)
        records.append(
            Stage2Record(
                file=path.name,
                classification=classification,
                ids_named=ids_named,
                missing_ids=missing,
            )
        )
    return records


def _write_json(
    output_path: Path,
    stage1: list[Stage1Finding],
    stage2: list[Stage2Record],
    generated_at: str,
) -> None:
    orphan_classes = {"fully_orphaned", "partially_registered", "not_registered_no_ids"}
    needs_read_classes = {"no_ids_named"}
    payload = {
        "schema_version": "thought_intake_audit/v1",
        "generated_at_utc": generated_at,
        "summary": {
            "stage1_broken_processed_links": len(stage1),
            "stage2_total": len(stage2),
            "stage2_orphaned_or_unregistered": sum(
                1 for r in stage2 if r.classification in orphan_classes
            ),
            "stage2_needs_human_read": sum(
                1 for r in stage2 if r.classification in needs_read_classes
            ),
            "stage2_all_registered": sum(1 for r in stage2 if r.classification == "all_registered"),
            "stage2_no_candidate_section": sum(
                1 for r in stage2 if r.classification == "no_candidate_section"
            ),
        },
        "stage1_broken_processed_links": [
            {"file": f.file, "broken_ids": f.broken_ids} for f in stage1
        ],
        "stage2_records": [r.to_json() for r in stage2],
    }
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_report(
    output_path: Path,
    stage1: list[Stage1Finding],
    stage2: list[Stage2Record],
    generated_at: str,
) -> None:
    orphan_classes = {"fully_orphaned", "partially_registered", "not_registered_no_ids"}
    orphans = [r for r in stage2 if r.classification in orphan_classes]
    needs_read = [r for r in stage2 if r.classification == "no_ids_named"]
    all_registered = [r for r in stage2 if r.classification == "all_registered"]
    no_section = [r for r in stage2 if r.classification == "no_candidate_section"]

    lines: list[str] = []
    lines.append("# Thought Intake Audit Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append(
        "Ground-truth cross-check of both thought-intake paths against `docs/claims/claims.yaml` "
        "-- not a keyword/marker check. See `docs/thoughts/README.md` for what the two paths are "
        "and `docs/thoughts/scripts/thought_intake_audit.py` module docstring for the method."
    )
    lines.append("")
    lines.append("## Stage 1 (raw capture, this folder) -- broken `Processed in:` links")
    lines.append("")
    lines.append(
        "A thought marked `processed` that points at a claim ID no longer in `claims.yaml` "
        "(renamed, merged, retracted since the link was written). `thought_sweep.py` cannot "
        "see this -- it only checks the link block exists, never that its targets are real."
    )
    lines.append("")
    if not stage1:
        lines.append("- _none -- every `Processed in:` claim reference resolves._")
    else:
        for f in stage1:
            lines.append(f"- `{f.file}` -- broken: {', '.join(f.broken_ids)}")
    lines.append("")
    lines.append("## Stage 2 (structured analysis, evidence/planning/thought_intake_*.md)")
    lines.append("")
    lines.append("| metric | count |")
    lines.append("|---|---|")
    lines.append(f"| total structured intakes | {len(stage2)} |")
    lines.append(f"| orphaned / explicitly unregistered | {len(orphans)} |")
    lines.append(f"| candidate section present, no IDs named (needs a human read) | {len(needs_read)} |")
    lines.append(f"| all named candidate IDs registered | {len(all_registered)} |")
    lines.append(f"| no candidate-claims section (nothing to check) | {len(no_section)} |")
    lines.append("")
    lines.append("### Orphaned / unregistered -- action needed")
    lines.append("")
    if not orphans:
        lines.append("- _none_")
    else:
        for r in orphans:
            if r.classification == "not_registered_no_ids":
                lines.append(f"- `{r.file}` -- explicit \"not registered\" prose, no concrete IDs named yet")
            else:
                lines.append(
                    f"- `{r.file}` -- named {r.ids_named}, MISSING from claims.yaml: {r.missing_ids}"
                )
    lines.append("")
    lines.append("### Needs a human read -- candidate section present, no ID to check")
    lines.append("")
    if not needs_read:
        lines.append("- _none_")
    else:
        for r in needs_read:
            lines.append(f"- `{r.file}`")
    lines.append("")
    lines.append(
        "Caveat: this audit only catches candidates that were given a claim-shaped ID (real or "
        "placeholder). A file with no 'Candidate claims'-style header at all is assumed to have "
        "nothing pending (per the README, some intakes are folded directly into canonical docs "
        "with no separate candidate list) -- that assumption is not independently verified here."
    )

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ground-truth audit of both thought-intake paths.")
    default_thoughts_root = Path(__file__).resolve().parents[1]
    default_assembly_root = default_thoughts_root.parents[1]
    parser.add_argument("--thoughts-root", type=Path, default=default_thoughts_root)
    parser.add_argument(
        "--planning-root", type=Path, default=default_assembly_root / "evidence" / "planning"
    )
    parser.add_argument(
        "--claims-yaml", type=Path, default=default_assembly_root / "docs" / "claims" / "claims.yaml"
    )
    parser.add_argument("--output-json", type=Path, default=None)
    parser.add_argument("--output-md", type=Path, default=None)
    parser.add_argument(
        "--check-clean",
        action="store_true",
        help="Exit non-zero if any Stage 1 broken link or Stage 2 orphan is found.",
    )
    args = parser.parse_args()

    thoughts_root = args.thoughts_root.resolve()
    planning_root = args.planning_root.resolve()
    claims_yaml = args.claims_yaml.resolve()
    output_json = args.output_json.resolve() if args.output_json else thoughts_root / "thought_intake_audit.v1.json"
    output_md = args.output_md.resolve() if args.output_md else thoughts_root / "INTAKE_AUDIT_REPORT.md"

    claim_ids = _load_claim_ids(claims_yaml)
    stage1 = _audit_stage1(thoughts_root, claim_ids)
    stage2 = _audit_stage2(planning_root, claim_ids)
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    _write_json(output_json, stage1, stage2, generated_at)
    _write_report(output_md, stage1, stage2, generated_at)

    orphan_classes = {"fully_orphaned", "partially_registered", "not_registered_no_ids"}
    orphan_count = sum(1 for r in stage2 if r.classification in orphan_classes)
    print(
        "Thought intake audit: "
        + f"stage1_broken_links={len(stage1)}, stage2_total={len(stage2)}, "
        + f"stage2_orphaned={orphan_count}, "
        + f"stage2_needs_read={sum(1 for r in stage2 if r.classification == 'no_ids_named')}"
    )

    if args.check_clean and (stage1 or orphan_count):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
