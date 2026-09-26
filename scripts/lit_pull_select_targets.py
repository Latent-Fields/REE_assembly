#!/usr/bin/env python3
"""Pick the next literature-pull targets from evidence_backlog.v1.json.

Shared selector for the scheduled lit-pull routines (ree-lit-pull-am, -am-b, -pm,
ree-weekend-lit). Before 2026-09-26 each routine carried its own inline copy of the
selector, and all of them walked the backlog in FILE order -- which is roughly claim-id
order -- so the claims the live build actually rests on (e.g. SD-070, MECH-523, at rank
~430 of 450) would not have been reached for months while ARC-118..ARC-149 (mostly V4)
were pulled first.

Tiers, consumed in order and deduped:

  Tier 0  (live front)  uncovered claims referenced by what is being built / run NOW:
                          - experiment_queue.json items (json + their script text)
                          - docs/CURRENT_FRONT.md and the full text of every live-path
                            V3-EXQ script it names
                          - evidence/planning/*.md docs those scripts cite by path
                          - the *_plan.md whose slug the front names in prose
                            (e.g. "coupled-loop repair campaign")
                        Derived, not curated, so it moves with the front.
  Tier 1  literature-primary: evidence_needed includes "literature"
  Tier 1b reasons include missing_literature_evidence / insufficient_literature_grounding
  Tier 2  high-priority in_progress conflict claims (fallback top-up only), excluding
          experimental-only claims already lit-ahead by > LIT_EXP_MARGIN.

Within Tiers 0/1/1b, order is: implementation_phase (v3, unset, v4, v5, v6, later),
then priority, then conflict ratio, then claim id. So the V4+ backlog drains only
after the V3-relevant work -- it is not dropped.

Coverage (a claim is skipped when covered): a name-matched targeted_review_* dir exists,
OR >= COVERAGE_MIN literature record.json entries tag it in claim_ids_tested.

Output: one line per pick,
  <claim_id>\t<backlog_id>\ttier=<t>\tphase=<p>\treason=<r>\tlit_entries=<n>
then a '# ' summary line with the denominators. NONE_AVAILABLE if no picks.
If the live-front sources cannot be read, the summary says FRONT=CANNOT_DETERMINE
(distinct from "front read, nothing uncovered") and selection falls back to Tier 1+.

Run from anywhere:  python3 scripts/lit_pull_select_targets.py [--n 2] [--json]
"""
import argparse
import glob
import json
import os
import re
import sys

ASSEMBLY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REE_V3 = os.path.join(os.path.dirname(ASSEMBLY), "ree-v3")
LITROOT = os.path.join(ASSEMBLY, "evidence", "literature")

COVERAGE_MIN = 3
LIT_EXP_MARGIN = 0.05
LITREASON = {"missing_literature_evidence", "insufficient_literature_grounding"}
PHASE_RANK = {"v3": 0, None: 1, "": 1, "v4": 2, "v5": 3, "v6": 4}
PRIO_RANK = {"high": 0, "medium": 1, "low": 2}
CLAIM_RE = re.compile(r"(?<![A-Za-z0-9-])(?:MECH|ARC|INV|SD|Q|EXT|GOV)-\d+[a-z]?\b")


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def load_phases():
    """claim_id -> implementation_phase, from claims.yaml (best effort)."""
    try:
        import yaml
        claims = yaml.safe_load(_read(os.path.join(ASSEMBLY, "docs", "claims", "claims.yaml")))
        return {c["id"]: c.get("implementation_phase") for c in claims
                if isinstance(c, dict) and "id" in c}
    except Exception as exc:  # phase ordering degrades to "unset" for everything
        print(f"# WARN: claims.yaml phases unavailable ({exc}); phase ordering disabled",
              file=sys.stderr)
        return {}


