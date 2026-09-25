"""Summarize the babbling probe against the PRE-REGISTERED criteria (bt0925-babble). ASCII only."""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SEEDS = [106, 107, 108, 109, 110]
res = {s: json.load(open(HERE / "results" / ("BAB_s%d.json" % s))) for s in SEEDS if (HERE / "results" / ("BAB_s%d.json" % s)).exists()}
seeds = sorted(res)
print("seeds present:", seeds)
for s in seeds:
    tp = HERE / "results" / ("BAB_L2R_s%d.json" % s)
    if tp.exists():
        tr = json.load(open(tp))
        res[s]["post"]["L2R"] = dict(tr["L2R"], trailing=True)
        print("s%d L2R from TRAILING block (restored after 08:49Z cap change); L2_pre recompute consistent=%s (%.4f vs %.4f)" % (
            s, tr["consistent_with_main"], tr["L2_pre_recomputed"]["disc4_h1"], tr["L2_pre_main_disc4_h1"]))


def ol(s, arm, key="z"):
    return res[s]["open_loop"]["%s|%s" % (arm, key)]["eval"]["disc4_h1"]


def post(s, arm, f="disc4_h1"):
    p = res[s]["post"].get(arm, {})
    return None if p.get("skipped") or "eval" not in p else p["eval"][f]


def sd(v):
    return float(np.std(v, ddof=1)) if len(v) > 1 else 0.0


print("\n== strata ==")
for s in seeds:
    r = res[s]
    print("s%d %-14s POL %s" % (s, r["hazard_class"], json.dumps({k: round(v, 2) for k, v in r["pol_run"].items()})))

print("\n== doses (entropy nats / mean run length / class counts) ==")
for s in seeds:
    d = res[s]["doses"]
    print("s%d " % s + " | ".join("%s H=%.3f run=%.2f %s" % (k, d[k]["entropy_nats"], d[k]["mean_run_length"], d[k]["class_counts"]) for k in ("L0", "L1", "L2", "POL")))
    print("     L1 generator h_pos_mean=%.3f h_pos_max=%.3f" % (d["L1"]["h_pos_mean"], d["L1"]["h_pos_max"]))

print("\n== open-loop heads: disc4_h1 (z) [pca] ; fit loss_last200/identity ; grad ==")
for s in seeds:
    row = []
    for arm in ("INIT", "B0", "B1", "B1S", "L0_pre", "L2_pre"):
        z = res[s]["open_loop"]["%s|z" % arm]
        pc = res[s]["open_loop"].get("%s|pca" % arm)
        row.append("%s %.3f[%s]" % (arm, z["eval"]["disc4_h1"], "%.3f" % pc["eval"]["disc4_h1"] if pc else "-"))
    print("s%d " % s + "  ".join(row))
    for arm in ("B0", "B1", "L2_pre"):
        t = res[s]["open_loop"]["%s|z" % arm]["train"]
        print("     %s fit %.2e/%.2e delta %.3f grad %s  k=%d h3=%.3f h5=%.3f" % (
            arm, t["loss_last200"], t["identity_mse"], t["param_delta"], t["grad_nonnull_step1"],
            res[s]["open_loop"]["%s|z" % arm]["eval"]["k"], res[s]["open_loop"]["%s|z" % arm]["eval"]["disc4_h3"],
            res[s]["open_loop"]["%s|z" % arm]["eval"]["disc4_h5"]))

# ---- S
b0 = [ol(s, "B0") for s in seeds]
M_S = max(0.05, sd(b0))
print("\n== S (sufficiency) M_S = max(0.05, SD(B0)=%.4f) = %.4f ==" % (sd(b0), M_S))
s_pass = 0
for s in seeds:
    g0, gs = ol(s, "B1") - ol(s, "B0"), ol(s, "B1") - ol(s, "B1S")
    ok = g0 > M_S and gs > M_S
    s_pass += ok
    print("s%d %-14s B1-B0=%+.3f B1-B1S=%+.3f -> %s" % (s, res[s]["hazard_class"], g0, gs, "pass" if ok else "fail"))
