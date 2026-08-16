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
                    "dispositioned": already})
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
            escalate=not bool(fixable),
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
            },
            route="/governance",
        ))

    return findings, {
        "detector": DETECTOR_ID, "title": DETECTOR_TITLE, "tier": TIER,
        "n_findings": len(findings),
        "n_groups": len(groups),
        "n_autofixable": n_fixable,
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
