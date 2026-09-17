#!/usr/bin/env python3
"""D-006 -- duplicate entries in evidence/planning/governance_flags.v1.json.

THE INCIDENT. MECH-449 / ARC-107 read four occurrences on the Mac checkout
against origin's two, from a repeated commit. Adopting origin cleaned it up by
accident rather than by design. Earlier instances are still on the tree:
GFLAG-0011/0012/0013 (one raise, written three times) and GFLAG-0014..0017 (one
raise, written four times), both produced by governance_flag.py's raise call
retrying on push rejection against a dirty shared checkout.

THE FIX IS ANNOTATION, NOT DELETION -- AND THAT IS A DELIBERATE DEPARTURE
=====================================================================
The brief for this detector says "dedup in place", which reads as "remove the
extra rows". Running it against the live registry says otherwise, and the
registry wins:

  1. The file's own `authority` field calls it a "derive-only,
     human/agent-adjudicated INPUT" -- an audit trail, not a cache.
  2. Every duplicate already on the tree was dispositioned by ANNOTATION:
     status flipped to `superseded` with a resolution_note naming the
     canonical entry. Five occurrences, five annotations, zero deletions.
     Deletion has no precedent here; annotation has all of it.
  3. Those notes reference each other BY FLAG ID ("Accidental duplicate of
     GFLAG-0011"). Deleting rows would dangle live cross-references.
  4. `superseded` is a first-class status in governance_flag.py
     (RESOLVE_STATUSES) and `list --status open` filters on it, so annotating
     genuinely removes the duplicate from the working set. The dedup is real;
     only the mechanism differs.
  5. A status flip is reversible from the file alone. A deletion is not.

Point 5 is what settles it against the T0 bar the brief itself sets: "each fix
is a single reversible edit", and "if a fix is ever ambiguous, it is not T0 --
demote it to T1 rather than guessing".

WHAT IS FIXED AND WHAT IS ONLY REPORTED
=====================================================================
Grouping is by (claim_ids, flag_type, raised-at DATE), exactly as briefed. The
AUTOFIX predicate is strictly narrower, because the grouping key alone can put
two genuinely different flags in one group -- same claim, same type, same day
is entirely possible for distinct findings. A group member is auto-fixable only
when ALL of:

  * its `summary` is byte-identical to the canonical's (the retry-loop
    signature: one raise call, written N times), AND
  * its `raised_at` matches to the SECOND, not merely the date, AND
  * it carries NO disposition -- status is still `open`.

Anything else is reported at T1 and left alone. The live tree shows exactly why
the last clause matters: GFLAG-0015 is a true duplicate whose status is
`resolved`, not `superseded`, and whose note says "resolved together. See
GFLAG-0014's resolution note for the full disposition." That is a human
decision recorded in the file. Flipping it would be the detector second-
guessing an adjudication it cannot see the reasoning for. It stays.

The consequence is that on the tree as of 2026-08-16 this detector applies ZERO
fixes: both duplicate groups are fully dispositioned. That is the correct
result, and it is what the clean-tree no-op test pins.

ROOT CAUSE IS ALREADY CLOSED UPSTREAM. governance_flag.py's raise path was
fixed to be idempotent across a CAS retry (RAISE_IDENTITY, stamped once rather
than per attempt), so this detector is a residue-cleaner for pre-fix history
plus a regression guard, not a live-defect alarm. Expect it to stay quiet.

Canonical entry = earliest raised_at, ties broken by lowest flag_id. That
reproduces every disposition already on the tree (GFLAG-0011 canonical for
0012/0013; GFLAG-0014 for 0015/0016/0017).

A SUPERSESSION CHAIN IS NOT A NEAR-DUPLICATE (GFLAG-0314 -> GFLAG-0328)
=====================================================================
The T1 near-duplicate report above fired on a shape it should never have
escalated: a flag and its own EXPLICIT SUCCESSOR, raised the same day. Those
match (claim_ids, flag_type, date) exactly and are not duplicates -- they are a
correctly-recorded correction, produced by CORRECT behaviour. Every careful
reissue makes one, so the shape recurs indefinitely.

Measured twice. GFLAG-0314 (2026-09-17 AM) recorded it plus six further
same-shape groups. GFLAG-0328 (2026-09-17 PM) made it decisive: that cycle's
Steward run escalated exactly THREE new findings and ALL THREE were this shape
(GFLAG-0315/0320, GFLAG-0316/0317, GFLAG-0325/0326) -- a 100% false-positive
rate for the whole escalation budget, which is the alarm-fatigue vector
GOV-FROZEN-1 warns about turned on the detector itself.

THE PREDICATE, and why it is POSITIONAL
---------------------------------------------------------------------
A group is a supersession chain when some member is already dispositioned
(`superseded`/`resolved`) AND another member OPENS by declaring itself that
member's successor: its flag_id appears inside the first
SUPERSESSION_DECLARATION_WINDOW characters of the successor's summary,
alongside a supersession-vocabulary token.

The leading-window clause is the load-bearing half, and it is set by
measurement, not taste. GFLAG-0328 specifies a two-clause test -- one member
dispositioned, another member's summary *contains* its flag_id -- and that test
as literally stated ALSO suppresses GFLAG-0307/0308, which GFLAG-0328 names as
the case that must keep escalating. On the live registry there is no field,
status, note or timestamp that separates 0307/0308 from the three PM groups:
0307 is `superseded`, carries a resolution_note naming 0308, and 0308's summary
names 0307. The ONE thing that does separate them is WHERE the reference sits:

    successor          flag_id offset in summary   summary length
    GFLAG-0047                              11              2119
    GFLAG-0109                              12              1503
    GFLAG-0127                              11              1054
    GFLAG-0320                              21              2100
    GFLAG-0317                              21              1326
    GFLAG-0326                              13               657
    GFLAG-0308  (must NOT suppress)        981              1090

Every true chain declares itself in its opening clause ("CORRECTED REISSUE of
GFLAG-0315", "Supersedes GFLAG-0046", "RESIDUAL of GFLAG-0106", "Successor to
GFLAG-0325"). GFLAG-0308 does not: it makes a DIFFERENT finding (EXP-0753's
provenance fields are unset, where 0307 said the row still read `proposed`) and
merely cites its predecessor in passing at the end. That is a real semantic
distinction -- declared successor vs. passing citation -- and the margin is 21
against 981, so the window is fitted to a gap, not to a point.

WHAT THIS DELIBERATELY DOES **NOT** SUPPRESS
---------------------------------------------------------------------
GFLAG-0314 listed six further groups as "the identical shape". Measurement says
three of them are not supersession chains at all, and they stay reported:

  * GFLAG-0151/0152 and GFLAG-0216/0217 -- two DISTINCT thought-digestion items
    sharing a claim, a type and a staging date. Neither summary names the other.
  * GFLAG-0266/0270 -- GFLAG-0270 opens "CORRECTION TO GFLAG-0265's REMEDY".
    It supersedes GFLAG-0265, which carries claim_ids [MECH-349, MECH-350] and
    therefore lands in a DIFFERENT group. 0266 and 0270 are genuinely distinct
    findings, and 0266 is still `open`.

Two wider predicates were tried against the live registry and REJECTED, because
each suppresses GFLAG-0307/0308 along with its targets: "every member is
dispositioned" (0307 superseded + 0308 resolved) and "the cross-reference may
live in the resolution_note" (0307's note names 0308). Do not re-propose either
without first retiring 0307/0308 as the negative control.

The suppression DE-PRIORITISES, it never hides: the group still appears in the
report with `escalate: False` and a detail naming the chain, matching the
Steward's own suppression doctrine (state/suppressions.yaml header). And it
never touches the T0 lane -- a group with byte-identical `open` re-writes is a
genuine retry-loop duplicate and is still auto-fixed.
"""

