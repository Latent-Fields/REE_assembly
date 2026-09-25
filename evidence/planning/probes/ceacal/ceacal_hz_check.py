"""POST-HOC input check (bt0925-ceacal): does the PRE-EMA env scalar hazard_at_agent (the value harm_obs_a EMAs,
causal_grid_world.py:3035-3037) itself separate hazard-adjacent from non-adjacent steps? usage: python ceacal_hz_check.py <results_dir>"""
import sys, json, torch, numpy as np
rd = sys.argv[1]; out = {}
for s in (11, 12, 13):
    E = torch.load("%s/rec_%d_EVAL.pt" % (rd, s), weights_only=False)
    HZ = E["HZ"].numpy(); DM = E["DM"].numpy(); X = E["X"][:, 0].numpy(); sc = np.arange(100, len(DM))
    adj = DM[sc] <= 1; far = DM[sc] >= 2
    out[s] = dict(hz_adj_mean=round(float(HZ[sc][adj].mean()), 3), hz_far_mean=round(float(HZ[sc][far].mean()), 3),
                  hz_far_frac_ge_0p99=round(float((HZ[sc][far] >= 0.99).mean()), 3), hz_adj_frac_ge_0p99=round(float((HZ[sc][adj] >= 0.99).mean()), 3),
                  hz_far_min=round(float(HZ[sc][far].min()), 3),
                  x_adj_mean=round(float(X[sc][adj].mean()), 3), x_far_mean=round(float(X[sc][far].mean()), 3),
                  corr_hz_dmin=round(float(np.corrcoef(HZ[sc], DM[sc])[0, 1]), 3))
print(json.dumps(out))
