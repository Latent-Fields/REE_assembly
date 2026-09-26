"""Probe R analysis (bt0926-repert). Reads RP_s<seed>.json files and applies the pre-registered
stage-entropy chain (record sec 1). ASCII output only.

usage: repert_analyze.py <json> [<json> ...]
"""
from __future__ import annotations

import json, math, sys
from collections import Counter, defaultdict

import numpy as np

A = 5
CEIL = math.log2(A)
F = 0.5                      # pre-registered drop fraction
STAGES = ("P", "SC", "SEL", "EXEC")


def H(c):
    c = np.asarray(c, dtype=float)
    s = c.sum()
    if s <= 0:
        return float("nan")
    q = c[c > 0] / s
    return float(-(q * np.log2(q)).sum())


def life_stats(L):
    e3 = [e for e in L["e3"] if not e.get("missing")]
    n = len(e3)
    st = {"n_e3": n, "n_missing": len(L["e3"]) - n, "n_ticks": len(L["ticks"])}
    if n == 0:
        return st
    pool = np.mean([np.asarray(e["pool"], float) / e["K"] for e in e3], axis=0)
    poolc = np.mean([np.asarray(e["pool_c"], float) / e["K"] for e in e3], axis=0)
    mass = np.mean([e["mass"] for e in e3], axis=0)
    shuf = np.mean([e["mass_shuf"] for e in e3], axis=0)
    sel = np.bincount([e["sel_cls"] for e in e3], minlength=A)
    argm = np.bincount([e["argmin_cls"] for e in e3], minlength=A)
    ex = np.bincount([t[0] for t in L["ticks"]], minlength=A)
    it0s = [e["it0"] for e in e3 if e.get("it0")]
    if it0s:
        it0 = np.zeros(A)
        for d in it0s:
            v = np.zeros(A)
            for k, c in d.items():
                v[int(k)] += c
            it0 += v / max(1.0, v.sum())
        st["H_P0"] = H(it0)
        st["P0"] = (it0 / len(it0s)).round(3).tolist()
    st.update({
        "H_P": H(pool), "H_Pc": H(poolc), "H_SC": H(mass), "H_SHUF": H(shuf), "H_SEL": H(sel),
        "H_ARGMIN": H(argm), "H_EXEC": H(ex),
        "P": pool.round(3).tolist(), "SC": mass.round(3).tolist(), "SEL": sel.tolist(), "EXEC": ex.tolist(),
        "w_H_pool": float(np.mean([H(e["pool"]) for e in e3])),
        "w_H_mass": float(np.mean([H(e["mass"]) for e in e3])),
        "w_H_cand": float(np.mean([e["hp"] for e in e3])),
        "w_perplex_frac": float(np.mean([2 ** e["hp"] / e["K"] for e in e3])),
        "K": float(np.mean([e["K"] for e in e3])),
        "T_med": float(np.median([e["T"] for e in e3])),
        "rng_over_T_med": float(np.median([e["sc_rng"] / max(e["T"], 1e-12) for e in e3])),
        "sc_std_med": float(np.median([e["sc_std"] for e in e3])),
        "agree_mean": float(np.mean([e["agree_mean"] for e in e3])),
        "pair_med": float(np.median([e["pair"] for e in e3])),
        "norm_med": float(np.median([e["norm_med"] for e in e3])),
        "dim_mean": np.mean([e["dim_mean"] for e in e3], axis=0).round(3).tolist(),
        "dim_std": np.mean([e["dim_std"] for e in e3], axis=0).round(3).tolist(),
        "committed_frac": float(np.mean([e["committed"] for e in e3])),
        "beta_frac": float(np.mean([t[2] for t in L["ticks"]])),
        "sel_eq_exec_e3": float(np.mean([e["sel_cls"] == e["exec_cls"] for e in e3])),
        "sp_inj_mean": float(np.mean([e["sp_inj"] for e in e3])),
        "ident_frac": float(np.mean([bool(e.get("ident", True)) for e in e3])),
        "pchk_max": float(max([e["pchk"] for e in e3 if e.get("pchk") is not None] or [float("nan")])),
    })
    # execution hold asymmetry (registered descriptive + EXEC sub-label): run length of each executed
    # class = ticks from one E3 tick to the next; per-class mean run length; moved / harm shares
    tk = L["ticks"]
    runs = defaultdict(list)
    cur, ln = None, 0
    for t in tk:
        if t[1]:
            if cur is not None:
                runs[cur].append(ln)
            cur, ln = t[0], 0
        ln += 1
    if cur is not None:
        runs[cur].append(ln)
    st["run_mean"] = {int(k): round(float(np.mean(v)), 2) for k, v in sorted(runs.items())}
    st["run_n"] = {int(k): len(v) for k, v in sorted(runs.items())}
    if len(tk[0]) >= 5:
        st["moved_frac"] = float(np.mean([t[3] for t in tk]))
        st["moved_by_cls"] = {c: round(float(np.mean([t[3] for t in tk if t[0] == c])), 2)
                              for c in range(A) if any(t[0] == c for t in tk)}
        st["harm_tick_frac"] = float(np.mean([abs(t[4]) > 0 for t in tk]))
    modal = int(np.argmax(ex))
    others = [x for k, v in runs.items() if k != modal for x in v]
    st["hold_ratio"] = (float(np.mean(runs[modal])) / float(np.mean(others))) if runs.get(modal) and others else float("nan")
    # chain
    prev = CEIL
    first = None
    ratios = {}
    for s in STAGES:
        h = st["H_" + s]
        r = h / prev if prev > 0 else float("nan")
        ratios[s] = r
        if first is None and prev > 0 and h < F * prev:
            first = s
        prev = h
    st["ratios"] = {k: round(v, 3) for k, v in ratios.items()}
    if st["H_EXEC"] >= F * CEIL:
        v = "NO-COLLAPSE"
    elif first is None:
        worst = min(ratios, key=lambda k: ratios[k])
        v = "GRADUAL(%s)" % worst
    else:
        v = first
        if first == "P":
            v = "P/DECODE" if (st["H_Pc"] >= F * CEIL and st["H_P"] < F * st["H_Pc"]) else "P/GENERATOR"
    if v == "EXEC" or v.startswith("GRADUAL(EXEC"):
        v += "/HOLD" if (st["hold_ratio"] == st["hold_ratio"] and st["hold_ratio"] >= 2.0) else "/OTHER"
    st["verdict"] = v
    st["scoring_bottleneck"] = bool(st["H_SC"] < F * st["H_SHUF"])
    return st


