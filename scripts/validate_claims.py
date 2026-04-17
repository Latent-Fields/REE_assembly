#!/usr/bin/env python3
"""
Validate docs/claims/claims.yaml schema.

Currently enforces the invariant-type schema introduced 2026-04-17:
  - invariant_type is mandatory on every claim_type: invariant entry
  - invariant_type must be one of: universal | emergent | grey_zone
  - emergent_from must be non-empty when invariant_type == emergent
  - emergent_from must be empty or absent when invariant_type == universal
  - emergent_from must be a subset of depends_on
  - grey_zone entries pass regardless of emergent_from content

Modes:
  --warn      (default) print issues, exit 0
  --strict    print issues, exit 1 if any ERROR
  --audit     print classification counts only (no validation)

Called at the top of build_claims_json.py and governance.sh.
See docs/architecture/invariant_types.md for schema semantics.
"""
import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

VALID_INVARIANT_TYPES = {"universal", "emergent", "grey_zone"}


def load_claims():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(2)
    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f)
    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(2)
    return claims


def validate_invariant(claim):
    """Return list of (level, msg) tuples for issues on one invariant."""
    issues = []
    cid = claim.get("id", "<no-id>")
    itype = claim.get("invariant_type")
    efrom = claim.get("emergent_from") or []
    depends_on = claim.get("depends_on") or []

    if itype is None:
        issues.append(("ERROR", f"{cid}: missing invariant_type (universal | emergent | grey_zone)"))
        return issues

    if itype not in VALID_INVARIANT_TYPES:
        issues.append(("ERROR", f"{cid}: invariant_type='{itype}' invalid; must be one of {sorted(VALID_INVARIANT_TYPES)}"))
        return issues

    if itype == "emergent":
        if not efrom:
            issues.append(("ERROR", f"{cid}: invariant_type=emergent requires non-empty emergent_from"))
        else:
            missing = [s for s in efrom if s not in depends_on]
            if missing:
                issues.append(("ERROR", f"{cid}: emergent_from {missing} not in depends_on"))
    elif itype == "universal":
        if efrom:
            issues.append(("ERROR", f"{cid}: invariant_type=universal must have empty/absent emergent_from (found {efrom})"))
    # grey_zone: permissive, no constraint on emergent_from / candidate_emergent_from

    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 on any ERROR")
    ap.add_argument("--audit", action="store_true", help="print classification counts only")
    args = ap.parse_args()

    claims = load_claims()
    invariants = [c for c in claims if c.get("claim_type") == "invariant"]

    if args.audit:
        counts = {"universal": 0, "emergent": 0, "grey_zone": 0, "unclassified": 0}
        for c in invariants:
            t = c.get("invariant_type")
            if t in counts:
                counts[t] += 1
            else:
                counts["unclassified"] += 1
        print(f"Total invariants: {len(invariants)}")
        for k, v in counts.items():
            print(f"  {k}: {v}")
        return 0

    all_issues = []
    for c in invariants:
        all_issues.extend(validate_invariant(c))

    errors = [msg for lvl, msg in all_issues if lvl == "ERROR"]
    warnings = [msg for lvl, msg in all_issues if lvl == "WARN"]

    if not all_issues:
        print(f"validate_claims: OK ({len(invariants)} invariants checked)")
        return 0

    mode = "strict" if args.strict else "warn-only"
    print(f"validate_claims [{mode}]: {len(errors)} error(s), {len(warnings)} warning(s) across {len(invariants)} invariants")
    for msg in errors:
        print(f"  ERROR: {msg}")
    for msg in warnings:
        print(f"  WARN: {msg}")

    if args.strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
