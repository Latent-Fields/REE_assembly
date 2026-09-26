"""Probe C analysis (bt0926-cgdisc). Reads cg_probe.py per-seed JSONs, applies the PRE-REGISTERED
DVs and verdict rules (record sec 2), prints ASCII tables and writes a summary JSON.

usage: cg_analyze.py <wt> <out_summary.json> <seed_json> [<seed_json> ...]
Seed JSONs are given in REGISTRATION ORDER (the first two registered are the tuning seeds).
"""
import json, math, sys, types
from collections import deque
from pathlib import Path

import numpy as np

WT = sys.argv[1]
OUT = sys.argv[2]
FILES = sys.argv[3:]
sys.path.insert(0, WT)
from ree_core.predictors.e3_selector import E3TrajectorySelector  # noqa: E402

import os
EXCL0 = int(os.environ.get("CG_EXCL0", 60))   # first ticks of every life excluded (EMA / policy-switch transient)
RESET_EXCL = 8       # ticks after any env reset excluded
K = int(os.environ.get("CG_K", 50))            # C0 / C1 post-change window
K2 = int(os.environ.get("CG_K2", 120))         # C2 post-change window
SEP_A, SEP_D = 0.70, 0.15
Q, WIN = 0.90, int(os.environ.get("CG_WIN", 60))
GRID_Q = [0.5, 0.75, 0.9, 0.95, 0.99, 0.999]
SHUF_MARGIN = 0.15
N_RAND = 1000


def load(f):
    d = json.load(open(f))
    return d


def arr(x):
    return np.array([np.nan if v is None else float(v) for v in x], dtype=float)


def signals(life):
    r = life["rec"]
    return {"RAW_MIX": arr(r["raw_mix"]), "EMA_MIX": arr(r["rv"]),
            "RAW_REAL": arr(r["raw_real"]), "EMA_REAL": arr(r["ema_real"])}


def valid_mask(life, n):
    m = np.ones(n, bool)
    m[:EXCL0] = False
    for t in life["events"]["resets"]:
        m[t + 1:t + 1 + RESET_EXCL] = False
    return m


def windows(n, tc, k):
    idx = np.arange(n)
    pre = (idx >= EXCL0) & (idx < tc)
    post = (idx >= tc + 1) & (idx <= tc + k)
    return pre, post


def auroc(pos, neg):
    pos = pos[np.isfinite(pos)]; neg = neg[np.isfinite(neg)]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    allv = np.concatenate([pos, neg])
    # average ties
    order = np.argsort(allv, kind="mergesort"); sv = allv[order]; rk = np.empty(len(allv))
    i = 0
    while i < len(sv):
        j = i
        while j + 1 < len(sv) and sv[j + 1] == sv[i]:
            j += 1
        rk[order[i:j + 1]] = (i + j) / 2.0 + 1
        i = j + 1
    rp = rk[:len(pos)].sum()
    return float((rp - len(pos) * (len(pos) + 1) / 2.0) / (len(pos) * len(neg)))


def sep(ch, nu, sig, tc, k, sel=None):
    """A_ch, A_null, D, separates. sel: optional per-tick boolean mask (e.g. probe-evidence ticks)."""
    out = []
    for life in (ch, nu):
        x = signals(life)[sig]; n = len(x)
        v = valid_mask(life, n)
        pre, post = windows(n, tc, k)
        if sel is not None:
            v = v & sel[:n]
        out.append(auroc(x[post & v], x[pre & v]))
    A, An = out
    D = A - An if math.isfinite(A) and math.isfinite(An) else float("nan")
    # report only: same post ticks, change life vs no-change life (lives identical before the change)
    xc = signals(ch)[sig]; xn = signals(nu)[sig]; n = min(len(xc), len(xn))
    vc = valid_mask(ch, n) & valid_mask(nu, n)
    if sel is not None:
        vc = vc & sel[:n]
    _pre, post = windows(n, tc, k)
    Ap = auroc(xc[:n][post & vc], xn[:n][post & vc])
    return {"A": A, "A_null": An, "D": D, "A_pair": Ap, "sep": bool(math.isfinite(D) and A >= SEP_A and D >= SEP_D)}


