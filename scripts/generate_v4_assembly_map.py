#!/usr/bin/env python3
"""Generate the V4 assembly map -- a cross-plan roll-up over the V4/V5 forward
roadmaps (evidence/planning/*_v4_plan.md) that makes the KINDS of blocker
machine-readable and sequences the literature-pull sweep.

It reads the per-node `blocker_class` and `lit_pull_status` fields (added
2026-06-13) plus the existing status/severity/depends_on/blocking_on and emits:

  * a per-plan blocker-class taxonomy table,
  * the V3-side bottleneck register (every v3_gate + v3_substrate node, the
    nodes that -- if closed -- unblock downstream V4 work; this is what the
    user asked to "mark special"),
  * per-plan root-blocker resolution (walk depends_on to where the chain
    actually bottoms out, so a plan gated by ONE upstream node reads as such),
  * the lit-pull sweep order (grounding nodes, in-progress first, then by how
    much load-bearing work each plan's grounding unblocks), with the
    completion-set harvest targets pulled from each grounding node,
  * environment-substrate and no-owning-node planning gaps detected in the
    blocker text.

Output: evidence/planning/v4_assembly_map.md (+ .json sidecar). Warn-only,
exits 0; this is a planning aid, never a gate. Generation: v4/v5 plans only --
the V3 closure % is untouched.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/generate_v4_assembly_map.py
"""
from __future__ import annotations

import glob
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.", file=sys.stderr)
    sys.exit(0)

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "evidence" / "planning"
OUT_MD = PLANNING / "v4_assembly_map.md"
OUT_JSON = PLANNING / "v4_assembly_map.json"

BLOCKER_CLASSES = ["v3_gate", "v3_substrate", "sibling_node", "lit_gap", "deferred"]
BLOCKED_STATUSES = {"blocked", "deferred"}
# severity ranks for the sweep weighting
SEV_RANK = {"load-bearing": 3, "high": 2, "medium": 1, "low": 0}
LIT_ORDER = {"active": 0, "partial": 1, "none": 2, "done": 3}

ENV_RE = re.compile(
    r"(V4 environment with|multimodal .{0,20}input substrate|"
    r"CausalGridWorld\w* conflates|a new env\b|new env where)",
    re.IGNORECASE,
)
# node_text joins fragments with " || " so a flag capture cannot bleed across
# fragments; stop at the sentinel.
FLAG_RE = re.compile(r"flag:\s*([^|]+)", re.IGNORECASE)


def load_plan(path: Path) -> dict | None:
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---\n"):
        return None
    end = txt.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(txt[4:end])
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    return fm.get("closure_plan")


def node_text(node: dict) -> str:
    parts = [str(node.get("blocking_on") or "")]
    parts += [str(x) for x in (node.get("readiness_gate") or [])]
    parts.append(str(node.get("completion_note") or ""))
    return " || ".join(p for p in parts if p)


def root_blocker(node: dict, by_id: dict) -> tuple[str, str]:
    """Walk depends_on (within-plan) to the first node that is NOT blocked by a
    sibling -- the true bottleneck class + node id for this node's chain.
    Cross-plan deps terminate the walk (reported as the cross-plan node)."""
    seen = set()
    cur = node
    while True:
        cid = cur.get("id")
        if cid in seen:
            return (cur.get("blocker_class") or "cycle", cid)
        seen.add(cid)
        bc = cur.get("blocker_class")
        if bc != "sibling_node":
            return (bc or cur.get("status") or "open", cid)
        deps = [d for d in (cur.get("depends_on") or []) if d in by_id]
        if not deps:
            # sibling_node but no in-plan dep resolvable -> cross-plan / unbuilt
            cpl = cur.get("cross_plan_link") or []
            return ("cross_plan" if cpl else "sibling_unresolved", cid)
        # follow the most-blocking dep (prefer one that is itself non-open)
        nxt = None
        for d in deps:
            dn = by_id[d]
            if dn.get("blocker_class") in ("v3_gate", "v3_substrate", "lit_gap"):
                nxt = dn
                break
        cur = nxt or by_id[deps[0]]


