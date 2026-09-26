"""Apply the pre-registered H0 verdict rule (record sec 5) to results/main.jsonl. ASCII output."""
import json, sys
path = sys.argv[1]
rows = [json.loads(l) for l in open(path)]
by = {}
for d in rows:
    by[(d["arm"], d["seed"])] = d  # last line wins

def band(a, b, reg):
    oa, ob = a[reg]["occupancy"], b[reg]["occupancy"]
    ea, eb = a[reg]["n_exit"], b[reg]["n_exit"]
    occ_ok = abs(ob - oa) <= 0.10
    ex_ok = abs(eb - ea) <= max(3, 0.5 * ea)
    return occ_ok, ex_ok

seeds = sorted({s for (a, s) in by if a == "A"})
for reg in ("mode", "freeze_scored", "commit"):
    print("== regime:", reg)
    calls = []
    for s in seeds:
        a, b = by.get(("A", s)), by.get(("B", s))
        if not a or not b:
            print("  seed %d: missing arm" % s); continue
        if reg == "commit":
            ent = a[reg]["n_enter"]
        else:
            ent = a[reg]["n_enter_native"]
        p1 = ent >= 1
        occ_ok, ex_ok = band(a, b, reg)
        ea = a[reg]["n_exit"]; via = a[reg]["n_exit_via_reset_call"]
        frac_reset = via / ea if ea else None
        supported = (b[reg]["occupancy"] > a[reg]["occupancy"] + 0.10 and b[reg]["n_exit"] <= 1
                     and frac_reset is not None and frac_reset >= 0.8)
        falsified = occ_ok and ex_ok
        call = ("CANNOT_DETERMINE(P1)" if not p1 else "SUPPORTED" if supported else
                "FALSIFIED" if falsified else "MIXED")
        calls.append(call)
        print("  seed %d ticks %d: occA=%.3f occB=%.3f (d=%+.3f, in-band=%s) exitsA=%d (at reset %s) exitsB=%d (in-band=%s) "
              "endoA=%d endoB=%d nativeEnterA=%d (<=k after bnd %d) nativeEnterB=%d -> %s" % (
                  s, a["ticks"], a[reg]["occupancy"], b[reg]["occupancy"], b[reg]["occupancy"] - a[reg]["occupancy"],
                  occ_ok, ea, ("%d/%d" % (via, ea)), b[reg]["n_exit"], ex_ok,
                  a[reg]["n_exit_endogenous_env"], b[reg]["n_exit_endogenous_env"], ent,
                  a[reg].get("n_enter_native_le_k_after_boundary", -1), b[reg].get("n_enter_native", b[reg]["n_enter"]), call))
    print("  calls:", calls)
print("== P1 z_harm_a d' (arm A):", {s: by[("A", s)]["p1_zharma"].get("dprime") for s in seeds if ("A", s) in by})
print("== outcomes (harm/tick, benefit/tick, ep_len):")
for s in seeds:
    for arm in ("A", "B", "C"):
        d = by.get((arm, s))
        if d:
            print("  %s s%d ticks=%d harm=%.4f ben=%.4f eplen=%.2f eps=%d forced=%d switches/ep=%.3f switches/life=%d" % (
                arm, s, d["ticks"], d["harm_per_tick"], d["benefit_per_tick"], d["ep_len_mean"], d["n_episodes"],
                d["n_forced_resets"], d["mode_switches_native_per_episode"], d["mode_switches_native_total"]))
for s in seeds:
    c = by.get(("C", s))
    if c:
        m = c["mode"]
        print("== C s%d: forced=%d exits=%d viaReset=%d atForcedNearWorldChange=%d atForcedFar=%d endoAny=%d "
              "nativeEnter=%d (<=k after bnd/forced %d) occ=%.3f" % (
                  s, c["n_forced_resets"], m["n_exit"], m["n_exit_via_reset_call"], m["n_exit_at_forced_near_world_change"],
                  m["n_exit_at_forced_far_from_world_change"], m["n_exit_endogenous_any"], m["n_enter_native"],
                  m["n_enter_native_le_k_after_boundary"], m["occupancy"]))