def hit_fa(life, sig, tc, k):
    x = signals(life)[sig]; n = len(x); v = valid_mask(life, n)
    pre, post = windows(n, tc, k)
    base = x[pre & v]; base = base[np.isfinite(base)]
    if len(base) < 20:
        return None
    thr = np.quantile(base, 0.99)
    hit = bool(np.nanmax(np.where(post & v, x, -np.inf)) > thr)
    wins = [(s, s + k) for s in range(EXCL0, tc - k + 1, k)]
    fa = np.mean([bool(np.nanmax(np.where(v[s:e], x[s:e], -np.inf)) > thr) for s, e in wins]) if wins else float("nan")
    return {"hit": hit, "fa": float(fa)}


def own_bars(x, q=Q, w=WIN):
    stub = types.SimpleNamespace(_commit_gate_variance_window=deque(maxlen=w),
                                 config=types.SimpleNamespace(commit_threshold_quantile=q))
    bars = np.full(len(x), np.nan)
    for t, v in enumerate(x):
        b = E3TrajectorySelector._variance_tracking_commit_bar(stub)
        bars[t] = np.nan if b is None else b
        if math.isfinite(v):
            stub._commit_gate_variance_window.append(float(v))
    return bars


def uncommitted(x, bar):
    """committed iff x < bar (native rule). A None/NaN bar (warmup) falls back to the absolute
    0.40 bar, as the native lever does."""
    b = np.where(np.isfinite(bar), bar, 0.40)
    u = ~(x < b)
    u[~np.isfinite(x)] = False
    return u


def appropriateness(life, u, tc, k):
    n = len(u); v = valid_mask(life, n); pre, post = windows(n, tc, k)
    pp = u[post & v].mean() if (post & v).any() else float("nan")
    pr = u[pre & v].mean() if (pre & v).any() else float("nan")
    occ = 1.0 - u[v].mean()
    return {"approp": float(pp - pr), "p_unc_post": float(pp), "false_decommit_pre": float(pr), "occupancy": float(occ)}


def entropy_bits(acts):
    c = np.bincount(np.asarray(acts, int), minlength=5).astype(float)
    if c.sum() == 0:
        return float("nan")
    p = c / c.sum(); p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def fmt(v, n=3):
    return "  nan" if v is None or (isinstance(v, float) and not math.isfinite(v)) else ("%.*f" % (n, v))


seeds = [load(f) for f in FILES]
SUM = {"files": FILES, "seeds": [d["seed"] for d in seeds], "params": dict(EXCL0=EXCL0, RESET_EXCL=RESET_EXCL, K=K, K2=K2,
       SEP_A=SEP_A, SEP_D=SEP_D, Q=Q, WIN=WIN, GRID_Q=GRID_Q, SHUF_MARGIN=SHUF_MARGIN)}
tc = seeds[0]["args"]["tc"]

# ------------------------------------------------------------------ screen + premises
print("== screen / premises ==")
for d in seeds:
    st = d["stages"]
    print("seed %d  S1 disc4 %s pass %s | S2 disc4 %s | premise b %s c cross@%s rv0 %s | d %s" % (
        d["seed"], fmt(st["S1"]["disc4"]["disc4_h1"]), st["S1"]["screen_pass"],
        fmt(st["S2"]["disc4"]["disc4_h1"]) if "S2" in st else "-",
        d["premise"].get("b_rv_before_after_agent_reset"), d["premise"].get("c_first_index_below_0p40"),
        [round(v, 3) for v in d["premise"].get("c_rv_first12_native", [])[:6]],
        {k: d["premise"].get(k) for k in ("d_raises_if_unset",)}))
# premise (a): raw_mix by k-since-E3 and agreement with raw_real at k=1
pa = {}
for d in seeds:
    life = d["stages"]["S1"]["lives"].get("NAT-none") or d["stages"]["S1"]["lives"].get("FS-none")
    r = life["rec"]; x = signals(life)
    since = None; bk = {}
    for t, e3 in enumerate(r["e3_tick"]):
        since = 0 if e3 else (None if since is None else since + 1)
        if since is None or t < EXCL0:
            continue
        kk = min(since, 5)
        bk.setdefault(kk, {"mix": [], "real": []})
        bk[kk]["mix"].append(x["RAW_MIX"][t]); bk[kk]["real"].append(x["RAW_REAL"][t])
    row = {}
    for kk, v in sorted(bk.items()):
        m = np.array(v["mix"]); rr = np.array(v["real"]); ok = np.isfinite(m) & np.isfinite(rr) & (rr > 0)
        row[kk] = {"n": int(len(m)), "mix_mean": float(np.nanmean(m)), "real_mean": float(np.nanmean(rr)),
                   "frac_equal_1pct": float(np.mean(np.abs(m[ok] - rr[ok]) / rr[ok] < 0.01)) if ok.any() else None,
                   "median_mix_over_real": float(np.median(m[ok] / rr[ok])) if ok.any() else None}
    pa[d["seed"]] = {"life": life["name"], "buckets": row}
    print("premise a seed %d (%s): %s" % (d["seed"], life["name"], "; ".join(
        "k%d n%d mix %.2e real %.2e eq %s ratio %s" % (kk, v["n"], v["mix_mean"], v["real_mean"],
                                                         fmt(v["frac_equal_1pct"], 2), fmt(v["median_mix_over_real"], 3))
        for kk, v in row.items())))
