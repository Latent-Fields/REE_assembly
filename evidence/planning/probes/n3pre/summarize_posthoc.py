"""Summarize the POST-HOC diagnostic (bt0925-n3pre). ASCII only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEEDS = [521, 522, 523, 524, 525]
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FIDW", "FULL"]


def main():
    lines = []
    P = lines.append
    for s in SEEDS:
        a = json.load(open(HERE / "results" / ("N3_s%d.json" % s)))
        b = json.load(open(HERE / "results" / ("N3PH_s%d.json" % s)))
        same = True
        for h in ("REAL", "SHUF"):
            for ag in AGGS:
                for k, v in a["metrics"][h][ag].items():
                    if b["metrics"][h][ag].get(k) != v:
                        same = False
        jabs = b["metrics"]["REAL"]["FULL"]["POSTHOC_J_abs_max"]
        P("s%d reproduces_preregistered_metrics=%s batch_canary=%.3g |J|max=%.3g rel=%.2g oracle_in_Qbest=%.2f (chance ~0.20)" % (
            s, same, b["batch_canary_max"], jabs, b["batch_canary_max"] / jabs if jabs else -1,
            b["metrics"]["REAL"]["FULL"]["POSTHOC_oracle_in_Qbest"]))
        for ag in AGGS:
            r, sh = b["metrics"]["REAL"][ag], b["metrics"]["SHUF"][ag]
            P("   %-8s flip_scaf %.2f/%.2f d=%+.2f | flip_native_cls %.2f/%.2f d=%+.2f" % (
                ag, r["POSTHOC_flip_scaf"], sh["POSTHOC_flip_scaf"], r["POSTHOC_flip_scaf"] - sh["POSTHOC_flip_scaf"],
                r["POSTHOC_flip_native_cls"], sh["POSTHOC_flip_native_cls"], r["POSTHOC_flip_native_cls"] - sh["POSTHOC_flip_native_cls"]))
    for ag in AGGS:
        n1 = n2 = 0
        for s in SEEDS:
            b = json.load(open(HERE / "results" / ("N3PH_s%d.json" % s)))
            r, sh = b["metrics"]["REAL"][ag], b["metrics"]["SHUF"][ag]
            n1 += (r["POSTHOC_flip_scaf"] - sh["POSTHOC_flip_scaf"]) > 0.15
            n2 += (r["POSTHOC_flip_native_cls"] - sh["POSTHOC_flip_native_cls"]) > 0.15
        P("%-8s (c)-on-scaffold diff>0.15: %d/5 ; (c)-native-first-class diff>0.15: %d/5" % (ag, n1, n2))
    txt = "\n".join(lines)
    print(txt)
    (HERE / "results" / "POSTHOC_SUMMARY.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
