"""Pool ceacal_analyze.py outputs across seeds (bt0925-ceacal). usage: python ceacal_pool.py <results_dir> <passes> <seed...>"""
import json, sys
from statistics import NormalDist
rd = sys.argv[1]; passes = int(sys.argv[2]); seeds = [int(s) for s in sys.argv[3:]]
D = [json.load(open("%s/ana_%d_p%d.json" % (rd, s, passes))) for s in seeds]
def zq(p): return NormalDist().inv_cdf(min(max(p, 1e-9), 1 - 1e-9))
rows = []
for reg in ("A", "B", "raw", "hexp_posthoc"):
    if reg not in D[0]["gates"]: continue
    for v in ("i_fixed", "ii_zscore", "iii_rate", "iv_ratio"):
        h = sum(d["gates"][reg][v]["pre"]["hits"] for d in D); no = sum(d["gates"][reg][v]["pre"]["n_onsets"] for d in D)
        fa = sum(d["gates"][reg][v]["pre"]["fa"] for d in D); npl = sum(d["gates"][reg][v]["pre"]["n_pool"] for d in D)
        H = (h + 0.5) / (no + 1); F = (fa + 0.5) / (npl + 1); Fw = 1 - (1 - F) ** 6
        per = [d["gates"][reg][v]["pre"]["dprime"] for d in D]
        sw = [d["gates"][reg][v]["sweep_posthoc"]["dprime"] if d["gates"][reg][v]["sweep_posthoc"] else None for d in D]
        rows.append(dict(regime=reg, variant=v, hits=h, onsets=no, fa=fa, pool=npl, H=round(h / max(1, no), 3),
                         F=round(fa / max(1, npl), 4), dprime_pooled=round(zq(H) - zq(Fw), 3), dprime_per_seed=per,
                         sweep_dprime_per_seed=sw))
for r in rows:
    print("%-4s %-10s H=%5.3f (%d/%d) F=%6.4f (%d/%d) d'pooled=%6.3f per-seed=%s sweep=%s" % (
        r["regime"], r["variant"], r["H"], r["hits"], r["onsets"], r["F"], r["fa"], r["pool"], r["dprime_pooled"], r["dprime_per_seed"], r["sweep_dprime_per_seed"]))
json.dump(rows, open("%s/pooled_p%d.json" % (rd, passes), "w"), indent=1)
