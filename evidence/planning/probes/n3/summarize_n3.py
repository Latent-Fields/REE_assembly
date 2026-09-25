"""Summarise N3 proper per the pre-registration (n3_e3_aggregation_probe_20260925.md). ASCII only."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _f(x):
    return "NA" if x is None else "%.2f" % x


SEEDS = [531, 532, 533, 534, 535]
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FIDW", "FULL"]
SIMPLE = ["DISC_0.5", "DISC_0.8", "FIDW", "FULL"]
R = {s: json.load(open(HERE / "results" / ("N3_s%d.json" % s))) for s in SEEDS
     if (HERE / "results" / ("N3_s%d.json" % s)).exists()}
out = []
P = out.append
P("N3 proper summary; seeds present: %s" % sorted(R))
if len(R) < 5:
    P("INCOMPLETE -- not all registered seeds present")

# preconditions
P("\n-- preconditions --")
P("seed | REAL disc4/k | REAL disc5 | SHUF disc4/disc5 | BLIND disc4 fair5 | BLINDR disc4 | INIT disc4 | REAL t1/t30/true | bar | twin | canaries")
bar_miss, twin_ok_n, canary_fail = [], 0, []
for s, r in sorted(R.items()):
    h = r["heads"]
    e = lambda n, k: h[n]["eval4"][k]
    t = lambda n, k: h[n]["tew"][k]
    val = r["probe"]["validation"]
    can = {"validation": val.get("verdict") == "PASS", "decomp": r["decomp_canary_full_eq_Lmax_max"] <= 1e-5,
           "batch_rel": r["batch_canary_rel_max"] <= 1e-4, "e3_struct": r["canary_e3_structure"],
           "act_disc": r["canary_action_discrimination"], "n_states": r["probe"]["n_states"] >= 20}
    if not all(can.values()):
        canary_fail.append((s, [k for k, v in can.items() if not v]))
    if not r["l2r_bar_real"]:
        bar_miss.append(s)
    twin_ok_n += int(r["twin_at_chance"])
    P("%d | %.3f/%d | %.3f | %.3f/%.3f | %.3f %.3f | %.3f | %.3f | %.2f/%.2f/%.2f | %s | %s | %s" % (
        s, e("REAL", "disc4_h1"), e("REAL", "k"), t("REAL", "disc5_h1_tew"), e("SHUF", "disc4_h1"), t("SHUF", "disc5_h1_tew"),
        e("BLIND", "disc4_h1"), t("BLIND", "disc5_h1_tew_tiefair"), e("BLINDR", "disc4_h1"), e("INIT", "disc4_h1"),
        t("REAL", "rollout_norm_t1_p50"), t("REAL", "rollout_norm_t30_p50"), t("REAL", "true_norm_p50"),
        r["l2r_bar_real"], r["twin_at_chance"], "ok" if all(can.values()) else "FAIL %s" % [k for k, v in can.items() if not v]))
    P("     n_states %d  maxdiff %s  decomp %.2g  batch_rel %.2g  BLIND w unchanged %s  guards R/S/B %s / %s / %s" % (
        r["probe"]["n_states"], val.get("max_abs_diff"), r["decomp_canary_full_eq_Lmax_max"], r["batch_canary_rel_max"],
        r["blind_action_weight_unchanged_from_init"], h["REAL"]["member"]["guard"], h["SHUF"]["member"]["guard"], h["BLIND"]["member"]["guard"]))
    P("     post actions R %s S %s B %s ; t30 SHUF %.2f BLIND %.2f BLINDR %.2f INIT %.1f" % (
        h["REAL"]["member"]["post_action_counts"], h["SHUF"]["member"]["post_action_counts"], h["BLIND"]["member"]["post_action_counts"],
        t("SHUF", "rollout_norm_t30_p50"), t("BLIND", "rollout_norm_t30_p50"), t("BLINDR", "rollout_norm_t30_p50"), t("INIT", "rollout_norm_t30_p50")))
bar_fail = len(bar_miss) >= 2
twin_fail = twin_ok_n < 4
P("L2R bar misses: %s -> %s ; twin at chance %d/5 -> %s ; canary failures: %s" % (
    bar_miss, "CD" if bar_fail else "ok", twin_ok_n, "CD" if twin_fail else "ok", canary_fail or "none"))

# gates
P("\n-- gates per aggregation (REAL / SHUF, diff) --")
res = {}
for ag in AGGS:
    a_pass, b_pass, c_pass, c_cd, lines = 0, 0, 0, 0, []
    for s, r in sorted(R.items()):
        mr, ms = r["metrics"]["REAL"][ag], r["metrics"]["SHUF"][ag]
        # (a)
        da = None
        if mr["rho_scaf"] is not None and ms["rho_scaf"] is not None and mr["rho_scaf_n"] >= 10:
            da = mr["rho_scaf"] - ms["rho_scaf"]
        pa = da is not None and da > 0.15
        a_pass += pa
        # (b)
        db = None if mr["pick_in_Qbest"] is None or ms["pick_in_Qbest"] is None else mr["pick_in_Qbest"] - ms["pick_in_Qbest"]
        pb = db is not None and db > 0.10 and mr["n_informative_q"] >= 10
        b_pass += pb
        # (c) reference rule
        if mr["ref_BLIND_degenerate_frac"] < 0.5:
            refn = "BLIND"
        elif mr["ref_BLINDR_degenerate_frac"] < 0.5:
            refn = "BLINDR"
        else:
            refn = None
        if refn is None:
            c_cd += 1; pc = False; dc = None
        else:
            dc = mr["flip_vs_" + refn] - ms["flip_vs_" + refn]
            pc = dc > 0.15
        c_pass += pc
        lines.append("  s%d a %s/%s d=%s %s | b %s/%s d=%s | c[%s] %s/%s d=%s %s (plain %.2f/%.2f; BLINDdeg %.2f BLINDRdeg %.2f) | vsINIT %.2f/%.2f | toward[%s] %s/%s | n3pre-form rho %s/%s" % (
            s, _f(mr["rho_scaf"]), _f(ms["rho_scaf"]), _f(da), "P" if pa else "-", _f(mr["pick_in_Qbest"]), _f(ms["pick_in_Qbest"]), _f(db),
            refn, _f(mr["flip_vs_" + refn] if refn else None), _f(ms["flip_vs_" + refn] if refn else None), _f(dc), "P" if pc else "-",
            mr["flip_vs_" + (refn or "BLINDR") + "_plain_argmin"], ms["flip_vs_" + (refn or "BLINDR") + "_plain_argmin"],
            mr["ref_BLIND_degenerate_frac"], mr["ref_BLINDR_degenerate_frac"], mr["flip_vs_INIT"], ms["flip_vs_INIT"],
            refn or "BLINDR", _f(mr["toward_better_vs_" + (refn or "BLINDR")]), _f(ms["toward_better_vs_" + (refn or "BLINDR")]),
            _f(mr["rho_scaf_n3pre_form"]), _f(ms["rho_scaf_n3pre_form"])))
    hab = [r["habit_contrast_REAL"][ag]["pick_agree_with_habit"] for r in R.values()]
    res[ag] = {"a": a_pass, "b": b_pass, "c": c_pass, "c_cd": c_cd}
    P("%s: (a) %d/5  (c) %d/5 (CD seeds %d)  (b, report) %d/5  habit-pick agreement %s" % (
        ag, a_pass, c_pass, c_cd, b_pass, ["%.2f" % x for x in hab]))
    for ln in lines:
        P(ln)
fidw_depths = {s: r["fidw_weight_depths"]["REAL"] for s, r in R.items()}
fidw_ok = sum(1 for d in fidw_depths.values() if any(x >= 2 for x in d)) >= 4
P("FIDW REAL weighted depths >= 2 per seed: %s -> SD-081 %s" % ({s: (min(d) if d else None, max(d) if d else None, len(d)) for s, d in fidw_depths.items()}, "compatible" if fidw_ok else "incompatible"))

# verdict
P("\n-- verdict --")
compat = {"DISC_0.5": True, "DISC_0.8": True, "FIDW": fidw_ok, "FULL": True}
c_overall_cd = any(res[ag]["c_cd"] >= 2 for ag in SIMPLE)
if bar_fail or twin_fail or canary_fail:
    P("CANNOT_DETERMINE (preconditions): bar misses %s twin %d/5 canaries %s" % (bar_miss, twin_ok_n, canary_fail))
sel = None
for ag in SIMPLE:
    if res[ag]["a"] >= 4 and res[ag]["c"] >= 4 and compat[ag]:
        sel = ag; break
P("descriptive selection (simplest passing (a)+(c), compatible): %s" % (sel or "NONE_PASS"))
P("(a)-only passers: %s ; (c) CD overall for any simple agg: %s" % ([ag for ag in AGGS if res[ag]["a"] >= 4], c_overall_cd))
if bar_miss:
    P("sensitivity without bar-miss seeds %s: recompute by hand from per-seed lines above" % bar_miss)
txt = "\n".join(out)
print(txt)
open(HERE / "results" / "SUMMARY.txt", "w").write(txt + "\n")
