"""Offline (open-loop) feasibility analysis of VF_s*.json for the grounded valuation candidates.

For each arm: E3 tick rates, committed fraction, softmax flatness, grounded event rates (G-all,
G-contact |r|>0.1), channel spreads and votes at the chosen candidate, and per-candidate
evidence-accumulation estimates (M1 sign rule, M2 vote regression, M3 eligibility), computed
on the RECORDED stream without feeding weights back (D1: does the signal exist / is it
attributable; not whether the closed loop would converge). ASCII-only output.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
CH = ["F", "harm", "residue", "benefit", "goal"]
WKEY = ["f_weight", "lambda_ethical", "rho_residue", "benefit_weight", "goal_weight"]
SIGN = np.array([1, 1, 1, -1, -1], float)
CONTACT_THR = 0.1


def arm_stats(arm):
    rew = np.asarray(arm["rewards"]); n = len(rew)
    ticks = [t for t in arm["ticks"] if len(t["terms"]) >= 2]
    w = np.array([arm["weights"][k] for k in WKEY])
    wsafe = np.where(w > 0, w, 1.0)
    steps = [t["step"] for t in ticks]
    out = {"n_steps": n, "n_select_calls": len(arm["ticks"]), "n_ticks_multi": len(ticks),
           "committed_frac": float(np.mean([t["committed"] for t in ticks])) if ticks else None,
           "K_mean": float(np.mean([len(t["terms"]) for t in ticks])) if ticks else None,
           "nonzero_r_steps": int((rew != 0).sum()), "contact_steps": int((np.abs(rew) > CONTACT_THR).sum()),
           "contact_neg": int((rew < -CONTACT_THR).sum()), "contact_pos": int((rew > CONTACT_THR).sum())}
    # softmax flatness on uncommitted ticks
    ent, pmax, gapn = [], [], []
    rows = []
    for i, t in enumerate(ticks):
        sc = np.asarray(t["scores"]); p = np.exp(-(sc - sc.min())); p /= p.sum()
        if not t["committed"]:
            ent.append(float(-(p * np.log(p + 1e-30)).sum() / np.log(len(p)))); pmax.append(float(p.max()))
        X = np.asarray(t["terms"]) / wsafe  # raw channel terms [K, 5]
        k = t["sel"]
        if k >= X.shape[0]:
            continue
        others = np.delete(X, k, axis=0)
        v = -SIGN * (X[k] - others.mean(0))
        sd = (np.asarray(t["terms"])).std(0)  # weighted spread
        s0 = t["step"]; s1 = steps[i + 1] if i + 1 < len(ticks) else n
        Rall = float(rew[s0:s1].sum()); rc = rew[s0:s1]
        Rcon = float(rc[np.abs(rc) > CONTACT_THR].sum())
        rows.append((t["committed"], v, sd, Rall, Rcon, s0, s1))
    out["uncommitted_softmax_norm_entropy_mean"] = float(np.mean(ent)) if ent else None
    out["uncommitted_softmax_pmax_mean"] = float(np.mean(pmax)) if pmax else None
    if not rows:
        return out, rows
    V = np.array([r[1] for r in rows]); SD = np.array([r[2] for r in rows])
    C = np.array([r[0] for r in rows]); RA = np.array([r[3] for r in rows]); RC = np.array([r[4] for r in rows])
    out["window_steps_mean"] = float(np.mean([r[6] - r[5] for r in rows]))
    out["weighted_spread_mean"] = dict(zip(CH, SD.mean(0).round(6).tolist()))
    out["vote_abs_mean"] = dict(zip(CH, np.abs(V).mean(0).round(6).tolist()))
    for tag, R in (("Gall", RA), ("Gcontact", RC)):
        m = C & (R != 0)
        out["ticks_committed_with_R_%s" % tag] = int(m.sum())
        out["ticks_all_with_R_%s" % tag] = int((R != 0).sum())
        res = {}
        # M1 sign rule increments on committed ticks with R != 0 (median-gated)
        if m.sum() >= 3:
            med = np.median(np.abs(V[C]), axis=0)
            U = np.sign(R[m])[:, None] * np.sign(V[m]) * (np.abs(V[m]) > med)
            mu = U.mean(0); sg = U.std(0) + 1e-12
            res["M1_mean_drift_per_event"] = dict(zip(CH, mu.round(3).tolist()))
            res["M1_events_for_2sd"] = dict(zip(CH, np.round(4 * sg ** 2 / np.maximum(mu ** 2, 1e-9), 0).tolist()))
        # M2 vote regression on committed ticks (all, incl zero R), per-channel simple regression t
        mc = C
        if mc.sum() >= 8:
            tt = {}
            for j, c in enumerate(CH):
                x = V[mc, j]; y = R[mc]
                if x.std() < 1e-12:
                    tt[c] = None; continue
                xc = x - x.mean(); b = (xc * (y - y.mean())).sum() / (xc ** 2).sum()
                resid = y - y.mean() - b * xc
                se = np.sqrt((resid ** 2).sum() / max(len(x) - 2, 1) / (xc ** 2).sum())
                tv = b / se if se > 0 else 0.0
                tt[c] = {"beta": float(b), "t": float(tv), "n": int(len(x)),
                         "n_for_t2": float(len(x) * (2.0 / tv) ** 2) if abs(tv) > 1e-6 else None}
            res["M2_vote_regression"] = tt
        out[tag] = res
    return out, rows


def m3_open_loop(arm, eta=0.01, lam=0.9, beta=0.05, contact=False):
    """ARC-108 constants, grounded delta, main channels, committed-tick injection; open loop."""
    rew = np.asarray(arm["rewards"]); w = np.array([arm["weights"][k] for k in WKEY]); w = np.where(w > 0, w, 1.0)
    inj = {}
    for t in arm["ticks"]:
        if len(t["terms"]) < 2 or not t["committed"] or t["sel"] >= len(t["terms"]):
            continue
        X = np.asarray(t["terms"]) / w; k = t["sel"]
        inj[t["step"]] = -SIGN * (X[k] - np.delete(X, k, axis=0).mean(0))
    e = np.zeros(5); Vh = 0.0; th = np.zeros(5); incs = []
    for s, r in enumerate(rew):
        if contact and abs(r) <= CONTACT_THR:
            r = 0.0
        e = lam * e + inj.get(s, 0.0)
        d = r - Vh; Vh += beta * (r - Vh)
        inc = eta * d * e * (1.0 if d > 0 else 0.5)
        th += inc; incs.append(inc)
    incs = np.asarray(incs)
    return {"theta_end": dict(zip(CH, th.round(5).tolist())),
            "per_step_inc_sd": dict(zip(CH, incs.std(0).round(6).tolist())),
            "z_end": dict(zip(CH, (th / (incs.std(0) * np.sqrt(len(incs)) + 1e-12)).round(2).tolist()))}


def main():
    seeds = [int(x) for x in sys.argv[1:]] or [43, 44, 42]
    allout = {}
    for s in seeds:
        p = HERE / "results" / ("VF_s%d.json" % s)
        if not p.exists():
            print("missing", p); continue
        d = json.load(open(p))
        allout[s] = {"gate_n": d["gate_n"], "reward_by_ttype": d["reward_by_ttype"], "arms": {}}
        for name, arm in d["arms"].items():
            st, _ = arm_stats(arm)
            st["summary"] = arm["summary"]
            st["M3_Gall"] = m3_open_loop(arm); st["M3_Gcontact"] = m3_open_loop(arm, contact=True)
            allout[s]["arms"][name] = st
    json.dump(allout, open(HERE / "results" / "VF_analysis.json", "w"), indent=1)
    for s, d in allout.items():
        print("=== seed %d gate_n=%d" % (s, d["gate_n"]))
        print(" reward by ttype:", json.dumps({k: [v["n"], round(v["min"], 3), round(v["max"], 3)] for k, v in d["reward_by_ttype"].items()}))
        for name, st in d["arms"].items():
            print(" --", name, json.dumps(st["summary"]))
            for k in ("n_select_calls", "n_ticks_multi", "committed_frac", "K_mean", "window_steps_mean", "nonzero_r_steps",
                      "contact_neg", "contact_pos", "uncommitted_softmax_norm_entropy_mean", "uncommitted_softmax_pmax_mean",
                      "ticks_committed_with_R_Gall", "ticks_committed_with_R_Gcontact", "ticks_all_with_R_Gcontact"):
                print("   %s: %s" % (k, st.get(k)))
            print("   spread:", st.get("weighted_spread_mean"))
            print("   |vote|:", st.get("vote_abs_mean"))
            for tag in ("Gall", "Gcontact"):
                r = st.get(tag, {})
                if "M1_mean_drift_per_event" in r:
                    print("   M1 %s drift/event %s ; events_for_2sd %s" % (tag, r["M1_mean_drift_per_event"], r["M1_events_for_2sd"]))
                if "M2_vote_regression" in r:
                    print("   M2 %s t: %s" % (tag, {c: (None if v is None else (round(v["t"], 2), None if v["n_for_t2"] is None else round(v["n_for_t2"]))) for c, v in r["M2_vote_regression"].items()}))
            print("   M3 Gall z_end %s ; Gcontact z_end %s" % (st["M3_Gall"]["z_end"], st["M3_Gcontact"]["z_end"]))
            print("   M3 Gall theta_end %s" % st["M3_Gall"]["theta_end"])


if __name__ == "__main__":
    main()
