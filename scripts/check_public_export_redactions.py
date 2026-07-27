#!/usr/bin/env python3
"""
Gate on the unattended public-export refresh: may this export be published
without a human looking at it first?

WHY THIS EXISTS (2026-07-27). The published export under
docs/public_explorer/data/ was found serving a 2026-06-15 snapshot -- six weeks
stale, 17 claims and 80 experiments missing. Nothing regenerates it: not
scripts/governance.sh, not a git hook, not a cron, not a workflow. It only ever
refreshed when a person happened to run the exporter, and for six weeks nobody
did. The fix is .github/workflows/public-explorer-refresh.yml, a weekly cron.

But a cron removes the one thing the old manual flow reliably had: a human
reading public_explorer_redaction_report.md before pushing. This module is what
replaces that reader, so the refresh can be automatic WITHOUT being unsupervised.

WHAT IS AND IS NOT AT RISK -- the part worth getting right.

It is tempting to describe this as "stops leaks reaching the public site". It
does not, and it does not need to. The scrub in export_public_explorer.py drops
the whole field on any sensitive-pattern match, unconditionally, approved or
not. Publishing is already safe with this gate asleep, absent, or empty. If the
gate were really the leak defence, then every week it passed would be a week the
site was protected by a JSON file nobody had reread -- which is precisely the
kind of reassurance that turns out to be load-bearing on nothing.

What unattended publishing actually loses is the human, and with them:

  1. OVER-REDACTION going unnoticed. This is the real hazard and the reason to
     gate. The scrub is deliberately blunt -- one match kills the ENTIRE field --
     so a legitimate result summary that happens to mention a hostname silently
     disappears from the public site. No error, no warning; the page just has
     less science on it. Unattended, that decays the site one field at a time.
  2. Nobody fixing the SOURCE. A machine identity inside an
     evidence_direction_note is a defect in the note. The scrub hides it well
     enough that it survives indefinitely.
  3. A SOURCE COLLAPSE publishing as if it were a real result. If claims.yaml
     half-parses or review_tracker.json gets truncated, the exporter does not
     crash -- it cheerfully emits a much smaller, perfectly valid export, and an
     unattended pusher would replace a good snapshot with a gutted one. A human
     would have noticed "196 -> 12" instantly. Gate 3 below is that instinct.

So the review question per entry is never "is dropping this safe?" (always yes)
but "should this field have been publishable, and is the source worth fixing?".

THREE GATES, in order of what they catch:

  1. NEW SCRUB HITS      -- every hit must be in the reviewed baseline
                            scripts/public_explorer_approved_redactions.json.
                            Keyed (record_type, record_id, field, pattern);
                            see that file's _README for why not `matched`.
  2. LEAK/SCOPE VALIDATION -- the exporter's own validate_outputs(), which is
                            what --check runs. Belt and braces on gate 1.
  3. COUNT COLLAPSE      -- published counts must not fall off a cliff versus
                            the currently-committed index.json.

WRITES NOTHING (except with --update). It calls exp.build_export(), which was
split out of main() for exactly this reason: a gate that had to perform the real
export in order to decide whether the real export is safe would be writing the
files it is gating. In a shared multi-session checkout that is the
read-modify-write contamination shape that got the test module redirected to a
tempdir in 7a6120e3e1. Being a pure read makes this safe to run anywhere, in any
checkout, at any time -- including on a developer's dirty tree.

Usage:
  python3 scripts/check_public_export_redactions.py
  python3 scripts/check_public_export_redactions.py --update --reviewed-by <name>
  python3 scripts/check_public_export_redactions.py --max-drop-frac 0.30

Exit codes:
  0  clean -- safe to publish unattended
  1  new, unreviewed scrub hit(s)
  2  published counts collapsed versus the committed snapshot
  3  leak/scope validation failed, or a canonical source is missing/malformed
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import export_public_explorer as exp

REPO_ROOT = Path(__file__).resolve().parents[1]
APPROVED = Path(__file__).resolve().parent / "public_explorer_approved_redactions.json"
COMMITTED_INDEX = REPO_ROOT / "docs" / "public_explorer" / "data" / "index.json"

# A fall of more than this fraction in either headline count, versus the
# snapshot currently committed, is treated as a source failure rather than
# governance churn. Calibrated against real movement: the 2026-06-15 ->
# 2026-07-27 refresh moved claims 179 -> 196 and experiments 153 -> 233, and
# within that the claim set lost 4 of 179 (~2%) to status changes while gaining
# 21. Ordinary churn is low single digits over six weeks; a genuine source
# collapse is near-total. 20% sits well clear of both.
DEFAULT_MAX_DROP_FRAC = 0.20

KEY_FIELDS = ("record_type", "record_id", "field", "pattern")


def hit_key(h):
    """Identity of a scrub hit for review purposes.

    Excludes `matched` on purpose -- see the baseline file's _README. A new
    RECORD tripping the scrub is the reviewable event; the same record tripping
    the same pattern on a different substring is not.
    """
    return tuple(str(h.get(f, "")) for f in KEY_FIELDS)


def load_approved(path=APPROVED):
    """Return (list_of_entries, set_of_keys). A missing file approves nothing."""
    if not path.exists():
        return [], set()
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("approved", [])
    if not isinstance(entries, list):
        raise ValueError(f"{path.name}: 'approved' must be a list")
    return entries, {hit_key(e) for e in entries}


def committed_counts(path=COMMITTED_INDEX):
    """Headline counts from the currently-published index.json, or None."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("counts") or None
    except (json.JSONDecodeError, OSError):
        return None


