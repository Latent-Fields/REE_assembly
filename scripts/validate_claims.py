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

Flag-drift warnings (WARN-level, no exit effect):
  - pending_substrate_reconfirmation: true but all substrates in emergent_from
    are active -> flag is stale, can be cleared.
  - pending_substrate_reconfirmation: false/absent but at least one substrate
    in emergent_from is below active -> invariant should be flagged.
  The flag is a governance artifact, not an auto-derived value. Warnings
  surface drift between flag state and substrate status; governance decides.

Modes:
  --warn      (default) print issues, exit 0
  --strict    print issues, exit 1 if any ERROR (Session D default in governance.sh)
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

SUBSTRATE_CLAIM_TYPES = {
    "design_decision",
    "architectural_commitment",
    "architecture_hypothesis",
}

# Statuses that count as terminal-positive for the flag-drift check.
# 'implemented' is included per 2026-04-17 governance decision: SD-005 and other
# 'implemented' substrates are wired into the codebase and should not trigger
# pending_substrate_reconfirmation drift warnings. If governance later wants
# 'resolved' / 'validated' / 'stable' treated the same way, extend this set.
ACTIVE_EQUIVALENT_STATUSES = {"active", "implemented"}


def build_substrate_status_map(claims):
    """Return {substrate_id: status} for all substrate claims."""
    status_map = {}
    for c in claims:
        if not isinstance(c, dict):
            continue
        if c.get("claim_type") in SUBSTRATE_CLAIM_TYPES:
            sid = c.get("id")
            if sid:
                status_map[sid] = c.get("status", "unknown")
    return status_map


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


def validate_invariant(claim, substrate_status=None):
    """Return list of (level, msg) tuples for issues on one invariant.

    substrate_status: optional mapping {substrate_id: status} used for
    flag-drift warnings on `pending_substrate_reconfirmation`. If None,
    flag-drift checks are skipped.
    """
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

    # Flag-drift warnings: pending_substrate_reconfirmation vs substrate status.
    # Warnings only -- the flag is a governance artifact, not auto-derived.
    if substrate_status is not None and itype == "emergent" and efrom:
        flag_set = bool(claim.get("pending_substrate_reconfirmation"))
        substrate_statuses = [
            (s, substrate_status.get(s)) for s in efrom
        ]
        below_active = [
            (s, st) for s, st in substrate_statuses
            if st is not None and st not in ACTIVE_EQUIVALENT_STATUSES
        ]
        all_known_active = (
            substrate_statuses
            and all(st in ACTIVE_EQUIVALENT_STATUSES for _, st in substrate_statuses)
        )
        if flag_set and all_known_active:
            issues.append((
                "WARN",
                f"{cid}: flag is stale -- all substrates now active, "
                f"pending_substrate_reconfirmation can be cleared.",
            ))
        elif (not flag_set) and below_active:
            s, st = below_active[0]
            issues.append((
                "WARN",
                f"{cid}: should be flagged -- substrate {s} is {st}.",
            ))

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

    substrate_status = build_substrate_status_map(claims)
    all_issues = []
    for c in invariants:
        all_issues.extend(validate_invariant(c, substrate_status=substrate_status))

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
