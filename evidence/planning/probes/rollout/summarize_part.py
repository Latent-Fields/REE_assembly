"""Tabulate partitioned_repair_probe.py results (ASCII only)."""
import glob, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = {}
for f in sorted(glob.glob(os.path.join(HERE, "results", "PART_s*.json"))):
    d = json.load(open(f)); s = os.path.basename(f)[6:-5]
    print("=" * 100)
    print("seed %s replay=%s depth_limit=%s" % (s, d["replay_class_counts"], d["depth_limit"]))
    for k, v in d["choice_quality"].items():
        print("  CHOICE %s n_inf=%d/%d pick_is_Qbest=%.2f chance=%.2f picks=%s" % (k, v["n_informative"], v["n_states"], v["pick_is_Qbest"] or -1, v["chance"] or -1, v["pick_counts"]))
    for arm, r in d["arms"].items():
        rows.setdefault(arm, []).append(r)
        print("  %-9s rew/100=%+.3f harm_ev=%.1f harm_sum=%+.3f ben_ev=%.2f ben_sum=%+.3f | H=%.2f maj=%.2f acts=%s | P3 maj=%.2f modal=%.2f ncls=%.2f" % (
            arm, r["reward_per_100"], r["harm_events_per_100"], r["harm_sum_per_100"], r["benefit_events_per_100"], r["benefit_sum_per_100"],
            r["action_entropy"], r["majority_share"], r["action_counts"], r["P3_maj_share"], r["P3_modal_frac"], r["P3_n_classes"]))
print("=" * 100)
print("MEANS over seeds")
for arm, rs in rows.items():
    m = lambda k: sum(r[k] for r in rs) / len(rs)
    print("  %-9s n=%d rew/100=%+.3f harm_sum=%+.3f ben_sum=%+.3f ben_ev=%.2f H=%.2f" % (arm, len(rs), m("reward_per_100"), m("harm_sum_per_100"), m("benefit_sum_per_100"), m("benefit_events_per_100"), m("action_entropy")))