S = "PASS" if s_pass >= 4 else "FAIL"
print("S = %s (%d/%d)" % (S, s_pass, len(seeds)))
b0p = [ol(s, "B0", "pca") for s in seeds]
M_Sp = max(0.05, sd(b0p))
print("  secondary PCA-32: " + "  ".join("s%d B1-B0=%+.3f B1-B1S=%+.3f" % (s, ol(s, "B1", "pca") - ol(s, "B0", "pca"), ol(s, "B1", "pca") - ol(s, "B1S", "pca")) for s in seeds) + "  (M=%.3f)" % M_Sp)

# ---- R / R3
print("\n== R / R3 ==")
if S != "PASS":
    print("R = CANNOT_DETERMINE (S did not pass; no babbling gain to retain)")
    print("R3 = CANNOT_DETERMINE (precondition not met; B3 also dropped for budget)")
else:
    r_pass = 0
    for s in seeds:
        gain = ol(s, "B1") - ol(s, "B0")
        ret = (post(s, "L1_post") - ol(s, "B0")) / gain if gain > M_S else None
        r_pass += bool(ret is not None and ret >= 0.5)
        print("s%d ret=%s" % (s, ret))
    print("R = %s (%d/%d)" % ("PASS" if r_pass >= 4 else "FAIL", r_pass, len(seeds)))
    print("R3 = CANNOT_DETERMINE (B3 dropped for budget)" if r_pass < 4 else "R3 = CANNOT_DETERMINE (R passed; not evaluated)")
print("  descriptive retention of the NATIVE L1 head (not a verdict): " + "  ".join(
    "s%d B1=%.3f L1post=%.3f B0=%.3f" % (s, ol(s, "B1"), post(s, "L1_post"), ol(s, "B0")) for s in seeds))

# ---- DR
l1p = [post(s, "L1_post") for s in seeds]
M_DR = max(0.05, sd(l1p))
print("\n== DR (dose-response after the post phase) M_DR = max(0.05, SD(L1_post)=%.4f) = %.4f ==" % (sd(l1p), M_DR))
dr_pass = 0
for s in seeds:
    a0, a1, a2 = post(s, "L0_post"), post(s, "L1_post"), post(s, "L2_post")
    ok = a0 < a1 < a2 and (a2 - a0) > M_DR
    dr_pass += ok
    print("s%d %-14s L0=%.3f L1=%.3f L2=%.3f  L2-L0=%+.3f  mono=%s -> %s" % (s, res[s]["hazard_class"], a0, a1, a2, a2 - a0, a0 < a1 < a2, "pass" if ok else "fail"))
print("DR = %s (%d/%d)" % ("PASS" if dr_pass >= 4 else "FAIL", dr_pass, len(seeds)))
print("  secondary, entropy-ordered (descriptive): ")
for s in seeds:
    d = res[s]["doses"]
    order = sorted(("L0", "L1", "L2"), key=lambda k: d[k]["entropy_nats"])
    vals = [post(s, k + "_post") for k in order]
    print("   s%d entropy order %s -> disc %s monotone=%s ; L2-L0 gap %+.3f" % (s, order, ["%.3f" % v for v in vals], vals[0] < vals[1] < vals[2], post(s, "L2_post") - post(s, "L0_post")))
print("  pre-post (open loop) doses: " + "  ".join("s%d L0=%.3f L1=%.3f L2=%.3f" % (s, ol(s, "L0_pre"), ol(s, "B1"), ol(s, "L2_pre")) for s in seeds))