SUM["premise_a"] = pa

# ------------------------------------------------------------------ C0: separation
print("\n== C0 separation (K=%d): A_change / A_null / D  [sep]" % K)
C0 = {}
for d in seeds:
    for stg in ("S1", "S2"):
        if stg not in d["stages"]:
            continue
        L = d["stages"][stg]["lives"]
        for pol in ("RND", "FS", "NAT", "FC", "CP", "OWN"):
            nu = L.get(pol + "-none")
            for kind in ("perm", "layout"):
                ch = L.get("%s-%s" % (pol, kind))
                if ch is None or nu is None:
                    continue
                row = {}
                for sig in ("RAW_MIX", "EMA_MIX", "RAW_REAL", "EMA_REAL"):
                    row[sig] = sep(ch, nu, sig, tc, K)
                    row[sig]["hitfa"] = hit_fa(ch, sig, tc, K)
                C0.setdefault(stg, {}).setdefault("%s-%s" % (pol, kind), {})[d["seed"]] = row
                print("%s %-10s s%d  " % (stg, pol + "-" + kind, d["seed"]) + "  ".join(
                    "%s %s/%s/%s%s(p%s)" % (sig, fmt(v["A"], 2), fmt(v["A_null"], 2), fmt(v["D"], 2), "*" if v["sep"] else " ", fmt(v["A_pair"], 2))
                    for sig, v in row.items()))
SUM["C0"] = C0


def input_sep(row, which):
    sigs = ("RAW_MIX", "EMA_MIX") if which == "mix" else ("RAW_REAL", "EMA_REAL")
    return any(row[s]["sep"] for s in sigs)


def tally(stg, cell, which):
    rows = C0.get(stg, {}).get(cell, {})
    return sum(input_sep(r, which) for r in rows.values()), len(rows)


verd = {}
PRIMARY = "RND-perm"
mix_n, n = tally("S1", PRIMARY, "mix")
real_n, _ = tally("S1", PRIMARY, "real")
mix_ok, real_ok = mix_n >= 4, real_n >= 4
if real_ok and not mix_ok:
    verd["C0"] = "SEPARATES-realised-only"
elif real_ok and mix_ok:
    verd["C0"] = "both"
elif mix_ok and not real_ok:
    verd["C0"] = "mixed-only"
else:
    verd["C0"] = "neither=H-SV"
verd["C0_tally"] = {"RND-perm S1 mix": [mix_n, n], "RND-perm S1 real": [real_n, n]}
for cell in ("FS-perm", "NAT-perm", "FC-perm", "CP-perm", "OWN-perm", "FS-layout", "NAT-layout"):
    verd["C0_tally"]["%s S1 mix" % cell] = list(tally("S1", cell, "mix"))
    verd["C0_tally"]["%s S1 real" % cell] = list(tally("S1", cell, "real"))
for cell in ("RND-perm", "NAT-perm"):
    verd["C0_tally"]["%s S2 mix" % cell] = list(tally("S2", cell, "mix"))
    verd["C0_tally"]["%s S2 real" % cell] = list(tally("S2", cell, "real"))
print("\nC0 verdict: %s  %s" % (verd["C0"], verd["C0_tally"]))

