#!/usr/bin/env python3
"""
Report which run_ids cited by an adjudication artifact are --dry-run smokes.

The adjudication guard for the dry-run leak. As of 2026-07-28 the *scoring* path
is gated in three places -- sync_v3_results.py (pack converter),
build_experiment_indexes.py (indexer), and generate_pending_review.py
(load_dry_run_run_ids excludes dry run_ids from every pending bucket). Nothing
stopped a /failure-autopsy or /governance session from READING a dry manifest
and reasoning over its metrics as evidence. Confirmed twice, in opposite
directions, six hours apart on 2026-05-19 for V3-EXQ-543i; full analysis in
evidence/planning/dry_run_smoke_in_autopsy_audit_2026-07-28.md.

Usage (from REE_assembly/, or anywhere -- paths resolve off this file):

    # every run_id / queue_id an autopsy cites, anywhere in the file
    python3 scripts/check_dry_run_citations.py \
        evidence/planning/failure_autopsy_543i_2026-05-19.json

    # bare ids, mixed with files; .md and .json both work
    python3 scripts/check_dry_run_citations.py v3_exq_543i_..._v3 V3-EXQ-543i

    # what would a family sweep hit? (the a6fda79367 failure mode)
    python3 scripts/check_dry_run_citations.py --family v3_exq_543f

    python3 scripts/check_dry_run_citations.py --list-dry

Ids are harvested by regex over EVERY string in a JSON file (or the raw text of
a .md), so a citation buried in prose -- a substrate_queue failure_record note,
an autopsy's section 8 draft -- is caught exactly like a structured targets[]
entry. That is deliberate: the confirmed damage in the 543i case was a prose
citation, not a schema field.

Exit codes:
    0  no cited run_id is dry (AMBIGUOUS queue-id hits may still be reported)
    1  at least one cited run_id resolves to a dry manifest
    2  usage error / nothing to check

--strict also exits 1 on AMBIGUOUS (a cited queue_id whose run set contains a
dry sibling -- the citation does not say which run was meant). Off by default:
a queue_id with a dry sibling is common and usually benign, and a guard that
fires on the benign case gets ignored on the real one.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    # Single source of truth for the truthiness check ("true"/"1"/"yes").
    # Do not re-implement it here -- a second copy is how the forms drift.
    from generate_pending_review import _is_dry_run, _NON_MANIFEST_FILES
except ImportError as exc:  # pragma: no cover - environment problem, be loud
    raise SystemExit(
        "cannot import _is_dry_run/_NON_MANIFEST_FILES from "
        "scripts/generate_pending_review.py: %s" % exc
    )

# A run_id always carries the manifest timestamp stem (20260518T063711Z).
RUN_ID_RE = re.compile(r"[A-Za-z0-9_.\-]*\d{8}T\d{6}Z[A-Za-z0-9_.\-]*")
QUEUE_ID_RE = re.compile(r"\b(?:V\d-)?EXQ-\d+[a-z]?\b")


def _looks_like_run_id(s):
    """Drop bare timestamps. Autopsy prose quotes `20260518T063711Z` on its own
    constantly; without this every such mention lands in UNKNOWN and buries the
    real findings. Every genuine run_id is `<stem>_<timestamp>_v3`."""
    return "_" in s


def _iter_manifest_paths():
    """Flat top-level manifests plus the canonical runs/<run_id>/manifest.json packs."""
    if not EVIDENCE_DIR.is_dir():
        return
    for f in EVIDENCE_DIR.glob("*.json"):
        if f.name not in _NON_MANIFEST_FILES:
            yield f
    for f in EVIDENCE_DIR.glob("*/runs/*/manifest.json"):
        yield f


def build_index():
    """run_id -> record, and queue_id -> [run_id]. Later reads do not clobber a dry flag."""
    by_run = {}
    by_queue = {}
    for f in _iter_manifest_paths():
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        rid = d.get("run_id")
        if not rid:
            continue
        dry = _is_dry_run(d)
        rec = by_run.get(rid)
        if rec is None:
            rec = {
                "run_id": rid,
                "queue_id": d.get("queue_id"),
                "experiment_type": d.get("experiment_type"),
                "elapsed_seconds": d.get("elapsed_seconds"),
                "dry_run": dry,
                "paths": [],
            }
            by_run[rid] = rec
        # A flat manifest and its pack copy can disagree (historic backfill gap):
        # treat dry on EITHER as dry -- the conservative direction for a guard.
        rec["dry_run"] = rec["dry_run"] or dry
        rec["paths"].append(str(f.relative_to(ROOT)))
        qid = rec.get("queue_id")
        if qid:
            by_queue.setdefault(qid, set()).add(rid)
    return by_run, by_queue


def harvest_ids(arg, by_run, by_queue):
    """Return (run_ids, queue_ids, source_label) for one CLI argument."""
    p = Path(arg)
    if p.exists() and p.is_file():
        text = p.read_text(errors="replace")
        return (
            {s for s in RUN_ID_RE.findall(text) if _looks_like_run_id(s)},
            set(QUEUE_ID_RE.findall(text)),
            str(p),
        )
    # Bare id.
    if RUN_ID_RE.fullmatch(arg) and _looks_like_run_id(arg):
        return {arg}, set(), "<arg>"
    if QUEUE_ID_RE.fullmatch(arg):
        return set(), {arg}, "<arg>"
    return set(), set(), "<arg>"


def main():
    ap = argparse.ArgumentParser(
        description="Report which cited run_ids are --dry-run smokes.")
    ap.add_argument("targets", nargs="*",
                    help="autopsy/planning file paths, bare run_ids, or queue_ids")
    ap.add_argument("--family", action="append", default=[],
                    help="experiment_type stem -- list every run in the family, "
                         "dry and real (use before any family-match sweep)")
    ap.add_argument("--list-dry", action="store_true",
                    help="print every dry run_id on disk and exit")
    ap.add_argument("--strict", action="store_true",
                    help="also exit 1 on AMBIGUOUS queue-id citations")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    by_run, by_queue = build_index()

    if args.list_dry:
        dry = sorted(r for r, v in by_run.items() if v["dry_run"])
        if args.as_json:
            print(json.dumps(dry, indent=2))
        else:
            for r in dry:
                print(r)
            print("-- %d dry run_id(s) of %d manifests on disk" % (len(dry), len(by_run)))
        return 0

    if not args.targets and not args.family:
        ap.print_usage()
        print("error: give at least one file/id, or --family, or --list-dry",
              file=sys.stderr)
        return 2

    findings = {"dry": [], "ambiguous": [], "clean": [], "unknown": [], "family": []}

    for fam in args.family:
        members = sorted(
            (v for v in by_run.values()
             if str(v.get("experiment_type") or "").startswith(fam)
             or v["run_id"].startswith(fam)),
            key=lambda v: v["run_id"])
        findings["family"].append({
            "family": fam,
            "dry": [v["run_id"] for v in members if v["dry_run"]],
            "real": [v["run_id"] for v in members if not v["dry_run"]],
        })

    seen_run, seen_queue = set(), set()
    sources = {}
    for arg in args.targets:
        runs, queues, src = harvest_ids(arg, by_run, by_queue)
        if not runs and not queues and src == "<arg>":
            findings["unknown"].append({"id": arg, "why": "not a file, run_id, or queue_id"})
        for r in runs:
            sources.setdefault(r, set()).add(src)
        for q in queues:
            sources.setdefault(q, set()).add(src)
        seen_run |= runs
        seen_queue |= queues

    for rid in sorted(seen_run):
        rec = by_run.get(rid)
        if rec is None:
            findings["unknown"].append({"id": rid, "why": "no manifest on disk"})
        elif rec["dry_run"]:
            findings["dry"].append({
                "run_id": rid,
                "queue_id": rec["queue_id"],
                "elapsed_seconds": rec["elapsed_seconds"],
                "cited_by": sorted(sources.get(rid, [])),
            })
        else:
            findings["clean"].append(rid)

    for qid in sorted(seen_queue):
        runs = sorted(by_queue.get(qid, []))
        dry = [r for r in runs if by_run[r]["dry_run"]]
        real = [r for r in runs if not by_run[r]["dry_run"]]
        # Only interesting when the queue_id is ambiguous AND the dry sibling was
        # not already named explicitly (in which case it is a DRY finding already).
        if dry and not set(dry) <= seen_run:
            findings["ambiguous"].append({
                "queue_id": qid, "dry": dry, "real": real,
                "cited_by": sorted(sources.get(qid, [])),
            })

    family_dry = sum(len(f["dry"]) for f in findings["family"])

    if args.as_json:
        print(json.dumps(findings, indent=2, sort_keys=True))
    else:
        for fam in findings["family"]:
            print("FAMILY %s -- %d dry / %d real"
                  % (fam["family"], len(fam["dry"]), len(fam["real"])))
            for r in fam["dry"]:
                print("    DRY  %s" % r)
            for r in fam["real"]:
                print("    real %s" % r)
        for d in findings["dry"]:
            print("DRY  %s (queue %s, elapsed %ss) -- cited by %s"
                  % (d["run_id"], d["queue_id"], d["elapsed_seconds"],
                     ", ".join(d["cited_by"]) or "<arg>"))
        for a in findings["ambiguous"]:
            print("AMBIGUOUS %s -- %d dry / %d real run(s); the citation does not "
                  "say which" % (a["queue_id"], len(a["dry"]), len(a["real"])))
            for r in a["dry"]:
                print("    DRY  %s" % r)
        for u in findings["unknown"]:
            print("UNKNOWN %s -- %s" % (u["id"], u["why"]))
        print("-- %d dry cited, %d dry in named families, %d ambiguous, "
              "%d clean, %d unknown"
              % (len(findings["dry"]), family_dry, len(findings["ambiguous"]),
                 len(findings["clean"]), len(findings["unknown"])))
        if findings["dry"] or family_dry:
            print("A dry manifest is NOT evidence. Do not reason over its metrics, "
                  "and never write evidence_direction / epistemic_category onto it.")

    if findings["dry"] or family_dry:
        return 1
    if args.strict and findings["ambiguous"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