from __future__ import annotations

import collections
import json
from pathlib import Path

from ._common import Context, finding

DETECTOR_ID = "D-006"
DETECTOR_TITLE = "Duplicate governance flag entries"
TIER = "T0"

REGISTRY_REL = "evidence/planning/governance_flags.v1.json"

# A flag carrying any of these has been looked at by a human or an adjudicating
# session. Only a still-`open` duplicate is safe to annotate mechanically.
DISPOSITIONED_STATUSES = {"resolved", "superseded"}

# A supersession chain declares itself in the successor's OPENING clause. The
# window is fitted to a measured gap, not a point: on the live registry every
# true chain names its predecessor at offset 11-21, and the one group that must
# keep escalating (GFLAG-0307/0308) names it at 981. See the module docstring's
# offset table before changing either constant.
SUPERSESSION_DECLARATION_WINDOW = 160
SUPERSESSION_TOKENS = ("supersede", "superseding", "supersession", "successor",
                       "reissue", "residual", "replaces", "replacing")


def _declares_successor_of(item: dict, other: dict) -> bool:
    """True when `item` OPENS by declaring itself `other`'s successor.

    Both clauses are required. The flag_id alone is a citation, which is what
    GFLAG-0308 does at offset 981; the vocabulary token alone would match a
    summary discussing supersession generally.
    """
    oid = str(other.get("flag_id") or "")
    if not oid:
        return False
    head = str(item.get("summary") or "")[:SUPERSESSION_DECLARATION_WINDOW].lower()
    return oid.lower() in head and any(t in head for t in SUPERSESSION_TOKENS)


