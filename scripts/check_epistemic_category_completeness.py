#!/usr/bin/env python3
"""Epistemic-category completeness audit (governance Step 3g, GOV-CAT-1).

The FOURTH sibling of the failure-autopsy standing scans, and the only one that
audits the artifacts' DATA QUALITY rather than the pattern their verdicts form:

  * GOV-CEIL-1 (check_substrate_ceiling_audit.py)   -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1 (check_diagnostic_chain_recurrence.py) -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1 (check_granularity_debt_recurrence.py) -- >=N structurally-different failures
  * GOV-CAT-1  (this file)                          -- the verdict was never RECORDED

WHY THIS AUDIT EXISTS. Two consumers key on `targets[].recommended_epistemic_category`:

  1. the re-derive brake rule R3 (`/failure-autopsy` SKILL.md Step 7) -- only a
     target recommending `substrate_ceiling` counts toward the brake threshold; and
  2. GOV-CEIL-1's ceiling-exhaustion overlay, whose hit definition (governance
     SKILL.md 6a-v-bis) is the same field.

Both read the field and skip the target when it is absent or null. So an autopsy
that genuinely reached a ceiling reading, but never stamped the field, is
SILENTLY UNCOUNTED by the very machinery built to act on it -- and nothing
anywhere reports the omission. The failure is invisible in both directions: the
artifact looks complete (its .md carries the reasoning) and the consumers look
correct (they counted every target that had a category).

Confirmed 2026-07-20: 27 of 336 confirmed autopsy targets (8.0%) across 11 files
carried no category, 12 of them claim-tagged. The gap was ONGOING, not
historical -- the two most recent instances were 3 and 1 days old. Backfilling
from each artifact's companion .md moved seven claims' ceiling counts (ARC-062
19->20, MECH-309 18->19, SD-033b 6->7, MECH-263 6->7, MECH-260 8->9, SD-032b
1->2, MECH-258 0->1); none crossed N=3, but that was luck, not a property of
the process.

The settled convention is that THE ARTIFACTS ARE THE SOURCE OF TRUTH and the fix
direction is the artifact -- do NOT widen R3 or GOV-CEIL-1 to tolerate a missing
field. This audit enforces that direction by making the omission loud at the
moment it is introduced, so the backfill never has to happen again.

BUCKETS

  missing_category   Confirmed autopsy target with a non-empty `claim_ids` but
                     no (absent or null) `recommended_epistemic_category`.
                     ACTIONABLE and STRICT-FAILING -- the target is claim-tagged,
                     so both consumers should see it and neither does. Fix by
                     reading the companion .md and recording the verdict it
                     already reached. If the reasoning genuinely supports no
                     category, record that explicitly rather than leaving the
                     field unset -- an absent field is indistinguishable from an
                     oversight, which is the whole defect this audit exists for.

  unkeyed_schema     Confirmed autopsy target that carries the SINGULAR legacy
                     key `claim_id` instead of the plural `claim_ids` that both
                     consumers read. WARN-only (never strict-fails): such a
                     target is invisible to the claim counters regardless of
                     what its category says, so stamping a category does not
                     make it countable. Surfaced because it is the same class of
                     silent invisibility and is otherwise unreported. Canonical
                     case: failure_autopsy_V3-EXQ-455a_2026-05-25 (9 targets).

  claimless_missing  Confirmed autopsy target with an EMPTY `claim_ids` and no
                     category. WARN-only. No claim counter can see it, so it
                     cannot corrupt a count -- but a claim-free diagnostic still
                     owes an explicit `not_applicable_claim_free_diagnostic` (or
                     similar) so that "no category" reads as a decision rather
                     than an omission.

Only `status: confirmed` artifacts are audited, matching both consumers.

Usage:
  python3 scripts/check_epistemic_category_completeness.py           # human report, exit 0
  python3 scripts/check_epistemic_category_completeness.py --strict  # exit 1 if any missing_category
  python3 scripts/check_epistemic_category_completeness.py --json    # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"

# The field both consumers key on.
CATEGORY_FIELD = "recommended_epistemic_category"
# The plural key both consumers read. A target using the singular `claim_id`
# instead is invisible to them no matter what its category says.
CLAIMS_FIELD = "claim_ids"
LEGACY_CLAIMS_FIELD = "claim_id"


def _target_label(target: dict, stem: str, index: int) -> str:
    """Best available human handle for a target, for the report."""
    return str(
        target.get("run_id")
        or target.get("queue_id")
        or target.get("lead_run_id")
        or target.get("lead_queue_id")
        or f"{stem}#{index}"
    )


def scan(autopsy_dir: Path) -> dict[str, list[dict]]:
    """Partition confirmed-autopsy targets by category-completeness defect.

    Returns {bucket_name: [finding, ...]}. A target lands in at most one bucket;
    a target with a category set is never reported.
    """
    buckets: dict[str, list[dict]] = {
        "missing_category": [],
        "unkeyed_schema": [],
        "claimless_missing": [],
    }
    if not autopsy_dir.is_dir():
        return buckets

    for path in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            # Unparseable artifacts are the JSON-validity gate's business, not
            # this audit's. Skip rather than fail the whole governance step.
            continue
        if str(data.get("status", "")).strip().lower() != "confirmed":
            continue

        for index, target in enumerate(data.get("targets") or []):
            if not isinstance(target, dict):
                continue
            has_category = bool(str(target.get(CATEGORY_FIELD) or "").strip())
            uses_legacy = CLAIMS_FIELD not in target and LEGACY_CLAIMS_FIELD in target
            claim_ids = target.get(CLAIMS_FIELD) or []

            finding = {
                "artifact": path.name,
                "target_index": index,
                "target": _target_label(target, path.stem, index),
                "claim_ids": (
                    [target[LEGACY_CLAIMS_FIELD]] if uses_legacy else list(claim_ids)
                ),
                "companion_md": path.with_suffix(".md").name,
            }

            if uses_legacy:
                # Reported whether or not a category is set: the defect is that
                # the counters cannot see this target at all.
                finding["has_category"] = has_category
                buckets["unkeyed_schema"].append(finding)
            elif has_category:
                continue
            elif claim_ids:
                buckets["missing_category"].append(finding)
            else:
                buckets["claimless_missing"].append(finding)

    return buckets


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="directory holding failure_autopsy_*.json")
    ap.add_argument("--json", action="store_true",
                    help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any claim-tagged target lacks a category")
    args = ap.parse_args()

    buckets = scan(args.autopsy_dir)
    n_missing = len(buckets["missing_category"])

    if args.json:
        json.dump({"buckets": buckets,
                   "n_missing_category": n_missing,
                   "n_unkeyed_schema": len(buckets["unkeyed_schema"]),
                   "n_claimless_missing": len(buckets["claimless_missing"])},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 1 if (args.strict and n_missing) else 0

    print("Epistemic-category completeness audit (GOV-CAT-1)")
    print(f"  claim-tagged, no category (ACTIONABLE): {n_missing}")
    print(f"  legacy singular claim_id  (WARN)      : {len(buckets['unkeyed_schema'])}")
    print(f"  claim-free, no category   (WARN)      : {len(buckets['claimless_missing'])}")

    if n_missing:
        print("\nACTIONABLE -- these targets are invisible to the re-derive brake (R3)")
        print("and to GOV-CEIL-1's ceiling audit. Read the companion .md and record")
        print("the verdict it already reached. Do NOT widen R3 to tolerate the gap.")
        for f in buckets["missing_category"]:
            print(f"  - {f['artifact']} [{f['target_index']}] {f['target']}")
            print(f"      claims: {', '.join(f['claim_ids'])}  ->  see {f['companion_md']}")
    else:
        print("\n  -- no claim-tagged target is missing its epistemic category.")

    for bucket, header in (
        ("unkeyed_schema",
         "WARN -- legacy singular `claim_id`; invisible to the claim counters "
         "regardless of category"),
        ("claimless_missing",
         "WARN -- claim-free target with no category; record one explicitly so "
         "'none' reads as a decision"),
    ):
        if buckets[bucket]:
            print(f"\n{header}:")
            for f in buckets[bucket]:
                print(f"  - {f['artifact']} [{f['target_index']}] {f['target']}")

    return 1 if (args.strict and n_missing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
