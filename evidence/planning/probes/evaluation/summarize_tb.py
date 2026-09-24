import json, sys
for s in sys.argv[1:]:
    try:
        d = json.load(open("results/TB_s%s.json" % s))
    except FileNotFoundError:
        continue
    lc = d["label_counts"]; ev = d["evaluators"]["trained"]
    print("seed %s | own-policy: harm %d (contacts %d, haz-prox %d) benefit %d (consume %d, ben-approach %d) | random: benefit %d (consume %d) | benefit pos in train %d, native gate open %s | harm auc %.2f ben auc %.2f" % (
        s, lc["native"]["harm_neg_reward"], lc["native"]["harm_contacts"], lc["native"]["hazard_approach"], lc["native"]["benefit_pos_reward"],
        lc["native"]["benefit_contacts"], lc["native"]["benefit_approach"], lc["random"]["benefit_pos_reward"], lc["random"]["benefit_contacts"],
        ev["n_benefit_pos_train"], d["native_gate_open"], ev["harm"]["heldout_auc"], ev["benefit"]["heldout_auc"]))
    for k, a in d["arms"].items():
        cq = a["choice_quality"]; t = cq["terms"]["xcand_std_mean"]
        n = a["steps"] / 100.0
        print("  %-13s rew %6.2f | harm: contacts %.2f haz-prox %.1f /100 | benefit: consume %.2f ben-approach %.1f /100 | ep %d ent %.2f | cq %.2f | std R %.4f H %.4f B %.4f flip %.2f | gate %s" % (
            k, a["reward_per_100"], a["harm_contacts"] / n, a["hazard_approach"] / n, a["benefit_contacts"] / n, a["benefit_approach"] / n,
            a["episodes_ended"], a["action_entropy"], cq["pick_is_Qbest"], t["residue"], t["harm"], t["benefit"], cq["terms"]["drop_eval_flip_rate"], a["benefit_gate_open"]))
