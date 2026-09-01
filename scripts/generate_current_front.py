#!/usr/bin/env python3
"""generate_current_front.py -- derive docs/CURRENT_FRONT.md (the live, no-history front).

SHP-6 of the status/history plane-separation design
(evidence/planning/status_history_plane_separation_design.md, status table Sec.7).

Fixes "Failure A -- routing": the true front of progress IS current in
insights_report.md / closure_status.md / the autopsy stream, but the Session-Startup
entry docs route to NONE of them. This emits a SHORT, LIVE-ONLY front doc that the
entry docs can point at, regenerated every governance run so it is never a third
abandoned manual doc.

DERIVE, DO NOT HAND-WRITE. The front is a projection over records that already exist:
  - insights_report.md  (Claude-authored by /insights; the front narrative + lead EXQs +
                          buildable-now item + the H1/H2 gate recommendation)
  - evidence/planning/closure_status.md  (generate_closure_snapshot.py; weighted % + remaining)

Robustness contract: every extraction has a labelled fallback. If a source is missing or
its wording drifts so an anchor cannot be found, the doc still emits with an explicit
"(could not derive -- see <source>)" marker and a needs_review note, rather than silently
fabricating or going stale invisibly. Worst case it degrades to a pointer, which still
beats the pre-SHP-6 zero-routing.

PROMOTES / DEMOTES NOTHING. Read-only over its sources; only writes docs/CURRENT_FRONT.md.

Usage (from REE_assembly root, or anywhere):
    python scripts/generate_current_front.py
Runs automatically in scripts/governance.sh.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSIGHTS = os.path.join(ROOT, "insights_report.md")
CLOSURE = os.path.join(ROOT, "evidence", "planning", "closure_status.md")
HYPOTHESIS_SPACE = os.path.join(ROOT, "evidence", "planning", "hypothesis_space.v1.json")
OUT = os.path.join(ROOT, "docs", "CURRENT_FRONT.md")

# em/en dash class for tolerant matching of Claude-authored prose
DASH = r"[-–—]"


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def _read_json(path):
    """Soft-load a JSON file. Returns None on any error so a missing/malformed
    hypothesis_space.v1.json degrades gracefully (the front doc still generates)."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _search(pattern, text, group=1, default=None, flags=0):
    m = re.search(pattern, text, flags)
    if not m:
        return default
    try:
        return m.group(group).strip()
    except IndexError:
        return default


