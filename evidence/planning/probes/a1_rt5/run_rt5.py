"""bt0925-rt5 driver (pre-registered; see a1_rt5_native_reseed_probe_20260925.md sec 2).
Screens env seeds 2001..2040 IN ORDER; one child process per seed under the Mac CPU lock
(with_lock.sh). Admission by screen order only: the first QUOTA benign and first QUOTA
hazard_trapped seeds (stratum from NATIVE, A1 rule) get NATIVE to 3000 + NATIVE-R1..R3; a seed
whose stratum quota is already full is screen-only (NATIVE stops after closed-loop step 599).
Stops when both quotas are full, at the seed ceiling, or when cumulative child compute wall
reaches BUDGET_S (checked before starting each new seed). ASCII-only output."""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST, LAST = 2001, 2040
QUOTA = 3
BUDGET_S = 85 * 60


def main():
    log = {"seeds": [], "admitted": {"benign": [], "hazard_trapped": []}, "stop_reason": None}
    out = HERE / "results" / "RT5_log.json"
    cum = 0.0
    for s in range(FIRST, LAST + 1):
        need = [st for st in ("benign", "hazard_trapped") if len(log["admitted"][st]) < QUOTA]
        if not need:
            log["stop_reason"] = "both quotas full"
            break
        if cum >= BUDGET_S:
            log["stop_reason"] = "compute budget %d s reached before seed %d" % (BUDGET_S, s)
            break
        jp = HERE / "results" / ("RT5_s%d.json" % s)
        with open(HERE / "logs" / ("rt5_s%d.log" % s), "w") as lf:
            rc = subprocess.call([str(HERE / "with_lock.sh"), "/opt/local/bin/python3", "-u",
                                  str(HERE / "rt5_native_reseed_probe.py"), "--env-seed", str(s),
                                  "--need", ",".join(need), "--out", str(jp)],
                                 stdout=lf, stderr=subprocess.STDOUT, cwd=str(HERE))
        row = {"seed": s, "rc": rc, "need": need}
        if rc == 0 and jp.exists():
            d = json.load(open(jp))
            row.update({"stratum": d["stratum"], "admitted": d["admitted"],
                        "early600": d["arms"]["NATIVE"]["early_terminations_600"], "t_s": d["t_total_s"]})
            cum += d["t_total_s"]
            if d["admitted"]:
                log["admitted"][d["stratum"]].append(s)
        else:
            row["stratum"] = "crashed"
        log["seeds"].append(row)
        log["cum_compute_s"] = round(cum, 1)
        json.dump(log, open(out, "w"), indent=1)
        print("RT5 seed=%d rc=%d stratum=%s admitted=%s early600=%s t=%s cum=%.0fs admitted=%s" % (
            s, rc, row.get("stratum"), row.get("admitted"), row.get("early600"), row.get("t_s"), cum,
            log["admitted"]), flush=True)
    else:
        log["stop_reason"] = "seed ceiling %d reached" % LAST
    log["cum_compute_s"] = round(cum, 1)
    json.dump(log, open(out, "w"), indent=1)
    print("RT5_DONE stop=%s admitted=%s screened=%d cum=%.0fs" % (log["stop_reason"], log["admitted"],
                                                                 len(log["seeds"]), cum), flush=True)


if __name__ == "__main__":
    main()