def main(paths):
    rows = defaultdict(dict)
    disc = {}
    for pth in paths:
        d = json.load(open(pth))
        s = d["seed"]
        for stg, sd in d["stages"].items():
            disc[(s, stg)] = sd.get("disc4", {}).get("disc4_h1")
            for arm, L in sd["lives"].items():
                rows["%s-%s" % (stg, arm)][s] = life_stats(L)
    seeds = sorted({s for r in rows.values() for s in r})
    n = len(seeds)
    need = math.ceil(0.6 * n)
    print("seeds %s  (cell verdict needs >= %d/%d)  CEIL %.3f bits  F %.2f" % (seeds, need, n, CEIL, F))
    print("disc4_h1: " + "  ".join("s%d %s U %.3f T %.3f" % (s, "", disc.get((s, "U")) or float("nan"),
                                                            disc.get((s, "T")) or float("nan")) for s in seeds))
    print()
    hdr = "%-14s %5s | %5s %5s %5s | %5s %5s %5s %5s %5s | %-13s %s" % (
        "cell", "seed", "H_P0", "H_Pc", "H_P", "H_SC", "SHUF", "H_SEL", "ARGMN", "H_EX", "verdict", "notes")
    print(hdr)
    summ = {}
    for cell in sorted(rows):
        vs = []
        for s in seeds:
            st = rows[cell].get(s)
            if not st or "H_P" not in st:
                continue
            vs.append(st["verdict"])
            print("%-14s %5d | %5s %5.2f %5.2f | %5.2f %5.2f %5.2f %5.2f %5.2f | %-13s e3=%d K=%.0f T=%.3g rng/T=%.3g pplx/K=%.2f wH_mass=%.2f agree=%.2f comm=%.2f beta=%.2f sb=%s EX=%s hold=%.2f run=%s mv=%s" % (
                cell, s, ("%.2f" % st["H_P0"]) if "H_P0" in st else "  -  ", st["H_Pc"], st["H_P"],
                st["H_SC"], st["H_SHUF"], st["H_SEL"], st["H_ARGMIN"], st["H_EXEC"], st["verdict"],
                st["n_e3"], st["K"], st["T_med"], st["rng_over_T_med"], st["w_perplex_frac"], st["w_H_mass"],
                st["agree_mean"], st["committed_frac"], st["beta_frac"], "Y" if st["scoring_bottleneck"] else "n",
                st["EXEC"], st["hold_ratio"], st["run_mean"], st.get("moved_by_cls")))
        base = [v.split("(")[0].split("/")[0] for v in vs]
        c = Counter(base).most_common()
        cv = c[0][0] if c and c[0][1] >= need else "MIXED %s" % dict(Counter(base))
        summ[cell] = (cv, dict(Counter(vs)))
        print("%-14s  CELL VERDICT: %s   (seed verdicts %s)" % (cell, cv, dict(Counter(vs))))
        print()
    print("SUMMARY")
    for cell, (cv, det) in summ.items():
        print("  %-14s %-22s %s" % (cell, cv, det))
    return rows, summ


if __name__ == "__main__":
    main(sys.argv[1:])
