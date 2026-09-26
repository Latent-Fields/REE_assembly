"""Summarize n3post results: canary check vs the original N3 (9608f3117a) committed JSON,
partitioned gate (a) tables (all/ge8/lt8) OFF, all-states ON, CANNOT_DETERMINE checks, verdict.
ASCII-only output."""
import json
import sys
from pathlib import Path

RES = Path("/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n3post/results")
ORIG = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes/n3/results")
SEEDS = [531, 532, 533, 534, 535]
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FULL"]
TOL = 1e-6


def load(p):
    return json.load(open(p)) if p.exists() else None


def diff(mr, ms):
    if mr is None or ms is None or mr.get("rho_scaf") is None or ms.get("rho_scaf") is None:
        return None
    return mr["rho_scaf"] - ms["rho_scaf"]


def main():
    print("=== CANARY: OFF all-states vs original N3 (9608f3117a) committed JSON ===")
    canary_ok = True
    canary_rows = []
    for S in SEEDS:
        new = load(RES / ("N3POST_off_s%d.json" % S))
        orig = load(ORIG / ("N3_s%d.json" % S))
        if new is None or orig is None:
            print("s%d: MISSING (new=%s orig=%s)" % (S, new is not None, orig is not None))
            canary_ok = False
            continue
        for ag in AGGS:
            new_r = new["metrics_by_partition"]["all"]["REAL"][ag]["rho_scaf"]
            new_s = new["metrics_by_partition"]["all"]["SHUF"][ag]["rho_scaf"]
            orig_r = orig["metrics"]["REAL"][ag]["rho_scaf"]
            orig_s = orig["metrics"]["SHUF"][ag]["rho_scaf"]
            ok_r = (new_r is None and orig_r is None) or (new_r is not None and orig_r is not None and abs(new_r - orig_r) <= TOL)
            ok_s = (new_s is None and orig_s is None) or (new_s is not None and orig_s is not None and abs(new_s - orig_s) <= TOL)
            if not (ok_r and ok_s):
                canary_ok = False
            canary_rows.append((S, ag, new_r, orig_r, ok_r, new_s, orig_s, ok_s))
            print("s%d %-8s REAL new=%s orig=%s %s | SHUF new=%s orig=%s %s" % (
                S, ag, new_r, orig_r, "OK" if ok_r else "MISMATCH", new_s, orig_s, "OK" if ok_s else "MISMATCH"))
    print("CANARY_OVERALL: %s" % ("PASS" if canary_ok else "FAIL"))
    print()

    print("=== Ticks-since-reset partition sizes ===")
    for arm in ("off", "on"):
        for S in SEEDS:
            d = load(RES / ("N3POST_%s_s%d.json" % (arm, S)))
            if d is None:
                continue
            p = d["probe"]
            print("%s s%d: n=%d n_ge8=%d n_lt8=%d frac_lt8=%.3f" % (arm, S, p["n_states"], p["n_ge8"], p["n_lt8"], p["frac_lt8"] or -1))
    print()

    print("=== CANNOT_DETERMINE preconditions (per arm, from TE4/TEW, not probe states) ===")
    for arm in ("off", "on"):
        bar_pass = 0
        twin_pass = 0
        for S in SEEDS:
            d = load(RES / ("N3POST_%s_s%d.json" % (arm, S)))
            if d is None:
                continue
            bar = d["l2r_bar_real"]; twin = d["twin_at_chance"]
            bar_pass += int(bar); twin_pass += int(twin)
            ce = d["canary_e3_structure"]; cd_ = d["canary_action_discrimination"]
            val = d["probe"]["validation"].get("verdict")
            decomp = d["decomp_canary_full_eq_Lmax_max"]; batch = d["batch_canary_rel_max"]
            print("%s s%d: l2r_bar=%s twin_chance=%s canaries(e3=%s,ad=%s) val=%s decomp=%.3g batch=%.3g" % (
                arm, S, bar, twin, ce, cd_, val, decomp, batch))
        print("%s: l2r_bar %d/5, twin_at_chance %d/5" % (arm, bar_pass, twin_pass))
    print()

    print("=== Gate (a): OFF, per partition, REAL-SHUF diff > 0.15, per aggregation ===")
    for part in ("all", "ge8", "lt8"):
        for ag in AGGS:
            diffs = []
            npass = 0
            nseeds_read = 0
            for S in SEEDS:
                d = load(RES / ("N3POST_off_s%d.json" % S))
                if d is None:
                    continue
                mp = d["metrics_by_partition"].get(part)
                if mp is None:
                    diffs.append(None)
                    continue
                mr, ms = mp["REAL"][ag], mp["SHUF"][ag]
                n_inf = mr.get("rho_scaf_n", 0)
                dd = diff(mr, ms)
                diffs.append(dd)
                if dd is not None:
                    nseeds_read += 1
                    if dd > 0.15 and n_inf >= 10:
                        npass += 1
            print("OFF %-4s %-8s diffs=%s pass=%d/%d(read)" % (part, ag, diffs, npass, nseeds_read))
    print()

    print("=== Gate (a): ON, all-states only, REAL-SHUF diff > 0.15, per aggregation ===")
    for ag in AGGS:
        diffs = []
        npass = 0
        for S in SEEDS:
            d = load(RES / ("N3POST_on_s%d.json" % S))
            if d is None:
                continue
            mp = d["metrics_by_partition"]["all"]
            mr, ms = mp["REAL"][ag], mp["SHUF"][ag]
            n_inf = mr.get("rho_scaf_n", 0)
            dd = diff(mr, ms)
            diffs.append(dd)
            if dd is not None and dd > 0.15 and n_inf >= 10:
                npass += 1
        print("ON  all  %-8s diffs=%s pass=%d/5" % (ag, diffs, npass))


if __name__ == "__main__":
    main()
