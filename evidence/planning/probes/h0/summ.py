import json, sys
for line in open(sys.argv[1]):
    d = json.loads(line)
    m, c, f = d["mode"], d["commit"], d["freeze_scored"]
    print("%-14s s%-3d eps=%-3d forced=%-3d eplen=%-6s harm=%.4f ben=%.4f | MODE occ=%.3f exit=%d viaReset=%d endoEnv=%d endoAny=%d nativeSw=%d | COMMIT occ=%.3f exit=%d | FREEZE occ=%.3f exit=%d viaReset=%d endoAny=%d | p1 d'=%s | skip=%d wall=%s" % (
        d["arm"], d["seed"], d["n_episodes"], d["n_forced_resets"], d["ep_len_mean"], d["harm_per_tick"], d["benefit_per_tick"],
        m["occupancy"], m["n_exit"], m["n_exit_via_reset_call"], m["n_exit_endogenous_env"], m["n_exit_endogenous_any"], d["mode_switches_native_total"],
        c["occupancy"], c["n_exit"], f["occupancy"], f["n_exit"], f["n_exit_via_reset_call"], f["n_exit_endogenous_any"],
        d["p1_zharma"].get("dprime"), sum(d["restore_skipped"].values()), d["wall_s"]))
