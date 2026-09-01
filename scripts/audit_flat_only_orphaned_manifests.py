#!/usr/bin/env python3
"""
Detect flat-only experiment manifests that are STILL structurally invisible to
build_experiment_indexes.py after the 2026-09-01 discovery fix -- i.e. ones the
indexer's own flat-only-orphan path cannot resolve an experiment_type for.

THE DEFECT (found 2026-08-30 by failure_autopsy_966-436g-951-959-822d-cluster,
diagnosed in full 2026-09-01 while working chip-20260830-exq547-runid-index-
invisible) was that build_experiment_indexes.py's _scan_runs discovered
evidence by a SINGLE glob, `base_dir.glob("**/runs/**/manifest.json")`, so a
manifest written ONLY via pack_writer.write_flat_manifest() (no sibling
runs/<experiment_type>/runs/<run_id>/manifest.json ever created) was
permanently invisible to claim_evidence.v1.json regardless of its run_id's
naming convention. GFLAG-0111 (evidence_discrepancy, raised 2026-09-01) named
the 9 claims (ARC-062, MECH-309, MECH-313, ARC-065, MECH-220, SD-015,
MECH-112, ARC-030, SD-012) whose confidence this changes.

FIXED 2026-09-01 (chip-20260901-indexer-flatonly-discovery): build_experiment_
indexes.py now discovers a flat-only manifest DIRECTLY, via
`_collect_pack_run_ids` + `_scan_flat_only_orphans`, scoring it from the flat
file itself when no pack exists anywhere for its run_id. That path infers
`experiment_type` from the manifest's own field, falling back to the flat
file's parent directory name -- and skips the manifest (uncounted) only when
NEITHER is available (i.e. the file sits directly at evidence/experiments/
top level AND carries no `experiment_type` field at all). See
evidence/planning/flat_only_manifest_indexer_invisibility_staged_20260901.md
for the corpus scan this was diagnosed from, and note the resulting confidence
/ evidence_quadrant movement (including an evidence_quadrant flip for
MECH-112, confirmed_established -> plausible_unproven) is a governance
disposition applied by /governance's own regen cycle, not by this fix or by
this script.

THIS SCRIPT, post-fix, mirrors that SAME experiment_type-inference logic
(kept in sync by hand -- see build_experiment_indexes._scan_flat_only_orphans)
so that "finding" now means "genuinely still un-scorable", not merely
"packless". It is the retrospective-and-CI-facing detection half only
(mirrors check_run_id_letter_hygiene.py's own split between detection and
fix). It is READ-ONLY: it writes nothing, commits nothing, and does not touch
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
    under evidence/experiments/ for its run_id;
  - AND no `experiment_type` is inferable (neither an explicit field nor a
    parent directory to fall back to) -- i.e. the indexer's own discovery
    path would skip it too.

USAGE
-----
    python3 scripts/audit_flat_only_orphaned_manifests.py            # summary, exit 0/1
    python3 scripts/audit_flat_only_orphaned_manifests.py --list     # print every finding

Exit codes:
    0  no findings
    1  one or more flat-only manifests found that the indexer still cannot score
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
        # Mirrors build_experiment_indexes.py's own flat-only-orphan discovery
        # loop: experiment_type from the manifest field, falling back to the
        # flat file's parent directory name when the file is not sitting
        # directly at evidence_dir's top level. Only a manifest for which
        # NEITHER resolves is still genuinely un-scorable post-fix.
        experiment_type = str(manifest.get("experiment_type", "")).strip()
        if not experiment_type and path.parent != evidence_dir:
            experiment_type = path.parent.name
        if experiment_type:
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
        print("no flat-only orphaned manifests found -- clean "
              "(the indexer's own flat-only-orphan path, added 2026-09-01, "
              "resolves an experiment_type for every packless flat manifest "
              "currently on disk)")
        return 0

    print(f"{len(findings)} flat-only manifest(s) found that the indexer "
          f"STILL cannot score (no matching run pack AND no experiment_type "
          f"inferable, neither an explicit field nor a parent directory):")
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