def derive():
    """Return (fields dict, needs_review bool). Never raises on drift."""
    insights = _read(INSIGHTS)
    closure = _read(CLOSURE)
    needs_review = False
    f = {}

    # --- provenance / currency -------------------------------------------------
    f["insights_date"] = _search(r"# Project Insights\s*" + DASH + r"*\s*(\d{4}-\d{2}-\d{2})",
                                 insights, default=None)
    f["insights_generated"] = _search(r"^Generated:\s*(\S+)", insights, default=None,
                                      flags=re.MULTILINE)
    f["closure_generated"] = _search(r"^Generated:\s*(\S+)", closure, default=None,
                                     flags=re.MULTILINE)

    # --- the gate: Recommendation 1 (the decided next step) --------------------
    # Anchor to the '## Recommendations' section so we get the DECISION, not the
    # first numbered list on the page (the 'genuinely hard part' enumeration).
    # Computed BEFORE headline/live-path below because both of those fall back to
    # this block's text when insights_report.md carries no separate campaign
    # section (e.g. the "clean state, nothing survives the four gates" format).
    rec_block = _search(r"(## Recommendations.*?)(?:\n## |\Z)", insights, default="",
                        flags=re.DOTALL)
    gate = _search(r"^1\.\s+\*\*([^*]+)\*\*", rec_block, default=None, flags=re.MULTILINE)
    if not gate:
        # fall back to item-1 lead text even if not bold-wrapped
        gate = _search(r"^1\.\s+(.+?)(?:\.\s|\.\n|\n)", rec_block, default=None,
                       flags=re.MULTILINE)
    if not gate:
        gate = "(could not derive the gate -- see insights_report.md Recommendations)"
        needs_review = True
    f["gate"] = gate.rstrip(".")

    # --- the one-line front headline ------------------------------------------
    # The '### The live front is ...' heading in insights_report.md is the single
    # most-important-front one-liner. Fallback 1: the live-campaign section
    # heading. Fallback 2: the '**Gate check result: ...**' bold summary line
    # /insights emits under Recommendations when there is no live campaign at all
    # (a genuinely clean, fully-routed snapshot) -- this is real content, not
    # drift, so it must not read as "could not derive".
    headline = _search(r"^###\s+(The live front[^\n]+)$", insights, default=None,
                       flags=re.MULTILINE)
    if not headline:
        headline = _search(r"^##\s+(The live campaign[^\n]+)$", insights, default=None,
                           flags=re.MULTILINE)
    if not headline:
        headline = _search(r"\*\*(Gate check result:[^*]+)\*\*", rec_block, default=None)
    if not headline:
        headline = "(could not derive front headline -- see insights_report.md)"
        needs_review = True
    f["headline"] = headline

    # --- live path: the lead diagnostic + the rest of the campaign fan-out -----
    # The '## The live campaign' table marks one row '(lead)'. Collect every
    # V3-EXQ id in that table, lead first. Fallback: no campaign table exists in
    # the "clean state" report format -- reuse the already-derived `gate` text
    # (Recommendation item 1), which names the specific EXQ ids still in flight
    # (e.g. already-queued re-tests) even when there is no separate campaign
    # section to point at.
    campaign_block = _search(r"(## The live campaign.*?)(?:\n## |\Z)", insights,
                             default="", flags=re.DOTALL)
    lead = _search(r"\|\s*\*\*(V3-EXQ-\d+[a-z]?)\*\*[^|]*\|\s*\*\*\d+\s*\(lead\)\*\*",
                   campaign_block, default=None)
    all_exq = []
    for m in re.finditer(r"(V3-EXQ-\d+[a-z]?)", campaign_block):
        eid = m.group(1)
        if eid not in all_exq:
            all_exq.append(eid)
    if lead and lead in all_exq:
        all_exq.remove(lead)
        all_exq.insert(0, lead)
    fallback_live_path = False
    if not all_exq:
        for m in re.finditer(r"(V3-EXQ-\d+[a-z]?)", gate):
            eid = m.group(1)
            if eid not in all_exq:
                all_exq.append(eid)
        fallback_live_path = bool(all_exq)
    f["lead_exq"] = lead
    f["live_path_exqs"] = all_exq[:4]  # keep it short
    f["live_path_is_fallback"] = fallback_live_path
    if not all_exq:
        needs_review = True

    # --- buildable-now item ----------------------------------------------------
    # "Ready & not-yet-implemented (buildable now): **MECH-090** (P2 -- ...)."
    build_id = _search(r"buildable now\)\s*:\s*\*\*([A-Z]+-\w+)\*\*", insights, default=None)
    build_desc = None
    if build_id:
        build_desc = _search(re.escape(build_id) + r"\*\*\s*\(([^)]+)\)", insights,
                             default=None)
    f["buildable_id"] = build_id
    f["buildable_desc"] = build_desc

    # --- closure headline ------------------------------------------------------
    f["weighted_pct"] = _search(r"Weighted progress:\s*\*\*([\d.]+)%\*\*", closure,
                                default=None)
    f["remaining"] = _search(r"Remaining\s*\([^)]*\)\s*:\s*\*\*(\d+)\*\*", closure,
                             default=None)

    # --- hypothesis space: the live "hero" question ----------------------------
    # One line pointing at the /progress map: the hypothesis-state breakdown on
    # the live question (design doc Sec.6). Soft: a missing/malformed JSON is
    # skipped silently (front doc still generates); it is an additive pointer,
    # not a gate.
    #
    # Deliberately does NOT read hero.surviving / .reduction_ratio / .bits_removed.
    # Those are build_hypothesis_space.py's rollup fields, and `surviving` folds in
    # a `synthesis.surviving_label` heuristic (+1 "composed survivor") on top of the
    # per-hypothesis state tally -- a heuristic that goes stale independently of the
    # states themselves (GFLAG-0093: competence_floor's synthesis prose was never
    # updated when its last alive leg resolved on 2026-08-08, so `surviving` stayed
    # frozen at 1 while every hypothesis was already eliminated/confirmed). `alive`
    # / `confirmed` / `resolved_out` / `superseded`, by contrast, are a direct tally
    # of each hypothesis's `resolution.state` with no synthesis involved, so they are
    # used here instead. Self-consistency (they must sum to `initial_frozen_count`)
    # is checked before trusting them; a mismatch degrades to "could not derive"
    # (needs_review) rather than printing a plausible-looking wrong number.
    f["hero"] = None
    hs = _read_json(HYPOTHESIS_SPACE)
    if isinstance(hs, dict):
        questions = hs.get("questions") or []
        hero = next((q for q in questions if isinstance(q, dict) and q.get("is_hero")), None)
        if hero:
            alive = hero.get("alive")
            confirmed = hero.get("confirmed")
            resolved_out = hero.get("resolved_out")
            superseded = hero.get("superseded")
            initial = hero.get("initial_frozen_count")
            counts = (alive, confirmed, resolved_out, superseded)
            if (all(isinstance(c, int) for c in counts) and isinstance(initial, int)
                    and sum(counts) == initial):
                f["hero"] = {
                    "short_title": hero.get("short_title") or hero.get("qid") or "(live question)",
                    "alive": alive,
                    "confirmed": confirmed,
                    "resolved_out": resolved_out,
                    "superseded": superseded,
                    "initial": initial,
                }
            else:
                f["hero"] = {"derive_failed": True}
                needs_review = True

    return f, needs_review


