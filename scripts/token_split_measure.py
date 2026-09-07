#!/usr/bin/env python3
"""Measure billed input-token composition across local Claude Code transcripts.

WHY THIS EXISTS
---------------
It produced `evidence/planning/token_split_measurement_20260907.md`, which decided
against adopting a tool-output compression layer (Headroom) and identified the
oversized `CLAUDE.md` files as the real lever instead. It is kept so the
post-restructure re-measure is a re-run rather than a rebuild -- the original ran
from a session scratchpad, which does not survive.

METHOD
------
Every `assistant` record in a transcript carries the API's own usage, so total input
tokens for turn i are known exactly:

    T_i = input_tokens + cache_read_input_tokens + cache_creation_input_tokens

Context at turn i = a constant baseline B (system prompt + CLAUDE.md + skill/tool
definitions -- never stored in the transcript) plus conversation content accumulated so
far, which IS stored and countable in characters:

    T_i = B + C_i / r          (C_i = cumulative conversation chars, r = chars/token)

Two unknowns, many turns -> ordinary least squares per session. B and r are therefore
CALIBRATED against ground truth, not assumed. Conversation content is then attributed by
category and weighted by how many turns re-read it, because prompt caching still charges
cache_read every turn.

FIT-QUALITY VACUITY TRAP (do not remove the per-turn diagnostic)
---------------------------------------------------------------
Comparing SUMMED fitted vs measured tokens reports ~0% error at every percentile no
matter how bad the fit is: OLS with an intercept forces the sum of residuals to zero by
construction. Only the per-turn R^2 / residual reported by --report is real. The original
measurement nearly shipped on the vacuous check.

MACHINE SCOPE
-------------
Local-only by design: it reads ~/.claude/projects, which exists on the Mac (canonical
DLAPTOP) and not on the hub or cloud workers. Read-only; writes nothing outside --json.

USAGE
    python3 token_split_measure.py --report
    python3 token_split_measure.py --report --since 2026-09-08   # post-restructure only
    python3 token_split_measure.py --report --json out.json
"""
import argparse, collections, glob, json, os, re, statistics as st, sys

CATS = ("tool_result", "assistant_text", "assistant_thinking", "assistant_tool_use",
        "user_prompt", "attachment", "system_other")
LABEL = {
    "tool_result": "tool results (Bash/Read/Grep/MCP output)",
    "assistant_tool_use": "assistant tool CALLS (params)",
    "assistant_text": "assistant prose",
    "assistant_thinking": "assistant thinking",
    "user_prompt": "user prompts",
    "attachment": "harness injections (nested memory, listings, hooks)",
    "system_other": "system-reminders",
}


def blk_chars(b):
    if isinstance(b, str):
        return len(b)
    if not isinstance(b, dict):
        return len(json.dumps(b))
    t = b.get("type")
    if t == "text":
        return len(b.get("text") or "")
    if t == "thinking":
        return len(b.get("thinking") or "")
    if t == "tool_use":
        return len(json.dumps(b.get("input") or {})) + len(b.get("name") or "")
    if t == "tool_result":
        c = b.get("content")
        if isinstance(c, str):
            return len(c)
        if isinstance(c, list):
            return sum(blk_chars(x) for x in c)
        return len(json.dumps(c or ""))
    return len(json.dumps(b))


def categorize(rec):
    out = []
    t = rec.get("type")
    if t == "assistant":
        for b in rec.get("message", {}).get("content", []) or []:
            bt = b.get("type") if isinstance(b, dict) else None
            out.append(({"text": "assistant_text", "thinking": "assistant_thinking",
                         "tool_use": "assistant_tool_use"}.get(bt, "assistant_text"),
                        blk_chars(b)))
    elif t == "user":
        content = rec.get("message", {}).get("content")
        for b in (content if isinstance(content, list) else [content]):
            if b is None:
                continue
            bt = b.get("type") if isinstance(b, dict) else "text"
            if bt == "tool_result":
                out.append(("tool_result", blk_chars(b)))
            else:
                raw = b if isinstance(b, str) else json.dumps(b)
                out.append(("system_other" if "<system-reminder>" in raw else "user_prompt",
                            blk_chars(b)))
    elif t == "attachment":
        out.append(("attachment", len(json.dumps(rec.get("attachment") or {}))))
    return out


def lstsq2(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx <= 0:
        return None
    return my - (sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) / sxx) * mx, \
           sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) / sxx


