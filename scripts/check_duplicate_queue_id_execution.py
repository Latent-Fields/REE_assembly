#!/usr/bin/env python3
"""
Detect a queue_id that was EXECUTED more than once -- i.e. more than one
flat manifest in evidence/experiments/ carries the same `queue_id`.

THE DEFECT. A queue_id identifies exactly one run: the runner removes it
from experiment_queue.json the moment it goes terminal (PASS/FAIL/ERROR --
see CLAUDE.md "Queue completion behaviour"), and a re-queued bug-fix or
redesign gets a NEW queue_id (a letter suffix or a new number -- CLAUDE.md
"EXQ Versioning and Supersession Policy"). So under normal operation a
queue_id can never legitimately appear on two manifests: supersession always
changes the queue_id, it never re-runs the same one.

CONFIRMED INCIDENT: V3-EXQ-861f (2026-08-23). The coordinator's claim
recovery let a second machine (ree-cloud-4) re-claim and execute a queue_id
still being computed by its original owner (DLAPTOP), which had a transient
~54-minute heartbeat gap mid-run. Both machines produced a complete,
PASS-ing manifest for the same queue_id, ~9h apart in wall-clock finish time.
Root cause + fix: db.HEARTBEAT_FRESH_DEFAULT_SECONDS (coordinator/db.py) and
evidence/planning/duplicate_run_v3_exq_861f_20260825.md. That fix narrows the
race; it does not close it (any absence-based recovery has SOME window), so
this script is the defense-in-depth half: if it happens again, this is loud
about it rather than the corpus quietly holding two histories for one
queue_id until someone notices by hand.

WHAT IS AND ISN'T HARMED. Neither manifest is deleted or altered -- this is
detection only. A duplicate is usually scientifically harmless (an
accidental replication, as 861f's was: both PASS, same conclusion) but it
represents wasted compute and, if the two disagree, an unresolved conflict
that governance has not been told to look at.

USAGE
-----
    python3 scripts/check_duplicate_queue_id_execution.py            # summary, exit 0/1
    python3 scripts/check_duplicate_queue_id_execution.py --list      # print every finding

Exit codes:
    0  every finding is already in the pinned KNOWN_DUPLICATE_QUEUE_IDS
       baseline
    1  a NEW finding not in the baseline (or a baseline entry no longer
       reproduces) -- KNOWN_DUPLICATE_QUEUE_IDS needs an explicit, deliberate
       update either way, matching this repo's "corpus fire count is pinned"
       convention for other corpus-wide lints (CLAUDE.md, corpus-scan sharing)
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"

_NON_MANIFEST_FILES = frozenset({
    "claim_evidence.v1.json",
    "claim_evidence_matrix.v1.json",
    "review_tracker.json",
    "runner_status.json",
    "substrate_status_snapshot.json",
    "pending_review.json",
    "arm_fingerprint_index.json",
})

# Pinned baseline, measured 2026-08-25 when this script was first run
# against the real corpus. Only V3-EXQ-861f (the incident this script was
# built from -- see module docstring) has an established root cause. The
# other 21 predate the 2026-08-23 coordinator fix and were NOT individually
# investigated in that session -- most of the short-elapsed ones (a handful
# of seconds, e.g. V3-EXQ-542a/543i/567/568/576/603/603b) look like an
# unrelated older re-queue-under-the-same-id pattern from a quick
# substrate-readiness-check class of experiment, while at least two
# (V3-EXQ-699b: two FAILs, ~14h and ~66h, ree-worker-1 + DLAPTOP-5.local;
# V3-EXQ-778: two PASSes ~51min apart, ree-cloud-4 + ree-worker-1) look like
# genuine earlier instances of the same duplicate-claim shape. Flagged here
# as a pinned baseline (not silently cleared) specifically so a future
# session doing that audit starts from this list rather than rediscovering
# it. A NEW entry beyond this baseline always needs a human decision (which
# manifest is authoritative, does one need evidence_direction: superseded,
# does governance need to see both) -- this script only ever detects, never
# resolves.
KNOWN_DUPLICATE_QUEUE_IDS = frozenset({
    "V3-EXQ-542a", "V3-EXQ-543i", "V3-EXQ-567", "V3-EXQ-568", "V3-EXQ-576",
    "V3-EXQ-590c", "V3-EXQ-603", "V3-EXQ-603b", "V3-EXQ-696", "V3-EXQ-699b",
    "V3-EXQ-705", "V3-EXQ-705b", "V3-EXQ-706", "V3-EXQ-706b", "V3-EXQ-707c",
    "V3-EXQ-728", "V3-EXQ-729", "V3-EXQ-734", "V3-EXQ-737", "V3-EXQ-778",
    "V3-EXQ-798a", "V3-EXQ-861f",
})


def _iter_flat_manifests(evidence_dir: Path):
    if not evidence_dir.is_dir():
        return
    for f in sorted(evidence_dir.glob("*.json")):
        if f.name in _NON_MANIFEST_FILES or f.name.startswith("_dry_"):
            continue
        yield f


def scan(evidence_dir: Path = EVIDENCE_DIR, root: Path = ROOT) -> list[dict]:
    """Every queue_id with more than one non-superseded manifest in
    `evidence_dir`. Best-effort: an unreadable/non-dict manifest is skipped,
    not fatal -- this is a hygiene report, not a schema gate.
    `evidence_dir`/`root` are parameterisable so tests can point this at a
    hermetic tmp tree rather than the real corpus."""
    by_qid = defaultdict(list)
    for f in _iter_flat_manifests(evidence_dir):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        qid = d.get("queue_id")
        if not qid:
            continue
        if d.get("evidence_direction") == "superseded":
            continue
        by_qid[qid].append({
            "run_id": d.get("run_id"),
            "machine": d.get("machine"),
            "path": str(f.relative_to(root)),
        })

    findings = []
    for qid, entries in sorted(by_qid.items()):
        if len(entries) > 1:
            findings.append({"queue_id": qid, "runs": entries})
    return findings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--list", action="store_true",
                     help="print every finding (known and new), not just the summary")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args(argv)

    # Read EVIDENCE_DIR/ROOT/KNOWN_DUPLICATE_QUEUE_IDS as module globals AT
    # CALL TIME (not via scan()'s bound-at-def-time defaults) so a test can
    # monkeypatch them onto this module and have main() actually observe it.
    findings = scan(EVIDENCE_DIR, ROOT)
    found_qids = {f["queue_id"] for f in findings}
    new = sorted(found_qids - KNOWN_DUPLICATE_QUEUE_IDS)
    missing = sorted(KNOWN_DUPLICATE_QUEUE_IDS - found_qids)

    if args.as_json:
        print(json.dumps({
            "findings": findings, "new": new, "no_longer_reproducing": missing,
        }, indent=2))
    elif args.list:
        for f in findings:
            tag = "known" if f["queue_id"] in KNOWN_DUPLICATE_QUEUE_IDS else "NEW"
            machines = [r.get("machine") for r in f["runs"]]
            print("%-6s %-14s machines=%s (%d run(s))"
                  % (tag, f["queue_id"], machines, len(f["runs"])))
            for r in f["runs"]:
                print("         run_id=%s  (%s)" % (r.get("run_id"), r.get("path")))

    if new:
        print("NEW duplicate-execution(s), not in the pinned "
              "KNOWN_DUPLICATE_QUEUE_IDS baseline:", file=sys.stderr)
        for qid in new:
            print("  %s" % qid, file=sys.stderr)
        print("A queue_id ran on more than one machine. Decide which run is "
              "authoritative (mark the other evidence_direction: superseded "
              "with a note, or flag both to governance if they disagree), "
              "then add the queue_id to KNOWN_DUPLICATE_QUEUE_IDS in this "
              "script. See coordinator/db.py HEARTBEAT_FRESH_DEFAULT_SECONDS "
              "and evidence/planning/duplicate_run_v3_exq_861f_20260825.md "
              "for the mechanism this usually comes from.", file=sys.stderr)
    if missing:
        print("Baseline entrie(s) no longer reproducing -- update "
              "KNOWN_DUPLICATE_QUEUE_IDS in this script: %s" % ", ".join(missing),
              file=sys.stderr)
    if not new and not missing and not args.as_json:
        print("duplicate queue_id execution: %d known finding(s), 0 new (clean)"
              % len(found_qids))

    return 1 if (new or missing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