def check_counts(new_counts, old_counts, max_drop_frac):
    """Return a list of failure strings for collapsed headline counts."""
    failures = []
    if not old_counts:
        return failures
    for key, new in (("claims_public", new_counts["claims"]),
                     ("experiments_public", new_counts["experiments"])):
        old = old_counts.get(key)
        if not isinstance(old, int) or old <= 0:
            continue
        if new <= 0:
            failures.append(
                f"{key} collapsed to {new} (was {old}). A zero count is never "
                f"ordinary churn -- treat this as a broken source.")
            continue
        drop = (old - new) / old
        if drop > max_drop_frac:
            failures.append(
                f"{key} fell {old} -> {new} ({drop:.0%} drop, limit "
                f"{max_drop_frac:.0%}). Governance churn does not move this "
                f"count that far; suspect a malformed or truncated source "
                f"before assuming the drop is real.")
    return failures


def do_update(hits, reviewed_by, path=APPROVED):
    """Fold the current hits into the baseline, preserving existing reviews."""
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"approved": []}
    existing = {hit_key(e): e for e in data.get("approved", [])}
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    added = []
    for h in hits:
        k = hit_key(h)
        if k in existing:
            continue
        entry = {
            "record_type": h["record_type"],
            "record_id": h["record_id"],
            "field": h["field"],
            "pattern": h["pattern"],
            "matched_when_reviewed": h.get("matched", ""),
            "verdict": "TODO -- true_positive | over_redaction",
            "reviewed_utc": now,
            "reviewed_by": reviewed_by,
            "note": "TODO -- why is dropping this field correct, and should the source be fixed?",
        }
        existing[k] = entry
        added.append(entry)
    data["approved"] = sorted(existing.values(), key=hit_key)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return added


