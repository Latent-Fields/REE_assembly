#!/usr/bin/env python3
"""Split claims.yaml `depends_on` into a DAG prerequisite layer and an undirected
`coupled_with` layer (GOV-EDGE-1, 2026-09-04).

WHY
---
`depends_on` was carrying three meanings at once: a directed build/evidential
prerequisite, an undirected architectural coupling (ARC-007 <-> ARC-018, the
hippocampal store/replay vs rollout pair), and a mutual explanation (a question,
its invariant and its mechanism all pointing at each other). Only the first
meaning has an acyclicity invariant worth enforcing, and while one field carried
all three the invariant could not be enforced anywhere: docs/claims/claim_index.md
(IMPL-018) said the edges "must stay acyclic" while scripts/validate_claims.py
(2026-09-01) said the graph "is not acyclic and is not meant to be". Measured on
2026-09-04: 1100 claims, 4012 depends_on edges, 25 cyclic SCCs covering 262
claims, one of them 197 claims wide. `emergent_from` (79 edges) was already a DAG.

WHAT THIS DOES
--------------
Moves the cycle-closing edges OUT of `depends_on` and INTO a new symmetric
`coupled_with` list, by two mechanical rules, in this order:

  1. MUTUAL PAIR. If A depends_on B and B depends_on A, neither can be a
     prerequisite of the other: both directions move to coupled_with. The one
     exception is an `emergent_from` edge, which is directional by definition and
     is never moved (its reverse is).
  2. RESIDUAL FEEDBACK ARC SET. For whatever cycles survive rule 1, repeatedly
     find one cycle and move ONE of its edges, chosen by a cost that prefers the
     edge running DOWN the abstraction ladder (an ARC/SD/INV claim depending on a
     MECH or Q is the direction a prerequisite normally does not run), then the
     edge whose source has the most out-edges (least specific), then lexical
     order for determinism. `emergent_from` edges are never chosen.

Rule 1 is unambiguous. Rule 2 is a HEURISTIC and every edge it moves is tagged
`cycle-break; re-judge` in the inline YAML comment and listed in the JSON audit
so governance can swap which edge of a given cycle is the coupled one. The
mechanical move preserves every claim's other fields byte-for-byte: the edit is
text-level (claims.yaml carries ~2500 inline comments that a yaml.dump would
destroy), and the script re-parses the result and asserts that only
`depends_on`/`coupled_with` changed, exactly as planned, and that `depends_on`
is now acyclic.

`coupled_with` is written SYMMETRIC (both endpoints list each other), which is
what validate_claims.py's `validate_edge_types` warns on if it drifts.

Idempotent: on an already-acyclic registry it reports nothing to do and writes
nothing.

USAGE
-----
  python3 scripts/split_claim_edge_types.py --dry-run
  python3 scripts/split_claim_edge_types.py --apply --audit-json <path>
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLAIMS_YAML = ROOT / "docs" / "claims" / "claims.yaml"
DATE = "2026-09-04"
RULE_ID = "GOV-EDGE-1"

sys.setrecursionlimit(50000)

# Abstraction ladder used by the residual-cycle cost. Lower number = more
# foundational. A prerequisite edge normally runs from a HIGHER number to a
# LOWER one (a mechanism depends on its architecture). An edge running the other
# way inside a cycle is the one most likely to be coupling, not prerequisite.
_LADDER = {"IMPL": 0, "ARC": 1, "SD": 1, "INV": 2, "MECH": 3, "GAP": 3, "LIT": 3,
           "FUN": 3, "SENT": 3, "GOV": 3, "Q": 4}


def _prefix(cid: str) -> str:
    return cid.split("-", 1)[0]


def _level(cid: str) -> int:
    return _LADDER.get(_prefix(cid), 3)


# --------------------------------------------------------------------------- graph
def load_graph(claims):
    ids = {c["id"] for c in claims if c.get("id")}
    g = collections.defaultdict(set)
    ef = set()
    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        for x in (c.get("depends_on") or []):
            if isinstance(x, str) and x in ids and x != cid:
                g[cid].add(x)
        for x in (c.get("emergent_from") or []):
            if isinstance(x, str) and x in ids:
                ef.add((cid, x))
    return ids, g, ef


def cyclic_sccs(ids, g):
    idx, low, st, on, out, n = {}, {}, [], set(), [], [0]

    def sc(v):
        idx[v] = low[v] = n[0]
        n[0] += 1
        st.append(v)
        on.add(v)
        for w in g[v]:
            if w not in idx:
                sc(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop()
                on.discard(w)
                comp.append(w)
                if w == v:
                    break
            out.append(comp)

    for v in sorted(ids):
        if v not in idx:
            sc(v)
    return [sorted(s) for s in out if len(s) > 1]


def find_one_cycle(g, comp):
    cs = set(comp)
    start = comp[0]
    stack = [(start, iter(sorted(g[start])))]
    path, onp = [start], {start}
    while stack:
        v, it = stack[-1]
        advanced = False
        for w in it:
            if w not in cs:
                continue
            if w in onp:
                return path[path.index(w):] + [w]
            onp.add(w)
            path.append(w)
            stack.append((w, iter(sorted(g[w]))))
            advanced = True
            break
        if not advanced:
            stack.pop()
            onp.discard(path.pop())
    return None


def plan_demotions(claims):
    """Return (moves, sccs_before) where moves is a list of dicts
    {src, dst, rule, cycle}."""
    ids, g, ef = load_graph(claims)
    sccs_before = cyclic_sccs(ids, g)
    moves = []
    moved = set()
    # Rule 1: mutual pairs.
    for a in sorted(g):
        for b in sorted(g[a]):
            if a < b and a in g[b]:
                for (s, t) in ((a, b), (b, a)):
                    if (s, t) in ef:
                        continue
                    moved.add((s, t))
                    moves.append({"src": s, "dst": t, "rule": "mutual-pair",
                                  "cycle": [s, t, s]})
    g2 = collections.defaultdict(set)
    for a in g:
        for b in g[a]:
            if (a, b) not in moved:
                g2[a].add(b)
    # Rule 2: residual feedback arc set.
    while True:
        comps = cyclic_sccs(ids, g2)
        if not comps:
            break
        for comp in comps:
            cyc = find_one_cycle(g2, comp)
            if not cyc:
                continue
            edges = [(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)]
            cand = [e for e in edges if e not in ef]
            if not cand:
                raise SystemExit(f"cycle made entirely of emergent_from edges: {cyc}")

            def cost(e):
                s, t = e
                downhill = 1 if _level(t) > _level(s) else 0
                return (downhill, len(g2[s]), e)

            s, t = max(cand, key=cost)
            moved.add((s, t))
            g2[s].discard(t)
            moves.append({"src": s, "dst": t, "rule": "cycle-break",
                          "cycle": cyc})
    return moves, sccs_before


# ----------------------------------------------------------------------- text edit
_ITEM_RE = re.compile(r'^(?P<ind>\s+)- (?P<q>["\']?)(?P<id>[A-Za-z0-9_.\-]+)(?P=q)\s*(?P<c>#.*)?$')
_FLOW_RE = re.compile(r'^(?P<key>  (depends_on|coupled_with)): \[(?P<body>[^\]]*)\]\s*(?P<c>#.*)?$')
_BLOCK_RE = re.compile(r'^  (?P<key>depends_on|coupled_with):\s*(?P<c>#.*)?$')


def _claim_blocks(lines):
    """Yield (claim_id, start, end) line ranges (end exclusive)."""
    starts = [i for i, ln in enumerate(lines) if ln.startswith("- id: ")]
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(lines)
        cid = lines[s][len("- id: "):].strip().strip('"').strip("'")
        yield cid, s, e


def _find_list(lines, s, e, key):
    """Locate list `key` in claim block. Returns (kind, line_idx, items) where
    kind in {flow, block, none}; items = list of (line_idx or None, id, comment)."""
    for i in range(s, e):
        ln = lines[i]
        m = _FLOW_RE.match(ln)
        if m and m.group("key").strip() == key:
            body = m.group("body").strip()
            items = []
            if body:
                for part in body.split(","):
                    items.append((None, part.strip().strip('"').strip("'"), ""))
            return "flow", i, items
        m = _BLOCK_RE.match(ln)
        if m and m.group("key") == key:
            items = []
            j = i + 1
            while j < e:
                mi = _ITEM_RE.match(lines[j])
                if not mi:
                    break
                items.append((j, mi.group("id"), (mi.group("c") or "").strip()))
                j += 1
            return "block", i, items
    return "none", None, []


def apply_moves(text, moves):
    lines = text.split("\n")
    out_by_src = collections.defaultdict(list)   # src -> [(dst, rule)]
    add_coupled = collections.defaultdict(list)  # cid -> [(other, note)]
    for mv in moves:
        out_by_src[mv["src"]].append((mv["dst"], mv["rule"]))
        note_s = ("moved from depends_on %s, %s: mutual pair" % (DATE, RULE_ID)
                  if mv["rule"] == "mutual-pair" else
                  "moved from depends_on %s, %s: cycle-break; re-judge (cycle %s)"
                  % (DATE, RULE_ID, " -> ".join(mv["cycle"])))
        add_coupled[mv["src"]].append((mv["dst"], note_s))
        if mv["rule"] == "cycle-break":
            # keep coupled_with symmetric
            add_coupled[mv["dst"]].append((mv["src"], "reverse of %s -> %s coupling, %s %s"
                                           % (mv["src"], mv["dst"], DATE, RULE_ID)))

    # Process claims from the bottom up so line indices stay valid.
    blocks = list(_claim_blocks(lines))
    for cid, s, e in reversed(blocks):
        removals = {d for d, _ in out_by_src.get(cid, [])}
        additions = add_coupled.get(cid, [])
        if not removals and not additions:
            continue
        carried = {}  # dst -> comment carried from the removed depends_on item
        kind, li, items = _find_list(lines, s, e, "depends_on")
        if removals:
            if kind == "none":
                raise SystemExit(f"{cid}: depends_on not found for removals {removals}")
            present = {it[1] for it in items}
            missing = removals - present
            if missing:
                raise SystemExit(f"{cid}: depends_on lacks {missing}")
            if kind == "flow":
                m = _FLOW_RE.match(lines[li])
                keep = [it[1] for it in items if it[1] not in removals]
                lines[li] = "%s: [%s]%s" % (m.group("key"), ", ".join(keep),
                                            ("   " + m.group("c")) if m.group("c") else "")
            else:
                for (j, iid, cmt) in reversed(items):
                    if iid in removals:
                        carried[iid] = cmt
                        del lines[j]
                items = [it for it in items if it[1] not in removals]
        if additions:
            # dedupe additions, prefer carried comment text
            seen = set()
            add_lines = []
            for other, note in additions:
                if other in seen:
                    continue
                seen.add(other)
                cmt = carried.get(other, "")
                if cmt:
                    cmt = cmt.rstrip() + "  [" + note + "]"
                else:
                    cmt = "# " + note
                add_lines.append((other, cmt))
            ckind, cli, citems = _find_list(lines, s, e, "coupled_with")
            existing = {it[1] for it in citems}
            add_lines = [(o, c) for (o, c) in add_lines if o not in existing]
            if ckind == "block":
                ind = "    "
                if citems:
                    ind = _ITEM_RE.match(lines[citems[0][0]]).group("ind")
                insert_at = (citems[-1][0] + 1) if citems else cli + 1
                for o, c in add_lines:
                    lines.insert(insert_at, f"{ind}- {o}  {c}")
                    insert_at += 1
            elif ckind == "flow":
                raise SystemExit(f"{cid}: flow-style coupled_with not supported; convert to block")
            else:
                # Insert a new block right after the depends_on list (or after id line).
                dkind, dli, ditems = _find_list(lines, s, e, "depends_on")
                if dkind == "block":
                    ind = _ITEM_RE.match(lines[ditems[0][0]]).group("ind") if ditems else "    "
                    insert_at = (ditems[-1][0] + 1) if ditems else dli + 1
                elif dkind == "flow":
                    ind = "    "
                    insert_at = dli + 1
                else:
                    ind = "    "
                    insert_at = s + 1
                new = ["  coupled_with:"] + [f"{ind}- {o}  {c}" for o, c in add_lines]
                lines[insert_at:insert_at] = new
    return "\n".join(lines)


# -------------------------------------------------------------------- verification
def verify(before_claims, after_claims, moves):
    b = {c["id"]: c for c in before_claims}
    a = {c["id"]: c for c in after_claims}
    assert list(b) == list(a), "claim id order changed"
    exp_removed = collections.defaultdict(set)
    exp_coupled = collections.defaultdict(set)
    for mv in moves:
        exp_removed[mv["src"]].add(mv["dst"])
        exp_coupled[mv["src"]].add(mv["dst"])
        if mv["rule"] == "cycle-break":
            exp_coupled[mv["dst"]].add(mv["src"])
    for cid in b:
        for k in set(b[cid]) | set(a[cid]):
            if k in ("depends_on", "coupled_with"):
                continue
            assert b[cid].get(k) == a[cid].get(k), f"{cid}: field {k} changed"
        bd = [x for x in (b[cid].get("depends_on") or [])]
        ad = [x for x in (a[cid].get("depends_on") or [])]
        assert ad == [x for x in bd if x not in exp_removed[cid]], f"{cid}: depends_on mismatch"
        bc = set(b[cid].get("coupled_with") or [])
        ac = set(a[cid].get("coupled_with") or [])
        assert ac == bc | exp_coupled[cid], f"{cid}: coupled_with mismatch {ac} vs {bc | exp_coupled[cid]}"
    ids, g, _ = load_graph(after_claims)
    assert not cyclic_sccs(ids, g), "depends_on still cyclic after split"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--audit-json", type=Path)
    args = ap.parse_args()
    text = CLAIMS_YAML.read_text(encoding="utf-8")
    claims = yaml.safe_load(text)
    moves, sccs_before = plan_demotions(claims)
    n_edges = sum(len(c.get("depends_on") or []) for c in claims)
    print(f"claims={len(claims)} depends_on_edges={n_edges} cyclic_sccs={len(sccs_before)} "
          f"claims_in_cycles={sum(map(len, sccs_before))}")
    print(f"planned moves: {len(moves)} "
          f"(mutual-pair={sum(m['rule']=='mutual-pair' for m in moves)}, "
          f"cycle-break={sum(m['rule']=='cycle-break' for m in moves)})")
    if not moves:
        print("depends_on is already acyclic -- nothing to do")
        return 0
    if args.dry_run or not args.apply:
        for m in moves:
            print(f"  {m['rule']:12s} {m['src']} -> {m['dst']}")
        return 0
    new_text = apply_moves(text, moves)
    after = yaml.safe_load(new_text)
    verify(claims, after, moves)
    CLAIMS_YAML.write_text(new_text, encoding="utf-8")
    print(f"wrote {CLAIMS_YAML.relative_to(ROOT)}")
    if args.audit_json:
        payload = {
            "rule": RULE_ID, "date": DATE,
            "before": {"claims": len(claims), "depends_on_edges": n_edges,
                       "cyclic_sccs": len(sccs_before),
                       "claims_in_cycles": sum(map(len, sccs_before)),
                       "scc_sizes": sorted((len(s) for s in sccs_before), reverse=True)},
            "after": {"depends_on_edges": n_edges - len(moves), "cyclic_sccs": 0},
            "moves": moves,
        }
        args.audit_json.parent.mkdir(parents=True, exist_ok=True)
        args.audit_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.audit_json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
