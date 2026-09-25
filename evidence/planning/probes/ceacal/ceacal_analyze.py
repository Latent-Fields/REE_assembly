"""CeA gate calibration probe, ANALYZE stage (bt0925-ceacal). Offline; no env stepping.

usage: cd <ree-v3 worktree @ aa14769>; python ceacal_analyze.py . <results_dir> <seed> [passes]
Loads rec_<seed>_EVAL.pt / rec_<seed>_TRAIN.pt (ceacal_record.py). Regime A = the EVAL agent's
encoder at init; regime B = a deep copy trained ONLINE (batch 1, time order, Adam lr 1e-3) on the
TRAIN trajectory with loss 0.1 x MSE(harm_accum_pred, harm_obs[-1]) == agent.compute_harm_accum_loss
at z_harm_a_aux_loss_weight=0.1 with the 935a native target. Scores the pre-registered gate variants
(i)-(iv) on s_t = mean|z_harm_a| and, as control (v), on the raw input x_t = harm_obs_a[0].
Prints one JSON line (ASCII) and writes <results_dir>/ana_<seed>_p<passes>.json.
"""
import json, sys, copy, math
root = sys.argv[1]; sys.path.insert(0, root)
rd = sys.argv[2]; seed = int(sys.argv[3]); passes = int(sys.argv[4]) if len(sys.argv) > 4 else 1
import torch, numpy as np
torch.set_num_threads(1)
from ree_core.latent.stack import AffectiveHarmEncoder
N_WIN = 5; BURN = 100; WARM = 20
E = torch.load("%s/rec_%d_EVAL.pt" % (rd, seed), weights_only=False)
T = torch.load("%s/rec_%d_TRAIN.pt" % (rd, seed), weights_only=False)
st = E["enc_state"]
zdim = st["encoder.2.weight"].shape[0]
encA = AffectiveHarmEncoder(harm_obs_a_dim=E["X"].shape[1], z_harm_a_dim=zdim, harm_history_len=E["H"].shape[1])
encA.load_state_dict(st)

def s_of(enc, X, H):
    with torch.no_grad():
        z, _ = enc(X, H)
    return z.abs().mean(-1).numpy().astype(np.float64)

# instrument check: my s_t (regime A) vs the agent's own CeA low_freq on the same obs
sA = s_of(encA, E["X"], E["H"])
SA = E["SA"].numpy()
ok = np.isfinite(SA)
instr = dict(max_abs_diff=float(np.max(np.abs(sA[ok] - SA[ok]))), n=int(ok.sum()))

# regime B: online training on TRAIN trajectory
encB = copy.deepcopy(encA)
opt = torch.optim.Adam(encB.parameters(), lr=1e-3)
XT, HT, YT = T["X"], T["H"], T["Y"].reshape(-1, 1)
ckpt = {}
eval_idx = torch.arange(BURN, E["X"].shape[0])
def scale_on_eval(enc):
    v = s_of(enc, E["X"][eval_idx], E["H"][eval_idx])
    return dict(mean=round(float(v.mean()), 4), max=round(float(v.max()), 4), min=round(float(v.min()), 4))
ckpt["0"] = scale_on_eval(encB)
losses = []
nT = XT.shape[0]
for p in range(passes):
    for i in range(nT):
        _, pred = encB(XT[i:i + 1], HT[i:i + 1])
        loss = 0.1 * torch.nn.functional.mse_loss(pred, YT[i:i + 1])
        opt.zero_grad(); loss.backward(); opt.step()
        losses.append(float(loss))
        k = p * nT + i + 1
        if k in (250, 500, 1000, 2000, 4000, 6000):
            ckpt[str(k)] = scale_on_eval(encB)
sB = s_of(encB, E["X"], E["H"])
xraw = E["X"][:, 0].numpy().astype(np.float64)
# POST-HOC exploratory control (vi), added after seed-11 results: harm_exposure (harm_obs[-1]),
# the faster nociceptive EMA that also enters the encoder via harm_history. NOT pre-registered.
hexp = E["Y"].numpy().astype(np.float64)

# ---------------- ground truth ----------------
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

# ---------------- gate scores (causal, online) ----------------
def scores(s):
    out = {"i_fixed": s.copy()}
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
        # update AFTER evaluation
        delta = s[t] - mu
        mu = mu + 0.05 * delta
        var = (1 - 0.05) * (var + 0.05 * delta * delta)
        if t >= 1:
            dv = (1 - 0.05) * dv + 0.05 * (s[t] - s[t - 1]) ** 2
        b = (1 - 0.01) * b + 0.01 * s[t]
    out["ii_zscore"] = z; out["iii_rate"] = d; out["iv_ratio"] = r
    return out
