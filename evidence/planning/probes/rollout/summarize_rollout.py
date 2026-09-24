"""Tabulate rollout_fidelity_probe.py results (ASCII only)."""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(HERE, "results", "*.json")))
for f in files:
    name = os.path.basename(f)[:-5]
    if name == "smoke":
        continue
    d = json.load(open(f))
    w = d["warm"]
    print("=" * 100)
    print("%s  world_dim=%s clamp=%s wt_delta=%.4f wf_loss_last50=%s selects=%s harm=%s t=%ss" % (
        name, d["world_dim"], d["clamp"], w.get("wt_delta", -1), w.get("wf_loss_last50", w.get("warm", {}).get("wf_loss_late_mean")),
        d["n_selects"], d["harm_ticks_wake"], d["t_total_s"]))
    m1 = d["M1_by_step"]
    ks = [k for k in ("0", "1", "2", "3", "5", "10", "20", "30") if k in m1]
    print("  M1 cand znorm p50: " + " ".join("t%s=%.3g" % (k, m1[k]["norm_p50"]) for k in ks)
          + "  late growth/step=%s" % (None if d["M1_growth_per_step_late"] is None else "%.3f" % d["M1_growth_per_step_late"]))
    print("  M1 rel pairwise spread: " + " ".join("t%s=%.3g" % (k, m1[k]["rel_pairwise_spread_p50"] or 0) for k in ks))
    for lab, m2 in (("M2", d["M2"]), ("M2R(random policy)", d.get("M2R_random_policy"))):
      if m2:
        print("  --", lab)
        print("  M2 n=%d k_pers=%d k_chance=%d visited_norm=%.3f" % (m2["n_starts"], m2["k_beats_persistence"],
                                                                     m2["k_beats_chance"], m2["visited_norm_p50"]))
        for h in ("1", "2", "3", "5", "10", "20", "30"):
            r = m2["by_h"].get(h)
            if r:
                print("    h=%-2s err/pers=%.3g err/chance=%.3g frac_beats_pers=%.2f cos=%s pred_norm=%.3g act_norm=%.3g" % (
                    h, r["err_over_pers"] or -1, r["err_over_chance"] or -1, r["frac_beats_pers"],
                    "%.2f" % r["cos_delta_p50"] if r["cos_delta_p50"] is not None else "na",
                    r["pred_norm_p50"], r["actual_norm_p50"]))
        if m2.get("action_discrimination"):
            print("    M2b action discrimination (executed first action closest to actual):",
                  {h: (v["n"], round(v["executed_is_closest"], 3), v["chance"], round(v["mean_rank"], 2)) for h, v in m2["action_discrimination"].items()})
        if m2.get("actual_delta_action_eta2"):
            print("    M2c actual dz by executed action:", m2["actual_delta_action_eta2"])
    m3 = d["M3"]
    print("  M3 n=%s J_std=%s native_sel==Jargmin=%s comp_std=%s" % (
        m3["n_selects"], m3["J_spread_std_p50"], m3["native_selected_eq_Jargmin"],
        {k: (None if v is None else float("%.3g" % v)) for k, v in m3["component_spread_std_p50"].items()}))
    for dd, r in m3["by_depth"].items():
        print("    d=%-2s trunc_same=%s shuf_same=%s trunc_rho=%s shuf_rho=%s deep_var_share=%s" % (
            dd, *["%.2f" % x if x is not None else "na" for x in (r["trunc_argmin_same"], r["shuf_argmin_same"],
                                                                 r["trunc_spearman"], r["shuf_spearman"], r["deep_var_share_p50"])]))
    m4 = d["M4"]
    if m4:
        for arm, v in m4.items():
            if "maj_share_mean" in v:
                print("  M4 %-14s maj_share=%.3f n_cls=%.2f H=%.3f modal_majority_frac=%.2f maj_counts=%s" % (
                    arm, v["maj_share_mean"], v["n_classes_mean"], v["entropy_mean"],
                    v["frac_states_with_modal_majority"], v["majority_class_counts_across_states"]))
        print("  M4 terrain_prior:", m4.get("terrain_prior_mean_first_action"))
