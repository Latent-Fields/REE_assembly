#!/usr/bin/env python3
"""Backfill `failure_record[].run_role` across `evidence/planning/substrate_queue.json`.

WHY THIS EXISTS
---------------
`generate_inter_governance_workset._substrate_landing_cutoff` dates a substrate
landing from `implemented_utc` AND from the run stamps in `failure_record[].run_id`,
on the assumption that a failure_record run is a POST-build validation experiment
(and therefore an UPPER bound on the landing instant). Measured on the live corpus
2026-08-15: of the 97 failure_record items that can be dated against their own
entry's `implemented_utc`, **37 (38%) PREDATE it** -- they are gap-CHARACTERISATION
runs that motivated the build, not validation runs against it. substrate_queue's own
`_schema_notes` describe a failure_record item that way too, so the two readings
genuinely disagreed.

A pre-build run used as a landing bound sets the cutoff EARLIER than the true
landing, so stale pre-substrate evidence counts as "a retest ran since the substrate
landed" -- a WRONG HOLD, which silently tells /governance a retest happened when it
did not. `run_role` makes the distinction explicit per item so the generator can use
POST-build runs only.

DERIVATION (deterministic, and recorded per item in `run_role_basis`)
---------------------------------------------------------------------
For each failure_record item, in order -- the first rule that fires wins:

  R1  the ITEM carries its own `substrate_built_utc`   -> compare the run stamp to it.
  R2  the run_id carries no parseable timestamp        -> `unknown` (it can never be
      a landing bound anyway, since the generator cannot date it either).
  R3  the ENTRY has a datable landing stamp            -> compare the run stamp to it.
  R4  no landing stamp anywhere, and the entry does not claim to have landed
                                                       -> `pre_build` (there is no
      build for a run to have validated).
  R5  otherwise (landed, but nothing dates the landing) -> `unknown`.

ERROR DIRECTION, which is why the heuristics below are acceptable -- and it is NOT
one-sided. `unknown` and `pre_build` are both EXCLUDED from the generator's cutoff,
and since the cutoff is a MAX, excluding a candidate moves it EARLIER or to ABSENT.
So a genuine post-build run left unmarked pulls the cutoff too early (risking a hold
that names a run which predates the landing -- bounded, because FM11 renders
`blocked` with that run NAMED for a human, never suppressed), while a
gap-characterisation run wrongly marked `post_build` pushes it too late (the original
FM11 re-staging pathology). Full argument in `_substrate_landing_cutoff`'s docstring.

The rules below therefore aim for the truthful label rather than a one-sided bias,
with two guardrails on the `post_build` side, which is the one a heuristic can most
easily get wrong:

  * free-text landing dates are accepted only from explicit
    LANDED / IMPLEMENTED / BUILT / VALIDATED / CLEARED phrases -- never from
    "queued" / "planned" / "owed" prose.
  * a bare `YYYY-MM-DD` landing date is read as 00:00Z on that day, so a same-day run
    comes out `post_build`. That is the one place the bias runs the wrong way; such
    items are flagged `same_day -- audit` in `run_role_basis` so a reader can check
    them (10 of 281 on the 2026-08-15 corpus).

WHY R3 TAKES THE EARLIEST LANDING DATE, NOT THE LATEST.
"Latest wins" is the more conservative-looking choice and was tried first; it is
wrong here for a specific, measured reason. These entries accumulate prose across
months, and later AMEND dates ("bug FIXED 2026-08-14") sit in the same fields as the
original landing. Taking the latest read MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION
as landing 2026-08-14 when its own `implementation_note` opens "IMPLEMENTED
2026-08-02" -- which relabelled the 861a validation run as `pre_build`, erased
ARC-045's cutoff entirely, and with it the coverage by v3_exq_436d that is the
confirmed FM11 incident (three re-staged, GC-reaped worktrees). So R3 answers "when
did this entry's substrate FIRST exist", which is what a failure_record item is
normally recorded against.

The phased-build case that "earliest" gets wrong is handled by R1, not by the
heuristic: an item whose relevant build is a LATER phase carries its own
`substrate_built_utc`, which overrides everything. SD-035's v3_exq_894a is the live
worked example -- it postdates the 2026-04-21 BLA/CeA landing but predates the
2026-08-09 trainable-attribution-head build it motivated, and only its own
`substrate_built_utc` can say so. When a governance session adds a failure_record
item to a multi-phase entry, setting `substrate_built_utc` on the item is what keeps
this correct.

USAGE
    python3 scripts/backfill_failure_record_run_role.py [--apply] [--report]

Without `--apply` it prints the derivation and writes nothing.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE_PATH = os.path.join(REPO, "evidence", "planning", "substrate_queue.json")

RUN_ROLE_PRE = "pre_build"
RUN_ROLE_POST = "post_build"
RUN_ROLE_UNKNOWN = "unknown"

_RUN_STAMP_RE = re.compile(r"(\d{8}T\d{6}Z)")
_DATE_ONLY_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})$")

# Entry-level fields that hold a machine-readable landing instant.
_LANDING_FIELDS = (
    "implemented_utc",
    "landed_utc",
    "implemented_at",
    "implementation_utc",
    "validated_utc",
    "amend_implemented_utc",
    "learned_binder_implemented_utc",
    "amended_utc",
    "collapse_decided_utc",
)
# Nested containers that carry a landing instant on some entries.
_NESTED_LANDING_CONTAINERS = (
    "implementation_log",
    "harm_pathway_stabilization_amend_2026_06_16",
    "residual_foraging_competence_amend_2026_06_05",
)
_NESTED_LANDING_KEYS = ("landed_utc", "utc", "implemented_utc", "validated_utc")

# Free-text landing phrases. Deliberately narrow: only phrasings that assert the
# build LANDED, never "queued"/"planned"/"owed".
_FREETEXT_LANDING_RE = re.compile(
    r"(?:IMPLEMENTED|LANDED|BUILT|VALIDATED|CLEARED)"
    r"[^.\n]{0,40}?(\d{4})[-_](\d{2})[-_](\d{2})",
    re.IGNORECASE,
)
_FREETEXT_FIELDS = (
    "status",
    "implementation_note",
    "implementation_note_update",
    "implemented_note",
    "status_note",
    "validation_note",
    "landing_status",
    "implementation_landed",
)

# Tokens that mean "this entry claims a build exists". Used only to separate R4
# (nothing landed -> pre_build) from R5 (landed but undatable -> unknown).
_LANDED_TOKEN_RE = re.compile(
    r"implement|\bland(?:ed|ing)?\b|validat|\bbuilt\b|\bdone\b|complete|subsumed|superseded",
    re.IGNORECASE,
)
_LANDED_SCAN_FIELDS = (
    "status",
    "implementation_status",
    "implementation_note",
    "implemented_session",
    "implemented_by",
    "implemented_by_session",
    "landing_status",
    "implementation_landed",
    "implementation_log",
)


def parse_ts(value: object) -> datetime | None:
    """`2026-08-04T07:15:41Z`, a `...20260804T071541Z...` run stamp, or `2026-08-04`.

    The date-only form is NOT accepted by the generator's own parser; it is
    accepted here because a bare date is still a usable landing bound for the
    backfill's comparison, and reading it as 00:00Z is the conservative direction
    for a pre/post split only in the sense noted in the module docstring
    (same-day cases are flagged).
    """
    s = str(value or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    if _DATE_ONLY_RE.match(s):
        # The regex only pins the SHAPE -- "2026-13-45" matches it and is not a
        # date, so the parse still has to be guarded.
        try:
            return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    m = _RUN_STAMP_RE.search(s)
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y%m%dT%H%M%SZ").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            return None
    return None


def _iter_nested(value: object):
    if isinstance(value, dict):
        yield value
        for v in value.values():
            yield from _iter_nested(v)
    elif isinstance(value, list):
        for v in value:
            yield from _iter_nested(v)


def entry_landing(entry: dict) -> tuple[datetime | None, str]:
    """EARLIEST datable landing instant on an entry, and how it was derived.

    Earliest, not latest, on purpose -- see "WHY R3 TAKES THE EARLIEST LANDING
    DATE" in the module docstring. Returns (None, "") when nothing dates a landing.
    """
    best: datetime | None = None
    basis = ""

    def offer(when: datetime | None, label: str) -> None:
        nonlocal best, basis
        if when is not None and (best is None or when < best):
            best, basis = when, label

    for field in _LANDING_FIELDS:
        offer(parse_ts(entry.get(field)), field)

    for container in _NESTED_LANDING_CONTAINERS:
        for node in _iter_nested(entry.get(container)):
            for key in _NESTED_LANDING_KEYS:
                offer(parse_ts(node.get(key)), f"{container}.{key}")

    for field in _FREETEXT_FIELDS:
        text = entry.get(field)
        if not isinstance(text, str):
            continue
        for m in _FREETEXT_LANDING_RE.finditer(text):
            offer(parse_ts("%s-%s-%s" % m.groups()), f"{field}:freetext")

    return best, basis


def entry_claims_a_build(entry: dict) -> bool:
    """True if the entry asserts anywhere that a build exists.

    Only separates R4 from R5; both outcomes are excluded from the cutoff, so a
    misread here changes the recorded LABEL but never the generator's behaviour.
    """
    for field in _LANDED_SCAN_FIELDS:
        if _LANDED_TOKEN_RE.search(json.dumps(entry.get(field), default=str)):
            return True
    return False


def classify(entry: dict, rec: dict) -> tuple[str, str]:
    """(run_role, run_role_basis) for one failure_record item."""
    run = parse_ts(rec.get("run_id"))
    own = parse_ts(rec.get("substrate_built_utc"))
    if own is not None and run is not None:
        role = RUN_ROLE_PRE if run < own else RUN_ROLE_POST
        return role, "R1 item.substrate_built_utc"
    if run is None:
        return RUN_ROLE_UNKNOWN, "R2 run_id carries no parseable timestamp"

    landed, basis = entry_landing(entry)
    if landed is not None:
        if run < landed:
            return RUN_ROLE_PRE, f"R3 run < entry.{basis}"
        same_day = run.date() == landed.date()
        return RUN_ROLE_POST, "R3 run > entry.%s%s" % (
            basis, " (same_day -- audit)" if same_day else ""
        )

    if not entry_claims_a_build(entry):
        return RUN_ROLE_PRE, "R4 entry names no landed build for a run to validate"
    return RUN_ROLE_UNKNOWN, "R5 entry claims a build but nothing dates it"


def backfill(doc: dict) -> tuple[int, collections.Counter, list]:
    changed = 0
    counts: collections.Counter = collections.Counter()
    rows = []
    for entry in doc.get("queue") or []:
        for rec in entry.get("failure_record") or []:
            if not isinstance(rec, dict):
                continue
            role, basis = classify(entry, rec)
            counts[role] += 1
            rows.append((entry.get("sd_id"), rec.get("run_id"), role, basis))
            if rec.get("run_role") != role or rec.get("run_role_basis") != basis:
                changed += 1
            rec["run_role"] = role
            rec["run_role_basis"] = basis
    return changed, counts, rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write substrate_queue.json")
    ap.add_argument("--report", action="store_true", help="print every item")
    args = ap.parse_args(argv)

    with open(QUEUE_PATH, encoding="utf-8") as fh:
        doc = json.load(fh)

    changed, counts, rows = backfill(doc)

    print("failure_record items: %d" % sum(counts.values()))
    for role in (RUN_ROLE_POST, RUN_ROLE_PRE, RUN_ROLE_UNKNOWN):
        print("  %-11s %d" % (role, counts[role]))
    print("items whose run_role/run_role_basis would change: %d" % changed)

    by_basis: collections.Counter = collections.Counter(
        (r[3].split(" (")[0], r[2]) for r in rows
    )
    print("\nderivation:")
    for (basis, role), n in sorted(by_basis.items()):
        print("  %-11s %-4d %s" % (role, n, basis))

    audit = [r for r in rows if "same_day" in r[3]]
    if audit:
        print("\nsame-day post_build (bare landing date read as 00:00Z) -- audit:")
        for sd, run, _role, _basis in audit:
            print("  %-46s %s" % (str(sd)[:46], str(run)[:70]))

    if args.report:
        print("\nfull derivation:")
        for sd, run, role, basis in rows:
            print("  %-44s %-11s %-44s %s"
                  % (str(sd)[:44], role, basis[:44], str(run)[:70]))

    if args.apply:
        # `json.dumps(doc, indent=2)` round-trips this file byte-identically
        # (verified 2026-08-15), so the diff is exactly the added keys. Do NOT add
        # ensure_ascii=False or sort_keys=True here -- either one re-serialises the
        # whole 157-entry file and buries the change in noise.
        with open(QUEUE_PATH, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=2)
            fh.write("\n")
        print("\nWROTE %s" % QUEUE_PATH)
    else:
        print("\n(dry run -- pass --apply to write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