PRE_THR = {"i_fixed": 0.5, "ii_zscore": 2.0, "iii_rate": 2.0, "iv_ratio": 1.25}

def zq(p):
    from statistics import NormalDist
    return NormalDist().inv_cdf(min(max(p, 1e-9), 1 - 1e-9))

def readout(sc, thr):
    fire = sc > thr
    hits = sum(1 for t0 in onsets if fire[win_of[t0]].any())
    lat = [next(t - t0 for t in win_of[t0] if fire[t]) for t0 in onsets if fire[win_of[t0]].any()]
    fa = int((fire & pool).sum()); npool = int(pool.sum())
    H = (hits + 0.5) / (len(onsets) + 1); F = (fa + 0.5) / (npool + 1)
    Fw = 1 - (1 - F) ** (N_WIN + 1)
    fa_res = int((fire & pool & res_adj).sum()); n_res = int((pool & res_adj).sum())
    fa_oth = int((fire & pool & ~res_adj).sum()); n_oth = int((pool & ~res_adj).sum())
    return dict(hits=hits, n_onsets=len(onsets), fa=fa, n_pool=npool,
                H_raw=round(hits / max(1, len(onsets)), 4), F_raw=round(fa / max(1, npool), 4),
                dprime=round(zq(H) - zq(Fw), 3),
                sustained_fire_rate=round(float((fire & sust).sum()) / max(1, int(sust.sum())), 4),
                median_latency=(float(np.median(lat)) if lat else None),
                fa_rate_resource_adj=round(fa_res / max(1, n_res), 4), n_pool_resource_adj=n_res,
                fa_rate_other=round(fa_oth / max(1, n_oth), 4), n_pool_other=n_oth)

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

out = dict(seed=seed, passes=passes, zdim=int(zdim), instrument_check=instr,
           n_eval=n, n_onsets=len(onsets), n_pool=int(pool.sum()), n_sustained=int(sust.sum()),
           train_loss_first100=round(float(np.mean(losses[:100])), 6), train_loss_last100=round(float(np.mean(losses[-100:])), 6),
           scale_ckpt_B=ckpt, target_range=[round(float(YT.min()), 4), round(float(YT.max()), 4)])
# signal/ground-truth descriptives (scored steps only)
sc_idx = np.arange(BURN, n)
for name, s in (("A", sA), ("B", sB), ("raw", xraw), ("hexp_posthoc", hexp)):
    out["corr_s_vs_dmin_" + name] = round(float(np.corrcoef(s[sc_idx], DM[sc_idx])[0, 1]), 4)
    out["s_scored_" + name] = dict(mean=round(float(s[sc_idx].mean()), 4), min=round(float(s[sc_idx].min()), 4), max=round(float(s[sc_idx].max()), 4))
    # mean first-difference at onset vs pool
    ds = np.diff(s, prepend=s[0])
    out["mean_ds_onset_" + name] = round(float(np.mean([ds[t] for t in onsets])) if onsets else float("nan"), 6)
    out["mean_ds_pool_" + name] = round(float(ds[pool].mean()), 6)
    out["sd_ds_pool_" + name] = round(float(ds[pool].std()), 6)
res = {}
for name, s in (("A", sA), ("B", sB), ("raw", xraw), ("hexp_posthoc", hexp)):
    S = scores(s)
    res[name] = {v: dict(pre=readout(S[v], PRE_THR[v]), sweep_posthoc=sweep(S[v])) for v in S}
out["gates"] = res
open("%s/ana_%d_p%d.json" % (rd, seed, passes), "w").write(json.dumps(out, indent=1))
brief = {r: {v: (res[r][v]["pre"]["H_raw"], res[r][v]["pre"]["F_raw"], res[r][v]["pre"]["dprime"],
                 res[r][v]["sweep_posthoc"]["dprime"] if res[r][v]["sweep_posthoc"] else None) for v in res[r]} for r in res}
print(json.dumps(dict(seed=seed, passes=passes, instr=instr, n_onsets=len(onsets), n_pool=int(pool.sum()),
                      scaleB=ckpt, brief_H_F_dpre_dsweep=brief)))
