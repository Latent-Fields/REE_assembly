"""bt0925-rt5 analysis (pre-registered with the record, sec 3). Per stratum (NATIVE's in-run
stratum), per metric: per-seed deltas NATIVE - NATIVE-Rk (k=1..3), 2 x RMS pooled over the stratum's
admitted seeds (the A1 sec 6.2 margin form), n / n_nonzero, and a seed-level bootstrap 90% interval
of 2 x RMS (2000 resamples of admitted seeds with replacement, numpy default_rng(0)).
Verdict per (metric, stratum) with an accepted A1 floor:
  CANNOT_DETERMINE  if < 8 deltas or any admitted seed has < 2 completed reseeds (A1 sec 6.2 rule)
  LOWER_BOUND       if floor <= measured 2 x RMS  (the floor is at or below the target noise)
  NOT_LOWER_BOUND   if floor >  measured 2 x RMS  (the floor exceeds the target noise; it binds)
  suffix _WITHIN_CI when the floor lies inside the bootstrap 90% interval (sampling-noise caveat).
ASCII-only output."""
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RES = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "results"
FLOORS = {("reward_LAST", "benign"): 0.90, ("reward_LAST", "hazard_trapped"): 2.4,
          ("contacts_LAST", "benign"): 1.6, ("contacts_LAST", "hazard_trapped"): 4.8,
          ("reward_change", "benign"): 1.44}
METRICS = ["reward_LAST", "contacts_LAST", "reward_change", "grounded_LAST", "consume_LAST_per100",
           "reward_FIRST"]


def arm_metrics(a):
    L, F = a["LAST"], a["FIRST"]
    return {"reward_LAST": L["reward_per100"], "reward_FIRST": F["reward_per100"],
            "reward_change": L["reward_per100"] - F["reward_per100"],
            "contacts_LAST": L["contacts_per100"], "grounded_LAST": L["grounded_per100"],
            "consume_LAST_per100": 100.0 * L["consume_count"] / 600.0}


def two_rms(ds):
    return 2.0 * math.sqrt(sum(x * x for x in ds) / len(ds)) if ds else float("nan")


def modal_share(a):
    c = a.get("action_counts") or {}
    tot = sum(c.values())
    return (max(c.values()) / tot, max(c, key=c.get)) if tot else (float("nan"), None)


