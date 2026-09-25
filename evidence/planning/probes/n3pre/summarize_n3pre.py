"""Summarize N3-pre results against the pre-registered criteria (bt0925-n3pre). ASCII only."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEEDS = [521, 522, 523, 524, 525]
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FIDW", "FULL"]


def f(x, n=3):
    return "--" if x is None else ("%.*f" % (n, x))


def main():
    rs = {}
    for s in SEEDS:
        p = HERE / "results" / ("N3_s%d.json" % s)
        if p.exists():
            rs[s] = json.load(open(p))
    out = []
    P = out.append
    P("seeds present: %s" % sorted(rs))
    # proxy bar / shuffled chance / canaries
    bar, chance, canary = 0, 0, True
    P("\nHEADS (TE4 disc4_h1 / k ; disc5 TEW ; k30 ; t1/t30/true norm)")
    for s, r in rs.items():
        h = r["heads"]
        for nm in ("INIT", "REAL_pre", "REAL", "SHUF_pre", "SHUF", "B0p"):
            e = h[nm]["eval4"]; tw = h[nm].get("tew")
            P("  s%d %-8s disc4=%s k=%s disc5(te4)=%s %s" % (s, nm, f(e["disc4_h1"]), e["k"], f(e["disc5_h1"]),
                ("disc5(tew)=%s k30=%s norms %s/%s/%s" % (f(tw["disc5_h1_tew"]), tw["k30"], f(tw["rollout_norm_t1_p50"], 2),
                 f(tw["rollout_norm_t30_p50"], 2), f(tw["true_norm_p50"], 2))) if tw else ""))
        b = h["REAL"]["eval4"]["disc4_h1"] >= 0.47 and h["REAL"]["eval4"]["k"] == 10
        c = h["SHUF"]["eval4"]["disc4_h1"] <= 0.32 and h["SHUF"]["tew"]["disc5_h1_tew"] <= 0.27
        pr = r["probe"]
        cn = (pr["validation_maxabs_max"] is not None and pr["validation_maxabs_max"] <= 1e-5 and r["decomp_canary_full_eq_Lmax_max"] <= 1e-5
              and r["batch_canary_max"] <= 1e-5 and pr["n_states"] >= 20)
        bar += b; chance += c; canary &= cn
        P("  s%d proxy_bar=%s shuf_at_chance=%s canaries_ok=%s | states=%d informative=%d val=%s decomp=%s batch=%s | retention_vs_B0p=%s | fidw depths REAL=%s SHUF=%s" % (
            s, b, c, cn, pr["n_states"], pr["n_informative_q"], pr["validation_maxabs_max"], r["decomp_canary_full_eq_Lmax_max"],
            r["batch_canary_max"], f(r["retention_vs_B0p"], 2), r["fidw_weight_depths"]["REAL"], r["fidw_weight_depths"]["SHUF"]))
        for nm in ("REAL", "SHUF"):
            pr_ = h[nm]["post_run"]
            P("  s%d post %s r/100=%s harm/100=%s ben/100=%s H=%s early=%d counts=%s" % (s, nm, f(pr_["reward_per_100"], 2),
              f(pr_["harm_events_per_100"], 1), f(pr_["benefit_events_per_100"], 2), f(pr_["action_entropy"], 2),
              pr_["early_terminations"], pr_["action_counts"]))
    n = len(rs)
    P("\nPROXY BAR %d/%d ; SHUF AT CHANCE %d/%d ; CANARIES %s" % (bar, n, chance, n, canary))
    cd = not (bar >= 4 and chance >= 4 and canary and n == 5)
    P("\nGATES per aggregation (REAL / SHUF / diff) per seed")
    passes = {}
    for ag in AGGS:
        cnt = {"a": 0, "b": 0, "c": 0}
        P("  %s" % ag)
        for s, r in rs.items():
            mr, ms = r["metrics"]["REAL"][ag], r["metrics"]["SHUF"][ag]
            da = (mr["rho_scaf"] - ms["rho_scaf"]) if (mr["rho_scaf"] is not None and ms["rho_scaf"] is not None) else None
            db = (mr["pick_in_Qbest"] - ms["pick_in_Qbest"]) if (mr["pick_in_Qbest"] is not None and ms["pick_in_Qbest"] is not None) else None
            dc = mr["flip_vs_init"] - ms["flip_vs_init"]
            pa = da is not None and da > 0.15 and mr["rho_scaf_n"] >= 10 and ms["rho_scaf_n"] >= 10
            pb = db is not None and db > 0.10 and mr["n_informative"] >= 10
            pc = dc > 0.15
            cnt["a"] += pa; cnt["b"] += pb; cnt["c"] += pc
            hc = r["habit_contrast_REAL"][ag]
            P("    s%d (a) %s/%s d=%s %s | (b) %s/%s d=%s %s (chance %s, n_inf %d) | (c) %s/%s d=%s %s | habit agree %s rho %s | rho_native2 %s/%s" % (
                s, f(mr["rho_scaf"], 2), f(ms["rho_scaf"], 2), f(da, 2), "P" if pa else "-",
                f(mr["pick_in_Qbest"], 2), f(ms["pick_in_Qbest"], 2), f(db, 2), "P" if pb else "-", f(mr["q_chance"], 2), mr["n_informative"],
                f(mr["flip_vs_init"], 2), f(ms["flip_vs_init"], 2), f(dc, 2), "P" if pc else "-",
                f(hc["pick_agree_with_habit"], 2), f(hc["rho_with_habit"], 2), f(mr["rho_native_secondary"], 2), f(ms["rho_native_secondary"], 2)))
        ok = all(v >= 4 for v in cnt.values())
        passes[ag] = ok
        P("    -> (a) %d/5 (b) %d/5 (c) %d/5 : %s" % (cnt["a"], cnt["b"], cnt["c"], "PASS" if ok else "FAIL"))
    fidw_compat = sum(1 for r in rs.values() if r["fidw_weight_depths"]["REAL"]) >= 4
    compat = {"D1": False, "DISC_0.5": True, "DISC_0.8": True, "FIDW": fidw_compat, "FULL": True}
    sel = next((ag for ag in AGGS if passes[ag] and compat[ag]), None)
    if cd:
        verdict = "CANNOT_DETERMINE"
    elif sel:
        verdict = "SELECTED=%s" % sel
    elif passes["D1"]:
        verdict = "D1_ONLY_SD081_CONFLICT"
    else:
        verdict = "NONE_PASS"
    P("\nSD-081 compat: %s" % compat)
    P("canary (FULL SHUF flip >= 0.5): %d/%d seeds" % (sum(r["metrics"]["SHUF"]["FULL"]["flip_vs_init"] >= 0.5 for r in rs.values()), n))
    P("VERDICT: %s  (passes=%s)" % (verdict, passes))
    txt = "\n".join(out)
    print(txt)
    (HERE / "results" / "SUMMARY.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
