"""Post-hoc recompute of the DCH2 detector statistics from a cell's stored per-record z stream.
recs rows: [gstep, src, pe, ac, z, s, gw, C_on, C_bab, Cnr_on, Cnr_bab, sps_on, sps_bab]. ASCII only."""


def cp_alarms(recs, K=0.5, H=5.0, sources=("on", "bab")):
    C = {"on": 0.0, "bab": 0.0}
    out = []
    for r in recs:
        if len(r) < 5 or r[1] not in sources:
            continue
        q = r[1]
        C[q] = max(0.0, C[q] + r[4] - K)
        if C[q] > H:
            out.append(r[0]); C[q] = 0.0
    return out


def cp_score(recs, lo, hi, K=0.5, sources=("on", "bab")):
    """max rise of the never-reset per-source CUSUM inside [lo, hi), max over sources."""
    C = {"on": 0.0, "bab": 0.0}; start = {"on": None, "bab": None}; best = {"on": 0.0, "bab": 0.0}
    for r in recs:
        if len(r) < 5 or r[1] not in sources:
            continue
        q = r[1]
        if r[0] >= lo and start[q] is None:
            start[q] = C[q]
        C[q] = max(0.0, C[q] + r[4] - K)
        if lo <= r[0] < hi:
            best[q] = max(best[q], C[q] - start[q])
    return max(best.values())


def mag_alarms(recs, thr=0.75, alpha=0.05, alpha_g=0.05, g_low=0.1, g_thr=0.5):
    s = ar = 0.0; co = False; out = []
    for r in recs:
        if len(r) < 5:
            continue
        s += alpha * (r[4] - s)
        ar += alpha_g * (float(s > thr) - ar)
        c = s > thr and g_low + (1 - g_low) * ar > g_thr
        if c and not co:
            out.append(r[0])
        co = c
    return out


def mag_score(recs, lo, hi, alpha=0.05):
    s = 0.0; best = -1e9
    for r in recs:
        if len(r) < 5:
            continue
        s += alpha * (r[4] - s)
        if lo <= r[0] < hi:
            best = max(best, s)
    return best