def analyze(path):
    recs = []
    for line in open(path, errors="replace"):
        line = line.strip()
        if line:
            try:
                recs.append(json.loads(line))
            except Exception:
                pass
    if not recs:
        return None
    running = {c: 0 for c in CATS}
    xs, ys, snaps = [], [], []
    out_tokens = 0
    entrypoint = None
    started = None
    nested = []          # (displayPath, chars) injections
    substrate_reads = 0  # negative control: reads of the split-out per-feature files

    for rec in recs:
        if started is None and rec.get("timestamp"):
            started = rec["timestamp"]
        if entrypoint is None and rec.get("entrypoint"):
            entrypoint = rec["entrypoint"]
        a = rec.get("attachment") or {}
        if a.get("type") == "nested_memory":
            nested.append((a.get("displayPath") or "?", len(json.dumps(a))))
        if rec.get("type") == "assistant":
            m = rec.get("message", {})
            u = m.get("usage") or {}
            tot = ((u.get("input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0)
                   + (u.get("cache_creation_input_tokens") or 0))
            if tot > 0:
                xs.append(sum(running.values()))
                ys.append(tot)
                snaps.append(dict(running))
                out_tokens += u.get("output_tokens") or 0
            for b in m.get("content", []) or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    if "docs/substrate/" in json.dumps(b.get("input") or {}):
                        substrate_reads += 1
        for cat, ch in categorize(rec):
            running[cat] += ch

    if len(xs) < 3:
        return None
    fit = lstsq2(xs, ys)
    if not fit:
        return None
    baseline, inv_r = fit
    if inv_r <= 0 or baseline <= 0 or not (1.5 < 1.0 / inv_r < 12):
        return None

    pred = [baseline + inv_r * x for x in xs]
    ybar = sum(ys) / len(ys)
    sst = sum((y - ybar) ** 2 for y in ys)
    sse = sum((ys[i] - pred[i]) ** 2 for i in range(len(ys)))
    return {
        "path": path, "entrypoint": entrypoint, "started": started,
        "n_turns": len(xs), "baseline_tokens": baseline,
        "chars_per_token": 1.0 / inv_r,
        "r2": (1 - sse / sst) if sst > 0 else None,
        "med_residual": st.median([abs(ys[i] - pred[i]) / ys[i] for i in range(len(ys))]),
        "billed_baseline": baseline * len(xs),
        "billed_cat": {c: sum(s[c] for s in snaps) * inv_r for c in CATS},
        "billed_total_measured": sum(ys),
        "output_tokens": out_tokens,
        "nested": nested, "substrate_reads": substrate_reads,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", help="only sessions whose FIRST turn is on/after this "
                                    "ISO date (e.g. 2026-09-08)")
    ap.add_argument("--days", type=int, default=21, help="file-mtime window (default 21)")
    ap.add_argument("--min-bytes", type=int, default=20480)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", help="write raw per-session results here")
    args = ap.parse_args()

    root = os.path.expanduser("~/.claude/projects")
    if not os.path.isdir(root):
        print(f"ERROR: {root} not found -- this script is Mac-local (see module docstring).",
              file=sys.stderr)
        return 2
    cutoff = __import__("time").time() - args.days * 86400
    files = [p for p in glob.glob(os.path.join(root, "*REE-Working*", "*.jsonl"))
             if os.path.getmtime(p) >= cutoff and os.path.getsize(p) >= args.min_bytes]

    results = []
    for p in files:
        try:
            r = analyze(p)
        except Exception:
            continue
        if not r:
            continue
        if args.since and (r["started"] or "") < args.since:
            continue
        results.append(r)

    if args.json:
        json.dump(results, open(args.json, "w"))
    if not args.report:
        print(f"{len(results)} sessions fitted (of {len(files)} candidates)")
        return 0
    if not results:
        print("No sessions matched -- widen --days or relax --since.")
        return 1

    base = sum(r["billed_baseline"] for r in results)
    cat = {c: sum(r["billed_cat"][c] for r in results) for c in CATS}
    grand = base + sum(cat.values())
    r2s = [r["r2"] for r in results if r["r2"] is not None]

    print("=" * 72)
    print("TOKEN-SPLIT MEASUREMENT")
    print("=" * 72)
    print(f"sessions {len(results)} (of {len(files)} candidates)"
          + (f", first turn >= {args.since}" if args.since else ""))
    print(f"assistant turns {sum(r['n_turns'] for r in results):,}")
    print(f"billed input tokens (API ground truth) {sum(r['billed_total_measured'] for r in results):,.0f}")
    print("\nFIT QUALITY -- per-turn, NOT summed (see docstring):")
    print(f"  R^2 median {st.median(r2s):.4f}   p10 {sorted(r2s)[int(.1*len(r2s))]:.4f}")
    print(f"  per-turn |residual|/actual median {100*st.median([r['med_residual'] for r in results]):.1f}%")
    print(f"\nmedian fixed baseline/turn {st.median([r['baseline_tokens'] for r in results]):,.0f} tok")
    print(f"median turns/session       {st.median([r['n_turns'] for r in results]):.0f}")

    print("\n--- share of billed INPUT tokens ---")
    items = [("FIXED PROMPT (sys+CLAUDE.md+skills+tool defs)", base)] + \
            [(LABEL[c], cat[c]) for c in CATS]
    for n, v in sorted(items, key=lambda x: -x[1]):
        if v > 0:
            print(f"  {n:48s} {100*v/grand:6.2f}%  {v:>14,.0f}")

    print("\n--- nested_memory injections (the WI-1 target) ---")
    agg = collections.defaultdict(list)
    for r in results:
        for dp, n in r["nested"]:
            agg[dp].append(n)
    if agg:
        for dp, ns in sorted(agg.items(), key=lambda x: -sum(x[1])):
            print(f"  {dp:34s} n={len(ns):>3}  mean {sum(ns)//len(ns):>10,} chars "
                  f"(~{sum(ns)//len(ns)//4:>8,} tok)")
    else:
        print("  (none observed)")

    print("\n--- NEGATIVE CONTROL: read-back of split-out per-feature files ---")
    print("  The WI-1 saving holds only while sessions do not read back many")
    print("  ree-v3/docs/substrate/ files. Watch this number.")
    reads = [r["substrate_reads"] for r in results]
    withany = [n for n in reads if n > 0]
    print(f"  sessions referencing docs/substrate/: {len(withany)}/{len(results)}")
    if reads:
        print(f"  reads per session: median {st.median(reads):.0f}  mean {sum(reads)/len(reads):.1f}  max {max(reads)}")
    print("\n  Compare against evidence/planning/token_split_measurement_20260907.md")
    print("  and section 7 of context_budget_restructure_plan.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
