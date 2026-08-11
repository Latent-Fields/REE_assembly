#!/usr/bin/env python3
"""Substrate-path overlap audit (governance Step 3k, GOV-SUBPATH-1).

The EIGHTH sibling of the governance standing scans, and the backward half of
the `/queue-experiment` Step 2.5c consumer gate:

  * GOV-CEIL-1     (check_substrate_ceiling_audit.py)        -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1     (check_diagnostic_chain_recurrence.py)    -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1     (check_granularity_debt_recurrence.py)    -- >=N structurally-different failures
  * GOV-CAT-1      (check_epistemic_category_completeness.py)-- the verdict was never RECORDED
  * GOV-APPLY-1    (check_unapplied_autopsy_recommendations.py) -- the verdict was never APPLIED
  * GOV-DRY-1      (check_dry_run_adjudication_leak.py)      -- the verdict rests on a SMOKE
  * GOV-SKILL-1    (check_skill_improvement_recurrence.py)   -- a LESSON keeps recurring, unabsorbed
  * GOV-SUBPATH-1  (this file)                                -- evidence ran against KNOWN-BAD CODE

WHY THIS AUDIT EXISTS. Every existing gate that stops an experiment from
running against known-bad substrate is keyed to the CLAIM the current
experiment is testing: `/queue-experiment` Step 2.5/2.5b check whether *this
experiment's own target SD* is built and hasn't already ceilinged; GOV-CEIL-1
and GOV-DIAG-1 count recurrence against *the claims an autopsy tagged*. None
of them ask whether a driver script imports a code path some OTHER,
unrelated claim's `/failure-autopsy` already flagged as broken -- because
`substrate_queue.json`'s `unblocks_claims` is claim-scoped, not code-scoped.
Design: `evidence/planning/substrate_defect_gate_plan_2026-08-07.md`.

Two new `substrate_queue.json` fields close the gap: `severity`
(`corrupting` / `degrading` / `cosmetic` -- how dangerous the defect is to
evidence quality) and `substrate_paths` (the repo-relative file(s), relative
to `ree-v3/`, the defect actually lives in). `/failure-autopsy` Step 7 fills
both when it recommends a `substrate_queue` entry. `/queue-experiment` Step
2.5c is the FORWARD half -- it stops a NEW experiment from being queued
against an open `corrupting` entry's `substrate_paths`. This script is the
BACKWARD half: it finds evidence that ALREADY ran against such substrate,
even when that evidence belongs to a claim the flagging autopsy never
mentioned, so nothing else would ever surface it.

WHAT THIS DOES (read-only; never edits a manifest or substrate_queue.json)
----------------------------------------------------------------------------
1. Loads every still-OPEN `severity: corrupting` entry from
   `evidence/planning/substrate_queue.json` (an entry with no `substrate_paths`
   is skipped -- there is nothing to match against). "Open" mirrors the
   `/queue-experiment` Step 2.5c rule: `implementation_status` / `status` does
   not read `implemented` / `implemented_validated` / `validated` / a
   `wontfix`-equivalent. Ambiguous reads as OPEN -- this gate fails toward
   surfacing a candidate, not toward silence, matching every sibling scan's
   posture on an unparseable/absent field.

   An entry with NO `added_utc` (or one that doesn't parse to a timestamp) is
   the one exception to that "ambiguous -> surface it" posture: `added_utc` is
   the ONLY thing that stops step 4 below from matching every completed run
   ever recorded, so a missing value would flood the report with hundreds of
   false "may need re-review" hits rather than surfacing a real signal --
   confirmed live on 2026-08-10 (see `substrate_defect_gate_plan_2026-08-07.md`
   and the SD-ORIENTING-DECISION-SCALE incident). Unlike the openness check
   above, this failure mode has real cost to false positives, not just
   under-coverage, so it fails the OTHER direction: the entry is excluded from
   gating (reported separately as `entries_missing_added_utc`, with a loud
   warning on stdout and, under `--strict`, a non-zero exit) rather than
   silently matching everything.
2. Builds the manifest index via `check_dry_run_citations.build_index()`
   (never re-implemented -- see that module for why a second copy is how the
   forms drift), which gives `{run_id: {experiment_type, dry_run, paths, ...}}`
   over BOTH flat and `runs/<run_id>/manifest.json` pack manifests. Dry runs
   are excluded (a smoke is never evidence -- GOV-DRY-1's lane, not this one's).
3. For each qualifying run, resolves its driver script
   `ree-v3/experiments/<experiment_type>.py` (current on-disk copy -- this is a
   "does the CURRENT driver still touch this" report, not a historical
   at-commit reconstruction like check_substrate_staleness_candidates.py; see
   "Deliberately simpler" below) and parses its `import` / `from ... import`
   statements via `ast` into a set of dotted module names.
4. A run_id is a CANDIDATE for a corrupting entry when: the entry's
   `substrate_paths` (converted file-path -> dotted module, `::function`
   suffix stripped -- matching is MODULE granularity, not function granularity)
   overlaps the driver's imported modules, AND the run's own timestamp (parsed
   from the run_id's embedded `YYYYMMDDTHHMMSSZ` stamp -- always present, see
   `check_dry_run_citations.RUN_ID_RE`) is AFTER the entry's `added_utc`.
   A run at or before `added_utc` could not have been warned by this entry and
   is not reported (the defect wasn't on record yet).

Deliberately simpler than `check_substrate_staleness_candidates.py`
---------------------------------------------------------------------
That script reconstructs a driver's source AT THE RECORDED COMMIT via a
throwaway git worktree, because it is answering "did the substrate change
under this specific run since it recorded its hash." This script asks a
narrower question -- "does the CURRENT driver still import a path a defect
review needs re-checked" -- so it reads the driver straight off the working
tree with no git archaeology. The cost of that simplicity: a driver script
that has since been rewritten to no longer import the flagged path will stop
appearing here even though the RUN in question still exercised the old
import at execution time. That is an acceptable false-negative for a
warn-only "candidates for re-review" report (the run's own manifest is the
ground truth of what actually happened; this script is a discovery aid, not
an audit of record) -- if this ever needs to be exact, follow
check_substrate_staleness_candidates.py's worktree-at-commit pattern instead
of reimplementing it here.

MATCHING IS MODULE-GRANULARITY, DELIBERATELY CONSERVATIVE
-------------------------------------------------------------
A `substrate_paths` entry naming `pkg/mod.py::some_function` still matches
ANY driver that imports `pkg.mod`, not only one that references
`some_function` by name -- the same "over-inclusive is safe, under-inclusive
hides a real corruption" posture `check_substrate_staleness_candidates.py`
states for its own scope declarations. A driver is matched if it imports the
target module directly (`import pkg.mod`, `from pkg import mod`, `from
pkg.mod import thing`) or imports a module INSIDE a target package path (a
`substrate_paths` entry naming a package rather than a single file).

This audit READS ONLY. It promotes/demotes nothing, edits no manifest, and
does not touch `substrate_queue.json`. Every re-review it recommends is a
human's / governance's call. It is WARN-ONLY and always exits 0 unless
`--strict`.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_substrate_path_overlap.py
    /opt/local/bin/python3 scripts/check_substrate_path_overlap.py --strict
    /opt/local/bin/python3 scripts/check_substrate_path_overlap.py --json
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent  # REE_assembly root
DEFAULT_SUBSTRATE_QUEUE = REPO_ROOT / "evidence" / "planning" / "substrate_queue.json"
DEFAULT_REE_V3_ROOT = REPO_ROOT.parent / "ree-v3"

# Reuse the dry-run guard's manifest index. Do NOT re-implement it here -- that
# module already imports the single `_is_dry_run` from generate_pending_review.py,
# and a second copy is how the forms drift (same rationale check_dry_run_
# adjudication_leak.py states for the same import).
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from check_dry_run_citations import RUN_ID_RE, build_index  # noqa: E402
except ImportError as exc:  # pragma: no cover - environment problem, be loud
    raise SystemExit(
        "cannot import from scripts/check_dry_run_citations.py: %s" % exc
    )

# implementation_status / status substrings that mean an entry is CLOSED (no
# longer a live gate). Substring match, case-insensitive -- the `status` field
# in this file is heavily free-text (confirmed: dozens of distinct long-form
# values), so an exact-value enum would miss most real closures. Ambiguous
# reads as OPEN (the safe direction for a corrupting-severity gate).
_CLOSED_MARKERS = (
    "implemented_validated",
    "implemented",
    "validated",
    "wontfix",
    "closed_aleatoric",
)

_TIMESTAMP_RE = re.compile(r"(\d{8}T\d{6}Z)")


def _entry_is_open(entry: Dict[str, Any]) -> bool:
    """Mirrors the /queue-experiment Step 2.5c 'open' rule -- see module docstring."""
    s1 = str(entry.get("implementation_status") or "").lower()
    s2 = str(entry.get("status") or "").lower()
    return not any(marker in s1 or marker in s2 for marker in _CLOSED_MARKERS)


def _module_from_path(path: str) -> Optional[str]:
    """'ree_core/predictors/e3_selector.py' -> 'ree_core.predictors.e3_selector'.
    Strips an optional '::function' suffix (matching is module-granularity --
    see module docstring). None for anything that doesn't look like a .py path.
    """
    bare = path.split("::", 1)[0].strip()
    if not bare.endswith(".py"):
        return None
    dotted = bare[: -len(".py")].replace("/", ".").strip(".")
    return dotted or None


def load_corrupting_entries(
    queue_path: Path,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Optional[str]]:
    """Return (entries, entries_missing_added_utc, error).

    entries is [] on any load problem (never a crash). An open
    severity=corrupting entry that otherwise qualifies (has substrate_paths)
    but carries no parseable `added_utc` is NOT included in `entries` -- see
    the module docstring's "one exception" paragraph -- and instead appears
    in `entries_missing_added_utc` so the caller can warn loudly instead of
    silently gating against every completed run.
    """
    try:
        data = json.loads(queue_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [], [], "cannot read %s: %s" % (queue_path, exc)
    if not isinstance(data, dict):
        return [], [], "%s did not parse to a JSON object" % queue_path
    out: List[Dict[str, Any]] = []
    missing_added_utc: List[Dict[str, Any]] = []
    for entry in data.get("queue") or []:
        if not isinstance(entry, dict):
            continue
        if str(entry.get("severity") or "").strip().lower() != "corrupting":
            continue
        paths = entry.get("substrate_paths") or []
        if not isinstance(paths, list) or not paths:
            continue
        if not _entry_is_open(entry):
            continue
        modules = {m for m in (_module_from_path(p) for p in paths) if m}
        if not modules:
            continue
        added_utc = str(entry.get("added_utc") or "")
        if _added_utc_compact(added_utc) is None:
            missing_added_utc.append({
                "sd_id": entry.get("sd_id"),
                "title": entry.get("title"),
                "substrate_paths": list(paths),
            })
            continue
        out.append({
            "sd_id": entry.get("sd_id"),
            "title": entry.get("title"),
            "substrate_paths": list(paths),
            "modules": modules,
            "added_utc": added_utc,
        })
    return out, missing_added_utc, None


def _run_timestamp(run_id: str) -> Optional[str]:
    """The embedded YYYYMMDDTHHMMSSZ stamp, or None if run_id carries none."""
    m = _TIMESTAMP_RE.search(run_id)
    return m.group(1) if m else None


def _added_utc_compact(added_utc: str) -> Optional[str]:
    """'2026-08-03T12:00:00Z' -> '20260803T120000Z', in the SAME 'YYYYMMDD' +
    'T' + 'HHMMSS' + 'Z' shape _run_timestamp() extracts from a run_id, so the
    two are directly string-comparable. None if added_utc doesn't parse."""
    digits = re.sub(r"[^0-9]", "", added_utc)
    if len(digits) < 14:
        return None
    return "%sT%sZ" % (digits[:8], digits[8:14])


