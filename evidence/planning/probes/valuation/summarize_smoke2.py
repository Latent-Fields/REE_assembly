"""Summarise SMOKE2_s*.json: detector v2 calls (pre-registered 13621d6db8), v1 info, theta trajectories. ASCII-only."""
import json
import sys
import numpy as np
EXPECT = {"M0": False, "M1RAW": True, "M4": False}
tot = {"correct": 0, "fp": 0, "fn": 0, "n": 0}
for s in [int(x) for x in sys.argv[1:]] or [45, 46]:
    try:
        d = json.load(open("results/SMOKE2_s%d.json" % s))
    except FileNotFoundError:
        print("missing", s); continue
    print("=== seed %d gate_n=%d" % (s, d["gate_n"]))
    for k, a in d["arms"].items():
        det = a["detector"]; th = np.array([t["theta"] for t in a["ticks"]]); n = len(th)
        call = ""
        if k in EXPECT:
            ok = det["FIRES"] == EXPECT[k]; tot["n"] += 1; tot["correct"] += ok
            tot["fp"] += (det["FIRES"] and not EXPECT[k]); tot["fn"] += (EXPECT[k] and not det["FIRES"])
            call = "expect=%s -> %s" % ("FIRE" if EXPECT[k] else "silent", "CORRECT" if ok else "WRONG")
        print(" %-5s v2 FIRES=%s %s | ever_floor=%s final=%.3f min=%.3f fracneg=%.2f nnz=%d | v1(info)=%s" % (
            k, det["FIRES"], call, det["ever_at_floor"], det["final_theta_harm"], det["min_theta_harm"],
            det["frac_nonzero_harm_updates_negative"], det["n_nonzero_harm_updates"], a["detector_v1_info"]["FIRES"]))
        print("       all1500=%s half1/2 harm contacts=%d/%d" % (json.dumps(a["all"]), a["half1"]["harm_contacts"], a["half2"]["harm_contacts"]))
        if n:
            q = [0, n // 4, n // 2, 3 * n // 4, n - 1]
            print("       theta F/harm/res/ben @steps " + "; ".join("%d:%s" % (a["ticks"][i]["step"], np.round(th[i], 3).tolist()) for i in q))
        if k == "M4":
            print("       m4_sd", np.round(a["m4_sd"], 4).tolist())
print("TOTAL detector calls: %d/%d correct, FP=%d FN=%d" % (tot["correct"], tot["n"], tot["fp"], tot["fn"]))
