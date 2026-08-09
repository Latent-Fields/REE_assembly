#!/usr/bin/env python3
"""Epistemic-category completeness + validity audit (governance Step 3g, GOV-CAT-1).

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
                     owes an explicit `standard` (the settled spelling of "no
                     category applies" -- see the validity arm below) so that
                     "no category" reads as a decision rather than an omission.

  invalid_category   Confirmed autopsy target whose category is NON-EMPTY and
                     NOT IN the `claims.yaml` enum. WARN-only, and never part of
                     the `--strict` exit condition (see `--strict-validity`).
                     Added 2026-08-09; the rest of this docstring is about it.

Only `status: confirmed` artifacts are audited, matching both consumers.

--------------------------------------------------------------------------
THE VALIDITY ARM (added 2026-08-09)
--------------------------------------------------------------------------

WHY. Presence was never the whole defect. `/governance` Step 6 applies
`recommended_epistemic_category` to the claim in `claims.yaml` **verbatim**, and
until now NOTHING upstream of that write checked the value against the enum:

  | stage                                  | presence | validity |
  |----------------------------------------|----------|----------|
  | `/failure-autopsy` SKILL.md (pre-fix)  |   --     | no       |
  | GOV-CAT-1 (this file, pre-2026-08-09)  |  yes     | **no**   |
  | `/governance` Step 6 apply             |   --     | no       |
  | `validate_claims.py --strict`          |   --     | yes      |

So `--strict` at commit time was the SOLE gate, and it fires only AFTER the value
is already in the registry and only if `--strict` is actually run. Confirmed live
2026-08-08/09: INV-034, Q-021 and MECH-074d reached the `claims.yaml` write
carrying `competence_implementation_gap` and were caught only there
(`REE_assembly` `6be9e3b98f`). This file already parsed every confirmed artifact
and already read this exact field -- it was the cheapest place in the pipeline to
catch it, and it was not looking.

THE ENUM IS IMPORTED, NEVER RESTATED. `VALID_EPISTEMIC_CATEGORIES` comes from
`scripts/validate_claims.py`, the same object the `claims.yaml` ERROR gate uses,
and normalization here is `.strip().lower()` to match that gate exactly. A
restated copy of the eight values would drift from the registry gate and then
pass vacuously -- the identical failure mode `remote_pytest.sh`'s
`_selftest_git_exclude` exists to prevent by sharing `RSYNC_EXCLUDES` rather than
restating the patterns. A failed import is LOUD (`SystemExit`), never a fallback
to a local copy.

FIELDS SWEPT. `targets[].recommended_epistemic_category` and
`recommended_epistemic_category_per_claim` (a `{claim_id: category}` map), the
latter both on a target and at file level. The per-claim map is the sharper of
the two for governance, since it is what a multi-claim target applies.

--------------------------------------------------------------------------
BACKLOG EXCLUSION -- and why it is the hard part
--------------------------------------------------------------------------

A naive validity arm reports **674 instances across 208 of the 376 confirmed
artifacts** on its first run (measured 2026-08-09; the corpus audit
`evidence/planning/epistemic_category_vocabulary_audit_2026-08-09.md` counts 683
over a slightly wider corpus definition). 57% of all value-instances are out of
enum, spread over 62 distinct values. That is the corpus NORM, not a stray typo.
Reporting it every cycle is how a standing scan gets ignored -- GOV-FROZEN-1's
design notes name ALARM FATIGUE as itself a Goodhart vector.

The values are inert for every current consumer (all 62 sit outside
`_EPI_SUPPRESS_PROPOSAL`), so the exposure is PROSPECTIVE: a future governance
session applying one. The backlog is not to be swept -- CLAUDE.md's standing
guidance on this corpus is per-artifact re-attribution with a stated reason,
never a corpus-wide rewrite. So the exclusion mechanism has to silence 674
historical instances WITHOUT touching a single artifact, while still firing on
the next new one.

TWO MECHANISMS, exactly mirroring GOV-DRY-1 (`check_dry_run_adjudication_leak.py`),
which faces the same shape and solves it with a seed table for the pre-existing
backlog plus an in-band marker for future adjudications:

  1. A BASELINE SNAPSHOT (`evidence/planning/epistemic_category_enum_backlog.v1.json`)
     -- GOV-DRY-1's `_ADJUDICATED_CITATIONS` role, EXTERNALIZED to a file purely
     because 674 entries will not live as a code literal the way its ~20 do. Same
     semantics: HIT-SCOPED, keyed `{artifact stem: [normalized value, ...]}`.

     Hit-scoped is the load-bearing property, and it is why a plain date cutoff
     was rejected. A cutoff excludes by FILE IDENTITY, so it permanently deafens
     every pre-cutoff artifact: a bad value added to an old file tomorrow is
     silently missed forever. The baseline excludes by (file, VALUE), so a NEW
     out-of-enum value in a baselined file still fires, and a brand-new artifact
     -- the actual prospective risk -- has no baseline entry at all and fires in
     full. Same rule GOV-DIAG-1 states as "a marker can quiet the chain it names;
     it can never permanently deafen the token".

     KNOWN RESIDUAL, stated rather than hidden: re-using a token ALREADY
     baselined for that same file at a new target does not fire. This is exactly
     GOV-DRY-1's residual (its citation exclusions are keyed artifact+run_id, not
     artifact+occurrence) and is accepted for the same reason -- the marginal
     signal of an Nth instance of a token the file already carries is near zero,
     and index-keying would re-fire the whole file on any target insertion.

     Regeneration requires the explicit `--write-baseline`, which prints what it
     is about to silence. It is never written as a side effect of a report run.

  2. An IN-BAND MARKER for future adjudications, so the next one needs no code
     change and no baseline regeneration (regenerating would silently absorb
     everything else accumulated since). A `failure_autopsy_*.json` may carry a
     top-level block, following GOV-DRY-1's `dry_run_citation_metabolized` and
     GOV-DIAG-1's `diagnostic_recurrence_metabolized` exactly:

         "epistemic_category_metabolized": {
           "date": "2026-08-10",
           "metabolized_hits": ["measurement_test_design_defect"],   # REQUIRED
           "note": "why this value is recorded here and what was decided"
         }

     `metabolized_hits` lists the CATEGORY VALUES adjudicated for this artifact.
     It is REQUIRED for the same reason both precedents require it: a marker
     missing it is IGNORED and REPORTED AS MALFORMED -- it fails loud rather than
     silently blanket-silencing the file. A new, unlisted out-of-enum value in
     the same artifact still fires.

WARN-ONLY BY DEFAULT, and `--strict` IS UNCHANGED. `--strict` still exits 1 on
`missing_category` alone, so no existing caller's exit contract moves. Validity
gets its own opt-in `--strict-validity`. Rationale: this arm promotes and demotes
nothing, recommends only governance writes, and sits on top of a backlog whose
exclusion is a judgement call -- coupling it to the pre-existing gate would let
that judgement wedge an unrelated blocking check.

PREVENTION AT SOURCE IS SEPARATE AND ALREADY LANDED: `/failure-autopsy` SKILL.md
now states the enum at the field definition, routes failure-mode diagnoses to
`four_layer_diagnosis` / `recommended_epistemic_category_note` instead, and
spells "no category applies" as `standard` (`REE_Working` `18313837`, both
mirrors). This arm is the NET, not the prevention.

Usage:
  python3 scripts/check_epistemic_category_completeness.py            # human report, exit 0
  python3 scripts/check_epistemic_category_completeness.py --strict   # exit 1 if any missing_category
  python3 scripts/check_epistemic_category_completeness.py --strict-validity
  python3 scripts/check_epistemic_category_completeness.py --json     # machine-readable
  python3 scripts/check_epistemic_category_completeness.py --show-baselined
  python3 scripts/check_epistemic_category_completeness.py --write-baseline   # deliberate, loud
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"
DEFAULT_BASELINE = (
    REPO_ROOT / "evidence" / "planning" / "epistemic_category_enum_backlog.v1.json"
)

# The enum is IMPORTED from the same module that gates claims.yaml, never
# restated here -- a local copy of the eight values drifts from the registry gate
# and then passes vacuously. A failed import is loud, never a fallback copy.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from validate_claims import VALID_EPISTEMIC_CATEGORIES  # noqa: E402
except ImportError as exc:  # pragma: no cover - environment problem, be loud
    raise SystemExit(
        "cannot import VALID_EPISTEMIC_CATEGORIES from scripts/validate_claims.py: "
        "%s (do NOT restate the enum here -- a restated copy drifts and then "
        "passes vacuously)" % exc
    )

# The field both consumers key on.
CATEGORY_FIELD = "recommended_epistemic_category"
# The per-claim map governance applies for a multi-claim target. Swept for
# validity on a target and at file level.
PER_CLAIM_FIELD = "recommended_epistemic_category_per_claim"
# The plural key both consumers read. A target using the singular `claim_id`
# instead is invisible to them no matter what its category says.
CLAIMS_FIELD = "claim_ids"
LEGACY_CLAIMS_FIELD = "claim_id"

# In-band, hit-scoped metabolization marker key on a failure_autopsy_*.json.
# Mirrors GOV-DRY-1's `dry_run_citation_metabolized` and GOV-DIAG-1's
# `diagnostic_recurrence_metabolized`, including the REQUIRED hits list.
METABOLIZED_KEY = "epistemic_category_metabolized"


def _norm(value) -> str:
    """Normalize a category exactly as validate_claims.py's ERROR gate does."""
    return str(value or "").strip().lower()


