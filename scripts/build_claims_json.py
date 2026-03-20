#!/usr/bin/env python3
"""
Build docs/assets/data/claims.json from docs/claims/claims.yaml.

Run this any time claims.yaml is updated (add to governance pipeline).
Output is consumed by docs/assets/js/claim-tooltips.js for hover tooltips
on the GitHub Pages site.
"""
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "claims.json"


def main():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(1)

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
        output[claim_id] = {
            "type": claim.get("claim_type", ""),
            "subject": claim.get("subject", ""),
            "status": claim.get("status", ""),
            "title": claim.get("title", ""),
        }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Written {len(output)} claims → {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
