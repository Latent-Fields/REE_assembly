import json, sys
for fn in sys.argv[1:]:
    d=json.load(open(fn)); s=d["summary"]
    print("#####", fn, {k:s[k] for k in ["n_rows","n_e3_tick_rows","determinism_action_same","determinism_score_rel"]})
    print("  bank", [(b["seed"],b["stream"],b["rel_spread"]) for b in s["bank_spread"]])
    f=lambda x: x if not isinstance(x,dict) else x["mean"]
    for k,v in s.items():
        if "." in k:
            print("  %-16s act_e3=%s score=%s e1=%s cw=%s cs=%s"%(k,v["act_changed_e3tick"],f(v["score_rel"]),f(v["e1_rel"]),f(v["cand_world_rel"]),f(v["cand_self_rel"])))
