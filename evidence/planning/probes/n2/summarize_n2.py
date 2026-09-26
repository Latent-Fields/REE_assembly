"""Summarise probe N2 results against the pre-registered decision rule (ASCII output)."""
import json, sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else "results")
SEEDS = [611, 612, 613, 614, 615]
ARMS = ["frozen", "reencode", "stored"]


def load(arm, twin, s):
    p = R / ("N2_%s_%s_s%d.json" % (arm, twin, s))
    return json.load(open(p)) if p.exists() else None


print("| seed | stratum | arm | pre disc4/k | **post disc4/k (current)** | disc5 | retention | SHUF post disc4/k | "
      "(e) t30/t0, late max | S1 std disc4/k | S2 ref-space disc4/k | norm x | PR ref->cur | woe drift | "
      "stale ret/onp | guard |")
print("|" + "---|" * 16)
summ = {}
for arm in ARMS:
    A = {"a": 0, "b": 0, "c_twin_a": 0, "d": 0, "e": 0, "n": 0, "a_std": 0, "a_ref": 0}
    for s in SEEDS:
        r, t = load(arm, "real", s), load(arm, "shuf", s)
        if r is None:
            continue
        A["n"] += 1
        A["a"] += r["gate_a"]
        A["b"] += (r["retention"] is not None and r["retention"] >= 0.5)
        A["d"] += all(v == "PASS" for k, v in r["guard"].items() if k == "e2_world") and \
            (t is None or all(v == "PASS" for k, v in t["guard"].items() if k == "e2_world"))
        A["e"] += r["rollout_current"]["gate_e"]
        A["a_std"] += r["gate_a_std_secondary"]
        A["a_ref"] += r["gate_a_refspace_secondary"]
        if t is not None:
            A["c_twin_a"] += t["gate_a"]
        pc, ps = r["post_current"], r["post_current_std"]
        rf = r["post_refspace"]
        st = r.get("staleness", {})
        print("| %d | %s | %s | %.3f / %d | **%.3f / %d** | %.3f | %s | %s | %.2f, %.3f | %.3f / %d | %.3f / %d | %.2f | %.2f->%.2f | %.3f | %s / %s | %s |" % (
            s, r["hazard_class"], arm, r["pre"]["disc4_h1"], r["pre"]["k"], pc["disc4_h1"], pc["k"], pc["disc5_h1"],
            "%.2f" % r["retention"] if r["retention"] is not None else "n/a",
            ("%.3f / %d" % (t["post_current"]["disc4_h1"], t["post_current"]["k"])) if t else "missing",
            r["rollout_current"]["t30_over_t0_median"], r["rollout_current"]["late_growth_max"],
            ps["disc4_h1"], ps["k"], rf["disc4_h1"], rf["k"], r["norm_ratio_current_over_ref"],
            r["latent_ref"]["pr"], r["latent_current"]["pr"], r["world_obs_encoder_rel_change"],
            "%.2f" % st["retained"]["rel_diff_median"] if "retained" in st else "-",
            "%.2f" % st["on_policy"]["rel_diff_median"] if "on_policy" in st else "-",
            ",".join("%s:%s" % kv for kv in sorted(r["guard"].items()))))
    keeps = A["n"] == 5 and A["a"] >= 4 and A["b"] >= 4 and A["c_twin_a"] <= 1 and A["d"] == 5 and A["e"] >= 4
    A["keeps_bar"] = keeps
    summ[arm] = A
print()
for arm in ARMS:
    A = summ[arm]
    print("%s: n=%d (a)=%d/5 (b)=%d/5 twin-meets-(a)=%d/5 (d)=%d/5 (e)=%d/5 | S1 std (a)=%d/5 S2 ref (a)=%d/5 -> keeps bar: %s" % (
        arm, A["n"], A["a"], A["b"], A["c_twin_a"], A["d"], A["e"], A["a_std"], A["a_ref"], A["keeps_bar"]))
ctrl_miss = summ["frozen"]["n"] - summ["frozen"]["a"]
if ctrl_miss >= 2:          # rule 1 is decidable from the control arm alone
    v = "CANNOT_DETERMINE"
elif summ["frozen"]["n"] < 5 or summ["reencode"]["n"] < 5 or summ["stored"]["n"] < 5:
    v = "INCOMPLETE"
elif summ["reencode"]["keeps_bar"]:
    v = "HOLDS-BOTH" if summ["stored"]["keeps_bar"] else "HOLDS-REENCODE"
elif summ["stored"]["keeps_bar"]:
    v = "HOLDS-STORED-ONLY"
else:
    v = "NEITHER"
print("VERDICT:", v)