def _supersession_chain(members: list[dict]) -> tuple[dict, dict] | None:
    """(predecessor, successor) when this group is an explicit chain, else None.

    The predecessor must already be dispositioned -- an `open` flag that someone
    has merely written a successor for still has its own owed action, and the
    group is not yet history.
    """
    for pred in members:
        if str(pred.get("status") or "") not in DISPOSITIONED_STATUSES:
            continue
        for succ in members:
            if succ is pred:
                continue
            if _declares_successor_of(succ, pred):
                return pred, succ
    return None


def _registry_path(ctx: Context) -> Path:
    return ctx.repo_root / REGISTRY_REL


def _load(path: Path) -> tuple[dict | None, str]:
    if not path.exists():
        return None, "registry not found at %s" % path
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, "registry parse failed: %s" % exc
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        return None, "registry has no items list"
    return data, ""


def _group_key(item: dict) -> tuple:
    """(claim_ids, flag_type, DATE) -- the briefed grouping key."""
    claims = tuple(sorted(str(c) for c in (item.get("claim_ids") or [])))
    return (claims, str(item.get("flag_type") or ""),
            str(item.get("raised_at") or "")[:10])


def _canonical(group: list[dict]) -> dict:
    return sorted(group, key=lambda it: (str(it.get("raised_at") or ""),
                                         str(it.get("flag_id") or "")))[0]


def _exact_duplicate(item: dict, canon: dict) -> bool:
    """The retry-loop signature: same raise, written more than once."""
    return (item.get("summary") == canon.get("summary")
            and str(item.get("raised_at") or "") == str(canon.get("raised_at") or "")
            and item.get("flag_id") != canon.get("flag_id"))


def analyse(ctx: Context) -> tuple[list[dict], dict]:
    """Shared by run() and fix() so detection and repair cannot drift apart."""
    path = _registry_path(ctx)
    data, err = _load(path)
    if data is None:
        return [], {"error": err, "groups": []}

    groups = collections.defaultdict(list)
    for it in data["items"]:
        if isinstance(it, dict):
            groups[_group_key(it)].append(it)

    out = []
    for key, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        canon = _canonical(members)
        exact, divergent, already = [], [], []
        for it in members:
            if it.get("flag_id") == canon.get("flag_id"):
                continue
            if not _exact_duplicate(it, canon):
                divergent.append(it)
            elif str(it.get("status") or "") in DISPOSITIONED_STATUSES:
                already.append(it)
            else:
                exact.append(it)
        out.append({"key": key, "members": members, "canonical": canon,
                    "fixable": exact, "divergent": divergent,
                    "dispositioned": already,
                    # Computed here rather than in run() so detection and repair
                    # read one shared verdict, as with fixable/divergent.
                    "supersession_chain": _supersession_chain(members)})
    return out, {"path": path, "data": data, "groups": out}