# ---- L2 retention vs L2R, NB
print("\n== secondary: L2 retention (one-off vs retained replay for a DIVERSE source) ==")
for s in seeds:
    g = ol(s, "L2_pre") - ol(s, "B0")
    rp = post(s, "L2_post"); rr = post(s, "L2R"); nb = post(s, "NB")
    fmt = lambda v: "n/a" if v is None else "%.3f" % v
    ret = (rp - ol(s, "B0")) / g if g > 0.0 else None
    retR = (rr - ol(s, "B0")) / g if (g > 0.0 and rr is not None) else None
    print("s%d L2_pre=%.3f B0=%.3f gain=%+.3f | L2_post=%s ret=%s | L2R=%s retR=%s | NB=%s | k: L2pre=%d L2post=%s L2R=%s" % (
        s, ol(s, "L2_pre"), ol(s, "B0"), g, fmt(rp), fmt(ret), fmt(rr), fmt(retR), fmt(nb),
        res[s]["open_loop"]["L2_pre|z"]["eval"]["k"], post(s, "L2_post", "k"), post(s, "L2R", "k")))

# ---- BEH
nr = [((post(s, "L2R") - ol(s, "B0")) / (ol(s, "L2_pre") - ol(s, "B0"))) for s in seeds
      if post(s, "L2R") is not None and ol(s, "L2_pre") - ol(s, "B0") > 0]
np_ = [((post(s, "L2_post") - ol(s, "B0")) / (ol(s, "L2_pre") - ol(s, "B0"))) for s in seeds if ol(s, "L2_pre") - ol(s, "B0") > 0]
print("L2 one-off retention >= 0.5 in %d/%d seeds; L2R (retained replay) >= 0.5 in %d/%d seeds with L2R" % (
    sum(r >= 0.5 for r in np_), len(seeds), sum(r >= 0.5 for r in nr), len(nr)))
print("\n== BEH (last 50%% of post phase; prediction reward L2>L1>L0, harm L2<=L0) ==")
n_rew, n_harm = 0, 0
for s in seeds:
    b = {k: res[s]["post"][k]["beh_last50"] for k in ("L0_post", "L1_post", "L2_post", "L2R", "NB") if "beh_last50" in res[s]["post"].get(k, {})}
    ro = b["L2_post"]["reward_per_100"] > b["L1_post"]["reward_per_100"] > b["L0_post"]["reward_per_100"]
    ho = b["L2_post"]["harm_events_per_100"] <= b["L0_post"]["harm_events_per_100"]
    n_rew += ro; n_harm += ho
    print("s%d %-14s " % (s, res[s]["hazard_class"]) + " | ".join(
        "%s r=%.2f harm=%.1f ben=%.2f H=%.2f early=%d" % (k.replace("_post", ""), v["reward_per_100"], v["harm_events_per_100"],
                                                         v["benefit_events_per_100"], v["action_entropy"], v["early_terminations"])
        for k, v in b.items()) + "  || rewardL2>L1>L0=%s harmL2<=L0=%s" % (ro, ho))
print("BEH direction: reward ordering matches in %d/%d seeds; harm L2<=L0 in %d/%d (sign-test p one-sided for reward, chance 1/6 per seed)" % (n_rew, len(seeds), n_harm, len(seeds)))

# ---- D2 and depth-1
print("\n== D2 reach (pick change vs native head at 20 probe states) ==")
for s in seeds:
    print("s%d n=%s valid_maxabs=%s %s" % (s, res[s].get("n_probe_states"), res[s].get("probe_validation_maxabs"),
                                          json.dumps(res[s].get("D2_pick_change_vs_native"))))
print("\n== depth-1 diagnostic: Spearman(J_pred, J_true) FULL / DEPTH1; pick-in-true-best FULL / DEPTH1 (chance) ==")
for s in seeds:
    dd = res[s].get("depth1_diag", {})
    print("s%d " % s + " | ".join("%s %.2f/%.2f %.2f/%.2f(%.2f)" % (k, v["spearman_Jpred_Jtrue_FULL"] or 0, v["spearman_Jpred_Jtrue_DEPTH1"] or 0,
                                                              v["pick_is_true_best_FULL"] or 0, v["pick_is_true_best_DEPTH1"] or 0, v["chance"] or 0) for k, v in dd.items()))
print("\nwall per seed:", {s: res[s]["t_total_s"] for s in seeds})
