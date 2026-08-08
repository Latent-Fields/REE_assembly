#!/usr/bin/env python3
"""
Report which targets[].run_id strings cited by confirmed failure-autopsy
artifacts do NOT resolve to a real manifest on disk.

The adjudication guard for the run-id CITATION defect. generate_pending_review.py
clears a run from the "never autopsied" blind-spot pool only when its EXACT
run_id appears as a targets[].run_id field of a status=="confirmed"
failure_autopsy_*.json (load_confirmed_autopsy_run_ids). A run_id that was
hand-composed from a claim-family naming pattern instead of copied verbatim from
ls/find output -- a truncated timestamp, a timestamp that never existed, a
fabricated experiment_type segment -- silently fails that exact-string match, so
the run re-enters the pending pool indistinguishable from one nobody ever looked
at, even though it was diagnosed correctly. Confirmed across /failure-autopsy
rounds 3-6 of the 2026-08-08 grandfathered-backlog sweep (session
failure-autopsy-9e8737); the round-4 397d hippo_quality_gap signature fell out of
confirmed coverage over an 8-character timestamp omission.

Resolution mirrors the manifest-discovery conventions the indexer and
generate_pending_review.load_dry_run_run_ids use:

    flat      evidence/experiments/<run_id>.json
    run-pack  evidence/experiments/<exp_dir>/runs/<run_id>/manifest.json
    run-pack  evidence/experiments/<exp_dir>/runs/<run_id>.json

(verified equivalent to a content-based scan of the run_id field across all
manifests: 0 disagreements over the 1054 distinct run_ids currently cited by
confirmed autopsies -- so a citation this tool flags is genuinely unresolvable,
not merely stored at an unusual path.)

Usage (from REE_assembly/, or anywhere -- paths resolve off this file):

    # every targets[].run_id in every CONFIRMED autopsy (the corpus scan)
    python3 scripts/check_autopsy_run_id_citations.py

    # one autopsy file -- checks all its targets regardless of status
    python3 scripts/check_autopsy_run_id_citations.py \
        evidence/planning/failure_autopsy_543i_2026-05-19.json

    # a bare run_id -- does it resolve on disk?
    python3 scripts/check_autopsy_run_id_citations.py \
        v3_exq_397d_arc007_matched_endpoint_20260423T202213Z_v3

    # a bare queue_id -- every cited run_id in the confirmed corpus under it
    python3 scripts/check_autopsy_run_id_citations.py V3-EXQ-397d

Targets with no run_id, or run_id: null, are skipped -- some diagnostic /
claim-free targets legitimately have none.

WARN-only by default (exit 0), matching check_dry_run_citations.py and
validate_experiments.py --checks dry_run_unreachable_criterion: a static scan
must not block a commit on a false positive. Pass --exit-nonzero for a future
CI / governance gate to opt into a hard failure.

Exit codes:
    0  no unresolved citation (or --exit-nonzero not given)
    1  at least one unresolved citation AND --exit-nonzero given
    2  usage error / nothing to check
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"
PLANNING_DIR = ROOT / "evidence" / "planning"
AUTOPSY_GLOB = "failure_autopsy_*.json"

QUEUE_ID_RE = re.compile(r"^(?:V\d-)?EXQ-\d+[a-z]?$", re.IGNORECASE)


def experiment_dirs(evidence_dir=EVIDENCE_DIR):
    """Top-level experiment directories under evidence/experiments/.

    Computed once and reused so a corpus scan does not re-list the tree per
    run_id. Returns [] rather than raising when the tree is absent."""
    if not evidence_dir.is_dir():
        return []
    return [d for d in evidence_dir.iterdir() if d.is_dir()]


def resolve_run_id(run_id, evidence_dir=EVIDENCE_DIR, exp_dirs=None):
    """Return the manifest Path a run_id resolves to, or None.

    Deterministic stat checks -- never a glob with the run_id interpolated, so a
    malformed 'run_id' carrying glob metacharacters or spaces (the exact prose
    citations this tool exists to catch) is handled safely rather than raising or
    matching by accident. A run_id containing a path separator can never resolve
    (real run_ids never do), which is the correct answer."""
    if not run_id or "/" in run_id:
        return None
    flat = evidence_dir / (run_id + ".json")
    if flat.is_file():
        return flat
    if exp_dirs is None:
        exp_dirs = experiment_dirs(evidence_dir)
    for exp in exp_dirs:
        runs = exp / "runs"
        pack = runs / run_id / "manifest.json"
        if pack.is_file():
            return pack
        direct = runs / (run_id + ".json")
        if direct.is_file():
            return direct
    return None


def iter_autopsy_files(planning_dir=PLANNING_DIR):
    if not planning_dir.is_dir():
        return
    for p in sorted(planning_dir.glob(AUTOPSY_GLOB)):
        yield p


def cited_run_ids(autopsy_path, confirmed_only=True):
    """(status, [run_id, ...]) cited via targets[].run_id in one autopsy file.

    Skips null / missing / non-string / empty run_ids. When confirmed_only is
    set and status != 'confirmed', returns (status, None) to signal 'not
    scanned' -- only confirmed artifacts clear the pending-review blind-spot net,
    so only they matter to a corpus scan."""
    try:
        data = json.loads(autopsy_path.read_text())
    except Exception:
        return (None, None)
    if not isinstance(data, dict):
        return (None, None)
    status = data.get("status")
    if confirmed_only and str(status) != "confirmed":
        return (status, None)
    out = []
    for target in data.get("targets", []) or []:
        if not isinstance(target, dict):
            continue
        rid = target.get("run_id")
        if isinstance(rid, str) and rid:
            out.append(rid)
    return (status, out)


def scan_file(autopsy_path, evidence_dir=EVIDENCE_DIR, exp_dirs=None,
              confirmed_only=True):
    """Resolve every cited run_id in one autopsy. Returns a finding dict."""
    if exp_dirs is None:
        exp_dirs = experiment_dirs(evidence_dir)
    status, rids = cited_run_ids(autopsy_path, confirmed_only=confirmed_only)
    if rids is None:
        return {"file": str(autopsy_path), "status": status,
                "scanned": False, "resolved": [], "unresolved": []}
    resolved, unresolved = [], []
    for rid in rids:
        if resolve_run_id(rid, evidence_dir, exp_dirs) is not None:
            resolved.append(rid)
        else:
            unresolved.append(rid)
    return {"file": str(autopsy_path), "status": status, "scanned": True,
            "resolved": resolved, "unresolved": unresolved}


def scan_corpus(planning_dir=PLANNING_DIR, evidence_dir=EVIDENCE_DIR):
    """Scan every confirmed failure_autopsy_*.json. Returns [finding, ...]."""
    exp_dirs = experiment_dirs(evidence_dir)
    findings = []
    for p in iter_autopsy_files(planning_dir):
        f = scan_file(p, evidence_dir, exp_dirs, confirmed_only=True)
        if f["scanned"]:
            findings.append(f)
    return findings


def _queue_stem(queue_id):
    """'V3-EXQ-397d' -> 'v3_exq_397d_' -- the run_id prefix runs of that queue
    entry share. Trailing underscore so EXQ-39 does not match EXQ-397's runs."""
    m = re.match(r"^(?:(V\d)-)?EXQ-(\d+[a-z]?)$", queue_id, re.IGNORECASE)
    if not m:
        return None
    gen = (m.group(1) or "").lower()
    num = m.group(2).lower()
    prefix = (gen + "_" if gen else "") + "exq_" + num + "_"
    return prefix


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Report autopsy targets[].run_id citations that do not "
                    "resolve to a manifest on disk.")
    ap.add_argument("targets", nargs="*",
                    help="autopsy file paths, a bare run_id, or a bare queue_id; "
                         "no args scans every confirmed autopsy")
    ap.add_argument("--exit-nonzero", action="store_true",
                    help="exit 1 when any unresolved citation is found "
                         "(for a CI / governance gate)")
    ap.add_argument("--planning-dir", default=None,
                    help="override evidence/planning directory (testing)")
    ap.add_argument("--evidence-dir", default=None,
                    help="override evidence/experiments directory (testing)")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args(argv)

    planning_dir = Path(args.planning_dir) if args.planning_dir else PLANNING_DIR
    evidence_dir = Path(args.evidence_dir) if args.evidence_dir else EVIDENCE_DIR
    exp_dirs = experiment_dirs(evidence_dir)

    findings = []
    unresolved_total = 0

    if not args.targets:
        # Corpus scan: every confirmed autopsy.
        for p in iter_autopsy_files(planning_dir):
            f = scan_file(p, evidence_dir, exp_dirs, confirmed_only=True)
            if f["scanned"]:
                findings.append(f)
                unresolved_total += len(f["unresolved"])
    else:
        for arg in args.targets:
            p = Path(arg)
            if p.exists() and p.is_file():
                # Explicit file: check ALL targets regardless of status.
                f = scan_file(p, evidence_dir, exp_dirs, confirmed_only=False)
                findings.append(f)
                unresolved_total += len(f["unresolved"])
            elif QUEUE_ID_RE.match(arg):
                stem = _queue_stem(arg)
                res, unres = [], []
                for ap_path in iter_autopsy_files(planning_dir):
                    status, rids = cited_run_ids(ap_path, confirmed_only=True)
                    if rids is None:
                        continue
                    for rid in rids:
                        if stem and not rid.lower().startswith(stem):
                            continue
                        if resolve_run_id(rid, evidence_dir, exp_dirs):
                            res.append(rid)
                        else:
                            unres.append(rid)
                findings.append({"file": "<queue %s>" % arg, "status": None,
                                 "scanned": True, "resolved": res,
                                 "unresolved": unres})
                unresolved_total += len(unres)
            else:
                # Treat as a bare run_id.
                ok = resolve_run_id(arg, evidence_dir, exp_dirs) is not None
                findings.append({
                    "file": "<arg>", "status": None, "scanned": True,
                    "resolved": [arg] if ok else [],
                    "unresolved": [] if ok else [arg]})
                if not ok:
                    unresolved_total += 1

    if args.as_json:
        print(json.dumps({"findings": findings,
                          "unresolved_total": unresolved_total},
                         indent=2, sort_keys=True))
    else:
        scanned_files = 0
        resolved_total = 0
        for f in findings:
            if not f["scanned"]:
                continue
            scanned_files += 1
            resolved_total += len(f["resolved"])
            for rid in f["unresolved"]:
                print("UNRESOLVED %s -- cited by %s%s"
                      % (rid, f["file"],
                         " (status %s)" % f["status"] if f["status"] else ""))
        print("-- %d unresolved of %d resolved cited run_id(s) across %d file(s)"
              % (unresolved_total, resolved_total, scanned_files))
        if unresolved_total:
            print("An unresolved targets[].run_id does NOT clear the run from "
                  "generate_pending_review.py's blind-spot pool. Fix the citation "
                  "verbatim from ls/find output; the diagnosis may already be "
                  "correct.")

    if args.exit_nonzero and unresolved_total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
