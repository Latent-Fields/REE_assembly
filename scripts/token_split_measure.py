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

BASELINE DOUBLE-COUNT (do not count BASELINE_ATTACHMENT_TYPES as conversation)
-------------------------------------------------------------------------------
The METHOD above assumes B is "never stored in the transcript". Since 2026-09-02 that is
false: Claude Code writes the context baseline INTO the transcript as attachments --
`instructions` (the loaded CLAUDE.md + MEMORY.md, ~154k chars, first seen
2026-09-02T18:00Z) and `prompt_snapshot` (~93k chars, first seen 2026-09-04T03:59Z).
Counted as conversation chars they put B into C_i at turn 0, so B is counted twice, the
OLS intercept goes negative and the `baseline <= 0` guard rejects the session. As landed,
`--report --since 2026-09-08` fitted 18/166 sessions (R^2 median 0.79), and those 18
printed an INVERTED fixed/injection split, with B shifted into the injection bucket.
With the exclusion: 157/166 fitted, R^2 median 0.998. A new baseline-restating
attachment type will show up the same way: "sessions fitted" collapses and intercepts go
negative. Record: evidence/planning/context_budget_restructure_plan.md section 7.1.

The negative control is fit-INDEPENDENT for the same reason. It once inspected only
fitted sessions, so when the fit collapsed it printed a vacuous 0/18 that read as a pass.

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

