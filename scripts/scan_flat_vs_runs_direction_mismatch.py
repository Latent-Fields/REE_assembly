#!/usr/bin/env python3
"""One-time scan: pair each evidence/experiments/<run_id>.json flat manifest
with its canonical evidence/experiments/<experiment_type>/runs/<run_id>/manifest.json
and triage indexer-invisible evidence_direction reclassifications.

Canonical incident: v3_exq_573_arc065_bias_scale_sweep had a 2026-05-16 governance
reclassification of all four tagged claims to non_contributory applied to the flat
JSON only; the canonical runs manifest (which is what build_experiment_indexes.py
reads) kept stale weakens/does_not_support directions. Fixed in commit c4d080082e
2026-05-31; this scan checks for the same shape elsewhere.

Output: prints a triage table + category counts. With --apply, mirrors flat-only
reclassifications (category a) onto the canonical runs manifest. Conservative:
only the three evidence_direction fields are touched.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EVID = REPO_ROOT / "evidence" / "experiments"

# Top-level flat JSONs we deliberately skip (indexes / planning, not experiment manifests).
SKIP_NAMES = {
    "claim_evidence.v1.json",
    "claim_evidence_matrix.v1.json",
    "review_tracker.json",
    "runner_status.json",
    "INDEX.json",  # not present, but guard
}


def iter_flat_manifests():
    for p in sorted(EVID.glob("*.json")):
        if p.name in SKIP_NAMES:
            continue
        yield p


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        return None


def canonical_runs_path(flat):
    et = flat.get("experiment_type")
    rid = flat.get("run_id")
    if not et or not rid:
        return None
    return EVID / et / "runs" / rid / "manifest.json"


def classify(flat, runs):
    """Return (category, fields_only_in_flat, fields_only_in_runs, fields_disagree)."""
    f_dir = flat.get("evidence_direction")
    r_dir = runs.get("evidence_direction")
    f_per = flat.get("evidence_direction_per_claim") or {}
    r_per = runs.get("evidence_direction_per_claim") or {}
    f_note = flat.get("evidence_direction_note")
    r_note = runs.get("evidence_direction_note")

    # Per-claim equality is a strict dict comparison
    dir_match = (f_dir == r_dir)
    per_match = (f_per == r_per)
    # Treat missing-vs-empty as equal for note presence
    fn = (f_note or "").strip()
    rn = (r_note or "").strip()
    note_match = (fn == rn)

    if dir_match and per_match and note_match:
        return ("d", None, None, None)

    # Detect direction-level disagreement (both non-null, distinct)
    if f_dir and r_dir and f_dir != r_dir:
        return ("c", None, None, ("evidence_direction", f_dir, r_dir))

    # Per-claim disagreement on overlapping keys with distinct values
    per_keys = set(f_per) & set(r_per)
    per_disagree = {k: (f_per[k], r_per[k]) for k in per_keys if f_per[k] != r_per[k]}
    if per_disagree:
        return ("c", None, None, ("evidence_direction_per_claim", per_disagree, None))

    # If runs has reclassification content the flat lacks: category (b)
    runs_has_more = False
    if r_dir and not f_dir:
        runs_has_more = True
    if r_per and not f_per:
        runs_has_more = True
    if rn and not fn:
        runs_has_more = True
    # Per-claim keys present only in runs that constitute a richer override
    runs_only_keys = set(r_per) - set(f_per)
    if runs_only_keys:
        runs_has_more = True

    # If flat has reclassification content the runs manifest lacks: category (a)
    flat_has_more = False
    if f_dir and (not r_dir or f_dir != r_dir):
        flat_has_more = True
    if f_per and (not r_per):
        flat_has_more = True
    if fn and not rn:
        flat_has_more = True
    flat_only_keys = set(f_per) - set(r_per)
    if flat_only_keys:
        flat_has_more = True

    # Prefer (a) when both look richer; this is the case the script can safely fix.
    # Genuine "both have distinct extras" still gets (a) only if flat is strictly more
    # complete than runs along these three fields.
    if flat_has_more and not runs_has_more:
        return ("a", (f_dir, f_per, fn), None, None)
    if runs_has_more and not flat_has_more:
        return ("b", None, (r_dir, r_per, rn), None)
    # If both have extras and neither strictly dominates, surface as (c) for human review.
    return ("c", None, None, ("mixed_extras", (f_dir, f_per, fn), (r_dir, r_per, rn)))


def apply_category_a(runs_path, runs_manifest, f_dir, f_per, f_note):
    """Mirror the three fields from flat into runs; preserve everything else."""
    if f_dir is not None:
        runs_manifest["evidence_direction"] = f_dir
    if f_per:
        runs_manifest["evidence_direction_per_claim"] = f_per
    if f_note:
        runs_manifest["evidence_direction_note"] = f_note
    with open(runs_path, "w") as f:
        json.dump(runs_manifest, f, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Mirror category-(a) flat reclassifications onto runs manifests.")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    scanned = 0
    no_runs = 0  # flat has no canonical runs manifest (skipped from analysis)
    counts = {"a": 0, "b": 0, "c": 0, "d": 0}
    a_entries = []
    b_entries = []
    c_entries = []

    for flat_path in iter_flat_manifests():
        flat = load_json(flat_path)
        if not flat or "run_id" not in flat:
            continue
        runs_path = canonical_runs_path(flat)
        if not runs_path or not runs_path.exists():
            no_runs += 1
            if args.verbose:
                print(f"  [no-runs-manifest] {flat_path.name}")
            continue
        runs = load_json(runs_path)
        if runs is None:
            continue
        scanned += 1
        cat, a_payload, b_payload, c_payload = classify(flat, runs)
        counts[cat] += 1
        rid = flat["run_id"]
        if cat == "a":
            a_entries.append((rid, flat_path, runs_path, runs, a_payload, flat))
        elif cat == "b":
            b_entries.append((rid, flat_path, runs_path, b_payload, flat, runs))
        elif cat == "c":
            c_entries.append((rid, flat_path, runs_path, c_payload, flat, runs))

    print("=" * 72)
    print(f"Flat manifests scanned: {scanned}")
    print(f"Skipped (no canonical runs manifest exists): {no_runs}")
    print(f"Category (a) flat-only reclassification: {counts['a']}")
    print(f"Category (b) runs-only reclassification: {counts['b']}")
    print(f"Category (c) genuine disagreement:        {counts['c']}")
    print(f"Category (d) agree (skip):                 {counts['d']}")
    print("=" * 72)

    if a_entries:
        print("\n--- Category (a): flat reclassification missing from runs ---")
        print(f"{'run_id':<70} | flat_dir            | runs_dir            | per_claim_keys     | note?")
        for rid, fp, rp, runs, payload, flat in a_entries:
            f_dir, f_per, f_note = payload
            r_dir = runs.get("evidence_direction") or "-"
            per_keys = ",".join(sorted((f_per or {}).keys())) or "-"
            note_flag = "yes" if f_note else "no"
            print(f"{rid:<70} | {str(f_dir or '-'):<19} | {str(r_dir):<19} | {per_keys:<18} | {note_flag}")

    if b_entries:
        print("\n--- Category (b): runs reclassification missing from flat (FLAG ONLY, do not mutate) ---")
        for rid, fp, rp, payload, flat, runs in b_entries:
            r_dir = runs.get("evidence_direction") or "-"
            f_dir = flat.get("evidence_direction") or "-"
            r_per_keys = ",".join(sorted((runs.get("evidence_direction_per_claim") or {}).keys())) or "-"
            r_note = "yes" if (runs.get("evidence_direction_note") or "").strip() else "no"
            print(f"{rid:<70} | flat={f_dir:<14} | runs={r_dir:<14} | runs_per_claim={r_per_keys:<18} | runs_note={r_note}")

    if c_entries:
        print("\n--- Category (c): genuine disagreement (FLAG ONLY, human review) ---")
        for rid, fp, rp, payload, flat, runs in c_entries:
            kind = payload[0] if payload else "?"
            print(f"{rid}")
            print(f"  kind     = {kind}")
            print(f"  flat_dir = {flat.get('evidence_direction')}")
            print(f"  runs_dir = {runs.get('evidence_direction')}")
            print(f"  flat_per = {flat.get('evidence_direction_per_claim')}")
            print(f"  runs_per = {runs.get('evidence_direction_per_claim')}")
            print(f"  flat_note_present = {bool((flat.get('evidence_direction_note') or '').strip())}")
            print(f"  runs_note_present = {bool((runs.get('evidence_direction_note') or '').strip())}")

    if args.apply and a_entries:
        print("\n--- Applying category (a) mirrors ---")
        for rid, fp, rp, runs, payload, flat in a_entries:
            f_dir, f_per, f_note = payload
            apply_category_a(rp, runs, f_dir, f_per, f_note)
            print(f"  mirrored: {rid}")
        print(f"Applied {len(a_entries)} mirror(s).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
