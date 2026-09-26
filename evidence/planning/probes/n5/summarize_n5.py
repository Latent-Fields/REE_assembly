"""Summarise N5 registered seeds against the pre-registered verdict (ASCII)."""
import json, sys
from pathlib import Path

R = Path(__file__).resolve().parent / "results"
seeds = [int(x) for x in (sys.argv[1:] or ["721", "722", "723", "724", "725"])]
rows, got = [], []
for s in seeds:
    f = R / ("N5_s%d.json" % s)
    if not f.exists():
        continue
    d = json.load(open(f))
    if len(d.get("cells", {})) < 5:
        continue
    got.append(s)
    C = d["cells"]
    ps = d["pre_shift_orig"]
    print("s%d %s | B0 %.3f pre %.3f/k%d | PRE-SHIFT orig %.3f/k%d bar=%s ret %.2f | on shifted map %.3f/k%d" % (
        s, d["hazard_class"], d["B0"]["disc4_h1"], d["pre"]["disc4_h1"], d["pre"]["k"], ps["disc4_h1"], ps["k"],
        d["pre_shift_bar"], d["pre_shift_retention"] or float("nan"), d["pre_shift_on_shifted_map"]["disc4_h1"],
        d["pre_shift_on_shifted_map"]["k"]))
    for name in ("shift_gated", "shift_clamped", "noshift_gated", "noshift_clamped", "shift_oracle"):
        c = C[name]; k = c["counts"]
        print("   %-16s shiftmap %.3f/k%2d bar=%-5s | orig %.3f/k%2d bar=%-5s ret %5.2f | bouts %2d ev %d firstcoinc %s repl %4d flush %4d | g_mean %.2f | wouldPE %d wouldAC %d | zon ac %+.2f pe %+.2f | p(s_ac>thr) %.2f p(s_pe>thr) %.2f" % (
            name, c["shift_map"]["disc4_h1"], c["shift_map"]["k"], c["bar_shift"], c["orig"]["disc4_h1"], c["orig"]["k"],
            c["bar_orig"], c["retention_orig"] if c["retention_orig"] is not None else float("nan"), k["bouts"],
            k["unfreeze_events"], k["first_coinc_step"], k["replaced"], k["flushed"], c["g_mean"] or 0,
            k["would_coinc_steps"]["pe"], k["would_coinc_steps"]["ac"], c["z_ac_on_mean"], c["z_pe_on_mean"],
            c["p_s_ac_gt_thr"] or 0, c["p_s_pe_gt_thr"] or 0))
    rows.append({
        "seed": s, "pre_bar": d["pre_shift_bar"],
        "shift_half": C["shift_gated"]["bar_shift"] and not C["shift_clamped"]["bar_shift"],
        "clamped_relearn": C["shift_clamped"]["bar_shift"],
        "noshift_half": C["noshift_gated"]["bar_orig"] and (C["noshift_gated"]["retention_orig"] or -1) >= 0.5,
        "oracle_bar": C["shift_oracle"]["bar_shift"],
        "gate_opened_shift": C["shift_gated"]["counts"]["bouts"] > 0,
        "spurious_noshift": C["noshift_gated"]["counts"]["unfreeze_events"],
    })
n = len(rows)
print("\nseeds complete: %s (%d)" % (got, n))
if n:
    f = lambda k: sum(1 for r in rows if r[k])
    print("pre-shift bar %d/%d | clamped re-learns %d/%d | SHIFT half %d/%d | NO-SHIFT half %d/%d | oracle reaches bar %d/%d | gate opened after shift %d/%d | spurious unfreeze events (noshift_gated) %s" % (
        f("pre_bar"), n, f("clamped_relearn"), n, f("shift_half"), n, f("noshift_half"), n, f("oracle_bar"), n,
        f("gate_opened_shift"), n, [r["spurious_noshift"] for r in rows]))
    if n == 5:
        if n - f("pre_bar") >= 2 or f("clamped_relearn") >= 2:
            v = "CANNOT_DETERMINE"
        elif f("shift_half") >= 4 and f("noshift_half") >= 4:
            v = "PASS"
        else:
            v = "FAIL (%s)" % ", ".join(h for h, ok in (("shift half", f("shift_half") >= 4), ("no-shift half", f("noshift_half") >= 4)) if not ok)
        print("VERDICT:", v)
