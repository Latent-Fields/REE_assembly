#!/usr/bin/env python3
"""
update_goblin_tale.py

Nightly refresh of the "campaign so far" stanza in the public goblin tale on the
GitHub Pages site (docs/ree_for_my_parents.md) -- and, best-effort, in the private
canonical creative file (../ree-paper/fantasy/the_goblin_who_would_not_name_the_soul.md
if that checkout is present alongside REE_assembly).

It rewrites ONLY the text between the CAMPAIGN_STATE markers, in the tale's voice,
from the real closure-map numbers. It NEVER writes an episode (those are hand-authored,
by the law of provenance) and NEVER names the soul.

Source of truth: evidence/planning/closure_status.md (regenerated earlier in
governance.sh by generate_closure_snapshot.py). If that snapshot is missing, the
stanza is left untouched.

Run:  python scripts/update_goblin_tale.py
      python scripts/update_goblin_tale.py --check   # report, change nothing
Idempotent. Stdlib only. ASCII-only stdout.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # REE_assembly/
SNAPSHOT = os.path.join(ROOT, "evidence", "planning", "closure_status.md")
PUBLIC_PAGE = os.path.join(ROOT, "docs", "ree_for_my_parents.md")
CANON_REL = os.path.join(ROOT, "..", "ree-paper", "fantasy",
                         "the_goblin_who_would_not_name_the_soul.md")

START = "<!-- CAMPAIGN_STATE:START -->"
END = "<!-- CAMPAIGN_STATE:END -->"


def parse_snapshot(text):
    """Pull the few numbers the stanza needs out of closure_status.md."""
    d = {}
    m = re.search(r"Weighted progress:\s*\*\*([\d.]+)%\*\*\s*across\s*(\d+)\s*non-deferred nodes in\s*(\d+)\s*plan", text)
    if m:
        d["pct"] = float(m.group(1))
        d["nodes"] = int(m.group(2))
        d["plans"] = int(m.group(3))
    m = re.search(r"Remaining \(open/in-progress/blocked/partial\):\s*\*\*(\d+)\*\*", text)
    if m:
        d["remaining"] = int(m.group(1))
    m = re.search(r"Done:\s*(\d+)\s*nodes", text)
    if m:
        d["done"] = int(m.group(1))
    # plan table rows: | `file` | Title | nodes | NN% | ... | date |
    plans = []
    for row in re.finditer(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|", text, re.M):
        plans.append({"file": row.group(1), "title": row.group(2).strip(),
                      "nodes": int(row.group(3)), "pct": int(row.group(4))})
    d["plan_rows"] = plans
    return d


def compose_stanza(d):
    """Build the campaign stanza, in the tale's voice, from the parsed numbers."""
    if "pct" not in d:
        return None
    pct = d["pct"]
    done = d.get("done")
    remaining = d.get("remaining")
    finished = [p for p in d.get("plan_rows", []) if p["pct"] >= 100]
    # the "next gate": the most-complete plan that is not yet done
    open_plans = sorted([p for p in d.get("plan_rows", []) if p["pct"] < 100],
                        key=lambda p: -p["pct"])
    lines = []
    lines.append(START)
    lines.append("### The campaign so far")
    lines.append("")
    # Lead sentence scales its tone to progress, but never crowns anything.
    lead = ("The under-mountain map is **{:.0f}%** lit.".format(pct))
    if done is not None and remaining is not None:
        lead += (" Of the gates that matter for this stretch, **{}** stand open and "
                 "**{}** are still shut.".format(done, remaining))
    lines.append("*" + lead + "*")
    lines.append("")
    if finished:
        names = ", ".join(_pretty(p["title"]) for p in finished[:4])
        more = "" if len(finished) <= 4 else ", and others"
        lines.append("*Gates the goblin has closed for good: {}{}.*".format(names, more))
        lines.append("")
    if open_plans:
        nxt = open_plans[0]
        lines.append("*Nearest to opening: {} ({}%). The gate of the council is still "
                     "being rewritten; the goblin is still at the table, the lantern still "
                     "tied to the blade.*".format(_pretty(nxt["title"]), nxt["pct"]))
        lines.append("")
    lines.append("<sub>Refreshed automatically from the closure map. The only part of the "
                 "tale a machine is allowed to write -- it does not name the soul.</sub>")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def _pretty(title):
    # Trim the parenthetical sub-titles so the prose stays clean.
    return re.sub(r"\s*\(.*?\)\s*$", "", title).strip()


def splice(path, stanza):
    """Replace the CAMPAIGN_STATE block in `path`. Returns (changed, reason)."""
    if not os.path.exists(path):
        return False, "file absent"
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        return False, "markers absent"
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = pat.sub(lambda _m: stanza, text, count=1)
    if new == text:
        return False, "no change"
    open(path, "w", encoding="utf-8").write(new)
    return True, "updated"


def main():
    check = "--check" in sys.argv
    if not os.path.exists(SNAPSHOT):
        print("update_goblin_tale: closure snapshot not found ({}); leaving tale untouched.".format(
            os.path.relpath(SNAPSHOT, ROOT)))
        return 0
    d = parse_snapshot(open(SNAPSHOT, encoding="utf-8").read())
    stanza = compose_stanza(d)
    if stanza is None:
        print("update_goblin_tale: could not parse progress from snapshot; leaving tale untouched.")
        return 0
    if check:
        print("update_goblin_tale --check: would set campaign stanza to {:.0f}% "
              "({} done / {} remaining).".format(d.get("pct", 0), d.get("done", "?"), d.get("remaining", "?")))
        return 0
    any_change = False
    for label, path in [("public page", PUBLIC_PAGE), ("canonical tale", CANON_REL)]:
        changed, reason = splice(path, stanza)
        rel = os.path.relpath(path, ROOT)
        print("update_goblin_tale: {} ({}) -> {}".format(label, rel, reason))
        any_change = any_change or changed
    if not any_change:
        print("update_goblin_tale: campaign stanza already current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
