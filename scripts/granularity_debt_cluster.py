#!/usr/bin/env python3
"""Granularity-debt cluster reader for ONE claim (the reactive `/failure-autopsy` check).

WHY THIS EXISTS. The `/failure-autopsy` skill's granularity-debt recurrence
trigger used to be specified as "grep the planning dir for the target id". That
grep counts FILES IN THE CLAIM'S TOPICAL NEIGHBOURHOOD -- any autopsy whose prose
happens to mention the id, or whose sibling targets tag adjacent claims -- not
autopsy TARGETS whose own `claim_ids` name the claim. It therefore systematically
over-counts, and over-counting fires `/claim-synthesis` on clusters that are
really measurement or implementation debt -- exactly the failure mode
`/claim-synthesis`'s own rails exist to prevent.

Confirmed 2026-07-22 (claim_synthesis_MECH-163_2026-07-22.md s1a). Six cited
autopsies did not tag the claim they were cited for:

  MECH-440 <- 709 (['MECH-439','ARC-108','ARC-110']), 710 (['MECH-140',
    'MECH-450','MECH-439']), 707b (['ARC-110']), 699 (['MECH-448','MECH-449'])
  MECH-204 <- 606 (['MECH-318']), 774 (['MECH-173'])

MECH-440's real cluster is 3 targets / 3 files, not the reported 7; MECH-204's is
5 targets / 3 files, not 5 across 4. Both turned out to be Step-3 STOPs with ZERO
genuine FAIL signatures.

SUPERSEDED TARGETS ARE NOT COUNTED. A target whose `recommended_evidence_direction`
is `superseded` is inactive evidence by the same convention the indexer applies
(EXQ Versioning and Supersession Policy), so it is listed for transparency but
kept out of the headline count. This is what reconciles MECH-204's raw 6 tagging
targets with its real cluster of 5: `EXQ-541`'s implementation-bug target was
superseded by 541a/541b in the same artifact.

WHAT IT COUNTS. Every `evidence/planning/failure_autopsy_*.json` target whose
`claim_ids` list CONTAINS the claim id. Single-scope and cluster-scope artifacts
both store their per-run rows under top-level `targets[]`, so one pass covers
both schemas; the difference is where the VERDICT lives -- per-run under
`targets[].four_layer_diagnosis`, cluster-level under `cluster_pattern.readings`
(surfaced separately, never counted as a target).

THE SELF-CHECK (the count alone is a weak signal). Each target is classified by
its own `four_layer_diagnosis.claim_alignment`, and the distribution is printed
beside the count. A cluster in which NO target reads `weakened` is measurement or
implementation debt, not granularity debt, however many autopsies exist -- that
classification, not the count, is what decided all three claims examined on
2026-07-22 (MECH-204 even had a target reading `strengthened`). `claim_alignment`
is free text in the corpus, so it is bucketed on its leading token and anything
unrecognized lands in `other` rather than being silently dropped.

READ-ONLY. Promotes nothing, writes nothing, touches no claims.yaml.

Usage:
  python3 scripts/granularity_debt_cluster.py MECH-440
  python3 scripts/granularity_debt_cluster.py MECH-440 --json
  python3 scripts/granularity_debt_cluster.py MECH-440 --all-status  # incl. non-confirmed
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"

# Leading-token buckets for the free-text `claim_alignment` field. Order matters:
# first match on the normalized string wins, so "unclear (was: weakened)" buckets
# as `unclear` (the author's actual reading) and not as `weakened`.
_ALIGNMENT_BUCKETS = (
    ("weakened", "weakened"),
    ("strengthened", "strengthened"),
    ("intact", "intact"),
    ("unclear", "unclear"),
    ("unrecoverable", "unrecoverable"),
    ("coarse", "coarse/under-specified"),
    ("could-not-express", "could-not-express"),
    ("could_not_express", "could-not-express"),
    ("untested", "untested"),
    ("not-tested", "untested"),
    ("not tested", "untested"),
    ("n/a", "n/a"),
    ("na ", "n/a"),
    ("n_a", "n/a"),
    ("not_applicable", "n/a"),
    ("not applicable", "n/a"),
)

# Buckets that do NOT license the "no target reads `weakened`" conclusion, because
# the reading is unknown rather than known-not-weakened. `claim_alignment` is free
# text and its long tail contains strings that BURY a weakened reading in prose
# (e.g. "split_strengthened_at_substrate_weakened_at_behavioural_necessity"), so
# treating an unrecognized string as "not weakened" would make the self-check fail
# in the unsafe direction -- silently clearing a cluster that has a real FAIL
# signature. They are reported as ambiguous and sent back to the human instead.
_AMBIGUOUS_BUCKETS = {"other", "unstamped"}


def bucket_alignment(value) -> str:
    """Bucket a free-text `claim_alignment` on its leading token.

    Unrecognized text buckets as `other` (never dropped): the field is prose in
    the corpus and a silent drop would understate the very distribution this
    reader exists to expose. Absent / non-string -> `unstamped`.
    """
    if not isinstance(value, str) or not value.strip():
        return "unstamped"
    norm = value.strip().lower()
    for prefix, label in _ALIGNMENT_BUCKETS:
        if norm.startswith(prefix):
            return label
    return "other"


def collect(claim_id: str, autopsy_dir: Path,
            confirmed_only: bool = True) -> dict:
    """Return the target-level cluster for one claim.

    A target counts iff `claim_id` appears in its own `claim_ids`. Files that
    merely mention the id in prose, or whose OTHER targets tag adjacent claims,
    do not count -- that neighbourhood reading is the defect this replaces.
    """
    claim_id = claim_id.strip()
    targets: list[dict] = []
    superseded: list[dict] = []
    cluster_readings: list[dict] = []
    if not autopsy_dir.is_dir():
        return {"claim_id": claim_id, "targets": [], "superseded_targets": [],
                "cluster_readings": [], "n_targets": 0, "n_files": 0,
                "n_superseded": 0, "alignment": {}, "any_weakened": False}
    for fp in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        status = str(data.get("status") or "").strip().lower()
        if confirmed_only and status != "confirmed":
            continue
        # `scope` is free text in a couple of artifacts ("cluster | EXTENDED ..."),
        # so normalize by substring rather than equality.
        scope = str(data.get("scope") or "").strip().lower()
        matched_here = False
        for tgt in (data.get("targets") or []):
            claim_ids = tgt.get("claim_ids")
            if not isinstance(claim_ids, list):
                continue
            if claim_id not in {str(c).strip() for c in claim_ids}:
                continue
            matched_here = True
            fld = tgt.get("four_layer_diagnosis")
            alignment = fld.get("claim_alignment") if isinstance(fld, dict) else None
            direction = str(tgt.get("recommended_evidence_direction") or "").strip().lower()
            bucket = superseded if direction == "superseded" else targets
            bucket.append({
                "artifact": fp.stem,
                "scope": scope or "unknown",
                "status": status,
                "run_id": str(tgt.get("run_id") or tgt.get("queue_id") or ""),
                "claim_ids": [str(c).strip() for c in claim_ids],
                "failed_criterion": tgt.get("failed_criterion"),
                "recommended_evidence_direction": tgt.get("recommended_evidence_direction"),
                "recommended_epistemic_category": tgt.get("recommended_epistemic_category"),
                "claim_alignment": alignment,
                "claim_alignment_bucket": bucket_alignment(alignment),
            })
        # Cluster-level verdicts live outside targets[]; surface (never count) them
        # for an artifact that actually tags the claim.
        if matched_here and "cluster" in scope:
            readings = (data.get("cluster_pattern") or {}).get("readings")
            if readings:
                cluster_readings.append({"artifact": fp.stem, "readings": readings})

    alignment: dict[str, int] = {}
    for t in targets:
        alignment[t["claim_alignment_bucket"]] = alignment.get(t["claim_alignment_bucket"], 0) + 1
    return {
        "claim_id": claim_id,
        "targets": targets,
        "superseded_targets": superseded,
        "cluster_readings": cluster_readings,
        "n_targets": len(targets),
        "n_superseded": len(superseded),
        "n_files": len({t["artifact"] for t in targets}),
        "alignment": dict(sorted(alignment.items(), key=lambda kv: (-kv[1], kv[0]))),
        "any_weakened": any(t["claim_alignment_bucket"] == "weakened" for t in targets),
        "n_ambiguous": sum(1 for t in targets
                           if t["claim_alignment_bucket"] in _AMBIGUOUS_BUCKETS),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("claim_id", help="claim id to read the cluster for, e.g. MECH-440")
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR)
    ap.add_argument("--all-status", action="store_true",
                    help="include artifacts whose status is not 'confirmed'")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    rec = collect(args.claim_id, args.autopsy_dir, confirmed_only=not args.all_status)

    if args.json:
        print(json.dumps(rec, indent=2))
        return 0

    print(f"Granularity-debt cluster for {rec['claim_id']} "
          f"(targets whose own claim_ids name it):")
    print(f"  {rec['n_targets']} target(s) across {rec['n_files']} file(s)"
          + (f"  (+{rec['n_superseded']} superseded, not counted)"
             if rec["n_superseded"] else ""))
    if not rec["targets"]:
        print("  -- no tagging targets. The trigger does NOT fire. (Files that merely")
        print("     mention the id in prose are the claim's topical neighbourhood,")
        print("     not its recurrence cluster.)")
        return 0
    for t in rec["targets"]:
        print(f"    - {t['artifact']} [{t['scope']}] run={t['run_id'] or '?'}")
        print(f"        claim_ids: {t['claim_ids']}")
        print(f"        direction={t['recommended_evidence_direction']} "
              f"category={t['recommended_epistemic_category']}")
        print(f"        claim_alignment [{t['claim_alignment_bucket']}]: {t['claim_alignment']}")
    for t in rec["superseded_targets"]:
        print(f"    ~ {t['artifact']} [{t['scope']}] run={t['run_id'] or '?'} "
              "-- SUPERSEDED, inactive evidence, not counted")
    print("  alignment distribution: "
          + ", ".join(f"{k}={v}" for k, v in rec["alignment"].items()))
    if rec["any_weakened"]:
        print("  -- at least one target reads `weakened`: a genuine FAIL signature is")
        print("     present. Granularity debt is live IF the signatures differ")
        print("     structurally; check that before routing to /claim-synthesis.")
    elif rec["n_ambiguous"]:
        print("  -- no target reads `weakened`, BUT "
              f"{rec['n_ambiguous']} target(s) carry free-text or unstamped")
        print("     claim_alignment (bucketed `other`/`unstamped`). Read those strings")
        print("     yourself before concluding -- a weakened reading can be buried in")
        print("     prose, and this reader will not assert a clear on an unknown.")
    else:
        print("  -- NO target reads `weakened`. This is measurement or implementation")
        print("     debt, NOT granularity debt, regardless of the count. Do NOT fire the")
        print("     trigger on the count alone.")
    for cr in rec["cluster_readings"]:
        print(f"  cluster-level readings ({cr['artifact']}, not counted as targets):")
        print("    " + json.dumps(cr["readings"])[:600])
    return 0


if __name__ == "__main__":
    sys.exit(main())
