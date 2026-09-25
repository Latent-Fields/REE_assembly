"""POST-HOC diagnostic for N3-pre (bt0925-n3pre). NOT pre-registered; labelled as such in the record.

Re-runs n3pre_probe.main() unchanged (same seed -> the pre-registered metrics must reproduce
bit-for-bit; checked by the summarizer) and adds, per head and aggregation:
  flip_scaf        : pick-flip vs INIT on the SCAFFOLD pool (distinct first actions)
  flip_native_cls  : does the native-pool pick's FIRST-ACTION CLASS change vs INIT
  oracle_in_Qbest  : P(argmin J_true in env-Q-best) -- the ceiling E3's own one-step valuation
                     places on gate (b), independent of head and aggregation
  J_abs_max        : max |J| on the native pool (scale for the float32 batch canary)
ASCII-only output.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import n3pre_probe as N  # noqa: E402

_orig = N.metrics


def metrics(rows_h, rows_init, states):
    out = _orig(rows_h, rows_init, states)
    orc = [int(np.argmin(r["jtrue"])) in set(np.nonzero(st["q"] >= st["q"].max() - 1e-9)[0].tolist())
           for r, st in zip(rows_h, states) if np.ptp(st["q"]) > 1e-9]
    jabs = float(max(np.abs(r["native"]["FULL"]).max() for r in rows_h))
    for ag in N.AGGS:
        fs, fc = [], []
        for r, ri in zip(rows_h, rows_init):
            fs.append(int(np.argmin(r["scaf"][ag])) != int(np.argmin(ri["scaf"][ag])))
            pc = r["pool_first_classes"]
            fc.append(pc[int(np.argmin(r["native"][ag]))] != pc[int(np.argmin(ri["native"][ag]))])
        out[ag]["POSTHOC_flip_scaf"] = float(np.mean(fs))
        out[ag]["POSTHOC_flip_native_cls"] = float(np.mean(fc))
        out[ag]["POSTHOC_oracle_in_Qbest"] = float(np.mean(orc)) if orc else None
        out[ag]["POSTHOC_J_abs_max"] = jabs
    return out


N.metrics = metrics

if __name__ == "__main__":
    N.main()
