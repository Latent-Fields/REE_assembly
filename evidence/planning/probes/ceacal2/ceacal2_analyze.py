"""CeA onset-input re-probe, ANALYZE stage (bt0925-ceacal2). Offline; no env stepping.

usage: cd <ree-v3 worktree @ 2ea0e3c>; python ceacal2_analyze.py . <results_dir> <config_name> <seed>
Loads rec_<config_name>_<seed>.pt (ceacal2_record.py). Regime A (untrained) only this
round (see module docstring of the record script for why). Builds five candidate streams:
  z_harm_a   -- mean|z_harm_a|, agent's OWN encoder weights (instrument-checked vs SA)
  z_harm_s   -- mean|z_harm_s| on harm_obs[51] (SD-010 5x5 local view + resource view +
                harm_exposure), agent's OWN encoder weights (instrument-checked vs SS)
  preema_hz  -- raw hazard_at_agent (HZ), no encoder, no smoothing
  fastema    -- post-hoc EMA of HZ at alpha=0.3 (vs the deployed harm_obs_a_ema_alpha=0.05
                / safety_proximity_ema_alpha default 0.05; causal_grid_world.py:3049-3052
                is the same recurrence at the default alpha), init 0.0 per env convention
                (causal_grid_world.py:1615)
  raw_a      -- X[:,0], the post-(default-alpha)-EMA harm_obs_a scalar (probe1's control v)
Scores gate variants (i)-(iv) from cea_gate_calibration_probe_20260925.md on each stream,
same ground truth / readout / pool definitions as that probe's Amendment 1.
Prints one JSON line (ASCII) and writes <results_dir>/ana2_<config_name>_<seed>.json.
"""
import json, sys, math
root = sys.argv[1]; sys.path.insert(0, root)
rd = sys.argv[2]; cfgname = sys.argv[3]; seed = int(sys.argv[4])
import torch, numpy as np
torch.set_num_threads(1)
from ree_core.latent.stack import AffectiveHarmEncoder, HarmEncoder
N_WIN = 5; N_WIN2 = 10; BURN = 100; WARM = 20; FAST_ALPHA = 0.3

E = torch.load("%s/rec_%s_%d.pt" % (rd, cfgname, seed), weights_only=False)

encA = AffectiveHarmEncoder(harm_obs_a_dim=E["X"].shape[1], z_harm_a_dim=E["enc_state_a"]["encoder.2.weight"].shape[0], harm_history_len=E["H"].shape[1])
encA.load_state_dict(E["enc_state_a"])
encS = HarmEncoder(harm_obs_dim=E["HO"].shape[1], z_harm_dim=E["enc_state_s"]["encoder.2.weight"].shape[0])
encS.load_state_dict(E["enc_state_s"])

def s_of_a(X, H):
    with torch.no_grad():
        z, _ = encA(X, H)
    return z.abs().mean(-1).numpy().astype(np.float64)

def s_of_s(HO):
    with torch.no_grad():
        z = encS(HO)
    return z.abs().mean(-1).numpy().astype(np.float64)

sA = s_of_a(E["X"], E["H"])
sS = s_of_s(E["HO"])
SA = E["SA"].numpy(); SS = E["SS"].numpy()
ok_a = np.isfinite(SA); ok_s = np.isfinite(SS)
instr = dict(
    z_harm_a=dict(max_abs_diff=float(np.max(np.abs(sA[ok_a] - SA[ok_a]))), n=int(ok_a.sum())),
    z_harm_s=dict(max_abs_diff=float(np.max(np.abs(sS[ok_s] - SS[ok_s]))), n=int(ok_s.sum())),
)

HZ = E["HZ"].numpy().astype(np.float64)
fastema = np.zeros_like(HZ)
prev = 0.0
for t in range(len(HZ)):
    prev = (1.0 - FAST_ALPHA) * prev + FAST_ALPHA * HZ[t]
    fastema[t] = prev
xraw = E["X"][:, 0].numpy().astype(np.float64)

# ---------------- ground truth (Amendment 1 definition, same as probe1) ----------------
DM = E["DM"].numpy(); TT = E["TT"]; EP = E["EP"].numpy(); TE = E["TE"].numpy(); RD = E["RD"].numpy()
n = len(DM)
haz = np.array([(DM[t] <= 1) or (TT[t] == "env_caused_hazard") for t in range(n)])
onsets = []
for t in range(BURN, n):
    if haz[t] and TE[t] >= 3 and not haz[t - 1] and not haz[t - 2] and not haz[t - 3]:
        onsets.append(t)
inwin = np.zeros(n, bool); win_of = {}
for t0 in onsets:
    w = [t for t in range(t0, min(n, t0 + N_WIN + 1)) if EP[t] == EP[t0]]
    win_of[t0] = w
    inwin[w] = True
pool = np.array([(t >= BURN) and (not haz[t]) and (TE[t] >= 3) and (not inwin[t]) for t in range(n)])
sust = np.array([(t >= BURN) and haz[t] and (not inwin[t]) for t in range(n)])
res_adj = RD <= 1
# secondary N_WIN2=10 window (brief: "also N=10 as a secondary")
inwin2 = np.zeros(n, bool); win_of2 = {}
for t0 in onsets:
    w = [t for t in range(t0, min(n, t0 + N_WIN2 + 1)) if EP[t] == EP[t0]]
    win_of2[t0] = w
    inwin2[w] = True
