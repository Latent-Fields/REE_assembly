import json, sys
for s in sys.argv[1:]:
    try:
        d = json.load(open("results/COMM_s%s.json" % s)); tb = json.load(open("results/TB_s%s.json" % s))
    except FileNotFoundError:
        continue
    print("seed %s | benefit pos train %d gate native %s | preamble==TB: %s" % (s, d["evaluators"]["trained"]["n_benefit_pos_train"], d["native_gate_open"],
          d["evaluators"]["trained"]["benefit"]["heldout_auc"] == tb["evaluators"]["trained"]["benefit"]["heldout_auc"]))
    for k, a in d["arms"].items():
        o = d["choice_quality"][k]; c = a["choice_quality_comm"]
        ro = o["terms"]["xcand_std_mean"]; rc = c["terms"]["xcand_std_normalised_mean"]; sc = c["terms"]["scales_used"]
        cs = a["comm_state"]
        print("  %-13s rew %6.2f | harm contacts %d haz-prox %d | consume %d ben-approach %d | ep %d ent %.2f | cq off %.2f on %.2f | comm n=%d engaged=%s" % (
            k, a["reward_per_100"], a["harm_contacts"], a["hazard_approach"], a["benefit_contacts"], a["benefit_approach"],
            a["episodes_ended"], a["action_entropy"], o["pick_is_Qbest"], c["pick_is_Qbest"], cs["n"], cs["last"].get("engaged")))
        print("      spread OFF F %.4f H %.4f R %.4f B %.4f | spread ON(normalised) F %.3f H %.3f R %.3f B %.3f | running scales F %.2e H %.2e R %.2e B %.2e | drop-eval flip off %.2f on %.2f" % (
            ro["F"], ro["harm"], ro["residue"], ro["benefit"], rc["F"], rc["harm"], rc["residue"], rc["benefit"],
            sc["F"], sc["harm"], sc["residue"], sc["benefit"], o["terms"]["drop_eval_flip_rate"], c["terms"]["drop_eval_flip_rate"]))
    for k in ("E1_FULL", "E2_FULL_EVAL", "E4_FULL_SHUF"):
        a = tb["arms"][k]
        print("   TB(no flag) %-13s rew %6.2f harm contacts %d haz-prox %d consume %d ben-approach %d" % (k, a["reward_per_100"], a["harm_contacts"], a["hazard_approach"], a["benefit_contacts"], a["benefit_approach"]))
