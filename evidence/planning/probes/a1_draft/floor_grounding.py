"""A1 pre-registration floor grounding (bt0925-a1prereg). Reads the SCRATCH-ONLY raw null-detector
JSONs (v1 s61-65 benign, v2 s66/s69 trapped; T2 regime, tie-break ON) and computes, per stratum, the
pooled SD of within-seed replicate deltas X(NULLj) - X(M0), j=0..4. NULLj share M0's env seed and
agent init and differ only by a matched-SD random walk in 4 channel weights, so these deltas are a
LOWER-BOUND analog of the NATIVE-vs-reseeded-NATIVE delta A1 calibrates on (reseeding also moves init).
Also the SCREEN log's between-seed distribution. ASCII-only output."""
import json, math, os, sys
B = sys.argv[1] if len(sys.argv) > 1 else "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924"  # raw JSONs are scratch-only
V1 = [B + "/nulldet/results/NULLDET_s%d.json" % s for s in (61, 62, 63, 64, 65)]
V2 = [B + "/nulldet2/results/NULLDET2_s%d.json" % s for s in (66, 69)]
CONTACT = {"agent_caused_hazard", "env_caused_hazard", "env_caused_multisource"}

def win_counts(tts, lo, hi):
    w = tts[lo:hi]; n = len(w)
    return {"contacts_per100": 100.0 * sum(t in CONTACT for t in w) / n,
            "consum_per100": 100.0 * sum(t == "resource" for t in w) / n,
            "prox_per100": 100.0 * sum(t in ("hazard_approach", "harm_gradient") for t in w) / n}

def metrics(arm):
    tts = arm["tts"]; T = len(tts)
    m = {"reward_all": arm["all"]["reward_per_100"], "reward_half2": arm["half2"]["reward_per_100"],
         "reward_half1": arm["half1"]["reward_per_100"]}
    m["reward_change_h1_h2"] = m["reward_half2"] - m["reward_half1"]
    last = win_counts(tts, T - 600, T); first = win_counts(tts, 0, 600)
    for k, v in last.items():
        m["LAST600_" + k] = v
    m["FIRST600_contacts_per100"] = first["contacts_per100"]
    return m

def run(paths, label):
    per_metric = {}
    rows = []
    for p in paths:
        d = json.load(open(p)); arms = d["arms"]
        m0 = metrics(arms["M0"])
        for j in range(5):
            mj = metrics(arms["NULL%d" % j])
            for k in m0:
                per_metric.setdefault(k, []).append(mj[k] - m0[k])
        rows.append((d["args"]["seed"], m0))
    print("== %s: seeds %s" % (label, [r[0] for r in rows]))
    for s, m0 in rows:
        print("  s%d M0: reward_all %.3f half2 %.3f LAST600 contacts/100 %.2f consum/100 %.2f FIRST600 contacts/100 %.2f"
              % (s, m0["reward_all"], m0["reward_half2"], m0["LAST600_contacts_per100"], m0["LAST600_consum_per100"],
                 m0["FIRST600_contacts_per100"]))
    out = {}
    for k, ds in per_metric.items():
        sd = math.sqrt(sum(x * x for x in ds) / len(ds))
        nz = sum(1 for x in ds if abs(x) > 1e-12)
        out[k] = {"rms_delta": sd, "two_x": 2 * sd, "n": len(ds), "n_nonzero": nz}
        print("  %-28s rms(NULLj-M0)=%.3f  2x=%.3f  n=%d nonzero=%d" % (k, sd, 2 * sd, len(ds), nz))
    return out

res = {"benign_T2_v1": run(V1, "benign (v1, T2, tiebreak ON, 1500 steps)"),
       "trapped_T2_v2": run(V2, "trapped (v2, T2, tiebreak ON, 1500 steps)")}
# per-seed benign excluding the zero-harm floor seeds (s61-63), where all nulls may equal M0
res["benign_harmful_only"] = run(V1[3:], "benign seeds with harm (s64, s65)")
scr = json.load(open(B + "/nulldet2/results/SCREEN_log.json"))
tr = [s for s in scr["seeds"] if s["stratum"] == "hazard_trapped"]; bn = [s for s in scr["seeds"] if s["stratum"] == "benign"]
def msd(v):
    mu = sum(v) / len(v); return mu, math.sqrt(sum((x - mu) ** 2 for x in v) / max(1, len(v) - 1))
print("== SCREEN (v2 rule = A1 rule: >=10 early terms <200 steps in first 600): %d screened, %d trapped (rate %.2f)"
      % (len(scr["seeds"]), len(tr), len(tr) / len(scr["seeds"])))
for lab, g in (("trapped", tr), ("benign", bn)):
    if g:
        mu, sd = msd([s["M0_first600_reward_per_100"] for s in g])
        print("  %s M0 first600 reward/100 mean %.3f between-seed SD %.3f (n=%d); early terms %s"
              % (lab, mu, sd, len(g), sorted(s["early_terminations_600"] for s in g)))
res["screen"] = {"n": len(scr["seeds"]), "n_trapped": len(tr), "wall_s": [s["wall_s"] for s in scr["seeds"]]}
json.dump(res, open(os.path.dirname(os.path.abspath(__file__)) + "/floor_grounding.json", "w"), indent=1)
