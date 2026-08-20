#!/usr/bin/env python3
"""
Detect run_id/queue_id "letter-drop" hygiene defects in the experiment
evidence corpus.

THE DEFECT. A lettered queue_id ("V3-EXQ-920a") identifies a re-queued
(typically bug-fixed) iteration of a driver, and that driver is commonly the
SAME script file as its predecessor, unrenamed -- the fix is often just an
in-place edit, re-queued under a new lettered queue_id (CLAUDE.md's own
"Bug fix / minor tweak" convention). The driver's run_id is usually built from
a hardcoded EXPERIMENT_TYPE module constant plus a timestamp, so unless the
author remembers to thread the letter through, the run_id silently omits it --
"V3-EXQ-920a" produces a run_id indistinguishable (once its number-prefixed
stem is taken) from plain "V3-EXQ-920"'s.

Confirmed and measured corpus-wide in
evidence/planning/failure_autopsy_V3-EXQ-920a_2026-08-16.md section 7a: 9 of
376 lettered queue_ids (2.4%) hit this shape (612c/612d, 737a/737b, 742a/742b,
766a, 914a, 920a), spanning six unrelated experiment families from 2026-05 to
2026-08 -- rare, but recurring, not a closed historical artefact.

WHAT IS AND ISN'T HARMED. The full run_id (its timestamp disambiguates) stays
unique corpus-wide -- no evidence has ever actually been lost. The exposure is
that anything keying on a STRIPPED run_id stem -- a family-match glob, a
filename-prefix sweep, an ad-hoc `v3_exq_920*` search -- silently conflates
the two runs. That is exactly the near-miss the 920a autopsy session hit: it
almost re-autopsied an already-covered run because a stem-based search did not
separate V3-EXQ-920 from V3-EXQ-920a.

NOT FLAGGED: the SD-068 family (V3-EXQ-778a..h), whose run_ids never encode
the queue NUMBER at all (v3_exq_sd068_<descriptive-slug>_diagnostic_...) --
those are separable by slug and are not a de-duplication hazard (the single
exception, 778b/778c sharing a slug, is a stem collision but not a
letter-drop, and is out of this script's scope).

THE FIX, both halves (this script is the detection half of each):
  1. Consumers must key on the FULL run_id, or on (queue_id, run_id) -- never
     a stripped stem. `scripts/check_autopsy_coverage.py` (umbrella scripts/)
     already does this (full-string match only, see its own module
     docstring). This script exists so the CORPUS itself is checked, not just
     one consumer's matching logic.
  2. Producers should thread the runner-supplied queue_id into the run_id (or
     at minimum notice when they didn't). `ree-v3/experiments/pack_writer.py`
     `write_flat_manifest` now prints a non-fatal warning at write time when
     this shape is detected (`_warn_if_queue_letter_dropped`) -- this script
     is the corpus-wide, retrospective-and-CI-facing counterpart.

DO NOT retro-rename a landed manifest to "fix" this -- that falsifies
provenance (the run_id is part of the record of what actually happened). The
correct remedy for an EXISTING finding is: fix the driver's run_id
construction so the NEXT re-queue of that script does not repeat it, then
remove the queue_id from KNOWN_LETTER_DROPS below (never edit the manifest).

USAGE
-----
    python3 scripts/check_run_id_letter_hygiene.py            # summary, exit 0/1
    python3 scripts/check_run_id_letter_hygiene.py --list      # print every finding

Exit codes:
    0  every finding is already in the pinned KNOWN_LETTER_DROPS baseline
    1  a NEW finding not in the baseline (or a baseline entry no longer
       reproduces) -- KNOWN_LETTER_DROPS needs an explicit, deliberate update
       either way, matching this repo's "corpus fire count is pinned"
       convention for other corpus-wide lints (CLAUDE.md, corpus-scan sharing)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"

# Same shape as check_dry_run_citations.QUEUE_ID_RE / pack_writer's
# _LETTERED_QUEUE_ID_RE -- kept as a separate, independent constant on
# purpose (this script must be able to catch a regression in either of
# those, not share a bug with them).
_LETTERED_QUEUE_ID_RE = re.compile(r"^(?:V\d-)?EXQ-(\d+)([a-z])$")

_NON_MANIFEST_FILES = frozenset({
    "claim_evidence.v1.json",
    "claim_evidence_matrix.v1.json",
    "review_tracker.json",
    "runner_status.json",
    "substrate_status_snapshot.json",
    "pending_review.json",
    "arm_fingerprint_index.json",
})

# Pinned baseline, measured 2026-08-16 (failure_autopsy_V3-EXQ-920a_2026-08-16.md
# sec 7a) and re-measured 2026-08-18 at chip-20260816-runid-identifier-hygiene
# time -- still exactly these nine, corpus-wide. A CHANGE to this set (new
# entry, or an entry that no longer reproduces) must be a deliberate edit, not
# something this script silently absorbs.
KNOWN_LETTER_DROPS = frozenset({
    "V3-EXQ-612c", "V3-EXQ-612d",
    "V3-EXQ-737a", "V3-EXQ-737b",
    "V3-EXQ-742a", "V3-EXQ-742b",
    "V3-EXQ-766a",
    "V3-EXQ-914a",
    "V3-EXQ-920a",
})


def is_letter_drop(queue_id: str, run_id: str) -> bool:
    """True iff `queue_id` is lettered (EXQ-<N><letter>) and `run_id` carries
    the number <N> but not the immediately-following letter. See module
    docstring for why the SD-068 shape (number never present) is excluded."""
    m = _LETTERED_QUEUE_ID_RE.match((queue_id or "").strip())
    if not m:
        return False
    number, letter = m.group(1), m.group(2)
    rid = run_id or ""
    idx = rid.find(number)
    if idx == -1:
        return False
    after = rid[idx + len(number):idx + len(number) + 1]
    return after != letter


def _iter_flat_manifests(evidence_dir: Path):
    if not evidence_dir.is_dir():
        return
    for f in sorted(evidence_dir.glob("*.json")):
        if f.name in _NON_MANIFEST_FILES or f.name.startswith("_dry_"):
            continue
        yield f


def scan(evidence_dir: Path = EVIDENCE_DIR, root: Path = ROOT) -> list[dict]:
    """Every (queue_id, run_id, path) triple in `evidence_dir` hitting the
    letter-drop shape. Best-effort: an unreadable/non-dict manifest is
    skipped, not fatal -- this is a hygiene report, not a schema gate.
    `evidence_dir`/`root` are parameterisable so tests can point this at a
    hermetic tmp tree rather than the real corpus."""
    findings = []
    for f in _iter_flat_manifests(evidence_dir):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        qid, rid = d.get("queue_id"), d.get("run_id")
        if not qid or not rid:
            continue
        if is_letter_drop(qid, rid):
            findings.append({
                "queue_id": qid, "run_id": rid,
                "path": str(f.relative_to(root)),
            })
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

    # Read EVIDENCE_DIR/ROOT/KNOWN_LETTER_DROPS as module globals AT CALL TIME
    # (not via scan()'s bound-at-def-time defaults) so a test can monkeypatch
    # them onto this module and have main() actually observe the override.
    findings = scan(EVIDENCE_DIR, ROOT)
    found_qids = {f["queue_id"] for f in findings}
    new = sorted(found_qids - KNOWN_LETTER_DROPS)
    missing = sorted(KNOWN_LETTER_DROPS - found_qids)

    if args.as_json:
        print(json.dumps({
            "findings": findings, "new": new, "no_longer_reproducing": missing,
        }, indent=2))
    elif args.list:
        for f in findings:
            tag = "known" if f["queue_id"] in KNOWN_LETTER_DROPS else "NEW"
            print("%-6s %-14s run_id=%s  (%s)"
                  % (tag, f["queue_id"], f["run_id"], f["path"]))

    if new:
        print("NEW letter-drop(s), not in the pinned KNOWN_LETTER_DROPS baseline:",
              file=sys.stderr)
        for qid in new:
            print("  %s" % qid, file=sys.stderr)
        print("Fix the driver's run_id/EXPERIMENT_TYPE construction going forward "
              "(never retro-rename the landed manifest -- that falsifies "
              "provenance), then add the queue_id to KNOWN_LETTER_DROPS in this "
              "script. See failure_autopsy_V3-EXQ-920a_2026-08-16.md sec 7a.",
              file=sys.stderr)
    if missing:
        print("Baseline entrie(s) no longer reproducing -- update "
              "KNOWN_LETTER_DROPS in this script: %s" % ", ".join(missing),
              file=sys.stderr)
    if not new and not missing and not args.as_json:
        print("run_id/queue_id letter hygiene: %d known finding(s), 0 new (clean)"
              % len(found_qids))

    return 1 if (new or missing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