def render(f, needs_review, now):
    src_bits = []
    if f["insights_date"]:
        src_bits.append("insights_report.md (%s)" % f["insights_date"])
    else:
        src_bits.append("insights_report.md")
    src_bits.append("evidence/planning/closure_status.md")
    provenance = " + ".join(src_bits)

    lines = []
    lines.append("<!-- GENERATED FILE -- do not edit by hand. -->")
    lines.append("# REE -- Current Front")
    lines.append("")
    lines.append("**The single live front of progress. LIVE-ONLY: no history -- history lives "
                 "in the sources below.**")
    lines.append("")
    lines.append("> **GENERATED -- do not edit by hand.** Regenerated by "
                 "`scripts/generate_current_front.py` (runs in `governance.sh`).  ")
    lines.append("> Generated: %s  " % now)
    lines.append("> Derived from: %s" % provenance)
    if needs_review:
        lines.append(">  ")
        lines.append("> **needs_review: an anchor could not be derived from a source "
                     "(wording may have drifted) -- read the sources directly and re-run the generator.**")
    lines.append("")
    lines.append("## The one live front")
    lines.append("")
    lines.append(f["headline"])
    lines.append("")

    # live path
    if f["live_path_exqs"]:
        path = ", ".join(f["live_path_exqs"])
        if f["lead_exq"]:
            path = path.replace(f["lead_exq"], f["lead_exq"] + " (lead)", 1)
        if f.get("live_path_is_fallback"):
            lines.append("- **Live path (from the gate text; no separate live-campaign "
                         "section this snapshot):** %s" % path)
        else:
            lines.append("- **Live path:** %s" % path)
    else:
        lines.append("- **Live path:** (could not derive -- see insights_report.md)")
    lines.append("- **The gate:** %s" % f["gate"])
    if f["buildable_id"]:
        b = f["buildable_id"]
        if f["buildable_desc"]:
            b += " (%s)" % f["buildable_desc"]
        lines.append("- **Buildable now (independent of the wall):** %s" % b)

    # hypothesis-space hero question (the live rival-explanation narrowing).
    # Reports the state tally directly (alive / confirmed / resolved out) rather
    # than a single collapsed "N of M still standing" figure -- see the
    # GFLAG-0093 note in derive() for why a collapsed figure is the thing that
    # went stale. A hero present but not derivable (needs_review) is skipped here;
    # the top-of-doc needs_review banner already covers it.
    hero = f.get("hero")
    if hero and not hero.get("derive_failed"):
        bits = []
        if hero["alive"]:
            bits.append("%d alive" % hero["alive"])
        if hero["confirmed"]:
            bits.append("%d confirmed" % hero["confirmed"])
        if hero["resolved_out"]:
            bits.append("%d resolved out" % hero["resolved_out"])
        if hero["superseded"]:
            bits.append("%d superseded" % hero["superseded"])
        if not bits:
            bits.append("0 hypotheses")
        lines.append("- **Live question (hypothesis space):** %s -- %s (of %s total). "
                     "Full map: `/progress`." % (hero["short_title"], ", ".join(bits),
                                                  hero["initial"]))
    lines.append("")

    # closure headline
    if f["weighted_pct"] or f["remaining"]:
        pct = ("%s%%" % f["weighted_pct"]) if f["weighted_pct"] else "?"
        rem = f["remaining"] if f["remaining"] else "?"
        lines.append("## Closure headline")
        lines.append("")
        lines.append("- v3 weighted progress: **%s** -- %s node(s) remaining." % (pct, rem))
        lines.append("")

    lines.append("## Where the detail + history live (this doc keeps none)")
    lines.append("")
    lines.append("- Full project analysis (trends, health, recommendations): "
                 "[insights_report.md](../insights_report.md)")
    lines.append("- Closure rollup + drift (per-node status, what is left): "
                 "[closure_status.md](../evidence/planning/closure_status.md) / "
                 "[closure_drift.md](../evidence/planning/closure_drift.md)")
    lines.append("- Roadmap Status Snapshot: [roadmap.md](roadmap.md)")
    lines.append("- The append-only front-moving record: the "
                 "`failure_autopsy_*.json` stream + each `evidence/planning/*_plan.md`.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    f, needs_review = derive()
    text = render(f, needs_review, now)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    rel = os.path.relpath(OUT, ROOT)
    status = "needs_review" if needs_review else "ok"
    print("wrote %s (%s)" % (rel, status))
    if needs_review:
        print("  WARNING: at least one anchor could not be derived; check sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