# ------------------------------------------------------------------ C1: operating point (offline, FS lives, EMA form)
C1 = {"input": None}
if verd["C0"] != "neither=H-SV":
    inp = "EMA_REAL" if real_ok else "EMA_MIX"
    C1["input"] = inp
    tun = seeds[:2]
    CELL = PRIMARY
    C1["cell"] = CELL
    pooled = np.concatenate([signals(d["stages"]["S1"]["lives"][CELL])[inp][
        windows(len(d["stages"]["S1"]["lives"][CELL]["rec"]["rv"]), tc, K)[0]] for d in tun])
    pooled = pooled[np.isfinite(pooled)]
    grid = [float(np.quantile(pooled, q)) for q in GRID_Q]
    best = None
    for gq, b in zip(GRID_Q, grid):
        aps = []
        for d in tun:
            life = d["stages"]["S1"]["lives"][CELL]; x = signals(life)[inp]
            aps.append(appropriateness(life, uncommitted(x, np.full(len(x), b)), tc, K)["approp"])
        m = float(np.mean(aps))
        if best is None or m > best[2] + 1e-12 or (abs(m - best[2]) <= 1e-12 and b > best[1]):
            best = (gq, b, m, aps)
    C1["fixed_tuned"] = {"grid_q": GRID_Q, "grid": grid, "chosen_q": best[0], "bar": best[1], "A_tune": best[2], "A_tune_per_seed": best[3]}
    A_tune = best[2]
    print("\n== C1 (input %s, RND lives, K=%d) FIXED-TUNED bar %.4g (pooled pre q%.3f) A_tune %.3f" % (inp, K, best[1], best[0], A_tune))
    rng = np.random.default_rng(12345)
    rows = {}
    for i, d in enumerate(seeds):
        for stg in ("S1", "S2"):
            if stg not in d["stages"] or CELL not in d["stages"][stg]["lives"]:
                continue
            L = d["stages"][stg]["lives"]; ch = L[CELL]; nu = L.get(CELL.replace("perm", "none"))
            x = signals(ch)[inp]; n = len(x)
            r = {}
            r["ABS"] = appropriateness(ch, uncommitted(x, np.full(n, 0.40)), tc, K)
            r["FIXED"] = appropriateness(ch, uncommitted(x, np.full(n, best[1])), tc, K)
            ob = own_bars(x)
            u_own = uncommitted(x, ob)
            r["OWN"] = appropriateness(ch, u_own, tc, K)
            perm = rng.permutation(n)
            xs = x[perm]
            r["SHUF"] = appropriateness(ch, uncommitted(xs, own_bars(xs)), tc, K)
            r["SHUFBAR"] = appropriateness(ch, uncommitted(x, own_bars(xs)), tc, K)
            occ = r["OWN"]["occupancy"]
            v = valid_mask(ch, n); pre, post = windows(n, tc, K)
            rand = []
            for _ in range(N_RAND):
                u = rng.random(n) >= occ
                rand.append(u[post & v].mean() - u[pre & v].mean())
            r["RAND_p95"] = float(np.quantile(rand, 0.95)); r["RAND_mean"] = float(np.mean(rand))
            r["ORACLE"] = 1.0
            if nu is not None:
                xn = signals(nu)[inp]
                r["FIXED_null_p_unc_post"] = appropriateness(nu, uncommitted(xn, np.full(len(xn), best[1])), tc, K)["p_unc_post"]
                r["OWN_null_p_unc_post"] = appropriateness(nu, uncommitted(xn, own_bars(xn)), tc, K)["p_unc_post"]
            role = "tune" if i < 2 else "heldout"
            rows.setdefault(stg, {})[d["seed"]] = dict(r, role=role)
            print("%s s%d %-7s ABS %s | FIXED A %s fd %s occ %s | OWN A %s fd %s occ %s | SHUF %s SHUFBAR %s RANDp95 %s" % (
                stg, d["seed"], role, fmt(r["ABS"]["approp"]), fmt(r["FIXED"]["approp"]), fmt(r["FIXED"]["false_decommit_pre"]),
                fmt(r["FIXED"]["occupancy"]), fmt(r["OWN"]["approp"]), fmt(r["OWN"]["false_decommit_pre"]),
                fmt(r["OWN"]["occupancy"]), fmt(r["SHUF"]["approp"]), fmt(r["SHUFBAR"]["approp"]), fmt(r["RAND_p95"])))
    C1["rows"] = rows
    crit = max(0.2, 0.5 * A_tune)

    def set_eval(stg, role=None):
        rs = [r for s, r in rows.get(stg, {}).items() if role is None or r["role"] == role]
        if not rs:
            return None
        need = math.ceil(2 * len(rs) / 3)
        fk = sum(r["FIXED"]["approp"] >= crit for r in rs)
        ok = sum(r["OWN"]["approp"] >= crit for r in rs)
        ob = sum((r["OWN"]["approp"] > r["SHUF"]["approp"] + SHUF_MARGIN) and (r["OWN"]["approp"] > r["RAND_p95"]) for r in rs)
        return {"n": len(rs), "need": need, "fixed_keeps": fk >= need, "own_keeps": ok >= need, "own_beats_controls": ob >= need,
                "counts": [fk, ok, ob]}
    sets = {"HO-S1": set_eval("S1", "heldout"), "S2": set_eval("S2")}
    C1["sets"] = sets; C1["crit"] = crit
    if A_tune < 0.2:
        v1 = "CANNOT_DETERMINE (no fixed bar reaches appropriateness 0.2 even in-sample)"
    else:
        sup = [k for k, s in sets.items() if s and (not s["fixed_keeps"]) and s["own_keeps"] and s["own_beats_controls"]]
        present = [k for k, s in sets.items() if s]
        if sup:
            v1 = "H1 SUPPORTED (%s)" % ",".join(sup)
        elif present and all(sets[k]["fixed_keeps"] for k in present):
            v1 = "H1 WEAKENED (%s)" % ",".join(present)
        elif present and not any(sets[k]["own_beats_controls"] for k in present):
            v1 = "CONTENT-BLIND"
        else:
            v1 = "CANNOT_DETERMINE (mixed)"
    verd["C1"] = v1
    print("C1 sets (crit %.3f): %s\nC1 verdict: %s" % (crit, sets, v1))
