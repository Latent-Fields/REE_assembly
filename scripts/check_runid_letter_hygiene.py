#!/usr/bin/env python3
"""
Report manifests whose lettered queue_id is not encoded in their run_id.

THE DEFECT (confirmed failure_autopsy_V3-EXQ-920a_2026-08-16, ratified by
/governance 2026-08-16). Under the EXQ versioning policy (CLAUDE.md "EXQ
Versioning and Supersession Policy"), a bug-fix re-queue appends a letter to
the queue_id (V3-EXQ-920 -> V3-EXQ-920a) while reusing the SAME driver
byte-unchanged. The driver's `EXPERIMENT_TYPE` is a module-level constant with
no access to its own `queue_id`, so the `run_id` it stamps
(`f"{EXPERIMENT_TYPE}_{ts}_v3"`) never carries the letter. Two different runs
then share one run_id STEM, separable only by the timestamp segment. Any
consumer that keys on the stem (a family sweep, a filename glob, a run-pack
directory name) silently collapses them into one -- which is exactly how the
920a autopsy nearly re-adjudicated an already-covered run (see
`check_autopsy_coverage.py`, the consumer-side fix for that specific
already-done check).

This script is the DETECTION half: it does not rename anything (a landed
manifest's run_id is provenance and must never be retro-edited -- CLAUDE.md
"Narrow Edits Only" analogue), it only reports. The PRODUCER half (thread
queue_id into the run-pack key so a same-driver re-queue cannot reproduce
this) is structural -- ~1160 drivers each compute their own run_id inline --
and is out of scope here; see the autopsy's Section 7a/10 item 6 for the full
writeup.

MEASURED SCALE (2026-08-16 autopsy, corpus-wide over
evidence/experiments/*.json): 733 manifests carry both queue_id and run_id;
376 have a lettered queue_id; 9 of those are genuine letter-drops (612c,
612d, 737a, 737b, 742a, 742b, 766a, 914a, 920a); 10 run_id stems are shared
by 2+ queue_ids corpus-wide (6 of the letter-drop shape). Rare (1.4% of
manifests) but recurring across 6 unrelated families from 2026-05 to
2026-08 -- not a closed historical artefact.

Usage (from REE_assembly/, or anywhere -- paths resolve off this file):

    python3 scripts/check_runid_letter_hygiene.py            # report, exit 0
    python3 scripts/check_runid_letter_hygiene.py --json
    python3 scripts/check_runid_letter_hygiene.py --exit-nonzero   # gate

Exit codes:
    0  always, unless --exit-nonzero is passed
    1  (--exit-nonzero only) at least one letter-drop or stem collision found
    2  usage error (evidence dir not found)

Deliberately NOT gated by default and NOT pinned against the known-9 baseline:
the defect is confirmed rare, no evidence has been lost (the full run_id
remains unique corpus-wide), and the fix direction is "consumers key on the
full run_id/(queue_id, run_id), never the stem" -- not "drive this count to
zero". See test_check_runid_letter_hygiene.py for hermetic behaviour tests.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"

# V3-EXQ-920a -> ("V3-EXQ-", "920", "a"). Deliberately excludes shapes like
# "742-m" / "742m-b" (a hyphenated or double-letter variant naming scheme,
# not the letter-suffix bug-fix convention) -- matching the autopsy's own
# classification of "9 genuine letter-drops" vs "3 different naming shape".
LETTERED_QUEUE_ID_RE = re.compile(r"^(V\d+-EXQ-)(\d+)([a-z])$")

# Strip a run_id down to a stem for collision detection: drop the trailing
# timestamp segment and/or the "_v3" generation suffix. Mirrors the shape
# used corpus-wide (compact timestamp form only -- the epoch-seconds form is
# not a suffix on the letter-drop family and is not needed here).
_TIMESTAMP_SUFFIX_RE = re.compile(r"_\d{8}T\d{6}Z?(?:_v[34])?$")
_GEN_SUFFIX_RE = re.compile(r"_v[34]$")


def stem_of(run_id):
    stem = _TIMESTAMP_SUFFIX_RE.sub("", run_id)
    stem = _GEN_SUFFIX_RE.sub("", stem)
    return stem


def _iter_manifest_paths(evidence_dir):
    """Flat top-level manifests plus the canonical runs/<run_id>/manifest.json packs.

    Mirrors check_dry_run_citations._iter_manifest_paths -- same two shapes,
    no _NON_MANIFEST_FILES filter needed here since a non-manifest JSON simply
    will not carry both queue_id and run_id and is silently skipped below.
    """
    if not evidence_dir.is_dir():
        return
    for f in sorted(evidence_dir.glob("*.json")):
        yield f
    for f in sorted(evidence_dir.glob("*/runs/*/manifest.json")):
        yield f


def load_pairs(evidence_dir):
    """Return a list of (queue_id, run_id, relpath) for every manifest carrying both."""
    pairs = []
    for f in _iter_manifest_paths(evidence_dir):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        qid = d.get("queue_id")
        rid = d.get("run_id")
        if not qid or not rid:
            continue
        try:
            rel = str(f.relative_to(evidence_dir.parent.parent))
        except ValueError:
            rel = str(f)
        pairs.append((str(qid), str(rid), rel))
    return pairs


def find_letter_drops(pairs):
    """Lettered queue_id whose run_id does not encode that letter after the number."""
    findings = []
    for qid, rid, path in pairs:
        m = LETTERED_QUEUE_ID_RE.match(qid)
        if not m:
            continue
        _prefix, number, letter = m.groups()
        # Look for the number immediately inside the run_id (optionally
        # zero-padded is not a real corpus shape, but strip leading zeros
        # defensively) followed by an optional letter run, then '_'.
        num_re = re.search(r"exq_0*" + re.escape(number) + r"([a-z]*)_", rid)
        if num_re is None:
            # Run_id does not reference this queue_id's number at all (e.g.
            # the SD-068 family, which encodes a descriptive slug instead of
            # a number) -- not this defect's shape, skip.
            continue
        found_letters = num_re.group(1)
        if letter not in found_letters:
            findings.append({"queue_id": qid, "run_id": rid, "path": path})
    return findings


def find_stem_collisions(pairs):
    """Distinct run_id stems shared by 2+ distinct queue_ids."""
    by_stem = {}
    for qid, rid, path in pairs:
        by_stem.setdefault(stem_of(rid), {}).setdefault(qid, []).append((rid, path))
    findings = []
    for stem, by_qid in sorted(by_stem.items()):
        if len(by_qid) < 2:
            continue
        findings.append({
            "stem": stem,
            "queue_ids": {qid: [rid for rid, _ in entries] for qid, entries in sorted(by_qid.items())},
        })
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--evidence-dir", default=str(EVIDENCE_DIR),
                     help="evidence/experiments dir to scan (default: real corpus)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--exit-nonzero", action="store_true",
                     help="exit 1 if any finding exists (default: always exit 0)")
    args = ap.parse_args(argv)

    evidence_dir = Path(args.evidence_dir)
    if not evidence_dir.is_dir():
        print("ERROR: evidence dir not found: %s" % evidence_dir, file=sys.stderr)
        return 2

    pairs = load_pairs(evidence_dir)
    letter_drops = find_letter_drops(pairs)
    stem_collisions = find_stem_collisions(pairs)

    if args.json:
        print(json.dumps({
            "manifests_with_both_ids": len(pairs),
            "letter_drops": letter_drops,
            "stem_collisions": stem_collisions,
        }, indent=2, sort_keys=True))
    else:
        print("manifests carrying both queue_id and run_id: %d" % len(pairs))
        print("lettered queue_id whose run_id omits the letter: %d" % len(letter_drops))
        for f in letter_drops:
            print("  %s -> %s  (%s)" % (f["queue_id"], f["run_id"], f["path"]))
        print("run_id stems shared by 2+ queue_ids: %d" % len(stem_collisions))
        for f in stem_collisions:
            print("  %s -> %s" % (f["stem"], sorted(f["queue_ids"].keys())))
        print()
        print("Full run_ids remain unique corpus-wide -- no evidence is lost. "
              "This is a report, not a gate (see module docstring); consumers "
              "must key on the full run_id or (queue_id, run_id), never a "
              "stripped stem.")

    if args.exit_nonzero and (letter_drops or stem_collisions):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