def main() -> int:
    plans = []
    for path in sorted(glob.glob(str(PLANNING / "*_v4_plan.md"))):
        plan = load_plan(Path(path))
        if not plan:
            continue
        gen = str(plan.get("generation") or "v3").strip().lower()
        if gen == "v3":
            continue  # safety: never roll a V3 plan into this map
        plan["_file"] = Path(path).name
        plans.append(plan)

    rows = []
    v3_bottlenecks = []   # v3_gate + v3_substrate nodes
    grounding = []        # grounding (lit_pull_status-bearing) nodes
    env_gaps = []
    flag_gaps = []
    global_class = {c: 0 for c in BLOCKER_CLASSES}
    total_nodes = 0

    for plan in plans:
        nodes = [n for n in (plan.get("nodes") or []) if isinstance(n, dict)]
        by_id = {n.get("id"): n for n in nodes}
        counts = {c: 0 for c in BLOCKER_CLASSES}
        frontier = []   # actionable now: open, load-bearing/high, deps satisfied-ish
        gnode = None
        for n in nodes:
            total_nodes += 1
            bc = n.get("blocker_class")
            if bc in counts:
                counts[bc] += 1
                global_class[bc] += 1
            st = (n.get("status") or "").strip().lower()
            sev = (n.get("severity") or "").strip().lower()
            if st in ("open", "in_progress") and sev in ("load-bearing", "high"):
                frontier.append(n.get("id"))
            if "lit_pull_status" in n:
                gnode = n
            if bc in ("v3_gate", "v3_substrate"):
                v3_bottlenecks.append({
                    "plan": plan.get("id"),
                    "node": n.get("id"),
                    "class": bc,
                    "severity": sev,
                    "unblocks_claims": n.get("unblocks_claims") or [],
                    "blocking_on": (n.get("blocking_on") or "").strip(),
                })
            txt = node_text(n)
            if ENV_RE.search(txt):
                env_gaps.append({"plan": plan.get("id"), "node": n.get("id"),
                                 "why": (n.get("blocking_on") or txt)[:200]})
            for fm_ in FLAG_RE.findall(txt):
                flag_gaps.append({"plan": plan.get("id"), "node": n.get("id"),
                                  "flag": fm_.strip()[:160]})

        # load-bearing/high BLOCKED count = how much grounding this plan gates
        blocked_lb = sum(
            1 for n in nodes
            if (n.get("status") or "").lower() in BLOCKED_STATUSES
            and (n.get("severity") or "").lower() in ("load-bearing", "high")
        )
        if gnode is not None:
            grounding.append({
                "plan": plan.get("id"),
                "file": plan.get("_file"),
                "node": gnode.get("id"),
                "status": gnode.get("status"),
                "lit_pull_status": gnode.get("lit_pull_status"),
                "unblocks_claims": gnode.get("unblocks_claims") or [],
                "harvest": gnode.get("readiness_gate") or [],
                "blocked_lb": blocked_lb,
            })
        rows.append({
            "plan": plan.get("id"),
            "file": plan.get("_file"),
            "title": plan.get("title"),
            "n_nodes": len(nodes),
            "counts": counts,
            "frontier": frontier,
            "lit": gnode.get("lit_pull_status") if gnode else "MISSING",
        })

    # sweep order: in-progress/partial first (finish them), then `none` by the
    # amount of load-bearing blocked work the plan's grounding unblocks.
    def sweep_key(g):
        return (LIT_ORDER.get(g["lit_pull_status"], 9), -g["blocked_lb"], g["plan"])
    sweep = [g for g in sorted(grounding, key=sweep_key)
             if g["lit_pull_status"] != "done"]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    L = []
    L.append("# V4 Assembly Map -- cross-plan blocker taxonomy + lit-pull sweep")
    L.append("")
    L.append(f"Generated: {now} by `scripts/generate_v4_assembly_map.py`")
    L.append("")
    L.append(
        "Roll-up over the V4/V5 forward roadmaps. Reads each node's "
        "`blocker_class` (v3_gate | v3_substrate | sibling_node | lit_gap | "
        "deferred) and grounding `lit_pull_status` (none | active | partial | "
        "done). **Generation v4/v5 only -- the V3 closure % is untouched.** "
        "Warn-only planning aid; regenerate after editing any `*_v4_plan.md`."
    )
    L.append("")
    L.append("**Blocker classes**")
    L.append("")
    L.append("| class | meaning | how it clears |")
    L.append("|---|---|---|")
    L.append("| `v3_gate` | a V3-phase claim/experiment must close | run/close the V3 experiment |")
    L.append("| `v3_substrate` | a V3 substrate is inert/coarse/missing | V3 substrate repair or enrichment |")
    L.append("| `sibling_node` | waiting on another roadmap node | build the upstream node first |")
    L.append("| `lit_gap` | biology grounding owed before build | run the /lit-pull (see sweep) |")
    L.append("| `deferred` | explicitly off the critical path | nothing now; revisit on trigger |")
    L.append("")
    gc = global_class
    L.append(
        f"**Totals:** {total_nodes} nodes across {len(plans)} plans -- "
        f"v3_gate={gc['v3_gate']}, v3_substrate={gc['v3_substrate']}, "
        f"sibling_node={gc['sibling_node']}, lit_gap={gc['lit_gap']}, "
        f"deferred={gc['deferred']}. Only {gc['v3_gate'] + gc['v3_substrate']} "
        "of the blocked nodes are gated on the V3 side; the rest are intra-V4 "
        "sequencing."
    )
    L.append("")

    # --- per-plan taxonomy ----------------------------------------------------
    L.append("## Per-plan blocker taxonomy")
    L.append("")
    L.append("| plan | nodes | v3_gate | v3_sub | sibling | lit_gap | defer | grounding |")
    L.append("|------|------:|-------:|------:|-------:|-------:|-----:|-----------|")
    for r in sorted(rows, key=lambda x: x["plan"]):
        c = r["counts"]
        L.append(
            f"| {r['plan']} | {r['n_nodes']} | {c['v3_gate']} | "
            f"{c['v3_substrate']} | {c['sibling_node']} | {c['lit_gap']} | "
            f"{c['deferred']} | {r['lit']} |"
        )
    L.append("")

    # --- V3 bottleneck register ----------------------------------------------
    L.append(f"## V3-side bottleneck register ({len(v3_bottlenecks)})")
    L.append("")
    L.append(
        "The nodes that gate V4 from the V3 side -- closing these is what "
        "actually moves the roadmap. Everything classed `sibling_node` "
        "ultimately waits behind one of these (or behind a lit-pull)."
    )
    L.append("")
    L.append("| plan | node | class | sev | unblocks | blocker |")
    L.append("|------|------|-------|-----|----------|---------|")
    for b in sorted(v3_bottlenecks, key=lambda x: (x["class"], x["plan"])):
        why = b["blocking_on"].replace("|", "\\|")
        if len(why) > 170:
            why = why[:167] + "..."
        cl = ",".join(b["unblocks_claims"][:4])
        L.append(f"| {b['plan']} | `{b['node']}` | {b['class']} | {b['severity']} | {cl} | {why} |")
    L.append("")

    # --- lit-pull sweep -------------------------------------------------------
    L.append(f"## Literature-pull sweep order ({len(sweep)} pulls owed)")
    L.append("")
    L.append(
        "The first pass of assembly work. Each grounding node's /lit-pull must "
        "(a) ground its registered claims AND (b) harvest the co-constitutive "
        "circuit partners the mechanism presupposes -- so building the substrate "
        "does not omit jointly-necessary components. In-progress pulls are "
        "listed first (finish them); the rest are ordered by how much "
        "load-bearing blocked work the plan's grounding unblocks."
    )
    L.append("")
    for i, g in enumerate(sweep, 1):
        L.append(
            f"### {i}. {g['plan']} -- `{g['node']}` "
            f"[{g['lit_pull_status']}; gates {g['blocked_lb']} load-bearing/high blocked nodes]"
        )
        L.append("")
        L.append(f"- **Ground:** {', '.join(g['unblocks_claims']) or '(see node)'}")
        if g["harvest"]:
            L.append("- **Pull + completion-set harvest:**")
            for h in g["harvest"]:
                L.append(f"  - {h}")
        L.append("")

    # --- cross-cutting planning gaps -----------------------------------------
    L.append(f"## Cross-cutting planning gaps")
    L.append("")
    # de-dupe env gaps by node
    seen_env = set()
    env_u = [e for e in env_gaps if not (e["node"] in seen_env or seen_env.add(e["node"]))]
    L.append(f"**Environment-substrate gated ({len(env_u)})** -- blockers needing a "
             "richer V4 environment than gridworld. A shared prerequisite: build "
             "the env once, unblock all of these.")
    L.append("")
    for e in sorted(env_u, key=lambda x: x["plan"]):
        L.append(f"- `{e['node']}` ({e['plan']}): {e['why'].strip()}")
    L.append("")
    if flag_gaps:
        L.append(f"**Author-flagged no-owning-node gaps ({len(flag_gaps)})** -- a "
                 "blocker names a substrate/module that has no roadmap node yet.")
        L.append("")
        for fgap in flag_gaps:
            L.append(f"- `{fgap['node']}` ({fgap['plan']}): {fgap['flag']}")
        L.append("")

    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")

    payload = {
        "generated_at": now,
        "totals": {"nodes": total_nodes, "plans": len(plans), "by_class": global_class},
        "plans": rows,
        "v3_bottlenecks": v3_bottlenecks,
        "lit_sweep": sweep,
        "env_gaps": env_u,
        "flag_gaps": flag_gaps,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}")
    print(f"  nodes={total_nodes} plans={len(plans)} v3_bottlenecks={len(v3_bottlenecks)} "
          f"lit_pulls_owed={len(sweep)} env_gaps={len(env_u)} flag_gaps={len(flag_gaps)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
