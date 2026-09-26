"""Analyse DCH2 / N5b stage 1 (bt0926-dch2). Reads results/DCH2_s<seed>.json for the registered seeds.
Pre-registered DVs and verdict: see h2_shift_detector_n5b_probe_20260926.md sec 2. ASCII only.
usage: dch2_analyze.py <out.json> <result.json>...
"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dch2_stats as D

# thresholds calibrated on calibration seed 840 NO-SHIFT cells only (addendum 3a): smallest value
# with <= 1 pooled alarm over its three no-shift cells (3600 steps)
CP_K, CP_H, MAG_THR, MAG_N5_THR = 0.5, 45.0, 1.2, 0.75

outp = sys.argv[1]
files = sys.argv[2:]
RUNS = [json.load(open(f)) for f in files]
ALLOW_FAIL = os.environ.get("DCH2_ALLOW_PA_FAIL") == "1"   # calibration-seed display only
RUNS = [r for r in RUNS if (r.get("pa_pass") or ALLOW_FAIL) and r.get("cells")]
COL = {"gs": 0, "src": 1, "pe": 2, "ac": 3, "z": 4, "s": 5, "gw": 6, "C_on": 7, "C_bab": 8,
       "Cnr_on": 9, "Cnr_bab": 10, "sps_on": 11, "sps_bab": 12}
SEP_MIN, AUC_MIN, MARGIN = 0.6, 0.8, 0.4


def window(run):
    ar = run["args"]
    return ar["t_shift"], ar["n_adult"]


def score(cell, stat, ts, n):
    if stat == "CP":
        return D.cp_score(cell["recs"], ts, n, K=CP_K)
    return D.mag_score(cell["recs"], ts, n)


def alarm_list(cell, stat):
    if stat == "CP":
        return D.cp_alarms(cell["recs"], K=CP_K, H=CP_H)
    if stat == "MAG":
        return D.mag_alarms(cell["recs"], thr=MAG_THR)
    return D.mag_alarms(cell["recs"], thr=MAG_N5_THR)


def alarms_in(cell, stat, lo, hi):
    return [x for x in alarm_list(cell, stat) if lo <= x < hi]


def auroc(pos, neg):
    s = 0.0
    for x in pos:
        for y in neg:
            s += 1.0 if x > y else (0.5 if x == y else 0.0)
    return s / (len(pos) * len(neg))


res = {"seeds": [r["seed"] for r in RUNS], "thresholds": {"CP_K": CP_K, "CP_H": CP_H, "MAG_THR": MAG_THR, "MAG_N5_THR": MAG_N5_THR}, "conditions": {}}
rng = np.random.default_rng(12345)
for probe in ("off", "on8", "on25"):
    for stat in ("MAG", "CP", "MAGn5"):
        key = "%s-%s" % (stat, probe)
        per = []
        for r in RUNS:
            if "shift_" + probe not in r["cells"] or "noshift_" + probe not in r["cells"]:
                continue
            ts, n = window(r)
            cs, cn = r["cells"]["shift_" + probe], r["cells"]["noshift_" + probe]
            hs, fs = alarms_in(cs, stat, ts, n), alarms_in(cn, stat, ts, n)
            per.append({"seed": r["seed"], "hit": bool(hs), "fa": bool(fs),
                        "latency": (hs[0] - ts) if hs else None,
                        "score_shift": score(cs, stat, ts, n), "score_noshift": score(cn, stat, ts, n),
                        "fa_per_1000_noshift": 1000.0 * len(alarm_list(cn, stat)) / n,
                        "alarms_total_shift": len(alarm_list(cs, stat)), "alarms_total_noshift": len(alarm_list(cn, stat)),
                        "rate_per_step": (len(alarm_list(cs, stat)) + len(alarm_list(cn, stat))) / (2.0 * n),
                        "L": n - ts})
        if not per:
            continue
        k = len(per)
        sep = (sum(p["hit"] for p in per) - sum(p["fa"] for p in per)) / k
        auc = auroc([p["score_shift"] for p in per], [p["score_noshift"] for p in per])
        paired = sum(p["score_shift"] > p["score_noshift"] for p in per)
        # rate-matched random trigger (wrong-reason control): same per-seed alarm rate, no information
        sims = np.zeros(20000)
        for p in per:
            q = 1.0 - (1.0 - p["rate_per_step"]) ** p["L"]
            sims += (rng.random(20000) < q).astype(float) - (rng.random(20000) < q).astype(float)
        sims /= k
        p_rand = float(np.mean(sims >= sep - 1e-12))
        res["conditions"][key] = {
            "n_seeds": k, "hits": sum(p["hit"] for p in per), "fas": sum(p["fa"] for p in per), "sep": sep,
            "auroc": auc, "paired_shift_gt_noshift": paired, "p_random_trigger": p_rand,
            "random_sep_p95": float(np.quantile(sims, 0.95)),
            "separates": bool(sep >= SEP_MIN and auc >= AUC_MIN and p_rand < 0.05),
            "fa_per_1000_noshift_mean": float(np.mean([p["fa_per_1000_noshift"] for p in per])),
            "latency": [p["latency"] for p in per], "per_seed": per}

C = res["conditions"]


def sep(k):
    return C[k]["sep"] if k in C else float("nan")


def sepd(k):
    return k in C and C[k]["separates"]


if len(RUNS) < 5:
    verdict = "CANNOT_DETERMINE (fewer than 5 registered seeds passed P-a: %d)" % len(RUNS)
elif sepd("CP-on8"):
    if sepd("MAG-on8") and sep("CP-on8") - sep("MAG-on8") < MARGIN:
        if not sepd("CP-off") and not sepd("MAG-off"):
            verdict = "F2 (separation appears with probes for both statistics and not without; the gain is the probe = ARC-156)"
        else:
            verdict = "F1 (both statistics separate, with and without probes; the change-point statistic adds nothing over calibrated magnitude)"
    elif sepd("CP-off") and sep("CP-on8") - sep("CP-off") < MARGIN:
        verdict = "STATISTIC-ONLY (CP separates without probes; the probe leg is not needed)"
    else:
        verdict = "SUPPORTED (CP with probes separates; MAG with probes and CP without probes do not, by margin)"
else:
    if sepd("CP-on25") or sepd("MAG-on25"):
        verdict = "F3 (separation only above the 10% probe-budget ceiling)"
    else:
        verdict = "F1 (with probes ON the change-point statistic does not separate; no better than magnitude)"
res["verdict"] = verdict

# P-b / informativeness readout
inf = {}
for r in RUNS:
    for cn, c in r["cells"].items():
        for kk, v in c["steplog_summary"].items():
            inf.setdefault(cn + ":" + kk, []).append(v["informative"])
res["informative_fraction_mean"] = {k: (float(np.mean([x for x in v if x is not None])) if any(x is not None for x in v) else None)
                                    for k, v in sorted(inf.items())}
json.dump(res, open(outp, "w"), indent=1, default=str)
print("seeds", res["seeds"])
for k in sorted(C):
    c = C[k]
    print("%-10s hits %d/%d fa %d/%d sep %+.2f auroc %.2f paired %d/%d p_rand %.3f fa/1000 %.2f lat %s -> %s" % (
        k, c["hits"], c["n_seeds"], c["fas"], c["n_seeds"], c["sep"], c["auroc"], c["paired_shift_gt_noshift"],
        c["n_seeds"], c["p_random_trigger"], c["fa_per_1000_noshift_mean"], c["latency"],
        "SEPARATES" if c["separates"] else "no"))
print("VERDICT:", verdict)
