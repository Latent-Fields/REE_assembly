#!/usr/bin/env python3
"""Generate a committed, server-free snapshot of the REE-v3 closure map.

The authoritative closure aggregation normally only exists when serve.py is
running (`/api/closure` -> closure.html). An agent reading the static repo --
no dev server -- has to discover and parse every evidence/planning/*_plan.md
frontmatter block by hand to answer "what still has to happen to close v3".

This script writes that rollup to evidence/planning/closure_status.md so the
answer is one committed file. It mirrors serve.py's read_closure() aggregation
(same CLOSURE_STATUS_WEIGHTS, same auto-discovery of every *_plan.md), reusing
check_closure_drift.parse_plan_frontmatter so the parse behaviour cannot drift
between the two scripts.

It is a hint/snapshot, NOT a gate: it never blocks the governance pipeline and
always exits 0. Accuracy auditing (node status vs. actual experiment terminal
state) is the job of check_closure_drift.py; this script links to that report
rather than re-deriving it.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/generate_closure_snapshot.py
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

# Reuse the drift checker's frontmatter parser so parse behaviour stays in lockstep.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from check_closure_drift import parse_plan_frontmatter
except Exception:  # pragma: no cover - fallback keeps the snapshot self-contained
    parse_plan_frontmatter = None  # type: ignore

# Cognitive-architecture-graveyard health ratios (WS-8 recommendation #1):
# surface governance-mass:cognitive-mass + capability-earning:registered as a
# first-class, periodically-reported block on the closure dashboard. Instrument
# only -- PROMOTES NOTHING. Imported softly so a git/parse hiccup in the ratio
# computation never blocks the closure snapshot.
try:
    from graveyard_health_ratios import render_markdown as render_graveyard_ratios
except Exception:  # pragma: no cover - dashboard still generates without the section
    render_graveyard_ratios = None  # type: ignore

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
SNAPSHOT = PLANNING_DIR / "closure_status.md"
DRIFT_REPORT = PLANNING_DIR / "closure_drift.md"
# Visual rollup for the GitHub Pages site (Jekyll builds docs/ only, so the
# evidence/planning snapshot above is invisible there). Regenerated every run.
DOCS_DASHBOARD = REPO_ROOT / "docs" / "closure_dashboard.md"

# Closure-status weights: import serve.py's CLOSURE_STATUS_WEIGHTS as the SINGLE
# SOURCE OF TRUTH so the static snapshot and the live /api/closure map can never
# report different % (they drifted once -- serve.py was missing upstream_blocked /
# blocked_pending_substrate / pending_governance_stamp, zero-crediting nodes the
# snapshot scored). `import serve` is stdlib-only and side-effect-free (~0.1s, no
# server bind). The inline fallback keeps the snapshot self-contained if serve.py
# is unavailable and MUST stay byte-identical to serve.py CLOSURE_STATUS_WEIGHTS.
# None == excluded from the progress denominator (deferred is not "what closes v3").
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # repo root for `import serve`
try:
    from serve import CLOSURE_STATUS_WEIGHTS as STATUS_WEIGHTS
except Exception:  # pragma: no cover - keep the snapshot self-contained
    STATUS_WEIGHTS = {
        "done": 1.0,
        "partial": 0.5,
        "in_progress": 0.4,
        "in-progress": 0.4,
        "blocked": 0.1,
        "upstream_blocked": 0.1,
        "blocked_pending_substrate": 0.1,
        "tracked": 0.2,
        "pending_governance_stamp": 0.4,
        "open": 0.0,
        "pending": 0.0,
        # Required-but-under-construction; excluded from the % (does not punish
        # correct assembly), surfaced on a separate assembly-frontier axis.
        # MUST stay byte-identical to serve.py CLOSURE_STATUS_WEIGHTS.
        "assembling": None,
        "open_by_design": None,
        "deferred": None,
        "deferred V4": None,
        "deferred_v4": None,
        "deferred_v5": None,
        "parked": None,
        "parked_indefinite": None,
        "closed": None,
    }

# Deferred == not required for v3 closure (excluded from the progress denominator).
DEFERRED_STATUSES = {"deferred", "deferred_v4"}
# Assembling == required for v3 but actively / intentionally under construction.
# Excluded from the closure % (so unhurried assembly is never scored as failure)
# AND held out of `remaining` (it is not a stalled gap) -- reported on its own
# "assembly frontier" axis instead. The anti-forcing keystone: the green-board
# gets a place to say "this is being built, leave it alone" without punishing
# the % or nagging it as drift. See evidence/planning/assembly_vs_closure_plan.md.
ASSEMBLING_STATUSES = {"assembling", "open_by_design"}
# "Remaining" is computed exhaustively as: not done and not deferred. That way a
# new/unforeseen status string (the snapshot has been bitten by
# blocked_pending_substrate before) always lands in a visible bucket instead of
# vanishing from every categorized section.


def _norm_status(s) -> str:
    if not s:
        return "open"
    return str(s).strip().lower().replace(" ", "_").replace("-", "_")


def _fallback_parse(path: Path):
    """Minimal frontmatter parse if check_closure_drift import failed."""
    try:
        import yaml
    except ImportError:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except Exception:
        return None
    return fm if isinstance(fm, dict) else None


def _parse(path: Path):
    if parse_plan_frontmatter is not None:
        return parse_plan_frontmatter(path)
    return _fallback_parse(path)


def _blocker(node: dict) -> str:
    """Short human-readable active blocker for a node."""
    for key in ("blocking_on", "resume_condition"):
        v = node.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
    ext = node.get("blocking_external")
    if isinstance(ext, list) and ext:
        return "ext: " + ", ".join(str(x) for x in ext)
    dep = node.get("depends_on")
    if isinstance(dep, list) and dep:
        return "depends_on: " + ", ".join(str(x) for x in dep)
    return ""


def _live_next(node: dict) -> str:
    """The projected next-step from a two-plane `live:` block (status_history_plane
    SHP-2), used as a fallback when a collapsed node no longer carries `awaiting:`.
    Empty string when the node has no `live` block."""
    live = node.get("live")
    if isinstance(live, dict):
        nxt = live.get("next")
        if isinstance(nxt, str) and nxt.strip():
            return nxt.strip()
    return ""


def _cell(v) -> str:
    """Sanitise a value for a markdown table cell."""
    if v is None:
        return ""
    return str(v).replace("|", "\\|").replace("\n", " ").strip()


def _bar(pct: float) -> str:
    """Inline-HTML progress bar (no external CSS; renders on plain GitHub Pages)."""
    colour = "#cf222e" if pct < 40 else "#bf8700" if pct < 75 else "#1a7f37"
    return (
        '<div style="background:#eaeef2;border-radius:5px;height:18px;width:100%;'
        'max-width:520px;overflow:hidden;display:inline-block;vertical-align:middle">'
        f'<div style="background:{colour};height:18px;width:{pct:.1f}%"></div></div>'
    )


def write_docs_dashboard(plans, overall, tally, n_remaining, n_deferred,
                         n_done, roadmap_plans, now_iso, n_assembling=0) -> None:
    """Emit a visual closure dashboard into docs/ for the Pages site."""
    o_total = n_remaining + n_done  # non-deferred V3 nodes
    D: list[str] = []
    D.append("---")
    D.append("title: Closure Dashboard")
    D.append("nav_order: 11")
    D.append("---")
    D.append("")
    D.append("# REE-v3 Closure Dashboard")
    D.append("")
    D.append(f"_Generated {now_iso} — regenerated every governance run; do not edit by hand._")
    D.append("")
    D.append(
        "How close V3 is to closing, per plan. Weighted by node status "
        "(done = 1, partial / in-progress = part credit, open / blocked = 0). "
        "The companion **drift audit** checks whether each node's self-declared "
        "status matches its experiments. This is the static, server-free view of "
        "the live `/closure` dashboard."
    )
    D.append("")
    D.append("## Overall")
    D.append("")
    D.append(f"<p style=\"font-size:1.6em;font-weight:600;margin:.2em 0\">{overall * 100:.1f}%</p>")
    D.append("")
    D.append(_bar(overall * 100))
    D.append("")
    D.append(
        f"{int(o_total)} non-deferred nodes across {len(plans)} plan(s) · "
        f"**{n_done} done · {n_remaining} remaining · {n_deferred} deferred**"
        + (f" · **{n_assembling} on the assembly frontier** (under construction, "
           "off the % axis)" if n_assembling else "")
        + "."
    )
    D.append("")
    tally_str = " · ".join(f"`{k}`&nbsp;{v}" for k, v in sorted(tally.items()))
    D.append(f"Status tally: {tally_str}")
    D.append("")
    D.append("## By plan")
    D.append("")
    D.append('<table style="border-collapse:collapse;width:100%">')
    D.append(
        '<thead><tr style="text-align:left;border-bottom:2px solid #d0d7de">'
        '<th style="padding:6px 10px">Plan</th>'
        '<th style="padding:6px 10px;width:55%">Progress</th>'
        '<th style="padding:6px 10px">Nodes</th>'
        '<th style="padding:6px 10px">Updated</th></tr></thead><tbody>'
    )
    for p in sorted(plans, key=lambda x: x["progress"]):
        pct = p["progress"] * 100
        title = _cell(p["title"])
        lu = _cell(p["last_updated"])
        D.append(
            '<tr style="border-bottom:1px solid #eaeef2">'
            f'<td style="padding:6px 10px"><strong>{title}</strong></td>'
            f'<td style="padding:6px 10px">{_bar(pct)}&nbsp;<span style="color:#57606a">{pct:.0f}%</span></td>'
            f'<td style="padding:6px 10px">{p["node_count"]}</td>'
            f'<td style="padding:6px 10px;color:#57606a">{lu}</td></tr>'
        )
    D.append("</tbody></table>")
    D.append("")
    if roadmap_plans:
        D.append(
            f"_Plus {len(roadmap_plans)} V4/V5 forward-roadmap plan(s), excluded "
            "from the V3 closure percentage._"
        )
        D.append("")
    D.append(
        "Full node-by-node detail (remaining work, blockers, owners) is in the "
        "generated `evidence/planning/closure_status.md` snapshot."
    )
    D.append("")

    # Graveyard health ratios (WS-8 rec #1) -- a companion health signal to the
    # closure %. Closure measures "how complete"; these measure "is the effort
    # earning capability or just managing the theory". Soft-imported so the
    # dashboard still renders if the ratio computation fails.
    if render_graveyard_ratios is not None:
        try:
            D.append(render_graveyard_ratios())
            D.append("")
        except Exception as e:  # pragma: no cover - never block the snapshot
            D.append("## Graveyard health ratios")
            D.append("")
            D.append(f"_Section unavailable this run ({e.__class__.__name__})._")
            D.append("")

    DOCS_DASHBOARD.write_text("\n".join(D) + "\n", encoding="utf-8")


def main() -> int:
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    plan_files = sorted(PLANNING_DIR.glob("*_plan.md")) if PLANNING_DIR.exists() else []

    plans = []                 # per-plan rollup dicts
    no_frontmatter = []        # *_plan.md with no closure_plan block
    all_nodes = []             # flattened node records with plan context
    # Node status strings with no entry in STATUS_WEIGHTS silently fall through
    # `.get(st, 0.0)` and get scored as `open` (unstarted) regardless of what they
    # actually mean -- confirmed 2026-08-13: `closed`/`parked`/`parked_indefinite`
    # (terminal-but-not-`done` decisions) and `pending` (queued) were all scoring
    # as 0.0-weighted `open` work before their weights were added. Collecting and
    # printing every miss here (instead of letting STATUS_WEIGHTS.get()'s default
    # absorb it quietly) is what keeps a FUTURE new status string from repeating
    # this -- the fix for one drift incident should be catching the next one, not
    # just patching the one found.
    unknown_statuses: list[tuple[str, str, str]] = []

    for path in plan_files:
        fm = _parse(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            no_frontmatter.append(path.name)
            continue

        # generation: v3 (default) | v4 | v5. V4/V5 forward-roadmap plans are
        # segmented out of the V3 closure % below; a plan with no field is V3.
        gen = str(plan.get("generation") or "v3").strip().lower()
        nodes = [n for n in (plan.get("nodes") or []) if isinstance(n, dict) and n.get("id")]
        counts: dict[str, int] = {}
        w_done = w_total = 0.0
        for n in nodes:
            st = _norm_status(n.get("status"))
            counts[st] = counts.get(st, 0) + 1
            if st not in STATUS_WEIGHTS:
                unknown_statuses.append((path.name, str(n.get("id")), st))
            w = STATUS_WEIGHTS.get(st, 0.0)
            if w is not None:
                w_total += 1.0
                w_done += w
            rec = dict(n)
            rec["_status"] = st
            rec["_generation"] = gen
            rec["_plan_id"] = str(plan.get("id") or path.stem)
            rec["_plan_file"] = path.name
            all_nodes.append(rec)

        plans.append({
            "id": str(plan.get("id") or path.stem),
            "title": plan.get("title") or path.stem,
            "file": path.name,
            "generation": gen,
            "last_updated": plan.get("last_updated"),
            "node_count": len(nodes),
            "counts": counts,
            "progress": (w_done / w_total) if w_total else 0.0,
        })

    # Segment by generation. The V3 sections below (overall %, remaining,
    # deferred, done, plans table) are computed over V3 nodes ONLY so V4/V5
    # roadmap plans never dilute the V3 closure %. Roadmap nodes get their own
    # section at the foot of the snapshot.
    DEFAULT_GEN = "v3"
    roadmap_nodes = [n for n in all_nodes if n.get("_generation", DEFAULT_GEN) != DEFAULT_GEN]
    roadmap_plans = [p for p in plans if p.get("generation", DEFAULT_GEN) != DEFAULT_GEN]
    all_nodes = [n for n in all_nodes if n.get("_generation", DEFAULT_GEN) == DEFAULT_GEN]
    plans = [p for p in plans if p.get("generation", DEFAULT_GEN) == DEFAULT_GEN]

    # Overall weighted progress across all non-deferred V3 nodes, all V3 plans.
    o_done = o_total = 0.0
    tally: dict[str, int] = {}
    for n in all_nodes:
        st = n["_status"]
        tally[st] = tally.get(st, 0) + 1
        w = STATUS_WEIGHTS.get(st, 0.0)
        if w is not None:
            o_total += 1.0
            o_done += w
    overall = (o_done / o_total) if o_total else 0.0

    done = [n for n in all_nodes if n["_status"] == "done"]
    deferred = [n for n in all_nodes if n["_status"] in DEFERRED_STATUSES]
    assembling = [n for n in all_nodes if n["_status"] in ASSEMBLING_STATUSES]
    # `remaining` is the genuine close-this-out backlog: not done, not deferred,
    # AND not assembling. An assembling node is on the frontier, not the backlog,
    # so it does not inflate "what is left to close v3".
    remaining = [n for n in all_nodes
                 if n["_status"] != "done"
                 and n["_status"] not in DEFERRED_STATUSES
                 and n["_status"] not in ASSEMBLING_STATUSES]

    # Order remaining by phase then severity so the "do next" items float up.
    sev_rank = {"load-bearing": 0, "load_bearing": 0, "high": 1, "medium": 2, "low": 3}

    def _phase_key(n):
        ph = n.get("phase")
        try:
            ph = int(ph)
        except (TypeError, ValueError):
            ph = 99
        return (ph, sev_rank.get(str(n.get("severity") or "medium").lower(), 2))

    remaining.sort(key=_phase_key)

    L: list[str] = []
    L.append("# REE-v3 Closure Status (snapshot)")
    L.append("")
    L.append(f"Generated: {now_iso}")
    L.append("")
    L.append(
        "GENERATED FILE -- do not edit by hand. This is a static, server-free "
        "snapshot of the closure map that serve.py serves live at `/api/closure` "
        "-> `/closure`. It is rebuilt from the `closure_plan` frontmatter of "
        "every `evidence/planning/*_plan.md` (auto-discovered, not whitelisted). "
        "Regenerate with `python scripts/generate_closure_snapshot.py` (runs "
        "automatically in `governance.sh`)."
    )
    L.append("")
    L.append(
        "ACCURACY: this snapshot reports each node's self-declared `status`. "
        "Whether that status matches the actual terminal state of its experiments "
        "is audited separately by `check_closure_drift.py` -> "
        "[`closure_drift.md`](closure_drift.md). Read both together."
    )
    L.append("")

    L.append("## Overall")
    L.append("")
    L.append(
        f"- Weighted progress: **{overall * 100:.1f}%** across {int(o_total)} "
        f"non-deferred nodes in {len(plans)} plan(s) with closure frontmatter."
    )
    L.append(f"- Remaining (open/in-progress/blocked/partial): **{len(remaining)}** nodes.")
    L.append(
        f"- Assembly frontier (required, under construction -- a SEPARATE axis, "
        f"not counted in the % above and not a stalled backlog): "
        f"**{len(assembling)}** nodes."
    )
    L.append(f"- Deferred (not required for v3 closure): {len(deferred)} nodes.")
    L.append(f"- Done: {len(done)} nodes.")
    tally_str = "  ".join(f"{k}={v}" for k, v in sorted(tally.items()))
    L.append(f"- Status tally: {tally_str}")
    L.append("")

    L.append("## Plans")
    L.append("")
    L.append("| plan | title | nodes | progress | status counts | last_updated |")
    L.append("|------|-------|-------|----------|---------------|--------------|")
    for p in sorted(plans, key=lambda x: x["progress"]):
        cstr = " ".join(f"{k}:{v}" for k, v in sorted(p["counts"].items()))
        L.append(
            f"| `{p['file']}` | {_cell(p['title'])} | {p['node_count']} | "
            f"{p['progress'] * 100:.0f}% | {_cell(cstr)} | {_cell(p['last_updated'])} |"
        )
    L.append("")

    L.append(f"## Remaining work to close v3 ({len(remaining)})")
    L.append("")
    L.append("Ordered by phase, then severity. This is the answer to \"what is left.\"")
    L.append("")
    if not remaining:
        L.append("_None -- all non-deferred nodes are done._")
    else:
        L.append("| plan | node | title | status | phase | sev | owner_exq | active blocker | last_updated |")
        L.append("|------|------|-------|--------|-------|-----|-----------|----------------|--------------|")
        for n in remaining:
            L.append(
                "| {pl} | `{nid}` | {title} | {st} | {ph} | {sev} | {exq} | {blk} | {lu} |".format(
                    pl=n["_plan_file"],
                    nid=_cell(n.get("id")),
                    title=_cell(n.get("title"))[:80],
                    st=n["_status"],
                    ph=_cell(n.get("phase")),
                    sev=_cell(n.get("severity") or "medium"),
                    exq=_cell(n.get("owner_exq"))[:48],
                    blk=_cell(_blocker(n))[:90],
                    lu=_cell(n.get("last_updated")),
                )
            )
    L.append("")

    L.append(f"## Assembly frontier -- required, under construction ({len(assembling)})")
    L.append("")
    L.append(
        "Nodes whose honest state is \"the substrate for this is being assembled\" "
        "-- NOT a stalled gap and NOT deferred. They are held out of the closure % "
        "(so correct, unhurried construction is never scored as failure) and out of "
        "the Remaining backlog, and surfaced here on their own axis. `awaiting` names "
        "the substrate under construction; `assembly_status` is its build state "
        "(queued / in_progress / built); a node is restful until its optional "
        "`revisit_after` date passes (see the drift report's Assembly-frontier section)."
    )
    L.append("")
    if not assembling:
        L.append("_None -- no node currently declares itself on the assembly frontier._")
    else:
        L.append("| plan | node | title | status | awaiting | assembly_status | revisit_after | last_updated |")
        L.append("|------|------|-------|--------|----------|-----------------|---------------|--------------|")
        for n in sorted(assembling, key=lambda x: (x["_plan_file"], str(x.get("id")))):
            L.append(
                "| {pl} | `{nid}` | {title} | {st} | {aw} | {asx} | {rv} | {lu} |".format(
                    pl=n["_plan_file"],
                    nid=_cell(n.get("id")),
                    title=_cell(n.get("title"))[:70],
                    st=n["_status"],
                    aw=_cell(n.get("awaiting") or _live_next(n) or _blocker(n))[:60],
                    asx=_cell(n.get("assembly_status")),
                    rv=_cell(n.get("revisit_after")),
                    lu=_cell(n.get("last_updated")),
                )
            )
    L.append("")

    L.append(f"## Deferred -- not required for v3 closure ({len(deferred)})")
    L.append("")
    if not deferred:
        L.append("_None._")
    else:
        L.append("| plan | node | title | status | reason / blocker |")
        L.append("|------|------|-------|--------|------------------|")
        for n in deferred:
            L.append(
                "| {pl} | `{nid}` | {title} | {st} | {blk} |".format(
                    pl=n["_plan_file"],
                    nid=_cell(n.get("id")),
                    title=_cell(n.get("title"))[:80],
                    st=n["_status"],
                    blk=_cell(_blocker(n))[:90],
                )
            )
    L.append("")

    L.append(f"## Done ({len(done)})")
    L.append("")
    if not done:
        L.append("_None._")
    else:
        for n in sorted(done, key=lambda x: (x["_plan_file"], str(x.get("id")))):
            title = _cell(n.get("title"))[:90]
            L.append(f"- `{n['_plan_file']}` `{_cell(n.get('id'))}` -- {title}")
    L.append("")

    L.append(f"## Plans WITHOUT closure_plan frontmatter ({len(no_frontmatter)})")
    L.append("")
    L.append(
        "These `*_plan.md` files exist but carry no `closure_plan` block, so "
        "their gaps are invisible to the structured closure map (they show as "
        "empty placeholder cards in the dashboard). Retrofit frontmatter to "
        "fold them in."
    )
    L.append("")
    if not no_frontmatter:
        L.append("_None -- every plan doc is mapped._")
    else:
        for name in no_frontmatter:
            L.append(f"- `evidence/planning/{name}`")
    L.append("")

    # --- V4/V5 forward roadmap (segmented out of the V3 closure % above) ---
    L.append("## V4 / V5 forward roadmap (excluded from v3 closure %)")
    L.append("")
    L.append(
        "Forward-roadmap plans (`generation: v4` / `v5`). These are NOT closure "
        "maps -- V4/V5 have no experiments yet, so their nodes carry no "
        "`owner_exq` and do not count toward the V3 closure percentage. Each "
        "node's gate is the V3-era prerequisite that must land first."
    )
    L.append("")
    if not roadmap_plans:
        L.append("_None registered yet._")
    else:
        # per-generation rollup line
        gens = sorted({p.get("generation", "?") for p in roadmap_plans})
        for g in gens:
            g_nodes = [n for n in roadmap_nodes if n.get("_generation") == g]
            gd = gt = 0.0
            for n in g_nodes:
                w = STATUS_WEIGHTS.get(n["_status"], 0.0)
                if w is not None:
                    gt += 1.0
                    gd += w
            g_plans = [p for p in roadmap_plans if p.get("generation") == g]
            L.append(
                f"- **{g.upper()}**: {(gd / gt * 100) if gt else 0.0:.1f}% across "
                f"{int(gt)} non-deferred nodes in {len(g_plans)} plan(s)."
            )
        L.append("")
        L.append("| gen | plan | node | title | status | sev | gate (readiness) | last_updated |")
        L.append("|-----|------|------|-------|--------|-----|------------------|--------------|")
        for n in sorted(roadmap_nodes, key=_phase_key):
            gate = n.get("readiness_gate")
            if isinstance(gate, list) and gate:
                gate_s = str(gate[0])
            else:
                gate_s = _blocker(n)
            L.append(
                "| {g} | {pl} | `{nid}` | {title} | {st} | {sev} | {gate} | {lu} |".format(
                    g=n.get("_generation", ""),
                    pl=n["_plan_file"],
                    nid=_cell(n.get("id")),
                    title=_cell(n.get("title"))[:70],
                    st=n["_status"],
                    sev=_cell(n.get("severity") or "medium"),
                    gate=_cell(gate_s)[:90],
                    lu=_cell(n.get("last_updated")),
                )
            )
    L.append("")

    SNAPSHOT.write_text("\n".join(L) + "\n", encoding="utf-8")

    write_docs_dashboard(plans, overall, tally, len(remaining), len(deferred),
                         len(done), roadmap_plans, now_iso, len(assembling))

    print(f"Closure snapshot written: {SNAPSHOT.relative_to(REPO_ROOT)}")
    print(f"Closure dashboard written: {DOCS_DASHBOARD.relative_to(REPO_ROOT)}")
    print(
        f"  plans_mapped={len(plans)}  remaining={len(remaining)}  "
        f"assembling={len(assembling)}  "
        f"deferred={len(deferred)}  done={len(done)}  "
        f"plans_without_frontmatter={len(no_frontmatter)}  "
        f"overall_progress={overall * 100:.1f}%  "
        f"roadmap_plans={len(roadmap_plans)}  roadmap_nodes={len(roadmap_nodes)}"
    )
    if unknown_statuses:
        print(
            f"WARNING: {len(unknown_statuses)} node(s) use a status not in "
            "STATUS_WEIGHTS -- scored as `open` (0.0) by default, which is almost "
            "certainly wrong. Add the status to CLOSURE_STATUS_WEIGHTS in serve.py "
            "(and the byte-identical fallback in this file) or fix the node:"
        )
        for plan_file, node_id, status in unknown_statuses:
            print(f"    {plan_file}  {node_id}  status={status!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