def run(ctx: Context) -> tuple[list[dict], dict]:
    groups, meta = analyse(ctx)
    if meta.get("error"):
        return [], {"detector": DETECTOR_ID, "title": DETECTOR_TITLE,
                    "tier": TIER, "n_findings": 0, "error": meta["error"]}

    findings = []
    n_fixable = 0
    for g in groups:
        claims, ftype, date = g["key"]
        canon_id = str(g["canonical"].get("flag_id"))
        fixable = g["fixable"]
        divergent = g["divergent"]
        n_fixable += len(fixable)

        # Fully-dispositioned groups are history, not a defect. Reporting them
        # every run would be exactly the "unfixed defect re-escalating forever"
        # noise the runner's NEW/RECURRING split exists to prevent -- except
        # worse, because there is nothing left to do about them.
        if not fixable and not divergent:
            continue

        if fixable:
            sev, conf, sig = "P2", 0.95, "strong"
            title = ("%d undispositioned duplicate flag(s) of %s (%s / %s)"
                     % (len(fixable), canon_id, ",".join(claims) or "-", ftype))
            detail = (
                "Group (claims=%s, flag_type=%s, date=%s) holds %d entries. "
                "%s is canonical (earliest raised_at). %s are byte-identical "
                "re-writes of the same raise with status still `open` -- the "
                "governance_flag.py retry-loop signature. T0 fix: set status to "
                "`superseded` and record a resolution_note naming %s, matching "
                "the disposition already applied by hand to every other "
                "duplicate in this registry. Rows are NOT deleted: the registry "
                "is an audit trail and its notes cross-reference flag ids."
                % (",".join(claims) or "-", ftype, date, len(g["members"]),
                   canon_id, ", ".join(str(x.get("flag_id")) for x in fixable),
                   canon_id))
        elif g.get("supersession_chain"):
            # A flag and its own declared successor. Not a duplicate: a
            # correctly-recorded correction, produced by CORRECT behaviour and
            # therefore recurring indefinitely. Reported so the disposition is
            # visible, never escalated. See the module docstring.
            pred, succ = g["supersession_chain"]
            sev, conf, sig = "P3", 0.6, "weak"
            title = ("supersession chain %s -> %s, not a duplicate (%s / %s)"
                     % (str(pred.get("flag_id")), str(succ.get("flag_id")),
                        ",".join(claims) or "-", ftype))
            detail = (
                "Group (claims=%s, flag_type=%s, date=%s) holds %d entries, but "
                "%s is already `%s` and %s OPENS by declaring itself its "
                "successor. That is a correction the registry recorded "
                "correctly, not a duplicate, so nothing is owed on the pair AS "
                "A PAIR -- each flag's own action is tracked on its own flag. "
                "NOT ESCALATED (GFLAG-0328): every careful reissue makes one of "
                "these, so escalating them spends the budget on correct "
                "behaviour indefinitely. Entries: %s"
                % (",".join(claims) or "-", ftype, date, len(g["members"]),
                   str(pred.get("flag_id")), str(pred.get("status")),
                   str(succ.get("flag_id")),
                   ", ".join(str(x.get("flag_id")) for x in g["members"])))
        else:
            sev, conf, sig = "P3", 0.6, "weak"
            title = ("%d near-duplicate flag(s) of %s need adjudication (%s / %s)"
                     % (len(divergent), canon_id, ",".join(claims) or "-", ftype))
            detail = (
                "Group (claims=%s, flag_type=%s, date=%s) holds %d entries "
                "sharing claim+type+date, but the extras are NOT byte-identical "
                "re-writes of %s. Same claim, same type, same day is entirely "
                "possible for genuinely distinct findings, so this is NOT "
                "auto-fixed -- it needs a human to say whether these are one "
                "flag or several. Entries: %s"
                % (",".join(claims) or "-", ftype, date, len(g["members"]),
                   canon_id,
                   ", ".join(str(x.get("flag_id")) for x in divergent)))

        findings.append(finding(
            detector=DETECTOR_ID,
            subject=canon_id,
            title=title,
            detail=detail,
            severity=sev,
            confidence=conf,
            signal=sig,
            # A T0 finding does not wake a model: --fix repairs it, and the
            # report says so. Escalation is reserved for the T1 tail that
            # genuinely needs adjudication.
            escalate=not bool(fixable) and not bool(g.get("supersession_chain")),
            tier=TIER if fixable else "T1",
            autofix=bool(fixable),
            evidence={
                "registry": REGISTRY_REL,
                "canonical": canon_id,
                "claim_ids": list(claims),
                "flag_type": ftype,
                "date": date,
                "group_size": len(g["members"]),
                "fixable_ids": [str(x.get("flag_id")) for x in fixable],
                "divergent_ids": [str(x.get("flag_id")) for x in divergent],
                "already_dispositioned_ids": [str(x.get("flag_id"))
                                              for x in g["dispositioned"]],
                "supersession_chain": (
                    [str(g["supersession_chain"][0].get("flag_id")),
                     str(g["supersession_chain"][1].get("flag_id"))]
                    if g.get("supersession_chain") else None),
            },
            route="/governance",
        ))

    return findings, {
        "detector": DETECTOR_ID, "title": DETECTOR_TITLE, "tier": TIER,
        "n_findings": len(findings),
        "n_groups": len(groups),
        "n_autofixable": n_fixable,
        "n_supersession_chains": sum(1 for g in groups
                                     if g.get("supersession_chain")),
        "n_escalated": sum(1 for f in findings if f.get("escalate")),
    }


