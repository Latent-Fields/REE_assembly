#!/usr/bin/env /opt/local/bin/python3
"""
check_backward_traceability.py -- Governance Proposal G2

Backward-traceability check: every claim that mentions developmental concepts
(by keyword match in its title or notes) should be referenced by at least one
row in the developmental_needs_register.md Claim IDs column.

Usage (from REE_assembly root):
    python scripts/check_backward_traceability.py           # exits non-zero if any WARNINGs
    python scripts/check_backward_traceability.py --warn-only  # informational; always exits 0

Exit codes:
    0  -- no untraced developmental claims (or --warn-only)
    1  -- one or more developmental claims lack a register row reference
"""

import argparse
import re
import sys
from pathlib import Path

CLAIMS_YAML = Path("docs/claims/claims.yaml")
REGISTER_MD = Path("docs/architecture/developmental_needs_register.md")

DEV_KEYWORDS = [
    "infant",
    "childhood",
    "play",
    "curriculum",
    "stage",
    "caregiver",
    "babbling",
    "pretend",
    "repertoire",
]

_CLAIM_ID_RE = re.compile(r"\b(INV|ARC|MECH|SD|Q|IMPL)-\d+[a-z]?\b")


def load_claims_yaml(path: Path) -> list:
    """Load claims from YAML. Returns list of dicts; each has at minimum 'id'."""
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
        sys.exit(2)

    raw = path.read_text(encoding="utf-8")
    docs = list(yaml.safe_load_all(raw))
    claims = []
    for doc in docs:
        if isinstance(doc, list):
            claims.extend(doc)
        elif isinstance(doc, dict) and "id" in doc:
            claims.append(doc)
    return claims


def extract_register_claim_ids(path: Path) -> set:
    """
    Parse developmental_needs_register.md and collect every claim ID
    found in the Claim IDs column (column index 3 in the pipe table).

    The register table has this column order:
      | Dev Need ID | Developmental Need | Stage | Claim IDs | ...
    Column index 0: Dev Need ID
    Column index 3: Claim IDs
    """
    text = path.read_text(encoding="utf-8")
    referenced = set()
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # Remove empty strings from split artefacts at start/end
        cells = [c for c in cells if c]
        if len(cells) < 4:
            continue
        # Skip header and separator rows
        claim_cell = cells[3]
        if claim_cell.startswith("-") or claim_cell.lower().startswith("claim"):
            continue
        for m in _CLAIM_ID_RE.finditer(claim_cell):
            referenced.add(m.group())
    return referenced


def claim_is_developmental(claim: dict) -> bool:
    """Return True if the claim's title or notes mention any developmental keyword."""
    haystack = " ".join([
        str(claim.get("title", "")),
        str(claim.get("notes", "")),
        str(claim.get("subject", "")),
    ]).lower()
    return any(kw in haystack for kw in DEV_KEYWORDS)


def main() -> int:
    parser = argparse.ArgumentParser(description="G2 backward traceability checker")
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Print warnings but always exit 0 (informational mode)",
    )
    args = parser.parse_args()

    if not CLAIMS_YAML.exists():
        print(
            "ERROR: {} not found. Run from REE_assembly root.".format(CLAIMS_YAML),
            file=sys.stderr,
        )
        return 2

    if not REGISTER_MD.exists():
        print(
            "ERROR: {} not found. Run from REE_assembly root.".format(REGISTER_MD),
            file=sys.stderr,
        )
        return 2

    claims = load_claims_yaml(CLAIMS_YAML)
    referenced = extract_register_claim_ids(REGISTER_MD)

    warnings = []
    for claim in claims:
        cid = claim.get("id", "")
        if not cid:
            continue
        status = claim.get("status", "")
        if status in ("retracted", "superseded", "retired"):
            continue
        if not claim_is_developmental(claim):
            continue
        if cid not in referenced:
            title = claim.get("title", "")[:80]
            warnings.append((cid, title))

    n_dev = sum(
        1 for c in claims
        if c.get("id") and c.get("status") not in ("retracted", "superseded", "retired")
        and claim_is_developmental(c)
    )

    print(
        "check_backward_traceability: {} developmental claim(s) found, "
        "{} register row(s) reference {} unique claim IDs".format(
            n_dev, len(referenced), len(referenced)
        )
    )

    if warnings:
        for cid, title in sorted(warnings):
            print("  WARNING: {} -- not referenced in register: {}".format(cid, title))
        print(
            "SUMMARY: {} developmental claim(s) lack a register row reference.".format(
                len(warnings)
            )
        )
    else:
        print("SUMMARY: all developmental claims are referenced in the register. OK")

    if warnings and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