def main():
    log = json.load(open(RES / "RT5_log.json"))
    per = {"benign": [], "hazard_trapped": []}
    for st in per:
        for s in log["admitted"][st]:
            d = json.load(open(RES / ("RT5_s%d.json" % s)))
            reps = [d["arms"][k] for k in sorted(d["arms"]) if k.startswith("NATIVE-R") and "LAST" in d["arms"][k]]
            per[st].append({"seed": s, "nat": d["arms"]["NATIVE"], "reps": reps})
    out = {"screen": {"n_screened": len(log["seeds"]),
                      "strata": {st: sum(1 for r in log["seeds"] if r.get("stratum") == st) for st in per},
                      "crashed": sum(1 for r in log["seeds"] if r.get("stratum") == "crashed"),
                      "stop_reason": log.get("stop_reason"), "cum_compute_s": log.get("cum_compute_s")},
           "admitted": log["admitted"], "strata": {}}
    print("== SCREEN: %d env seeds screened (%s), stop=%s, compute %.0fs" % (
        out["screen"]["n_screened"], out["screen"]["strata"], out["screen"]["stop_reason"],
        out["screen"]["cum_compute_s"] or 0))
    for r in log["seeds"]:
        print("  s%d stratum=%s early600=%s admitted=%s t=%ss" % (r["seed"], r.get("stratum"), r.get("early600"),
                                                                r.get("admitted"), r.get("t_s")))
    rng = np.random.default_rng(0)
    for st, seeds in per.items():
        blk = {"seeds": [x["seed"] for x in seeds], "metrics": {}, "per_seed": []}
        print("== STRATUM %s: admitted seeds %s" % (st, blk["seeds"]))
        cd_seed = any(len(x["reps"]) < 2 for x in seeds)
        for x in seeds:
            m0 = arm_metrics(x["nat"])
            ms, mo = modal_share(x["nat"])
            row = {"seed": x["seed"], "NATIVE": m0, "NATIVE_modal_action": [mo, round(ms, 3)],
                   "reps": [], "rep_own_strata": [r.get("stratum") for r in x["reps"]]}
            print("  s%d NATIVE: reward F %.3f L %.3f chg %.3f contacts/100 L %.2f grounded L %.3f modal a%s %.2f"
                  % (x["seed"], m0["reward_FIRST"], m0["reward_LAST"], m0["reward_change"], m0["contacts_LAST"],
                     m0["grounded_LAST"], mo, ms))
            for r in x["reps"]:
                mr = arm_metrics(r)
                ms2, mo2 = modal_share(r)
                row["reps"].append({"k": r["k"], "metrics": mr, "own_stratum": r.get("stratum"),
                                    "modal_action": [mo2, round(ms2, 3)]})
                print("     R%d (own %s): reward F %.3f L %.3f chg %.3f contacts/100 L %.2f grounded L %.3f modal a%s %.2f"
                      % (r["k"], r.get("stratum"), mr["reward_FIRST"], mr["reward_LAST"], mr["reward_change"],
                         mr["contacts_LAST"], mr["grounded_LAST"], mo2, ms2))
            blk["per_seed"].append(row)
        for met in METRICS:
            by_seed = [[arm_metrics(x["nat"])[met] - arm_metrics(r)[met] for r in x["reps"]] for x in seeds]
            ds = [d for bs in by_seed for d in bs]
            val = two_rms(ds)
            boots = []
            if len(seeds) >= 2:
                for _ in range(2000):
                    idx = rng.integers(0, len(seeds), len(seeds))
                    bd = [d for i in idx for d in by_seed[i]]
                    boots.append(two_rms(bd))
            ci = [float(np.percentile(boots, 5)), float(np.percentile(boots, 95))] if boots else None
            rec = {"two_rms": val, "n": len(ds), "n_nonzero": sum(1 for d in ds if abs(d) > 1e-12),
                   "boot90": ci, "per_seed_rms2": [two_rms(b) for b in by_seed]}
            fl = FLOORS.get((met, st))
            if fl is not None:
                rec["floor"] = fl
                if len(ds) < 8 or cd_seed:
                    v = "CANNOT_DETERMINE"
                else:
                    v = "LOWER_BOUND" if fl <= val else "NOT_LOWER_BOUND"
                    if ci and ci[0] <= fl <= ci[1]:
                        v += "_WITHIN_CI"
                rec["verdict"] = v
                rec["ratio_measured_over_floor"] = (val / fl) if ds else None
            blk["metrics"][met] = rec
            print("  %-20s 2xRMS=%s n=%d nz=%d boot90=%s floor=%s -> %s" % (
                met, ("%.3f" % val) if ds else "nan", rec["n"], rec["n_nonzero"],
                ("[%.3f, %.3f]" % tuple(ci)) if ci else "-", fl, rec.get("verdict", "(reported)")))
        # stratum concordance of reseeds (A1 classifies from NATIVE only)
        own = [r for x in blk["per_seed"] for r in x["rep_own_strata"]]
        blk["reseed_stratum_concordance"] = [sum(1 for o in own if o == st), len(own)]
        print("  reseed own-stratum concordance with NATIVE's: %d/%d" % tuple(blk["reseed_stratum_concordance"]))
        nat_last = [arm_metrics(x["nat"])["reward_LAST"] for x in seeds]
        if len(nat_last) >= 2:
            mu = sum(nat_last) / len(nat_last)
            blk["between_seed_sd_NATIVE_reward_LAST"] = math.sqrt(sum((v - mu) ** 2 for v in nat_last) / (len(nat_last) - 1))
            print("  between-seed SD of NATIVE reward_LAST: %.3f" % blk["between_seed_sd_NATIVE_reward_LAST"])
        out["strata"][st] = blk
    json.dump(out, open(RES / "RT5_analysis.json", "w"), indent=1)


if __name__ == "__main__":
    main()
