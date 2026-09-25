"""Pool ceacal2_analyze.py outputs across seeds (bt0925-ceacal2). usage: python ceacal2_pool.py <results_dir> <config_name> <seed...>"""
import json, sys
from statistics import NormalDist
rd = sys.argv[1]; cfgname = sys.argv[2]; seeds = [int(s) for s in sys.argv[3:]]
D = [json.load(open("%s/ana2_%s_%d.json" % (rd, cfgname, s))) for s in seeds]
def zq(p): return NormalDist().inv_cdf(min(max(p, 1e-9), 1 - 1e-9))
rows = []
for stream in ("z_harm_a", "z_harm_s", "preema_hz", "fastema", "raw_a"):
    for v in ("i_fixed", "ii_zscore", "iii_rate", "iv_ratio"):
        h = sum(d["gates"][stream][v]["pre"]["hits"] for d in D); no = sum(d["gates"][stream][v]["pre"]["n_onsets"] for d in D)
        fa = sum(d["gates"][stream][v]["pre"]["fa"] for d in D); npl = sum(d["gates"][stream][v]["pre"]["n_pool"] for d in D)
        H = (h + 0.5) / (no + 1); F = (fa + 0.5) / (npl + 1); Fw = 1 - (1 - F) ** 6
        per = [d["gates"][stream][v]["pre"]["dprime"] for d in D]
        sw = [d["gates"][stream][v]["sweep_posthoc"]["dprime"] if d["gates"][stream][v]["sweep_posthoc"] else None for d in D]
        h10 = sum(d["gates"][stream][v]["pre_n10"]["hits"] for d in D)
        fa10 = sum(d["gates"][stream][v]["pre_n10"]["fa"] for d in D); npl10 = sum(d["gates"][stream][v]["pre_n10"]["n_pool"] for d in D)
        H10 = (h10 + 0.5) / (no + 1); F10 = (fa10 + 0.5) / (npl10 + 1); Fw10 = 1 - (1 - F10) ** 11
        rows.append(dict(config=cfgname, stream=stream, variant=v, hits=h, onsets=no, fa=fa, pool=npl,
                         H=round(h / max(1, no), 3), F=round(fa / max(1, npl), 4),
                         dprime_pooled=round(zq(H) - zq(Fw), 3), dprime_per_seed=per, sweep_dprime_per_seed=sw,
                         dprime_pooled_n10=round(zq(H10) - zq(Fw10), 3), H_n10=round(h10 / max(1, no), 3)))
for r in rows:
    print("%-6s %-10s %-10s H=%5.3f (%d/%d) F=%6.4f (%d/%d) d'pooled=%6.3f per-seed=%s sweep=%s" % (
        r["config"], r["stream"], r["variant"], r["H"], r["hits"], r["onsets"], r["F"], r["fa"], r["pool"], r["dprime_pooled"], r["dprime_per_seed"], r["sweep_dprime_per_seed"]))
json.dump(rows, open("%s/pooled2_%s.json" % (rd, cfgname), "w"), indent=1)