def lit_coverage_counts():
    counts = {}
    for rec in glob.glob(os.path.join(LITROOT, "*", "entries", "*", "record.json")):
        try:
            r = json.loads(_read(rec))
        except Exception:
            continue
        for cid in (r.get("claim_ids_tested") or []):
            k = str(cid).upper().strip()
            counts[k] = counts.get(k, 0) + 1
    return counts


def live_front_refs():
    """Return (refs: claim_id -> set(source tags), stats dict) or (None, stats) on failure."""
    refs, stats = {}, {"queue_items": 0, "live_scripts": 0, "plan_docs": 0}

    def add(tag, text):
        for m in set(CLAIM_RE.findall(text)):
            refs.setdefault(m, set()).add(tag)

    cited_docs = set()

    def scan_script(tag, path):
        text = _read(path)
        add(tag, text)
        cited_docs.update(re.findall(r"evidence/planning/[A-Za-z0-9_.-]+\.md", text))

    try:
        front = _read(os.path.join(ASSEMBLY, "docs", "CURRENT_FRONT.md"))
        q = json.loads(_read(os.path.join(REE_V3, "experiment_queue.json")))
    except Exception as exc:
        stats["error"] = str(exc)
        return None, stats

    add("front", front)
    for it in (q.get("items") if isinstance(q, dict) else q) or []:
        stats["queue_items"] += 1
        add("queue", json.dumps(it))
        script = it.get("script") or ""
        p = os.path.join(REE_V3, script)
        if script and os.path.isfile(p):
            scan_script("queue", p)
    for exq in set(re.findall(r"V3-EXQ-(\d+[a-z]?)\b", front)):
        for p in glob.glob(os.path.join(REE_V3, "experiments", f"v3_exq_{exq}_*.py")):
            stats["live_scripts"] += 1
            scan_script("live_path", p)
    # Campaign plan named in the front's PROSE ("coupled-loop repair campaign" ->
    # coupled_loop_repair_campaign_plan.md): slug-match plan stems against the front text.
    front_slug = re.sub(r"[^a-z0-9]+", "_", front.lower())
    for p in glob.glob(os.path.join(ASSEMBLY, "evidence", "planning", "*_plan.md")):
        stem = os.path.basename(p)[:-len("_plan.md")]
        if len(stem) > 8 and stem in front_slug:
            cited_docs.add(os.path.relpath(p, ASSEMBLY))
    for rel in sorted(cited_docs):
        p = os.path.join(ASSEMBLY, rel)
        if os.path.isfile(p):
            stats["plan_docs"] += 1
            add("plan_doc", _read(p))
    return refs, stats


def claim_keys(cid):
    c = cid.lower()
    keys = {c.replace("-", "_")}
    m = re.match(r"([a-z]+)-?(\d+)([a-z]?)", c)
    if m:
        pre, num, suf = m.groups()
        for n in {num, num.zfill(3), num.lstrip("0") or "0"}:
            for base in (f"{pre}_{n}", f"{pre}{n}"):
                keys |= {base + suf, base, "connectome_" + base + suf, "connectome_" + base}
    return {k for k in keys if k}