else:
    verd["C1"] = "CANNOT_DETERMINE (C0 stop: H-SV)"
SUM["C1"] = C1

# ------------------------------------------------------------------ C2: escape evidence (S1, perm, K2)
print("\n== C2 (S1, perm, K2=%d): RAW_REAL A/A_null/D per clamp; CP probe-tick detection" % K2)
C2 = {}
for d in seeds:
    L = dict(d["stages"]["S1"]["lives"])
    r = {}
    # FC == NAT when the native gate is committed on every tick (verified): NAT stands in for FC
    if "FC-perm" not in L and "NAT-perm" in L:
        natc = min(float(np.mean(L["NAT-perm"]["rec"]["committed"])), float(np.mean(L["NAT-none"]["rec"]["committed"])))
        r["FC_from_NAT"] = natc
        if natc == 1.0:
            L["FC-perm"] = L["NAT-perm"]; L["FC-none"] = L["NAT-none"]
    for pol in ("RND", "NAT", "FC", "FS", "CP", "OWN"):
        if pol + "-perm" in L and pol + "-none" in L:
            r[pol] = sep(L[pol + "-perm"], L[pol + "-none"], "RAW_REAL", tc, K2)
            r[pol + "_mix"] = sep(L[pol + "-perm"], L[pol + "-none"], "RAW_MIX", tc, K2)
            ch = L[pol + "-perm"]; n = len(ch["rec"]["act"]); pre, post = windows(n, tc, K2)
            acts = np.array(ch["rec"]["act"])
            r[pol + "_entropy"] = {"pre": entropy_bits(acts[pre]), "post": entropy_bits(acts[post])}
            r[pol + "_commit_occ"] = float(np.mean(ch["rec"]["committed"]))
    if "CP-perm" in L:
        pr = np.array(L["CP-perm"]["rec"]["probe"], bool)
        ev_ticks = np.zeros(len(pr), bool); ev_ticks[1:] = pr[:-1]
        r["CP_probe"] = sep(L["CP-perm"], L["CP-none"], "RAW_REAL", tc, K2, sel=ev_ticks)
        pre, post = windows(len(pr), tc, K2)
        r["CP_probe"]["n_pre"] = int((ev_ticks & pre).sum()); r["CP_probe"]["n_post"] = int((ev_ticks & post).sum())
        r["CP_probe_rate"] = float(pr.mean())
        sel = np.array(L["CP-perm"]["rec"]["sel"]); act = np.array(L["CP-perm"]["rec"]["act"])
        r["CP_exec_differs"] = float(np.mean(sel != act))
        # FC evidence on the SAME tick positions (is it the probe or the position?)
        r["FC_at_probe_ticks"] = sep(L["FC-perm"], L["FC-none"], "RAW_REAL", tc, K2, sel=ev_ticks) if "FC-perm" in L else {"A": float("nan"), "A_null": float("nan"), "D": float("nan"), "sep": False}
    C2[d["seed"]] = r
    print("s%d " % d["seed"] + " | ".join("%s %s/%s/%s%s H %s>%s" % (
        pol, fmt(r[pol]["A"], 2), fmt(r[pol]["A_null"], 2), fmt(r[pol]["D"], 2), "*" if r[pol]["sep"] else " ",
        fmt(r[pol + "_entropy"]["pre"], 2), fmt(r[pol + "_entropy"]["post"], 2)) for pol in ("RND", "NAT", "FC", "FS", "CP", "OWN") if pol in r)
        + (" || CPprobe %s/%s/%s%s n%d/%d | FC@probe %s/%s/%s" % (
            fmt(r["CP_probe"]["A"], 2), fmt(r["CP_probe"]["A_null"], 2), fmt(r["CP_probe"]["D"], 2), "*" if r["CP_probe"]["sep"] else " ",
            r["CP_probe"]["n_pre"], r["CP_probe"]["n_post"], fmt(r["FC_at_probe_ticks"]["A"], 2),
            fmt(r["FC_at_probe_ticks"]["A_null"], 2), fmt(r["FC_at_probe_ticks"]["D"], 2)) if "CP_probe" in r else ""))
