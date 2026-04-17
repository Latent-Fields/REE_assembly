#!/usr/bin/env python3
"""
Build docs/assets/data/claims.json from docs/claims/claims.yaml.

Run this any time claims.yaml is updated (add to governance pipeline).
Output is consumed by docs/assets/js/claim-tooltips.js for hover tooltips
on the GitHub Pages site.

Runs scripts/validate_claims.py in warn-only mode before emitting JSON.
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "claims.json"
VALIDATOR = Path(__file__).parent / "validate_claims.py"


def run_validator():
    if not VALIDATOR.exists():
        return
    subprocess.run([sys.executable, str(VALIDATOR)], check=False)


def main():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(1)

    run_validator()

    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f)

    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(1)

    output = {}
    for claim in claims:
        claim_id = claim.get("id")
        if not claim_id:
            continue
        entry = {
            "type": claim.get("claim_type", ""),
            "subject": claim.get("subject", ""),
            "status": claim.get("status", ""),
            "title": claim.get("title", ""),
        }
        if claim.get("claim_type") == "invariant":
            itype = claim.get("invariant_type")
            if itype is not None:
                entry["invariant_type"] = itype
            efrom = claim.get("emergent_from") or []
            if efrom:
                entry["emergent_from"] = list(efrom)
            if claim.get("pending_substrate_reconfirmation"):
                entry["pending_substrate_reconfirmation"] = True
        output[claim_id] = entry

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Written {len(output)} claims -> {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