def main():
    ap = argparse.ArgumentParser(
        description="Gate the unattended public-export refresh.")
    ap.add_argument("--update", action="store_true",
                    help="Fold current hits into the reviewed baseline (writes).")
    ap.add_argument("--reviewed-by", default=None,
                    help="Reviewer identity recorded by --update (required with it).")
    ap.add_argument("--max-drop-frac", type=float, default=DEFAULT_MAX_DROP_FRAC,
                    help=f"Headline-count drop treated as a source failure "
                         f"(default {DEFAULT_MAX_DROP_FRAC}).")
    args = ap.parse_args()

    if args.update and not args.reviewed_by:
        print("ERROR: --update requires --reviewed-by (the baseline records who "
              "looked at each hit; an anonymous approval is not a review).",
              file=sys.stderr)
        return 3

    try:
        built = exp.build_export()
    except exp.ExportSourceError as excinfo:
        print(f"ERROR: {excinfo}", file=sys.stderr)
        return 3

    hits = built["redactions"].pattern_hits
    counts = built["counts"]
    print(f"Export built (nothing written): claims {counts['claims']}, "
          f"experiments {counts['experiments']}, scrub hits {len(hits)}")

    if args.update:
        added = do_update(hits, args.reviewed_by)
        if added:
            print(f"\nAdded {len(added)} entr(y/ies) to {APPROVED.name}:")
            for e in added:
                print(f"  {e['record_type']} {e['record_id']} [{e['pattern']}]")
            print("\nNow replace each TODO `verdict` and `note` with the real "
                  "finding -- an approval nobody wrote a reason for is not one.")
        else:
            print(f"\n{APPROVED.name} already covers every current hit; nothing added.")
        return 0

    failures, exit_code = [], 0

    # --- gate 1: new scrub hits ------------------------------------------
    approved_entries, approved_keys = load_approved()
    seen = {hit_key(h) for h in hits}
    new_hits = [h for h in hits if hit_key(h) not in approved_keys]
    stale = [e for e in approved_entries if hit_key(e) not in seen]

    if new_hits:
        exit_code = 1
        print(f"\nGATE 1 FAILED -- {len(new_hits)} unreviewed scrub hit(s):", file=sys.stderr)
        for h in new_hits:
            print(f"  {h['record_type']} {h['record_id']}\n"
                  f"    field={h['field']} pattern={h['pattern']} matched={h['matched']!r}",
                  file=sys.stderr)
        print("\n  The field was DROPPED, so nothing leaked -- publishing is safe\n"
              "  either way. What needs a person is whether it SHOULD have been\n"
              "  publishable (over-redaction quietly removes science from the\n"
              "  site) and whether the source note is worth fixing.\n"
              "  Review, then: python3 scripts/check_public_export_redactions.py "
              "--update --reviewed-by <name>", file=sys.stderr)
    else:
        print(f"GATE 1 ok -- all {len(hits)} scrub hit(s) previously reviewed")

    # Stale approvals mean a source got fixed. Good news; never a failure.
    if stale:
        print(f"\nNOTICE: {len(stale)} approved entr(y/ies) no longer fire "
              f"(source fixed, or record no longer published). Prune when convenient:")
        for e in stale:
            print(f"  {e['record_type']} {e['record_id']} [{e['pattern']}]")

    # --- gate 2: the exporter's own leak/scope validation -----------------
    # validate_outputs() re-reads exp.OUT_DIR from disk, so it validates the
    # snapshot currently on disk. In CI that is the export just written by the
    # workflow's own exporter run; run this gate after it.
    val_failures = exp.validate_outputs()
    if val_failures:
        exit_code = exit_code or 3
        failures.extend(val_failures)
        print(f"\nGATE 2 FAILED -- leak/scope validation:", file=sys.stderr)
        for f in val_failures:
            print(f"  - {f}", file=sys.stderr)
    else:
        print("GATE 2 ok -- leak/scope validation clean")

    # --- gate 3: count collapse ------------------------------------------
    old = committed_counts()
    count_failures = check_counts(counts, old, args.max_drop_frac)
    if count_failures:
        exit_code = 2
        print(f"\nGATE 3 FAILED -- published counts collapsed:", file=sys.stderr)
        for f in count_failures:
            print(f"  - {f}", file=sys.stderr)
    elif old:
        print(f"GATE 3 ok -- counts {old.get('claims_public')} -> {counts['claims']} claims, "
              f"{old.get('experiments_public')} -> {counts['experiments']} experiments")
    else:
        print("GATE 3 skipped -- no committed index.json to compare against")

    if exit_code == 0:
        print("\nAll gates passed: safe to publish unattended.")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
