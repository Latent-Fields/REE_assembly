"""Tabulate balanced_replay_probe.py results (ASCII only)."""
import glob, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(HERE, "results", "BAL*_s*.json"))):
    d = json.load(open(f))
    print("=" * 90)
    print("%s replay n=%d classes=%s probe_states=%d" % (os.path.basename(f), d["replay_n"], d["replay_class_counts"], d["probe_states"]))
    for arm, v in d["arms"].items():
        fi, m1, m2, m3 = v["fidelity"], v["M1_e3"], v["M2_choice"], v.get("M3_closed_loop", {})
        disc = "/".join("%.2f" % fi["action_disc"][h]["executed_closest"] for h in ("1", "3", "5"))
        print(" %-11s ess=%.0f share=%s | k=%s disc(h1/3/5)=%s e/p h1=%.2f cos1=%.2f" % (
            arm, v["train"]["ess"], {k: round(x, 2) for k, x in v["train"]["effective_class_share"].items()},
            fi["k"], disc, fi["err_over_pers_h1"], fi["cos_h1"] or -9))
        print("   M1 trunc_flip d1/3/5=%s shuf_flip=%.2f Jvar>5=%s" % (
            "/".join("%.2f" % m1["trunc_flip_rate"][k] for k in ("1", "3", "5")), m1["shuffle_steps_gt3_flip_rate"],
            None if m1["J_var_share_steps_gt5_p50"] is None else "%.2f" % m1["J_var_share_steps_gt5_p50"]))
        print("   M2 n=%d pick=true_best FULL=%.2f DEPTH1=%.2f chance=%.2f rho FULL=%s D1=%s picks=%s true_best=%s" % (
            m2["n_states"], m2["pick_is_true_best_FULL"], m2["pick_is_true_best_DEPTH1"], m2["chance"],
            None if m2["spearman_Jpred_Jtrue_FULL"] is None else "%.2f" % m2["spearman_Jpred_Jtrue_FULL"],
            None if m2["spearman_Jpred_Jtrue_DEPTH1"] is None else "%.2f" % m2["spearman_Jpred_Jtrue_DEPTH1"],
            m2["FULL_pick_counts"], m2["true_best_class_counts"]))
        if m3:
            print("   M3 exec=%s H=%.2f maj=%.2f harm=%d | P3 maj_share=%.2f modal_frac=%.2f maj=%s tp=%s" % (
                m3["exec_action_counts"], m3["exec_action_entropy_nats"], m3["exec_majority_share"], m3["harm_ticks"],
                m3["P3_maj_share"], m3["P3_modal_majority_frac"], m3["P3_majority_counts"], m3["terrain_prior_first_action"]))