pool2 = np.array([(t >= BURN) and (not haz[t]) and (TE[t] >= 3) and (not inwin2[t]) for t in range(n)])

def scores(s):
    z = np.full(n, -np.inf); d = np.full(n, -np.inf); r = np.full(n, -np.inf)
    mu = s[0]; var = 0.0; dv = 0.0; b = s[0]
    for t in range(n):
        if t >= WARM:
            sd = max(math.sqrt(var), 1e-3 * abs(mu) + 1e-8)
            z[t] = (s[t] - mu) / sd
            dd = s[t] - s[t - 1]
            sdd = max(math.sqrt(dv), 1e-8)
            d[t] = dd / sdd if dd > 0 else -np.inf
            r[t] = s[t] / b if b > 1e-12 else -np.inf
        delta = s[t] - mu
        mu = mu + 0.05 * delta
        var = (1 - 0.05) * (var + 0.05 * delta * delta)
        if t >= 1:
            dv = (1 - 0.05) * dv + 0.05 * (s[t] - s[t - 1]) ** 2
        b = (1 - 0.01) * b + 0.01 * s[t]
    return {"i_fixed": s.copy(), "ii_zscore": z, "iii_rate": d, "iv_ratio": r}
PRE_THR = {"i_fixed": 0.5, "ii_zscore": 2.0, "iii_rate": 2.0, "iv_ratio": 1.25}

def zq(p):
    from statistics import NormalDist
    return NormalDist().inv_cdf(min(max(p, 1e-9), 1 - 1e-9))

def readout(sc, thr, win_of_=win_of, pool_=pool, nwin=N_WIN):
    fire = sc > thr
    hits = sum(1 for t0 in onsets if fire[win_of_[t0]].any())
    lat = [next(t - t0 for t in win_of_[t0] if fire[t]) for t0 in onsets if fire[win_of_[t0]].any()]
    fa = int((fire & pool_).sum()); npool = int(pool_.sum())
    H = (hits + 0.5) / (len(onsets) + 1); F = (fa + 0.5) / (npool + 1)
    Fw = 1 - (1 - F) ** (nwin + 1)
    return dict(hits=hits, n_onsets=len(onsets), fa=fa, n_pool=npool,
                H_raw=round(hits / max(1, len(onsets)), 4), F_raw=round(fa / max(1, npool), 4),
                dprime=round(zq(H) - zq(Fw), 3),
                sustained_fire_rate=round(float((fire & sust).sum()) / max(1, int(sust.sum())), 4),
                median_latency=(float(np.median(lat)) if lat else None))

def readout2(sc, thr):
    return readout(sc, thr, win_of_=win_of2, pool_=pool2, nwin=N_WIN2)

def sweep(sc):
    fin = sc[np.isfinite(sc) & (np.arange(n) >= BURN)]
    if fin.size == 0:
        return None
    qs = np.unique(np.quantile(fin, np.linspace(0.5, 0.995, 40)))
    best = None
    for q in qs:
        ro = readout(sc, q)
        if best is None or ro["dprime"] > best[1]["dprime"]:
            best = (float(q), ro)
    return dict(thr=round(best[0], 5), **{k: best[1][k] for k in ("dprime", "H_raw", "F_raw", "hits", "fa")})

streams = dict(z_harm_a=sA, z_harm_s=sS, preema_hz=HZ, fastema=fastema, raw_a=xraw)
out = dict(config=cfgname, seed=seed, n_eval=n, n_onsets=len(onsets), n_pool=int(pool.sum()),
           n_sustained=int(sust.sum()), instrument_check=instr,
           hz_mean_scored=round(float(HZ[BURN:].mean()), 4), hz_min_scored=round(float(HZ[BURN:].min()), 4),
           fast_alpha=FAST_ALPHA)
for name, s in streams.items():
    ds = np.diff(s, prepend=s[0])
    out["corr_" + name + "_vs_dmin"] = round(float(np.corrcoef(s[BURN:], DM[BURN:])[0, 1]), 4)
    out["mean_ds_onset_" + name] = round(float(np.mean([ds[t] for t in onsets])) if onsets else float("nan"), 6)
    out["sd_ds_pool_" + name] = round(float(ds[pool].std()), 6)
res = {}
for name, s in streams.items():
    S = scores(s)
    res[name] = {v: dict(pre=readout(S[v], PRE_THR[v]), pre_n10=readout2(S[v], PRE_THR[v]),
                          sweep_posthoc=sweep(S[v])) for v in S}
out["gates"] = res
open("%s/ana2_%s_%d.json" % (rd, cfgname, seed), "w").write(json.dumps(out, indent=1))
brief = {r: {v: (res[r][v]["pre"]["H_raw"], res[r][v]["pre"]["F_raw"], res[r][v]["pre"]["dprime"],
                 res[r][v]["sweep_posthoc"]["dprime"] if res[r][v]["sweep_posthoc"] else None) for v in res[r]} for r in res}
print(json.dumps(dict(config=cfgname, seed=seed, instr=instr, n_onsets=len(onsets), n_pool=int(pool.sum()),
                      hz_scored=(out["hz_mean_scored"], out["hz_min_scored"]),
                      brief_H_F_dpre_dsweep=brief)))
