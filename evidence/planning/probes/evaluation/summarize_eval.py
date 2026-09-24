import json, sys
for s in sys.argv[1:]:
    d = json.load(open("results/EVAL_s%s.json" % s))
    lc = d["label_counts"]; ev = d["evaluators"]["trained"]; nb = d.get("native_b", {})
    print("seed %s labels native harm/ben %d/%d random %d/%d | harm auc %.2f ben auc %s (n+ test %d, train %d) | natb corr %s auc %s gate %s" % (
        s, lc["native"]["harm_neg_reward"], lc["native"]["benefit_pos_reward"], lc["random"]["harm_neg_reward"], lc["random"]["benefit_pos_reward"],
        ev["harm"]["heldout_auc"], None if ev["benefit"]["heldout_auc"] is None else round(ev["benefit"]["heldout_auc"], 2), ev["benefit"]["heldout_npos"], ev["n_benefit_pos_train"],
        None if not nb else round(nb["trained"]["heldout_corr_exposure"] or 0, 3), None if not nb else round(nb["trained"]["heldout_auc_benefit_contact"] or 0, 2), None if not nb else nb["gate"]))
    for k, a in d["arms"].items():
        cq = a["choice_quality"]; t = cq.get("terms", {}).get("xcand_std_mean", {})
        print("  %-15s rew %6.2f harm %5.1f (c %3d) ben %4.2f (c %d) ep %2d ent %.2f maj %.2f | cq %.2f | std F %.4f H %.4f R %.4f B %.4f | flip %s" % (
            k, a["reward_per_100"], a["harm_events_per_100"], a["harm_contacts"], a["benefit_events_per_100"], a["benefit_contacts"], a["episodes_ended"],
            a["action_entropy"], a["majority_share"], cq["pick_is_Qbest"], t.get("F", -1), t.get("harm", -1), t.get("residue", -1), t.get("benefit", -1), cq.get("terms", {}).get("drop_eval_flip_rate")))
