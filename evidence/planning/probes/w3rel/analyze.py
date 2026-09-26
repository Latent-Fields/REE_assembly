"""Aggregate W3REL_s*.json (real+shuf, post=1200) into pass rate + predictor separation.
Pre-registered analysis: w3_reliability_sweep_20260926.md sec 2 "Analysis".
ASCII only.
"""
import glob, json, math, sys

files = sorted(glob.glob("results/W3REL_s*.json"))
rows = []
for f in files:
    d = json.load(open(f))
    r = d["arms"]["real"]
    s = d["arms"]["shuf"]
    rows.append({
        "seed": d["seed"], "gate_a": r["gate_a"],
        "post_disc4": r["post"]["disc4_h1"], "post_k": r["post"]["k"],
        "twin_disc4": s["post"]["disc4_h1"], "retention": r["retention"],
        "guard_pass": all(v == "PASS" for v in r["guard"].values()),
        "frozen_ok": r["frozen_retained_unchanged_after_post"],
        "B0": d["B0"], "INIT": d["init"]["disc4_h1"],
        "babble_entropy": r["babble_entropy"], "babble_stay_share": r["babble_stay_share"],
        "babble_wallpush": r["babble_wallpush_share_of_moves"],
        "post_entropy": r["post_entropy"], "post_stay_share": r["post_stay_share"],
        "post_wallpush": r["post_wallpush_share_of_moves"],
        "stratum": r["hazard_stratum_A1"].get("stratum", "CANNOT_DETERMINE"),
        "rollout_bounded": r["rollout_late_step_growth_max"] <= 1.2 and 0.5 <= r["rollout_t30_over_t0_median"] <= 2,
    })

n = len(rows)
k = sum(1 for r in rows if r["gate_a"])


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None, None)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (p, max(0.0, center - half), min(1.0, center + half))


def clopper_pearson(k, n):
    # exact 95% CI via beta quantiles (no scipy: fall back to a coarse search if unavailable)
    try:
        from scipy import stats
        lo = 0.0 if k == 0 else stats.beta.ppf(0.025, k, n - k + 1)
        hi = 1.0 if k == n else stats.beta.ppf(0.975, k + 1, n - k)
        return (lo, hi)
    except Exception:
        return (None, None)


p, wlo, whi = wilson(k, n)
clo, chi = clopper_pearson(k, n)

print("N = %d, pass = %d, pass_rate = %s" % (n, k, ("%.3f" % p) if p is not None else "NA"))
print("Wilson 95%% CI: [%s, %s]" % (("%.3f" % wlo) if wlo is not None else "NA",
                                     ("%.3f" % whi) if whi is not None else "NA"))
print("Clopper-Pearson 95%% CI: [%s, %s]" % (("%.3f" % clo) if clo is not None else "NA (scipy unavailable)",
                                              ("%.3f" % chi) if chi is not None else ""))
print()

pass_rows = [r for r in rows if r["gate_a"]]
miss_rows = [r for r in rows if not r["gate_a"]]
print("pass n=%d miss n=%d" % (len(pass_rows), len(miss_rows)))


def cohend(a, b):
    if len(a) < 2 or len(b) < 2:
        return None
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
    sp = math.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2))
    if sp == 0:
        return None
    return (ma - mb) / sp


PREDICTORS = ["B0", "INIT", "babble_entropy", "babble_stay_share", "babble_wallpush",
              "post_entropy", "post_stay_share", "post_wallpush"]
print("\nPredictor separation (Cohen's d, pass-mean minus miss-mean; |d|>=0.8 = separating):")
for p_ in PREDICTORS:
    a = [r[p_] for r in pass_rows]
    b = [r[p_] for r in miss_rows]
    if not a or not b:
        print("  %-18s CANNOT_DETERMINE (one group empty: pass=%d miss=%d)" % (p_, len(a), len(b)))
        continue
    d = cohend(a, b)
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    flag = "SEPARATING" if (d is not None and abs(d) >= 0.8) else "no"
    print("  %-18s pass_mean=%.4f miss_mean=%.4f d=%s  %s" % (
        p_, ma, mb, ("%.3f" % d) if d is not None else "NA (zero pooled SD)", flag))

print("\nA1 hazard stratum (pass rate by stratum, Wilson 95%% CI):")
for strat in ("hazard_trapped", "benign", "CANNOT_DETERMINE"):
    sub = [r for r in rows if r["stratum"] == strat]
    if not sub:
        continue
    ks = sum(1 for r in sub if r["gate_a"])
    ps, lo, hi = wilson(ks, len(sub))
    print("  %-16s n=%2d pass=%2d rate=%s CI=[%s,%s]" % (
        strat, len(sub), ks, ("%.3f" % ps) if ps is not None else "NA",
        ("%.3f" % lo) if lo is not None else "NA", ("%.3f" % hi) if hi is not None else "NA"))

print("\nAnomalies: guard_fail=%d frozen_broken=%d rollout_unbounded=%d" % (
    sum(1 for r in rows if not r["guard_pass"]), sum(1 for r in rows if not r["frozen_ok"]),
    sum(1 for r in rows if not r["rollout_bounded"])))

print("\nPer-seed table:")
print("seed post_disc4 k twin_disc4 gate_a retention stratum B0 INIT bab_ent bab_stay bab_wall post_ent post_stay post_wall")
for r in sorted(rows, key=lambda x: x["seed"]):
    print("%4d %.4f %2d %.4f %-5s %s %-14s %.4f %.4f %.3f %.3f %.3f %.3f %.3f %.3f" % (
        r["seed"], r["post_disc4"], r["post_k"], r["twin_disc4"], str(r["gate_a"]),
        ("%.3f" % r["retention"]) if r["retention"] is not None else "NA", r["stratum"],
        r["B0"], r["INIT"], r["babble_entropy"], r["babble_stay_share"], r["babble_wallpush"],
        r["post_entropy"], r["post_stay_share"], r["post_wallpush"]))

miss_seeds = sorted(r["seed"] for r in miss_rows)
print("\nMISS seeds (in order): %s" % miss_seeds)
print("First 5 for DOSE probe: %s" % miss_seeds[:5])

json.dump({"n": n, "pass": k, "pass_rate": p, "wilson_ci": [wlo, whi], "cp_ci": [clo, chi],
           "miss_seeds": miss_seeds, "rows": rows}, open("results/SUMMARY.json", "w"), indent=1)