def select(n):
    bk = json.loads(_read(os.path.join(ASSEMBLY, "evidence", "planning", "evidence_backlog.v1.json")))
    items = bk["items"]
    suffixes = [d[len("targeted_review_"):] for d in os.listdir(LITROOT)
                if d.startswith("targeted_review_")]
    counts = lit_coverage_counts()
    phases = load_phases()
    refs, fstats = live_front_refs()

    def has_dir(cid):
        keys = claim_keys(cid)
        return any(s == k or s.startswith(k + "_") for s in suffixes for k in keys)

    def lit_n(it):
        rec = counts.get(str(it["claim_id"]).upper().strip(), 0)
        sig = ((it.get("signals") or {}).get("source_counts") or {}).get("literature", 0) or 0
        return max(rec, sig)

    def reason(it):
        rs = (it.get("reasons") or [""])[0]
        return rs.get("reason") if isinstance(rs, dict) else rs

    def cratio(it):
        return (it.get("signals") or {}).get("conflict_ratio", 0) or 0

    def needs_lit(it):
        return ("literature" in (it.get("evidence_needed") or [])
                or bool(set(it.get("reasons") or []) & LITREASON))

    def lit_widens_conflict(it):
        if set(it.get("evidence_needed") or []) != {"experimental"}:
            return False
        cs = (it.get("signals") or {}).get("confidence_split") or {}
        d = cs.get("delta_lit_minus_exp")
        if d is None:
            lc, ec = cs.get("literature_confidence"), cs.get("experimental_confidence")
            if lc is None or ec is None:
                return False
            d = lc - ec
        return d > LIT_EXP_MARGIN

    def order(it):
        return (PHASE_RANK.get(phases.get(it["claim_id"]), 5),
                PRIO_RANK.get(it.get("priority"), 9), -cratio(it), it["claim_id"])

    uncovered = [it for it in items if not (has_dir(it["claim_id"]) or lit_n(it) >= COVERAGE_MIN)]
    t0 = sorted([it for it in uncovered if refs is not None and it["claim_id"] in refs
                 and needs_lit(it)], key=order)
    seen = {it["claim_id"] for it in t0}
    t1 = sorted([it for it in uncovered if it["claim_id"] not in seen
                 and "literature" in (it.get("evidence_needed") or [])], key=order)
    seen |= {it["claim_id"] for it in t1}
    t1b = sorted([it for it in uncovered if it["claim_id"] not in seen
                  and set(it.get("reasons") or []) & LITREASON], key=order)
    seen |= {it["claim_id"] for it in t1b}
    rank = {"active_conflict": 0, "directional_conflict_alert": 1}
    t2 = sorted([it for it in uncovered if it["claim_id"] not in seen
                 and it.get("priority") == "high" and it.get("status") == "in_progress"
                 and reason(it) in rank and not lit_widens_conflict(it)],
                key=lambda it: (rank[reason(it)], it["claim_id"]))

    picks = []
    for tier, lst in (("0", t0), ("1", t1), ("1b", t1b), ("2", t2)):
        for it in lst:
            if len(picks) >= n:
                break
            picks.append({"claim_id": it["claim_id"], "backlog_id": it.get("backlog_id"),
                          "tier": tier, "phase": phases.get(it["claim_id"]) or "unset",
                          "reason": reason(it), "lit_entries": lit_n(it),
                          "front_sources": sorted(refs.get(it["claim_id"], [])) if refs else []})
    summary = {
        "backlog_items": len(items), "uncovered": len(uncovered),
        "tier0": len(t0), "tier1": len(t1), "tier1b": len(t1b), "tier2": len(t2),
        "front": "CANNOT_DETERMINE" if refs is None else "ok",
        "front_refs": 0 if refs is None else len(refs), "front_sources": fstats,
        "tier0_remaining": [it["claim_id"] for it in t0],
    }
    return picks, summary


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=2, help="number of targets to pick (default 2)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    picks, summary = select(a.n)
    if a.json:
        print(json.dumps({"picks": picks, "summary": summary}, indent=1))
        return
    for p in picks:
        print(f'{p["claim_id"]}\t{p["backlog_id"]}\ttier={p["tier"]}\tphase={p["phase"]}'
              f'\treason={p["reason"]}\tlit_entries={p["lit_entries"]}')
    if not picks:
        print("NONE_AVAILABLE")
    s = summary
    print(f'# backlog={s["backlog_items"]} uncovered={s["uncovered"]} tier0={s["tier0"]} '
          f'tier1={s["tier1"]} tier1b={s["tier1b"]} tier2={s["tier2"]} front={s["front"]} '
          f'front_refs={s["front_refs"]} sources={s["front_sources"]}')
    if s["tier0_remaining"]:
        print("# tier0 (live-front) queue: " + " ".join(s["tier0_remaining"]))


if __name__ == "__main__":
    main()
