#!/usr/bin/env python3
"""
Detect flat-only experiment manifests that are structurally invisible to
build_experiment_indexes.py -- a manifest with no matching run PACK.

THE DEFECT (found 2026-08-30 by failure_autopsy_966-436g-951-959-822d-cluster,
diagnosed in full 2026-09-01 while working chip-20260830-exq547-runid-index-
invisible). build_experiment_indexes.py's _scan_runs discovers evidence by a
SINGLE glob: `base_dir.glob("**/runs/**/manifest.json")` (build_experiment_
indexes.py:1731). A flat manifest at evidence/experiments/<run_id>.json is
read ONLY as a governance-annotation OVERLAY for an ALREADY-DISCOVERED pack
(_resolve_flat_sibling / _merge_flat_manifest_overrides, ~line 1774) -- never
as an independent discovery source. So a manifest written ONLY via pack_writer.
write_flat_manifest(), with no sibling runs/<experiment_type>/runs/<run_id>/
manifest.json ever created, is permanently invisible to claim_evidence.v1.json,
REGARDLESS of its run_id's naming convention (the original chip's hypothesis
-- that the "_v3" suffix sitting mid-string rather than at the end caused
this -- was checked and is FALSE: none of the 3 confirmed counter-examples in
the corpus with a mid-string "_v3" ARE visible when they lack a pack, and
renaming the run_id field alone would not change the glob-discovery outcome
at all).

write_flat_manifest is a DELIBERATE, sanctioned writer (pack_writer.py's own
docstring: "The single sanctioned writer for a FLAT V3 experiment manifest"),
used directly (no companion write_pack call) by an entire family of
"substrate-readiness diagnostic" scripts. So this is not a one-off data bug in
a single manifest -- it is a standing structural gap between a sanctioned
authoring path and the indexer's discovery path. See
evidence/planning/flat_only_manifest_indexer_invisibility_staged_20260901.md
for the full corpus scan, affected-claim table, and two candidate remediations
(indexer-side discovery of pack-less flat manifests, vs backfilling a run pack
per affected manifest) left for /governance to choose between -- deliberately
NOT decided or applied by this script, since either remediation would change
what counts as scored evidence for several claims (ARC-062, MECH-309,
MECH-313, ARC-065 have "supports"-direction flat-only orphans right now) and
that is a scoring-semantics call, not a mechanical one.

THIS SCRIPT is the retrospective-and-CI-facing detection half only (mirrors
check_run_id_letter_hygiene.py's own split between detection and fix). It is
READ-ONLY: it writes nothing, commits nothing, and does not touch
claim_evidence.v1.json or any manifest.

WHAT COUNTS AS A FINDING. A flat manifest at evidence/experiments/<run_id>.json
(or evidence/experiments/<experiment_type>/<run_id>.json) such that:
  - it is NOT a --dry-run smoke (no truthy top-level dry_run, and the filename
    does not carry the `_dry_` / `..._dry` convention that also marks a smoke
    -- mirrors build_experiment_indexes._is_dry_run / _load_dry_run_run_ids);
  - it resolves a real status via the same precedence pack_writer._resolve_
    flat_status uses (status | overall_outcome | outcome), i.e. it is not a
    stub;
  - no runs/<any experiment_type>/runs/<run_id>/manifest.json exists anywhere
    under evidence/experiments/.

USAGE
-----
    python3 scripts/audit_flat_only_orphaned_manifests.py            # summary, exit 0/1
    python3 scripts/audit_flat_only_orphaned_manifests.py --list     # print every finding

Exit codes:
    0  no findings
    1  one or more flat-only orphaned manifests found
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"

# Filenames at the top of evidence/experiments/ that are indexes/reports, not
# manifests -- must not be read as one.
_NON_MANIFEST_NAMES = {
    "claim_evidence.v1.json",
}


def _load_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _is_dry_run(manifest: dict[str, Any], path: Path) -> bool:
    if str(manifest.get("dry_run", "")).strip().lower() in ("true", "1", "yes"):
        return True
    stem = path.stem
    return stem.startswith("_dry_") or stem.endswith("_dry")


def _resolve_flat_status(manifest: dict[str, Any]) -> str | None:
    for key in ("status", "overall_outcome", "outcome", "result"):
        val = manifest.get(key)
        if val not in (None, ""):
            return str(val)
    return None


def find_flat_only_orphans(evidence_dir: Path) -> list[dict[str, Any]]:
    pack_run_ids: set[str] = set()
    for manifest_path in evidence_dir.glob("**/runs/**/manifest.json"):
        run_dir = manifest_path.parent
        if run_dir.parent.name != "runs":
            continue
        pack_run_ids.add(run_dir.name)
        pm = _load_json(manifest_path)
        if pm:
            rid = pm.get("run_id")
            if isinstance(rid, str) and rid.strip():
                pack_run_ids.add(rid.strip())

    findings: list[dict[str, Any]] = []
    flat_paths = sorted(evidence_dir.glob("*.json")) + sorted(
        evidence_dir.glob("*/[!_]*.json")
    )
    seen_paths: set[Path] = set()
    for path in flat_paths:
        if path in seen_paths:
            continue
        seen_paths.add(path)
        if path.name in _NON_MANIFEST_NAMES:
            continue
        if "runs" in path.parts:
            continue
        manifest = _load_json(path)
        if manifest is None:
            continue
        run_id = manifest.get("run_id")
        if not isinstance(run_id, str) or not run_id.strip():
            continue
        run_id = run_id.strip()
        if run_id in pack_run_ids:
            continue
        if _is_dry_run(manifest, path):
            continue
        status = _resolve_flat_status(manifest)
        if status is None:
            continue
        findings.append({
            "path": str(path.relative_to(ROOT.parent)),
            "run_id": run_id,
            "status": status,
            "experiment_purpose": manifest.get("experiment_purpose"),
            "evidence_direction": manifest.get("evidence_direction"),
            "claim_ids": manifest.get("claim_ids") or [],
        })
    findings.sort(key=lambda f: f["run_id"])
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--list", action="store_true",
                     help="print every finding (default: summary only)")
    args = ap.parse_args(argv)

    findings = find_flat_only_orphans(EVIDENCE_DIR)

    if not findings:
        print("no flat-only orphaned manifests found -- clean")
        return 0

    print(f"{len(findings)} flat-only orphaned manifest(s) found "
          f"(a real result, no matching run pack -- invisible to "
          f"claim_evidence.v1.json regardless of run_id naming):")
    contributory = [
        f for f in findings
        if f["claim_ids"] and f["evidence_direction"] in
        ("supports", "does_not_support", "weakens")
    ]
    if contributory:
        print(f"  {len(contributory)} carry a scoring-relevant "
              f"evidence_direction and non-empty claim_ids -- these change "
              f"claim confidence if/when made visible:")
        for f in contributory:
            print(f"    {f['run_id']}  {f['evidence_direction']}  "
                  f"claims={f['claim_ids']}")
    if args.list:
        print()
        for f in findings:
            print(f"  run_id={f['run_id']}")
            print(f"    path={f['path']}")
            print(f"    status={f['status']} purpose={f['experiment_purpose']} "
                  f"evidence_direction={f['evidence_direction']} "
                  f"claim_ids={f['claim_ids']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
