"""Analyse OP_s*.json: per evaluator set and channel, regress the grounded outcome on the
channel's vote for the executed random action. Positive t = the channel's vote predicts better
grounded outcome (the sign a valid channel should carry). ASCII-only output."""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
CH = ["F", "harm", "residue", "benefit"]
SIGN = np.array([1, 1, 1, -1], float)
THR = 0.1


def reg_t(x, y):
    if x.std() < 1e-12 or y.std() < 1e-12:
        return None
    xc = x - x.mean(); b = (xc * (y - y.mean())).sum() / (xc ** 2).sum()
    res = y - y.mean() - b * xc
    se = np.sqrt((res ** 2).sum() / max(len(x) - 2, 1) / (xc ** 2).sum())
    return float(b / se) if se > 0 else None


def main():
    seeds = [int(s) for s in sys.argv[1:]] or [43, 44, 42]
    out = {}
    for s in seeds:
        p = HERE / "results" / ("OP_s%d.json" % s)
        if not p.exists():
            print("missing", p); continue
        rows = json.load(open(p))["rows"]
        r = np.array([x["r"] for x in rows]); a = np.array([x["a"] for x in rows])
        ys = {"Gall": r, "Gcontact": np.where(np.abs(r) > THR, r, 0.0),
              "contact_neg": (r < -THR).astype(float) * -1.0, "contact_pos": (r > THR).astype(float)}
        out[s] = {"n": len(r), "n_contact_neg": int((r < -THR).sum()), "n_contact_pos": int((r > THR).sum()),
                  "n_nonzero": int((r != 0).sum()), "sets": {}}
        for k in rows[0]["terms"]:
            X = np.array([x["terms"][k] for x in rows])  # [n, A, 4]
            n, A, _ = X.shape
            sel = X[np.arange(n), a]  # [n,4]
            oth = (X.sum(1) - sel) / (A - 1)
            V = -SIGN * (sel - oth)
            spread = X.std(1).mean(0)
            res = {"xstate_spread_mean": dict(zip(CH, spread.round(6).tolist())), "t": {}}
            for yk, y in ys.items():
                res["t"][yk] = {c: (None if reg_t(V[:, j], y) is None else round(reg_t(V[:, j], y), 2)) for j, c in enumerate(CH)}
            # action fixed effects: demean vote and outcome within executed-action class
            Vd = V.copy(); res["t_fe"] = {}
            for aa in range(A):
                m = a == aa
                if m.sum():
                    Vd[m] -= V[m].mean(0)
            for yk, y in ys.items():
                yd = y.astype(float).copy()
                for aa in range(A):
                    m = a == aa
                    if m.sum():
                        yd[m] -= y[m].mean()
                res["t_fe"][yk] = {c: (None if reg_t(Vd[:, j], yd) is None else round(reg_t(Vd[:, j], yd), 2)) for j, c in enumerate(CH)}
            out[s]["sets"][k] = res
    json.dump(out, open(HERE / "results" / "OP_analysis.json", "w"), indent=1)
    for s, d in out.items():
        print("=== seed %d n=%d nonzero=%d contact_neg=%d contact_pos=%d" % (s, d["n"], d["n_nonzero"], d["n_contact_neg"], d["n_contact_pos"]))
        for k, res in d["sets"].items():
            print(" %-12s spread %s" % (k, res["xstate_spread_mean"]))
            for yk, tv in res["t"].items():
                print("    t   [%-11s] %s" % (yk, tv))
            for yk, tv in res["t_fe"].items():
                print("    tFE [%-11s] %s" % (yk, tv))


if __name__ == "__main__":
    main()
