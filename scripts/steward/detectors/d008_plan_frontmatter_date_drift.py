#!/usr/bin/env python3
"""D-008 -- plan-level `last_updated` older than its newest node's.

THE INCIDENT. self_attribution_plan.md's frontmatter read `last_updated:
2026-06-04` while its nodes had been reconciled on 2026-07-29. The morning
digest reads the plan-level field to compute staleness, so it reported the plan
as "72d stale" and sent attention to a plan that had in fact been worked on
seven days earlier. The drift does not corrupt anything; it misdirects
attention, which on a scarce-attention pipeline is the same harm.

WHY THIS IS SAFELY T0. Bumping this field to match the nodes is not a new
convention invented here -- it is already the established governance action,
performed by hand and recorded in the nodes themselves. From
sleep_substrate_plan.md, twice:

    "last_updated bumped to clear the closure-drift stale-since-review flag"

So the fix direction is settled precedent, the target value is computed (not
chosen), and the edit is one line. It is also strictly monotonic: the field is
only ever moved FORWARD, to a date the plan's own nodes already assert. It can
never invent recency the plan does not have.

THE EDIT IS A TARGETED LINE REPLACEMENT, NOT A YAML ROUND-TRIP. These plans are
hand-written markdown with rich, ordered, commented frontmatter; loading and
re-dumping the YAML would reformat every one of them and produce exactly the
order-of-magnitude diff CLAUDE.md's "Narrow Edits Only" rule forbids. So the
fixer locates the single plan-level `last_updated:` line and rewrites its value
in place, preserving indentation, key spelling and the rest of the file byte
for byte.

THE EDIT SITE MUST BE UNAMBIGUOUS OR IT IS NOT T0. Plan-level `last_updated`
sits at indent 2; node-level ones at indent 6+, so they cannot collide. The
fixer additionally requires EXACTLY ONE indent-2 `last_updated:` in the region
between `closure_plan:` and `  nodes:`, and a bare ISO date as its value.
Verified across all 59 plans on the 2026-08-16 tree: every one satisfies both.
Any plan that does not is reported at T1 and left alone rather than guessed at.

NOT A DEFECT, AND DELIBERATELY NOT FLAGGED: a plan-level date NEWER than every
node (drives_motivation_v4_plan.md: plan 2026-08-05, newest node 2026-06-14).
Plan-level edits -- scope_claims, sibling_plans, prose -- legitimately touch the
plan without touching a node. Only the backwards direction is drift.
"""

from __future__ import annotations

import re
from pathlib import Path

from ._common import Context, finding

DETECTOR_ID = "D-008"
DETECTOR_TITLE = "Plan frontmatter last_updated drift"
TIER = "T0"

PLANNING_REL = "evidence/planning"
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLAN_LU_LINE = re.compile(r"^(  last_updated:[ \t]*)(.*?)([ \t]*)$")


def _iso(value) -> str:
    """Normalise a YAML date|str to an ISO date string, or "" if unusable."""
    if value is None:
        return ""
    text = str(value).strip().strip('"').strip("'")
    return text if ISO_DATE.match(text) else ""