def load_baseline(path: Path) -> dict[str, set[str]]:
    """Read the backlog snapshot as {artifact stem: {normalized value, ...}}.

    A missing / unreadable / malformed baseline yields an EMPTY exclusion set, so
    the failure direction is "report the backlog loudly", never "silently pass".
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, dict):
        return {}
    out: dict[str, set[str]] = {}
    for stem, values in entries.items():
        if isinstance(values, str):
            values = [values]
        if not isinstance(values, (list, tuple)):
            continue
        norm = {_norm(v) for v in values if _norm(v)}
        if norm:
            out[str(stem)] = norm
    return out


def _load_marker(path: Path, data: dict) -> tuple[set[str], dict | None]:
    """Read an artifact's in-band metabolization marker.

    Returns (metabolized_values, malformed_record). A marker without a non-empty
    `metabolized_hits` is IGNORED and reported -- it never blanket-silences.
    """
    marker = data.get(METABOLIZED_KEY)
    if not isinstance(marker, dict):
        return set(), None
    hits = marker.get("metabolized_hits")
    if isinstance(hits, str):
        hits = [hits]
    if not isinstance(hits, (list, tuple)):
        hits = []
    norm = {_norm(h) for h in hits if _norm(h)}
    if not norm:
        return set(), {
            "artifact": path.name,
            "reason": "missing or empty metabolized_hits",
            "date": marker.get("date"),
        }
    return norm, None


def _category_instances(data: dict, stem: str) -> list[dict]:
    """Every non-empty category VALUE an artifact records, with its location.

    Covers `targets[].recommended_epistemic_category`, the per-claim map on a
    target, and the same map at file level (no target of its own).
    """
    found: list[dict] = []

    def _add(raw, index, label, field, claim):
        if _norm(raw):
            found.append({"value": str(raw), "normalized": _norm(raw),
                          "target_index": index, "target": label,
                          "field": field, "claim": claim})

    def _add_map(node, index, label):
        if isinstance(node, dict):
            for claim, raw in node.items():
                _add(raw, index, label, PER_CLAIM_FIELD, str(claim))

    for index, target in enumerate(data.get("targets") or []):
        if not isinstance(target, dict):
            continue
        label = _target_label(target, stem, index)
        _add(target.get(CATEGORY_FIELD), index, label, CATEGORY_FIELD, None)
        _add_map(target.get(PER_CLAIM_FIELD), index, label)

    _add_map(data.get(PER_CLAIM_FIELD), None, "<file-level>")
    return found


def _target_label(target: dict, stem: str, index: int) -> str:
    """Best available human handle for a target, for the report."""
    return str(
        target.get("run_id")
        or target.get("queue_id")
        or target.get("lead_run_id")
        or target.get("lead_queue_id")
        or f"{stem}#{index}"
    )


def scan(autopsy_dir: Path,
         baseline: dict[str, set[str]] | None = None) -> dict[str, list[dict]]:
    """Partition confirmed-autopsy targets by category-completeness defect.

    Returns {bucket_name: [finding, ...]}. For the COMPLETENESS buckets a target
    lands in at most one, and a target with a category set is never reported.
    The VALIDITY buckets are computed independently and overlap with them by
    design -- e.g. a legacy-`claim_id` target can also carry a bad value; those
    are two different defects and suppressing either would hide one of them.
    """
    baseline = baseline or {}
    buckets: dict[str, list[dict]] = {
        "missing_category": [],
        "unkeyed_schema": [],
        "claimless_missing": [],
        # validity arm
        "invalid_category": [],
        "invalid_baselined": [],
        "invalid_metabolized": [],
        "malformed_markers": [],
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
        if not isinstance(data, dict):
            continue
        if str(data.get("status", "")).strip().lower() != "confirmed":
            continue

        # --- validity arm ------------------------------------------------
        # Hit-scoped exclusion: baselined/metabolized VALUES for THIS artifact
        # only, so a new out-of-enum value in the same file still fires.
        metabolized, bad_marker = _load_marker(path, data)
        if bad_marker:
            buckets["malformed_markers"].append(bad_marker)
        baselined = baseline.get(path.stem, set())
        for inst in _category_instances(data, path.stem):
            if inst["normalized"] in VALID_EPISTEMIC_CATEGORIES:
                continue
            finding = {
                "artifact": path.name,
                "target_index": inst["target_index"],
                "target": inst["target"],
                "field": inst["field"],
                "claim": inst["claim"],
                "value": inst["value"],
                "companion_md": path.with_suffix(".md").name,
            }
            if inst["normalized"] in metabolized:
                buckets["invalid_metabolized"].append(finding)
            elif inst["normalized"] in baselined:
                buckets["invalid_baselined"].append(finding)
            else:
                buckets["invalid_category"].append(finding)

        # --- completeness arm --------------------------------------------
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


def build_baseline(autopsy_dir: Path) -> dict:
    """Snapshot every out-of-enum value currently in the confirmed corpus.

    Keyed {artifact stem: [normalized value, ...]} -- hit-scoped, so a NEW value
    in a snapshotted artifact still fires. Deliberately built from an
    exclusion-free scan: the baseline records what IS, not what a previous
    baseline already forgave.
    """
    raw = scan(autopsy_dir, baseline={})
    entries: dict[str, set[str]] = {}
    n = 0
    for f in (raw["invalid_category"] + raw["invalid_baselined"]
              + raw["invalid_metabolized"]):
        stem = f["artifact"][:-len(".json")] if f["artifact"].endswith(".json") \
            else f["artifact"]
        entries.setdefault(stem, set()).add(_norm(f["value"]))
        n += 1
    return {
        "note": (
            "GOV-CAT-1 validity-arm backlog snapshot. Hit-scoped exclusion keyed "
            "(artifact stem, normalized category value): a NEW out-of-enum value "
            "in a listed artifact still fires, and a new artifact is not listed "
            "at all. Regenerate ONLY with --write-baseline, and only when you "
            "have decided the current findings are historical -- regenerating "
            "absorbs everything accumulated since. Prefer the in-band "
            "`epistemic_category_metabolized` marker for a single adjudication."
        ),
        "n_instances": n,
        "n_artifacts": len(entries),
        "n_distinct_values": len({v for vs in entries.values() for v in vs}),
        "entries": {k: sorted(v) for k, v in sorted(entries.items())},
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="directory holding failure_autopsy_*.json")
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="backlog snapshot excluding pre-existing out-of-enum values")
    ap.add_argument("--json", action="store_true",
                    help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any claim-tagged target lacks a category "
                         "(UNCHANGED -- validity findings never affect this)")
    ap.add_argument("--strict-validity", action="store_true",
                    help="exit 1 if any non-baselined out-of-enum category is found")
    ap.add_argument("--show-baselined", action="store_true",
                    help="list the excluded backlog instances in full")
    ap.add_argument("--write-baseline", action="store_true",
                    help="REGENERATE the backlog snapshot from the corpus and exit")
    args = ap.parse_args()

    if args.write_baseline:
        snap = build_baseline(args.autopsy_dir)
        args.baseline.parent.mkdir(parents=True, exist_ok=True)
        args.baseline.write_text(
            json.dumps(snap, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        print("WROTE %s" % args.baseline)
        print("  SILENCED %d out-of-enum instance(s) across %d artifact(s), "
              "%d distinct value(s)."
              % (snap["n_instances"], snap["n_artifacts"], snap["n_distinct_values"]))
        print("  This is hit-scoped: a NEW value in any listed artifact still fires,")
        print("  and a NEW artifact is not listed at all. Review the diff before")
        print("  committing -- regeneration absorbs everything accumulated since the")
        print("  last one. For a single adjudication prefer the in-band")
        print("  `%s` marker instead." % METABOLIZED_KEY)
        return 0

    baseline = load_baseline(args.baseline)
    buckets = scan(args.autopsy_dir, baseline)
    n_missing = len(buckets["missing_category"])
    n_invalid = len(buckets["invalid_category"])
    n_excluded = len(buckets["invalid_baselined"]) + len(buckets["invalid_metabolized"])
    n_bad_marker = len(buckets["malformed_markers"])

    def _rc() -> int:
        if args.strict and n_missing:
            return 1
        if args.strict_validity and n_invalid:
            return 1
        return 0

    if args.json:
        json.dump({"buckets": buckets,
                   "n_missing_category": n_missing,
                   "n_unkeyed_schema": len(buckets["unkeyed_schema"]),
                   "n_claimless_missing": len(buckets["claimless_missing"]),
                   "n_invalid_category": n_invalid,
                   "n_invalid_excluded": n_excluded,
                   "n_malformed_markers": n_bad_marker,
                   "baseline_path": str(args.baseline),
                   "baseline_artifacts": len(baseline),
                   "valid_categories": sorted(VALID_EPISTEMIC_CATEGORIES)},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
        return _rc()

    print("Epistemic-category completeness + validity audit (GOV-CAT-1)")
    print(f"  claim-tagged, no category (ACTIONABLE): {n_missing}")
    print(f"  out-of-enum value, new    (ACTIONABLE): {n_invalid}")
    print(f"  legacy singular claim_id  (WARN)      : {len(buckets['unkeyed_schema'])}")
    print(f"  claim-free, no category   (WARN)      : {len(buckets['claimless_missing'])}")
    print(f"  out-of-enum, baselined/metabolized    : {n_excluded}"
          f"  (baseline: {len(baseline)} artifact(s))")

    if n_missing:
        print("\nACTIONABLE -- these targets are invisible to the re-derive brake (R3)")
        print("and to GOV-CEIL-1's ceiling audit. Read the companion .md and record")
        print("the verdict it already reached. Do NOT widen R3 to tolerate the gap.")
        for f in buckets["missing_category"]:
            print(f"  - {f['artifact']} [{f['target_index']}] {f['target']}")
            print(f"      claims: {', '.join(f['claim_ids'])}  ->  see {f['companion_md']}")
    else:
        print("\n  -- no claim-tagged target is missing its epistemic category.")

    if n_invalid:
        print("\nACTIONABLE -- out-of-enum `%s`. /governance Step 6"
              % CATEGORY_FIELD)
        print("applies this field to claims.yaml VERBATIM, where validate_claims.py")
        print("--strict raises an ERROR -- but only AFTER the value is in the registry.")
        print("Fix the ARTIFACT: a failure-mode diagnosis belongs in")
        print("`four_layer_diagnosis` / `recommended_epistemic_category_note`, and")
        print("'no category applies' is spelled `standard`. Valid values: %s"
              % ", ".join(sorted(VALID_EPISTEMIC_CATEGORIES)))
        for f in buckets["invalid_category"]:
            where = f["field"] + (f" [{f['claim']}]" if f["claim"] else "")
            idx = "-" if f["target_index"] is None else f["target_index"]
            print(f"  - {f['artifact']} [{idx}] {f['target']}")
            print(f"      {where} = {f['value']!r}  ->  see {f['companion_md']}")
    else:
        print("\n  -- no new out-of-enum epistemic category in the confirmed corpus.")

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

    if n_bad_marker:
        print("\nWARN -- malformed %s marker(s), IGNORED (never blanket-silences):"
              % METABOLIZED_KEY)
        for m in buckets["malformed_markers"]:
            print(f"  - {m['artifact']}: {m['reason']}")

    if n_excluded:
        # Not printed in full by default: the backlog is ~674 instances and
        # dumping it every cycle is the alarm fatigue the exclusion exists to
        # avoid. Summarised so nothing is hidden; --show-baselined for the list.
        by_value: dict[str, int] = {}
        for f in buckets["invalid_baselined"] + buckets["invalid_metabolized"]:
            by_value[_norm(f["value"])] = by_value.get(_norm(f["value"]), 0) + 1
        top = sorted(by_value.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
        print("\nexcluded as historical backlog (no action owed; %d instance(s), "
              "%d distinct value(s))" % (n_excluded, len(by_value)))
        print("  top: %s" % ", ".join("%s x%d" % (v, c) for v, c in top))
        print("  hit-scoped: a NEW value in any of these artifacts still fires.")
        if args.show_baselined:
            for f in buckets["invalid_baselined"] + buckets["invalid_metabolized"]:
                idx = "-" if f["target_index"] is None else f["target_index"]
                print(f"  - {f['artifact']} [{idx}] {f['field']} = {f['value']!r}")

    return _rc()


if __name__ == "__main__":
    raise SystemExit(main())