# pooled cross-seed probe-tick test (report only): per seed, divide RAW_REAL by the median of that
# life's pre-window probe-evidence ticks, then pool post vs pre across seeds.
pool = {"perm": [[], []], "none": [[], []]}
for d in seeds:
    L = d["stages"]["S1"]["lives"]
    if "CP-perm" not in L:
        continue
    pr = np.array(L["CP-perm"]["rec"]["probe"], bool); evt = np.zeros(len(pr), bool); evt[1:] = pr[:-1]
    for kind in ("perm", "none"):
        life = L["CP-" + kind]; x = signals(life)["RAW_REAL"]; n = len(x); v = valid_mask(life, n) & evt[:n]
        pre, post = windows(n, tc, K2)
        base = x[pre & v]; base = base[np.isfinite(base)]
        if len(base) == 0:
            continue
        m = np.median(base)
        pool[kind][0].extend((x[post & v] / m).tolist()); pool[kind][1].extend((x[pre & v] / m).tolist())
C2["_pooled_probe"] = {k: {"A": auroc(np.array(v[0]), np.array(v[1])), "n_post": len(v[0]), "n_pre": len(v[1])} for k, v in pool.items()}
print("pooled CP probe-tick AUROC: %s" % C2["_pooled_probe"])
SUM["C2"] = C2
ns = len([s for s in C2 if s != "_pooled_probe"])
need4 = max(1, math.ceil(0.8 * ns)); need3 = max(1, math.ceil(0.6 * ns))
fs_sep = sum(C2[s]["FS"]["sep"] for s in C2 if s != "_pooled_probe" and "FS" in C2[s])
rnd_sep = sum(C2[s]["RND"]["sep"] for s in C2 if s != "_pooled_probe" and "RND" in C2[s])
X = "FS" if fs_sep >= need4 else "RND"
x_sep = fs_sep if X == "FS" else rnd_sep
fc_sep = sum(C2[s]["FC"]["sep"] for s in C2 if s != "_pooled_probe" and "FC" in C2[s])
fc_close = sum((C2[s]["FC"]["D"] >= C2[s][X]["D"] - 0.10) for s in C2 if s != "_pooled_probe" and "FC" in C2[s] and X in C2[s])
cp_sep = sum(C2[s]["CP_probe"]["sep"] for s in C2 if s != "_pooled_probe" and "CP_probe" in C2[s])
if any("FC" not in C2[s] for s in C2 if s != "_pooled_probe"):
    v2 = "CANNOT_DETERMINE (no forced-committed arm: native gate not committed on every tick and FC not run)"
elif x_sep < need4:
    v2 = "CANNOT_DETERMINE (neither forced sampling nor scripted-random actions separate the change at K2 on >=4/5 seeds: no evidence even when exploring)"
elif fc_sep >= need4 and fc_close >= need4:
    v2 = "H2 NOT-NEEDED"
elif (ns - fc_sep) >= need4 and cp_sep >= need3:
    v2 = "H2 SUPPORTED"
else:
    v2 = "CANNOT_DETERMINE (mixed)"
verd["C2"] = v2
verd["C2_tally"] = {"exposure_ref": X, "RND_sep": [rnd_sep, ns], "FS_sep": [fs_sep, ns], "FC_sep": [fc_sep, ns], "FC_close_to_FS": [fc_close, ns], "CP_probe_sep": [cp_sep, ns]}
print("C2 verdict: %s %s" % (v2, verd["C2_tally"]))
SUM["verdicts"] = verd
json.dump(SUM, open(OUT, "w"), indent=1, default=lambda o: None)
print("\nVERDICTS: %s" % json.dumps({k: v for k, v in verd.items() if not k.endswith("tally")}))