# Attachment types that restate the fixed baseline B rather than add conversation. Read
# "BASELINE DOUBLE-COUNT" in the module docstring before adding to or removing from this.
BASELINE_ATTACHMENT_TYPES = frozenset((
    "instructions", "prompt_snapshot", "session_context", "environment", "model", "date",
    "deferred_tools_record",
))


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
        a = rec.get("attachment") or {}
        if a.get("type") not in BASELINE_ATTACHMENT_TYPES:   # already inside B
            out.append(("attachment", len(json.dumps(a))))
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
    cache_read = cache_create = fresh_input = 0
    turn_read_share = []   # per-turn cache_read / billed input, in turn order
    out_tokens = 0
    entrypoint = None
    started = None
    nested = []          # (displayPath, chars) injections
    substrate_reads = 0  # negative control: reads of the split-out per-feature files

    # READ-CHANNEL COUNT (chip-20260914-token-split-read-channel-count). A CLAUDE.md
    # loads into the session's readFileState -- and so gets NO nested_memory
    # attachment -- once a successful Read tool call has put it there (see
    # evidence/planning/reev3_nested_memory_trigger_drop_20260914.md). Counting
    # nested_memory alone therefore undercounts "loaded": a session that Reads
    # ree-v3/CLAUDE.md (small enough to Read since the WI-1 split) shows 0
    # nested_memory injections even though the instructions loaded. Pair each
    # Read tool_use with its tool_result by tool_use_id so only a SUCCESSFUL
    # (non-is_error) Read counts. isSidechain records (subagent transcripts
    # embedded inline) are skipped -- a subagent's own Read is not this session's
    # main-thread context loading.
    pending_claude_reads = {}   # tool_use_id -> real repo-relative path
    read_via_tool = set()       # real paths successfully Read this session

    for rec in recs:
        if started is None and rec.get("timestamp"):
            started = rec["timestamp"]
        if entrypoint is None and rec.get("entrypoint"):
            entrypoint = rec["entrypoint"]
        is_sidechain = bool(rec.get("isSidechain"))
        a = rec.get("attachment") or {}
        if a.get("type") == "nested_memory":
            # Key by the REAL path, never displayPath: displayPath is relative to the
            # session's cwd, so a session rooted in ree-v3 reports `ree-v3/CLAUDE.md`
            # as plain "CLAUDE.md" -- which silently averages it together with
            # REE_assembly/CLAUDE.md and produced a nonsense ~574 KB mean for a
            # 133 KB file on 2026-09-07.
            real = a.get("path") or a.get("displayPath") or "?"
            try:
                real = os.path.relpath(real, os.path.expanduser("~/REE_Working"))
            except Exception:
                pass
            nested.append((real, len(json.dumps(a))))
        if rec.get("type") == "assistant":
            m = rec.get("message", {})
            u = m.get("usage") or {}
            ui = u.get("input_tokens") or 0
            ur = u.get("cache_read_input_tokens") or 0
            uc = u.get("cache_creation_input_tokens") or 0
            tot = ui + ur + uc
            if tot > 0:
                xs.append(sum(running.values()))
                ys.append(tot)
                snaps.append(dict(running))
                out_tokens += u.get("output_tokens") or 0
                fresh_input += ui
                cache_read += ur
                cache_create += uc
                turn_read_share.append(ur / float(tot))
            for b in m.get("content", []) or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    if "docs/substrate/" in json.dumps(b.get("input") or {}):
                        substrate_reads += 1
                    if not is_sidechain and b.get("name") == "Read":
                        fp = (b.get("input") or {}).get("file_path") or ""
                        if fp.endswith("CLAUDE.md"):
                            real = fp
                            try:
                                real = os.path.relpath(real, os.path.expanduser("~/REE_Working"))
                            except Exception:
                                pass
                            tuid = b.get("id")
                            if tuid:
                                pending_claude_reads[tuid] = real
        elif rec.get("type") == "user" and not is_sidechain and pending_claude_reads:
            content = rec.get("message", {}).get("content")
            for b in (content if isinstance(content, list) else [content]):
                if isinstance(b, dict) and b.get("type") == "tool_result":
                    tuid = b.get("tool_use_id")
                    real = pending_claude_reads.pop(tuid, None)
                    if real is not None and not b.get("is_error"):
                        read_via_tool.add(real)
        for cat, ch in categorize(rec):
            running[cat] += ch

    # A session the fit rejects still returns its fit-free observations, so the negative
    # control can cover every session (see "BASELINE DOUBLE-COUNT" in the docstring).
    # `nested` and `read_via_tool` are included here too (not just in the fitted return
    # below) so the Read-channel report can cover every in-window session, fitted or
    # not -- exactly the fit-independent scope the negative control already uses, and
    # for the same reason: a short/headless session (e.g. a scheduled task) is likelier
    # to fail the `len(xs) < 3` or baseline<=0 fit gate, and that is precisely the
    # population this chip is about (nightly-documentation-update sessions).
    unfitted = {"fitted": False, "path": path, "entrypoint": entrypoint, "started": started,
                "substrate_reads": substrate_reads, "nested": nested,
                "read_via_tool": sorted(read_via_tool)}
    if len(xs) < 3:
        return unfitted
    fit = lstsq2(xs, ys)
    if not fit:
        return unfitted
    baseline, inv_r = fit
    if inv_r <= 0 or baseline <= 0 or not (1.5 < 1.0 / inv_r < 12):
        return unfitted

    pred = [baseline + inv_r * x for x in xs]
    ybar = sum(ys) / len(ys)
    sst = sum((y - ybar) ** 2 for y in ys)
    sse = sum((ys[i] - pred[i]) ** 2 for i in range(len(ys)))
    return {
        "fitted": True, "path": path, "entrypoint": entrypoint, "started": started,
        "n_turns": len(xs), "baseline_tokens": baseline,
        "chars_per_token": 1.0 / inv_r,
        "r2": (1 - sse / sst) if sst > 0 else None,
        "med_residual": st.median([abs(ys[i] - pred[i]) / ys[i] for i in range(len(ys))]),
        "billed_baseline": baseline * len(xs),
        "billed_cat": {c: sum(s[c] for s in snaps) * inv_r for c in CATS},
        "billed_total_measured": sum(ys),
        "output_tokens": out_tokens,
        "nested": nested, "substrate_reads": substrate_reads,
        "read_via_tool": sorted(read_via_tool),
        # --- prompt-cache behaviour (WI-I). Realized cache performance, measured
        # from the same usage blocks the OLS fit above already consumes. Independent
        # of the fit: these are raw API counters, not estimates.
        "cache_read_tokens": cache_read,
        "cache_creation_tokens": cache_create,
        "fresh_input_tokens": fresh_input,
        "cache_read_share": cache_read / float(cache_read + cache_create + fresh_input)
                            if (cache_read + cache_create + fresh_input) > 0 else None,
        "cache_creation_share": cache_create / float(cache_read + cache_create + fresh_input)
                                if (cache_read + cache_create + fresh_input) > 0 else None,
        # A turn with cache_read == 0 re-paid for the whole prefix. The FIRST turn of a
        # session has nothing to hit, so it is never a miss.
        "cache_misses": sum(1 for s in turn_read_share[1:] if s <= 0.0),
        "cache_miss_turns_considered": max(0, len(turn_read_share) - 1),
        "med_turn_cache_read_share": st.median(turn_read_share) if turn_read_share else None,
        "turn_cache_read_share": turn_read_share,
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

    results = []     # fitted sessions: everything the OLS split is computed over
    observed = []    # EVERY in-window session, fitted or not: fit-free controls use this
    for p in files:
        try:
            r = analyze(p)
        except Exception:
            continue
        if not r:
            continue
        if args.since and (r["started"] or "") < args.since:
            continue
        observed.append(r)
        if r["fitted"]:
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

    # --- PROMPT CACHE (WI-I) -------------------------------------------------
    # Added 2026-09-14. Every line above this block is unchanged on purpose: the
    # 2026-09-14T08:00Z re-measure ran against the pre-WI-I script and the two
    # outputs must stay diffable. This section only ADDS.
    c_read = sum(r["cache_read_tokens"] for r in results)
    c_make = sum(r["cache_creation_tokens"] for r in results)
    c_fresh = sum(r["fresh_input_tokens"] for r in results)
    c_billed = c_read + c_make + c_fresh
    pooled = [s for r in results for s in r["turn_cache_read_share"]]
    miss = sum(r["cache_misses"] for r in results)
    miss_of = sum(r["cache_miss_turns_considered"] for r in results)
    sess_share = [r["cache_read_share"] for r in results if r["cache_read_share"] is not None]
    sess_med = [r["med_turn_cache_read_share"] for r in results
                if r["med_turn_cache_read_share"] is not None]

    print("\n--- PROMPT CACHE (realized) ---")
    print("  Complementary to the split above: that measures WHAT is in the input,")
    print("  this measures how much of it was served from cache rather than re-billed")
    print("  at full rate. Denominator is the same billed input total.")
    if c_billed <= 0:
        print("  (no usage data)")
    else:
        print(f"  cache READ     {100*c_read/c_billed:6.2f}%  {c_read:>14,.0f}")
        print(f"  cache CREATION {100*c_make/c_billed:6.2f}%  {c_make:>14,.0f}")
        print(f"  uncached input {100*c_fresh/c_billed:6.2f}%  {c_fresh:>14,.0f}")
        print(f"  per-turn cache-read share: median {100*st.median(pooled):.2f}%"
              f"  (pooled over {len(pooled):,} turns)")
        print(f"  per-SESSION cache-read share: median {100*st.median(sess_share):.2f}%"
              f"  min {100*min(sess_share):.2f}%  max {100*max(sess_share):.2f}%")
        print(f"  per-session median-of-medians: {100*st.median(sess_med):.2f}%")
        print(f"  MISSES (cache_read == 0 on a non-first turn): {miss:,} of {miss_of:,} turns"
              f"  ({(100.0*miss/miss_of) if miss_of else 0:.2f}%)")
        nmiss = [r for r in results if r["cache_misses"] > 0]
        print(f"  sessions with >=1 miss: {len(nmiss)}/{len(results)}"
              + (f"  worst {max(r['cache_misses'] for r in nmiss)} misses" if nmiss else ""))

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

    print("\n--- Read-channel CLAUDE.md loads (chip-20260914-token-split-read-channel-count) ---")
    print("  A CLAUDE.md loads into readFileState -- and so gets NO nested_memory")
    print("  attachment -- once a successful Read tool call has put it there. The")
    print("  nested_memory count above therefore undercounts 'loaded'; this adds the")
    print("  Read channel and the union. Scope: ALL in-window sessions (fitted or not,")
    print("  same fit-independent scope as the negative control below), since a short")
    print("  headless session is likelier to fail the OLS fit gate.")
    nested_paths = collections.defaultdict(set)
    read_paths = collections.defaultdict(set)
    for r in observed:
        for dp, _ in r["nested"]:
            nested_paths[dp].add(r["path"])
        for dp in r["read_via_tool"]:
            read_paths[dp].add(r["path"])
    all_claude_paths = set(nested_paths) | set(read_paths)
    if all_claude_paths:
        for dp in sorted(all_claude_paths):
            n_nested = len(nested_paths[dp])
            n_read = len(read_paths[dp])
            n_union = len(nested_paths[dp] | read_paths[dp])
            print(f"  {dp:34s} nested_memory={n_nested:>3}  read={n_read:>3}  "
                  f"union={n_union:>3}  (of {len(observed)} in-window sessions)")
    else:
        print("  (none observed)")

    print("\n--- NEGATIVE CONTROL: read-back of split-out per-feature files ---")
    print("  The WI-1 saving holds only while sessions do not read back many")
    print("  ree-v3/docs/substrate/ files. Watch this number.")
    # Over ALL in-window sessions, not only fitted ones -- scoped to `results` it printed
    # a vacuous 0/18 when the baseline double-count collapsed the fit (docstring).
    reads = [r["substrate_reads"] for r in observed]
    withany = [n for n in reads if n > 0]
    print(f"  sessions referencing docs/substrate/: {len(withany)}/{len(observed)}"
          f"  (all in-window sessions, fitted or not)")
    if reads:
        print(f"  reads per session: median {st.median(reads):.0f}  mean {sum(reads)/len(reads):.1f}  max {max(reads)}")
    print("\n  Compare against evidence/planning/token_split_measurement_20260907.md")
    print("  and section 7 of context_budget_restructure_plan.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