def _frontmatter_span(text: str) -> tuple[int, int] | None:
    """(start, end) character offsets of the frontmatter body, or None."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return 4, end


def _locate_plan_line(text: str) -> tuple[int, str, str] | None:
    """Find the single plan-level `last_updated` line.

    Returns (line_index, current_value, full_line), or None when the site is
    ambiguous -- which is the signal to report rather than fix.
    """
    span = _frontmatter_span(text)
    if not span:
        return None
    body = text[span[0]:span[1]]
    lines = body.split("\n")

    try:
        start = next(i for i, l in enumerate(lines)
                     if l.rstrip() == "closure_plan:")
    except StopIteration:
        return None
    try:
        stop = next(i for i, l in enumerate(lines)
                    if i > start and re.match(r"^  nodes:", l))
    except StopIteration:
        stop = len(lines)

    hits = [i for i in range(start, stop) if PLAN_LU_LINE.match(lines[i])]
    # Exactly one candidate in the plan-level region, and none lurking at
    # indent 2 anywhere else in the frontmatter.
    all_hits = [i for i, l in enumerate(lines) if PLAN_LU_LINE.match(l)]
    if len(hits) != 1 or len(all_hits) != 1:
        return None

    idx = hits[0]
    m = PLAN_LU_LINE.match(lines[idx])
    assert m is not None
    return idx, m.group(2).strip(), lines[idx]


def _drifted(ctx: Context) -> list[dict]:
    """Every plan whose frontmatter date trails its newest node date."""
    out = []
    by_file: dict[str, list] = {}
    for node in ctx.nodes:
        by_file.setdefault(node.plan_file, []).append(node)

    for plan in ctx.plans:
        fname = plan.get("file")
        if not fname:
            continue
        path = ctx.repo_root / PLANNING_REL / fname
        if not path.exists():
            continue

        node_dates = []
        n_unparsed = 0
        for node in by_file.get(fname, []):
            raw = node.raw.get("last_updated")
            if raw is None:
                continue
            iso = _iso(raw)
            if iso:
                node_dates.append(iso)
            else:
                n_unparsed += 1
        if not node_dates:
            continue

        newest = max(node_dates)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        located = _locate_plan_line(text)
        if located is None:
            out.append({"plan": plan, "path": path, "newest": newest,
                        "current": None, "ambiguous": True,
                        "n_unparsed": n_unparsed, "text": text, "line": None})
            continue

        idx, current_raw, _line = located
        current = _iso(current_raw)
        if not current:
            out.append({"plan": plan, "path": path, "newest": newest,
                        "current": current_raw, "ambiguous": True,
                        "n_unparsed": n_unparsed, "text": text, "line": idx})
            continue
        if current >= newest:
            continue  # in sync, or plan legitimately newer -- not drift

        out.append({"plan": plan, "path": path, "newest": newest,
                    "current": current, "ambiguous": False,
                    "n_unparsed": n_unparsed, "text": text, "line": idx,
                    "newest_nodes": sorted(
                        n.node_id for n in by_file.get(fname, [])
                        if _iso(n.raw.get("last_updated")) == newest)})
    return out


def run(ctx: Context) -> tuple[list[dict], dict]:
    drifted = _drifted(ctx)
    findings = []
    n_fixable = 0

    for d in drifted:
        fname = d["plan"]["file"]
        if d["ambiguous"]:
            findings.append(finding(
                detector=DETECTOR_ID,
                subject=fname,
                title="%s: last_updated edit site is ambiguous" % fname,
                detail=(
                    "Nodes assert a newest last_updated of %s, but the "
                    "plan-level `last_updated` line could not be located "
                    "unambiguously (expected exactly one indent-2 "
                    "`last_updated:` between `closure_plan:` and `nodes:`, "
                    "holding a bare ISO date; found %r). Not auto-fixed -- a "
                    "guessed edit site is how a targeted fix becomes a "
                    "corruption. Fix by hand."
                    % (d["newest"], d["current"])),
                severity="P3", confidence=0.7, signal="weak",
                escalate=True, tier="T1", autofix=False,
                evidence={"plan_file": fname, "newest_node_date": d["newest"]},
                route="/governance",
            ))
            continue

        n_fixable += 1
        findings.append(finding(
            detector=DETECTOR_ID,
            subject=fname,
            title="%s: frontmatter %s trails newest node %s"
                  % (fname, d["current"], d["newest"]),
            detail=(
                "closure_plan.last_updated reads %s while node(s) %s assert "
                "%s. The morning digest computes plan staleness from the "
                "frontmatter field, so this inflates the reported stale age by "
                "the gap and misdirects attention to a plan that has in fact "
                "been worked on. T0 fix: move the frontmatter field forward to "
                "%s -- one line, monotonic, and the same action governance "
                "already performs by hand ('last_updated bumped to clear the "
                "closure-drift stale-since-review flag')."
                % (d["current"], ", ".join(d.get("newest_nodes") or []) or "-",
                   d["newest"], d["newest"])),
            severity="P3", confidence=0.98, signal="strong",
            # T0: --fix repairs it. No model needs to see this.
            escalate=False, tier=TIER, autofix=True,
            evidence={
                "plan_file": fname,
                "plan_id": d["plan"].get("id"),
                "current": d["current"],
                "newest_node_date": d["newest"],
                "newest_nodes": d.get("newest_nodes") or [],
                "drift_days": _days_between(d["current"], d["newest"]),
                "unparsed_node_dates": d["n_unparsed"],
            },
            route="/governance",
        ))

    return findings, {
        "detector": DETECTOR_ID, "title": DETECTOR_TITLE, "tier": TIER,
        "n_findings": len(findings), "n_autofixable": n_fixable,
    }


def _days_between(a: str, b: str) -> int:
    from datetime import date
    try:
        ya, ma, da = (int(x) for x in a.split("-"))
        yb, mb, db = (int(x) for x in b.split("-"))
        return (date(yb, mb, db) - date(ya, ma, da)).days
    except Exception:
        return 0


def fix(ctx: Context, now: str, dry_run: bool = True) -> list[dict]:
    """Move each drifted plan-level `last_updated` forward to its newest node date."""
    records = []
    for d in _drifted(ctx):
        if d["ambiguous"]:
            continue
        fname = d["plan"]["file"]
        path: Path = d["path"]
        text: str = d["text"]
        idx: int = d["line"]

        span = _frontmatter_span(text)
        if not span:
            continue
        head, body, tail = text[:span[0]], text[span[0]:span[1]], text[span[1]:]
        lines = body.split("\n")
        m = PLAN_LU_LINE.match(lines[idx])
        if not m:
            continue

        records.append({
            "action": "autofix",
            "detector": DETECTOR_ID,
            "finding_id": "%s:%s" % (DETECTOR_ID, fname),
            "path": "%s/%s" % (PLANNING_REL, fname),
            "subject": fname,
            "change": "closure_plan.last_updated %s -> %s"
                      % (d["current"], d["newest"]),
            "reverse": "set closure_plan.last_updated back to %s" % d["current"],
            "dry_run": bool(dry_run),
        })
        if not dry_run:
            lines[idx] = "%s%s" % (m.group(1), d["newest"])
            path.write_text(head + "\n".join(lines) + tail, encoding="utf-8")
    return records