def _driver_path(ree_v3_root: Path, experiment_type: Optional[str]) -> Optional[Path]:
    if not experiment_type:
        return None
    p = ree_v3_root / "experiments" / ("%s.py" % experiment_type)
    return p if p.is_file() else None


def resolve_driver_imports(source: str) -> Set[str]:
    """Every dotted module name this driver source imports, from both `import
    a.b.c` and `from a.b import c` forms (the latter also yields the bare
    module 'a.b', so a target naming the module itself still matches a
    from-import of one of its names). Best-effort: unparseable source yields
    the empty set, never a crash.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()
    out: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                out.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level:  # relative import -- not used by ree_core/coordinator drivers
                continue
            module = node.module
            if not module:
                continue
            out.add(module)
            for alias in node.names:
                if alias.name == "*":
                    continue
                out.add("%s.%s" % (module, alias.name))
    return out


def _modules_overlap(target_modules: Set[str], imported: Set[str]) -> bool:
    for target in target_modules:
        for imp in imported:
            if imp == target:
                return True
            if imp.startswith(target + "."):
                return True
            if target.startswith(imp + "."):
                return True
    return False


def scan(
    queue_path: Path = DEFAULT_SUBSTRATE_QUEUE,
    ree_v3_root: Path = DEFAULT_REE_V3_ROOT,
) -> Dict[str, Any]:
    entries, entries_missing_added_utc, load_error = load_corrupting_entries(queue_path)
    if load_error:
        return {"load_error": load_error, "entries": [], "candidates": [],
                "entries_missing_added_utc": [], "n_entries": 0,
                "n_runs_scanned": 0, "n_candidates": 0}

    by_run, _by_queue = build_index()
    n_scanned = 0
    driver_import_cache: Dict[str, Set[str]] = {}
    candidates: List[Dict[str, Any]] = []

    for run_id, rec in sorted(by_run.items()):
        if rec.get("dry_run"):
            continue  # a smoke is never evidence -- GOV-DRY-1's lane
        stamp = _run_timestamp(run_id)
        if not stamp:
            continue
        experiment_type = rec.get("experiment_type")
        if experiment_type not in driver_import_cache:
            driver_path = _driver_path(ree_v3_root, experiment_type)
            if driver_path is None:
                driver_import_cache[experiment_type] = set()
            else:
                try:
                    source = driver_path.read_text(encoding="utf-8")
                except OSError:
                    source = ""
                driver_import_cache[experiment_type] = resolve_driver_imports(source)
        imported = driver_import_cache[experiment_type]
        if not imported:
            continue
        n_scanned += 1

        for entry in entries:
            # load_corrupting_entries() already excludes anything whose
            # added_utc doesn't parse (see entries_missing_added_utc), so
            # added_compact is never None here -- this call is belt-and-
            # suspenders, not the gate itself.
            added_compact = _added_utc_compact(entry["added_utc"])
            if added_compact is not None and stamp <= added_compact:
                continue  # ran at/before the defect was recorded -- not a candidate
            if not _modules_overlap(entry["modules"], imported):
                continue
            candidates.append({
                "run_id": run_id,
                "experiment_type": experiment_type,
                "sd_id": entry["sd_id"],
                "sd_title": entry["title"],
                "substrate_paths": entry["substrate_paths"],
                "added_utc": entry["added_utc"],
                "run_timestamp": stamp,
                "manifest_paths": rec.get("paths"),
            })

    return {
        "load_error": None,
        "entries": [{"sd_id": e["sd_id"], "title": e["title"],
                      "substrate_paths": e["substrate_paths"]} for e in entries],
        "candidates": candidates,
        "entries_missing_added_utc": entries_missing_added_utc,
        "n_entries": len(entries),
        "n_runs_scanned": n_scanned,
        "n_candidates": len(candidates),
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--substrate-queue", type=Path, default=DEFAULT_SUBSTRATE_QUEUE,
                    help="substrate_queue.json to read")
    ap.add_argument("--ree-v3-root", type=Path, default=DEFAULT_REE_V3_ROOT,
                    help="ree-v3 checkout to resolve driver scripts against")
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any candidate is found, or if any open "
                         "corrupting entry is missing a parseable added_utc")
    args = ap.parse_args()

    result = scan(args.substrate_queue, args.ree_v3_root)
    n = result["n_candidates"]
    missing = result["entries_missing_added_utc"]

    if args.as_json:
        json.dump(result, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 1 if (args.strict and (n or missing)) else 0

    if result["load_error"]:
        print("Substrate-path overlap audit (GOV-SUBPATH-1): %s" % result["load_error"])
        return 0

    print("Substrate-path overlap audit (GOV-SUBPATH-1): %d open severity=corrupting "
          "entr%s with a recorded code footprint, %d run(s) scanned"
          % (result["n_entries"], "y" if result["n_entries"] == 1 else "ies",
             result["n_runs_scanned"]))

    if missing:
        print("\nWARNING -- %d open severity=corrupting entr%s substrate_paths but NO "
              "parseable added_utc, so this audit CANNOT gate against %s and skipped "
              "it entirely (a missing added_utc would otherwise match every completed "
              "run ever recorded -- see module docstring). Backfill added_utc on:"
              % (len(missing), "y has" if len(missing) == 1 else "ies have",
                 "it" if len(missing) == 1 else "them"))
        for e in missing:
            print("  - %s (%s) -- %s" % (e["sd_id"], e["title"], e["substrate_paths"]))

    if not result["n_entries"]:
        if missing:
            print("\n  -- 0 gate-able entries (see WARNING above); nothing else to scan.")
        else:
            print("\n  -- no open severity=corrupting substrate_queue entry carries "
                  "substrate_paths (healthy, or the field is not yet populated).")
        return 1 if (args.strict and missing) else 0

    if not n:
        print("\n  -- no completed, non-dry run's driver imports a flagged path "
              "after its entry's added_utc.")
        return 1 if (args.strict and missing) else 0

    print("\nACTIONABLE -- these runs completed AFTER a substrate_queue entry recorded a")
    print("corrupting defect in a module their own driver imports. Evidence, not just")
    print("the originating claim's evidence, may need re-review:")
    candidates_sorted = sorted(result["candidates"], key=lambda c: (c["sd_id"] or "", c["run_id"]))
    for c in candidates_sorted:
        print("  - %s [%s]" % (c["run_id"], c["experiment_type"]))
        print("      substrate_queue %s (%s) -- %s" % (c["sd_id"], c["sd_title"], c["substrate_paths"]))
        print("      run %s > entry added_utc %s" % (c["run_timestamp"], c["added_utc"]))

    return 1 if (args.strict and (n or missing)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
