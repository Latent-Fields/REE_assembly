#!/usr/bin/env python3
"""Validate brain_region_map.yaml against claims.yaml and brain_map_sagittal.svg."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
MAP_FILE = ROOT / "docs" / "architecture" / "brain_region_map.yaml"
SVG_FILE = ROOT / "docs" / "architecture" / "brain_map_sagittal.svg"
CLAIMS_FILE = ROOT / "docs" / "claims" / "claims.yaml"


def load_claim_prefixes() -> set[str]:
    raw = yaml.safe_load(CLAIMS_FILE.read_text(encoding="utf-8"))
    claims = raw.get("claims", raw) if isinstance(raw, dict) else (raw or [])
    prefs: set[str] = set()
    for c in claims:
        if not isinstance(c, dict):
            continue
        sub = str(c.get("subject") or "")
        if sub:
            prefs.add(sub.split(".")[0])
    return prefs


def svg_ids() -> set[str]:
    text = SVG_FILE.read_text(encoding="utf-8")
    return set(re.findall(r'\bid="([^"]+)"', text))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not MAP_FILE.exists():
        print(f"ERROR: missing {MAP_FILE}", file=sys.stderr)
        return 1
    if not SVG_FILE.exists():
        print(f"ERROR: missing {SVG_FILE}", file=sys.stderr)
        return 1

    map_doc = yaml.safe_load(MAP_FILE.read_text(encoding="utf-8")) or {}
    known = set(map_doc.get("known_anatomy_prefixes") or [])
    ids_in_svg = svg_ids()

    prefix_owner: dict[str, str] = {}
    all_svg_refs: list[str] = []

    for bucket in ("regions", "engineering_nodes"):
        for node in map_doc.get(bucket) or []:
            nid = str(node.get("id") or "")
            for pref in node.get("subject_prefixes") or []:
                pref = str(pref)
                if pref in prefix_owner and prefix_owner[pref] != nid:
                    errors.append(
                        f"duplicate prefix '{pref}': {prefix_owner[pref]} and {nid}"
                    )
                prefix_owner[pref] = nid
            for pid in node.get("svg_path_ids") or []:
                all_svg_refs.append(str(pid))
                if str(pid) not in ids_in_svg:
                    errors.append(f"svg path id '{pid}' (region {nid}) not in SVG")

    claim_prefs = load_claim_prefixes()
    for pref in sorted(claim_prefs):
        if pref in known and pref not in prefix_owner:
            warnings.append(f"known anatomy prefix '{pref}' has no region mapping")

    orphan_svg = ids_in_svg - set(all_svg_refs) - {
        "silhouette_outline",
        "ghost_hatch",
        "silhouette_stroke",
        "engineering_strip",
        "pathway_overlay",
    }
    for oid in sorted(orphan_svg):
        if oid.startswith("region_") or oid.startswith("node_"):
            warnings.append(f"SVG id '{oid}' not referenced in brain_region_map.yaml")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        return 1
    n_regions = len(map_doc.get("regions") or [])
    n_eng = len(map_doc.get("engineering_nodes") or [])
    print(f"OK: brain region map valid ({n_regions} regions, {n_eng} engineering nodes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
