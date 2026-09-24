"""Tabulate residue_reach_probe outputs across cells (ASCII only)."""
import glob
import json
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "results"
ARMS = ["NONE", "OFF_10", "ON_10", "SCR_10", "SCRL_10", "ALT_10",
        "OFF_300", "ON_300", "SCR_300", "SCRL_300", "ALT_300", "RBF_ONLY"]

for f in sorted(glob.glob(str(OUT / "w*_s*.json"))):
    d = json.load(open(f))
    print("=" * 100)
    print("%s  seed=%s harm_bw=%s eff_bw=%.3f warm=%s harm_hist=%d W1harm=%d W2harm=%d wall=%.0fs" % (
        Path(f).name, d["seed"], d["harm_bw"], d["effective_bw"], d["warm"].get("warm_steps"),
        d["harm_history"], d["harm_ticks_w1"], d["harm_ticks_w2"], d["wall_s"]))
    if d["warm"].get("warm_steps"):
        print("  warm loss first50=%.5f last50=%.5f" % (d["warm"]["loss_first50"], d["warm"]["loss_last50"]))
    q2 = d["q2"]
    for c in ("_get_terrain_action_object_mean", "compute_residue_cost", "_score_trajectory"):
        if c in q2:
            h = q2[c]["to_harm_pool_bw"]
            print("  Q2 %-32s n=%7d dist-to-harm-pool (bw) p5=%.3f p50=%.3f p95=%.3f max=%.3f" % (
                c, q2[c]["n"], h["p5"], h["p50"], h["p95"], h["p100"]))
    print("  Q2 E3 frac <=0.5bw=%.3f  in ON shell [0.75,1.25]bw=%.3f  <=1.25bw=%.3f" % (
        q2.get("_e3_frac_le_0p5bw", -1), q2.get("_e3_frac_0p75_to_1p25bw", -1), q2.get("_e3_frac_le_1p25bw", -1)))
    print("  Q2 manifold pairwise (bw) p50=%.3f p95=%.3f ; harm pool pairwise p50=%.3f max=%.3f ; shells OFF p50=%.2f ON p50=%.2f" % (
        q2["_manifold_pairwise_bw"]["p50"], q2["_manifold_pairwise_bw"]["p95"],
        q2["_harm_pool_pairwise_bw"]["p50"], q2["_harm_pool_pairwise_bw"]["p100"],
        q2["_sample_shell_OFF_bw"]["p50"], q2["_sample_shell_ON_bw"]["p50"]))
    nc = d["native_cycle"]
    print("  NATIVE cycle fired=%s trains=%s steps=%s loss %.4g -> %.4g" % (
        nc.get("mech018_residue_integration_fired"), nc.get("mech018_residue_trains"),
        nc.get("mech018_residue_steps"), nc.get("mech018_residue_integration_loss_first", -1),
        nc.get("mech018_residue_integration_loss_last", -1)))
    e3 = d["e3_cf"]
    cem = d["cem_cf"]
    v = d["values_w2"].get("compute_residue_cost", {})
    vt = d["values_w2"].get("_get_terrain_action_object_mean", {})
    print("  E3 usable=%d committed_frac=%.2f total score spread p50=%.3f ; rbf@E3q mean=%.3f std=%.3f ; rbf@current mean=%.3f std=%.4f" % (
        e3["usable_selects"], e3["committed_frac"], e3["score_spread_total"]["p50"],
        v.get("rbf_mean", float("nan")), v.get("rbf_std", float("nan")),
        vt.get("rbf_mean", float("nan")), vt.get("rbf_std", float("nan"))))
    print("  CEM iterations=%d elite %d/%d" % (cem["cem_iterations"], cem["num_elite"], cem["num_candidates"]))
    print("  %-9s %9s %9s %8s | %6s %9s %9s | %8s %8s %10s" % (
        "arm", "0.1nn@E3", "corr_rbf", "0.1nn@cur", "E3flip", "rhoPhiSpr", "selCore", "CEMjacc", "CEMchg", "eliteCore"))
    for a in ARMS:
        print("  %-9s %9.4f %9.3f %8.4f | %6d %9.4f %9.5f | %8.3f %8.3f %10.5f" % (
            a,
            v.get("%s_neural01_mean" % a, 0.0), v.get("%s_corr_rbf" % a, float("nan")),
            vt.get("%s_neural01_mean" % a, 0.0),
            e3["argmin_flips_vs_OFF_10"].get(a, -1),
            (e3["rho_phi_spread"].get(a) or {}).get("p50", float("nan")),
            e3["selected_minus_pool_rbf_core_phi_mean"].get(a) or 0.0,
            cem["mean_elite_jaccard_vs_OFF_10"].get(a) or 0.0,
            cem["frac_iter_elite_changed_vs_OFF_10"].get(a) or 0.0,
            cem["elite_minus_pool_rbf_core_terrain_mean"].get(a) or 0.0))
