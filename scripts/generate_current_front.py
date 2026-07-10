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

import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSIGHTS = os.path.join(ROOT, "insights_report.md")
CLOSURE = os.path.join(ROOT, "evidence", "planning", "closure_status.md")
OUT = os.path.join(ROOT, "docs", "CURRENT_FRONT.md")

# em/en dash class for tolerant matching of Claude-authored prose
DASH = r"[-–—]"


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


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

    # --- the one-line front headline ------------------------------------------
    # The '### The live front is ...' heading in insights_report.md is the single
    # most-important-front one-liner. Fallback: the live-campaign section heading.
    headline = _search(r"^###\s+(The live front[^\n]+)$", insights, default=None,
                       flags=re.MULTILINE)
    if not headline:
        headline = _search(r"^##\s+(The live campaign[^\n]+)$", insights, default=None,
                           flags=re.MULTILINE)
    if not headline:
        headline = "(could not derive front headline -- see insights_report.md)"
        needs_review = True
    f["headline"] = headline

    # --- live path: the lead diagnostic + the rest of the campaign fan-out -----
    # The '## The live campaign' table marks one row '(lead)'. Collect every
    # V3-EXQ id in that table, lead first.
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
    f["lead_exq"] = lead
    f["live_path_exqs"] = all_exq[:4]  # keep it short
    if not all_exq:
        needs_review = True

    # --- the gate: Recommendation 1 (the decided next step) --------------------
    # Anchor to the '## Recommendations' section so we get the DECISION, not the
    # first numbered list on the page (the 'genuinely hard part' enumeration).
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
        lines.append("- **Live path:** %s" % path)
    else:
        lines.append("- **Live path:** (could not derive -- see insights_report.md)")
    lines.append("- **The gate:** %s" % f["gate"])
    if f["buildable_id"]:
        b = f["buildable_id"]
        if f["buildable_desc"]:
            b += " (%s)" % f["buildable_desc"]
        lines.append("- **Buildable now (independent of the wall):** %s" % b)
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
