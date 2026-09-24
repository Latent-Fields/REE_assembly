"""Common-mode check: fraction of committed ticks where each channel votes FOR the pick, and
M3 open-loop z with asym=1.0 (symmetric) vs 0.5 (ARC-108). ASCII-only."""
import json
import numpy as np
import analyze_feasibility as AF
for s in (42, 43, 44):
    d = json.load(open("results/VF_s%d.json" % s))
    for name in ("T2_FULL_EVAL", "T3_FULL_SHUF"):
        arm = d["arms"][name]
        _, rows = AF.arm_stats(arm)
        V = np.array([r[1] for r in rows if r[0]])
        frac = (V > 0).mean(0)
        R = np.array([r[4] for r in rows if r[0]])
        # M3 with symmetric asym
        orig = AF.m3_open_loop
        rew = np.asarray(arm["rewards"]); w = np.array([arm["weights"][k] for k in AF.WKEY]); w = np.where(w > 0, w, 1.0)
        inj = {}
        for t in arm["ticks"]:
            if len(t["terms"]) < 2 or not t["committed"]:
                continue
            X = np.asarray(t["terms"]) / w; k = t["sel"]
            inj[t["step"]] = -AF.SIGN * (X[k] - np.delete(X, k, axis=0).mean(0))
        res = {}
        for asym in (0.5, 1.0):
            e = np.zeros(5); Vh = 0.0; th = np.zeros(5); incs = []
            for st, r in enumerate(rew):
                r = r if abs(r) > 0.1 else 0.0
                e = 0.9 * e + inj.get(st, 0.0); dlt = r - Vh; Vh += 0.05 * (r - Vh)
                inc = 0.01 * dlt * e * (1.0 if dlt > 0 else asym); th += inc; incs.append(inc)
            incs = np.asarray(incs)
            res[asym] = (th / (incs.std(0) * np.sqrt(len(incs)) + 1e-12)).round(2)[:4].tolist()
        print("s%d %-13s vote_for_pick_frac(F,harm,res,ben)=%s  contactR<0 ticks=%d >0=%d  M3z asym0.5=%s asym1.0=%s" % (
            s, name, frac.round(2)[:4].tolist(), int((R < 0).sum()), int((R > 0).sum()), res[0.5], res[1.0]))