def fix(ctx: Context, now: str, dry_run: bool = True) -> list[dict]:
    """Annotate every undispositioned exact duplicate as `superseded`.

    One narrow structural change per row -- status, resolution_note,
    resolved_at -- with every other field and every other row preserved
    verbatim. Never deletes. Never commits: a human reviews the diff and lands
    it, which is the whole reason this is safe to run unattended.
    """
    groups, meta = analyse(ctx)
    if meta.get("error"):
        return []

    path: Path = meta["path"]
    data: dict = meta["data"]
    records = []
    touched = False

    for g in groups:
        canon_id = str(g["canonical"].get("flag_id"))
        for item in g["fixable"]:
            fid = str(item.get("flag_id"))
            note = ("Accidental duplicate of %s (identical summary, identical "
                    "raised_at %s). Marked superseded by Steward %s; rows are "
                    "retained because the registry is an audit trail. See %s "
                    "for the substantive disposition."
                    % (canon_id, item.get("raised_at"), DETECTOR_ID, canon_id))
            records.append({
                "action": "autofix",
                "detector": DETECTOR_ID,
                "finding_id": "%s:%s" % (DETECTOR_ID, canon_id),
                "path": REGISTRY_REL,
                "subject": fid,
                "change": "%s status %s -> superseded" % (fid, item.get("status")),
                "reverse": ("set %s status back to %r and remove the "
                            "Steward-authored resolution_note/resolved_at"
                            % (fid, item.get("status"))),
                "dry_run": bool(dry_run),
            })
            if not dry_run:
                item["status"] = "superseded"
                item["resolution_note"] = note
                if not item.get("resolved_at"):
                    item["resolved_at"] = now
                touched = True

    if touched:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    return records
